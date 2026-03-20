## III-b. Wave 2: Dependent Computations (4 tasks, requires W1-1 and W1-2)

### W2-1: GGE Dark Matter Abundance via Q-Theory

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW

**Prompt**:

Compute dark matter abundance Omega_DM from GGE quasiparticle relic using q-theory, addressing the 2000x shortfall (S42: Omega_DM/Omega_Lambda ~ 2e-4).

**Context.** Paper 35 (`researchers/Volovik/35_2016_Klinkhamer_Volovik_Dark_Matter_Dark_Energy_q_Theory.md`): DM = q-field perturbation delta_q with rho_DM = (1/2) * <(d_t delta_q)^2 + c_q^2 (nabla delta_q)^2>. Paper 35 predicts DM/DE ~ 3 without fine-tuning; framework gives 2e-4. Mismatch 10^4 → naive S_fold = rho_Lambda identification wrong.

S42 R4 Q2: q-theory works without thermal equilibrium (self-tuning is thermodynamic, not thermal).

Two-source budget: GGE quasiparticles (internal-space, w=0) + q-field perturbations (spatial tau fluctuations, w=0 by Paper 35).

**Computation Steps**:

1. **Load W1-1 results** from `tier0-computation/s43_qtheory_selftune.npz`. Also load `tier0-computation/s42_gradient_stiffness.npz` and `tier0-computation/s42_gge_energy.npz`.

2. **Q-field perturbation spectrum.** Following Paper 35:

   $$\ddot{\delta q} + 3H\dot{\delta q} - \frac{c_q^2}{a^2}\nabla^2\delta q + m_q^2 \delta q = 0$$

   where m_q^2 = d^2_rho/dq^2|_{q_0} (from W1-1) and c_q^2 = Z / (m_q^2 * M_KK^{-2}).

3. **Compute rho_DM from q-perturbations.** Initial amplitude from quantum fluctuations or KZ defect density (xi_KZ = 0.152 M_KK^{-1} from S42 W5-5):

   $$\langle\delta q^2\rangle \sim \frac{n_{\text{pairs}}}{\xi_{\text{KZ}}^3} \cdot \frac{1}{m_q^2}$$

4. **Omega_DM/Omega_Lambda.** Use rho_DM and rho_Lambda from W1-1. Compare to observed 0.3.

5. **Two-source budget.** Total DM = GGE (59.8 pairs, E_exc = 50.9 M_KK) + q-field perturbations. Compute ratio.

6. **Paper 35 oscillation amplification diagnostic.** omega_q = m_q * c^2/hbar ~ m_tau * M_KK ~ 2.3e41 Hz. Jeans scale and free-streaming for this field.

**Pre-registered gate GGE-DM-43**:
- PASS: Omega_DM/Omega_Lambda > 0.03
- FAIL: < 0.001
- INTERMEDIATE: 0.001 to 0.03

**Input**: W1-1 output + `tier0-computation/s42_gradient_stiffness.npz`, `s42_gge_energy.npz`, `s42_dm_profile.npz`, `s42_constants_snapshot.npz`
**Output**: `tier0-computation/s43_gge_dm_abundance.{py,npz,png}`

---

### W2-2: Two-Fluid w(z) Trajectory for DESI

**Agent**: `einstein-theorist`
**Model**: opus
**Cost**: MEDIUM (numerical ODE integration)

**Prompt**:

Compute w(z) from Volovik's Landau-Khalatnikov two-fluid model (Paper 37 in `researchers/Volovik/`) using framework parameters.

**Context.** S42 W-Z-42 REDO #2: w = -1 + O(10^{-29}) from single-component spectral action. Paper 37: superfluid + normal → mutual friction → w departing from -1 at percent level. Prediction: rho_m ~ t^{-0.4}, rho_Lambda ~ t^{0.6}.

Framework parameters: superfluid = spectral action (after W1-1 q-theory), normal = GGE (59.8 pairs, 50.9 M_KK), mutual friction via m_tau = 2.062 M_KK and omega_att = 1.430 M_KK (S38).

DESI DR2: w_0 = -0.72 ± 0.07 (3.1 sigma). Wang & Mota (Paper 37 in `researchers/Cosmic-Web/`): driven by dataset tensions. Skeptical assessment supports w = -1.

Critical: Gamma/H ~ 10^{58} >> 1. Two fluids in local equilibrium → w = -1 exactly. Departure requires z-dependent Gamma or non-trivial GGE evolution.

S42 Nazarewicz W3-1 review: 5 mechanisms ALL defeated by effacement. Breathing mode open but likely effacement-suppressed.

**Computation Steps**:

1. **Load upstream data.** S42 computation files + W1-1 q-theory results.

2. **Set up two-fluid equations (Paper 37)**:

   $$H^2 = \frac{8\pi G}{3}(\rho_s + \rho_n)$$
   $$\dot{\rho}_s + 3H(\rho_s + P_s) = -\Gamma(\rho_s + P_s)$$
   $$\dot{\rho}_n + 3H(\rho_n + P_n) = +\Gamma(\rho_s + P_s)$$

3. **Fix mutual friction**: Gamma = omega_att/(2*pi) = 1.430 * M_KK / (2*pi) ~ 2.6e40 s^{-1}. Gamma/H ~ 10^{58}.

4. **Handle hierarchy.** If Gamma >> H, two fluids in local equilibrium, w = -1 exactly. Test for z-dependent Gamma or GGE evolution that could produce departure.

5. **Compute w(z) from z=0 to z=5.** CPL parameters w_0, w_a.

6. **Effacement check.** Any correction suppressed by |E_BCS|/S_fold ~ 3e-7?

7. **DESI comparison.** Plot framework w(z) vs DESI DR2 constraints.

**Pre-registered gate TWOFLUID-W-43**:
- PASS: |w_0+1| > 0.001
- FAIL: |w_0+1| < 10^{-6}
- INTERMEDIATE: 10^{-6} to 0.001

**Input**: S42 computation files + `tier0-computation/s38_attempt_freq.npz` + `researchers/Volovik/37_2024_Volovik_Landau_Khalatnikov_Two_Fluid_de_Sitter.md`
**Output**: `tier0-computation/s43_twofluid_wz.{py,npz,png}`

---

### W2-3: Carlip CC Mechanism Interface (F-FOAM-5)

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: LOW (analytic, closed-form with CONST-FREEZE-42 inputs)

**Prompt**:

Compute the Wheeler-DeWitt pocket width for Carlip's wavefunction-trapping mechanism with Lambda_internal from the framework's spectral action. Determine whether Carlip + framework produces Lambda_obs.

**Source**: S42 master collab T1-2 (QF 3A, rated CRITICAL). S42 QF collab Section 3A: "NOW COMPUTABLE. Lambda_internal = 2.2e-9 M_P^4 from CONST-FREEZE-42. Carlip provides ~10^{113} suppression. Required L ~ 10^{-7} m predicts force anomalies Delta F/F ~ 10^{-23}."

**Context.** Carlip's midisuperspace foam (Papers 08, 11, 14, 15 in `researchers/Quantum-Foam/`):

$$|\Psi(\bar\theta)|^2 \sim \exp\left(-\frac{2\pi^2 \Lambda \bar\theta^2 L^4}{\hbar}\right)$$

The framework provides Lambda_internal. Carlip provides the suppression through wavefunction trapping in the zero-expansion sector.

**Computation Steps**:

1. **Framework Lambda.** From CONST-FREEZE-42:
   - S_fold = 250,361 M_KK^4
   - M_KK = 7.4e16 GeV (gravity route)
   - Lambda = S_fold * M_KK^4 / (16*pi^2) = 250,361 * (7.4e16)^4 / 158 = 4.8e67 GeV^4
   - In Planck units: Lambda/M_P^4 = 4.8e67 / 2.2e76 = 2.2e-9

2. **Required suppression.** Lambda_obs = 2.9e-122 M_P^4. Suppression needed: 2.2e-9 / 2.9e-122 = 7.6e112. So ~113 orders.

3. **Carlip trapping scale.** From Paper 14 eq C14-3: suppression ~ exp(-Lambda * L^4). Need Lambda * L^4 ~ 260 (for 10^{113} suppression). With Lambda = 2.2e-9 M_P^4:
   - L^4 = 260 / (2.2e-9) = 1.2e11 in Planck units
   - L = (1.2e11)^{1/4} = 5.9e2 l_P = 9.5e-33 m

   Wait — that's sub-Planckian. Recheck. From QF 3A: "L ~ 10^{28} l_P ~ 10^{-7} m." This uses a different formula. Verify which Carlip equation applies.

4. **Verify from Paper 14 directly.** Read `researchers/Quantum-Foam/15_2023_Carlip_Spacetime_Foam_Review.md` and extract the correct trapping formula with all numerical prefactors.

5. **Compute Lambda_eff.** If the trapping produces the correct suppression, Lambda_eff ~ Lambda_obs. Report the averaging scale L required and whether it is physically reasonable.

6. **Force anomaly prediction.** Paper 14 eq C14-5: Delta F/F ~ (l_P/L)^{2/3}. Compute for the required L.

**Pre-registered gate F-FOAM-5-43**:
- PASS: Lambda_eff within 10 orders of Lambda_obs for a physically reasonable L (L > l_P, L < 1 m)
- FAIL: No L produces Lambda_eff near Lambda_obs, OR required L is sub-Planckian
- INFO: Computation completed but depends critically on which Carlip formula is used

**Input**: `tier0-computation/s42_constants_snapshot.npz`, `tier0-computation/s42_gradient_stiffness.npz`, Carlip papers in `researchers/Quantum-Foam/`
**Output**: `tier0-computation/s43_carlip_cc.{py,npz,png}`

---

### W2-4: Acoustic Impedance Mismatch T(m, delta_tau) at Domain Walls

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: LOW (analytic formula + existing eigenvalue data)

**Prompt**:

Compute the transmission coefficient T(m, delta_tau) for KK quasiparticles crossing a domain wall where tau changes by delta_tau. Determine whether mass-dependent filtering creates the 3-decade dynamic range the HF gate requires.

**Source**: S42 master collab T0-3 (QA 3.1). S42 QA collab Section 3.1: "computable from existing data." S42 CW addendum Section A.2-A.3: "impedance mismatch creates MASS-DEPENDENT FILTERING at void walls."

**Computation Steps**:

1. Load BdG quasiparticle masses M*(tau) from `tier0-computation/s42_fabric_dispersion.npz` and eigenvalue derivatives from `tier0-computation/s42_gradient_stiffness.npz`.

2. Acoustic impedance at each tau: Z_acoustic(tau) = M*(tau) * v_g(tau), where v_g = k/omega = k/sqrt(M*^2 + k^2).

3. Transmission coefficient through a tau-step boundary:

   $$T = \frac{4 Z_1 Z_2}{(Z_1 + Z_2)^2}$$

4. For small delta_tau: delta_Z/Z ~ (dM*/dtau) * delta_tau / M*.

5. Compute T(m, delta_tau) for:
   - Each of the 8 BdG quasiparticle modes (B2 ×4, B1 ×1, B3 ×3)
   - delta_tau values: [0.001, 0.005, 0.01, 0.02, 0.05, 0.10]
   - k values spanning [0, 10] M_KK

6. Compute effective branching ratio from impedance filtering. Does the mass-dependent T produce > 3 decades of dynamic range?

7. Compare to HF-KK-42 sector-level DR of 1.51 decades. Does impedance filtering improve this?

**Pre-registered gate IMP-FILTER-43**:
- PASS: Impedance filtering produces DR > 3 decades for delta_tau > 0.01
- FAIL: DR < 2 decades for all delta_tau
- INFO: DR between 2-3 decades

**Input**: `tier0-computation/s42_fabric_dispersion.npz`, `tier0-computation/s42_gradient_stiffness.npz`, `tier0-computation/s42_hauser_feshbach.npz`
**Output**: `tier0-computation/s43_impedance_mismatch.{py,npz,png}`

---

