# Session 50: O-Z Investigation — Computation Prompts

**Purpose**: All prompts dispatched to agents testing the O-Z identity alpha_s = n_s² - 1 and its escape routes. Collected for review of methodology, assumptions, and potential gaps.

**Result**: 8 computations, 7 FAIL, 1 PASS (sigma_8 viable). The identity is confirmed structural by 5 independent proofs.

---

## 1. W1-A: 3-Pole Leggett Propagator (LEGGETT-PROPAGATOR-50)

**Agent**: landau-condensed-matter-theorist | **Verdict**: FAIL

**Prompt**:

You are computing the 3-pole Leggett propagator on the 32-cell fabric for the Phonon-Exflation framework.

**Context**: S49 proved alpha_s = n_s² - 1 = -0.069 is an EXACT algebraic identity for the single-pole O-Z propagator P(K) = T/(J K² + m²). This is 6σ from Planck (alpha_s = 0.000 ± 0.008). All 6 reviewers converge: the escape is that the BCS state on SU(3) has 3 inter-sector bands (B1-B2, B2-B3, B1-B3) with Josephson couplings J_12 = 0.035, J_23 = 0.00181, J_13 ~ 0. The propagator has 3 poles, not 1. The single-pole O-Z is a long-wavelength approximation.

From S49 DIPOLAR-CATALOG-49: The Leggett mode provides Goldstone mass omega_L1 = 0.070 M_KK (18% from n_s target m_req = 0.059 M_KK). From S49 ALPHA-S-BAYES-49: J_ij uncertainties contribute 0% to alpha_s variance in O-Z. The question is whether the FUNCTIONAL FORM changes with 3 poles.

Tesla (S49 wayforward): "The Leggett spectral function with GGE occupations" is one of three alternative propagators. Landau: "The 3-band Josephson propagator has 3 poles. Multi-pole propagator modifies the running formula — alpha_s is NOT rigid if O-Z is wrong."

**Method**:
1. Read `tier0-computation/canonical_constants.py` for all framework constants.
2. Read `tier0-computation/s49_alpha_s_bayes.py` for the O-Z propagator implementation.
3. Read `tier0-computation/s49_dipolar_catalog.py` for Josephson coupling data.
4. Read `tier0-computation/s48_leggett_mode.npz` (or S48 Leggett data files) for omega_L1, omega_L2, J_ij values.
5. Construct the 3×3 Josephson response matrix G(K, omega) for the 3-band system on the 32-cell fabric (4×4×2 lattice with anisotropic J_xy = 0.933, J_z = 0.059). The matrix has entries G_ab(K) = [delta_ab * (J_a K² + m_a²) - J_ab]^{-1} where m_a is the sector-dependent Leggett mass.
6. The physical propagator is P(K) = Tr[G(K)] or the appropriate projection. Decompose into partial fractions: P(K) = sum_{i=1}^{3} R_i / (K² + mu_i²) where mu_i are the 3 pole positions and R_i are the residues.
7. Compute n_s from the angular-averaged P(K): n_s(K) = 1 + d ln P_avg(K) / d ln K where P_avg(K) = (1/4pi) integral P(K_vec) d(Omega) at fixed |K|
8. Compute alpha_s = d n_s / d ln K at K_pivot (CMB pivot mapped to fabric).
9. Compare to the O-Z prediction: does alpha_s still equal n_s² - 1?

**Pre-registered gate**: PASS if alpha_s in [-0.040, 0] AND n_s in [0.950, 0.980]. FAIL if identity survives.

---

## 2. W1-C: Bogoliubov Imprint (BOGOLIUBOV-IMPRINT-50)

**Agent**: volovik-superfluid-universe-theorist | **Verdict**: FAIL

**Prompt**:

You are computing Bogoliubov coefficients during transit to test whether the Leggett mass survives post-transit.

**Context**: S49 proved the Leggett mode is DESTROYED post-transit (LEGGETT-TRANSIT-49 FAIL, LEGGETT-GGE-49 INFO): Delta=0, J=0, omega_L=0. The Volovik paradox: the Leggett mass (omega_L1 = 0.070 M_KK) exists only with the pre-transit condensate, but n_s must survive post-transit. Volovik's resolution (S49 wayforward): "Bogoliubov coefficients carry frozen imprint of the pre-transit Leggett gap into the post-transit power spectrum" (Paper 27 methodology).

From S38: P_exc = 1.000, transit is sudden quench. From S49 KZ-3COMPONENT: n = 59.82 pairs created via Landau-Zener. The pair creation spectrum IS a power spectrum — do the Bogoliubov coefficients encode the Leggett mass?

**Method**:
1. Read `tier0-computation/canonical_constants.py`.
2. Read `tier0-computation/s49_leggett_transit.py` and `.npz` for transit dynamics data.
3. Read `tier0-computation/s49_kz_3component.py` and `.npz` for the LZ pair creation data.
4. Read `tier0-computation/s49_dipolar_catalog.py` and `.npz` for the Leggett coupling data.
5. Read Volovik Paper 27 from `researchers/Volovik/` for the Bogoliubov formalism.
6. Compute the Bogoliubov coefficients beta_k for the transit through the BCS condensation region. The pre-transit state has 3 Leggett modes. The sudden quench produces quasiparticles with occupation n_k = |beta_k|^2.
7. Compute the power spectrum P(K) = sum_k |beta_k|^2 delta(K - k). Does it carry an imprint of the Leggett pole structure?
8. If yes, extract n_s and alpha_s from the Bogoliubov spectrum.

**The Deep Question**: The GGE has 8 conserved quantities (Richardson-Gaudin integrals I_alpha). These determine the ENTIRE post-transit state. The question is whether I_alpha "remember" the Leggett mass: I_alpha are determined by the pre-transit BCS ground state → BCS includes J_ij → J_ij determine omega_L → therefore I_alpha → omega_L is a function. But is it DETECTABLE in P(K)?

**Pre-registered gate**: PASS if |beta_k|² encodes Leggett mass. FAIL if featureless (LZ P~1 for all modes).

---

## 3. W1-F: Running Mass from Anomalous Dimension (RUNNING-MASS-50)

**Agent**: landau-condensed-matter-theorist | **Verdict**: FAIL

**Prompt**:

You are computing the running mass m(K) from the anomalous dimension of the fabric order parameter.

**Context**: S49 proved alpha_s = n_s² - 1 = -0.069 is exact for the O-Z propagator with CONSTANT mass. Landau (S49 wayforward) proposes: if the Goldstone mass RUNS with wavevector m(K) ~ K^gamma, the tilt formula changes. The O-Z identity relies on m being K-independent. Running mass modifies:

n_s = 1 - 2m²/(JK² + m²) → n_s = 1 - 2m(K)²/(JK² + m(K)²)

Need gamma > 1.7 for the running to bring alpha_s within 2σ of Planck (shift +0.061 from -0.069 to -0.008).

**Method**:
1. Read `tier0-computation/canonical_constants.py`.
2. Read `tier0-computation/s49_alpha_s_bayes.py` and `.npz`.
3. Construct the GL free energy for the Goldstone field phi on the 32-cell lattice: F[phi] = sum_<ij> J_ij/2 (phi_i - phi_j)² + sum_i m²/2 phi_i² + sum_i lambda/4! phi_i⁴
4. Compute the 1-loop self-energy on the lattice.
5. The running mass is: m(K)² = m_0² + Sigma(K) - Sigma(0). The anomalous dimension is: gamma = d ln m(K) / d ln K.
6. With m(K) running, recompute n_s and alpha_s.
7. Scan lambda over [0.01, 10] to determine: at what coupling does gamma reach 1.7?

**Pre-registered gate**: PASS if gamma > 1.7 AND alpha_s shifts within 2σ Planck. FAIL if gamma < 0.5.

---

## 4. W1-H: Eikonal Damping in Fabric Propagator (EIKONAL-DAMPING-50)

**Agent**: quantum-acoustics-theorist | **Verdict**: FAIL

**Prompt**:

You are computing whether eikonal breakdown (78% of T²) produces physical damping in the fabric propagator.

**Context**: S49 ANALOG-TRAPPED-49 found that 78.3% of T² has Mach > 1 (eikonal breakdown — condensate texture varies faster than phonons can resolve). QA (S49 wayforward): "78% of T² where WKB fails could act as physical damping modifying the propagator." Also: "Modified dispersion from sub-gap proximity (omega_L/2Delta_B3 = 0.41 → anomalous group velocity near band edge)."

From S49: The Mach field is the amplitude gradient, not superflow. But it IS a physical diagnostic: phonons scatter strongly off the condensate texture in these regions. The question: does this scattering produce an imaginary part in the fabric propagator P(K)?

**Method**:
1. Read `tier0-computation/canonical_constants.py`.
2. Read `tier0-computation/s49_analog_trapped.py` and `.npz` for Mach field and condensate texture data.
3. Read `tier0-computation/s49_cavity_resonance.py` and `.npz` for c_BdG and cavity geometry.
4. Compute the phonon self-energy from scattering off the condensate texture. The texture acts as a static potential V(x) = delta_c_s(x) for phonons.
5. The imaginary part Im[Sigma(K)] gives the damping rate Gamma(K). This converts the Goldstone propagator from P(K) = 1/(K² + m²) to P(K) = 1/(K² + m² + i Gamma(K)).
6. If Gamma(K_pivot) comparable to m²: propagator at CMB scales substantially modified.
7. Extract n_s and alpha_s from the damped propagator. Compare to undamped O-Z.

**Pre-registered gate**: PASS if Gamma(K_pivot)/m² > 0.1. FAIL if < 0.01.

---

## 5. W2-A: Anomalous Dispersion on Disordered Fabric (ANOMALOUS-DISPERSION-50)

**Agent**: landau-condensed-matter-theorist | **Verdict**: FAIL

**Prompt**:

You are computing whether the Z_3-disordered Voronoi fabric produces sub-quadratic effective dispersion.

**Context**: The Naz deep-dive discovered that the identity alpha_s = n_s² - 1 is specific to K² dispersion. For P(K) = T/(J·K^alpha + m²):

  alpha_s = -(1 - n_s)(alpha - 1 + n_s)

At alpha = 2: alpha_s = -0.069 (6σ). At alpha = 0.5: alpha_s = +0.019 (1.8σ). The framework needs alpha_eff < 0.55.

Physical mechanisms for alpha < 2:
- Anomalous diffusion from long-range correlated disorder (Lévy flights)
- Non-local stiffness from pair correlations spanning multiple cells (ξ_BCS/l_cell = 5.3)
- Fractional Laplacian from fabric topology (Z_3 domain structure)

**Method**:
1. Read `tier0-computation/canonical_constants.py`.
2. Read `tier0-computation/s49_bragg_goldstone.py` and `.npz` for tessellation geometry.
3. Construct the ACTUAL 32-cell Josephson coupling matrix with Z_3-dependent couplings: same-domain J_C2 = 0.933, cross-domain J_C2 × cos²(2π/3) = J_C2/4. Include J_xy vs J_z anisotropy.
4. Build the 32×32 lattice Green's function. Diagonalize the full Josephson matrix to get phonon band structure.
5. From the band structure, compute effective dispersion alpha_eff(K) = d ln epsilon / d ln K at K_pivot.
6. Also compute: density of states, participation ratio, phonon propagator P(K).
7. From P(K), extract n_s and alpha_s.

**Pre-registered gate**: PASS if alpha_eff(K_pivot) < 0.55. FAIL if > 1.5.

---

## 6. W2-B: Fabric RPA Phonon Propagator (FABRIC-RPA-50)

**Agent**: nazarewicz-nuclear-structure-theorist | **Verdict**: FAIL

**Prompt**:

You are computing the RPA-screened phonon propagator — the nuclear "effective charge" analog.

**Context**: The Naz deep-dive identified g²χ₀ ~ 1.54 as O(1), meaning RPA corrections are significant. Nuclear precedent: effective charges correct transition rates by factors of 2-5 (Paper 07). The Schur Lemma Trap: V(B2,B2) = 0.1557 is k-independent by Schur's lemma, making mean-field featureless. But the RPA vertex correction involves the PAIR SUSCEPTIBILITY χ₀(K,ω), which IS K-dependent because it includes the spatial structure of the Cooper pair wave function across multiple cells.

**Method**:
1. Read `tier0-computation/canonical_constants.py`.
2. Read `sessions/session-50/session-50-naz-deepdive.md` Sections 3.3 and 3.6.
3. Compute the bare pair susceptibility χ₀(K) on the 32-cell fabric: χ₀(K) = sum_{k} F(k,K) / [E(k) + E(k+K)] where F is the pair form factor.
4. Compute the RPA-screened propagator: D_RPA(K) = D₀(K) / [1 - g² · χ₀(K) · D₀(K)]
5. The KEY physics: χ₀(K) is K-dependent because the pair wave function extends over ξ_BCS/l_cell = 5.3 cells. At K·ξ ~ 1, χ₀ develops structure.
6. From D_RPA(K), extract effective J_eff(K) and test whether it introduces K-dependence that breaks K².
7. Extract n_s(RPA) and alpha_s(RPA). Test the identity.

**Pre-registered gate**: PASS if alpha_s(RPA) in [-0.040, 0]. FAIL if identity survives.

---

## 7. W2-C: Spatially-Resolved KZ Pair Creation (KZ-SPATIAL-50)

**Agent**: volovik-superfluid-universe-theorist | **Verdict**: FAIL

**Prompt**:

You are computing whether cell-dependent quench rates produce a red-tilted power spectrum directly from transit dynamics.

**Context**: The Naz deep-dive identified a route that bypasses the propagator entirely: the cosmological power spectrum may come from TRANSIT DYNAMICS, not from an equilibrium correlator. On the 32-cell FABRIC, the quench rate varies cell-to-cell because each cell has different local geometry (size, shape, domain wall proximity). This spatial variation in quench rate produces SPATIALLY CORRELATED density fluctuations.

Nuclear analog (Naz): "In nuclear fission, the post-scission fragment excitation spectrum depends on the trajectory across the barrier."

**Method**:
1. Read `tier0-computation/canonical_constants.py`.
2. Read `tier0-computation/s49_kz_3component.py` and `.npz` for the LZ formula.
3. Read `tier0-computation/s49_bragg_goldstone.py` and `.npz` for tessellation geometry.
4. Assign cell-dependent quench parameters: |dε/dt|_i = v_terminal × |dε/dτ| × (V_avg / V_i)^{1/3}
5. For each cell i and mode k: P_LZ(k, i) = 1 - exp(-π × Δ_k² / |dε_k/dt|_i), then n_pairs(i) = sum_k ρ_k × P_LZ(k, i)
6. Compute power spectrum of density fluctuations: δn(x_i) = n(x_i) - <n>, P(K) = |sum_i δn(x_i) exp(-iK·x_i)|²
7. Extract n_s from P(K).

**Pre-registered gate**: PASS if n_s in [0.950, 0.980]. FAIL if n_s = 1.000 (featureless).

---

## 8. W2-F: sigma_8 from O-Z Rigid Prediction (SIGMA8-OZ-50)

**Agent**: gen-physicist | **Verdict**: PASS

**Prompt**:

You are computing sigma_8 from the rigid O-Z prediction to document the lensing tension.

**Context**: S49 Cosmic-Web warned: "alpha_s = -0.069 → σ_8 shift 21% → already excluded by lensing if O-Z is the full story." This computation checks that claim.

Key parameters: n_s = 0.9649, alpha_s = n_s² - 1 = -0.0688, A_s = 2.1e-9, Ω_m = 0.315.

**Method**:
1. Compute primordial power spectrum with running: P_R(k) = A_s × (k/k_pivot)^{n_s - 1 + (1/2) alpha_s ln(k/k_pivot)}
2. Compute matter power spectrum with transfer function (Eisenstein-Hu or BBKS).
3. Compute σ_8 = sqrt((1/2π²) integral k² P_m(k) W²(kR) dk) with R = 8 h⁻¹ Mpc.
4. Compare: (a) alpha_s = 0 (LCDM), (b) alpha_s = -0.069 (O-Z rigid), (c) alpha_s = -0.038 (S48 lattice).
5. Compute S_8 = σ_8 sqrt(Ω_m/0.3).

**Pre-registered gate**: PASS if σ_8 in [0.740, 0.820]. FAIL if outside [0.640, 0.920].

---

## 9. Naz Deep-Dive (post-Wave 1 review)

**Agent**: nazarewicz-nuclear-structure-theorist | **Output**: session-50-naz-deepdive.md

**Prompt**:

The team-lead is asking you to perform a deep dive, validation, and speculation report on the Wave 1 results. The user is NOT ready to discard O-Z — there was strong prior evidence that it is structural. Your job is to stress-test the FAIL verdicts, look for hidden assumptions, and speculate on what might be missed.

**Section 1: Validation** — For each of the 4 FAIL results:
1. What assumptions went in? Are any questionable?
2. Is the mathematical argument watertight, or does it rely on approximations?
3. What would have to be wrong for the result to change?
4. Nuclear physics sanity check.

**Section 2: What O-Z Got Right** — Review the structural evidence: K^{-2} Goldstone spectrum, fabric texture correlations, Leggett mass at correct scale, phi crossing, parameter-free nature. Is the O-Z FORM wrong, or is the O-Z MASS wrong?

**Section 3: Speculation** — Think like a nuclear theorist confronting a strong experimental signal that the theory predicts wrong. Evaluate:
1. The m² = 140 M_KK² forced by n_s: is this the right mass identification?
2. Non-O-Z functional forms: what propagator forms WOULD break the identity?
3. Scale mapping problem: K_pivot outside BZ?
4. Two-propagator architecture (Tesla S49).
5. Transit dynamics directly: pair creation spectrum IS the power spectrum?
6. Nuclear analogy: wrong transition rate, right level scheme → effective charges?
7. Fabric disorder from Z_3 domain walls.
8. Beyond mean-field: the 29× fluctuation dominance.

**Key discoveries from this prompt**:
- Sub-quadratic dispersion breaks the identity: for P(K) = T/(J K^α + m²), at α = 0.5 → alpha_s = +0.019 (Planck-compatible)
- The Schur Lemma Trap: V(B2,B2) is Casimir, k-independent by construction
- Nuclear "wrong transition rate" precedent: effective charges as the missing correction
- g²χ₀ ~ 1.54 (later corrected to 0.51) suggesting O(1) RPA corrections

---

## Summary: What Each Prompt Tested

| # | Escape Route | Mechanism | Kill Shot |
|:--|:-------------|:----------|:----------|
| 1 | Multi-pole propagator | 3 poles from 3-band Josephson | Poles 99.95% degenerate (m² >> J) |
| 2 | Bogoliubov imprint | Pre-transit Leggett mass → post-transit spectrum | Trans-Planckian erasure (ω_L/ω_transit = 10⁻⁵) |
| 3 | Running mass | m(K) ~ K^γ modifies identity | Structural bound γ < 1-n_s = 0.035 |
| 4 | Eikonal damping | Texture scattering → Im[Σ(K)] | Zero-mode protection (⟨V⟩_{T²} = 0) |
| 5 | Anomalous dispersion | K^α with α < 2 from disorder | Goldstone theorem: α = 2 structural |
| 6 | RPA beyond mean-field | Vertex correction breaks identity | χ₀(K) too flat + mass hierarchy |
| 7 | Transit dynamics | Cell-dependent KZ → spatial P(K) | Sudden-quench universality |
| 8 | sigma_8 viability | Does α_s = -0.069 kill σ_8? | **NO** — σ_8 = 0.799, viable |

**Common root cause**: The mass hierarchy m²/(JK²) ~ 56 at K_pivot. The n_s = 0.965 constraint forces m² so large that ALL K-dependent corrections are parametrically suppressed. The only escape that was tested at the *right level* (changing the exponent, not adding corrections) was W2-A, which was killed by the Goldstone theorem.
