## III-a. Wave 1: CRITICAL + HIGH (4 tasks, parallel)

### W1-1: Self-Consistent q-Theory + BCS Gap Equation (Q-THEORY-SELFCONSISTENT-46)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: HIGH (self-consistent gap solve at 40+ tau values x 992 modes)
**Rollup items**: #1 (7/7 convergence), #2 (T3-T5 lock-on, 3/7)

**Prompt**:

You are computing the single most important quantity in the phonon-exflation framework: the self-consistent q-theory Gibbs-Duhem crossing with a tau-dependent BCS gap Delta(tau).

**Why this is critical.** S45 established the q-theory BCS-corrected crossing at tau* = 0.209 (Q-THEORY-BCS-45, PASS). This used a CONSTANT gap approximation: Delta was fixed at its fold value Delta_0 = 0.770 M_KK across all tau. In reality, Delta(tau) depends on the pairing interaction V(tau) and the density of states N(E_F, tau), both of which vary with the Jensen deformation. The self-consistent gap equation is:

    1/g(tau) = sum_k d_k / (2 E_k(tau))

where E_k(tau) = sqrt(lambda_k(tau)^2 + Delta(tau)^2), d_k = dim(p,q)^2 is the Peter-Weyl degeneracy, and g(tau) is the BCS coupling extracted from the pairing interaction V_{kl}(tau) restricted to the BCS-active modes. The coupling g(tau) inherits tau-dependence from the B2 sector Casimir eigenvalue structure.

The q-theory Gibbs-Duhem condition for the gravitating vacuum energy is:

    rho_gs(tau) = epsilon(tau) - tau * d(epsilon)/d(tau) = 0

where epsilon(tau) = (1/2) sum_k d_k^{singlet} ln((lambda_k(tau)^2 + Delta(tau)^2) / mu_ref^2) is the BCS trace-log restricted to the (0,0) singlet sector (16 modes, EIH projection from S22b block-diagonal theorem).

The decisive question: does self-consistent Delta(tau) lock the crossing tau* onto the fold at tau_fold = 0.190?

**The T3-T5 crossing (item #2).** The spectral-geometer review (S45) identified a true eigenvalue crossing at tau = 0.19104 between the T3 (singlet top) and T5 (non-singlet bottom) eigenvalues. The BCS gap Delta(tau) may have a discontinuity or kink at this crossing because the DOS rearranges. If so, the q-theory crossing tau* could lock onto the spectral crossing rather than varying smoothly with Delta. Explicitly check: does Delta(tau) have a slope discontinuity at tau = 0.191 +/- 0.003?

**Computation Steps**:

1. **Load data.** Eigenvalues lambda_k(tau) from `tier0-computation/s44_dos_tau.npz` and `tier0-computation/s41_spectral_refinement.npz`. BCS coupling and pairing matrix from `tier0-computation/s42_hauser_feshbach.npz`. Prior q-theory results from `tier0-computation/s45_qtheory_bcs.npz` (constant-gap crossing at 0.209). Import constants from `tier0-computation/canonical_constants.py`: tau_fold, E_cond, Delta_0_GL, a0_fold, a2_fold, M_KK_gravity.

2. **Construct tau grid.** Use 60 values: tau = 0.00, 0.02, 0.05, 0.08, 0.10, 0.12, 0.14, 0.16, 0.17, 0.175, 0.180, 0.185, 0.186, 0.187, 0.188, 0.189, 0.190, 0.191, 0.192, 0.193, 0.194, 0.195, 0.196, 0.198, 0.200, 0.205, 0.210, 0.215, 0.220, 0.230, 0.240, 0.250, 0.260, 0.280, 0.300, 0.320, 0.340, 0.360, 0.380, 0.400, 0.420, 0.440, 0.460, 0.480, 0.500 (dense scan around 0.185-0.200 to catch the T3-T5 crossing and potential tau* lock).

3. **Self-consistent BCS gap at each tau.** For each tau value:
   a. Interpolate or recompute eigenvalues lambda_k(tau) for all 992 modes.
   b. Compute the effective BCS coupling g_eff(tau) from the B2-sector pairing interaction V(tau). Use the flatband approximation as in S45 W2-R5: g_eff = V_B2 * N(E_F, tau) where V_B2 is the singlet pairing interaction (known from s42_hauser_feshbach.npz) and N(E_F, tau) is the DOS at the Fermi level (mu = 0, S34 result).
   c. Solve the gap equation self-consistently: iterate Delta_new = g_eff * sum_k d_k Delta / (2 E_k) until convergence (|Delta_new - Delta_old| / Delta_old < 1e-10). Initial guess: Delta_0_GL = 0.770.
   d. Store Delta(tau), E_cond(tau), n_k(tau) for each tau.

4. **BCS trace-log at each tau.** Compute TL_singlet(tau) = (1/2) sum_{k in singlet} ln((lambda_k(tau)^2 + Delta(tau)^2) / mu_ref^2) with the SELF-CONSISTENT Delta(tau). The singlet sector has 16 modes (8 eigenvalues with multiplicity 2 each for particle/hole).

5. **Gibbs-Duhem crossing.** Compute rho_gs(tau) = epsilon(tau) - tau * d(epsilon)/d(tau) using numerical differentiation (central differences, step h = 0.001). Find tau* where rho_gs crosses zero. Report tau* and d(rho_gs)/d(tau) at the crossing (stability check: should be negative for a stable equilibrium).

6. **T3-T5 lock diagnostic.** Compute d(Delta)/d(tau) across the dense scan around tau = 0.190. Check for slope discontinuity (|d^2(Delta)/d(tau)^2| spike at the T3-T5 crossing). Report the ratio Delta(0.191)/Delta(0.189) -- if this ratio differs from 1.000 by more than 0.1%, there is a gap discontinuity at the spectral crossing.

7. **Displacement residual.** Compute the CC gap at the crossing: rho_gs(tau*) = 0 by construction. At the fold: rho_fold = c_2 * (tau* - tau_fold)^2 where c_2 = d^2(epsilon)/d(tau)^2 at tau*. Convert to orders of magnitude relative to rho_Lambda_obs = 2.7e-47 GeV^4.

8. **Cross-checks.** (a) Delta -> 0 limit: must recover S45 W1-R1 vacuum result tau* = 0.472. (b) Delta = constant: must recover S45 W2-R5 result tau* = 0.209. (c) mu_ref independence: verify rho_gs is independent of mu_ref (it cancels in the Gibbs-Duhem identity).

**Formula Audit**:
- (a) Formula: TL_singlet(tau) = (1/2) sum_{k in singlet} d_k ln((lambda_k(tau)^2 + Delta(tau)^2) / mu_ref^2). [TL] dimensionless. [lambda_k] = [Delta] = [mu_ref] = M_KK.
- (b) Dimensional check: argument of ln is (M_KK^2 / M_KK^2) = dimensionless. Verified.
- (c) Limiting case: Delta = 0 recovers vacuum trace-log (S45 W1-R1). Verified to machine epsilon.
- (d) Citation: Volovik Papers 05, 15-16 (q-theory); Abrikosov-Gorkov-Dzyaloshinski Ch. 7 (BCS gap equation); S45 W2-R5 (constant-gap q-theory).

**Pre-registered gate Q-THEORY-SELFCONSISTENT-46**:
- PASS: tau* in [0.17, 0.21] with self-consistent Delta(tau)
- FAIL: No crossing in [0.05, 0.35]

**Pre-registered gate Q-THEORY-T3T5-46** (subsidiary):
- PASS: tau* locks onto [0.188, 0.194]
- FAIL: tau* outside [0.15, 0.25]

**Input files**:
- `tier0-computation/s45_qtheory_bcs.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/s44_dos_tau.npz`
- `tier0-computation/canonical_constants.py`
- `researchers/Volovik/05_2005_Volovik_Vacuum_Energy_Cosmological_Constant.md`
- `researchers/Volovik/15_2008_Klinkhamer_Volovik_q_Theory.md`
- `researchers/Volovik/16_2017_Klinkhamer_Volovik_q_Theory_Dark_Energy.md`

**Output files**:
- Script: `tier0-computation/s46_qtheory_selfconsistent.py`
- Data: `tier0-computation/s46_qtheory_selfconsistent.npz`
- Plot: `tier0-computation/s46_qtheory_selfconsistent.png`

**Working paper section**: W1-R1

**Critical notes**:
- Read Volovik Papers 05, 15-16 FIRST. The Gibbs-Duhem identity rho_gs = epsilon - tau * d(epsilon)/d(tau) is a thermodynamic identity, not an ansatz.
- The gap equation MUST be solved self-consistently at each tau. Do NOT use constant gap.
- The T3-T5 crossing at tau = 0.19104 is the key spectral feature. Dense scan there is essential.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
- Report ALL intermediate values of Delta(tau), tau*, c_2, displacement residual.

---

### W1-2: Hose-Count Pair Mode Exponent (HOSE-COUNT-46)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM (BdG diagonalization per sector, ~10 sectors)
**Rollup items**: #10 (6/7 convergence), #11 (K_7 selection rules)

**Prompt**:

You are computing the pair-mode scaling exponent alpha that determines the spectral tilt n_s in the phonon-exflation framework.

**The n_s crisis.** Session 45 established that the internal spectral tilt is n_s = -0.68, set by d=3 Kibble-Zurek universality from the 3-sector decomposition (B1, B2, B3). This is PROVEN -- the KZ formula n_s - 1 = -d*z*nu/(1 + z*nu) with d=3 (sector count from [iK_7, D_K] = 0), z=2 (Bogoliubov), nu=0.6301 (3D XY) gives n_s = -0.6815, matching the computed forward-backward asymptotic value to 0.13%. The Planck measurement n_s = 0.9649 requires a +1.65 shift. The tilt decomposes as:

    n_s - 1 = alpha - beta

where alpha is the "hose count exponent" (how many independent pair creation channels exist at each Casimir wavenumber k = sqrt(C_2)) and beta is the "per-hose rate exponent" (how fast each channel creates pairs, decreasing with k). Single-particle gives alpha = 6 (Weyl degeneracy d^2 ~ k^6). Collective gives alpha = 0 (one mode per branch). Planck needs alpha ~ 1.

**What to compute.** For each (p,q) sector in the BCS-active spectrum, diagonalize the sector-restricted BdG Hamiltonian and count the number of independent pair modes. The pair modes are eigenvectors of:

    H_BdG^{(p,q)} = ( h_{(p,q)}     Delta_{(p,q)} )
                     ( Delta*_{(p,q)}  -h_{(p,q)}   )

where h_{(p,q)} is the single-particle Hamiltonian restricted to sector (p,q) (diagonal in the eigenvalue basis: h_{kk'} = lambda_k delta_{kk'} for k in sector (p,q)) and Delta_{(p,q)} is the BCS gap matrix restricted to that sector (from the pairing interaction V_{kl} in s42_hauser_feshbach.npz).

The pair mode count at Casimir wavenumber k = sqrt(C_2(p,q)) is the number of DISTINCT eigenvalues of H_BdG^{(p,q)} (or equivalently, the rank of the pairing matrix Delta_{(p,q)} restricted to modes within the BCS window).

**K_7 selection rules (item #11).** The Cooper pair operator P^+ = sum_k c_{k,up} c_{-k,down} carries K_7 charge q_7(k) + q_7(-k). For K_7-neutral pairs (q_7 = 0, self-conjugate reps in B2), all pair modes are K_7-allowed. For charged pairs (B1-B3 inter-sector), only q_7(k) + q_7(k') = 0 modes are allowed. This halves the pair count for inter-sector contributions. Determine the K_7 charge of every pair mode and report n_allowed(k) and n_forbidden(k) separately.

**GPV fragmentation prediction.** From nuclear physics, the giant pairing vibration (GPV) fragments into 2-4 components per sector when the pairing window exceeds the single-particle level spacing. The fragmentation strength scales as S_pair ~ d(p,q)^{1/2}, predicting alpha_frag ~ 1.0 from nuclear pair-transfer sum rules (cf. Cappuzzello et al. 2015, Fortunato et al. 2019 -- Papers 23, 24 in researchers/Landau/).

**Computation Steps**:

1. **Load data.** From `tier0-computation/s42_hauser_feshbach.npz`: eigenvalues, sector labels (B1/B2/B3), K_7 charges, pairing interaction V_{kl}, representation labels (p,q), Casimir values C_2(p,q). From `tier0-computation/canonical_constants.py`: Delta_0_GL, E_cond, tau_fold.

2. **Identify BCS-active sectors.** Sectors with eigenvalues within the BCS pairing window |lambda_k - E_F| < omega_D (where E_F = 0 from S34, omega_D is the Debye-analogue cutoff, approximately 2*Delta_0). List all sectors and their Casimir wavenumber k = sqrt(C_2).

3. **Construct H_BdG per sector.** For each BCS-active sector (p,q):
   a. Extract the N_{(p,q)} eigenvalues in that sector.
   b. Form the 2N x 2N BdG Hamiltonian using the sector-restricted pairing matrix.
   c. Diagonalize. Count the number of distinct positive eigenvalues (the pair modes).
   d. For each pair mode, compute its K_7 charge.

4. **Pair mode count vs Casimir.** Plot n_pair(k) vs k = sqrt(C_2) on log-log axes. Fit: n_pair(k) ~ k^alpha. Report alpha and its uncertainty (from fit residuals).

5. **K_7 restriction.** Separate: n_pair = n_allowed (K_7-conserving) + n_forbidden (K_7-violating). Refit: n_allowed(k) ~ k^{alpha_restricted}. Report both alpha and alpha_restricted.

6. **n_s prediction.** From the S45 tinfoil analysis: n_s - 1 = alpha - beta where beta = 1.68 (the KZ per-hose exponent, d*z*nu/(1+z*nu) with d=3). Compute n_s = 1 + alpha - beta. Also compute with alpha_restricted.

7. **Cross-checks.** (a) Sum rule: sum of pair-mode strengths must equal total pairing energy. (b) Large-k limit: n_pair should approach Weyl's law (d^2) divided by some factor. (c) Small-k limit: n_pair should approach 1 (singlet has one pair mode).

**Formula Audit**:
- (a) Formula: H_BdG^{(p,q)} = standard Nambu-Gorkov form. [H] = M_KK. n_pair = rank(Delta_{(p,q)}) = number of non-zero singular values.
- (b) Dimensional check: [lambda_k] = [Delta] = M_KK. BdG eigenvalues in M_KK. Pair count dimensionless.
- (c) Limiting case: For a single mode (dim 1 sector), n_pair = 1 (one pair). For free particles (Delta = 0), n_pair = 0 (no pairing).
- (d) Citation: Bogoliubov-de Gennes, "Superconductivity of Metals and Alloys" (1966); Ring-Schuck Ch. 8 (nuclear BdG); Cappuzzello et al. 2015 (GPV fragmentation, Paper 23); S35 RPA-BCS-35.

**Pre-registered gate HOSE-COUNT-46**:
- PASS: alpha in [0.8, 1.2], giving n_s in [0.955, 0.975] (using beta = 1.68)
- FAIL: alpha < 0.5 or alpha > 2.0

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s44_dos_tau.npz`
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/canonical_constants.py`
- `researchers/Landau/23_2015_Cappuzzello_Giant_Pairing_Vibration_14C_15C.md`
- `researchers/Landau/24_2019_Fortunato_GPV_Heavy_Nuclei.md`
- `researchers/Landau/25_2025_GPV_Fragmentation_Many_Body.md`

**Output files**:
- Script: `tier0-computation/s46_hose_count.py`
- Data: `tier0-computation/s46_hose_count.npz`
- Plot: `tier0-computation/s46_hose_count.png`

**Working paper section**: W1-R2

**Critical notes**:
- The target is alpha ~ 1. Weyl gives 6. Collective gives 0. The pair mode count is the INTERMEDIATE quantity.
- K_7 charges are known from s42_hauser_feshbach.npz. Use them for the selection rule.
- The GPV fragmentation analogy (Cappuzzello, Fortunato) predicts alpha ~ 1 from nuclear pair-transfer sum rules. Read Papers 23-25 FIRST.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

### W1-3: Independent Geometric a_2 from Jensen Ricci Scalar (GEOMETRIC-A2-46)

**Agent**: `schwarzschild-penrose-geometer`
**Model**: opus
**Cost**: LOW (purely analytic computation)
**Rollup item**: #31 (4/7 convergence)

**Prompt**:

You are computing the Seeley-DeWitt a_2 coefficient from the analytically known Ricci scalar of the Jensen-deformed SU(3) metric, independent of the spectral eigenvalue sum. This quantifies the truncation error and determines whether the 0.83-decade M_KK tension is a truncation artifact.

**Context.** The heat kernel audit (S45 HEAT-KERNEL-AUDIT-45) classified Seeley-DeWitt coefficients as Tier 2 APPROXIMATION on the finite truncated spectrum. The spectral a_2 = 2776.17 (from s42_constants_snapshot.npz, CONST-FREEZE-42) is computed as:

    a_2^{spectral} = sum_k d_k / lambda_k^2

This is exact for the truncated spectrum (max_pq_sum = 5, 992 modes) but omits all modes at higher truncation. The GEOMETRIC a_2 is:

    a_2^{geometric} = (4 pi)^{-dim/2} * Tr(E) * integral_K dV

For a Dirac operator D on a compact Riemannian manifold K of dimension dim = 8, the a_2 coefficient of the heat kernel Tr(e^{-t D^2}) is:

    a_2 = (4 pi)^{-4} * integral_K Tr_S( R/6 * Id + E ) * sqrt(g) d^8x

where R is the Ricci scalar of the Jensen-deformed SU(3) metric, E is the endomorphism term (curvature of the spinor connection), Tr_S is the trace over the 16-dimensional spinor bundle, and the integral is over the SU(3) manifold with the Jensen metric.

For a LEFT-INVARIANT metric on a Lie group (which the Jensen metric is), the Ricci scalar R(tau) is constant on the manifold (homogeneity). The integral becomes:

    a_2^{geometric} = (4 pi)^{-4} * [ R(tau)/6 * 16 + Tr_S(E) ] * Vol(SU(3), g(tau))

The Ricci scalar R(tau) is known analytically from S20a (147/147 Riemann tensor checks):

    R(tau) = sum_{i,j} R^i_{j} = Tr(Ric)

on the Jensen family g_ij(tau).

**Computation Steps**:

1. **Load data.** From `tier0-computation/r20a_riemann_tensor.npz` or recompute: the Ricci scalar R(tau) and sectional curvatures at tau = tau_fold = 0.19. From `tier0-computation/s42_constants_snapshot.npz`: a_2^{spectral} = 2776.17. Import from `tier0-computation/canonical_constants.py`: tau_fold, a2_fold, Vol_SU3_Haar, M_KK_gravity.

2. **Ricci scalar at the fold.** The Jensen metric on SU(3) has 8 orthogonal generators split into (2 Cartan, 6 root). The Jensen deformation scales root generators by e^{2 tau} relative to Cartan. Compute R(tau_fold) from the structure constants of SU(3) and the Jensen metric tensor. The formula for the Ricci tensor on a Lie group with left-invariant metric is:

    Ric(X,Y) = -(1/2) sum_k g([X,e_k], [Y,e_k]) + (1/4) sum_{k,l} g([e_k,e_l],X) g([e_k,e_l],Y) - (1/2) g([X,Y], sum_k [e_k,e_k]')

    where {e_k} is an orthonormal basis and [,]' involves the metric Lie bracket.

    For SU(3) this simplifies because the Killing form is well-known. Use the S20a verified expressions.

3. **Endomorphism term E.** For the Dirac operator on a Lie group, E = (1/4) R_{abcd} gamma^{ab} gamma^{cd} restricted to the spinor bundle. For a homogeneous space, Tr_S(E) can be computed from the Riemann curvature tensor. In many cases Tr_S(E) = -(1/12) R * dim(spinor) for a standard Dirac operator. Verify this identity or compute Tr_S(E) directly from the S20a Riemann tensor.

4. **Volume.** Vol(SU(3), g(tau)) = Vol_Haar * det(g(tau)/g(0))^{1/2}. The Jensen deformation scales 6 of 8 metric components by e^{2 tau} each, so det(g(tau)/g(0)) = e^{12 tau}. Thus Vol(SU(3), g(tau)) = Vol_SU3_Haar * e^{6 tau} (square root of determinant ratio). Verify from canonical_constants.py: Vol_SU3_Haar = 1349.74.

5. **Geometric a_2.** Combine:

    a_2^{geometric}(tau_fold) = (4 pi)^{-4} * [ R(tau_fold)/6 * 16 + Tr_S(E) ] * Vol(SU(3), g(tau_fold))

6. **Comparison.** Compute the ratio a_2^{spectral} / a_2^{geometric}. This ratio quantifies the truncation error of the max_pq_sum = 5 spectrum. If it is within 30%, the spectral computation is Tier 2 valid.

7. **M_KK implication.** G_N = 1 / (48 pi a_2 M_KK^2) (Sakharov induced gravity). If a_2^{geometric} > a_2^{spectral}, then M_KK^{geometric} < M_KK^{spectral}, narrowing the 0.83-decade tension.

8. **Cross-checks.** (a) At tau = 0 (round SU(3)): R = 12 (standard normalization). Verify a_2^{geometric}(0) against known result. (b) The geometric a_2 must be POSITIVE (Ricci scalar of SU(3) is positive definite for any Jensen deformation, since all sectional curvatures remain positive). (c) Verify Vol(SU(3), g(tau_fold)) against S45 corrected value.

**Formula Audit**:
- (a) Formula: a_2 = (4pi)^{-4} * [R/6 * 16 + Tr_S(E)] * Vol. [a_2] dimensionless (in M_KK units). [R] = M_KK^2. [Vol] = M_KK^{-8}. Combined: M_KK^2 * M_KK^{-8} * (M_KK)^{-8 from (4pi)^{-4}}... NOTE: careful with conventions. In natural units with the metric in M_KK^{-2} units, a_2 is dimensionless.
- (b) Dimensional check: Verify explicitly in the computation.
- (c) Limiting case: tau = 0 (round SU(3)), R = 12.
- (d) Citation: Gilkey (1975), "The Spectral Geometry of a Riemannian Manifold." Berline-Getzler-Vergne Ch. 4. S20a (Riemann tensor, 147 checks). Milnor (1976) for Ricci on Lie groups.

**Pre-registered gate A2-GEOMETRIC-46**:
- PASS: a_2^{spectral} agrees with a_2^{geometric} within 30%
- FAIL: disagreement > 100%

**Input files**:
- `tier0-computation/s42_constants_snapshot.npz` (a_2 spectral, M_KK)
- `tier0-computation/s42_hauser_feshbach.npz` (eigenvalue spectrum for cross-check)
- `tier0-computation/canonical_constants.py`

**Output files**:
- Script: `tier0-computation/s46_geometric_a2.py`
- Data: `tier0-computation/s46_geometric_a2.npz`
- Plot: `tier0-computation/s46_geometric_a2.png`

**Working paper section**: W1-R3

**Critical notes**:
- This is a PURELY ANALYTIC computation. No numerical diagonalization. The Ricci scalar of a left-invariant metric on SU(3) is computable in closed form from the structure constants.
- The Jensen metric is g_ij(tau) = g_ij(0) + (e^{2 tau} - 1) P_ij where P projects onto root directions. All curvature quantities follow from the Lie bracket structure.
- Vol(SU(3)) = 8 sqrt(3) pi^4 = 1349.74 (Weyl integration formula, corrected in S44). Use canonical_constants.py.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

### W1-4: Zubarev Derivation and Keldysh Cross-Check (ZUBAREV-DERIVATION-46)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: LOW (analytic derivation + numerical verification)
**Rollup items**: #25 (5/7 convergence), #42 (Zubarev citation)

**Prompt**:

You are pinning the derivation of the formula alpha = S_GGE / (S_max - S_GGE) that gives the DM/DE ratio, either to a specific equation in Zubarev's published work or by deriving it from first principles. This is the sole MODERATE formula audit violation from S45.

**Why this matters.** The ALPHA-EFF-45 computation (S45 W2-R1) tested 11 methods for computing the DM/DE ratio from the GGE state. Only one -- Method 7c, the formula alpha = S_GGE / (S_max - S_GGE) -- reached the PASS window: alpha = 0.410 versus observed Omega_DM/Omega_DE = 0.388 (1.06x agreement, zero free parameters). The S45 formula audit flagged this as a MODERATE violation: "Zubarev formalism cited by author name only, no specific publication or equation number." The agreement may be an artifact of a specific approximation within the Zubarev framework.

The formula works as follows. The GGE state has von Neumann entropy S_GGE (in nats). The maximum entropy state (Gibbs thermal) with the same total energy has entropy S_max. The "non-thermality" of the GGE is measured by alpha = S_GGE / (S_max - S_GGE). This non-thermality determines the DM/DE split because:
- DM = energy that gravitates as pressureless dust (proportional to non-thermal occupation fluctuations)
- DE = energy that gravitates as vacuum energy (proportional to the departure from thermal equilibrium)

**The key values from S45**:
- S_GGE = 3.456 nats (from s42_gge_energy.npz, 8-mode Richardson-Gaudin GGE)
- S_max = ln(256) = 5.545 nats (8 qubits, maximum entropy)
- S_max - S_GGE = 2.089 nats (departure from thermality)
- alpha = 3.456 / 2.089 = 1.654... wait, that gives alpha = 1.654 not 0.410.

**CORRECTION**: Re-derive from the actual S45 ALPHA-EFF-45 npz. The formula may be alpha = (S_max - S_GGE) / S_GGE = 0.604, or alpha = S_GGE / S_max = 0.623, or something else entirely. Load `tier0-computation/s45_alpha_eff.npz` and trace the EXACT formula used. This is precisely the provenance gap the formula audit flagged.

**Computation Steps**:

1. **Load S45 data.** From `tier0-computation/s45_alpha_eff.npz`: extract all stored values including alpha, S_GGE, S_max, method labels. From `tier0-computation/s42_gge_energy.npz`: GGE occupation numbers, temperatures, energies.

2. **Trace the exact formula.** Read the s45_alpha_eff.py script to identify the EXACT algebraic expression that produces alpha = 0.410. Write it down as a single self-contained equation with all variables defined.

3. **Zubarev derivation.** D.N. Zubarev, "Nonequilibrium Statistical Thermodynamics" (Consultants Bureau, 1974). The Zubarev non-equilibrium statistical operator is:

    rho_ne = exp(-sum_n F_n P_n) / Z

where F_n are thermodynamic forces conjugate to the constants of motion P_n. For the GGE, P_n are the Richardson-Gaudin integrals. The non-equilibrium thermodynamic potential is:

    Omega = -ln Z = -ln Tr exp(-sum_n F_n P_n)

The DM/DE partition arises from decomposing the total energy into a thermalized component (tracked by F_n -> common temperature) and a non-thermal component (the DIFFERENCE between the actual F_n and the common-temperature values). Derive alpha from this decomposition.

4. **Keldysh cross-check.** In the Schwinger-Keldysh formalism, the non-equilibrium Green's function is:

    G^< (omega) = -i * f(omega) * A(omega)

where f(omega) is the distribution function (GGE, NOT Fermi-Dirac) and A(omega) is the spectral function. The total energy is:

    E = integral (omega/2) [G^>(omega) + G^<(omega)] d(omega)/(2pi)

Decompose into thermal and non-thermal parts using the Fermi-Dirac reference: f_GGE = f_FD + delta_f. The non-thermal energy fraction is:

    E_non-thermal / E_total = integral omega * delta_f * A d(omega) / integral omega * f_GGE * A d(omega)

Compute this ratio numerically from the 8-mode GGE spectrum and compare to alpha.

5. **Agreement test.** If Zubarev and Keldysh give the same alpha within 50%, PASS. Report the discrepancy and identify the source of any difference (approximation in one formalism vs the other).

6. **Cross-checks.** (a) Thermal limit: S_GGE -> S_max, alpha -> 0 (all energy is vacuum energy, no DM). (b) Zero-temperature limit: S_GGE -> 0, alpha -> infinity (all energy is DM, no vacuum energy). (c) Consistency with S45 Method 7c: reproduce alpha = 0.410 to machine epsilon from the identified formula.

**Formula Audit**:
- (a) Formula: alpha = [exact expression to be determined from s45_alpha_eff.py]. [alpha] dimensionless.
- (b) Dimensional check: S_GGE and S_max in nats (dimensionless). alpha dimensionless. Verified.
- (c) Limiting case: S_GGE = S_max gives alpha -> 0 (thermal equilibrium, no DM). S_GGE = 0 gives alpha -> infinity (ground state, all DM).
- (d) Citation: MUST pin to Zubarev (1974) with specific equation number, or explicitly derive from first principles and cite as "original to this framework."

**Pre-registered gate ZUBAREV-DERIVATION-46**:
- PASS: Zubarev and Keldysh derivations agree within 50% on the value of alpha
- FAIL: Disagree by more than 50%

**Input files**:
- `tier0-computation/s45_alpha_eff.npz`
- `tier0-computation/s42_gge_energy.npz`
- `tier0-computation/canonical_constants.py`
- Zubarev, D.N. (1974), "Nonequilibrium Statistical Thermodynamics," Consultants Bureau.

**Output files**:
- Script: `tier0-computation/s46_zubarev_derivation.py`
- Data: `tier0-computation/s46_zubarev_derivation.npz`
- Plot: `tier0-computation/s46_zubarev_derivation.png` (alpha from multiple methods, bar chart)

**Working paper section**: W1-R4

**Critical notes**:
- The FIRST thing to do is read s45_alpha_eff.py and extract the EXACT formula. The formula audit identified a provenance gap; this computation fills it.
- If the formula cannot be traced to Zubarev, derive it from first principles and EXPLICITLY STATE that it is original to the framework. Do not hand-wave the derivation.
- The Keldysh formalism provides an independent derivation using non-equilibrium Green's functions. The two formalisms must agree if the formula is correct.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
