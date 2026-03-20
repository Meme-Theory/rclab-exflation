# Cosmic Web -- Collaborative Feedback on Session 36

**Author**: Cosmic Web Theorist
**Date**: 2026-03-08
**Re**: Session 36 Results -- The Lava Inside the Tube

---

## Section 1: Key Findings from My Domain

Session 36 produced 13 gate verdicts across 4 waves. From the cosmic web perspective, the decisive results are:

1. **TAU-STAB-36 (FAIL)**: S_full(tau) monotonically increasing. dS/dtau = +58,673 at the fold. All 10 Peter-Weyl sectors separately monotonic. No minimum exists in the linear spectral action.
2. **TAU-DYN-36 (FAST ROLL)**: The moduli trajectory rushes through the BCS pairing window in ~10^{-3} spectral time units, 38,600x faster than BCS condensation requires.
3. **BBN-LITHIUM-36 (FAIL)**: delta_H/H = -6.6 x 10^{-5}, structurally negligible. The BCS gap is a 10^{-4} perturbation on the UV-dominated spectral sums.
4. **The cascade hypothesis** (framework-bbn-hypothesis.md): tau is dynamically linked to the dominant phonon wavelength at each epoch. Exflation is a staircase of wall collapses, not a smooth roll.

From my domain, the cascade hypothesis is the first element of this framework that makes contact with observable large-scale structure. Everything before it was internal geometry. The cascade is the lava.

---

## Section 2: Cross-Domain Implications

The cascade staircase changes the relationship between the framework and my domain from "single parameter CC -> H(z) -> DESI" to something potentially richer. Three implications:

**A. The staircase expansion history is not LCDM.** LCDM has smooth radiation-dominated, matter-dominated, and Lambda-dominated eras. The cascade produces discrete bursts of expansion at each wall collapse (tau ~ 0.54, 0.34, 0.24, 0.190). This is qualitatively different from both standard inflation (smooth exponential) and LCDM (smooth deceleration-to-acceleration). Whether it is observationally distinguishable depends on the energy released per step and the redshift at which each step occurs.

**B. The spectral action cutoff IS scale separation.** The Connes spectral action Tr f(D^2/Lambda^2) suppresses modes above Lambda. In the cascade picture, Lambda tracks the current phonon scale at each epoch. This means the effective gravitational constants (a_0, a_2, a_4 coefficients) are epoch-dependent -- not through a rolling scalar field, but through a physically motivated cutoff that follows the fragmentation cascade.

**C. BBN is reframed.** The fold-level computation (BBN-LITHIUM-36 FAIL, delta_H/H ~ 10^{-5}) is the wrong computation because during BBN, tau occupies a higher saddle (tau ~ 0.34-0.54), not the fold. The relevant modification to H(T_BBN) comes from the saddle-scale spectral action coefficients. This is UNCOMPUTED.

---

## Section 3: The Lava -- Observable Structure from the Cascade

This is the section the user asked for. What fills the cosmic web if this framework is correct? I will be precise about what the cascade predicts, what it does not predict, and what it cannot predict without further computation.

### 3.1 Cascade Staircase and the Matter Power Spectrum

The cascade produces a staircase expansion history: discrete bursts of expansion at tau = {0.54, 0.34, 0.24, 0.190}. Each burst seeds perturbations at a characteristic comoving scale set by the Hubble radius at that epoch. In standard inflation, the power spectrum is nearly scale-invariant because the inflaton rolls smoothly. In a staircase expansion:

- Each step produces a **step-like feature** in the primordial power spectrum P_prim(k) at the comoving wavenumber k_i = a_i H_i corresponding to that burst.
- The transitions between steps produce **oscillatory features** (ringing) around each k_i.
- The spectral index n_s becomes **scale-dependent**: n_s(k) varies with k rather than being a constant.

The predicted signature in P(k) is NOT a single bump at a preferred scale but a sequence of steps. This is qualitatively similar to "features in the primordial power spectrum" models that have been constrained by Planck CMB data. Planck places an upper bound of roughly 5-10% on step-like features in the primordial power spectrum at k ~ 0.001-0.3 Mpc^{-1} (Planck 2018 X, Table 7). The cascade must either produce steps below this amplitude or place them at k values outside the Planck window.

**Quantitative gap**: The cascade hypothesis specifies which tau values correspond to which steps but does NOT specify the energy scale of each burst, the mapping between tau and cosmic time t, or the mapping between tau and comoving wavenumber k. Without CUTOFF-SA-37 and CASCADE-DYN-37, the comoving scales of the cascade steps are unconstrained. This is a pre-prediction, not a prediction.

### 3.2 Preferred Scales from Wall Collapses

Each wall collapse at a specific tau deposits energy at a characteristic scale. If the saddle structure of S_f(tau) has saddles at tau = {0.54, 0.34, 0.24}, the scale hierarchy between steps is set by the eigenvalue ratios at those tau values. From TAU-STAB-36 (W4-A), the per-level contributions at the fold are:

| Level | S_level | Eigenvalue scale (proxy) |
|:-----:|:-------:|:------------------------:|
| 0     | 14.2    | ~0.84                    |
| 1     | 962     | ~2.5                     |
| 2     | 20,621  | ~7                       |
| 3     | 228,764 | ~20                      |

If each cascade step corresponds to a different KK level "decoupling" through the cutoff, the scale ratios between steps are roughly 3:1 to 3:1, producing preferred scales separated by factors of ~3 in comoving distance. Whether this maps to 30 Mpc, 100 Mpc, 300 Mpc, or 1 Gpc depends entirely on M_KK and the cascade dynamics -- both uncomputed.

**Connection to Einasto's 100-130 Mpc scale** (Paper 06, E06-E4): Einasto identified a quasi-periodic supercluster-void spacing of ~100-130 Mpc. In LCDM, this is the BAO scale -- the sound horizon at recombination. In the cascade framework, the BAO scale is unaffected (the BCS transition at 10^{-41} s is utterly irrelevant to recombination at z ~ 1100). So the 100-130 Mpc scale is explained the same way in both models: it is the sound horizon, period. The cascade does NOT produce this scale.

What the cascade COULD produce is a scale at ~300-400 Mpc (3x the BAO scale), corresponding to the next cascade step. This would appear as a secondary feature in xi(r) or P(k) at a scale 3x the BAO peak. DESI's precision on the correlation function at r ~ 300-400 Mpc/h is currently ~5-10% (Paper 17), which may be sufficient to detect or exclude a ~5% feature. This is a concrete, testable prediction -- IF the cascade dynamics calculation (CASCADE-DYN-37) can pin down the scale ratio.

### 3.3 DESI BAO Signal

The BAO peak position measures the sound horizon r_s at recombination. The cascade does not modify recombination physics (tau ~ 0.54 during BBN implies tau >> 0.54 at recombination, deep in the pre-fragmentation regime). Therefore:

- **BAO peak position**: UNCHANGED. r_s is set by pre-recombination physics, which the cascade does not touch.
- **BAO peak shape**: POTENTIALLY MODIFIED. If the cascade alters the expansion history at z < z_recombination (post-recombination wall collapses), the BAO feature in the correlation function could be broadened or shifted by the modified growth rate. The relevant quantity is the growth factor D(z) integrated through the staircase epochs.
- **BAO as a w(z) probe**: DESI measures w_0 = -1.016 +/- 0.035, w_a = -0.11 +/- 0.35. The cascade predicts w = -1 at late times (the present-day vacuum is the BCS condensate, whose equation of state is that of a cosmological constant). The framework's w(z) prediction at earlier epochs (z > 1, where cascade steps may have occurred) is UNCOMPUTED. If a cascade step occurred at z ~ 0.5-2.0, it would produce a transient deviation in w(z) that DESI could detect.

**Discriminating test**: The cascade predicts w(z) = -1 today but allows transient deviations at specific redshifts (corresponding to wall collapses). LCDM predicts w(z) = -1 at all z. If DESI detects w_a != 0 at > 3-sigma in future data releases, this would be consistent with a cascade step but NOT uniquely predicted by it (quintessence models also predict w_a != 0). The cascade's unique signature would be a DISCRETE step in w(z), not a smooth variation -- but current DESI precision cannot distinguish these.

### 3.4 Void Statistics

Voids are my sharpest tool for testing new physics. In LCDM, void size distributions are fully predicted by the initial power spectrum and the growth factor. The cascade modifies both:

- **Preferred void sizes**: If the cascade introduces preferred scales in P_prim(k), these propagate into preferred void sizes via the excursion-set formalism. A step at k_c produces an excess of voids with radius R_void ~ pi/k_c.
- **Void profiles**: LCDM voids have universal density profiles (Hamaus et al. 2014, Paper 13). If the effective gravitational constant G_eff depends on epoch through the cascade's epoch-dependent spectral action coefficients, void profiles would differ from LCDM at the level of the G_eff modification. From BBN-LITHIUM-36, the fold-level modification is delta_G/G ~ 10^{-4} -- negligible. But saddle-level modifications are UNCOMPUTED.
- **Void dynamics**: The Alcock-Paczynski test via voids (Sutter et al. 2014, Paper 12) directly measures H(z) and D_A(z). A staircase expansion produces kinks in the H(z) curve that voids could detect. Current void-based AP precision is ~5% on H(z) at z ~ 0.5-0.8 (BOSS/DESI). A cascade step at z ~ 0.5 producing delta_H/H ~ 5% would be detectable.

**Critical constraint**: The cascade's internal geometry domain walls exist in the SU(3) fiber, not in position space (Session 29 permanent result). The "walls" of the cosmic web (void walls, filament boundaries) are gravitationally formed structures in position space, not topological defects from the substrate. The cascade does NOT predict that void walls are domain walls. This is a category error that I have flagged since Session 29.

### 3.5 Giant Arc, Hercules-Corona Borealis, Big Ring

These anomalously large structures (1-3 Gpc) challenge the cosmological principle at the 3-4 sigma level (Papers 14, 16). Could cascade modes produce them?

**Analysis**: The cascade staircase operates at energy scales near M_KK ~ 10^{16} GeV. The comoving Hubble radius at that epoch is ~10^{-25} Mpc. This is 28 orders of magnitude below the Gpc scales of the Giant Arc. No cascade step at the KK energy scale seeds perturbations at Gpc scales -- those scales were never inside the Hubble volume during the cascade.

The Giant Arc and HCBGW are at z ~ 0.8-2.0. If a cascade step occurred at z ~ 1-2 (a post-recombination wall collapse), it could seed large-scale correlations. But the cascade hypothesis places the LAST wall collapse at the fold (tau ~ 0.190), which corresponds to the GUT/KK scale, not z ~ 1. There is no cascade step at z ~ 1 in the current picture.

**Verdict**: The cascade does NOT naturally explain the Giant Arc, HCBGW, or Big Ring. These anomalous structures, if real, remain anomalous in both LCDM and the cascade framework. They have low discriminating power between the two.

### 3.6 Bulk Flows and Long-Range Correlations

Watkins et al. (Paper 15) measured bulk flows of 400-600 km/s at 100 Mpc/h, 2-3x larger than LCDM predicts. Could phononic correlations from the cascade persist as coherent large-scale flows?

**Analysis**: Bulk flows arise from the large-scale density dipole. In LCDM, the predicted bulk flow at 100 Mpc/h is ~200-250 km/s. The cascade modifies the initial power spectrum, potentially enhancing large-scale power. But increasing large-scale power to match the bulk flow anomaly would simultaneously increase the amplitude of the CMB quadrupole and octupole beyond Planck constraints.

More importantly, the cascade's phonon correlations are in the INTERNAL SU(3) geometry, not in position space. The framework does not predict spatial long-range order beyond what gravitational instability produces from the initial perturbation spectrum. The cascade modifies the initial spectrum (through staircase features) but does NOT introduce new long-range spatial correlations in the 4D spacetime.

**Verdict**: The cascade does not naturally explain anomalous bulk flows. This remains an LCDM tension with no cascade-specific resolution.

---

## Section 4: Points of Agreement and Disagreement

### Agreements

1. **TAU-STAB-36 is decisive.** The linear spectral action's monotonicity is the session's most important negative result. The mechanism chain is broken at the linear level.
2. **The cutoff escape route is physically motivated.** Connes never uses S = Sum |lambda_k|. The physical spectral action is Tr f(D^2/Lambda^2). This is not a rescue hypothesis -- it is the correct formulation that should have been used from the start.
3. **W6-SPECIES-36 (PASS)** is the session's most significant positive result. The species scale resolution removes a genuine structural concern.
4. **BBN-LITHIUM-36 (FAIL)** is correctly identified as "wrong computation" in the cascade picture. The cascade reframes BBN as a saddle-epoch phenomenon.

### Disagreements

1. **The cascade is a hypothesis, not a result.** The framework-bbn-hypothesis document presents the cascade as if it resolves TAU-STAB and TAU-DYN failures. It does not. It reframes them as "wrong computations" -- but the reframing depends on CUTOFF-SA-37, which is uncomputed. Until S_f(tau) with a physical cutoff is shown to have a minimum, the cascade is a narrative, not a mechanism.
2. **The cascade's observational predictions are empty until CASCADE-DYN-37 is computed.** I identified six potential observational channels above (Sections 3.1-3.6). Every single one requires knowing the mapping between tau and comoving scale, which requires the cascade dynamics computation. Zero predictions can be made today.
3. **Post-hoc danger.** If CUTOFF-SA-37 produces a minimum AND CASCADE-DYN-37 produces specific scales, the temptation will be to compare those scales to known features in P(k) and declare agreement. This would be post-hoc unless the scales are pre-registered BEFORE the comparison. I pre-register the following: if the cascade predicts a feature at comoving scale R_cascade, the discriminating test is whether xi(r) from DESI shows a feature at R_cascade with amplitude > 2% of xi(r_BAO). The amplitude threshold is chosen because DESI can detect 2% features at r ~ 100-400 Mpc/h.

---

## Section 5: Recommendations and Pre-Registered Tests

### Priority Computations

1. **CUTOFF-SA-37** (HIGHEST): Compute S_f(tau) with the physical Connes cutoff. Does a minimum appear near the fold? This is the prerequisite for everything in my domain. Without it, the cascade is speculation.
2. **CASCADE-DYN-37** (HIGH, contingent on CUTOFF-SA-37 PASS): Compute tau(t) through the cascade with scale-dependent cutoff. This determines which saddle tau occupies at which epoch, and maps cascade steps to comoving scales.
3. **P_prim(k) from cascade** (MEDIUM, contingent on CASCADE-DYN-37): Compute the primordial power spectrum from the staircase expansion. This is the first computation that produces an observable testable against Planck + DESI.

### Pre-Registered Observational Gates

| Gate ID | Observable | Prediction | Data | Pass/Fail |
|:--------|:-----------|:-----------|:-----|:----------|
| CASCADE-PK-37 | Feature in P(k) at k_cascade | Amplitude > 2% of P(k_BAO) | DESI DR2 | Feature present / absent |
| CASCADE-W-37 | w(z) at cascade redshift | Discrete step, delta_w > 0.05 | DESI w_0/w_a | Step detected / smooth |
| CASCADE-VOID-37 | Preferred void radius | R_void = pi/k_cascade +/- 20% | BOSS/DESI VIDE | Excess at R_void / no excess |

### What This Domain Cannot Do

My domain CANNOT uniquely confirm the framework. The cosmic web's relationship to the phonon-exflation cascade is:

- **Sentinel role**: Any deviation from LCDM in P(k), xi(r), void statistics, or w(z) that is INCONSISTENT with the cascade prediction falsifies the cascade. This is a valid constraint.
- **Non-uniqueness**: Any feature the cascade produces in P(k) can also be produced by other models (step inflation, features in the inflaton potential, modified gravity). The cascade's unique fingerprint is the SPECIFIC scale ratios between steps, set by the SU(3) eigenvalue spectrum. If these ratios match nothing else in the literature, the prediction has high discriminating power.

The lava is in there. But to see it, we need CUTOFF-SA-37 to open the tube. Until then, this domain watches and waits -- sentinel, not spectator.
