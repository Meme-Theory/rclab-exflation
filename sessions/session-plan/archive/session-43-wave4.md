## III-d. Wave 4: Structural Computations (5 tasks, parallel)

### W4-1: Off-Jensen Gradient Stiffness Z_{ij} (3×3)

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM (extends s42_gradient_stiffness.py to T1 and T2 directions)

**Prompt**:

Extend the gradient stiffness computation to the full 3×3 matrix Z_{ij} on the U(2)-invariant moduli space.

**Source**: S42 master collab T1-3 (Baptista 3.1). S42 Baptista collab Section 3.1.

**Context.** Paper 15 eq 3.79 gives the two-field kinetic energy for the (phi, sigma) parameterization:

    T = (1/2)(d_phi/dt)^2 + (5/2)(d_sigma/dt)^2

The sigma direction (T2 cross-block deformation) has kinetic coefficient 5/2 = 2.5, DIFFERENT from the Jensen coefficient of 5.0. The spectral gradient stiffness matrix is:

    Z_{ij} = sum_k (d lambda_k / d modulus_i)(d lambda_k / d modulus_j) * mult_k

Computing Z_{phi,phi}, Z_{sigma,sigma}, and Z_{phi,sigma} determines whether off-Jensen directions have lower or higher gradient cost. If an off-Jensen direction has dramatically lower Z, spatial perturbations could preferentially deform in that direction, breaking the 1D Jensen approximation.

**Computation Steps**:

1. Load `tier0-computation/s42_gradient_stiffness.py` and `tier0-computation/tier1_dirac_spectrum.py`.

2. Identify the T1 (breathing) and T2 (cross-block) deformation directions from Paper 15 Section 3.6 (U(2)-invariant moduli on SU(3)). The Jensen direction is the diagonal (2, -2, 1) in the (u(1), su(2), C^2) decomposition. T1 is the volume-preserving breathing mode. T2 is the cross-block deformation.

3. At the fold tau=0.190, compute D_K eigenvalues at 5 off-Jensen points: tau ± h in the T1 direction, tau ± h in the T2 direction, with h = 0.001.

4. Compute eigenvalue derivatives d lambda_k / d modulus_i by central finite differences for each of the 3 moduli directions (Jensen, T1, T2).

5. Construct the 3×3 matrix Z_{ij} = sum_k mult_k * (d lambda_k / d modulus_i) * (d lambda_k / d modulus_j).

6. Diagonalize Z_{ij}. Report eigenvalues and eigenvectors. The eigenvalues determine the gradient cost in each principal direction. If the smallest eigenvalue is << Z_{Jensen} = 74,731, spatial perturbations prefer that direction.

7. Cross-check: the Jensen diagonal element Z_{JJ} should reproduce 74,731 from W1-1 (S42).

**Pre-registered gate ZMATRIX-43**: INFO (structural). Report the condition number Z_max/Z_min.

**Input**: `tier0-computation/s42_gradient_stiffness.py`, `tier1_dirac_spectrum.py`, Paper 15 eq 3.60, 3.79 in `researchers/Baptista/`
**Output**: `tier0-computation/s43_offjensen_z_matrix.{py,npz,png}`

---

### W4-2: Lichnerowicz Laplacian Stability at Fold

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute eigenvalues of the Lichnerowicz Laplacian on U(2)-invariant TT 2-tensors at the fold. Any negative eigenvalue = gravitational instability threatening spatial homogeneity.

**Source**: S42 master collab T1-6 (Baptista 3.2).

**Context.** The Lauret stability formula (Paper 37 `researchers/Baptista/37_2021_Lauret_Stability_Homogeneous_Einstein_I.md`, Theorem 1.1) gives Lichnerowicz Laplacian eigenvalues on G-invariant TT tensors in terms of Casimir operators. Round SU(3) is stable (Einstein metric). Jensen-deformed fold metric is NOT Einstein. Paper 39 (Schwahn `researchers/Baptista/39_2023_Schwahn_Lichnerowicz_Laplacian_Homogeneous.md`) extends to normal homogeneous spaces. Jensen preserves U(2) isotropy (Paper 15 Section 3.6).

S20b proved "TT stability: no tachyons at any tau" for the DIRAC spectrum. The Lichnerowicz Laplacian on symmetric 2-tensors is a DIFFERENT operator with a different spectrum. Paper 48 (Semmelmann-Weingart `researchers/Baptista/48_2019_Semmelmann_Weingart_Destabilising_Einstein.md`) shows Einstein metrics CAN be destabilized by specific deformation modes.

Fold anisotropic Ricci: Ric|_{u(1)} = 1.50, Ric|_{su(2)} = 1.930, Ric|_{C^2} = 2.171 (S36 collab).

**Computation Steps**:

1. Read Papers 37, 38, 39 in `researchers/Baptista/` for the algebraic framework.

2. Construct the Lichnerowicz Laplacian Delta_L on symmetric 2-tensors restricted to U(2)-invariant TT tensors at the fold metric. Paper 37 eq 3.1 reduces this to a finite-dimensional eigenvalue problem using representation theory.

3. The Jensen metric at tau=0.190 has specific structure constants computable from `tier0-computation/tier1_dirac_spectrum.py` (orthonormal frame, connection coefficients).

4. Compute all eigenvalues of Delta_L restricted to the U(2)-invariant TT subspace.

5. Check: any negative eigenvalue means the fold is gravitationally unstable to TT perturbations. This would be a structural threat — spatial homogeneity (HOMOG-42) acquires a classical instability channel independent of quantum fluctuations.

6. Report: full eigenvalue spectrum, minimum eigenvalue, comparison to round SU(3) (where all eigenvalues are positive).

**Pre-registered gate LICHN-43**: PASS if all eigenvalues positive. FAIL if any negative (structural threat).

**Input**: Papers 37-39, 48 in `researchers/Baptista/`, fold metric from `s42_gradient_stiffness.npz`
**Output**: `tier0-computation/s43_lichnerowicz.{py,npz,png}`

---

### W4-3: Breathing Mode of 32-Cell Tessellation

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the breathing mode frequency omega_breathe — the giant monopole resonance (GMR) analog for the 32-cell fabric.

**Source**: S42 master collab T1-5 (QA 3.5). S42 Naz collab W3-1 mechanism (d). S42 QA collab Section 3.5.

**Context.** The breathing mode frequency is (QA 3.5):

    omega_breathe^2 = K_fabric / (M_fabric * R_cell^2)

where K_fabric is the bulk modulus — second derivative of total energy with respect to uniform scaling:

    K_fabric = d^2 E_total / d(alpha)^2 |_{alpha=1}

with E_total = S_fold + E_BCS + E_gradient. In nuclear physics, K = 9 * rho * d^2(E/A)/drho^2 ~ 230 MeV (nuclear compressibility). The spectral action dominates (effacement), but BCS contribution could have OPPOSITE sign (condensation LOWERS energy → d^2E_BCS/dalpha^2 could be negative if scaling weakens pairing). A negative BCS contribution would soften the breathing mode.

Naz W3-1 review mechanism (d): collective ZP energy T_ZP = 108 M_KK^4 at the fold. Zero-point oscillation of the breathing mode.

**Computation Steps**:

1. Load `s36_sfull_tau_stabilization.npz` (S_full(tau)), `s42_gradient_stiffness.npz` (Z, d2S/dtau2), `s38_cc_instanton.npz` (BCS gap data).

2. Evaluate S_fold at uniformly scaled tau: S(alpha * tau_fold) for alpha = 0.95, 0.98, 0.99, 1.00, 1.01, 1.02, 1.05.

3. Evaluate E_BCS at scaled tau using the BCS gap equation with scaled eigenvalues.

4. E_gradient = (1/2) Z * (nabla tau)^2 — for uniform scaling this contributes through the Z(tau) dependence on alpha.

5. K_spectral = d^2 S / d(alpha)^2 |_{alpha=1} (spectral action contribution to bulk modulus).

6. K_BCS = d^2 E_BCS / d(alpha)^2 |_{alpha=1} (BCS contribution — check sign).

7. K_fabric = K_spectral + K_BCS. Report sign and magnitude of each.

8. omega_breathe = sqrt(K_fabric / M_ATDHFB) / R_cell, where R_cell ~ (V_obs/32)^{1/3} / (1+z_transit).

9. Compare to nuclear GMR systematics: nuclear K ~ 230 MeV, omega_GMR ~ 80/A^{1/3} MeV.

**Pre-registered gate BREATHE-43**: INFO. If K_BCS < 0 and |K_BCS| > K_spectral, report ANOMALOUS (breathing mode unstable).

**Input**: `s36_sfull_tau_stabilization.npz`, `s42_gradient_stiffness.npz`, `s38_cc_instanton.npz`, `s40_collective_inertia.npz`
**Output**: `tier0-computation/s43_breathing_mode.{py,npz,png}`

---

### W4-4: One-Loop LIV Coefficient from KK Tower

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: HIGH

**Prompt**:

Compute the one-loop Lorentz invariance violation coefficient alpha_LIV from integrating out all 992 massive KK modes.

**Source**: S42 master collab T2-3 (QF 3B). S42 QF collab Section 3B.

**Context.** Classical spectral action Tr f(D^2/Lambda^2) preserves Lorentz invariance exactly (c_fabric = c by construction, C-FABRIC-42). But quantum corrections from integrating out massive KK modes at one loop could generate effective LIV operators suppressed by powers of M_KK/M_P.

The LHAASO bound (Paper 18 in `researchers/Quantum-Foam/18_2024_LHAASO_LIV_GRB221009A.md`): E_QG,1 > 10 E_P for linear LIV. This constrains alpha_LIV < 0.1 * M_KK/M_P ~ 10^{-2.5}.

Additional bounds (QF 3B):
- Vasileiou stochastic E_QG > 2.8 E_P (Paper 23)
- KM3NeT quadratic Lambda_2 > 5e19 GeV (Paper 27)
- IceCube decoherence L_decoh > 2e24 m (Paper 28)
- Bustamante anisotropy |c|/M_P < 1.2e-31 (Paper 29)

**Computation Steps**:

1. Load full KK spectrum from `s42_hauser_feshbach.npz` (992 eigenvalues with masses and multiplicities).

2. The one-loop effective action from integrating out a massive scalar of mass m generates LIV operators at dimension 5:

   $$\mathcal{L}_{\text{LIV}} = \frac{\alpha_{\text{LIV}}}{M_{\text{KK}}} \bar\psi \gamma^\mu \partial_\mu \partial_\nu \partial^\nu \psi$$

   The coefficient from a single KK mode is alpha_i ~ (m_i/M_KK)^2 / (16*pi^2).

3. Sum over all 992 modes: alpha_LIV = (1/(16*pi^2)) * sum_i mult_i * (m_i/M_KK)^2.

4. Compare to LHAASO threshold alpha_LIV < 10^{-2.5}.

5. Also compute the quadratic LIV coefficient beta_LIV (dimension 6 operator), relevant for the KM3NeT bound.

6. Report: alpha_LIV, beta_LIV, comparison to all 5 bounds listed above.

**Pre-registered gate LIV-43**: PASS if alpha_LIV < 10^{-2.5}. FAIL if exceeds any bound.

**Input**: `s42_hauser_feshbach.npz`, LIV papers in `researchers/Quantum-Foam/`
**Output**: `tier0-computation/s43_oneloop_liv.{py,npz,png}`

---

### W4-5: Phonon Thermal Conductivity (3-Phonon Decay)

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

Compute the 3-phonon decay rate from the B2 ~ 2*B1 near-resonance and determine the fabric's thermal conductivity.

**Source**: S42 master collab T2-4 (QA 3.3). S42 QA collab Section 3.3.

**Context.** The fabric has c_fabric = c, m_tau = 2.062 M_KK, 32-cell tessellation. omega_B2 ~ 2*omega_B1 with 0.6% detuning (S40 QRPA) provides a specific 3-phonon decay channel. The thermal conductivity is (QA 3.3):

    kappa ~ c_fabric^2 / (3 * Gamma_scattering)

The 3-phonon decay rate is:

    Gamma_{3ph} = (2*pi) * |V_3|^2 * rho_2(omega_B2) / hbar

where V_3 is the cubic anharmonic vertex and rho_2 is the 2-phonon joint DOS at B2 frequency. S41 no-Umklapp theorem: rep lattice is infinite and non-periodic → no Umklapp scattering. Only normal (momentum-conserving) processes exist. Without Umklapp, the fabric may be a perfect thermal conductor (analogous to superfluid He-4 below lambda point).

**Computation Steps**:

1. Load V_rem from `s36_mmax_authoritative.npz` and omega_B1, omega_B2 from S40 QRPA data.

2. Extract the cubic anharmonic vertex V_3 from the third-order expansion of the spectral action around the fold: V_3 = (1/6) * d^3S/dtau^3 projected onto the B2-B1-B1 channel.

3. Compute the 2-phonon joint DOS rho_2(omega) = integral delta(omega - omega_1 - omega_2) * g(omega_1) * g(omega_2) at omega = omega_B2.

4. Compute Gamma_3ph and the mean free path l_mfp = c / Gamma_3ph.

5. Compute thermal conductivity kappa = c^2 / (3 * Gamma_3ph).

6. Compare to Umklapp-free prediction: if Gamma_3ph is the ONLY scattering mechanism, report kappa. If kappa → infinity (Gamma_3ph → 0 from selection rules), the fabric is a perfect thermal conductor.

7. Nuclear benchmark: in ^4He below lambda point, kappa → infinity (second sound). Report whether the framework's fabric has the same property.

**Pre-registered gate THERM-COND-43**: INFO. Report kappa value and whether fabric is perfect conductor.

**Input**: `s36_mmax_authoritative.npz`, S40 QRPA data, `s42_gradient_stiffness.npz` (for d^3S/dtau^3)
**Output**: `tier0-computation/s43_thermal_conductivity.{py,npz,png}`

---

