## III-a. Wave 1: Root Computations (Parallel, 8 tasks)

### W1-1: Q-Theory Self-Tuning from Spectral Action

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the highest-priority open computation in the framework: whether the q-theory self-tuning mechanism (Klinkhamer-Volovik 2008, 2009) produces rho(q_0) = 0 when applied to the spectral action data.

**Context.** The CC overshoots by 80-127 orders (S42 W3-1 Step 6). All CC candidates (V_fold=250,361, |E_cond|=0.115, V_fold-V(0)=5,522, V(0.5)-V_fold=34,003) overshoot. Papers 15-16 in `researchers/Volovik/` introduce vacuum variable q that self-tunes to rho(q_0) = 0 at equilibrium. Paper 23 connects to volume-preserving deformations: det(e) = const ↔ Jensen det(g) = const (proven S12). The Gibbs-Duhem relation rho = epsilon - q * d_epsilon/dq gives the gravitating vacuum energy. At equilibrium, rho = 0 by thermodynamic identity.

S42 R4 Q4 (Volovik scales workshop): Paper 05 theorem APPLIES because equilibrium needs to EXIST asymptotically, not to have been occupied. tau=0 IS the ground state (zero vacuum energy). All Lambda is perturbative from GGE. Q-theory self-tuning timescale tau_q ~ 3e-4 M_KK^{-1} << H^{-1}: system already at q-equilibrium.

Nazarewicz Sugg 4 (S42 collab): GCM zero-point E_ZP = (1/2)*omega_0 = (1/2)*433 = 216.5 M_KK. Is this included in S_fold or an independent correction? If independent, E_ZP/S_fold = 8.7e-4 (0.087%) — largest identified CC correction. See W1-8 for this computation.

Nazarewicz Q3: Correct Friedmann functional is a_0/(2*(4pi)^2), NOT S_fold. Factor 111x error caught in HOMOG-42 v1→v2.

QF Q1: Does Carlip work at Lambda ~ 10^{-9} M_P^4? W1-1 provides Lambda_internal for F-FOAM-5 (W2-3).

CW Q1: Does Volovik Gibbs-Duhem spectral analog exist? This is what W1-1 tests.

**Computation Steps**:

1. Load spectral action data from `tier0-computation/s36_sfull_tau_stabilization.npz` (fields: `tau_combined`, `S_full`) and gradient stiffness from `tier0-computation/s42_gradient_stiffness.npz` (fields: `tau_grid`, `Z_spectral`, `dS_dtau`, `d2S_dtau2`, `S_total`).

2. **Identify the q-variable.** Following Paper 15 (Section "Vacuum Variable Framework") and Paper 23 (Section "Volume-Preserving Deformations as Fundamental"): the vacuum variable q for the framework is NOT tau itself but the thermodynamic potential. In a condensed matter system, q is the conserved charge of the equilibrium. For the BCS condensate on SU(3), q is the vacuum charge density — proportional to the pair density. Following Paper 16 (gluonic vacuum), q is analogous to the gluon condensate magnitude. In the framework, this maps to |Delta|^2 (BCS gap squared), computable from `tier0-computation/s38_cc_instanton.npz`.

3. **Construct rho(q).** The vacuum energy density entering the gravitational field equations is (Paper 05, Section "Four Sources"):

   $$\rho = \epsilon(q) - q \frac{d\epsilon}{dq}$$

   where epsilon(q) is the microscopic energy density as a function of q. This is the Gibbs-Duhem relation for the vacuum. At equilibrium, rho = 0 because the system minimizes its thermodynamic potential.

   For the framework: epsilon(q) = S_full(tau(q)) * M_KK^4. The relationship between q and tau: q = n_pairs * M_KK^3 (pair density from BCS gap). At the fold tau=0.190, n_pairs = 59.8 (S38). At tau=0, n_pairs = 0.

   Compute rho(q) = epsilon - q * d_epsilon/dq at each tau point.

4. **Test rho(q_0) = 0.** Plot rho(q) vs q. Determine whether rho crosses zero anywhere in q ∈ [0, q_max]. If it crosses at q_0, self-tuning condition is satisfied in principle.

5. **If rho(q_0) = 0 exists, compute residual CC from GGE perturbation.** Following Paper 15 Section "Imperfect Vacuum": for an imperfect vacuum with quasiparticle matter density rho_matter = E_exc = 50.9 M_KK (from S38 E-GGE-42):

   $$\rho_\Lambda \sim \frac{1}{2} \frac{d^2\rho}{dq^2}\bigg|_{q_0} (\delta q)^2$$

   where delta_q ~ sqrt(rho_matter / (d^2_rho/dq^2)).

6. **Q-field dynamics.** Write the q-field EOM q_ddot + 3H*q_dot + d_rho/dq = 0 and compute:
   - Q-oscillation frequency omega_q = sqrt(d^2_rho/dq^2 |_{q_0})
   - Relaxation timescale tau_q ~ 1/omega_q
   - Hubble friction ratio 3H/omega_q (using H_0 = 2.184e-18 s^{-1})
   - Whether tau_q << H^{-1} (system already at q-equilibrium, as estimated in S42 R4: tau_q ~ 3e-4 M_KK^{-1})

7. **Dimensional CC estimate.** Following Paper 16: Lambda ~ K^3/E_Pl^2 where K = M_KK. Compute Lambda ~ M_KK^3/M_Pl^2 and compare to Lambda_obs = 2.9e-122 M_Pl^4.

8. **Cross-check: Alternative q identifications.** Test q = tau (naive), q = |Delta|^2 (BCS gap), q = S_fold(tau) (spectral action), q = n_pairs (pair count). Report rho(q) for each identification. At least one should produce a zero crossing if q-theory applies.

**Pre-registered gate QFIELD-43**:
- PASS: rho(q_0) = 0 exists AND residual rho_Lambda < 10^{-40} GeV^4
- FAIL: No zero crossing for ANY q identification, OR residual > 10^{-10} GeV^4
- Null: rho monotonic positive for all identifications. Framework inherits CC.

**Input files**:
- `tier0-computation/s36_sfull_tau_stabilization.npz` — S_full(tau) at 16 tau points
- `tier0-computation/s42_gradient_stiffness.npz` — Z(tau), dS/dtau, d2S/dtau2, S_total
- `tier0-computation/s38_cc_instanton.npz` — instanton gas parameters, gap data
- `tier0-computation/s42_gge_energy.npz` — GGE energy budget (E_exc = 50.9 M_KK)
- `tier0-computation/s42_constants_snapshot.npz` — M_KK routes (gravity 7.4e16, gauge 5.0e17)
- `researchers/Volovik/05_2005_Volovik_Vacuum_Energy_Cosmological_Constant.md`
- `researchers/Volovik/15_2008_Klinkhamer_Volovik_Self_Tuning_Vacuum.md`
- `researchers/Volovik/16_2009_Klinkhamer_Volovik_Gluonic_Vacuum_Q_Theory.md`
- `researchers/Volovik/23_2023_Nissinen_Volovik_Tetrads_q_Theory_Volume_Preserving.md`

**Output files**:
- Script: `tier0-computation/s43_qtheory_selftune.py`
- Data: `tier0-computation/s43_qtheory_selftune.npz`
- Plot: `tier0-computation/s43_qtheory_selftune.png`

**Critical notes**:
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
- Read ALL four Volovik papers FIRST. Paper 15 Section "Vacuum Variable Framework" defines q. Paper 23 connects det(e)=const to volume-preserving deformations. Paper 05 Section "Four Sources" gives the Gibbs-Duhem relation. Paper 16 gives the dimensional estimate.
- The q→tau mapping is the critical step. If q = tau naively, rho = S_full - tau * dS/dtau, which CAN have a zero because S_full is sublinear in tau (S_full(0) = 244,839, S_full(0.5) = 284,364 — grows slower than linearly). Check this numerically.
- Report ALL intermediate numbers. Cross-check between q identifications is essential.
- The GCM zero-point correction (W1-8) may modify the result. Note this dependency but proceed with the uncorrected S_fold.

---

### W1-2: Lifshitz Transition Classification at the Fold

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM (eigenvalue trajectory analysis at multiple tau, topological invariant computation)

**Prompt**:

You are classifying the Lifshitz transition type at the fold (tau=0.190) using Volovik's classification scheme (Papers 24, 33 in `researchers/Volovik/`).

**Context.** The fold is a Lifshitz transition where N_eff jumps 32→240 (S41 step function), Van Hove singularity M_max=1.674 (S35), BCS instability 1D theorem (S35). S42 scales workshop R1 (Volovik) preliminarily classified as "Type I + Type 5" but this was not computed.

Paper 24 (`researchers/Volovik/24_2016_Volovik_Zhang_Type_II_Weyl_Lifshitz_Transition.md`) defines tilting parameter alpha = v_parallel/v_perp. The Lifshitz transition occurs at alpha=1 (type I/type II boundary). Paper 33 (`researchers/Volovik/33_2017_Volovik_Exotic_Lifshitz_Transitions_Topological_Materials.md`) provides 5-type classification: Type I (Fermi surface pinch-off), Type II (saddle-point), Dirac-to-Weyl, Weyl pair production, band inversion.

Classification determines:
1. Van Hove exponent → KZ universality class → n_s. The 52-sigma failure (NS-TILT-42, eta=0.243 structural) closes slow-roll permanently. KZ is sole surviving route (Tesla 3a, Baptista Q4, QF 4C all identify this).
2. Whether fold has horizon structure (Hawking-type vs Parker-type pair creation)
3. Topological invariant that changes (Chern/winding/Hopf)
4. DOS scaling N(E) ~ |E - E_c|^gamma near the fold

S42 Tesla diagnosis: eta measures Gruneisen parameter frequency-dependence. Jensen is non-conformal. Mode-dependent differential shifts produce eta ~ 0.24.

S42 Baptista warning: standard 3D Ising gives n_s - 1 = -0.89 (too red). Mean-field gives -1.0. KZ route requires non-standard universality class. Paper 47 (hyperbolic BCS) may provide curvature corrections.

S42 Tesla 3a: KZ power spectrum at KK scale is flat (n_s = 1) because k_pivot << 1/xi_KZ. Tilt comes from transfer function, not KZ spectrum alone.

W1-4 (phonon DOS) provides the raw eigenvalue histogram that feeds this computation.

**Computation Steps**:

1. Load eigenvalue data from `tier0-computation/s41_spectral_refinement.npz` and `tier0-computation/s36_sfull_tau_stabilization.npz`. Also load BCS data from `tier0-computation/s35_ed_corrected_dos.npz` and `tier0-computation/s36_mmax_authoritative.npz`.

2. **Extract eigenvalue trajectories lambda_i(tau)** for i=1,...,16 in the (0,0) singlet sector across a dense tau grid (at least 20 points from 0.05 to 0.30). Use `tier0-computation/tier1_dirac_spectrum.py` to recompute if needed.

3. **Identify the gap-edge eigenvalues** (closest to zero, participating in BCS pairing). Track trajectories through the fold.

4. **Compute the tilting parameter.** For each gap-edge eigenvalue lambda_i(tau):

   $$\alpha_i(\tau) = \frac{|d\lambda_i/d\tau|}{|\lambda_i(\tau)|}$$

   At the Lifshitz transition, alpha → infinity (eigenvalue crosses zero) or alpha = 1 (tilt equals cone velocity). Classify which occurs.

5. **Count topological changes.** Track eigenvalues that change sign as tau crosses 0.190. Each sign change is band inversion (Type 5). Count Fermi surface pockets (positive) vs holes (negative) at each tau.

6. **Compute Van Hove exponent.** Near the fold, DOS diverges as N(E) ~ |E - E_c|^gamma. From eigenvalue spacing at fold, extract gamma. Standard Type I in 3D: gamma = 1/2. Framework's 8D internal space reduced to 1D tau: gamma may differ. M_max = 1.674 constrains gamma.

7. **Determine KZ universality class.** Dynamic critical exponents (z, nu) follow from Lifshitz type. For KZ perturbation spectrum:

   $$n_s - 1 = -\frac{2z\nu + d}{z\nu + 1}$$

   where d is spatial dimension of defect network. Standard z=1, nu=1/2 (mean field): n_s = 0.67 (worse than S42's 0.746). Determine whether actual universality class gives z, nu compatible with n_s ~ 0.96.

8. **Classify.** State Lifshitz type (I through V per Paper 33), Van Hove exponent, topological invariant that changes, KZ dynamic exponents.

**Pre-registered gate LIFSHITZ-43**:
- PASS: Type uniquely identified + Van Hove exponent computed + KZ n_s > 0.90
- FAIL: Ambiguous OR KZ n_s < 0.80
- INFO: Type classified but KZ exponents undetermined
- Null: Standard Type I, gamma=1/2, z=1, nu=1/2 → n_s ~ 0.67 (WORSE than S42)

**Input files**:
- `tier0-computation/tier1_dirac_spectrum.py`
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`
- `tier0-computation/s36_mmax_authoritative.npz`
- `tier0-computation/s35_ed_corrected_dos.npz`
- `researchers/Volovik/24_2016_Volovik_Zhang_Type_II_Weyl_Lifshitz_Transition.md`
- `researchers/Volovik/33_2017_Volovik_Exotic_Lifshitz_Transitions_Topological_Materials.md`

**Output files**:
- Script: `tier0-computation/s43_lifshitz_class.py`
- Data: `tier0-computation/s43_lifshitz_class.npz`
- Plot: `tier0-computation/s43_lifshitz_class.png`

**Critical notes**:
- Read BOTH Volovik papers first. Paper 24 defines the tilting parameter. Paper 33 gives the 5-type classification with examples.
- The spectral flow (eigenvalue sign changes) connects to W1-3 baryogenesis. Share eigenvalue trajectory data.
- If eigenvalue trajectories need recomputation at denser tau grid, use tier1_dirac_spectrum.py (~8.7s per tau point per sector).

---

### W1-3: K_7 Chiral Anomaly Diagnostics at the Fold

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: LOW (matrix algebra on existing Kosmann and K_7 matrices)

**Prompt**:

You are computing diagnostics for baryogenesis via the K_7 chiral anomaly at the fold, following Volovik's 3He-A analog (Paper 09 in `researchers/Volovik/`).

**Context.** [iK_7, D_K] = 0 at ALL tau (S34 permanent). Jensen breaks SU(3) → U(1)_7 × SU(2) exactly. Cooper pairs carry K_7 = ±1/2 (S35). BCS condensate breaks U(1)_7 spontaneously.

S42 Dirac review: "Structural Triangle" {[J,D_K]=0, effacement 10^{-6}, eta_kinematic 10^{-9}}. Most vulnerable vertex: J-symmetry at domain wall. eta_kinematic = 3.4e-9 is CP-even ceiling, not prediction. eta_net = eta_kin * epsilon_CP. Framework has no epsilon_CP. LHCb Paper 21: A_CP = 2.45% in baryon decays at 5.2 sigma.

Paper 09 (`researchers/Volovik/09_1998_Volovik_Axial_Anomaly_3He_A_Baryogenesis.md`): chiral anomaly produces baryon-like asymmetry through spectral flow at vortices. In the framework: K_7 → baryon number, Jensen texture → l-vector analog, domain walls → vortex analogs.

S42 Nazarewicz F/K addendum: B2 (adjoint) is baryon-neutral. Baryogenesis from DECAY into (1,0)+(0,1) fundamental channels. Two-stage cascade: Stage 1 (KK redistribution, DR=1.51), Stage 2 (F-level exit to SM).

S42 Dirac Q3: BDI constrains baryogenesis — P-type channel only (S41: S_F^Connes = 0).

Sakharov: (1) K_7 violation via spectral flow, (2) CP via [J, iK_7], (3) departure from equilibrium (fold transit).

This is DIAGNOSTIC. Full J-odd at wall (W3-3) and chiral eta (W3-4) follow in Wave 3.

**Computation Steps**:

1. Load Dirac infrastructure from `tier0-computation/tier1_dirac_spectrum.py` and Kosmann matrices from `tier0-computation/s23a_kosmann_singlet.py`.

2. **Compute K_7 matrix in B2 sector.** Load K_7 generator (index 6 in SU(3) generators from `su3_generators()`). Construct iK_7 in 16×16 spinor representation. Verify [iK_7, D_K(tau)] = 0 at tau=0.190.

3. **Compute J (real structure) in spinor representation.** J = gamma_1 * gamma_3 * gamma_5 * gamma_7 (corrected form from S34). Verify J^2 = +1 (BDI class T^2 = +1).

4. **Test CP violation: [J, iK_7].** Compute commutator [J, iK_7] in 16×16 representation. If nonzero: J does NOT commute with K_7 generator → CP violation needed for baryogenesis EXISTS.

5. **Spectral flow diagnostic.** At the fold, count eigenvalues that change K_7 quantum number as they cross:

   $$\Delta N_{K_7} = N_{K_7}(\tau=0.20) - N_{K_7}(\tau=0.18)$$

   where N_{K_7} = sum over occupied states of their K_7 eigenvalue. Share eigenvalue trajectory data with W1-2.

6. **Eta invariant at the fold.** APS eta invariant:

   $$\eta_D = \sum_i \text{sign}(\lambda_i) |\lambda_i|^{-s}\bigg|_{s=0}$$

   Compute at tau = 0.17, 0.18, 0.19, 0.20, 0.21, 0.22. Change Delta_eta across fold gives anomaly coefficient.

7. **Asymmetry estimate.** If [J, iK_7] != 0 and spectral flow nonzero:

   $$\eta \sim \frac{\Delta N_{K_7}}{N_{\text{total}}} \cdot \frac{\Delta\eta}{\eta_{\text{total}}} \cdot \frac{E_{\text{BCS}}}{E_{\text{GGE}}}$$

   Compare to observed eta = 6.12e-10.

**Pre-registered gate BARYO-K7-43**:
- PASS: [J, iK_7] != 0 AND spectral flow != 0 AND eta within 10 OOM
- FAIL: [J, iK_7] = 0 OR spectral flow = 0
- INFO: CP violation exists but asymmetry unreliable
- Null: J and K_7 both diagonal → no CP violation

**Input files**:
- `tier0-computation/tier1_dirac_spectrum.py`
- `tier0-computation/s23a_kosmann_singlet.py`
- `tier0-computation/s35_k7_dphys.npz`
- `tier0-computation/s35_pfaffian_corrected_j.npz`
- `researchers/Volovik/09_1998_Volovik_Axial_Anomaly_3He_A_Baryogenesis.md`

**Output**: `tier0-computation/s43_baryo_k7.{py,npz,png}`

---

### W1-4: Phonon DOS Histogram at the Fold

**Agent**: `quantum-acoustics-theorist`
**Model**: opus
**Cost**: ZERO (existing data, simple histogram)

**Prompt**:

Compute the phonon density of states at the fold from all 992 D_K eigenvalues with multiplicity weighting. Identify van Hove singularities, cumulative distribution, per-sector decomposition. Feeds W1-2 (Lifshitz classification).

**Source**: S42 master collab T0-1 (QA 3.2).

**Computation Steps**:

1. Load eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz` (contains all 992 eigenvalues at fold with sector labels and multiplicities).

2. Construct multiplicity-weighted histogram rho(omega) with bins of width 0.02 M_KK across [0.8, 2.1] M_KK.

3. Compute cumulative distribution N(omega) = integral_0^omega rho(omega') d_omega'.

4. Identify van Hove singularities: peaks in rho(omega) corresponding to band edges, saddle points, and flat regions. Classify each as M_0 (minimum), M_1 (saddle), M_2 (maximum), or M_3 (flat band) type.

5. Per-sector decomposition: separate histograms for (0,0), (1,0)+(0,1), (1,1), (2,0)+(0,2), (3,0)+(0,3), (2,1)+(1,2).

6. Report: total bandwidth, spectral gap, number of van Hove singularities, flat-band fraction (bandwidth < 0.05 M_KK per sector).

**Pre-registered gate DOS-43**: INFO (diagnostic, no PASS/FAIL — feeds W1-2).

**Input**: `tier0-computation/s42_hauser_feshbach.npz`
**Output**: `tier0-computation/s43_phonon_dos.{py,npz,png}`

---

### W1-5: Modulus Fluctuation Angular Blur vs Perlman Bound

**Agent**: `quantum-foam-theorist`
**Model**: opus
**Cost**: ZERO (existing HOMOG-42 numbers)

**Prompt**:

Verify that random-walk modulus fluctuations coupled through the spectral action produce angular blur below the Perlman bound (Paper 12 eq P12-1 in `researchers/Quantum-Foam/`).

**Source**: S42 master collab T0-2 (QF 3D). S42 QF collab Section 3D: "the effacement ratio likely saves the prediction" but computation not done.

**Computation Steps**:

1. From HOMOG-42: delta_tau_transit = 1.75e-6 * tau_fold = 3.3e-7. L_H at transit ~ 10^{42} l_P.

2. Modulus fluctuation at distance l: delta_tau(l) ~ delta_tau_transit * sqrt(l / L_H) (random walk of KZ domains).

3. Coupling to external metric: delta_g/g ~ (dS/dtau / S) * delta_tau ~ 0.234 * delta_tau.

4. Angular blur: delta_theta ~ delta_g * (l_P / l)^{1/2} for distant sources.

5. Compare to Perlman bound delta_theta < 10^{-27} arcsec.

6. Report: is the framework below the Perlman bound? By how many orders?

**Pre-registered gate PERLMAN-43**: INFO.

**Input**: `tier0-computation/s42_homogeneity.npz`, `tier0-computation/s42_gradient_stiffness.npz`
**Output**: `tier0-computation/s43_perlman_blur.{py,npz,png}`

---

### W1-6: Paper 16 Adiabaticity Diagnostic

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: ZERO (existing eigenvalue derivative data)

**Prompt**:

Compute |d ln lambda/dtau| * |dtau/dt| vs lambda at the fold. Independent confirmation of TAU-DYN shortfall via Paper 16 (`researchers/Baptista/24_2016_Gauge_Coupling_evolution_5D_Weinberg.md`) mass variation framework.

**Source**: S42 master collab T0-6 (Baptista 3.3). S42 Baptista collab Section 3.3: adiabaticity criterion |d ln m/(m dt)| < m violated by factor ~83,000.

**Computation Steps**:

1. Load eigenvalue derivatives from `tier0-computation/s42_gradient_stiffness.npz` (d_lambda/d_tau per eigenvalue).

2. Transit velocity dtau/dt ~ dS/dtau / M_ATDHFB = 58,673 / 1.695 = 34,615.

3. For each eigenvalue lambda_i, compute adiabaticity ratio:

   $$R_i = \frac{|d\ln\lambda_i/d\tau| \cdot |d\tau/dt|}{|\lambda_i|}$$

   R > 1 means non-adiabatic. Plot R_i vs lambda_i for all 992 eigenvalues.

4. Report: fraction of eigenvalues with R > 1, R > 10, R > 100. Maximum R. Mean R by sector.

**Pre-registered gate ADIAB-43**: INFO (independent TAU-DYN cross-check).

**Input**: `tier0-computation/s42_gradient_stiffness.npz`, `tier0-computation/s42_hauser_feshbach.npz`
**Output**: `tier0-computation/s43_adiabaticity.{py,npz,png}`

---

### W1-7: Pair Transfer Form Factor at Finite Momentum

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: ZERO (8×8 trace over existing BdG amplitudes)

**Prompt**:

Compute the pair transfer form factor F(q) = <GGE| P^+(q) |GGE> where P^+(q) is the pair creation operator at finite momentum q in KK representation space. Determines whether GGE pairs are spatially extended (relevant for fabric domain walls) or localized (relevant for tessellation).

**Source**: S42 Nazarewicz collab Suggestion 5. "An 8×8 trace over existing BdG amplitudes u_k, v_k. Cost: minutes."

**Computation Steps**:

1. Load BdG amplitudes from `tier0-computation/s37_pair_susceptibility.npz` (u_k, v_k for 8 modes).

2. Construct pair creation operator P^+(q) = sum_k u_k(q) * v_k(-q) * c^+_k * c^+_{-k} in momentum space.

3. Compute F(q) = sum_k u_k * v_k * exp(i*q*r_k) for q values spanning [0, 10] M_KK.

4. Classify: F(q) ~ 1/q (extended BCS) or F(q) ~ delta(q) (localized BEC). The crossover criterion is xi_pair * q_max where xi_pair is the pair coherence length (1.118 M_KK^{-1} from S37).

5. Report: F(q) profile, pair spatial extent, BCS vs BEC character.

**Pre-registered gate PAIR-FF-43**: INFO.

**Input**: `tier0-computation/s37_pair_susceptibility.npz`
**Output**: `tier0-computation/s43_pair_form_factor.{py,npz,png}`

---

### W1-8: GCM Zero-Point Correction to S_fold

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: ZERO (analytic, 30 minutes)

**Prompt**:

Determine whether the spectral action S_fold = 250,361 includes or excludes the collective zero-point energy E_ZP = (1/2)*omega_0 = 216.5 M_KK from the tau modulus oscillation. If excluded, compute the corrected S_fold and its impact on the CC estimate.

**Source**: S42 Nazarewicz collab Suggestion 4. "E_ZP/S_fold = 8.7e-4 (0.087%). In nuclear physics, GCM zero-point correction is 0.03-0.1% — a genuine beyond-mean-field effect."

**Computation Steps**:

1. omega_0 = sqrt(d2S/dtau2 / M_ATDHFB) = sqrt(317,863 / 1.695) = 433 M_KK.

2. E_ZP = (1/2) * omega_0 = 216.5 M_KK.

3. In the GCM framework (Paper 13 in `researchers/Nazarewicz/`): E_HFB(q_0) does NOT include GCM zero-point. Corrected: E_GCM = E_HFB + E_ZP.

4. By analogy: if S_fold is analogous to E_HFB, then E_ZP is a REAL correction. S_fold_corrected = S_fold + E_ZP = 250,361 + 217 = 250,578.

5. But: the spectral action Tr f(D^2/Lambda^2) at fixed tau already sums over ALL eigenvalues including their zero-point contributions. The question is whether the COLLECTIVE tau oscillation adds to this or is already captured.

6. Resolve by comparing: S_fold includes sum_i (1/2)*omega_i for each D_K eigenvalue (these ARE included — they are the eigenvalues). The collective mode omega_0 = 433 is a DIFFERENT mode — it describes oscillation of tau itself, not oscillation of individual eigenvalues. In nuclear DFT: HFB includes single-particle zero-point but NOT collective zero-point. By analogy, E_ZP is genuinely beyond S_fold.

7. Report: E_ZP magnitude, classification (included/excluded), corrected S_fold, impact on CC via W1-1.

**Pre-registered gate GCM-ZP-43**: INFO (feeds W1-1).

**Input**: `tier0-computation/s42_gradient_stiffness.npz`, `tier0-computation/s40_collective_inertia.npz`
**Output**: `tier0-computation/s43_gcm_zeropoint.{py,npz,png}`

---

