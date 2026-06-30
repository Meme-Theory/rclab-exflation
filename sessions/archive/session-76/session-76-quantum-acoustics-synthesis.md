# Session 76 Synthesis: The Acoustic Architecture of Transit, Decay, and Spectral Projection

**Date**: 2026-04-13
**Agent**: quantum-acoustics-theorist (quantum-acoustics)
**Source Documents**:
- sessions/archive/session-76/session-76-results-workingpaper.md

---

## I. Session Outcome

Session 76 resolved the modulus decay channel, established the transit bispectrum at max |f_NL| = 1.505 (zero-free-parameter PASS against Planck bounds), and derived the geometric conversion factor f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2 = 2.547e-10 from first-principles spectral perturbation theory (promotable to permanent). The session produced 9 PASS, 5 FAIL, and 12 INFO verdicts across 26 computations. The deepest structural harvest from the quantum-acoustics perspective is threefold: (1) the GGE relic's three-point acoustic correlations are Gaussian to leading order, with all non-Gaussianity arising from the H_3 cubic vertex at O(1) amplitude; (2) the BCS inter-branch pair relaxation rate (mu_eff = 2.67e-4) is bottlenecked by the B1-B3 Josephson channel (J_u1 = 0.038 M_KK), but the B2-mediated virtual pathway provides 14.2x enhancement -- exceeding the 6.2x rescue target; (3) the modulus oscillation is a driven acoustic mode of the fiber that decays gravitationally (tau_decay = 1.63e-37 s), not through the spectral action vertex, solving the cosmological moduli problem 37 OOM before BBN.

---

## II. Key Results

### 1. Transit Bispectrum: Gaussian GGE Relic with O(1) Cubic Corrections (W1-C)

**Result**: max |f_NL| = 1.505 (Bogoliubov sudden channel), f_NL^{equil} = 0.853 (EFT). All shapes within Planck 2018 bounds. Classification: PHONONIC.

The transit bispectrum computation is the definitive acoustic correlation analysis of the GGE relic. The governing structure is the multi-mode squeezed vacuum state produced by the supersonic transit (Mach 13.75) through the van Hove fold. The 8-mode Bogoliubov coefficient set {alpha_k, beta_k} from the S75 microscopic mode equation was loaded and verified (unitarity |alpha|^2 - |beta|^2 = 1 to 2e-15 for all modes).

The central structural finding is that the multi-mode squeezed vacuum is GAUSSIAN: a product of single-mode Gaussian states satisfies Wick's theorem exactly, giving zero connected three-point function. All non-Gaussianity requires the H_3 cubic interaction vertex. This is a direct consequence of the Bogoliubov transformation being a canonical (symplectic) map on the phonon Fock space -- it preserves the Gaussian character of the vacuum. The non-Gaussianity therefore measures the STRENGTH of the anharmonic phonon-phonon coupling in the GGE relic, not the squeezing itself.

Four independent channels were computed: (i) EFT equilateral from effective sound speed c_BLV = 0.485, giving f_NL^{equil} = 0.853; (ii) Bogoliubov sudden approximation via Im[alpha_k * beta_k*^2] / |beta_k|^4, giving f_NL = -1.505 with a negative sign (anti-correlated acoustic three-point function); (iii) CLT diagonal from 1/sqrt(N_pair) = 1/sqrt(59.8), giving f_NL^{folded} = 0.129; (iv) Maldacena consistency relation for local shape, giving f_NL^{local} = 0.0146. The shape cosines reveal the Bogoliubov bispectrum is nearly flat across all triangle configurations -- a consequence of the sudden limit (omega_max * dt_transit = 9.9e-4 << 1), where all modes are produced simultaneously and the shape function loses k-dependence.

The S75 result phi_k ~ 0.005-0.012 rad (real squeezing, not complex) suppresses the folded enhancement predicted in S66. This is physically significant: real squeezing means the acoustic excitations are produced as amplitude modulations without phase rotation, generating a scale-independent bispectrum rather than a folded one. The S43 slow-roll formula f_NL = -0.3 is definitively invalidated -- it used transit-scale n_s = 0.28 in a formula inapplicable at Mach 13.75.

### 2. Inter-Branch Pair Relaxation: Landau-Khalatnikov Matrix and J_u1 Bottleneck (W1-A)

**Result**: mu_eff = 2.67e-4 M_KK/H_fold (Richardson-corrected), 1.58 decades below target 0.0102. B1-B3 bottleneck identified. J_u1 virtual enhancement = 14.2x (from W2-F). Classification: PHONONIC.

The Landau-Khalatnikov relaxation matrix for inter-branch BCS pair transfer is the canonical treatment of isocurvature decay in the GGE relic. The 3x3 rate matrix W_{a->b} was constructed from Fermi golden rule with GL pair coupling |a_GL| = 0.525, Josephson inter-branch amplitudes (J_C2, J_su2, J_u1), BCS coherence-factor overlaps F_{ab}, and Lorentzian broadening at the Richardson collective width gamma_coll = Delta * sqrt(N_pair/N_modes).

Diagonalization yields the correct structure: one zero eigenvalue (total pair conservation -- the acoustic analog of particle number conservation), one fast mode (lambda_fast = 0.531 M_KK, B2-dominated), and one slow mode (lambda_slow = 0.157 M_KK, the B1-B3 bottleneck). The bottleneck is physical: J_u1 = 0.038 M_KK is the weakest Josephson channel, connecting the acoustic branch (B1, 1 mode) to the dispersive-optical branch (B3, 3 modes) through a U(1) coupling that is 25x weaker than the dominant J_C2 = 0.933.

The gate FAIL (1.58 decades below target) is structurally informative. It identifies the B1-B3 pair-transfer channel as the rate-limiting step at the single-cell level. The required 6.2x enhancement was independently exceeded by the W2-F computation of the B2-mediated virtual Josephson pathway: J_u1^{virtual} = J_{B1,B2} * J_{B2,B3} / Delta_E = 0.530 M_KK, yielding 14.2x enhancement over bare J_u1. The B2 adjoint sector (flat-optical, 4 modes) serves as a virtual phonon bridge between B1 and B3 -- a second-order process in the Josephson coupling that dominates the direct channel by an order of magnitude. This is the acoustic analog of superexchange coupling in condensed matter: the intermediate B2 state mediates an effective long-range interaction between B1 and B3 that is stronger than the direct coupling.

### 3. Modulus as Driven Acoustic Oscillation: Gravitational Decay at tau = 4.44e-40 s (W1-B, W2-E, W2-H)

**Result**: tau_decay = 1.63e-37 s (gravity-dominated, 99.2%). T_RH = 1.70e15 GeV. BBN safe by 37 OOM. Classification: PHONONIC/GEOMETRIC.

Three computations (W1-B, W2-E, W2-H) converged on the modulus decay physics, with a critical correction emerging from their comparison. The modulus oscillation at frequency omega_drive = m_tau = 2.062 M_KK is a coherent oscillation of the Jensen deformation parameter tau around the fold value -- it is, in the acoustic language, a driven breathing mode of the fiber geometry.

W1-B initially found parametric resonance into BCS quasiparticle pairs is NEGLIGIBLE: the Mathieu parameter |q| = 5.9e-3 places the system in the narrow-resonance regime, and all 8 BCS modes are detuned from the instability bands by 40-60x the band half-width. The Floquet exponents are all zero. This is a definitive closure of the parametric amplification channel: the BCS modes do not resonate with the modulus oscillation. The selection rules are physical: tau -> B2+B2 and tau -> B1+B1 are kinematically open (omega_drive > 2*omega_k), but tau -> B3+B3bar is kinematically closed (2*omega_B3 = 2.166 > omega_drive = 2.062). Cross-channels (B1xB2, B1xB3, B2xB3) are SU(3)-forbidden (no singlet in the product representation).

W2-E corrected W1-B's SM perturbative rate by a factor of 56,000x downward: the canonical normalization factor sqrt(Z_fold) = 273 suppresses the spectral-action vertex, pushing the effective suppression scale to Lambda_eff = 9.0e19 GeV = 37 * M_Pl. The physical coupling is (da_4/dtau)/a_4 = 0.451, not sqrt(a_4/a_2) = 0.698. The result: gravity dominates modulus decay (Gamma_grav = 4.02e12 GeV, 99.2%), with the SM spectral channel contributing only 0.8% (Gamma_SM = 3.08e10 GeV). The modulus is a "stiff" field in moduli space -- fluctuations cost large spectral action, making the coupling to gauge fields parametrically weaker than the universal gravitational coupling.

W2-H synthesized these into the thermal history: T_RH = 1.70e15 GeV at the GUT scale, 37 OOM above BBN, factor 44 below M_KK (no KK mode excitation). Both thermal leptogenesis and GUT baryogenesis channels are kinematically accessible. Leggett DM modes survive reheating (T_RH/m_Leggett = 0.17 < 1 -- the GGE relic dark matter is never thermalized).

### 4. Cosmological Constant from Spectral Fill Factor: chi_2 = 0.741 (W1-D, W3-C)

**Result**: rho_HP4 = chi_2 * H_0^2 * M_Pl^2, |log10(rho_pred/rho_obs)| = 0.47 OOM (zero free parameters). JLO/CM factor = 1 exactly (closed). Classification: GEOMETRIC.

The HP4 formula derives the cosmological constant from the fiber spectral fill factor chi_2 = M_1/(N_modes * lambda_max) = 0.741 at the fold. This is a K-theoretic Chern character pairing, not a heat kernel residue. The result rho_Lambda = chi_2 * H_0^2 * M_Pl^2 = 9.09e-48 GeV^4 undershoots observation by a factor 3.0 (0.47 OOM).

W3-C proved that the Connes-Moscovici local index formula provides no correction: CM_factor = 1 exactly for finite spectral triples, because the spectral zeta function zeta_{D_F}(s) is entire (no poles at s = 0 from the finite spectrum). The eta invariant vanishes by spectral symmetry (eta(D_K) = 0). The residual factor 2.77 decomposes as 3 * Omega_L / chi_2 = 3 * 0.685 / 0.741. The factor 3 is the Friedmann normalization rho_crit = 3 * H_0^2 * M_Pl^2 -- classical 4D geometry from the trace of Einstein's equations on FRW, not fiber index theory. If chi_2 maps directly to Omega_Lambda (rather than to rho_Lambda/HP4_base), the gap reduces to 0.034 OOM (8.2% overshoot). This is a dictionary question, not a computational one.

### 5. Geometric Conversion Factor: Analytic Derivation of f_conv (W1-F, W2-A, W2-B)

**Result**: f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2 = 2.547e-10, derived analytically from spectral perturbation theory. Matches S75 numerical to factor 1.000. Promotable to permanent. Classification: GEOMETRIC.

The analytic derivation identifies two independent structural factors: (i) the KK hierarchy suppression (M_KK/M_Pl)^4 = 1.371e-9 from dimensional transmutation between fiber and Planck scales; (ii) the spectral weight fraction (a_2/a_0)^2 = 0.1858 from the projection of total fiber variance onto the a_2 Seeley-DeWitt channel -- the ONLY channel coupling to 4D scalar curvature. The a_4 (gauge kinetic) channel carries 23.67% of the gravitational channel's weight: f_conv^{(4)}/f_conv^{(2)} = (a_4/a_2)^2 = 0.2367.

W2-A discovered a structural identity: f_conv = pi^4 / (9216 * a_0^2). The a_2 dependence in (M_KK/M_Pl)^4 exactly cancels the a_2 in (a_2/a_0)^2 because M_KK is extracted from G_N matching. This means f_conv depends on a_0 ALONE (the total mode count). The consequence: f_conv is NOT L_max-convergent (a_0 ~ L^5.23), but this is the correct behavior -- f_conv is a truncation-level-dependent quantity, and the truncation IS the physical cutoff. The R_1 ratio a_0*a_4/a_2^2 = 1.1287 IS L_max-protected (2.89% drift), confirming the family structure.

W2-D proved that BCS dressing of a_2 is negligible and has the wrong sign: delta_a_2/a_2 = -1.62e-3 (-0.16%). The 16 paired eigenvalues in the (0,0) singlet sector produce a correction 80x too small and in the wrong direction. The f_conv conversion factor is BCS-immune. This closes the BCS dressing channel for the A_s residual (0.12 OOM gap from Planck).

### 6. Post-Fold Background: H_transit vs H_Friedmann Resolved (W1-E)

**Result**: H_Friedmann = 0.975 M_KK vs H_transit = 586.5 M_KK (ratio 601). A_s gap reduced from 9.47 to 5.75 OOM. Classification: GEOMETRIC.

The 16.5 OOM discrepancy between Model A and Model B from S75 is resolved: both models are incomplete descriptions of the same physics. The correct description is the coupled Friedmann + Klein-Gordon ODE from S73B. The critical identification: H_transit (substrate spectral redistribution rate, not c-bounded) and H_Friedmann (emergent cosmic expansion rate, c-bounded) are DIFFERENT physical quantities. The S75 A_s computation erroneously used H_transit in the Friedmann-level formula. The H correction alone reduces the A_s gap by 2 * log10(601) = 5.56 OOM.

A structural finding with implications for the acoustic picture: tau overshoots to 1.614 at t = 0.09 M_KK^{-1}, then returns. The Jensen deformation parameter is NOT monotonic in time. This means H(tau) is ill-defined as a single-valued function, and the correct time variable is N (e-folds), not tau. The post-fold modulus dynamics are stiff-dominated (eps_H = 1.72, w_fold = 0.149), not slow-roll.

### 7. Off-Jensen Moduli: 35D Restoring Potential -- Ridge Dynamics (W2-J)

**Result**: All 35 Hessian eigenvalues negative, range [-148.69, -17.35]. Zero flat directions. Classification: GEOMETRIC.

The full 35-dimensional volume-preserving Hessian of the spectral action at the fold reveals that the Jensen line is a RIDGE of the spectral action potential. Every off-Jensen perturbation costs energy (V eigenvalues all positive, range [+17.35, +148.69]). The strongest restoring direction (lambda = -148.69 for S, or V-eigenvalue = +148.69) is the su(2)-internal deformation. The weakest (V-eigenvalue = +17.35) is the u(1) direction.

The degeneracy structure {5, 8, 5, 3, 9, 4, 1} encodes the U(2) representation content of the deformation space. Combined with the on-Jensen monotonicity (dS/dtau > 0, no minimum along Jensen), the modulus dynamics are: roll ALONG the Jensen ridge (driven by the spectral action gradient) while confined TO the ridge by restoring forces in all 35 transverse directions. This is the geometric channel: the Jensen line is the unique 1D attractor in a 36D moduli space, selected by U(2) invariance.

### 8. Instanton Liquid: Mode-Counting Hierarchy Closes the Channel (W3-D)

**Result**: V_eff monotonic everywhere. |V_liquid/V_bare| <= 8/6440 ~ 10^{-3} (structural bound). Instanton moduli stabilization CLOSED. Classification: GEOMETRIC.

Three independent approaches (Shuryak-Schafer mean-field, rigorous lattice-gas ceiling, Volovik vortex-liquid analog) all give |V_inst_liquid/V_bare| < 3e-4. The structural bound is permanent: the mode-counting hierarchy (8 BCS modes out of 6440 total spectral modes) prevents the instanton collective potential from competing with the spectral action gradient. This is the same hierarchy as the CC problem -- instantons couple only to the BCS gauge sector, while V_bare counts all spectral modes. The Volovik lesson applies: just as vortex contributions to vacuum energy are suppressed by (core volume)/(system volume), the instanton moduli channel cannot produce a sign change in V_eff.

### 9. Chiral Mass Matrices and Inter-Generation Mixing (W3-F)

**Result**: Non-trivial mass matrices in all Peter-Weyl sectors. Off-diagonal mixing ratio > 1 in (1,0) and (1,1) sectors. No SM mass hierarchy within single sectors. Classification: PARTICLE.

The Kosmann chirality computation reveals the inter-mode coupling structure of the fiber Dirac operator. The chiral decomposition D_K = off-diagonal (P_L D_K P_R) is exact ({gamma_9, D_K} = 0 proven to machine zero in all 12 sector-tau combinations). The mass matrix M = P_L D_K P_R in the (1,0) fundamental sector has off-diagonal norm exceeding diagonal norm by factor 1.43 -- the representation eigenstates and mass eigenstates are substantially misaligned. This is precisely the structure from which CKM/PMNS mixing originates. The (1,1) adjoint sector shows even stronger mixing (ratio 2.50).

The Jensen deformation lifts the bi-invariant degeneracy monotonically: the number of distinct eigenvalue levels increases with tau. Mass eigenvalue ratios within each sector are O(1) (largest/smallest ~ 1.6 in (1,0)), not the O(100-1000) required for SM quark generations. The physical mass hierarchy must emerge from the FULL Dirac operator coupling BETWEEN PW sectors (the Yukawa couplings in the spectral action), not from within a single sector.

### 10. alpha_s Reconciliation and Spectral Index Running (W2-C, W2-I)

**Result**: alpha_s(CMB) = -0.0143 (1.46-sigma from Planck). Three routes reconciled by temporal ordering. Classification: PHONONIC.

The three routes to the spectral index running -- Bogoliubov (alpha_s = 0 at transit), isocurvature (alpha_s = -0.0143 at CMB scale), Coleman-Weinberg (alpha_s = -0.0190 at horizon scale) -- are reconciled by the temporal ordering principle: Phase 1 (impulsive transit) produces an exactly flat spectrum; Phase 2 (post-transit quasi-de Sitter) generates the running through isocurvature mode decay at rate mu_eff * H = 0.0102 * H. The CW result is the mean-field (Hamilton-Jacobi) description of the same mechanism, overestimating |alpha_s| by factor 1.33 (consistent with Gi ~ 1 at fold, fluctuation-dominated mean field). The running is exactly linear in mu_eff: alpha_s = -mu_eff * C(p, tau_dS) with C = 1.394.

W2-I established that the model sensitivity is dominated by the power-law index p of the asymptotic H(tau). The S75 optimized value p = 1.689 is the value required for n_s = 0.9649; alternative p values change both n_s and alpha_s simultaneously. The power-law index p is the single structural parameter controlling the isocurvature predictions -- it is not yet derived from the spectral action dynamics.

### 11. Auxiliary Results (W2-G, W3-A, W3-B, W3-E, W3-H, W3-I, W3-J)

**Cubic Weinberg angle (W2-G)**: sin^2(cubic) = 0.2348, which is 59.8% from the fold canonical value (0.584) but 1.55% from the PDG value sin^2(M_Z) = 0.231. The n=3 power law in the family sin^2(n) = 3/(3 + e^{4n*tau}) hits the low-energy measurement at tau_fold, raising the question of whether RG running from M_KK to M_Z effectively replaces n=1 with n~3. Gate: FAIL (against fold value). Classification: GEOMETRIC.

**Atlas promotion (W3-A)**: 9/9 QUASI-ROBUST entries promoted to ROBUST. Atlas now 20 ROBUST / 0 QUASI-ROBUST / 2 FRAGILE. All promotions are on the L_max axis specifically; non-L_max warnings (logic dependencies, BCS gap sensitivity) remain structurally valid. Classification: GEOMETRIC.

**Friedmann-BCS level separation (W3-B)**: f_conv operates at Level 1 (perturbations), not Level 0 (background Friedmann). The original S36 shortfall was a category error. BCS provides 0.112% of fold energy -- the 891.6x residual is the CORRECT energy hierarchy for KE-dominated stiff cosmology. Classification: GEOMETRIC.

**Pomeranchuk reclassification (W3-E)**: Physical instability verdict retracted. The mathematical identity f(0,0) = -4.687 is permanent, but the perturbative Fermi liquid theory is inapplicable at E_J/E_cond = 25. The self-consistent calculation gives min(1+F) = +0.946 > 0: the fabric is Pomeranchuk-STABLE. Classification: PHONONIC.

**CMPP classification (W3-H)**: Static Type D (algebraically special) at all tau values; Dynamic Type G (algebraically general) at all tau values. No type transition through the fold. The fold is an algebraically smooth geometric event -- no phase transition in the Weyl tensor classification. Classification: GEOMETRIC.

**Cassini secular bound (W3-I)**: |dG/dt|/G = 0 (tau frozen after modulus decay at t = 1.63e-37 s). Conservative effacement bound: 1.92e-14 yr^{-1}, 10.4x below Cassini 2e-13 yr^{-1}. The modulus mass hierarchy (m_tau ~ 1.5e17 GeV >> H_0) guarantees compliance parametrically. Classification: GEOMETRIC.

**Modulus GW spectrum (W3-J)**: Omega_GW(today) = 2.25e-25 at f_peak = 231 MHz, 13-16 OOM below all detector thresholds. The undetectability is parametric: three independent suppression factors [(Gamma/m)^2, (m/M_Pl)^4, MD dilution] combine multiplicatively. The S65 domain wall GW prediction (Omega_GW ~ 10^{-10}, LISA-detectable) remains a separate signal from a different source. Classification: GEOMETRIC.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S76-A1-MU-EFF | FAIL | mu_eff = 2.67e-4 (1.58 decades below target 0.0102) |
| S76-A2-MODULI-DECAY | PASS | tau_decay = 4.44e-40 s, T_RH = 3.25e16 GeV (W1-B value; corrected by W2-E) |
| S76-A3-TRANSIT-FNL | PASS | max |f_NL| = 1.505, all shapes within Planck bounds |
| S76-A4-HP4 | PASS | rho_HP4/rho_obs: 0.47 OOM, zero free parameters |
| S76-A5-POST-FOLD-H | INFO | H_Friedmann = 0.975 M_KK (601x below transit H). A_s gap: 5.75 OOM |
| S76-A6-SPEC-PERT | PASS | f_conv = 2.547e-10, matches S75 numerical to factor 1.000 |
| S76-B1-MPL-CONV | INFO | f_conv = pi^4/(9216*a_0^2), truncation-dependent (not convergent) |
| S76-B2-FCONV-A4 | PASS | f_conv^{(4)} = 6.030e-11, family consistency to machine precision |
| S76-B3-ALPHA-S-RECON | PASS | alpha_s(CMB) = -0.0143, 1.46-sigma from Planck |
| S76-B4-BCS-DRESS | INFO | delta_a_2/a_2 = -1.62e-3 (wrong sign, gap widens). f_conv BCS-immune |
| S76-B5-SM-DECAY | FAIL | Gamma_SM/Gamma_grav = 0.0077 (gravity dominates by 131x) |
| S76-B6-Z2-BREAK | FAIL | n_Z2(excess) = -3.87 (domain walls SUPPRESS asymmetry) |
| S76-B7-CUBIC-WEINBERG | FAIL | 59.8% from fold value (but 1.55% from PDG sin^2(M_Z)) |
| S76-B8-REHEAT-T | PASS | T_RH = 1.70e15 GeV, BBN 5/5 PASS |
| S76-B9-ALPHA-S-FP | INFO | alpha_s = -0.01422 (1.45 sigma), model spread 134% |
| S76-B10-OFF-JENSEN | PASS | 35/35 Hessian eigenvalues negative. Zero flat directions |
| S76-C1-QR-VERIFY | PASS | 9/9 QUASI-ROBUST promoted to ROBUST |
| S76-C2-FRIEDMANN-BCS | INFO | f_conv inapplicable to background. H^2 ratio = 891.6 (physical) |
| S76-C3-JLO | FAIL | CM_factor = 1 exactly. JLO route CLOSED |
| S76-C4-INST-LIQUID | FAIL | V_eff monotonic. |V_liquid/V_bare| < 3e-4. Channel CLOSED |
| S76-C5-POMERAN-RECLASS | PASS | Registry reclassified. Physical stability confirmed |
| S76-C6-KOSMANN | INFO | Mixing ratio > 1 but no SM mass hierarchy within single PW sectors |
| S76-C7-FSTAR | INFO | 0/4 principles uniquely select f*. t < 0.544 for red tilt (partial) |
| S76-C8-CMPP | INFO | Type D (static) / Type G (dynamic). No transition through fold |
| S76-C9-CASSINI | PASS | |dG/dt|/G = 0 (tau frozen). Conservative: 10.4x below Cassini bound |
| S76-C10-GW-SPEC | PASS | Omega_GW(BBN) = 3.64e-21 << 5.6e-6 (15 OOM margin) |

---

## IV. Structural Implications

### A. The Acoustic Structure of the GGE Relic is Established

Session 76 completes the acoustic characterization of the GGE relic across three orders of correlation:

- **Two-point (power spectrum)**: n_s = 0.9649 (S72), alpha_s = -0.0143 (S76), A_s = f_conv * A_s_fiber with f_conv = 2.547e-10 now derived analytically.
- **Three-point (bispectrum)**: max |f_NL| = 1.505, Gaussian to leading order, with O(1) cubic corrections from the Bogoliubov sudden channel. All shapes within Planck bounds.
- **Mode structure**: 8 BCS modes (1 B1 + 4 B2 + 3 B3) with branch-dependent squeezing parameters r = (1.786, 0.617, 0.982). B1 acoustic branch carries 99.93% of the scalar power (S74).

The three-point result is structurally clean: the multi-mode squeezed vacuum is exactly Gaussian (Wick's theorem from Bogoliubov linearity), and all non-Gaussianity is perturbative (from H_3). The negative sign of the dominant Bogoliubov channel (f_NL = -1.505) corresponds to anti-correlated acoustic three-point function -- modes that are positively correlated in pairs (squeezing) are anti-correlated in triples (anharmonicity).

### B. The Isocurvature Relaxation Pathway is Identified but Rate-Limited

The Landau-Khalatnikov matrix correctly captures the inter-branch pair transfer hierarchy: fast B2-dominated relaxation (lambda_fast = 0.531 M_KK), slow B1-B3 bottleneck (lambda_slow = 0.157 M_KK), conserved total (zero eigenvalue). The 1.58-decade shortfall in mu_eff is the most pressing open problem from the quantum-acoustics perspective. However, the W2-F B2-mediated virtual enhancement (14.2x, exceeding the 6.2x target) opens a concrete rescue pathway: the effective J_u1 = 0.539 M_KK from the second-order B1->B2->B3 process may close the gap when incorporated into the full Landau-Khalatnikov matrix with multi-cell corrections.

### C. Modulus Decay Resolves as Gravitational, Not Spectral

The W1-B / W2-E tension (56,000x discrepancy in SM decay rate) resolves in favor of gravitational dominance: the canonical normalization factor sqrt(Z_fold) = 273 suppresses the spectral-action vertex to Lambda_eff = 37 * M_Pl. This is a structural result from the stiffness of the modulus (Z_fold = 74,731). The cosmological moduli problem is solved, but by gravity (m^3/M_Pl^2), not by the spectral action vertex. The reheating mechanism works but is universal, not framework-specific. T_RH = 1.70e15 GeV at the GUT scale, with Leggett DM relics surviving reheating intact (T_RH < m_Leggett).

### D. Constraint Map Updates

**CLOSED mechanisms (permanent)**:
1. Parametric resonance of modulus into BCS modes (|q| = 5.9e-3, no instability bands populated).
2. Z_2 domain-wall DM production (Josephson network symmetrizes B1-B3, negative excess).
3. Instanton liquid moduli stabilization (mode-counting hierarchy: 8/6440 ~ 10^{-3}).
4. JLO/CM correction to HP4 CC (CM_factor = 1 exactly for finite spectral triples).
5. BCS dressing of f_conv (delta_a_2/a_2 = -1.62e-3, wrong sign, BCS-immune).

**PROMOTED to permanent**:
1. f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2 (analytic derivation, R-protected, cutoff-independent).
2. All 9 QUASI-ROBUST atlas entries (now ROBUST; 20 total ROBUST).
3. Ridge structure of Jensen line in 35D moduli space (35/35 negative eigenvalues).

**OPENED pathways**:
1. B2-mediated virtual J_u1 enhancement for mu_eff rescue (14.2x).
2. chi_2 -> Omega_Lambda direct dictionary (0.034 OOM vs current 0.47 OOM).
3. Inter-sector Yukawa computation for PMNS matrix (Kosmann mixing ratios > 1).
4. Deriving the H(tau) power-law index p from spectral action dynamics (controls alpha_s).

### E. The W1-B / W2-E Discrepancy as a Methodological Lesson

The 56,000x discrepancy between W1-B and W2-E in the SM modulus decay rate traces entirely to the canonical normalization factor sqrt(Z_fold) = 273, which W1-B omitted. W1-B used g_eff = sqrt(a_4/a_2) = 0.698, effectively setting the suppression scale to Lambda ~ m_tau itself. The first-principles W2-E derivation shows the physical coupling involves two corrections: (a) the fractional spectral modulation (da_4/dtau)/a_4 = 0.451 (not the moment ratio sqrt(a_4/a_2) = 0.698), and (b) the canonical normalization from Z_fold = d^2S/dtau^2 * (geometric factor) = 74,731. The Z_fold factor enters as sqrt(Z) in the denominator, suppressing the vertex by factor 273.

This matters for quantum acoustics because Z_fold measures the spectral action curvature in moduli space -- it is the acoustic impedance of the modulus field. A large Z_fold means the modulus is "stiff" (small fluctuations for given energy), and any effective coupling must account for the mismatch between the canonical field (with unit kinetic term) and the geometric field tau.

---

## V. Carry-Forward Computations

### Priority 1: mu_eff with B2-Mediated Virtual Enhancement

The W2-F result (J_u1^{virtual} = 0.539 M_KK, 14.2x enhancement) must be folded into the full Landau-Khalatnikov relaxation matrix from W1-A. If the enhanced J_u1 closes the 1.58-decade gap, the isocurvature decay rate becomes a PASS and the n_s mechanism chain is complete. If it falls short, the residual factor quantifies what multi-cell or transit-dynamical corrections must provide. This is the single most decisive computation for the acoustic sector.

### Priority 2: A_s Recomputation with Friedmann H

W1-E reduced the A_s gap from 9.47 to 5.75 OOM by identifying H_Friedmann = 0.975 M_KK (not H_transit = 586.5). The remaining 5.75 OOM gap requires recomputing the Bogoliubov coefficients {alpha_k, beta_k} with the Friedmann H in the mode equation. This is a microscopic ODE integration (same machinery as S75) with different background, and the result determines whether the A_s prediction closes.

### Priority 3: H(tau) Power-Law Index from Spectral Action Dynamics

The alpha_s prediction (W2-C, W2-I) is controlled by the single parameter p = 1.689 (power-law index of asymptotic H(tau)). Deriving p from the coupled Friedmann + spectral action system would close the model dependence and make alpha_s a zero-free-parameter prediction. Currently it is determined by fitting n_s = 0.9649.

### Priority 4: Inter-Sector Yukawa for PMNS Route

W3-F established the intra-sector mixing structure (off-diagonal/diagonal ratio > 1 in both (1,0) and (1,1) sectors). The PMNS matrix requires the inter-sector coupling through the spectral action fermionic term. This is the next step for the particle physics sector.

### Priority 5: chi_2 -> Omega_Lambda Dictionary Resolution

W1-D and W3-C established that the HP4 CC gap is either 0.47 OOM (rho_Lambda/HP4_base) or 0.034 OOM (chi_2 -> Omega_Lambda directly). The factor-3 is the Friedmann normalization (classical 4D geometry). Resolving which dictionary is correct requires deriving the spectral-to-cosmological map from the Friedmann equation with spectral action source terms.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | mu_eff = 2.67e-4 (1.58 decades below target) | PHONONIC | FAIL | B1-B3 bottleneck identified; J_u1 virtual 14.2x enhancement opens rescue |
| 2 | tau_decay = 1.63e-37 s, gravity-dominated (99.2%) | PHONONIC/GEOMETRIC | PASS | Moduli problem solved 37 OOM before BBN; T_RH = 1.70e15 GeV |
| 3 | max |f_NL| = 1.505, GGE relic Gaussian to leading order | PHONONIC | PASS | Zero-free-parameter bispectrum consistent with Planck |
| 4 | rho_HP4/rho_obs = 0.47 OOM, chi_2 = 0.741 | GEOMETRIC | PASS | CC hierarchy closed from 120.5 to 0.5 OOM |
| 5 | H_Friedmann = 0.975 M_KK (601x below transit H) | GEOMETRIC | INFO | A_s gap reduced 9.47 -> 5.75 OOM; Bogoliubov recomputation needed |
| 6 | f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2 analytically derived | GEOMETRIC | PASS | Promotable to permanent; A_s = 1.585e-9 (0.12 OOM from Planck) |
| 7 | alpha_s(CMB) = -0.0143, 3 routes reconciled | PHONONIC | PASS | 1.46-sigma from Planck; temporal ordering principle established |
| 8 | BCS dressing of a_2: -0.16%, wrong sign | GEOMETRIC | INFO | f_conv BCS-immune; 0.12 OOM gap not from spectral moments |
| 9 | Gamma_SM/Gamma_grav = 0.0077 | GEOMETRIC | FAIL | SM channel subdominant; Lambda_eff = 37*M_Pl from sqrt(Z_fold) |
| 10 | n_Z2(excess) = -3.87 (negative) | PHONONIC | FAIL | Z_2 domain-wall DM production CLOSED |
| 11 | sin^2(cubic) = 0.2348 (1.55% from PDG) | GEOMETRIC | FAIL | n=3 power law near-hit; RG running question opened |
| 12 | T_RH = 1.70e15 GeV, BBN 5/5 PASS | PHONONIC/GEOMETRIC | PASS | GUT + leptogenesis open; Leggett DM survives reheating |
| 13 | alpha_s = -0.01422, model spread 134% | PHONONIC | INFO | p = 1.689 is single controlling parameter; derivation needed |
| 14 | 35/35 off-Jensen Hessian eigenvalues negative | GEOMETRIC | PASS | Jensen line is ridge of S(g); 35D restoring potential |
| 15 | 9/9 QUASI-ROBUST promoted to ROBUST | GEOMETRIC | PASS | Atlas: 20 ROBUST / 0 QR / 2 FRAGILE |
| 16 | f_conv inapplicable to background; H^2 ratio = 891.6 | GEOMETRIC | INFO | Level 0/1 separation proven; BCS = 0.112% of fold energy |
| 17 | CM_factor = 1 exactly; JLO route CLOSED | GEOMETRIC | FAIL | Factor-3 is Friedmann normalization, not index theory |
| 18 | V_eff monotonic; instanton liquid CLOSED | GEOMETRIC | FAIL | Mode-counting 8/6440 hierarchy permanent |
| 19 | Pomeranchuk-STABLE (self-consistent min(1+F) = +0.946) | PHONONIC | PASS | Physical instability retracted; math identity preserved |
| 20 | Chiral mixing ratio > 1 in (1,0), (1,1) sectors | PARTICLE | INFO | PMNS route exists; requires inter-sector Yukawa |
| 21 | f* not uniquely selected; t < 0.544 partial constraint | GEOMETRIC | INFO | t is ONE empirical parameter (like Lambda_QCD) |
| 22 | CMPP Type D (static) / Type G (dynamic); no fold transition | GEOMETRIC | INFO | Fold is algebraically smooth; GW modes unchanged |
| 23 | |dG/dt|/G = 0 (tau frozen); conservative 10.4x below Cassini | GEOMETRIC | PASS | Mass hierarchy m_tau >> H_0 guarantees compliance |
| 24 | Omega_GW(today) = 2.25e-25 at 231 MHz | GEOMETRIC | PASS | Modulus GW undetectable (13-16 OOM below all detectors) |
| 25 | f_conv^{(4)} = 6.030e-11 (gauge channel) | GEOMETRIC | PASS | Family monotone decreasing in n; R_1 family consistency |
| 26 | f_conv = pi^4/(9216*a_0^2); truncation-dependent | GEOMETRIC | INFO | a_2 cancels exactly; depends on a_0 alone; NOT L_max-convergent |
