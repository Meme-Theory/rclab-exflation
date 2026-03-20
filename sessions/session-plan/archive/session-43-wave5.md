## III-e. Wave 5: Medium-Priority Computations (12 tasks, parallel)

### W5-1: Off-Jensen J-Symmetry Breaking

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Verify whether [J, D_K] = 0 persists for off-Jensen deformations in the g_73 direction (softest Hessian mode from HESS-40).

**Source**: S42 T2-1 (Dirac Comp 3). S42 Dirac collab Section 3, Computation 3.

**Context.** Theorem T1 ([J, D_K(tau)] = 0) is proven for the 1-parameter Jensen family. The off-Jensen space has not been checked. From S29, the true minimum is in the U(2)-invariant 3D subspace. If g_73 direction introduces [J, D_K] != 0, this provides: (a) CPT violation (testable against BASE 16 ppt, ALPHA 2 ppt), (b) CP violation for baryogenesis.

Kostelecky SME thresholds (Paper 18 in `researchers/Antimatter/`): electron |b_0^e| < 2e-25 GeV, quark |b^u| < 1e-21 GeV, gravitational < 1e-13. Neutral meson CPT (Paper 26): kaon delta_CPT^K < 1e-13, B_s < 1e-11. Any off-Jensen J-breaking at M_KK must produce SME coefficients below these after RGE running.

**Computation Steps**:

1. Load `tier1_dirac_spectrum.py`. Construct D_K at the fold for the Jensen metric AND for a metric deformed in the g_73 direction by epsilon = 0.001, 0.01, 0.05.

2. Compute [J, D_K(off-Jensen)] in the 16×16 representation at each epsilon.

3. Compute ||[J, D_K]|| / ||D_K||. If > 10^{-12}: conflicts with BASE. If exactly 0: J-symmetry more general than proven. If nonzero but < 10^{-12}: geometric epsilon_CP within CPT bounds.

4. If nonzero: compute the low-energy SME coefficients by RGE running from M_KK to the meson scale. Compare to Paper 18 thresholds.

**Pre-registered gate OFFJ-J-43**: PASS if nonzero AND < 10^{-12} (geometric epsilon_CP). FAIL if > 10^{-12} (conflicts BASE). INFO if exactly zero.

**Input**: `tier1_dirac_spectrum.py`, Papers 18, 26 in `researchers/Antimatter/`
**Output**: `tier0-computation/s43_offj_jsymm.{py,npz,png}`

---

### W5-2: Twisted Real Structure (Filaci-Landi)

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: HIGH (algebraic)

**Prompt**:

Determine whether a Filaci-Landi twisted real structure with sigma^2 = id resolves the Axiom 5 failure (order-one violation = 4.000, Session 31) while preserving CPT and BDI.

**Source**: S42 T2-2 (Dirac Comp 4). S42 Dirac collab Section 3, Computation 4.

**Context.** Venselaar-Sitarz (Paper 30 in `researchers/Antimatter/`) classify all real structures on almost-commutative spectral triples — 2-4 inequivalent J operators per geometry. Filaci-Landi (Paper 31 in `researchers/Antimatter/`) generalize to twisted real structures: J a J^{-1} = sigma(a) instead of [J, a] = 0. The modified first-order condition [[D, a], sigma(b)^dagger] = 0 can accommodate gauge structures the standard axioms reject.

Paper 24 (Chamseddine-Connes-vS): dropping the first-order condition entirely generates Pati-Salam. If twisted real structure provides CONTROLLED weakening rather than full removal, it could: (1) preserve CPT (Paper 31 proves this when sigma^2 = id), (2) introduce geometric epsilon_CP through sigma, (3) resolve Axiom 5, (4) connect to Boyle-Farnsworth (Paper 29) super-algebraic structure.

**Computation Steps**:

1. Read Papers 29-31 in `researchers/Antimatter/`.

2. Construct the framework's real structure J = gamma_1*gamma_3*gamma_5*gamma_7 in the 16×16 representation.

3. Search for involutive automorphisms sigma (sigma^2 = id) on the algebra A = C^inf(M) tensor A_F that satisfy: (a) sigma^2 = id, (b) BDI compatibility (T, C, S symmetries preserved), (c) ||sigma - id|| bounded by BASE/ALPHA CPT limits.

4. For each candidate sigma: check whether the twisted first-order condition [[D_K, a], sigma(b)^dagger] = 0 is satisfied (or closer to satisfied than the untwisted condition, which fails at 4.000).

5. If a valid sigma exists: compute the geometric epsilon_CP = ||sigma - id|| and assess its baryogenesis implications.

**Pre-registered gate TWIST-43**: PASS if sigma exists satisfying all 3 criteria. FAIL if no valid sigma. INFO if sigma exists but BDI compatibility undetermined.

**Input**: Papers 29-31 in `researchers/Antimatter/`, `s35_pfaffian_corrected_j.npz`
**Output**: `tier0-computation/s43_twisted_real.{py,npz,png}`

---

### W5-3: BCS Universality Class on SU(3)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: HIGH

**Prompt**:

Determine the universality class of the BCS phase transition on Jensen-deformed SU(3) and compute the critical exponents (nu, z) that determine n_s via the KZ mechanism.

**Source**: S42 T2-5 (Baptista Q4, QF 4C). S42 Baptista collab Q4: "standard 3D Ising gives n_s - 1 = -0.89 (too red). Mean-field gives -1.0. KZ route requires non-standard universality class."

**Context.** GL-CUBIC-36 established the BCS transition is second-order with Z_2 universality. Standard 3D Ising: nu = 0.6301, z = 2.02. But the BCS transition occurs on CURVED SU(3) — the positive curvature may modify critical exponents.

Paper 47 (`researchers/Baptista/47_2025_Hyperbolic_BCS_Curved_Space.md`) studies BCS on hyperbolic spaces where curvature corrections to critical phenomena are known. SU(3) has POSITIVE curvature (Ricci scalar R = 7.19 at fold), opposite sign from hyperbolic. But the methodology transfers: curvature enters the GL functional through gradient terms with curvature-dependent coefficients.

Uses W1-2 Lifshitz classification result for the Van Hove exponent and topological type.

**Computation Steps**:

1. Read Paper 47 in `researchers/Baptista/`.

2. Write the Ginzburg-Landau free energy for the B2 sector BCS order parameter on Jensen-deformed SU(3). The GL functional is:

   $$F[\Delta] = \int_{SU(3)} \sqrt{g} \left[ a|\Delta|^2 + \frac{b}{2}|\Delta|^4 + c|D_\mu\Delta|^2 + \text{curvature corrections} \right]$$

3. The curvature corrections enter through the Laplacian on SU(3): the covariant derivative D_mu includes the Christoffel connection of the Jensen metric. The R*|Delta|^2 term is the leading correction.

4. Compute the modified critical exponents from the curvature-corrected GL equation. In the epsilon-expansion: nu = 1/2 + (R/R_c) * delta_nu where R_c is a characteristic curvature scale. Determine delta_nu.

5. Compute z from the dynamic scaling near the BCS critical point. The BCS dynamics on a curved manifold: does the curved metric change the dynamical exponent?

6. Compute n_s from the KZ formula with the curvature-corrected exponents. Report whether n_s > 0.90 is achievable.

**Pre-registered gate BCS-CLASS-43**: INFO. Report (nu, z, n_s). PASS if n_s > 0.90.

**Input**: W1-2 results, Paper 47, `s36_mmax_authoritative.npz`, `s35_ed_corrected_dos.npz`
**Output**: `tier0-computation/s43_bcs_universality.{py,npz,png}`

---

### W5-4: Discrete+Continuum Fano at 4D Boundaries

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM-HIGH

**Prompt**:

Compute the transmission coefficient T(E) for a 4D particle incident on a tau-step boundary, looking for Fano zeros from discrete+continuum interference.

**Source**: S42 T2-10 (Naz Sugg 3). PI caveat on HF-BOUNDARY-42.

**Context.** HF-BOUNDARY-42 proved discrete+discrete coupling produces no Fano zeros (q = infinity, structural from anti-Hermitian Kosmann). But the PHYSICAL setup at a fabric boundary is discrete (internal-space compound nucleus) + continuum (4D spacetime dispersion E = sqrt(m^2 + p^2)). This IS textbook Fano: discrete state embedded between two asymmetric continua (different tau → different KK masses → different impedances).

Nuclear analog: neutron transmission through compound nucleus with closely-spaced resonances (Feshbach optical potential, Naz Paper 14 Section 3).

**Computation Steps**:

1. For each KK eigenvalue lambda_k(tau), construct 4D continuum band omega_k(p) = sqrt(lambda_k^2 + p^2).

2. The boundary coupling V_boundary(k, k') connects mode k on side 1 (tau_1) to mode k' on side 2 (tau_2 = tau_1 + delta_tau).

3. Construct the scattering matrix S(E) using Green's function methods: G(E) = (E - H_1 - H_2 - V_boundary)^{-1}.

4. Compute T(E) = |t(E)|^2 for a 4D particle with energy E incident on the tau-step boundary.

5. Look for Fano zeros: energies where destructive interference between direct transmission and boundary-mediated virtual excitation produces T → 0. Compute Fano parameter q(E) for each channel.

6. If Fano zeros found: compute the mass-dependent selectivity (dynamic range in sector branching). Does this produce > 3 decades of DR?

**Pre-registered gate FANO-CONT-43**: PASS if Fano zeros found with |q| < 1 for any channel. FAIL if q = infinity everywhere.

**Input**: `s42_coupled_doorway.npz`, `s42_hauser_feshbach.npz`, `s23a_kosmann_singlet.npz`
**Output**: `tier0-computation/s43_fano_continuum.{py,npz,png}`

---

### W5-5: f*sigma_8(z) Growth Rate vs DESI DR1

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: ZERO

**Prompt**:

Compare framework growth rate predictions (= LCDM, since w = -1) against DESI DR1 RSD measurements. The framework's most sensitive observational sentinel.

**Source**: S42 T0-4 (CW 3.1 Test A). S42 CW collab Section 3.1.

**Context.** Growth rate f(z) = d ln D / d ln a ~ Omega_m^{0.55}. Measured via RSD in void-galaxy cross-correlation. Hamaus et al. (Paper 13 in `researchers/Cosmic-Web/`) constrains f(R) gravity at 2-3 sigma with this method. Framework overpredicts DESI DR1 by 1-3 sigma at z = 0.3-1.3 (S42 W5-3).

**Computation Steps**:

1. Solve linear growth ODE for LCDM with Planck 2018 parameters (Omega_m = 0.3153, sigma_8 = 0.8111, h = 0.6736).

2. Compute f*sigma_8(z) at z = 0.295, 0.510, 0.706, 0.930, 1.317 (DESI DR1 redshift bins).

3. Compare to DESI DR1 measurements (from S42 W5-3 table: 0.408, 0.426, 0.424, 0.382, 0.297 with errors).

4. Compute tension in sigma for each bin. Report whether the 1-3 sigma overprediction persists.

5. Also compare to eBOSS measurements if available.

**Pre-registered gate FSIG8-43**: INFO (sentinel — framework = LCDM).

**Input**: Planck parameters, DESI DR1 data (from S42 W5-3)
**Output**: `tier0-computation/s43_fsigma8.{py,npz,png}`

---

### W5-6: Void Expansion Rate as Growth Probe

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute void expansion dynamics as independent growth measurement. Framework predicts exact LCDM void expansion.

**Source**: S42 T2-8 (CW 3.1 Test B). S42 CW collab Section 3.1.

**Context.** Void dynamics (Paper 13 in `researchers/Cosmic-Web/`, H13-E1):

    R_v_ddot + 2H R_v_dot = -(4*pi*G/3) rho_bar (1 + 3w)

Euclid void size function (Paper 33, Co33-E1) forecasts FoM(w0,wa) = 17 from voids alone — sufficient to test w = -1 at percent level. Any deviation in void expansion relative to LCDM falsifies both LCDM and framework simultaneously.

**Computation Steps**:

1. Solve the void expansion ODE with Planck parameters and w = -1.

2. Compute R_v(z)/R_v(0) at z = 0.3, 0.5, 0.7, 1.0, 1.5.

3. Compare to Hamaus-Sutter-Wandelt universal void profile stacking predictions.

4. Compute the Euclid Y5 expected precision on w from void expansion rate alone.

5. Report: framework prediction, LCDM prediction (identical), and the precision at which deviation would falsify both.

**Pre-registered gate VOID-EXP-43**: INFO.

**Input**: Planck parameters, Paper 13 methodology, Paper 33 forecasts
**Output**: `tier0-computation/s43_void_expansion.{py,npz,png}`

---

### W5-7: DESI DR2 Void Catalog Comparison

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: ZERO

**Prompt**:

Compare void size distribution from DESI/ASTRA against framework (= LCDM) predictions.

**Source**: S42 T0-7 (CW 3.6). S42 CW collab Section 3.6.

**Context.** ASTRA void catalog (Paper 34 in `researchers/Cosmic-Web/34_2024_ASTRA_Cosmic_Web_Classification.md`): mean void radius ~24 h^{-1} Mpc. Void size function follows Sheth-van de Weygaert excursion set to ~5%.

**Computation Steps**:

1. Load or construct the LCDM void size function n(R_v) from the SvdW excursion set prediction with Planck parameters.

2. Compare to ASTRA measured void size distribution.

3. Report residuals. Any feature (bump, dip) at > 3 sigma above smooth SvdW fit would be a signal.

4. Cross-reference with the 32-cell tessellation: does the tessellation cell scale (~7000 Mpc) or sub-cell scale (~1957 Mpc from 240/32 subdivision) appear in the void size distribution?

**Pre-registered gate VOID-CAT-43**: INFO.

**Input**: Paper 34 in `researchers/Cosmic-Web/`, Planck parameters
**Output**: `tier0-computation/s43_void_catalog.{py,npz,png}`

---

### W5-8: LRD Clustering Quantitative b Comparison

**Agent**: `little-red-dots-jwst-analyst`
**Model**: opus
**Cost**: ZERO

**Prompt**:

Quantitatively compare measured LRD clustering bias with model predictions.

**Source**: S42 T0-5 (LRD 3.2). S42 LRD collab Section 3.2.

**Context.** Paper 23 (Carranza-Escudero 2025) in `researchers/Little-Red-Dots/`: 124 LRDs over COSMOS-Web + GOODS, bias b ~ 1.5-2.5, M_h ~ 10^{10}-10^{11.5} M_sun. Paper 55 (Roberts 2025): uSIDM predicts b_eff ~ 4.5. Paper 42 (Pacucci 2025): low-spin CDM predicts b ~ 3-4. Framework (inheriting CDM) predicts b ~ 1.5-2.5.

**Computation Steps**:

1. Load measured angular correlation function from Paper 23 data.

2. Compute predicted angular correlation for: (a) framework CDM (b ~ 1.5-2.5), (b) uSIDM (b ~ 4.5, Paper 55), (c) low-spin CDM (b ~ 3-4, Paper 42).

3. Compute chi-squared for each model against the measured correlation.

4. Report: which model is preferred? What is the exclusion significance for uSIDM?

**Pre-registered gate LRD-CLUST-43**: INFO.

**Input**: Papers 23, 42, 55 in `researchers/Little-Red-Dots/`
**Output**: `tier0-computation/s43_lrd_clustering.{py,npz,png}`

---

### W5-9: Simons Observatory CMB Lensing Pre-Registration

**Agent**: `little-red-dots-jwst-analyst`
**Model**: opus
**Cost**: LOW

**Prompt**:

Pre-register the framework's prediction for Simons Observatory CMB lensing convergence power spectrum.

**Source**: S42 T2-6 (LRD 3.4). S42 LRD collab Section 3.4.

**Context.** Paper 30 (Mehta 2025) in `researchers/Little-Red-Dots/`: Simons Observatory achieves 10.4 sigma discrimination between modified cosmology and modified astrophysics for the "too massive too early" tension. CMB lensing enhanced ONLY by modified cosmology. Framework predicts UNCHANGED lensing (w = -1, CDM identical to LCDM). If enhanced lensing detected at z > 2 at > 3 sigma: framework excluded.

**Computation Steps**:

1. Compute the Planck LCDM lensing convergence power spectrum C_l^{kappa kappa} at l = 100-2000 using standard Limber approximation with Planck parameters.

2. This IS the framework prediction (no modification — w = -1 identity theorem).

3. Document: pre-registered prediction = Planck LCDM C_l^{kappa kappa}. Falsification: > 3 sigma deviation in lensing auto-spectrum at z > 2.

4. Compute the Simons Observatory expected error bars at each l bin.

5. Report formal pre-registration document with specific C_l values and error bars.

**Pre-registered gate SIMONS-43**: INFO (pre-registration).

**Input**: Planck parameters, Paper 30
**Output**: `tier0-computation/s43_simons_prereg.{py,npz,png}`

---

### W5-10: SIDM vs NFW Halo Profiles in Lensed LRDs

**Agent**: `little-red-dots-jwst-analyst`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute spatially resolved sigma(r) predictions for lensed LRDs at z > 5 under framework NFW vs uSIDM models.

**Source**: S42 T2-7 (LRD 3.1). S42 LRD collab Section 3.1.

**Context.** Framework predicts NFW 1/r cusp (DM-PROFILE-42). uSIDM (Papers 32, 55, 56 in `researchers/Little-Red-Dots/`) predicts isothermal cores or gravothermal cusps rho ~ r^{-2.2}. FDM predicts soliton cores. Paper 51 (Juodbalis 2025): first direct dynamical BH mass in LRD (M_BH = 50 ± 10 M M_sun at z=7.04).

Transition from BH-dominated to DM-dominated kinematics at r ~ 100-300 pc — resolvable in lensed systems with magnification mu > 10.

**Computation Steps**:

1. Load `s42_dm_profile.npz` (NFW parameters for framework CDM).

2. Construct sigma(r) profile for: (a) NFW (1/r cusp), (b) uSIDM (isothermal core, r_core ~ 100 pc), (c) FDM (soliton core).

3. Add BH point mass (M_BH = 50 M M_sun) to each profile.

4. Compute the observable velocity dispersion profile sigma_obs(r) including seeing/magnification effects for a lensed system at z = 7 with mu = 10.

5. Report: at what r can JWST NIRSpec IFU distinguish NFW from SIDM? What magnification is needed?

**Pre-registered gate SIDM-NFW-43**: INFO.

**Input**: `s42_dm_profile.npz`, Papers 32, 51, 55, 56 in `researchers/Little-Red-Dots/`
**Output**: `tier0-computation/s43_sidm_nfw.{py,npz,png}`

---

### W5-11: Angular-Momentum-Coupled HF Cascade

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the proper Hauser-Feshbach evaporation cascade with angular momentum coupling to resolve the n_breaks ambiguity in the eta prediction.

**Source**: S42 Naz Sugg 1. S42 Nazarewicz collab Section 3 Suggestion 1.

**Context.** Dominant uncertainty in eta = 3.4e-9 is the integer n_breaks (pair-breaking events). Range: n=1 gives 2.2e-7, n=2 gives 3.4e-9, n=3 gives 5.5e-11. The matching n_breaks = 2.18 is suggestively close to integer 2.

Standard nuclear cascade calculation (Bohr-Mottelson Vol. II Ch. 4; PACE4/EMPIRE codes): model sequential evaporation tracking angular momentum at each step. Each emission involving pair-breaking costs exp(-Delta/T_a) = 0.016.

Ingredients exist: 992 KK eigenvalues (HF-KK-42), V matrix (S34 Kosmann), T_a = 0.112 (S40), E_exc = 50.9 (S38).

**Computation Steps**:

1. Load `s42_hauser_feshbach.npz` (masses, multiplicities, branching ratios) and `s23a_kosmann_singlet.npz` (V matrix).

2. Model sequential evaporation: compound state (8 DOF, E_exc = 50.9 M_KK) → first emission → daughter compound → second emission → ... Track angular momentum budget using the KK sector quantum numbers as analog of J, pi.

3. At each step: compute which emissions require pair-breaking (those that change the B2 condensate occupation). Each pair-breaking costs exp(-Delta/T_a) = 0.016.

4. Run 10,000 Monte Carlo cascade trajectories. Record the distribution of n_breaks per cascade.

5. Report: mean n_breaks, standard deviation, mode, and whether the integer ambiguity is resolved (sigma < 0.5).

6. From the n_breaks distribution, compute the eta distribution and compare to observed 6.12e-10.

**Pre-registered gate HF-CASCADE-43**: PASS if n_breaks determined to ±0.5. FAIL if sigma > 1.

**Input**: `s42_hauser_feshbach.npz`, `s23a_kosmann_singlet.npz`, `s38_cc_instanton.npz`
**Output**: `tier0-computation/s43_hf_cascade.{py,npz,png}`

---

### W5-12: Bayesian M_KK Posterior

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Construct a joint Bayesian posterior P(M_KK | alpha_EM, G_N, FIRAS) replacing the current "two routes" approach with a single posterior with quantified uncertainty.

**Source**: S42 Naz Sugg 2. S42 Nazarewicz collab Section 3 Suggestion 2.

**Context.** Two M_KK routes disagree by 0.83 decades: gravity (7.4e16 GeV) vs gauge (5.0e17 GeV). HOMOG-42 constrains M_KK < 1.07e17 from FIRAS. Paper 06 methodology in `researchers/Nazarewicz/` provides GP emulator + Bayesian inference framework.

**Computation Steps**:

1. Define the likelihood for each observable as a function of M_KK:
   - L(alpha_EM | M_KK): from Kerner formula sin^2(theta_W)(tau) with RGE running
   - L(G_N | M_KK): from Seeley-DeWitt a_2 coefficient
   - L(FIRAS | M_KK): from HOMOG-42 delta_tau/tau(M_KK) < 3e-6

2. Construct the joint likelihood L(data | M_KK) = product of individual likelihoods.

3. Use flat log-prior on M_KK in [10^9, 10^{19}] GeV.

4. Compute posterior P(M_KK | data) by MCMC (or grid evaluation if 1D is sufficient).

5. Report: posterior mode, 68% CI, 95% CI, KL divergence between gravity and gauge routes.

6. Identify which observable provides the most information (largest D_KL contribution).

**Pre-registered gate MKK-BAYES-43**: INFO (produces posterior with CI).

**Input**: `s42_constants_snapshot.npz`, `s42_homogeneity.npz`, PDG values
**Output**: `tier0-computation/s43_mkk_posterior.{py,npz,png}`

---

