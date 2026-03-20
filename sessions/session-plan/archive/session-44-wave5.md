## III-e. Wave 5: Medium-Priority (6 tasks, parallel)

### W5-1: Jacobson Mapping for GGE (JACOBSON-SPEC-44)

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the gravitating energy density from the Jacobson thermodynamic derivation of Einstein's equations, applied to the GGE relic. Jacobson (1995) derived G_mu_nu = 8 pi G T_mu_nu from delta Q = T dS on local Rindler horizons. For the GGE with 8 conserved charges, the first law becomes delta Q = sum_k T_k dS_k.

**Context.** S43 CC workshop emerged E3: "Multi-temperature Jacobson equation for GGE. The correct first law is delta Q = sum_k T_k dS_k. This naturally produces an 8-fluid cosmology." S43 FIRSTLAW-43 PASS: verified to 1.26e-7 fractional deviation with 4-order effacement hierarchy.

The Jacobson approach gives rho_grav as the heat flux through a Rindler horizon, NOT as the absolute spectral action value. This is independent of the functional-form debate (polynomial vs logarithmic).

**Computation Steps**:

1. Load GGE temperatures from `tier0-computation/s43_gge_temp.npz` (T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178) and entropy data from `tier0-computation/s43_gsl_transit.npz`.

2. **Jacobson heat flux.** At a local Rindler horizon with acceleration a:

   $$\delta Q = a \cdot \delta A / (8\pi G_N) = T_U \cdot \delta S$$

   where T_U = a/(2 pi) is the Unruh temperature. For the GGE:

   $$\delta Q = \sum_k T_k \cdot \delta S_k$$

3. **Gravitating energy density.** From Jacobson's derivation:

   $$\rho_{\text{Jacobson}} = \frac{1}{8\pi G_N} \sum_k T_k \frac{dS_k}{d\ln a}$$

   Compute using the GGE mode temperatures and the entropy gradients from FIRSTLAW-43.

4. **Comparison.** Report:
   - rho_Jacobson
   - rho_spectral (S_fold * M_KK^4)
   - rho_obs = 2.3e-47 GeV^4
   - log10(rho_Jacobson / rho_obs)

5. **8-fluid equation of state.** Each GGE sector k has its own w_k = P_k / rho_k. Compute w_k for B2, B1, B3. The total w = sum_k f_k w_k where f_k = rho_k / rho_total.

**Pre-registered gate JACOBSON-SPEC-44**:
- PASS: rho_Jacobson within 30 OOM of Lambda_obs
- FAIL: rho_Jacobson > 10^{60} * Lambda_obs (no improvement over spectral action)
- INFO: intermediate

**Input files**:
- `tier0-computation/s43_gge_temp.npz`
- `tier0-computation/s43_gsl_transit.npz`
- `tier0-computation/s43_first_law.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `researchers/Hawking/17_2019_Jacobson_Thermodynamic_Einstein_Equation.md`

**Output files**:
- Script: `tier0-computation/s44_jacobson_spec.py`
- Data: `tier0-computation/s44_jacobson_spec.npz`
- Plot: `tier0-computation/s44_jacobson_spec.png`

**Working paper section**: W5-1

---

### W5-2: f_NL from Voronoi Initial Conditions (VORONOI-FNL-44)

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the non-Gaussianity parameter f_NL produced by Voronoi tessellation initial conditions at large angular scales (l < 30). S43 established that the tessellation boundary network percolates on any spherical shell. If the CMB pattern at large angles reflects the Voronoi structure, f_NL must satisfy the Planck bound |f_NL| < 5.

**Context.** S43 CC workshop convergence C7: "CMB-as-Voronoi requires reinterpretation. Percolation kills naive identification. Voronoi structure sets large-angle initial conditions (l < 10) only." S43 MOD-REHEAT-43: modulated reheating gives f_NL = 18.4, FAILS Planck. But Voronoi ICs at l < 30 are different from modulated reheating at all scales.

**Computation Steps**:

1. **Generate Voronoi tessellation on S^2.** Place 32 random points on a sphere (representing KZ domain centers). Construct the Voronoi tessellation.

2. **CMB-like map.** Assign temperature T = T_mean * (1 + delta_T) where delta_T depends on the local Voronoi cell: delta_T ~ delta_tau/tau ~ 1.75e-6 (from HOMOG-42) at cell boundaries and ~0 at cell centers.

3. **Angular power spectrum.** Compute C_l from the Voronoi map for l = 2 to 100. Compare to Planck LCDM C_l.

4. **Bispectrum.** Compute the angular bispectrum B_{l1,l2,l3} from the Voronoi map. Extract f_NL using the KSW estimator:

   $$f_{\text{NL}} = \frac{\sum_{l_1 l_2 l_3} B^{\text{obs}}_{l_1 l_2 l_3} B^{\text{template}}_{l_1 l_2 l_3} / C_{l_1} C_{l_2} C_{l_3}}{\sum_{l_1 l_2 l_3} (B^{\text{template}}_{l_1 l_2 l_3})^2 / C_{l_1} C_{l_2} C_{l_3}}$$

5. **Average over tessellation realizations.** Generate 100 random 32-cell tessellations. Compute mean and variance of f_NL.

6. **Report.** f_NL from Voronoi ICs, comparison to Planck bound, impact on CMB-as-Voronoi hypothesis.

**Pre-registered gate VORONOI-FNL-44**:
- PASS: |f_NL| < 5 (Planck bound satisfied)
- FAIL: |f_NL| > 5 (Voronoi ICs at l < 30 excluded)
- INFO: f_NL computed but dominated by cosmic variance

**Input files**:
- `tier0-computation/s42_homogeneity.npz` (delta_tau/tau)
- Standard Planck LCDM C_l

**Output files**:
- Script: `tier0-computation/s44_voronoi_fnl.py`
- Data: `tier0-computation/s44_voronoi_fnl.npz`
- Plot: `tier0-computation/s44_voronoi_fnl.png`

**Working paper section**: W5-2

---

### W5-3: Phonon DOS at 5 tau Values Across Transit (DOS-TAU-44)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM (eigenvalue computation at 5 tau points)

**Prompt**:

You are computing the phonon density of states at 5 tau values across the transit [0.00, 0.05, 0.10, 0.15, 0.19] to track how van Hove singularities evolve. This feeds the n_s computation (LIFSHITZ-ETA-44) and the Strutinsky diagnostic (STRUTINSKY-DIAG-44).

**Computation Steps**:

1. Use `tier0-computation/tier1_dirac_spectrum.py` to compute D_K eigenvalues at tau = 0.00, 0.05, 0.10, 0.15, 0.19 for sectors up to max_pq_sum = 6. (~8.7s per tau per sector, ~5 min total.)

2. Construct multiplicity-weighted histogram rho(omega, tau) at each tau with bins 0.02 M_KK.

3. Track van Hove singularity positions through the transit. At tau=0 (round SU(3)): maximal degeneracy, fewest singularities. As tau increases: symmetry breaking lifts degeneracies, creating new singularities.

4. Report: singularity positions vs tau, DOS bandwidth vs tau, spectral gap vs tau.

**Pre-registered gate DOS-TAU-44**: INFO (diagnostic, feeds LIFSHITZ-ETA-44 and STRUTINSKY-DIAG-44).

**Input files**:
- `tier0-computation/tier1_dirac_spectrum.py`
- `tier0-computation/s43_phonon_dos.npz`

**Output files**:
- Script: `tier0-computation/s44_dos_tau.py`
- Data: `tier0-computation/s44_dos_tau.npz`
- Plot: `tier0-computation/s44_dos_tau.png`

**Working paper section**: W5-3

---

### W5-4: FRG Pilot for 3-Sector System (FRG-PILOT-44)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: HIGH

**Prompt**:

You are implementing a pilot functional renormalization group (FRG) flow for the 3-sector (B1/B2/B3) BCS system, testing whether the FRG effective action deviates from the heat kernel expansion.

**Context.** S43 UV/IR workshop (Nazarewicz R1 recommendation 3): "Formulate the FRG flow for the spectral action. The Wetterauth effective average action Gamma_k interpolates continuously between the microscopic action (k = Lambda) and the full quantum effective action (k = 0). No expansion in a small parameter is required."

The FRG flow equation (exact):

$$\partial_t \Gamma_k = \frac{1}{2} \text{Tr}\left[(\Gamma_k^{(2)} + R_k)^{-1} \partial_t R_k\right]$$

where t = ln(k/Lambda), Gamma_k^{(2)} is the second functional derivative, and R_k is the regulator. For the 3-sector system with 8 gap-edge modes (4 B2, 1 B1, 3 B3), this reduces to an 8x8 flow equation.

**Computation Steps**:

1. Load gap-edge eigenvalues from `tier0-computation/s36_mmax_authoritative.npz` and BCS data from `tier0-computation/s38_cc_instanton.npz`.

2. **Truncation.** Restrict to the 8 gap-edge modes. The effective action:

   $$\Gamma_k = \sum_{i=1}^{8} Z_i(k) \xi_i^2 + \sum_{i<j} V_{ij}(k) \xi_i \xi_j + \Delta(k) \sum_{\langle ij\rangle} \xi_i \xi_j$$

   where Z_i are wavefunction renormalization factors, V_ij are effective interactions, and Delta is the BCS gap.

3. **Regulator.** Use the Litim optimized regulator: R_k(p) = (k^2 - p^2) theta(k^2 - p^2).

4. **Flow.** Integrate from k = Lambda_max (above all eigenvalues) down to k = 0. At each step, update Z_i, V_ij, Delta.

5. **Compare to heat kernel.** At k = 0, the FRG gives the full effective action Gamma_0. Compare:
   - Gamma_0(FRG) vs S_fold(heat kernel)
   - Delta_Gamma/Gamma = |Gamma_0 - S_fold| / S_fold

6. **Report.** Deviation, flow trajectory, fixed points if any.

**Pre-registered gate FRG-PILOT-44**:
- PASS: > 10% deviation from heat kernel (FRG reveals non-perturbative structure)
- FAIL: < 1% deviation (heat kernel is adequate despite UV/IR workshop concerns)
- INFO: intermediate

**Input files**:
- `tier0-computation/s36_mmax_authoritative.npz`
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/s42_hauser_feshbach.npz`

**Output files**:
- Script: `tier0-computation/s44_frg_pilot.py`
- Data: `tier0-computation/s44_frg_pilot.npz`
- Plot: `tier0-computation/s44_frg_pilot.png`

**Working paper section**: W5-4

---

### W5-5: Constrain Cutoff Function f from Sakharov + a_2 (CUTOFF-F-44)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW (depends on W1-1 output)

**Prompt**:

You are constraining the spectral action cutoff function f by requiring consistency between the Sakharov formula and the spectral action a_2 coefficient for G_N. This uses the output of SAKHAROV-GN-44 (W1-1).

**Context.** S43 CC workshop emerged E4: if SAKHAROV-GN-44 gives G_N(Sakharov) != G_N(a_2), the discrepancy determines the correct cutoff function f. The Sakharov formula corresponds to f(x) = -ln(x). The spectral action with moment f_2 = integral x f(x) dx gives the polynomial route. Matching both determines f up to two constraints. With f_0 (CC) and f_4 (Higgs mass), f may be fully determined.

S43 UV/IR workshop (Nazarewicz R1 Section 4): The one-parameter family f_alpha(x) = x^{-alpha} exp(-x) CANNOT suppress f_0 relative to f_2 (f_0/f_2 = 1/(1-alpha) diverges as alpha -> 1). The Mittag-Leffler family E_{alpha,beta}(-x) also fails (f_0 integral diverges logarithmically for alpha < 1). The polynomial and logarithmic functionals are in DIFFERENT functional spaces.

**Computation Steps**:

1. Load W1-1 results from `tier0-computation/s44_sakharov_gn.npz`.

2. **Extract f_2 from matching.** From W1-1:

   $$f_2 = \frac{G_N^{\text{Sak}}}{G_N^{\text{spec}}} \cdot f_2^{\text{assumed}}$$

   Report f_2.

3. **Extract f_0 from CC.** If we want rho_vac = rho_obs:

   $$f_0 = \frac{\rho_{\text{obs}}}{a_0 \Lambda^{d}}$$

   Report f_0 and the ratio f_0 / f_2.

4. **Hausdorff moment problem.** Do f_0 and f_2 admit a positive, decreasing function f on [0, infinity)? The necessary condition (Hausdorff criterion): the sequence must be completely monotone. Test whether f_0, f_2 satisfy this.

5. **Comparison to known cutoff functions.** Report the f_0/f_2 ratio for:
   - Exponential: f(x) = exp(-x), f_0/f_2 = 1
   - Theta: f(x) = theta(1-x), f_0/f_2 = 2
   - Sakharov: f(x) = -ln(x), f_0 = infinity (not integrable)
   - Required: f_0/f_2 = (computed from steps 2-3)

6. **Report.** Whether f is self-consistently determined, or whether the polynomial and logarithmic regimes are irreconcilable (as the UV/IR workshop suggested).

**Pre-registered gate CUTOFF-F-44**:
- PASS: f uniquely determined to O(1) from {G_N, rho_Lambda}
- FAIL: No positive decreasing f satisfies both constraints (polynomial framework broken)
- INFO: f constrained but not uniquely determined

**Input files**:
- `tier0-computation/s44_sakharov_gn.npz` (W1-1 output)
- `tier0-computation/s42_constants_snapshot.npz`

**Output files**:
- Script: `tier0-computation/s44_cutoff_f.py`
- Data: `tier0-computation/s44_cutoff_f.npz`
- Plot: `tier0-computation/s44_cutoff_f.png`

**Working paper section**: W5-5

---

### W5-6: HOMOG-42 Recompute with Corrected H (HOMOG-42-RECOMPUTE-44)

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: LOW (reruns existing script with corrected input)

**Prompt**:

You are rerunning the HOMOG-42 homogeneity computation with the corrected Hubble rate H after accounting for the E-vs-F correction. HOMOG-42 has the tightest margin (4.5x) of any gate and is the most sensitive to the correction.

**Context.** S43 E-vs-F audit Instance 6: "H^2 ~ a_0 * M_KK^4 / M_Pl^2. If a_0 -> a_0 * f, then H -> H * sqrt(f), and <phi^2> ~ H^4 / m^2 scales as f^2. The delta_tau/tau fluctuation scales as f." The margin is 4.5x (delta_tau/tau = 6.7e-7 vs FIRAS bound ~3e-6). If f > 4.5, the gate flips.

Since TRACE-LOG-CC-44 (W1-4) may provide the correction factor f = E/S, this computation should wait for W1-4 if possible. Otherwise use f estimates from the E-vs-F audit.

**Computation Steps**:

1. Load original HOMOG-42 script and results from `tier0-computation/s42_homogeneity.py` and `tier0-computation/s42_homogeneity.npz`.

2. **E-vs-F correction factor.** If W1-4 (TRACE-LOG-CC-44) results are available, use the computed f = E/S. Otherwise, parametrize: f = 1 (baseline), f = 2, f = 5, f = 10.

3. **Corrected H.** H_corrected = H_original * sqrt(f).

4. **Corrected delta_tau/tau.** delta_tau/tau = (original) * f. (Because <phi^2> ~ H^4/m^2 ~ f^2, and delta_tau ~ sqrt(<phi^2>) ~ f.)

5. **Compare to FIRAS bound.** delta_tau/tau < 3e-6 (FIRAS, from spectral distortion bound on energy injection).

6. **Report.** Corrected margin for each f value. At what f does the gate flip?

**Pre-registered gate HOMOG-42-RECOMPUTE-44**:
- PASS: 4.5x margin survives (f < 4.5)
- FAIL: margin violated (f > 4.5, delta_tau/tau > 3e-6)
- INFO: f from W1-4 gives marginal result

**Input files**:
- `tier0-computation/s42_homogeneity.py`
- `tier0-computation/s42_homogeneity.npz`
- W1-4 results (if available)

**Output files**:
- Script: `tier0-computation/s44_homog_recompute.py`
- Data: `tier0-computation/s44_homog_recompute.npz`
- Plot: `tier0-computation/s44_homog_recompute.png`

**Working paper section**: W5-6

---
