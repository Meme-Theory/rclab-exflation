# Observational Excursion: What Can We See and When

**Team**: Einstein, Cosmic-Web, Little Red Dots, Hawking
**Date**: 2026-02-28
**Designated Writer**: Einstein
**Objective**: Map the phonon-exflation framework's observational predictions across redshift

---

## I. The Tau-Redshift Map

The phonon-exflation framework describes a universe whose internal geometry evolves through a single parameter tau, the Jensen deformation of the SU(3) fiber. The one-parameter scaling from Session 29Ab converts this evolution to physical time and redshift.

### The Conversion

| Quantity | Formula | Value (M_KK = 10^16 GeV) |
|:---------|:--------|:--------------------------|
| BCS transition time | t_BCS = 0.16 / M_KK | 1.3 x 10^{-41} s |
| BCS transition temperature | T_BCS ~ M_KK | ~10^{16} GeV |
| BCS transition redshift | z_BCS ~ T_BCS / T_CMB | ~10^{28} |
| Hubble rate at transition | H ~ 0.014 x M_KK | 1.4 x 10^{14} GeV |

The BCS transition occurs 12 orders of magnitude above the electroweak epoch (z ~ 10^{15}) and 22 orders above recombination (z ~ 1100). Everything we directly observe -- the CMB, galaxies, BAO, supernovae, quasar absorption lines, gravitational waves -- is deep in the post-freeze epoch (z << z_BCS).

The dimensionless modulus trajectory is M_KK-independent. Only the conversion to physical units (time, temperature, redshift) depends on M_KK. This makes M_KK the framework's sole free parameter, and the tau-redshift map is:

```
z = 0          Laboratory (present)           tau = tau_frozen
z ~ 0.5-3      DESI / Euclid / Rubin          tau = tau_frozen
z ~ 3-11       JWST / Roman                   tau = tau_frozen
z ~ 1100       CMB (Planck / CMB-S4)          tau = tau_frozen
z ~ 10^9       BBN                            tau = tau_frozen
z ~ 10^{15}    Electroweak epoch              tau = tau_frozen
z ~ 10^{28}    BCS transition                 tau -> tau_frozen (freezing)
z > 10^{28}    Pre-freeze (rolling)           tau(t) evolving
```

The critical observation: for every epoch accessible to any existing or planned instrument, the internal geometry is already frozen. The modulus has been trapped at tau_frozen for 10^{58} dynamical times by the time the CMB forms. The observable universe is the post-freeze universe.

---

## II. Before the Freeze (z > z_BCS)

### The Rolling Epoch

Before the BCS transition, the modulus tau rolls freely from the round metric (tau = 0) toward larger deformations. During this epoch, the physics is fundamentally different from anything we observe:

**Time-dependent gauge couplings.** The ratio g_1/g_2 = e^{-2*tau(t)} changes as the modulus rolls. At the round metric (tau = 0), g_1 = g_2 (unification). As tau increases, the U(1) and SU(2) couplings diverge. The rate of change dalpha/alpha = -3.08 * tau_dot (Session 22d, E-3). During the rolling phase, tau_dot is O(M_KK), producing dalpha/alpha ~ O(1) per Hubble time. This 15,000x violation of atomic clock bounds is irrelevant because no atomic clocks exist at z ~ 10^{28}.

**Time-dependent Newton's constant.** G_eff = G_12 / Vol_K(tau). The volume of the internal space Vol_K changes with the deformation, so the effective 4D gravitational constant varies during the rolling phase. The Friedmann equation receives a contribution from the modulus kinetic energy, giving an equation of state w ~ 1 (stiff matter, kinetic-dominated).

**Parametric particle creation.** As the modulus rolls, the Dirac eigenvalues shift in time, creating Bogoliubov quasiparticles via parametric amplification (KC-1). The particle creation spectrum is anti-thermal (B_k positively correlated with omega, Pearson r = +0.74 at tau = 0.50). The gap-edge modes are preferentially populated, with each Peter-Weyl sector ringing at its own characteristic frequencies. This is the Chladni pattern of the internal space -- resonance patterns on a compact manifold with discrete eigenvalues.

**The equation of state history.** The pre-freeze expansion is dominated by the modulus kinetic energy: rho_KE ~ tau_dot^2 * G_{tau,tau} ~ M_KK^4. With w ~ 1 (stiff matter), the scale factor grows as a(t) ~ t^{1/3}. The Hubble friction dissipates < 1% of the kinetic energy (Session 29Ab, 29b-2). The modulus rolls essentially undamped toward the BCS transition.

### Observational Status: Structurally Inaccessible

The rolling epoch is permanently inaccessible to observation. The comoving wavenumber of fluctuations produced during this epoch is k_transition = 9.4 x 10^{23} h/Mpc -- 24 orders of magnitude above the DESI observable window. The gravitational wave frequency from the transition is f_peak = 1.3 x 10^{12} Hz -- 17 orders above LISA. Without an inflationary epoch to stretch these fluctuations (the modulus rolls through a fraction of an e-fold), no large-scale structure signature can form.

This inaccessibility is structural, not a tuning failure. The formula k ~ M_KK * T_CMB / M_Pl shows that reaching k ~ 0.1 h/Mpc requires M_KK ~ 0.1 eV -- a macroscopic (~1 mm) compactification radius incompatible with any sensible particle physics. For any physically reasonable KK scale, the transition imprints at microscopic comoving distances.

---

## III. The Transition Epoch (z ~ z_BCS)

### Thermodynamics of the BCS Freeze

The BCS transition is a first-order phase transition (L-9: cubic invariant c = 0.006-0.007 in the (3,0)/(0,3) sectors). First-order transitions have three universal thermodynamic consequences, all computed in Session 29.

**1. Latent heat release.** The 3-sector BCS condensation energy F_BCS = -17.22 (spectral action units). In physical units: Q ~ |F_BCS| * M_KK^4. For M_KK = 10^{16} GeV, Q ~ 10^{64} GeV^4. Distributed among g_* = 106.75 relativistic species, the reheating temperature is T_RH ~ (Q/g_*)^{1/4} ~ M_KK ~ 10^{15-16} GeV. This is not a free parameter -- it is fixed by F_BCS and M_KK.

**2. Equation of state discontinuity.** At the transition surface, the equation of state changes from w ~ 1 (stiff, kinetic-dominated rolling) to w = 1/3 (radiation, from thermalized latent heat). The Israel-Darmois junction conditions require continuity of the induced metric and discontinuity of the extrinsic curvature, consistent with the sudden release of latent heat. The Friedmann equation:

H^2 = (8*pi*G/3) * [rho_stiff(t) + rho_rad(t)]

shows a sharp transition from stiff-matter domination to radiation domination at t_BCS.

**3. Entropy discontinuity.** The latent heat Q divided by the transition temperature T_BCS gives Delta_S = Q/T_BCS. This entropy is released into the 4D universe as radiation. The total entropy produced determines the photon number density, which determines the baryon-to-photon ratio eta through whatever baryogenesis mechanism operates at T ~ T_RH.

### The Sector Cascade

Different Peter-Weyl sectors have different BCS gaps (Delta varies by a factor of ~2 across sectors). The transition temperature T_c ~ Delta/(1.76 * k_B) is sector-dependent, so the sectors freeze at different tau values:

1. (3,0)/(0,3) sectors freeze first (largest gap, largest condensation energy)
2. Adjacent sectors follow in a cascade
3. The (0,0) singlet sector freezes last or not at all (smallest gap)

This produces a staircase in the equation of state -- each sector that freezes releases its latent heat in a separate step. However, ALL steps complete at T >> T_BBN by 12 orders of magnitude. The staircase is thermodynamically real but observationally invisible: by BBN (T ~ 1 MeV), all sectors have frozen and all latent heat has thermalized.

### The Trapping Mechanism

The modulus is trapped by kinetic energy extraction. The first-order transition acts as a one-way valve: adiabatic entry, sudden bubble nucleation, irreversible trapping. The trapping condition is KE < Q (kinetic energy less than latent heat). At mu_eff = 1.2 * lambda_min: KE/Q = 0.86 (trapped). At mu_eff = lambda_min: KE/Q = 2.13 (not trapped). The 20% sensitivity window between these scenarios is the principal remaining uncertainty (Section X of the Session 29 wrapup). KC-3's n_gap = 37.3 >> 20 (nearly 2x threshold) implies mu_eff substantially overshoots lambda_min, favoring trapping.

The Bianchi identity (Paper 06, contracted form nabla_mu G^{mu nu} = 0) ensures self-consistency: the modulus trajectory is not an independent postulate but a consequence of the 12D Einstein equations. The BCS condensate modifies the effective stress-energy tensor, the Bianchi identity propagates this into the modulus equation of motion, and the modulus halts where the transition extracts sufficient kinetic energy. This is EIH (Paper 10) applied to a compactification modulus: motion from geometry.

---

## IV. After the Freeze (z < z_BCS)

### The Frozen Vacuum

After the BCS transition, the internal geometry is frozen at the off-Jensen minimum within the U(2)-invariant family. All physical constants are determined by this frozen geometry:

| Quantity | Formula | Status |
|:---------|:--------|:-------|
| Gauge coupling ratio | g_1/g_2 = e^{-2*tau_frozen} | Framework-derived, zero-parameter |
| Weinberg angle | sin^2(theta_W) = L_2/(L_1 + L_2) | Framework-derived, zero-parameter (P-30w) |
| Mass ratio | phi_paasch = m_{(3,0)}/m_{(0,0)} | Framework-derived, zero-parameter |
| Fine structure constant | alpha_EM from RGE running | Framework-derived, needs RGE computation |
| Newton's constant | G_eff = G_12 / Vol_K(tau_frozen) | Fixed, absorbed into measured G |
| Cosmological constant | Lambda from BCS sector cancellation | Framework-derived, needs L-8 sector sum |
| Proton lifetime | tau_p ~ M_KK^4 / m_p^5 | One-parameter (M_KK) |
| Dark energy EOS | w = -1 exactly | Framework-derived, null prediction |

### The Equivalence Principle Is Satisfied Exactly

The frozen modulus means:
- **No varying constants.** dalpha/alpha = 0 at all z < z_BCS (clock constraint satisfied with infinite margin after freeze).
- **No fifth forces.** The modulus is trapped, not slowly rolling. No long-range scalar field mediates additional forces.
- **No Lorentz violation.** The condensate is rigid on all cosmological scales. The Jeans length of the frozen condensate is lambda_J ~ c_s * sqrt(pi / G*rho) where c_s ~ O(M_KK). For M_KK ~ 10^{16} GeV, lambda_J >> H^{-1}_0. The condensate does not respond to cosmological density perturbations.
- **Standard black hole physics.** G_eff is constant. The Hawking temperature T_H = hbar*c^3/(8*pi*G_eff*k_B*M) is unmodified for all astrophysical black holes (T_H << BCS gap). The Bekenstein-Hawking entropy S_BH = A/(4*l_P^2) is standard. The BCS ground state is a pure state with zero entropy and does not contribute to the black hole entropy budget.

The post-freeze universe IS the Standard Model on a standard FRW background with a specific cosmological constant. The framework does not predict exotic physics after the freeze. It predicts the Standard Model -- but for a REASON.

### Framework-Derived vs Framework-Adjacent

A critical epistemic distinction identified in this excursion (Cosmic-Web, Round 3): only predictions that follow from the KK reduction of the Dirac spectrum on SU(3) are framework-derived. Predictions imported from Volovik's emergent gravity program (condensate-dependent G_eff, sector-dependent graviton propagation) are framework-adjacent -- they require additional theoretical development not yet performed. This document restricts itself to framework-derived predictions.

---

## V. What Current Instruments Could See

### V.1 Laboratory (z = 0)

**Proton lifetime.** The framework predicts proton decay through superheavy KK gauge bosons with mass M_X ~ M_KK * g(tau_frozen). The lifetime scales as tau_p ~ M_KK^4 / (alpha_GUT^2 * m_p^5). For M_KK = 10^{16} GeV: tau_p ~ 10^{36} yr. The current Super-K lower bound is tau_p > 1.6 x 10^{34} yr (p -> e+ pi^0). Hyper-K (operational ~2027) projects sensitivity to ~10^{35} yr. This is a one-parameter (M_KK) prediction within the reach of a currently-under-construction experiment.

**Gauge couplings (already measured).** The framework predicts g_1/g_2 = e^{-2*tau_frozen} at M_KK, which must reproduce the measured ratio at M_Z = 91.2 GeV after SM RGE running. This is a zero-parameter test (after tau_frozen is determined by P-30w). The RGE computation is a two-part gate:
- Part A (ratio): Does e^{-2*tau_frozen} at M_KK run to the correct g_1/g_2 at M_Z? This requires only the SM one-loop beta functions (b_1 = 41/10, b_2 = -19/6) and tau_frozen. Zero free parameters.
- Part B (absolute normalization): Do the individual g_1(M_Z) and g_2(M_Z) match experiment? This requires the spectral action cutoff normalization, which introduces one parameter (equivalent to M_KK).

If Part A fails, the framework's spectral geometry produces the wrong Standard Model. Every observation at every redshift is then a falsification -- not through a specific smoking gun, but through the entire body of concordance physics.

**Weinberg angle (already measured).** sin^2(theta_W) = 0.23122 +/- 0.00003 (PDG). The framework predicts this from the off-Jensen BCS minimum: sin^2(theta_W) = L_2/(L_1 + L_2) where L_1, L_2 are the frozen metric scale factors. Pre-registered gate P-30w: sin^2(theta_W) in [0.20, 0.25]. Zero-parameter.

### V.2 DESI / Euclid / Rubin (z = 0 - 3)

**Dark energy equation of state: w = -1 exactly.** The frozen modulus (L-9 first-order trapping) guarantees zero post-freeze dynamics. The clock constraint (Session 22d, 15,000x margin) ensures dtau/dt = 0 to extraordinary precision. The framework predicts:

- w_0 = -1.000 (no deviation at any precision)
- w_a = 0.000 (no time evolution)

This is a genuinely falsifiable null prediction. It is not "w approximately equals -1" -- it is w = -1 as a consequence of a first-order phase transition, not a slow roll. DESI DR1 reported hints of w_a < 0 (dynamical dark energy). The framework predicts these hints will not survive with more data.

Pre-registered criterion: w_0 in [-1.05, -0.95], w_a in [-0.15, +0.15] at 95% CL. DESI DR2 (expected ~2026) and DR3 (~2028) test this directly.

This prediction distinguishes the framework from quintessence models, which generically predict w != -1. It is the single cleanest observational prediction because it requires NO additional computation beyond what Session 29 already established.

**BAO peak position as M_KK constraint.** The reheating temperature T_RH ~ M_KK determines (through baryogenesis) the baryon-to-photon ratio eta, which determines the sound horizon r_s at recombination, which determines the BAO peak position. DESI measures the BAO peak to ~0.5% precision. This constrains M_KK independently of proton decay, providing a consistency check: the SAME M_KK must satisfy both constraints. However, the BAO-M_KK chain requires assuming a baryogenesis mechanism, introducing model dependence.

**Growth rate: null prediction.** The framework predicts f*sigma_8 consistent with standard GR (G_eff = G_Newton exactly, no condensate-induced modification). The S8 tension (DESI sigma_8 = 0.777 vs Planck 0.811, ~1.5 sigma) is not explained by the framework unless gravity is derived as emergent from the condensate (Volovik's program), which is framework-adjacent, not framework-derived.

### V.3 JWST / Roman (z = 3 - 11)

**No unique predictions beyond concordance astrophysics.** The frozen ground state IS the Standard Model. Every photon JWST detects was emitted by processes governed by alpha_EM, alpha_s, G_F, and G_N -- all frozen at their post-BCS values, which are identical to their present values. Little red dots, high-z AGN, early massive galaxies -- all are governed by the same SM physics at z ~ 7 as at z = 0.

The "impossibly massive" JWST galaxies are not currently anomalous: BIC-preferred galaxy-only fits account for 75% of LRDs (Wang et al.), and BH mass estimates drop by 2-3 dex with electron scattering corrections (Rusakov et al., Nature 2025). The remaining tension is at the 1-2 sigma level against LCDM halo mass functions.

The framework's JWST prediction is the Standard Model itself. If the RGE-corrected gauge couplings match the SM (Section V.1), then JWST observations are automatically consistent. If they don't, every JWST observation is a falsification. There is no intermediate regime where high-z galaxies provide a unique constraint that laboratory measurements don't already provide more precisely.

**One indirect handle**: The BAO scale at z ~ 5-7 (DESI Lyman-alpha, ~2% precision) constrains the distance-redshift relation D_A(z) and H(z) at these redshifts. If M_KK is independently constrained by proton lifetime, the predicted BAO position at z ~ 5-7 is a one-parameter consistency test. But current precision is insufficient to be discriminating.

### V.4 Planck / ACT / SPT (z ~ 1100)

**N_eff prediction.** The default prediction is N_eff = 3.046 (standard). All KK tower modes have masses ~ M_KK and decay well before BBN (T_BBN ~ 1 MeV << M_KK ~ 10^{16} GeV).

However, if the BCS condensate breaks a U(1) symmetry (Cooper pair phase), the resulting massless Goldstone boson contributes to N_eff. The Goldstone decouples at T ~ M_KK (its coupling is suppressed by 1/M_KK) and contributes:

Delta_N_eff ~ (4/7) * (g_*(T_dec) / g_*(T_nu_dec))^{-4/3} ~ 0.027

for T_dec ~ 10^{15} GeV. This is below current Planck sensitivity (sigma(N_eff) ~ 0.18) but within projected CMB-S4 sensitivity (sigma ~ 0.03). The prediction is:

N_eff = 3.046 + 0.027 = 3.073

This is independent of M_KK to leading order (the Goldstone decouples at T >> 1 MeV regardless of the precise value of M_KK). It is a framework-derived prediction conditional on the BCS condensate breaking a U(1) -- which it does, since Cooper pairs carry a definite phase.

**CMB otherwise standard.** The framework predicts standard CMB physics (same recombination, same Thomson scattering, same acoustic peaks) because the frozen ground state produces standard electromagnetism and standard hydrogen physics. No anomalous spectral distortions, no non-standard recombination history, no unusual polarization patterns -- all of these would require post-freeze modulus dynamics, which the clock constraint forbids.

---

## VI. What Future Instruments Could See

### VI.1 Hyper-K (operational ~2027-2030)

**Proton decay.** Sensitivity to tau_p ~ 10^{35} yr in the p -> e+ pi^0 channel. For M_KK in the natural GUT range [10^{15}, 10^{17}] GeV, the predicted tau_p spans [10^{32}, 10^{40}] yr. The Hyper-K window overlaps the lower end of this range:

| M_KK (GeV) | tau_p (yr) | Hyper-K detectable? |
|:------------|:-----------|:--------------------|
| 10^{15} | ~10^{32} | Already excluded by Super-K |
| 10^{15.5} | ~10^{34} | Yes -- within reach |
| 10^{16} | ~10^{36} | Marginal -- requires extended run |
| 10^{17} | ~10^{40} | No -- beyond any foreseeable detector |

A Hyper-K detection would fix M_KK to ~0.5 dex precision. A null result pushes M_KK > 10^{16} GeV but does not falsify the framework.

### VI.2 CMB-S4 (projected ~2030)

**N_eff precision.** Projected sigma(N_eff) ~ 0.03. The framework predicts Delta_N_eff = 0.027 from the BCS Goldstone boson. CMB-S4 would measure N_eff = 3.07 +/- 0.03, placing the Goldstone contribution at the edge of detectability (~1 sigma). A definitive test requires a factor ~3 improvement beyond CMB-S4.

### VI.3 DESI DR2/DR3 (2026-2028)

**w(z) precision.** The framework predicts w = -1 exactly. DESI DR2/DR3 will determine w_0 and w_a to ~3% and ~0.15 precision respectively. If the DR1 hints of w_a < 0 persist, the framework is under pressure. If they wash out (as the framework predicts), this is a confirmed null prediction.

### VI.4 Next-Generation Gravitational Wave Detectors

**No framework-specific signal.** The GW spectrum from the BCS transition peaks at f ~ 10^{12} Hz, 17 orders above LISA and 10 orders above Einstein Telescope. No planned or conceivable detector reaches this frequency. The total GW energy from the transition contributes to the radiation budget at a level far below N_eff sensitivity.

However, the multi-peak structure from the sector cascade (5 sectors with distinct gaps producing 5 characteristic frequencies) is a zero-parameter structural fingerprint. If electromagnetic GW detection (inverse Gertsenshtein effect) ever reaches THz frequencies, this pattern would be distinguishable from any generic first-order transition. The probability of such a measurement within the foreseeable future is negligible.

### VI.5 Varying-Constants Experiments

**Null prediction: dalpha/alpha = 0.** The frozen modulus guarantees zero variation of fundamental constants at all post-freeze redshifts. Current constraints from quasar absorption lines: |dalpha/alpha| < 10^{-5} at z ~ 2-4 (Webb et al.; Murphy et al.). Future constraints from ELT-ANDES: projected |dalpha/alpha| < 10^{-6} at z ~ 2-4. The framework predicts all of these measurements will return null.

**Null prediction: dG/dt = 0.** Binary pulsar timing and lunar laser ranging constrain |dG/dt|/G < 10^{-13}/yr. The framework predicts this bound will hold at arbitrary precision. BH shadow measurements at different redshifts (EHT at z ~ 0.004 for M87, future ngEHT at higher z) provide independent constraints on G(z). The framework predicts G(z) = constant.

---

## VII. The Cognitive Dissonance -- What Standard Cosmology Misses

### The Standard View

Standard cosmology treats the early universe as "the same physics at higher temperature." The Standard Model is taken as given -- its gauge groups, coupling constants, and particle content are input parameters. Cosmology asks how matter and radiation evolve under these fixed rules. The cosmic microwave background, baryon acoustic oscillations, supernovae, and galaxy surveys all test this evolution, not the rules themselves.

### What the Framework Changes

The phonon-exflation framework says the rules have a REASON. The gauge group is the isometry group of the internal space (SU(3) for the fiber). The coupling constants are determined by the frozen geometry (g_1/g_2 = e^{-2*tau_frozen}). The particle spectrum is the eigenvalue spectrum of the Dirac operator on the fiber. The cosmological constant is the BCS condensation energy summed over Peter-Weyl sectors. None of these are input parameters -- they are output of the geometry.

The cognitive dissonance is this: for the entire observable universe (z < z_BCS ~ 10^{28}), the framework agrees with standard cosmology. It predicts the same expansion history (w = -1), the same growth rate (G_eff = G_Newton), the same BBN (standard eta), the same CMB (standard recombination), the same galaxy formation (standard SM physics). There is no exotic signature, no anomalous feature in P(k), no deviation from LCDM at any redshift where we have data.

The framework's predictions are not exotic. They are the SPECIFIC VALUES of the Standard Model parameters, derived from geometry rather than measured. The framework claims to explain WHY alpha_EM = 1/137, WHY sin^2(theta_W) = 0.231, WHY the proton is stable on timescales of 10^{36} years but not forever. Standard cosmology cannot make these claims because it takes the SM as given.

### The Testable Difference

The difference between "the SM is given" and "the SM is derived" becomes testable in exactly one way: the derived values must MATCH the measured values. If the off-Jensen minimum at P-30w produces sin^2(theta_W) = 0.231, that is not a fit -- it is a zero-parameter derivation of a number that standard cosmology treats as an input. If it produces 0.15 or 0.30, the framework is wrong.

The framework's greatest strength is that it explains the SM. Its greatest weakness is that -- for the observable universe -- it predicts the SM. Its testable content is concentrated in a handful of frozen-state predictions:

1. Does the derived Weinberg angle match the measured one?
2. Does the derived gauge coupling ratio, after RGE running, reproduce the measured alpha_EM?
3. Is the proton lifetime within the predicted range for consistent M_KK?
4. Is the derived cosmological constant within 10-20 orders of the observed one?

These are not features in the power spectrum. They are not anomalies in the expansion history. They are the PARAMETERS of the concordance model itself. The framework's prediction is not "there will be a bump at 47 Mpc." It is: the values of sin^2(theta_W), alpha_EM, tau_p, and Lambda that define the Standard Model should follow from the BCS sector sum with zero free parameters beyond M_KK.

### The Pre-Freeze Universe as Explanation, Not Observation

The pre-freeze universe (z > 10^{28}) is where the framework differs most dramatically from standard cosmology -- rolling couplings, time-dependent Newton's constant, parametric particle creation, the BCS phase transition itself. But this epoch is permanently inaccessible. The 24-order gap to the nearest instrument is not a parameter that can be tuned away; it is a structural consequence of compactification at the GUT scale.

The pre-freeze epoch is an EXPLANATION, not an OBSERVATION. It explains why the post-freeze universe has the specific parameters it has. The observable consequences are the frozen-state values. We do not need to see the BCS transition directly. We live in its aftermath.

---

## VIII. Priority Observational Tests

### The One-Parameter Consistency Web

The framework has one free parameter: M_KK. Multiple independent observables constrain this single parameter. If one value of M_KK satisfies ALL constraints simultaneously, the framework passes a multi-observable consistency test. If no value of M_KK can satisfy them simultaneously, the framework is falsified.

```
                         M_KK
                        / | \
                       /  |  \
                      /   |   \
            tau_p    eta  |   g_i(M_Z)
           (Hyper-K) (BBN)|   (colliders)
                      \   |   /
                       \  |  /
                        \ | /
                     Consistency
```

### Ranked by Immediacy and Decisiveness

**Tier 1 -- Pre-registerable now, testable within 5 years:**

| Test | Type | Parameters | Instrument | Timeline | Pre-registered criterion |
|:-----|:-----|:-----------|:-----------|:---------|:------------------------|
| w = -1 exactly | Null prediction | 0 | DESI DR2/DR3 | 2026-2028 | w_0 in [-1.05, -0.95], w_a in [-0.15, +0.15] |
| sin^2(theta_W) at off-Jensen | Internal consistency | 0 | Computation (P-30w) | Session 30 | [0.20, 0.25] |
| Proton lifetime | Positive prediction | 1 (M_KK) | Hyper-K | 2027-2035 | tau_p in [10^{34}, 10^{38}] yr |

**Tier 2 -- Testable with existing data, requires framework computation:**

| Test | Type | Parameters | Instrument | Prerequisite |
|:-----|:-----|:-----------|:-----------|:-------------|
| RGE consistency (ratio) | Gate | 0 | Existing collider data | P-30w (tau_frozen) |
| RGE consistency (absolute) | Gate | 1 (M_KK) | Existing collider data | Spectral action normalization |
| BAO as M_KK constraint | Consistency | 1 (M_KK) | DESI | Baryogenesis model |

**Tier 3 -- Directional predictions, not yet quantitative:**

| Test | Type | Parameters | Instrument | Prerequisite |
|:-----|:-----|:-----------|:-----------|:-------------|
| N_eff = 3.073 | Positive prediction | 0 | CMB-S4 | Goldstone coupling calculation |
| dG/dt = 0 | Null prediction | 0 | LLR / binary pulsars | None (already constrained) |
| dalpha/alpha = 0 | Null prediction | 0 | ELT-ANDES | None (already constrained) |

**Tier 4 -- Theoretical, requires new computation:**

| Test | Type | Parameters | Prerequisite |
|:-----|:-----|:-----------|:-------------|
| Lambda from sector cancellation | Positive prediction | 0 | Full L-8 sector sum + renormalization |
| CKM phase from off-Jensen geometry | Positive prediction | 0 | Paper 18 CP formalism at BCS minimum |
| Multi-peak GW fingerprint | Structural signature | 0 | THz GW detection technology |

### The RGE Gate: Existential, Immediate

The single most important computation for observational contact is the RGE running of g_1/g_2 from M_KK to M_Z. This can be performed NOW, before P-30w, as a function of tau_frozen. The result determines whether the framework can produce the Standard Model at all. If it fails, every observation at every redshift is a falsification. If it passes, the framework is consistent with the entire body of existing measurements -- not as a fit, but as a derivation.

The RGE gate is a prerequisite for all other tests. It should be computed in Session 30 alongside P-30w.

---

## Closing

The phonon-exflation framework makes its observational predictions through a single structural fact: the BCS condensation on Jensen-deformed SU(3) freezes the internal geometry at a specific point, and that frozen geometry determines the Standard Model parameters. The observable universe is the post-freeze universe. The pre-freeze epoch -- where the physics is most dramatically different from standard cosmology -- is permanently inaccessible.

The framework's testable content is concentrated in frozen-state predictions: gauge couplings (RGE gate), the Weinberg angle (P-30w), proton lifetime (Hyper-K), the cosmological constant (sector cancellation), and N_eff (BCS Goldstone). These are connected through a one-parameter consistency web anchored by M_KK.

The sharpest near-term prediction is w = -1 exactly -- a null prediction derived from the first-order BCS freeze, testable by DESI DR2. The framework predicts that DESI's DR1 hints of dynamical dark energy will not survive. This is pre-registerable today.

The crown jewel remains P-30w: the zero-parameter Weinberg angle at the off-Jensen BCS minimum. If it matches, the geometry speaks. If it misses, the miss is honest.

We do not need to see the faucet fall. We see the frozen pattern it left behind. The question is whether that pattern matches the Standard Model -- and this question has a computable answer.

---

*Observational Excursion filed by Einstein-Theorist (designated writer), with contributions from Cosmic-Web-Theorist (sector cancellation channel, framework-derived distinction, Jeans length argument), Little-Red-Dots-Analyst (RGE two-part gate, one-parameter consistency web, LRD concordance assessment), and Hawking-Theorist (w = -1 prediction, entropy staircase, N_eff analysis, observational pyramid). Three rounds of discussion across four domains: general relativity, large-scale structure, high-z observational astronomy, and black hole thermodynamics. 2026-02-28.*
