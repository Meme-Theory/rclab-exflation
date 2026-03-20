## III-c. Wave 3: Synthesis + Baryogenesis Deep Dive (5 tasks, depends on W1-3 + W2)

### W3-1: Cold Big Bang Timeline

**Agent**: `gen-physicist`
**Model**: opus
**Cost**: LOW (synthesis)

**Prompt**:

Construct the complete Cold Big Bang timeline: epoch-by-epoch evolution from tau=0 to z=0, incorporating all W1-W2 results. Side-by-side comparison with standard hot big bang. Identify first observational divergence point.

**Context.** S42 scales R1 7-epoch mapping (E0-E6). S42 R4: cold big bang = quantum annealing (ZDZ 2005). First heating Schwinger-type. GGE has 8 temperatures (Paper 34). Virtual/real emergent from complexity.

Key S42 numbers: T_RH=1.1*M_KK, eta=3.4e-9, w=-1+O(10^{-29}), sigma/m=5.7e-51, lambda_fs=3.1e-48, c_fabric=c, m_tau=2.062, Z=74,731, delta_tau/tau=1.75e-6, f_NL=0.014, M_KK(gravity)=7.4e16, sin^2(theta_W)=0.584, n_s=0.746 (FAIL).

Hawking (S42 collab): Parker creation (not Hawking). S_ent=0. No information paradox.
CW (S42 collab): ZERO distinctive LSS predictions. Sentinel role. DESI falsification.
LRD (S42 collab): Observational degeneracy 7th session. CDM-identical at z<10^{28}.

**Computation**: Load ALL W1-W2 results → epoch table → Cold vs Hot comparison → first divergence point.

**Pre-registered gate CBB-TIMELINE-43**: PASS if complete timeline + 1 falsifiable prediction.

**Input**: All `s43_*.npz` + S42 computation files.
**Output**: `tier0-computation/s43_cbb_timeline.{py,npz,png}`

---

### W3-2: Quantum Fluctuation Analysis at tau=0

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: LOW (analytic + light numerics)

**Prompt**:

Analyze quantum fluctuation spectrum at tau=0 (unstable maximum of spectral action). Compute primordial power spectrum P_R(k), e-fold count N_e, flatness from BDI topology.

**Context.** S42 R4: tau=0 unstable maximum (dS/dtau=+58,673). ANY perturbation triggers cascade. CRYSTAL-SPEC-42: smooth spectrum tau=0 to 0.05. Paper 04 (Fermi point): universe naturally flat from BDI topology.

S42 HOMOG-42: delta_tau/tau = 1.75e-6, m_tau/H = 25.9 (superheavy), N_transit ~ 5e-5 e-folds.

**Computation Steps**:

1. Characterize unstable maximum: S(0), dS/dtau|_0, d2S/dtau2|_0, Z(0).

2. Inverted harmonic oscillator: V(tau) = V_0 + (1/2)*V''_0*tau^2 with V''_0 < 0.

   $$\langle\tau^2\rangle = \frac{\hbar}{2\sqrt{|V''_0| \cdot Z_0}}$$

3. Fluctuation spectrum:

   $$P_\tau(k) = \frac{(H_{\text{init}}/2\pi)^2}{Z_0}$$

4. Curvature power spectrum: P_R(k) = V / (24*pi^2 * M_Pl^4 * epsilon). Compare to A_s = 2.1e-9.

5. Flatness from topology (Paper 04). Chern-Simons contribution.

6. Transit duration: N_e = integral_0^{0.19} H/tau_dot dtau.

7. Compare to inflation: N_e > 60? A_s ~ 2.1e-9? n_s ~ 0.965?

**Pre-registered gate QFLUC-43**: PASS if P_R within 10 OOM of A_s AND N_e > 10.

**Input**: `s36_sfull_tau_stabilization.npz`, `s42_gradient_stiffness.npz`, `s42_constants_snapshot.npz`, `researchers/Volovik/04_2008_Volovik_Emergent_Physics_Fermi_Point_Scenario.md`
**Output**: `tier0-computation/s43_qfluc_tau0.{py,npz,png}`

---

### W3-3: J-Odd Perturbation at Domain Wall

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute [J, V_phys] where V_phys = Kosmann connection + off-Jensen boundary terms at a domain wall. Determine whether [K_a, J] = 0 or != 0 at the wall. Closes or opens baryogenesis channel permanently.

**Source**: S42 master collab T1-1 (Dirac Comp 1, rated CRITICAL). S42 Dirac collab Section 3 Computation 1: "The path to baryogenesis must break one vertex of the structural triangle. The most vulnerable vertex is the J-symmetry: not in the bulk (where it is a theorem) but at the domain wall boundary."

Uses W1-3 results for [J, iK_7] and spectral flow.

**Computation Steps**:

1. Load K_a matrices from `tier0-computation/s23a_kosmann_singlet.npz`. Load J from `tier0-computation/s35_pfaffian_corrected_j.npz`.

2. Compute [K_a, J] for each of the 8 Kosmann generators a=0,...,7 in the 16×16 representation.

3. If [K_a, J] = 0 for all a: J-symmetry is preserved at the wall. Baryogenesis channel CLOSED.

4. If [K_a, J] != 0 for any a: compute ||[K_a, J]|| / ||K_a|| for each a. This is the geometric epsilon_CP.

5. For nonzero results: compute the baryon asymmetry from the Callan-Harvey mechanism at the wall. The asymmetry per wall crossing is:

   $$\epsilon_{\text{CP}} \sim \frac{||[K_a, J]||}{||K_a||} \cdot \frac{\Delta_{K_7}}{E_{\text{GGE}}}$$

6. Combined with W1-3 eta_kinematic: eta_net = eta_kin * epsilon_CP. Compare to 6.12e-10.

**Pre-registered gate JODD-WALL-43**:
- PASS: [K_a, J] != 0 AND epsilon_CP > 10^{-6}
- FAIL: [K_a, J] = 0 for all a (permanent closure)

**Input**: `s23a_kosmann_singlet.npz`, `s35_pfaffian_corrected_j.npz`, W1-3 results
**Output**: `tier0-computation/s43_jodd_wall.{py,npz,png}`

---

### W3-4: Chiral Eta Invariant at Domain Wall

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the chiral eta invariant (restricted to (1±gamma_9)/2 sectors) as function of position across wall profile tau(x) with xi_BCS = 1.118 M_KK^{-1}. Test whether chiral spectral asymmetry is nonzero.

**Source**: S42 master collab T1-4 (Dirac Comp 2). S42 Dirac collab Section 3 Computation 2: "The full D_K eta invariant vanishes identically by spectral pairing ({gamma_9, D_K} = 0). But the CHIRAL eta invariant need not vanish."

S42 master collab insight #4: "A nonzero chiral eta invariant at the wall would manifest as entropy imbalance between chiral sectors — thermodynamic driving force for baryogenesis."

**Computation Steps**:

1. Load D_K eigenvalues and eigenvectors at multiple tau from tier1_dirac_spectrum.py.

2. Construct wall profile: tau(x) = tau_fold + (Delta_tau/2) * tanh(x / xi_BCS).

3. At each position x across the wall (10 points from -3*xi to +3*xi):
   - Compute D_K(tau(x)) eigenvalues {lambda_i}
   - Project onto chiral sectors: P_± = (1 ± gamma_9)/2
   - Compute chiral eta: eta_± = sum_{lambda_i in ± sector} sign(lambda_i) |lambda_i|^{-s}|_{s=0}

4. If eta_+ != eta_-: chiral spectral asymmetry exists at the wall.

5. Compute Delta_eta_chiral = eta_+(wall center) - eta_+(bulk).

6. Connect to Callan-Harvey: the anomaly inflow from 3+1 dimensions to the 2+1D wall is proportional to Delta_eta_chiral.

**Pre-registered gate CHIRAL-ETA-43**:
- PASS: |eta_+ - eta_-| > 10^{-6} at wall center
- FAIL: eta_+ = eta_- to machine precision everywhere

**Input**: `tier1_dirac_spectrum.py`, `s35_pfaffian_corrected_j.npz`
**Output**: `tier0-computation/s43_chiral_eta.{py,npz,png}`

---

### W3-5: KZ Power Spectrum Transfer Function

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the 2-point correlation function of the stochastic KZ tau field and derive the transfer function that maps KZ micro-structure to the primordial power spectrum at CMB scales.

**Source**: S42 Tesla collab Section 3a: "The KZ power spectrum at KK scale is flat (n_s = 1) because k_pivot << 1/xi_KZ. The tilt comes from the projection mechanism (transfer function), not the KZ spectrum alone."

Uses W1-2 (Lifshitz type, critical exponents) and W3-2 (vacuum fluctuation analysis).

**Computation Steps**:

1. From W1-2: KZ universality class (z, nu), xi_KZ = 0.152 M_KK^{-1}.

2. KZ field correlation function in 3D:

   $$\langle\delta\tau(x)\delta\tau(x')\rangle = A \cdot |x-x'|^{-(d-2+\eta_{\text{Ising}})} \text{ for } |x-x'| < \xi_{\text{KZ}}$$

   with eta_Ising ~ 0.036 for 3D Ising.

3. Power spectrum P(k):
   - k > 1/xi_KZ: P(k) ~ k^{-(d+z_KZ)} (KZ scaling)
   - k < 1/xi_KZ: P(k) ~ const (white noise)

4. Transfer function: the projection from KZ micro-structure to CMB observables through:
   - Modulated reheating: delta_T_RH/T_RH ~ (d ln T_RH/d tau) * delta_tau
   - Spectral action modulation: delta_S/S ~ (d ln S/d tau) * delta_tau
   - Sachs-Wolfe: delta_T/T ~ (1/3) * delta_Phi

5. Compute n_s from the tilt of the PROJECTED spectrum at k_pivot = 0.05 Mpc^{-1}.

6. Report: n_s(KZ), comparison to 0.9649, comparison to slow-roll 0.746.

**Pre-registered gate KZ-NS-43**:
- PASS: n_s(KZ) in [0.90, 1.00]
- FAIL: n_s(KZ) outside [0.80, 1.10]

**Input**: W1-2 results, W3-2 results, `s42_gradient_stiffness.npz`
**Output**: `tier0-computation/s43_kz_transfer.{py,npz,png}`

---

