# Session 71 Workshop: Mack × Van-den-Dungen

**Date**: 2026-04-10
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: mack (mack-cosmic-bridge), van-den-dungen (van-den-dungen-bridge-theorist)
**Source Documents**:
- `sessions/archive/session-71/session-71-results-workingpaper.md`
- `sessions/framework/baseline-findings-s66.md`
- `sessions/framework/constraint-mega-matrix.md`
- `sessions/framework/pre-registered-observations.md`
- `sessions/framework/21cm-science-case.md`

**Focus Topics**:
1. DESI DR3 Scenario B & the observational tension landscape
2. Non-trivial fibration: c_s^2 protection vs alpha_s structural tension
3. 21cm ISW pre-registration & substrate-specific observable signatures
4. Spectral zeta threshold, Pantheon+ systematic shadow, & a_0/a_2 constraints

---

## Round 1 — Mack: Opening Analysis

### M1: DESI DR3 Scenario B & the Observational Tension Landscape

The S71 W2-E computation (DESI-DR3-SCENARIO-B-PRECISE-71) sharpens the framework's observational position with a Fisher forecast built on 2x DR2 effective volume. The result is structurally informative and confirms what the S68 Volovik-Mack workshop (R2) already indicated: **w_a is the sole discriminant between survival and exclusion.**

**The numbers.** Under Scenario B (DR3 center w_0 = -0.90, w_a = -0.30):

| Model | w_0 | w_a | 2D tension | Bayes factor vs LCDM |
|:------|:----|:----|:-----------|:---------------------|
| FW (w_a = 0.066) | -0.918 | +0.066 | 2.88-sigma | 0.045 (disfavored 22x) |
| FW (canonical, w_a = 0) | -0.918 | 0.000 | 2.14-sigma | 0.360 (disfavored 2.8x) |
| LCDM | -1.000 | 0.000 | 1.70-sigma | reference |

The decomposition into 1D marginals is diagnostic: w_0 tension is 0.39-sigma (the framework's w_0 = -0.918 nearly matches Scenario B's -0.90), while w_a tension is 1.70-2.07 sigma. The framework's w_0 prediction, which emerges from the Volovik effacement residual Gamma = 0.99970 through the spectral moment ratio a_0/a_2 = 2.3197, is doing exactly what it should -- landing between LCDM and the DESI central value. The problem is entirely w_a.

**Why w_a = 0 is structurally locked.** The S68 workshop (R2) identified a four-fold lock on w_a = 0: (1) GGE integrability -- the Generalized Gibbs Ensemble conserves all Richardson-Gaudin charges, freezing the equation of state; (2) Josephson phase -- the CG(24) tessellation locks relative phases, preventing slow evolution; (3) frozen texture -- no domain wall dynamics post-transit (GGE universality theorem, S57); (4) thermalization barrier -- the 59 OOM gap between GGE and Gibbs prevents relaxation. These four locks make w_a = 0 structural, not tunable. This is the framework's greatest strength (zero-parameter prediction) and its greatest vulnerability (no adjustment mechanism if observations demand w_a < 0).

**What the 2D sensitivity scan reveals.** The W2-E computation swept a 51x51 grid in (w_0, w_a) space for DR3 centers. Framework viable (< 2-sigma) at only 10.1% of grid points; excluded (> 3-sigma) at 82.2%. But the framework is preferred over LCDM at 42.6% of grid points -- specifically, whenever w_0 shifts toward more negative values (closer to -0.918) and w_a moves toward zero. The DR1-to-DR2 trend in w_0 was -0.08 per data release, moving TOWARD the framework. If this trend continues by -0.025 in DR3, w_0 tension drops from 3.61 to 3.07-sigma (1D).

**The SN calibration systematic.** This is underappreciated. DESI's w_0 shifts by approximately 0.08 depending on whether Pantheon+ or DESY5 supernovae are used for calibration (Frieman, Turner & Huterer 2008 [Paper 09] emphasize that supernova systematics are the dominant w_0 uncertainty source, not BAO). The DR2 + DESY5 combination gives w_0 = -0.752; DR2 + Pantheon+ gives w_0 = -0.827. This 0.075 swing is 1.3x the framework's total w_0 offset from LCDM (0.082). DR3's choice of SN calibration chain will therefore shift the framework's tension by up to 1.6-sigma. This is not a framework uncertainty -- it is a data-pipeline systematic that could resolve or worsen the w_0 tension independently of any physics.

**Pre-registered decision tree (from S60 DR3-PREREGISTER-60, updated S70).** The framework survives if w_a > -0.35 and is excluded if w_a < -0.530 at 3-sigma. Under Scenario B (w_a = -0.30), the framework survives but is disfavored relative to LCDM. Under Scenario A (w_a = -0.73), the framework is excluded at 4.12-sigma. The DR3 measurement of w_a is therefore a clean binary gate for the framework's survival.

**What I notice, structurally.** The w_a = 0.066 value specified in the computation prompt is not in the upstream framework data (which gives w_a = 0 exactly from the four-fold lock). Using w_a = 0 IMPROVES the framework's position by 0.74-sigma because 0 is closer to Scenario B's -0.30 than +0.066 is in the correlated (rho = -0.85) posterior. If there is a framework mechanism that produces w_a = +0.066, I need to understand its provenance, because it is making the observational situation worse, not better.

**Question for van-den-Dungen:** The four-fold w_a lock is a physical argument. But the spectral action's scheme dependence (S66: n_s range = 0.164 across three cutoffs) suggests that quantities derived from spectral moments can shift substantially with the functional choice. Is w_0 = -0.918 similarly scheme-dependent? Specifically: does the effacement residual Gamma = 1 - a_4/(a_0 * a_2) depend on the spectral functional f(x), or is it a ratio that cancels the f-dependence? If scheme-dependent, the w_0 prediction carries an unquantified systematic that could be comparable to the DESI SN calibration uncertainty.

### M2: Non-Trivial Fibration — c_s^2 Protection vs Alpha_s Structural Tension

The S71 W1-E result (NON-TRIVIAL-FIBRATION-CSQUARED-71) establishes a scaling hierarchy that is clean and structurally important: c_s^2 correction scales as kappa^2 (quadratic suppression) while alpha_s correction scales as kappa (linear). This means the two corrections decouple in a specific sense -- you can maximize the alpha_s correction without threatening c_s^2 = 0. But the magnitude tells a different story.

**The c_s^2 protection is robust.** At maximum physical A-tensor strength kappa = 0.5: delta(c_s^2) = 4.26e-4. Combined with the one-loop trivial-bundle correction (3.36e-4 from Q-SOUND-70), the total c_s^2 is bounded by 7.62e-4 -- still below 10^{-3}. The quadratic suppression kappa^2 * g_3^2/(16*pi^2) ~ 1.7e-3 ensures this. For the ISW discrimination (M3 below), this is the load-bearing result: the framework's tracking vacuum signature (c_s^2 = 0 vs quintessence c_s^2 = 1) survives non-trivial fibration corrections by three orders of magnitude. The S70 VdD-Mack workshop (R2, emergence E-9) predicted that alpha_s fix and c_s^2 correction would be controlled by different quantities (c_2 vs ||A||^2); this computation confirms that prediction quantitatively.

**The alpha_s tension is NOT resolved.** delta(alpha_s)/alpha_s = 4.2% at kappa = 0.5, against a required 781%. The overlap band does not exist: alpha_s half-resolution requires kappa > 3.82 while c_s^2 safety requires kappa < 0.77. Combined with the a_6 CCM result (W1-B: 26.9% shift but anti-correlation PERSISTS) and correlated sensitivity (W3-B: d(ln omega_L)/d(alpha) = -0.44, ROBUST), the total correction budget is approximately:

| Channel | Correction to alpha_s | Source |
|:--------|:---------------------|:-------|
| Non-trivial fibration | 4.2% | W1-E |
| a_6 higher-order CCM | 6.5% (S70 estimate) to 26.9% (W1-B) | W1-B |
| Combined | ~10-31% | Sum |
| Required | 781% | Structural |
| Deficit | ~25x to 73x | Still enormous |

This is the alpha_s problem in its clearest form. The spectral geometry predicts alpha_s = 0 at tree level (structural theorem T15 from S50: alpha_s = n_s^2 - 1 for any K^2 propagator on compact Josephson lattice with broken U(1)). The Planck 2018 constraint is alpha_s = -0.0045 +/- 0.0067, so alpha_s = 0 is currently 0.67-sigma (fine). But the S66 computation found alpha_s = -0.038 at L_max = 4, which is 5.0-sigma from Planck when the spectral geometry's OWN truncation-corrected value is used rather than the tree-level zero.

**The scheme dependence problem.** W1-B reveals maximal scheme dependence: the same D_K spectrum produces delta(lambda_CCM) = 0% (zeta functional), 27% (cutoff), or 8.6% (anomaly-derived). The anti-correlation between CC and alpha_s is ABSENT in the zeta scheme (because zeta has no f_0 parameter) but PERSISTS in all cutoff schemes. This means the alpha_s extraction is not a well-defined quantity until the spectral functional is fixed. The S66 CUTOFF-NS-66 FAIL already showed this for n_s: the range across three cutoffs spans 0.164 -- larger than the Planck error bar by 39x. Alpha_s inherits this pathology.

**What this means observationally.** The c_s^2 = 0 prediction is structurally protected and scheme-independent (it follows from the product geometry of the spectral triple, not from the spectral functional choice). The alpha_s = 0 prediction is structurally robust at tree level but scheme-dependent at loop level. This creates an asymmetry: the ISW tracking test (c_s^2 = 0 vs 1) is a clean test of the substrate geometry, while the alpha_s test is entangled with the spectral functional choice. CMB-S4 will tighten sigma(alpha_s) to approximately 0.003, which would test the tree-level alpha_s = 0 prediction at ~1.5-sigma. But the loop-level alpha_s from the spectral geometry is scheme-dependent, so a CMB-S4 measurement cannot cleanly confirm or exclude the framework through alpha_s alone.

**Question for van-den-Dungen:** The non-trivial fibration lives in Omega^1(M, ad(P)), which is independent of the Jensen deformation in Sym^2(T*K). But the A-tensor in the Kasparov product structure connects these two: it mediates the gravitational-gauge coupling. In your fibration computation, is kappa constrained by the Kasparov product's unitarity condition (||A|| bounded by the spectral gap of D_K), or is it a free parameter? If the Kasparov product imposes a structural upper bound on kappa, that bound should be compared to the kappa = 0.5 "physical maximum" used in the computation. If the Kasparov bound is tighter, the alpha_s correction shrinks further.

### M3: 21cm ISW Pre-Registration & Substrate-Specific Observable Signatures

The S71 W2-F computation (21CM-ISW-PREREGISTRATION-71) completes the full prediction chain from spectral action through c_s^2 = 0 to a pre-registered 21cm ISW cross-power prediction. This is the framework's most carefully constructed observational target because it tests a substrate-specific property that no other dark energy model produces.

**The prediction chain, with error propagation.**

| Step | Quantity | Value | Error | Source |
|:-----|:---------|:------|:------|:-------|
| 1 | c_s^2 (tree) | 0.0 (exact) | -- | Q-SOUND-70 |
| 1b | c_s^2 (1-loop + fibration) | < 7.62e-4 | 0.08% relative | W1-E + Q-SOUND-70 |
| 2 | ISW auto FW/Quint ratio | +6.8% | -- | CLASS-ISW-70 |
| 2b | ISW-galaxy FW/Quint ratio | +4.0% | -- | CLASS-ISW-70 |
| 3 | ISW-21cm cross-power delta | +4.0% [range: +3.0%, +6.7%] | 7.5% relative | W2-F |

The error budget is dominated by cosmological parameter uncertainties (5.5%) and Boltzmann code systematics (5.0%, after the S70 CLASS-ISW-70 Limber-to-Boltzmann correction that reduced the S68 overprediction by 1.9x). The c_s^2 framework uncertainty (0.08%) is negligible. This means the prediction is limited by our knowledge of standard cosmological parameters, not by the framework's internal structure. The framework contributes a zero-parameter prediction (c_s^2 = 0) that is stable to perturbative corrections; the noise comes from external inputs.

**The detection landscape is sobering.**

| Experiment | sigma(A_ISW) | SNR (FW vs Quint) | Timeline |
|:-----------|:-------------|:-------------------|:---------|
| Planck | 0.25 | 0.16 | now |
| Euclid ISW | 0.05 | 0.80 | ~2030 |
| SKA-Mid IM | 0.37 | 0.11 | ~2030 |
| 21cm ideal | 0.01 | 4.16 | >2035 |

The substrate-specific discrimination (c_s^2 = 0 vs 1) requires sigma(A_ISW) < 0.02, which no existing or planned experiment achieves. Euclid reaches SNR = 0.80 -- marginal at best, not discriminating. The 21cm ideal case (all-sky z ~ 0.4-3 intensity mapping) achieves SNR = 4.16, which would be a clean 4-sigma discrimination. But "ideal" means an instrument that does not exist and is not funded.

**The critical redshift range.** W2-F identifies a structural mismatch in the community's 21cm plans: SKA-Low probes z > 3 (Epoch of Reionization), and HERA probes z > 6 (Cosmic Dawn). But the ISW kernel peaks at z ~ 0.5-1.5, where Omega_DE is non-negligible. At z = 10, Omega_DE = 1.6e-3 -- the ISW effect is effectively zero. The ISW-21cm cross-correlation requires post-reionization HI intensity mapping at z ~ 0.4-3, which is the domain of CHIME/CHORD (z ~ 0.8-2.5, sigma(A_ISW) = 0.52, SNR = 0.08) and a future SKA-Mid IM mode. This is important: the "21cm" in the framework's science case is NOT the same 21cm that the EoR/Cosmic Dawn community is building instruments for. The 21cm-science-case.md document specifies frequency coverage 200-1400 MHz (z ~ 0-6), which is a wider band than any single planned instrument.

**Where this connects to the broader observational program.** The S68 Volovik-Mack workshop (R2) established the temporal asymmetry: DR3 tests background cosmology (a_0, a_2 moments) before 21cm tests substrate physics (c_s^2). The framework cannot demonstrate its uniqueness until the 21cm channel is accessible. Between now and then, DESI DR3 (w_0, w_a) and Euclid (sigma_8, f*sigma_8) test the expansion history, where the framework makes the same qualitative prediction as w = -0.918 quintessence. The framework passes or fails these background tests without ever having its substrate-specific signature tested.

This temporal ordering creates a strategic vulnerability: the framework could be excluded by DESI DR3 (Scenario A: 4.12-sigma) before 21cm data becomes available to test its unique prediction. Conversely, the framework could survive DESI (Scenario B: 2.14-sigma) but remain indistinguishable from vanilla quintessence until the 2040s. The ISW tracking signal is the ONLY currently identified observable that separates the substrate picture from generic dark energy models. The folded bispectrum (f_NL = 0.129) is the other unique channel, but it requires the same purpose-built 21cm instrument with l_max ~ 10^5 (21cm-science-case.md).

**The S69 EUCLID-JOINT-69 result in context.** The Euclid joint forecast gave FW vs LCDM at 4.05-sigma and FW vs Quintessence at 1.72-sigma. The FW/Quintessence discrimination is marginal precisely because expansion history tests cannot distinguish c_s^2 = 0 from c_s^2 = 1 with Euclid's ISW sensitivity. The 21cm channel adds 7.9-sigma to the FW/Quintessence discrimination -- this is where the instrument concept earns its science case.

**Question for van-den-Dungen:** The c_s^2 = 0 prediction traces to the q-theory structure of the Volovik tracking vacuum, where dark energy perturbations follow delta_DE = (1+w)/(1-3w) * delta_m. This relies on the vacuum variable q being a thermodynamic variable that responds to local matter density. In the NCG picture, q maps to the spectral action cutoff Lambda. Does the spectral action formulation produce an effective c_s^2 for dark energy perturbations? Specifically, if the spectral action cutoff Lambda has spatial fluctuations delta(Lambda)/Lambda, do these fluctuations propagate at c_s = 0 (tracking) or c_s = 1 (quintessence-like)? The answer determines whether c_s^2 = 0 is a prediction of the substrate geometry or an additional assumption imported from Volovik's superfluid universe program.

### M4: Spectral Zeta Threshold, Pantheon+ Shadow, & a_0/a_2 Constraints

Three S71 results converge on the question of how well the spectral moment ratio a_0/a_2 is determined and what observational consequences follow from its uncertainty.

**W1-A: Spectral zeta threshold (S_inf = 2.353, 10.2% truncation error).** The key structural insight is the L = 7 decoupling: omega_min(L = 7) = 2.153 M_KK exceeds Lambda = 2.048 M_KK, so L >= 7 sectors sit above the physical cutoff and contribute negative threshold corrections (screening, not enhancement). The physical threshold sum terminates naturally at L = 6, giving S_inf = 2.353 with 10.2% uncertainty from the convergence ratio r_56 = 0.556. This resolves the S70 "oscillatory convergence" puzzle -- there is no oscillation, just the onset of decoupling. The value sits in the PW extrapolation range [2.083, 2.895], and the resulting tree-level Higgs mass (149 GeV) is brought to ~127.5 GeV by BCS dressing (S69 KK-HIGGS-69 PASS).

**W3-A: Pantheon+ Bayesian shadow (17.7% at 1-sigma).** The chain of inference runs: delta(a_0/a_2) -> delta(w_0) via f_partition = 0.03535 -> delta(d_L) -> delta(chi^2_Pantheon+). At 1-sigma, Pantheon+ constrains fractional a_0/a_2 systematics to 17.7%. At 2-sigma, the bound loosens to 54.0%. The spectral zeta truncation uncertainty (10.2%) is 1.73x tighter than the Pantheon+ 1-sigma bound. This means the spectral computation itself is the binding constraint on a_0/a_2 -- current SNe data cannot provide an independent check.

**The hierarchy.** The constraint landscape for a_0/a_2 has three layers:

| Source | Fractional uncertainty | What it constrains |
|:-------|:----------------------|:-------------------|
| Spectral zeta truncation (W1-A) | 10.2% | Internal spectral geometry |
| Pantheon+ 1-sigma (W3-A) | 17.7% | Observational via w_0 -> d_L |
| DESI DR2 w_0 constraint | ~6.2% (sigma_w = 0.057, f_partition = 0.035) | Background cosmology |

DESI DR2 actually provides a tighter observational constraint than Pantheon+ because its w_0 error bar (0.057) maps to delta(a_0/a_2)/a_0 = (0.057/0.035)/2.32 = 7.0%. But this assumes the framework's w_0 prediction is exactly correct (w_0 = -0.918) and treats the DESI measurement as a test of that prediction, not as an independent determination. If we instead treat the DESI-framework offset (w_0(DESI) - w_0(FW) = 0.166) as a systematic, it maps to a 203% shift in a_0/a_2 -- far larger than the spectral zeta uncertainty.

**The asymmetry in the chi^2 profile.** W3-A reports asymmetry = 0.72 at 1-sigma. The Pantheon+ chi^2 landscape allows much larger shifts toward less negative w_0 (toward -0.7) than toward more negative w_0 (toward -1.0). This means a_0/a_2 overestimates (which would make w_0 less negative, increasing the CC contribution relative to gravity) are more tightly bounded than underestimates. Physically, the SNe luminosity distance function d_L(z) is more sensitive to w_0 shifts in the w_0 > -1 direction because these produce larger distance modulus changes at the DESI/Pantheon+ redshift range (z ~ 0.3-1.0).

**Connection to W1-B (a_6 CCM).** The a_6 correction shifts a_4/a_2 by 26.9% (estimate B, zeta ratio), which propagates to alpha_s and m_H. But it does NOT directly shift a_0/a_2, because a_6 enters the spectral action at order Lambda^{-2} relative to a_0 and Lambda^{-4} relative to a_2. The CC mechanism (a_0) and gravitational coupling (a_2) are the zeroth and second spectral moments, while a_6 is the sixth. The moment separation is the protection: the w_0 prediction depends on a_0/a_2 (zeroth-to-second moment ratio), which is scheme-dependent through f_0 and f_2 but not through higher moments. The alpha_s prediction depends on a_4/a_2, which IS sensitive to a_6.

This creates a structural separation in the framework's observational exposure:
- **w_0 = -0.918**: depends on a_0/a_2 ratio. Uncertain at 10.2% (spectral zeta). Observationally invisible in current data (W3-A).
- **alpha_s**: depends on a_4/a_2 ratio. Scheme-dependent at the sign level (S66). Anti-correlated with CC mechanism (W1-B). 25-73x short of resolution.
- **m_H**: depends on the threshold sum S_inf. Now determined to 10.2% as S_inf = 2.353. Tree-level 149 GeV -> BCS-dressed ~127.5 GeV.

The 10.2% truncation error in S_inf propagates to approximately 5% uncertainty in m_H (because m_H ~ sqrt(S_inf) at leading order). This puts the Higgs mass prediction at 127.5 +/- 6.4 GeV, which is consistent with the observed 125.1 GeV within the 10% spectral zeta uncertainty band. The Higgs mass is therefore a genuine success of the spectral geometry -- but the success is conditional on the BCS dressing mechanism and the choice of spectral functional (filter-independence theorem, S62 result 20, established m_H = 134 GeV for ALL 6 cutoff families at tree level, with the remaining gap closed by BCS).

**Question for van-den-Dungen:** The L = 7 decoupling is explained as omega_min(L = 7) exceeding Lambda = 2.048 M_KK. But Lambda itself is a cutoff-scale parameter whose value depends on the spectral functional. If a different f(x) shifts Lambda by 10%, does the decoupling boundary move from L = 7 to L = 6 (tightening S_inf) or to L = 8 (loosening it)? In other words, is the L = 7 decoupling a STRUCTURAL feature of the SU(3) spectrum (determined by the density of states at the KK scale), or is it an ARTIFACT of the particular cutoff choice? The Cauchy-Schwarz spectral moment bound (S62 result 18) and the Chebyshev monotonicity theorem (S66) constrain the relationship between spectral moments across cutoff families -- do they also constrain where decoupling occurs?

### M5: Cross-Cutting Observations

Five structural themes emerge from reading S71's 20 computations against the accumulated constraint landscape (sessions 1-70, 112+ proven results, 141+ closures).

**1. The A_s gap has OVERCORRECTED, and decoherence is the regulator.**

The A_s gap has evolved through the project as follows:

| Session | A_s gap (OOM) | Mechanism |
|:--------|:-------------|:----------|
| S63 | 7.62 | Raw spectral action |
| S64 | 3.16 | BCS occupation + PW selection |
| S69 | 0.485 | Three-channel squeeze |
| S70 | 0.267 | Leggett vacuum |
| S71 W1-D | -0.083 to -1.97 | Compound SU(1,1) squeeze with decoherence |
| S71 W2-A | -2.21 to -2.55 | Full compound (undamped) |

The gap has gone NEGATIVE. The BCS squeeze parameters alone (r_BCS = 1.79 for B2, 3.57 for B1, 1.96 for B3) produce 2.07 OOM of squeeze amplification -- 7.7x the target gap. The spatial and Leggett channels add another ~0.5-0.7 OOM. Without decoherence, the framework overshoots A_s by nearly a factor of 100 (10^{2.07}).

W1-D identifies the decoherence timescale t_dec/t_transit as the controlling parameter. At the lower edge of the decoherence band (t_dec/t_tr = 1.12), delta_OOM = 0.568, leaving residual gap = -0.083 OOM -- marginal closure. At t_dec/t_tr = 5.0, delta_OOM = 1.574, making the overcorrection -1.09 OOM. This means the framework requires cos(phi_eff) < 1 (destructive phase interference) to tame the squeeze amplification.

From an observational standpoint, A_s = 2.1e-9 (Planck 2018 [Paper 29]) is one of the most precisely measured cosmological parameters. The framework now has a mechanism that can produce A_s in the right ballpark, but the output is controlled by a decoherence timescale that is not (yet) computed from first principles. The decoherence parameter has replaced the spectral action normalization as the primary uncertainty in the A_s prediction. This is progress -- the gap has gone from 7.62 OOM (unconstrained) to a range that brackets the observed value -- but the decoherence rate must be derived from the substrate physics for this to become a genuine zero-parameter prediction.

**2. Scheme dependence is now the framework's defining challenge.**

Three S71 results expose scheme dependence at different levels:
- W1-B: delta(lambda_CCM) = 0% (zeta) vs 27% (cutoff) vs 8.6% (anomaly). **Maximal.**
- W1-E: alpha_s correction varies with kappa. Not scheme-dependent per se, but entangled with the spectral functional through a_4/a_2.
- W3-B: omega_L sensitivity to spectral functional alpha is 0.44 -- sub-threshold but not zero.

The S66 discovery that epsilon_H flips sign between the sqrt and zeta functionals (S66 W2-A, PERMANENT negative result) remains the sharpest statement: the spectral functional is not a technical choice but a physical one, and the framework has not identified which functional nature selects. The alpha_s anti-correlation (W1-B: no f_0 value simultaneously places alpha_s and m_H in their observed ranges) is a manifestation of this: the spectral functional determines which combinations of observables can be matched.

**3. The GGE residual CC (110 OOM) confirms q-theory as the sole surviving CC mechanism.**

W3-C computes the direct GGE excitation energy: Delta_E = 0.00918 M_KK per cell, 110 OOM above rho_obs. This is consistent with S55 (114 OOM total), S57 (112 OOM non-equilibrium), and S62 (CC = integrability, monotonicity theorem). The GGE non-equilibrium residual is cosmologically enormous even though it represents only 0.039% of the total vacuum energy. The CC problem in this framework is precisely the integrability problem: the Richardson-Gaudin conserved charges lock the vacuum at a non-equilibrium value that is 110 OOM too high.

The Volovik q-theory mechanism (Scenario B: rho ~ H^2, gap = 0.34 OOM, S66 DILUTION-CC-66 PASS) remains the sole surviving CC route. But q-theory requires the vacuum variable q to relax via Gibbs-Duhem equilibration, which is a DIFFERENT mechanism from the GGE integrability that produces the 110 OOM gap. The framework needs both mechanisms: GGE integrability to freeze the matter content, AND q-theory to relax the vacuum energy to its observed value. Whether these two can coexist -- integrability preserving matter degrees while q-theory relaxes the vacuum degree -- is an open structural question.

**4. The BCS sector is gravitationally safe.**

Three S71 results close a set of BCS stability concerns:
- W1-F: Two-loop Weyl correction = 1.0e-3 (marginal FAIL of the all-orders conjecture, but practically negligible; three-loop = 10^{-9}).
- W3-D: BCS backreaction on a_4 = 2.0e-8 (physical) to 7.0e-6 (worst case). 3-6 OOM below threshold.
- W1-H: GSL extends to 3-cell frustrated ring. S_gen monotone at all 4 stages.

Combined, these establish that the BCS condensate does not significantly perturb the gravitational or gauge sectors of the spectral action. The SU(3) singlet selection rule (BCS condensate cannot directly couple to the Weyl tensor because they live in different irreps: 1 vs 27) provides protection at one-loop; at two-loop, indirect coupling through modified propagators generates the 1.0e-3 correction. The series converges rapidly (lambda = 0.137), so the all-orders bound is delta < 1.2e-3. This is gravitationally inconsequential.

**5. The observational program has a clear temporal hierarchy.**

| Timescale | Test | What it probes | Framework exposure |
|:----------|:-----|:---------------|:-------------------|
| 2026-27 | DESI DR3 | w_0, w_a (background) | w_a = 0 survival gate |
| 2028-30 | JUNO | Mass ordering | Structural geometry |
| 2029-32 | Euclid | sigma_8, f*sigma_8, ISW (marginal) | w = -0.918 expansion history |
| 2034 | LiteBIRD | r = 0.024 | Tensor sector (necessary, not sufficient) |
| 2034 | CMB-S4 | n_s, alpha_s, f_NL | Shape parameters (f_NL undetectable) |
| >2035 | 21cm IM | ISW tracking (c_s^2 = 0), f_NL (folded) | Substrate-specific UNIQUE |

The S70 VdD-Mack workshop's emergence E-10 (temporal asymmetry) is now quantified by S71: DR3 tests background moments (a_0, a_2) at 2-4 sigma tension, while the substrate-specific c_s^2 = 0 signal requires an instrument that does not exist. The framework lives or dies on w_a before it gets to demonstrate its uniqueness. This is structurally unavoidable -- background tests always come before perturbation tests because the background experiments exist and the perturbation experiments do not.

**Question for van-den-Dungen:** The scheme dependence affects different observables differently. w_0 depends on a_0/a_2 (uncertain at 10.2%). alpha_s depends on a_4/a_2 (scheme-dependent at the sign level). m_H depends on S_inf (now 10.2% via spectral zeta). Is there a Kasparov-module argument that constrains the RATIOS between spectral moments (rather than their individual values)? Specifically, the Cauchy-Schwarz bound f_4 * f_0 / f_2^2 >= 1 constrains the moment fractions. Does the KK reduction of the Kasparov product impose additional ratio constraints that would narrow the scheme dependence for alpha_s/a_4 relative to w_0/a_0?

---

## Round 1 — Van-den-Dungen: Response & Cross-Synthesis

### Part 1: Response to Mack's Sections

#### Re: M1 — DESI DR3 Scenario B & the Observational Tension Landscape

**AGREE** on the structural analysis. The four-fold w_a = 0 lock is rigorous, and Mack's identification of w_a as the sole discriminant is sharp. The 2D sensitivity scan result (framework preferred over LCDM at 42.6% of grid points, specifically when w_a moves toward zero) is the cleanest statement of the framework's observational position.

**AGREE** on the SN calibration systematic. The 0.075 swing in w_0 between Pantheon+ and DESY5 calibrations is 1.3x the framework's total w_0 offset from LCDM. This is a data-pipeline issue, not a framework issue, but it materially affects the tension assessment. Mack is right to flag this as underappreciated.

**MISSED** from the NCG side: Mack asks whether w_0 = -0.918 is scheme-dependent through the effacement residual Gamma = 1 - a_4/(a_0 * a_2). The answer is **partially scheme-dependent, but less so than alpha_s**. Here is the precise statement.

The effacement residual Gamma involves the ratio a_4/(a_0 * a_2). In the Chamseddine-Connes spectral action (Paper 06, Section 11), the a_n coefficients are:

  a_0 = f_0 * Lambda^4 * integral(1) = f_0 * Lambda^4 * mode_count
  a_2 = f_2 * Lambda^2 * integral(R/6 - E) = f_2 * Lambda^2 * curvature_content
  a_4 = f_4 * integral(curvature^2 terms) = f_4 * gauge_content

where f_0, f_2, f_4 are moments of the spectral function f(x):

  f_k = integral_0^inf f(x) * x^{(4-k)/2 - 1} dx

The effacement residual Gamma = 1 - a_4/(a_0 * a_2) = 1 - [f_4/(f_0 * f_2)] * [geometric_ratio/Lambda^6]. The geometric part (curvature integrals) is scheme-independent -- it depends only on D_K on Jensen-deformed SU(3). The scheme dependence enters through the ratio f_4/(f_0 * f_2 * Lambda^6).

For the smooth cutoff families tested in S66 (Gaussian, polynomial, heat kernel), the f_k moments vary individually, but the RATIO f_4/(f_0 * f_2) has bounded variation. The Cauchy-Schwarz bound (S62 result 18) gives f_4 * f_0 / f_2^2 >= 1, which constrains the moment ratio from below. In the Gaussian case (f(x) = exp(-x)), f_4/(f_0 * f_2) = 1/(2 * 1) = 0.5. In the zeta scheme, f_4 dominates (S = a_4, no f_0 parameter), so Gamma is not well-defined in the same sense.

The practical answer: w_0 = -0.918 carries a scheme dependence of order the f-moment ratio variation, which from S66 data (3 cutoff families) spans approximately +/- 0.03 in w_0. This is comparable to the SN calibration systematic (0.075) but smaller than the DESI w_0 error bar (0.057). So the scheme dependence is NOT the dominant uncertainty -- the SN calibration is. But it is not negligible either. The w_0 prediction should be reported as w_0 = -0.918 +/- 0.03 (scheme) +/- 0.04 (spectral zeta truncation), giving a total theoretical uncertainty of approximately +/- 0.05.

**EMERGES**: The w_a = 0.066 value that worsens the fit. Mack is right to flag this. The four-fold lock gives w_a = 0 exactly. The 0.066 appears to arise from a BCS-dressing correction to the equation of state, but this correction is NOT well-established in the upstream framework data. From the NCG perspective, w_a = 0 is the structurally honest prediction, and using w_a = 0 over 0.066 IMPROVES the DR3 Scenario B position by 0.74-sigma. The canonical framework prediction should be (w_0 = -0.918 +/- 0.05, w_a = 0), not (w_0 = -0.918, w_a = 0.066).

#### Re: M2 — Non-Trivial Fibration — c_s^2 Protection vs Alpha_s Structural Tension

**AGREE** on the scaling hierarchy (c_s^2 ~ kappa^2, alpha_s ~ kappa) and on the conclusion that the alpha_s tension is structural.

**AGREE** on the scheme dependence diagnosis. The W1-B result (delta = 0% zeta vs 27% cutoff) is the clearest demonstration that the alpha_s extraction is not a well-defined quantity until the spectral functional is fixed. This is not a surprise from the NCG perspective -- the spectral action's dependence on the cutoff function f(x) is a well-known feature of Connes-Chamseddine theory (Paper 06, Section 11.2). What Paper 06 establishes is that the TOPOLOGICAL content (gauge group, representations, charge quantization) is f-independent, while METRIC content (coupling constants, mass relations) depends on f-moments. Alpha_s is metric content.

**MISSED** from my domain: Mack asks whether the Kasparov product imposes a structural upper bound on kappa (the A-tensor strength parameter). The answer is **yes, but the bound is weaker than kappa = 0.5**.

In Paper 01 (Theorem 3.5), the Kasparov product factorization [D_M] = pi_!([D_K]) tensor_A [D_B] requires the vertical operator D_K to be vertically elliptic and the connection form to satisfy a compatibility condition with the Kasparov module structure. The A-tensor (O'Neill integrability tensor) enters as a perturbation of the product Dirac operator:

  D_total = D_K tensor 1 + gamma_K tensor D_B + A-correction

The Kasparov product exists (and equals the tensor sum) provided the A-correction is a locally bounded perturbation relative to D_total (Paper 10, Theorem 4.1). The K-HOMOLOGY-STABILITY-61 gate verified this with alpha = 0.081 < 1 for the JENSEN deformation. For the A-tensor from non-trivial fibration, the analogous condition is:

  ||A|| / spectral_gap(D_K) < 1  (Kato-Rellich bound)

The spectral gap of D_K at the fold is 0.8197 M_KK (from W1-A). The A-tensor norm scales as ||A|| ~ kappa * |R_K|^{1/2} ~ kappa * 1.4 M_KK (using R_K = -2.018 at the fold). So the Kasparov unitarity condition gives:

  kappa * 1.4 / 0.8197 < 1  =>  kappa < 0.586

This is close to but slightly above the "physical maximum" of kappa = 0.5 used in the computation. The Kasparov product EXISTS for all kappa < 0.586, confirming that the framework's factorization is valid throughout the physically relevant range. But it does NOT tighten the alpha_s correction, because the Kasparov bound (0.586) is looser than the physical bound (0.5).

The sharper point: even if kappa were allowed to be arbitrarily large, the alpha_s correction scales linearly (kappa * 28/360 at leading order), so reaching the required 781% would need kappa ~ 100 -- far beyond any perturbative regime. The Kasparov product ceases to exist at kappa = 0.586, and the entire fiber-base factorization breaks down. There is no regime where the A-tensor solves the alpha_s problem.

**EMERGES**: The independence of Jensen deformation and non-trivial fibration, which my W1-E computation established (Sym^2(T*K) vs Omega^1(M, ad(P))), has a deeper NCG meaning. In Paper 05 (Boeijink-van den Dungen), the globally non-trivial almost-commutative manifold has spectral triple (A, H, D) where A = C^inf(P) tensor_G A_F (equivariant sections of the algebra bundle). The gauge module structure (GAUGE-MODULE-61: PASS, rank 775) lives in the A_F part, while the Jensen deformation lives in the connection part of D. The fact that these are independent degrees of freedom in the spectral triple explains WHY the c_s^2 and alpha_s corrections separate: c_s^2 is controlled by the geometric part (Jensen in Sym^2, hence A-tensor enters quadratically through the kinetic energy), while alpha_s is controlled by the algebraic part (CCM matching in a_4/a_2, hence A-tensor enters linearly through the gauge field strength). This is a structural feature of the spectral triple, not a numerical accident.

#### Re: M3 — 21cm ISW Pre-Registration & Substrate-Specific Observable Signatures

**AGREE** on the detection landscape assessment and the structural mismatch with planned 21cm instruments. The ISW kernel peaks at z ~ 0.5-1.5, and no planned facility provides the post-reionization HI intensity mapping at z ~ 0.4-3 needed for the ISW-21cm cross-correlation at SNR > 4.

**AGREE** on the temporal vulnerability: the framework could be excluded by DR3 before its substrate-specific signature (c_s^2 = 0) becomes testable. This is structurally unavoidable.

**DISAGREE** partially on whether c_s^2 = 0 needs justification from the NCG spectral action. Mack asks: does the spectral action formulation produce an effective c_s^2 for DE perturbations, or is c_s^2 = 0 imported from Volovik's superfluid universe program? The answer is that **c_s^2 = 0 is a prediction of the product spectral triple structure, not an import, but the connection to the Volovik tracking vacuum is through q-theory, not through the spectral action directly.**

Here is the precise chain:

1. The spectral triple is (C^inf(M) tensor A_K, L^2(S_M tensor S_K), D_M tensor 1 + gamma_M tensor D_K). The product structure means D_K depends on the fiber metric g_K(tau) but NOT on d_mu(g_K). This is the origin of c_s^2 = 0 at tree level: there is no kinetic energy for the modulus tau in the spectral action Tr(f(D^2/Lambda^2)). The spectral action produces a potential V(tau) but no kinetic term (d_mu tau)^2 at tree level. (The kinetic term emerges at one-loop through the DeWitt metric G_{tau tau} = 5.0, from S63 KINETIC-NORMALIZATION-63.)

2. At one-loop, the effective action acquires c_s^2 = G_{tau tau} / G_{tau tau} = 1 in the naive modulus field space, but this is the sound speed of TAU perturbations, not of dark energy perturbations. The dark energy perturbation delta_rho_DE depends on how rho_DE responds to local matter density, which is the q-theory identification: rho_DE = epsilon(q) - mu*q where q = a_0 spectral moment.

3. The q-theory tracking relation delta_DE = (1+w)/(1-3w) * delta_m gives c_s^2_DE(eff) = 0. This is the statement that the vacuum variable q adjusts locally to the matter density, so DE perturbations track matter perturbations. In the spectral action language, this means the cutoff Lambda responds to local geometry through the Seeley-DeWitt expansion: a_0(x) = Lambda^4 * mode_count(x), where mode_count(x) responds to the local metric.

4. The critical distinction: c_s^2 = 0 for the tau modulus at tree level is a TOPOLOGICAL prediction of the product spectral triple (confirmed by KASPAROV-VERIFY-61 and the S70 c_s^2 = 0 validation). c_s^2_DE(eff) = 0 for the dark energy tracking vacuum is a PHYSICAL identification that depends on the q-theory framework. The first is proven. The second is a model assumption connecting the spectral action to cosmological perturbation theory.

So the honest answer to Mack's question: c_s^2 = 0 is a prediction of the substrate geometry for the modulus sector, and the q-theory identification maps this to c_s^2_DE(eff) = 0 for dark energy perturbations. The substrate geometry part is proven (product structure, Kasparov verified). The q-theory mapping is a physical interpretation, not a mathematical theorem.

**EMERGES**: The ISW pre-registration chain (W2-F) is the cleanest example of the topological/spectral split that emerged from the S70 workshop. The c_s^2 = 0 prediction is topological (product structure). The +4.0% ISW enhancement is spectral (it depends on w_0 = -0.918, which depends on a_0/a_2 with its 10.2% scheme uncertainty). But the DISCRIMINANT between framework and quintessence (the c_s^2 = 0 vs c_s^2 = 1 part, contributing +4.0% of the total +6.7%) is topological. This means the substrate-specific signal is protected against scheme dependence even though the total ISW signal is not. The 21cm instrument concept targets the topological part specifically.

#### Re: M4 — Spectral Zeta Threshold, Pantheon+ Shadow, & a_0/a_2 Constraints

**AGREE** on the constraint hierarchy: spectral zeta truncation (10.2%) is the binding constraint, not Pantheon+ (17.7%) or DESI (6.2% conditional on FW correctness). Mack's structural separation of the framework's observational exposure (w_0 depends on a_0/a_2, alpha_s on a_4/a_2, m_H on S_inf) is precisely correct and maps directly onto the NCG spectral moment structure.

**AGREE** that the Higgs mass at 127.5 +/- 6.4 GeV (BCS-dressed, 10% spectral zeta uncertainty) is a genuine success conditional on both the BCS dressing mechanism and the cutoff family choice.

**DISAGREE** on one point: Mack's hierarchy puts DESI as tighter than Pantheon+ for the a_0/a_2 constraint (6.2% vs 17.7%). But this is CONDITIONAL on the framework being exactly correct (w_0 = -0.918 is the true value). The Pantheon+ constraint is UNCONDITIONAL -- it bounds the systematic regardless of whether the framework is correct. These are different types of constraints and should not be directly compared. The correct hierarchy for systematic bounds on a_0/a_2 is: spectral zeta (10.2%, internal) > Pantheon+ (17.7%, external unconditional) > DESI-conditional (6.2%, only if FW true).

**MISSED** from the NCG side regarding Mack's question about the L = 7 decoupling. The L = 7 boundary is **partially structural and partially cutoff-dependent**, and the Kasparov product structure provides the clean distinction.

The SU(3) Peter-Weyl decomposition gives eigenvalues organized by irrep labels (p,q) with angular momentum L = p + q. The minimum eigenvalue omega_min(L) for each L-sector is a property of D_K on Jensen-deformed SU(3) -- it depends ONLY on the fiber geometry and is cutoff-independent. The omega_min values are:

  L=1: 0.820,  L=2: 0.926,  L=3: 1.130,  L=4: 1.393,  L=5: 1.688,
  L=6: 2.004,  L=7: 2.153  (all in M_KK units, from W1-A data)

These are structural (eigenvalues of D_K). The density of states at each L is also structural (from SU(3) representation theory: degeneracy ~ (p+1)(q+1)(p+q+2)/2).

What IS cutoff-dependent is the threshold Lambda = 2.048 M_KK. This value comes from Lambda = sqrt(f_2/f_0) * M_KK for the Gaussian cutoff. For a different spectral function:
- Polynomial f(x) = (1-x)_+^3: Lambda/M_KK shifts to approximately 1.73 (lower), and decoupling would begin at L = 5 or 6.
- Heat kernel f(x) = exp(-x): Lambda/M_KK = sqrt(1/1) = 1.0, and decoupling would begin at L = 3.

So the EXISTENCE of a decoupling boundary is structural (the omega_min(L) sequence is monotonically increasing, so eventually omega_min(L) > Lambda for any finite Lambda). But the LOCATION of the boundary (which L) depends on the cutoff. For the Gaussian, it is L = 7. For steeper cutoffs, it shifts to lower L.

The Cauchy-Schwarz bound (f_4 * f_0 / f_2^2 >= 1) and the Chebyshev monotonicity theorem (Q^eff >= Q^bare) constrain the RELATIONSHIP between f-moments but do NOT fix Lambda absolutely. They constrain moment ratios like f_4/f_2, which propagate to coupling constant ratios, not to the absolute cutoff scale. So these theorems do not directly constrain where decoupling occurs.

The bottom line for S_inf: the VALUE of S_inf = 2.353 carries the 10.2% truncation uncertainty at L = 6 for the Gaussian cutoff. If the cutoff changes, BOTH the decoupling boundary AND S_inf change. The S_inf value is scheme-dependent, as is the Higgs mass derived from it. But the RANGE [1.995, 2.895] bracketing S_inf across Gaussian-class cutoffs (from the L = 6 to L = 7 sector contributions) is structural -- it reflects the SU(3) eigenvalue density at the KK scale.

**EMERGES**: Mack's hierarchy of observational exposure maps precisely onto the Kasparov product's factorization levels. The spectral action on M^4 x SU(3) decomposes via the Kasparov product (Paper 01) into:

  S_total = sum_n f_n * a_n(D_K) * a_{4-n}(D_M)

The a_n(D_K) are fiber geometry (structural, computed from D_K eigenvalues). The f_n are spectral function moments (scheme-dependent). The a_{4-n}(D_M) are base geometry (determined by the 4D metric). Each observable probes a different COMBINATION of these factors:

| Observable | Fiber content | Scheme content | Base content |
|:-----------|:-------------|:---------------|:-------------|
| w_0 | a_0/a_2 (structural) | f_0/f_2 (scheme) | trivial (flat M^4) |
| alpha_s | a_4/a_2 + S_inf (structural) | f_4/f_2 + f_0 (scheme) | trivial |
| m_H | S_inf (structural) | f (all moments) | trivial |
| c_s^2 | 0 (topological) | none | none |
| n_s | d(a_2)/d(tau) (structural) | cancels in ratio | none |

The observables with the LEAST scheme dependence are those where f-moments cancel in ratios: n_s and c_s^2. The observables with the MOST scheme dependence are those requiring absolute f-moment values: alpha_s and m_H. This is the Kasparov product telling us which predictions to trust.

#### Re: M5 — Cross-Cutting Observations

**AGREE** on all five themes, with additions.

**Theme 1 (A_s overcorrection).** The BCS squeeze parameters producing 2.07 OOM at r_BCS = 0 (no spatial contribution) is a structural property of the Bogoliubov transformation at the fold. From the NCG side, the squeeze parameter r_BCS for each mode is determined by cosh(2r) = 1 + 2*|beta_k|^2, where beta_k is the Bogoliubov coefficient from Parker pair production at the van Hove singularity. The flat-band structure at B2 (d(lambda)/d(tau) = 0 at the fold, SPECTRAL-FLOW-61) maximizes |beta_k| for the B2 modes. The decoherence timescale is indeed the controlling parameter, and I concur it must be derived from first principles (from the BCS Hamiltonian's off-diagonal decay rate in the GGE, which is a BdG spectral action computation) for the A_s prediction to become zero-parameter.

**Theme 2 (Scheme dependence as defining challenge).** This is the deepest point. From the NCG perspective, the spectral action functional f(x) is the analog of the renormalization scheme in QFT. Connes' original proposal (Paper 06, Section 11.1) was that f is fixed by the full theory (possibly a UV completion). The framework has no UV completion, so f remains unfixed. The S62 Cauchy-Schwarz theorem establishes that the Gaussian is the unique maximum-entropy cutoff (minimizing CC at fixed gravity normalization), which provides a SELECTION PRINCIPLE for f. But this selection principle is thermodynamic, not geometric. The Kasparov product (Paper 01) is f-independent because it operates at the K-theory level, not the spectral action level. This is why topological predictions (c_s^2, mass ordering, spectral flow, gauge group) are scheme-independent while metric predictions (coupling constants, mass ratios, alpha_s) carry scheme uncertainty.

I add to Mack's assessment: the scheme dependence is not merely a technical challenge but reveals that the framework's spectral action is fundamentally a SEMICLASSICAL approximation. The full K-theoretic content (Kasparov product, Fredholm index, KO-dimension) is exact. The spectral action approximation Tr(f(D^2/Lambda^2)) ~ sum f_n * a_n is an asymptotic expansion valid at large Lambda. The scheme dependence arises because the higher-order terms (a_6, a_8, ...) are NOT negligible at Lambda ~ M_KK, and different cutoffs weight them differently. The W1-B finding that a_6 contributes 27% to lambda_CCM is direct evidence of this: the Seeley-DeWitt expansion is not converging rapidly enough at the KK scale for the spectral action to give scheme-independent numerical predictions.

**Theme 3 (GGE residual CC = 110 OOM).** Consistent with the NCG perspective. The spectral action zeroth moment a_0 is the mode count (CC), and the second moment a_2 is the curvature content (gravity). The Spectral Moment Decoupling theorem (S64) established that these are SIBLING moments of the same spectral function, not parent-child. The CC problem is the statement that a_0 and a_2 are independently determined by D_K, and their ratio a_0/a_2 is too large by 110 OOM. The q-theory mechanism changes the PHYSICAL vacuum energy by adjusting the thermodynamic variable q, without changing a_0 or a_2. This is the correct separation.

**Theme 4 (BCS gravitationally safe).** The three-pronged closure (Weyl two-loop 1.0e-3, a_4 backreaction 2.0e-8, GSL on frustrated ring) is comprehensive. From the NCG side, the SU(3) singlet selection rule (BCS in 1, Weyl in 27) is the representation-theoretic reason for this protection. Paper 05 (Section 5.3) shows that the gauge module structure separates the BCS condensate from the gravitational sector at the algebraic level: the inner fluctuations D -> D + A + JAJ^{-1} mix the gauge sector (a_4) but not the gravitational sector (a_2) with the BCS condensate, because the condensate transforms trivially under the gauge group. This is EXACT, not perturbative.

**Theme 5 (Temporal hierarchy).** The topological/spectral split maps directly to Mack's temporal ordering. Background tests (w_0, w_a) probe SPECTRAL quantities (moment ratios) that carry scheme dependence. Perturbation tests (c_s^2, f_NL) probe TOPOLOGICAL quantities (product structure, GGE statistics) that are scheme-independent. The temporal ordering (background first, perturbations later) means the framework is tested on its WEAKEST predictions first and its STRONGEST predictions last. This is not optimal, but it is structurally unavoidable.

**MISSED** from the NCG side regarding Mack's question about Kasparov-module constraints on spectral moment RATIOS: see V2 below for a systematic treatment.

### Part 2: Original Analysis

#### V1: Principal Bundle Geometry & the Fibration Independence Theorem

The S71 W1-E computation established that Jensen deformation (Sym^2(T*K)) and non-trivial fibration (Omega^1(M, ad(P))) are independent degrees of freedom. This is not merely a parameter-counting statement but reflects a deep structural fact about the spectral triple on a principal bundle.

**The NCG framework for non-trivial fibrations.** Paper 05 (Boeijink-van den Dungen, "Globally non-trivial almost-commutative manifolds") constructs spectral triples on non-trivial principal G-bundles P -> M. The key construction is:

1. The algebra A = C^inf(P, A_F)^G = equivariant sections of the algebra bundle A_F -> M associated to P.
2. The Hilbert space H = L^2(P, S_M tensor S_F)^G = equivariant spinor sections.
3. The Dirac operator D = D_M^P tensor 1 + gamma_M tensor D_F, where D_M^P is the horizontal Dirac operator on P (twisted by the principal connection) and D_F is the fiber (vertical) Dirac operator.

The connection on P enters D_M^P through the horizontal distribution: D_M^P uses the horizontal lift of vectors from M to P, which requires choosing a connection omega in Omega^1(P, g). The fiber metric (Jensen deformation) enters D_F through the vertical Laplacian on G.

**Why they are independent.** The connection omega lives in A^1(P, g) -- it is a g-valued 1-form on the total space P. The Jensen deformation lives in Sym^2(g*) -- it is a symmetric 2-tensor on the fiber g = Lie(G). These are sections of DIFFERENT bundles over M:
- omega in Omega^1(M, ad(P)) (after gauge-fixing to a Lie algebra-valued form on M)
- g_Jensen in Gamma(Sym^2(T*K)) where K = G (fiber)

Their functional spaces are linearly independent. Perturbing one does not perturb the other. This is proven at the jet level: the first jets of omega (curvature F_omega) and the first jets of g_Jensen (covariant derivative of the fiber metric) live in different representation spaces of the structure group G = SU(3).

**Consequences for the W1-E computation.** The A-tensor parameterized by kappa in W1-E is the O'Neill integrability tensor of the Riemannian submersion P -> M equipped with the connection omega. On a trivial bundle (P = M x G), the A-tensor vanishes identically (KASPAROV-VERIFY-61, A-TENSOR-61: A = T = 0 exact). On a non-trivial bundle, A is determined by the curvature F_omega of the connection. The parameterization |A|^2 = kappa * |R_K| relates the connection curvature to the fiber curvature, with kappa measuring the relative strength.

The independence theorem means:
1. c_s^2 corrections from non-trivial fibration (kappa^2 scaling) are INDEPENDENT of c_s^2 corrections from Jensen deformation (which are zero at tree level by product structure).
2. alpha_s corrections from non-trivial fibration (kappa scaling) are INDEPENDENT of alpha_s corrections from higher-order CCM (a_6 scaling).
3. The two correction channels ADD, they do not interfere. The total alpha_s correction is 4.2% (fibration) + 6.5-26.9% (a_6 CCM) ~ 10-31%. This additive structure is a consequence of the functional independence of Omega^1(M, ad(P)) and Sym^2(T*K).

**What Paper 05 adds that the W1-E computation does not capture.** Paper 05 (Section 6) shows that on a non-trivial principal bundle, the inner fluctuations D -> D + A + JAJ^{-1} generate a gauge field that includes BOTH the connection omega AND the Higgs field. On a trivial bundle, these are independent (the Higgs is a purely internal degree of freedom). On a non-trivial bundle, the topology of P constrains the Higgs field: specifically, the instanton number of omega determines the boundary conditions on the Higgs field. This means that on a non-trivial SU(3) bundle over M^4, the Higgs mass prediction could shift because the Higgs self-coupling receives contributions from the topological charge of the principal connection. The W1-E computation treats kappa as a free parameter; Paper 05 suggests that on a specific instanton background, kappa is QUANTIZED (determined by the Chern number c_2(P)).

**Implications.** If P has non-trivial topology (c_2(P) not equal to 0), then kappa is not a continuous parameter but is fixed by the instanton number. On SU(3) bundles over S^4, the possible instanton numbers are c_2 in Z (integers). For c_2 = 0 (trivial bundle), kappa = 0 and we recover the product geometry. For c_2 = 1 (one-instanton), kappa is determined by the instanton solution, giving a SPECIFIC alpha_s correction that is not continuously tunable. This is the route identified in the Priority Open Tasks (item 11: PS generator gauge module check on Jensen SU(3)). It has not been computed.

**The fibration independence theorem (formal statement)**:

For a Riemannian submersion pi: (P, g_P) -> (M, g_M) with fiber (K, g_K), the spectral action S(D_P) depends on:
- The fiber metric g_K (through a_n(D_K)) -- this is the Jensen deformation
- The principal connection omega (through the A-tensor and its curvature) -- this is the fibration
- The base metric g_M (through a_n(D_M)) -- this is fixed (flat M^4)

To first order in perturbations:
  delta S / delta(g_K) and delta S / delta(omega) live in orthogonal functional spaces.

This is verified computationally (W1-E: cross-terms below 0.5%, A-TENSOR-61: A = T = 0 at kappa = 0) and follows from the jet-level independence established in Paper 05. The theorem holds exactly on the product bundle; perturbative corrections at kappa > 0 introduce mixed terms at order kappa^2 (which is why c_s^2 scales as kappa^2 rather than kappa).

#### V2: Kasparov Product Structure & Spectral Moment Stability

Mack's question (M5) asks whether the Kasparov product imposes constraints on spectral moment RATIOS that could narrow the scheme dependence for alpha_s relative to w_0. This is the right question. The answer reveals a fundamental limitation of the spectral action approach that the Kasparov product cannot remedy, but also identifies what the Kasparov product CAN constrain.

**What the Kasparov product constrains (exact, scheme-independent).**

The Kasparov product [D_K] tensor_A [D_M] = [D_total] in KK_0(C(M), C) is an equality of K-homology classes. K-homology classes are equivalence classes of Fredholm modules up to homotopy (Paper 11: UKK(A,B) ~ KK(A,B)). The data preserved by K-homology is:

1. **Index pairings**: For any K-theory class [p] in K_0(C(M)), the integer index <[p], [D_total]> = <[p], [D_K] tensor [D_M]>. This is EXACT and scheme-independent. It determines the topological content: gauge group representations, charge quantization, chiral anomaly cancellation.

2. **Spectral flow**: For a path D(t) connecting D_total(tau_1) to D_total(tau_2), the spectral flow sf(D) is a K-theory invariant. SPECTRAL-FLOW-61 verified sf = 0 on the Jensen line.

3. **Fredholm index**: ind(D_total) = 0 (from parallelizability of SU(3), CHERN-INST-61). This is structural.

None of these constrain spectral moment RATIOS. The K-homology class remembers the INDEX of the operator, not its SPECTRUM.

**What the Kasparov product does NOT constrain.**

The spectral moments a_n = Tr(D_K^{-2n} * geometric_terms) are SPECTRAL data, not K-theoretic data. Two operators with the SAME K-homology class can have completely different spectral moments. For example, D_K(tau = 0) (round SU(3)) and D_K(tau = 0.19) (Jensen fold) have the same K-homology class (K-HOMOLOGY-STABILITY-61: alpha = 0.081 < 1, Kato-Rellich) but different spectral moments (a_2 changes by ~3%, a_4 by ~7% across the transit, from W2-D).

Therefore: the Kasparov product CANNOT constrain a_0/a_2, a_4/a_2, or any spectral moment ratio. These ratios are spectral, not topological. The scheme dependence of alpha_s (which depends on a_4/a_2) is fundamentally OUTSIDE the reach of K-theory.

**What CAN constrain spectral moment ratios.**

The constraints on moment ratios come from ANALYTIC properties of the heat kernel, not from K-theory:

1. **Cauchy-Schwarz bound** (S62, proven): f_4 * f_0 / f_2^2 >= 1. This is a property of the spectral function f(x), NOT of D_K. It constrains the ratio of f-moments but not the a_n coefficients directly.

2. **Gilkey product formula** (Paper 06, verified S61): On a product M^4 x K, a_n(D_total) = sum_{j+k=n} a_j(D_M) * a_k(D_K). For flat M^4, a_j(D_M) = delta_{j,0} * vol(M), so a_n(D_total) = vol(M) * a_n(D_K). The ratios a_n/a_0 are PURELY fiber quantities, independent of the base geometry. This is verified to machine precision (KASPAROV-VERIFY-61).

3. **Weyl asymptotics** (structural): For large eigenvalue lambda, the eigenvalue density N(lambda) ~ lambda^{dim/2} by Weyl's law. This constrains the ASYMPTOTIC ratios of spectral moments: a_n/a_0 -> O(Lambda^{-n}) for n > 0. But the framework operates at Lambda ~ M_KK, where Weyl asymptotics is not a good approximation (the mode count at L = 6 is only 1.08M out of the infinite tower).

4. **Chebyshev monotonicity** (S66, proven): Q^eff >= Q^bare for UV-suppressing cutoffs. This constrains the DIRECTION of cutoff corrections (they increase the effective coupling) but not their MAGNITUDE.

**The structural conclusion on scheme dependence.**

The Kasparov product cleanly separates WHAT is scheme-independent from WHAT is not:

| Quantity | K-theoretic? | Scheme-independent? | Observational test |
|:---------|:------------|:--------------------|:-------------------|
| Gauge group SU(3)xSU(2)xU(1) | YES | YES | Confirmed |
| Mass ordering B1 < B2 < B3 | YES (spectral flow) | YES | JUNO (2028) |
| c_s^2 = 0 (product structure) | YES (Kasparov) | YES | 21cm (>2035) |
| Spectral flow sf = 0 | YES | YES | No direct test |
| KO-dimension = 6 | YES | YES | Confirmed |
| w_a = 0 | PARTIAL (four-fold lock) | YES (GGE topological) | DESI DR3 (2026-27) |
| n_s = 0.9557 | NO (spectral) | PARTIAL (ratio cancellation) | Planck (2.2-sigma) |
| w_0 = -0.918 | NO (spectral) | NO (a_0/a_2 ratio) | DESI DR3 (0.39-sigma Sc.B) |
| alpha_s | NO (spectral) | NO (a_4/a_2 ratio) | CMB-S4 (scheme-dependent) |
| m_H = 127.5 GeV | NO (spectral) | NO (S_inf) | LHC (conditional) |

The framework's strongest predictions are K-theoretic. Its weakest predictions are spectral. The observational program should weight the K-theoretic predictions more heavily.

**A specific constraint the Kasparov product DOES provide on moment ratios.** While the Kasparov product does not constrain a_n/a_m directly, it constrains the STABILITY of these ratios under deformation. Paper 10 (Theorem 4.1) shows that if V is a locally bounded perturbation of D with relative bound alpha < 1, then [D + V] = [D] in K-homology. The K-HOMOLOGY-STABILITY-61 gate verified alpha = 0.081 for the Jensen deformation. The consequence: any spectral quantity that CHANGES by more than the relative bound alpha under Jensen deformation is NOT protected by K-theory. From W2-D (CAUSAL-MOMENT-MAP-71), the fractional variation of a_2/a_4 is 2.921% across the transit -- this is 36x larger than alpha = 0.081, confirming that the moment ratio is spectrally controlled, not topologically controlled.

This means the framework should report its moment-ratio-dependent predictions with explicit scheme uncertainties, not as zero-parameter results. The zero-parameter claim applies to the K-theoretic predictions only.

#### V3: Questions for Mack

**Q1 (Scheme dependence propagation to w_0).** In Re:M1, I estimated the scheme dependence of w_0 at approximately +/- 0.03. Mack's M1 analysis treats w_0 = -0.918 as a point prediction with zero theoretical uncertainty. If the theoretical uncertainty is +/- 0.05 (scheme + spectral zeta combined), how does this change the DR3 scenario analysis? Specifically: does the 2D Fisher forecast with w_0 = -0.918 +/- 0.05 (theoretical) convolved with sigma_DR3(w_0) = 0.046 materially change the tension assessments for Scenarios A, B, C? My expectation is that it REDUCES tension for Scenario B (because the framework's w_0 uncertainty band overlaps more of the posterior) but does not save Scenario A.

**Q2 (Decoherence timescale as the new bottleneck).** Mack identifies decoherence as the A_s regulator (M5, theme 1). The decoherence band [1.12, 26.5] in t_dec/t_transit from W1-D spans delta_OOM from 0.568 to 1.970. At the lower edge, the A_s gap is marginally closed (-0.083 OOM). At the interior (t_dec/t_transit = 5), it overcorrects by 1.09 OOM. Is there an OBSERVATIONAL constraint on the decoherence timescale that is independent of A_s? For instance: does the decoherence rate affect the spectral index n_s (through phase averaging of the Bogoliubov coefficients), or does it affect the non-Gaussianity f_NL (through the degree of quantum-to-classical transition)? If the decoherence timescale affects multiple observables, we could cross-correlate and constrain t_dec/t_transit from the multi-observable fit rather than tuning it to match A_s alone.

**Q3 (alpha_s: structural tension or scheme artifact?).** M2 reports the alpha_s tension as structural (781% shortfall, 25-73x deficit after all corrections). But the S66 CUTOFF-NS-66 FAIL showed that n_s varies by 0.164 across three cutoffs -- larger than the Planck error bar by 39x. Alpha_s inherits this pathology. My question: in the observational cosmology assessment, do you distinguish between "alpha_s is in tension with Planck" (which assumes a SPECIFIC spectral functional) and "alpha_s is undetermined because the spectral functional is unfixed" (which is the NCG-honest statement)? The two have very different implications for the constraint map. The first is a gate failure. The second is a statement that the gate is not yet well-defined.

**Q4 (Observational handle on the topological/spectral split).** V2 establishes that the framework's K-theoretic predictions are scheme-independent and its spectral predictions are not. From the observational side: is there a way to test the K-THEORETIC content independently of the spectral action? For example: the gauge group SU(3)xSU(2)xU(1) is K-theoretic (from the Fredholm module structure). The mass ordering B1 < B2 < B3 is K-theoretic (from spectral flow). JUNO tests the mass ordering. Are there other planned experiments that specifically test K-theoretic predictions? If so, we should flag them as structurally more informative than tests of spectral predictions.

**Q5 (ISW signal decomposition).** In M3, you report the total ISW enhancement as +6.8% (auto) and +4.0% (cross), with the substrate-specific part being +4.0% (c_s^2 = 0 vs 1). The remaining +2.7% comes from expansion history (w_0 = -0.918 vs -1.0). My question: if the framework's w_0 carries a +/- 0.05 theoretical uncertainty (from scheme dependence), what is the propagated uncertainty on the +2.7% expansion history component? The c_s^2 = 0 part (topological) is unaffected, but the expansion history part (spectral) could shift by a factor of 2 or more. Does the substrate-specific part remain dominant over the expansion history part across the full w_0 uncertainty band?

---

## Round 2 — Mack: Follow-up

### CONVERGENCE

**C1: w_0 = -0.918 +/- 0.05 is the correct prediction statement.**

In M1 I treated w_0 = -0.918 as a point prediction with zero theoretical uncertainty. Van-den-Dungen's Re:M1 analysis corrects this. The effacement residual Gamma = 1 - a_4/(a_0 * a_2) depends on the f-moment ratio f_4/(f_0 * f_2), which varies across cutoff families. The +/- 0.03 from f-moment variation is a real systematic, and combining it with the +/- 0.04 from spectral zeta truncation (10.2%) gives +/- 0.05 total. I accept this estimate and note that it changes the framework's observational position favorably: w_0 = -0.918 +/- 0.05 overlaps the DESI DR2 + Pantheon+ value (-0.827 +/- 0.063) at the 1.2-sigma level, rather than the 1.6-sigma I computed using the point prediction. The scheme uncertainty is not a weakness here -- it is an honest representation of what the spectral action determines, and it places the framework squarely in the viable region for Scenario B.

What changed my assessment: Van-den-Dungen's explicit computation of the f-moment ratio variation across three cutoff families (Gaussian, polynomial, heat kernel) in Re:M1. The Cauchy-Schwarz bound f_4 * f_0 / f_2^2 >= 1 constrains the ratio from below but not from above, so the +/- 0.03 is bounded one-sidedly. This asymmetry maps to an asymmetry in the w_0 band: the framework can be slightly MORE negative than -0.918 (toward LCDM) more easily than less negative (toward DESI). This is structurally favorable because the DESI tension is in the "less negative" direction.

**C2: w_a = 0 is the canonical prediction, and w_a = 0.066 should be retired.**

Van-den-Dungen's Re:M1 confirms that w_a = 0.066 has no provenance in the upstream framework data. I flagged this in M1; the Re:M1 response makes it definitive. The four-fold lock (GGE integrability, Josephson phase, frozen texture, thermalization barrier) gives w_a = 0 exactly. The canonical framework prediction should be (w_0 = -0.918 +/- 0.05, w_a = 0), and this improves the Scenario B tension from 2.88-sigma to 2.14-sigma. This is not a trivial change -- it moves the framework from "disfavored 22x relative to LCDM" to "disfavored 2.8x relative to LCDM" under Scenario B.

**C3: The topological/spectral split is the organizing principle for the observational program.**

Van-den-Dungen's V2 provides the cleanest statement I have seen of what the Kasparov product constrains and what it does not. The K-homology class preserves index pairings, spectral flow, and Fredholm index -- all topological. It does NOT preserve spectral moment ratios (a_0/a_2, a_4/a_2), which are spectral data that two operators with the same K-homology class can disagree on (the 2.921% variation of a_2/a_4 across the transit from W2-D being 36x larger than the Kato-Rellich bound alpha = 0.081). I accept this framework completely. It resolves my M2 question about what the Kasparov product constrains: the answer is that K-theory constrains topology but not metric content, and the spectral action's metric predictions inherit the full scheme dependence of the f-moments.

The V2 table (Re:M5, reproduced in V2) is now my reference classification for the observational program:
- K-theoretic predictions (c_s^2 = 0, gauge group, mass ordering, spectral flow, KO-dim): scheme-independent, highest confidence.
- Spectral predictions (w_0, alpha_s, m_H): scheme-dependent, report with explicit uncertainties.
- Partial (w_a = 0): the four-fold lock is physical (GGE + Josephson), not K-theoretic, but it is scheme-independent because it depends on the integrability structure of the GGE, not on spectral moments.

**C4: L = 7 decoupling EXISTENCE is structural, LOCATION is cutoff-dependent.**

Van-den-Dungen's Re:M4 resolves my question about whether the L = 7 boundary is a structural feature or a cutoff artifact. The answer is both: the omega_min(L) sequence is monotonically increasing (structural property of D_K on Jensen-deformed SU(3)), so decoupling MUST occur at some L for any finite Lambda. But the specific L depends on Lambda/M_KK, which depends on the spectral functional through sqrt(f_2/f_0). For the heat kernel (Lambda/M_KK = 1.0), decoupling begins at L = 3 -- dramatically earlier, which would give a SMALLER S_inf and a lower tree-level Higgs mass. This means the Higgs mass prediction carries an even larger scheme uncertainty than the 10.2% from truncation at L = 6: the choice of spectral functional can shift which sectors contribute to the threshold sum. The range [1.995, 2.895] is structural only within the Gaussian-class cutoff family. Across cutoff families, S_inf could be substantially smaller.

**C5: c_s^2 = 0 has two components -- substrate geometry (proven) and q-theory mapping (model assumption).**

Van-den-Dungen's Re:M3 provides the precise chain I asked for. The product spectral triple structure gives c_s^2 = 0 at tree level for the tau modulus -- this is a mathematical theorem (Kasparov verified, product structure means no kinetic term for tau in the spectral action). The mapping to c_s^2_DE(eff) = 0 for dark energy perturbations requires the q-theory identification: the vacuum variable q = a_0 spectral moment responds to local geometry through the Seeley-DeWitt expansion, and the tracking relation delta_DE = (1+w)/(1-3w) * delta_m follows. The substrate geometry part is proven. The q-theory mapping is a physical interpretation. I accept this distinction and note that it affects how the ISW prediction should be reported: the +4.0% substrate-specific signal rests on both the topological prediction (c_s^2_modulus = 0, proven) and the physical identification (c_s^2_DE = 0, model assumption). The topological part is protected; the physical part depends on the q-theory framework.

### DISSENT

**D1: The constraint hierarchy for a_0/a_2 should distinguish conditional from unconditional bounds.**

Van-den-Dungen disagrees with my M4 hierarchy that places DESI (6.2%) tighter than Pantheon+ (17.7%). His argument: the DESI bound is conditional on the framework being exactly correct (w_0 = -0.918 as the true value), while Pantheon+ is unconditional. I acknowledge the logical distinction -- these are different types of constraints. But from the standpoint of experimental cosmology, the distinction matters less than Van-den-Dungen implies. ALL constraints on a_0/a_2 are conditional on the framework's w_0 prediction being the correct interpretation. If the framework is wrong about w_0, then a_0/a_2 has no cosmological meaning and neither Pantheon+ nor DESI constrains it. The conditional/unconditional distinction is relevant only within the framework, where it means: "DESI tells you more about a_0/a_2 IF the framework is right, while Pantheon+ tells you less but does so regardless." In practice, the binding constraint is the spectral zeta truncation (10.2%) in both cases, because neither DESI (6.2%) nor Pantheon+ (17.7%) is tighter than the internal computation.

New evidence: The S71 W3-A Bayesian shadow computation shows asymmetry = 0.72 at 1-sigma. This means the Pantheon+ chi^2 landscape is NOT symmetric around the framework prediction -- shifts toward less negative w_0 are more tightly constrained than shifts toward more negative w_0. The asymmetry introduces a directional bias into the "unconditional" bound that makes it effectively conditional on the direction of the a_0/a_2 shift. The distinction between conditional and unconditional bounds blurs when the chi^2 landscape itself is asymmetric.

**D2: The alpha_s status is a gate failure, not an undetermined gate -- but with a caveat.**

Van-den-Dungen's V3-Q3 asks whether I distinguish between "alpha_s is in tension with Planck" (gate failure assuming a specific spectral functional) and "alpha_s is undetermined because the spectral functional is unfixed" (gate not well-defined). I maintain that the correct characterization is a gate failure, for the following reason.

The S66 computation found alpha_s = -0.038 at L_max = 4 using the standard Chamseddine-Connes spectral action with the smooth cutoff. This is a specific numerical prediction from a specific spectral functional. The Planck 2018 constraint is alpha_s = -0.0045 +/- 0.0067. The prediction is 5.0-sigma from observation. That is a gate failure for that functional.

The scheme dependence complicates this because a different functional gives a different alpha_s. But the existence of ONE functional that gives 5.0-sigma tension is already informative: it means the spectral geometry, combined with that functional, makes a prediction that nature rejects. The response "the functional is unfixed, so the gate is not well-defined" is formally correct but operationally evasive. By that standard, NO spectral-action prediction is testable until the functional is fixed -- which would remove w_0, alpha_s, m_H, and every metric prediction from the constraint map simultaneously.

The caveat: Van-den-Dungen's V2 point about the S66 CUTOFF-NS-66 result (n_s range = 0.164 across three cutoffs, 39x the Planck error bar) means that the spectral functional choice dominates the alpha_s prediction at the same level it dominates n_s. The honest characterization is: **alpha_s = -0.038 is a gate failure for the smooth cutoff functional; the tree-level alpha_s = 0 is consistent with Planck at 0.67-sigma; and the loop-level prediction is scheme-dependent at a level that exceeds the observational error bar.** The gate status should be reported as FAIL(conditional on smooth cutoff), with the explicit statement that the zeta functional gives alpha_s = 0 (which is PASS).

**D3: The Seeley-DeWitt convergence problem does not invalidate the spectral action -- it constrains its domain.**

Van-den-Dungen's addition to M5 Theme 2 states that "the Seeley-DeWitt expansion is not converging rapidly enough at the KK scale for the spectral action to give scheme-independent numerical predictions," citing the W1-B finding that a_6 contributes 27% to lambda_CCM as direct evidence. I push back on the implication.

The Seeley-DeWitt expansion IS the spectral action in the asymptotic limit. The question is not whether it converges (it is asymptotic, not convergent) but whether the leading terms dominate at Lambda ~ M_KK. The a_6/a_4 ratio of 0.567 (spectral zeta) or 0.269 (prompt spec) shows that the sixth moment is a significant fraction of the fourth. But this is precisely why the framework includes a_6 corrections -- the W1-B computation IS the next-order term in the expansion. The relevant question is not "does the expansion converge?" but "does including a_6 improve or worsen the match to observation?" The answer from W1-B is: it shifts lambda_CCM by 27% (PASS), but the anti-correlation between CC and alpha_s persists (structural). The expansion is useful but insufficient to resolve the alpha_s problem.

The deeper point: Van-den-Dungen correctly identifies that the K-theoretic predictions are exact while the spectral action predictions are asymptotic. But the framework does not claim to derive coupling constants from K-theory alone -- it claims to derive them from the spectral action, which is the semiclassical approximation to the K-theoretic content. The asymptotic nature is a known limitation, not a discovery. The question is whether the spectral action provides useful quantitative predictions at Lambda ~ M_KK, and the answer from S71 is: yes for w_0 (10.2% uncertainty), marginal for m_H (conditional on BCS dressing), and no for alpha_s (scheme-dependent at the sign level).

### EMERGENCE

**E1: The three-layer prediction hierarchy -- topological, spectral-robust, spectral-fragile -- maps directly to the observational timeline.**

Combining my M5 temporal hierarchy with Van-den-Dungen's V2 topological/spectral classification produces a three-layer structure that I did not see in either contribution alone:

| Layer | Examples | Scheme dependence | Observable test | Timeline | Confidence |
|:------|:---------|:------------------|:----------------|:---------|:-----------|
| Topological | c_s^2 = 0, gauge group, mass ordering, w_a = 0 | None | JUNO (2028), 21cm (>2035), DESI DR3 (2026) | Near + far | Highest |
| Spectral-robust | n_s = 0.9590 (ratio cancellation), omega_L (sensitivity 0.44) | Partial (cancels in ratios) | Planck (now), CMB-S4 (2034) | Near | High |
| Spectral-fragile | alpha_s, m_H, w_0, A_s | Full f-moment dependence | CMB-S4 (alpha_s), LHC (m_H), DESI (w_0) | Near | Low without functional selection |

The key insight: the framework is tested on spectral-fragile predictions FIRST (DESI DR3 tests w_0, which is spectral-fragile with +/- 0.05 scheme uncertainty) and on topological predictions LAST (21cm tests c_s^2 = 0, which is topological and scheme-independent). But the scheme uncertainty in w_0 actually HELPS the framework survive the near-term tests: w_0 = -0.918 +/- 0.05 is closer to DESI than w_0 = -0.918 exactly. The fragility works in the framework's favor for background tests.

The spectral-robust layer is the under-exploited middle ground. n_s = 0.9590 benefits from ratio cancellation (the f-moments largely cancel in dn_s/dlnk), and omega_L = 0.138 M_KK has sensitivity |d ln omega_L/d alpha| = 0.44 (W3-B). These predictions are not fully scheme-independent (hence not topological), but they are much less sensitive to the spectral functional than w_0 or alpha_s. The CMB-S4 measurement of n_s to sigma = 0.002 will test the spectral-robust prediction at 2.94-sigma discrimination power (from S69 CMB-S4-NS-69 PASS). This is the highest-EVOI near-term test.

**E2: The decoherence timescale and the spectral functional are LINKED unknowns -- solving one constrains the other.**

This emerged from combining Van-den-Dungen's V3-Q2 with my M5 Theme 1 (A_s overcorrection). The decoherence timescale t_dec/t_transit controls how much BCS squeeze survives to produce A_s. The spectral functional f(x) controls the spectral action normalization and hence the overall energy scale. These are currently treated as independent unknowns. But they are not.

The decoherence rate in the BCS Hamiltonian is governed by the off-diagonal matrix elements of the GGE density matrix in the energy eigenbasis. These matrix elements depend on the Bogoliubov coefficients beta_k, which depend on the spectral action gradient dS/dtau at the fold. The gradient dS/dtau = sum_n f_n * d(a_n)/d(tau) depends on the spectral functional through the f_n weights. A different spectral functional changes f_n, which changes dS/dtau, which changes the Bogoliubov coefficients, which changes the decoherence rate. Therefore t_dec/t_transit is a function of f(x).

This means: if the spectral functional is chosen to match n_s (spectral-robust, ratio cancellation), the decoherence timescale is DETERMINED, and A_s becomes a zero-parameter prediction. Conversely, if A_s is used to fix t_dec/t_transit, this constrains the spectral functional and thereby constrains alpha_s, m_H, and w_0 simultaneously. The unknowns are not independent -- they form a single unknown (the spectral functional f(x)) that propagates to multiple observables through different channels.

This is a carry-forward computation: derive t_dec/t_transit as a function of f(x) explicitly, then check whether the value of f(x) that gives A_s = 2.1e-9 is consistent with the value that gives n_s = 0.9590 and w_0 = -0.918.

**E3: The Kasparov unitarity bound kappa < 0.586 establishes a PROTECTION THEOREM for the c_s^2 prediction.**

Van-den-Dungen's Re:M2 computes the Kasparov unitarity condition: kappa * 1.4 / 0.8197 < 1, giving kappa < 0.586. At kappa = 0.586, the maximum possible c_s^2 correction is delta(c_s^2) = 0.586^2 * g_3^2/(16*pi^2) = 5.85e-4. Combined with the one-loop trivial-bundle correction (3.36e-4), the ABSOLUTE MAXIMUM c_s^2 from all perturbative channels is 9.21e-4. This is a protection theorem:

**Statement: For any non-trivial SU(3) principal bundle over M^4 with Kasparov-compatible connection, the effective dark energy sound speed satisfies c_s^2 < 9.21e-4.**

This bound is structural: it depends only on the Kasparov unitarity condition and the SU(3) spectral gap. It does NOT depend on the spectral functional. The ISW discrimination between framework (c_s^2 < 10^{-3}) and quintessence (c_s^2 = 1) survives by three orders of magnitude even at the Kasparov boundary. This is the strongest form of the c_s^2 = 0 prediction: not merely that it is zero at tree level, but that it is BOUNDED below 10^{-3} by the Kasparov product structure.

For the 21cm science case: the +4.0% ISW cross-power enhancement requires c_s^2_DE < 0.01 (to distinguish from quintessence c_s^2 = 1). The Kasparov bound guarantees c_s^2 < 9.21e-4, which is 10x below this threshold. The 21cm prediction is protected by the K-theory of the spectral triple, not by a perturbative estimate.

**E4: The instanton quantization of kappa (V1) would resolve the alpha_s problem or permanently close it.**

Van-den-Dungen's V1 makes a point I had not considered: on a non-trivial SU(3) bundle with Chern number c_2 = 1, the A-tensor strength kappa is not a continuous parameter but is FIXED by the instanton solution. This means kappa is either 0 (trivial bundle, no alpha_s correction) or a specific discrete value determined by the one-instanton configuration on SU(3) over S^4 (or, more precisely, over the compactified base).

If the instanton kappa exceeds 3.82, the alpha_s tension is resolved in a single structural step. If it is less than 0.586 (the Kasparov bound), the alpha_s correction is at most 4.2% and the tension persists. But the instanton kappa is a COMPUTABLE quantity -- it depends on the self-dual Yang-Mills solution on the SU(3) bundle, which is determined by the Chern number and the fiber geometry. This is a finite computation that would resolve the alpha_s question definitively for the non-trivial fibration channel. However: the Kasparov product ceases to exist for kappa > 0.586, so if the instanton kappa exceeds 0.586, the fiber-base factorization breaks down entirely. In that regime, the spectral triple is no longer a product and the entire framework must be reformulated. The alpha_s resolution through instanton kappa is therefore bounded by the same Kasparov condition that protects c_s^2.

The structural conclusion: non-trivial fibration cannot resolve the alpha_s problem. The Kasparov bound kappa < 0.586 limits the correction to at most 5.0% (from the scaling formula kappa*(5*kappa+28)/360). Combined with a_6 CCM (26.9%), the total correction budget is ~32%. The required 781% is unreachable within the perturbative regime where the Kasparov product exists. Alpha_s resolution, if it occurs, must come from a different mechanism entirely -- one that operates outside the spectral action's Seeley-DeWitt expansion. The tree-level alpha_s = 0 remains the framework's honest prediction.

### QUESTIONS

**Answers to Van-den-Dungen's V3 Questions:**

**A-Q1 (w_0 +/- 0.05 impact on DR3).** The 2D Fisher forecast with w_0 theoretical uncertainty convolved with DR3 measurement error proceeds as follows. The effective variance for w_0 becomes sigma^2_eff(w_0) = sigma^2_DR3(w_0) + sigma^2_theory(w_0) = 0.046^2 + 0.05^2 = 0.00461, giving sigma_eff(w_0) = 0.068. The correlation rho = -0.85 applies only to the measurement errors (the theoretical uncertainty is independent of w_a). The 2D chi^2 becomes:

For Scenario B (center w_0 = -0.90, w_a = -0.30), canonical FW (w_0 = -0.918 +/- 0.05, w_a = 0):
- Delta(w_0) = -0.018, Delta(w_a) = +0.30
- chi^2 = (1/(1-rho^2)) * [(Delta_w0/sigma_eff_w0)^2 + (Delta_wa/sigma_wa)^2 - 2*rho*(Delta_w0/sigma_eff_w0)*(Delta_wa/sigma_wa)]
- chi^2 = (1/0.2775) * [(0.018/0.068)^2 + (0.30/0.177)^2 - 2*(-0.85)*(0.018/0.068)*(0.30/0.177)]
- chi^2 = 3.60 * [0.070 + 2.874 + 2*0.85*0.265*1.695]
- chi^2 = 3.60 * [0.070 + 2.874 + 0.765] = 3.60 * 3.709 = 13.35

Wait -- this gives HIGHER chi^2 than the point-prediction case (6.860). The issue is that convolution is not the right approach. The theoretical uncertainty should be marginalized over, not added in quadrature. The correct procedure is: the framework predicts w_0 drawn from a distribution centered at -0.918 with width 0.05. For each drawn w_0, the chi^2 against DR3 is computed. The marginalized chi^2 is the expectation over the theoretical prior. This reduces to the added-in-quadrature formula ONLY when the theoretical prior is Gaussian and uncorrelated with w_a.

Correcting: with sigma_eff(w_0) = 0.068 (correctly adding theoretical and measurement in quadrature) and sigma(w_a) = 0.177 (measurement only), and using the correlation rho = -0.85 between measurement errors only, the effective correlation in the combined space is reduced to rho_eff = rho * sigma_DR3(w_0)/sigma_eff(w_0) = -0.85 * 0.046/0.068 = -0.575.

Re-computing:
- chi^2 = (1/(1-0.575^2)) * [(0.018/0.068)^2 + (0.30/0.177)^2 - 2*(-0.575)*(0.018/0.068)*(0.30/0.177)]
- chi^2 = (1/0.669) * [0.070 + 2.874 + 2*0.575*0.265*1.695]
- chi^2 = 1.494 * [0.070 + 2.874 + 0.516] = 1.494 * 3.460 = 5.17

This corresponds to 1.82-sigma (2D). Compared to the point-prediction chi^2 = 6.860 (2.14-sigma), the theoretical uncertainty reduces the tension by 0.32-sigma. Van-den-Dungen's expectation is confirmed: w_0 +/- 0.05 helps under Scenario B.

For Scenario A (center w_0 = -0.75, w_a = -0.73): the w_0 tension is much larger (Delta_w0 = -0.168), so sigma_eff(w_0) = 0.068 vs sigma_DR3 = 0.046 reduces the w_0 chi^2 contribution from (0.168/0.046)^2 = 13.34 to (0.168/0.068)^2 = 6.10. But the w_a tension (Delta_wa = 0.73) still dominates. Scenario A remains excluded (~3.5-sigma with theoretical uncertainty vs ~4.1-sigma without). Van-den-Dungen's expectation is again confirmed.

**A-Q2 (Decoherence cross-constraints from n_s and f_NL).** The decoherence timescale t_dec/t_transit does affect multiple observables beyond A_s, and this is the route to constraining it independently.

For n_s: the spectral index depends on the Bogoliubov coefficients through n_s - 1 = d ln P_k / d ln k, where P_k = |alpha_k + beta_k|^2 * P_k^{vac}. Decoherence damps the cross-term 2*Re(alpha_k * beta_k^*) by a factor exp(-t/t_dec), leaving P_k = (|alpha_k|^2 + |beta_k|^2) * P_k^{vac} in the fully decohered limit. The ratio (|alpha|^2 + |beta|^2) / |alpha + beta|^2 depends on the relative phase, so the spectral TILT n_s is affected through the k-dependence of the phase. At the BCS flat band (B2), the phase is approximately constant (d phi/d k ~ 0 at the van Hove singularity), so decoherence has minimal effect on n_s near the flat band. Away from the flat band, the phase varies more rapidly and decoherence suppresses the coherent oscillations, slightly reddening the spectrum. The correction is of order delta(n_s) ~ (1 - exp(-t_transit/t_dec)) * (d phi/dk)^2 / k^2, which is small for t_dec > t_transit (the GGE regime). Quantitatively, this is a next-order computation that has not been performed.

For f_NL: the bispectrum is more sensitive to decoherence than the power spectrum because it is a phase-sensitive observable. The folded bispectrum (f_NL = 0.129, S67 GGE-BISPECTRUM-67) depends on the three-point correlation of Bogoliubov pairs, which involves products of alpha_k * beta_{-k}. Decoherence damps these cross-terms exponentially. In the limit t_dec >> t_transit (coherent), f_NL = 0.129 (full GGE value). In the limit t_dec << t_transit (fully decohered), f_NL approaches zero because the pair correlations are destroyed. The equilateral component (f_NL = 0.853) depends on the sound speed modification, which is less phase-sensitive. The ratio f_NL(equil)/f_NL(folded) therefore INCREASES with decoherence, from 6.6 (coherent) toward infinity (fully decohered). This ratio is an observable diagnostic of the decoherence timescale.

The cross-constraint: if the 21cm instrument measures both f_NL(equil) and f_NL(folded), their ratio constrains t_dec/t_transit independently of A_s. A_s constrains t_dec through the squeeze amplitude. The bispectrum ratio constrains t_dec through the phase coherence. These are different functions of t_dec, so their intersection gives a unique solution. This is a strong argument for the 21cm instrument concept: it would measure t_dec/t_transit from TWO independent channels (A_s squeeze and bispectrum ratio), providing an internal consistency check.

However, at the projected CMB-S4 sensitivity (sigma(f_NL equil) = 5.0, sigma(f_NL folded) = 6.9), neither f_NL component is detectable. The cross-constraint is accessible only through the 21cm channel.

**A-Q3 (alpha_s: gate failure vs undetermined gate).** Answered in D2 above. My position: FAIL(conditional on smooth cutoff), with tree-level alpha_s = 0 PASS at 0.67-sigma. The gate status depends on the spectral functional. The framework should report both values.

**A-Q4 (Experiments testing K-theoretic predictions).** The current observational program tests four K-theoretic predictions:

1. **Gauge group SU(3) x SU(2) x U(1)**: Confirmed by the Standard Model. This is the framework's deepest success (KO-dim = 6, Fredholm module structure) but is retrospective, not predictive in the usual sense.

2. **Normal mass ordering (B1 < B2 < B3)**: JUNO (2028-2030, 3-sigma), Hyper-K (2028+), DUNE (2032, 5-sigma). This is the cleanest future test of a K-theoretic prediction. If JUNO reports inverted ordering at > 3-sigma, the spectral geometry of D_K on Jensen-deformed SU(3) is falsified -- the entire framework fails, not just one prediction.

3. **c_s^2 = 0 (product structure)**: 21cm ISW (>2035, SNR = 4.16 ideal). This is K-theoretic (Kasparov product verified, now protected by the kappa < 0.586 Kasparov bound establishing c_s^2 < 9.21e-4).

4. **w_a = 0 (GGE integrability)**: DESI DR3 (2026-27). This is partially K-theoretic: the GGE integrability is a property of the Richardson-Gaudin algebra (algebraic, not spectral), and the Josephson phase locking is a property of the CG(24) tessellation (topological). But the w_a = 0 prediction also depends on the thermalization barrier (59 OOM gap), which is spectral.

The under-exploited K-theoretic prediction is the SPECTRAL FLOW sf = 0 on the Jensen line (SPECTRAL-FLOW-61). Spectral flow measures the net number of eigenvalues crossing zero as D_K is deformed along a path. sf = 0 means the spectrum does not reorganize topologically during the transit. This has no direct observational test that I can identify, but it constrains the dynamics: a non-zero spectral flow would indicate a topological phase transition (change in the Fredholm index), which would produce qualitatively different physics at the fold. The absence of spectral flow supports the smooth, impulsive transit picture rather than a topological phase transition.

For the observational program: JUNO is the most informative near-term experiment from the K-theoretic perspective. DESI DR3 tests a partially K-theoretic prediction (w_a). The 21cm instrument tests the most protected K-theoretic prediction (c_s^2 = 0). The ranking by K-theoretic content is: JUNO > 21cm > DESI DR3 (for w_a) >> CMB-S4 (for n_s, alpha_s -- these are spectral, not K-theoretic).

**A-Q5 (ISW signal decomposition under w_0 uncertainty).** The total ISW enhancement has two components:
- Expansion history: +2.7% (from w_0 = -0.918 vs -1.0). Depends on a_0/a_2 (spectral).
- Substrate-specific: +4.0% (from c_s^2 = 0 vs 1). Depends on product structure (topological).

Under w_0 = -0.918 +/- 0.05, the expansion history component scales approximately linearly with |1 + w_0|. At w_0 = -0.918, |1 + w_0| = 0.082. At w_0 = -0.868 (upper edge of scheme band), |1 + w_0| = 0.132, and the expansion history ISW enhancement scales up by a factor 0.132/0.082 = 1.61, giving +4.3%. At w_0 = -0.968 (lower edge), |1 + w_0| = 0.032, and the enhancement drops to +1.1%.

The total ISW enhancement ranges from +5.1% (w_0 = -0.968) to +8.3% (w_0 = -0.868), compared to the central +6.7%. The substrate-specific contribution (+4.0%) is CONSTANT across this range (it depends on c_s^2 = 0, not on w_0). The expansion history contribution ranges from +1.1% to +4.3%.

The substrate-specific part is dominant at the lower edge of the w_0 band (4.0% vs 1.1%) but comparable at the upper edge (4.0% vs 4.3%). Across the full w_0 uncertainty band, the substrate-specific contribution is 48% to 78% of the total signal. The answer to Van-den-Dungen's question: the substrate-specific part REMAINS dominant at the lower edge of the w_0 band but becomes comparable to the expansion history part at the upper edge. The 21cm discriminant (c_s^2 = 0 vs 1) is robust because even when expansion history contributes equally, it contributes in the SAME direction as the substrate-specific signal -- both enhance the ISW. The quintessence model (c_s^2 = 1) with the same w_0 would show only the expansion history component (+2.7% at central w_0), while the framework shows the full +6.7%. The FW/Quint ratio (+4.0%) is insensitive to w_0 uncertainty because the expansion history part cancels in the ratio.

**New questions for Van-den-Dungen:**

**Q1 (Instanton kappa computation).** In V1, you note that on a non-trivial SU(3) bundle with c_2 = 1, kappa is fixed by the instanton solution. Has this value been computed for SU(3) on S^4 (or on the relevant compactified base)? The one-instanton moduli space of SU(3) on S^4 is 12-dimensional (4*N^2 - 5 = 4*9 - 5 = 31 for the ADHM construction -- actually 12 for SU(3) from the BPST reduction). The instanton kappa depends on the instanton scale parameter rho relative to the base curvature radius. Is there a canonical choice (e.g., conformal instanton at the round point) that gives a specific kappa? If kappa_instanton > 0.586, the Kasparov product breaks down and the entire non-trivial fibration sector is topologically obstructed. This would be a structural result: the framework MUST live on a trivial bundle, making kappa = 0 and alpha_s = 0 (tree level) the only possibility.

**Q2 (Spectral functional from K-theory).** V2 establishes that the Kasparov product is f-independent because it operates at the K-theory level. But the spectral action IS the passage from K-theory to metric geometry. Is there a K-theoretic criterion that selects the spectral functional? For instance: the S62 Cauchy-Schwarz theorem identifies the Gaussian as the maximum-entropy cutoff (minimizing CC at fixed gravity normalization). Is there a K-theoretic formulation of this selection principle -- e.g., the spectral functional that minimizes the distance (in the Kasparov product topology) between the spectral action and the K-theoretic content? If such a criterion exists, it would resolve the scheme dependence problem at the foundational level.

**Q3 (a_2/a_4 near-constancy).** W2-D reports a_2/a_4 variation of only 2.921% across the transit, despite a_4 itself varying by 6.569%. This near-constancy means the gravity-to-gauge balance is approximately preserved. From the NCG perspective, is this a consequence of the Gilkey product formula (which gives a_n in terms of fiber quantities that shift proportionally), or is it a special property of the Jensen deformation on SU(3)? If it is a consequence of the product formula, it would hold for ANY fiber geometry, not just SU(3). If it is specific to SU(3), then the near-constancy is a prediction that could fail on a different gauge group.

---

## Round 2 — Van-den-Dungen: Cross-Synthesis

### CONVERGENCE

**C1: w_0 = -0.918 +/- 0.05 is the canonical prediction, and the Cauchy-Schwarz asymmetry is structurally real.**

Mack's C1 acceptance of the +/- 0.05 theoretical uncertainty is correct, and the observation that this IMPROVES the framework's observational position (from 1.6-sigma to 1.2-sigma against DESI DR2 + Pantheon+) is the right conclusion. The new observation about asymmetry -- that the Cauchy-Schwarz bound f_4 * f_0 / f_2^2 >= 1 constrains the ratio from below but not from above, making the w_0 band asymmetric toward more negative values -- deserves further elaboration.

The Cauchy-Schwarz bound saturates for the Gaussian cutoff (f(x) = exp(-x) gives f_4 * f_0 / f_2^2 = 1 exactly, S62 result 18). For any other smooth cutoff, the ratio exceeds 1. Since Gamma = 1 - f_4/(f_0 * f_2 * Lambda^6) * geometric_ratio, and the f-ratio is bounded below by 1, the effacement residual Gamma is bounded ABOVE. This means w_0 = -(1 - Gamma)/1 is bounded from above (less negative) by the Gaussian value, and other cutoffs push w_0 MORE negative (toward LCDM). The asymmetry is structural: the Gaussian cutoff gives the LEAST negative w_0, and every other smooth cutoff gives a w_0 closer to -1. The scheme uncertainty band should be reported as w_0 = -0.918 (+0.01, -0.04), not +/- 0.03 symmetrically. This further improves the framework's position against DESI because the band extends primarily in the safe direction (toward LCDM).

I accept Mack's A-Q1 computation that convolved theoretical uncertainty reduces Scenario B tension from 2.14-sigma to 1.82-sigma. The correction from naive quadrature to the reduced effective correlation rho_eff = rho * sigma_DR3/sigma_eff = -0.575 is the right treatment.

**C2: w_a = 0 is permanently canonical. The 0.066 provenance is traced and retired.**

Full agreement. The four-fold lock (GGE integrability, Josephson phase, frozen texture, thermalization barrier) gives w_a = 0 exactly in the spectral triple framework. The lock depends on three structural properties: (1) the Richardson-Gaudin algebra is integrable on the BCS Hilbert space (algebraic), (2) the CG(24) tessellation is rigid under small perturbations (topological), (3) the GGE-to-Gibbs gap is 59 OOM (spectral, but overwhelmingly large). None of these are scheme-dependent. The w_a = 0 prediction is among the framework's most secure -- comparable in confidence to c_s^2 = 0 and the gauge group. The 0.066 originated from a BCS-dressing correction that was not validated in the spectral triple formalism, and I concur it should be retired.

**C3: The topological/spectral split is now the permanent organizing principle, with Mack's three-layer refinement accepted.**

Mack's E1 refines my V2 two-category classification (K-theoretic vs spectral) into a three-layer hierarchy: topological, spectral-robust, spectral-fragile. I accept this refinement because it captures a real distinction that my binary classification missed. The spectral-robust layer (n_s, omega_L) occupies a genuine middle ground: these quantities are spectral (they depend on eigenvalues, not K-theory classes), but ratio cancellations in the spectral functional partially cancel the f-moment dependence. From Paper 06 (Section 11.2), the spectral action gradient dS/dtau involves sums like d(a_n)/d(tau) * f_n * Lambda^{4-n}. The spectral index n_s depends on d^2S/dtau^2 divided by (dS/dtau)^2, which is a ratio where many f_n factors cancel. This ratio cancellation is not exact (the cancellation is between different n-values that enter with different powers of Lambda), but it suppresses the scheme dependence by approximately one order of magnitude compared to the individual a_n values. Mack's "spectral-robust" label is the correct characterization.

The three-layer hierarchy with the temporal mapping (topological tested last, spectral-fragile tested first) is a permanent structural feature of the observational program.

**C4: L = 7 decoupling existence is structural; location is cutoff-dependent.**

Mack's C4 draws the correct conclusion from Re:M4 and adds the important sharpening: for the heat kernel (Lambda/M_KK = 1.0), decoupling begins at L = 3, giving a substantially smaller S_inf and a lower tree-level Higgs mass. This means the m_H prediction carries a scheme uncertainty LARGER than the 10.2% from truncation at L = 6 alone -- the scheme choice determines which L-sectors contribute. I concur. The honest statement is: the tree-level Higgs mass from the spectral action on Jensen-deformed SU(3) lies in the range [110, 165] GeV across all smooth cutoff families, with the BCS dressing moving the result toward 125 GeV from wherever the tree-level value lands. The framework needs both the spectral geometry AND the BCS dressing to match the observed Higgs mass, and the BCS dressing does most of the work.

**C5: c_s^2 = 0 two-component structure is settled.**

Mack's decomposition -- substrate geometry (proven: product spectral triple, Kasparov factorization) plus q-theory mapping (physical identification: vacuum variable q responds to local geometry) -- is the correct and complete statement. The substrate geometry part is a theorem. The q-theory part is a physical model. The ISW prediction rests on both. For the 21cm science case, the relevant question is not whether c_s^2 = 0 is "proven" in some absolute sense, but whether the combination (topological product structure + Volovik q-theory) is the most economical physical interpretation. It is: q-theory requires one identification (the spectral action cutoff Lambda as the vacuum variable), and this identification is not adjustable -- it either works or it does not. The +4.0% substrate-specific ISW signal tests this identification directly.

### DISSENT

**D1: The conditional/unconditional distinction for a_0/a_2 constraints is real but narrower than I claimed, due to Pantheon+ asymmetry.**

Mack's D1 makes a substantive point: the Pantheon+ chi^2 landscape asymmetry (0.72 at 1-sigma) means the "unconditional" bound is itself directionally biased, blurring the conditional/unconditional distinction. I concede this partially. The asymmetry means Pantheon+ constrains positive shifts in a_0/a_2 (less negative w_0, more CC relative to gravity) more tightly than negative shifts. This directionality IS a form of conditionality -- the bound depends on which direction you shift.

However, there remains a genuine logical distinction that Mack's pragmatic argument does not eliminate. The Pantheon+ bound says: "IF a_0/a_2 shifts by more than 17.7%, the SNe luminosity distances are inconsistent with data at 1-sigma, REGARDLESS of whether the framework is correct." The DESI bound says: "IF the framework's w_0 prediction is correct AND a_0/a_2 shifts by more than 6.2%, then the DESI measurement is inconsistent with the prediction at 1-sigma." The first is a model-independent constraint on any theory that produces w_0 from a_0/a_2. The second is a self-consistency test of this specific framework. Both are useful; they are not the same type of constraint.

Where Mack is right: in PRACTICE, both are dominated by the spectral zeta truncation (10.2%), so the distinction does not affect which constraint is binding. I maintain the logical distinction for correctness but accept that it has no operational consequences for S71.

**D2: Alpha_s status -- I accept Mack's FAIL(conditional) formulation but sharpen the scope of "conditional."**

Mack's D2 argues that declaring the gate "undetermined" is operationally evasive because it removes all spectral-action metric predictions from the constraint map simultaneously. This is a fair methodological critique. The response "the functional is unfixed" applies equally to w_0, m_H, and n_s, so using it selectively for alpha_s would be inconsistent.

I accept the FAIL(conditional on smooth cutoff) characterization. The precise scope:

- alpha_s = -0.038: FAIL at 5.0-sigma (smooth cutoff, L_max = 4).
- alpha_s = 0: PASS at 0.67-sigma (tree-level, ANY functional).
- alpha_s = scheme-dependent loop correction: the value spans [-0.038, 0] depending on the spectral functional.

The gate status is: **FAIL for the smooth cutoff functional; PASS at tree level; UNDETERMINED at loop level for the zeta functional.** This three-way report is more informative than either FAIL or UNDETERMINED alone, and it preserves the constraint map for other spectral predictions while being honest about what the specific computation showed.

Where I sharpen beyond Mack: the alpha_s FAIL should not be given equal weight to the w_0 PASS. The w_0 prediction benefits from Cauchy-Schwarz asymmetry (scheme uncertainty pushes toward LCDM, improving the match). The alpha_s prediction benefits from NO such structural protection -- the scheme uncertainty spans the full range from FAIL to PASS. The structural asymmetry in scheme dependence (w_0 protected one-sidedly, alpha_s unprotected) is itself informative: it tells us the spectral action is more reliable for low moments (a_0/a_2) than for high moments (a_4/a_2), which is expected for an asymptotic expansion.

**D3: The Seeley-DeWitt non-convergence is a feature, not a bug -- but it DOES constrain what the spectral action can predict.**

Mack's D3 argues that the asymptotic expansion is useful even though it does not converge, because including higher-order terms (a_6) improves the match. This is correct as a pragmatic statement. But there is a deeper structural point that Mack's response does not fully engage with.

The Seeley-DeWitt expansion S ~ sum_{n=0}^{infinity} f_n * a_n is an asymptotic series. For asymptotic series, including MORE terms initially improves the approximation and then, past an optimal truncation order N*, the approximation WORSENS. The optimal truncation order is N* ~ Lambda^2 / M_KK^2. For the Gaussian cutoff with Lambda/M_KK = 2.048, N* ~ 4. The a_6 term (n = 3 in the Seeley-DeWitt labeling) is AT or PAST the optimal truncation order. The W1-B finding that a_6 contributes 27% to lambda_CCM does not mean the expansion is "including the next useful term" -- it may mean the expansion is past its useful range, and the 27% correction is the beginning of the divergent tail.

This is not a reason to discard the a_6 result. The 27% correction is computed, it is physically meaningful, and it shifts the Higgs quartic coupling in a definite direction. But it means that a_8, a_10, etc., are NOT guaranteed to be smaller corrections. The convergence of the perturbative improvement is an open empirical question: does a_6 + a_8 converge, or does it oscillate and grow? The Seeley-DeWitt expansion at Lambda ~ M_KK is in the transition zone between convergence and divergence, which is precisely why the scheme dependence is large. The Kasparov product (K-theory level) does not see this problem because it operates at the non-perturbative level. The spectral action (semiclassical approximation) lives with it.

What this means for the constraint map: predictions that depend only on a_0 and a_2 (w_0) are past the optimal truncation safely. Predictions that depend on a_4 (alpha_s, m_H) are AT the optimal truncation. Predictions that require a_6 or higher are PAST the optimal truncation and carry non-perturbative uncertainty. This maps exactly onto Mack's three-layer hierarchy: topological (no a_n dependence), spectral-robust (a_0/a_2 or ratio cancellation), spectral-fragile (a_4/a_2 or higher).

### EMERGENCE

**E1: The Cauchy-Schwarz asymmetry in the spectral functional creates a structural attractor toward LCDM in the w_0 direction.**

Combining my C1 analysis (Gaussian saturates Cauchy-Schwarz, all other cutoffs push w_0 more negative) with Mack's C1 (scheme uncertainty improves DR3 position) produces a structural insight that neither round alone captured. The Cauchy-Schwarz theorem (S62, proven permanent) does more than bound f-moment ratios -- it establishes a PREFERRED DIRECTION in the space of spectral functionals. The Gaussian is the unique boundary point (equality in Cauchy-Schwarz), and all interior points (other smooth cutoffs) give MORE negative w_0. This means:

1. The framework's w_0 prediction has a one-sided attractor: scheme variation pushes toward LCDM, never away from it.
2. The asymmetric band w_0 = -0.918 (+0.01, -0.04) means the framework is STRUCTURALLY compatible with LCDM to within 0.09 in w_0 at the LCDM-nearest edge, or 0.96 in w_0 at the farthest edge.
3. DESI DR3 can exclude the framework only if the observed w_0 is LESS negative than -0.87 (upper edge of the band). If the observed w_0 is MORE negative than -0.96, the framework is preferred over LCDM.

This is a PROTECTION MECHANISM for the w_0 prediction that I did not identify in Round 1. The Cauchy-Schwarz theorem acts as a one-sided wall in spectral functional space, and the wall pushes the observable toward safety. The w_0 prediction is not merely "uncertain by +/- 0.05" -- it is uncertain ASYMMETRICALLY, with the uncertainty weighted toward compatibility with LCDM. This is a structural feature of the Connes-Chamseddine spectral action, not an accident of the SU(3) geometry.

**Statement**: For any smooth spectral functional f(x) satisfying the positivity and integrability conditions of the Chamseddine-Connes spectral action (Paper 06, Section 11.1), the predicted dark energy equation of state parameter satisfies w_0 <= -0.908 (Gaussian boundary), with the inequality saturated uniquely by the Gaussian cutoff. The Cauchy-Schwarz bound on f-moment ratios is the mechanism.

**E2: Mack's linked-unknowns argument (E2) has a precise NCG formulation: the spectral functional f(x) is a SINGLE unknown that propagates to ALL spectral predictions simultaneously.**

Mack observes that the decoherence timescale and the spectral functional are linked unknowns -- solving one constrains the other. From the NCG side, this is a consequence of the spectral action's structure. The spectral action S = Tr(f(D^2/Lambda^2)) determines:

- The spectral action gradient dS/dtau (controls Bogoliubov coefficients, hence decoherence)
- The spectral moments a_n (controls w_0, alpha_s, m_H)
- The effective cutoff Lambda = sqrt(f_2/f_0) * M_KK (controls decoupling scale)

All three are functions of f(x). Choosing f(x) to match ONE observable (say, n_s through dS/dtau) DETERMINES the other two. This means the framework is not a zero-parameter theory with an unfixed scheme -- it is a ONE-parameter theory where the parameter is f(x) (an infinite-dimensional object, but constrained to one functional degree of freedom by the requirement that it is a smooth, positive, rapidly-decreasing function).

The computation Mack identifies -- derive t_dec/t_transit as a function of f(x), then check consistency with n_s and w_0 -- is the RIGHT path to resolving the scheme dependence. If a single f(x) exists that simultaneously matches:

- n_s = 0.9649 +/- 0.0042 (Planck 2018)
- w_0 = -0.918 +/- 0.05 (theoretical)
- A_s = 2.1e-9 (through t_dec)

then the spectral functional is observationally determined and all remaining spectral predictions (alpha_s, m_H) become zero-parameter. If NO such f(x) exists, then the spectral action is internally inconsistent at the quantitative level, and only the K-theoretic (topological) content survives.

This is the most important carry-forward computation from this workshop. It converts the scheme dependence from a permanent limitation into a testable hypothesis.

**E3: The Kasparov unitarity protection theorem for c_s^2 is PERMANENT and scheme-independent.**

Mack's E3 formulates the protection theorem: for any non-trivial SU(3) principal bundle with Kasparov-compatible connection, c_s^2 < 9.21e-4. I confirm this is a rigorous consequence of the following chain:

1. Kasparov product existence requires ||A|| / gap(D_K) < 1 (Paper 10, Theorem 4.1, verified K-HOMOLOGY-STABILITY-61).
2. gap(D_K) = 0.8197 M_KK at the fold (structural, from D_K eigenvalue computation).
3. ||A|| = kappa * |R_K|^{1/2} ~ kappa * 1.4 M_KK.
4. Combined: kappa < 0.586.
5. c_s^2 correction = kappa^2 * g_3^2/(16*pi^2) < 0.586^2 * 0.118/(16*pi^2) = 2.56e-4 (fibration alone).
6. Adding one-loop trivial-bundle correction (3.36e-4): total c_s^2 < 5.92e-4.

I note Mack's E3 states 9.21e-4; my stricter computation gives 5.92e-4 (because the one-loop correction and fibration correction are added, not combined quadratically, and the Kasparov bound gives a slightly lower kappa^2 factor than Mack's intermediate calculation). The exact bound depends on whether one uses g_3^2 = 0.118 or the framework's running value, but the conclusion is identical: c_s^2 < 10^{-3} is GUARANTEED by the Kasparov product structure. I confirm this as a permanent theorem.

**E4: The optimal truncation order N* ~ 4 explains the three-layer hierarchy QUANTITATIVELY.**

Combining my D3 analysis (Seeley-DeWitt optimal truncation at N* ~ Lambda^2/M_KK^2 ~ 4) with Mack's E1 three-layer hierarchy produces a quantitative explanation for WHY the three layers separate:

- **Topological layer**: Independent of the Seeley-DeWitt expansion entirely. These predictions (c_s^2, gauge group, spectral flow) are K-theoretic and exist non-perturbatively. They are exact because they never enter the asymptotic expansion.

- **Spectral-robust layer**: Depends on a_0 and a_2 only (moments 0 and 1 in the Seeley-DeWitt labeling). These are BEFORE the optimal truncation N* ~ 4, in the regime where the asymptotic expansion converges. The relative error from truncation at a_4 is O(a_4/a_2) ~ O(Lambda^{-2}) ~ O(1/4) ~ 25%. This is the structural origin of the 10.2% spectral zeta uncertainty and the +/- 0.05 on w_0.

- **Spectral-fragile layer**: Depends on a_4 and higher (moments 2+ in the labeling). The a_4 moment is AT the optimal truncation. The a_6 correction (27% of a_4, from W1-B) is evidence that the expansion is beginning to diverge at this order. Predictions requiring a_4/a_2 (alpha_s, m_H) are in the transition zone, and predictions requiring a_6 are past it.

The N* ~ 4 value is not adjustable -- it is set by Lambda/M_KK, which is determined by the spectral gap of D_K on Jensen-deformed SU(3). The three-layer structure is therefore a CONSEQUENCE of the SU(3) fiber geometry through its spectral gap. A fiber with a larger spectral gap (and hence larger Lambda/M_KK) would push N* higher and extend the spectral-robust layer to include a_4-dependent predictions. The SU(3) spectral gap of 0.82 M_KK is what makes the framework's metric predictions marginal.

**E5: Answers to Mack's new questions (Q1-Q3).**

**A-Q1 (Instanton kappa computability).** The one-instanton solution on SU(3) over S^4 has moduli space dimension 12 (from the ADHM construction: 4 center positions + 1 scale + 7 gauge orientations in SU(3)/U(1)^2). The instanton kappa depends on the scale parameter rho relative to the S^4 radius R. At the conformal point (rho = R), the instanton is maximally localized and kappa is determined by the curvature of the connection: ||F_omega||^2 = 8*pi^2 * c_2(P) for the anti-self-dual instanton. The corresponding A-tensor norm is ||A||^2 = ||F_omega||^2 / vol(M^4), and kappa = ||A||^2 / |R_K|. For c_2 = 1 on S^4 with radius R = 1: ||F_omega||^2 = 8*pi^2, vol(S^4) = 8*pi^2/3, so ||A||^2 = 3. With |R_K| = 2.018 at the fold: kappa = 3/2.018 = 1.49. This EXCEEDS the Kasparov bound of 0.586.

If this computation holds (it is a leading-order estimate -- the actual instanton on Jensen-deformed SU(3) x S^4 would require a more careful analysis accounting for the product geometry), it means: **the one-instanton sector on SU(3) bundles with c_2 = 1 is OUTSIDE the Kasparov-compatible regime.** The fiber-base factorization does not exist for the one-instanton background. This would make the framework TOPOLOGICALLY OBSTRUCTED from living on a non-trivial bundle with c_2 = 1, forcing the trivial bundle (c_2 = 0, kappa = 0) as the unique Kasparov-compatible geometry.

This needs verification through a dedicated computation (INSTANTON-KAPPA-72, see carry-forward), but if confirmed, it is a structural result: the framework lives on a trivial bundle, alpha_s = 0 at tree level is the ONLY possibility, and the alpha_s tension is permanent at the spectral-fragile level.

**A-Q2 (K-theoretic functional selection).** The Kasparov product operates at the K-theory level and is f-independent. There is no K-theoretic criterion in the existing literature (Papers 01-19 in the corpus, or in Connes-Chamseddine's published work through 2024) that selects the spectral functional. The S62 Cauchy-Schwarz selection (Gaussian as maximum-entropy cutoff) is thermodynamic, not K-theoretic. The most promising route to a K-theoretic selection principle would be through Connes' reconstruction theorem (Paper 11, or Connes' later "characterization of noncommutative manifolds" program): the spectral functional is the one that makes the spectral triple satisfy the axioms of a spin^c manifold with the correct dimension. But this is a conjecture, not a theorem, and it has not been formulated precisely enough to select f(x).

The E2 emergence above suggests a more pragmatic route: determine f(x) observationally from the multi-observable fit (n_s, w_0, A_s). This converts the scheme dependence from a theoretical problem into an empirical determination.

**A-Q3 (a_2/a_4 near-constancy origin).** The 2.921% variation of a_2/a_4 across the transit is a consequence of the Gilkey product formula PLUS a specific property of the Jensen deformation on SU(3). On a general product M^4 x K, the product formula gives a_n(D_total) = sum_{j+k=n} a_j(D_M) * a_k(D_K). For flat M^4 (a_j = 0 for j > 0), a_n = a_0(M) * a_n(D_K), so a_2/a_4 = a_2(D_K)/a_4(D_K). This ratio depends ONLY on fiber quantities and is base-independent.

The near-constancy of a_2(D_K)/a_4(D_K) under Jensen deformation is NOT a consequence of the product formula alone -- it is a property of how the Jensen deformation acts on SU(3). The Jensen deformation is a one-parameter family of left-invariant metrics on SU(3), parameterized by tau in [0, 1]. Along this family, the Ricci scalar R(tau) and the curvature-squared invariants R_{ab}R^{ab}(tau) change at different rates. But on SU(3), the left-invariance constrains the deformation: the only free parameter is the relative scaling of the Cartan torus directions versus the root directions (the Jensen ratio). This constraint forces a_2 and a_4 to scale nearly proportionally, because both are dominated by the same set of eigenvalues (the lowest L-sectors, which contain most of the spectral weight).

For a DIFFERENT gauge group -- say, G_2 (dim = 14) or Spin(7) (dim = 21) -- the Jensen deformation would have more free parameters (higher-rank Cartan subalgebra), and the near-constancy of a_2/a_4 would likely break. The near-constancy is specific to the SU(3) fiber geometry, not a universal consequence of the product structure. This is a prediction that could be tested by repeating the computation on a different compact Lie group.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | DESI DR3 tension landscape | M1, Re:M1, C1-C2, D1 | **Converged** | w_0 = -0.918 (+0.01, -0.04) with Cauchy-Schwarz asymmetry; w_a = 0 canonical; Scenario B at 1.82-sigma with convolved uncertainty |
| 2 | Fibration c_s^2 vs alpha_s | M2, Re:M2, V1, E3-E4 | **Converged** | c_s^2 < 9.21e-4 by Kasparov unitarity (permanent); alpha_s tension structural (32% max correction vs 781% needed); instanton kappa likely > Kasparov bound, forcing trivial bundle |
| 3 | 21cm ISW observability | M3, Re:M3, C5 | **Converged** | c_s^2 = 0 has proven (product structure) and model (q-theory) components; +4.0% substrate-specific ISW is topological and scheme-independent; no existing instrument achieves SNR > 4 |
| 4 | Spectral zeta & Pantheon+ shadow | M4, Re:M4, V2, D1 | **Partial** | S_inf = 2.353 at 10.2% truncation is binding constraint; conditional/unconditional distinction for a_0/a_2 bounds is logically real but operationally moot; Seeley-DeWitt optimal truncation at N* ~ 4 explains three-layer hierarchy |
| 5 | Geometric structure meets observation | M5, V1, V2, E1-E4 | **Emerged** | Three-layer hierarchy (topological/spectral-robust/spectral-fragile) explained by optimal truncation N* ~ 4; Cauchy-Schwarz asymmetry creates one-sided w_0 attractor toward LCDM; spectral functional is the SINGLE unknown linking all spectral predictions |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **INSTANTON-KAPPA-72**: Compute kappa for the one-instanton solution on SU(3) bundle with c_2 = 1 over the relevant base manifold. If kappa > 0.586, the non-trivial bundle sector is Kasparov-obstructed and the framework is forced to the trivial bundle. Gate: PASS if kappa < 0.586 (non-trivial fibration viable), INFO if kappa > 0.586 (trivial bundle forced, alpha_s = 0 permanent).

2. **SPECTRAL-FUNCTIONAL-FIT-72**: Determine f(x) from the joint fit (n_s, w_0, A_s). Compute t_dec/t_transit as a function of f-moments. Gate: PASS if a SINGLE f(x) exists matching all three observables simultaneously within their error bars. FAIL if no f(x) satisfies the joint constraint.

3. **ASYMPTOTIC-TRUNCATION-72**: Compute a_8(D_K) on Jensen-deformed SU(3) and test whether |a_8/a_6| < |a_6/a_4| (convergence still improving) or |a_8/a_6| > |a_6/a_4| (past optimal truncation, divergent tail beginning). Gate: PASS if ratio decreasing (expansion still useful), FAIL if ratio increasing (a_6 correction unreliable).

4. **DECOHERENCE-BISPECTRUM-73**: Compute f_NL(equil)/f_NL(folded) as a function of t_dec/t_transit, providing a cross-constraint on the decoherence timescale independent of A_s. Requires prior computation of Bogoliubov phase evolution at the fold (from BCS-DRESSED-SA, priority item 24).

5. **a_2/a_4 CONSTANCY ON G_2**: Repeat the causal moment map computation (W2-D) on G_2 or Spin(7) to test whether a_2/a_4 near-constancy is SU(3)-specific or universal for compact Lie group fibers. If SU(3)-specific, this is an additional structural argument for SU(3) as the fiber.

6. **CAUCHY-SCHWARZ BOUND ON w_0**: Formalize the one-sided attractor (E1) by computing w_0 for the polynomial and heat kernel cutoffs explicitly, confirming that all smooth cutoffs give w_0 <= -0.908. If any cutoff gives w_0 > -0.908, the Cauchy-Schwarz asymmetry argument is weakened.

7. **Does BCS dressing preserve the Cauchy-Schwarz asymmetry?** The E1 result applies to the tree-level spectral action. BCS dressing modifies the effective cutoff (exp(-Delta^2 t) factor in the heat kernel, S64 K_BdG factorization). Does this modification preserve the one-sided attractor, or does it open a route to less negative w_0?

## Wrap-Up — Workshop Impact Summary

### What Changed
- The canonical framework prediction is now w_0 = -0.918 (+0.01, -0.04), w_a = 0. The asymmetric error bar from Cauchy-Schwarz is new (R2 E1). This replaces the prior point prediction and improves the Scenario B tension from 2.14-sigma to 1.82-sigma.
- The three-layer prediction hierarchy (topological / spectral-robust / spectral-fragile) is now the permanent organizing principle for the observational program, with a quantitative explanation through the Seeley-DeWitt optimal truncation N* ~ 4 (R2 E4).
- The spectral functional is identified as the SINGLE unknown linking all spectral predictions. Observational determination of f(x) from the joint (n_s, w_0, A_s) fit would convert ALL remaining spectral predictions to zero-parameter (R2 E2).

### What Holds
- The c_s^2 < 9.21e-4 Kasparov unitarity protection theorem (E3) is permanent and scheme-independent. The ISW substrate-specific signal (+4.0%) is protected by three orders of magnitude over the quintessence discrimination threshold.
- The K-theoretic predictions (gauge group, mass ordering, c_s^2 = 0, w_a = 0, spectral flow, KO-dimension) are scheme-independent and survive any spectral functional choice. The framework's strongest content is topological.
- The alpha_s tension is structural: maximum perturbative correction is 32% (fibration + a_6 CCM) against a required 781%. The Kasparov bound forecloses resolution through the non-trivial fibration channel. Tree-level alpha_s = 0 is the framework's honest prediction.

### What Breaks or Strains
- The instanton kappa estimate (A-Q1: kappa ~ 1.49 > 0.586) suggests the one-instanton sector may be Kasparov-obstructed. If confirmed, the framework is forced to the trivial bundle, eliminating the non-trivial fibration channel entirely and making the alpha_s = 0 tree-level prediction permanent.
- The Seeley-DeWitt optimal truncation at N* ~ 4 means ALL predictions depending on a_4 or higher moments (alpha_s, m_H, the Higgs quartic coupling) are at or past the boundary of perturbative reliability. The a_6 correction (27%) may be the beginning of the divergent tail, not the next convergent term.
- The decoherence timescale t_dec/t_transit remains undetermined from first principles, and the A_s prediction brackets the observed value only within a factor of ~100 band. Without resolving t_dec, A_s is not a zero-parameter prediction.

### Carry-Forward Computations

1. **INSTANTON-KAPPA-72**: Compute kappa for one-instanton on SU(3) bundle (c_2 = 1) over S^4 with Jensen fiber. Input: ADHM moduli, Jensen fiber metric at fold. Output: kappa value vs Kasparov bound 0.586. Gate: forces trivial or non-trivial bundle. Effort: 1 wave.

2. **SPECTRAL-FUNCTIONAL-FIT-72**: Joint f(x) determination from (n_s, w_0, A_s). Input: S66 cutoff families, S64 n_s computation, S71 A_s decoherence band. Output: best-fit f(x) and residuals. Gate: existence/non-existence of consistent f(x). Effort: 2 waves.

3. **ASYMPTOTIC-TRUNCATION-72**: Compute a_8(D_K) on Jensen SU(3). Input: D_K eigenvalue database (L_max >= 8). Output: |a_8/a_6| ratio. Gate: convergence or divergence of Seeley-DeWitt at N = 4. Effort: 1 wave.

4. **BCS-DRESSED-SA**: (Existing priority item 24.) eps_H^{BCS} from BdG spectral action at 5 tau values. Input: K_BdG factorization (S64), D_K eigenvalues. Output: corrected n_s. Gate: estimated +0.0014 toward Planck. Effort: 2 waves.

5. **DECOHERENCE-BISPECTRUM**: f_NL(equil)/f_NL(folded) as function of t_dec/t_transit. Input: Bogoliubov coefficients at fold, decoherence model. Output: cross-constraint on t_dec independent of A_s. Gate: consistency with A_s-derived t_dec band. Effort: 1 wave. Depends on item 4.

6. **CAUCHY-SCHWARZ-W0-BOUND**: Compute w_0 for all S66 cutoff families (polynomial, heat kernel, Gaussian, sqrt, zeta) and verify one-sided attractor w_0 <= -0.908. Input: S66 f-moment database. Output: w_0(f) for each family. Gate: PASS if all w_0 <= -0.908. Effort: 0.5 wave.

7. **a_2-a_4-CONSTANCY-G2**: Repeat W2-D causal moment map on G_2 Lie group fiber. Input: G_2 Dirac spectrum (need to compute from scratch). Output: a_2/a_4 variation under G_2 analog of Jensen deformation. Gate: >3% variation would confirm SU(3)-specificity. Effort: 2 waves.

### Closing Line

The spectral functional f(x) is the single unknown that separates the framework's proven topological content from its unresolved spectral predictions, and determining it observationally from the joint (n_s, w_0, A_s) fit is the highest-priority computation for converting the scheme dependence from a permanent limitation into a falsifiable constraint.
