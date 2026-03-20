## III-f. Wave 6: Long-Term + Specialist Investigations (22 tasks, parallel)

All Wave 6 tasks are independent and can run in parallel. Each is a computation from the S42 recommendation library that has not been executed in any prior session.

### W6-1: Schwinger-Instanton Duality and epsilon_CP

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: HIGH
**Source**: T3-1 (Dirac Q4). S42 Dirac collab Q4.

**Prompt**:

Compute whether KK Schwinger pair production rate differs for particles vs antiparticles in chiral sectors.

**Context.** S38 duality S_Schwinger(0.070) = S_inst(0.069) identifies instanton gas with pair creation in Euclidean time. In QED, Schwinger mechanism is CP-symmetric. But the KK version involves the full Dirac operator D_K with chiral structure: J*gamma = -gamma*J (KO-dim 6). The chiral sectors (1+gamma_9)/2 and (1-gamma_9)/2 have different eigenvalue distributions because the Jensen deformation breaks SU(3) → U(1)_7 × SU(2) asymmetrically across chiralities.

**Computation Steps**:

1. Load `tier0-computation/s38_cc_instanton.npz` (S_inst, gap data), `tier0-computation/s35_pfaffian_corrected_j.npz` (J matrix), and Dirac infrastructure from `tier0-computation/tier1_dirac_spectrum.py`.

2. Separate the Schwinger pair production integral into chiral sectors. The pair production rate per unit volume per unit time is:

   $$\Gamma_\pm = \frac{(eE)^2}{4\pi^3} \sum_n \frac{1}{n^2} \exp\left(-\frac{n\pi m_\pm^2}{eE}\right)$$

   where m_± are the effective masses in the (1±gamma_9)/2 sectors. The "electric field" E is the spectral action gradient dS/dtau = 58,673.

3. Compute the effective mass spectrum in each chiral sector separately. Project D_K eigenvalues onto (1+gamma_9)/2 and (1-gamma_9)/2. By Theorem T2 ({gamma_9, D_K} = 0), the full spectrum is paired (lambda ↔ -lambda). But within each chiral sector, the eigenvalue DISTRIBUTION may differ.

4. Compute Gamma_+ and Gamma_- independently. If Gamma_+ ≠ Gamma_-:

   $$\epsilon_{\text{CP}} = \frac{\Gamma_+ - \Gamma_-}{\Gamma_+ + \Gamma_-}$$

5. If epsilon_CP ≠ 0: combine with W1-3 eta_kinematic to get eta_net = eta_kin * epsilon_CP. Compare to observed 6.12e-10.

6. Cross-check: verify that Gamma_+ + Gamma_- reproduces the total Schwinger rate from S38.

**Pre-registered gate SCHWINGER-CP-43**: INFO. If epsilon_CP > 10^{-6}: baryogenesis channel from Schwinger duality. If epsilon_CP = 0 exactly: chiral sectors produce equal matter/antimatter (CP-symmetric).

**Input**: `s38_cc_instanton.npz`, `s35_pfaffian_corrected_j.npz`, `tier1_dirac_spectrum.py`
**Output**: `tier0-computation/s43_schwinger_cp.{py,npz,png}`

### W6-2: Quality Factor Spectrum Q_i for 8 BdG Modes

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: LOW
**Source**: T3-2 (QA 3.4). S42 QA collab Section 3.4.

**Prompt**:

Extend S41 Q_B2 ~ 10 (struck drum) to all 8 BdG modes. The quality factor Q_i = omega_i / (2*Im[Sigma_i]) where Im[Sigma] is the self-energy imaginary part from V_rem coupling.

**Context.** S41 computed Q_B2 ~ 10. The full Q spectrum reveals: which modes are long-lived (Q >> 1, bell-like) vs overdamped (Q ~ 1, drum-like), whether B1 has anomalously low Q at the van Hove singularity (v_B1 = 0 at tau ~ 0.25), and whether any mode has Q → infinity protected by selection rules (V(B1,B1) = 0 exact from S23a).

**Computation Steps**:

1. Load V_8x8_full from `tier0-computation/s36_mmax_authoritative.npz` and BdG spectrum from S40 QRPA data.

2. For each mode i (B2×4, B1×1, B3×3): compute the self-energy imaginary part:

   $$\text{Im}[\Sigma_i(\omega_i)] = \pi \sum_j |V_{ij}|^2 \rho_j(\omega_i)$$

   where rho_j is the density of states of mode j at frequency omega_i.

3. Compute Q_i = omega_i / (2 * Im[Sigma_i]) for all 8 modes.

4. Classify each mode: Q > 100 (bell), 10 < Q < 100 (moderate), Q < 10 (drum), Q < 1 (overdamped).

5. Check: does B1 have Q → infinity from V(B1,B1) = 0 selection rule? If so, B1 is an undamped mode protected by U(2) symmetry.

6. Report: Q spectrum table, damping classification, selection rule identification.

**Pre-registered gate Q-SPECTRUM-43**: INFO.

**Input**: `s36_mmax_authoritative.npz`, S40 QRPA data
**Output**: `tier0-computation/s43_quality_factors.{py,npz,png}`

### W6-3: BG Spinor Overlap Correction to Polariton Gap

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM
**Source**: T3-5 (Baptista 3.4). S42 Baptista collab Section 3.4.

**Prompt**:

Compute the Bourguignon-Gauduchon spinor comparison map correction to the POLARITON-42 polariton gap.

**Context.** POLARITON-42: min gap 0.063 M_KK, 3.7e13x too large for Higgs. Paper 18 Appendix B in `researchers/Baptista/`: tilde{Phi} map between eigenspinors at different metrics introduces overlap matrix modifying effective coupling to V_{ij} * <Phi(psi_i)|psi_j>. Expected O(1) — unlikely to close 13-order gap but is missing systematic.

**Computation Steps**:

1. Read Paper 18 Appendix B. Construct tilde{Phi} (parallel transport of spinors between g(tau) and g(tau+delta_tau) along Jensen curve).

2. Compute overlap matrix O_{ij} = <Phi(psi_i(tau))|psi_j(tau+delta_tau)> for all 8 BdG eigenstates at fold.

3. Corrected couplings: V^{corr}_{ij} = V_{ij} * O_{ij}.

4. Recompute all 5 polariton gaps with corrected couplings.

5. Report: correction factors, corrected gaps, comparison to uncorrected.

**Pre-registered gate BG-POL-43**: INFO.

**Input**: Paper 18 in `researchers/Baptista/`, `s42_polariton.npz`, `tier1_dirac_spectrum.py`
**Output**: `tier0-computation/s43_bg_spinor_polariton.{py,npz,png}`

### W6-4: Relic Modulus Fluctuation as Spatial Alpha Pattern

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: MEDIUM
**Source**: T3-8 (QF Q5). S42 QF collab Section 3D. S42 CW addendum F.1 (ALPHA-ENV-43).

**Prompt**:

Compute the spatial power spectrum of delta_alpha/alpha from KZ domain structure and determine whether it is detectable by quasar absorption spectroscopy.

**Context.** HOMOG-42: delta_tau/tau = 1.75e-6 at transit. Clock constraint (S22d): dalpha/alpha = -3.08 * delta_tau → delta_alpha/alpha ~ 5.4e-6. This is the sole surviving LSS discriminant (ALPHA-ENV-43 from CW addendum). Webb/Barrow quasar absorption surveys reach ~10^{-6} precision. The framework predicts a SPATIAL PATTERN in alpha correlated with cosmic web topology (voids vs filaments).

**Computation Steps**:

1. Model the tau field as random KZ domains with correlation length xi_KZ = 0.152 M_KK^{-1} and amplitude delta_tau/tau = 1.75e-6 (HOMOG-42).

2. The spatial power spectrum of delta_tau is P_tau(k) ~ const for k < 1/xi_KZ, ~ k^{-(d+z_KZ)} for k > 1/xi_KZ.

3. Convert to alpha: P_alpha(k) = (3.08)^2 * P_tau(k).

4. Project through modulated reheating to the last-scattering surface. Compute the angular power spectrum C_l^{alpha} at l = 100-1000.

5. Compare amplitude to current quasar absorption survey precision (~10^{-6}, Webb et al. 2011 UVES/VLT).

6. Cross-reference with CW addendum F.1: the prediction is delta_alpha/alpha correlated with void/cluster environment. Compute the expected Spearman correlation coefficient.

**Pre-registered gate ALPHA-PATTERN-43**: INFO. If amplitude > 10^{-6}: detectable with current instruments.

**Input**: `s42_homogeneity.npz`, `s42_gradient_stiffness.npz`, `s42_constants_snapshot.npz`
**Output**: `tier0-computation/s43_alpha_pattern.{py,npz,png}`

### W6-5: Generalized Second Law for Fabric Transit

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: LOW
**Source**: Hawking 3.1. S42 Hawking collab Section 3.1.

**Prompt**:

Extend GSL-40 to the fabric picture with 32-cell spatial structure. Verify dS_gen/dt >= 0 throughout the transit.

**Context.** S_gen = S_spec(tau) + S_GGE + S_defects. S_spec monotonically increasing (CUTOFF-SA-37). S_GGE jumps 0 → 6.701 bits at transit. S_defects proportional to KZ string network length (decreasing as strings reconnect). Bekenstein bound: S_max = 2*pi*R*E/(hbar*c) = 2*pi * (1/M_KK) * 50.9*M_KK = 320 nats per KK site. Actual S_Gibbs = 4.64 nats (69x below bound, consistent with product state S_ent = 0).

**Computation Steps**:

1. Compute S_spec(tau) at tau = 0 (pre-transit), 0.19 (fold), 0.15 (post-transit). Use S_full from `s36_sfull_tau_stabilization.npz`. S_spec ~ ln(S_full) as entropy analog.

2. S_GGE: 0 at tau=0, 6.701 bits = 4.64 nats at fold (from S40), 6.701 bits post-transit (permanent by integrability).

3. S_defects: estimate string network length from KZ density n_string = 1/xi_KZ^2 = 13.8 M_KK^2. String entropy ~ n_string * L_string * mu_string / T. Decreasing as strings reconnect.

4. Sum S_gen at each epoch. Verify dS_gen/dt >= 0 at each transition.

5. Report Bekenstein saturation fraction at each epoch.

**Pre-registered gate GSL-43**: INFO. FAIL if dS_gen/dt < 0 at any epoch (GSL violated).

**Input**: `s42_gradient_stiffness.npz`, `s42_gge_energy.npz`, `s42_kz_fnl.npz`
**Output**: `tier0-computation/s43_gsl_transit.{py,npz,png}`

### W6-6: Internal First Law with Fabric EOS

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: LOW
**Source**: Hawking 3.2. S42 Hawking collab Section 3.2.

**Prompt**:

Verify the analog first law numerically at the fold: dE = T_a dS_GGE + X_tau dtau + sigma dA_wall + mu_string dL_string. T_a = 0.112 M_KK (acoustic temperature, S40). X_tau = dS/dtau = 58,673 (spectral action gradient). sigma = wall surface energy from W-Z-42. mu_string = string tension from FNL-42. Effacement: T_a dS_GGE term negligible vs X_tau dtau (ratio 10^{-6}).

**Computation**: Compute each term from existing data at fold. Take delta_tau = 0.001. Verify sum of right-hand side = total dE. Report fractional contribution of each term.

**Pre-registered gate FIRSTLAW-43**: INFO. FAIL if sum deviates from dE by > 1%.

**Input**: `s42_gradient_stiffness.npz`, `s42_gge_energy.npz`, `s42_fabric_wz_v2.npz`, `s42_kz_fnl.npz`
**Output**: `tier0-computation/s43_first_law.{py,npz,png}`

---

### W6-7: Trans-Planckian Universality for KZ Spectrum

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: LOW
**Source**: Hawking 3.3. S42 Hawking collab Section 3.3.

**Prompt**:

Test whether f_NL = 0.014 (FNL-42) and xi_KZ = 0.152 M_KK^{-1} are insensitive to the KK tower truncation level max_pq_sum. If critical exponents (nu=0.63, z=2.02) are truly universal (infrared properties), xi_KZ should converge as truncation increases. This is the trans-Planckian universality argument (Hawking Paper 05) applied to KZ defects.

**Computation**: Recompute M_max and BCS gap at max_pq_sum = 4, 5, 6, 7 using `tier1_dirac_spectrum.py`. Derive xi_KZ at each truncation. Report convergence. Variation > 10% = universality violated.

**Pre-registered gate TRANSP-43**: INFO. Report convergence rate.

**Input**: `tier1_dirac_spectrum.py`, `s42_kz_fnl.npz`
**Output**: `tier0-computation/s43_transplanckian.{py,npz,png}`

---

### W6-8: Greybody Factor from Acoustic Metric

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM
**Source**: Hawking 3.5. S42 Hawking collab Section 3.5.

**Prompt**:

Compute the greybody factor Gamma(omega) for BdG quasiparticle modes propagating through the acoustic geometry near the van Hove singularity. T_a/T_Gibbs = 0.993 (S40) but T_Rindler = 0.158 M_KK (40% higher). The discrepancy IS the greybody factor — the acoustic metric modifies the effective potential. The ratio T_a/T_Rindler = 0.71 should be reproduced by the transmission coefficient through the effective potential barrier.

**Computation**: Construct acoustic metric near B1 van Hove (v_B1 = 0 at tau ~ 0.25, creating a turning point). Solve scalar wave equation in this background for each BdG mode. Extract transmission T(omega). Compare Gamma_eff = T_a/T_Rindler to the computed transmission.

**Pre-registered gate GREYBODY-43**: INFO. PASS if computed Gamma reproduces 0.71 ± 10%.

**Input**: S40 QRPA data, `s42_fabric_dispersion.npz`
**Output**: `tier0-computation/s43_greybody.{py,npz,png}`

---

### W6-9: Polariton Dispersion Across Full BZ

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: LOW
**Source**: Tesla 3b. S42 Tesla collab Section 3b.

**Prompt**:

Map all 8 dressed bands omega_i(k) for k in [0, pi/a_KK]. POLARITON-42 found B2-B1 anticrossing at k* = 0.209 M_KK with gap 0.160 M_KK. Full BZ map identifies: additional group velocity zeros beyond B2 flat band, Dirac-cone-like linear crossings (topologically protected), anomalous DOS near anticrossings (van Hove singularities in dressed spectrum).

**Computation**: Construct 8×8 dressed Hamiltonian H(k) = H_bare(k) + V for k grid of 100 points in [0, pi/a_KK]. Diagonalize at each k. Map bands, identify all anticrossings, Reststrahlen gaps, group velocity zeros. Compare to phononic crystal band structures.

**Pre-registered gate POL-BZ-43**: INFO.

**Input**: `s42_polariton.npz`, `s36_mmax_authoritative.npz` (V_8x8_full)
**Output**: `tier0-computation/s43_polariton_bz.{py,npz,png}`

---

### W6-10: Acoustic Metric from Tau Modulus

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM
**Source**: Tesla 3c. S42 Tesla collab Section 3c.

**Prompt**:

Compute the multi-metric structure where each BdG branch sees a different effective acoustic metric. Dispersion omega^2 = k^2 + m_i^2 gives g^{mu nu}_eff = diag(-1,1,1,1) + (m_i^2/omega^2)*diag(1,0,0,0) per branch. B1 (m=1.138), B2 (m=2.228), B3 (m=0.990) each see different effective metrics — phononic bimetric (trimetric) gravity.

**Computation**: Construct effective metric for each branch. Compute mode-dependent: group velocity v_g(omega), light-cone structure, causal structure differences between branches. Assess whether multi-metric produces: slow-light effects at anticrossings, mode-dependent gravitational coupling, any observable signature.

**Pre-registered gate ACOUS-METRIC-43**: INFO.

**Input**: `s42_fabric_dispersion.npz`, `s42_polariton.npz`
**Output**: `tier0-computation/s43_acoustic_metric.{py,npz,png}`

---

### W6-11: 2:1 Parametric Near-Resonance Instability

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM
**Source**: Tesla 3d. S42 Tesla collab Section 3d.

**Prompt**:

Test whether the omega_B2/omega_B1 = 1.988 near-resonance (0.6% from exact 2:1) drives parametric instability that modifies GGE occupation numbers over cosmological timescales.

**Context.** If tau modulus oscillates at omega_tau = 2.062 M_KK (zero-point amplitude sigma_ZP = 0.026), it can parametrically excite B1 modes because omega_tau ~ 1.8 * omega_B1. Map the Mathieu stability diagram for each BdG mode. Detuning = (omega_tau - 2*omega_Bi)/(2*omega_Bi). If any mode falls within instability tongue: zero-point tau oscillation amplifies that quasiparticle mode → GGE occupation numbers evolve → tests whether GGE is truly permanent or parametric resonance slowly drains energy between branches (challenging integrability protection).

**Computation**: Construct Mathieu equation for each of 8 modes coupled to tau oscillation. Compute instability tongue boundaries for driving amplitude sigma_ZP = 0.026. Determine which modes (if any) are inside an instability tongue. Report growth rate for unstable modes.

**Pre-registered gate PARAM-RES-43**: INFO. If any mode unstable: GGE permanence challenged.

**Input**: `s42_fabric_dispersion.npz`, `s42_gradient_stiffness.npz`, `s37_pair_susceptibility.npz`
**Output**: `tier0-computation/s43_parametric_resonance.{py,npz,png}`

### W6-12: Persistent Homology at Sub-Cell Scales

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: HIGH
**Source**: T3-3 (CW 3.1 Test C). S42 CW collab Section 3.1 Test C.

**Prompt**:

Test whether 32-cell tessellation imprints on persistent Betti numbers of the matter distribution. Papers 27 (Wilding) and 28 (Pranav) in `researchers/Cosmic-Web/` established persistent homology as rigorous cosmic web characterization. Tessellation imprint would produce excess beta_2 (void cavity) persistence at cell geometry scales. In LCDM, Betti numbers fully determined by initial P(k) + gravity. Excess beta_2 at L > 500 Mpc exceeding LCDM 99th percentile from mock catalogs = signal.

**Computation**: Construct LCDM mock catalogs (N-body or heuristic). Compute Betti curves beta_0, beta_1, beta_2 as function of density threshold delta. Compare standard LCDM to tessellation-modified ICs. Look for excess features at any scale above BAO.

**Pre-registered gate PERS-HOM-43**: INFO. Report whether any beta excess detected.

**Input**: LCDM N-body mocks, Papers 27, 28 in `researchers/Cosmic-Web/`
**Output**: `tier0-computation/s43_persistent_homology.{py,npz,png}`

---

### W6-13: Spectral Triple Dissolution Threshold

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: HIGH
**Source**: T3-4 (QF Q3). S42 QF collab Q3.

**Prompt**:

Determine at what metric fluctuation amplitude the Dirac operator D_K transitions from Poisson level statistics (integrable, block-diagonal) to GOE statistics (chaotic, blocks dissolved). Block-diagonal theorem (S22b) is exact for ANY left-invariant metric. Planck-scale foam fluctuations are NOT left-invariant. QF collab: delta_g/g ~ (M_KK/M_P)^{1/2} ~ 10^{-0.75} → 20% perturbation of D_K.

**Computation**: Add random non-left-invariant perturbations to g_K at amplitudes epsilon = 0.001, 0.01, 0.05, 0.10, 0.20, 0.50. Diagonalize D_K at each. Compute level spacing statistics (nearest-neighbor spacing distribution). Identify crossover from Poisson (P(s) = exp(-s)) to GOE (P(s) = (pi*s/2)*exp(-pi*s^2/4)). Report crossover amplitude.

**Pre-registered gate DISSOLUTION-43**: INFO. Report epsilon_crossover.

**Input**: `tier1_dirac_spectrum.py`
**Output**: `tier0-computation/s43_spectral_dissolution.{py,npz,png}`

---

### W6-14: Foam Imprint in GGE Occupations

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: HIGH
**Source**: T3-7 (QF Q4). S42 QF collab Q4.

**Prompt**:

If transit occurs through foamy external metric (Hawking), stochastic gravitational corrections modify GGE occupation numbers at order (l_P * M_KK)^2 ~ 10^{-3}. The GGE is determined by ground state + unitary evolution + integrability (S38). Foam introduces DECOHERENCE that could break Richardson-Gaudin integrability. Is the 10^{-3} correction detectable in DM abundance or matter-antimatter ratio?

**Computation**: Model foam as stochastic perturbation to the BCS Hamiltonian during transit. Amplitude ~ (l_P * M_KK)^2. Evolve the GGE with and without foam noise. Compare occupation numbers. Report delta_n_i for each of 8 modes.

**Pre-registered gate FOAM-GGE-43**: INFO.

**Input**: `s42_gge_energy.npz`, `s38_cc_instanton.npz`, `s37_pair_susceptibility.npz`
**Output**: `tier0-computation/s43_foam_gge.{py,npz,png}`

---

### W6-15: GQuEST Null Prediction Pre-Registration

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: ZERO
**Source**: QF 3F. S42 QF collab Section 3F.

**Prompt**:

Pre-register: framework predicts ZERO pixellon noise at GQuEST (Paper 17 in `researchers/Quantum-Foam/`). Reasoning: m_tau = 2.062 M_KK >> any lab frequency. Fabric fluctuations at optical f ~ 10^{14} Hz suppressed by exp(-m_tau*c^2/(h*f)) ~ exp(-10^{25}) = 0. Document the prediction formally. If GQuEST detects signal: either non-fabric origin, wrong m_tau, or ungapped DOF.

**Computation**: Compute the suppression factor at GQuEST's operating frequency. Write formal pre-registration document.

**Pre-registered gate GQUEST-43**: INFO (pre-registration document).

**Input**: `s42_fabric_dispersion.npz` (m_tau), Paper 17 in `researchers/Quantum-Foam/`
**Output**: `tier0-computation/s43_gquest_prereg.{py,npz,png}`

---

### W6-16: Dowker-Sorkin Everpresent Lambda Comparison

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: LOW
**Source**: QF 3E. S42 QF collab Section 3E.

**Prompt**:

Document the structural comparison between Dowker-Sorkin everpresent Lambda (Paper 19 in `researchers/Quantum-Foam/`: Lambda ~ 1/sqrt(V), fluctuating, V-dependent) and the framework (Lambda = const from spectral action, no V-dependence). These are structurally incompatible. If DESI confirms w_a != 0: framework excluded, Dowker-Sorkin survives (accommodates w_a != 0 through Lambda sign reversals on Hubble timescales). Document mutual falsification criteria.

**Computation**: Compare the two Lambda predictions quantitatively. For V = H_0^{-4}: Lambda_DS ~ H_0^2, Lambda_framework = S_fold * M_KK^4. Report ratio. Identify the DESI sigma threshold at which one model is excluded.

**Pre-registered gate DS-LAMBDA-43**: INFO.

**Input**: Paper 19 in `researchers/Quantum-Foam/`, `s42_fabric_wz_v2.npz`
**Output**: `tier0-computation/s43_dowker_sorkin.{py,npz,png}`

---

### W6-17: Volovik Flat Band Reinterpretation

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM
**Source**: Volovik 3b. S42 Volovik collab Section 3b.

**Prompt**:

Determine whether the B2 sector at the fold is in the flat-band BCS regime (Paper 18 in `researchers/Volovik/`: T_c ~ g, linear) or conventional BCS (T_c ~ exp(-1/gN)). Currently W/Delta ~ 0.9 (crossover, not deep flat-band). Even moderate flattening produces linear-in-g scaling (Paper 18 central result).

**Computation**: Map eigenvalue dispersion lambda_k(tau) across full BCS window [0.15, 0.25] using `tier1_dirac_spectrum.py`. Compute effective bandwidth W(tau) of the B2 gap-edge modes at each tau. Flat-band criterion: W << Delta_pair (Delta = 0.464 M_KK from S37). Compute T_c(g) scaling from actual DOS: is it exponential or linear in g? Report W/Delta ratio, T_c scaling, and whether flat-band enhancement is operative.

**Pre-registered gate FLATBAND-43**: INFO.

**Input**: `tier1_dirac_spectrum.py`, `s35_ed_corrected_dos.npz`, Paper 18 in `researchers/Volovik/`
**Output**: `tier0-computation/s43_flat_band.{py,npz,png}`

### W6-18: Elasticity Tetrad Derivation of Z(tau)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM
**Source**: Volovik 3c. S42 Volovik collab Section 3c.

**Prompt**:

Derive Z(tau) microscopically from the elasticity tetrad formalism (Papers 22-23 in `researchers/Volovik/`) and compare to the spectral sum Z_spectral = 74,731 from S42.

**Context.** Papers 22-23 establish structural identity between elasticity tetrads and gravitational tetrads. Z(tau) = C_ijkl * d^i d^j d^k d^l where C is the elastic tensor of SU(3) under Jensen. Paper 22: R_4D ~ nabla nabla u ~ Z * (nabla tau)^2. The microscopic derivation gives the FULL elastic modulus tensor (all directions), not just the Jensen trace.

S42 Baptista collab: Z_spectral is the spectral pullback of the DeWitt supermetric through the BG spinor map. Z/G = 14,946 encodes spectral amplification by 992 eigenvalues.

**Computation Steps**:

1. Read Papers 22, 23 in `researchers/Volovik/`.

2. Write the Jensen deformation as an elasticity tetrad: e^a_I = delta^a_I + epsilon^a_I(tau).

3. Compute the elastic modulus tensor C^{IJKL} from the spectral action's response to strain: C^{IJKL} = d^2 S / (d epsilon^{IJ} d epsilon^{KL}).

4. Contract with Jensen deformation direction: Z_tetrad = C^{IJKL} * n_IJ * n_KL.

5. Compare Z_tetrad to Z_spectral = 74,731. If they agree: the spectral sum and elastic modulus compute the same thing, confirming the structural identity.

6. Report the full C tensor (not just the trace). Identify if any direction has dramatically different stiffness.

**Pre-registered gate ELAST-Z-43**: INFO. Report Z_tetrad and Z_tetrad/Z_spectral ratio.

**Input**: `s42_gradient_stiffness.npz`, Papers 22, 23 in `researchers/Volovik/`
**Output**: `tier0-computation/s43_elasticity_tetrad.{py,npz,png}`

---

### W6-19: Schwinger-Instanton Factor 36 Resolution

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM
**Source**: Volovik 3d. S42 Volovik collab Section 3d.

**Prompt**:

Resolve the factor 36 discrepancy between S_Schwinger computed from the PG horizon formula and S_inst from the BCS instanton gas.

**Context.** S42 Volovik collab 3d: kappa_eff = (1/2)*|dV/dtau|/sqrt(Z) = 58,673/(2*273.4) = 107. S_Schwinger = pi*Delta^2/(kappa_eff*c_fabric) = pi*(0.115)^2/(107*210) = 0.0019. But S_inst = 0.069 (S37). Factor 36. The effective kappa must involve BCS dynamics, not just spectral action gradient. Paper 29 (`researchers/Volovik/29_2016_Volovik_Black_Hole_Hawking_PG_Analog.md`) gives the PG horizon pair creation formula.

**Computation Steps**:

1. Read Paper 29 (PG horizon pair creation).

2. Recompute kappa_eff using the BCS-relevant gradient (dE_BCS/dtau at the fold, not dS/dtau). The BCS energy gradient is much smaller (~102 vs 58,673).

3. With kappa_BCS = (1/2)*|dE_BCS/dtau|/sqrt(Z_B2): compute S_Schwinger_BCS.

4. Compare to S_inst = 0.069. If they match: the duality is between BCS dynamics and instanton gas (same universality class). If not: numerical coincidence.

5. Report: which kappa gives the correct S_Schwinger, and what this means for the pair creation mechanism.

**Pre-registered gate SCHWINGER-36-43**: INFO. Report whether factor 36 is resolved.

**Input**: `s38_cc_instanton.npz`, `s42_gradient_stiffness.npz`, Paper 29 in `researchers/Volovik/`
**Output**: `tier0-computation/s43_schwinger_factor36.{py,npz,png}`

---

### W6-20: All 8 GGE Effective Temperatures

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW
**Source**: T-GGE-43. Paper 34 in `researchers/Volovik/`. S42 R4 Q3.

**Prompt**:

Compute all 8 GGE effective temperatures beta_k^{-1} from the Richardson-Gaudin conserved integrals. The GGE is a time crystal (Paper 34) with persistent oscillations at omega_n = dE/dN_n. T_RH = 1.1*M_KK from E-GGE-42 is ONE of these 8.

**Context.** S42 R4 Q3: "The reheating is genuinely the FIRST heating. T_eff is not a thermodynamic temperature but a GGE effective temperature — the first of eight beta_i^{-1} Lagrange multipliers."

**Computation Steps**:

1. Load Richardson-Gaudin eigenvalues from `tier0-computation/s37_pair_susceptibility.npz`.

2. The GGE density matrix is rho_GGE = (1/Z_GGE) * exp(-sum_k beta_k I_k).

3. For each conserved integral I_k: compute beta_k = dS_GGE/dI_k where S_GGE = -Tr(rho_GGE ln rho_GGE).

4. Convert to temperatures: T_k = 1/beta_k.

5. Identify which T_k corresponds to T_RH = 1.1*M_KK (the one conjugate to total energy).

6. Report: all 8 temperatures, their ratios, physical interpretation of each (which observable couples to which temperature).

**Pre-registered gate GGE-TEMP-43**: INFO.

**Input**: `s37_pair_susceptibility.npz`, `s38_cc_instanton.npz`, Paper 34 in `researchers/Volovik/`
**Output**: `tier0-computation/s43_gge_temperatures.{py,npz,png}`

---

### W6-21: KZ-CELL Monte Carlo N_cell Variants

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: MEDIUM
**Source**: KZ-CELL-43 (S42 scales workshop).

**Prompt**:

Test multiple N_cell values to determine which (if any) discrete mode count from the Dirac spectrum matches observed giant structure scales.

**Context.** GIANT-VORONOI-42 tested N=32 → structures 5x too large (median L_max = 4,672 Mpc vs Giant Arc ~1,000 Mpc). The 240/32 subdivision gives N_sub = 240 with cell scale ~1,957 Mpc (still 2x large). This is NOT parameter fitting — it tests whether ANY N from the Dirac spectrum's mode structure matches observations.

**Computation Steps**:

1. Use the `s42_giant_voronoi.py` methodology (1,000 Poisson-Voronoi realizations, random observer position, shell intersections at z=0.8 and z=1.6). NOTE: reduced from 10,000 to avoid OOM kills.

2. Run for N_cell = 32, 64, 128, 240, 500 (5 values, reduced from 7).

3. For each N: record P(N_giant >= 2), median L_max, mean N_giant, N_giant distribution.

4. Identify which N produces median L_max ~ 1,000 Mpc (Giant Arc scale). If none: the tessellation hypothesis fails at all mode counts.

5. Cross-reference: N=32 (tau=0 eigenvalue types), N=240 (tau>0 eigenvalue types). Are any other N values structurally motivated from the Dirac spectrum?

**Pre-registered gate KZ-CELL-43**: INFO. Report which N (if any) matches Giant Arc scale.

**Input**: `s42_giant_voronoi.py` (methodology), N_eff values from S41
**Output**: `tier0-computation/s43_kz_cell_variants.{py,npz,png}`

---

### W6-22: Cosmic Web Pre-Registerable Predictions (F.1-F.5)

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: LOW
**Source**: CW addendum F.1-F.5. S42 `sessions/session-42/session-42-cosmic-web-addendum.md`.

**Prompt**:

Formalize all 5 pre-registerable predictions from the S42 cosmic web addendum as formal pre-registration documents with specific pass/fail criteria, instruments, expected signals, and LCDM comparisons.

**The 5 predictions**:

1. **F.1 ALPHA-ENV-43**: delta_alpha/alpha ~ 10^{-6} correlated with void/cluster environment. Instrument: VLT/UVES, Keck/HIRES, ELT/ANDES. Survey: cross-match quasar absorption (Murphy et al. 2022, ~300 absorbers) with DESI DR2 void catalogs. PASS: Spearman rho > 0.2 at > 2 sigma. FAIL: |rho| < 0.05 at 95% CL with N > 100 pairs.

2. **F.2 IMP-ASYM-43**: Void wall impedance asymmetry in xi_vg. Instrument: DESI/Euclid. Expected: asymmetry ~ 10^{-6} (effacement-suppressed). PASS: asymmetry detected > 3 sigma. Likely FAIL (effacement kills it).

3. **F.3 VSF-43**: Void size function features from acoustic selection rules. Instrument: DESI Y5/Euclid. PASS: feature > 5% above smooth SvdW fit at > 3 sigma. FAIL: residuals consistent with noise.

4. **F.4 PH-TESS-43**: Persistent homology anomaly at tessellation scale. Instrument: DESI/Euclid. PASS: excess beta_2 above LCDM 99th percentile at L > 500 Mpc.

5. **F.5 MVGAD-43**: Massive void galaxy assembly delay > 0.5 Gyr at M* > 10^{11} M_sun after density matching. Instrument: DESI spectroscopy + JWST photometry. LCDM: no significant delay for M* > 10^{11} (massive halos form independently of UV feedback). Conditional on Z(tau) quasiparticle depletion channel.

**Computation**: Write formal pre-registration document for each. Include: prediction, null hypothesis, instrument, survey methodology, pass/fail criteria, expected signal amplitude, LCDM comparison.

**Pre-registered gate CW-PREREG-43**: INFO (5 pre-registration documents).

**Input**: `sessions/session-42/session-42-cosmic-web-addendum.md`, Papers in `researchers/Cosmic-Web/`
**Output**: `tier0-computation/s43_cw_preregistrations.{py,npz,png}`

---

