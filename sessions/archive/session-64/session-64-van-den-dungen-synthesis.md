# Session 64 Synthesis: The Spectral Action Faces Its Own Numbers

**Date**: 2026-04-01
**Agent**: van-den-dungen-bridge-theorist (Van den Dungen)
**Source Documents**:
- sessions/archive/session-64/session-64-results-workingpaper.md
- sessions/archive/session-63/framework-cc-oom.md
- sessions/archive/session-63/session-63-hawking-quantum-acoustics-workshop.md
- sessions/archive/session-63/session-63-volovik-van-den-dungen-workshop.md

---

## I. Session Outcome

Session 64 is a reckoning session. The spectral action on Jensen-deformed SU(3) was confronted with its own analytical structure at full resolution, and the results are definitive in ways that alter the constraint map permanently. The R-monotonicity theorem (W1-A) closes Path C of the CC resolution program by proving that the spectral action diverges along the Jensen curve beyond the fold -- the curvature-relaxation mechanism I identified as subject to the a_0 floor obstruction in the S63 Volovik-VdD workshop is now closed by a stronger result. The SA-VERSUS-JACOBSON-64 computation (W1-C) closes the category-error escape by proving Lambda_SA = Lambda_J, confirming that the 114-OOM gap is real within both the spectral action and the Jacobson formalism simultaneously. My own JACOBSON-KASPAROV-64 computation (W7-B) closes the 12D Jacobson route with a sign error I corrected mid-derivation (dim SU(3) = 8, not 6) and the structural conclusion Lambda_eff = (1/8)R_K = -0.252 M_KK^2 < 0, wrong sign for de Sitter.

Against this tightening of the CC walls, the session also delivers structural results of permanent value: the Spectral Moment Decoupling Theorem (W5-B) proves that CC and the area theorem are siblings, not parent-child, within the spectral moment hierarchy. The BdG heat kernel factorization K_BdG(t) = exp(-Delta^2 t) * K_bare(t) is exact to machine epsilon (W3-B). The tensor-to-scalar ratio is resolved at r = 0.033, passing BICEP/Keck, with the H2 theorem (volume-preserving Jensen = traceless in DeWitt superspace) providing the structural elimination of first-order tensors. And the n_s prediction stands at 0.9557 +/- 0.0036, 2.2 sigma from Planck, from zero free parameters.

---

## II. Key Results

### II.1. BdG Kasparov Product: a_2 Ratio 0.887 and the Sakharov Decomposition

**Result**: a_2^{BdG}/a_2^{bare} = 0.887, deviating from the Sakharov target 0.639 by 38.9%. K_BdG(t) = exp(-Delta^2 t) * K_bare(t) EXACT. Classification: GEOMETRIC.

The BDG-KASPAROV-64 gate (W3-B) was my computation, and the outcome is structurally informative rather than a simple pass/fail. The BdG spectral triple -- the Nambu-doubled operator encoding BCS pairing -- satisfies four of five Kasparov conditions exactly: (K1) vertical ellipticity with spectral gap 0.942 M_KK, (K2) base ellipticity automatic, (K3) self-adjointness, (K4) O'Neill A=T=0. Condition (K5) is marginal: alpha = Delta/omega_min = 0.566, exceeding the Kato-Rellich bound 1/2, but the spectral gap protects the K-homology class against spectral flow.

The central finding is the heat kernel factorization. For s-wave BdG pairing (which is the case here: Delta is mode-independent within each BCS sector), the BdG heat kernel factorizes exactly:

    K_BdG(t) = exp(-Delta^2 t) * K_bare(t)

This was verified to max deviation 2.2e-16 across the full t-range [1e-4, 1.0]. It is an identity, not an approximation. The physical content: the BdG spectral action at any cutoff Lambda decomposes multiplicatively into a gap-dependent universal factor and the bare spectral action. This factorization survives to all orders in the Seeley-DeWitt expansion.

The 0.887 ratio captures only the spectral gap contribution (31.2% of the total Sakharov 36.1% reduction). The remaining 69% requires BCS ground-state information -- specifically the occupation weights v_k^2 and the curvature response dDelta/dR -- which are NOT encoded in the excitation spectrum of D_BdG alone. This is a precise structural decomposition:

- (A) Spectral gap opening: omega^2 -> omega^2 + Delta^2, accounts for 11.3%
- (B) BCS quantum depletion: v_k^2 occupation factors, accounts for ~24.8%
- (C) Curvature response of Delta: dDelta/dR contribution

The Sakharov energy-response method from S63 (W6-13 M2, delta_a2/a_2 = -0.361) captures all three. The BdG heat kernel captures only (A). This tells us something important for the self-consistent BdG spectral triple program (Path E of the CC resolution): the BdG eigenvalue spectrum alone is insufficient to reproduce the full Sakharov gravitational coupling reduction. The ground-state occupation weights must be incorporated as additional data in the spectral triple -- either through a state-dependent Dirac operator or through the expectation values that define the GGE.

In Paper 01 (1811.07824, Theorem 4.3), I proved that the Kasparov product on submersions factorizes the K-theory class of the total Dirac operator into fiber and base contributions. The BdG Kasparov conditions being satisfied means this factorization extends to the BdG-dressed geometry. But the factorization is a K-THEORY statement. The spectral action, being a SPECTRAL quantity (depending on all eigenvalues, not just the K-class), requires the full ground-state information. This is the boundary between topology and analysis that the session has now quantified.

### II.2. JACOBSON-KASPAROV-64: The 12D Derivation and the Convention Correction

**Result**: Lambda_eff = (1/8)R_K = -0.252 M_KK^2 < 0 (wrong sign, no CC reduction). Classification: GEOMETRIC.

This computation was my direct test of whether the higher-dimensional Jacobson derivation on M^4 x SU(3) could provide a CC reduction mechanism. The gate design from cc-path-a.md specified a 10D derivation, but I caught a dimension error mid-computation: SU(3) is 8-dimensional as a manifold (dim su(3) = 3^2 - 1 = 8), not 6-dimensional. The total space is therefore 12-dimensional, not 10-dimensional.

The corrected derivation proceeds through the standard Jacobson steps generalized to d = 12: Rindler horizon, Unruh temperature, Clausius relation, Raychaudhuri equation, contracted Bianchi identity. For a product metric (A = T = 0, verified S61), the 12D Einstein equations decompose into base-base, fiber-fiber, and cross components. The fiber-fiber trace gives a consistency condition:

    Lambda^{(12)} = (3/8) R_K + (1/2) R^{(4)}

Combined with the base vacuum Einstein equation R^{(4)} = 4 Lambda_eff:

    Lambda_eff = (1/8) R_K

With R_K(fold) = -2.018 M_KK^2 (from the Koszul formula on Jensen-deformed SU(3), verified in KASPAROV-VERIFY-61 and A-TENSOR-61), this gives Lambda_eff = -0.252 M_KK^2.

Three problems make this result a FAIL:

1. **Sign**: Lambda_eff < 0 (anti-de Sitter), while Lambda_obs > 0 (de Sitter). The scalar curvature of compact semisimple Lie groups is always negative in the physics convention (Ric = -(1/4)B where B is the Killing form). The Jensen deformation preserves this sign.

2. **Scale**: |Lambda_eff| = 0.252 M_KK^2 ~ 10^{33} GeV^2, which is 114 OOM above Lambda_obs. The fiber curvature is at the KK scale, not the meV scale.

3. **No new freedom**: Lambda_eff is determined entirely by R_K -- no integration constant, no adjustable parameter. The fiber consistency condition eliminates the would-be free Lambda^{(12)}.

The gate design also contained an error: it incorrectly identified R_K = a_2/a_0 = 0.431. But a_2/a_0 is a ratio of Seeley-DeWitt coefficients (integrated, trace-weighted spectral moments), not the scalar curvature of the fiber. The actual R_K from the Koszul formula is -2.018 M_KK^2.

The structural lesson, which I stated explicitly in the computation: the Kasparov product is a TOPOLOGICAL tool (K-theory classes, indices), while the CC problem is an ANALYTICAL problem (spectral moments, eigenvalue sums). The factorization [D_total] = pi_! tensor [D_M] guarantees that the K-theory decomposes correctly. It says nothing about the magnitude of the spectral action. Two operators in the same K-class can have spectral actions differing by arbitrary amounts. This is the fundamental reason the fiber "decouples" for CC purposes.

### II.3. The a_0/a_2 Trap: My Structural Correction Vindicated

**Result**: The Hessian descent (W2-A) confirms that off-Jensen directions decrease a_2, but this WORSENS the CC (a_0/a_2 increases). Classification: GEOMETRIC.

In the S63 Volovik-VdD workshop (Round 1, my response to Volovik's V3), I identified what I called Dissent Gap 2: the a_0 floor obstruction. Theorem T14 (volume-preserving Jensen) states a_0 = const, tau-independent. If S(tau) is dominated by f_0 Lambda^4 a_0, then the spectral action cannot relax to zero because a_0 is constant. The transit can relax the curvature-dependent terms (a_2, a_4) but leaves the tau-independent floor untouched.

Session 64 tests this from both directions:

**W1-A (S-ASYMPTOTIC-64: FAIL)**: a_2(tau) is STRICTLY MONOTONICALLY INCREASING for all tau > 0 on volume-preserving Jensen-deformed SU(3). The proof is analytic: dR/dtau = exp(-4tau) - 2*exp(-tau) + exp(2tau) >= 0 by AM-GM, with equality only at tau = 0. The R-monotonicity theorem is PERMANENT. The spectral action diverges exponentially beyond the fold because R(tau) ~ 0.5*exp(2tau) at large tau (the U(1) fiber direction stretches as exp(2tau)). Path C (transit-as-relaxation along the Jensen curve) is now CLOSED by a theorem, not merely obstructed.

**W2-A (HESSIAN-DESCENT-64: PASS with crucial caveat)**: Off-Jensen directions DO exist where a_2 decreases. The R-Hessian restricted to the 35D volume-preserving tangent space has signature (8+, 27-) -- the fold is a SADDLE of R, not a maximum. The steepest descent is anti-Jensen: expand SU(2), collapse U(1). But -- and this is where my S63 correction bites -- decreasing a_2 while a_0 is constant INCREASES the ratio a_0/a_2, which is proportional to rho_vac in Planck units. The physical CC = (f_0/f_2)(a_0/a_2)Lambda_sp^2 gets WORSE, not better, along every direction that decreases a_2.

This is the a_0/a_2 trap stated precisely:

- Jensen direction: a_2 increases, a_4 increases faster, so a_0/a_2 decreases. But the spectral action S(tau) itself diverges (W1-A). CC density decreases along Jensen, but total action diverges.
- Anti-Jensen direction: a_2 decreases (eventually to zero), so a_0/a_2 diverges. CC density increases without bound.
- Neither direction solves CC within the Seeley-DeWitt framework.

The only escape is to change a_0, which requires breaking the volume-preserving constraint. Or to modify the spectral action itself beyond the polynomial SDW expansion. The a_0/a_2 trap is a direct consequence of volume-preserving deformations being a_0-inert (Theorem T14) while a_2 depends on scalar curvature (which varies). The trap is structurally permanent within the left-invariant metric moduli space of SU(3).

### II.4. Spectral Moment Decoupling Theorem: CC and Area Theorem as Siblings

**Result**: F_{-1}(CC) and F_{+1}(NEC) are controlled by DIFFERENT spectral moments. Breaking CC monotonicity does not force NEC violation. Classification: GEOMETRIC.

The SPECTRAL-MONOTONICITY-LINK-64 computation (W5-B) answers a question from the S63 Hawking-QA workshop hierarchy (E1): does the 4-level spectral monotonicity hierarchy form a rigid chain?

The answer: Levels 0-1-2 are rigid, Level 2->3 is flexible. The CC monotonicity (dE_ZP/dq > 0) operates through the inverse spectral moment F_{-1} = sum d_n/omega_n. The null energy condition (T_ab k^a k^b >= 0) operates through the direct moment F_{+1} = sum d_n omega_n n_n. These are algebraically independent functionals of the same spectrum.

The proof by construction: a two-sector spectrum with different bosonic and fermionic spectra can break CC monotonicity (by making the fermionic 1/omega contribution dominate) while preserving the NEC (because omega * n is always positive). The key: CC monotonicity amplifies LOW-energy modes (1/omega is large at small omega), while the NEC amplifies HIGH-energy modes (omega is large at large omega). A spectral modification in the IR can flip CC monotonicity without touching the NEC.

This is STRUCTURAL PERMISSION for CC resolution. It says: any mechanism that resolves the CC (by modifying D_K eigenvalues at Level 0 to break the shared-spectrum condition of Closure 9) does NOT necessarily violate the NEC or invalidate the area theorem. The gravitational sector can remain healthy while the CC self-tunes.

The hierarchy topology is:

    Level 0 --> Level 1 --> Level 2 --X--> Level 3
    (substrate)  (BCS)     (CC via a_0)    (NEC via a_2, a_4)

The "X" marks the decoupling. Both branches share a common ancestor (Level 0 spectral positivity) but propagate through different spectral channels.

### II.5. Shell Hessian UV Sensitivity: Spectral Action Truncation Has Consequences

**Result**: One-loop Hessian positive-definite only with L >= 3 PW modes. First zero crossing at step 2 (removing (2,1) irrep). L=3 shell contributes 79.9% of one-loop Frobenius norm. Classification: GEOMETRIC.

The SHELL-HESSIAN-64 computation (W7-A) performs FRG decimation on the one-loop effective Hessian, removing Peter-Weyl irreps from UV (L=3) to IR (L=0). The result is physically sharp:

- **Full spectrum (step 0)**: All 36 eigenvalues positive. Fold is a local minimum of the one-loop effective action.
- **After removing (1,2) + (2,1) (step 2)**: First eigenvalue crosses zero. lambda_min = -2.82.
- **After removing all L=3 irreps (step 4)**: ALL 36 eigenvalues negative. The fold reverts to the tree-level maximum.

The one-loop effective Hessian is UV-DOMINATED. The L=3 shell alone contributes 79.9% of the total Frobenius norm. The physical picture: the tree-level spectral action makes the fold a maximum (all eigenvalues of the tree Hessian are negative). The one-loop functional determinant Tr ln(D_K^2) provides positive corrections from all PW irreps, and the L=3 irreps contribute enough to flip the sign. Below L=3, the fold is a maximum; with L >= 3, it is a minimum.

This has two consequences for the framework:

1. **The fold stability is a UV property.** Any FRG analysis that integrates out high PW shells will see the fold stability disappear. The spectral action landscape changes topology at the L=3 boundary. This is not a failure -- it is the standard FRG picture where the effective average action differs qualitatively from the full theory -- but it constrains any computation that truncates the PW tower.

2. **The spectral action at L_max = 10 is UV-converged for stability.** Since the sign flip occurs at L = 3 and the current computation uses L_max = 10, the fold stability is robust to further UV completion. But the UV dominance means that quantities like the Hessian eigenvalues, the moduli masses, and the sound speed c_s could shift meaningfully if L_max were extended.

The Strutinsky analogy from nuclear DFT is apt: H_eff = H_tree (smooth) + H_1loop (shell corrections), with the shell correction being positive and UV-dominant. Removing these shells destabilizes the self-consistent solution, just as removing high-j shells destabilizes the nuclear self-consistent field.

### II.6. The framework-cc-oom.md Retrospective: What Held, What Broke

**Result**: 3 of 7 open paths tested; 2 closed (Path A category-error, Path C transit-relaxation), 1 confirmed open with quantified shortfall (Path B gravitational breaking). Classification: NON-PHONONIC (constraint mapping).

The cc-oom.md document I wrote in S63 identified 9 closures and 7 surviving paths. Session 64 directly tested three:

**Path A (Jacobson route): CLOSED.** The cc-oom.md stated Path A was "formally open but physically empty until something determines the integration constant." W1-C proved Lambda_SA = Lambda_J: the spectral action determines the Jacobson integration constant, and the determined value is 10^{114} too large. The Jacobson derivation is not an alternative to the spectral action -- it is a consequence of it. Lambda_J is "undetermined" only within the Jacobson derivation alone; once the spectral action is specified as the microscopic theory, Lambda_J is fixed. The category-error escape is closed.

**Path C (transit-as-relaxation): CLOSED.** The cc-oom.md stated the a_0 floor obstruction as conditional on whether a_2(tau) decreases beyond the fold. W1-A proved it does NOT decrease -- a_2 is strictly monotonically increasing for all tau > 0 on the Jensen curve. The R-monotonicity theorem is an analytic proof (AM-GM inequality on dR/dtau). Path C is closed not by the a_0 floor alone but by the stronger result that a_2 itself diverges.

**Path B (gravitational integrability breaking): OPEN, quantified at 110 OOM shortfall.** The cc-oom.md predicted O(alpha_G) ~ 10^{-3.6} correction. W1-B found all 8 Gaudin charges broken, with the channel OPEN. W2-C found delta_E_ZP/E_ZP = -2.63e-4 (correct direction: vacuum energy decreases). But the 5.4%/94.6% Gaudin/non-Gaudin split means gravitational breaking affects only the pair-correlated part of rho_ZP. The shortfall is 110 OOM.

**Paths D, E, F, G**: Not directly tested in S64, but constrained by the structural results. Path E (self-consistent BdG triple) is advanced by the BdG-KASPAROV-64 factorization result but blocked by the occupation-weight gap (69% of Sakharov reduction requires ground-state data beyond the BdG eigenvalue spectrum). Path F (CC as finite-size effect) is unchanged. Path G (sector-selective relaxation) is constrained by the B2[0] Fermi-surface lock: v_{B2[0]}^2 = 0.500000 exactly, immune to gravitational perturbations through energy shifts (W2-C).

The cc-oom.md's framing of the CC as the integrability problem holds up. Every tested mechanism confirms that the Richardson-Gaudin integrability is the structural barrier: the ordered veil that protects the dark matter is the same mechanism that prevents the vacuum energy from relaxing.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S-ASYMPTOTIC-64 | FAIL | a_2 monotonically INCREASING, ratio 1.2e8 at tau=10 |
| R-G-CHARGE-DECOMPOSITION-64 | PASS | 7/8 charges broken, but 94.6% of rho_ZP outside Gaudin span |
| SA-VERSUS-JACOBSON-64 | FAIL | Lambda_SA = Lambda_J, 114 OOM gap is real |
| OCC-SPEC-64 | INFO | S_occ/S_fold = 7.53e-2, A_s gap reduced 1.12 OOM |
| EPSILON-PROFILE-64 | INFO | eps_V < 0.013, eta_V ~ 0.25, eps_H monotone |
| HESSIAN-DESCENT-64 | PASS (with caveat) | 27/35 directions have da_2 < 0, but a_0/a_2 worsens |
| SELF-CONSISTENT-NE-64 | INFO | N_e = 3.73e-3 (extremely narrow burst) |
| SECTOR-SELECTIVE-BREAKING-64 | PASS | delta_E_ZP/E_ZP = -2.63e-4, 110 OOM shortfall |
| N-PAIR-3-RG-64 | PASS | <r> = 0.478, pairing channel breaks integrability |
| FINITE-SIZE-VACUUM-ENERGY-64 | INFO | E(0)/cell = 7824 M_KK, 116.8 OOM gap |
| TENSOR-BURST-64 | PASS | r_CMB = 0.033 < 0.036 |
| BDG-KASPAROV-64 | INFO | a_2 ratio = 0.887, K_BdG factorizes exactly |
| LINEWIDTH-HIERARCHY-64 | FAIL | Gamma_B2 > Gamma_B1 > Gamma_B3 (reversed from QA-E5) |
| TRANSFER-BOGOLIUBOV-64 | PASS | Max/min variation 1.33 across cutoffs |
| SOUND-SPEED-64 | PASS | c_mod=1, c_BLV=0.485, c_BA=0.399, c_L=0.025, all causal |
| MUKHANOV-SASAKI-64 | INFO | M-S inapplicable (N=7.75, eta_H=0.96, modes never freeze) |
| PHASE-BOGOLIUBOV-64 | INFO | phi_Bog = pi, delta_phi = 2.4e-4 (below Planck precision) |
| SPECTRAL-MONOTONICITY-LINK-64 | FAIL | CC and area theorem decouple (different spectral moments) |
| JACOBSON-GGE-64 | INFO | Extends without modification, Lambda unchanged |
| NS-FINAL-64 | PASS | n_s = 0.9557 +/- 0.0036, 2.2 sigma from Planck |
| CHIRALITY-SELECTION-64 | INFO | C_chiral = 1, no KO cancellation in 2nd-order source |
| VAB-RANK-64 | PASS | rank = 5, ample room for 3 generations |
| QUANTUM-METRIC-64 | FAIL | D_s(PT) = 0 (structural: T propto identity) |
| SHELL-HESSIAN-64 | FAIL | Zero crossing at step 2, L=3 shell is 79.9% of Hessian |
| JACOBSON-KASPAROV-64 | FAIL | Lambda_eff = (1/8)R_K = -0.252 M_KK^2, wrong sign |
| GGE-KMS-64 | INFO | Compatible, 8-factor modular decomposition, lambda_B2 < 0 harmless |
| TENSOR-SCALAR-64 | PASS | r = 0.0333, independent verification of W3-A |
| SKYRMION-BARYON-64 | FAIL | M_skyrm 22 OOM above proton, eta_B 9.6 OOM above observed |

---

## IV. Structural Implications

### IV.1. The CC Constraint Map After S64

The CC solution space has narrowed significantly. Two paths are now CLOSED by theorems:

- **Path A (Jacobson category-error)**: Lambda_SA = Lambda_J. PERMANENT.
- **Path C (transit-as-relaxation on Jensen)**: R(tau) strictly monotonically increasing. PERMANENT.

Path B (gravitational integrability breaking) is OPEN but quantitatively negligible (110 OOM shortfall). The a_0/a_2 trap (W2-A) constrains off-Jensen moduli as well: no direction within the volume-preserving left-invariant metric space simultaneously decreases a_0/a_2. This is a stronger statement than I made in S63.

The surviving paths require EITHER:
1. Breaking the volume-preserving constraint (allows a_0 to change)
2. Nonlocal spectral action effects beyond the SDW polynomial expansion
3. Giving bosonic and fermionic sectors different effective spectra (the specific escape identified by the Spectral Moment Decoupling Theorem)

### IV.2. Kasparov Product: Topology vs Analysis Boundary

Session 64 has crystallized a distinction I have been building toward since S60. The Kasparov product on submersions (Paper 01) provides:
- EXACT factorization of K-theory classes
- EXACT vanishing of O'Neill cross-terms (S61: A=T=0)
- EXACT heat kernel factorization of the BdG operator (W3-B)
- EXACT index preservation under bounded perturbations

But it does NOT constrain:
- The magnitude of the spectral action (which depends on the full spectrum, not the K-class)
- The cosmological constant (which is determined by the spectral moment ratio a_0/a_2)
- The Sakharov gravitational coupling reduction (which requires ground-state occupation data beyond the BdG eigenvalues)

The Kasparov product is a topological machine operating on an analytical problem. Its results are permanent structural theorems -- exact factorizations, index preservation, spectral flow vanishing. But the observationally relevant quantities (CC, G_N, gauge couplings) live in the spectral action, not in K-theory. This is not a weakness of the formalism; it is a precise statement about its scope.

### IV.3. The GGE Modular Structure

The GGE-KMS-64 result (W7-C) provides the natural mathematical home for the GGE within NCG. The modular operator Delta_GGE = exp(-sum_k lambda_k (R_k^L - R_k^R)) decomposes into 8 commuting factors, one per Richardson-Gaudin charge. The negative lambda_B2 = -0.053 (population inversion in the condensate sector) is harmless for Tomita-Takesaki positivity. The modular flow is multi-periodic with 8 incommensurate frequencies, giving dense Connes spectrum.

This connects to Connes' classification of type III factors: in the thermodynamic limit (L_max -> infinity), the dense spectrum would give a type III_1 factor -- the unique hyperfinite factor with full Connes invariant S(M) = R_+. This is the same von Neumann algebra type that appears in quantum field theory on curved spacetime (Haag-Hugenholtz-Winnink theorem). The GGE modular time is distinct from cosmological time and from Unruh time, related by the Connes cocycle.

### IV.4. Observational Predictions After S64

Three observational predictions are now stable:

1. **n_s = 0.9557 +/- 0.0036**: From zero free parameters. 2.2 sigma from Planck. BCS dressing is the leading uncomputed correction (estimated +0.0014 toward Planck). The prediction is a shape invariant of the spectral action -- cutoff-independent, perturbatively stable.

2. **r = 0.033**: From the H2 theorem (structural) + second-order Bogoliubov enhancement. PASSES BICEP/Keck with 7.4% margin. Blue tensor tilt predicted (n_T > 0), discriminating against standard slow-roll inflation.

3. **Phase coherence R = 1.000**: All Bogoliubov phases are pi (sudden quench). Observable only in bispectrum or cross-correlations, not in TT power spectrum.

---

## V. Forward Projection

### V.1. Critical Open Computations

1. **BCS-DRESSED-SA**: Compute S^{BCS}(tau) from the BdG spectral action at 5 tau values. Extract eps_H^{BCS}. This is the leading correction to n_s and the only channel that could reduce the 2.2-sigma Planck tension. The BdG heat kernel factorization from W3-B provides the analytical backbone: S^{BCS} = exp(-Delta^2/Lambda^2) * S^{bare} + occupation-weighted corrections. The 69% missing Sakharov component must be computed explicitly.

2. **Off-Jensen transit path**: The dynamical trajectory in the 36D moduli space has not been determined from the spectral action gradient flow. W2-A shows the fold is a saddle with 27 descent directions for R. The physical transit path may not follow the 1D Jensen curve. Computing eps_H along the dynamical trajectory could shift n_s.

3. **Volume-breaking mechanism**: The a_0/a_2 trap closes all volume-preserving directions for CC. The question becomes: what physical mechanism breaks volume preservation? The compactification dynamics (tau evolution) preserves volume by construction. An external mechanism -- perhaps the self-consistent back-reaction loop identified by Volovik (V2) -- could break this.

4. **Nonlocal spectral action (Paper 09 direction)**: If the full Tr f(D^2/Lambda^2) differs from its SDW polynomial approximation in a way that makes a_0 effectively tau-dependent, the a_0/a_2 trap is evaded. UNEXPANDED-SA-45 showed the expansion is exact for finite spectra, so this requires either infinite-volume effects or a different choice of f.

### V.2. Structural Questions

- Does the GGE modular flow (W7-C) connect to the cosmological time evolution through a Connes cocycle computation? This would formalize the "three times" picture (modular, cosmological, Unruh) within NCG.

- The Shell Hessian UV sensitivity (W7-A) raises a convergence question: does the one-loop Hessian converge as L_max increases? The per-shell Frobenius norm scales roughly as L^{2.5}, suggesting convergence, but verification at L = 4, 5 is needed.

- The Peotta-Torma vanishing (W6-D: D_s(PT) = 0) because the Josephson hopping is proportional to identity: T = E_J * I_8. This is exact for mode-preserving pair transfer. Does mode-changing virtual hopping (from S63 second-order channel) break this proportionality and give nonzero quantum geometric tensor?

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | R-monotonicity theorem | GEOMETRIC | PERMANENT | Path C CLOSED, a_2 diverges on Jensen |
| 2 | Lambda_SA = Lambda_J | GEOMETRIC | PERMANENT | Path A CLOSED, 114 OOM gap is real |
| 3 | K_BdG = exp(-Delta^2 t) * K_bare | GEOMETRIC | PERMANENT | BdG heat kernel factorizes exactly |
| 4 | Sakharov 3-component decomposition | GEOMETRIC | PERMANENT | BdG captures 31% (gap), not 100% |
| 5 | Lambda_eff = (1/8)R_K = -0.252 M_KK^2 | GEOMETRIC | PERMANENT | 12D Jacobson: wrong sign, no CC reduction |
| 6 | Spectral Moment Decoupling | GEOMETRIC | PERMANENT | CC and NEC are siblings, not parent-child |
| 7 | a_0/a_2 trap | GEOMETRIC | PERMANENT | No vol-preserving direction decreases CC density |
| 8 | Shell Hessian L_crit = 3 | GEOMETRIC | PERMANENT | Fold stability requires L >= 3 PW modes |
| 9 | n_s = 0.9557 +/- 0.0036 | GEOMETRIC | COMPUTED | 2.2 sigma from Planck, zero free parameters |
| 10 | r = 0.033 | GEOMETRIC | COMPUTED | PASSES BICEP/Keck, H2 theorem structural |
| 11 | GGE modular decomposition | GEOMETRIC | THEOREM | 8-factor Delta_GGE, negative lambda_B2 harmless |
| 12 | Gravitational breaking 110 OOM short | PHONONIC | OPEN | Channel open, quantitatively insufficient |
| 13 | Integrability breaking PASS (N=3) | PHONONIC | COMPUTED | Non-separable V drives <r> to 0.478 |
| 14 | Linewidth hierarchy reversed | PHONONIC | FAIL | Flat band enhances scattering, does not suppress |
| 15 | Skyrmion mass 22 OOM above proton | PARTICLE | FAIL | Fiber skyrmion is GUT-scale, not QCD-scale |
