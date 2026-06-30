# Crystal to Cosmos: A Cosmologist's Assessment of Phonon-Exflation

**Author**: Katie Mack (Cosmic Bridge Agent)
**Date**: 2026-03-23 (original, S57); **comprehensively expanded 2026-05-25 (S93-era whole-project view)**
**Sources**: Framework documents, Sessions 57-93 results, knowledge MCP (constants/theorems/closed/gates), `canonical_constants.py`, Mack/Greene corpus (Papers 01-30)

> **Revision note (S93)**: This document was written at Session 57. In the ~36 sessions since, the framework's cosmology + observational-contact domain changed more than any other. The headline conclusion of the original draft — that the cosmological constant was "112-114 orders of magnitude above observation" with a resolving "mechanism [that] does not yet exist" — is *no longer the framework's state*: the entire DILUTION-CC resolution apparatus (S66) postdates the original draft. I have rewritten the CC treatment, the spectral-index treatment, the tensor-to-scalar treatment, the dark-matter abundance mapping, and the BBN section to the current state, and added the observational program (falsifier inventory, pre-registered observations, the f_NL bispectrum and GW arcs, the §VII cross-pillar cosmology bridges) that the original never covered. I have kept my register: I report only the kind of truth I could rederive mathematically, I keep "what the data shows / what it suggests / what it does not address" as three distinct categories, and I have not converted genuine open frontiers into fabricated resolutions. Where a result is scheme-dependent I write it as a (value, scheme) pair, not a bare number. Provenance for every number is pinned to a `canonical_constants.py` entry, a permanent theorem, a closed mechanism, or a gate verdict.

---

## 1. Executive Summary

The phonon-exflation framework proposes that Standard Model particles are phononic excitations of M^4 x SU(3), with a one-parameter internal deformation (the Jensen metric, parameterized by tau) serving as a cosmological clock. It is not an alternative to LCDM in the sense that quintessence or f(R) gravity are alternatives. It is an attempt to derive LCDM's inputs -- the particle spectrum, the dark matter abundance, the cosmological constant, the expansion history -- from the spectral geometry of a compact internal manifold. The ambition is extraordinary. The execution, after 93 sessions of systematic computation, is the most thoroughly self-audited theoretical framework I have encountered.

Let me be precise about what I mean by that. This is a framework that has closed 32+ of its own proposed mechanisms by theorem, that computes its predictions to machine epsilon and then tests them against pre-registered gates, and that distinguishes between what it has proven (at numerical precision 10^{-15}) and what it claims (with stated uncertainties). The algebraic skeleton -- KO-dimension 6, SM quantum numbers from C^16, CPT as a theorem, gauge coupling ratios from Jensen metric components -- is mathematically proven and does not depend on the stabilization mechanism or the cosmological interpretation. This is genuinely impressive algebraic geometry.

But a cosmologist does not evaluate frameworks on internal consistency alone. The question is: does the framework make contact with the observable universe in ways that are both specific enough to be tested and novel enough to be interesting? When I wrote the first version of this assessment at Session 57, my answer was a heavily qualified "in the right ballpark, but with a fatal CC problem." That answer is out of date in three structurally important ways, and the honest thing to do is state the reversal up front.

**First, the cosmological constant is no longer the framework's catastrophe.** At S57 the framework had a positive CC of the right sign but the wrong magnitude by ~114 orders, and I described the resolving mechanism as nonexistent. Session 66 (DILUTION-CC-66, PASS) supplied it. The mechanism is Volovik's q-theory tracking vacuum: the vacuum energy is not static but tracks the expansion as rho_vac(t) ~ M_Pl^2 H(t)^2 (Volovik 2003 §29.4; Klinkhamer-Volovik q-theory, the framework's Volovik Papers 25/35). As H falls from the GUT scale to its present value, the M_Pl^2 H^2 reservoir is diluted to the observed dark-energy density. The closure computes rho_vac/rho_obs = 1.032 — a 0.01-order-of-magnitude residual, not 114. The number `CC_OOM = 115.5` (canonical, S66 W1-A) is the *dilution depth* the tracking vacuum traverses, not a measure of failure. This is the single biggest change since S57, and I lay out the substitution chain in §3b.

**Second, the spectral index is no longer a 262-sigma deficiency.** At S57 the framework's only n_s was the naive Kibble-Zurek power-law fit, n_s = 2.065, which is blue, wildly inconsistent with Planck, and was correctly flagged as closed. But that was the wrong observable — a fit to the post-transit excitation spectrum P(K), not the curvature-perturbation tilt at the CMB pivot. The Hubble slow-roll route (opened S42, first-viable S62 at n_s = 0.9567, triple-confirmed as a Bogoliubov-invariant in S73a, and made gauge-invariant in S84-85 via the exact identity eps_BLV = 2 - 1/eps_SA) gives the canonical prediction `n_s_framework = 0.9561`. Against Planck's 0.9649 +/- 0.0042 that is 2.1 sigma; against the wider 0.0062 error bar, 1.4 sigma. O(1) sigma, not 262. The headline deficiency of the original draft is superseded (§5.2).

**Third, several "gaps" I flagged as decisive are now computed.** The dark-matter abundance factor-of-3 ambiguity — which I called "the single most important unresolved issue" — is closed by LEGGETT-MOMENT-70 (a Type-F single-summand-projection trace that fixes the mapping with no interpretive freedom), giving Omega_DM h^2 ~ 0.120, within ~1% of Planck (§3a). The tensor-to-scalar ratio is no longer 3.86e-10-and-unobservable; the dual-pathway program gives r in the 0.007-0.012 range, comfortably under BICEP/Keck (r < 0.036) and within LiteBIRD/CMB-S4 reach (§6 Test 2). BBN is no longer "entirely conceptual" — BBN-VOLOVIK-67 passes and the S75 thermalization theorem shows ~10^14 e-folds erase the GGE initial conditions, returning N_eff = 3.044 to machine precision (§5.3). And the late-time ISW channel (ISW-TRACKING-68) gives a +12.3% cross-correlation signal relative to LCDM, the framework's first genuine late-time observable (§3e).

What has NOT changed is my discipline about the difference between a reformulation and a measurement, and about which of these results the data actually tests. The CC resolution rests on an ASSUMED-PARTIALLY-PROVEN scaling form (assumption C10: that rho_vac ~ M_Pl^2 H^2 holds at the substrate-IS level), and the late-time dark-energy equation of state w_0 carries a genuine two-value ambiguity (-0.918 canonical vs -0.842454 on the R_842 branch) that only DESI DR3 will settle. The f_NL folded-shape bispectrum is the framework's most distinctive signature but is, on current forecasts, detector-sterile even at a cosmic-variance-limited 21cm survey. I will be explicit throughout about which claims the data confirms, which it merely allows, and which it does not yet touch.

The framework is not dead. It is not vindicated. It occupies a narrow but mathematically well-defined corridor of viability — substantially better-mapped in the cosmology domain than it was at S57 — and it makes predictions that the next decade of experiments (DESI DR3, CMB-S4, LiteBIRD, LISA, SKA-21cm) can test. What follows is my detailed map of where it connects to real cosmology, where it departs, and what observations would settle the question.

---

## 2. What the Framework Claims

The core mechanism, as described in `Phononic-framework-hypothesis.md` and refined through 57 sessions, proceeds in five steps:

**Step 1: The internal geometry.** The universe has the product structure M^4 x K, where K = SU(3) equipped with the Jensen metric g_tau. This metric scales three blocks independently -- u(1), su(2), and the C^2 coset -- parameterized by a single number tau:

    L_1 = e^{2*tau}     (u(1), 1 direction)
    L_2 = e^{-2*tau}    (su(2), 3 directions)
    L_3 = e^{tau}        (C^2, 4 directions)

The volume is exactly preserved: L_1 * L_2^3 * L_3^4 = 1 for all tau. This is a theorem (`Phononic-Crystal-Geometry.md`, S12).

**Step 2: The Dirac spectrum.** The Dirac operator D_K(tau) on (SU(3), g_tau) has a discrete eigenvalue spectrum that is block-diagonal in the Peter-Weyl basis (10 independent sectors at max_pq_sum = 3), proven to machine epsilon (S22b). The spectrum encodes particle quantum numbers through KO-dimension 6 classification (S7-8). The CPT theorem is hardwired: [J, D_K(tau)] = 0 identically (S17a).

**Step 3: The BCS condensation.** At tau ~ 0.19, a van Hove singularity in the B2 flat band produces a divergent density of states. BCS pairing occurs with exactly N_pair = 1 Cooper pair in the singlet (0,0) sector (S53). The system is not a macroscopic superfluid -- it is a single quantum of vibration on a 32-cell tessellation of SU(3), in the Mott insulator regime (E_J/E_c = 0.818 < 1).

**Step 4: The transit.** The modulus tau is not stabilized at the fold -- all 32+ static stabilization mechanisms are closed by theorem. Instead, tau transits through the fold at terminal velocity v = 442.4 M_KK, producing a sudden quench that shatters the BCS condensate (P_exc = 1.000 for the single-cell case, P_exc = 0.081 for the 2-cell case at physical rate). The post-transit state is a Generalized Gibbs Ensemble (GGE) protected from thermalization by exact integrability (8 Richardson-Gaudin conserved quantities, block-diagonal theorem).

**Step 5: The cosmological identification.** The framework identifies:
- Dark matter = quasiparticle excitations of the GGE relic (Leggett mode parametric excitations + BCS quasiparticles). As of S70 the mass anchor is sharpened: the Leggett channel closes as a Type-F single-summand-projection trace on the algebra A_K (LEGGETT-MOMENT-70), giving Omega_DM h^2 ~ 0.120 with no interpretive freedom in the mapping (§3a).
- Cosmological constant = the a_0 zeroth spectral-action moment, a non-equilibrium vacuum-energy residual (E_GGE - E_BCS > 0, positive). Crucially, as of S66 this residual is not static — it is diluted by the Volovik tracking vacuum as the universe expands (DILUTION-CC-66; §3b). The CC is a *different spectral moment* than gravity (a_2) or the gauge sector (a_4): the spectral action's a_0/a_2/a_4 are independently Volovik-self-tuned.
- Expansion = acoustic, driven by the 229x sound speed hierarchy (c_fabric/c_Gold = 229.5) through the BLV metric. The transit is supersonic (Mach 13.75 through the van Hove fold — impulsive, not quasi-static), which is the substrate's reason it is "exflation, not inflation": spectral complexity grows inside each point, the eigenvalue spectrum reorganizes; space is not metrically inflating. After the transit the late-time expansion history is read through the emergent FRW metric, where the framework now has w_0, the ISW signal, and N_eff (§3e, §5.3, §5.4).

A note on direction, because it governs every identification above. The substrate IS the spectral triple (A_K, H_K, D_K); it is not a field living IN a pre-existing spacetime. Space is an emergent description of how the fabric's spectral weight distributes itself: the 4D metric g_M emerges from the a_2 Seeley-DeWitt coefficient, Newton's constant is the second spectral moment, the cosmological term is the zeroth. Every cosmological observable below flows D_K eigenvalues -> spectral-action moments -> emergent FRW quantity -> measured number. When I compare against LCDM, LCDM is the comparison container, not the explanation.

---

## 3. Where It Connects to Real Cosmology

### 3a. Dark Matter

The framework's DM candidate is a quasiparticle excitation spectrum -- the Leggett mode parametric excitations plus intra-cell BCS pair-breaking quasiparticles produced by the transit quench. Session 57 (W2-4, FABRIC-DM-ABUNDANCE-57) only bracketed the prediction (Omega_DM h^2 in [0.017, 0.188], with a factor-3 ambiguity between two interpretations of the energy-to-density mapping). **That ambiguity is now closed.** Session 70 (LEGGETT-MOMENT-70, PROVEN) identifies the Leggett channel as a Type-F single-summand-projection trace on the algebra A_K — an *algebra-INVARIANT* observable in the 4-corner classification, which means it is a spectrum-only functional with no state-dependent freedom. The mass anchor is Mass_LeggettDM / Delta_BCS = 11.97 at zero free parameters, and the abundance follows.

**Substitution chain — CLAIM 2 (the factor-3 mapping is closed; Omega_DM h^2 ~ 0.120):**

    Step 1: Omega_DM h^2 (Leggett-only) = (F_Leggett-anchored mass moment)   [LEGGETT-MOMENT-70, Type-F single-summand trace on A_K, Door-S70]
    Step 2:                              = 0.03985 * 3.010                    [Leggett-channel anchor x multiplicity; s70_leggett_moment]
    Step 3:                              = 0.11995                            [LEGGETT-MOMENT-70 PASS; Sage-exact 0.1199485]
    Step 4: Planck reference: Omega_DM h^2 = 0.1186 +/- 0.0020 (Planck 2018, Paper 29); canonical pin Omega_DM_obs = 0.264 (Planck 2020 DR2) -> 0.264 * 0.674^2 = 0.11993
    Step 5: |0.11995 - 0.1186| / 0.1186 = 1.14%  (vs Planck 2018);  |0.11995 - 0.11993| / 0.11993 < 0.1%  (vs the DR2-anchored pin)
    Conclusion: Omega_DM h^2 ~ 0.120, agreeing with the observed cold-dark-matter density to ~1% (Planck 2018) / sub-1% (Planck 2020 DR2). The Type-F trace fixes the mapping; the S57 "Interpretation A/B factor-3" freedom is superseded — there is no longer a choice to make.

I want to be careful about what category this is. What the data *shows*: the framework's zero-parameter Leggett-only anchor lands on the measured CDM density to ~1%. What it *suggests*: that the Type-F classification is the right way to read the abundance (the alternative readings the S57 draft entertained are not just disfavored, they are structurally excluded). What it does *not* address: the full multi-channel Volovik partition still carries internal structure I discuss next, and the absolute mass scale of the Leggett quasiparticle (which sets free-streaming) is anchored to Delta_BCS, not measured. A ~1% agreement with one free-parameter-free anchor is comparable in weight to the original WIMP-miracle coincidence — noteworthy, not a proof.

**The Volovik energy partition (why so much goes to the vacuum).** The reason the matter sector is small relative to the total fabric energy is the Volovik partition (S58): the Josephson condensation energy F_Josephson = -336.6 (in M_KK units) is overwhelmingly negative and routes to the vacuum sector (95.9% of the total), while the matter sector F_BCS + F_BA + F_Leggett = 14.411 is what becomes dark matter plus baryonic-analog content. This is the substrate's version of "why is Omega_m << 1": most of the post-transit fabric energy is vacuum (a_0 channel), not matter. The dark-matter *fraction* f_DM carries some scheme-dependence worth flagging as a (value, scheme) pair: f_DM = 0.209 (Leggett-only energy fraction, S58 — the "sole bottleneck" the framework flagged) vs f_DM = 1.000 within the substrate matter sector (S86), against an observed f_DM = Omega_DM/Omega_m = 0.844. The Leggett-only-vs-full-sector spread is a real open question about which channels inherit into the cosmological matter budget; it does not undermine the LEGGETT-MOMENT-70 abundance anchor, which is a mass-moment trace, not a fraction.

This is the right ballpark — better than ballpark, now — which is noteworthy. But let me map the constraints this candidate would face against what my papers actually say.

**Relic abundance.** Standard thermal relic dark matter satisfies Omega_chi h^2 ~ 3 x 10^{-27} cm^3 s^{-1} / <sigma v> (Paper 10, Sec. 2). The phononic DM is not a thermal relic -- it is produced by a sudden quench, analogous to Parker (1969) cosmological particle production. The abundance is set by the Bogoliubov squeezing formula, not freeze-out. This is conceptually legitimate -- it is the same mechanism that produces particles in an expanding universe, applied to the internal SU(3) transit. The framework computes this from the Leggett mode frequency ratios omega_i/omega_f during the quench, with zero free parameters (S57 W1-2).

**Self-interaction constraints.** Paper 10 reviews the SIDM cross-section window: sigma/m ~ 0.1-10 cm^2/g is needed to explain core-cusps while satisfying cluster constraints. The phononic DM consists of quasiparticle excitations with infinite lifetime at N_pair = 1 (Gamma/omega = 0 exactly, S53). These excitations propagate ballistically on the internal lattice. Their self-interaction cross section is identically zero at N_pair = 1 -- there is literally nothing to scatter off. This is both a strength (CDM-like behavior, T^{0i} = 0 by construction, S44 W1-2) and a weakness (no self-interaction means no solution to small-scale problems, and the SIDM window is unexplored).

**Stability is now a gated result, not an assumption.** At S57 the DM's infinite lifetime rested on the integrability protection. The obvious worry — and one I would have pressed — is gravitational decay: even a perfectly integrable quasiparticle can radiate gravitons. Session 67 computed this (LEGGETT-GRAV-DECAY-67, PASS): the gravitational decay vertex <g,g|H_grav|L> gives Gamma_grav < H_0, so the Leggett dark matter survives a Hubble time. The graviton gap provides the same kinematic protection for gravitational decay that the BCS gap provides for quasiparticle decay (the Leggett mode at omega_L = 0.138 M_KK cannot decay into the gapped graviton sector). The framework also proved that *single*-Leggett gravitational decay is FORBIDDEN (S67, three-line kinematic argument). So the stability claim is no longer "assume integrability" — it is "the one decay channel a cosmologist would worry about has been computed and it is slow enough." This is exactly the kind of result I wanted to see, and the framework produced it.

**Free-streaming constraints.** Paper 16 derives a combined constraint z_tr > 6.2 x 10^7 for hidden-sector DM, where z_tr is the redshift at which the DM becomes non-relativistic. The phononic DM has a dispersion relation omega(K) = 2J(1 - cos Ka) on the 32-cell lattice, with maximum group velocity c_Gold = 0.915 M_KK. Whether this velocity constitutes "relativistic" depends on the mapping between M_KK and cosmological scales. At M_KK ~ 10^{16} GeV (GUT scale, from T_init = 8.32 x 10^{15} GeV), the DM would be non-relativistic from very early times, likely satisfying the Paper 16 constraint. But this has not been computed explicitly. It should be.

**Annihilation signals.** Papers 01, 04, and 17 describe DM annihilation phenomenology. The phononic DM at N_pair = 1 has no annihilation channel -- the quasiparticles are exactly stable by integrability protection. This prediction is falsifiable: if DM annihilation signals are definitively detected (e.g., in the circumgalactic medium at z ~ 20-40, Paper 04), the phononic DM candidate is excluded.

**What I wanted computed — and what came back (T(k)).** At S57 I flagged the matter power spectrum transfer function T(k) as "the single most impactful computation the project could do," because Paper 15's hidden-sector methods apply directly and the phononic DM has a specific dispersion relation. The framework computed it (S58 transfer-function work, now consolidated in `framework-dm-properties.md`): **T(k) = 1.0000 at all observable scales — CDM-like across the entire probed range.** This is the cleanest possible answer for compatibility with Lyman-alpha forest data (Lyman-alpha constrains WDM to m_WDM > 5.3 keV via an exponential cutoff; T(k) = 1 has no cutoff and is unconstrained). It is also, candidly, the *least distinctive* answer — it means small-scale structure does not discriminate the phononic DM from vanilla CDM. The framework also records an effective warm-DM mass and free-streaming horizon in the same registry; the free-streaming constraint from Paper 16 (z_tr > 6.2e7) is satisfied because at M_KK ~ 10^16 GeV the Leggett quasiparticle is non-relativistic from extremely early times. So the test I wanted is done, it passes, and the lesson is that the phononic DM is observationally CDM-like at the power-spectrum level — the discriminating signatures live elsewhere (annihilation nulls, the f_NL bispectrum shape, §6).

### 3b. Dark Energy and the Cosmological Constant

Session 57 (W2-3, CC-SIGN-57) establishes that the CC has the correct sign:

    Lambda_eff = E_GGE - E_BCS = +1.709 M_KK > 0

This is the "anti-binding energy" interpretation: destroying the BCS condensate by the transit quench releases binding energy as positive vacuum energy. The equation of state w_GGE = -0.408 satisfies w < -1/3 (accelerating expansion). The 3He-B analog is exact: a quenched superfluid produces a positive energy excess that drives acoustic expansion.

The sign is correct. At Session 57, the magnitude looked catastrophically wrong — Lambda_eff/Lambda_obs ~ 1.93e114 — and I devoted most of this section to the reformulation-vs-solution distinction. **That assessment is superseded.** The resolving mechanism I called nonexistent was supplied by Session 66 (DILUTION-CC-66, PASS), and it is worth being precise about why it is a solution and not a relabeling.

The error at S57 was a static reading. A CC of 10^114 x observed is only a problem if the vacuum energy is *constant* (rho_vac ~ H^0). The framework's vacuum is not constant. In Volovik's q-theory — which this framework is a concrete substrate realization of — the equilibrium vacuum energy is exactly zero (the Gibbs-Duhem relation forces Lambda = 0 in the self-consistent ground state), and the *observed* dark energy is the small departure from equilibrium that tracks the expansion: rho_vac(t) ~ M_Pl^2 H(t)^2 (Volovik 2003 §29.4; Klinkhamer-Volovik q-theory, framework Volovik Papers 25 §V / 35). This is assumption C10 in the framework's ledger — ASSUMED-PARTIALLY-PROVEN, meaning the scaling form is taken as the Volovik q-theory ansatz at the substrate-IS level, not yet derived from the spectral triple from first principles. I flag that honestly: the resolution is conditional on C10.

**Substitution chain — CLAIM 1 (DILUTION-CC closes the CC gap; the magnitude is no longer a 114-OOM failure):**

    Step 1: Lambda_naive / Lambda_obs ~ 1.93e114      [S57 value; M_KK^4-scale GGE excess read STATICALLY]
    Step 2: rho_vac(today) = M_Pl^2 * H_0^2           [Volovik q-theory tracking law; C10 ASSUMED-PARTIALLY-PROVEN, S66; rho_vac ~ H^2, NOT H^0]
    Step 3: ratio = rho_vac(tracking) / rho_obs       [DILUTION-CC-66 substitution; H tracks down from the GUT scale to H_0 as the universe expands]
    Step 4:       = 1.032                              [S66 W1-A PASS, s66_w1a_dilution_cc.npz; 0.01-OOM residual]
    Step 5: 1.032 ~ 1  ==>  the H^2-tracking vacuum dilutes the M_Pl^2 H^2 initial reservoir to the observed value as H falls; the 114-OOM "gap" was the static (H^0) misidentification, NOT a tuning problem.
    Conclusion: the CC magnitude is RESOLVED at 0.01 OOM under Volovik tracking. The canonical number CC_OOM = 115.5 (S66 W1-A) is the dilution DEPTH the vacuum traverses, not a failure metric.

Let me hold this against the standard CC problem honestly. Paper 09 (Frieman-Turner-Huterer) states the discrepancy as rho_vac(predicted)/rho_vac(observed) ~ 10^120 *for a static vacuum*. The framework's claim is precisely that the vacuum is not static — the same move Volovik makes in the helium-droplet program. So the comparison is not "framework 10^114 vs standard 10^120, both bad"; it is "the framework adopts the tracking vacuum that makes the depth a feature." What the data *shows*: nothing yet directly — this is a theoretical resolution, not a measurement. What it *suggests*: that the dark-energy density today is parametrically M_Pl^2 H_0^2, which is the coincidence the tracking picture is built to explain. What it does *not* address: whether C10's scaling form survives a first-principles spectral-triple derivation (it is on the assumption ledger, anchored at `framework-cc-oom.md` and the W11 Volovik CC Tracking Wall; the §VII.AT cross-pillar registry slot for it is currently OPEN). The reformulation has become a resolution *conditional on C10* — a much stronger statement than the S57 "it might be progress," but still a conditional one, and I will not overstate it.

This also dissolves the integrability tension I made central at S57. I argued that the same integrability protecting the DM forced the CC too large, because getting from ||f^GGE - f^eq|| = 0.195 to 10^-57 per mode required breaking integrability. That argument assumed the static reading. Under tracking, the GGE excess does not need to be tuned to 10^-57 — it is diluted dynamically by the expansion. The DM stays integrable (LEGGETT-GRAV-DECAY-67) AND the CC comes out right (DILUTION-CC-66). The two are no longer in tension. The "integrability problem" framing of the original draft is retired.

**DESI constraints — the live discriminant.** This is where the framework still has genuine observational skin in the game, and where my reading has sharpened rather than reversed. The dark-energy equation of state carries a real two-value ambiguity that I write as a (value, scheme) pair: w_0 = -0.918 (canonical, the Volovik partition + effacement Gamma_eff = 0.99970, S58) OR w_0 = -0.842454 (the R_842 branch-(iv), substrate-compaction reading where the fiber tau tracks density, S85 W10-2). Both give w_a = 0 from the four-fold structural lock. DESI DR2 measured w_0 = -0.752 +/- 0.057 (DR2-DESY5). Post-Dovekie (2026), the framework's sigma-distances are 2.130 sigma for the canonical w_0 = -0.918 and 0.731 sigma for the branch-(iv) -0.842454 — i.e., the branch-(iv) value is currently the better fit to DESI. The framework has pre-registered a binding falsifier rectangle, R_842 = [-1.05, -0.85] x [-0.2, +0.2] in (w_0, w_a), under the S84-DR3-RESPONSE-PROTOCOL: DESI DR3 (Window-14) is the binding instrument. If DR3's (w_0, w_a) posterior lands outside R_842, the substrate-compaction branch is falsified; if it lands inside and confirms w_a significantly nonzero, the canonical w_a = 0 four-fold lock is challenged. Either way this is a clean, pre-registered, soon-resolved test — the framework is not hiding from it. (Note: which late-time value the substrate actually predicts is itself regulator-conditional — the zeta-branch Penrose diagram gives w_0 ~ -0.997 while the Zubarev branch gives ~ -0.494; the R_842 rectangle is the framework's honest pre-registration of that uncertainty, not a point prediction dressed up as one.)

### 3b-ii. The Overshoot, the Tracking Vacuum, and the Expansion Engine (S66 update)

At S57 this subsection was titled "A Reframing" and I ended it by saying it was "an agenda, not a result." The agenda has since been executed (DILUTION-CC-66, S66), so I have retitled it and rewritten the head. The S57 reframing — that the large initial vacuum energy is the expansion engine rather than a catastrophe — turned out to be the right intuition, and the Volovik tracking vacuum is the mechanism that makes it quantitative. I preserve the literature connection to Greene-Levin below because it remains the closest published analog, and I preserve the cautions that are still live (the C10 conditionality, and the e-fold question, which is a *separate* issue from the CC magnitude).

**The standard framing** is: the framework predicts Lambda_eff = 1.709 M_KK, observation gives Lambda_obs ~ 10^{-120} M_Pl^4, and the ratio 10^{114} is a catastrophic failure *if the vacuum is static*. This is how I assessed it at S57, and how Frieman-Turner-Huterer (Paper 09) frame the standard CC problem: rho_vac(theory) ~ 10^{113} J/m^3 while rho_vac(observed) ~ 10^{-9} J/m^3, a 120-order discrepancy.

**The reframing** is: the large initial vacuum energy is not the problem -- it is the expansion engine. In any QFT on a compact internal space, the initial state at tau = 0 (the round metric on SU(3)) carries vacuum energy of order M_KK^4. This is expected. It is the same scale that Paper 19 (Greene-Levin) identifies when they write rho_Casimir ~ alpha/b^{4+n} for Casimir energy on compact dimensions -- the vacuum energy density on a space of characteristic size b goes as b^{-(4+n)}, which at the KK scale is enormous. Nobody disputes that a compact manifold at the Planck or GUT scale carries vacuum energy of this magnitude. The question is what happens to it.

What happens, in the phonon-exflation framework, is a sector-by-sector cancellation cascade. The S57 data (W2-3, CC-SIGN-57) gives the per-sector decomposition of the non-equilibrium vacuum energy via the Volovik formula Lambda_k = delta_n_k * (E_k - mu_eff_k):

    Sector   | Lambda_k (M_KK) | Physical origin
    ---------|-----------------|---------------------------
    B2       | +0.316          | Overpopulated flat-band modes
    B1       | -0.165          | Underpopulated gap-edge mode
    B3       | -0.150          | Suppressed high-energy modes
    ---------|-----------------|---------------------------
    Total    | +0.00145        | 0.46% residual

Three sectors. Leading order. Already 99.5% cancelled. The residual +0.00145 M_KK is the leftover from three competing contributions that nearly balance. The DIFFERENCE between the initial vacuum energy (~M_KK^4) and this near-cancelled residual has gone somewhere -- and the reframing says it went into spatial expansion. The magnitude of the initial vacuum energy, far from being a problem, is the fuel that drives the ~60 e-folds of inflationary expansion. Each additional layer of cancellation (more Peter-Weyl sectors beyond level 3, instanton averaging, inter-sector coupling at next order) would further reduce the residual and source more expansion.

This is not an entirely new idea. Paper 19 (Greene-Levin) demonstrates exactly this dual role in a simpler setting: Casimir energy on toroidal extra dimensions simultaneously stabilizes the internal geometry (through the radion potential minimum) and drives accelerated expansion in the large directions. The equation of state is w_a = -1 for the large dimensions and w_b = -2 for the compact dimensions (Paper 19, Section on connection to dark energy). The phonon-exflation framework proposes the same dual function on SU(3) with Jensen metric -- except that Casimir stabilization has been closed by theorem (Structural Monotonicity, S37), and the dynamics are a transit rather than a static minimum. The vacuum energy still does double duty: it powers expansion AND its progressive cancellation determines the CC.

**The e-fold deficit through this lens.** Section 5.8 flags the 2.92 acoustic e-fold deficit (the framework produces 2.92 e-folds from the sound-speed hierarchy c_fabric/c_Gold = 229.5, far short of ~60). The reframing suggests the deficit exists because the current computation includes only 3 Peter-Weyl sectors at leading order. The Structural Monotonicity Theorem (S37) proved that all 10 computed sectors are individually monotonic in the same direction -- which means each sector contributes vacuum energy that participates in the cancellation cascade. The total available vacuum energy scales with the number of sectors included. At max_pq_sum = 3, the computation covers 10 sectors out of an infinite tower. The first 10 sectors carry ~155,984 weighted modes (S36). If the cancellation cascade extends through the KK tower, the total vacuum energy released (initial minus residual) could be orders of magnitude larger than the 3-sector estimate, potentially closing the e-fold gap.

But I want to be careful here. The 99.5% cancellation at 3 sectors is a suggestive number, not a derivation. Let me identify what it does and does not tell us.

**What it does tell us.** The sector cancellation has a definite structure. The B2 flat-band modes are overpopulated relative to equilibrium (the GGE preserves the BCS occupation pattern: too many particles near the gap, too few far from it). The B1 gap-edge and B3 high-energy modes are underpopulated. These opposite signs are a direct consequence of the BCS-to-GGE quench -- the same physics that produces quasiparticle excitations (dark matter) also produces the occupation mismatch (vacuum energy). The near-cancellation is a structural property of the Volovik equilibrium theorem: in any system where the equilibrium vacuum energy is exactly zero (as q-theory requires for the BCS ground state), the non-equilibrium residual is the DIFFERENCE between opposite-sign contributions, and this difference is small when the system is close to equilibrium. The GGE is close to equilibrium in the sense that ||f^GGE - f^eq||/N_pair = 0.195 -- an O(1) departure mode by mode, but the weighted sum nearly cancels.

**What it does not tell us.** The 99.5% cancellation does not automatically compound as more sectors are added. Each additional Peter-Weyl sector adds both positive AND negative contributions. Whether the total residual decreases monotonically with sector count, or fluctuates, or grows, depends on the specific GGE occupations at each level -- which are determined by the quench dynamics and the spectrum. This has not been computed beyond level 3. The claim "more sectors = more cancellation" is plausible but unproven.

**The Volovik attractor.** The q-theory equilibrium theorem (Volovik, Papers 15-16, 35 in the framework's Volovik corpus) provides the theoretical backbone: in a self-consistent vacuum, the cosmological constant is Lambda = 0 exactly at equilibrium, because the vacuum adjusts itself to satisfy the Gibbs-Duhem relation. The observed Lambda ~ 10^{-120} M_Pl^4 is then the tiny departure from equilibrium. In the phonon-exflation reframing, the GGE is a non-equilibrium state that NEVER reaches equilibrium because integrability protection (8 Richardson-Gaudin conserved quantities, block-diagonal theorem) prevents thermalization. The observed CC is the distance between the GGE and the Lambda = 0 attractor. This is Volovik's program applied to a specific computable substrate.

The question I posed at S57 was whether integrability protection produces the RIGHT distance to the Lambda = 0 attractor. I argued it could not without a 10^-57-per-mode tuning that would destroy the DM-protecting integrability — and I called this "the deepest structural problem in the framework." **The tracking vacuum dissolves the problem rather than solving it on those terms.** The static reading demanded the GGE match equilibrium to 10^-57 per mode at one instant. The tracking reading (DILUTION-CC-66) does not: the GGE excess starts at the M_Pl^2 H^2 scale and is *diluted by the expansion itself* as H falls — no per-mode fine-tuning is required, because the smallness of today's dark energy is the smallness of H_0^2, not the smallness of an occupation mismatch. The DM stays integrable; the CC comes out right; the tension I flagged is gone. What I got wrong at S57 was treating the vacuum energy as a number to be tuned rather than a quantity that tracks a dynamical scale. (The framework's own per-sector near-cancellation — B2/B1/B3 summing to +0.00145 M_KK at three sectors — is a separate and weaker observation; it is suggestive of self-tuning structure but, as I noted then and maintain now, has not been shown to compound monotonically with sector count. The CC resolution does not rest on it; it rests on C10's tracking law.)

**What computation would test the still-open piece?** The CC magnitude is now a result (DILUTION-CC-66, conditional on C10), so these are no longer "promote the CC reframing from narrative to result." They target the *separable* open question — the e-fold count and the full Friedmann mapping (§5.4, §5.8). Of the three, #1 and #3 remain live; #2's "cascade-convergence" framing is superseded by the tracking law (the residual smallness is set by H_0, not by sector-count cancellation), and I retain it only as a diagnostic of the per-sector structure, not as the CC mechanism:

1. **Sector-resolved N_efolds.** Compute the vacuum energy released per Peter-Weyl sector as the GGE forms. If the cancellation cascade produces a cumulative N_efolds = integral sqrt(Lambda_eff(sector count) / 3 M_Pl^2) dt that grows toward 60 as more sectors are included, the reframing has quantitative support. If N_efolds saturates well below 60, the reframing fails.

2. **Cancellation scaling with KK level.** Extend the GGE occupation computation from max_pq_sum = 3 (10 sectors) to max_pq_sum = 4 or 5. Track the total residual Lambda_eff as a function of sector count. If the residual decreases systematically (as Lambda_eff ~ N_sectors^{-alpha} with alpha > 0), the Volovik attractor picture has empirical support within the framework. If the residual fluctuates or grows, the cancellation at 3 sectors is accidental.

3. **Friedmann equation from spectral action source terms.** Derive H^2 = (8*pi*G/3) * rho from the spectral action, with rho decomposed into matter (quasiparticle) and vacuum (GGE excess) contributions. This would close the convention-mapping gap identified in Section 5.9 and make the e-fold count meaningful in FRW terms.

**The DESI discriminant (now a binding pre-registration).** The tracking vacuum has an immediate observational consequence for w(z), and the framework has since turned it into a binding, pre-registered test rather than a loose qualitative expectation. The substrate-compaction reading (the fiber tau tracking density, T8) gives a dynamical dark energy: w_0 > -1 with w_a generated by the tracking, qualitatively consistent with the DESI DR1/DR2 hints of dynamical DE. The Volovik-partition reading gives w_a = 0 from the four-fold structural lock. These are the two branches I flagged as a (value, scheme) pair in §3b. Rather than leave this as "the reframing is in tension with w_a = 0," the framework pre-registered the R_842 falsifier rectangle (S84-DR3-RESPONSE-PROTOCOL) so that DESI DR3 adjudicates cleanly: R_842 = [-1.05, -0.85] x [-0.2, +0.2] in (w_0, w_a). The branch-(iv) substrate-compaction prediction w_0 = -0.842454 lies inside R_842 by construction; DR3 either confirms a (w_0, w_a) inside the rectangle (supporting the dynamical branch) or lands outside (falsifying it). This is the cleanest kind of cosmological test — a number pre-registered before the data, with a documented response protocol — and it is the framework's single most consequential near-term observational handle. DESI DR3 (Window-14) is the binding instrument.

**Honest assessment (updated S66).** Two of the three cautions I raised at S57 have been answered; one remains open and is worth keeping distinct from the CC magnitude.

First (answered): I worried the overshoot was being reinterpreted as a feature "without computing the consequences." The consequence — that today's dark-energy density is M_Pl^2 H_0^2 — *is* now computed (DILUTION-CC-66, ratio 1.032). The CC magnitude is no longer a reinterpreted number; it is a closed gate, conditional on C10.

Second (answered/dissolved): I worried the cascade had to converge to 10^-120 by a fine-tuned stopping mechanism — "the same fine-tuning in different clothes." Under the tracking vacuum there is no cascade-stopping fine-tuning: the residual is set by H_0, not by where a cancellation halts. The worry was an artifact of the static reading.

Third (still open, but separable): the **e-fold question**. The acoustic transit produces ~2.9 e-folds (the sound-speed hierarchy), far short of the ~60 that solve horizon/flatness in standard inflation. This is genuinely unresolved — but it is NOT the same as the CC problem, and the framework's answer is not "more cancellation sectors." The framework's answer is that exflation is not inflation: it does not attempt to solve the horizon problem by 60 e-folds of metric expansion. The horizon problem is "ameliorated by tau-simultaneity, NOT eliminated" (S41), and the pre/post-transit causal disconnect is handled by the acoustic white hole (S85 W6 formal causal-disconnect computation), not by inflationary stretching. Whether that is *sufficient* — whether tau-simultaneity plus an acoustic white hole prepares the observed homogeneity without a separate inflationary epoch — is, in my judgment, the framework's deepest remaining cosmological open question. I scope it as open in §5.8, not resolved.

So this subsection is no longer "an agenda." The CC magnitude is a result (DILUTION-CC-66, conditional on C10). The Greene-Levin Casimir analogy remains the right published comparison (vacuum energy doing double duty: stabilization + expansion), with the caveat that the framework's stabilization is dynamical-transit, not a static Casimir minimum (which it closed by the Structural Monotonicity Theorem, S37). What remains an agenda is the horizon/flatness preparation, which I treat as a distinct problem.

### 3c. Extra Dimensions

This is my specialty, and the most natural point of contact with my published work. The framework proposes 8 internal dimensions (SU(3), dim = 8). How does this compare to other extra-dimension scenarios?

**Comparison with LED.** Paper 05 constrains large extra dimensions (LED) via micro black hole production and vacuum decay. Paper 13 extends this to PBH dark matter with 2-6 extra dimensions. The key relationship is:

    G_N ~ 1/(M*^{2+n} V_extra)

where M* is the fundamental Planck scale and V_extra is the internal volume. In LED models, the extra dimensions are flat and large (mm-scale for n = 2). In the phonon-exflation framework, the extra dimensions are curved (SU(3) with Jensen metric) and Planck-scale (a_cell ~ 1.596 M_KK^{-1}).

The critical difference: LED predicts a lowered Planck scale M* ~ TeV, detectable at colliders and in UHECR (Paper 05). The framework predicts M_KK ~ 10^{16} GeV -- near the GUT scale, far above any terrestrial experiment. This puts the framework outside the reach of the LED constraints I helped derive, which is both a strength (not excluded) and a weakness (not testable by the same methods).

**Comparison with Greene's Casimir stabilization.** Paper 19 (Greene-Levin) proposes Casimir energy from bulk fields as the stabilization mechanism for toroidal extra dimensions, simultaneously providing dark energy. This is structurally the same idea the phonon-exflation framework pursued for 20 sessions before closing it by theorem. The Structural Monotonicity Theorem (S37) proves that the spectral action S[D_K, f, Lambda] is monotonically increasing in tau for any smooth monotone cutoff function f. No Casimir-type minimum exists on SU(3) with Jensen metric.

This is a genuinely important negative result. Greene-Levin's mechanism works on flat tori because the Casimir energy of a box depends non-monotonically on the box size. On a compact Lie group with volume-preserving deformation, the spectral action is monotone. The framework discovered -- by computation, not assumption -- that the Greene-Levin mechanism does not generalize from flat tori to curved internal manifolds. This is a contribution to the extra-dimensions literature regardless of whether the phonon-exflation framework itself succeeds.

**Comparison with hyperbolic compactifications.** Paper 21 (Greene) constructs inflation from large-volume hyperbolic compactifications with a large spectral gap (k_1^2 >= 171/784, independent of volume). The framework uses SU(3), which has a different spectral structure -- no large gap, but a Van Hove singularity at the fold. The Buser bound for hyperbolic manifolds does not apply to SU(3). The framework's spectral gap is the BCS gap (0.370 M_KK for single-cell), which decreases with cell count as N^{-1.84} (S57 W1-3). This is the opposite of what Paper 21 needs for its bulk inflaton construction.

**KK dark matter.** Paper 10 (TASI lectures) discusses KK dark matter -- the lightest KK mode of a bulk particle in compactified space as a DM candidate. The phononic DM is structurally different: it is not a KK mode but a quasiparticle excitation of the BCS condensate on the internal manifold. The KK modes in the framework are the Peter-Weyl sectors of D_K, which are the particle spectrum, not the dark matter. The dark matter comes from the dynamics (transit quench), not the kinematics (KK tower).

**Non-orientable geometry and CP violation.** Papers 25-26 (Greene) study Klein bottle compactification, where non-orientable topology produces CP violation and fermion condensate walls. The framework uses orientable SU(3) and has CP = 0 structurally (S52, three independent proofs). This is a point of departure: Greene's Klein bottle cosmology predicts CP violation from topology, while phonon-exflation predicts CP conservation from topology. The CKM and PMNS CP phases must arise from a different mechanism in the phonon-exflation framework -- and this mechanism has not been identified. The PMNS route through the singlet sector has been closed (ceiling R ~ 5.9, S35).

### 3d. Phase Transitions and the Fold

The framework describes a specific cosmological phase transition at the fold (tau ~ 0.19):
- Classification: the BCS transition is second-order, 3D Ising universality class (Z_2, n=1), with z = 2.024, nu = 0.6301, beta = 0.3265 (`Classification-of-phonon-exflation.md`, Table II.B).
- The transit through the fold is a sudden quench, not a gradual cooling. The quench time is 38,600x faster than the BCS formation timescale.

**Standard cosmological phase transitions.** In standard cosmology, the electroweak transition (T ~ 100 GeV) is a crossover in the SM, potentially first-order in extensions with additional scalars. The QCD transition (T ~ 150 MeV) is a crossover. A first-order phase transition produces bubble nucleation and gravitational waves (Paper 06, Section on DM phase transitions).

The framework's fold transition is qualitatively different from standard cosmological phase transitions in several ways:

1. It occurs in the internal space, not in 4D spacetime. The 4D observer experiences it through the acoustic metric, not directly.
2. The relevant temperature is T_init = 8.32 x 10^{15} GeV (GUT scale), determined with zero free parameters (S53).
3. The transition is a sudden quench (Kibble-Zurek mechanism), producing 59.8 quasiparticle pairs (S38) or P_exc = 0.081 in the 2-cell system (S57 W1-1).
4. The post-transit state is a permanent non-thermal GGE relic, not a thermal plasma.

**Comparison with Volovik's superfluid vacuum.** The transit physics has a direct analog in Volovik's "Universe in a Helium Droplet" program, which the framework explicitly cites. In He-3B, a rapid temperature quench through the superfluid transition temperature produces a non-equilibrium quasiparticle distribution via the Kibble-Zurek mechanism. The quasiparticles experience an effective curved spacetime through the acoustic metric, while the substrate remains flat. The phonon-exflation framework is the first concrete realization of this program on a compact Lie group rather than a laboratory superfluid. The structural correspondence is exact in several places (block-diagonal theorem = sector decoupling, BDI classification = symmetry class, GGE permanence = integrability protection), but the cosmological consequences are far more constrained than the He-3B analog because the internal manifold SU(3) has rigid topology.

**The "Shattering" (S57).** Session 57 introduces the Shattering mechanism: channel-selective diabaticity at the BCS freeze partitions the fabric energy between DM and CC channels. The Leggett modes are deeply diabatic throughout transit (gamma_LZ = 1.5 x 10^{-5}, P_exc = 0.9996 from LZ formula), meaning the relative-phase degrees of freedom between cells are fully excited. However, the correct formalism is Bogoliubov squeezing (harmonic oscillator with time-dependent frequency), not Landau-Zener (two-level system). The squeezing formula gives mean excitation numbers <n_exc> ~ 0.05-0.48 per mode (S57 W1-2), distributed across all 31 dispersive modes. This is cosmological particle creation -- the same Parker (1969) mechanism that produces particles in an expanding FRW universe, applied to the internal SU(3) geometry.

The percolation analysis (S57 W3-2) adds a dramatic structural feature: at the fold and BCS freeze, the 32-cell tessellation is completely fragmented (zero active Josephson bonds). Every cell is a causally isolated quantum system. The fabric is not gradually losing coherence -- it shatters instantaneously at tau_frag = 0.1048, well before the fold. This is a first-order fragmentation (all-or-nothing), not critical percolation. The equilibrium fragmentation is physical but dynamically irrelevant at the physical transit rate (Mach 2700), because the phase correlations freeze at their pre-fragmentation values.

**Gravitational wave signatures (the GW arc: S59 -> S77 retraction -> S87 discriminator).** This is a place where I have to report a retraction the framework made about itself, and I think the retraction is to its credit. At S59 the framework predicted a domain-wall gravitational-wave background at LISA frequencies, Omega_GW ~ 10^-10 at 1 mHz — a genuinely exciting, near-term-testable signal. Session 77 killed it. The percolation/Josephson analysis (S77-C8-DW-GW, FAIL) showed that the Josephson bias destroys the domain walls 15,000x faster than they could survive to reheating; the walls never persist long enough to source a GW background, and the recomputed Omega_GW ~ 5e-45 is ~46 OOM below LISA sensitivity. The S59 LISA prediction is RETRACTED (and the channel `domain_wall_GW_GUT_GHz` is closed: a GUT-scale annihilation produces GHz-band GWs, while LISA needs a TeV-scale transition — a frequency mismatch). So the framework's GUT-scale phase transition is gravitationally silent in the conventional domain-wall sense, exactly as Paper 06's frequency scaling f ~ (T_*/100 GeV) x (beta/H) x 10^-2 Hz would push it (at T ~ 10^15 GeV, f ~ 10^11 Hz, far above any detector).

What survives is more subtle and, to its credit, the framework kept the honest piece: the *transit* GW (the impulsive acoustic transit through the fold) is PROVEN to source a stochastic background, and Session 87 computed a LISA discriminator from the regulator-class structure of the late-time vacuum — Omega_GW_Lambda_A vs Omega_GW_Lambda_C at LISA frequencies (the two values differ by the regulator-class split documented in `regulator-pin-discipline.md`, Sage-exact: Omega_GW^(C) ~ 8.3e-58, with the A/C split ~47 OOM). These are far below LISA's ~10^-12 sensitivity at 1 mHz, so this is currently a `DETECTOR-STERILE` channel in the falsifier-rigor-registry (the migration threshold to detectability is ~10^-40, S83 Channel-5). I record it not as a near-term test but as a structural prediction whose regulator-class dependence is computed. The lesson a cosmologist should take: the framework's most headline-friendly GW claim (S59 LISA) did not survive its own scrutiny, and the framework retracted it rather than defending it. That is the behavior you want.

**The second-sound CMB feature.** Independently of GWs, the framework predicts a specific CMB temperature-power-spectrum feature at l ~ 721 from the 229x sound-speed hierarchy: l_second_sound = pi x (c_fabric/c_Gold) = pi x 229.48 = 720.9 (S53, Sage-verified), with amplitude delta C_l/C_l = 0.7% (~24 muK^2). This is the acoustic horizon of the GGE pair sound, not a feature of the photon-baryon fluid. It is below Planck noise at l ~ 700 (~50 muK^2) but within CMB-S4's projected reach (noise floor below 5 muK^2 at l ~ 700). A concrete, quantitative prediction that distinguishes the framework from LCDM's smooth damping tail (§6 Test 2).

### 3e. Hubble Tension

Papers 07 and 12 establish that the Hubble tension (H_0 ~ 67 vs 73 km/s/Mpc) persists even when early-universe physics is decoupled from the analysis. Paper 12 demonstrates Omega_m = 0.302 +/- 0.008 is robust and early-universe insensitive. The tension cannot be resolved by pre-recombination modifications alone -- it requires post-recombination physics or systematics.

The phonon-exflation framework does not resolve the Hubble tension, and I want to keep that honest — but the "no late-time observable at all" statement of the S57 draft is now too strong. The framework's expansion mechanism (acoustic, ~2.9 e-folds) occurs at T ~ 10^15 GeV, far before recombination, and the transit equation of state w = 0.202 is decelerating. What has changed since S57 is that the framework now has a *late-time dark-energy sector with observable consequences* (§5.4): w_0 = -0.918 (canonical) / -0.842454 (R_842 branch), and an Integrated Sachs-Wolfe cross-correlation prediction.

**The ISW channel — the framework's first genuine late-time observable (ISW-TRACKING-68, PASS).** Because the framework's dark energy is the Volovik tracking vacuum with sound speed c_s^2_DE = 0 (it clusters with matter, unlike a smooth quintessence field with c_s^2 = 1), it produces a *larger* late-time ISW signal than LCDM. The framework computed the galaxy-temperature cross-correlation (S68/S69, Limber approximation):

    Step 1: A_FW   = 1.1230  (w_0 = -0.918, c_s^2_DE = 0)    [s69_euclid_joint, ISW amplitude relative to LCDM]
    Step 2: A_Quint = 1.0440 (w_0 = -0.918, c_s^2_DE = 1)    [same w_0, smooth DE]
    Step 3: total ISW excess vs LCDM = A_FW - 1 = +12.3%
    Step 4: substrate-specific clustering excess = A_FW - A_Quint = 1.1230 - 1.0440 = +7.9%   [the part that is specifically due to c_s^2_DE = 0, not just w_0 != -1]
    Conclusion: the framework predicts a +12.3% ISW cross-correlation enhancement over LCDM, of which +7.9% is the distinctive clustering signature (a smooth-DE model with the same w_0 gives only +4.4%).

Against the Planck constraint A_ISW = 1.00 +/- 0.25 this is 0.49 sigma — consistent, with a forecast SNR ~ 1.58 (Euclid + DESI multi-tracer improves this ~1.7x). What the data *shows*: the framework's ISW prediction is consistent with current measurements (it is not yet a discriminating detection). What it *suggests*: the c_s^2_DE = 0 clustering signature is a real, distinctive handle that a high-SNR ISW measurement could test against smooth quintessence. What it does *not* address: a full Boltzmann (CLASS/CAMB) treatment with c_s^2_DE = 0 would refine the low-l part of the signal by ~5% (the W1-C caveat); and there is still no full H(z)/distance-redshift relation tied to BAO and SN Ia (§5.4). It also gives sigma_8 = 0.811 (Planck-consistent).

So this is no longer "the framework does not address late-time cosmology at all." It has a dark-energy equation of state, an ISW signal, and sigma_8 — a partial late-time sector. What it does not have is the full H(z) backbone, which I keep as the live gap in §5.4. The framework does not claim to resolve the H_0 tension specifically (my Paper 12 result — that the tension is early-universe-insensitive — means a post-recombination mechanism would be needed, and the framework has not built one).

---

## 4. What It Gets Right (Structural Strengths)

**4.1. Mathematical rigor of the algebraic skeleton.** The following results are proven at machine epsilon and do not depend on the cosmological interpretation:
- KO-dimension = 6 (parameter-free, S7-8)
- SM quantum numbers from Psi_+ = C^16 (S7)
- CPT hardwired: [J, D_K(tau)] = 0 (S17a)
- Block-diagonality of D_K in Peter-Weyl basis (8.4e-15, any left-invariant metric, S22b)
- g_1/g_2 = e^{-2tau} from Jensen metric (S17a)
- Volume preservation: exact at all tau (S12)
- 67/67 Baptista geometry checks (S17b)
- 147/147 Riemann tensor checks (S20a)

These are not approximations. They are exact mathematical results about the Dirac operator on (SU(3), g_Jensen). They would survive even if the cosmological interpretation is entirely wrong.

**4.2. Honest self-audit.** The spectral post-mortem (`spectral-post-mortem.md`) is a 20-session chronicle of how the perturbative stabilization program was pursued, failed, and was closed by theorem. This is how science should work. The framework tried the obvious mechanism (Casimir stabilization, as in Greene-Levin Paper 19), found it fails on SU(3), proved WHY it fails (Structural Monotonicity Theorem), and pivoted to a different paradigm (dynamical transit). The documentation of this process -- with specific gate verdicts, named closures, and clear attribution of what killed each mechanism -- is exemplary.

**4.3. The DM abundance is now anchored to ~1%, not just bracketed.** At S57 this was a factor-3 bracket [0.017, 0.188] containing 0.120. As of S70 it is a point anchor: LEGGETT-MOMENT-70 (Type-F single-summand-projection trace, algebra-INVARIANT) gives Omega_DM h^2 = 0.11995 at zero free parameters, ~1% from Planck 2018 (0.1186) and sub-1% from the Planck 2020 DR2 pin (0.11993). The factor-3 interpretive freedom is structurally closed (the Type-F classification fixes the mapping). A zero-parameter prediction that lands on a 10^-1 number to ~1% is stronger than the original WIMP-miracle coincidence, which gives the right order of magnitude but not the percent. And the stability worry is gated (LEGGETT-GRAV-DECAY-67, Gamma_grav < H_0). This is, in my view, the framework's strongest single quantitative contact with observation in the cosmology domain.

**4.4. The CC sign is correct AND its magnitude is now resolved (conditional on C10).** Lambda_eff > 0 (accelerating expansion) from the GGE energy excess — the "destroy a condensate, release positive binding energy" picture, with a direct He-3B analog. As of S66 the magnitude is also addressed: the Volovik tracking vacuum (DILUTION-CC-66, ratio 1.032) dilutes the M_Pl^2 H^2 reservoir to the observed dark-energy density, conditional on the C10 scaling assumption. I keep the conditional explicit, but the upgrade from "sign right, magnitude catastrophic" (S57) to "sign right, magnitude resolved conditional on C10" (S66) is the single largest change in the framework's cosmological standing.

**4.8. BBN compatibility and N_eff (new gated results, S67/S75).** BBN-VOLOVIK-67 passes (the tracking vacuum at z ~ 10^9 gives rho_vac/rho_rad = 0.67 with |w_vac - 1/3| = 3.39e-41), and the S75 thermalization theorem (W3-M) shows ~10^14 e-folds between the fold and neutrino decoupling completely erase the GGE initial conditions, returning N_eff = 3.044 to machine precision — matching the SM value. The reheating temperature is computed (T_RH = 1.70e15 GeV, S77). At S57 BBN was "entirely conceptual"; it is now a set of passed gates (§5.3).

**4.5. T_init at GUT scale with no tuning.** T_acoustic = 0.112 M_KK = 8.32 x 10^{15} GeV is a zero-parameter output that lands at the GUT scale. This is a non-trivial coincidence that deserves attention regardless of the framework's ultimate fate. In standard inflation, the reheating temperature is a free parameter constrained by BBN to T_rh > ~1 MeV and by gravitino overproduction to T_rh < ~10^9 GeV (in SUSY models). The phonon-exflation framework's T_init is GUT-scale without SUSY and without tuning -- it emerges from the BCS quasiparticle spectrum (determined by the Kosmann kernel on SU(3)). Whether this number survives the full cosmological evolution (cooling trajectory through BBN to CMB) is uncomputed.

**4.6. The Shattering mechanism as cosmological particle creation.** The S57 identification of the Leggett channel as the DM source via Bogoliubov squeezing is physically well-motivated. The mechanism is the same Parker (1969) particle production that operates in standard cosmological pair creation, applied to internal geometric degrees of freedom rather than 4D spacetime. The mode-independent excitation theorem (S57 W2-1: all 31 BA modes have identical |beta|^2 because the frequency ratio omega_n(tau)/omega_n(0) is mode-independent by graph Laplacian factorization) is a clean structural result. It means the particle production is determined by a single function of tau, not 31 independent calculations.

**4.7. The gap scaling exponent.** The result alpha = -1.84 (gap decreases as N^{-1.84} with cell count, S57 W1-3) resolves a 260-order-of-magnitude ambiguity in the framework. Before this computation, it was unclear whether the multi-cell gap grows (Hawking's scenario: exponential protection, P_exc ~ 10^{-258}) or shrinks (Berry's scenario: Josephson band dispersion dominates). The computation definitively excludes the growth scenario and confirms gap collapse, establishing that the 32-cell fabric is far more excitable than the 2-cell prototype. This has direct cosmological consequences: it means the DM abundance from Leggett mode excitation should INCREASE when extrapolated from 2 cells to 32 cells, potentially closing the factor-2.7 shortfall.

---

## 5. What It Gets Wrong or Leaves Unanswered

**5.1. The cosmological constant magnitude — RESOLVED at S66 (conditional on C10); this is no longer the framework's most severe problem.** I am leaving this entry in §5 because it was the headline problem of the S57 draft, but the honest status is that it has moved out of "what it gets wrong." At S57 I wrote that the CC was the framework's most severe problem and that reformulation was not resolution. The S66 DILUTION-CC-66 result (full chain in §3b CLAIM 1) supplies the resolution: the vacuum is not static, it tracks as rho_vac ~ M_Pl^2 H^2 (Volovik q-theory, C10), and the M_Pl^2 H^2 reservoir dilutes to the observed dark-energy density as H falls — ratio rho_vac/rho_obs = 1.032, a 0.01-OOM residual. The S57 argument that the GGE had to match equilibrium to 10^-57 per mode was an artifact of the static reading; under tracking there is no per-mode tuning. The "integrability problem" framing (the same integrability protecting DM forcing the CC large) is dissolved, because the smallness of today's dark energy is the smallness of H_0^2, not of an occupation mismatch.

The honest residual caveat: C10 (rho_vac ~ M_Pl^2 H^2) is ASSUMED-PARTIALLY-PROVEN — adopted as the Volovik q-theory ansatz at the substrate-IS level, not yet derived from the spectral triple from first principles. So the correct statement is "the CC magnitude is resolved conditional on C10," and the open work is the first-principles derivation of C10's scaling form (the W11 Volovik CC Tracking Wall; §VII.AT registry slot OPEN). That is a far narrower and more tractable open problem than "find an integrability-breaking mechanism that tunes 56 orders of magnitude," which is what S57 faced. The S57 list of five candidate integrability-breaking mechanisms (Pomeranchuk, phonon-phonon, off-Jensen, multi-mode resonance, cross-susceptibility) is moot — none is needed, because integrability is no longer the obstruction.

**5.2. The spectral index — the naive value was the WRONG OBSERVABLE; the slow-roll value is O(1) sigma from Planck.** This is the second large reversal since S57. At S57 the framework's only n_s was the naive Kibble-Zurek power-law fit n_s = 2.065 — a fit to the post-transit excitation spectrum P(K) over k in [0.002, 0.358] M_KK. That is blue, 262 sigma from Planck, and correctly CLOSED. But it is a fit to the wrong quantity: P(K) is the excitation-number spectrum of the quench, not the curvature-perturbation tilt at the CMB pivot. Confusing the two is like reporting the Fourier spectrum of the reheating field and calling it the primordial scalar tilt.

**Substitution chain — CLAIM 3 (n_s is no longer a 262-sigma failure):**

    Step 1: n_s_naive = 2.065  (S53 KZ power-law fit over P(K) on [0.002, 0.358] M_KK)   [the WRONG observable]
    Step 2: n_s_slow-roll = 1 - 2*eps_H                                                   [Hubble slow-roll from the spectral-action ratio, S42/S62]
    Step 3: eps_H from the spectral-action fold formula; eps_BLV = 2 - 1/eps_SA (exact)   [S64; gauge invariance S66 T7 — BLV and SA give identical n_s]
    Step 4: n_s_framework = 0.9561                                                        [canonical, S84-85 gauge-invariant; S62 first-viable 0.9567; S73a triple-confirmed Bogoliubov-invariant 0.9567]
    Step 5: |0.9561 - 0.9649| / 0.0042 = 2.10 sigma  (Planck TT,TE,EE+lowE+lensing, sigma = 0.0042);  |0.9561 - 0.9649| / 0.0062 = 1.42 sigma (wider error bar)
    Conclusion: n_s is O(1) sigma from Planck. The 262-sigma was the naive-KZ observable (P(K), the wrong quantity); the slow-roll observable (the curvature tilt at the CMB pivot) is O(1) sigma. The S57 headline deficiency is SUPERSEDED.

Two notes I owe the reader. **(value, scheme) tagging:** n_s carries a small scheme-spread that I write explicitly rather than collapse — 0.9561 (canonical, gauge-invariant S84/85) / 0.9567 (Hubble-SA, S62/S73a, which Planck-compares at 1.9-1.95 sigma and was flagged SCHEME-DEPENDENT in the S66 baseline). These differ at the third decimal; the canonical pin is 0.9561. **The running alpha_s and a symbol-overload trap:** the framework reports alpha_s = (n_s)^2 - 1 = (0.9561)^2 - 1 = -0.08587279. This is a *substrate-distance* running (a Mellin-residue quantity inside the Brillouin zone), NOT the inflationary running d(n_s)/d(ln k) that Planck/ACT measure (~0; ACT DR4 + Planck give +0.0023 +/- 0.0063). The framework's substrate carries TWO scale-separated alpha_s observables and the symbol is overloaded; the -0.0859 value is the topological/substrate-distance one and should not be compared to the CMB-pivot running. I flag this because conflating them would manufacture a fake 12-sigma "tension" that is purely a scale-mismatch.

What this does NOT fix is the horizon/flatness preparation. Standard slow-roll inflation produces n_s = 1 - 2/N ~ 0.965 AND ~60 e-folds in one mechanism; the framework produces a slow-roll-consistent n_s = 0.9561 through the spectral-action geometry but only ~2.9 acoustic e-folds. The framework's position remains "exflation is not inflation" — it does not solve horizon/flatness by metric expansion, but by tau-simultaneity + the acoustic white hole (§3b-ii, §5.8). Whether that is sufficient is the live open question. But the spectral index itself is no longer a deficiency; it is an O(1)-sigma prediction.

**5.3. BBN connection — now a set of passed gates (S67/S75/S76), not "entirely conceptual."** At S57 the BBN hypothesis was a conceptual phonon-cascade sketch with no computation. Three results since have made it concrete. (i) BBN-VOLOVIK-67 (PASS): the Volovik tracking vacuum at z ~ 10^9 gives rho_vac/rho_rad = 0.67 at nucleosynthesis, with the radiation-domination equation of state satisfied to |w_vac - 1/3| = 3.39e-41 — the vacuum behaves as radiation during BBN and does not spoil it (the effective Newton's constant ratio G_eff/G = 1.5 sits marginally inside the BBN bounds). (ii) S75 W3-M (PASS): the thermalization theorem shows ~10^14 e-folds between the fold and neutrino decoupling completely erase the GGE initial conditions — the ratio Gamma_thermalization/H is enormous, so by BBN the GGE has fully thermalized and N_eff(BBN) = N_eff(recomb) = 3.044, matching the SM to machine zero. This is structurally important: it means the exotic transit physics is invisible to BBN, which is exactly what compatibility requires. (iii) S76/S77: the reheating temperature is computed, T_RH = 1.70e15 GeV (N_decay = 63.4 e-folds of modulus-decay reheating, gravity-dominated). So BBN went from "conceptual" to "5/5 PASS." The lithium problem is not solved (the framework's delta_H/H does not land in the lithium-favored window), but standard BBN is not worsened — the framework is BBN-compatible, which is the relevant bar.

**5.4. Late-time expansion history — PARTIALLY FILLED (ISW + w_0 + sigma_8), but the full H(z) backbone remains the live gap.** At S57 there was no late-time observable at all. That is no longer true (§3e): the framework now has a dark-energy equation of state w_0 = -0.918 (canonical) / -0.842454 (R_842 branch), an ISW cross-correlation prediction (ISW-TRACKING-68, +12.3% vs LCDM, 0.49 sigma, SNR ~ 1.58), and sigma_8 = 0.811 (Planck-consistent). What is still genuinely missing is the *full* distance-redshift backbone: there is no derived H(z) from first principles connecting the GGE relic to today, no sound-horizon r_s, no BAO scale d_A(z)/r_s, no SN Ia distance modulus. The framework can compute the dark-energy sector's *observable consequences* (ISW, w(z) at low z) but not yet the complete expansion history that would let it be fit jointly to Planck + DESI + SN Ia like a full cosmological model. I keep this as the framework's principal remaining cosmological gap — narrower than the S57 "no late-time anything," but real. Deriving H(z) from the spectral-action source terms (the Friedmann equation from a_0 + a_2 decomposition; §5.9) is the computation that would close it.

**5.5. PMNS mixing angles unresolved.** The neutrino mass ratio R ~ 33 (from oscillation data) requires inter-sector or off-Jensen approaches after the singlet ceiling R ~ 5.9 was established (S35). The three-generation structure from Z_3 is topological and elegant, but the quantitative mixing angles are not derived.

**5.6. CP violation absent.** CP = 0 structurally (three independent proofs, S52). The observed CKM and PMNS CP phases must arise from a mechanism not yet identified. Compare with Greene's Klein bottle scenario (Papers 25-26), where CP violation is built into the topology.

**5.7. Baryogenesis mechanism absent.** Standard baryogenesis requires all three Sakharov conditions: B violation, C and CP violation, departure from equilibrium. The framework has the third condition in abundance (the transit is maximally out of equilibrium). But CP = 0 structurally, and no baryon number violation mechanism has been identified within the SU(3) internal geometry. The Klein bottle cosmology (Paper 26) satisfies all three Sakharov conditions through topology. The phonon-exflation framework would need an analogous mechanism, perhaps from off-Jensen deformations or multi-pair effects, but this is speculative.

**5.8. The 2.92 e-fold deficit.** The acoustic expansion produces 2.92 e-folds, far short of the ~60 e-folds needed to solve the horizon and flatness problems. The framework explicitly acknowledges this (Section 7B of `Phononic-framework-hypothesis.md`): "Exflation does not need accelerated expansion." But the framework has not explained what DOES solve the horizon and flatness problems. If the phonon-exflation transit does not produce enough expansion and does not produce the right spectral index, what prepares the initial conditions for the observed universe? This is the deepest cosmological question the framework leaves unanswered.

One possible response: the framework could be embedded within a larger cosmological scenario where standard inflation occurs first, setting up the homogeneous initial conditions, and the phonon-exflation transit occurs later (at T ~ 10^{15} GeV) as a post-inflationary phase transition. In this picture, inflation provides the 60 e-folds and the nearly scale-invariant spectrum, while phonon-exflation provides the particle content, DM abundance, and CC. This is a logically consistent division of labor, but the framework documents do not advocate for it explicitly, and the interface between inflation and the transit would need to be specified.

**5.9. Convention mapping between spectral geometry and FRW cosmology.** The framework uses spectral geometry conventions (tau as modulus, M_KK as mass scale, spectral action as effective action) that do not have standard mappings to FRW cosmological conventions (H(z), Omega parameters, distances). The Friedmann equation in standard cosmology relates H^2 to the total energy density via

    H^2 = (8 pi G / 3) rho_total

In the framework, the "energy density" comes from several sources (spectral action gradient, BCS condensation energy, Leggett excitation energy, Josephson condensation energy) that do not all have well-defined FRW counterparts. The mapping between E_matter = 11.40 M_KK and Omega_m = 0.315 is still assumed (S57 W2-4) rather than derived from a closed Friedmann equation. At S57 I called this "the single most important unresolved issue for cosmological contact." That framing is now too strong: the *dark-matter abundance* no longer depends on it (LEGGETT-MOMENT-70's Type-F trace bypasses the energy-fraction mapping; see the next paragraph), and the CC magnitude is set by the tracking law (DILUTION-CC-66), not by this identification. What the assumed E_matter <-> Omega_m mapping still gates is the *full distance ladder* (H(z), r_s, BAO) — which is one of the framework's open items (§5.4), no longer the single dominant one.

To be concrete about the original concern: at S57 the framework computed f_DM = E_DM/E_matter and then faced two interpretations of the abundance mapping (Omega_DM h^2 = f_DM x Omega_m x h^2 vs f_DM x h^2) differing by a factor of 3, which I called the single most important unresolved issue. **That factor-3 is closed at the abundance-anchor level (S70).** LEGGETT-MOMENT-70 anchors the DM mass directly as a Type-F single-summand-projection trace on A_K (Mass_LeggettDM/Delta_BCS = 11.97) and gives Omega_DM h^2 = 0.11995 with no interpretive choice — the trace fixes the number, it does not pass through the ambiguous energy-fraction mapping (§3a CLAIM 2). So the abundance prediction no longer carries the factor-3 systematic.

What remains in this section as genuinely open is the *full* Friedmann mapping: deriving H^2 = (8 pi G/3) rho from the spectral action with rho decomposed into the a_0 (vacuum/CC) and matter (a_2-sourced) contributions, so that E_matter = 11.40 M_KK maps to Omega_m = 0.315 *by derivation* rather than by the assumed identification of S57 W2-4. The DILUTION-CC tracking law (§3b) supplies the a_0/vacuum piece's scaling (conditional on C10), and the ISW sector (§3e) supplies late-time observables, but the closed Friedmann equation from spectral-action source terms is still the missing structural piece — the same gap as the H(z) backbone (§5.4). It no longer infects the DM abundance, but it does still limit the framework's ability to be fit as a complete FRW model.

---

## 6. The Observational Gauntlet

I propose the following specific tests, ordered by feasibility:

### Test 1: DESI DR3 w_0 and w_a

**Observable**: Dark energy equation of state parameters w_0 and w_a.

**Framework prediction** (updated S84-85; the S49 P-8 w_0 in [-0.43, -0.59] band is superseded): w_0 = -0.918 (canonical, Volovik partition) OR w_0 = -0.842454 (R_842 branch-(iv), substrate-compaction); w_a = 0 (four-fold lock). Written as a (value, scheme) pair because the two readings are physically distinct. **Pre-registered falsifier rectangle**: R_842 = [-1.05, -0.85] x [-0.2, +0.2] in (w_0, w_a), under the S84-DR3-RESPONSE-PROTOCOL.

**LCDM prediction**: w_0 = -1, w_a = 0.

**Current data**: DESI DR1 (Paper 30): w_0 = -0.72 +/- 0.08, w_a = -0.41 +/- 0.31. DESI DR2 (DR2-DESY5): w_0 = -0.752 +/- 0.057, w_a = -0.73. Post-Dovekie (2026) combined: w_0 = -0.803 (non-binding).

**Discriminant**: DESI DR3 (Window-14) is the binding instrument. Post-Dovekie sigma-distances: 2.130 sigma for the canonical w_0 = -0.918, 0.731 sigma for the branch-(iv) -0.842454 — i.e., the substrate-compaction branch is currently the better fit to DESI. If DR3's (w_0, w_a) posterior lands OUTSIDE R_842, the substrate-compaction branch is falsified. If it lands inside with w_a significantly nonzero, the canonical w_a = 0 four-fold lock is challenged. This is a binding, pre-registered, soon-resolved test with a documented response protocol — the strongest near-term observational handle the framework has.

**Feasibility**: DESI DR3 expected ~2026-2027. HIGH.

### Test 2: CMB-S4 Second-Sound Multipole Feature

**Observable**: CMB temperature power spectrum feature at l ~ 721.

**Framework prediction** (P-9): Oscillatory feature at l = pi x (c_fabric/c_Gold) = 721 with amplitude delta C_l/C_l = 0.7% (24 muK^2).

**LCDM prediction**: Smooth damping tail, no additional oscillatory feature at l ~ 721.

**Current data**: Planck noise at l ~ 700 is ~50 muK^2 (above the predicted 24 muK^2 signal).

**Discriminant**: CMB-S4 noise floor at l ~ 700 is projected below 5 muK^2. If CMB-S4 achieves this sensitivity and no feature is detected at 24 muK^2, the prediction is excluded. Detection would be strong evidence for the framework.

**Feasibility**: CMB-S4 first light expected ~2028-2030. MEDIUM.

### Test 3: Dark Matter Self-Interaction Cross Section

**Observable**: DM self-interaction cross section sigma/m.

**Framework prediction**: sigma/m = 0 exactly (N_pair = 1, no scattering channels).

**LCDM prediction**: No prediction (CDM assumes sigma = 0, SIDM models allow sigma/m ~ 0.1-10 cm^2/g).

**Current data**: Cluster mergers (Bullet Cluster) constrain sigma/m < 1.25 cm^2/g. Dwarf galaxy observations suggest sigma/m ~ 0.5-5 cm^2/g may help with core-cusp problem.

**Discriminant**: If DM self-interactions are conclusively detected (sigma/m > 0 at high significance), the framework's N_pair = 1 prediction is excluded unless the multi-pair sector (N_pair >= 2, uncomputed) introduces interactions. If CDM-like behavior is confirmed down to smaller scales, the framework remains consistent.

**Feasibility**: Ongoing (HST, JWST strong lensing, cluster observations). MEDIUM.

### Test 4: Lorentz Invariance Violation at Planck Scale

**Observable**: Energy-dependent speed of light from GRB timing or UHECR.

**Framework prediction** (P-2): Lorentz violation at E ~ M_Pl with dispersion Delta v/c ~ (E/M_Pl)^n, where n is determined by the SU(3) dispersion relation. The Brillouin zone edge K_BZ = 0.716 M_KK is a physical cutoff.

**LCDM prediction**: Exact Lorentz invariance at all energies.

**Standard KK prediction**: Exact Lorentz invariance (infinite KK tower, no Debye cutoff).

**Current data**: Fermi-LAT GRB constraints: Delta v/c < 10^{-20} at E ~ 10 GeV. This constrains n = 1 (linear dispersion) below current sensitivity for M_Pl ~ 10^{19} GeV. Quadratic (n = 2) dispersion is not yet constrained at the Planck scale.

**Discriminant**: This is the sharpest distinction between phonon-exflation and standard KK. Standard KK predicts exact Lorentz invariance. The framework predicts emergent Lorentz invariance with Planck-scale breaking. Current experiments are many orders of magnitude short of the required sensitivity for n >= 2.

**Feasibility**: Current sensitivity insufficient. LOW (generational timescale).

### Test 5: Phononic DM Transfer Function

**Observable**: Small-scale matter power spectrum P(k) at k > 10 h/Mpc (Lyman-alpha forest, 21cm).

**Framework prediction**: Modified transfer function T(k) from phononic dispersion relation omega(K) = 2J(1 - cos Ka). Should produce a specific cutoff and oscillatory features different from both CDM and WDM.

**LCDM/CDM prediction**: T(k) = 1 (no cutoff).

**WDM prediction**: Exponential suppression T(k) ~ exp(-(k/k_fs)^2) below free-streaming scale.

**Current data**: Lyman-alpha forest constrains WDM to m_WDM > 5.3 keV. **The phononic transfer function has now been computed (S58):** T(k) = 1.0000 at all observable scales — CDM-like, no cutoff (`framework-dm-properties.md`).

**Discriminant**: With T(k) = 1, the framework is *compatible* with Lyman-alpha (no cutoff to violate the m_WDM bound) but *indistinguishable* from CDM at the power-spectrum level. So this test passes but does not discriminate — it removes a potential falsifier rather than providing a positive signature. The discriminating DM signatures live in the annihilation nulls (Tests 6, 8) and the f_NL bispectrum shape (§6A), not in T(k).

**Feasibility**: DONE (S58). Result: T(k) = 1, CDM-like. Resolved.

### Test 6: DM Annihilation Signals

**Observable**: Gamma-ray, X-ray, and 21cm signals from DM annihilation in halos and the CGM.

**Framework prediction**: No annihilation (phononic DM at N_pair = 1 is exactly stable).

**LCDM prediction**: Model-dependent (WIMPs annihilate; hidden-sector DM may not).

**Current data**: No definitive detection. Papers 01, 04, 17 quantify expected signals for thermal relic DM.

**Discriminant**: A definitive detection of DM annihilation signals (e.g., 21cm excess at z ~ 20-40, Paper 17; CGM ionization, Paper 04) would exclude the phononic DM candidate unless multi-pair effects introduce annihilation channels.

**Feasibility**: SKA (21cm), next-generation gamma-ray telescopes. MEDIUM.

### Test 7: Gravitational Wave Background from Phase Transition

**Observable**: Stochastic gravitational wave background at nHz-mHz frequencies.

**Framework prediction** (updated; the GW arc S59 -> S77 -> S87): the S59 domain-wall LISA prediction (Omega_GW ~ 10^-10 at 1 mHz) is RETRACTED (S77-C8-DW-GW FAIL — the Josephson bias destroys the walls 15,000x before reheating; recomputed Omega_GW ~ 5e-45). What survives is the transit GW (PROVEN to source a background) with a regulator-class-dependent LISA amplitude: Omega_GW_Lambda_A vs Omega_GW_Lambda_C (Sage-exact Omega_GW^(C) ~ 8.3e-58; A/C split ~47 OOM), computed in S87 as a discriminator.

**LCDM prediction**: No prediction (depends on BSM physics).

**Discriminant**: Both the retracted domain-wall value and the surviving transit-GW values are far below LISA's ~10^-12 sensitivity at 1 mHz — this is a `DETECTOR-STERILE` channel (migration threshold to detectability ~10^-40). So LISA will not see the framework's stochastic background. A *positive* LISA detection of a GUT-scale stochastic background would actually be in tension with the framework (which predicts silence). The structural value here is the regulator-class A/C split, computed but not detectable.

**Feasibility**: Spectrum computed (S87). LISA ~2035. Detector-sterile (no detection expected). LOW.

### Test 8: Neutron Star Dark Matter Heating

**Observable**: Thermal emission from nearby neutron stars heated by captured DM annihilation/interaction.

**Framework prediction**: Phononic DM at N_pair = 1 has zero self-interaction and zero annihilation cross section. If captured by a neutron star's gravitational field, it would accumulate without thermalizing or annihilating. No DM heating of neutron stars would occur.

**Standard DM prediction**: WIMPs captured by neutron stars annihilate in the core, producing thermal emission F ~ (R_NS/d)^2 sigma_B T^4 detectable by ELT/TMT at distances < 50 pc (Paper 18).

**Current data**: No definitive detection of DM-heated neutron stars. Paper 18 identifies candidate nearby pulsars for follow-up.

**Discriminant**: If DM heating of nearby neutron stars is confirmed (e.g., unexplained thermal excess at the levels predicted for WIMPs), and the heating rate is consistent with annihilating DM, the phononic DM candidate is excluded. Conversely, if nearby neutron stars are confirmed to be cooler than WIMP heating would predict, it is consistent with non-interacting phononic DM.

**Feasibility**: ELT first light ~2028. MEDIUM.

---

## 6A. The Pre-Registered Observational Program (S58-S93)

The S57 draft listed eight ad-hoc tests. Since then the framework built an actual *program* — a falsifier inventory, a pre-registered-observations table with detector forecasts, and a rigor registry that tags each channel by how decisively a real instrument can touch it. The original eight tests are the ancestors of this program; I map them forward below. This section is new; the S57 document never covered it.

### 6A.1. Tensor-to-scalar ratio r — the dual-pathway program (supersedes the Appendix r = 3.86e-10)

At S57 the only r the framework had was r = 3.86e-10 (S44), self-consistent but ~10^8 below BICEP and effectively untestable. That is superseded. The framework now has a dual-pathway tensor program at the CMB pivot, written as a (value, scheme) pair:

- **r_CMB_framework = 0.0117315** (Path-C, the c_sub-modified scalar pathway; S83 G46 TENSOR-TRANSFER, PASS; `s83_w3_g46_tensor_transfer.npz`).
- **r_PathH = 0.0074705** (Path-H, the transverse-tensor fiber-oscillation pathway; S86; forward-derived as r_PathC x (H_BASELINE/H_TD)^2).

Both lie comfortably under BICEP/Keck Stage-4 (r < 0.036 at 2 sigma) — a PASS, where the S57 r was simply invisible. The two pathways differ by 36% (Path-C-relative), and that split is itself observable: the tensor tilt n_T discriminates them. The framework predicts n_T(k_CMB) = -3.024e-3 (= -r/8, the slow-roll consistency relation, exact for Path-H and inheritance-forced for Path-C), and separately a blue n_T(transit) = +0.4676 at the transit scale — a GEOMETRIC FLOOR, NOT a CMB-pivot prediction, separated from the CMB scale by 54.04 decades in k. (This scale separation is a permanent feature: LiteBIRD probes k_CMB, so the transit-scale blue tilt is a geometric floor, not a detector-comparable number. Conflating them would be an error.) On the discrimination: LiteBIRD's 3-yr forecast sigma(n_T) ~ 0.054 makes Path-H vs Path-C decisive (Window-13), and the BK-Array 2026 readout gives a ~1.4-sigma marginal first look. So r went from "untestable" to "PASS now, decisive by ~2030."

### 6A.2. The f_NL bispectrum — the framework's most distinctive (but detector-sterile) signature

If you want the cleanest theoretical fingerprint the framework leaves on the CMB, it is the shape of primordial non-Gaussianity. The GGE relic is an integrable, non-thermal state, and its three-point function has a *folded-triangle* shape that no single-field slow-roll inflation produces (single-field models produce squeezed/local f_NL; the folded shape requires the kind of non-Bunch-Davies initial state the GGE supplies). The framework computes f_NL across three pathways (a (value, scheme) trio): f_NL^equilateral = 0.0547 (S82 GGE-FNL channel projection, canonical pin), f_NL^folded = 0.129 (S67 GGE-BISPECTRUM-67, in-in formalism, N_pair = 59.8 diagonal CLT), and an analytic-template-folded 0.7685 (S85). Against Planck's equilateral constraint (-26 +/- 47) the equilateral value is 0.57 sigma — consistent.

Here I have to be honest about detectability, because this is where the framework's most beautiful prediction meets observational reality and loses. The folded f_NL ~ 0.13 is small. The forecast SNR on the folded shape is sub-1-sigma even at a cosmic-variance-limited 21cm survey (S83-21CM: sigma_phase-2 ~ 0.80 at SKA Phase-2, and the multi-tracer ISW/lensing route gives SNR ~ 0.01 on the fold). The channel is tagged `DETECTOR-STERILE` in the falsifier-rigor-registry. So the folded-shape bispectrum is the framework's most *distinctive* prediction (no single-field model gives it) and simultaneously one of its least *testable* (no planned instrument reaches it). What the data *shows*: consistency with Planck (0.57 sigma). What it *suggests*: a qualitatively unique shape that *would* discriminate if it could be measured. What it does *not* address: it cannot be measured by any forecast instrument — I scope it as a genuine, honestly-stated detector-sterile frontier, not a near-term test.

### 6A.3. The detector timeline (pre-registered-observations)

The framework's `pre-registered-observations.md` and `falsifier-rigor-registry.md` (18 channels, with `ZERO-FREE-PARAMETER` / `DETECTOR-STERILE` tags) give a concrete forecast timeline. Mapping the channels to instruments and decades:

| Era | Instrument | Channel | Framework value | Status |
|:----|:-----------|:--------|:----------------|:-------|
| 2026-2027 | DESI DR3 | w_0, w_a (R_842 binding) | -0.918 / -0.842454; w_a = 0 | BINDING (Window-14) |
| ~2026 | BICEP/Keck Array | r | 0.0075-0.0117 (dual-pathway) | PASS (r < 0.036); ~1.4 sigma first look |
| now-ongoing | Planck/Euclid/DESI ISW | A_ISW cross-corr | +12.3% vs LCDM | 0.49 sigma; SNR ~ 1.58 |
| ~2028-2030 | CMB-S4 | second-sound l ~ 721; alpha_s/beta_s; n_T | delta C_l/C_l = 0.7% | MEDIUM (noise < 5 muK^2) |
| ~2030+ | LiteBIRD | n_T (Path-H vs Path-C) | -3.024e-3 | DECISIVE (sigma_nT ~ 0.054) |
| ~2035 | LISA | Omega_GW transit (A/C split) | ~10^-57 | DETECTOR-STERILE |
| future | SKA-21cm | folded f_NL | 0.129 | DETECTOR-STERILE (SNR < 1) |

The honest reading of this table: the framework has TWO genuinely decisive near-term tests (DESI DR3 on w_0/w_a, LiteBIRD on n_T/r), one consistency-level handle now (ISW), one medium-term CMB-S4 feature (the l ~ 721 second sound), and a cluster of structurally-real but detector-sterile predictions (LISA GW, folded f_NL). This is a much more honest and better-organized observational posture than the S57 ad-hoc eight-test list. The framework is falsifiable on a defined timeline, and it does not pretend its detector-sterile channels are near-term tests.

### 6A.4. The §VII cross-pillar cosmology bridges + LRD/JWST contact

Two cosmology-relevant entries live in the framework's permanent-results registry (§VII), connecting substrate-IS observables on one "pillar" to laboratory-IN observables on another:

- **§VII.AT — the W11 Volovik CC Tracking Wall** (the DILUTION-CC-66 result; §3b). Currently anchored at `framework-cc-oom.md` + `falsifier-watchlist.md`; the dedicated §VII slot is OPEN (recommended for promotion). This is the registry home of the CC resolution's structural status.
- **§VII.AX.OP-PROJ — the PBH-density bridge** (I am the registry's sole writer for this entry per my bridge role). The substrate-IS observable is a primordial-black-hole number density n_PBH = n_edge_saturated x prob_form / L_pix_LRD^3, built from the saturated edge-mode count and the JWST little-red-dot pixelation scale L_pix_LRD. It is a Wodzicki-BCS bridge (a new bridge-map class, K=2 in the cross-pillar K-counter). As of S93 W-1 its Level-3 anchor is HELD `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor` because the divergent channel's truncation-invariant content is a dimensionful magnitude (Tier-2-dimensionful); the joint theorem-structure is STAGE-3-PERMANENT, but the m^-3 number-density row awaits a physical-scale anchor. I flag this precisely: the bridge structure is permanent, the dimensionful n_PBH value is not yet a satisfied Level-3 prediction.

The LRD/JWST contact is the observational entry point for §VII.AX: the framework's little-red-dots analyst has contributed across S56/S58/S84 (constraints recorded in `lrd-observational-constraints.md` and the `atlas-lrd-collab` review), and the n_PBH bridge consumes the JWST LRD pixelation scale. This is the framework's only direct contact with a current (2024-2026) observational anomaly — the JWST overmassive-black-hole / little-red-dot population — and it is appropriately tentative: a bridge structure with a held dimensionful anchor, not a claimed detection.

---

## 7. Connections to My Research Program

The framework intersects my published work at several specific points:

**Extra dimensions (Papers 05, 11, 13, 19).** The framework's SU(3) internal manifold is a specific realization of extra-dimensional physics. My papers constrain LED models via micro black hole production (05, 11) and PBH dark matter (13). The framework avoids these constraints because M_KK ~ 10^{16} GeV is far above the LED regime (M* ~ TeV). Greene's Casimir stabilization (19) is the closest analog to what the framework attempted and closed by theorem. The framework's discovery that Casimir stabilization fails on SU(3) with volume-preserving deformation is a result I would cite in future extra-dimensions work.

**Dark matter phenomenology (Papers 01, 04, 10, 15, 16, 17).** The phononic DM candidate needs to be confronted with the constraints I have helped develop. The most urgent need is the free-streaming constraint from Paper 16 (z_tr > 6.2 x 10^7) and the matter power spectrum transfer function from Paper 15. The DM annihilation program (01, 04, 17) provides a falsification test: phononic DM at N_pair = 1 predicts zero annihilation signal.

**Dark energy (Papers 09, 30).** The Frieman-Turner-Huterer review (09) establishes the observational landscape; the framework now sits in it via the Volovik tracking vacuum (DILUTION-CC-66) rather than as an unsolved CC catastrophe. DESI (30) provides the sharpest current test, and the framework's w_0 is pre-registered as a (value, scheme) pair (-0.918 canonical / -0.842454 R_842 branch) inside a binding falsifier rectangle for DR3 — the branch-(iv) value is currently the better fit to DR2 (0.731 sigma vs 2.130 sigma). This is the framework's single most consequential near-term test, and unlike the S57 state it is now backed by a tracking-vacuum mechanism for *why* w_0 != -1.

**Vacuum decay (Papers 05, 27).** The framework's instanton gas (S_inst = 0.069) is not a vacuum decay in the Coleman-De Luccia sense (Paper 27). The bounce action is effectively zero -- this is a quantum critical point, not tunneling. The Higgs metastability connection (Paper 27: lambda turns negative at ~10^{11} GeV) is relevant because the framework's T_init = 8.32 x 10^{15} GeV is above the instability scale. If the framework's internal geometry modifies the Higgs effective potential (through KK loop contributions, as discussed in Paper 27 Section on extra dimensions), this could affect vacuum stability.

**Klein bottle cosmology (Papers 25, 26).** The framework's CP = 0 result contrasts with Greene's topological CP violation from non-orientable compactification. The Bogoliubov particle production in Paper 26 (|beta_k|^2 ~ 10^{-3}-10^{-4} from brane transit through condensate wall) is structurally identical to the Parker mechanism computed in S57 W2-1 (|beta|^2 = 1.015 from BA mode frequency change during transit). The mathematics is the same; the physical setups differ (Klein bottle condensate wall vs SU(3) Jensen deformation). This parallel deserves exploration.

**Hubble tension (Papers 07, 12).** The framework does not address the Hubble tension. My Paper 12 result -- that the tension cannot be resolved by pre-recombination physics alone -- means the framework would need a post-recombination mechanism to contribute. The framework's late-time expansion history is unspecified.

---

## 8. Recommendations for the Project

I am keeping the S57 recommendations and marking each with what the framework actually did in S58-S93, because the audit trail of "I recommended X, the project computed X, here is the result" is itself informative. Four of the seven original recommendations have been executed; the executions changed the framework's cosmological standing materially.

### 8.1. Compute the phononic DM transfer function T(k) — DONE (S58)

This was my "single most impactful computation" recommendation. **Executed:** T(k) = 1.0000 at all observable scales — CDM-like, no cutoff (`framework-dm-properties.md`). It passes Lyman-alpha trivially (no cutoff to violate m_WDM > 5.3 keV) but, as I note in §6 Test 5, is therefore non-discriminating at the power-spectrum level. The decisive test came back, it passed, and the lesson is that the phononic DM's distinctive signatures are elsewhere (annihilation nulls, f_NL shape).

### 8.2. Derive the late-time expansion history H(z) — PARTIALLY EXECUTED (S68/S69); the full backbone remains the live recommendation

**Partially executed.** The framework now has w_0 (-0.918 / -0.842454), the ISW cross-correlation (ISW-TRACKING-68: +12.3% vs LCDM, 0.49 sigma), and sigma_8 = 0.811 — a partial late-time dark-energy sector (§3e, §5.4). What remains is the *full* H(z)/distance-redshift backbone (sound horizon, BAO scale, SN Ia distance modulus) derived from the spectral-action Friedmann equation. **This is still my top structural recommendation**: derive H^2 = (8 pi G/3) rho from the a_0 + a_2 spectral-action decomposition so the framework can be fit jointly to Planck + DESI + SN Ia. The DILUTION-CC tracking law supplies the a_0 scaling (conditional on C10); the closed Friedmann equation is the missing piece.

### 8.3. Resolve the integrability/CC problem — DONE (S66, conditional on C10)

I framed this as "resolve the integrability problem or accept the CC as unsolved." **Executed, via a route I did not anticipate:** the CC was resolved not by breaking integrability but by recognizing the vacuum tracks the expansion (DILUTION-CC-66, rho_vac ~ M_Pl^2 H^2, ratio 1.032). The five candidate integrability-breaking mechanisms I worried about are moot. The remaining open piece is narrow and well-defined: derive the C10 scaling form (rho_vac ~ M_Pl^2 H^2) from the spectral triple from first principles (the §VII.AT slot). I recommend promoting that derivation, because the entire CC resolution is currently conditional on it.

### 8.4. Compute the spectral index from a surviving route — DONE (S62/S84-85)

**Executed.** The Hubble slow-roll route gives n_s_framework = 0.9561 (gauge-invariant, S84-85; first-viable S62 at 0.9567; triple-confirmed Bogoliubov-invariant S73a). Against Planck this is 1.4-2.1 sigma — O(1) sigma, not 262 sigma. The naive KZ n_s = 2.065 was the wrong observable (the excitation spectrum P(K), not the curvature tilt). The framework is NOT falsified at the spectral index; my S57 "262-sigma, falsified as a complete cosmological model" conclusion is superseded (§5.2). The remaining n_s work is the (value, scheme) disambiguation (0.9561 vs 0.9567) and pinning the substrate-distance alpha_s = -0.0859 cleanly apart from the inflationary running (a symbol-overload hygiene issue, not a physics gap).

### 8.5. Baryogenesis via the Bogoliubov/Klein-bottle parallel — STILL OPEN (a live recommendation)

The Parker/Bogoliubov particle production in the framework is mathematically identical to the mechanism in Paper 26 (Klein bottle baryogenesis). I still recommend investigating whether the same formalism that produces DM (Leggett mode squeezing, the mechanism behind LEGGETT-MOMENT-70) also produces baryons. The obstacle is unchanged and remains genuinely open: CP = 0 structurally (S52, three proofs), so the Sakharov C/CP-violation condition is not met within SU(3); off-Jensen deformations might break this but have not been computed. Baryogenesis is one of the framework's real remaining gaps (§5.6, §5.7) — I do not have a result to report here, and I am not manufacturing one.

### 8.6. Free-streaming constraint — SATISFIED (S58, via the T(k) work)

Paper 16 constrains single-species hidden DM to z_tr > 6.2e7. This is now addressed by the S58 transfer-function work (`framework-dm-properties.md`): T(k) = 1.0000 CDM-like, with the effective warm-DM mass and free-streaming horizon recorded, and the constraint satisfied because at M_KK ~ 10^16 GeV the Leggett quasiparticle is non-relativistic from extremely early times. The recommendation is executed; the constraint passes.

### 8.7. Engage with the DESI DR3 prediction honestly — the prediction has been updated and a binding rectangle pre-registered

The S57 version of this recommendation cited a now-dead pre-registration (w_0 = -0.509 +/- 0.079, which was the S49 Zubarev-Keldysh band). That band is superseded. The current pre-registration is the (value, scheme) pair w_0 = -0.918 (canonical Volovik partition) / -0.842454 (R_842 branch-(iv) substrate-compaction), w_a = 0, inside the binding falsifier rectangle R_842 = [-1.05, -0.85] x [-0.2, +0.2] under the S84-DR3-RESPONSE-PROTOCOL (§3b, §6 Test 1). Against DESI DR2 (-0.752 +/- 0.057), post-Dovekie sigma-distances are 2.130 sigma (canonical) / 0.731 sigma (branch-(iv)) — the substrate-compaction branch is the better current fit. The framework HAS confronted this head-on: it pre-registered a rectangle with a documented response protocol before DR3. My recommendation now is simply to hold to the pre-registration when DR3 lands — do not move the rectangle after seeing the data (that would be the post-hoc-pre-registration-editing failure mode). This is the framework's strongest near-term test, and its honesty here is exemplary.

---

## Appendix: Convention Translation Table

This table maps between standard FRW cosmological conventions and the phonon-exflation framework's spectral geometry conventions. Mismatches in this mapping are a source of systematic uncertainty in all cosmological predictions.

This table is updated to current canonical values (S93; pinned to `canonical_constants.py` unless noted). Where a framework quantity is scheme-dependent it is given as a (value, scheme) pair. Rows whose S57 status was "wrong" or "uncomputed" and are now resolved are marked [RESOLVED]; rows still genuinely open are marked [OPEN].

| Cosmological Quantity | Standard Convention | Framework Equivalent (S93 canonical) | Notes |
|:---|:---|:---|:---|
| Hubble parameter H(z) | H^2 = (8piG/3) rho | Full H(z) not yet derived; w_0/ISW/sigma_8 sector present | [OPEN] Friedmann from a_0+a_2 still the live gap (§5.4) |
| Scale factor a(t) | FRW metric ds^2 = -dt^2 + a^2 dx^2 | a_acoustic = a_geom * sqrt(rho/c_s) | BLV acoustic metric (S53) |
| Dark matter density Omega_DM h^2 | 0.1186 +/- 0.0020 (Planck18); 0.264 obs (DR2) | 0.11995 (LEGGETT-MOMENT-70, Type-F trace) | [RESOLVED] ~1% Planck18 / sub-1% DR2; factor-3 closed |
| CC / dark energy density | 5.96e-30 g/cm^3 (rho_obs) | rho_vac ~ M_Pl^2 H^2 -> rho_vac/rho_obs = 1.032 | [RESOLVED, cond. C10] DILUTION-CC-66; CC_OOM=115.5 = dilution DEPTH |
| EOS w(z) | w_0 = -1, w_a = 0 (LCDM) | w_0 = -0.918 (Volovik) / -0.842454 (R_842 branch); w_a = 0 | Binding DESI DR3 test (R_842 rectangle) |
| Spectral index n_s | 0.9649 +/- 0.0042 (Planck) | 0.9561 (gauge-inv slow-roll) / 0.9567 (Hubble-SA) | [RESOLVED] 1.4-2.1 sigma; naive-KZ 2.065 was wrong observable |
| Running alpha_s = dn_s/dln k | -0.0045 +/- 0.0067 (Planck); +0.0023 +/- 0.0063 (ACT+Planck) | substrate-distance (n_s^2-1) = -0.08587279; inflationary ~0 | SYMBOL OVERLOAD: -0.0859 is substrate-distance, NOT CMB-pivot running |
| Tensor-to-scalar ratio r | < 0.036 (BK Stage-4, 2 sigma) | 0.0117315 (Path-C, G46) / 0.0074705 (Path-H) | [RESOLVED] PASS; supersedes S44 r=3.86e-10; LiteBIRD-decisive |
| Tensor tilt n_T | (slow-roll: -r/8) | -3.024e-3 (k_CMB) / +0.4676 (transit GEOMETRIC FLOOR) | 54.04 decades separate transit & CMB k-scales |
| sigma_8 | 0.811 +/- 0.006 (Planck) | 0.811 | Planck-consistent |
| ISW cross-correlation A_ISW | 1.00 +/- 0.25 (Planck) | 1.1230 (c_s^2_DE=0) -> +12.3% vs LCDM | [RESOLVED] 0.49 sigma; SNR ~ 1.58 (ISW-TRACKING-68) |
| N_eff | 3.044 (SM) | 3.044 (S75 thermalization; GGE ICs erased) | [RESOLVED] matches SM to machine zero |
| Reheating temperature T_RH | free param (BBN: > ~1 MeV) | 1.70e15 GeV (S77, N_decay=63.4) | [RESOLVED] GUT-scale, no SUSY tuning |
| f_NL (non-Gaussianity) | -26 +/- 47 equil (Planck) | equil 0.0547 / folded 0.129 / template 0.7685 | folded shape UNIQUE but DETECTOR-STERILE |
| CMB feature multipole | smooth damping tail | l = pi x 229.48 = 720.9 (second sound) | delta C_l/C_l = 0.7%; CMB-S4 reach |
| Temperature T | CMB photon temperature | T_acoustic = 0.112 M_KK | GUT scale, zero parameters |
| Particle mass m | Rest mass (GeV/c^2) | Dirac eigenvalue lambda_k(tau_0) x M_KK | Requires tau_0 and M_KK |
| Internal volume | V_extra (compact dimensions) | V_Haar = 32 x 42.2 M_KK^{-8} | Volume-preserving (exact) |
| Planck scale M_Pl | 1.22 x 10^{19} GeV | M_KK_gravity = 7.4287e16 GeV | From spectral zeta / Newton's G route (S42) |
| Matter power spectrum T(k) | CDM: T(k) = 1 | T(k) = 1.0000 (CDM-like, S58) | [RESOLVED] no cutoff; non-discriminating |
| Sound horizon r_s | 147 +/- 0.3 Mpc (Planck) | Not yet computed | [OPEN] requires H(z) |
| BAO scale | d_A(z)/r_s, H(z)*r_s | Not yet computed | [OPEN] requires H(z) |
| PBH number density n_PBH | (observational, JWST LRD) | n_edge_sat x prob_form / L_pix_LRD^3 (§VII.AX) | dimensionful Level-3 anchor HELD pending physical-scale anchor |
| Number of extra dimensions n | 0 (4D LCDM), 6 (string), 2-7 (LED) | 8 (SU(3), fixed) | Not LED; Planck-scale |

The most important update to this table since S57: the four rows that were the framework's headline deficiencies — CC (was "114 OOM above observation"), n_s (was "262-sigma, CLOSED"), Omega_DM (was "factor-3 ambiguity"), and r (was "untestable") — are now all marked [RESOLVED] (the CC conditional on C10). The remaining [OPEN] rows are the full H(z) backbone (and the r_s/BAO scales that depend on it) and the dimensionful n_PBH Level-3 anchor. Every comparison still passes through the spectral-action energy decomposition; the difference from S57 is that the dark-matter abundance no longer depends on the assumed E_matter <-> Omega_m identification (the Type-F trace bypasses it), while the full distance ladder still does. Deriving the Friedmann equation from the a_0 + a_2 spectral-action source terms is the one computation that would close the remaining [OPEN] rows at once.

---

## References

### Framework Documents
- `sessions/framework/Phononic-framework-hypothesis.md` -- core hypothesis
- `sessions/framework/Phononic-Crystal-Geometry.md` -- geometric structure
- `sessions/framework/Classification-of-phonon-exflation.md` -- Landau classification
- `sessions/framework/Phononic-Investigation.md` -- investigation status
- `sessions/framework/registry/spectral-post-mortem.md` -- spectral action closure chronicle
- `sessions/framework/framework-bbn-hypothesis.md` -- BBN connection
- `sessions/framework/framework-chaotic-instantons.md` -- instanton physics

### Session 57
- `sessions/archive/session-57/session-57-results-workingpaper.md` -- 25 computations
- `sessions/archive/session-57/session-57-master-collab.md` -- 5-reviewer synthesis

### Mack/Greene Corpus (by number)
- 01: Mack (2013), DM annihilation unknowns (1309.7783)
- 04: Schon-Mack-Wyithe (2017), DM circumgalactic medium (1706.04327)
- 05: Mack-McNees (2018), extra dimensions + micro BH (1809.05089)
- 07: Lin-Mack-Hou (2019), Hubble tension (1910.02978)
- 09: Frieman-Turner-Huterer (2008), dark energy review (0803.0982)
- 10: Lin (2019), TASI DM models (1904.07915)
- 11: Mack-Song-Vincent (2019), micro BH neutrino telescopes (1912.06656)
- 12: Lin-Chen-Mack (2021), uncalibrated cosmic standards (2102.05701)
- 13: Friedlander-Mack-et al. (2022), PBH extra dimensions (2201.11761)
- 15: Ganjoo-Erickcek-Lin-Mack (2022), hidden sector particles (2209.02735)
- 16: Lin-Chen-Ganjoo-Hou-Mack (2023), hidden dark matter (2305.08943)
- 17: Hou-Mack (2024), DM annihilation cosmic dawn (2411.10626)
- 19: Greene-Levin (2007), dark energy + extra dimensions (0707.1062)
- 20: Greene-Kabat-Marnerides (2009), decompactification (0908.0955)
- 21: Greene (2010), bulk inflaton large gap (1001.1423)
- 22: Greene (2011), brane motion KK splitting (1103.2174)
- 23: Greene (2013), landscape instabilities (1303.4428)
- 25: Greene (2025), non-orientable CP (2510.05270)
- 26: Greene (2025), Klein bottle cosmology (2511.23447)
- 27: Vacuum decay review (2015)
- 28: Bonanno (2018), asymptotic safety inflation (1803.02355)
- 29: Planck Collaboration (2018), cosmological parameters
- 30: DESI Collaboration (2024), BAO results
