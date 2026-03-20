## III-c. Wave 3: Predictions + Topology (4 tasks, partially depends on W1-5 and W2)

### W3-1: Fisher Forecast for 325 Mpc First-Sound Ring (FIRST-SOUND-44)

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the Fisher forecast for detecting the first-sound ring at 325 Mpc in the DESI DR2 galaxy correlation function. This is the framework's first distinctive LSS prediction and the most important observational test available.

**Context.** S43 KK-CMB-TF-43: first-sound ring at r_1 = 325.3 Mpc, amplitude 20.4% of BAO, +10.6% in xi(r)*r^2. S43 CW-PREREG-43: FIRST-SOUND-XI-44 pre-registered: xi(r) peak at 305-345 Mpc, SNR 2-5 (central 3.4). S43 CC workshop convergence C4: first-sound ring is the framework's most distinctive LSS prediction.

The BAO feature at ~147 Mpc is detected at >10 sigma in current surveys. The first-sound ring at 325 Mpc has amplitude ~20% of BAO, so expected SNR scales as 0.2 * sqrt(V_survey/V_BAO). For DESI DR2 with V_eff ~ 25 Gpc^3, estimate SNR.

**Computation Steps**:

1. **LCDM baseline xi(r).** Compute the LCDM correlation function xi(r) from the matter power spectrum P(k) using the Eisenstein-Hu fitting formula for BAO wiggles. Include the BAO peak at r_BAO = 147.2 Mpc.

2. **Framework xi(r).** Add the first-sound contribution:

   $$\xi_{\text{framework}}(r) = \xi_{\text{LCDM}}(r) + A_1 \cdot \frac{\sin(k_1 r)}{k_1 r} \cdot e^{-\Sigma_1^2 k_1^2 / 2}$$

   where A_1 is the first-sound amplitude (20.4% of BAO), k_1 = 2 pi / r_1, and Sigma_1 is the nonlinear damping scale.

3. **Fisher matrix.** For a galaxy survey with number density n_g and volume V_eff, the Fisher information for A_1:

   $$F_{A_1} = V_{\text{eff}} \int_0^{k_{\max}} \frac{4\pi k^2}{(2\pi)^3} \left[\frac{\partial \ln P(k)}{\partial A_1}\right]^2 \frac{P(k)^2}{[P(k) + 1/n_g]^2} \, dk$$

   Compute with DESI DR2 parameters: V_eff ~ 25 Gpc^3, n_g P ~ 3 (LRG sample).

4. **SNR estimate.** SNR = sqrt(F_{A_1}) * A_1. Report for:
   - DESI DR2 (2025): V ~ 25 Gpc^3
   - DESI complete (2028): V ~ 50 Gpc^3
   - Euclid Y5 (2030): V ~ 100 Gpc^3

5. **Systematics.** Fiber collision scale (~1 Mpc), nonlinear damping at 325 Mpc, reconstruction bias. The first-sound ring is at 325 Mpc, well above the nonlinear scale (~10 Mpc), so systematics should be small.

6. **Alternative: configuration-space test.** Compute the chi^2 difference between LCDM xi(r) and framework xi(r) in the range r = [250, 400] Mpc. Report delta_chi^2 for each survey.

7. **Pre-registration specification.** Define the exact test: "Search for a peak in xi(r)*r^2 at r = 325 +/- 20 Mpc with amplitude A_1 > 0.5 (h^{-1} Mpc)^2 above the smooth LCDM baseline."

**Pre-registered gate FIRST-SOUND-44**:
- PASS: expected SNR > 3 in DESI DR2 (framework prediction is testable NOW)
- FAIL: expected SNR < 1 in Euclid Y5 (prediction requires next-generation surveys)
- INFO: SNR between 1-3 (marginal detection expected)

**Input files**:
- `tier0-computation/s43_kk_cmb_transfer.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- Standard LCDM cosmological parameters

**Output files**:
- Script: `tier0-computation/s44_first_sound_fisher.py`
- Data: `tier0-computation/s44_first_sound_fisher.npz`
- Plot: `tier0-computation/s44_first_sound_fisher.png`

**Working paper section**: W3-1

---

### W3-2: Multi-Wall Bragg Transfer Matrix (COHERENT-WALL-44)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the coherent multi-wall Bragg transfer matrix for KK quasiparticles propagating through 32 KZ domain walls. The 32-cell tessellation creates a periodic potential for quasiparticles, potentially producing Bragg diffraction and band gaps in the 4D propagation spectrum.

**Context.** S43 IMP-FILTER-43: single-wall DR = 2.99 decades (HF + impedance); near arbitrary 3.00 threshold. S43 FANO-CONT-43: Fano q = 1 algebraic identity; zero additional DR from Fano. The single-wall result is marginal. Multi-wall coherent effects may increase the DR through Bragg-type constructive interference of reflected waves.

S43 COHERENT-WALL-44 pre-registered in quicklook: DR > 3 decades at any frequency.

**Computation Steps**:

1. Load impedance data from `tier0-computation/s43_impedance_mismatch.npz` and BdG masses from `tier0-computation/s42_fabric_dispersion.npz`.

2. **Single-wall transfer matrix.** For a domain wall at position x_j with impedance mismatch Z_j, the 2x2 transfer matrix is:

   $$M_j = \frac{1}{2Z_j}\begin{pmatrix} Z_j + Z_{j+1} & Z_j - Z_{j+1} \\ Z_j - Z_{j+1} & Z_j + Z_{j+1} \end{pmatrix} \cdot \begin{pmatrix} e^{ik_j d_j} & 0 \\ 0 & e^{-ik_j d_j} \end{pmatrix}$$

   where d_j is the domain size and k_j = sqrt(omega^2 - m_j^2) is the wavevector in domain j.

3. **Multi-wall transfer matrix.** For 32 domains with random sizes drawn from KZ statistics (mean size L_KZ = xi_KZ = 0.152 M_KK^{-1}, distribution from S43 PAIR-FF-43 tessellation):

   $$M_{\text{total}} = \prod_{j=1}^{32} M_j$$

4. **Transmission coefficient.** T(omega) = 1 / |M_total(1,1)|^2. Compute T(omega) across the full bandwidth [0.8, 2.1] M_KK.

5. **Band structure.** For periodic arrangements (all domains equal size), compute the Bloch band structure. Identify band gaps where T(omega) = 0.

6. **Disorder average.** For the random KZ tessellation, average T(omega) over 1000 realizations. Report the mean transmission and its standard deviation.

7. **Dynamic range.** DR = max_mode T(mode) / min_mode T(mode) across the 8 BdG quasiparticle modes. Report DR for: (a) single wall, (b) 32 walls periodic, (c) 32 walls disordered.

8. **Anderson localization check.** For disordered walls: does T ~ exp(-L/xi_loc) (localization) or T ~ 1/L (diffusive)? Compute the localization length xi_loc from the Lyapunov exponent of M_total.

**Pre-registered gate COHERENT-WALL-44**:
- PASS: DR > 3 decades (log10(T_max/T_min) > 3) for the disordered 32-wall case
- FAIL: DR < 2 decades for all configurations
- INFO: periodic case gives DR > 3 but disordered case gives DR < 3

**Input files**:
- `tier0-computation/s43_impedance_mismatch.npz`
- `tier0-computation/s42_fabric_dispersion.npz`
- `tier0-computation/s42_hauser_feshbach.npz`

**Output files**:
- Script: `tier0-computation/s44_coherent_wall.py`
- Data: `tier0-computation/s44_coherent_wall.npz`
- Plot: `tier0-computation/s44_coherent_wall.png`

**Working paper section**: W3-2

---

### W3-3: N_3 Topological Invariant for BdG Spectrum (N3-BDG-44)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the N_3 topological invariant for the BdG (not D_K) spectrum at the fold. If the BdG spectrum has point nodes with N_3 != 0, Volovik's Fermi-point vacuum energy cancellation applies.

**Context.** S43 CC workshop divergent D4: Volovik proposes N_3 != 0 in BdG spectrum; Hawking predicts FAIL (flat band is Fermi surface not Fermi point). S43 FLATBAND-43: B2 bandwidth = 0 exactly (Schur's lemma on U(2)). Volovik R2 modification: accept flat band is not a Fermi point, but BdG particle-hole crossings may create conical nodes. Target BdG spectrum.

Paper 04 (`researchers/Volovik/04_2008_Volovik_Emergent_Physics_Fermi_Point_Scenario.md`): the N_3 invariant classifies topologically protected point nodes in the Green's function. Near a Fermi point with N_3 = 1, the vacuum energy is EXACTLY zero by topological protection. This is the strongest known cancellation mechanism.

The BdG Hamiltonian has particle-hole symmetry. In a spectrum with particle-hole crossings, conical intersections (Dirac/Weyl points) may form. These have N_3 = +/- 1 and topologically protect the vacuum energy at that point to be zero.

**Computation Steps**:

1. Load BdG data from `tier0-computation/s38_cc_instanton.npz` (BdG amplitudes u_k, v_k) and eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz`.

2. **Construct BdG Hamiltonian.** The BdG Hamiltonian in the quasiparticle basis:

   $$H_{\text{BdG}} = \begin{pmatrix} h(\mathbf{k}) - \mu & \Delta(\mathbf{k}) \\ \Delta^\dagger(\mathbf{k}) & -(h(-\mathbf{k}) - \mu)^T \end{pmatrix}$$

   where h(k) is the single-particle Hamiltonian (from D_K eigenvalues) and Delta(k) is the gap function. For the framework: h = D_K^2 restricted to the 8 gap-edge modes, Delta from the BCS self-consistent solution.

3. **Spectrum of H_BdG.** Compute the BdG eigenvalues E_n(k) as a function of a parameter k that interpolates across the Brillouin zone analog. Since the internal space is compact, k is discrete. Plot the BdG band structure.

4. **Identify point nodes.** Search for values of k where E_n(k) = 0 (zero-energy crossings). At each node, determine whether it is:
   - A conical intersection (Dirac/Weyl point): E ~ |k - k_0|, N_3 = +/- 1
   - A quadratic touching: E ~ |k - k_0|^2, N_3 = 0
   - A flat band crossing: E = 0 over a finite region, N_3 not defined

5. **Compute N_3.** For each identified Fermi point, compute:

   $$N_3 = \frac{1}{24\pi^2} \epsilon^{ijk} \int_{S^2} \text{tr}\left[G \partial_i G^{-1} \cdot G \partial_j G^{-1} \cdot G \partial_k G^{-1}\right] \, d^2S$$

   where G(omega, k) = (i*omega - H_BdG(k))^{-1} is the Green's function and the integral is over a small sphere enclosing the node.

6. **Vacuum energy at Fermi points.** If N_3 != 0: the vacuum energy contribution from modes near the Fermi point is ZERO by topological protection (Paper 04, Section on vacuum energy). Compute the fraction of total GGE energy that is topologically protected.

7. **Report.** Number of Fermi points, N_3 values, fraction of energy protected.

**Pre-registered gate N3-BDG-44**:
- PASS: N_3 != 0 found in BdG spectrum (topological CC suppression applies)
- FAIL: No point nodes, or all nodes have N_3 = 0 (no topological protection)
- INFO: nodes found but N_3 computation ambiguous

**Input files**:
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s35_ed_corrected_dos.npz`
- `researchers/Volovik/04_2008_Volovik_Emergent_Physics_Fermi_Point_Scenario.md`

**Output files**:
- Script: `tier0-computation/s44_n3_bdg.py`
- Data: `tier0-computation/s44_n3_bdg.npz`
- Plot: `tier0-computation/s44_n3_bdg.png`

**Working paper section**: W3-3

---

### W3-4: Tensor-to-Scalar Ratio from BCS First Principles (BCS-TENSOR-R-44)

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are computing the tensor-to-scalar ratio r from BCS dynamics at the fold, confirming the r ~ 10^{-9} prediction from first principles. This is a standing prediction (S43 CC workshop convergence C3) but has not been derived from a single self-contained computation.

**Context.** S43 MOD-REHEAT-43: BCS tensors give r ~ 4e-10. S43 CC workshop C3: "Both derivations give r ~ 4e-10 from BCS gap + M_KK/M_Pl hierarchy. Condensed matter analog (3He-B) confirms suppression (Delta/E_F)^2." The prediction r ~ 10^{-9} is undetectable by LiteBIRD/CMB-S4. r > 10^{-5} excludes framework.

The physical mechanism: tensor perturbations (gravitational waves) are sourced by the stress-energy tensor anisotropy during transit. The BCS condensate has anisotropic stress Delta_T^{ij} ~ Delta_0^2 / E_F. The ratio to scalar perturbations gives r ~ (Delta_0 / E_F)^2 * (M_KK / M_Pl)^2.

**Computation Steps**:

1. Load BCS data from `tier0-computation/s38_cc_instanton.npz`, constants from `tier0-computation/s42_constants_snapshot.npz`.

2. **Scalar power spectrum.** The curvature power spectrum from KZ perturbations:

   $$P_R = \frac{V(\tau_{\text{fold}})}{24\pi^2 M_{\text{Pl}}^4 \epsilon_H}$$

   where V = S_fold * M_KK^4 and epsilon_H ~ 1.4e-6 (BCS-only, S43).

3. **Tensor power spectrum.** Gravitational waves sourced by BCS anisotropic stress:

   $$P_T = \frac{2}{\pi^2} \left(\frac{H}{M_{\text{Pl}}}\right)^2 + P_T^{\text{BCS}}$$

   where the BCS contribution:

   $$P_T^{\text{BCS}} = \frac{4}{\pi^2 M_{\text{Pl}}^4} \cdot |\Delta_0|^4 \cdot N(E_F)^2$$

4. **Tensor-to-scalar ratio.** r = P_T / P_R. Compute from both the standard vacuum contribution (16 epsilon_H) and the BCS source.

5. **3He-B analog.** In superfluid 3He-B, the tensor perturbation analog (transverse sound mode mixing with order parameter oscillations) has amplitude suppressed by (Delta/E_F)^2. Compute this ratio for the framework: Delta_0 = 0.115 M_KK, E_F ~ spectral gap = 0.819 M_KK.

6. **Report.** r from first principles, comparison to BICEP bound (r < 0.036), prediction for LiteBIRD sensitivity (r ~ 10^{-3}).

**Pre-registered gate BCS-TENSOR-R-44**:
- PASS: r in [10^{-15}, 10^{-5}] (consistent with undetectable B-modes)
- FAIL: r > 10^{-3} (detectable, in tension with BICEP if > 0.036)
- INFO: r computed but strong cutoff dependence

**Input files**:
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/s42_gradient_stiffness.npz`

**Output files**:
- Script: `tier0-computation/s44_bcs_tensor_r.py`
- Data: `tier0-computation/s44_bcs_tensor_r.npz`
- Plot: `tier0-computation/s44_bcs_tensor_r.png`

**Working paper section**: W3-4

---
