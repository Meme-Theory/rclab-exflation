# Session 70 Plan: Leggett Vacuum, Alpha_s Resolution, Observational Chain Refinement

**Date**: 2026-04-05
**Author**: Van den Dungen (bridge theorist, planner)
**Format**: Compute (wave-based parallel independent agents)
**Source**: S69 master collab synthesis (9 reviewers, 40 computations + 2 housekeeping), S69 working paper, S69 Bucher singularity review, EVOI framework, VdD agent memory
**Motivation**: S69 passed 9/9 data tests, narrowed A_s gap to 0.485 OOM, established 7 BCS protections and 2 permanent theorems (off-Jensen gradient, alpha_s structural = 0). The remaining gap is dominated by a single computable unknown: the Leggett vacuum state at the transit boundary. The strongest particle-physics tension (alpha_s = 0.022 vs observed 0.1180) requires systematic resolution. The observational chain needs sharpening with full covariance matrices and Boltzmann-level ISW.
**Results file**: `sessions/archive/session-70/session-70-results-workingpaper.md`

---

## I. Session Objective

Session 70 attacks the three highest-EVOI questions simultaneously:

1. **LEGGETT-VACUUM-70** (CRITICAL, 7/9 reviewers): Solve the Mathieu equation for the relative phase phi_{23} during the BCS transit. If r_L > 0.3, the A_s gap drops from 0.485 to approximately 0.312 OOM -- the single largest remaining correction. If r_L = 0 (adiabatic limit), the squeeze channel is exhausted and the gap remains at 0.485 OOM.

2. **F0-ALPHA-S-70** (CRITICAL, 3/9 reviewers): The alpha_s(M_Z) = 0.022 extraction is 5.4x below the observed 0.1180. Scan the spectral function normalization f_0, test non-perturbative spectral action at Lambda = 2.048, and determine whether a consistent f_0 exists that simultaneously accommodates alpha_s and m_H.

3. **Q-SOUND-70** (CRITICAL, 2/9 reviewers): The ISW tracking signal (7.6% FW/Quint) -- the substrate-specific discriminant -- rests on c_s^2 = 0 as an assumption, not a derivation. Derive c_s^2 from the spectral action q-variable. PASS = prediction; FAIL = assumption.

Additionally: complete the Bell-GGE test (NOT STARTED from S69), sharpen observational fits with full covariance, extend PW to L_max=7, test parametric resonance for A_s, and execute 5 Bucher singularity tests connecting phase-singularity universality to the GGE relic.

**Pre-registered master gates**:

- **LEGGETT-VACUUM-70**: PASS if r_L > 0.3 (non-adiabatic excitation), FAIL if r_L = 0 (adiabatic)
- **F0-ALPHA-S-70**: PASS if consistent f_0 exists in [0.5, 5.0] giving alpha_s in [0.10, 0.13], FAIL if no such f_0 exists
- **Q-SOUND-70**: PASS if c_s^2 = 0 derived from spectral action, FAIL if c_s^2 = 1

---

## II. Wave Structure

### Dependency Graph

```
Wave 1 (parallel, no dependencies -- 3 CRITICAL + 2 HOUSEKEEPING + 5 HIGH):
  W1-A: LEGGETT-VACUUM-70 (CRITICAL)
  W1-B: F0-ALPHA-S-70 (CRITICAL)
  W1-C: Q-SOUND-70 (CRITICAL)
  W1-D: BCS-GAP-CANONICAL (HOUSEKEEPING)
  W1-E: RATIO-GILKEY-DOCUMENT (HOUSEKEEPING)
  W1-F: BELL-GGE-70 (HIGH)
  W1-G: NON-PERT-SA-70 (HIGH)
  W1-H: PARAMETRIC-GGE-70 (HIGH)
  W1-I: TRAPPED-ACOUSTIC-70 (HIGH)
  W1-J: LMAX7-PW-70 (HIGH)

    Decision Point: W1-A determines A_s gap final budget (0.312 vs 0.485 OOM)
    Decision Point: W1-B determines if alpha_s tension is normalization or structural
    Decision Point: W1-C determines if ISW tracking is prediction or assumption
    Decision Point: W1-D establishes canonical Delta for all subsequent scripts

Wave 2 (parallel, W2-A/D may use W1-D canonical Delta; others independent):
  W2-A: FULL-COV-PANTHEON-70 (HIGH)
  W2-B: FULL-COV-RSD-70 (HIGH)
  W2-C: CLASS-ISW-70 (HIGH)
  W2-D: PHI-EFF-COMPOUND-70 (HIGH)
  W2-E: VOID-SIZE-70 (HIGH)

    Decision Point: W2-A/B sharpen Delta_chi^2 vs LCDM (currently -5.66)
    Decision Point: W2-C validates ISW at Boltzmann level

Wave 3 (parallel, no dependencies on W1/W2):
  W3-A: BERRY-DENNIS-GGE-70 (MEDIUM, Bucher Test 1)
  W3-B: SUPERLUMINAL-FRACTION-70 (MEDIUM, Bucher Test 2)
  W3-C: GGE-PAIR-CORRELATION-70 (MEDIUM, Bucher Test 3)
  W3-D: ANNIHILATION-TIME-70 (MEDIUM, Bucher Test 4)
  W3-E: DISCRETE-BERRY-DENNIS-70 (MEDIUM, Bucher Test 5)
  W3-F: ZETA-AS-BUDGET-70 (MEDIUM)
  W3-G: LEGGETT-MOMENT-70 (MEDIUM)
  W3-H: PENROSE-SEQUENCE-70 (MEDIUM)
  W3-I: KRETSCHNER-BCS-70 (MEDIUM)
  W3-J: MEISSNER-ED-70 (MEDIUM)

    Decision Point: W3-A through W3-E determine if Berry-Dennis universality
    applies to the GGE relic (Bucher bridge)

Wave 4 (parallel, independent):
  W4-A: HYDROSTATIC-CLUSTER-70 (MEDIUM)
  W4-B: CHIRP-PENUMBRA-70 (MEDIUM)
  W4-C: CAVITY-BCS-HORIZON-70 (MEDIUM)
  W4-D: AP-VOID-70 (MEDIUM)
  W4-E: BULK-FLOW-70 (MEDIUM)
  W4-F: BETTI-FISHER-70 (MEDIUM)
  W4-G: OFF-JENSEN-HESS-70 (MEDIUM)
  W4-H: SPECTRAL-DIM-FLOW-70 (MEDIUM)
  W4-I: BCS-PROXIMITY-70 (MEDIUM)

    Decision Point: W4-B/C advance the acoustic analog program
    Decision Point: W4-G completes off-Jensen characterization (perpendicular Hessian)

Wave 5 (parallel, no dependencies -- LOW level):
  W5-A: DM-PAIR-DECAY-70 (LOW)
  W5-B: KURAMOTO-SYNC-70 (LOW)
  W5-C: WEYL-NP-SCALARS-70 (LOW)
  W5-D: NEAR-EXTREMAL-70 (LOW)
  W5-E: BAO-PEAK-DAMP-70 (LOW)
  W5-F: VOID-CS2-70 (LOW)
  W5-G: PDF-FOLDED-70 (LOW)
  W5-H: EPSH-ALPHA-SENSITIVITY-70 (LOW)
  W5-I: CONSISTENCY-FI-MAP-70 (LOW)
  W5-J: 3-MODE-BAW-70 (LOW)
  W5-K: DESI-DR3-UPDATE-70 (LOW)
  W5-L: GEODESIC-MODULI-70 (LOW)

    Decision Point: W5-A determines Leggett DM observability
```

---

## III. Wave 1: Critical Priority + Housekeeping + High Priority

### W1-A: LEGGETT-VACUUM-70 -- Mathieu Equation for Leggett Phase During Transit

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: Mack, Volovik, VdD, Lizzi, Tesla, Phonon-First, SP (7/9 reviewers)

**Prompt**:

This is the single highest-EVOI computation in the project. The A_s gap stands at 0.485 OOM. The non-BD squeeze from SQUEEZE-RECON-69 contributed +0.226 OOM assuming r_L = 0 (Bunch-Davies vacuum at the Leggett transition). If the Leggett mode is non-adiabatically excited during the BCS transit, r_L > 0, and the squeeze parameter increases to r_L = arctanh(Delta/E_F) = 0.617, giving +0.443 OOM total (the W1-F upper bound). The difference is 0.217 OOM -- the single largest computable correction.

The physical question: does the relative phase phi_{23} between B2 and B3 BCS sectors remain in its ground state during the transit, or does the sudden onset of the Leggett potential non-adiabatically excite it?

**Method**: The Leggett mode obeys a Mathieu-type equation during the BCS onset:

  d^2 phi_{23}/dt^2 + Gamma_L * d(phi_{23})/dt + Omega_L^2(t) * sin(phi_{23}) = 0

where Omega_L(t) is the Leggett frequency that turns on as the BCS gap opens. The key dimensionless parameter is the suddenness ratio:

  eta = Omega_L * dt_BCS_onset

where Omega_L = omega_L1 = 0.138 M_KK (from canonical_constants.py, S52 GL-Josephson) and dt_BCS_onset is the timescale over which the BCS gap goes from 0 to Delta_0.

From the S69 four-speed computation (FOUR-SPEED-69), the 3He-B parent system provides the prediction: the answer depends on eta. If eta >> 1 (adiabatic), r_L = 0. If eta << 1 (sudden quench), r_L = arctanh(Delta/E_F).

Import all constants from `computations/canonical_constants.py`. Key values: omega_L1 = 0.138 M_KK, Delta_0_OES = 0.464 M_KK, dt_transit = 0.00113 M_KK^{-1}, E_B2_mean = 0.845 M_KK, v_terminal = 26.545 M_KK.

**Computation**:
1. Determine the BCS onset timescale dt_BCS. The BCS gap turns on as the system crosses the Pomeranchuk instability. Use the transit speed v_terminal = 26.545 (dtau/dt at fold) and the width of the BCS onset region delta_tau_BCS. Estimate delta_tau_BCS from the Thouless criterion: the BCS gap opens when the pairing susceptibility diverges, which occurs over a window delta_tau ~ Delta_0 / (dE/dtau) where dE/dtau is the rate of change of the B2 level energy at the fold.
2. Compute the suddenness parameter eta = omega_L1 * dt_BCS. Three regimes:
   - eta >> 1: Adiabatic. phi_{23} remains in ground state. r_L = 0.
   - eta ~ 1: Intermediate. Solve Mathieu equation numerically.
   - eta << 1: Sudden quench. r_L = arctanh(Delta_0_OES / E_B2_mean).
3. For the intermediate regime, solve the linearized Mathieu equation:
   d^2 u/dt^2 + [Omega_L(t)]^2 * u = 0
   where Omega_L(t) = omega_L1 * tanh(t / dt_BCS) (smooth turn-on profile). Use scipy.integrate.solve_ivp with u(t=0) = 0, du/dt(t=0) = omega_L1/2 (zero-point fluctuation). Compute the Bogoliubov coefficient:
   beta = |<0_out|1_in>|^2 = (1/2) * |u_out / u_in - 1|^2
   The squeeze parameter is r_L = arcsinh(sqrt(|beta|^2)).
4. Scan dt_BCS over a factor-of-10 range around the central estimate to bracket r_L.
5. Compute the A_s correction: delta_OOM = log10(cosh(2*r_L)) - log10(cosh(0)) for the squeeze contribution.
6. Cross-check with 3He-B: the parent system has omega_L^{3He} / omega_transit^{3He} ~ 0.1 (sudden quench regime), giving r_L^{3He} > 0. The FOUR-SPEED-69 scaling A_fw/A_3He = 0.95 predicts the framework ratio should be similar.

**Input files**:
- `computations/canonical_constants.py` (all constants)
- `computations/s69_four_speed.npz` (speed hierarchy, scaling ratios)
- `computations/s69_squeeze_reconciled.npz` (squeeze parameters, r_k values)
- `computations/s67_leggett_grav_decay.npz` (Leggett mass and decay data)
- `computations/s67_transit_ps.npz` (transit power spectrum)

**Pre-registered gate**: **LEGGETT-VACUUM-70**
- PASS: r_L > 0.3 (non-adiabatic excitation; A_s gap reduces to approximately 0.31 OOM)
- FAIL: r_L = 0 within numerical precision (adiabatic; A_s gap remains 0.485 OOM)
- INFO: 0 < r_L < 0.3 (partial excitation; A_s gap intermediate)

**Output files**:
- Script: `computations/s70_leggett_vacuum.py`
- Data: `computations/s70_leggett_vacuum.npz`
- Working paper: Section W1-A

---

### W1-B: F0-ALPHA-S-70 -- Spectral Function Normalization Scan for Alpha_s

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: Baptista, Lizzi, VdD (3/9 reviewers)

**Prompt**:

The framework extracts alpha_s(M_Z) = 0.022 from the spectral action threshold sum, a factor 5.4x below the observed 0.1180. This is the most serious particle-physics tension (7/9 reviewers confirm). The extraction uses alpha_3(M_KK) = g_3^2 / (4*pi) where g_3^2 = 2*pi^2 * f_0 / a_4, and then RG-runs from M_KK to M_Z. The spectral function normalization f_0 enters directly: alpha_3 is proportional to f_0 / a_4.

The question: does a value of f_0 exist in [0.5, 5.0] (the physical range for f(x) = sqrt(x) and nearby spectral functions) that simultaneously gives alpha_s(M_Z) in [0.10, 0.13] (2-sigma around PDG) AND keeps m_H in [120, 135] GeV?

**Method**: The threshold sum formalism (Chamseddine-Connes) gives:

  alpha_3(M_KK) = 2 * pi^2 * f_0 / a_4

where a_4 = 1350.72 (from canonical_constants.py). The Higgs mass depends on f_0 through:

  m_H^2 = (2 * f_2 * Lambda^2 * a_2 * M_KK^2) / (f_0 * Lambda^4 * a_0) * (some ratio)

but the dominant dependence is on the a_4/a_2 ratio, which is f_0-independent. The key question is whether the f_0-dependence in alpha_3 is degenerate with the f_0-dependence in m_H.

Import all constants from `computations/canonical_constants.py`. Key values: a_0 = 6440, a_2 = 2776.17, a_4 = 1350.72, M_KK = 7.429e16 GeV, M_Z = 91.1876 GeV.

**Computation**:
1. For f_0 in np.linspace(0.1, 10.0, 200):
   a. Compute alpha_3(M_KK) = 2 * pi^2 * f_0 / a_4.
   b. RG-run alpha_3 from M_KK to M_Z using 2-loop QCD beta function with n_f = 6 (all quarks active at M_KK). The 2-loop formula:
      d(alpha_s)/d(ln mu) = -(b_0 * alpha_s^2 + b_1 * alpha_s^3) / (2*pi)
      where b_0 = (33 - 2*n_f)/3 = 7, b_1 = (306 - 38*n_f)/3 = 26 (for n_f=6).
      Include threshold corrections at m_t, m_b, m_c.
   c. Record alpha_s(M_Z) as a function of f_0.
2. For each f_0, compute the Higgs mass prediction:
   a. The Chamseddine-Connes formula: m_H^2 = 8 * pi^2 * f_2 * M_KK^2 / (f_0 * a_0) * y_ratio
      where y_ratio involves Yukawa coupling sums. However, m_H primarily depends on the threshold sum ratio, not f_0 alone. Use the S69 KK-HIGGS-69 result (m_H = 127.51 GeV at standard f_0) and propagate the f_0 sensitivity: dm_H/df_0 from the mass formula.
   b. Alternatively, use the Lizzi functional selection result (S67): m_H is approximately f_0-independent to leading order because both numerator and denominator scale as f_0. Verify this.
3. Plot alpha_s(M_Z) vs f_0 and m_H vs f_0 on the same figure. Shade the allowed region: alpha_s in [0.10, 0.13] AND m_H in [120, 135].
4. If a consistent f_0 exists, report it. If no f_0 simultaneously satisfies both constraints, the tension is structural (not normalization-related).
5. Additionally, check the SWAMPLAND constraint (SWAMP-69 PASS at c = 3.52): does the optimal f_0 still satisfy c > 1?
6. Cross-check: compute alpha_s using the Kerner route (M_KK_kerner = 5.04e17 GeV) instead of the gravity route. The 0.83-decade M_KK ambiguity feeds directly into the RG running.

**Input files**:
- `computations/canonical_constants.py` (all constants)
- `computations/s69_kk_higgs.npz` (Higgs mass data)
- `computations/s69_swampland.npz` (swampland data)
- `computations/s64_kk_threshold.npz` (threshold sum data)
- `computations/s67_functional_select.npz` (functional selection data)

**Pre-registered gate**: **F0-ALPHA-S-70**
- PASS: A consistent f_0 exists in [0.5, 5.0] with alpha_s(M_Z) in [0.10, 0.13] AND m_H in [120, 135] GeV
- FAIL: No such f_0 exists (alpha_s tension is structural, not normalization)
- INFO: f_0 exists but outside [0.5, 5.0] or requires fine-tuning > 10%

**Output files**:
- Script: `computations/s70_f0_alpha_s.py`
- Data: `computations/s70_f0_alpha_s.npz`
- Working paper: Section W1-B

---

### W1-C: Q-SOUND-70 -- Sound Speed of Dark Energy Perturbations from Spectral Action

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: Volovik, Mack (2/9 reviewers)

**Prompt**:

The ISW tracking signal (7.6% FW/Quint, ISW-BOLTZ-69 PASS) is the substrate-specific discriminant -- the one signature that distinguishes the framework from generic quintessence with the same w_0. But it rests on assigning c_s^2 = 0 to dark energy perturbations. Volovik raises the critical question: does the q-theory actually predict c_s^2 = 0 from the spectral action, or is it an assumption?

The q-variable in Volovik's formulation (Paper 13, arXiv:0904.4113) is the 4-form field strength q = (1/24) * epsilon^{abcd} * F_{abcd}. In the spectral action context, q corresponds to the spectral weight a_0 -- the zeroth Seeley-DeWitt coefficient. The equation of state of DE perturbations depends on whether q is dynamical (c_s^2 = 1, propagating mode) or non-dynamical (c_s^2 = 0, tracking).

**Method**: In q-theory, the vacuum energy is epsilon(q) where q is the conserved charge. The perturbation equation for delta_q depends on the Lagrangian structure:

  L = -epsilon(q) + q * A_0 (non-dynamical, c_s^2 = 0)

vs

  L = (1/2) * K(q) * (partial q)^2 - epsilon(q) (dynamical, c_s^2 = K * d^2 epsilon / dq^2)

In the spectral action, the a_0 term enters as f_0 * Lambda^4 * a_0. The question: does the spectral action generate a kinetic term for fluctuations of a_0?

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Write the spectral action in q-theory language. The spectral action S = Tr f(D^2/Lambda^2) contains:
   - S_0 = (2/pi^2) * f_0 * Lambda^4 * a_0 (cosmological constant term)
   - S_2 = (2/pi^2) * f_2 * Lambda^2 * a_2 (Einstein-Hilbert term)
   The q-variable is q = a_0 / Vol(K) = a_0 / Vol_SU3_Haar.
2. Check whether the spectral action generates a kinetic term (d_mu q)^2. This requires examining the second variation of the spectral action with respect to fluctuations of the fiber metric (which determines a_0). The key identity: delta^2 S / delta(g_K)^2 evaluated at the Jensen metric. From the Hessian computations (S64, all 36 eigenvalues), this information exists.
3. Specifically: decompose the fiber metric perturbation into trace (volume-changing) and traceless (volume-preserving) parts. The q-variable corresponds to the trace part (det g_K). From the H2 theorem (S64 permanent): volume-preserving perturbations have pi_{ij} = 0 in DeWitt superspace. The q-perturbation is ORTHOGONAL to these.
4. Compute c_s^2 = delta^2 L / delta(partial_mu q)^2 / (delta^2 L / delta q^2). If the spectral action has no kinetic term for det(g_K), then c_s^2 = 0 (non-dynamical q). If the Hessian generates a kinetic structure, c_s^2 > 0.
5. Cross-check with Volovik Paper 13 (arXiv:0904.4113): in the original q-theory, c_s^2 = 0 when q enters the action only algebraically (no derivatives). The spectral action writes S = sum_n a_n(g_K) * integral(curvature invariants), where a_n depends on g_K but NOT on derivatives of g_K. This structure formally gives c_s^2 = 0.
6. Caveats: the above argument is for the bare spectral action. One-loop corrections can generate kinetic terms. Estimate: delta(c_s^2) from one-loop ~ (S_1loop/S_tree)^2 ~ 0.27 (using S_1loop/S_b = 0.52 from S62). Is this negligible?

**Input files**:
- `computations/canonical_constants.py` (all constants)
- `computations/s67_volovik_q_a0.npz` (q-theory data)
- `computations/s66_dilution_cc.npz` (dilution data)
- `computations/s64_hessian_descent.npz` (Hessian data)
- `computations/s69_isw_tracking.npz` (ISW tracking data) -- if it exists, else use s68_isw_tracking_test.npz

**Pre-registered gate**: **Q-SOUND-70**
- PASS: c_s^2 = 0 derived from spectral action structure (non-dynamical q-variable)
- FAIL: c_s^2 = 1 (dynamical q-variable; ISW tracking signal vanishes)
- INFO: c_s^2 in (0, 1) from one-loop corrections (partial tracking)

**Output files**:
- Script: `computations/s70_q_sound.py`
- Data: `computations/s70_q_sound.npz`
- Working paper: Section W1-C

---

### W1-D: BCS-GAP-CANONICAL -- Establish Single Canonical Delta

**Agent**: `van-den-dungen-bridge-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Van den Dungen (S69 convention warning)

**Prompt**:

S69 computations use two different BCS gap values without clear distinction: Delta = 0.464 M_KK (Delta_0_OES from S37 pair susceptibility) and Delta = 0.52 M_KK (appearing in some S69 scripts). Protection margins are large enough that no verdict is affected, but for reproducibility a canonical BCS gap value must be established.

**Method**: Audit and resolve.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Read canonical_constants.py and identify all BCS gap entries: Delta_0_GL = 0.770 M_KK, Delta_0_OES = 0.464 M_KK, Delta_B3 = 0.176 M_KK. These are THREE different quantities:
   - Delta_0_GL: Ginzburg-Landau order parameter amplitude (not the BCS gap)
   - Delta_0_OES: pair-addition gap from odd-even staggering (the physical BCS gap)
   - Delta_B3: gap in the B3 sector specifically (smaller than total gap)
2. Search all S69 scripts for hardcoded Delta values. Grep for "0.52", "0.464", "0.770", "Delta" in computations/s69_*.py.
3. For each occurrence of 0.52, determine its provenance. The value 0.52 likely arises from Delta_0_OES rounded up, or from a different extraction (e.g., mean-field gap equation vs ED).
4. Determine the canonical value: Delta_BCS = Delta_0_OES = 0.4643 M_KK is the canonical BCS gap (pair-addition energy from exact diagonalization, S37, 256-state Hilbert space). This is the gap measured by adding/removing a Cooper pair.
5. Add to canonical_constants.py a clear alias:
   Delta_BCS = Delta_0_OES  # Canonical BCS gap (M_KK units)
   with a provenance comment explaining that Delta_0_GL is a different quantity (order parameter, not excitation gap) and Delta_B3 is sector-specific.
6. Document the 0.52 provenance and mark it as superseded if it comes from an earlier, less precise calculation.

**Input files**:
- `computations/canonical_constants.py`
- All `computations/s69_*.py` scripts (grep for Delta values)

**Pre-registered gate**: **BCS-GAP-CANONICAL-70** (housekeeping, no PASS/FAIL)
- INFO: Canonical Delta_BCS established, all occurrences documented

**Output files**:
- Updated: `computations/canonical_constants.py` (add Delta_BCS alias + documentation)
- Script: `computations/s70_bcs_gap_canonical.py` (audit script)
- Working paper: Section W1-D

---

### W1-E: RATIO-GILKEY-DOCUMENT -- Resolve a_4/a_2 vs ratio_gilkey Convention

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Baptista (S69 W3-C, 14.9% discrepancy flagged)

**Prompt**:

The S69 Higgs mass computation (KK-HIGGS-69) flagged a 14.9% discrepancy between a_4/a_2 = 1350.72/2776.17 = 0.4865 and a quantity called ratio_gilkey used in earlier threshold sum calculations. This discrepancy does not affect the m_H gate verdict (passed with m_H = 127.51 GeV in [120, 135]) but must be resolved for alpha_s work.

**Method**: Trace the provenance of ratio_gilkey and determine whether it equals a_4/a_2 or involves additional factors.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Search computations/ for all uses of "ratio_gilkey" and "a4.*a2" to identify the two conventions.
2. The Gilkey-Seeley formula for a_4 on a Riemannian manifold is:
   a_4(D^2) = (1/(360*(4*pi)^{d/2})) * integral( 5*R^2 - 2*R_{ij}R^{ij} + 2*R_{ijkl}R^{ijkl} + 60*R*E + 180*E^2 + 30*Omega_{ij}Omega^{ij} + 12*Delta(R) + 60*Delta(E) )
   where E is the endomorphism and Omega is the curvature of the Clifford connection. For the pure geometric case (E = 0, Omega = 0), the ratio a_4/a_2 depends only on curvature invariants.
3. Determine: is ratio_gilkey = a_4/a_2, or ratio_gilkey = a_4 / (a_2 * some_factor) where some_factor comes from the Chamseddine-Connes normalization convention?
4. Reconcile. If the 14.9% discrepancy is a normalization factor (e.g., 1/(4*pi)^2 or Vol_SU3), document it. If it is an error in one computation, identify which.
5. Record the resolution in the working paper and flag any downstream consequences for alpha_s.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_kk_higgs.py` (source of the discrepancy)
- `computations/s64_kk_threshold.npz` (threshold sum data)

**Pre-registered gate**: **RATIO-GILKEY-70** (housekeeping, no PASS/FAIL)
- INFO: Convention resolved and documented

**Output files**:
- Script: `computations/s70_ratio_gilkey_document.py`
- Working paper: Section W1-E

---

### W1-F: BELL-GGE-70 -- CHSH Inequality for GGE Relic Quasiparticle Pairs

**Agent**: `kitaev-quantum-chaos-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Volovik, VdD, Phonon-First, Tesla (4/9 reviewers)

**Prompt**:

This completes the NOT STARTED gate from S69 (BELL-GGE-69). The GGE relic consists of 59.8 Bogoliubov quasiparticle pairs created by the impulsive KZ mechanism at the fold. Each pair (k, -k) is entangled through the Bogoliubov transformation: |BCS> = product_k (u_k + v_k * c_k^dagger * c_{-k}^dagger)|0>. The CHSH parameter S should exceed 2 (Bell violation) for all modes, demonstrating that the GGE relic is a genuinely quantum state, not a classical thermal ensemble.

**Method**: For each Bogoliubov pair (k, -k), the entanglement is encoded in the ratio v_k/u_k. The CHSH parameter for a two-mode squeezed state with squeeze parameter r_k = arctanh(|v_k/u_k|) is:

  S(r_k) = 2 * sqrt(2) * tanh(r_k) / sqrt(1 + tanh^2(r_k))

For r_k > 0, S > 2 (Bell violation). The violation is maximal (S = 2*sqrt(2)) as r_k -> infinity.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load Bogoliubov amplitudes (u_k, v_k) from the S67 exact diagonalization data. These are stored in the ED ground state decomposition.
2. For each of the 8 BCS modes (4 B2 + 1 B1 + 3 B3), compute:
   a. r_k = arctanh(|v_k / u_k|)
   b. S_k = 2 * sqrt(2) * tanh(r_k) / sqrt(1 + tanh^2(r_k))
   c. The concurrence C_k = 2 * |u_k * v_k| / (|u_k|^2 + |v_k|^2)
   d. The von Neumann entanglement entropy S_vN = -cosh^2(r_k) * ln(cosh^2(r_k)) + sinh^2(r_k) * ln(sinh^2(r_k)) -- use the standard formula for two-mode squeezed states but with the sign corrected: S_vN = cosh^2(r_k) * ln(cosh^2(r_k)) - sinh^2(r_k) * ln(sinh^2(r_k))
3. Compute the total entanglement entropy of the GGE relic: S_total = sum_k S_vN(k).
4. Check for GGE thermalization: the GGE state is NOT a thermal state if the individual S_k values vary significantly across modes (different effective temperatures per mode). Compute the spread sigma(S_k) / mean(S_k).
5. Cross-check: the n_Bog = 0.999 (canonical_constants.py) implies r_k is large for all modes, so S >> 2 is expected. Verify this is consistent.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_bell_gge.npz` (partial computation from S69)
- `computations/s67_transit_ps.npz` (transit data with Bogoliubov coefficients)
- `computations/s56_gge_fabric.npz` (GGE occupation numbers)

**Pre-registered gate**: **BELL-GGE-70**
- PASS: S > 2 for ALL 8 BCS modes (Bell violation; GGE is quantum)
- FAIL: S <= 2 for ANY mode (classical correlations sufficient)
- INFO: S > 2 but marginal (S < 2.1) for any mode

**Output files**:
- Script: `computations/s70_bell_gge.py`
- Data: `computations/s70_bell_gge.npz`
- Working paper: Section W1-F

---

### W1-G: NON-PERT-SA-70 -- Non-Perturbative Spectral Action at Lambda = 2.048

**Agent**: `lizzi-spectral-functional-theorist`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: Baptista (1/9 reviewers)

**Prompt**:

The spectral action is computed perturbatively via the heat kernel expansion S ~ sum_n a_n * Lambda^{d-n}. But at Lambda = M_KK (i.e., Lambda/M_KK = 1), or at the fold where the effective cutoff may be Lambda_eff = 2.048 (the swampland value from SWAMP-69), the asymptotic expansion may break down. This computation tests whether the exact (non-perturbative) spectral action agrees with the heat kernel truncation.

**Method**: The non-perturbative spectral action is:

  S_exact = sum_{n} d_n * f(lambda_n^2 / Lambda^2)

where f is the spectral function (f(x) = sqrt(x) for the framework), lambda_n are the D_K eigenvalues, d_n are the Peter-Weyl degeneracies, and the sum is over the full eigenvalue spectrum. The heat kernel approximation is:

  S_HK = (2/pi^2) * [f_0 * Lambda^4 * a_0 + f_2 * Lambda^2 * a_2 + f_4 * a_4 + ...]

where f_k = integral_0^infty x^{k/2-1} f(x) dx (which diverges for f(x) = sqrt(x); use regulated values).

For f(x) = sqrt(x): S_exact = sum_n d_n * |lambda_n| / Lambda, which is finite and computable directly from the spectrum.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the D_K eigenvalue spectrum at L_max = 6 from `computations/s30b_full_spectrum.npz`. At L_max = 6, there are approximately 20,000 eigenvalues (35 PW sectors, each with degeneracy dim(p,q)^2).
2. At tau = tau_fold = 0.19, compute S_exact(Lambda) = sum_n d_n * |lambda_n(tau)| / Lambda for Lambda values: 0.5, 1.0, 1.5, 2.0, 2.048, 3.0, 5.0, 10.0 (in M_KK units).
3. Compute S_HK(Lambda) = a_0/Lambda^3 - a_2/Lambda + a_4*Lambda + ... (the heat kernel series truncated at a_4, with appropriate coefficients for f(x) = sqrt(x)). Note: for f(x) = sqrt(x), the Mellin transform moments are f_0 divergent, f_2 divergent, and the spectral action is actually just sum |lambda_n|, which does not have a clean heat kernel expansion. Instead, compute S_exact directly and compare to the asymptotic form at large Lambda.
4. Compute the relative deviation: |S_exact - S_HK| / S_HK as a function of Lambda.
5. At Lambda = 2.048: is the deviation < 10%?
6. Plot S_exact(Lambda) and S_HK(Lambda) to show where the asymptotic expansion breaks down.
7. Compute the alpha_s-relevant quantity: the ratio a_4^{eff}(Lambda) = [S_exact(Lambda) - S_0(Lambda)] / [appropriate power of Lambda] where S_0 is the volume term. If a_4^{eff} differs from a_4 by more than 14.9% (the ratio_gilkey discrepancy), the non-perturbative correction may resolve the alpha_s tension.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s30b_full_spectrum.npz` (full D_K eigenvalue spectrum)
- `computations/s69_swampland.npz` (Lambda = 2.048 context)

**Pre-registered gate**: **NON-PERT-SA-70**
- PASS: |S_exact - S_HK| / S_HK < 0.10 at Lambda = 2.048
- FAIL: |S_exact - S_HK| / S_HK > 0.50 (heat kernel badly broken)
- INFO: deviation in [0.10, 0.50] (marginal; higher-order a_n needed)

**Output files**:
- Script: `computations/s70_non_pert_sa.py`
- Data: `computations/s70_non_pert_sa.npz`
- Working paper: Section W1-G

---

### W1-H: PARAMETRIC-GGE-70 -- Post-Transit Parametric Resonance in BCS Modes

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Tesla (1/9 reviewers)

**Prompt**:

After the transit, the 8 BCS modes oscillate with characteristic frequencies determined by the BCS dispersion relation. If any pair of modes satisfies a parametric resonance condition omega_i + omega_j ~ 2*omega_drive (where omega_drive comes from the modulus oscillation around tau_fold), energy can be transferred from the geometric sector to the BCS sector, amplifying the mode amplitude. This would contribute to A_s closure.

**Method**: Parametric resonance occurs when the Floquet exponent mu is positive. For a driven oscillator with time-dependent frequency omega(t) = omega_0 + epsilon * cos(2*omega_drive * t), the instability tongues are centered at omega_drive / omega_0 = 1/n for integer n.

Import all constants from `computations/canonical_constants.py`. Key values: omega_att = 1.430 M_KK (modulus attractor frequency), E_B1 = 0.819, E_B2_mean = 0.845, E_B3_mean = 0.978 M_KK (BCS mode energies).

**Computation**:
1. The driving frequency is omega_drive = omega_att = 1.430 M_KK (modulus oscillation at fold).
2. For each BCS mode i (8 modes), the natural frequency is omega_i = E_Bi (in the BCS dispersion relation). Check the resonance condition: omega_drive / omega_i for each mode.
3. For mode pairs (i, j), check sum resonance: |omega_i + omega_j - 2*omega_drive| < Gamma_pair where Gamma_pair is the resonance width. The width is set by the coupling epsilon = |delta(E_Bi)/delta(tau)| * (delta_tau oscillation amplitude).
4. Compute the Floquet exponent mu for each resonant pair using the Mathieu equation:
   d^2 x / dt^2 + [omega_i^2 + epsilon * cos(2*omega_drive * t)] * x = 0
   The maximum Floquet exponent is mu_max = epsilon / (2*omega_i) (for the principal resonance tongue).
5. The amplification factor after time T is exp(mu * T) where T is the post-transit oscillation duration before damping. Use T ~ 10 * 2*pi/omega_att (10 oscillation periods) as a conservative estimate.
6. Compute the A_s enhancement: delta_OOM = log10(exp(2*mu*T)) for the most resonant pair.
7. Cross-check with S67 Floquet post-transit computation (s67_floquet_post_transit.npz) for consistency.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s68_bcs_dressed_mode.npz` (BCS mode energies)
- `computations/s56_gge_fabric.npz` (GGE occupation numbers)
- `computations/s67_floquet_post_transit.npz` (prior Floquet analysis)

**Pre-registered gate**: **PARAMETRIC-GGE-70**
- PASS: Total A_s enhancement > 0.1 OOM from parametric resonance
- FAIL: Enhancement < 0.01 OOM (resonance negligible)
- INFO: Enhancement in [0.01, 0.1] OOM (marginal contribution)

**Output files**:
- Script: `computations/s70_parametric_gge.py`
- Data: `computations/s70_parametric_gge.npz`
- Working paper: Section W1-H

---

### W1-I: TRAPPED-ACOUSTIC-70 -- Null Expansion at the Fold

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: SP (1/9 reviewers)

**Prompt**:

The conformal factor computation (CONF-FACTOR-69) found that the fold region at tau = 0.19 has Omega(fold) = 4.28e-3 with a wide penumbra (8.41 k_tach). The acoustic white hole interpretation requires that there is NO trapped surface at the fold -- the null expansion theta(k) must be positive everywhere outside the sonic horizon.

**Method**: In the acoustic metric framework, the null expansion is:

  theta(k) = nabla_mu k^mu

where k^mu is the outgoing null vector of the acoustic metric. For a (1+1)D effective acoustic metric ds^2 = Omega^2 * [-(c_s^2 - v^2)*dt^2 - 2*v*dt*dx + dx^2], the null expansion is:

  theta = (1/Omega) * d(Omega)/dx + (c_s + v) / (c_s * x_coord_factor)

The trapped surface condition is theta < 0 (converging null rays). The acoustic white hole has theta > 0 outside the sonic horizon and theta = 0 at the horizon.

Import all constants from `computations/canonical_constants.py`. Key values: c_fabric = 209.97 (fabric sound speed), v_terminal = 26.545 (transit velocity), Mach = v_terminal / c_fabric.

Wait -- the transit is supersonic with Mach = v_terminal / c_s where c_s = c_fabric * sqrt(something). Use the S63 result c_s = 0.485 M_KK and Mach = 13.75 from the kinetic normalization.

**Computation**:
1. Load the conformal factor data from s69_conformal_factor.npz. This contains the effective acoustic metric components as functions of position (or tau).
2. Compute the null expansion theta(k) = (c_s + v) * d(ln Omega)/dr + geometric terms, where v(tau) is the flow velocity and c_s(tau) is the local sound speed.
3. Evaluate theta(k) at 100 points from tau = 0.01 to tau = 0.50. Focus on the fold region tau in [0.15, 0.25].
4. Identify the sonic horizon: the surface where v(tau) = c_s(tau). At this surface, theta should change sign for an acoustic black hole (but should NOT change sign for a white hole -- the null expansion should remain positive on the outgoing side).
5. Plot theta(k) vs tau and identify any trapped regions (theta < 0).
6. If no trapped surface exists: the fold is a genuine acoustic white hole with past singularity (pre-transit) and future infinity (post-transit). This is the correct Penrose diagram topology.
7. If a trapped surface exists: the Penrose diagram has different topology and the acoustic analog interpretation must be revised.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_conformal_factor.npz`
- `computations/s67_transit_ps.npz` (velocity profile)

**Pre-registered gate**: **TRAPPED-ACOUSTIC-70**
- PASS: No trapped surface (theta > 0 everywhere outside sonic horizon)
- FAIL: Trapped surface exists (theta < 0 in some region)
- INFO: theta = 0 tangentially (marginally trapped, no interior)

**Output files**:
- Script: `computations/s70_trapped_acoustic.py`
- Data: `computations/s70_trapped_acoustic.npz`
- Working paper: Section W1-I

---

### W1-J: LMAX7-PW-70 -- Peter-Weyl Extension to L_max = 7

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: Baptista (1/9 reviewers)

**Prompt**:

The threshold sum for alpha_s extraction depends on the a_4 Seeley-DeWitt coefficient, which is computed from the D_K eigenvalue spectrum truncated at L_max. The current computation uses L_max = 6 (the s30b_full_spectrum.npz file). The Shell Hessian result (S64 W7-A) showed that fold stability is UV-dominated with 79.9% of the contribution from L = 3 modes. The threshold sum convergence needs verification at L_max = 7.

**Method**: Extend the Peter-Weyl decomposition of D_K to include all irreducible representations (p, q) with p + q <= 7. Each sector contributes eigenvalues with degeneracy dim(p,q)^2 = ((p+1)*(q+1)*(p+q+2)/2)^2.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the D_K eigenvalue spectrum at L_max = 6 from s30b_full_spectrum.npz. Identify the representation structure.
2. For representations at L = 7 (i.e., (p,q) with p+q = 7): (7,0), (0,7), (6,1), (1,6), (5,2), (2,5), (4,3), (3,4). Compute the Casimir eigenvalue C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3 for each.
3. The D_K eigenvalue in sector (p,q) at the Jensen metric is determined by the Casimir and the Jensen deformation parameter tau. Use the formula from the block-diagonal structure (S22, D_K block-diagonal proven):
   lambda_{p,q,j}(tau) depends on the representation labels and the specific branch j within each sector.
4. Compute the Seeley-DeWitt coefficients at L_max = 7:
   a_n(L=7) = sum_{(p,q): p+q=7} dim(p,q)^2 * sum_j a_n^{(p,q,j)}
   where a_n^{(p,q,j)} are the per-eigenvalue contributions.
5. Compute the convergence ratio r_7 = |S(L_max=7) - S(L_max=6)| / |S(L_max=6) - S(L_max=5)|. If r_7 < 1.5, the series is converging. If r_7 > 2, the truncation error is growing.
6. Compute the Aitken-extrapolated S_inf = S(L=7) - [S(L=7)-S(L=6)]^2 / [S(L=7)-2*S(L=6)+S(L=5)] and the relative change delta(S_inf) = |S_inf(new) - S_inf(old)| / |S_inf(old)|.
7. Report the impact on alpha_s: if a_4 changes by more than 5% at L_max = 7, the alpha_s extraction is affected.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s30b_full_spectrum.npz` (D_K eigenvalue spectrum)
- `computations/s64_kk_threshold.npz` (threshold sum data)
- `computations/s64_shell_hessian.npz` (shell Hessian for UV convergence)

**Pre-registered gate**: **LMAX7-PW-70**
- PASS: r_7 < 1.5 AND delta(S_inf) < 1% (threshold sum converging)
- FAIL: r_7 > 2 OR delta(S_inf) > 5% (truncation error significant)
- INFO: intermediate values

**Output files**:
- Script: `computations/s70_lmax7_pw.py`
- Data: `computations/s70_lmax7_pw.npz`
- Working paper: Section W1-J

---

## IV. Wave 2: High Priority -- Observational Chain + Compound Observables

### W2-A: FULL-COV-PANTHEON-70 -- Full 1701x1701 Covariance Pantheon+ Reanalysis

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: Mack, Cosmic Web (2/9 reviewers)

**Prompt**:

The S69 Pantheon+ fit (PVD-SNE-69 PASS) used diagonal errors only, giving chi^2/dof = 1.025 and Delta_chi^2 = -4.47 vs LCDM across 37 bins from 1701 SNe. The full Brout+2022 covariance matrix includes off-diagonal terms (systematic correlations between redshift bins, calibration covariances, selection effects). The question: does the FW preference survive when off-diagonal correlations are included?

**Method**: The chi^2 with full covariance is:

  chi^2 = (mu_obs - mu_th)^T * C^{-1} * (mu_obs - mu_th)

where C is the full covariance matrix (1701 x 1701 or the binned version).

The framework distance modulus is:
  mu_th(z) = 5 * log10(d_L(z) / 10 pc)

where d_L(z) = (1+z) * integral_0^z dz' / H(z') and H(z) uses the FW cosmology: w_0 = -0.918, w_a = 0, Omega_m = 0.315, H_0 = 67.4 km/s/Mpc.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the S69 Pantheon+ computation from s69_pvd04_sne.npz. This contains the binned distance moduli and diagonal errors.
2. Construct the Brout+2022 covariance matrix. Since the actual 1701x1701 matrix is not available locally, use the published statistical + systematic covariance structure: C_ij = sigma_i^2 * delta_ij + sigma_sys^2 * f(z_i, z_j) where f(z_i, z_j) encodes the calibration correlation. Model the off-diagonal structure as:
   - Calibration floor: sigma_cal = 0.01 mag (correlated across all bins)
   - Peculiar velocity: sigma_pv = 250 km/s / (c * z) (correlated at z < 0.05)
   - Selection: sigma_sel = 0.005 * (1 + z) (correlated within z-bins)
3. Form C = C_stat + C_cal + C_pv + C_sel (each component is a rank-deficient matrix).
4. Invert C and compute chi^2 for both FW and LCDM models.
5. Report: Delta_chi^2(full cov) vs Delta_chi^2(diag) = -4.47. If Delta_chi^2 becomes less negative, the FW preference was partly driven by correlated errors.
6. Compute the BIC and AIC: FW has 0 free cosmological parameters (w_0 is derived), LCDM has 0 free parameters also (both use the same Planck priors). The model comparison is purely chi^2.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_pvd04_sne.npz` (Pantheon+ diagonal fit)
- `computations/s69_pvd04_sne.py` (script for reference)

**Pre-registered gate**: **FULL-COV-PANTHEON-70**
- INFO: Report Delta_chi^2(full cov) and compare to Delta_chi^2(diag) = -4.47

**Output files**:
- Script: `computations/s70_full_cov_pantheon.py`
- Data: `computations/s70_full_cov_pantheon.npz`
- Working paper: Section W2-A

---

### W2-B: FULL-COV-RSD-70 -- Full Covariance DESI RSD Reanalysis

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

The S69 f*sigma_8 fit (PVD-FSIG8-69 PASS, chi^2/dof = 0.761 vs LCDM 0.893) used independent bin errors. DESI DR1 provides correlated errors between overlapping redshift tracers. This computation includes the full covariance.

**Method**: Same chi^2 formalism as FULL-COV-PANTHEON-70 but for the f*sigma_8 observable.

The framework prediction: f*sigma_8(z) = Omega_m(z)^{0.55} * sigma_8(z) where sigma_8(z) = sigma_8(0) * D(z)/D(0) and the growth factor D(z) satisfies:

  D'' + (3/2 - w_DE/(1+w_DE*Omega_DE)) * D'/a - (3/2) * Omega_m(z) * D = 0

with w_DE = w_0 = -0.918, w_a = 0.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load PVD-FSIG8-69 results from s69_pvd05_fsigma8.npz. This contains the 9 RSD data points.
2. Construct the RSD covariance matrix. The DESI DR1 public data provides statistical errors per bin. Model the inter-bin correlations:
   - For bins at similar redshifts (overlapping tracers like LRG and ELG at z ~ 0.8): r_ij = 0.3 (typical overlap correlation)
   - For non-overlapping bins: r_ij = 0.0 (independent)
   - Systematic floor: sigma_sys = 0.005 (theoretical systematic from scale cuts)
3. Compute chi^2 with full covariance for both FW and LCDM.
4. Report: Delta_chi^2(full cov) vs Delta_chi^2(diag) = -1.19.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_pvd05_fsigma8.npz`
- `computations/s69_pvd05_fsigma8.py`

**Pre-registered gate**: **FULL-COV-RSD-70**
- INFO: Report Delta_chi^2(full cov) with full covariance

**Output files**:
- Script: `computations/s70_full_cov_rsd.py`
- Data: `computations/s70_full_cov_rsd.npz`
- Working paper: Section W2-B

---

### W2-C: CLASS-ISW-70 -- Full Boltzmann ISW with c_s^2_DE = 0

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: HIGH
**Carry-Forward**: Mack, VdD (2/9 reviewers)

**Prompt**:

The S69 ISW tracking test (ISW-BOLTZ-69 PASS) demonstrated a 7.6% FW/Quint signal using a simplified ISW calculation. This computation uses the full Boltzmann hierarchy to compute the ISW effect with c_s^2_DE = 0 (the tracking vacuum prediction).

**Method**: The ISW effect on the CMB temperature is:

  (Delta T / T)_ISW = -2 * integral_0^{z_*} d(Phi + Psi)/dt * e^{-tau} * dz / H(z)

where Phi and Psi are the Newtonian potentials. With DE perturbations at c_s^2 = 0, the potentials evolve differently from the c_s^2 = 1 (quintessence) case because the DE density perturbation tracks the matter perturbation.

The full computation requires solving the coupled Einstein-Boltzmann system:
  delta_DE' = -(1+w_DE) * (theta_DE + h'/2) - 3*(c_s^2 - w_DE) * H * delta_DE
  theta_DE' = -(1 - 3*c_s^2) * H * theta_DE + c_s^2 * k^2 * delta_DE / (1+w_DE)

with w_DE = -0.918, c_s^2 = 0.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Implement the coupled system for CDM + baryons + radiation + DE with c_s^2 = 0 in the synchronous gauge.
2. For each multipole l in [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 50, 100], compute the ISW contribution to C_l^{TT}.
3. Compare three models:
   a. LCDM (w = -1): no DE perturbations, standard ISW
   b. Quintessence (w = -0.918, c_s^2 = 1): DE perturbations with stiff sound speed
   c. Framework (w = -0.918, c_s^2 = 0): DE perturbations with tracking sound speed
4. Compute the fractional difference Delta(C_l) = (C_l^{FW} - C_l^{Quint}) / C_l^{LCDM} at each l.
5. Focus on l = 2-10 where the ISW effect dominates. Pre-registered threshold: Delta > 5% at l = 2-10.
6. Compute the ISW auto-power spectrum C_l^{ISW-ISW} and the ISW-galaxy cross-correlation C_l^{ISW-g} for the three models.
7. Estimate the Euclid SNR for discriminating FW from Quint: SNR = sum_l (2l+1) * [Delta(C_l)]^2 / [Var(C_l)].

**Input files**:
- `computations/canonical_constants.py`
- `computations/s68_isw_tracking_test.npz` (prior ISW data)
- `computations/s69_pvd10_isw_sdss.npz` (ISW-SDSS comparison)

**Pre-registered gate**: **CLASS-ISW-70**
- PASS: |C_l^{FW} - C_l^{Quint}| / C_l^{LCDM} > 5% for l in [2, 10]
- FAIL: |C_l^{FW} - C_l^{Quint}| / C_l^{LCDM} < 1% for all l (no discriminating power)
- INFO: signal in [1%, 5%]

**Output files**:
- Script: `computations/s70_class_isw.py`
- Data: `computations/s70_class_isw.npz`
- Working paper: Section W2-C

---

### W2-D: PHI-EFF-COMPOUND-70 -- SU(1,1) Reconciliation of Squeeze Phases

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Phonon-First (1/9 reviewers)

**Prompt**:

W1-A (PHI-EFF-69) computed the per-mode BCS squeeze phase: cos(phi_eff) = -0.181 (weakly destructive interference). W2-B (SU11-PHASE-69) computed the spatial thermal phase coherence: <cos(phi)> = +0.800 (constructive interference, von Mises distribution). These are different projections of the same SU(1,1) algebraic structure. The compound observable has not been calculated.

**Method**: The SU(1,1) group parametrizes two-mode squeezed states via three generators: K_0 (number), K_+ (squeeze), K_- (de-squeeze). The per-mode BCS squeeze is an element of SU(1,1) with squeeze parameter r_k and phase phi_k. The spatial thermal average is an integration over the U(1) subgroup (generated by K_0).

The compound squeeze parameter is obtained by SU(1,1) group multiplication:
  S_compound = S_spatial * S_BCS

where each S is a 2x2 matrix in the Bargmann representation:
  S(r, phi) = [[cosh(r), e^{i*phi} * sinh(r)], [e^{-i*phi} * sinh(r), cosh(r)]]

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the per-mode BCS squeeze data from s69_phi_eff.npz: r_k and phi_eff_k for each of 8 BCS modes.
2. Load the spatial phase data from s69_su11_phase.npz: the von Mises distribution kappa = E_J / T, <cos(phi)> = 0.800.
3. For each BCS mode k:
   a. Construct S_BCS(r_k, phi_eff_k) in the SU(1,1) Bargmann representation.
   b. Average over spatial phases using the von Mises distribution:
      <S_compound> = integral_0^{2pi} S_spatial(r_spatial, phi) * S_BCS(r_k, phi_eff_k) * P_vM(phi; kappa) * dphi / (2*pi)
      where r_spatial is determined by the thermal fluctuation amplitude and P_vM is the von Mises PDF.
   c. Extract the compound squeeze parameter r_compound and compound phase phi_compound from <S_compound>.
4. Compute the compound cos(phi_compound). Pre-registered: should be in [-0.181, +0.800] (between the two individual values).
5. Compute the compound A_s correction: delta_OOM = log10(cosh(2*r_compound)) and compare to the separate corrections (+0.226 OOM from W1-F and +0.043 OOM from W1-A).
6. Key question: does the compound observable give a LARGER or SMALLER A_s correction than the sum of separate corrections? (SU(1,1) multiplication is nonlinear, so the answer is not obvious.)

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_phi_eff.npz` (per-mode BCS squeeze phases)
- `computations/s69_su11_phase.npz` (spatial thermal phase distribution)
- `computations/s69_squeeze_reconciled.npz` (reconciled squeeze parameters)

**Pre-registered gate**: **PHI-EFF-COMPOUND-70**
- Pre-registered range: cos(phi_compound) in [-0.181, +0.800]
- INFO: report compound r and phi for all modes

**Output files**:
- Script: `computations/s70_phi_eff_compound.py`
- Data: `computations/s70_phi_eff_compound.npz`
- Working paper: Section W2-D

---

### W2-E: VOID-SIZE-70 -- Void Size Function at FW Cosmology

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

Voids are sensitive probes of dark energy because their abundance depends on the growth factor and the expansion history. The framework predicts w_0 = -0.918 (less negative than LCDM), which suppresses structure growth and should produce slightly fewer large voids.

**Method**: The void size function dn/dR is computed from the excursion set formalism (Sheth-van de Weygaert 2004):

  dn/dR = f(nu) * |d(ln sigma)/d(ln R)| * (rho_mean / M) / R

where nu = delta_v / sigma(R), delta_v = -2.71 (void shell-crossing threshold), sigma(R) is the mass variance at radius R, and f(nu) is the Sheth-van de Weygaert multiplicity function.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Compute the linear power spectrum P(k) for FW cosmology (w_0 = -0.918, Omega_m = 0.315, H_0 = 67.4, sigma_8 = 0.793 from PVD-FSIG8-69).
2. Compute sigma(R) = sqrt((1/(2*pi^2)) * integral k^2 * P(k) * W^2(kR) dk) where W is the top-hat window function, for R in [5, 50] Mpc/h.
3. Apply the Sheth-van de Weygaert void multiplicity function to compute dn/dR at z = 0.
4. Repeat for LCDM (w = -1, sigma_8 = 0.811).
5. Compare with BOSS void catalog data (Mao et al. 2017 or Nadathur et al. 2020): approximately 1000 voids with R in [10, 40] Mpc/h at z = 0.1-0.7.
6. Compute chi^2/dof for both FW and LCDM against the void size function data.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_pvd05_fsigma8.npz` (sigma_8 at FW)

**Pre-registered gate**: **VOID-SIZE-70**
- PASS: chi^2/dof < 2 for FW void size function
- FAIL: chi^2/dof > 5 (FW produces wrong void distribution)
- INFO: intermediate

**Output files**:
- Script: `computations/s70_void_size.py`
- Data: `computations/s70_void_size.npz`
- Working paper: Section W2-E

---

## V. Wave 3: Medium Priority -- Bucher Singularity Tests + Fiber Physics + Geometry

### W3-A: BERRY-DENNIS-GGE-70 -- Bucher Test 1: Velocity Distribution

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Phonon-First (1/9 reviewers, Bucher review)

**Prompt**:

Bucher et al. (2025) established that optical phase singularity ensembles follow the Berry-Dennis universal velocity distribution. The GGE relic is a multimode superposition from the impulsive KZ mechanism on CG(24). If the GGE modes are well-described by a Gaussian random wave model, their velocity distribution should obey the Berry-Dennis distribution.

**Method**: The Berry-Dennis velocity distribution for singularity velocities in a 2D Gaussian random wave field is:

  P(|v|) = 8 * pi^2 * <v>^2 * |v| / (pi^2 * |v|^2 + 4 * <v>^2)^2

where <v> is the mean velocity determined by the spectral width.

Import all constants from `computations/canonical_constants.py`. Key values: c_Gold = 0.915, omega_L1 = 0.138, omega_L2 = 0.192 M_KK.

**Computation**:
1. For each of three GGE channels (Goldstone, BA = broken-axial, Leggett):
   a. Compute the mean velocity <v> from the channel's dispersion relation:
      - Goldstone: omega = c_Gold * k, so <v> = c_Gold * <|k|> / <k^2>^{1/2} ~ c_Gold for linear dispersion.
      - BA: omega = sqrt(c_BA^2 * k^2 + Delta_BA^2), so <v> = c_BA * k / sqrt(c_BA^2 * k^2 + Delta_BA^2). Use c_BA from the S52 spectrum.
      - Leggett: omega = sqrt(omega_L^2 + v_L^2 * k^2), where omega_L = 0.138 M_KK is the gap. The phase velocity v_ph = omega/k >> group velocity v_g = v_L^2 * k / omega.
   b. Generate N = 10,000 random superpositions of GGE modes at the channel's occupation numbers (from s56_gge_fabric.npz). Each mode has amplitude ~ sqrt(n_k), phase uniform in [0, 2*pi].
   c. Compute the velocity field v(x) = sum_k n_k^{1/2} * v_g(k) * exp(i*k*x + i*phi_k) on CG(24) vertices (24 sites).
   d. Locate phase singularities (zeros of the wave field) and measure their velocities.
   e. Histogram the velocity distribution and fit to the Berry-Dennis form.
2. Compute chi^2/ndof for each channel against the Berry-Dennis prediction.
3. Verify: <v>_Gold / c_Gold should be near 1.05. <v>_Leggett / c_BLV should be near 2.18 (from the Bucher review predictions).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s56_gge_fabric.npz` (GGE occupation numbers)
- `computations/s69_four_speed.npz` (speed hierarchy)

**Pre-registered gate**: **BERRY-DENNIS-GGE-70**
- PASS: chi^2/ndof < 2 across all three channels, with <v> consistent with predictions to 30%
- FAIL: chi^2/ndof > 5 in ANY channel
- INFO: partial agreement (some channels match, others do not)

**Output files**:
- Script: `computations/s70_berry_dennis_gge.py`
- Data: `computations/s70_berry_dennis_gge.npz`
- Working paper: Section W3-A

---

### W3-B: SUPERLUMINAL-FRACTION-70 -- Bucher Test 2: Superluminal Fraction

**Agent**: `phonon-first-cosmologist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Phonon-First (Bucher review)

**Prompt**:

Bucher found that a significant fraction of phase singularities move faster than the medium's phase velocity. In the GGE relic, the analogous question is: what fraction of quasiparticle velocities exceed c_BLV (the BLV speed from the analog gravity program)?

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Using the velocity data from BERRY-DENNIS-GGE-70 (or computing independently if run in parallel):
   a. For each channel, compute F(|v| > c_BLV) = fraction of singularity velocities exceeding c_BLV.
   b. Predicted from the Berry-Dennis distribution: F = 1 - 4*<v>^2 / (pi^2*c_BLV^2 + 4*<v>^2).
2. Compute F_Gold and F_Leggett. Predicted: F_Gold = 61%, F_Leggett = 66%.
3. The Leggett channel should show the highest superluminal fraction because v_ph/v_g = 9.6 (large gap-to-kinetic ratio).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s56_gge_fabric.npz`
- `computations/s69_four_speed.npz`

**Pre-registered gate**: **SUPERLUMINAL-FRACTION-70**
- PASS: F(|v| > c_BLV) within 20% of prediction AND F_Leggett > 50%
- FAIL: F_Leggett < 30%
- INFO: partial agreement

**Output files**:
- Script: `computations/s70_superluminal_fraction.py`
- Data: `computations/s70_superluminal_fraction.npz`
- Working paper: Section W3-B

---

### W3-C: GGE-PAIR-CORRELATION-70 -- Bucher Test 3: Pair Correlations

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Phonon-First (Bucher review)

**Prompt**:

Bucher measured pair correlation functions between same-sign and opposite-sign phase singularities. In the GGE relic, Bogoliubov quasiparticles come in (k, -k) pairs with well-defined correlation structure on CG(24).

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. On CG(24) (the Cayley graph of the permutation group S_4 with 24 vertices), define the graph distance d(i,j) as the minimal number of edges between vertices i and j.
2. For each GGE configuration (generated as in BERRY-DENNIS-GGE-70):
   a. Locate phase singularities (zeros of the wave field) and classify their topological charge (winding number = +1 or -1).
   b. Compute the pair correlation function g_{+|+}(d) = <n_+(i) * n_+(j)>_{d(i,j)=d} / <n_+>^2 (same-sign pairs).
   c. Compute g_{+|-}(d) = <n_+(i) * n_-(j)>_{d(i,j)=d} / (<n_+> * <n_->) (opposite-sign pairs).
3. Average over 10,000 random configurations.
4. Check Bucher predictions:
   - g_{+|+}(d=0) < 0.1 (same-sign singularities repel at zero distance)
   - g_{+|-}(d=0) > 2.0 (opposite-sign singularities attract at zero distance)
   - g(d >= 2) in [0.5, 1.5] (decorrelation at large graph distance)

**Input files**:
- `computations/canonical_constants.py`
- `computations/s56_gge_fabric.npz`

**Pre-registered gate**: **GGE-PAIR-CORR-70**
- PASS: g_{+|+}(d=0) < 0.1 AND g_{+|-}(d=0) > 2.0 AND g(d>=2) in [0.5, 1.5]
- FAIL: g_{+|+}(d=0) > 1.0 OR g_{+|-}(d=0) < 1.0
- INFO: mixed results

**Output files**:
- Script: `computations/s70_gge_pair_correlation.py`
- Data: `computations/s70_gge_pair_correlation.npz`
- Working paper: Section W3-C

---

### W3-D: ANNIHILATION-TIME-70 -- Bucher Test 4: Pair Annihilation Timescale

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Phonon-First (Bucher review)

**Prompt**:

Bucher found pre-annihilation acceleration of singularity pairs. In the GGE relic, the pair annihilation timescale t_ann should be ~ 10^{-42} s on CG(24) -- exactly the timescale suppressed by Richardson-Gaudin integrability.

Import all constants from `computations/canonical_constants.py`. Key values: M_KK = 7.429e16 GeV, hbar_GeV_s = 6.582e-25 GeV*s.

**Computation**:
1. Compute the annihilation timescale t_ann for a singularity-antisingularity pair on CG(24):
   t_ann ~ d_initial / v_approach
   where d_initial ~ 1 graph step (lattice spacing a = M_KK^{-1}) and v_approach ~ c_Gold = 0.915 M_KK.
   So t_ann ~ 1 / (c_Gold * M_KK) = 1 / (0.915 * 7.429e16 GeV) in natural units.
   Convert to seconds: t_ann = hbar / (c_Gold * M_KK) = 6.582e-25 / (0.915 * 7.429e16) = 9.7e-42 s.
2. Compute the BA (broken-axial) oscillation timescale t_BA = 2*pi / omega_BA where omega_BA ~ Delta_B3 * M_KK.
   t_BA = 2*pi * hbar / (0.176 * 7.429e16 GeV) = 3.2e-41 s.
3. Check: t_ann / t_BA should be in [0.1, 10] (same order of magnitude).
4. Compare with the Richardson-Gaudin integrability timescale: the GGE is frozen (t_relax = infinity in the integrable limit). The actual relaxation timescale from integrability-breaking perturbations is t_relax ~ (M_KK / delta_E_integ)^2 * t_ann where delta_E_integ is the integrability-breaking energy scale. From the Liouvillian computation (S52), gamma_RP = 0.0398 M_KK, giving t_relax = t_ann / gamma_RP^2 ~ t_ann * 630 ~ 6e-39 s.
5. Key physical point: t_ann ~ 10^{-42} s is the timescale AT WHICH pairs WOULD annihilate if integrability were broken. The fact that the GGE is integrable means this annihilation is SUPPRESSED, and the pair density is frozen. This is the Bucher connection: in the framework, the GGE is a SNAPSHOT (not a steady-state) of the velocity/singularity distribution.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s56_gge_fabric.npz`

**Pre-registered gate**: **ANNIHILATION-TIME-70**
- PASS: t_ann in [10^{-43}, 10^{-40}] s AND t_ann/t_BA in [0.1, 10]
- FAIL: t_ann > 10^{-35} s OR t_ann < 10^{-50} s
- INFO: within range but scaling unexpected

**Output files**:
- Script: `computations/s70_annihilation_time.py`
- Data: `computations/s70_annihilation_time.npz`
- Working paper: Section W3-D

---

### W3-E: DISCRETE-BERRY-DENNIS-70 -- Bucher Test 5: Discrete Graph Limit

**Agent**: `kitaev-quantum-chaos-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Phonon-First (Bucher review)

**Prompt**:

The Berry-Dennis distribution is derived for continuous Gaussian random wave fields. CG(24) is a finite graph with 24 vertices. Does the Berry-Dennis universality survive discretization onto such a small graph?

**Method**: Construct the discrete analog of the Berry-Dennis Gaussian random wave model on CG(24) and test whether the singularity statistics converge.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Define the graph Laplacian L on CG(24): L_{ij} = degree(i) * delta_{ij} - A_{ij} where A is the adjacency matrix.
2. Compute the eigenmodes phi_n(v) of L (24 eigenmodes on 24 vertices). These replace the plane waves of the continuous Berry-Dennis model.
3. Generate N = 50,000 random Gaussian wave fields: psi(v) = sum_n a_n * phi_n(v) where a_n ~ N(0, S(omega_n)) and S(omega_n) is a spectral density function.
4. For each realization, identify phase singularities: vertices where the phase of psi winds around a plaquette (triangle or square face of CG(24)).
5. Measure the velocity of each singularity using the discrete analog: v_sing = delta(phase)/delta(time) computed from the group velocity of the dominant spectral components.
6. Histogram the velocity distribution and fit to the Berry-Dennis form.
7. Test convergence: repeat for CG(48), CG(120) (Cayley graphs of larger groups) to check if the fit improves with graph size. Report: at what N_vertices does chi^2/ndof drop below 3?
8. If CG(24) is too small for convergence, report the minimum N and classify as INFO.

**Input files**:
- `computations/canonical_constants.py`

**Pre-registered gate**: **DISCRETE-BERRY-DENNIS-70**
- PASS: chi^2/ndof < 3 on CG(24) for the discrete Berry-Dennis distribution
- FAIL: No well-defined discrete limit exists for N_vertices < 100
- INFO: Discrete limit exists but requires N > 24 for convergence

**Output files**:
- Script: `computations/s70_discrete_berry_dennis.py`
- Data: `computations/s70_discrete_berry_dennis.npz`
- Working paper: Section W3-E

---

### W3-F: ZETA-AS-BUDGET-70 -- A_s Gap Budget in Zeta Scheme

**Agent**: `lizzi-spectral-functional-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Lizzi (1/9 reviewers)

**Prompt**:

The A_s gap budget (0.485 OOM) was computed in the cutoff scheme with f(x) = sqrt(x). Lizzi's functional selection analysis (S66-S67) showed that eps_H is approximately functional-independent to leading order. However, the A_s normalization depends on the full mode equation, not just eps_H. This computation re-derives the A_s anatomy in the zeta scheme and checks whether any channel has different magnitude.

**Method**: In the zeta scheme, the spectral action is S_zeta = a_4(D_K^2), and the scalar amplitude is:

  A_s = H^2 / (8*pi^2 * eps_H * M_Pl^2 * c_s)

where H and eps_H are derived from the zeta action rather than the cutoff action. If eps_H is functional-independent (same in both schemes), the A_s ratio between schemes is determined by the ratio of H values.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the S66 zeta spectral action data from s66_zeta_sa.npz. Extract: S_zeta(tau), eps_H^{zeta}(tau_fold), and the zeta-scheme Hubble parameter.
2. Re-derive the A_s anatomy from the S69 squeeze analysis (s69_squeeze_reconciled.npz) but with zeta-scheme eps_H:
   - A_s^{zeta} = (H^{zeta})^2 / (8*pi^2 * eps_H^{zeta} * M_Pl^2 * c_s)
   - BCS correction: same fractional shift (+0.046 OOM) since it modifies the mode equation, not the background
   - Squeeze correction: same (+0.226 OOM) since it modifies the initial state, not the action
   - Phase correction: same (+0.043 OOM) since it is algebraic
3. Compute the A_s gap in the zeta scheme: gap_zeta = log10(A_s^{obs} / A_s^{zeta}).
4. Compare: is gap_zeta significantly different from gap_cutoff = 0.485 OOM?
5. If the gaps differ by > 0.1 OOM, the A_s gap is scheme-dependent and functional selection matters for normalization, not just for n_s.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s66_zeta_sa.npz` (zeta spectral action)
- `computations/s69_squeeze_reconciled.npz` (squeeze data)
- `computations/s69_as_normalization.npz` (A_s normalization chain)

**Pre-registered gate**: **ZETA-AS-BUDGET-70**
- INFO: Report gap_zeta and |gap_zeta - gap_cutoff|. Flag if difference > 0.1 OOM.

**Output files**:
- Script: `computations/s70_zeta_as_budget.py`
- Data: `computations/s70_zeta_as_budget.npz`
- Working paper: Section W3-F

---

### W3-G: LEGGETT-MOMENT-70 -- Which Spectral Moment Controls the Leggett Gap

**Agent**: `lizzi-spectral-functional-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Lizzi (1/9 reviewers)

**Prompt**:

The Leggett gap omega_L = 0.138 M_KK emerges from inter-sector coupling in the BCS Hamiltonian. Which Seeley-DeWitt coefficient a_{2k} controls it? If the Leggett gap is dominated by a_6 (the 6th coefficient, sensitive to curvature-cubed terms), it could be scheme-dependent. If it is controlled by a_4 or lower, it is more robust.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. The Leggett gap arises from the inter-sector Josephson coupling J_{23} between B2 and B3 sectors. From canonical_constants.py, J_C2 = 0.933, J_su2 = 0.059, J_u1 = 0.038. The Leggett frequency is omega_L^2 ~ J_23 * Delta_B2 * Delta_B3 / (n_B2 * n_B3) (Anderson-Leggett formula).
2. Express J_23 in terms of spectral action integrals. The inter-sector coupling comes from the off-diagonal blocks of D_K^2 in the Peter-Weyl decomposition. Since D_K is block-diagonal (proven S22), J_23 arises from the BCS interaction, not from the bare Dirac operator. The BCS interaction is a four-fermion term proportional to the coupling constant g, which is extracted from a_4.
3. Compute the sensitivity: d(omega_L) / d(a_n) for n = 0, 2, 4, 6. The chain is:
   omega_L -> J_23 -> g -> a_4 (if the coupling comes from gauge kinetic term)
   or omega_L -> Delta -> E_cond -> ... (if the gap dominates)
4. Determine which a_{2k} has the largest fractional sensitivity. If a_6-dominated, flag it.
5. Cross-check: the BCS gap Delta_0 = 0.464 M_KK is set by the pairing interaction. In BCS theory, Delta ~ exp(-1/lambda) where lambda = g * rho(E_F). Here g comes from the spectral action (a_4 sector) and rho(E_F) from the density of states at the Fermi level.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s30b_full_spectrum.npz` (D_K spectrum for a_{2k} extraction)

**Pre-registered gate**: **LEGGETT-MOMENT-70**
- INFO: Report which a_{2k} dominates the Leggett gap. Flag if a_6-dominated.

**Output files**:
- Script: `computations/s70_leggett_moment.py`
- Data: `computations/s70_leggett_moment.npz`
- Working paper: Section W3-G

---

### W3-H: PENROSE-SEQUENCE-70 -- 4-Panel Conformal Diagram Evolution

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: SP (1/9 reviewers)

**Prompt**:

Construct the 4-panel conformal diagram showing the acoustic spacetime evolution through the transit: (1) pre-transit (subsonic), (2) fold approach (sonic horizon formation), (3) transit (supersonic, acoustic white hole), (4) post-transit (subsonic, GGE relic). This provides the visual representation of the acoustic causal structure.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the conformal factor and velocity profile from s69_conformal_factor.npz and s67_transit_ps.npz.
2. For each of 4 panels, compute the null geodesics of the acoustic metric:
   ds^2 = Omega^2(tau) * [-(c_s^2 - v^2) * dt^2 - 2*v*dt*dx + dx^2]
   The null geodesics satisfy: dx/dt = (-v +/- c_s) (outgoing/ingoing).
3. Panel 1 (pre-transit, tau > 0.25): v/c_s < 1. Both null cones open. No horizon.
4. Panel 2 (fold approach, tau ~ 0.20): v/c_s -> 1. Null cones pinch. Sonic horizon forms.
5. Panel 3 (transit, tau = 0.19): v/c_s > 1 (Mach 13.75). Outgoing null geodesics are dragged inward. Acoustic white hole: no signals escape from the past.
6. Panel 4 (post-transit, tau < 0.15): v/c_s < 1 again. Null cones re-open. GGE relic propagates freely.
7. Plot the Penrose diagram with conformal coordinates (U, V) where U = t - integral(dx/(v+c_s)) and V = t + integral(dx/(-v+c_s)). Use the standard compactification tan^{-1}(U) vs tan^{-1}(V).
8. Mark: sonic horizon, fold, penumbra region (8.41 k_tach wide from CONF-FACTOR-69).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_conformal_factor.npz`
- `computations/s67_transit_ps.npz`

**Pre-registered gate**: **PENROSE-SEQUENCE-70**
- INFO: 4-panel conformal diagram with causal structure classified

**Output files**:
- Script: `computations/s70_penrose_sequence.py`
- Data: `computations/s70_penrose_sequence.npz`
- Working paper: Section W3-H

---

### W3-I: KRETSCHNER-BCS-70 -- Kretschmer Scalar Under BCS Backreaction

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: SP (1/9 reviewers)

**Prompt**:

Compute the Kretschner scalar K = R_{abcd} * R^{abcd} of the acoustic metric under BCS backreaction. The BCS condensate modifies the Ricci-type curvature (trace sector) but should preserve the Weyl-type curvature (traceless sector) by the protection hierarchy.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the Petrov classification data from s69_petrov_bcs.npz, which contains the Weyl scalars and curvature invariants.
2. Compute K(tau) = R_{abcd} * R^{abcd} for the bare Jensen metric and the BCS-dressed Jensen metric at tau values in [0.01, 0.50].
3. Decompose: K = K_Weyl + K_Ricci + K_scalar (the Gauss decomposition of the Kretschmer scalar).
4. Verify: K_Weyl is unchanged by BCS (Petrov type preserved from PETROV-BCS-69). K_Ricci changes. Report the fractional change delta(K)/K at the fold.
5. Check for singularities: K should be finite at all tau (no curvature singularity at the fold). The maximum K occurs at the fold where curvature is maximal.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_petrov_bcs.npz`

**Pre-registered gate**: **KRETSCHNER-BCS-70**
- INFO: K(tau) profile with BCS decomposition

**Output files**:
- Script: `computations/s70_kretschner_bcs.py`
- Data: `computations/s70_kretschner_bcs.npz`
- Working paper: Section W3-I

---

### W3-J: MEISSNER-ED-70 -- BCS-Dressed Meissner Stiffness from Exact Diagonalization

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Volovik (1/9 reviewers)

**Prompt**:

The Meissner stiffness (superfluid density) rho_s determines how the BCS condensate responds to perturbations. In the framework, rho_s controls the dark energy equation of state through the effective stiffness of the spectral weight. If rho_s has a systematic shift under BCS dressing, w_0 may shift from -0.918.

**Method**: The Meissner stiffness is computed from the second derivative of the free energy with respect to an imposed phase twist:

  rho_s = (1/V) * d^2 F / d(phi)^2 |_{phi=0}

where phi is a twist in the boundary conditions on CG(24).

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the S67 exact diagonalization data (8-mode BCS Hamiltonian, 256-state Hilbert space).
2. Impose a phase twist phi on the hopping terms: t_{ij} -> t_{ij} * exp(i * phi * hat_r_{ij}) for bonds along a chosen direction.
3. Diagonalize the BCS Hamiltonian at phi = -0.05, -0.025, 0, +0.025, +0.05 (5-point stencil).
4. Compute F(phi) = -T * ln(Z(phi)) at the GGE temperature T_acoustic = 0.112 M_KK.
5. Extract rho_s = d^2 F / d(phi)^2 using finite differences.
6. Compare bare rho_s (no BCS, normal state) with BCS-dressed rho_s. The ratio delta(rho_s)/rho_s is the systematic shift in w_0.
7. Estimate: delta(w_0) ~ delta(rho_s) / rho_total. If delta(w_0) > 0.01, it is an observable systematic.
8. Cross-check with the S62 partition function computation (s62_cc_qtheory_gge.npz).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s67_transit_ps.npz` (ED data)
- `computations/s62_cc_qtheory_gge.npz` (partition function)
- `computations/s56_gge_fabric.npz` (GGE data)

**Pre-registered gate**: **MEISSNER-ED-70**
- INFO: Report rho_s (bare), rho_s (BCS), delta(w_0). Flag if |delta(w_0)| > 0.01.

**Output files**:
- Script: `computations/s70_meissner_ed.py`
- Data: `computations/s70_meissner_ed.npz`
- Working paper: Section W3-J

---

## VI. Wave 4: Medium Priority -- Observational Chain + Analog Program + Moduli

### W4-A: HYDROSTATIC-CLUSTER-70 -- Cluster Mass Function with Hydrostatic Bias

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Mack (1/9 reviewers)

**Prompt**:

PVD-CLUST-69 found chi^2/dof = 4.1 for the cluster mass function (FW), compared to LCDM = 3.7. The tension is partly driven by sigma_8 (FW: 0.793 vs LCDM: 0.811) and partly by the hydrostatic mass bias (1-b). Including a realistic mass bias calibration may improve the fit.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the cluster data from s69_pvd08_cluster.npz.
2. The Planck SZ cluster count depends on the cluster mass function, which is calibrated with hydrostatic mass estimates. The bias parameter (1-b) is typically 0.58-0.80 (CMB lensing calibration) or 0.75-0.85 (WL calibration).
3. Recompute the cluster mass function at FW cosmology (sigma_8 = 0.793) with three bias calibrations:
   a. (1-b) = 0.62 (Planck CMB lensing, lower bound)
   b. (1-b) = 0.73 (HSC WL calibration)
   c. (1-b) = 0.80 (conservative upper bound)
4. For each, compute chi^2/dof against Planck SZ + ACT cluster counts.
5. Determine: at what (1-b) does FW become competitive with LCDM? Report the crossover.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_pvd08_cluster.npz`

**Pre-registered gate**: **HYDROSTATIC-CLUSTER-70**
- INFO: Report chi^2/dof at three bias calibrations; identify crossover with LCDM

**Output files**:
- Script: `computations/s70_hydrostatic_cluster.py`
- Data: `computations/s70_hydrostatic_cluster.npz`
- Working paper: Section W4-A

---

### W4-B: CHIRP-PENUMBRA-70 -- Chirp Rate of Tachyonic Sweep

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Tesla (1/9 reviewers)

**Prompt**:

The z''/z barrier from S67 has a tachyonic region (z''/z < 0) near the fold. The rate at which the tachyonic band sweeps through k-space determines the efficiency of particle production (parametric amplification). This is the "chirp rate" of the tachyonic sweep.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the z''/z data from the S67 transit power spectrum (s67_transit_ps.npz).
2. For the tachyonic region (where z''/z < 0), compute:
   a. k_tach(tau) = sqrt(-z''/z) at each tau value
   b. The chirp rate: dk_tach/dtau and dk_tach/dt = (dk_tach/dtau) * v_terminal
3. Compare the exact numerical chirp to the WKB approximation:
   In WKB, the particle production coefficient is beta_k ~ exp(-pi * k^2 / |dk_tach/dt|).
   The WKB prediction for the power spectrum enhancement is: P(k) ~ |beta_k|^2 / (4*pi*k).
4. Compute the relative error: |P_exact - P_WKB| / P_exact for each k in the tachyonic band.
5. Report whether WKB matches to < 10% (PASS criterion).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s67_transit_ps.npz`

**Pre-registered gate**: **CHIRP-PENUMBRA-70**
- PASS: |P_exact - P_WKB| / P_exact < 10% across the tachyonic band
- FAIL: WKB error > 50%
- INFO: WKB error in [10%, 50%]

**Output files**:
- Script: `computations/s70_chirp_penumbra.py`
- Data: `computations/s70_chirp_penumbra.npz`
- Working paper: Section W4-B

---

### W4-C: CAVITY-BCS-HORIZON-70 -- Transmission Through Compound Barrier

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Tesla (1/9 reviewers)

**Prompt**:

The z''/z barrier at the fold has a compound structure: a geometric barrier (from the Jensen deformation) superimposed with a BCS barrier (from the gap turning on). This forms an acoustic "cavity" between two barriers. Transmission through a compound barrier can show resonant tunneling (Fabry-Perot-like) at specific frequencies.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load z''/z from s67_transit_ps.npz and the BCS gap profile Delta(tau) from s69_bcs_hessian.npz.
2. Construct the compound effective potential V_eff(tau) = z''/z + Delta(tau)^2 * (correction factor).
3. For k-modes in [0.1, 10.0] * k_tach, compute the transmission coefficient T(k) through the compound barrier using the transfer matrix method:
   a. Divide the barrier into N = 1000 thin slabs.
   b. For each slab, the transfer matrix is M_j = [[cos(q_j*dx), sin(q_j*dx)/q_j], [-q_j*sin(q_j*dx), cos(q_j*dx)]] where q_j^2 = k^2 - V_eff(tau_j).
   c. The total transfer matrix is M = product of M_j.
   d. T(k) = 1 / |M_{11}|^2.
4. Plot T(k) and identify any resonant peaks (Fabry-Perot resonances in the cavity).
5. If resonances exist, compute the Q-factor and the enhancement of specific k-modes. These would produce spectral features in the primordial power spectrum.
6. Compute the conformal factor profile through the barrier region.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s67_transit_ps.npz`
- `computations/s69_bcs_hessian.npz` (BCS gap profile)
- `computations/s69_conformal_factor.npz`

**Pre-registered gate**: **CAVITY-BCS-HORIZON-70**
- INFO: Report T(k) profile, number of resonances, Q-factors

**Output files**:
- Script: `computations/s70_cavity_bcs_horizon.py`
- Data: `computations/s70_cavity_bcs_horizon.npz`
- Working paper: Section W4-C

---

### W4-D: AP-VOID-70 -- Alcock-Paczynski Test from Void Stacking

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

The Alcock-Paczynski (AP) test measures the ratio D_A(z) * H(z) / c from the geometric distortion of stacked void shapes. Voids in redshift space should appear spherical in the correct cosmology. In the wrong cosmology, they appear oblate or prolate.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Compute the AP ratio F_AP(z) = D_A(z) * H(z) / c for FW and LCDM at z = [0.2, 0.4, 0.6, 0.8].
2. The fractional difference (F_AP^{FW} - F_AP^{LCDM}) / F_AP^{LCDM} quantifies the void shape distortion.
3. Use the BOSS void catalog stacking measurements (Hamaus et al. 2016) as reference. Their constraints are at z ~ 0.57 with approximately 5% precision.
4. Compute chi^2 for both cosmologies against the void AP data.
5. Report whether the FW prediction is distinguishable from LCDM at current void catalog precision.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_pvd13_da.npz` (distance data)

**Pre-registered gate**: **AP-VOID-70**
- INFO: Report F_AP(z) for both models and chi^2 against void stacking data

**Output files**:
- Script: `computations/s70_ap_void.py`
- Data: `computations/s70_ap_void.npz`
- Working paper: Section W4-D

---

### W4-E: BULK-FLOW-70 -- Bulk Flow Amplitude at FW Cosmology

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

The bulk flow (coherent large-scale velocity) is sensitive to the growth rate f(z) * sigma_8(z). The framework predicts slightly lower growth (f*sigma_8 suppressed by ~4%). Compute the bulk flow amplitude and compare with observations.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. The bulk flow within a sphere of radius R is: V_bulk^2 = (H_0 * f)^2 / (2*pi^2) * integral_0^infty P(k) * |W(kR)|^2 dk where W is the top-hat window function.
2. Compute V_bulk(R) for R = [50, 100, 150, 200, 300] Mpc/h at FW cosmology.
3. Compare with observations: Watkins et al. (2023) bulk flow at R ~ 150 Mpc/h.
4. Repeat for LCDM.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_pvd05_fsigma8.npz`

**Pre-registered gate**: **BULK-FLOW-70**
- INFO: Report V_bulk(R) for FW and LCDM

**Output files**:
- Script: `computations/s70_bulk_flow.py`
- Data: `computations/s70_bulk_flow.npz`
- Working paper: Section W4-E

---

### W4-F: BETTI-FISHER-70 -- Persistent Betti Number Forecast

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

Persistent homology (Betti numbers as a function of density threshold) captures the topology of the cosmic web. The framework predicts different growth history (sigma_8 = 0.793 vs 0.811), which changes the Betti number statistics.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Use the Feldbrugge+2019 scaling relations for Betti numbers in Gaussian random fields:
   beta_k(nu) ~ nu^{d-k} * exp(-nu^2/2) where nu = delta / sigma is the density threshold.
2. For the FW power spectrum (suppressed by (sigma_8^{FW}/sigma_8^{LCDM})^2 = 0.955):
   a. Compute beta_0 (connected components), beta_1 (loops/tunnels), beta_2 (voids) as functions of nu.
   b. Compute the persistent diagram: birth/death pairs for each topological feature.
3. Compute the expected Fisher information for discriminating FW from LCDM using Betti statistics from a Euclid-like survey volume (V = 10 Gpc^3).
4. Report the SNR for FW/LCDM discrimination.

**Input files**:
- `computations/canonical_constants.py`

**Pre-registered gate**: **BETTI-FISHER-70**
- INFO: Report SNR for FW/LCDM discrimination using persistent Betti numbers

**Output files**:
- Script: `computations/s70_betti_fisher.py`
- Data: `computations/s70_betti_fisher.npz`
- Working paper: Section W4-F

---

### W4-G: OFF-JENSEN-HESS-70 -- Full 35x35 Off-Jensen Hessian at Fold

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Baptista (1/9 reviewers)

**Prompt**:

The off-Jensen gradient vanishes exactly (W5-G permanent theorem). But the off-Jensen HESSIAN (second derivatives) characterizes the curvature of the valley. The BCS Hessian (BCS-HESS-69) computed the 8x8 Hessian of the 8 Jensen moduli but not the full 35x35 Hessian including all independent metric components of the bi-invariant metric on SU(3).

SU(3) has 8 dimensions. A general left-invariant metric has 8*(8+1)/2 = 36 independent components. One is the overall volume (fixed by the spectral action). So there are 35 independent off-Jensen directions.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the BCS Hessian data from s69_bcs_hessian.npz, which contains the 8x8 diagonal Hessian in the Jensen parameter basis.
2. The Jensen metric has 8 equal diagonal entries g_{aa} = g_0 * exp(2*tau) for a = 1..4 and g_{aa} = g_0 * exp(-2*tau) for a = 5..8 (approximate). The off-Jensen directions break this structure.
3. Parametrize off-Jensen perturbations: h_{ab} = delta(g_{ab}) with constraints tr(h) = 0 (volume-preserving) and h symmetric. This gives 35 independent directions.
4. For each off-Jensen direction e_i (i = 1..35), compute d^2 S / dh_i^2 by finite differences: perturb g -> g + epsilon * e_i, compute S(g + epsilon * e_i), and use the 3-point formula.
5. Assemble the full 35x35 Hessian matrix H_ij = d^2 S / (dh_i * dh_j).
6. Diagonalize H. All eigenvalues should be positive (the Jensen metric is a local minimum in all off-Jensen directions, which is stronger than the gradient vanishing).
7. Report: eigenvalue spectrum, condition number, softest mode.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_bcs_hessian.npz`
- `computations/s30b_full_spectrum.npz` (D_K spectrum for perturbative SA)
- `computations/s69_off_jensen_gradient.npz`

**Pre-registered gate**: **OFF-JENSEN-HESS-70**
- INFO: Report full 35x35 eigenvalue spectrum. Flag any negative eigenvalues.

**Output files**:
- Script: `computations/s70_off_jensen_hess.py`
- Data: `computations/s70_off_jensen_hess.npz`
- Working paper: Section W4-G

---

### W4-H: SPECTRAL-DIM-FLOW-70 -- Spectral Dimension Flow Over 5 Decades

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Volovik (1/9 reviewers)

**Prompt**:

The spectral dimension d_s(sigma) = -2 * d(ln P(sigma)) / d(ln sigma) where P(sigma) = Tr exp(-sigma * D_K^2) measures the effective dimensionality of the geometry at scale sigma. SPEC-DIM-BCS-69 showed d_s is BCS-protected (0.094% shift on the full 992-mode spectrum). This computation extends the measurement to 5 decades in sigma, both bare and BCS-dressed.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the D_K eigenvalue spectrum from s30b_full_spectrum.npz at tau = tau_fold.
2. Compute P(sigma) = sum_n d_n * exp(-sigma * lambda_n^2) for sigma in np.logspace(-4, 1, 500) (5 decades).
3. Compute d_s(sigma) = -2 * d(ln P) / d(ln sigma) using finite differences.
4. Repeat for the BCS-dressed spectrum: shift the 8 near-Fermi eigenvalues by the BCS gap Delta_BCS = 0.464 M_KK.
5. Plot d_s(sigma) for both spectra on the same axes. Expected behavior:
   - sigma -> 0 (UV): d_s -> 8 (full 8D SU(3) geometry)
   - sigma -> infinity (IR): d_s -> 0 (discrete spectrum, finite volume)
   - Intermediate: possible flow through d_s = 4 (emergent 4D behavior)
6. Identify the scale sigma_4 where d_s = 4 (if it exists). This is the scale at which the geometry "looks 4-dimensional."
7. Report delta(d_s)/d_s at each sigma decade for the BCS shift.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s30b_full_spectrum.npz`
- `computations/s69_spectral_dim_bcs.npz` (prior spectral dimension data)

**Pre-registered gate**: **SPECTRAL-DIM-FLOW-70**
- INFO: Report d_s(sigma) over 5 decades, bare vs BCS, identify d_s = 4 scale

**Output files**:
- Script: `computations/s70_spectral_dim_flow.py`
- Data: `computations/s70_spectral_dim_flow.npz`
- Working paper: Section W4-H

---

### W4-I: BCS-PROXIMITY-70 -- Induced Pairing Beyond 8 Near-Fermi Modes

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM
**Carry-Forward**: Volovik (1/9 reviewers)

**Prompt**:

The BCS condensate occupies 8 near-Fermi modes (4 B2 + 1 B1 + 3 B3). The proximity effect in condensed matter physics induces pairing in neighboring modes through the anomalous propagator. This computation checks whether modes 9-16 (the next shell beyond the Fermi surface) acquire induced gaps through BCS proximity.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the D_K eigenvalue spectrum and identify modes 1-8 (BCS active) and modes 9-16 (first proximity shell).
2. The induced gap in mode n (with energy E_n > E_F + Delta) is:
   Delta_ind(n) = sum_m V_{nm} * Delta_m / (2 * E_m) * f(E_n - E_m)
   where V_{nm} is the inter-mode pairing interaction and f is a Lorentzian cutoff with width ~ Delta.
3. Estimate V_{nm} from the BCS coupling constant: V ~ g / N_modes where g is the dimensionless coupling. For modes near the Fermi surface, V ~ 1/N. For modes further away, V decays as 1/(E_n - E_F)^2.
4. Compute Delta_ind for modes 9-16. If Delta_ind > 0.01 * Delta_BCS for any mode, the 8/992 counting is incomplete and the BCS footprint extends further.
5. Compute the total proximity-corrected Plancherel weight: w_BCS = sum over all modes with Delta_ind > threshold of dim(p,q)^2 / sum all dim(p,q)^2.
6. Cross-check: the Plancherel weight of modes 1-8 is 0.008% (from S69). If proximity doubles this, it is still negligible for spectral moment protections but could matter for eigenvalue-level predictions.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s30b_full_spectrum.npz`
- `computations/s67_transit_ps.npz` (ED Bogoliubov data)
- `computations/s56_gge_fabric.npz`

**Pre-registered gate**: **BCS-PROXIMITY-70**
- INFO: Report Delta_ind for modes 9-16. Flag if Delta_ind > 0.01 * Delta_BCS for any mode (8/992 counting incomplete).

**Output files**:
- Script: `computations/s70_bcs_proximity.py`
- Data: `computations/s70_bcs_proximity.npz`
- Working paper: Section W4-I

---

## VII. Wave 5: Low Priority

### W5-A: DM-PAIR-DECAY-70 -- Leggett Decay Rate vs FIRAS/PIXIE

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Mack (1/9 reviewers)

**Prompt**:

If the Leggett channel GGE quasiparticles constitute dark matter, their decay rate must be below the FIRAS spectral distortion bound. The Leggett mode decays via coupling to the Goldstone (acoustic) channel.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the Leggett gravitational decay data from s67_leggett_grav_decay.npz.
2. The Leggett decay rate is Gamma_L = (coupling)^2 * omega_L^3 / (8*pi * rho_s) where the coupling comes from the cubic vertex in the BCS effective action.
3. The FIRAS bound on spectral distortion: delta_mu < 9e-5 (95% CL). A decaying dark matter species with lifetime tau_DM contributes delta_mu ~ (Gamma_DM / H_0) * (Omega_DM / Omega_rad) * (T_decay / T_CMB)^{3/2}.
4. Compute: is Gamma_L < FIRAS bound? What is the minimum lifetime?
5. If the lifetime is longer than the age of the universe, the Leggett DM is stable. If shorter, check the PIXIE forecast sensitivity (sigma_mu ~ 5e-8).

**Input files**:
- `computations/canonical_constants.py`
- `computations/s67_leggett_grav_decay.npz`

**Pre-registered gate**: **DM-PAIR-DECAY-70**
- PASS: Gamma_L * t_universe < sigma_FIRAS (stable against FIRAS)
- FAIL: Gamma_L * t_universe > 1 (decays within age of universe)
- INFO: intermediate (detectable by PIXIE but not FIRAS)

**Output files**:
- Script: `computations/s70_dm_pair_decay.py`
- Data: `computations/s70_dm_pair_decay.npz`
- Working paper: Section W5-A

---

### W5-B: KURAMOTO-SYNC-70 -- CG(24) Josephson as Kuramoto Model

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Tesla (1/9 reviewers)

**Prompt**:

The 32-cell Josephson junction array on CG(24) can be mapped to a Kuramoto model of coupled oscillators. The critical coupling kappa_c determines the synchronization threshold. If kappa_c < E_J/T = 3.60 (from SU11-PHASE-69), the system is in the synchronized phase.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. The Kuramoto model on CG(24): d(theta_i)/dt = omega_i + (K/N) * sum_j A_{ij} * sin(theta_j - theta_i) where A is the adjacency matrix.
2. The critical coupling K_c = 2 / (pi * g(0)) where g(omega) is the distribution of natural frequencies.
3. For the GGE, the natural frequencies are the BCS mode energies with disorder from the GGE occupation numbers. Compute g(omega) from the 8 BCS modes.
4. Compare K_c to K_actual = E_J = 0.933 * M_KK (the Josephson coupling from canonical_constants.py, J_C2).
5. Compute the Kuramoto order parameter r = |<exp(i*theta)>| as a function of K. Identify the critical K.

**Input files**:
- `computations/canonical_constants.py`

**Pre-registered gate**: **KURAMOTO-SYNC-70**
- PASS: K_c < 3.60 (system synchronized; collective phase coherence)
- FAIL: K_c > 3.60 (no synchronization at the GGE temperature)
- INFO: K_c near 3.60 (marginal synchronization)

**Output files**:
- Script: `computations/s70_kuramoto_sync.py`
- Data: `computations/s70_kuramoto_sync.npz`
- Working paper: Section W5-B

---

### W5-C: WEYL-NP-SCALARS-70 -- Newman-Penrose Scalars Under BCS

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: SP (1/9 reviewers)

**Prompt**:

Compute the full set of Newman-Penrose scalars Psi_0 through Psi_4 for the acoustic metric under BCS backreaction. PETROV-BCS-69 showed the Petrov type is preserved (D for static, G for dynamic). This computation extracts the individual NP scalars.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the Petrov data from s69_petrov_bcs.npz.
2. Construct the NP tetrad (l, n, m, m*) for the acoustic metric at the fold.
3. Compute Psi_A = C_{abcd} * l^a * X^b * l^c * Y^d for appropriate tetrad projections:
   - Psi_0 = C_{abcd} * l^a * m^b * l^c * m^d (ingoing radiation)
   - Psi_1 = C_{abcd} * l^a * n^b * l^c * m^d (longitudinal frame dragging)
   - Psi_2 = C_{abcd} * l^a * m^b * m*^c * n^d (Coulomb-like)
   - Psi_3 = C_{abcd} * l^a * n^b * m*^c * n^d (outgoing frame dragging)
   - Psi_4 = C_{abcd} * n^a * m*^b * n^c * m*^d (outgoing radiation)
4. For the acoustic white hole, Psi_4 should dominate (outgoing radiation from the white hole).
5. Compare bare vs BCS-dressed values.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_petrov_bcs.npz`

**Pre-registered gate**: **WEYL-NP-SCALARS-70**
- INFO: Report all 5 NP scalars, bare and BCS-dressed

**Output files**:
- Script: `computations/s70_weyl_np_scalars.py`
- Data: `computations/s70_weyl_np_scalars.npz`
- Working paper: Section W5-C

---

### W5-D: NEAR-EXTREMAL-70 -- BCS Thermodynamics Near Extremality

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: SP (1/9 reviewers)

**Prompt**:

BCS-SURFACE-69 found kappa_BCS = 3.59 (surface gravity at the BCS gap "horizon") and T_BCS = 0.571 M_KK. The BCS gap is nearly extremal (kappa_0 = 0). Compute the thermodynamic properties near extremality: entropy, specific heat, and the approach to T = 0.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load BCS surface gravity data from s69_bcs_surface_gravity.npz.
2. Near extremality, the specific heat C ~ T^alpha where alpha depends on the near-horizon geometry. For Reissner-Nordstrom: C ~ T. For the BCS gap: determine alpha from the dispersion relation.
3. The entropy at the BCS gap: S_BCS = integral_0^{T_BCS} C(T)/T dT.
4. Compare the temperature hierarchy: T_GH/T_BCS = 116 (from S69). Is T_GH the geometric Hawking temperature of the fiber, and T_BCS the condensate temperature?
5. Compute the gap-closing temperature: T_c where Delta(T_c) = 0. This is the BCS critical temperature.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_bcs_surface_gravity.npz`

**Pre-registered gate**: **NEAR-EXTREMAL-70**
- INFO: Report near-extremal thermodynamics, specific heat exponent, entropy

**Output files**:
- Script: `computations/s70_near_extremal.py`
- Data: `computations/s70_near_extremal.npz`
- Working paper: Section W5-D

---

### W5-E: BAO-PEAK-DAMP-70 -- 2nd/3rd BAO Harmonic at n_s = 0.9595

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

BAO harmonics beyond the first peak are sensitive to the spectral index n_s and the sound horizon r_d. The framework predicts n_s = 0.9595 (slightly higher than Planck 0.9649 but within 1.2% from PVD-CL-69). Compute the 2nd and 3rd BAO harmonics and their damping.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. The BAO signal in P(k) is an oscillation: P_BAO(k) = P_smooth(k) * [1 + A * exp(-(k*Sigma)^2) * sin(k*r_d + phi)] where r_d is the sound horizon, Sigma is the Silk damping scale, and A is the amplitude.
2. Compute the 1st peak (k_1 = pi/r_d), 2nd peak (k_2 = 2*pi/r_d), 3rd peak (k_3 = 3*pi/r_d).
3. The damping at each peak: exp(-(k_n * Sigma)^2). At n_s = 0.9595 (FW) vs 0.9649 (Planck), the P_smooth(k) changes, modifying the BAO peak heights.
4. Compute the relative peak height ratios: H_2/H_1 and H_3/H_1 for both FW and LCDM.
5. Compare with DESI DR1 BAO measurements. The 2nd peak has been detected; the 3rd is marginal.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_pvd13_da.npz`

**Pre-registered gate**: **BAO-PEAK-DAMP-70**
- INFO: Report 2nd/3rd harmonic peak ratios for FW vs LCDM

**Output files**:
- Script: `computations/s70_bao_peak_damp.py`
- Data: `computations/s70_bao_peak_damp.npz`
- Working paper: Section W5-E

---

### W5-F: VOID-CS2-70 -- Void Profiles at c_s^2 = 0 vs 1

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

Void density and velocity profiles are sensitive to c_s^2 of dark energy. Clustering DE (c_s^2 = 0) fills voids partially, changing the profile shape.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. The void density profile in the linear regime: delta(r) = delta_v * (1 - (r/R_v)^3) for r < R_v (top-hat void).
2. With c_s^2 = 0 (clustering DE): delta_DE(r) = (1+w) * delta_m(r) (DE tracks matter, including inside voids).
3. With c_s^2 = 1 (smooth DE): delta_DE = 0 everywhere (DE does not cluster).
4. The compensated void profile (matter + DE) at c_s^2 = 0 has a different shape at the void wall.
5. Compute the stacked void profile for both cases at R_v = [10, 20, 30] Mpc/h and z = 0.5.
6. Quantify the difference: max |delta(c_s^2=0) - delta(c_s^2=1)| / delta.
7. Estimate the number of voids needed to distinguish at 3-sigma.

**Input files**:
- `computations/canonical_constants.py`

**Pre-registered gate**: **VOID-CS2-70**
- INFO: Report void profile difference and required sample size

**Output files**:
- Script: `computations/s70_void_cs2.py`
- Data: `computations/s70_void_cs2.npz`
- Working paper: Section W5-F

---

### W5-G: PDF-FOLDED-70 -- Density PDF with Folded f_NL

**Agent**: `cosmic-web-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Cosmic Web (1/9 reviewers)

**Prompt**:

EUCLID-FOLDED-69 showed that folded f_NL is undetectable by Euclid (sigma = 18.9, SNR = 0.007). But the 1-point density PDF might be more sensitive because it captures all-orders non-Gaussianity, not just the bispectrum.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. The density PDF with Gaussian initial conditions is log-normal: P(delta) = (1/(sqrt(2*pi)*sigma)) * (1/(1+delta)) * exp(-ln^2(1+delta)/(2*sigma^2)).
2. With folded f_NL, the PDF acquires a skewness: S_3 = <delta^3> / <delta^2>^2 = (6/5) * f_NL^{fold} * sigma(R).
3. Using the Edgeworth expansion: P(delta) = P_G(delta) * [1 + (S_3/6) * H_3(delta/sigma) + ...] where H_3 is the 3rd Hermite polynomial.
4. Compute the KL divergence between the folded f_NL PDF and the Gaussian PDF at sigma = 0.5 (nonlinear scale).
5. Estimate the number of independent density cells needed to detect the KL divergence at 3-sigma.
6. Compare this sample size with the number of cells in a Euclid-volume survey.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_euclid_folded.npz`

**Pre-registered gate**: **PDF-FOLDED-70**
- INFO: Report KL divergence and required sample size

**Output files**:
- Script: `computations/s70_pdf_folded.py`
- Data: `computations/s70_pdf_folded.npz`
- Working paper: Section W5-G

---

### W5-H: EPSH-ALPHA-SENSITIVITY-70 -- Sensitivity of eps_H to Strong Coupling

**Agent**: `lizzi-spectral-functional-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Lizzi (1/9 reviewers)

**Prompt**:

Compute d(eps_H)/d(alpha) where alpha parametrizes the spectral function f_alpha(x) = x^{alpha/2} (so alpha = 1 gives the framework's sqrt(x)). This determines how sensitive the slow-roll parameter (and hence n_s) is to the spectral function choice near alpha = 1.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. For alpha in [0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.5], compute S_alpha(tau) = sum_n d_n * |lambda_n|^alpha at tau values near the fold.
2. Compute eps_H(alpha) = -(1/S_alpha) * dS_alpha/dtau at tau_fold.
3. Compute d(eps_H)/d(alpha) by finite differences.
4. Report: how much does eps_H change per unit change in alpha? If |d(eps_H)/d(alpha)| < 0.01, eps_H is robust. If > 0.1, it is sensitive.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s30b_full_spectrum.npz`

**Pre-registered gate**: **EPSH-ALPHA-SENSITIVITY-70**
- INFO: Report d(eps_H)/d(alpha) and sensitivity classification

**Output files**:
- Script: `computations/s70_epsh_alpha_sensitivity.py`
- Data: `computations/s70_epsh_alpha_sensitivity.npz`
- Working paper: Section W5-H

---

### W5-I: CONSISTENCY-FI-MAP-70 -- Functional Independence vs Scheme Dependence Map

**Agent**: `lizzi-spectral-functional-theorist`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Lizzi (1/9 reviewers)

**Prompt**:

TRANSIT-CONSIST-69 found 7 observables collapse to 5 independent ones with 2 consistency relations. Classify each consistency relation as FUNCTIONAL-INDEPENDENT (FI) or SCHEME-DEPENDENT (SD).

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the transit consistency data from s69_transit_consistency.npz.
2. The two consistency relations from W2-A:
   a. alpha_s = 0 (structural, from k << k_tach by 60 decades)
   b. Impulsive r-n_T-n_s-f_NL consistency
3. For relation (a): alpha_s = d(n_s)/d(ln k) involves the scale-dependence of the spectral action. This is FI because it depends on the geometric fact that all CMB scales are deep in the super-horizon limit, not on the spectral function choice. Verify by computing alpha_s in 3 spectral functions.
4. For relation (b): the impulsive consistency links r, n_T, n_s, and f_NL through the transit dynamics. This involves eps_H (approximately FI) and the mode equation (potentially SD at the squeeze/initial state level).
5. Classify each relation as FI or SD with quantitative evidence.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_transit_consistency.npz`
- `computations/s30b_full_spectrum.npz`

**Pre-registered gate**: **CONSISTENCY-FI-MAP-70**
- INFO: Classification of each consistency relation as FI or SD

**Output files**:
- Script: `computations/s70_consistency_fi_map.py`
- Data: `computations/s70_consistency_fi_map.npz`
- Working paper: Section W5-I

---

### W5-J: 3-MODE-BAW-70 -- Multi-Mode BAW Design

**Agent**: `tesla-resonance`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Tesla (1/9 reviewers)

**Prompt**:

BAW-ANALOG-69 designed a single-mode BAW experiment requiring N_shots = 71 for 3-sigma squeeze detection. A multi-mode BAW (3 coupled resonators) could amplify the signal through mode-mode coupling.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Design a 3-coupled BAW resonator system with frequencies f_1, f_2, f_3 chosen to mimic the B2/B1/B3 sector structure.
2. The coupling between resonators is via shared electrodes: J_{12}, J_{13}, J_{23}.
3. Compute the normal mode frequencies and mode shapes.
4. The squeeze generation rate is enhanced by constructive interference of 3 modes: delta_r ~ 3^{1/2} * delta_r_single.
5. Compute the reduced N_shots for 3-sigma detection with the 3-mode system.
6. Report the design parameters (frequencies, couplings, Q-factors) for a practical implementation.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_baw_analog.npz`

**Pre-registered gate**: **3-MODE-BAW-70**
- INFO: Report design parameters and N_shots reduction

**Output files**:
- Script: `computations/s70_3_mode_baw.py`
- Data: `computations/s70_3_mode_baw.npz`
- Working paper: Section W5-J

---

### W5-K: DESI-DR3-UPDATE-70 -- Decision Tree Update for DESI DR3

**Agent**: `mack-cosmic-bridge`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Mack (1/9 reviewers)

**Prompt**:

DESI DR3 will provide approximately 5x the spectroscopic sample of DR1, with better redshift coverage at z > 1. Update the S68 decision tree (s68_desi_dr3_forecast.npz) with the S69 data test results.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. Load the S68 DESI DR3 forecast from s68_desi_dr3_forecast.npz.
2. Update the decision tree with S69 results:
   - PVD-DA-69: D_M/r_d chi^2/dof = 2.08 (the framework's weakest link)
   - PVD-FSIG8-69: f*sigma_8 chi^2/dof = 0.761 (FW preferred)
   - The LRG2 bin at z = 0.706 has the worst pull (-2.26 sigma)
3. Forecast the DR3 improvement:
   - Statistical errors scale as 1/sqrt(N): factor ~2.2x improvement
   - Systematic floors remain (calibration, template mismatch)
4. Compute the DR3 discriminating power for FW vs LCDM:
   - D_M/r_d: if the -0.68 sigma mean pull persists, DR3 reaches ~1.5 sigma coherent pull
   - f*sigma_8: if Delta chi^2 = -1.19 persists, DR3 reaches ~2.6 sigma
5. Pre-register the DESI DR3 decision tree:
   - If chi^2/dof(D_M) drops below 1.5: BAO tension RESOLVED
   - If chi^2/dof(D_M) rises above 3.0 with DR3 precision: w_a = 0 under severe stress
   - If f*sigma_8 Delta_chi^2 < -3: FW firmly preferred over LCDM

**Input files**:
- `computations/canonical_constants.py`
- `computations/s68_desi_dr3_forecast.npz`
- `computations/s69_pvd13_da.npz`
- `computations/s69_pvd05_fsigma8.npz`

**Pre-registered gate**: **DESI-DR3-UPDATE-70**
- INFO: Updated decision tree and discriminating power forecast

**Output files**:
- Script: `computations/s70_desi_dr3_update.py`
- Data: `computations/s70_desi_dr3_update.npz`
- Working paper: Section W5-K

---

### W5-L: GEODESIC-MODULI-70 -- Geodesic Distance on Moduli Space

**Agent**: `baptista-spacetime-analyst`
**Model**: opus
**Cost**: LOW
**Carry-Forward**: Baptista (1/9 reviewers)

**Prompt**:

The moduli space of left-invariant metrics on SU(3) has a DeWitt metric G_{ij} = d^2 S / (dg_i dg_j). The geodesic distance from the round metric (tau = 0) to the fold (tau = 0.19) determines the "distance" in moduli space that the transit traverses. This connects to the Swampland distance conjecture.

Import all constants from `computations/canonical_constants.py`.

**Computation**:
1. The DeWitt metric in the 1D Jensen subspace is G_{tau tau} = 5.0 (from S63 KINETIC-NORM-63).
2. The geodesic distance in the full 36D moduli space from the round metric to the fold is:
   d(round, fold) = integral_0^{0.19} sqrt(G_{tau tau}) dtau = sqrt(5.0) * 0.19 = 0.425 (in M_KK units).
3. The Swampland distance conjecture (SWAMP-69, c = 3.52 >> 1): delta(phi) > c implies tower of states. Does d(round, fold) satisfy the conjecture?
4. Extend to the full 36D: compute the geodesic in the higher-dimensional moduli space. Since the Jensen direction is an attractor (OFF-JENSEN-GRAD-69 permanent theorem), the geodesic should stay close to the Jensen line. Compute the deviation using the off-Jensen Hessian eigenvalues.
5. Report the geodesic distance and the Swampland ratio phi / M_Pl.

**Input files**:
- `computations/canonical_constants.py`
- `computations/s69_off_jensen_gradient.npz`
- `computations/s69_swampland.npz`

**Pre-registered gate**: **GEODESIC-MODULI-70**
- INFO: Report geodesic distance and Swampland distance comparison

**Output files**:
- Script: `computations/s70_geodesic_moduli.py`
- Data: `computations/s70_geodesic_moduli.npz`
- Working paper: Section W5-L

---

## VIII. Constraint Gates Summary

| Gate ID | Wave | Type | Level | PASS | FAIL |
|:--------|:-----|:-----|:-----|:-----|:-----|
| LEGGETT-VACUUM-70 | W1-A | A_s gap | CRITICAL | r_L > 0.3 | r_L = 0 |
| F0-ALPHA-S-70 | W1-B | Particle physics | CRITICAL | Consistent f_0 in [0.5, 5.0] | No such f_0 |
| Q-SOUND-70 | W1-C | DE perturbations | CRITICAL | c_s^2 = 0 derived | c_s^2 = 1 |
| BCS-GAP-CANONICAL-70 | W1-D | Housekeeping | HK | INFO | -- |
| RATIO-GILKEY-70 | W1-E | Housekeeping | HK | INFO | -- |
| BELL-GGE-70 | W1-F | Quantum state | HIGH | S > 2 all modes | S <= 2 any mode |
| NON-PERT-SA-70 | W1-G | SA validity | HIGH | deviation < 10% | deviation > 50% |
| PARAMETRIC-GGE-70 | W1-H | A_s gap | HIGH | > 0.1 OOM enhancement | < 0.01 OOM |
| TRAPPED-ACOUSTIC-70 | W1-I | Causal structure | HIGH | No trapped surface | Trapped surface |
| LMAX7-PW-70 | W1-J | Convergence | HIGH | r_7 < 1.5, delta < 1% | r_7 > 2 or delta > 5% |
| FULL-COV-PANTHEON-70 | W2-A | Observational | HIGH | INFO | -- |
| FULL-COV-RSD-70 | W2-B | Observational | HIGH | INFO | -- |
| CLASS-ISW-70 | W2-C | Observational | HIGH | FW/Quint > 5% (l=2-10) | FW/Quint < 1% |
| PHI-EFF-COMPOUND-70 | W2-D | Compound obs. | HIGH | cos in [-0.181, +0.800] | -- |
| VOID-SIZE-70 | W2-E | Observational | HIGH | chi^2/dof < 2 | chi^2/dof > 5 |
| BERRY-DENNIS-GGE-70 | W3-A | Bucher Test 1 | MEDIUM | chi^2/ndof < 2, <v> to 30% | chi^2/ndof > 5 |
| SUPERLUMINAL-FRACTION-70 | W3-B | Bucher Test 2 | MEDIUM | F within 20%, F_L > 50% | F_L < 30% |
| GGE-PAIR-CORR-70 | W3-C | Bucher Test 3 | MEDIUM | g_{++}(0)<0.1, g_{+-}(0)>2 | g_{++}(0)>1 or g_{+-}(0)<1 |
| ANNIHILATION-TIME-70 | W3-D | Bucher Test 4 | MEDIUM | t_ann in [1e-43, 1e-40], ratio [0.1,10] | Outside range |
| DISCRETE-BERRY-DENNIS-70 | W3-E | Bucher Test 5 | MEDIUM | chi^2/ndof < 3 on CG(24) | No discrete limit N<100 |
| ZETA-AS-BUDGET-70 | W3-F | A_s scheme | MEDIUM | INFO | -- |
| LEGGETT-MOMENT-70 | W3-G | Spectral moment | MEDIUM | INFO | -- |
| PENROSE-SEQUENCE-70 | W3-H | Visualization | MEDIUM | INFO | -- |
| KRETSCHNER-BCS-70 | W3-I | Curvature | MEDIUM | INFO | -- |
| MEISSNER-ED-70 | W3-J | w_0 systematic | MEDIUM | INFO | -- |
| HYDROSTATIC-CLUSTER-70 | W4-A | Observational | MEDIUM | INFO | -- |
| CHIRP-PENUMBRA-70 | W4-B | WKB validity | MEDIUM | WKB < 10% | WKB > 50% |
| CAVITY-BCS-HORIZON-70 | W4-C | Resonance | MEDIUM | INFO | -- |
| AP-VOID-70 | W4-D | Observational | MEDIUM | INFO | -- |
| BULK-FLOW-70 | W4-E | Observational | MEDIUM | INFO | -- |
| BETTI-FISHER-70 | W4-F | Forecast | MEDIUM | INFO | -- |
| OFF-JENSEN-HESS-70 | W4-G | Moduli space | MEDIUM | INFO | -- |
| SPECTRAL-DIM-FLOW-70 | W4-H | UV/IR flow | MEDIUM | INFO | -- |
| BCS-PROXIMITY-70 | W4-I | BCS scope | MEDIUM | INFO | -- |
| DM-PAIR-DECAY-70 | W5-A | DM stability | LOW | Gamma < FIRAS | Gamma > t_univ^{-1} |
| KURAMOTO-SYNC-70 | W5-B | Synchronization | LOW | K_c < 3.60 | K_c > 3.60 |
| WEYL-NP-SCALARS-70 | W5-C | NP scalars | LOW | INFO | -- |
| NEAR-EXTREMAL-70 | W5-D | Thermodynamics | LOW | INFO | -- |
| BAO-PEAK-DAMP-70 | W5-E | BAO harmonics | LOW | INFO | -- |
| VOID-CS2-70 | W5-F | Void profiles | LOW | INFO | -- |
| PDF-FOLDED-70 | W5-G | Non-Gaussianity | LOW | INFO | -- |
| EPSH-ALPHA-SENSITIVITY-70 | W5-H | Sensitivity | LOW | INFO | -- |
| CONSISTENCY-FI-MAP-70 | W5-I | Classification | LOW | INFO | -- |
| 3-MODE-BAW-70 | W5-J | Lab design | LOW | INFO | -- |
| DESI-DR3-UPDATE-70 | W5-K | Decision tree | LOW | INFO | -- |
| GEODESIC-MODULI-70 | W5-L | Swampland | LOW | INFO | -- |

**Total: 46 gates (40 agenda computations + 2 housekeeping + 4 additional Bucher singularity tests from Section 4)**

---

## IX. Decision Points

### After Wave 1

1. **LEGGETT-VACUUM-70 (W1-A)**: If r_L > 0.3, the A_s gap drops to approximately 0.31 OOM. The remaining gap becomes accessible to higher-order BCS corrections and parametric resonance. If r_L = 0, the gap remains at 0.485 OOM and new channels must be identified.

2. **F0-ALPHA-S-70 (W1-B)**: If a consistent f_0 exists, the alpha_s tension is resolved through normalization. The Higgs mass must be re-checked at the new f_0. If no f_0 works, the tension is structural and points to missing physics (non-perturbative corrections, higher PW modes, or modified GUT-scale matching).

3. **Q-SOUND-70 (W1-C)**: If c_s^2 = 0 is derived, the ISW tracking signal is a genuine prediction (7.6% FW/Quint, detectable by Euclid at 2.5 sigma, 21cm at 7.9 sigma). If c_s^2 = 1, the ISW tracking signal vanishes and the framework loses its most distinctive observational discriminant.

4. **BCS-GAP-CANONICAL (W1-D)**: All subsequent computations using Delta_BCS must import the canonical value. This must complete before Wave 2.

### After Wave 2

5. **FULL-COV-PANTHEON-70 + FULL-COV-RSD-70 (W2-A/B)**: If Delta_chi^2 with full covariance remains significantly negative (< -3 combined), the FW preference over LCDM is robust against systematic correlations. If Delta_chi^2 weakens to near zero, the preference was partly an artifact of ignoring off-diagonal covariance.

6. **CLASS-ISW-70 (W2-C)**: If the Boltzmann-level ISW confirms the simplified calculation (> 5% FW/Quint at low l), the pre-registered CMB-S4 decision tree from CMB-S4-NS-69 gains the ISW channel as a second discriminant.

### After Wave 3

7. **Bucher tests (W3-A through W3-E)**: If 3/5 Bucher tests PASS, the Berry-Dennis universality connects the GGE relic to a well-studied class of random wave fields. This provides new predictions for BEC analog experiments and validates the Gaussian random wave model for the GGE. If all 5 FAIL, the GGE is not in the Berry-Dennis universality class (possibly due to CG(24) being too small or the GGE being non-Gaussian).

### After Wave 5

8. **Full session assessment**: With all 42 gates computed, update the A_s gap budget (incorporating LEGGETT-VACUUM-70, PARAMETRIC-GGE-70, PHI-EFF-COMPOUND-70, and ZETA-AS-BUDGET-70), the alpha_s status (F0-ALPHA-S-70, LMAX7-PW-70, NON-PERT-SA-70), and the observational scorecard (all PVD-* tests + forecasts).

---

## X. Execution Notes

- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- **Output directory**: `computations/`
- **Script prefix**: `s70_`
- **Results file**: `sessions/archive/session-70/session-70-results-workingpaper.md`
- **Total computations**: 40 agenda + 2 housekeeping + 4 additional Bucher tests = 46
- **Wave distribution**: W1 (10), W2 (5), W3 (10), W4 (9), W5 (12) -- note some LOW computations are cheap and can run in parallel with MEDIUM
- **Estimated cost**: 46 agents x opus = HIGH total; expect 8-12 hours with parallel execution per wave
- **Input file verification**: All referenced .npz files have been verified to exist in computations/
- **Convention**: All scripts MUST `from canonical_constants import *` and MUST NOT hardcode M_KK, Delta, a_0, a_2, a_4, or tau_fold
- **Critical path**: W1-A (LEGGETT-VACUUM-70) -> entire A_s gap budget -> session assessment. This single computation determines the session's strategic outcome.
- **Substrate framing reminder**: All agents must frame results in substrate language (spectral action, fiber excitations, GGE physics) per the phononic framing rules. Container thinking (space expands, fields in curved spacetime) must be corrected in prompts.
