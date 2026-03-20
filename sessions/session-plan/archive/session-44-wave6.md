## III-f. Wave 6: Specialist + Remaining (8 tasks, parallel)

### W6-1: Chladni Patterns of GGE on SU(3) (CHLADNI-GGE-44)

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the spatial pattern of the 8 GGE occupation numbers n_i(y) on the SU(3) manifold. The GGE modes are eigenstates of D_K with definite representation content. Their spatial distributions on SU(3) form Chladni-like nodal patterns. These patterns determine the internal structure of a KZ domain cell.

**Context.** S43 CDM-CONSTRUCT-43: GGE modes are internal-space excitations with zero 4D momentum. Their spatial distribution on SU(3) determines the local physics (gauge couplings, particle masses) at each point of the internal manifold. If the patterns have specific symmetry (e.g., aligned with the U(1)_7 direction), this constrains baryogenesis at domain walls.

**Computation Steps**:

1. Load eigenvectors from `tier0-computation/tier1_dirac_spectrum.py` at tau = 0.19 for the 8 gap-edge modes.

2. **Spatial density.** For each mode k, compute |psi_k(y)|^2 on a grid of SU(3) points. Since SU(3) is 8-dimensional, reduce to the 2D Cartan torus (parametrized by the two Casimir eigenvalues) by integrating over the SU(3) fiber.

3. **Chladni patterns.** Plot the nodal lines (|psi_k|^2 = 0) and maxima on the Cartan torus for each of the 8 modes: 4 B2 modes, 1 B1 mode, 3 B3 modes.

4. **GGE composite pattern.** The GGE state has specific occupation numbers n_k. Plot the composite density:

   $$\rho_{\text{GGE}}(y) = \sum_k n_k |psi_k(y)|^2$$

5. **Symmetry analysis.** Which symmetries does rho_GGE preserve? Does rho_GGE respect U(1)_7? Does it have nodal lines that could serve as domain wall nucleation sites?

6. **Report.** Spatial patterns, symmetry, implications for baryogenesis and domain wall structure.

**Pre-registered gate CHLADNI-GGE-44**: INFO (diagnostic, no PASS/FAIL).

**Input files**:
- `tier0-computation/tier1_dirac_spectrum.py`
- `tier0-computation/s42_gge_energy.npz`

**Output files**:
- Script: `tier0-computation/s44_chladni_gge.py`
- Data: `tier0-computation/s44_chladni_gge.npz`
- Plot: `tier0-computation/s44_chladni_gge.png`

**Working paper section**: W6-1

---

### W6-2: Second-Sound Attenuation Length (2ND-SOUND-ATTEN-44)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are computing the attenuation length of second sound (u_2 = c/sqrt(3)) in comoving Mpc. This determines whether the BAO analog feature at 147 Mpc is damped or enhanced relative to standard LCDM BAO.

**Context.** S43 THERM-COND-43: kappa = infinity (ballistic transport, no Umklapp). The fabric is a perfect thermal conductor. Second sound at u_2 = c/sqrt(3) was confirmed. In superfluid He-4 below the lambda point, second sound propagates with very low attenuation (Q ~ 10^3-10^4). The framework's fabric should have comparable or higher Q.

**Computation Steps**:

1. Load thermal conductivity data from `tier0-computation/s43_thermal_conductivity.npz` and quality factors from `tier0-computation/s43_quality_factors.npz`.

2. **Attenuation from 3-phonon processes.** Even without Umklapp, normal 3-phonon processes (B2 -> B1 + B1) cause attenuation. The attenuation rate:

   $$\alpha_2 = \frac{\omega^2}{2 \rho c_2} \cdot \left(\frac{4\eta_s}{3} + \zeta + \kappa\left(\frac{1}{c_v} - \frac{1}{c_p}\right)\right)$$

   For the fabric: eta_s (shear viscosity), zeta (bulk viscosity), kappa (thermal conductivity = infinity).

3. **Attenuation length.** l_atten = 1 / alpha_2. Convert to comoving Mpc.

4. **Comparison to sound horizon.** If l_atten >> r_BAO = 147 Mpc, second sound is undamped at the BAO scale. If l_atten ~ r_BAO, significant damping.

5. **Impact on BAO amplitude.** Damped second sound has amplitude ~ exp(-r/l_atten). Report the expected amplitude at r_BAO and at r_1 = 325 Mpc.

6. **Report.** l_atten in Mpc, Q factor of second sound, comparison to standard BAO Silk damping.

**Pre-registered gate 2ND-SOUND-ATTEN-44**: INFO.

**Input files**:
- `tier0-computation/s43_thermal_conductivity.npz`
- `tier0-computation/s43_quality_factors.npz`

**Output files**:
- Script: `tier0-computation/s44_2nd_sound_atten.py`
- Data: `tier0-computation/s44_2nd_sound_atten.npz`
- Plot: `tier0-computation/s44_2nd_sound_atten.png`

**Working paper section**: W6-2

---

### W6-3: Bayesian f Posterior (Mittag-Leffler Family) (BAYESIAN-f-44)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are extending MKK-BAYES-43 to a 2-parameter family of cutoff functions, following the S43 UV/IR workshop prescription. Parametrize f as a generalized Mittag-Leffler family and compute the posterior on (alpha, beta) from {G_N, alpha_EM, FIRAS}.

**Context.** S43 UV/IR workshop (Nazarewicz R1 Section 4): The one-parameter family f_alpha(x) = x^{-alpha} exp(-x) cannot suppress f_0/f_2. The Mittag-Leffler E_{alpha,beta}(-x) also fails for the CC. But testing the 2-parameter posterior quantifies the functional-form discrepancy. S43 MKK-BAYES-43: 0.70-decade tension between gravity and gauge routes.

**Computation Steps**:

1. Load eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz` and constants from `tier0-computation/s42_constants_snapshot.npz`.

2. **Mittag-Leffler family.** f_{alpha,beta}(x) = E_{alpha,beta}(-x) where:

   $$E_{\alpha,\beta}(z) = \sum_{k=0}^{\infty} \frac{z^k}{\Gamma(\alpha k + \beta)}$$

   At alpha=beta=1: f = exp(-x) (standard). Compute moments f_0(alpha,beta), f_2(alpha,beta), f_4(alpha,beta).

3. **Observables.** For each (alpha,beta) on a 50x50 grid with alpha in [0.3, 2.0], beta in [0.3, 2.0]:
   - M_KK from G_N: 1/(16 pi G_N) = f_2 Lambda^2 a_2 => M_KK(alpha,beta)
   - alpha_EM from a_4/a_2 ratio
   - FIRAS: delta_tau/tau from HOMOG-42 formula

4. **Posterior.** p(alpha, beta | data) proportional to L(G_N) * L(alpha_EM) * L(FIRAS) * pi(alpha,beta). Use flat prior on (alpha,beta). Compute on the grid.

5. **Tension diagnostic.** Is there any (alpha, beta) that simultaneously satisfies G_N, alpha_EM, and FIRAS within 1 sigma? If not, the functional-form tension is irreducible.

6. **Report.** Posterior map, best-fit (alpha, beta), tension quantification, comparison to standard exponential cutoff.

**Pre-registered gate BAYESIAN-f-44**: INFO (diagnostic for functional form).

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/s43_mkk_bayes.npz`

**Output files**:
- Script: `tier0-computation/s44_bayesian_f.py`
- Data: `tier0-computation/s44_bayesian_f.npz`
- Plot: `tier0-computation/s44_bayesian_f.png`

**Working paper section**: W6-3

---

### W6-4: Omega_DM/Omega_DE from 3 Methods (DM-DE-RATIO-44)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are computing the DM/DE ratio from three independent methods to test whether the ratio is tractable even if the absolute scales are not.

**Context.** S43 CC workshop convergence C9: "DM and CC are the SAME problem. Both require 120-order suppression from the same energy scale M_KK^4. Any CC mechanism must be universal across all 8 GGE modes. The DM/DE ratio depends on GGE mode structure, not absolute scale."

CDM-CONSTRUCT-43: ALL GGE energy is CDM (w=0). The framework produces NO dark energy from the transit. The DE must come from the residual vacuum energy (spectral action or trace-log).

**Computation Steps**:

1. Load GGE data from `tier0-computation/s42_gge_energy.npz` and constants from `tier0-computation/s42_constants_snapshot.npz`.

2. **Method 1: GGE mode partition.** Omega_DM = E_exc (all modes). Omega_DE = rho_vac (from spectral action or trace-log, after equilibrium subtraction). Ratio = E_exc / rho_vac. With E_exc = 50.9 M_KK and rho_vac = Delta_S = 5522 M_KK^4: the ratio depends on dimensional factors.

3. **Method 2: q-theory (Paper 35).** Following Klinkhamer-Volovik 2016: DM/DE ~ 3 (predicted from q-theory without fine-tuning). The ratio Omega_DM/Omega_Lambda ~ (omega_q/H_0) * (delta_q/q_0)^2. Compute with framework parameters.

4. **Method 3: Flat-band partition.** B2 modes (flat band, CDM) vs B1+B3 modes. The flat band contributes a specific fraction of E_exc. The remaining fraction becomes the "normal component." Compute the ratio.

5. **Report.** Omega_DM/Omega_DE from all 3 methods, comparison to observed 0.39, whether any method is within factor 10.

**Pre-registered gate DM-DE-RATIO-44**:
- PASS: any method within factor 10 of 0.39
- FAIL: all methods off by > 100
- INFO: ratios computed but model-dependent

**Input files**:
- `tier0-computation/s42_gge_energy.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/s43_qtheory_selftune.npz`
- `researchers/Volovik/35_2016_Klinkhamer_Volovik_Dark_Matter_Dark_Energy_q_Theory.md`

**Output files**:
- Script: `tier0-computation/s44_dm_de_ratio.py`
- Data: `tier0-computation/s44_dm_de_ratio.npz`
- Plot: `tier0-computation/s44_dm_de_ratio.png`

**Working paper section**: W6-4

---

### W6-5: Multi-Temperature Jacobson First Law (MULTI-T-JACOBSON-44)

**Agent**: `hawking-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are computing the 8-temperature generalization of Jacobson's thermodynamic first law for the GGE, deriving the 8-fluid equation of state. This extends JACOBSON-SPEC-44 (W5-1) with the full multi-temperature structure.

**Context.** S43 CC workshop emerged E3: "The correct first law is delta Q = sum_k T_k dS_k. This naturally produces an 8-fluid cosmology." S43 GGE-TEMP-43: T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178. Negative pairwise T(B2,B1) = -0.066 (time-crystalline signature, Paper 34).

**Computation Steps**:

1. Load GGE temperatures from `tier0-computation/s43_gge_temp.npz` and first law data from `tier0-computation/s43_first_law.npz`.

2. **8-fluid decomposition.** Each GGE mode k has: energy density rho_k, pressure P_k = 0 (dust), temperature T_k, entropy S_k.

3. **Coupled Friedmann equations.** For 8 non-interacting dust components:

   $$H^2 = \frac{8\pi G_N}{3} \sum_{k=1}^{8} \rho_k$$

   $$\dot{\rho}_k + 3H \rho_k = 0 \quad \text{(each separately conserved)}$$

4. **Cross-temperature contributions.** The negative T(B2,B1) = -0.066 introduces off-diagonal terms in the first law. Compute whether this produces effective pressure (w != 0) in the coupled system.

5. **Report.** 8-fluid EOS, effective total w, contribution of negative cross-temperatures.

**Pre-registered gate MULTI-T-JACOBSON-44**: INFO (8-fluid EOS).

**Input files**:
- `tier0-computation/s43_gge_temp.npz`
- `tier0-computation/s43_first_law.npz`
- `tier0-computation/s42_gge_energy.npz`

**Output files**:
- Script: `tier0-computation/s44_multi_t_jacobson.py`
- Data: `tier0-computation/s44_multi_t_jacobson.npz`
- Plot: `tier0-computation/s44_multi_t_jacobson.png`

**Working paper section**: W6-5

---

### W6-6: Spectral Dimension from Polariton Band Structure (SPECTRAL-DIM-BAND-44)

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are computing the spectral dimension d_s from the polariton band structure at the fold, using the flat-band B2 as a diagnostic. A flat band has d_s -> 0 (no propagation), while dispersive bands have d_s > 0. The overall d_s depends on the ratio of flat to dispersive bands.

**Context.** S43 POL-BZ-43: 6 anticrossings, tightest gap 0.0019 M_KK, 2 topological bands (Berry phase pi). S43 FLATBAND-43: B2 bandwidth = 0 exactly. The polariton band structure mixes internal (KK) and external (acoustic) modes, creating a hybrid spectrum with both flat and dispersive components.

**Computation Steps**:

1. Load polariton data from `tier0-computation/s42_polariton.npz` and flat band data from `tier0-computation/s43_flatband.npz`.

2. **d_s from heat kernel on polariton spectrum.** P(sigma) = sum_n exp(-sigma omega_n^2) where omega_n are the polariton band energies at each crystal momentum.

3. **d_s at different scales.** UV (sigma small): d_s should approach the space dimension. IR (sigma large): d_s decreases due to gaps and flat bands.

4. **Flat-band contribution.** The flat band (B2, 4 modes with identical energy) gives a delta-function contribution to P(sigma), independent of sigma. This pulls d_s toward 0 at all scales.

5. **Report.** d_s(sigma) from polariton spectrum, comparison to d_s from D_K eigenvalues (W2-2), contribution of flat band to d_s reduction.

**Pre-registered gate SPECTRAL-DIM-BAND-44**: INFO (flow diagnostic).

**Input files**:
- `tier0-computation/s42_polariton.npz`
- `tier0-computation/s43_flatband.npz` (if exists, otherwise s43 results)

**Output files**:
- Script: `tier0-computation/s44_spectral_dim_band.py`
- Data: `tier0-computation/s44_spectral_dim_band.npz`
- Plot: `tier0-computation/s44_spectral_dim_band.png`

**Working paper section**: W6-6

---

### W6-7: Dissolution Threshold Scaling (DISSOLUTION-SCALING-44)

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

You are testing whether the spectral triple dissolution threshold epsilon_crossover ~ 0.014 (S43 DISSOLUTION-43) scales as 1/sqrt(N) with the number of modes N (max_pq_sum), or has a different scaling. This determines whether the spectral triple becomes more or less robust as the truncation is extended.

**Computation Steps**:

1. Load dissolution data from `tier0-computation/s43_dissolution.npz`.

2. **Recompute at multiple truncations.** For max_pq_sum = 3, 4, 5, 6 (giving N = 112, 240, 432, 992 modes), compute the dissolution threshold epsilon_c where the spectral triple axioms first fail.

3. **Scaling fit.** Fit epsilon_c(N) to: (a) 1/sqrt(N), (b) 1/N, (c) 1/ln(N), (d) constant.

4. **Extrapolation.** If 1/sqrt(N): extrapolate to N -> infinity (continuum limit). epsilon_c -> 0 means the spectral triple is EMERGENT and dissolves at any foam strength.

5. **Report.** Scaling law, extrapolation, implications for the spectral triple's stability.

**Pre-registered gate DISSOLUTION-SCALING-44**:
- PASS: 1/sqrt(N) scaling confirmed (spectral triple is emergent)
- FAIL: constant epsilon_c (spectral triple is robust)
- INFO: other scaling

**Input files**:
- `tier0-computation/s43_dissolution.npz`
- `tier0-computation/tier1_dirac_spectrum.py`

**Output files**:
- Script: `tier0-computation/s44_dissolution_scaling.py`
- Data: `tier0-computation/s44_dissolution_scaling.npz`
- Plot: `tier0-computation/s44_dissolution_scaling.png`

**Working paper section**: W6-7

---

### W6-8: Van Hove Singularity Tracking (VAN-HOVE-TRACK-44)

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are tracking the positions of all 13 van Hove singularities (identified in S43 DOS-43) across the tau range [0.05, 0.25], using eigenvalue data at 5 tau points (from DOS-TAU-44, W5-3, if available, otherwise recompute).

**Computation Steps**:

1. Load eigenvalue data at 5 tau values. If DOS-TAU-44 output exists at `tier0-computation/s44_dos_tau.npz`, use it. Otherwise use `tier0-computation/tier1_dirac_spectrum.py` to compute at tau = 0.05, 0.10, 0.15, 0.19, 0.25.

2. **Identify singularity positions.** At each tau, compute the DOS histogram and identify peaks (M_0 minima, M_1 saddles, M_2 maxima, M_3 flat). Track each singularity's energy position E_vH(tau).

3. **Singularity trajectories.** Plot E_vH(tau) vs tau for all 13 singularities. Identify any mergers, bifurcations, or annihilations.

4. **Connection to Lifshitz.** At the Lifshitz transition (tau=0), some singularities merge (degeneracy of round SU(3)). The number of singularities should INCREASE as tau increases from 0 (symmetry breaking). Verify.

5. **Report.** Singularity trajectories, connection to Lifshitz transition, impact on DOS shape across transit.

**Pre-registered gate VAN-HOVE-TRACK-44**: INFO (diagnostic).

**Input files**:
- `tier0-computation/s44_dos_tau.npz` (W5-3 output, if available)
- `tier0-computation/tier1_dirac_spectrum.py`
- `tier0-computation/s43_phonon_dos.npz`

**Output files**:
- Script: `tier0-computation/s44_vanhove_track.py`
- Data: `tier0-computation/s44_vanhove_track.npz`
- Plot: `tier0-computation/s44_vanhove_track.png`

**Working paper section**: W6-8

---
