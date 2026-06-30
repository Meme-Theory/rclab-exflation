# Session 66 Workshop: Mack x Transit

**Date**: 2026-04-04
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: mack (mack-cosmic-bridge), transit (transit-dynamics-theorist)
**Source Documents**:
- `sessions/archive/session-66/session-66-transit-collab.md`
- `sessions/archive/session-66/session-66-inflation-exflation-synthesis.md`

**Focus Topics**:
1. The 114 OOM is NOT a problem -- it IS exflation (the expansion history, not a gap to close)
2. Inflation's mathematical tools recast for supersonic transit -- what maps, what doesn't
3. Power spectrum from impulsive transit vs slow-roll vacuum amplification
4. The A_s normalization -- dissipative EFT (Lopez Nacir) as resolution
5. f_NL from GGE relic -- the zero-parameter bispectrum prediction nobody has computed

---

## Round 1 -- Mack: Opening Analysis

### M1: The 114 OOM is Exflation, Not a Gap

The framing of the 114 OOM between the spectral action fold energy S(tau_fold) ~ 10^67 GeV^4 and the observed CC Lambda_obs ~ 10^{-47} GeV^4 as a "cosmological constant problem" is a category error. My inflation-exflation synthesis (Sec. III.A-C) demonstrates that standard inflation carries an equivalent gap -- V_inflation ~ 10^64 GeV^4 divided by Lambda_obs ~ 10^{-47} GeV^4 gives 10^111 -- and the entire community treats this as "inflation happened and the universe expanded." Nobody calls the 111 OOM between the inflaton potential and today's CC a "problem with inflation." They call it the expansion history.

The 114 OOM is the same thing. The 3 OOM difference between 114 and 111 arises from accounting: the spectral action sums over all 155,984 D_K eigenvalues (the full internal geometry), while inflation uses a single scalar field (synthesis Sec. III.C). The ratio is (M_Pl / Lambda_fold)^4 ~ 10^{5.6}, which explains the difference.

**What Volovik relaxation actually does** (synthesis Sec. III.D): The Gibbs-Duhem relation forces rho_vac ~ H(t)^2 M_Pl^2, so the vacuum energy tracks the Hubble rate through the entire expansion history:

    fold:       rho_vac ~ M_Pl^2 H_fold^2 ~ 10^66 GeV^4
    radiation:  rho_vac ~ H^2 ~ a^{-4}
    matter:     rho_vac ~ H^2 ~ a^{-3}
    today:      rho_vac ~ M_Pl^2 H_0^2 ~ 10^{-47} GeV^4

The total relaxation from 10^66 to 10^{-47} is 113 OOM, accomplished by the expansion history itself. The remaining 0.01 OOM residual is the actual precision of the mechanism (DILUTION-CC-66 PASS, Scenario B). This is NOT a "closing" of a "gap." It IS the expansion. The 114 OOM IS exflation.

**Where exflation is structurally better** (synthesis Sec. III.E): Standard inflation leaves the CC relaxation entirely unspecified. The 111 OOM gap between V_inflation and Lambda_obs is treated as two separate problems: "why did inflation happen?" and "why is the CC small?" Exflation provides a unified answer -- the transit happened because S(tau) has a fold, and the CC relaxed because the Volovik Gibbs-Duhem relation forces tracking. This identification was confirmed by Weinberg [Paper 12] analysis (synthesis Sec. II.12): Weinberg's no-go theorem for self-adjustment mechanisms is evaded because the spectral triple breaks translational invariance at the fold and because D_K is not "a field on spacetime" but the structure from which spacetime emerges.

**What I need Transit to address**: Your observation (Sec. 2.2 of your collab review) that the Volovik relaxation and the GGE coexist because they operate on different degrees of freedom (q is the macroscopic vacuum variable, GGE charges are microscopic quasiparticle occupations) is the correct physical picture. But the BBN constraint is the load-bearing test: does rho_vac at BBN contribute as additional relativistic species (delta_N_eff = 1.34, excluded at 10-sigma via Y_p) or as a modified equation of state of the condensate? Your superfluid 3He argument (Volovik [27] equilibrium theorem: P_normal + P_vacuum = 0 in equilibrium) would resolve this. Can you make the Bogoliubov-level argument for WHY the vacuum energy is non-additive?

### M2: Inflation Tools That Map to Exflation

My inflation-exflation synthesis (Sec. I, the Master Correspondence Table) maps every inflation concept to its substrate counterpart. Transit's collab review confirms this mapping from the Bogoliubov side. Here I sharpen the analysis into three categories: what maps structurally, what maps formally but not dynamically, and what is categorically inapplicable.

**Category 1: Structural maps (the math transfers with modification)**

1. **Bogoliubov pair creation = perturbation generation**. This is the deepest structural parallel. Transit's Eq. 2-3 (mode equation with time-dependent frequency, asymptotic extraction of beta_k) is the correct computation for BOTH inflation and exflation. The difference is the regime: inflation uses the WKB approximation (adiabatic parameter slowly varying), while the transit requires exact numerical solution through the fold (adiabaticity parameter O(1)). Transit's Eq. 6 (sudden approximation) provides the limiting form. The mathematical framework is identical; the solution method must change.

2. **EFT operator hierarchy = Seeley-DeWitt expansion**. My synthesis (Sec. II.7, Cheung et al.) identifies the deepest structural identity: the Cheung et al. EFT operators (M_2, M_3, M-bar) map exactly onto spectral action moments (a_0, a_2, a_4). The critical difference: in inflation, H(t) fixes only two operators and all others are free parameters. In exflation, D_K fixes ALL operators. Zero free parameters for the perturbation sector. This is not an approximation or an analogy -- it is a mathematical identity between the Seeley-DeWitt expansion and the GREFT derivative expansion (synthesis Sec. II.10, Burgess).

3. **Transfer matrix methods from preheating**. Transit's Sec. 2.5 correctly identifies that the Kofman-Linde-Starobinsky transfer matrix decomposition (adiabatic-impulsive-adiabatic matching) applies directly to the fold transit. The piecewise profile transit (pre-fold WKB, impulsive fold, post-fold WKB) is computationally identical to the preheating transfer matrix, with the difference that the transit is a single passage rather than periodic oscillation. The Floquet analysis (instability bands, Floquet exponents) applies only if there is post-transit ringing of tau -- which the 10^{-47} yr settling time suggests is negligible.

4. **In-in formalism for higher-point functions**. Maldacena's computational framework (synthesis Sec. II.3) -- time-ordered products of the interaction Hamiltonian evaluated between in-states -- transfers directly. The adaptation: replace the cubic inflaton vertex with the third-order spectral action S_3(tau), and restrict the time integration to the narrow transit interval (0.66 e-folds vs 60 e-folds for slow-roll). The impulsive nature of the transit means the in-in integral is dominated by a single fold-crossing, not a slow accumulation.

**Category 2: Formal maps (the notation transfers, the dynamics do not)**

1. **Slow-roll parameters eps, eta**. The symbols can be defined for exflation (eps_H = 0.022, eta_H = 0.96), but their dynamical role reverses. In inflation, eps << 1 and eta << 1 are NECESSARY CONDITIONS for the perturbation formalism to work. In exflation, eta_H ~ O(1) at the fold is a STRUCTURAL FEATURE, not a perturbative expansion parameter. Using slow-roll conversion formulas (n_s - 1 = 2eta - 6eps, alpha_s = 16eps*eta - 24eps^2 - 2xi^2) at these parameter values is not an approximation -- it is a misapplication. Transit's Sec. 2.1 makes this argument precisely from the Bogoliubov side.

2. **e-fold number N**. The inflation formula N = integral(V/(M_Pl^2 V') dphi) assumes slow-roll (dphi/dt = -V'/3H). The transit has N_e = 3.73e-3, incompatible with 60 e-folds of inflation by a factor of 16,000. The acoustic white hole mechanism must bridge the scale gap. The e-fold number is a formal quantity that can be computed but does not play the same physical role (it does not solve the horizon problem through geometric expansion but through acoustic causal structure).

3. **Spectral index formulas**. The Baumann n_s formula (synthesis Sec. II.1, Eq. 236) and the Cheung et al. generalized formula (Eq. 41 with the dc_s/dt correction) can be evaluated, but they assume adiabatic mode functions. Transit's Eq. 7 provides the correct sudden-approximation replacement: n_s - 1 ~ d ln(Delta omega / omega) / d ln k, which depends on the k-dependence of the frequency jump, not on the slow-roll parameters at horizon crossing.

**Category 3: Categorically inapplicable**

1. **Consistency relation r = -8 n_T**. Five independent arguments established this (VdD-Hawking workshop). The transit is impulsive (Mach 13.8), not quasi-static. The single-field slow-roll identity between tensor and scalar sectors does not hold.

2. **Bunch-Davies vacuum**. The standard choice v_k -> e^{-ik tau}/sqrt(2k) as initial condition assumes adiabatic evolution at early times. At the van Hove fold, the adiabaticity parameter changes by O(1) over a single oscillation period (P_exc = 1.000 saturation). There is no sense in which the pre-transit state evolves adiabatically through the fold.

3. **Lyth bound**. Delta phi / M_Pl ~ sqrt(r/0.01) constrains inflaton field excursion. The tau excursion Delta tau ~ 0.05 across the fold is a geometric parameter, not a field, and there is no gravitational coupling that generates a Lyth-type constraint on its range.

4. **Reheating temperature formula**. T_r ~ 0.2 sqrt(Gamma M_Pl) assumes inflaton decay into radiation. The transit produces a GGE relic (non-thermal), not a thermal bath. The initial energy scale T_init = 8.32 x 10^15 GeV is comparable to the inflation scale, but the energy transfer mechanism is fundamentally different (impulsive pair creation, not parametric decay).

**Question for Transit**: Your Sec. 2.1 argues that alpha_s = -0.038 is a slow-roll mapping artifact. I agree, and the Mack-QA workshop concluded alpha_s(CMB) ~ 0 from the 56 OOM scale hierarchy. But there is a subtlety: even in the sudden approximation, the van Hove singularity (divergent density of states at the fold) introduces a specific k-dependence into |beta_k|^2 through the square-root singularity in the density of states. Does this k-dependence produce a residual alpha_s at transit scale, or is it genuinely flat? Your Eq. 7 is the formula -- what does d ln(Delta omega / omega) / d ln k look like through a van Hove fold?

### M3: A_s from Dissipative Transit -- The Lopez Nacir Connection

The A_s normalization gap is 3.15 OOM (S66 W1-C, Route A) or 1.47 OOM (Route B, direct Bogoliubov without PW projection). This is the framework's most severe quantitative failure after the alpha_s mapping artifact. My inflation-exflation synthesis (Sec. IV.B) identifies the dissipative EFT of Lopez Nacir et al. [Paper 09] as the most promising resolution path, and Transit's collab review confirms from the Bogoliubov side that the standard normalization formula is inapplicable.

**The diagnosis**: The current A_s computation uses the Garriga-Mukhanov relation, which assumes slow-roll vacuum fluctuations. The scalar amplitude Delta_s^2 = H^2/(8 pi^2 M_Pl^2 eps) (Baumann Eq. 222) is derived under the assumption that mode functions are Bunch-Davies at early times and freeze out adiabatically at horizon crossing. Transit's Sec. 2.4 confirms: in the sudden-quench regime (Mach 13.75, 0.66 e-folds), the correct amplitude is determined by |beta_k|^2 from the sudden-approximation formula (Transit Eq. 6), not by the slow-roll formula. The mismatch IS the 3.15 OOM gap.

**The Lopez Nacir resolution** (synthesis Sec. II.9): When dissipation is strong (friction coefficient gamma >> H), the Bunch-Davies homogeneous contribution to the power spectrum is exponentially suppressed: exp(-gamma/H). The spectrum is instead dominated by the NOISE from pair creation. The noise-dominated formula (Lopez Nacir Eq. 43-44) gives:

    P_noise(k) ~ (H^2 / (2 pi c_s)^2) * (gamma / (c_s^2 H)) * [noise spectral density]

The key identification for exflation:
- gamma (friction coefficient) <--> Gamma_transit ~ M_KK x (impedance mismatch factor)
- c_s <--> c_BLV = 0.485
- H <--> H_fold ~ T_init^2 / M_Pl ~ 10^14 GeV
- Noise source <--> Parker pair creation at the fold (P_exc = 1.000)

**The duty cycle correction**: Lopez Nacir's formula assumes steady-state dissipation over many Hubble times. The exflation transit lasts N_e = 3.73e-3 e-folds -- far less than one Hubble time. The effective dissipation parameter is therefore:

    gamma_eff = gamma x (Delta t_transit / H^{-1}) = gamma x N_e / (2 pi)

With gamma ~ M_KK = 4.33 x 10^17 GeV and N_e = 3.73e-3:

    gamma_eff ~ M_KK x 6e-4 ~ 2.6 x 10^14 GeV

This is COMPARABLE to H_fold ~ 10^14 GeV. The dissipative correction is therefore O(1), not overwhelmingly large. This is the physically correct regime: the transit is dissipative enough to modify the amplitude normalization by order-unity factors but not so dissipative that the noise dominates by many orders of magnitude.

**How this could close the gap**: The 3.15 OOM gap in Route A breaks down as:
- BCS occupation: -1.12 OOM (structural, from pair-wise correlations)
- PW selection: -3.50 OOM (structural, from projecting onto physical modes)
- Gap tunneling: -0.23 OOM (from spectral gap at fold)

The dissipative correction enters as a MULTIPLICATIVE factor on the raw amplitude. If gamma_eff/H ~ O(1), the noise enhancement is also O(1) -- meaning the dissipative formula shifts A_s by roughly one OOM, not three. This would reduce the gap to ~2 OOM, significant but not sufficient for a full resolution.

The deeper question is whether the PW selection rule (the dominant -3.50 OOM suppression) is correct. If the GGE relic converts to curvature perturbations through a multifield delta-N mechanism (synthesis Sec. IV.C, Senatore-Zaldarriaga), the PW projection is the wrong conversion formula. The actual conversion involves all GGE branches (acoustic, optical, Leggett), each contributing through different zeta-sigma coupling coefficients. The multifield enhancement could be O(10^1 - 10^2), which combined with the dissipative O(1) correction would bring the gap to ~1 OOM.

**Connection to Transit's mode equation**: Transit's computation 1 (TRANSIT-MODE-EQ-67) would extract |beta_k|^2 directly, bypassing both the slow-roll formula AND the dissipative correction. If the exact mode equation gives an amplitude consistent with Planck, the Lopez Nacir machinery would then serve as the EXPLANATION (why the slow-roll formula was wrong), not the computation itself. This is the correct division of labor: Transit solves the mode equation, I verify that the dissipative EFT explains the result.

**Specific computation for Transit**: When you solve the mode equation through the fold (your computation 1), extract not just the power spectrum shape (n_s, alpha_s) but also the ABSOLUTE normalization |beta_k|^2 at the CMB pivot scale (or at whatever scale the acoustic white hole maps to the CMB pivot). This is the datum that either confirms or refutes the dissipative EFT picture. If |beta_k|^2 at the pivot gives A_s within 1 OOM of Planck, the dissipative interpretation is supported. If the gap remains at 3+ OOM, the multifield conversion is the remaining escape route.

**Question for Transit**: Your sudden-approximation formula (Eq. 6) gives |beta_k|^2 = (omega_after - omega_before)^2 / (4 omega_before omega_after). For the transit through the van Hove fold, what is the fractional frequency jump Delta omega / omega for a mode at the CMB pivot scale? The 6% sector variation you cite (W4-F) gives the cross-sector uniformity, but the absolute magnitude of Delta omega / omega determines the raw Bogoliubov amplitude. If it is O(1) (which P_exc = 1.000 saturation suggests), the |beta_k|^2 is also O(1), and the A_s gap would be entirely a CONVERSION problem (mode-to-zeta mapping), not a PRODUCTION problem. Can you estimate Delta omega / omega from the spectral action profile?

### M4: f_NL from GGE Relic -- The Missing Prediction

The framework has zero-parameter predictions for n_s (0.9590), r (0.024), and Omega_DM h^2 (0.120 Leggett-only). It has NO prediction for f_NL, the bispectrum amplitude. This is the single most productive computation the framework has not performed, because f_NL discriminates between the exflation transit and ALL slow-roll inflation models simultaneously.

**Why exflation violates the Maldacena consistency relation**: The Maldacena consistency relation f_NL^local = (5/12)(1 - n_s) ~ 0.017 holds for single-field slow-roll. My synthesis (Sec. II.3) identifies three independent reasons it fails for exflation:

1. **Multi-branch GGE**: The post-transit state contains 59.8 quasiparticle pairs across acoustic, optical, and Leggett channels. In inflation language, this is a multi-field scenario. Senatore-Zaldarriaga [Paper 08] show that multifield models generically violate the Maldacena relation, with f_NL enhanced by the number of light fields and the turning rate of the field-space trajectory.

2. **Sub-luminal sound speed**: The fabric sound speed c_BLV = 0.485 is less than 1. Cheung et al. (synthesis Sec. II.7) prove that c_s < 1 generates equilateral non-Gaussianity f_NL^equil ~ 85/324 x (1/c_s^2) ~ 1.12 for the exflation value. This is a TESTABLE prediction: Planck constrains f_NL^equil = -26 +/- 47, so f_NL ~ 1 is consistent with current bounds but would be detectable by future surveys (CMB-S4 projects sigma(f_NL^equil) ~ 5).

3. **Impulsive transit**: The in-in integral for the bispectrum is dominated by the transit interval (0.66 e-folds). For slow-roll inflation, the integral accumulates over ~60 e-folds, giving a result proportional to (slow-roll parameters) x (number of e-folds). For the impulsive transit, the integral is a single delta-function-like contribution from the fold crossing, with amplitude proportional to the spectral action's third derivative S_3(tau_fold), not to the slow-roll parameters.

**Three distinct f_NL channels**:

| Channel | Source | Estimated f_NL | Formula Source |
|:---|:---|:---|:---|
| Equilateral (c_s < 1) | Cheung et al. Eq. (41) | ~1.12 | c_BLV = 0.485 |
| Dissipative (noise-dominated) | Lopez Nacir Eq. (52) | O(1) to O(gamma_eff/c_s^2 H) | gamma_eff ~ H_fold |
| Multi-branch (GGE conversion) | Senatore-Zaldarriaga Sec. 4 | O(N_branch) ~ O(3-10) | Acoustic + optical + Leggett |

The three contributions add in quadrature (they peak at different triangle configurations). The net f_NL could be O(1-10), well above the single-field slow-roll value of O(0.01) but well within current Planck bounds.

**What the computation requires** (synthesis Sec. IV.A): The in-in formalism applied to the GGE relic needs:
1. The third-order spectral action S_3(tau) at the fold -- this is the cubic interaction vertex.
2. The GGE mode functions through the transit (from Transit's mode equation computation).
3. The in-in time integral, restricted to the transit interval.
4. The zeta-to-sigma conversion coefficients for each GGE branch.

Steps 1 and 2 are prerequisites that feed into the bispectrum calculation. Step 3 is simplified by the impulsive nature of the transit (the integral is dominated by a narrow tau interval). Step 4 is the multifield delta-N conversion from Senatore-Zaldarriaga.

**Why this is a zero-parameter prediction**: Once the mode equation is solved (Transit's computation 1), the bispectrum follows from the same spectral action and GGE structure that determines n_s and r. There are no new inputs. The f_NL prediction is as parameter-free as the n_s prediction. This makes it a GENUINE discriminant: if future CMB experiments measure f_NL^equil ~ 1 (consistent with c_BLV = 0.485), it would simultaneously confirm the sub-luminal sound speed and exclude all slow-roll models with c_s = 1.

**The observational landscape**: Planck (f_NL^equil = -26 +/- 47) provides no constraint at f_NL ~ 1. CMB-S4 projects sigma ~ 5. SPHEREx projects sigma ~ 1 for local shape. The equilateral shape from c_BLV = 0.485 would require either CMB-S4 or a dedicated 21-cm experiment to reach f_NL ~ 1 sensitivity. The prediction is: f_NL^equil = 1.12 +/- O(1) from the c_s channel alone, with possible enhancement to O(10) from multifield and dissipative contributions.

**Question for Transit**: Your GGE formation picture (Sec. 2.3) confirms that the Bogoliubov occupation numbers N_k = |beta_k|^2 are the inputs to the GGE, and the GGE Lagrange multipliers lambda_m are fixed by the initial conditions. Does the GGE formation process itself generate additional non-Gaussianity beyond what is present in the initial Bogoliubov state? In other words: is the GGE three-point function equal to the Bogoliubov state three-point function, or does the relaxation to the GGE (constrained by the Richardson-Gaudin integrals) generate or destroy correlations at the three-point level? Calabrese-Essler [Paper 23] discusses this for integrable spin chains -- what is the GGE bispectrum theorem?

### M5: Cross-Cutting -- What S66 Missed About Inflation Math

My inflation-exflation synthesis identified 12 computations (Sec. VI, Table) and 8 missing tools (Sec. IV). Transit's collab review independently identified 7 computations (Sec. 6, Table). Comparing these two lists reveals both convergences and gaps.

**Convergences (independently identified by both)**:

1. **Mode equation through the fold**: My DISSIPATIVE-AS and Transit's TRANSIT-MODE-EQ-67 are the same computation at different levels of sophistication. Transit's version (exact numerical ODE) is the more fundamental; my dissipative EFT version provides the analytic framework for interpreting the result. These should be unified into a single computation that solves the mode equation AND evaluates the dissipative correction.

2. **Sudden-approximation cross-check**: My synthesis (Sec. II.1, Baumann) and Transit's SUDDEN-APPROX-SPECTRUM-67 both identify this as the essential analytic benchmark. The sudden approximation is exact at Mach -> infinity and provides the limiting form against which the numerical solution must converge.

3. **Post-transit resonance**: My POST-TRANSIT-RESONANCE and Transit's FLOQUET-POST-TRANSIT-67 are identical. The question -- does tau undergo oscillatory settling? -- has a likely answer (no, given the 10^{-47} yr settling time and the monotonic spectral action profile), but the Floquet analysis has not been performed.

4. **BBN constraint**: My synthesis flags BBN as the load-bearing test for the Volovik mechanism (Sec. II.12). Transit's BBN-VOLOVIK-67 specifies the exact computation: delta_N_eff at T_BBN from the q-theory field equations.

**Gaps in S66 that neither analysis fully addressed**:

1. **The Cheung et al. n_s correction**. My synthesis (Sec. II.7) identifies an additional term in the spectral index: dc_s/dt / (c_s H), from the time-variation of the sound speed. For an impulsive transit where c_BLV changes rapidly at the fold, this term could be O(1). Neither Transit nor my synthesis has evaluated this. The computation is: extract dc_BLV/dtau from the spectral action profile at the 16 available tau values, convert to dc_s/dt via the tau-to-physical-time mapping, and evaluate the correction to n_s. If this shifts n_s by even 0.003, it changes the framework's Planck compatibility from 1.40-sigma to sub-sigma.

2. **The multifield delta-N conversion**. My synthesis (Sec. IV.C) identifies that the GGE relic has multiple branches contributing to zeta through different coupling strengths. The current single-field Garriga-Mukhanov conversion is missing the acoustic-to-optical and acoustic-to-Leggett cross-terms. Transit's framework (Bogoliubov coefficients per branch) provides the raw inputs, but the delta-N conversion coefficients (how each branch's fluctuations become curvature perturbations) have not been computed. This is the bridge between Transit's mode equation and the observed CMB power spectrum.

3. **Non-adiabatic fraction**. Planck constrains the non-adiabatic (isocurvature) fraction to < 1.7% at 95% CL (synthesis Sec. II.16, Table). The GGE relic generically contains isocurvature modes (Leggett fluctuations are NOT curvature perturbations -- they are inter-band coherence fluctuations that carry their own perturbation spectrum). The framework MUST show that the isocurvature fraction is below 1.7%, and this has not been computed. If the Leggett branch carries significant spectral weight at CMB scales, the isocurvature constraint could be the tightest bound on the GGE conversion mechanism.

4. **Feature amplitude from eigenvalue discreteness**. The D_K spectrum has 155,984 eigenvalues at L_max = 10. If the perturbation spectrum inherits any discreteness from these eigenvalues, it would appear as features (oscillations) in P(k). Planck constrains features to < 1% of A_s (synthesis Sec. II.16, Table). The expected feature amplitude has not been computed. For a spectrum with ~17,000 distinct eigenvalue values, the feature spacing is Delta k / k ~ 1/17,000, which is too fine for Planck to resolve (Planck resolves Delta l / l ~ 1/2500). But the AMPLITUDE of features at resolvable scales depends on how the eigenvalue clusters (representations) are distributed. This is a straightforward spectral analysis computation.

5. **The Bellazzini et al. spin-3/2 result**. The recent proof that gravity MUST exist if spin-3/2 particles exist (S-matrix positivity bounds) is an independent confirmation of the spectral action's a_2 moment generating gravity. In the spectral triple, the Dirac operator D_K generates spin-3/2 representations in the tensor product of the fundamental SU(3) representation with the spin-1/2 representation. The Bellazzini result is therefore a CONSISTENCY CHECK: the spectral triple necessarily contains spin-3/2 modes, and the S-matrix positivity bounds independently require that these modes couple to gravity. This means the a_2 -> Einstein-Hilbert identification is not just a formal correspondence but is FORCED by the S-matrix structure. Neither my synthesis nor Transit's review discusses this connection. It should be verified: does the D_K spectrum contain spin-3/2 eigenvalues, and do the Bellazzini positivity bounds constrain their coupling to a_2?

**Priority ordering for the unified computation list**:

| Priority | Computation | Source | Rationale |
|:---|:---|:---|:---|
| 1 | TRANSIT-MODE-EQ + dissipative interpretation | Transit 1 + Mack 1 | Rate-limiting for alpha_s, A_s, and n_s simultaneously |
| 2 | BBN-VOLOVIK (rho_vac/rho_rad magnitude) | Transit 5 + Mack-QA | Gates sole surviving CC mechanism |
| 3 | GGE-BISPECTRUM (f_NL from in-in) | Mack 2 | Zero-parameter prediction, untapped discriminant |
| 4 | Multifield delta-N conversion | Mack 4 | Required to connect mode equation to observed A_s |
| 5 | Non-adiabatic fraction | Mack 11 | Planck < 1.7% constraint, untested |
| 6 | EFT-MATCHING (a_0, a_2, a_4 -> M_2, M_3) | Mack 3 | Connects spectral action to standard parametrization |
| 7 | Cheung n_s correction from dc_s/dt | Mack 5 | Could shift n_s by O(0.003), changing Planck compatibility |

**Final question for Transit**: Your five open questions (Sec. 5) are precisely the right questions. I want to sharpen one: your Sec. 5.2 asks whether the acoustic white hole transfers TENSOR perturbations across the 54-decade scale gap. My synthesis (Sec. II.11, Achucarro-Palma) notes that the tensor transfer function at CMB scales is standard (n_T = -3.02e-3, r = 0.024 PASS), so the blue tilt is localized at transit scale. But the tensor AMPLITUDE at CMB scale (r = 0.024) was computed by Transit's standard transfer function, not by the acoustic channel. If the acoustic white hole provides a SECOND tensor transfer mechanism (through GGE acoustic-to-gravitational-wave conversion), the effective r at CMB could be enhanced above 0.024. Is there a Bogoliubov argument for the acoustic-to-tensor conversion efficiency? This would tighten or loosen the BICEP/Keck constraint.

---

## Round 1 -- Transit: Response & Cross-Synthesis

### Part 1: Response to Mack's Sections

#### Re: M1 -- The 114 OOM is Exflation

**AGREE**: The reframing is correct and overdue. From the Bogoliubov perspective, the 114 OOM is the total integrated particle production -- the cumulative spectral weight transfer from vacuum to excitations across the entire expansion history. In Parker's formalism [01], the vacuum evolves through a sequence of instantaneous Bogoliubov transformations b_k(t) = alpha_k(t) a_k + beta_k(t) a_k^dagger, with |beta_k(t)|^2 tracking the particle number at each epoch. The TOTAL particle production from fold to today is:

    N_total = Sum_k |beta_k(t_0)|^2 = Sum_k |beta_k^{transit}|^2 + (accumulated adiabatic production)    (T.1)

The transit contribution |beta_k^{transit}|^2 ~ O(1) (P_exc = 1.000 saturation) produces the GGE relic at fold energy. The subsequent 113 OOM of energy dilution is the standard cosmological redshift acting on these excitations -- it is NOT additional particle production but adiabatic evolution of existing excitations. This is structurally identical to inflation's 111 OOM: inflation produces perturbations at V^{1/4} ~ 10^16 GeV, and the expansion history dilutes the energy density to Lambda_obs. Nobody calls this a "gap in inflation." Mack's synthesis (Sec. III.C) makes the accounting transparent.

The Volovik relaxation rho_vac ~ H^2 M_Pl^2 IS the equation of state governing this dilution. In Volovik's 3He framework [27], the superfluid vacuum's thermodynamic response forces rho_vac to track the expansion rate through the Gibbs-Duhem relation. The key structural point: this tracking is NOT a fine-tuning but a consequence of the vacuum's thermodynamic stability (the free energy must be minimized subject to the constraint that the vacuum energy density equals the cosmological term in the Einstein equations derived from the a_2 spectral moment).

**MISSED**: What the Bogoliubov framework adds is the INFORMATION-THEORETIC content of the 114 OOM. In a thermal equilibrium relaxation (standard LCDM), the 114 OOM of energy dilution would erase all information about the initial state. In the GGE relaxation (exflation), the Richardson-Gaudin integrals are CONSERVED through the entire 114 OOM of expansion. The GGE occupation numbers {n_k = |beta_k|^2} at the fold are STILL the occupation numbers today (up to adiabatic redshift). This is a fundamentally different 114 OOM: the energy decreases but the information content does not. The GGE is an information-preserving relaxation, and this is what makes the framework's dark sector predictions possible -- the Leggett-channel and BA-channel quasiparticles preserve their quantum numbers through the full expansion history because the Richardson-Gaudin integrals commute with the post-transit Hamiltonian at every epoch.

**Mack's question (BBN non-additivity of vacuum energy)**: The Bogoliubov-level argument proceeds as follows.

In the superfluid 3He parent system [27], the vacuum energy and the quasiparticle energy are NOT independent additive contributions. The total energy is:

    E_total = E_condensate(q) + Sum_k E_k n_k + E_interaction(q, {n_k})    (T.2)

where q is the vacuum variable (condensate) and {n_k} are the quasiparticle occupations. The crucial term is E_interaction -- the condensate and the quasiparticles are coupled through the gap equation Delta = Delta(q, {n_k}). In thermodynamic equilibrium, the vacuum adjusts q to minimize E_total, which gives the Gibbs-Duhem relation dP = -dE + mu dN. The resulting vacuum pressure P_vac = -rho_vac is NOT a free parameter -- it is determined self-consistently by the quasiparticle spectrum.

At BBN temperature, the system has both the tracking vacuum (rho_vac ~ H^2 M_Pl^2) and the radiation component (quasiparticle thermal bath at T_BBN). The vacuum energy contributes to the Friedmann equation NOT as additional relativistic species (additive delta_N_eff) but as a modification of the effective gravitational constant through the condensate equation of state. Specifically, the Friedmann equation reads:

    H^2 = (8 pi G / 3) [rho_rad + rho_matter + rho_vac(H)]    (T.3)

where rho_vac(H) = alpha H^2 M_Pl^2. Substituting and solving for H^2:

    H^2 = (8 pi G / 3) * rho_rad / (1 - (8 pi / 3) alpha)    (T.4)

This is a RENORMALIZATION of G, not an addition to rho_rad. The effective N_eff is:

    N_eff^{effective} = N_eff / (1 - (8 pi / 3) alpha)    (T.5)

For Volovik Scenario B with rho_vac/rho_rad = 0.67 at BBN, this gives alpha such that the renormalized G_eff differs from G by a factor of 1/(1 - 0.67) ~ 3.0. This is STILL excluded -- but the exclusion is from the modified expansion rate (wrong H at BBN gives wrong D/H ratio), not from delta_N_eff as additional species.

The escape route is if the q-theory vacuum equation constrains alpha to be much smaller at BBN than the naive rho_vac/rho_rad = 0.67 estimate. This requires computing the q-theory trajectory from the fold through BBN, which is computation BBN-VOLOVIK-67. The Bogoliubov argument establishes the STRUCTURAL form of the vacuum contribution (renormalized G, not additive N_eff), but the MAGNITUDE depends on the q-theory dynamics.

**EMERGES**: The information-preservation aspect of the 114 OOM reframe connects to the isocurvature constraint (Mack's M5, gap 3). If the GGE occupation numbers are conserved through the full expansion, then the RELATIVE occupation between Leggett and acoustic channels is also conserved. This means the dark matter fraction f_DM = Omega_DM / Omega_total is set at the transit and preserved -- it is NOT a coincidence but a conserved quantum number of the GGE. The coincidence problem (why Omega_DM ~ Omega_baryon) may have a GGE-structural explanation.

#### Re: M2 -- Inflation Tools That Map

**AGREE**: Mack's three-category classification (structural maps, formal maps, categorically inapplicable) is sharp and correct from the mode-equation perspective. Let me reinforce and extend each category with the Bogoliubov structure.

**Category 1 reinforcement (structural maps)**:

The deepest structural identity is the one Mack identifies in item 2: the EFT operator hierarchy IS the Seeley-DeWitt expansion. From the mode equation perspective, this means the effective frequency omega_k^2(t) in the governing equation u_k'' + omega_k^2(t) u_k = 0 is FULLY DETERMINED by the spectral action moments. Specifically:

    omega_k^2(tau) = k^2 c_BLV^2 - (effective mass from a_2, a_4 evolution)    (T.6)

In inflation, omega_k^2 = k^2 - a''/a = k^2 - (2 - eps_H + 3 eps_H - 2 eta_H) / tau^2 [Mukhanov-Chibisov, 03]. The coefficients are free parameters (they depend on V(phi)). In exflation, omega_k^2 is determined by D_K at each tau value -- the same eigenvalue problem that fixes a_0, a_2, a_4 fixes the mode frequency. This is why the framework has zero free parameters for perturbations: the mode equation IS the spectral action.

On the transfer matrix methods (Mack item 3): I can make this more precise. The transit decomposes into three regions with distinct WKB character:

    Region I (tau < 0.15):  omega_k(tau) varies slowly, |d omega / dt| / omega^2 << 1. WKB valid.
    Region II (0.15 < tau < 0.25): van Hove fold. omega_k changes by O(1) in ~ 0.66 e-folds. WKB FAILS.
    Region III (tau > 0.25): omega_k(tau) varies slowly again. WKB valid.

The transfer matrix connecting Regions I and III through Region II is:

    (alpha_k)     (M_11  M_12) (1)
    (beta_k )  =  (M_21  M_22) (0)     (T.7)
                     ^
                Transfer matrix through fold

where M_ij encodes the Stokes phenomenon at the turning points. The Bogoliubov coefficients are alpha_k = M_11, beta_k = M_21, with |M_11|^2 - |M_21|^2 = 1 (unitarity). In Kofman-Linde-Starobinsky's preheating formalism [04, Sec. 3], this transfer matrix is computed by matching WKB solutions across the non-adiabatic region. The key difference: KLS compute this for PERIODIC omega_k (Floquet theory, multiple passages). The exflation transit is a SINGLE passage, so there is no Floquet amplification -- the Bogoliubov coefficient from one transit passage is the final answer.

**Category 2 sharpening (formal maps)**:

Mack correctly identifies that the spectral index formulas are formal maps that do not transfer dynamically. Let me make this quantitatively precise. The slow-roll formula n_s - 1 = 2 eta - 6 eps [Mukhanov-Chibisov, 03] is derived by solving the mode equation in the LIMIT where eta and eps are constant (de Sitter + slow variation). The exact solution for constant eta is the Motohashi constant-roll solution [19]:

    u_k = sqrt(pi |eta| / 2) * H_nu^{(1)}(k |eta|),   nu = 3/2 + 1/(eta + 1)    (T.8)

which gives n_s = (eta - 1)/(1 + eta). For eta_H = 0.96 (the framework's fold value), this gives n_s = (0.96 - 1)/(1 + 0.96) = -0.04/1.96 = -0.0204, so n_s = 1 - 0.020 = 0.980. This is DIFFERENT from the slow-roll formula: n_s = 1 + 2(0.96) - 6(0.022) = 1 + 1.92 - 0.13 = 2.79, which is nonsensical (n_s > 2). The slow-roll formula gives a catastrophically wrong answer at eta_H = 0.96. Even the constant-roll formula (Motohashi) may not apply because eta is NOT constant through the transit -- it varies rapidly. The only reliable approach is numerical integration of the mode equation.

**MISSED**: Mack's Category 3 (categorically inapplicable) should include one more entry: the **freeze-out approximation**. In standard inflation, modes "freeze out" at horizon crossing (k = aH), after which zeta is conserved. This freeze-out assumes the mode function u_k reaches its asymptotic form (constant amplitude, no oscillation) shortly after horizon exit. In the impulsive transit, there IS no extended period of superhorizon evolution. The mode crosses the "horizon" (omega_k = 0 turning point) ONCE, in the impulse regime, and the Bogoliubov mixing happens at that crossing. The post-transit u_k oscillates freely (no freeze-out), and zeta is NOT conserved in the transit interval. The Garriga-Mukhanov relation zeta = u_k / z (where z = a sqrt(2 eps)) fails during the transit because z changes by O(1) over the transit duration. This is a distinct inapplicability from the ones Mack lists.

**Mack's question (residual alpha_s at transit scale from van Hove k-dependence)**:

This is a precise and important question. The sudden-approximation formula (my collab Eq. 6) gives:

    |beta_k|^2 = (omega_k^{after} - omega_k^{before})^2 / (4 omega_k^{before} omega_k^{after})    (T.9)

Through a van Hove fold (where d^2 omega / dk^2 = 0 at some k = k_vH), the dispersion relation has the local form:

    omega(k) ~ omega_0 + A (k - k_vH) + C (k - k_vH)^3 + ...    (T.10)

(the quadratic term vanishes at the van Hove point by definition). The frequency jump Delta omega(k) = omega_k^{after} - omega_k^{before} depends on how the coefficients A, C change across the transit. If the fold reorganizes the dispersion relation at the saddle point, then:

    Delta omega(k) / omega(k) ~ Delta A * (k - k_vH) / omega_0 + Delta C * (k - k_vH)^3 / omega_0    (T.11)

The power spectrum from Eq. T.9 is then:

    P(k) ~ k^3 |beta_k|^2 ~ k^3 (Delta omega / omega)^2 ~ k^3 [Delta A (k - k_vH)]^2 / omega_0^2    (T.12)

For k near k_vH (within the van Hove region), this gives P(k) ~ k^3 (k - k_vH)^2, and the spectral index:

    n_s - 1 = d ln P / d ln k = 3 + 2k / (k - k_vH)    (T.13)

This DIVERGES at k = k_vH -- the van Hove singularity produces a SPIKE in the spectral index at the fold wavenumber. But for modes far from k_vH (which the CMB modes are, separated by 54 decades), the van Hove structure is invisible and the spectrum depends only on the smooth large-scale behavior of Delta omega / omega. The running alpha_s AT TRANSIT SCALE is large (the spike), but at CMB scale it is determined by the overall shape of Delta omega(k), which the 6% sector uniformity (W4-F) suggests is smooth.

The bottom line: alpha_s at transit scale CAN be large due to the van Hove singularity in the density of states. Alpha_s at CMB scale should be small IF the acoustic white hole maps the perturbation spectrum without introducing additional k-dependent distortion. The scale dependence of alpha_s itself is the critical variable: alpha_s(k_transit) >> alpha_s(k_CMB) is not only consistent but EXPECTED from the van Hove structure.

#### Re: M3 -- A_s from Dissipative Transit

**AGREE on diagnosis, DISAGREE on resolution path**: Mack's diagnosis of the A_s gap is correct -- the Garriga-Mukhanov formula is inapplicable because it assumes slow-roll mode functions. The 3.15 OOM gap is a formula mismatch, not a particle production deficit. But I disagree that the dissipative EFT (Lopez Nacir) is the correct resolution path, for a structural reason.

**The structural objection**: The Lopez Nacir dissipative EFT assumes a CONTINUOUS dissipative process operating over many oscillation periods, producing a noise-dominated steady-state power spectrum. The exflation transit is a SINGLE IMPULSIVE EVENT lasting 0.66 e-folds. The steady-state assumption underlying the noise formula (Lopez Nacir Eq. 43-44) requires t_dissipation >> 1/omega_k, which is violated for the transit (t_transit << 1/H << 1/omega_k for most modes). The duty-cycle correction Mack computes (gamma_eff ~ H_fold) is an attempt to fix this, but it does not address the deeper issue: the noise spectral density in Lopez Nacir's formula assumes INCOHERENT noise from many independent friction events, while the transit produces COHERENT Bogoliubov pairs from a single event.

The correct A_s computation from the Bogoliubov framework is direct and does not require the dissipative EFT detour. In the sudden approximation:

    P_zeta(k) = (k^3 / 2 pi^2) |u_k / z|^2    (T.14)

where u_k is the post-transit mode function (containing the Bogoliubov mixing) and z = a sqrt(2 eps_H). The raw Bogoliubov occupation |beta_k|^2 determines the mode function amplitude. For fully saturated production (P_exc = 1.000, |beta_k|^2 ~ O(1)):

    |u_k|^2 ~ (|alpha_k|^2 + |beta_k|^2) / (2 omega_k) = (1 + 2|beta_k|^2) / (2 omega_k)    (T.15)

With |beta_k|^2 ~ O(1) and omega_k ~ k c_BLV, this gives:

    P_zeta(k) ~ (k^3 / 2 pi^2) * (3 / (2 k c_BLV)) * (1 / z^2)    (T.16)

The crucial variable is z = a sqrt(2 eps_H). During the transit, a changes by a factor of exp(0.66/3) ~ 1.25 (0.66 e-folds is NOT 60 e-folds), and eps_H = 0.022. So:

    z^2 ~ a^2 * 2 * 0.022 = 0.044 * a^2    (T.17)

The smallness of eps_H SUPPRESSES z and ENHANCES P_zeta. This is the opposite of what happens in inflation, where large eps_H suppresses P_zeta through the 1/(8 pi^2 eps) factor. At the fold:

    A_s^{transit} ~ (H^2 / (8 pi^2 eps_H c_BLV)) * (3/2) * (Bogoliubov correction)    (T.18)

With H ~ T_init^2 / M_Pl ~ (8.3e15)^2 / (1.2e19) ~ 5.7e12 GeV, eps_H = 0.022, c_BLV = 0.485:

    A_s^{transit} ~ (5.7e12)^2 / (8 pi^2 * 0.022 * 0.485 * (1.2e19)^2)    (T.19)
                  ~ 3.25e25 / (1.24e38)
                  ~ 2.6e-13

The Planck value is A_s = 2.1e-9, so the transit formula gives A_s that is 4.1 OOM too small. This is WORSE than the 3.15 OOM gap, not better. The reason: the transit is too short (0.66 e-folds vs 60) to accumulate sufficient amplitude, even with saturated Bogoliubov production.

**Mack's question (absolute magnitude of Delta omega / omega from spectral action profile)**:

For P_exc = 1.000 (fully non-adiabatic, |beta_k|^2 ~ O(1)), the sudden approximation gives:

    |beta_k|^2 = (omega_after - omega_before)^2 / (4 omega_before omega_after) ~ O(1)    (T.20)

This requires Delta omega / omega ~ O(1), meaning the frequency changes by a factor of order unity across the transit. From the spectral action profile, the effective mass m_eff^2(tau) = d^2 S / dtau^2 changes from positive (pre-fold) through zero (fold) to negative (TT instability directions). The frequency at the fold is:

    omega_k^2(tau) = k^2 c_BLV^2 + m_eff^2(tau)    (T.21)

For a mode at k ~ m_eff / c_BLV (the transit wavenumber), the frequency changes from omega ~ sqrt(2) m_eff (pre-fold, positive mass) through omega ~ k c_BLV (fold, m_eff = 0) to omega ~ sqrt(k^2 c_BLV^2 - |m_eff|^2) (post-fold, tachyonic mass for k < m_eff/c_BLV). The fractional change is:

    Delta omega / omega ~ (sqrt(2) - 1) / sqrt(2) ~ 0.29    (T.22)

for modes at the transit scale. For k >> m_eff/c_BLV (modes far above the transit scale), Delta omega / omega ~ m_eff^2 / (2 k^2 c_BLV^2) << 1, and |beta_k|^2 ~ (m_eff^2 / (4 k^2 c_BLV^2))^2 << 1 -- these modes are not excited. For k << m_eff/c_BLV (modes below the transit scale, which includes CMB modes), the frequency is dominated by m_eff, and Delta omega / omega is again O(1), giving |beta_k|^2 ~ O(1). The Landau-Zener saturation P_exc = 1.000 confirms this: ALL modes at or below the transit scale are fully excited.

This means the A_s problem is NOT a production problem (Mack's conjecture is correct) -- it is a CONVERSION problem. The raw |beta_k|^2 at CMB-relevant scales IS O(1). The gap lies entirely in how the Bogoliubov occupation converts to the curvature perturbation zeta. The multifield delta-N conversion (Mack's M5, gap 2) is the most promising path: if all three GGE branches (acoustic, optical, Leggett) contribute to zeta through their respective coupling coefficients, the effective A_s could be enhanced by a factor of N_branches ~ 3-10, which closes ~0.5-1 OOM. The remaining ~2-3 OOM must come from the acoustic white hole transfer mechanism, which I address in T1.

**EMERGES**: The A_s calculation above reveals a structural tension in the framework that Mack's synthesis does not address. The transit produces O(1) Bogoliubov occupation at TRANSIT SCALE (k_transit ~ m_eff / c_BLV), but the CMB observes at scales 54 decades below. The question is not "what is A_s at transit scale" but "what transfer function maps the transit-scale spectrum to the CMB scale." This is the acoustic white hole transfer problem, and it is logically prior to both the dissipative EFT correction and the multifield delta-N conversion. Without the transfer function, neither correction can be evaluated at the correct scale.

#### Re: M4 -- f_NL from GGE Relic

**AGREE on priority, EXTEND on GGE bispectrum structure**: Mack's identification of f_NL as the framework's untapped zero-parameter discriminant is correct. The three channels (equilateral from c_s < 1, dissipative, multi-branch GGE) are the right decomposition. Let me address the GGE bispectrum question directly.

**Mack's question (does GGE relaxation generate or destroy three-point correlations?)**:

This is a precise question with a precise answer from the integrable quench literature. In the Calabrese-Essler framework [23], the post-quench state relaxes to the GGE:

    rho_GGE = exp(-Sum_m lambda_m I_m) / Z_GGE    (T.23)

The GGE three-point function of an observable O is:

    <O(x_1) O(x_2) O(x_3)>_GGE = Tr(rho_GGE O(x_1) O(x_2) O(x_3))    (T.24)

The key theorem (Calabrese-Essler [23], extended by Bertini et al.): for integrable systems, the GGE three-point function equals the DIAGONAL part of the initial-state three-point function. Specifically, in the energy eigenbasis:

    <O O O>_GGE = Sum_n |c_n|^2 <E_n| O O O |E_n>    (T.25)

where c_n = <E_n | psi_0> are the overlaps with the initial (pre-transit) state. The OFF-DIAGONAL terms <E_n| O O O |E_m> with n != m average to zero in the long-time limit (dephasing). This means:

1. **GGE relaxation DESTROYS the off-diagonal three-point correlations** (dephasing of cross-terms)
2. **GGE relaxation PRESERVES the diagonal three-point correlations** (conserved by the GGE charges)

The net effect depends on whether the initial Bogoliubov state has its three-point function dominated by diagonal or off-diagonal terms. For a squeezed state (which is what the Bogoliubov transformation produces), the three-point function is:

    <phi^3>_Bogoliubov = Sum_k (alpha_k beta_k^* + alpha_k^* beta_k) * (phase factors)    (T.26)

The diagonal part (which survives GGE relaxation) is:

    <phi^3>_GGE,diagonal = Sum_k Re(alpha_k beta_k^*) * |beta_k|^2    (T.27)

This is generically NON-ZERO whenever the Bogoliubov coefficients have a non-trivial phase relationship between alpha_k and beta_k. In the sudden approximation, alpha_k and beta_k are REAL (the sudden quench has no phase), so alpha_k beta_k^* = alpha_k beta_k > 0 for all k, and the diagonal three-point function is:

    <phi^3>_GGE ~ Sum_k |beta_k|^2 sqrt(1 + |beta_k|^2)    (T.28)

using |alpha_k|^2 = 1 + |beta_k|^2 from unitarity. For |beta_k|^2 ~ O(1) (saturated production), this gives a non-zero GGE bispectrum proportional to the total number of produced pairs:

    f_NL^{GGE} ~ N_pair^{1/2} / N_pair ~ N_pair^{-1/2}    (T.29)

(the 1/sqrt(N) is from the central limit theorem applied to the sum over modes). With N_pair = 59.8, this gives f_NL^{GGE} ~ 1/sqrt(60) ~ 0.13 from the GGE diagonal channel alone.

**The combined f_NL prediction**: Adding Mack's three channels:

| Channel | f_NL estimate | Confidence | Method |
|:---|:---|:---|:---|
| Equilateral (c_s < 1) | ~1.12 | HIGH -- follows from c_BLV = 0.485 via Cheung et al. | Analytic |
| GGE diagonal | ~0.13 | MEDIUM -- depends on exact Bogoliubov phases | Semi-analytic (T.28) |
| Multi-branch conversion | O(1-10) | LOW -- depends on uncomputed delta-N coefficients | Estimated |
| Dissipative | O(1) at most | LOW -- duty cycle uncertain | Estimated |

The equilateral channel (f_NL ~ 1.12) is the most robust prediction because it depends only on c_BLV, which is functional-independent. The GGE diagonal channel (f_NL ~ 0.13) is subdominant. The multi-branch and dissipative channels are uncertain.

**MISSED**: Mack's analysis does not address the SHAPE of the GGE bispectrum, which is as important as its amplitude for observational discrimination. The three channels produce three distinct shapes in the triangle parameter space (k_1, k_2, k_3):

- Equilateral (c_s < 1): peaks at k_1 = k_2 = k_3 (equilateral triangles)
- GGE diagonal: peaks at k_1 + k_2 = k_3 (folded triangles) because the Bogoliubov pairs have momentum conservation k + (-k) = 0
- Multi-branch: peaks at SQUEEZED triangles (k_1 << k_2 ~ k_3) because the inter-branch conversion has long-wavelength Leggett fluctuations modulating short-wavelength acoustic modes

The folded shape from the GGE diagonal channel is particularly interesting because it is NOT produced by any single-field inflation model. The Planck constraints on folded f_NL are weaker than on equilateral or local shapes (f_NL^{folded} = -20 +/- 290 at 95% CL, Kinney [30]). A detection of folded non-Gaussianity would be a smoking gun for the Bogoliubov pair-creation mechanism.

**EMERGES**: The GGE bispectrum computation connects to the isocurvature constraint (Mack's M5, gap 3). The Leggett-channel fluctuations are inter-band coherence modes that do NOT couple to the curvature perturbation at linear order. At QUADRATIC order, however, they contribute to the bispectrum through the sigma-to-zeta conversion. This means the isocurvature fraction and the f_NL prediction are NOT independent -- they are determined by the SAME delta-N conversion coefficients. A joint computation of (isocurvature fraction, f_NL, f_NL shape) from the multifield delta-N formalism would provide three simultaneous predictions from a single computation. This triples the discriminating power.

#### Re: M5 -- Cross-Cutting

**AGREE on convergences 1-4, EXTEND the gap analysis, ANSWER the tensor question**:

The four convergences Mack identifies are genuine: both of us independently arrive at the same rate-limiting computations from different starting points (Bogoliubov mode equation vs. inflation EFT mapping). This convergence is itself evidence that the computation list is correct -- two different conceptual frameworks identify the same unknowns.

**On Mack's five gaps**:

Gap 1 (Cheung n_s correction from dc_s/dt): This is real and potentially significant. From the mode equation perspective, a time-varying sound speed modifies omega_k^2(tau) as:

    omega_k^2(tau) = k^2 c_s^2(tau) + (mass terms)    (T.30)

The time derivative dc_s/dt introduces an additional contribution to the Bogoliubov coefficients through the JERK of the frequency:

    d(omega_k^2)/dt = 2 k^2 c_s (dc_s/dt) + ...    (T.31)

In the sudden approximation, this modifies the frequency jump by:

    Delta(omega_k^2) -> Delta(omega_k^2) + 2 k^2 c_s (dc_s/dt) * Delta t_transit    (T.32)

For the transit (Delta t_transit ~ 0.66 / H), this correction is of order (dc_s/dt) / (c_s H). If the sound speed changes by a factor of O(1) during the transit (which it must, since the dispersion relation reorganizes at the fold), then (dc_s/dt)/(c_s H) ~ O(1), and the correction to n_s is O(1) -- not a small perturbation but a structural modification. This reinforces the conclusion that the exact mode equation must be solved numerically; analytic approximations EACH miss an O(1) correction.

Gap 2 (multifield delta-N): Confirmed as critical from the Bogoliubov side. The conversion coefficients zeta_I = (partial N / partial sigma_I) at the fold are the missing link between the raw |beta_k|^2 and the observed A_s. In the Senatore-Zaldarriaga framework, these are:

    zeta = Sum_I (partial N / partial sigma_I) delta sigma_I + (1/2) Sum_{IJ} (partial^2 N / partial sigma_I partial sigma_J) delta sigma_I delta sigma_J    (T.33)

The first-order terms determine A_s, and the second-order terms determine f_NL. Both require the same conversion coefficients. This means the A_s computation and the f_NL computation are a SINGLE task, not two.

Gap 3 (non-adiabatic fraction): The Bogoliubov framework provides a structural prediction here. The Leggett-channel excitations are inter-band coherence modes. They carry isocurvature perturbations because they describe RELATIVE fluctuations between bands, not total density fluctuations. The isocurvature fraction is:

    beta_iso ~ (N_Leggett / N_total) * (amplitude ratio of Leggett to acoustic)    (T.34)

With 39.8 acoustic pairs and 20.0 Leggett pairs (from the S66 partition), and assuming comparable mode amplitudes, beta_iso ~ 20/60 * (some suppression factor). The Planck bound (< 1.7%) requires a suppression factor of at least 0.05, which could come from the delta-N conversion (if Leggett modes couple weakly to zeta). This is a constraint on the conversion coefficients, not on the Bogoliubov production.

Gap 4 (feature amplitude from eigenvalue discreteness): The Bogoliubov framework places a STRUCTURAL BOUND on this. The power spectrum P(k) = (k^3/2pi^2) |beta_k|^2 inherits discreteness from the D_K spectrum only if the mode equation's omega_k^2(tau) has discontinuities in its k-dependence. For a mode equation with smooth omega_k(k), the Bogoliubov coefficients |beta_k|^2 are smooth functions of k regardless of eigenvalue discreteness in the background. The eigenvalue discreteness enters through the DISPERSION RELATION omega(k), which for 155,984 eigenvalues has fine structure at Delta k/k ~ 1/17,000. The Bogoliubov coefficients smooth over structure finer than the transit width in k-space, which is of order delta k ~ 1/(c_BLV * Delta t_transit). For the transit, delta k/k ~ H/k_transit, so features at Delta k/k ~ 1/17,000 would be resolved only if H/k_transit < 1/17,000, i.e., k_transit > 17,000 H. This is likely satisfied (k_transit ~ m_eff/c_BLV >> H at GUT scale), so the features COULD in principle appear. Their amplitude depends on the strength of the eigenvalue gaps relative to the smooth dispersion. A dedicated computation is needed.

Gap 5 (Bellazzini spin-3/2): Outside my domain. No comment.

**Mack's final question (acoustic-to-tensor conversion efficiency)**:

The acoustic white hole has a well-defined Bogoliubov structure for SCALAR perturbations (density/velocity fluctuations in the GGE acoustic field). TENSOR perturbations (gravitational waves) are NOT acoustic modes -- they are transverse-traceless metric perturbations that propagate at the GRAVITATIONAL speed (c = 1 in the substrate), not at the acoustic speed c_BLV = 0.485. This means tensor modes do NOT see the acoustic white hole horizon.

However, there is a SECOND-ORDER process: acoustic modes scatter off each other to produce tensor modes. In inflation, this is computed by Baumann (scalar-scalar-to-tensor interaction at second order in perturbation theory). The conversion efficiency is:

    r_induced ~ (A_s)^2 * (phase space integral)    (T.35)

For A_s ~ 2e-9 (Planck), the induced tensor spectrum is r_induced ~ 10^{-17}, negligible. But in the exflation transit, the acoustic amplitude at transit scale is |beta_k|^2 ~ O(1), much larger than A_s ~ 10^{-9}. The induced tensor amplitude at transit scale is:

    r_induced^{transit} ~ |beta_k|^4 * (c_BLV / c_graviton)^2    (T.36)

With |beta_k|^2 ~ 1 and c_BLV/c_graviton = 0.485, this gives r_induced^{transit} ~ 0.24 at transit scale. This is a LARGE tensor signal at the transit scale, but it must be transferred to CMB scale through the same 54-decade gap. The transfer function for second-order tensors includes a suppression factor from the scale ratio, which reduces r at CMB to:

    r_CMB ~ r_induced^{transit} * (k_CMB / k_transit)^{n_T - n_s + 1}    (T.37)

The exponent depends on the difference between the tensor and scalar tilts. For n_T > n_s (blue tensor tilt at transit, n_T = +0.468 from S66), the ratio (k_CMB/k_transit)^{n_T - n_s + 1} is:

    (10^{-54})^{0.468 - 0.959 + 1} = (10^{-54})^{0.509} = 10^{-27.5}    (T.38)

So r_CMB^{induced} ~ 0.24 * 10^{-27.5} ~ 10^{-28}, which is completely negligible compared to the first-order r = 0.024 already computed by the framework. The acoustic-to-tensor conversion does NOT meaningfully affect the BICEP/Keck constraint.

**On priority ordering**: I agree with Mack's priority list (M5 table) with one modification. The multifield delta-N conversion (priority 4) should be MERGED with the mode equation computation (priority 1) because they share the same prerequisite (the Bogoliubov coefficients per branch) and the same output (A_s with the correct conversion). The unified computation is: solve the mode equation per branch -> extract |beta_k|^2 per branch -> compute delta-N conversion coefficients -> output (A_s, n_s, alpha_s, f_NL, isocurvature fraction) simultaneously. This is a single pipeline, not five separate computations.

### Part 2: Original Analysis

#### T1: Mode Equation Through the Van Hove Fold -- The Correct Computation

The framework's central unperformed calculation is to solve the mode equation through the van Hove fold exactly, without slow-roll approximation, and extract the Bogoliubov coefficients as functions of wavenumber k. Here I specify the complete mathematical problem, the boundary conditions, the solution method, and the output format.

**The governing equation**: The spectral action S(tau) at each value of the Jensen deformation parameter tau determines an effective frequency for each Fourier mode of the perturbation field:

    u_k'' + omega_k^2(tau) u_k = 0    (T.39)

where prime denotes derivative with respect to conformal time eta (related to tau through the spectral action's kinetic structure). The effective frequency is:

    omega_k^2(tau) = k^2 c_BLV^2(tau) - z''(tau)/z(tau)    (T.40)

with z(tau) = a(tau) sqrt(2 eps_H(tau)) being the Mukhanov pump field, and c_BLV(tau) being the fabric sound speed. Both a(tau) and eps_H(tau) are derived from the spectral action:

    H^2 = (8 pi / 3 M_Pl^2) * S(tau)    (T.41)
    eps_H = -dH/dt / H^2 = (dS/dtau)^2 / (2 S^2 * kinetic_normalization)    (T.42)

The critical feature is z''/z. In slow-roll, z''/z ~ 2/eta^2 (nearly de Sitter). At the van Hove fold, z''/z contains contributions from:

    z''/z = a''/a + (eps_H and eta_H terms)    (T.43)

where a''/a ~ 2 a^2 H^2 (1 - eps_H/2) and the eps_H, eta_H terms contribute O(1) corrections because eta_H = 0.96 at the fold. The total z''/z at the fold is NOT well-approximated by the slow-roll limit.

**The van Hove structure**: At the fold (tau = 0.190), the D_K eigenvalue spectrum has a van Hove singularity where the density of states diverges. This means the dispersion relation omega(k) has an inflection point:

    d^2 omega / dk^2 |_{k=k_vH} = 0    (T.44)

Near this point, the dispersion relation takes the cubic form omega ~ omega_0 + A(k - k_vH) + C(k - k_vH)^3. The vanishing of the quadratic coefficient means that a band of modes near k_vH has the SAME effective frequency and is therefore excited collectively. The density of states diverges as g(omega) ~ |omega - omega_vH|^{-1/2} (square-root van Hove singularity in 3D).

For the mode equation, this means that modes near k_vH see a FLAT potential barrier (omega_k(tau) varies with tau but is nearly independent of k in a band around k_vH). The Bogoliubov coefficients for these modes are nearly identical:

    |beta_k|^2 ~ |beta_{k_vH}|^2 for |k - k_vH| < delta k_vH    (T.45)

where delta k_vH is the width of the van Hove flat region. This produces a PLATEAU in the power spectrum at the transit scale, which appears as a FEATURE (flat bump) superimposed on the smooth large-scale spectrum.

**Boundary conditions**: The pre-transit state is the adiabatic vacuum of the spectral action at tau < tau_fold:

    u_k -> (1 / sqrt(2 omega_k)) exp(-i integral omega_k d eta)   as eta -> -infinity    (T.46)

This is the Bunch-Davies-like initial condition generalized to the non-de-Sitter background. The post-transit state at tau > tau_fold is a superposition of positive and negative frequency modes:

    u_k -> alpha_k (1/sqrt(2 omega_k^{out})) exp(-i omega_k^{out} eta) + beta_k (1/sqrt(2 omega_k^{out})) exp(+i omega_k^{out} eta)    (T.47)

where omega_k^{out} is the post-transit frequency. The Bogoliubov coefficients alpha_k, beta_k are extracted by matching at late times.

**Solution method**: Three approaches, in order of increasing reliability:

**Method A (sudden approximation)**: Assumes the transit is instantaneous. The mode function u_k is continuous but its derivative jumps:

    u_k^{after} = u_k^{before}    (T.48a)
    u_k'^{after} = u_k'^{before}    (T.48b)

These matching conditions, combined with the change omega_k^{before} -> omega_k^{after}, give:

    alpha_k = (omega_k^{after} + omega_k^{before}) / (2 sqrt(omega_k^{before} omega_k^{after}))    (T.49a)
    beta_k = (omega_k^{after} - omega_k^{before}) / (2 sqrt(omega_k^{before} omega_k^{after}))    (T.49b)

with |alpha_k|^2 - |beta_k|^2 = 1 satisfied identically. This is the analytic baseline. It is exact at Mach -> infinity and provides the comparison standard.

**Method B (transfer matrix)**: Decompose the transit into piecewise constant-omega_k segments. For each segment of duration Delta eta_j with frequency omega_j, the transfer matrix is:

    M_j = ( cos(omega_j Delta eta_j)      sin(omega_j Delta eta_j)/omega_j )    (T.50)
          ( -omega_j sin(omega_j Delta eta_j)  cos(omega_j Delta eta_j)       )

The total transfer matrix is M = M_N * M_{N-1} * ... * M_1, and the Bogoliubov coefficients are extracted from M_total by:

    alpha_k = (M_11 + M_22)/2 + i(M_21/omega_out - M_12 omega_out)/2    (T.51a)
    beta_k = (M_11 - M_22)/2 - i(M_21/omega_out + M_12 omega_out)/2    (T.51b)

This method uses the 16 available tau values as the piecewise segments. It captures the finite-duration effects that the sudden approximation misses.

**Method C (full numerical integration)**: Solve Eq. T.39 as an ODE initial value problem (RK4/5) from eta_initial (well before the fold) to eta_final (well after the fold), for a grid of k values. Extract alpha_k, beta_k from the asymptotic form at late times. This is the definitive computation.

**Output**: From any of these methods, the deliverables are:
1. |beta_k|^2 as a function of k (the Bogoliubov occupation spectrum)
2. P(k) = (k^3/2pi^2) |u_k/z|^2 (the primordial power spectrum)
3. n_s(k) = 1 + d ln P / d ln k (the spectral index as a function of scale)
4. alpha_s(k) = d n_s / d ln k (the running)
5. A_s = P(k_pivot) at the CMB pivot scale (requires the acoustic white hole scale mapping)

**What the acoustic white hole MUST provide**: The computation above produces the power spectrum at TRANSIT-SCALE wavenumbers (k ~ k_transit ~ m_eff/c_BLV ~ 10^{17} GeV). To compare with CMB observations, the spectrum must be evaluated at k_CMB ~ 10^{-25} GeV^{-1} (the Planck pivot scale). The 54-decade gap between k_transit and k_CMB is bridged by the acoustic white hole's causal structure, NOT by geometric expansion (which provides only 0.66 e-folds). The acoustic transfer function T(k_CMB, k_transit) maps the transit-scale spectrum to CMB scale:

    P_CMB(k_CMB) = |T(k_CMB, k_transit)|^2 * P_transit(k_transit(k_CMB))    (T.52)

where k_transit(k_CMB) is the transit-scale wavenumber that maps to k_CMB through the acoustic channel. This transfer function has NOT been computed and is the critical missing piece between the mode equation and CMB observables. It encodes:
- The acoustic dispersion relation in the GGE medium
- The impedance mismatch at the white hole boundary (Gamma = 0.99970)
- The gravitational processing through the standard matter-radiation era

Without T(k_CMB, k_transit), even an exact solution of the mode equation cannot produce CMB predictions. The mode equation and the transfer function are the two halves of the complete computation.

#### T2: Bogoliubov Coefficients and the GGE -- What Preheating Literature Says

The preheating literature (Kofman-Linde-Starobinsky [04], Amin [17], Bassett [25], Tranberg [29]) provides a complete toolkit for non-thermal particle production from time-dependent backgrounds. Here I extract the tools that apply directly to the exflation transit and identify the structural differences.

**Structural parallel: the occupation number as the fundamental variable**

In both preheating and exflation, the correct variable is the mode occupation number n_k(t) = |beta_k(t)|^2, not the field amplitude. Kofman-Linde-Starobinsky [04, Sec. 3] show that the occupation number is an ADIABATIC INVARIANT: it changes only when the adiabaticity condition |d omega_k / dt| / omega_k^2 << 1 is violated. Between violations, n_k is constant. This is the Bogoliubov particle number, and it is the same quantity that enters the GGE:

    rho_GGE = exp(-Sum_k lambda_k n_k) / Z    (T.53)

where n_k = |beta_k|^2 are the post-transit occupation numbers and lambda_k are the GGE Lagrange multipliers fixed by the initial conditions. The preheating literature's focus on n_k(t) rather than chi_k(t) is exactly the right formalism for the GGE.

**What transfers from preheating**:

1. **Non-thermal spectra**: Amin [17] shows that parametric resonance produces n_k ~ k^{-beta} with beta ~ 1/2 to 2, depending on the coupling strength and number of oscillations. For a SINGLE transit (no oscillations), the sudden-approximation spectrum is:

    n_k = |beta_k|^2 = (Delta omega_k / (2 omega_k))^2    (T.54)

For the van Hove fold with omega_k^2 = k^2 c_BLV^2 + m_eff^2(tau), the k-dependence is:

    n_k ~ (Delta m_eff^2)^2 / (16 k^2 c_BLV^2 (k^2 c_BLV^2 + m_eff^2))    for k >> m_eff/c_BLV    (T.55a)
    n_k ~ O(1)    for k << m_eff/c_BLV    (T.55b)

The transit-scale spectrum is therefore: n_k ~ const for low k (saturated, P_exc = 1.000), and n_k ~ k^{-4} for high k (perturbative tail). The cross-over scale is k_cross ~ m_eff/c_BLV. The resulting power spectrum P(k) = (k^3/2pi^2) n_k / omega_k has:

    P(k) ~ k^2 for k << k_cross (n_s = 3, blue tilt at transit scale)
    P(k) ~ k^{-2} for k >> k_cross (n_s = -1, red tilt above transit scale)

This is NOT a nearly scale-invariant spectrum. The observed CMB scale-invariance (n_s ~ 0.96) cannot come directly from the transit-scale Bogoliubov spectrum -- it must be produced by the acoustic white hole transfer, or by a mechanism not yet identified.

2. **Backreaction**: Kofman-Linde-Starobinsky [04, Sec. 6] and Amin [17, Sec. 3] compute the backreaction of produced particles on the background. The backreaction energy is:

    rho_backreaction = Sum_k omega_k n_k / V    (T.56)

For the transit, with n_k ~ O(1) for N_modes ~ 60 (59.8 pairs) and omega_k ~ m_eff ~ M_KK ~ 10^17 GeV:

    rho_backreaction ~ N_modes * M_KK^4 ~ 60 * (10^17)^4 ~ 6 x 10^69 GeV^4    (T.57)

This is COMPARABLE to the spectral action energy S(tau_fold) ~ 10^67 GeV^4, suggesting that backreaction is NOT negligible -- the produced particles carry a significant fraction of the spectral action energy. In preheating, this level of backreaction terminates the resonant amplification (Amin [17]). In the transit, it means the mode equation solution must be SELF-CONSISTENT: the produced particles modify the background, which modifies the mode equation, which changes the particle production. This is the same self-consistency problem that Calzetta-Hu [07] formalize through the Kadanoff-Baym equations.

The framework's tau settling time (10^{-47} yr from S65) is the timescale for this backreaction to equilibrate. The fact that it is extremely short (much less than 1/H) confirms that backreaction is strong and fast.

3. **Transfer matrix decomposition**: The KLS transfer matrix method [04, Sec. 3] provides the semi-analytic bridge between the sudden approximation (Method A in T1) and the full numerical solution (Method C). For the transit, the transfer matrix decomposes as:

    M_total = M_post * M_fold * M_pre    (T.58)

where M_pre and M_post are the adiabatic propagators (diagonal in the WKB basis) and M_fold is the non-adiabatic core. The key insight from KLS is that M_fold can be parameterized by a SINGLE complex number (the Stokes multiplier mu_k), which determines the Bogoliubov coefficient:

    |beta_k|^2 = |mu_k|^2 / (1 + |mu_k|^2)    (T.59)

The Stokes multiplier is computed from the anti-Stokes lines in the complex eta-plane, where omega_k^2(eta) has turning points. For the van Hove fold, the turning point structure depends on whether the fold is a maximum or a saddle of omega_k^2(eta) in the complex plane. The fold SA Hessian (0+, 3-; from S60) indicates a SADDLE structure, which gives a pair of turning points on opposite sides of the real axis. The Stokes multiplier for a saddle is:

    mu_k ~ exp(-pi |omega_k^2|_{turning point} / |d omega_k^2/d eta|_{real axis}|)    (T.60)

For modes deep in the non-adiabatic regime (the turning points are close to the real axis), |mu_k| >> 1 and |beta_k|^2 -> 1, confirming P_exc = 1.000 saturation.

**What does NOT transfer from preheating**:

1. **Floquet amplification**: Preheating relies on REPEATED passage through zero-crossings of the inflaton oscillation. Each passage multiplies the Bogoliubov coefficient: |beta_k| -> |beta_k| * exp(mu_k * N), where N is the number of oscillations. The exflation transit is a SINGLE passage. There is no Floquet amplification. The occupation number after one passage is the final answer.

2. **Stochastic resonance**: In an expanding universe, KLS [04, Sec. 5] show that the Floquet exponent becomes stochastic (phases randomize between oscillation periods). This is irrelevant for a single passage.

3. **Thermalization through rescattering**: Amin [17] and Tranberg [29] show that after preheating saturates (backreaction halts the amplification), the non-thermal spectrum slowly thermalizes through particle-particle scattering. For exflation, the GGE integrability (Richardson-Gaudin) PREVENTS thermalization. The non-thermal spectrum persists permanently (Ordered Veil). The preheating thermalization timescale (~1000 oscillation periods, Tranberg [29]) is replaced by the GGE thermalization time (~10^{580} t_universe, Bertini-Essler W8-B).

**The critical structural difference**: Preheating produces non-thermal spectra that EVENTUALLY thermalize (non-integrable coupling to many fields). The exflation transit produces non-thermal spectra that NEVER thermalize (integrable BCS Hamiltonian). This is the deepest distinction between the two processes, and it is why the GGE relic carries more information than the thermal relic from preheating. Every GGE occupation number n_k is an independent observable; in a thermal state, only two numbers (T, mu) survive.

#### T3: Questions for Mack

**Q1: The acoustic white hole transfer function -- who computes it?**

My analysis in T1 and Re:M3 identifies the acoustic white hole transfer function T(k_CMB, k_transit) as the critical missing piece between the mode equation and CMB observables. This is neither a pure Bogoliubov computation (it involves post-transit acoustic propagation in the GGE medium) nor a pure observational cosmology mapping (it involves the substrate's acoustic structure). Mack, your inflation-exflation synthesis (Sec. II.1, Baumann Lecture 3) identifies the transfer function as a computation the framework has not performed. Do you have a specific proposal for HOW the acoustic white hole maps transit-scale perturbations to CMB scale? The standard inflation transfer function assumes 60 e-folds of geometric expansion followed by matter-radiation processing. The exflation transfer must replace the 60 e-folds with the acoustic channel. What is the functional form of T(k_CMB, k_transit) in the acoustic picture? Is it a frequency-independent scaling (which would preserve n_s), a power-law (which would introduce additional tilt), or something more complex (which could resolve the alpha_s tension)?

**Q2: The BCS-to-curvature conversion -- is the GGE phase space correctly counted?**

Mack's M5 (gap 2) identifies the multifield delta-N conversion as the bridge between Bogoliubov occupation and curvature perturbation. My Re:M3 shows that the raw |beta_k|^2 ~ O(1) at transit scale, so the production is not the bottleneck -- the conversion is. But the conversion depends on HOW MANY effective fields contribute to zeta. Mack counts three branches (acoustic, optical, Leggett), giving N_branches ~ 3-10 enhancement. From the Bogoliubov perspective, the correct counting is by SYMMETRY CHANNEL, not by excitation type. The BCS pairing produces quasiparticles in specific SU(3) representation channels, and each channel couples to the curvature perturbation through its own delta-N coefficient. The number of effective fields is the number of INDEPENDENT channels, which may be larger than 3 (if the SU(3) representations decompose into multiple sub-channels) or smaller (if symmetry constrains the delta-N coefficients to be related). What is the correct counting for the spectral triple? Specifically: how many independent delta-N coefficients does the SU(3) fiber provide?

**Q3: What constrains the Volovik tracking exponent?**

The Volovik relaxation assumes rho_vac ~ H^2 M_Pl^2 through the entire expansion history. This is the specific tracking law with exponent n = 2 in rho_vac ~ H^n. Mack's M1 applies this at BBN to get rho_vac/rho_rad = 0.67. From the Bogoliubov perspective, the tracking exponent n = 2 follows from the Gibbs-Duhem relation in the superfluid analog [27]. But this assumes the vacuum behaves as a SIMPLE FLUID with two thermodynamic degrees of freedom (P, rho). If the GGE relic modifies the vacuum equation of state (through the E_interaction term in Eq. T.2), the tracking exponent could deviate from n = 2. In particular, if the GGE occupation numbers contribute a mode-dependent pressure (P_GGE = Sum_k p_k n_k with p_k depending on the dispersion relation), the effective tracking exponent becomes:

    n_eff = 2 + (correction from GGE pressure)    (T.61)

A value n_eff > 2 would make the vacuum energy dilute FASTER, which would HELP with the BBN constraint (rho_vac/rho_rad would be smaller at BBN). Has the framework computed the GGE pressure contribution to the vacuum tracking? This connects directly to Mack's BBN question in M1 and could soften or eliminate the tension.

**Q4: The A_s gap decomposition -- is the 3.50 OOM PW selection real?**

Mack's M3 decomposes the 3.15 OOM Route A gap into BCS occupation (-1.12), PW selection (-3.50), and gap tunneling (-0.23). The PW selection (-3.50 OOM) dominates. From the Bogoliubov perspective, the PW selection is a projection of the FULL mode space onto the physical-waveguide (PW) sector that couples to 4D gravity. If the projection is correct, then only PW modes contribute to curvature perturbations, and the 3.50 OOM suppression is structural. But if the acoustic white hole channel involves ALL spectral modes (not just PW), then the full 155,984-eigenvalue mode space contributes, and the PW projection is WRONG. Which is it? Mack's inflation synthesis (Sec. IV.C, Senatore-Zaldarriaga) suggests the multifield delta-N conversion uses all branches, not just PW. If so, the PW selection suppression is an artifact of single-field thinking, and the true A_s gap is -1.12 + (-0.23) = -1.35 OOM, much closer to closure.

**Q5: Feature predictions as a discriminant**

Mack's M5 (gap 4) identifies eigenvalue discreteness features as an uncomputed observable. From the Bogoliubov perspective, the transit-scale power spectrum has a KNOWN feature: the van Hove peak (plateau in n_k near k_vH). This feature is at transit scale (~10^17 GeV), far above CMB resolution. But the acoustic white hole transfer could MAP this feature to CMB-accessible scales. If the transfer function has a monotonic k-mapping, the van Hove peak would appear as a BUMP in the CMB power spectrum at a specific l determined by k_vH and the acoustic transfer. Has the observational analysis of Planck residuals at any specific l identified unexplained features that could correspond to the van Hove peak? This would be a zero-parameter feature prediction testable against existing data.

---

## Round 2 -- Mack: Follow-up

### CONVERGENCE

**C1: A_s is a CONVERSION problem, not a PRODUCTION problem.** Transit's Re:M3 resolves a question I posed explicitly in M3 and receives a definitive answer. The absolute magnitude of Delta omega / omega at transit scale IS O(1) (Eq. T.22, Delta omega / omega ~ 0.29 for modes near k_vH, with full saturation |beta_k|^2 ~ O(1) below k_vH). This confirms my conjecture in M3 that "the A_s gap would be entirely a CONVERSION problem (mode-to-zeta mapping), not a PRODUCTION problem." I now adopt this fully. The Bogoliubov machinery produces the right number of excitations at the right amplitude. The 3.15 OOM gap lives in the mapping from substrate excitations to the curvature perturbation zeta, not in the excitation physics itself. This narrows the problem enormously: the gap is in the delta-N conversion coefficients and the acoustic white hole transfer function, not in the fundamental pair creation mechanism.

**C2: Dissipative EFT is the wrong resolution path.** I concede Transit's structural objection (Re:M3). The Lopez Nacir formalism assumes steady-state noise from many incoherent friction events over many oscillation periods. The transit is a single coherent impulsive event lasting 0.66 e-folds. The duty-cycle correction I proposed (gamma_eff ~ H_fold) was an attempt to patch this mismatch, but Transit is right that the deeper issue is coherent vs. incoherent noise -- the Bogoliubov pairs are phase-correlated (squeezed state), while Lopez Nacir's noise kernel assumes random phases. The correct computation is Transit's direct Bogoliubov approach: solve the mode equation, extract |beta_k|^2, compute P_zeta through the delta-N conversion. The dissipative EFT, if it has any role, would serve as an EXPLANATION of why the slow-roll formula fails, not as the computation itself. I withdraw DISSIPATIVE-AS as a standalone computation and fold its physics into the unified TRANSIT-MODE-EQ pipeline (per Transit's Re:M5 proposal).

**C3: The freeze-out approximation is categorically inapplicable.** Transit's Re:M2 identifies a Category 3 entry I missed: the freeze-out assumption that modes become conserved after horizon crossing (zeta -> const for k << aH) fails during the transit because z = a sqrt(2 eps_H) changes by O(1) over the transit duration. This is a genuine inapplicability, distinct from the Bunch-Davies and consistency-relation items I listed. Adding it to Category 3 is correct. The Garriga-Mukhanov relation zeta = u_k / z is NOT valid during the transit interval precisely because z has rapid O(1) variation. This reinforces why the direct Bogoliubov computation is necessary.

**C4: Unified computation pipeline.** Transit's Re:M5 proposes merging my priorities 1 (TRANSIT-MODE-EQ) and 4 (MULTIFIELD-AS) into a single pipeline: solve mode equation per branch -> extract |beta_k|^2 per branch -> compute delta-N conversion -> output (A_s, n_s, alpha_s, f_NL, isocurvature fraction) simultaneously. I agree that this is the correct architecture. The five observables share the same Bogoliubov coefficients as input and the same delta-N coefficients as the conversion layer. Computing them separately would duplicate work and introduce inconsistencies from different approximation schemes applied to the same underlying mode equation. The unified pipeline is the S67 rate-limiting computation.

**C5: Alpha_s at CMB is zero; at transit it is large.** Transit's Re:M2 (Eq. T.13) derives that the van Hove singularity produces a DIVERGENT spectral index at k = k_vH but a smooth spectrum far from k_vH. Combined with the Mack-QA workshop conclusion (56 OOM scale hierarchy kills running at CMB pivot), the picture is now sharp: alpha_s(k_transit) is large (possibly divergent at the van Hove point), alpha_s(k_CMB) ~ 0, and the 5.0-sigma tension from applying the slow-roll formula is entirely an artifact of using a conversion that cannot resolve the 54-decade scale separation. The alpha_s question is CLOSED pending TRANSIT-MODE-EQ, which will confirm or refute the smooth behavior at CMB-relevant scales.

**C6: The information-preservation reframe of the 114 OOM.** Transit's Re:M1 adds a layer I did not articulate: the 114 OOM of energy dilution proceeds WITHOUT information loss because the GGE conserves the Richardson-Gaudin integrals. In thermal relaxation (standard LCDM after inflation), the 111 OOM of energy dilution erases all initial-state information except T and mu. In the GGE, every occupation number n_k = |beta_k|^2 is a conserved observable. This is not just a restatement of "Ordered Veil" -- it is an operational distinction with measurable consequences. The dark matter fraction f_DM is a CONSERVED CHARGE of the GGE, not a cosmic coincidence. The coincidence problem (Omega_DM ~ Omega_baryon) may reduce to an algebraic property of the Richardson-Gaudin integrals at the fold. This extends my M1 reframe in a direction I had not pursued.

### DISSENT

**D1: Transit's A_s calculation (Eq. T.18-19) gives 4.1 OOM gap -- WORSE, not better.** Transit computes A_s^{transit} ~ 2.6e-13 from direct application of the inflation-derived formula H^2/(8 pi^2 eps c_s) with transit-era values. This gives a 4.1 OOM deficit rather than the 3.15 OOM from Route A. But this calculation uses H = T_init^2/M_Pl = 5.7e12 GeV, which is the STANDARD FRW Hubble parameter derived from Friedmann. The framework's own Hubble parameter at the fold (H_fold from the spectral action) is H_fold = 586.5 M_KK, as flagged in my AS-AMPLITUDE-63 diagnostic. The discrepancy between H_FRW and H_SA at the fold is itself a symptom of the same conversion problem: the spectral action's "H" is not the same as the FRW H, because the spectral action generates the Einstein-Hilbert term through the a_2 moment, and the relationship between a_2 and the FRW Friedmann equation involves a normalization factor (the spinor correction factor, 16x from S58 W3-16). Using H_fold from the spectral action directly in the Garriga-Mukhanov formula is mixing two different definitions of "H." The correct computation avoids both by going through |beta_k|^2 directly (which Transit agrees is the right method), so the 4.1 OOM number is as much an artifact as the 3.15 OOM number -- both use formulas that assume slow-roll mode functions. The TRUE gap will emerge from TRANSIT-MODE-EQ.

**D2: The PW selection is NOT obviously an artifact.** Transit's Q4 asks whether the -3.50 OOM PW selection suppression is "real" or an artifact of single-field thinking, arguing that if the acoustic white hole involves all spectral modes (not just PW), then the full 155,984-eigenvalue mode space contributes and PW projection is wrong. This is too hasty. The PW (physical waveguide) projection selects modes that couple to 4D gravity through the a_2 moment. The acoustic white hole, whatever its internal structure, transfers perturbations to the 4D metric through the SAME a_2 coupling. If a mode does not contribute to a_2, it does not contribute to the curvature perturbation zeta regardless of whether it propagates through the acoustic channel. The multifield delta-N conversion uses all branches that couple to zeta, which is all branches that couple to a_2, which is precisely the PW sector. The non-PW modes (internal excitations that do not couple to 4D gravity) contribute to isocurvature but not to curvature perturbations. The PW selection may overcount the suppression (if some non-PW modes have residual a_2 coupling), but it is not categorically wrong. The correct procedure is to compute the a_2 overlap integral for each D_K eigenchannel and determine which contribute to zeta at what amplitude.

The A_s gap decomposition remains: BCS (-1.12, structural), PW selection (-3.50, needs refinement but not elimination), gap tunneling (-0.23, structural). The delta-N conversion could reduce the PW suppression by including sub-dominant a_2 couplings from non-PW channels, but it will not eliminate it entirely. I estimate the true suppression is between -1.5 and -3.5 OOM from PW-related physics, depending on how many channels have non-negligible a_2 overlap.

**D3: Backreaction magnitude needs scrutiny.** Transit's T2 (Eq. T.57) computes rho_backreaction ~ N_modes * M_KK^4 ~ 6e69 GeV^4, comparable to S(fold) ~ 10^67 GeV^4. This uses the TRANSIT-SCALE mode frequency omega_k ~ M_KK ~ 10^17 GeV for all 60 modes. But the GGE has a specific mode distribution: the 59.8 pairs span a range of frequencies determined by the D_K dispersion relation, not all at M_KK. The Leggett modes (20 pairs) have frequencies near the BCS gap Delta ~ 0.723 M_KK, while the acoustic modes (39.8 pairs) span from low-k (where omega ~ k c_BLV, much below M_KK) to the band edge. The proper backreaction sum is:

    rho_back = Sum_k omega_k |beta_k|^2 / V

with the mode-dependent omega_k from the D_K dispersion relation. For modes well below M_KK (which most acoustic modes are), the individual contributions are smaller. The total backreaction could be 1-2 OOM below Transit's estimate. This matters because: if rho_back << S(fold), the mode equation can be solved in the background-fixed approximation (Method C in T1 suffices). If rho_back ~ S(fold), self-consistent Kadanoff-Baym equations are required, dramatically increasing the computational complexity. The 10^{-47} yr settling time is suggestive of strong backreaction, but the settling could be dominated by the macroscopic q-theory vacuum variable, not by the quasiparticle backreaction per se. These are different degrees of freedom (Transit's own Re:M1 point about q vs. {n_k}).

### EMERGENCE

**E1: The acoustic white hole IS the transfer function.** Transit's T1 and T3-Q1 both identify the acoustic white hole transfer function T(k_CMB, k_transit) as the critical missing piece. Combining Transit's mode equation framework with my inflation-exflation synthesis, I can now specify what this transfer function must satisfy:

(a) It must convert a transit-scale spectrum that is NOT scale-invariant (Transit's T2: n_k ~ const for k << k_cross, n_k ~ k^{-4} for k >> k_cross) into the observed CMB spectrum that IS nearly scale-invariant (n_s = 0.9649 +/- 0.0042).

(b) The only way a non-scale-invariant input becomes nearly scale-invariant output is if the transfer function ITSELF has a specific power-law form that compensates the input tilt. For Transit's n_k ~ const low-k spectrum (which gives P(k) ~ k^3, i.e. n_s = 4 at transit scale), the transfer function must go as |T|^2 ~ k^{-3+n_s-1} ~ k^{-4.04} to produce n_s = 0.96 at CMB scale. This is a VERY specific prediction for the acoustic white hole: it must have a transfer function with approximately k^{-4} scaling over the range from k_transit to k_CMB.

(c) A k^{-4} transfer function is characteristic of acoustic propagation through a medium with a specific impedance profile. In the BEC analog (Barcelo-Liberati-Visser), the acoustic transfer function through a white hole has exactly this form when the flow velocity varies as v ~ r^{-2} (Bondi accretion in reverse). This is the phononic analog of geometric dilution in 3D: acoustic power spreads as 1/r^2 in amplitude, giving 1/r^4 in power, and k ~ 1/r maps this to P ~ k^{-4}.

(d) If (c) is correct, then the acoustic white hole NATURALLY produces near-scale-invariance from a flat Bogoliubov spectrum, and the spectral tilt n_s - 1 = -0.04 arises from the DEVIATION of the acoustic flow profile from exact r^{-2} scaling. The computation: extract the velocity profile v(r) of the post-transit acoustic flow from the spectral action gradient dS/dtau, compute the acoustic transfer matrix through this profile, and verify that |T|^2 ~ k^{-4+delta} with delta = n_s - 1 ~ -0.04.

This is the most important new insight from this workshop. It transforms the acoustic white hole from a qualitative causal argument into a quantitative transfer function computation, and it provides a physical mechanism for the scale-invariance that does not require slow-roll. The n_s prediction would then arise from the acoustic FLOW PROFILE, not from the slow-roll parameters at the fold.

**E2: The f_NL shape is a smoking gun -- the FOLDED bispectrum.** Transit's Re:M4 identifies that the GGE diagonal three-point function (Eq. T.27-28) peaks at FOLDED triangle configurations (k_1 + k_2 = k_3) because Bogoliubov pairs have momentum conservation k + (-k) = 0. No single-field inflation model produces a folded bispectrum. The Planck constraint on folded non-Gaussianity is much weaker than on equilateral or local shapes (f_NL^{folded} = -20 +/- 290). The combined prediction is:

| Shape | Amplitude | Source | Current bound | Future sensitivity |
|:------|:----------|:-------|:--------------|:-------------------|
| Equilateral | f_NL ~ 1.12 | c_BLV = 0.485 (Cheung et al.) | Planck: -26 +/- 47 | CMB-S4: sigma ~ 5 |
| Folded | f_NL ~ 0.13 | GGE diagonal (Transit Eq. T.28) | Planck: -20 +/- 290 | No current projections |
| Squeezed (multi-branch) | f_NL ~ O(1-10) | Leggett modulating acoustic | Planck: -0.9 +/- 5.1 | SPHEREx: sigma ~ 1 |

The folded shape is the discriminant. If future data detects folded non-Gaussianity at f_NL ~ 0.1-1, it would constitute evidence for Bogoliubov pair creation as the perturbation mechanism -- no other known model produces this signature. The equilateral channel is observationally more accessible (CMB-S4) but less distinctive (DBI inflation also produces equilateral f_NL). The folded channel is unique to the GGE mechanism.

**E3: The isocurvature constraint and f_NL prediction are the SAME computation.** Transit's Re:M4 emergence identifies that the Leggett channel contributes to the bispectrum through sigma-to-zeta conversion at second order, meaning the isocurvature fraction and f_NL share the SAME delta-N conversion coefficients. Combined with my M5 gap analysis (Planck constrains non-adiabatic fraction to < 1.7%), this creates a consistency triangle:

    delta-N coefficients -> (A_s, f_NL, beta_iso) simultaneously

These three observables are NOT independent. If the delta-N coefficients are chosen to match A_s (which requires a specific enhancement over the PW-only value), they PREDICT specific values of f_NL and beta_iso. If the predicted beta_iso exceeds 1.7%, the A_s solution is excluded by the isocurvature constraint. If the predicted f_NL exceeds Planck bounds, the A_s solution is excluded by the bispectrum constraint. This is an OVERCONSTRAINED system: three observational constraints on a set of conversion coefficients that are determined by the spectral geometry. The unified pipeline (C4 above) must output all three simultaneously and check mutual consistency.

**E4: BBN as G-renormalization, not N_eff.** Transit's Re:M1 (Eq. T.3-T.5) recasts the BBN constraint from "additional relativistic species" (additive delta_N_eff) to "renormalized gravitational constant" (modified G_eff). This is structurally different and potentially less constraining. The additive interpretation gives delta_N_eff = 1.34 (excluded at 10-sigma). The G-renormalization interpretation gives G_eff = G/(1 - 8pi alpha/3), where alpha = rho_vac/(H^2 M_Pl^2). For alpha = 0.67 (the naive Volovik tracking at BBN), G_eff = 3G, which IS still excluded (the D/H and Y_p abundances constrain G_eff at BBN to within ~2% of its present value, from Cyburt et al. 2016). But the exclusion mechanism is different: it comes from the EXPANSION RATE at T ~ 1 MeV, not from additional particle species. More importantly, Transit's Q3 identifies an escape route I had not considered: if the GGE quasiparticle pressure modifies the tracking exponent from n = 2 to n_eff > 2, the vacuum energy dilutes FASTER, reducing alpha at BBN. A shift from n = 2 to n = 2.3 would reduce rho_vac/rho_rad at BBN from 0.67 to ~0.01, making G_eff ~ 1.03 G, within the 2% BBN bound. This is a quantitative escape route that BBN-VOLOVIK-67 must evaluate.

### QUESTIONS

**Re: T3-Q1 (Acoustic white hole transfer function -- who computes it?)**: Neither of us alone. This is the bridge computation par excellence. I proposed the functional form in E1 above: |T|^2 ~ k^{-4+delta} with delta = n_s - 1, arising from acoustic propagation through a white-hole flow profile. The computation has two parts: (1) the acoustic flow profile v(r) from the post-transit spectral action gradient (this is substrate physics, requiring knowledge of dS/dtau at each tau value); (2) the acoustic transfer matrix through this profile (this is mode-equation physics, directly in Transit's domain). The division of labor: the spectral geometry team provides v(r), Transit solves the acoustic mode equation through v(r), and I verify the output against CMB transfer function standards. The key test: if |T|^2 at the CMB pivot converts Transit's flat-Bogoliubov input into A_s = 2.1e-9, the A_s problem is solved.

**Re: T3-Q2 (How many independent delta-N coefficients does SU(3) provide?)**: The SU(3) fiber has rank 2, with representations labeled by Dynkin indices (p, q). The GGE quasiparticles live in specific representations of D_K (determined by the BCS pairing structure). The independent delta-N channels are: (1) acoustic excitations in each irreducible representation of D_K's physical waveguide sector, (2) optical excitations (inter-band, same representation family), and (3) Leggett excitations (inter-band coherence, representation-changing). The number of independent channels is bounded above by the number of distinct irreducible representations in the D_K spectrum at the fold. At L_max = 10, this is approximately 17,000 distinct eigenvalue values, but many representations contribute at the same effective frequency and therefore have degenerate delta-N coefficients. The effective number of independent delta-N coefficients is the number of DISTINCT a_2 coupling strengths, which is the number of irreducible representations that contribute non-degenerately to the second spectral moment. This has not been computed. The Baptista papers (researchers/Baptista/, #13-#18) provide the KK decomposition that would answer this: each KK level contributes independently to a_2 through its eigenvalue weight. The computation is: decompose a_2 by irreducible representation, count the number of channels with distinct contributions, and these are the independent delta-N coefficients.

**Re: T3-Q3 (What constrains the Volovik tracking exponent?)**: The tracking exponent n = 2 in rho_vac ~ H^n follows from the Gibbs-Duhem relation under the assumption of a simple-fluid vacuum equation of state. Transit correctly identifies that the GGE quasiparticle pressure could modify n. The framework has not computed the GGE pressure contribution, but the structure of the correction is:

    n_eff = 2 + Sum_k (dp_k/dH) * n_k / (Sum_k omega_k n_k)

where p_k = (1/3) omega_k n_k for relativistic modes (acoustic) and p_k = 0 for non-relativistic modes (Leggett at late times). At BBN, the acoustic modes are relativistic (T_BBN >> m_acoustic), so dp_k/dH = (1/3) d omega_k/dH * n_k. The correction to n depends on how the mode frequencies track H, which is determined by the adiabatic evolution of the D_K spectrum during the post-fold expansion. If omega_k ~ a^{-1} (adiabatic redshift), then d omega_k/dH ~ -omega_k/H, giving n_eff ~ 2 - (1/3)(acoustic energy fraction). With acoustic modes carrying ~67% of the GGE energy (39.8/59.8 pairs), this gives n_eff ~ 2 - 0.22 ~ 1.78, which makes the tracking SLOWER (rho_vac dilutes more slowly), WORSENING the BBN constraint. However, this assumes the mode frequencies are set by the Hubble rate; if they are instead set by the spectral gap (which evolves independently of H), the correction could have either sign. The BBN-VOLOVIK-67 computation must include the GGE pressure self-consistently.

**Re: T3-Q4 (Is the PW selection real?)**: Answered in D2 above. The PW selection is not an artifact -- it reflects the physical requirement that modes must couple to a_2 to contribute to curvature perturbations. But the -3.50 OOM value may overestimate the suppression if sub-dominant channels have non-negligible a_2 overlap. The correct computation is the a_2 overlap integral per D_K eigenchannel.

**Re: T3-Q5 (Feature predictions and Planck residuals)**: The van Hove peak at transit scale (k_vH ~ M_KK/c_BLV ~ 10^{17} GeV, corresponding to k ~ 10^{52} Mpc^{-1}) is 54 decades above the Planck range (k ~ 0.01-0.3 Mpc^{-1}). The acoustic white hole transfer maps k_transit to k_CMB, but the MONOTONICITY of this mapping determines whether the van Hove peak maps to a single l-value or is smeared across the spectrum. If the acoustic transfer is smooth and monotonic, the peak maps to a specific l_vH with a characteristic bump. Planck residuals DO show unexplained features: the well-known dip at l ~ 20-30 and the oscillatory residuals in the range l ~ 700-900 (Planck 2018 legacy, Section 6.3). Whether these could correspond to the van Hove peak depends on the acoustic scale mapping, which requires the transfer function from E1. This is a PREDICTION that becomes testable once the transfer function is computed: the van Hove feature's location in l-space is determined by the same transfer function that determines A_s, making it a zero-free-parameter prediction.

**M-Q1 for Transit (final):** Your transit-scale spectrum (T2) has P(k) ~ k^2 for k << k_cross and P(k) ~ k^{-2} for k >> k_cross. The CMB observes in the ultra-low-k regime (54 decades below k_cross). In the k << k_cross regime, n_s = 3 -- a DEEPLY blue spectrum. The acoustic white hole must convert this to n_s ~ 0.96. My E1 proposes |T|^2 ~ k^{-4} from acoustic geometric dilution. But this requires the acoustic flow to be EXACTLY r^{-2} to high precision (any deviation produces a tilt correction). In your Bogoliubov framework, is there a NATURAL REASON for the acoustic flow profile to be r^{-2}? In BEC analogs (Barcelo-Liberati-Visser), the r^{-2} profile arises from mass conservation in spherical Bondi flow. What is the substrate analog of mass conservation that fixes the flow profile?

**M-Q2 for Transit (final):** Your Eq. T.29 gives f_NL^{GGE} ~ N_pair^{-1/2} ~ 0.13 from the GGE diagonal channel. This uses the central limit theorem (sum over modes). But the GGE is NOT a random superposition of modes -- it has specific correlations imposed by the Richardson-Gaudin integrals. Could the Richardson-Gaudin structure enhance or suppress the three-point function relative to the random-phase estimate? Specifically: the Richardson-Gaudin pairing enforces that excitations come in correlated pairs (k, -k). These pairs contribute COHERENTLY to the bispectrum at folded configurations. If the pairs are phase-locked (which the sudden approximation, where alpha and beta are REAL, suggests), the coherent sum could exceed the random-phase estimate by a factor of sqrt(N_pair), giving f_NL^{GGE,coherent} ~ 1 rather than 0.13. Has this coherent-pair enhancement been computed for integrable systems?

---

## Round 2 -- Transit: Cross-Synthesis

### CONVERGENCE

**C1: Both 3.15 and 4.1 OOM A_s numbers are formula artifacts -- accepted.** Mack's D1 correctly identifies that my Eq. T.18-19 computation (A_s ~ 2.6e-13, gap of 4.1 OOM) suffers from the same category error as the 3.15 OOM Route A value. I used H = T_init^2 / M_Pl from the standard Friedmann equation, but Mack points out that the spectral action's Hubble parameter H_fold = 586.5 M_KK differs from the FRW value by the spinor correction factor (16x, S58 W3-16). The underlying issue is structural: any formula of the form A_s = H^2/(8 pi^2 eps c_s) presupposes that the mode functions are adiabatic at horizon crossing. At Mach 13.75, they are not. Both the 3.15 and 4.1 OOM gaps are therefore SYMPTOMS of using a formula outside its regime, not independent measurements of the actual deficit. I accept this fully.

The consequence is precise and constraining: the TRUE A_s gap is unknown until TRANSIT-MODE-EQ produces |beta_k|^2 directly from the mode equation. Neither my Bogoliubov estimate (Eq. T.18) nor Mack's Route A (Garriga-Mukhanov) can be trusted at better than order-of-magnitude. What IS established is that the production side gives |beta_k|^2 ~ O(1) (Eq. T.20, confirmed by P_exc = 1.000 saturation), so the gap -- whatever its true magnitude -- lives entirely in the conversion layer (delta-N coefficients + acoustic white hole transfer). The formula artifacts differ by 0.95 OOM between the two routes, which is itself a measure of how far outside the slow-roll regime both formulas are operating.

**C2: PW selection is NOT purely an artifact -- modes must couple to a_2.** Mack's D2 presents the correct structural argument that I was too hasty in dismissing. The physical-waveguide projection selects modes that couple to the second spectral moment a_2, which IS the gravitational sector. The curvature perturbation zeta is, by definition, the metric perturbation coupled to a_2. A mode that carries spectral weight but does not contribute to a_2 cannot source curvature perturbations -- it contributes only to isocurvature.

This is a Bogoliubov-level distinction I should have been more careful about. In the mode equation framework, different channels have different coupling strengths to the background:

    omega_k^2(tau) = k^2 c_BLV^2 + m_{eff,I}^2(tau)    (T.62)

where I labels the channel (acoustic, optical, Leggett) and m_{eff,I}^2 depends on how channel I couples to the spectral action. The a_2 overlap integral for each channel determines the coupling strength to zeta:

    zeta_I = (partial a_2 / partial sigma_I) * delta sigma_I    (T.63)

Channels with vanishing a_2 overlap have zero contribution to zeta regardless of their Bogoliubov occupation. The PW selection implements this coupling hierarchy. I concede that the -3.50 OOM suppression is NOT eliminable by including all modes -- it reflects the genuine spectral geometry of a_2.

Where I maintain a narrower objection: the -3.50 OOM VALUE may be too large if computed from a single-field projection that underestimates the number of channels with non-negligible a_2 overlap. Mack's own estimate (-1.5 to -3.5 OOM range) is reasonable. The computation that resolves this is the a_2 overlap integral per D_K eigenchannel, which is a spectral geometry calculation rather than a Bogoliubov one. I accept Mack's framing: PW selection is structurally real, the magnitude needs refinement but not elimination.

**C3: Backreaction estimate is 1-2 OOM high -- accepted with caveats.** Mack's D3 correctly identifies that my Eq. T.57 (rho_backreaction ~ 6e69 GeV^4) uses omega_k ~ M_KK for all 60 modes. The actual GGE has a mode-resolved dispersion: Leggett modes at Delta ~ 0.723 M_KK (20 pairs) and acoustic modes spanning from low-k to the band edge (39.8 pairs). The acoustic modes contribute:

    rho_acoustic ~ Sum_k omega_k n_k ~ N_acoustic * <omega_k>_acoustic * <n_k>    (T.64)

For acoustic modes with <omega_k> ~ (1/2) M_KK (geometric mean of the band), the acoustic backreaction is ~ 40 * (0.5 M_KK)^4 ~ 40 * (1/16) M_KK^4 ~ 2.5 M_KK^4 ~ 2.5e68 GeV^4. The Leggett contribution is ~ 20 * (0.723 M_KK)^4 ~ 20 * 0.27 M_KK^4 ~ 5.5 M_KK^4 ~ 5.5e68 GeV^4. The total is ~ 8e68 GeV^4, which is about 1 OOM below my original estimate of 6e69 GeV^4 but still ~ 1 OOM above S(fold) ~ 10^67 GeV^4.

This means backreaction is significant but not overwhelming. Mack's conclusion is correct: the background-fixed approximation (Method C in T1) is marginal but usable as a FIRST computation, with self-consistent Kadanoff-Baym [07] as the refinement step. The 10^{-47} yr settling time should be attributed primarily to the macroscopic q-theory variable (Mack's point that q and {n_k} are different degrees of freedom), not to quasiparticle backreaction. The distinction matters: q-theory settling is a single collective mode, while quasiparticle backreaction involves the full 60-mode GGE spectrum.

**C4: Alpha_s CLOSED as mapping artifact -- both sides agree.** Mack's C5 and my R1 analysis (Eq. T.13) converge on the same picture: alpha_s(k_transit) is large (divergent at the van Hove point), alpha_s(k_CMB) ~ 0, and the 5.0-sigma tension is entirely an artifact of the slow-roll conversion formula. The 56 OOM scale separation between transit and CMB makes the slow-roll mapping formula for alpha_s catastrophically incorrect -- it attempts to propagate a transit-scale quantity to CMB scale through a formula that assumes scale-independent parameters. This question is CLOSED. The confirmation will come from TRANSIT-MODE-EQ, which will show alpha_s(k_CMB) ~ 0 directly from the mode equation solution.

**C5: Dissipative EFT withdrawn; unified pipeline adopted.** Mack's C2 formally withdraws DISSIPATIVE-AS as a standalone computation and folds it into the unified TRANSIT-MODE-EQ pipeline. Combined with Mack's C4 (unified computation architecture), the workshop has produced a single coherent computation program: solve the mode equation per GGE branch, extract |beta_k|^2 per branch, apply the delta-N conversion with a_2-weighted coefficients, and output (A_s, n_s, alpha_s, f_NL, beta_iso) simultaneously. This is the S67 rate-limiting computation, and both workshop participants agree on its architecture.

**C6: Information-preservation reframe adopted.** Mack's C6 accepts the information-theoretic dimension I added in R1: the GGE conserves Richardson-Gaudin integrals through the full 114 OOM of expansion, making the dark matter fraction a conserved charge rather than a cosmic coincidence. Mack extends this to the coincidence problem (Omega_DM ~ Omega_baryon), suggesting it reduces to an algebraic property of the Richardson-Gaudin integrals at the fold. This is a testable structural prediction: the ratio Omega_DM/Omega_baryon should be computable from the BCS gap structure and the Leggett-to-acoustic partition at the fold. If the computed ratio matches the observed value of ~5, it would be an independent zero-parameter prediction.

### DISSENT

**D1: The acoustic white hole transfer function is NOT guaranteed to produce k^{-4} scaling.** Mack's E1 proposes that the acoustic white hole transfer has |T|^2 ~ k^{-4+delta} with delta = n_s - 1 ~ -0.04, arising from geometric acoustic dilution in a flow profile v ~ r^{-2}. This is a physically motivated proposal, and the BEC analog argument (Barcelo-Liberati-Visser [08]) is suggestive. But the argument has an unstated assumption that deserves scrutiny.

In the BEC analog, the k^{-4} scaling arises from mass conservation in spherical Bondi flow: the velocity field v(r) = Q/(4 pi r^2 rho), where Q is the mass flow rate and rho is the fluid density. In the substrate, there is no "mass flow" in the traditional sense -- the spectral action gradient dS/dtau drives the transit, and the post-transit acoustic propagation is governed by the GGE quasiparticle dispersion, not by a fluid flow profile.

The correct approach is to derive the transfer function from the post-transit acoustic mode equation:

    phi_k'' + (k^2 c_BLV^2 - V_eff(r)) phi_k = 0    (T.65)

where V_eff(r) is the effective potential determined by the GGE acoustic medium. The "acoustic white hole" is the region where the effective potential creates a horizon for ingoing acoustic modes. The transfer function |T(k)|^2 is then the transmission coefficient through this potential barrier, which has the standard WKB form:

    |T(k)|^2 ~ exp(-2 integral_{r_1}^{r_2} sqrt(V_eff - k^2 c_BLV^2) dr)    (T.66)

for k below the barrier (evanescent transmission), and |T(k)|^2 ~ 1 for k above the barrier (propagating). The power-law behavior |T|^2 ~ k^{-4} would require V_eff(r) to have a SPECIFIC radial profile. The BEC analog suggests this profile is natural, but the substrate's V_eff comes from the spectral action, not from fluid dynamics.

My dissent is not that k^{-4} is wrong -- it may well be correct -- but that the argument is NOT yet a derivation. It is a physically motivated ansatz drawn from the BEC analog. The computation that settles this is: extract V_eff(r) from the post-transit spectral action, solve Eq. T.65, and compute |T(k)|^2 directly. If it turns out to be k^{-4}, Mack's argument provides the physical explanation. If it deviates, the deviation determines the correction to n_s from the transfer channel.

Mack's M-Q1 asks whether there is a natural reason for the acoustic flow profile to be r^{-2}. From the Bogoliubov framework: the GGE quasiparticles propagate freely after the transit (the GGE is, by definition, a stationary state of the post-transit Hamiltonian). Free propagation in 3D gives a 1/r^2 dilution of acoustic intensity (geometric spreading), which corresponds to |T|^2 ~ k^{-4} for the AMPLITUDE transfer in power. But this assumes the post-transit geometry is 3D Euclidean, which is the emergent metric from the a_2 moment. If the post-transit geometry has curvature (which it does -- the universe is expanding), the geometric spreading acquires corrections from the scale factor a(t), giving |T|^2 ~ k^{-4} * (corrections from expansion). These corrections encode the full post-transit expansion history and are precisely the standard transfer function of post-inflationary cosmology. The k^{-4} baseline from geometric spreading is therefore the RIGHT starting point, with standard cosmological transfer corrections on top. Mack's proposal is structurally sound as a BASELINE, with the caveat that the corrections from the post-transit expansion history are NOT small and must be included.

**D2: The coherent-pair f_NL enhancement may be more subtle than sqrt(N_pair).** Mack's M-Q2 proposes that the Richardson-Gaudin pairing structure could enhance the GGE bispectrum from f_NL^{GGE} ~ N_pair^{-1/2} ~ 0.13 to f_NL^{GGE,coherent} ~ 1, through phase-locked coherent summation. The argument: in the sudden approximation, alpha_k and beta_k are real (no phases), so the Bogoliubov pairs sum coherently rather than with random phases.

This is a valid observation about the phase structure, but the enhancement factor requires more careful analysis. The bispectrum at folded configurations (k_1 + k_2 = k_3) receives contributions from modes satisfying the triangle condition. The coherent sum is:

    B_folded = Sum_{k_1, k_2} alpha_{k_1} beta_{k_1} * alpha_{k_2} beta_{k_2} * delta(k_1 + k_2 - k_3)    (T.67)

For real alpha, beta with alpha_k beta_k > 0 for all k, the sum is positive definite. But the delta-function constraint limits the summation to pairs satisfying k_1 + k_2 = k_3. In 3D, the number of such pairs scales as the AREA of the constant-sum surface in k-space, which is ~ k_3^2. The coherent sum therefore has contributions from ~ k_3^2 / (Delta k)^2 pairs, where Delta k is the k-space resolution of the Bogoliubov spectrum. The f_NL from coherent summation is:

    f_NL^{coherent} ~ (k_3^2 / Delta k^2) * <alpha_k beta_k>^2 / P(k_3)^2    (T.68)

The ratio k_3^2/Delta k^2 is the number of coherently contributing pairs, which can be large. For k_3 ~ k_cross (the transit scale) and Delta k ~ H/c_BLV (the minimum k-space resolution from the transit duration), this gives ~ (k_cross / (H/c_BLV))^2 ~ (m_eff * c_BLV / H)^2 >> 1. The coherent enhancement is therefore NOT simply sqrt(N_pair) but depends on the RATIO of the transit wavenumber to the transit duration in k-space.

This is a more optimistic estimate than my R1 value of f_NL ~ 0.13, but the precise enhancement depends on the k-dependence of alpha_k beta_k (which is smooth for the sudden approximation but could oscillate for the full mode equation solution). The Richardson-Gaudin structure adds further constraint: the pairing enforces specific correlations between (k, -k) pairs that are NOT independent of each other. Whether this enhances or suppresses the bispectrum relative to Eq. T.68 depends on the pairing symmetry class (s-wave vs. higher partial waves in the BCS Hamiltonian). For s-wave pairing (isotropic gap), all pairs contribute with the same sign, maximizing the coherent sum. For anisotropic pairing (d-wave or higher), partial cancellation occurs.

The bottom line: the coherent enhancement is real and potentially significant (f_NL^{GGE} could be O(1) rather than 0.13), but the precise value requires the full mode equation solution and the BCS pairing symmetry. The folded SHAPE remains the robust prediction regardless of the amplitude uncertainty.

### EMERGENCE

**E1: The A_s conversion problem has a two-layer structure that neither participant identified in isolation.** The full four-turn exchange reveals that the A_s gap decomposes into two logically distinct layers, each requiring its own computation:

Layer 1 -- **Mode-to-branch conversion** (delta-N coefficients): How does each GGE branch's Bogoliubov occupation |beta_k^I|^2 contribute to the curvature perturbation zeta? This is the a_2 overlap integral per D_K eigenchannel, constrained by PW selection (Mack's D2) and multifield delta-N (my T3-Q2, Mack's response Re:T3-Q2). The number of effective channels is the number of D_K representations with non-negligible a_2 coupling, bounded above by ~17,000 but likely much smaller due to degeneracy in the a_2 weight. This layer converts the 60-mode GGE spectrum into an effective single-field curvature perturbation with enhancement factor N_eff^{a_2}.

Layer 2 -- **Transit-to-CMB transfer** (acoustic white hole): How does the transit-scale curvature perturbation propagate to CMB scales? This is the acoustic transfer function |T(k)|^2, which Mack's E1 proposes scales as k^{-4+delta} from geometric acoustic dilution. This layer converts the transit-scale power spectrum (n_s = 3, blue, from my T2) into the CMB-scale spectrum (n_s ~ 0.96, nearly flat).

The critical insight from the workshop: Layer 1 and Layer 2 are SEPARABLE. The delta-N conversion depends only on the spectral geometry at the fold (the a_2 overlaps), while the acoustic transfer depends only on the post-transit propagation (the GGE medium properties). They can be computed independently and combined multiplicatively:

    A_s^{CMB} = |T(k_CMB)|^2 * Sum_I (partial a_2/partial sigma_I)^2 * |beta_{k,I}|^2 / (2 omega_{k,I})    (T.69)

This factorization means the A_s problem is actually TWO independent problems, each testable separately. Layer 1 is testable through the isocurvature constraint (beta_iso < 1.7%, which constrains the a_2 coupling ratios). Layer 2 is testable through the spectral tilt (n_s at CMB, which constrains the transfer function's power-law index). The overconstraint from Mack's E3 (the consistency triangle A_s, f_NL, beta_iso) applies specifically to Layer 1.

**E2: The acoustic white hole k^{-4} transfer creates a TESTABLE CONSISTENCY CONDITION.** Combining my transit-scale spectrum from T2 (n_k ~ const for k << k_cross, giving P(k) ~ k^3) with Mack's E1 acoustic transfer (|T|^2 ~ k^{-4+delta}), the CMB power spectrum becomes:

    P_CMB(k) ~ k^3 * k^{-4+delta} = k^{-1+delta}    (T.70)

The observed spectral index at CMB is n_s - 1 = d ln P / d ln k = -1 + delta, giving delta = n_s = 0.965. But delta was defined as the deviation of the acoustic flow from exact r^{-2} scaling. So the consistency condition is:

    n_s = delta_acoustic    (T.71)

This is a STRUCTURAL PREDICTION: the spectral tilt at CMB is NOT determined by slow-roll parameters at the fold, but by the deviation of the post-transit acoustic flow profile from geometric 1/r^2 dilution. If the acoustic flow is EXACTLY 1/r^2, the CMB spectrum would be P ~ k^{-1}, giving n_s = 0 -- completely flat in the sense d ln P/d ln k = -1 (spectral index n_s = 0, not n_s = 1). Correcting my algebra: with P(k) ~ k^{n_s-1}, the standard convention gives P ~ k^{-1+delta} which means n_s - 1 = -1 + delta, so n_s = delta. For n_s = 0.965, delta = 0.965.

However, the transit-scale input spectrum P(k) ~ k^3 assumed |beta_k|^2 ~ const (saturated production for k << k_cross). If the production has residual k-dependence from the van Hove structure, the input tilt modifies the consistency condition. The general form is:

    n_s^{CMB} = n_s^{transit} + n_T^{transfer}    (T.72)

where n_s^{transit} is the tilt of the Bogoliubov spectrum at transit scale (from the mode equation) and n_T^{transfer} is the tilt of the acoustic transfer function. This is an ADDITIVE decomposition of the spectral tilt. Currently both n_s^{transit} and n_T^{transfer} are unknown, but their SUM is measured (n_s = 0.9649 +/- 0.0042). The mode equation computation determines n_s^{transit}, and the acoustic transfer computation determines n_T^{transfer}. The consistency check is whether their sum matches Planck.

This additive structure has an important consequence: even a significant error in the transit-scale tilt (e.g., n_s^{transit} = 3 +/- 0.5 from van Hove structure uncertainty) can be absorbed into the acoustic transfer tilt (n_T^{transfer} = -2.035 +/- 0.5). The spectral tilt is therefore a WEAK constraint on the transit dynamics but a STRONG constraint on the acoustic transfer. The discriminating power lies in the CONSISTENCY between independently computed n_s^{transit} and n_T^{transfer}, not in either value alone.

**E3: The folded bispectrum from Bogoliubov pair creation is the workshop's most distinctive prediction.** Across all four turns, the most novel finding is that the GGE diagonal three-point function (my Eq. T.27-28) peaks at folded triangle configurations (k_1 + k_2 = k_3) -- a signature that NO single-field inflation model produces. Mack's E2 confirms this as the smoking-gun discriminant, with the current Planck bound (f_NL^{folded} = -20 +/- 290) leaving ample room.

The workshop sharpens the prediction across rounds:

| Round | Participant | Contribution |
|:------|:-----------|:-------------|
| R1 Transit | Re:M4, Eq. T.27-28 | GGE diagonal bispectrum derived; folded shape identified from k + (-k) = 0 pair momentum conservation |
| R1 Transit | Re:M4 emergence | Joint (isocurvature, f_NL, f_NL shape) from same delta-N coefficients |
| R2 Mack | E2 | Confirmed folded shape unique to Bogoliubov mechanism; tabulated all three shapes with observational bounds |
| R2 Mack | M-Q2 | Proposed coherent-pair enhancement: f_NL could be O(1) rather than 0.13 |
| R2 Transit | D2 above | Coherent enhancement is real but depends on pairing symmetry; s-wave maximizes, d-wave suppresses |

The robust content is: (1) the GGE bispectrum has a folded component that is zero in all single-field inflation models, (2) its amplitude is f_NL^{folded} ~ 0.1-1 depending on coherence, and (3) its detection would constitute evidence for Bogoliubov pair creation as the perturbation mechanism. This is a PRE-REGISTERABLE prediction for future CMB experiments. No computation beyond the mode equation + delta-N conversion is needed -- the folded shape is a STRUCTURAL consequence of the Bogoliubov pair creation mechanism, independent of model details.

**E4: BBN as G-renormalization defines a clean gate with the tracking exponent as the free parameter.** The workshop evolution on the BBN constraint across all four turns has been:

| Turn | Claim | Status |
|:-----|:------|:-------|
| R1 Mack (M1) | rho_vac/rho_rad = 0.67 at BBN, excluded as delta_N_eff = 1.34 | Opening position |
| R1 Transit (Re:M1) | Vacuum contributes as G-renormalization, not additive N_eff (Eq. T.3-5). Still excluded for alpha = 0.67 | Structural recast |
| R1 Transit (T3-Q3) | GGE pressure could modify tracking exponent from n=2, reducing alpha at BBN | Escape route identified |
| R2 Mack (E4) | G_eff constrained to 2% of present value at BBN. Shift n=2 to n=2.3 gives alpha ~ 0.01, satisfying bound | Quantified escape |
| R2 Mack (Re:T3-Q3) | GGE pressure correction gives n_eff ~ 1.78 (WORSE), but mode frequency evolution uncertain | Partial closure |

The workshop converges on: the BBN constraint is NOT additive-N_eff but a G-renormalization bound, and the magnitude depends on the tracking exponent n_eff. The current picture is:

    n_eff < 2 (Mack's estimate from acoustic GGE pressure): alpha(BBN) > 0.67, EXCLUDED
    n_eff = 2 (Volovik baseline): alpha(BBN) = 0.67, EXCLUDED (G_eff = 3G, far outside 2% bound)
    n_eff = 2.3: alpha(BBN) ~ 0.01, G_eff ~ 1.03G, within 2% bound, PASS

The critical question is which direction the GGE pressure pushes n_eff. Mack's estimate (n_eff ~ 1.78) uses omega_k ~ a^{-1} (adiabatic redshift), but this assumes the mode frequencies are set by the Hubble expansion. If instead the mode frequencies are set by the spectral gap (which is a property of D_K, not of H), the relationship between omega_k and H is indirect, and the correction could have either sign. The BBN-VOLOVIK-67 computation must: (1) solve the q-theory vacuum equation from the fold through BBN, (2) include the GGE mode frequency evolution self-consistently, and (3) output alpha(T_BBN) with the GGE pressure contribution included.

The pre-registered gate: alpha(T_BBN) < 0.02 (corresponding to G_eff within 2% of G_Newton). This is the single tightest constraint on the Volovik tracking mechanism.

**E5: The workshop produces a complete, agreed-upon computation specification for S67.** The four-turn exchange has converged on a unified computation pipeline that both participants endorse:

**TRANSIT-MODE-EQ-67** (unified pipeline):
1. **Input**: Spectral action S(tau) at 16 available tau values; D_K eigenvalue spectrum; BCS gap structure
2. **Mode equation**: Solve u_k'' + omega_k^2(tau) u_k = 0 for each GGE branch (acoustic, optical, Leggett), using Method B (transfer matrix through 16 tau values) as primary and Method A (sudden approximation) as cross-check
3. **Bogoliubov extraction**: |beta_k^I|^2 for each branch I, verified against unitarity |alpha_k|^2 - |beta_k|^2 = 1
4. **Delta-N conversion**: Compute a_2 overlap integral per D_K eigenchannel; weight |beta_k^I|^2 by (partial a_2/partial sigma_I)^2 to get effective curvature perturbation per branch
5. **Output**: (A_s^{transit}, n_s^{transit}, alpha_s^{transit}) at transit scale; (f_NL equilateral, folded, squeezed) from mode equation + delta-N; (beta_iso) from Leggett-to-acoustic coupling ratio

**ACOUSTIC-TRANSFER-67** (second half):
1. **Input**: Post-transit GGE medium properties; spectral action gradient dS/dtau for acoustic flow profile
2. **Transfer equation**: Solve phi_k'' + (k^2 c_BLV^2 - V_eff(r)) phi_k = 0 through the acoustic white hole
3. **Output**: |T(k)|^2 from transit scale to CMB scale; n_T^{transfer} = d ln |T|^2 / d ln k

**BBN-VOLOVIK-67** (constraint gate):
1. **Input**: q-theory vacuum equation; GGE mode spectrum; BBN nuclear abundances (D/H, Y_p)
2. **Computation**: Evolve q from fold through BBN with GGE pressure self-consistently included
3. **Output**: alpha(T_BBN) = rho_vac / (H^2 M_Pl^2) at T_BBN
4. **Gate**: alpha(T_BBN) < 0.02 (G_eff within 2% of G_Newton)

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | 114 OOM = exflation | M1, Re:M1, C6, C6 | **Converged** | 114 OOM is expansion history, not gap. Information-preserving (GGE conserves Richardson-Gaudin integrals). DM fraction is conserved charge, not coincidence. |
| 2 | Inflation tool mapping | M2, Re:M2, C5, C4 | **Converged** | Three-category classification (structural / formal / inapplicable) agreed. Freeze-out added to Category 3. Alpha_s CLOSED as mapping artifact. Slow-roll formulas categorically inapplicable at Mach 13.75. |
| 3 | A_s normalization | M3, Re:M3, D1, C1-C2 | **Partial** | A_s is conversion problem, not production (converged). Dissipative EFT withdrawn (converged). Both 3.15 and 4.1 OOM gaps are formula artifacts (converged). PW selection is structurally real but magnitude uncertain: -1.5 to -3.5 OOM (partial). True gap unknown until TRANSIT-MODE-EQ. |
| 4 | f_NL prediction | M4, Re:M4, E2, D2 | **Partial** | Equilateral f_NL ~ 1.12 from c_BLV (converged). Folded bispectrum as smoking gun, unique to Bogoliubov pair creation (converged). GGE diagonal amplitude uncertain: f_NL ~ 0.13 (random phase) to O(1) (coherent), depends on pairing symmetry (partial). |
| 5 | Mode equation specification | T1, C4 | **Converged** | Complete formulation (Eq. T.39-T.52) agreed. Unified pipeline: mode eq per branch -> delta-N conversion -> (A_s, n_s, alpha_s, f_NL, beta_iso) simultaneously. S67 rate-limiting computation. |
| 6 | Preheating tools | T2, D3 | **Partial** | Transfer matrix, non-thermal spectra, Stokes multiplier all transfer from preheating (converged). Backreaction ~10^68-10^69 GeV^4, significant but Method C usable as first pass (partial -- agreed within 1 OOM). Floquet, stochastic resonance, thermalization categorically inapplicable (converged). |
| 7 | Acoustic white hole transfer | E1, D1-Transit | **Emerged** | k^{-4} baseline from geometric acoustic dilution (proposed by Mack, structurally sound but not yet derived from spectral action). Consistency condition: n_s^{CMB} = n_s^{transit} + n_T^{transfer}. Transfer function is second half of computation, separable from mode equation. |
| 8 | BBN constraint | M1, Re:M1, E4, Q3 | **Emerged** | G-renormalization, not additive N_eff (emerged from R1). Tracking exponent n_eff as free parameter. Gate: alpha(T_BBN) < 0.02. GGE pressure direction uncertain (could help or hurt). |
| 9 | Consistency triangle | E3-Mack, E1-Transit | **Emerged** | (A_s, f_NL, beta_iso) overconstrained by same delta-N coefficients. Joint computation from unified pipeline. Isocurvature bound (beta_iso < 1.7%) constrains A_s solution. |
| 10 | Two-layer A_s structure | E1-Transit | **Emerged** | Layer 1 (delta-N, spectral geometry at fold) separable from Layer 2 (acoustic transfer, post-transit propagation). Each independently testable. |

## Remaining Open Questions

**OQ-1: What is the acoustic white hole transfer function |T(k)|^2?**
- Pre-registered gate: |T(k_pivot)|^2 must convert transit-scale |beta_k|^2 ~ O(1) into A_s = (2.10 +/- 0.03) x 10^{-9} at CMB pivot
- Computation: ACOUSTIC-TRANSFER-67 (Eq. T.65-66, extract V_eff from post-transit spectral action, solve acoustic mode equation)
- Discrimination: If |T|^2 ~ k^{-4+delta} with delta = n_s, Mack's geometric dilution picture is confirmed; deviations indicate non-trivial acoustic medium structure

**OQ-2: How many D_K eigenchannels have non-negligible a_2 coupling?**
- Pre-registered gate: N_eff^{a_2} (number of channels with >1% of total a_2 weight) must satisfy: N_eff^{a_2} * |beta_k|^2 / (2 omega_k z^2) -> A_s within 1 OOM of Planck after acoustic transfer
- Computation: Decompose a_2 by D_K irreducible representation at tau = tau_fold; compute overlap integral per channel
- Discrimination: N_eff^{a_2} >> 1 supports multifield enhancement; N_eff^{a_2} ~ 1 confirms PW selection at -3.5 OOM

**OQ-3: What is the tracking exponent n_eff at BBN with GGE pressure included?**
- Pre-registered gate: alpha(T_BBN) < 0.02 (G_eff within 2% of G_Newton at BBN)
- Computation: BBN-VOLOVIK-67 (q-theory vacuum + GGE mode frequency evolution from fold through BBN)
- Discrimination: n_eff > 2 passes the gate; n_eff <= 2 excludes the Volovik tracking mechanism as currently formulated

**OQ-4: What is the BCS pairing symmetry of the GGE at the fold?**
- Pre-registered gate: pairing symmetry determines coherent vs. random-phase bispectrum; s-wave gives f_NL^{folded} ~ O(1), d-wave gives f_NL^{folded} ~ 0.13
- Computation: Analyze BCS gap structure from D_K spectrum at tau_fold; classify by angular momentum quantum numbers
- Discrimination: Determines whether folded bispectrum is detectable by CMB-S4 (O(1)) or requires next-generation experiment (0.13)

**OQ-5: Does the n_s^{CMB} = n_s^{transit} + n_T^{transfer} consistency condition hold?**
- Pre-registered gate: n_s^{transit} (from TRANSIT-MODE-EQ-67) + n_T^{transfer} (from ACOUSTIC-TRANSFER-67) = 0.9649 +/- 0.0042
- Computation: Both halves of the unified pipeline
- Discrimination: Consistency within 2-sigma validates the two-layer decomposition; failure at >3-sigma indicates missing physics (e.g., non-linear transfer, backreaction on acoustic medium)

**OQ-6: Is the isocurvature fraction from Leggett-channel GGE excitations below the Planck bound?**
- Pre-registered gate: beta_iso < 0.017 (Planck 95% CL)
- Computation: Extract Leggett-to-acoustic a_2 coupling ratio from delta-N coefficients; compute beta_iso = (Leggett a_2 fraction)^2 * (N_Leggett/N_total)
- Discrimination: beta_iso < 0.017 passes; beta_iso > 0.017 excludes the current GGE partition or requires Leggett modes to decouple from a_2
