## III-a. Wave 1: CRITICAL Anchors (5 tasks, parallel)

### W1-1: Sakharov Induced Gravity from 992 KK Modes (SAKHAROV-GN-44)

**Agent**: `volovik-superfluid-universe-theorist`
**Additional Researcher Context** researchers/Quantum-Acoustics/index.md
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the single most diagnostic quantity for the CC problem: G_N from the Sakharov induced gravity formula using the logarithmic functional, compared to G_N from the spectral action polynomial a_2 coefficient.

**Context.** The S43 UV/IR workshop (Volovik+Nazarewicz) established that the 113-order CC gap contains a ~13-order structural contribution from using the wrong functional weighting (polynomial spectral action vs logarithmic Sakharov/trace-log). The spectral action computes G_N from Tr f(D^2/Lambda^2), which weights eigenvalues polynomially through the moment f_2. The Sakharov formula computes G_N from Tr ln(D^2/Lambda^2), which weights eigenvalues logarithmically. In condensed matter (Paper 07, Paper 30), the gravitating quantity is ALWAYS the trace-log functional.

S43 CC workshop convergence D5: if SAKHAROV-GN-44 gives G_N(Sakharov) != G_N(a_2), the discrepancy determines the correct cutoff function f. The Sakharov formula corresponds to f(x) = -ln(x). The spectral action a_2 corresponds to f(x) with moment f_2 = integral x f(x) dx. Matching both determines f(x) up to these constraints.

S43 UV/IR workshop (Volovik R1 Section 2): The BCS free energy is computed from the LOGARITHM of the BdG determinant: F = -(1/2) Tr ln det(H_BdG). The vacuum energy depends logarithmically on Lambda/Delta, not as Lambda^4. The Sakharov weighting gives ~8 orders less per mode than the polynomial weighting. S43 UV/IR workshop (Volovik R2): corrected accounting gives ~13 total orders from functional form change, leaving ~100 orders unidentified.

S43 CC workshop emerged insight E2: S_F^Connes = 0 (BDI symmetry) means the fermionic spectral action vanishes identically. G_N comes from the bosonic part only. The Sakharov formula using the FULL spectrum (bosonic + fermionic) provides an independent test.

S43 CC workshop emerged insight E4: if SAKHAROV-GN-44 and INDUCED-G-44 (W4-2) agree, the cutoff function f is self-consistently determined.

**Computation Steps**:

1. Load the full KK spectrum from `tier0-computation/s42_hauser_feshbach.npz` (992 eigenvalues lambda_k with sector labels and multiplicities) and from `tier0-computation/s42_constants_snapshot.npz` (M_KK routes, a_2 coefficient, G_N extraction).

2. **Sakharov formula for G_N.** Following Paper 07 (`researchers/Volovik/07_1994_Volovik_Induced_Gravity_3He_A_BCS.md`) and Paper 30 (`researchers/Volovik/30_2022_Volovik_Newton_Constant_Planck_Length.md`):

   $$\frac{1}{16\pi G_N^{\text{Sak}}} = \frac{1}{2} \sum_{k=1}^{992} d_k \cdot \ln\left(\frac{\Lambda^2}{\lambda_k^2}\right)$$

   where d_k is the multiplicity (dimension of the representation squared) and Lambda is the UV cutoff. Compute for Lambda = M_Pl and Lambda = 10*M_KK and Lambda = 100*M_KK. Report cutoff dependence.

3. **Spectral action a_2 formula for G_N.** From S42 CONST-FREEZE-42:

   $$\frac{1}{16\pi G_N^{\text{spec}}} = f_2 \cdot \Lambda^2 \cdot a_2$$

   where a_2 = sum_k d_k / lambda_k^2 is the second Seeley-DeWitt coefficient and f_2 is the second moment of the cutoff function f. Extract the G_N already computed in `s42_constants_snapshot.npz` (gravity route: M_KK = 7.4e16 GeV).

4. **Compute the ratio.** R = G_N^{spec} / G_N^{Sak}. This ratio directly measures the overestimate from the polynomial weighting. Report log10(R).

5. **Physical G_N comparison.** Compare both G_N values to G_N^{obs} = 6.674e-11 m^3 kg^{-1} s^{-2}. Which is closer? By how many orders?

6. **CC implication.** If the Sakharov G_N is correct, the vacuum energy density computed from the trace-log is:

   $$\rho_{\text{vac}}^{\text{log}} = \frac{1}{2} \sum_k d_k \cdot \lambda_k^4 \cdot \ln\left(\frac{\Lambda^2}{\lambda_k^2}\right)$$

   Compare to the spectral action vacuum energy rho_vac^{poly} = f_0 Lambda^4 a_0. Report the ratio and the implied CC reduction in orders of magnitude.

7. **Cutoff function constraint.** If both formulae give the same G_N (R ~ 1), extract the implied f_2 and f_0. Report whether a positive, decreasing function f exists with these moments (Hausdorff moment problem test).

8. **Cross-check with BCS condensation energy.** The BCS free energy from the trace-log is:

   $$\Delta F_{\text{BCS}} = -\frac{1}{2} N(E_F) \Delta^2 \sim -6.6 \text{ (spectral units)}$$

   Compare to Delta_S = 5522. This ratio (Section 5, UV/IR workshop Volovik R2) should be ~836 (~3 orders).

**Pre-registered gate SAKHAROV-GN-44**:
- PASS: G_N^{Sakharov} within factor 100 of G_N^{obs} (2 OOM)
- FAIL: G_N^{Sakharov} > 1000x from G_N^{obs} (> 3 OOM off)
- BONUS: if |log10(G_N^{Sak}/G_N^{spec})| < 1, the two functionals agree and f is constrained

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz` — full 992-eigenvalue spectrum
- `tier0-computation/s42_constants_snapshot.npz` — M_KK, a_2, G_N extraction
- `tier0-computation/s36_sfull_tau_stabilization.npz` — S_full(tau), S_fold
- `researchers/Volovik/07_1994_Volovik_Induced_Gravity_3He_A_BCS.md`
- `researchers/Volovik/30_2022_Volovik_Newton_Constant_Planck_Length.md`
- `researchers/Volovik/05_2005_Volovik_Vacuum_Energy_Cosmological_Constant.md`

**Output files**:
- Script: `tier0-computation/s44_sakharov_gn.py`
- Data: `tier0-computation/s44_sakharov_gn.npz`
- Plot: `tier0-computation/s44_sakharov_gn.png`

**Working paper section**: W1-1

**Critical notes**:
- Read ALL three Volovik papers FIRST. Paper 07 gives the Sakharov formula for induced gravity in 3He-A. Paper 30 gives G_N ~ Delta^2/rho_0 in superfluid vacuum. Paper 05 gives the Gibbs-Duhem identity.
- The cutoff Lambda is the CRITICAL parameter. The Sakharov formula is LOGARITHMIC in Lambda, so G_N depends only weakly on the cutoff. The spectral action is polynomial (f_2 Lambda^2), so G_N depends strongly on Lambda. Report G_N at 3 different cutoffs.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
- Report ALL intermediate numbers. This is the session's anchor computation.

---

### W1-2: CDM by Construction — Formal Proof and Downstream (CDM-CONSTRUCT-44)

**Agent**: `volovik-superfluid-universe-theorist`
**Additional Researcher Context** researchers/Cosmic-Web/index.md
**Model**: opus
**Cost**: LOW

**Prompt**:

You are formalizing the CDM-CONSTRUCT-43 proof (post-workshop addendum to S43 quicklook) that GGE quasiparticles have T^{0i}_4D = 0 identically, making the framework's dark matter CDM by construction. This supersedes CDM-RETRACTION-44 and FLAT-DM-44 entirely.

**Context.** CDM-CONSTRUCT-43 (S43 quicklook addendum): Five-part proof that GGE modes carry energy but not 4D momentum. Both S42 (lambda_fs = 3.1e-48 Mpc) and S43 W2-1 (lambda_fs = 89 Mpc) committed category errors: S42 applied 4D dispersion E(p) = sqrt(m^2+p^2) to internal modes; S43 converted internal c_q = 210 M_KK to 4D velocity, getting c_q_4D = 1.28c (superluminal = category error).

The five parts: (1) KK decomposition phi(x,y) = sum psi_n(x) Y_n(y) gives T^{0i} = 0 for homogeneous modes. (2) Group velocity v_g = k_4D/omega = 0 because modes are created at k_4D = 0 (Schwinger pair creation). (3) Domain wall upper bound v_eff = 2.37e-6 c (400x below CDM/HDM threshold). (4) Two-fluid model inapplicable (v_g = 0 in 4D). (5) Internal temperatures are NOT 4D thermal velocities.

This computation formalizes the proof, examines domain wall corrections, and maps downstream impacts.

**Computation Steps**:

1. Load GGE data from `tier0-computation/s42_gge_energy.npz`, domain wall profile from `tier0-computation/s43_pair_form_factor.npz`, and eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz`.

2. **T^{mu nu} from KK reduction.** Write the 4D stress-energy tensor from integrating the higher-dimensional T^{MN} over the SU(3) fiber:

   $$T^{\mu\nu}_{4D} = \int_K T^{\mu\nu}[\phi] \, dV_K$$

   For a GGE state |{n_k}> (product state in internal quantum numbers), show T^{0i} = 0 algebraically.

3. **Domain wall correction.** At a KZ domain boundary with delta_tau ~ 10^{-6}, the gradient in tau creates an effective 4D momentum. Compute:

   $$v_{\text{eff}} = \frac{\delta\tau \cdot |d\lambda/d\tau|_{\text{max}}}{\lambda_{\text{min}}} \leq 2.37 \times 10^{-6} \, c$$

   Verify this is well below the CDM/HDM threshold (10^{-3} c for z ~ 10^4 decoupling).

4. **Gravitational scattering cross-section.** GGE modes couple to gravity through their energy density. Compute the gravitational scattering cross-section sigma_grav = G_N^2 m^4 / (4 pi) and verify sigma/m << any observational bound.

5. **Self-interaction.** CDM self-interaction: the only inter-cell coupling is through the tau-field gradient (effacement). Compute sigma_self/m from the spectral action's tau-tau-BdG vertex.

6. **Downstream impacts.** List ALL computations that used lambda_fs or v_fs as input and state whether they are superseded:
   - S42 lambda_fs = 3.1e-48 Mpc: SUPERSEDED (category error)
   - S43 lambda_fs = 89 Mpc: SUPERSEDED (category error)
   - S43 CC workshop C2 (mixed B2/B1 CDM/HDM): DISSOLVED (all branches CDM)
   - FLAT-DM-44: DISSOLVED
   - CDM-RETRACTION-44: SUPERSEDED

**Pre-registered gate CDM-CONSTRUCT-44**:
- PASS: T^{0i} = 0 proven algebraically for general GGE state. v_eff < 10^{-3} c at domain walls.
- FAIL: Non-zero T^{0i} from inter-sector coupling or domain wall effects exceeds 10^{-3} c.

**Input files**:
- `tier0-computation/s42_gge_energy.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s43_pair_form_factor.npz`
- `tier0-computation/s43_cdm_category.npz`

**Output files**:
- Script: `tier0-computation/s44_cdm_construct.py`
- Data: `tier0-computation/s44_cdm_construct.npz`
- Plot: `tier0-computation/s44_cdm_construct.png`

**Working paper section**: W1-2

---

### W1-3: Lifshitz Anomalous Dimension for n_s (LIFSHITZ-ETA-44)

**Agent**: `landau-condensed-matter-theorist`
**Additional Researcher Context** researchers/Volovik/index.md
**Model**: opus
**Cost**: HIGH

**Prompt**:

You are computing the anomalous dimension eta at the Type I Lifshitz transition on SU(3), which determines the spectral tilt n_s. This is one of two surviving routes to n_s (the other is spectral dimension flow, DIMFLOW-44 in W2).

**Context.** S43 LIFSHITZ-43: Type I Lifshitz transition uniquely identified. N_eff jump 32 to 240 at tau=0. Naive KZ gives n_s = 1.50 (blue, wrong). Tesla's transfer function (S43 KZ-NS-43) gives n_s = 0.9649, but this was INPUT (epsilon_H = 0.0176 assumed). The actual tilt mechanism is unidentified.

S43 CC workshop divergent D2: Lifshitz eta vs spectral dimension flow. Volovik proposes eta from Type I transition universality class. Hawking proposes d_s(tau) flow. Concern (Hawking R2): eta at tau=0 (round SU(3)) may be trivially zero because the perturbation spectrum is frozen by sudden quench.

S43 CC workshop emerged E5: does eta depend on the PRE-transition state (tau < 0, nonexistent) or the TRANSITION POINT itself (tau = 0)? If eta is a critical exponent, it depends only on universality class. If it requires van Hove singularities (which appear only at tau > 0), then eta(0) = 0.

Key question: the fold is NOT a standard Lifshitz transition in a crystal. It is a transition in the INTERNAL geometry of a compact manifold. The Fermi surface topology changes from 0 to 32 pockets. Standard Lifshitz universality (z_Lifshitz, nu, eta) may not apply because the "momentum space" is the representation lattice of SU(3), not R^d.

S43 BCS-CLASS-43: 3D Ising universality (Z_2, nu=0.6301, z=2.024). But this is the BCS universality class, which determines the ORDER PARAMETER dynamics. The perturbation spectrum tilt depends on a DIFFERENT universality class: the Lifshitz transition itself.

**Computation Steps**:

1. Load eigenvalue data from `tier0-computation/s41_spectral_refinement.npz`, `tier0-computation/s36_sfull_tau_stabilization.npz`, and BCS data from `tier0-computation/s36_mmax_authoritative.npz`.

2. **Lifshitz anomalous dimension from van Hove scaling.** At the Type I Lifshitz transition, the DOS scales as N(E) ~ |E-E_c|^{(d-2)/2} in d dimensions. For the framework, the effective dimensionality d_eff at the transition point determines eta. The internal space is SU(3) (8-dimensional manifold), but the transition occurs along the 1-dimensional Jensen direction. Compute N(E) near E_c at tau = 0:

   $$N(E) \sim |E - E_c|^{\gamma}, \quad \gamma = \frac{d_{\text{eff}} - 2}{2}$$

   Extract d_eff from the exponent gamma. From S43 DOS-43: 13 van Hove singularities, all optical.

3. **Anomalous dimension at tau=0.** At the round metric (tau=0), all eigenvalues have maximal degeneracy (SU(3) symmetry). The Lifshitz transition occurs as tau increases from 0. Compute eta at tau=0 from:

   $$\eta = 2 - d_{\text{eff}} + 2\gamma$$

   where gamma is from step 2.

4. **Anomalous dimension at tau=fold.** Repeat the computation at tau = 0.190. Compare eta(0) and eta(fold).

5. **n_s from Lifshitz eta.** The spectral tilt from a Lifshitz transition is (Volovik Paper 24):

   $$n_s - 1 = -\eta_{\text{eff}}$$

   where eta_eff accounts for the transfer function from KK to CMB scales. Compute eta_eff at both tau=0 and tau=fold.

6. **Van Hove singularity contribution.** S43 DOS-43 identified 13 van Hove singularities. Near each singularity, N(E) has a specific power-law. Compute the integrated tilt contribution from summing over all singularities.

7. **Comparison to Planck.** Report n_s and compare to n_s = 0.9649 +/- 0.0042.

8. **UNIFICATION GATE preparation.** Report eta_eff and n_s in a format that DIMFLOW-44 (W2-2) can compare against. The unification gate: |n_s(LIFSHITZ) - n_s(DIMFLOW)| < 0.005.

**Pre-registered gate LIFSHITZ-ETA-44**:
- PASS: eta_eff in [0.025, 0.045], giving n_s in [0.955, 0.975]
- FAIL: eta_eff = 0 at tau=0 (trivially vanishing) or eta_eff > 0.1 (too red)
- INFO: eta_eff computed but regime of validity unclear

**Input files**:
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `tier0-computation/s36_mmax_authoritative.npz`
- `tier0-computation/s43_phonon_dos.npz`
- `tier0-computation/s43_lifshitz_class.npz`
- `researchers/Volovik/24_2016_Volovik_Zhang_Type_II_Weyl_Lifshitz_Transition.md`
- `researchers/Volovik/33_2017_Volovik_Exotic_Lifshitz_Transitions_Topological_Materials.md`

**Output files**:
- Script: `tier0-computation/s44_lifshitz_eta.py`
- Data: `tier0-computation/s44_lifshitz_eta.npz`
- Plot: `tier0-computation/s44_lifshitz_eta.png`

**Working paper section**: W1-3

---

### W1-4: Trace-Log CC from BdG Determinant (TRACE-LOG-CC-44)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Additional Researcher Context** researchers/Spectral-Geometry/index.md
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the vacuum energy density from the trace-log functional Tr ln(D_BdG^2/Lambda^2), which is the correct gravitating functional according to the S43 UV/IR workshop consensus. This replaces the polynomial spectral action for CC estimation.

**Context.** S43 UV/IR workshop (Volovik R1 Section 2): "In condensed matter, the gravitating quantity is ALWAYS the trace-log functional, never a polynomial in the spectrum." The BCS free energy is F = -(1/beta) Tr ln det(H_BdG). At T=0: F = -(1/2) sum_k (E_k - |xi_k|). This is LOGARITHMIC in the cutoff, not polynomial.

S43 UV/IR workshop corrected accounting (Volovik R2): equilibrium subtraction gives 1.66 orders, wrong weighting gives ~8 orders, sign cancellations give ~3 orders, total ~13 orders. Remaining ~100 orders unidentified.

S43 E-vs-F audit: the spectral action S(tau) was used as rho_grav in 9 instances. The correct gravitating quantity is the internal energy E, not the free energy F or the spectral action S. The Legendre transform E = F + TS gives E > F > 0, making the CC WORSE if naively applied. The trace-log functional is different: it gives the EXACT one-loop effective potential, which includes all sign cancellations.

S43 UV/IR workshop (Nazarewicz R1 Section 5): Delta F_BCS ~ -(1/2) N(E_F) Delta^2 ~ -6.6 (spectral units) vs Delta_S = 5522. Ratio ~836 (~3 orders). But this is equilibrium; the GGE perturbation at the fold is not equilibrium.

**Computation Steps**:

1. Load eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz` (992 eigenvalues at fold with multiplicities), BCS data from `tier0-computation/s38_cc_instanton.npz` (gap, BdG amplitudes), and GGE data from `tier0-computation/s42_gge_energy.npz`.

2. **BdG spectrum at the fold.** Construct the BdG quasiparticle energies E_k = sqrt(xi_k^2 + Delta_k^2) for all 992 modes, where xi_k = lambda_k - mu (with mu=0, S34) and Delta_k is the BCS gap for each mode (from the self-consistent gap equation, or approximated as Delta_k = Delta_0 * V_kk' for modes near E_F and 0 otherwise).

3. **Trace-log vacuum energy (paired state).** The one-loop effective potential:

   $$\rho_{\text{vac}}^{\text{log}} = -\frac{1}{2} \sum_k d_k \left[ E_k - |\xi_k| - \frac{\Delta_k^2}{2|\xi_k|} + \ldots \right]$$

   For the FULL trace-log (not the weak-coupling expansion):

   $$\rho_{\text{vac}}^{\text{log}} = \frac{1}{2} \sum_k d_k \left[ \xi_k - E_k \right] + \frac{|\Delta_0|^2}{V_{\text{eff}}}$$

   where V_eff is the effective pairing interaction.

4. **Trace-log vacuum energy (unpaired reference state).** The normal state (Delta=0) has:

   $$\rho_{\text{vac},0}^{\text{log}} = \frac{1}{2} \sum_k d_k \, |\xi_k|$$

   The DIFFERENCE is the condensation energy.

5. **Subtract equilibrium.** Following Paper 05 (Gibbs-Duhem): the equilibrium energy does not gravitate. Compute:

   $$\rho_{\text{residual}} = \rho_{\text{vac}}^{\text{log}}(\text{GGE}) - \rho_{\text{vac}}^{\text{log}}(\text{equilibrium})$$

   where the GGE state has the 59.8 quasiparticle pairs with energies from `s42_gge_energy.npz`.

6. **Compare to spectral action CC.** Report:
   - rho_vac^{poly} = Delta_S * M_KK^4 / (16 pi^2) (spectral action, S43)
   - rho_vac^{log} from step 3
   - rho_residual from step 5
   - Ratio R_CC = log10(rho_residual / rho_obs) where rho_obs = 2.3e-47 GeV^4

7. **Strutinsky decomposition.** Following S43 UV/IR workshop (Nazarewicz R1 Section 2c): decompose rho_vac^{log} into smooth (Strutinsky-averaged) and oscillating (shell correction) parts. Report each.

8. **Report the irreducible CC gap.** After trace-log replacement AND equilibrium subtraction, how many orders remain?

**Pre-registered gate TRACE-LOG-CC-44**:
- PASS: rho_residual < 10^{-6} * rho_vac^{poly} (>6 orders of reduction)
- FAIL: rho_residual > 0.1 * rho_vac^{poly} (<1 order of reduction)
- INFO: intermediate result with quantified gap

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/s42_gge_energy.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `researchers/Volovik/05_2005_Volovik_Vacuum_Energy_Cosmological_Constant.md`

**Output files**:
- Script: `tier0-computation/s44_tracelog_cc.py`
- Data: `tier0-computation/s44_tracelog_cc.npz`
- Plot: `tier0-computation/s44_tracelog_cc.png`

**Working paper section**: W1-4

---

### W1-5: First-Sound Imprint Mechanism (FIRST-SOUND-IMPRINT-44)

**Agent**: `quantum-acoustics-theorist`
**Additional Researcher Context** researchers/Volovik/index.md
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the physical mechanism by which internal first sound (c_1 = c) in the phononic substrate imprints on the 4D matter power spectrum P(k), producing the predicted 325 Mpc feature.

**Context.** S43 THERM-COND-43: fabric has second sound u_2 = c/sqrt(3) (ballistic, no Umklapp). S43 KK-CMB-TF-43: first-sound ring at r_1 = 325.3 Mpc, amplitude 20.4% of BAO. S43 CC workshop convergence C4: first-sound ring is the framework's most distinctive LSS prediction. Steinhauer BEC analog confirms two-speed systems produce two correlation peaks. r_1/r_BAO = 2.21 from two-fluid formula.

The key question this computation answers: HOW does the internal first sound at c_1 = c couple to the 4D spatial correlation function xi(r)? The internal sound propagates in the SU(3) fiber. The 4D correlation must come from the modulation of the spectral action by the internal acoustic mode, which affects the 4D expansion rate and hence the BAO processing.

S43 CW-PREREG-43: FIRST-SOUND-XI-44 pre-registered: xi(r) peak at 305-345 Mpc, SNR 2-5.

**Computation Steps**:

1. Load spectral action data from `tier0-computation/s42_gradient_stiffness.npz`, acoustic metric from `tier0-computation/s43_acoustic_metric.npz` (if available, otherwise compute from s43 results), and BAO data from standard LCDM cosmology.

2. **Two-sound system.** The fabric has two acoustic speeds:
   - First sound: c_1 = c (propagation speed in the substrate)
   - Second sound: c_2 = c/sqrt(3) (BAO analog, from two-fluid formula)

   The ratio c_1/c_2 = sqrt(3) gives the ring separation: r_1/r_BAO = sqrt(3) * (correction factors from damping and acoustic processing).

3. **Coupling mechanism.** The internal first sound modulates the spectral action through the eigenvalue dependence on the acoustic displacement field. Compute:

   $$\frac{\delta S}{\delta u_{\text{acoustic}}} = \sum_k d_k \cdot \frac{d\lambda_k}{d\tau} \cdot \frac{d\tau}{du}$$

   where u is the acoustic displacement in the internal space.

4. **4D power spectrum imprint.** The first-sound modulation creates a 4D density perturbation:

   $$\frac{\delta\rho}{\delta u} = \frac{dS}{d\tau} \cdot \frac{d\tau}{du} \cdot M_{\text{KK}}^4$$

   This contributes to P(k) at k_1 = 2 pi / r_1 = 2 pi / 325 Mpc.

5. **Amplitude.** Compute the amplitude of the first-sound peak relative to the BAO peak. S43 KK-CMB-TF-43 found 20.4% of BAO. Verify from first principles.

6. **Damping.** First sound has a different damping scale than second sound. Compute the Silk damping analog for first-sound modes. Report the damping ratio and whether the 325 Mpc feature survives.

7. **Report.** The first-sound mechanism, amplitude, damping, and whether the feature is observable.

**Pre-registered gate FIRST-SOUND-IMPRINT-44**:
- PASS: Physical mechanism identified AND amplitude consistent with 10-30% of BAO
- FAIL: No coupling mechanism exists OR amplitude < 1% of BAO
- INFO: mechanism exists but amplitude uncertain

**Input files**:
- `tier0-computation/s42_gradient_stiffness.npz`
- `tier0-computation/s43_thermal_conductivity.npz`
- `tier0-computation/s43_kk_cmb_transfer.npz`
- `tier0-computation/s42_constants_snapshot.npz`

**Output files**:
- Script: `tier0-computation/s44_first_sound_imprint.py`
- Data: `tier0-computation/s44_first_sound_imprint.npz`
- Plot: `tier0-computation/s44_first_sound_imprint.png`

**Working paper section**: W1-5

---
