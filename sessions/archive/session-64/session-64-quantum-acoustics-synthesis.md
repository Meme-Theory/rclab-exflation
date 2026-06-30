# Session 64 Synthesis: The Acoustic Reckoning

**Date**: 2026-04-01
**Agent**: quantum-acoustics-theorist (Workhorse-Quantum-Acoustics)
**Source Documents**:
- `sessions/archive/session-64/session-64-results-workingpaper.md`
- `sessions/archive/session-63/framework-cc-oom.md`
- `sessions/archive/session-63/session-63-hawking-quantum-acoustics-workshop.md`
- `sessions/archive/session-63/session-63-volovik-van-den-dungen-workshop.md`

---

## I. Session Outcome

Session 64 mapped the cosmological constant problem to its structural core, resolved the tensor-to-scalar ratio crisis from S62/S63, and taught me -- the acoustic specialist -- that I had been importing a transport intuition into a scattering problem. The session produced 7 permanent theorems, closed 5 additional CC mechanisms (bringing the total to 14 closures), established r = 0.033 below BICEP/Keck from two independent computations, and reduced the scalar amplitude gap from 8 to 3.16 OOM through the Bogoliubov transfer function. My three direct computations yielded one PASS (SECTOR-SELECTIVE-BREAKING-64), one FAIL (LINEWIDTH-HIERARCHY-64), and one INFO (PHASE-BOGOLIUBOV-64). The FAIL corrected a prediction I made in S62 (QA-E5) and exposes a conceptual error in my reasoning that I must document honestly. The Master Gate CC-COMBO-64 = FAIL.

---

## II. Key Results

### 1. LINEWIDTH-HIERARCHY-64 -- The Prediction I Got Wrong

**Result**: Gamma_B2 = 1.337 > Gamma_B1 = 1.126 > Gamma_B3 = 1.030 M_KK. PHONONIC. Gate: FAIL.

In the S62 collab review, I predicted (QA-E5) that the linewidth hierarchy would be Gamma_B3 > Gamma_B1 > Gamma_B2, with the flat band B2 exhibiting the SMALLEST scattering rate due to its zero group velocity suppressing phonon-phonon interactions. The computed result is exactly REVERSED. B2 has the LARGEST linewidth, and all quality factors are Q < 1.

**What went wrong.** I conflated two distinct physical regimes: phonon transport in a continuum, and phonon scattering on a discrete spectrum. In a continuum phonon system (say, a real crystal), the phonon mean free path is lambda = v_g * tau_scatt, and flat-band phonons with v_g = 0 carry no heat and have zero thermal conductivity. The transport is suppressed. I imported this into the scattering rate, reasoning that zero group velocity means zero transport means suppressed scattering. This is wrong on a discrete spectrum. The scattering rate Gamma_k = (2*pi) * sum_{k'} |V_{eff}(k,k')|^2 * L(E_k - E_k', eta_k') depends on the density of energy-conserving final states weighted by matrix elements, not on the group velocity of the initial state. On the B2 flat band (bandwidth W = 0.058 M_KK), the modes are nearly energy-degenerate. The Lorentzian L = eta/((dE)^2 + eta^2) peaks sharply when dE is small. For B2-B2 scattering: dE ~ 0.03-0.13 M_KK with eta_B2 = 0.012 M_KK gives Lorentzian values 1-10 (near-resonant). For B3-B3 scattering: dE ~ 0.07-0.08 M_KK with eta_B3 = 0.65 M_KK gives Lorentzian values ~1.5 (off-resonant). The narrow B2 broadening concentrates spectral weight at the resonance, making B2-B2 the dominant scattering channel.

The condensed matter literature is unambiguous on this point: flat bands near the Fermi surface enhance pairing and scattering, not suppress it. In nuclear structure, the degenerate j-shell with uniform pairing has the strongest Cooper effect precisely because the density of pair-scattering final states is maximized. I knew this from S31Ca (||V||/W = 2.59 = strong coupling on B2), from S43 (FGR breakdown with |V_rem|^2 * rho / DeltaE^2 ~ 10^9 for B2-B2), and from the very definition of the flat band as a bound-state-in-continuum. The information was available. I drew the wrong conclusion because I was thinking about sound propagation (transport) rather than sound scattering (decay rates).

**The correction to record.** Never import group-velocity arguments into scattering-rate calculations on discrete spectra. The relevant quantity for decay is the energy-resolved matrix-element-weighted density of final states, not the spatial propagation speed of the initial state. The hierarchy Gamma_B2 > Gamma_B1 > Gamma_B3 is set by two cooperating effects: (a) Josephson anisotropy delta_t_k is largest for modes near the Fermi surface (B2), contributing 75.9% of total |V_eff|^2; (b) the B2 flat-band broadening eta is smallest, making the Lorentzian sharper and the near-degenerate scattering more resonant. Both effects enhance B2 scattering.

**Structural consequence.** All quality factors Q < 1 (B2: 0.4, B1: 0.8, B3: 1.1). The quasiparticle picture is breaking down. The GGE relic is a non-thermal state of STRONGLY interacting quasiparticles, not a dilute gas of long-lived phonons. This means DM stability -- if Leggett modes are to serve as the dark matter candidate -- cannot rely on individual quasiparticle lifetimes. It must rely on collective mode protection (RPA, Leggett gap, phase coherence), which is a qualitatively different mechanism. The S57 Bogoliubov squeezing analysis of Leggett modes remains valid because it operates on the collective gap frequency, not on individual quasiparticle lifetimes.

### 2. Transfer Function and the A_s Gap Reduction

**Result**: A_s gap reduced from 8.01 to 3.16 OOM. PHONONIC. Gate: TRANSFER-BOGOLIUBOV-64 PASS.

The Bogoliubov transfer function decomposes the 8-OOM gap between the full spectral action S_fold = 250,361 and the observed scalar amplitude A_s = 2.1 x 10^{-9} into three structurally independent suppression steps:

| Step | Suppression | Cumulative gap | Mechanism |
|:-----|:------------|:---------------|:----------|
| Bare spectral action | -- | 8.01 OOM | Full mode count |
| BCS occupation weighting | -1.12 OOM | 6.89 OOM | v_k^2 coherence factors |
| Peter-Weyl (0,0) selection | -3.50 OOM | 3.39 OOM | Only SU(3) singlets couple to 4D metric |
| Gap tunneling (16 gaps) | -0.23 OOM | 3.16 OOM | Landau-Zener through hybridization gaps |

The dominant suppression is representation-theoretic: only 16 of 155,984 D_K modes are SU(3) singlets (dim^2 = 1 for the (0,0) sector). This is the Peter-Weyl selection rule. Modes carrying SU(3) gauge quantum numbers -- the (1,0), (0,1), (1,1), (2,0), ... sectors -- decouple from the scalar metric perturbation because the trace over gauge indices vanishes. The (0,0) sector's spectral weight S_occ_00 = 6.016 is 3.19 x 10^{-4} of S_occ = 18,852.

From the acoustic perspective, this is the statement that only radially symmetric vibrational modes of the fiber couple to the base-space metric. Modes with angular momentum (higher PW sectors) average out over the fiber and cannot source large-scale scalar perturbations. The 3.50 OOM suppression is a permanent structural feature, independent of dynamics.

The gap tunneling through 16 hybridization gaps (from S62 PHONON-DISP-FULL-62) is a minor 0.23 OOM correction. The largest gap (Delta = 0.260 M_KK) transmits 83% of the amplitude; the smallest (0.009 M_KK) transmits 99.98%. All gaps are in the adiabatic regime (Delta << W_local), making the Landau-Zener transmission efficient. This confirms the S62 workshop conjecture QA-E3: the transfer function depends on the total (0,0) spectral weight, not on individual gap details.

Trans-Planckian universality is confirmed: variation across three cutoff families (Gaussian, sharp, zeta-s4) is factor 1.33, well below the factor-2 threshold. The physical output is UV-independent, consistent with the van Hove protection mechanism established in S60 (TRANSPLANCKIAN-BOGO-60).

The remaining 3.16 OOM gap between the framework's (0,0)-sector prediction and A_s_CMB requires either a normalization factor from the proper mode-counting in the Mukhanov-Sasaki equation (shown inapplicable by W4-A) or a resonant enhancement at the van Hove fold. This is the next open structural question for the scalar amplitude.

### 3. The Four-Speed Acoustic Hierarchy

**Result**: c_mod = 1.000 > c_BLV = 0.485 > c_BA = 0.399 > c_L = 0.025 M_KK. PHONONIC. Gate: SOUND-SPEED-64 PASS.

Session 64 established the complete four-speed hierarchy governing wave propagation on the substrate. Each speed governs a distinct physical channel, and the ordering is structurally determined:

| Speed | Value | Governs | Physical origin | He-3B analog |
|:------|:------|:--------|:----------------|:-------------|
| c_mod | 1.000 | Tensor (graviton) | Canonical modulus kinetic term P(X) = X - V | First sound |
| c_BLV | 0.485 | Scalar (zeta), acoustic horizon | Anisotropic spectral action: Z_spectral / d2S_dtau2 | Fourth sound |
| c_BA | 0.399 | BCS condensate, GGE dynamics | Josephson phase stiffness on CG(24) | Second sound |
| c_L | 0.025 | Dark matter (Leggett) sector | Inter-band coherence gap (epsilon * E_J) | Spin waves |

The critical result is the identification of c_BLV = 0.485 as the scalar sound speed, which restores the Mach 13.8 supersonic transit. The W1-E computation had reported subsonic Mach numbers (0.17-0.27) due to a dimensional error: it confused sqrt(Z/G) (a mass scale with dimensions of energy) with a propagation speed (dimensionless in natural units). The correct Mach number is v_terminal / c_BLV = 26.5 / 0.485 = 54.7 for the terminal velocity, or v_friction / c_BLV = 6.67 / 0.485 = 13.8 for the friction velocity. The transit is deeply supersonic throughout.

This resolves the apparent contradiction between the S38 "Mach 13.75" supersonic transit and the W1-E "subsonic" claim. The acoustic horizon EXISTS at all tau in [0.05, 0.30]. Pre-transit modes cannot communicate with post-transit modes. The sonic white hole interpretation is structurally intact.

The He-3B analogy carries physical content, not merely notational convenience. In He-3B, the four sound modes arise from four distinct broken-symmetry channels: first sound (density, fastest), fourth sound (entropy), second sound (superfluid counterflow), and spin waves (slowest). The framework's four speeds emerge from four distinct spectral channels: the full spectral action (geometry), the spatial-temporal anisotropy of the product Dirac operator, the Josephson phase coherence, and the inter-band Leggett coupling. The ordering c_geom > c_scalar > c_condensate > c_interband is a consequence of the coupling hierarchy: modes that couple to the full spectral action (all eigenvalues) propagate faster than modes coupling to the BCS order parameter (8 eigenvalues near the Fermi surface), which propagate faster than inter-band coherence modes (gap-suppressed by epsilon = 0.00374).

### 4. Chirality and the Absence of Cancellation

**Result**: C_chiral = 1 exactly. {gamma_9, dD_K/dtau} = 0 to machine epsilon. GEOMETRIC/PHONONIC.

The KO chirality operator gamma_9 on D_K generates a spectral pairing: every eigenvalue lambda_n is paired with -lambda_n, and their tau-derivatives are antisymmetric (d(lambda_n)/dtau = -d(-lambda_n)/dtau). This was verified numerically across 9 PW sectors (1216 eigenvalues) to relative precision 9.5 x 10^{-11}.

The acoustic consequence is that the scalar source dS/dtau involves products of eigenvalues with their derivatives: f'(lambda^2) * 2*lambda * (dlambda/dtau). For a chiral pair, both the eigenvalue and its derivative flip sign, so their product is INVARIANT. Chiral pairs ADD constructively in the scalar source -- they do not cancel. This is the antisym-times-antisym = symmetric identity. Similarly, the second-order tensor source involves products of two antisymmetric derivatives, which is again symmetric.

What chirality DOES kill is the linear (first-order) tensor source: the eta-invariant eta(D_K) = 0 exactly, and the index ind(D_K) = 0. Any quantity linear in the eigenvalues with equal positive/negative weight vanishes. But the physical sources (scalar and tensor power spectra) are quadratic, and the chirality identity prevents cancellation at this order.

This result is permanent. It constrains any future attempt to invoke chirality as a suppression mechanism for cosmological observables. The C = 1 identity means the full spectral action gradient is available for transit driving and perturbation production -- there is no "chirality tax" on the scalar amplitude.

### 5. Sector-Selective Breaking and the Fermi-Surface Lock

**Result**: |delta_E_ZP / E_ZP| = 2.63 x 10^{-4}. v^2(B2[0]) = 1/2 exactly. PHONONIC. Gate: PASS.

The gravitational channel to the (0,0) condensate is OPEN at O(alpha_G), but quantitatively insufficient by 110 OOM. The computation loaded the gravitational eigenvalue shifts delta_eps_k from W1-B and solved the perturbed BCS gap equation self-consistently.

The structurally significant finding is the Fermi-surface lock: v^2(B2[0]) = 0.500000 before and after the gravitational perturbation, to machine epsilon. This is not a fine-tuning -- it is a kinematic identity of BCS theory. When a mode sits at the Fermi surface (eps = 0), its Bogoliubov occupation is v^2 = (1/2)(1 - eps/E) = 1/2 regardless of the gap Delta. The only way to change v^2(B2[0]) is to move it off the Fermi surface (shift the chemical potential), not to modify its energy in the gap equation.

This is STRONGER than the sector-selective obstruction from the Peter-Weyl Casimir (C_2^{PW}(0,0) = 0). The Casimir argument is group-theoretic; the Fermi-surface lock is purely kinematic. The cc-path-g.md estimate of delta(v^2_{B2[0]}) = +4.1 x 10^{-5} was wrong because it used eps_B2 = 0.845 M_KK (the D_K eigenvalue measured from zero) rather than the BCS single-particle energy relative to the chemical potential (which is zero by construction for the mode at the Fermi surface).

The gap INCREASES by 0.038%, strengthening Cooper pairing. The vacuum energy DECREASES by 2.63 x 10^{-4}, in the correct direction for CC relaxation. But the shortfall is 110 OOM. The gravitational backreaction is a perturbative O(alpha_G) ~ 10^{-3.6} correction to a quantity that needs O(10^{-114}) suppression. Bootstrap iteration confirms first-order sufficiency (correction 0.03%).

### 6. Bogoliubov Phases: pi Exactly, Invisible Observationally

**Result**: phi_Bog = pi + 2.41 x 10^{-4} rad. Phase coherence R = 1.0000. max |delta_l/l| = 7.67 x 10^{-5}. PHONONIC. Gate: INFO (NEGLIGIBLE).

The Bogoliubov coefficients at k = 0 (which is where all CMB peaks sit, given the 56 OOM hierarchy between k_CMB ~ 10^{-20} M_KK and k_KK ~ 1 M_KK) have the form beta_k = -|beta_k|, i.e., they are negative real for ALL 8 BCS modes. The phase is pi to within 10^{-4} rad. This is the exact sudden-quench result: the transit at v_tau = 442 M_KK is effectively instantaneous relative to all mode frequencies (omega_max ~ 5 M_KK at k = 0), so the adiabatic parameter eta = v_tau |domega/dtau| / omega^2 >> 1.

The |beta|^2 values match the sudden-quench formula (r + 1/r - 2)/4 to 10^{-12}, confirming the S57 mode-independent BA theorem: the transit is a conformal stretching that produces identical |beta|^2 for all Bogoliubov-active modes.

Phase coherence is COMPLETE (R = 1.0000 to 6 decimal places). All modes are created with identical phase. This confirms the S63 Mack workshop prediction: impulsive transit produces coherent pair creation, not random-phase stochastic production.

However, the pi phase is INVISIBLE in the TT power spectrum. C_l measures |delta(k)|^2, which is insensitive to the overall sign. The physical peak shift comes only from the finite-time correction delta_phi = pi - phi_Bog = 2.4 x 10^{-4} rad, giving delta_l/l = -delta_phi / (n*pi) for peak n. The largest shift (peak 1) is delta_l = -0.017, which is 39x below Planck precision (sigma_l ~ 0.66). The prediction is structurally robust but observationally below threshold.

A critical technical lesson: linear phase averaging near +/-pi gives the WRONG answer (the initial computation returned -0.464 rad due to phase wrapping). Use circular mean ALWAYS when phases cluster near pi.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| SECTOR-SELECTIVE-BREAKING-64 | **PASS** | |delta_E_ZP/E_ZP| = 2.63e-4 > 10^{-6}. 110 OOM shortfall |
| LINEWIDTH-HIERARCHY-64 | **FAIL** | Gamma_B2 > Gamma_B1 > Gamma_B3 (REVERSED from QA-E5) |
| PHASE-BOGOLIUBOV-64 | **INFO (NEGL)** | phi_Bog = pi + 2.4e-4 rad. |delta_l/l| = 7.67e-5 < 10^{-4} |

Other session gates with acoustic significance (not my direct computations):

| Gate | Verdict | Acoustic Implication |
|:-----|:--------|:--------------------|
| TRANSFER-BOGOLIUBOV-64 | PASS | A_s gap 8.01 -> 3.16 OOM. PW selection dominates |
| SOUND-SPEED-64 | PASS | Four-speed hierarchy. Mach 13.8 restored |
| CHIRALITY-SELECTION-64 | INFO | C=1 exactly. No chirality suppression of scalar source |
| TENSOR-BURST-64 | PASS | r = 0.033 < 0.036. H2 kills first-order tensors |
| NS-FINAL-64 | PASS | n_s = 0.9557 +/- 0.0036. Sound speed EXCLUDED from tilt |

---

## IV. Structural Implications

### What the LINEWIDTH FAIL Teaches About the Acoustic Perspective

The FAIL is not just a wrong prediction. It reveals a systematic bias in my reasoning that I need to correct going forward. The bias is: I tend to think about the substrate in terms of TRANSPORT (sound propagation, group velocity, mean free path, thermal conductivity) rather than SCATTERING (decay rates, matrix elements, density of final states). In a continuum system with well-defined quasiparticles (Q >> 1), these perspectives converge: the scattering rate sets the mean free path which sets the transport coefficient. But the substrate at the fold is in the strong-coupling regime (Q < 1 for all branches), where the quasiparticle picture breaks down and the two perspectives diverge.

The transport perspective says: flat band -> zero group velocity -> no propagation -> no scattering. The scattering perspective says: flat band -> energy degeneracy -> enhanced density of final states -> MAXIMUM scattering. On a discrete spectrum with Lorentzian broadening, the scattering perspective is correct. The transport perspective applies in the thermodynamic limit with well-defined quasiparticles. The substrate's 8-mode spectrum in the strong-coupling regime is about as far from that limit as possible.

This bias explains several earlier near-misses in my reasoning:
- In S43, I noted FGR breakdown for B2-B2 (|V|^2 rho/DeltaE^2 ~ 10^9) but did not connect this to the ENHANCED scattering that FGR breakdown implies.
- In S56, I characterized the BA sound speed c_BA = 0.399 as "monotone decreasing" and labeled this "no acoustic stabilization," when the relevant question was not about sound propagation but about scattering channels.
- In S62, when formulating QA-E5, I explicitly invoked "group velocity arguments" to predict B2 suppression. The S62 collab review even flagged this as a testable prediction. It was testable. It failed.

The correction: when analyzing scattering on discrete spectra, start from the matrix element and the density of final states. Never begin with group velocity. Group velocity governs where energy goes in real space; the scattering rate governs how fast energy redistributes in mode space. On a discrete spectrum without spatial extent, only the latter matters.

### The Four-Speed Hierarchy as Organizational Principle

The four speeds are not merely numerical values -- they encode the coupling hierarchy of the substrate. In Landau's quasiparticle framework, the number of distinct sound modes equals the number of distinct broken-symmetry channels. The phonon-exflation substrate has four:

1. **Geometric channel** (c_mod = 1): all D_K eigenvalues couple collectively. The full spectral action S(tau) serves as the potential. This is the "fastest sound" because it involves the largest number of degrees of freedom.

2. **Scalar perturbation channel** (c_BLV = 0.485): the spatial-temporal anisotropy of the product Dirac operator D = D_4 x 1 + gamma_5 x D_K introduces a cross-term that makes the spatial spectral response Z_spectral differ from the temporal response d2S/dtau2. The ratio is c_BLV^2 = 0.235.

3. **Condensate channel** (c_BA = 0.399): the BCS phase mode on the Josephson array CG(24). This is the Anderson-Bogoliubov mode. It depends on E_J and the pair-transfer amplitude S_+, both of which are BCS quantities involving only the 8 modes near the Fermi surface.

4. **Inter-band channel** (c_L = 0.025): the Leggett mode, coupling internal (B2-B3) phase differences. Suppressed by epsilon = 0.00374 relative to the Josephson coupling.

The ordering c_geom > c_scalar > c_cond > c_interband follows from the number of participating modes: 155,984 > 16 (singlets) > 8 (BCS) > 3 (Leggett). Fewer participating modes means weaker restoring force means slower propagation.

### The CC Problem from the Acoustic Perspective

Session 64 closed 5 additional CC mechanisms:
- Path C along Jensen (R-monotonicity, permanent)
- Category error between Lambda_SA and Lambda_J (Lambda_SA = Lambda_J, permanent)
- S43 multi-T Jacobson
- 12D Jacobson-Kasparov (Lambda_eff = (1/8)R_K = -0.252, wrong sign)
- Spectral monotonicity decoupling (CC and area theorem are siblings, not parent-child)

The acoustic reading of the CC problem is now sharper than ever. The CC monotonicity theorem (dE_ZP/dq = sum positive terms > 0) is equivalent to the statement that all phonon modes have positive spectral weight. The CC problem = the phonon lifetime problem: if the R-G integrability were broken, the conserved charges would decay, the GGE would thermalize, and the vacuum energy would relax toward the Volovik equilibrium (rho_vac = 0). The Ordered Veil (GGE integrability) that protects the condensate is the same mechanism that prevents CC relaxation. The 14 closures have systematically eliminated every proposed integrability-breaking channel within the current spectral action framework.

The spectral moment decoupling theorem (W5-B) provides structural permission: CC resolution need not violate the NEC or break the area theorem, because CC and NEC operate through different spectral moments (F_{-1} vs F_{+1}). This is the first positive structural result for the CC -- it says the problem CAN be solved without destroying gravity. But it does not say HOW.

### Bogoliubov Phase Coherence: Structurally True, Observationally Hidden

The pi phase coherence (R = 1.0000) is a genuine structural prediction that distinguishes exflation from inflation. Standard inflation produces perturbations from quantum vacuum fluctuations, which have RANDOM phases. Exflation produces perturbations from impulsive pair creation, which has COHERENT phases (all modes created in the same sudden-quench event, all acquiring phase pi from the universal frequency-ratio change).

The distinction is invisible in C_l (which measures |delta|^2 and loses phase information) but would be visible in:
- The bispectrum B(k1, k2, k3) -- phase coherence produces specific non-Gaussian correlations
- Cross-correlations between TT and polarization spectra
- The sign of the compression-rarefaction asymmetry at the first acoustic peak

These are second-order effects requiring dedicated computation. The bispectrum signature is the most promising discriminant: a sudden-quench origin predicts f_NL with a specific scale-dependence tied to the mode-independent |beta|^2 spectrum.

---

## V. Forward Projection

### Highest Priority: BCS-Dressed Spectral Action Profile

The n_s prediction (0.9557, 2.2 sigma from Planck) has one dominant uncomputed correction: the BCS dressing of the spectral action profile S(tau). The S63 VdD workshop estimated delta(n_s) ~ +0.0014 toward Planck from Delta^2/Lambda^2 ~ 0.033. The BdG heat kernel factorization (K_BdG = exp(-Delta^2 t) * K_bare, proven exact in W3-B) provides the computational backbone. Computing S^{BCS}(tau) at 5 tau values would determine delta(eps_H) and potentially reduce the Planck tension from 2.2 to ~1.5 sigma. This is the single highest-impact computation for the observational scorecard.

### Acoustic Priorities

1. **COLLECTIVE-MODE-LINEWIDTH**: The LINEWIDTH FAIL established that individual quasiparticle lifetimes are Q < 1 (strong coupling). But the DM candidate is the collective Leggett mode, not an individual quasiparticle. The Leggett mode linewidth should be computed from the RPA response function, not from single-particle FGR. In nuclear structure, the giant dipole resonance has Q ~ 3-5 even when single-particle states have Q < 1, because the collective mode carries a different selection rule structure. Pre-register: Gamma_Leggett < omega_L (Q > 1 for the collective mode).

2. **BISPECTRUM-PHASE**: The phase coherence R = 1.0000 is invisible in C_l but should produce a specific f_NL signature. Compute the bispectrum from sudden-quench Bogoliubov modes with uniform |beta|^2 and phase pi. Pre-register: f_NL distinguishable from slow-roll inflation at 3-sigma for Planck data.

3. **A_s NORMALIZATION**: The 3.16 OOM residual gap in the scalar amplitude requires understanding the mode-counting normalization in the substrate's perturbation theory. The Mukhanov-Sasaki equation is inapplicable (W4-A, permanent), so the scalar power spectrum must be derived directly from the GGE acoustic excitation spectrum. This is the framework's native acoustic calculation.

4. **CC COLLECTIVE-THERMALIZATION**: The 14 CC closures block all single-mode and few-mode integrability-breaking channels. But the substrate has 32 cells x 8 modes = 256 degrees of freedom in the full fabric. The question is whether N-body collective effects at large N can break the R-G integrability that persists at small N. The N-PAIR-3-RG-64 PASS (<r> = 0.478 in the pairing channel) opens this door. Compute <r> at N_pair = 4, 5, 6 in the pairing-only sector. If <r> -> 0.53 (GOE) with increasing N, the collective thermalization route reopens.

### What the Acoustic Perspective Got Right

- The four-speed hierarchy (predicted S56, confirmed S64)
- The van Hove protection of physical observables from UV sensitivity (predicted S60, confirmed S64 via trans-Planckian universality PASS)
- The Bogoliubov phase coherence (predicted S57 mode-independent theorem, confirmed S64)
- The sudden-quench regime for all BCS modes (predicted S57, confirmed S64 to 10^{-12})
- The Fermi-surface lock v^2 = 1/2 (consistent with BCS kinematics, though I did not predict the exact mechanism before computation)
- The Peter-Weyl selection as the dominant amplitude suppression (S62 workshop conjecture QA-E3, confirmed S64)

### What the Acoustic Perspective Got Wrong

- **LINEWIDTH-HIERARCHY (QA-E5)**: Group velocity does not suppress scattering on discrete spectra. REVERSED ordering. The most significant error I have made in this project.
- **He-4 analogy (S56)**: Previously flagged. Z_cell^N misses Josephson condensation energy.
- The omission of Josephson dominance in early fabric estimates (S55-S56)

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Linewidth hierarchy REVERSED | PHONONIC | FAIL | Flat band enhances scattering via energy degeneracy. Q<1 all branches. Transport != scattering on discrete spectra |
| 2 | A_s gap reduced 8->3.16 OOM | PHONONIC | PASS | PW selection (-3.50 OOM) dominates. Trans-Planckian universality confirmed |
| 3 | Four-speed hierarchy complete | PHONONIC | PASS | c_mod > c_BLV > c_BA > c_L. Mach 13.8 restored. Acoustic horizon intact |
| 4 | Chirality C=1 exactly | GEOMETRIC | INFO | Antisym x antisym = sym. No cancellation in quadratic sources |
| 5 | Sector-selective breaking | PHONONIC | PASS | Channel open at O(alpha_G). 110 OOM shortfall. Fermi-surface lock: v^2=1/2 exact |
| 6 | Bogoliubov phase pi exact | PHONONIC | INFO | Sudden quench confirmed. R=1.0000. delta_l/l = 7.7e-5 below Planck |
| 7 | r = 0.033 (two independent) | GEOMETRIC | PASS | H2 kills first-order tensors. BICEP/Keck cleared by 7.4% |
| 8 | n_s = 0.9557 +/- 0.0036 | GEOMETRIC | PASS | One-loop computed. Sound speed excluded from tilt by T12 |
| 9 | CC Master Gate | NON-PHONONIC | FAIL | 14 closures. R-monotonicity permanent. Lambda_SA = Lambda_J permanent |
| 10 | Spectral moment decoupling | GEOMETRIC | PERMANENT | CC and NEC are siblings (F_{-1} vs F_{+1}), not parent-child. CC solvable without breaking gravity |
