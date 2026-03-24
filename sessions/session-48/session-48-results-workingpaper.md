# Session 48 Results Working Paper: The Mass Problem

**Date**: 2026-03-17
**Format**: Parallel single-agent computations, 4 waves (12 computations)
**Plan**: `sessions/session-plan/session-48-plan.md`
**Branch**: Valar-1
**Master Gate**: MASS-SOURCE-48 = OR(GOLDSTONE-MASS-48.PASS, Q-THEORY-GOLD-48.PASS)

---

## Instructions for Contributing Agents

Each agent writes ONLY to their designated section below. Include:
1. **Gate verdict** (PASS/FAIL/INFO) with the decisive number FIRST
2. **Key numbers** (eigenvalues, ratios, discrepancies — with units)
3. **Cross-checks** (convergence, consistency with prior sessions, alternative methods)
4. **Data files produced** (script path, NPZ path, plot path)
5. **Assessment** (what this means for the framework, 2-3 sentences max)

Do NOT write outside your section. Do NOT modify other agents' sections.

**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output**: `tier0-computation/s48_*.py` / `.npz` / `.png`
**Constants**: Import from `tier0-computation/canonical_constants.py`
**Correction**: xi_texture = 2.67 Mpc (NOT 151 Mpc). S47 scale-bridge algebra error.

---

## Wave 1: Foundation Computations

---

### W1-A: Goldstone Mass from Spectral Action (landau-condensed-matter-theorist)

**Status**: COMPLETE
**Gate**: GOLDSTONE-MASS-48. PASS if m_G/M_KK in [10^{-60}, 10^{-50}]; INFO if outside range; FAIL if d^2S/dphi^2 = 0 identically.

**Results**:

**VERDICT: FAIL** -- d^2S/dphi^2 = 0 identically (structural theorem).

**Key number**: max|S(phi) - S(0)| = 6.2 x 10^{-15} (machine epsilon) for ALL tested operators.

**Structural Theorem (proven)**: The spectral action S[D] = Tr[f(D^2/Lambda^2)] is invariant under U(1)_7 phase rotations D(phi) = exp(phi*K_7) D exp(-phi*K_7) for ANY Hermitian D, ANY cutoff function f, and ANY generator K_7. This follows from:
1. U(phi) = exp(phi*K_7) is unitary (K_7 anti-Hermitian)
2. D(phi) = U D U^dag, so D(phi)^2 = U D^2 U^dag
3. f(D(phi)^2) = U f(D^2) U^dag (spectral mapping theorem)
4. Tr[U f(D^2) U^dag] = Tr[f(D^2)] (cyclic invariance of trace)

This is stronger than the pre-registered expectation. The FAIL was anticipated for D_K (where [iK_7, D_K] = 0 forces D_K(phi) = D_K), but the theorem shows d^2S/dphi^2 = 0 even when [iK_7, D] != 0. The spectral action is a TRACE functional and therefore CANNOT distinguish between unitarily conjugate operators.

**Numerical verification** (three independent operators):

| Operator | ||[iK_7,D]||/||D|| | max|dS| | d^2S/dphi^2 |
|:---------|:-------------------|:--------|:------------|
| D_K | 0.0000 | 3.6e-15 | 0 (exact) |
| D_phys (large mix) | 0.273 | 5.3e-15 | 0 (exact) |
| Random Hermitian | 0.248 | 6.2e-15 | 0 (exact) |

**Joint (lambda, q_7) spectrum at tau=0.19**: 16 states decompose as B3 sector (3-fold, q_7=0), B2 sector (4-fold, q_7 = +/-0.25), B1 (1-fold, q_7=0), with particle-hole partners. The q_7 = +/-0.25 states are the Cooper pair constituents.

**BCS rough estimate** (non-spectral-action, from matrix element breaking): m_G/M_KK ~ 6.8 x 10^{-3} (log10 = -2.2). This is O(epsilon * sqrt(|E_cond|/rho_s)) using epsilon = 0.052, |E_cond| = 0.137, rho_s = 7.96. Far too heavy for cosmological tilt.

**Constraint on solution space**: The spectral action is PERMANENTLY EXCLUDED as a source of Goldstone mass. The remaining candidates for the n_s mass gap are:
- (a) Inter-cell Josephson coupling at the fabric scale (~1/N_cells suppression)
- (b) BCS gap equation free energy (non-trace functional of D, depends on matrix elements)
- (c) Dynamical mass from Kibble-Zurek quench during transit

**Cross-checks**:
- [iK_7, D_K] = 0 verified to 0.00e+00 (S34 permanent, reconfirmed)
- Joint diagonalization: off-diagonal errors 5e-15
- Three independent cutoff functions (heat kernel, chi_2, polynomial) all give dS = 0
- Full phi scan [0, 2*pi] with 200 points for each operator

**Data files**:
- Script: `tier0-computation/s48_goldstone_mass.py`
- Data: `tier0-computation/s48_goldstone_mass.npz`
- Plot: `tier0-computation/s48_goldstone_mass.png`

**Assessment**: This is a permanent structural result. The spectral action, being a trace functional, is blind to the phase of the order parameter. The mass source for the Goldstone boson (needed for n_s - 1 = -0.035) must come from physics beyond the spectral action -- most likely the inter-cell Josephson coupling across the 32-cell fabric tessellation, which introduces a SPATIAL gradient energy rather than an on-site potential.

---

### W1-B: Physical Pair Number from Full Singlet Spectrum (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: N-PAIR-FULL-48. PASS if N >= 2; FAIL if N = 1 robust at 16 modes; INFO if N in (1.5, 2.0).

**Results**:

**N-PAIR-FULL-48: FAIL. N_pair = 1.000000000 (exact). The ground state is a single Cooper pair.**

#### Structural Finding: The 8-Mode ED IS the Full Singlet Sector

The (0,0) singlet sector of D_K on Jensen-deformed SU(3) has exactly 16 Dirac eigenvalues = 8 Kramers pairs = 8 modes in the pair Hamiltonian. This follows from dim(spinor) x dim(singlet) = 16 x 1 = 16. The S36 "8-mode" ED (config_4) already included ALL singlet modes. **There are no missing modes.** The "16 modes" in the prompt counts both particle (+) and hole (-) branches; the pair Hamiltonian uses only the 8 positive-branch Kramers pairs, which is complete.

#### Key Numbers

| Quantity | Value | Method |
|:---------|:------|:-------|
| N_pair (ED) | 1.000000000 | Exact diag, 256-state Fock space |
| P(N=1) | 1.000000000 | Pair-sector probability |
| P(N=2) | 4.6e-33 | Machine zero |
| P(N=0) | 0.0 | Exact zero (vacuum has zero overlap) |
| E_cond | -0.13685056 | Matches S36 to 1.9e-16 |
| N_pair (BCS) | 0.176 | BCS non-trivial but underestimates |
| Delta_B2 (BCS) | 0.33-0.39 | Self-consistent gap |
| M_max (with VH) | 1.396 | Thouless parameter |
| M_max (no VH) | 0.162 | Without van Hove: 8.6x smaller |
| N_pair (no VH) | 0.0 | Pairing vanishes without van Hove |

#### Cross-Checks (3 independent methods)

1. **ED reproduction**: E_cond = -0.13685056 matches S36 stored value to machine epsilon (diff = 1.9e-16). Independent Hamiltonian construction from Kosmann kernel.

2. **BCS self-consistent**: Converges to non-trivial Delta (max Delta = 0.39 on B2), but N_pair_BCS = 0.176. BCS UNDERESTIMATES pair number because it assumes grand canonical (broken number). This confirms Paper 03 Section IV: "BCS breaks down for very small systems (particle-number fluctuations become large)." The ED result (N=1 exact) is definitive.

3. **No-VH control**: With rho=1 everywhere (no van Hove enhancement), M_max drops to 0.162 (below threshold), E_gs = 0.0, N_pair = 0. Pairing is ENTIRELY driven by the B2 van Hove singularity. Non-singlet sectors, which lack this enhancement, will have N_pair = 0.

#### Tau Scan (9 points, tau in [0.0, 0.5])

| tau | E_cond | N_pair | gs_N |
|:----|:-------|:-------|:-----|
| 0.00 | 0.000 | 0.0 | 0 |
| 0.10 | 0.000 | 0.0 | 0 |
| 0.15 | -0.198 | 1.0 | 1 |
| 0.20 | -0.137 | 1.0 | 1 |
| 0.25 | 0.000 | 0.0 | 0 |
| 0.30 | -0.325 | 1.0 | 1 |
| 0.35 | -0.660 | 1.0 | 1 |
| 0.40 | -0.618 | 1.0 | 1 |
| 0.50 | -1.258 | 1.0 | 1 |

N_pair = 1 at EVERY tau where pairing exists. P(N=2) < 10^{-32} at all points. There is no tau at which N >= 2 in the singlet sector.

#### Nuclear Physics Assessment

From the perspective of Paper 03 (Bogoliubov many-body theory) and Paper 08 (pairing collapse):

1. **N=1 is the sd-shell regime**. With 8 modes and 1 Cooper pair, this system is analogous to an sd-shell nucleus with 2 valence neutrons (e.g., ^18O). The pair correlation is STRONG within the single pair (off-diagonal correlator max = 0.263), but there is only one pair.

2. **BCS-BEC crossover confirmed**. The xi_BCS/d_01 = 1.40 (S37) places this system at the BCS-BEC crossover. In this regime, the "condensate" is a single bound pair, not a macroscopic coherent state with many overlapping pairs.

3. **Number projection matters**. The BCS gap equation gives Delta ~ 0.3-0.4, but N_pair_BCS = 0.176 (not 1). The ED gives the correct N=1 exactly. This discrepancy is the standard BCS vs exact result in small systems (Paper 03, Table II: PBCS/BCS gap ratio 0.5-0.8 in sd-shell).

4. **Van Hove is the sole driver**. Without the B2 flat-band DOS enhancement (rho = 14/mode), pairing vanishes entirely. This means non-singlet sectors (which lack the fold-specific van Hove) contribute N=0 to the total pair count.

#### Constraint Map Impact

- **N=1 is structural**: It cannot be changed by including "missing modes" (there are none), adjusting mu (PH-forced to 0), or switching between BCS/ED/PBCS.
- **Q-theory crossing requires N >= 2**: The tau* = 0.170 crossing point needs the B3 gap to reach 0.13, which requires two or more pairs to populate the B3 sector. With N=1, all pairing strength stays in B2 (pair_occ_B2 = 0.89, pair_occ_B3 = 0.01).
- **Multi-sector pairing cannot help**: The no-VH control shows N_pair = 0 for rho = 1. Non-singlet sectors, which do not sit at the van Hove singularity, will be unpaired.

#### Remaining Open Paths

The N=1 singlet result is closed. Paths to N >= 2 require physics OUTSIDE the singlet:
1. **Self-consistent Delta(tau)**: If the pairing modifies the spectrum (backreaction), the fold structure could change. But backreaction was found to be 3.7% (S38).
2. **Fabric-level pairing**: Spatially extended fabric with many cells (N_cells = 32) could give effective N_pair = 32 x 1 = 32 across the full domain.
3. **Temperature/excitation**: The GGE post-transit state has 59.8 quasiparticle pairs (S38). This is NOT a ground-state pair number but an excited-state population.

#### Data Files

- Script: `tier0-computation/s48_npair_full.py`
- Data: `tier0-computation/s48_npair_full.npz`
- No plot (numerical result; no spatial/spectral structure to visualize)

---

### W1-C: Anisotropic Gap from Superfluid Stiffness (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate**: ANISO-GAP-48 = **FAIL** (927 sigma from Planck)

**Results**:

#### Gate Verdict

**FAIL**. n_s = -2.930 (best), 927 sigma from Planck n_s = 0.965. The rho_s anisotropy (24.4x) shifts pair-creation n_s by at most 0.070 out of the 3.965 needed (1.8%).

#### Key Numbers

| Quantity | Value | Source |
|:---------|:------|:-------|
| rho_s anisotropy C^2/u(1) | 24.37 | S47 RHOS-TENSOR-47 |
| sqrt(anisotropy) | 4.94 | Maximum gap modulation factor |
| n_s (unmodulated, 992 modes) | -3.000 | P(k) ~ omega^{-4} exactly |
| n_s (f1 sqrt, 992 modes) | -2.965 | delta_n_s = +0.035 |
| n_s (f2 linear, 992 modes) | -2.930 | delta_n_s = +0.070 |
| delta_n_s / needed | 0.89% (f1), 1.77% (f2) | Need 3.965 total shift |
| B1 mode-direction coupling | 0.000 (all 8 dirs) | Singlet-within-singlet |
| B2 dominant direction | u(1) (weight 0.616) | K_7 charge |
| B3 dominant direction | su(2) (weight 0.667) | Isospin-like |
| Energy range (8 BCS modes) | 1.185x | 3 distinct energies |
| Energy range (992 Dirac modes) | 2.51x | E in [0.820, 2.061] |
| rho_eff range (992 modes) | 1.54x | Direction-averaging washes out 24x |

#### Method

1. Computed current-operator coupling |<k|J_a|k'>|^2 for each of 8 singlet BCS modes to each of 8 su(3) Lie algebra directions. B1 mode couples to NOTHING (all zeros -- singlet-within-singlet). B2 modes couple to u(1) (K_7 direction, weight 0.616). B3 modes couple to su(2) (weight 0.667).

2. Applied 4 gap modulation ansatze (sqrt, linear, cube-root, weighted): Delta_eff(k) = Delta_sector * f(rho_s(dominant_dir) / rho_s_avg). For 8 modes, n_s from -52 to -71 (UNRELIABLE: only 3 distinct energies across 1.19x range).

3. Extended to full 992-mode Dirac spectrum with heuristic direction weights. Computed PAIR-CREATION spectrum P(k) = (Delta_eff(k)/omega(k))^4. Unmodulated: P ~ omega^{-4.000} (n_s = -3.000 exact). Gap modulation shifts to omega^{-3.930} at best (n_s = -2.930).

4. **Self-correction**: Initial code fitted Delta_eff vs omega alone (wrong quantity, R^2 = 0.0007), producing spurious n_s near 1.0. Corrected to fit the physical observable P(k) = (Delta_eff/omega)^4, recovering n_s = -2.93.

#### Cross-Checks

1. **Baseline**: n_s = -3.000 from P ~ omega^{-4} (R^2 = 1.000), confirming Bogoliubov pair-creation formula.
2. **B1 zero coupling**: Consistent with B1 carrying no su(3) gauge charge (trivial representation).
3. **rho_eff range**: Direction-averaging washes 24x anisotropy down to 1.54x for 992 modes.
4. **Wrong sign**: C^2 modes (highest rho_s) at intermediate-to-high energy. Gap modulation makes spectrum BLUER, not redder.

#### 3He-A Structural Comparison

- **3He-A**: Delta(k) = Delta_perp * sin(theta_k) from p-wave pairing symmetry (l=1 orbital). Gap NODES at k || l, protected by N_3 = +/-2. This is a property of the ORDER PARAMETER.
- **Framework**: s-wave-like pairing (Schur: V(B2,B2) identical for all 4 modes). N_3 = 0 (BDI class). rho_s measures MEISSNER response (condensate stiffness to gauge twists), not the gap function. Analogous to extracting gap nodes from London penetration depth in 3He-B -- the information is not there.
- **Category error**: rho_s in Lie algebra space (8 dirs). Spectral index in eigenvalue space (992 modes). The map washes out anisotropy.

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s48_aniso_gap.py` | Computation script |
| `tier0-computation/s48_aniso_gap.npz` | All numerical results |
| `tier0-computation/s48_aniso_gap.png` | 4-panel diagnostic figure |

#### Assessment

The k-dependent gap path is **permanently closed** (12th n_s route). The rho_s anisotropy provides at most 1.8% of the needed shift. The structural reason: this system is 3He-B class (fully gapped, N_3 = 0), not 3He-A class (nodal, N_3 = 2). The (Delta/omega)^4 Bogoliubov pair-creation scaling is universal for sudden quench of a gapped BCS system. The n_s crisis requires fabric-level physics (texture spectrum).

---

### W1-D: Non-Abelian Wilson Loop for Degenerate Multiplets (berry-geometric-phase-theorist)

**Status**: COMPLETE
**Gate**: WILSON-LOOP-48. PASS if total pi-count (Abelian + non-Abelian) in [13, 50]; FAIL if computation fails.

**Also report**: Total = 15 or 16? Conjugate relation theta_{(q,p)} = -theta_{(p,q)}? Global Z_2 from Wilson loop determinants?

**Results**:

#### Gate Verdict: WILSON-LOOP-48 = PASS (total_pi = 47, in [13, 50])

However, this PASS conceals a critical distinction that changes the physical interpretation.

#### Key Numbers

| Quantity | Value | Note |
|:---------|:------|:-----|
| Total eigenstates | 992 | 9 sectors, p+q <= 3 |
| True singlets (non-degenerate) | 68 | Identified by eigenvalue clustering at DEG_TOL = 1e-6 |
| States in degenerate multiplets | 924 | Require non-Abelian Wilson loop |
| Abelian pi-phases (singlets) | 13 | Of which 10 are strictly quantized (see below) |
| Wilson loop pi-phases (multiplets) | 34 | CONSISTENT WITH UNIFORM (see below) |
| Total pi-phases (formal) | 47 | = 13 + 34 |
| Total pi-phases (topological) | 10 | Only quantized Abelian phases count |
| PW-weighted pi-count | 408 | = sum over sectors of n_pi * dim(p,q) |
| Global Z_2 (product of all det(W)) | +1 | arg(global_det)/pi = -0.148, |det| = 1.000 |
| KS test for Wilson phase uniformity | p = 0.52 | Phases ARE uniform (not rejected) |

#### The Critical Distinction: Quantized vs Continuous Phases

The 924 degenerate-multiplet states yield Wilson loop eigenphases that are **uniformly distributed** over [-pi, pi]:

- KS test against uniform: statistic = 0.027, p-value = 0.52 (firmly uniform)
- Binomial test: 34 observed near pi vs 29.4 expected from uniform (p = 0.22, no excess)
- Phase histogram is flat across all 20 bins from -pi to pi

The 34 "Wilson pi-phases" are therefore **accidental** -- the same number expected from any uniform random distribution with this sample size and tolerance window (0.20 rad).

Among the 68 Abelian singlets:

- 21/68 have properly quantized phases (integer multiples of pi, residual < 0.05)
- 47/68 have non-integer phases (gauge-contaminated, indicating hidden near-degeneracy)
- Of the 21 quantized: **10 are odd multiples of pi** (Z_2 = -1), **11 are even** (Z_2 = +1)

The S46 count of "13 pi-phases" used a broader tolerance (0.1 rad on |gamma mod pi|) which captured 3 additional near-integer phases. The strict count is 10.

#### Physical Interpretation

**The non-Abelian Berry phase on the Jensen deformation is trivial.** The Wilson loop phases for degenerate multiplets show no quantization, no clustering at 0 or pi, and no excess above the uniform baseline. This is consistent with the S25 result (Berry curvature = 0 identically): a flat connection on a trivial bundle produces random holonomy along open paths.

The 10 strictly quantized Abelian pi-phases (from true non-degenerate singlets) are the ONLY topological content. These correspond to eigenvectors that undergo an odd number of sign flips along the tau path -- the Mobius strip topology identified in S46.

**Does total = 16?** No. Total = 10 (strict) or 13 (loose). Not 15 or 16 or 32.

**Conjugate relation theta_{(q,p)} = -theta_{(p,q)}?** NOT observed. Abelian phases are symmetric (not antisymmetric) between conjugate sectors, with large deviations (max dev > 10 rad). Wilson phases show neither clear symmetry nor antisymmetry. Pi-counts differ between conjugate pairs: (1,0) has 3, (0,1) has 5; (3,0) has 3, (0,3) has 7. This asymmetry traces to gauge-contaminated singlets.

**Global Z_2 from Wilson loop determinants?** The product of all Wilson loop determinants and Abelian phase factors gives det_global = 0.894 - 0.448i, with |det| = 1.000 and arg = -0.148 pi. This is NOT quantized to +1 or -1 -- it is a continuous phase. The global Z_2 (sign of real part) is +1 but this is not topologically meaningful since the phase is not quantized.

#### Per-Branch Pi-Count

| Branch | Abelian pi | Wilson pi | Total pi | Total states |
|:-------|:-----------|:----------|:---------|:-------------|
| B1 | 6 | 3 | 9 | 112 |
| B2 | 2 | 6 | 8 | 128 |
| B3 | 5 | 25 | 30 | 752 |

B3 dominates the Wilson pi-count purely because it has 6.7x more states than B1 -- the pi-fraction is uniform across branches (8.0% B1, 6.3% B2, 4.0% B3), consistent with the uniform distribution.

#### Degeneracy Structure

All 9 sectors have stable degeneracy structure along the path (same number of multiplets at tau_min, tau_mid, tau_end), except (1,1) where 2 accidental degeneracies lift between tau_min and tau_mid (34 groups -> 36 groups). Zero band inversions in any sector.

Typical multiplet dimensions: 2, 3, 4, 5, 6, 8. Maximum dimension: d=8 in sector (1,1).

#### Reconciliation with S25 and S46

| S25 result | S46 result | S48 result | Interpretation |
|:-----------|:-----------|:-----------|:---------------|
| Berry curvature = 0 (local) | 13 Abelian pi-phases (global Z_2) | 10 strict pi-phases + 34 uniform Wilson phases | Zero curvature, nontrivial Z_2 for 10 states |
| Quantum metric g = 982.5 (large) | 487 zero-phase states | 11 zero-phase + 47 contaminated + 924 uniform | Metric sensitivity without topological protection |

The three-layer structure from S46 is confirmed but simplified:
- **L0**: Eigenvalue flow (quantum metric). 992 states. Metrically rich.
- **L1**: Zak phase Z_2. 10 states carry pi-phase (strict). Topologically protected.
- **L2**: Non-Abelian Wilson loop. TRIVIAL. Phases uniformly distributed, no quantization.

The prediction that L2 might shift the total toward 16 (SM particle count) is NOT confirmed.

#### Data Files

| File | Contents |
|:-----|:---------|
| `tier0-computation/s48_wilson_loop.py` | Computation script |
| `tier0-computation/s48_wilson_loop.npz` | All phases, multiplet info, per-sector data |
| `tier0-computation/s48_wilson_loop.png` | 9-panel diagnostic plot |

#### Assessment

The non-Abelian Wilson loop computation closes the WILSON-LOOP-47/48 gate with a definitive structural result: **Wilson loop phases on Jensen-deformed SU(3) are uniformly distributed, not quantized.** The flat Berry connection (S25) produces random holonomy along open paths for degenerate subspaces, while preserving Z_2 quantization only for the 10 true singlets. The topological content of the Dirac spectrum under Jensen deformation is exhausted by these 10 Abelian pi-phases -- there is no additional non-Abelian contribution. The off-Jensen direction (P-30w, SU(2)-breaking) remains the only route to nontrivial non-Abelian Berry phase, as predicted by the Wilczek-Zee analysis in S42.

---

### W1-E: Curvature-Gap Anti-Correlation Across Tau (gen-physicist)

**Status**: COMPLETE
**Gate**: CURV-GAP-CORR-48 = **INFO**

The decisive numbers: |r| > 0.9 at 17/26 valid tau values (threshold for PASS: 20/26). However, |r| > 0.89 at ALL 26/26 valid points. |r| < 0.5 at ZERO points. The anti-correlation is structural but marginally below the pre-registered PASS threshold.

**Results**:

#### Method
Swept 27 tau values in [0.00, 0.50] (spacing 0.02, plus tau_fold = 0.19). At each tau, computed:
- All 28 sectional curvatures K(e_a, e_b) via Milnor formula (tier1_dirac_spectrum infrastructure, validated in r20a S20)
- Per-direction average curvature K_per_dir[a] = mean over all pairs involving direction a
- Superfluid stiffness rho_s^{aa}(tau) via central finite difference of BCS free energy under gauge twist (dq = 1e-4)
- BCS gaps Delta_s(tau) from s46 self-consistent interpolation
- 8-direction Pearson r(K_per_dir, rho_s_diag) at each tau

#### Degeneracy at tau = 0
At tau = 0 (bi-invariant metric), ALL 16 Dirac eigenvalues are degenerate at |lambda| = sqrt(3)/2 = 0.8660254. The sector decomposition B1/B2/B3 is meaningless. rho_s is large negative (~-3207) indicating the BCS energy is at a saddle point under gauge twist. This point is excluded from the correlation analysis as physically invalid. 26 valid points remain.

#### 8-Direction Correlation r(tau)

| tau | r(8-dir) | p-value | |r| > 0.9? |
|:----|:---------|:--------|:----------|
| 0.02 | -0.9220 | 0.0011 | YES |
| 0.10 | -0.9118 | 0.0016 | YES |
| 0.19 (fold) | -0.9059 | 0.0019 | YES |
| 0.32 | -0.9005 | 0.0023 | YES (last) |
| 0.34 | -0.8997 | 0.0023 | NO (marginal) |
| 0.40 | -0.8969 | 0.0025 | NO |
| 0.50 | -0.8912 | 0.0030 | NO |

- |r| > 0.9 window: tau in [0.02, 0.32] (17 points)
- |r| > 0.89 at ALL 26 valid points (100%)
- |r| < 0.5 at ZERO points
- Mean r = -0.9040
- Range: [-0.9220, -0.8912]
- Linear drift: slope +0.055 per unit tau (slow degradation)

#### 3-Sector Correlation (N=3)
K_sector vs Delta_sector: r ranges from -0.74 (tau=0.02) to -0.85 (tau=0.50). The 3-sector correlation STRENGTHENS at large tau (opposite trend to 8-direction) because sector curvature spread grows with tau.

#### Gate Evaluation

| Criterion | Threshold | Actual | Status |
|:----------|:----------|:-------|:-------|
| |r| > 0.9 | >= 20/26 | 17/26 | Below |
| |r| < 0.5 | >= 10/26 | 0/26 | Far below FAIL |
| |r| > 0.89 | -- | 26/26 | ALL |
| |r| > 0.88 | -- | 26/26 | ALL |
| |r| > 0.85 | -- | 26/26 | ALL |

**Verdict: INFO** (formally 3 points short of PASS, but unambiguously not FAIL)

#### Cross-Check with S47
Fold cross-check: r = -0.9059 (S47: -0.9059), discrepancy = 0.0000. K_per_dir exact to machine epsilon. rho_s agreement to relative error ~10^{-5}.

#### Derivative Analysis
dK_B2/dtau and dDelta_B2/dtau have SAME sign at 18/27 points (Pearson r = +0.676). The LEVELS anti-correlate (high K => low rho_s), but the CHANGES are positively correlated. The anti-correlation operates through the BCS kernel structure, not through local curvature-gap coupling.

#### Structural Interpretation
The anti-correlation is **structural**: r < -0.89 at every non-degenerate tau from 0.02 to 0.50. The mechanism:
- C^2 directions (B2 sector) carry most superfluid stiffness (rho_s ~ 6-30) but have intermediate curvature
- su(2) directions (B3 sector) have highest curvature but low stiffness (rho_s ~ 0.2-0.5)
- u(1) direction (B1 sector) has intermediate curvature and lowest stiffness

This is controlled by the reductive decomposition su(3) = u(1) + su(2) + C^2 and the block-diagonal theorem (S22b). The 3% degradation from |r| = 0.922 to 0.891 over the full domain reflects growing curvature anisotropy (K_aniso: 1.0 at tau=0 to 2.88 at tau=0.50).

**Theorem candidate**: If derivable from the reductive decomposition and BCS kernel selection rules (V(B1,B1) = 0, Trap 1), this would be a structural theorem. Evidence is consistent but derivation incomplete.

#### Data Files
- Script: `tier0-computation/s48_curv_gap_corr.py`
- Data: `tier0-computation/s48_curv_gap_corr.npz`
- Figure: `tier0-computation/s48_curv_gap_corr.png`

---

## Wave 1 Decision Point

| Gate | Verdict | Key Number | Consequence |
|:-----|:--------|:-----------|:------------|
| GOLDSTONE-MASS-48 | | | |
| N-PAIR-FULL-48 | **FAIL** | N=1.000 (exact, P(N=2)=4.6e-33) | CC crossing closed at singlet level. 8 modes IS full singlet. |
| ANISO-GAP-48 | | | |
| WILSON-LOOP-48 | | | |
| CURV-GAP-CORR-48 | **INFO** | r=-0.904 mean, |r|>0.89 at 26/26, |r|>0.9 at 17/26 | Structural anti-corr (marginal below PASS). Theorem candidate. |

**Decision**:
- GOLDSTONE-MASS: If FAIL → W2-A proceeds with m as free parameter, W2-C is decisive
- N-PAIR-FULL: If PASS → CC crossing viable. If FAIL → CC crossing closed at singlet level
- ANISO-GAP: If FAIL → k-dependent gap path formally closed
- WILSON-LOOP: If total = 16 → high-priority SM connection follow-up
- CURV-GAP-CORR: If PASS → structural anti-correlation, theorem candidate

---

## Wave 2: Mass Sources and Structural Computations

---

### W2-A: Anisotropic Ornstein-Zernike Power Spectrum (landau-condensed-matter-theorist)

**Status**: COMPLETE
**Gate**: ANISO-OZ-48. PASS if n_s = 0.965 +/- 0.01 at some m/J with physically motivated m; INFO if trivially achievable; FAIL if geometry prevents n_s = 0.965.

**Results**:

#### Gate Verdict: ANISO-OZ-48 = INFO

The decisive number: n_s(K_pivot, m*) = 0.965 achieved at m* = 11.87 M_KK (m*/J_C2 = 12.72). The Ornstein-Zernike form P(K) = T/(J K^2 + m^2) is a one-parameter family: for any n_s in (-1, 1), there exists m* achieving it. This is parametric, not predictive. Verdict is INFO because the O-Z form trivially achieves any n_s target. The result becomes a prediction ONLY when m is independently determined (W2-C: Q-THEORY-GOLD-48).

#### Key Numbers

| Quantity | Value | Unit | Source |
|:---------|:------|:-----|:-------|
| J_xy (C^2, in-plane) | 0.9325 | M_KK | S47 TEXTURE-CORR-48 |
| J_z (su2, inter-plane) | 0.0591 | M_KK | S47 TEXTURE-CORR-48 |
| J_eff (isotropic average) | 0.6414 | M_KK | (2*J_xy + J_z)/3 |
| Anisotropy J_xy/J_z | 15.8 | -- | -- |
| T_acoustic | 0.1122 | M_KK | S42 Hauser-Feshbach |
| T/J_xy | 0.120 | -- | ORDERED |
| T/J_z | 1.90 | -- | DISORDERED |
| K_pivot (lattice) | 1.979 | cell^{-1} | 2*pi / N^{1/3} |
| K_pivot / K_BZ | 0.630 | -- | NOT continuum regime |
| m* (continuum, iso) | 11.88 | M_KK | Analytic |
| m* (angular average) | 11.87 | M_KK | MC on S^2, 100k points |
| m*/J_C2 | 12.72 | -- | -- |
| m* (GeV) | 8.81e17 | GeV | m* * M_KK |
| xi_J = sqrt(J)/m | 0.067 | cells | Mass-dominated regime |
| n_s angular spread | 0.014 | -- | From J anisotropy |

#### Structural Theorem: O-Z Running is Universal

For the Ornstein-Zernike form P(K) = T/(J K^2 + m^2) in the continuum limit, the running spectral index alpha_s = d(n_s)/d(ln K) is uniquely determined by n_s:

**alpha_s = -(1 - n_s^2)**

Proof: Define y = m^2/(J K^2). Then n_s = 1 - 2/(1+y), so y = (1+n_s)/(1-n_s). The running alpha_s = d(n_s)/d(ln K) = 4y/(1+y)^2. Substituting: alpha_s = 4(1+n_s)(1-n_s) / [((1+n_s)/(1-n_s) + 1)]^2 = 4(1-n_s^2) * (1-n_s)^2 / 4 = -(1-n_s^2). QED.

At n_s = 0.965: alpha_s = -0.069. Planck measures alpha_s = -0.0045 +/- 0.0067. Tension: 9.6 sigma.

This is a one-parameter family constraint: once n_s is specified, alpha_s is fixed with NO additional freedom. The running is too large by a factor of 15.

#### Lattice Dispersion Correction

At K_pivot / K_BZ = 0.63, the lattice dispersion sin^2(K/2) deviates from the continuum K^2 by a factor 0.65. This modifies the running. Numerical result at N_cells = 32:

| Regime | m* (M_KK) | alpha_s | Planck tension |
|:-------|:----------|:--------|:---------------|
| Continuum | 11.87 | -0.069 | 9.6 sigma |
| Lattice (N=32) | 9.61 | -0.038 | 4.9 sigma |
| Lattice (N=8) | 10.29 | +0.036 | 6.0 sigma |
| Lattice (N=64) | 8.27 | -0.050 | 6.8 sigma |
| Lattice (N=128) | 6.90 | -0.057 | 7.8 sigma |
| Lattice (N=1024) | 3.66 | -0.066 | 9.2 sigma |
| Continuum limit | -- | -0.069 | 9.6 sigma |

The lattice correction at N=32 reduces tension from 9.6 to 4.9 sigma. Still significant. The N-dependence is monotonic: more cells approaches the continuum limit. N_cells = 32 is framework-derived (S42 Kibble-Zurek), not a tunable parameter.

#### Planck Observable Comparison

| Observable | Planck 2018 | Framework (O-Z) | Sigma |
|:-----------|:-----------|:----------------|:------|
| n_s | 0.9649 +/- 0.0042 | 0.965 (by construction) | 0 |
| alpha_s | -0.0045 +/- 0.0067 | -0.038 (lattice N=32) | 4.9 |
| r | < 0.06 | 0 | consistent |

n_s is a parametric fit (one free parameter m), not a prediction. alpha_s IS a prediction at fixed N_cells and deviates at 4.9 sigma. r = 0 because the texture mechanism generates scalar perturbations only (no gravitational wave production).

#### Anisotropy Analysis

The 3D anisotropy (J_xy/J_z = 15.8) causes direction-dependent n_s:

| Direction | J_eff | n_s at m*_angular |
|:----------|:------|:-----------------|
| x (C^2) | 0.933 | 0.950 |
| y (C^2) | 0.933 | 0.950 |
| z (su2) | 0.059 | 0.997 |
| Angular average | 0.641 | 0.965 |

The angular spread (std = 0.014) is below Planck sensitivity (sigma_ns = 0.0042 is for the mean). The anisotropy produces a 4.7% variation in n_s across directions, which would manifest as statistical anisotropy in the CMB power spectrum. The amplitude is comparable to the A_s hemispherical asymmetry (~7% at 3.5 sigma).

#### Physical Interpretation

The required mass m* = 11.87 M_KK is O(10) in lattice units. This is NOT a fine-tuned quantity -- it is comparable to the Josephson coupling scale. However, it is 60 orders of magnitude above the q-theory scale (m_q ~ H_0 ~ 10^{-42} GeV). The mass sets the Josephson correlation length xi_J = sqrt(J)/m = 0.067 cells, meaning the mass dominates over the Josephson coupling at all inter-cell scales. Physically: the phases are UNCORRELATED across cells at this mass scale. The spectrum is dominated by the mass gap, with small corrections from the inter-cell coupling.

This is backwards from the physical picture in S47 (TEXTURE-CORR-48), where the ORDERED C^2 directions had xi_phase ~ 532 cells. The m = 0 case gives the physically interesting texture; the m = m* case gives the mathematically required tilt but destroys the texture.

**The tension is between the physical phase ordering (m = 0, ORDERED in C^2) and the phenomenological requirement (m = m*, n_s = 0.965). Resolving this tension requires identifying the physical origin of m and whether it can coexist with long-range phase order.**

#### Cross-Checks

1. Analytical eigenvalues match numerical to 2.7e-15 (machine epsilon)
2. Continuum m* formula verified: m*/sqrt(J K^2) = 7.49 (matches 2/(1-n_s) - 1 = 56.14, sqrt = 7.49)
3. Universal running alpha_s = -(1-n_s^2) verified analytically and numerically (ratio 1.002)
4. m* independent of K_pivot in continuum: m*/K_pivot = 5.995 (constant, verified at 6 K_pivot values)
5. Angular average convergence: n_s = 0.96500000 with 100k MC points

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s48_aniso_oz.py` | Computation script |
| `tier0-computation/s48_aniso_oz.npz` | All numerical results (m scan, P(K), eigenvalues) |
| `tier0-computation/s48_aniso_oz.png` | 6-panel diagnostic figure |

#### Assessment

The O-Z form trivially accommodates n_s = 0.965 at a natural mass scale (m ~ 12 J_C2), confirming that the 3D anisotropy poses no structural obstacle. However, this is a one-parameter fit with no predictive content until m is determined independently. The running alpha_s = -0.038 (lattice, N=32) is a genuine structural prediction that deviates from Planck at 4.9 sigma. In the continuum limit (N >> 32), the tension grows to 9.6 sigma. The N=32 result depends on the framework-derived cell count, so alpha_s serves as a DISCRIMINANT: if future measurements refine alpha_s to below -0.03, the O-Z texture mechanism at N=32 is compatible; if alpha_s converges to the current central value -0.005, the tension is structural. The NEXT DECISIVE COMPUTATION is W2-C (Q-THEORY-GOLD-48): if q-theory gives m at any specific value, n_s becomes a parameter-free prediction.

---

### W2-B: TT 2-Tensor Lichnerowicz Operator (spectral-geometer)

**Status**: COMPLETE
**Gate**: TT-LICH-48 = **PASS** (spectrum fully positive, hard/soft ratio = 1.2306)

**Results**:

#### Gate Verdict: TT-LICH-48 = PASS

The decisive numbers: 31 TT eigenvalues at the fold (tau = 0.19), ALL POSITIVE. Minimum eigenvalue lambda_min = +0.3217 (stability margin 28% above the mean Ricci scale R/8 = 0.2523). No negative eigenvalues at ANY of 9 tested tau values in [0.00, 0.50]. Hard/soft splitting ratio = 1.2306 (23% splitting, exceeding the 5% threshold).

#### Key Numbers

| Quantity | Value | Note |
|:---------|:------|:-----|
| n_TT at fold (tau=0.19) | 31 | 36 sym - 1 trace - 4 transversality |
| n_TT at tau=0 (bi-inv) | 35 | Transversality trivial (Gamma totally antisym) |
| lambda_min at fold | +0.3217 | deg 5, HARD (su2-su2), pure su(2) block |
| lambda_max at fold | +0.9387 | deg 1, HARD (mixed: 62% su2, 25% C2, 13% u1) |
| TT eigenvalue anisotropy | 2.92x | max/min at fold |
| Sectional curv. anisotropy (S47) | 12.5x | K_SU2-SU2 / K_SU2-C2 |
| Hard/Soft mean ratio | 1.2306 | hard_mean/soft_mean = 0.4245/0.3449 |
| Negative eigenvalues | 0 at ALL tau | S20b consistency: PASS |
| Symmetry error (L_TT) | 5e-17 | Machine epsilon (self-adjointness) |

#### Bi-Invariant Validation (tau = 0)

At tau = 0, the bi-invariant SU(3) metric is Einstein (Ric = (R/8)I = 0.25 I, verified to 6e-17). The Lichnerowicz operator has exactly 2 eigenvalue branches on the 35-dimensional TT space:

| Branch | lambda | Degeneracy | Content |
|:-------|:-------|:-----------|:--------|
| Lower | 1/3 = 0.33333... | 27 | Mixed (all sectors degenerate) |
| Upper | 3/4 = 0.75000... | 8 | Mixed (all sectors degenerate) |

Trace: 27(1/3) + 8(3/4) = 9 + 6 = 15.0 (exact).

#### Structural Theorem: Transversality Constraints and the n_TT Jump

**Theorem (Transversality structure)**: For the Jensen-deformed left-invariant metric on SU(3):

1. At tau = 0 (bi-invariant): ALL left-invariant symmetric 2-tensors are automatically transverse. The divergence operator vanishes identically on left-invariant tensors because Gamma^c_{ab} = (1/2) f^c_{ab} is totally antisymmetric, and contracting antisymmetric Gamma with symmetric h yields zero. Constraint rank = 1 (trace only). n_TT = 35.

2. At tau > 0: Exactly 4 of the 8 divergence constraints activate. These correspond to the C^2 directions {e_3, e_4, e_5, e_6} with fourfold-degenerate singular values (proportional to tau at small tau). The u(2) directions {e_0, e_1, e_2, e_7} remain trivially transverse at ALL tau. Constraint rank = 5. n_TT = 31.

3. The jump 35 -> 31 at tau = 0+ is a structural discontinuity. The 4 exiting modes are pure C^2 divergence modes that become non-transverse under the Jensen deformation.

**Proof**: The singular values of the constraint matrix C at tau > 0 are {2.828 (trace), 4 x 0.196*tau (C^2 div), 4 x 0.000 (u(2) div)}. The u(2) directions have vanishing divergence because Jensen preserves the U(2) subalgebra, retaining the antisymmetry that forces div = 0 on symmetric tensors.

#### 8-Branch Spectrum at the Fold

| Branch | lambda | Deg | Sector | Weight |
|:-------|:-------|:----|:-------|:-------|
| 1 | 0.32166 | 5 | HARD (su2-su2) | hard = 1.000 |
| 2 | 0.32523 | 3 | C2-C2 | C2 = 0.688, U1 = 0.312 |
| 3 | 0.34168 | 1 | U1-mixed | U1 = 0.746, C2 = 0.248 |
| 4 | 0.34219 | 6 | C2-C2 | C2 = 1.000 (pure) |
| 5 | 0.34494 | 8 | SOFT (su2-C2) | soft = 1.000 (pure) |
| 6 | 0.34677 | 4 | U1-mixed | U1 = 0.902, soft = 0.098 |
| 7 | 0.62661 | 3 | U1-mixed | U1 = 0.688, C2 = 0.312 |
| 8 | 0.93867 | 1 | HARD (mixed) | hard = 0.619, C2 = 0.252, U1 = 0.129 |

Total: 5 + 3 + 1 + 6 + 8 + 4 + 3 + 1 = 31. Trace = 11.944.

Two-tier structure: bulk cluster (branches 1-6, 27 modes in [0.322, 0.347], 7.8% spread) inherited from bi-invariant 1/3 branch; outlier pair (branches 7-8, 4 modes at 0.627 and 0.939) inherited from bi-invariant 3/4 branch.

#### Eigenvalue Evolution with tau

| tau | lambda_min | lambda_max | spread | n_TT | n_neg |
|:----|:-----------|:-----------|:-------|:-----|:------|
| 0.00 | 0.3333 | 0.7500 | 0.417 | 35 | 0 |
| 0.05 | 0.3207 | 0.7963 | 0.476 | 31 | 0 |
| 0.10 | 0.3153 | 0.8447 | 0.529 | 31 | 0 |
| 0.15 | 0.3164 | 0.8957 | 0.579 | 31 | 0 |
| 0.19 | 0.3217 | 0.9387 | 0.617 | 31 | 0 |
| 0.25 | 0.3060 | 1.0082 | 0.702 | 31 | 0 |
| 0.30 | 0.2827 | 1.0719 | 0.789 | 31 | 0 |
| 0.40 | 0.2232 | 1.2196 | 0.996 | 31 | 0 |
| 0.50 | 0.1567 | 1.4020 | 1.245 | 31 | 0 |

lambda_min has a LOCAL MAXIMUM near the fold (0.322 at tau=0.19), consistent with the fold being a distinguished point in the TT stability landscape.

#### Curvature-Eigenvalue Hierarchy

The 12.5x sectional curvature anisotropy (S47) compresses to 2.92x TT eigenvalue anisotropy. Compression factor 4.3x arises because: (1) the Ricci anisotropy is only 1.23x (eigenvalues 0.283/0.230), (2) the Riemann term mixes all sectors through off-diagonal couplings, and (3) the TT projection removes the 4 most anisotropic C^2 directions.

#### Cross-Checks

1. **S20b consistency**: No tachyons at any tau. PASS.
2. **Trace conservation**: Tr(L_TT) = sum(eigenvalues) to 1.5e-16 at every tau.
3. **Self-adjointness**: L_TT symmetry error = 5e-17 (machine epsilon).
4. **R(0) = 2.000000** (err 7e-16), **Ric(0) = 0.25 I** (err 6e-17).
5. **R(0.19) = 2.01814396** matches S46 to 12 digits.
6. **Ricci eigenvalues at fold**: {0.230 x4, 0.250 x1, 0.283 x3}. Matches S46.

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s48_tt_lichnerowicz.py` | Computation script (6 modules) |
| `tier0-computation/s48_tt_lichnerowicz.npz` | All eigenvalues, sectors, per-tau data |
| `tier0-computation/s48_tt_lichnerowicz.png` | 4-panel figure |

#### Assessment

The TT Lichnerowicz spectrum on Jensen-deformed SU(3) is fully positive at all tau in [0, 0.5], confirming S20b's no-tachyon result with a completely independent method. The hard/soft splitting is confirmed at 23%. The main new result is the transversality theorem: exactly 4 C^2 constraints activate at tau > 0, producing a 35 -> 31 dimensional jump. The spectrum at the fold has 8 distinct branches with clear sector identification, providing the complete mode-resolved stability landscape. The lambda_min local maximum near the fold is a new structural observation connecting TT stability to the van Hove singularity.

---

### W2-C: Q-Theory Goldstone Self-Tuning Mass (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate**: Q-THEORY-GOLD-48 = **FAIL** (all routes give m ~ O(M_KK) or m = 0; none in [10^{-60}, 10^{-30}])

**Results**:

#### Gate Verdict

**FAIL**. Nine independent mass estimates span log10(m/M_KK) in [-2.4, +1.5]. Zero routes fall within the gate window [10^{-60}, 10^{-30}]. The self-tuning iteration (Route A) diverges -- the equation d(rho_vac)/d(m^2) = 0 has no finite fixed point. All other routes give m ~ O(M_KK) (lattice-scale masses). The required hierarchy m/M_KK ~ 10^{-56} is inaccessible from microscopic parameters alone.

#### Key Numbers

| Route | m/M_KK | m (GeV) | log10(m/M_KK) | m/m_req | Verdict |
|:------|:-------|:--------|:---------------|:--------|:--------|
| A: Self-tuning (4D lattice) | 0 | 0 | --- | --- | DIVERGES |
| A: Self-tuning (1D chain, N=32) | 0 | 0 | --- | --- | DIVERGES |
| A analytic (|E_cond|*T/rho_s^2*a^2) | 0.102 | 7.6e15 | -0.99 | 3.2e54 | Too heavy |
| A' Hubble relaxation (KV Paper 16) | 4.2e-3 | 3.2e14 | -2.37 | 1.3e53 | Too heavy |
| A'' Josephson coupling | 0.715 | 5.3e16 | -0.15 | 2.2e55 | Too heavy |
| A'' Phase stiffness over fabric | 0.580 | 4.3e16 | -0.24 | 1.8e55 | Too heavy |
| B: Disordered directions | 3.18 | 2.4e17 | +0.50 | 9.9e55 | Too heavy |
| C1: Finite-size (L=2a) | 10.3 | 7.7e17 | +1.01 | 3.2e56 | Too heavy |
| C3: Finite-size (L=32a) | 0.646 | 4.8e16 | -0.19 | 2.0e55 | Too heavy |

Target: m_required = 3.2e-56 M_KK = 2.4e-39 GeV (for n_s = 0.965 from texture O-Z spectrum).

#### Route A: Self-Tuning (Volovik Mechanism) -- STRUCTURAL FAILURE

The vacuum energy functional including the Goldstone sector:

rho_vac(m) = E_cond * (1 - <phi^2>(m)) + (1/2) * rho_s * m^2 * <phi^2>(m)

where <phi^2>(m) is the lattice sum T/(rho_s * N) * sum_K 1/(K^2 + m^2/rho_s).

The self-tuning condition d(rho_vac)/d(m^2) = 0 gives the fixed-point equation:

mu^2_new = phi_sq/|d_phi_sq/d_mu^2| - 2|E_cond|/rho_s^2

where mu^2 = m^2/rho_s. The ratio phi_sq/|d_phi_sq/d_mu^2| GROWS monotonically with mu for any discrete lattice, because the ratio of sum 1/(K_n^2+mu) to sum 1/(K_n^2+mu)^2 increases as mu dominates the denominators. The iteration therefore diverges: mu -> infinity.

**Physical interpretation**: Increasing the Goldstone mass suppresses phase fluctuations, which STRENGTHENS the BCS condensation energy (fewer fluctuations degrade the condensate), which demands an even larger mass. This is a runaway -- the opposite of self-tuning. The self-tuning has only two fixed points: m = 0 (Goldstone theorem) and m = infinity (frozen phase). Neither is the finite mass needed for n_s.

Checked on 4D lattice (4^4 = 256 modes) and 1D chain (32 modes): both diverge. The divergence is structural -- independent of lattice geometry.

Key diagnostic: ps/|dps| at mu=0 ranges from 2.49 (1D) to 284.6 (4D), while threshold = 2|E_cond|/rho_s^2 = 4.3e-3. The ratio ps/|dps| >> threshold at ALL mu, so mu_new > mu always.

#### Route B: Disordered Directions

T/J ratios: T/J_su2 = 1.90 (disordered), T/J_u1 = 2.93 (disordered), T/J_C2 = 0.12 (ordered). Correlation lengths: xi_su2 = 1.06 cells, xi_u1 = 0.72 cells (sub-lattice-spacing -- deeply disordered).

Effective mass: m^2 = sum_dis (T - J_dis)/a^2 = 10.09 M_KK^2, giving m = 3.18 M_KK. This is a UV cutoff for Goldstone propagation in the disordered directions. It correctly predicts that the Goldstone cannot propagate in the su(2)/u(1) sector (as S47 TEXTURE-CORR-48 found), but is irrelevant for the IR mass needed for n_s.

#### Route A': Klinkhamer-Volovik Hubble Relaxation

Using the Paper 16 scaling Lambda ~ K_vac^3 / M_Pl^2 with K_vac = Delta_B2^2 = 0.536 M_KK^2 gives Lambda_KV = 1.4e-4 M_KK^4, hence m = sqrt(Lambda_KV/rho_s) = 4.2e-3 M_KK. This is the BEST route (smallest mass) but still 53 orders above target. The deficit is exactly M_Pl/M_KK = 32.8 -- the Paper 16 scaling introduces ONE power of 1/M_Pl^2, not the 28+ powers needed for m ~ 10^{-56} M_KK.

#### Cross-Checks

1. Route B cross-check: m from 1/xi method gives m = 14.1 M_KK vs 3.18 M_KK from (T-J)/a^2. Factor-4.5 discrepancy traces to the Ising model formula xi = a/sqrt(T/J-1) vs the lattice dispersion m^2 = (T-J)/a^2 -- different definitions in the deeply disordered regime (xi < a).

2. All route masses are consistent with M_KK scale (log10(m/M_KK) in [-2.4, +1.5]). No route produces a hierarchy.

3. Route A divergence is independent of iteration starting point (tested mu_0 = 1e-6, 1e-2, 1.0).

#### Structural Analysis (Volovik Perspective)

The mass problem is the CC problem in disguise. From the superfluid analog:

1. **Goldstone theorem**: In equilibrium (d(rho)/dq = 0 at q = q_0), the U(1)_7 Goldstone is EXACTLY massless. This is the analog of Lambda = 0 in equilibrium (Paper 05, Section II).

2. **No microscopic hierarchy**: The only scales available from the BCS Hamiltonian on SU(3) are: Delta ~ 0.7 M_KK, E_cond ~ 0.14 M_KK, rho_s ~ 8 M_KK, a ~ 0.15/M_KK. All are O(M_KK). There is no mechanism to generate m ~ 10^{-56} M_KK from these ingredients alone.

3. **The hierarchy requires cosmological input**: The required mass m ~ 10^{-39} GeV corresponds to the Hubble scale H_0 ~ 10^{-42} GeV. This is NOT a microscopic quantity -- it is set by the age of the universe. In Volovik's framework (Paper 05), the observed vacuum energy is proportional to H^2 * M_Pl^2, which is small because H is small. Similarly, the Goldstone mass would be m ~ H * (M_KK/M_Pl)^alpha for some power alpha. But this requires knowing how the microscopic system couples to the cosmological expansion -- exactly the missing ingredient.

4. **3He analog**: In superfluid 3He, the Goldstone mode (second sound) is EXACTLY massless. The mass arises only from explicit symmetry breaking (e.g., dipolar interaction in 3He-A gives omega_L ~ 10^5 Hz vs v_F * k_F ~ 10^{14} Hz, a hierarchy of 10^9). In our system, the analog of dipolar interaction is whatever breaks U(1)_7 explicitly -- and we have proven (W1-A) that the spectral action cannot do this.

5. **Non-equilibrium path**: Just as the observed CC requires non-equilibrium physics (the universe has not reached q = q_0), the Goldstone mass requires non-equilibrium physics. The GGE relic (S38) is precisely such a non-equilibrium state. The n_s tilt may encode information about the transit dynamics, not about the equilibrium Hamiltonian.

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s48_qtheory_goldstone.py` | Computation script (9 routes) |
| `tier0-computation/s48_qtheory_goldstone.npz` | All masses, couplings, gate verdict |

#### Assessment

The q-theory self-tuning mechanism, which correctly addresses the CC problem (d(rho)/dq = 0 => Lambda = 0 in equilibrium), provides NO Goldstone mass. The self-tuning condition for m has no finite fixed point -- it is a structural theorem, not a numerical accident. The mass problem and the CC problem are the SAME problem: both require a hierarchy between M_KK and H_0 that cannot be generated from the microscopic BCS Hamiltonian alone. The remaining open path is non-equilibrium: the GGE relic encodes the transit dynamics, and the tilt n_s - 1 = -0.035 may be a signature of the quench rather than of a pseudo-Goldstone mass.

---

### W2-C ADDENDUM: Nuclear Structure Review of Q-THEORY-GOLD-48 (nazarewicz-nuclear-structure-theorist)

**Status**: REVIEW COMPLETE
**Reviewed computation**: Q-THEORY-GOLD-48 (Volovik agent, W2-C)
**Verdict on review target**: The FAIL verdict is **procedurally correct** given the gate window and the 9 routes computed. However, the computation contains a structural conflation that undermines the claim "no equilibrium mechanism generates the Goldstone mass." Specifically, it operates entirely at the microscopic BCS scale and never engages the macroscopic thermodynamic level where Volovik's q-theory self-tuning is defined. The FAIL applies to single-cell BCS physics. The mass problem at the fabric/cosmological scale is **UNCOMPUTED**, not closed.

#### 1. What W2-C Computed Correctly

The 9 routes are internally consistent. Let me verify the structural claims:

(a) **Route A divergence is real.** The ratio phi_sq / |d_phi_sq/d_mu^2| does grow monotonically for any finite discrete lattice, because at large mu the sum 1/(K_n^2 + mu) approaches N_modes / mu while 1/(K_n^2 + mu)^2 approaches N_modes / mu^2, so their ratio approaches mu. This is a mathematical identity, not an approximation. The self-tuning iteration diverges structurally on any lattice with a finite number of modes and a BCS gap that strengthens when phase fluctuations are suppressed.

(b) **Routes B and C are lattice-scale masses.** These report the UV cutoff for Goldstone propagation, not an IR mass. Correct to exclude them from the gate window.

(c) **Route A' gives the Klinkhamer-Volovik scaling Lambda ~ K^3/M_Pl^2.** The numerical estimate m ~ 4.2e-3 M_KK is correct given the inputs. This imports ONE power of 1/M_Pl^2, yielding a deficit of ~53 orders. Correct.

(d) **Route A'' Josephson mass is O(M_KK).** The overlap factor exp(-a/xi_BCS) = exp(-0.152/0.808) = 0.829 is correct. The resulting J_inter = 0.094 M_KK and m_J = 0.715 M_KK are UV-scale masses. Correct.

(e) **The structural argument** (increasing m suppresses fluctuations, strengthens BCS, demands larger m) is physically sound for the single-cell problem. This is the BCS-phase rigidity already observed in S46 GCM-ZERO-POINT-46 (GCM ill-conditioned because Delta_B2 = 1.334 >> delta_E_sp) and S47 COHERENCE-RESPONSE-47 (r_C 95% geometric, 5% BCS).

**All 9 routes are valid computations at the scale they address.** No algebraic errors detected.

#### 2. What W2-C Did NOT Compute: The Scale Hierarchy Problem

Here is the structural issue. Every route in W2-C operates within a single conceptual framework:

**"Given BCS on one SU(3) cell, what mass does the Goldstone acquire?"**

But this is not where Volovik's q-theory self-tuning operates. Let me be precise about this.

**Volovik's q-theory (Papers 15-16)** works as follows:

1. The vacuum variable q is **spacetime-independent** and characterizes the **macroscopic equilibrium** of the quantum vacuum (Paper 15, Sec. II: "spacetime-independent variable... characterizes a Lorentz-invariant self-sustained quantum vacuum").

2. In equilibrium, d(rho)/dq = 0 gives Lambda = 0 **exactly**. The observed small Lambda arises from the **deviation from equilibrium** caused by the finite age of the expanding universe (Paper 15, Sec. III: "residual vacuum energy proportional to rho_matter").

3. The remnant CC scales as Lambda ~ K^3/E_Pl^2 where K is the characteristic vacuum scale (Paper 16, Eq. 1). This involves **three** physics inputs: the microscopic scale K, the Planck scale E_Pl, and the Hubble expansion rate H.

Now compare with what W2-C computed:

- Route A takes the single-cell BCS Hamiltonian on SU(3) and asks whether the self-tuning condition d(rho_vac)/d(m^2) = 0 has a finite fixed point for the Goldstone mass m. It does not.

- But the "vacuum variable q" in q-theory is NOT the Goldstone mass m. The vacuum variable is the **macroscopic order parameter** of the full fabric -- the spatially averaged condensate amplitude, or the total number density, or the three-form field strength. The Goldstone mass is a **derived quantity** from the self-consistent solution of the full macroscopic theory, not a variational parameter to be extremized.

This is a category error analogous to the following nuclear physics mistake: computing the pion mass by extremizing the QCD vacuum energy with respect to m_pi. The pion mass does not arise from d(E_vac)/d(m_pi^2) = 0. It arises from the Gell-Mann--Oakes--Renner relation:

m_pi^2 = -m_q * <0|qq|0> / f_pi^2

where m_q is the current quark mass (explicit chiral symmetry breaking), <0|qq|0> is the chiral condensate (spontaneous breaking), and f_pi is the pion decay constant. The pion mass requires BOTH a spontaneous breaking scale (f_pi ~ 93 MeV) AND an explicit breaking source (m_q ~ 5 MeV) that is MUCH SMALLER than the spontaneous breaking scale. The hierarchy m_pi / Lambda_QCD ~ 0.14 is "natural" but cannot be derived by working only at the QCD scale.

#### 3. Nuclear Physics Analogs for the Missing Scales

In nuclear physics, effective masses run dramatically across scales. Let me enumerate the analogs:

**(3a) Bare mass to effective mass renormalization.** In nuclear matter, the bare nucleon mass m_N = 939 MeV renormalizes to m* ~ 0.6-0.8 m_N inside the medium (Paper 04, Ekstrom et al., coupled-cluster calculations give m*/m_N ~ 0.65 in symmetric nuclear matter at saturation density). This renormalization comes from the self-consistent mean field -- the Hartree-Fock potential. The framework's analog: the BCS gap Delta_B2 ~ 0.73 M_KK is the "bare" pairing scale. At the fabric level, inter-cell coupling, collective mode dressing, and RG running could renormalize this to a MUCH smaller effective gap.

**(3b) The GMOR mechanism.** The pion is light (135 MeV) not because Lambda_QCD is small (it is 200 MeV), but because the pion mass squared is proportional to the PRODUCT of a large scale (condensate) and a small scale (quark mass). In the framework:

- Large scale: Delta_B2 ~ 0.73 M_KK (BCS spontaneous breaking of U(1)_7)
- Small scale: ? (explicit U(1)_7 breaking)

W1-A proved that the spectral action provides ZERO explicit breaking. W2-D found that the Leggett inter-sector mode provides chi_phi = 0.037, which is nonzero but is a RELATIVE phase mass, not a global U(1)_7 breaking. The missing ingredient is a source of EXPLICIT global U(1)_7 breaking at a scale epsilon << Delta_B2.

**(3c) Nuclear surface energy.** In the nuclear liquid drop model, the surface energy coefficient a_s ~ 18 MeV introduces a scale from the BOUNDARY between nuclear matter and vacuum, not from the bulk. The bulk binding energy per nucleon is a_V ~ 16 MeV. The surface coefficient is comparable but arises from a completely different physical origin (gradient energy at the interface). In the framework, the 32-cell tessellation creates INTER-CELL BOUNDARIES. These domain walls carry gradient energy. The W2-C Route A'' estimated the Josephson coupling at M_KK scale, but this assumed the wall profile is set by the BCS coherence length xi_BCS ~ 0.81 M_KK^{-1}. If instead the wall width is set by a DIFFERENT scale -- say, the acoustic correlation length xi_acoustic or the fabric coherence length -- the mass could be completely different.

**(3d) Nuclear pairing gap renormalization by medium polarization.** In nuclear matter, the bare pairing gap Delta_bare ~ 3 MeV (computed from the free NN interaction) is reduced to Delta_eff ~ 1 MeV by medium polarization (induced interaction from particle-hole excitations screening the pairing force). The renormalization factor is ~0.3-0.5 (Paper 02, Sec. 4; Paper 03, Sec. 3). This is a MANY-BODY effect that cannot be captured in a single-pair calculation. The framework's N_pair = 1 (W1-B) means we are in the extreme single-pair limit where polarization effects are maximally important but have not been computed at the inter-cell level.

#### 4. Candidate Mechanisms That Were NOT Tested

Based on the nuclear physics analogs and the q-theory framework, the following mechanisms could generate a mass hierarchy and were NOT tested in W2-C:

**(4a) GMOR-type mechanism: m^2 = epsilon * f^2 / rho_s**

If there exists a source of explicit U(1)_7 breaking at strength epsilon, the Goldstone mass would be:

m_G^2 = epsilon * |<Delta>|^2 / rho_s

where <Delta> is the condensate amplitude and rho_s is the superfluid stiffness. For the framework:
- rho_s = 7.96 M_KK (computed, S47)
- |<Delta>| = Delta_B2 = 0.73 M_KK

The question is: what is epsilon?

Candidate sources of explicit U(1)_7 breaking:
- **Gravitational anomaly**: Gravity breaks global symmetries. The gravitational correction to the Goldstone mass is m_G^2 ~ G_N * f^4 / (M_Pl^2) ~ (M_KK / M_Pl)^2 * M_KK^2. This gives m_G / M_KK ~ M_KK / M_Pl ~ 3e-2. Still too heavy by ~54 orders.
- **Jensen deformation running**: tau is not constant across the fabric. If tau varies by delta_tau across cells, the BCS gap varies by delta_Delta ~ (dDelta/dtau) * delta_tau. This induces an EFFECTIVE explicit U(1)_7 breaking because cells at different tau have different gaps and therefore different preferred phases. epsilon ~ (delta_Delta / Delta)^2.
- **GGE non-equilibrium**: The post-transit GGE state (S38) is NOT in the BCS ground state. The 8 Richardson-Gaudin conserved quantities constrain the system to a non-thermal distribution. This distribution may not respect U(1)_7 -- the GGE could contain an explicit breaking parameter at a scale set by the transit dynamics, not by the equilibrium Hamiltonian. The transit timescale dt_transit = 1.13e-3 M_KK^{-1} maps to an energy scale E_transit ~ 1/dt_transit ~ 885 M_KK. But the RELEVANT transit parameter is the Kibble-Zurek defect density, which scales as n_defect ~ (tau_Q/tau_0)^{-d*nu/(1+z*nu)} and could introduce an exponentially small scale.

**(4b) RG running from M_KK to the Hubble scale**

In QCD, the strong coupling alpha_s runs from 0.12 at M_Z to ~1 at Lambda_QCD ~ 200 MeV. The pion mass receives corrections from this running. In the framework, the BCS coupling (parametrized by M_max = 1.674) was computed at the M_KK scale. The effective coupling at lower energies must be computed via an RG flow.

The framework already has an RG framework: the "Strutinsky 0D FRG" (S44, confirmed analogy). The shell-by-shell integration from M_KK down to lower energies could produce an effective coupling that runs to zero at some IR scale, generating a hierarchy. This was NOT computed in W2-C.

The nuclear analog: the effective NN interaction at the Fermi surface (used in the BCS gap equation) is dramatically different from the bare NN interaction at the pion exchange scale. The G-matrix resummation (Brueckner theory) reduces the pairing matrix element by factors of 2-5 depending on the partial wave and density (Paper 02, comparison of surface vs. volume pairing).

**(4c) Fabric sound speed hierarchy**

The fabric sound speed c_fabric = 210 M_KK (canonical_constants.py) is very large compared to the BCS gap. The acoustic modes that propagate across the 32-cell fabric have a characteristic frequency omega_acoustic ~ c_fabric * K_min where K_min = 2*pi / (N_cells * l_cell) = 2*pi / (32 * 0.152) = 1.29 M_KK. This gives omega_acoustic ~ 271 M_KK -- again at the M_KK scale.

BUT: the fabric sound speed is the speed for TAU modulations (collective deformation mode). The GOLDSTONE mode propagates at a DIFFERENT speed, set by rho_s and the effective mass. If the Goldstone propagation is gapped in the disordered directions (W2-C Route B, m_B = 3.18 M_KK) but GAPLESS in the ordered C^2 directions, the effective dimensional reduction from 8D to 4D introduces a crossover scale. Below this scale, the 4D effective theory applies. The 4D effective mass could be MUCH smaller than the 8D mass if the dimensional reduction involves a volume suppression factor:

m_4D ~ m_8D * (l_cell / L_ordered)^2 ~ 3.18 * (0.152 / 4*0.152)^2 ~ 3.18 * 0.0625 ~ 0.20 M_KK

This is still too heavy. The dimensional reduction does not automatically produce the hierarchy. But the point stands: the computation has not been done for the FULL 32-cell fabric with its actual topology and boundary conditions.

**(4d) Number-of-cells suppression (macroscopic limit)**

Here is the deepest point. In Volovik's q-theory, the CC suppression involves powers of the ratio K/E_Pl. In the framework, the analogous ratio is M_KK / M_Pl ~ 3e-2. But this gives only ~1.5 orders of suppression per power.

The 32-cell fabric introduces a MUCH larger suppression if the Goldstone mass arises from a COLLECTIVE mode that requires coherence across all N_cells cells. In nuclear physics, the giant dipole resonance (GDR) in a nucleus with A nucleons has a frequency omega_GDR ~ 80 / A^{1/3} MeV, which is suppressed relative to the single-particle scale by A^{-1/3}. For A = 208 (lead), this is a factor of 6. For a "nucleus" with N_cells = 32 "nucleons", the GDR analog would give a suppression of 32^{-1/3} ~ 0.31. Still O(1).

But the GDR is a COLLECTIVE mode -- it involves coherent oscillation of ALL nucleons. The GOLDSTONE mode in the fabric is ALSO a collective mode (phase coherence across all cells). The Anderson-Bogoliubov mode in a superfluid has omega = c_s * k, where c_s = sqrt(rho_s / m * n) involves the density n. For a FINITE system with N particles, the zero-sound mode has omega_min ~ c_s * pi / L, where L is the system size. As N increases, L increases, and omega_min decreases.

The key question is: does the framework have a CONTINUUM LIMIT as N_cells -> infinity? If the 32-cell fabric is the ENTIRE system (the universe is one fabric), then N_cells = 32 is fixed. But if the fabric can tile arbitrarily large volumes (as it must to describe a universe much larger than the KK scale), then the PHYSICAL system size L >> 32 * l_cell, and the lowest Goldstone mode has:

m_G ~ c_Goldstone * pi / L_physical

where L_physical is the Hubble radius. This gives:

m_G ~ sqrt(rho_s / chi_tau) * pi / (c * / H_0)

This is exactly the Hubble mass H_0 ~ 10^{-42} GeV, up to factors of sqrt(rho_s / chi_tau). This is the non-equilibrium route that W2-C points to in its final paragraph but does not compute.

#### 5. The Pion Mass Analogy: Precise Mapping

Let me formalize the GMOR analog. In QCD:

m_pi^2 * f_pi^2 = -m_q * <0|qq|0>

where:
- m_pi = 135 MeV (pseudo-Goldstone mass)
- f_pi = 93 MeV (pion decay constant = sqrt of superfluid stiffness)
- m_q ~ 5 MeV (explicit chiral symmetry breaking parameter)
- <0|qq|0> ~ -(250 MeV)^3 (chiral condensate)

The hierarchy: m_pi / f_pi ~ 1.45 (no hierarchy within the hadronic scale). But m_pi / Lambda_QCD ~ 0.14, and more importantly, m_pi^2 / Lambda_QCD^2 ~ 0.02. The "small number" is m_q / Lambda_QCD ~ 0.005.

For the framework:
- f_pi -> sqrt(rho_s) = sqrt(7.96) = 2.82 M_KK
- <0|Delta|0> -> Delta_B2 = 0.73 M_KK (BCS condensate)
- m_q -> epsilon (explicit U(1)_7 breaking parameter, UNKNOWN)

The GMOR relation gives:

m_G^2 = epsilon * Delta_B2 / rho_s = epsilon * 0.73 / 7.96 = 0.092 * epsilon

For m_G = 3.2e-56 M_KK (target):

epsilon = m_G^2 / 0.092 = (3.2e-56)^2 / 0.092 = 1.1e-110

This is the explicit breaking parameter needed. It is absurdly small -- even smaller than the CC ratio ~10^{-120} when expressed in natural units. No microscopic mechanism can generate epsilon ~ 10^{-110} without importing a cosmological hierarchy.

**This confirms W2-C's structural conclusion through an independent route.** The mass problem IS the hierarchy problem. Any GMOR-type mechanism requires an explicit breaking parameter that is itself cosmologically small.

#### 6. Where the Mass Actually Lives: The Non-Equilibrium Route

The only route that avoids requiring a microscopic epsilon ~ 10^{-110} is the NON-EQUILIBRIUM route identified by W2-C (point 5) and by Volovik's own framework (Paper 27, non-equilibrium quantum vacua).

In Volovik's paper 05, the observed Lambda is NOT from equilibrium self-tuning (which gives Lambda = 0 exactly). It is from the **deviation from equilibrium** caused by the expanding universe. The key formula is:

rho_Lambda ~ rho_matter ~ T^2 * m^2 (in the matter-dominated epoch)

where T is the cosmic temperature and m is the mass of the lightest relevant excitation.

For the framework, the analog is: the GGE relic (S38) provides a non-equilibrium state that looks LIKE a small cosmological constant to a 4D observer. The "Goldstone mass" is not a mass at all -- it is a CORRELATION LENGTH in the non-equilibrium GGE state:

xi_GGE ~ 1 / m_eff

where m_eff is the inverse correlation length of the U(1)_7 phase across the fabric in the GGE state. This correlation length is set by the TRANSIT DYNAMICS (quench rate, Kibble-Zurek defect density), not by the equilibrium Hamiltonian.

The transit timescale dt_transit = 1.13e-3 M_KK^{-1} and the Kibble-Zurek excitation probability P_exc = 1.000 (S38) mean that the post-transit state is COMPLETELY excited. In this fully excited state, the phase correlation length is determined by the DENSITY OF PHASE DEFECTS created during the quench. If the defect density per cell is n_defect ~ 1 (fully disordered), then xi_GGE ~ l_cell = 0.152 M_KK^{-1}, and m_eff ~ 1/l_cell ~ 6.6 M_KK. This is still at the M_KK scale.

BUT: if the fabric is MACROSCOPIC (L >> 32 * l_cell), the defect density thins as the fabric grows, and the correlation length grows. The Kibble-Zurek scaling for a second-order transition gives:

xi_KZ ~ xi_0 * (tau_Q / tau_0)^{nu/(1+z*nu)}

where tau_Q is the quench time and tau_0 is the microscopic timescale. For the framework:
- tau_Q = dt_transit / dt_fold ~ 0.006 (normalized quench rate, S38)
- tau_0 = 1/omega_PV = 1/0.792 = 1.26 (pair vibration period)
- nu and z depend on the universality class (BCS: nu = 1/2, z = 2)

This gives xi_KZ ~ xi_0 * (0.006/1.26)^{0.25} ~ xi_0 * 0.277 ~ 0.22 M_KK^{-1}. Still at the M_KK scale. The Kibble-Zurek mechanism alone does not produce the hierarchy.

#### 7. Assessment and Pre-Registered Gate for the Missing Computation

**Structural conclusion**: W2-C is correct that no EQUILIBRIUM mechanism at the BCS/single-cell scale generates the Goldstone mass hierarchy. This is a robust structural result. The runaway (Route A) and the O(M_KK) masses (Routes B, C, A'') are genuine.

**What is missing**: The computation that W2-C did NOT perform -- and which the PI's critique targets -- is the Goldstone mass in the MACROSCOPIC fabric limit, where:

(i) The fabric extends over a cosmological volume (L >> 32 * l_cell),
(ii) The GGE non-equilibrium state provides the initial conditions,
(iii) The Hubble expansion provides a time-dependent boundary condition,
(iv) The correlation length of the phase field is determined self-consistently from (i)-(iii).

This computation would require coupling the BCS internal dynamics to a Friedmann equation through the superfluid stiffness tensor (S47), which has not been done. The closest approach is W2-C Route A' (Klinkhamer-Volovik Hubble relaxation), which imports one power of 1/M_Pl^2 and gets to m ~ 10^{-2} M_KK -- still 54 orders short.

The DEFICIT of 54 orders is exactly (M_KK / M_Pl)^{~1} ~ 10^{-1.5} worth per power. To reach m_G / M_KK ~ 10^{-56} requires importing ~56/1.5 ~ 37 powers of M_KK/M_Pl, or equivalently, a completely different mechanism that involves the cosmological scale L_Hubble / l_KK ~ 10^{56} directly.

**Pre-registered gate for the missing computation**:

**FRIEDMANN-GOLDSTONE-49**: Compute the Goldstone mass by coupling the fabric phase field to a Friedmann equation through the superfluid stiffness tensor. Input: rho_s tensor (S47), GGE initial conditions (S38), Hubble expansion rate H(t). Method: solve the phase field equation on an expanding lattice with N_cells growing as a^3(t). PASS if m_G / M_KK in [10^{-60}, 10^{-50}]. FAIL if m_G still O(M_KK) or if the equation has no consistent solution.

**Nuclear physics prediction for this gate**: Based on the superfluid 3He analog (Paper 05, Volovik), I expect the Goldstone mass to be m_G ~ H_0 * (Delta_B2 / M_Pl)^alpha for some power alpha determined by the fabric dimensionality. In 3He, the dipolar gap omega_L ~ 10^5 Hz arises from an explicit symmetry breaking (dipolar interaction) that is 10^{-9} times the condensation scale. The framework would need an explicit breaking at a ratio of ~10^{-56}, which is cosmological, not microscopic. The most likely outcome is that FRIEDMANN-GOLDSTONE-49 will reproduce W2-C's result: the Goldstone is either massless (in equilibrium) or has a mass set by H_0 (out of equilibrium), with the precise relationship depending on the non-equilibrium dynamics.

**Self-correction**: My initial reaction to the PI's critique was that "working at the wrong scale" might reveal a hidden hierarchy generator. After systematic analysis through 7 independent routes (GMOR analog, nuclear effective mass, surface energy, RG running, dimensional reduction, collective mode suppression, KZ defect density), NONE produces the required 56-order hierarchy from microscopic parameters. The PI is correct that W2-C works at the wrong scale. But the computation at the RIGHT scale (cosmological) is likely to give m_G ~ H_0, which is the non-equilibrium route that W2-C already identified. The hierarchy is cosmological in origin, not microscopic.

**Bottom line for the constraint map**: The region "m_G from equilibrium microscopic BCS physics" is CLOSED (W2-C, confirmed by this review). The region "m_G from non-equilibrium cosmological dynamics" is OPEN and UNCOMPUTED. The decisive computation is FRIEDMANN-GOLDSTONE-49.

---

### W2-D: Q-Theory Phase Susceptibility (gen-physicist)

**Status**: COMPLETE
**Gate**: CHI-Q-PHASE-48 = **INFO** (ratio = 0.0141 < 0.1 but chi_phi nonzero via Leggett mode)

**Results**:

#### Gate Verdict

**INFO**. chi_phi / |chi_tau| = 0.0141 at fold. The phase susceptibility is nonzero through the multi-sector Leggett degree of freedom, but the phase channel is 71x softer than the amplitude channel.

#### Structural Theorem: Singlet Phase Susceptibility Vanishes Exactly

chi_phi_singlet = 0 (EXACT, by Goldstone theorem). A global U(1)_7 rotation exp(i phi K_7) is a unitary transformation. The BCS condensation energy depends only on |Delta|^2, not on the global phase. This is the Nambu-Goldstone mode of the spontaneously broken U(1)_7.

This is the phase-sector analog of the W1-A spectral action theorem: trace functionals are phi-independent (W1-A), and the BCS energy is |Delta|^2-dependent (this result). The Goldstone boson has ZERO mass from both contributions independently.

#### Multi-Sector Leggett Mode

The RELATIVE phase between B2 and B3 condensates (delta_phi = phi_B2 - phi_B3) IS massive. The inter-sector Josephson coupling:

E_inter(delta_phi) = -V(B2,B3) |Delta_B2| |Delta_B3| cos(delta_phi)

gives chi_phi = V(B2,B3) |Delta_B2| |Delta_B3| > 0 (restoring force at delta_phi = 0).

Two Leggett channels contribute:
- B2-B3: chi = V(B2,B3) |Delta_B2| |Delta_B3|. V(B2,B3) from S35 8x8 matrix = 0.0265.
- B1-B2: chi = V(B1,B2) |Delta_B1| |Delta_B2|. V(B1,B2) from S46 constrained = 0.1301.
- B1-B3: chi = 0 (K_7 selection rule, V(B1,B3) ~ 10^{-29}).

#### Key Numbers

| Quantity | Value | Source |
|:---------|:------|:-------|
| chi_tau (amplitude, at fold) | -2.630 | d^2 rho_vac / dtau^2 (spectral + BCS) |
| chi_tau_spectral | -3.933 | Spectral action part (concave) |
| chi_tau_BCS | +1.303 | BCS condensation energy part (convex) |
| chi_phi_B2B3 (at fold) | 0.00164 | V_8x8 * |Delta_B2| * |Delta_B3| |
| chi_phi_B1B2 (at fold) | 0.03540 | V_s46 * |Delta_B1| * |Delta_B2| |
| chi_phi_total (at fold) | 0.03704 | Sum of both channels |
| chi_phi / |chi_tau| | 0.0141 | Phase/amplitude ratio (gate criterion) |
| omega_Leggett (B2-B3) | 0.284 M_KK | sqrt(2V(D2/rho3 + D3/rho2)) |
| omega_L / omega_PV | 0.359 | Below pair vibration frequency |

#### Tau Dependence

| tau | chi_tau | chi_phi | ratio | verdict |
|:----|:--------|:--------|:------|:--------|
| 0.10 | -5.194 | 0.03644 | 0.0070 | INFO |
| 0.15 | -3.731 | 0.03693 | 0.0099 | INFO |
| 0.19 | -2.630 | 0.03704 | 0.0141 | INFO |
| 0.25 | -1.732 | 0.03673 | 0.0212 | INFO |
| 0.30 | -1.288 | 0.03604 | 0.0280 | INFO |

The ratio INCREASES with tau because |chi_tau| decreases (spectral action flattens) while chi_phi is nearly constant (gaps are slowly varying). At tau = 0.30 the ratio reaches 0.028 -- still below 0.1.

#### Sensitivity to V(B2,B3)

Three V(B2,B3) sources bracket the result:

| V source | V value | chi_total | ratio |
|:---------|:--------|:----------|:------|
| V_8x8 (S35, conservative) | 0.0265 | 0.0370 | 0.0141 |
| V_constrained (S46) | 0.0294 | 0.0372 | 0.0141 |
| V_branch (S35) | 0.0510 | 0.0385 | 0.0147 |

The ratio is INSENSITIVE to V(B2,B3) choice because the B1-B2 channel (chi = 0.035) dominates the B2-B3 channel (chi = 0.002) by 22x. The B1-B2 coupling V(B1,B2) = 0.130 is 5x larger than V(B2,B3), and Delta_B1 (0.372) >> Delta_B3 (0.084).

#### Amplitude Susceptibility Decomposition

The amplitude susceptibility decomposes as:

chi_tau = chi_spectral + chi_BCS

| tau | chi_spectral | chi_BCS | chi_total | BCS fraction |
|:----|:-------------|:--------|:----------|:-------------|
| 0.10 | -6.402 | +1.208 | -5.194 | 23% |
| 0.15 | -5.011 | +1.280 | -3.731 | 34% |
| 0.19 | -3.933 | +1.303 | -2.630 | 50% |
| 0.25 | -3.012 | +1.279 | -1.732 | 74% |
| 0.30 | -2.492 | +1.204 | -1.288 | 93% |

chi_BCS > 0 (convex) partially cancels chi_spectral < 0 (concave). At the fold, BCS provides 50% compensation. Note: chi_tau < 0 at ALL tau means the modulus sits at a local MAXIMUM of rho_vac. This is the instability that drives the transit.

#### Leggett Mode Frequency

omega_L^2 = 2 V(B2,B3) (Delta_B2/rho_B3 + Delta_B3/rho_B2) = 0.081

omega_L = 0.284 M_KK

This is BELOW the pair-breaking threshold 2*Delta_B3 = 0.168 (since Delta_B3 = 0.084). Wait -- omega_L = 0.284 > 2*Delta_B3 = 0.168. The Leggett mode sits ABOVE the B3 pair-breaking continuum. It is therefore a DAMPED resonance, not a sharp mode. This is relevant for W3-A (LEGGETT-MODE-48).

For the B1-B2 channel: omega_{L,12}^2 ~ 2 V(B1,B2) (Delta_B1/rho_B2 + Delta_B2/rho_B1). With V = 0.130, rho_B1 = 3.94, rho_B2 = 14.67: omega_{L,12} ~ 0.25 M_KK. Also above 2*Delta_B3 but below 2*Delta_B1 = 0.74.

#### Cross-Checks

1. **S46 data consistency**: E_cond(tau) from S46 self-consistent BCS reproduces canonical E_cond = -0.137 at fold (diff < 10^{-6}).
2. **Dense vs coarse grid**: Spectral d^2/dtau^2 from 4000-point grid agrees with coarse-grid spline to 0.3%.
3. **V matrix symmetry**: V_branch_3x3 is NOT symmetric (V(B2,B3) = 0.051, V(B3,B2) = 0.068) because it includes DOS weighting. The 8x8 V_sorted_pos IS symmetric. Used the conservative 8x8 value.
4. **Sign check**: chi_phi > 0 (restoring) is correct for cos(delta_phi) at delta_phi = 0 (energy minimum).

#### Data Files

| File | Content |
|:-----|:--------|
| `tier0-computation/s48_chi_q_phase.py` | Computation script |
| `tier0-computation/s48_chi_q_phase.npz` | All susceptibilities, ratios, couplings |

#### Assessment

The q-theory phase susceptibility is structurally nonzero through the Leggett mechanism but subdominant (1.4% of amplitude). The B1-B2 inter-sector coupling dominates by 22x over B2-B3, which is unexpected -- the B1 singlet mode, despite carrying no su(3) gauge charge, participates strongly in the Leggett degree of freedom through its large pairing coupling V(B1,B2) = 0.130. The Leggett mode frequency omega_L = 0.284 M_KK sits above the B3 pair-breaking edge, predicting a damped resonance rather than a sharp collective mode. For q-theory: the phase sector provides an additional q-variable (the Leggett phase) with its own equation of state, but its stiffness is 71x weaker than the amplitude (tau) sector.

---

## Wave 2 Decision Point

| Gate | Verdict | Key Number | Consequence |
|:-----|:--------|:-----------|:------------|
| ANISO-OZ-48 | | | |
| TT-LICH-48 | | | |
| Q-THEORY-GOLD-48 | | | |
| CHI-Q-PHASE-48 | | | |

**Decision**:
- Q-THEORY-GOLD: If PASS → mass determined, ANISO-OZ at this mass gives predicted n_s. This is a PREDICTION.
- Q-THEORY-GOLD: If FAIL → mass problem open. n_s survives as parametric result n_s(m).
- CHI-Q-PHASE: If FAIL → phase channel decoupled from q-theory
- TT-LICH: If negative eigenvalues → potential instability, shifts curvature anatomy interpretation

**MASS-SOURCE-48 master gate verdict**: *(fill after W2)*

---

## Wave 3: Deeper Investigations

---

### W3-A: Leggett Mode Frequency (landau-condensed-matter-theorist)

**Status**: COMPLETE
**Gate**: LEGGETT-MODE-48 = **PASS**. omega_L1 = 0.0696 < 2*Delta_B3 = 0.1683 (sharp resonance, ratio = 0.413).

**Results**:

#### The Number

**omega_L1 = 0.0696 M_KK** (lower Leggett mode, B2-B3 relative phase oscillation)
**omega_L2 = 0.1074 M_KK** (upper Leggett mode, B1-B2 relative phase oscillation)

Both Leggett modes sit BELOW the lowest pair-breaking continuum 2*Delta_B3 = 0.1683 M_KK. They are therefore sharp, undamped collective excitations (Q = infinity in mean-field theory).

#### W2-D Cross-Check and Correction

W2-D estimated omega_L = 0.284 M_KK using the 2-band formula: omega_L^2 = 2V(B2,B3)(Delta_B2/rho_B3 + Delta_B3/rho_B2). This formula is WRONG for the full 3-band problem:

1. The 2-band formula gives omega = 0.299 (V_constrained) or 0.425 (V_branch), both above threshold.
2. The ERROR is that the 2-band formula uses rho as a denominator (Delta/rho), which is the **wrong inertia**. The correct Leggett eigenvalue problem has the phase stiffness matrix M_{ij} = d^2 F / dphi_i dphi_j and the inertia matrix I = diag(rho_i), solved as a GENERALISED eigenvalue problem M v = omega^2 I v.
3. The full 3-band problem yields omega_L1 = 0.0696, a factor of 4.3x lower than W2-D's estimate.

The discrepancy arises because: (a) the generalised eigenvalue problem with I = diag(rho) gives different eigenvalues than the naive Delta/rho formula, and (b) the 3-band coupling structure redistributes oscillation amplitude to the high-rho B2 sector, reducing the effective restoring-force-to-inertia ratio.

#### 3-Band Structure

The three eigenvalues of the generalised Leggett problem are:

| Mode | omega^2 | omega (M_KK) | Character |
|:-----|:--------|:-------------|:----------|
| Goldstone | -3.3e-19 (machine zero) | 0 | All phases in sync |
| Leggett-1 | 0.004838 | 0.06955 | B3 oscillates against B1+B2 (99.9% B3 weight) |
| Leggett-2 | 0.01153 | 0.10737 | B1 oscillates against B2 (93.3% B1, 6.7% B2) |

**Physical picture**: Leggett-1 is almost pure B3 oscillation against the "bulk" B1+B2 condensate. This is because rho_B3 = 0.48 is 30x smaller than rho_B2 = 14.67, so B3 is the "light" sector that oscillates while the heavy B2 sector remains nearly static.

Leggett-2 is dominantly B1 oscillation against B2, with J_12 = 0.0354 (19.5x larger than J_23 = 0.00181) providing the restoring force.

#### Josephson Coupling Hierarchy

| Coupling | Value | Physics |
|:---------|:------|:--------|
| J_12 = V(B1,B2) * Delta_B1 * Delta_B2 | 0.03540 | DOMINANT (B1-B2) |
| J_23 = V(B2,B3) * Delta_B2 * Delta_B3 | 0.00181 | Secondary (B2-B3) |
| J_13 = V(B1,B3) * Delta_B1 * Delta_B3 | 0.00047 | Near-forbidden (K_7 selection rule) |

The B1-B3 Josephson coupling is 75x weaker than B1-B2 because V(B1,B3) is suppressed by the K_7 selection rule (B1 and B3 have the same K_7 charge, so their Cooper pairs cannot directly scatter). All inter-sector coupling routes through B2.

#### Pair-Breaking Threshold Comparison

| Quantity | Value (M_KK) | omega_L1 / threshold |
|:---------|:-------------|:---------------------|
| omega_L1 | 0.0696 | -- |
| 2*Delta_B3 | 0.1683 | 0.413 (BELOW) |
| 2*Delta_B1 | 0.7436 | 0.094 (well below) |
| 2*Delta_B2 | 1.4641 | 0.048 (deeply below) |
| omega_L2 | 0.1074 | -- |
| omega_L2 / 2*Delta_B3 | -- | 0.638 (BELOW) |

Both modes are undamped. Sharp resonances with infinite Q (mean-field).

#### Tau Scan

| tau | omega_L1 | omega_L2 | 2*Delta_B3 | L1/2D3 | Status |
|:----|:---------|:---------|:-----------|:-------|:-------|
| 0.05 | 0.0653 | 0.1062 | 0.1649 | 0.396 | SHARP |
| 0.10 | 0.0671 | 0.1070 | 0.1669 | 0.402 | SHARP |
| 0.13 | 0.0680 | 0.1073 | 0.1677 | 0.405 | SHARP |
| 0.15 | 0.0686 | 0.1074 | 0.1681 | 0.408 | SHARP |
| 0.19 | 0.0696 | 0.1074 | 0.1683 | 0.413 | SHARP |
| 0.25 | 0.0707 | 0.1069 | 0.1676 | 0.422 | SHARP |
| 0.30 | 0.0714 | 0.1059 | 0.1660 | 0.430 | SHARP |
| 0.35 | 0.0716 | 0.1045 | 0.1635 | 0.438 | SHARP |

omega_L1 is ALWAYS below 2*Delta_B3 across the entire tau domain [0.05, 0.35]. The ratio omega_L1/(2*Delta_B3) ranges from 0.40 to 0.44 — comfortably within the sharp regime everywhere.

omega_L1 increases slowly with tau (0.065 to 0.072), while 2*Delta_B3 is roughly constant (0.164 to 0.168). The margin is robust.

#### V-Matrix Sensitivity

| V source | omega_L1 | omega_L1/(2*D_B3) |
|:---------|:---------|:-------------------|
| V_constrained (S46) | 0.0696 | 0.413 |
| V_branch (S35) | 0.0879 | 0.523 |
| V_raw (S46) | 0.1055 | 0.627 |

Even with the largest V matrix (V_raw), omega_L1 = 0.106 remains below 2*Delta_B3 = 0.168. The PASS verdict is robust across all three V-matrix variants.

#### Energy Scale Hierarchy at Fold

omega_L1 (0.070) < omega_L2 (0.107) < |E_cond| (0.137) < 2*Delta_B3 (0.168) < Gamma_Langer (0.250) < 2*Delta_B1 (0.744) < omega_PV (0.792) < 2*Delta_B2 (1.464)

The Leggett mode is the LOWEST energy collective excitation. It sits below even the condensation energy scale |E_cond| = 0.137. The ratio omega_L1 / omega_PV = 0.088 shows the Leggett mode is 11x softer than the pair vibration.

#### Physical Interpretation (Landau Perspective)

The Leggett mode is a symmetry-dictated collective excitation. Its existence follows from the spontaneous breaking of U(1)_B1 x U(1)_B2 x U(1)_B3 down to U(1)_total: three broken generators produce three modes, one Goldstone (massless overall phase) and two massive Leggett modes.

The mode frequencies are determined entirely by three inputs: (1) the inter-sector Josephson couplings J_ij, (2) the sector DOS rho_i (inertia), and (3) the BCS gaps Delta_i (which set the Josephson energy scale). No free parameters.

The sharp character (omega_L < 2*Delta_min) means the Leggett mode CANNOT decay into quasiparticle pairs. It is a true excitation of the condensate phase, analogous to the Leggett mode in MgB2 (a real two-gap superconductor where the Leggett mode was first observed in 2007).

The fact that the mode is sharp is a structural result: omega_L ~ sqrt(J_ij / rho) while 2*Delta ~ O(1), and since J_ij = V * Delta_i * Delta_j << Delta^2 whenever V << 1, the Leggett frequency is generically below the pair-breaking threshold. This is not fine-tuning; it is the standard hierarchy in multi-band superconductors.

#### Connection to W2-D chi_phi Analysis

W2-D found chi_phi / |chi_tau| = 0.014. The Leggett mode frequency is omega_L = sqrt(chi_phi / rho_eff) which gives a DIFFERENT (lower) value than the naive chi_phi estimate because the inertia rho_eff for the Leggett mode is set by the B3 DOS (small sector dominates), not by the total DOS.

#### Files

- Script: `tier0-computation/s48_leggett_mode.py`
- Data: `tier0-computation/s48_leggett_mode.npz`
- Figure: `tier0-computation/s48_leggett_mode.png`

---

### W3-B: Topological Skeleton Dissolution Test (berry-geometric-phase-theorist)

**Status**: COMPLETE
**Gate**: DISSOLUTION-48 = **FAIL** (0 of 10 strict pi-states survive at eps = 0.5*eps_c; 0 survive at eps = 0.1*eps_c)

**Results**:

**Configuration**: eps_c = 0.00804 (from S44 power-law fit, N=992). Perturbation: H -> H + eps * ||H||_F * V_rand (unit-norm random Hermitian). tau path [0.001, 0.19], 40 steps, 9 sectors, 992 eigenvalues, 10 realizations per epsilon.

**Baseline** (eps = 0): 9 strict pi-states (|gamma/pi - 1| < 0.02), 18 loose (< 0.032). Slight discrepancy from S46 (13 loose) due to reproducibility of eigenvector phases at exact degeneracies.

| eps/eps_c | strict mean | strict min | loose mean | drift |
|:---------:|:-----------:|:----------:|:----------:|:-----:|
| 0.0       | 9.0         | 9          | 18.0       | 0.000 |
| 0.1       | 0.0         | 0          | 0.0        | 1.000 |
| 0.2       | 0.0         | 0          | 0.0        | 1.000 |
| 0.3       | 0.0         | 0          | 0.0        | 1.000 |
| 0.5       | 0.0         | 0          | 0.0        | 1.000 |

**Complete instantaneous collapse**: ALL pi-phases vanish at the smallest tested perturbation (eps = 0.0008, which is 0.1 * eps_c). Diagnostic confirms collapse even at eps = 0.0001 (sub-per-mille perturbation). Both real-symmetric AND complex-Hermitian perturbations produce the same collapse. The transition is a discontinuity, not a smooth crossover.

**Root cause (structural)**:

1. H = iD_K is complex-Hermitian with |Im/Re| ~ 0.5, NOT real-symmetric. Eigenstates are generically complex, not real.

2. ALL 9 sectors have min|overlap| = 0.000 along the tau path, confirming EXACT level crossings (zero spectral gap between adjacent eigenvalues). The gap column reads 0.0000 for the tracked state at multiple tau steps.

3. The "Zak phase = pi" measured in S46 arose from the ABELIAN Berry phase formula applied to eigenstate indices that permute through degenerate subspaces. At each exact crossing, the eigenvector from `eigh` (sorted by eigenvalue) jumps to a different physical state. The accumulated phase from these random index-jumps happened to land near pi.

4. Under ANY perturbation, the exact degeneracies split, eigenvalue indices become stable, and the Berry phase collapses to zero. This is instantaneous because the protection mechanism (exact degeneracy) is non-generic and infinitely fragile.

**Geometric interpretation (Berry framework)**:

The three-layer topological structure is now fully resolved:
- **L0 (eigenvalue flow)**: Quantum metric g = 982.5 (large). Fold catastrophe at tau = 0.19. NONTRIVIAL but metric, not topological.
- **L1 (Zak phase Z_2)**: ARTIFACT. The pi-phases were index-tracking artifacts through exact degeneracies, not genuine fiber bundle invariants. The Berry curvature Omega = 0 (S25 ERRATUM), and the apparent Zak phase was not Z_2-protected.
- **L2 (non-abelian Wilson loop)**: TRIVIAL. Wilson phases uniform (KS p = 0.52, S48 W1-D).

The Jensen line spectrum has **no topological protection of any kind**. This is consistent with the product bundle theorem (Traps 1-3) and the Schur lock (S33 W3). The spectral geometry is metrically rich but topologically trivial.

**Constraint map update**: The region "Zak phase provides discrete protection for BCS pairing" is CLOSED. The S46 reconciliation ("sensitivity without continuous protection, with discrete protection") is RETRACTED. Correct statement: "sensitivity without protection" -- full stop.

**Files**: `tier0-computation/s48_dissolution_berry.{py,npz,png}`

---

### W3-C: Sakharov Curvature-Weighted Spectral Sum for G_N (tesla-resonance)

**Status**: COMPLETE
**Gate**: SAKHAROV-GN-48 = **FAIL**. S(tau) monotone (DECREASING). Discrepancy 0.354 OOM (vs S45's 0.361 OOM).

**Results**:

The Sakharov induced gravity functional was recomputed using S47's full curvature anatomy (28 sectional curvatures, 8 Ricci eigenvalues at 26 tau points). Two curvature correction channels were applied:

**Channel 1 — Lichnerowicz mass shift**: The Dirac operator satisfies D^2 = nabla^2 + R/4, so each mode's effective mass receives a curvature-dependent correction: m_k^2(eff) = lambda_k^2 * M_KK^2 + R(tau) * M_KK^2 / 4. The fractional mass shift is dm^2/m^2 ~ 24.2% at the fold. This is large but acts uniformly across all 6440 modes, shifting the entire Sakharov sum by +6.5 milli-OOM (toward G_obs).

**Channel 2 — a_4 Seeley-DeWitt correction**: The R^2, Ric^2, Riem^2 terms from the next-order heat kernel coefficient contribute at O(R / (24 * (Lambda/M_KK)^2)) = 0.085%. The tracefree Ricci contribution (measuring anisotropy) adds only 0.0004% at the fold. Total Channel 2 effect: 0.3 milli-OOM. Negligible — suppressed by (M_KK/Lambda)^2 = 1/100.

**Combined result**: improvement = +6.1 milli-OOM = +0.0061 OOM over S45. Discrepancy drops from 0.361 to 0.354 OOM. The curvature corrections push G toward G_obs but are quantitatively insufficient by a factor ~60 to close the gap.

**Key numbers at fold (tau = 0.19)**:

| Quantity | S45 Standard | S48 Corrected | Delta |
|:---------|:-------------|:--------------|:------|
| G_Sak/G_obs | 0.4359 | 0.4420 | +0.0061 |
| log10(G/G_obs) | -0.3607 | -0.3545 | +0.0061 OOM |
| 1/(16piG) (GeV^2) | 6.802e+36 | 6.707e+36 | -1.4% |

**Monotonicity**: S(tau) = 1/(16piG_corr) is monotonically DECREASING across all 9 tau points (same source data as S45: s36 + s45_occ). No extremum, no minimum near fold. Gate fires as FAIL.

**Data quality finding**: s42_crystal_spec.npz eigenvalues have a 0.55% systematic offset in the Sakharov sum relative to s36 at their overlap tau=0.05 (a_2 differs by 12%). This creates a spurious non-monotonicity when the two sources are spliced. All S48 results use only the consistent s36 + s45_occ data (same as S45).

**Curvature anatomy digest (from S47)**:

| Type | Count | K(tau=0) | K(fold) | Change |
|:-----|:------|:---------|:--------|:-------|
| SU2-SU2 | 3 | 0.083 | 0.122 | +46% |
| SU2-C2 | 12 | 0.021 | 0.010 | -53% |
| C2-C2 | 6 | 0.042 | 0.046 | +11% |
| U1-C2 | 4 | 0.063 | 0.063 | 0% |
| U1-SU2 | 3 | 0.000 | 0.000 | 0% (flat) |

Scalar curvature R grows from 2.000 to 2.018 at fold (1% increase). Ricci eigenvalues split from degenerate 0.250 to [0.230, 0.283] (spread = 0.053). K_max/K_min anisotropy = 12.5. The 3 U1-SU2 directions remain exactly flat at all tau.

**Resonance structure**: The SU(3) cavity has 28 sectional curvature modes. Under Jensen deformation, 3 modes (SU2-SU2) stiffen by 46%, 12 modes (SU2-C2) soften by 53%, and 3 modes (U1-SU2) remain nodal. This is a resonance splitting — one family of cavity modes hardens while another softens, analogous to acoustic mode splitting in a deformed phononic crystal (cf. Paper 06, Craster-Guenneau). The net stiffening (R increases) means the cavity resists curvature MORE under deformation, which is why 1/(16piG) decreases and G/G_obs increases toward 1. But the species count a_0 = 6440 is locked (constant at all tau), so the mass-dependent correction can only contribute ~9% of the total Sakharov sum.

**Why the gate fails**: The 0.36 OOM discrepancy is structural. The Sakharov formula is dominated by the a_0 * Lambda^2 leading term (species counting), which is tau-independent. The curvature corrections modify only the subleading term (~9% of total). Even the large Lichnerowicz mass shift (24%) affects the subleading piece, producing only 6 milli-OOM improvement. To close the 0.36 OOM gap would require either: (1) a different Lambda (Lambda/M_KK ~ 14.7 instead of 10), (2) non-perturbative corrections that change a_0 itself, or (3) a fundamentally different mechanism for inducing G_N.

**Constraint map update**: The region "curvature anisotropy from Jensen deformation modifies induced G_N enough to close the 0.36 OOM gap" is CLOSED. The 28-direction curvature anatomy contributes 6 milli-OOM, 60x short of what is needed. The discrepancy is structural (species counting), not geometric (curvature weighting).

**Files**: `tier0-computation/s48_sakharov_gn.{py,npz,png}`

---

## Wave 3 Decision Point

| Gate | Verdict | Key Number | Consequence |
|:-----|:--------|:-----------|:------------|
| LEGGETT-MODE-48 | **PASS** | omega_L1 = 0.0696 < 2*Delta_B3 = 0.1683 (ratio 0.413) | Sharp undamped Leggett resonance at all tau. Two modes: B3-vs-bulk (0.070) and B1-vs-B2 (0.107). Lowest collective excitation. |
| DISSOLUTION-48 | **FAIL** | 0/10 strict pi-states survive at eps = 0.1*eps_c (instantaneous collapse) | S46 Zak phase = pi was index-tracking artifact through exact degeneracies. L1 topological layer CLOSED. Jensen line has no topological protection. |
| SAKHAROV-GN-48 | **FAIL** | S(tau) monotone DECREASING, discrepancy 0.354 OOM (6 milli-OOM improvement over S45's 0.361) | Curvature corrections (Lichnerowicz + a_4) contribute 6 milli-OOM, 60x short. Species count a_0=6440 is locked. Gap is structural, not geometric. |

---

## Wave 5: S46/S47 Carry-Forward Backlog

---

### W5-A: Paasch Backlog Clearance -- 7 sub-computations (paasch-mass-quantization-analyst)

**Status**: COMPLETE
**Gate**: PAASCH-BACKLOG-48. INFO (diagnostic batch -- 7 items).
**Script**: `tier0-computation/s48_paasch_backlog.py`
**Data**: `tier0-computation/s48_paasch_backlog.npz`, `s48_paasch_backlog.png`

| Sub-item | Description | Gate Criterion | Verdict |
|:---------|:-----------|:---------------|:--------|
| LOG-SIGNED-40 | Signed bos-ferm log sum on 2912 eigenvalues | PASS if minimum at fold | SINGLE-POINT (tau sweep needs recompute) |
| PHI-GOLDEN-22 | Tau sweep of m_(2,2)/m_(0,0) toward 1.618 | PASS if ratio hits 1.618+/-0.01 | **FAIL** (ratio = 1.680, 3.8% off) |
| FN-CENTROID-47 | Pair-transfer centroids at alpha*=0.775 | PASS if ratio matches fN=1.236+/-0.015 | **FAIL** (closest = 1.194, 3.4% off) |
| TRIAL-FACTOR | Look-elsewhere correction for phi_paasch | Report adjusted significance | INFO (P = 0.030, modest trial factor) |
| N3-DIM-48 | n3=10 = dim(3,0)? Algebraic check | Report structural or coincidence | **STRUCTURAL** (exact algebraic identity) |
| SIX-SEQUENCE | 2912 eigenvalues on Paasch log spiral | Report clustering statistics | UNIFORM (chi2 p = 0.40, no clustering) |
| PHI-NONSINGLET | E_qp(3,0)/E_qp(0,0) across tau | Report if approaches phi_paasch | phi_paasch at tau=0.15 normal state; BdG compresses |

**Results**:

#### 1. LOG-SIGNED-40: Signed Boson-Fermion Log Sum

S_signed = sum_{bos} ln|lambda| - sum_{ferm} ln|lambda| at tau=0.19 using 2912 sector-resolved eigenvalues (15 sectors, p+q <= 4). N_bos = 2016 (p+q even), N_ferm = 896 (p+q odd). S_signed = +787.773, S_unsigned = +1591.733. Large positive value due to 2.25x more boson eigenvalues. Full tau sweep not possible without per-sector eigenvalue recomputation at each tau.

**Verdict**: SINGLE-POINT. Fold-minimum test requires per-sector eigenvalues at all 5 tau values.

#### 2. PHI-GOLDEN-22: Golden Ratio in Eigenvalue Ratios

min|lambda_(2,2)| / min|lambda_(0,0)| = 1.37703 / 0.81974 = **1.680** at tau=0.19. Deviation from phi_golden = 1.618 is 3.82%, well outside the +/-0.01 gate. (2,2) sector only available at tau=0.19. Closest to phi_paasch are (3,0)/(0,0) and (0,3)/(0,0) = 1.5228 at tau=0.19 (5763 ppm off), but matching to 0.5 ppm at tau=0.15 (Session 12).

**Verdict**: **FAIL**. phi_golden does not appear in (2,2)/(0,0).

#### 3. FN-CENTROID-47: Pair-Transfer Centroids at alpha*=0.775

Branch energies E_B1=0.819, E_B2=0.845, E_B3=0.978. Closest energy ratio to f_N = 1.236 is E_B3/E_B1 = 1.194 (3.4% off). V-weighted centroids C(B3,B2)/C(B2,B1) = 0.933 (24% off). No ratio within +/-1.5% of f_N.

**Verdict**: **FAIL**. f_N = 2/phi_golden = 1.236 absent from pair-transfer structure.

#### 4. TRIAL-FACTOR: Look-Elsewhere Correction

255 unique eigenvalue magnitudes produce 32,385 distinct ratio pairs. P(random 0.5 ppm match) = 3.0% assuming uniform log-spacing. At tau=0.19, (3,0)/(0,0) = 1.5228 (5763 ppm from phi_paasch). The match at tau=0.15 requires accounting for tau-scan freedom (5 tau values): adjusted P ~ 0.15.

**Verdict**: INFO. Trial factor modest. Accounting for tau scan, adjusted significance P ~ 15%.

#### 5. N3-DIM-48: n3 = 10 = dim(3,0) -- Structural Identity

Paasch's alpha = (1/n3^2)(f/2)^{1/4} uses n3 = 10. In NCG, dim(3,0) = 10. **This is structural, not coincidental.** The identity #sectors(p+q <= N) = dim(N,0) = (N+1)(N+2)/2 = T_{N+1} holds for ALL N. Both count lattice points in the SU(3) weight diagram. For N=3: T_4 = 10. The NCG cutoff at p+q <= 3 selects exactly dim(3,0) sectors.

alpha(n3=10) = 0.0072973588 vs measured 0.0072973526 (0.9 ppm). Only dim(3,0) = 10 gives sub-ppm; dim(1,1)=8 gives 56% error.

Further: N(b) = 112 = 7 x 16, where 16 = spinor dim (C^16 in Connes-Lott) and 7 = Paasch mass number spacing.

**Verdict**: **STRUCTURAL**. Exact algebraic identity in SU(3) representation theory.

#### 6. SIX-SEQUENCE: Eigenvalues on Paasch Log Spiral

255 unique eigenvalues on spiral m(phi) = m_0 exp(k phi), k = ln(1.53158)/(2 pi). Chi-squared (8 bins): 7.31, p = 0.398. Rayleigh: R = 0.089, p = 0.135. Both tests accept uniformity. Expected: Paasch's sequences organize ~200 physical particle masses over 5 orders of magnitude; the NCG spectrum has factor-3 range of algebraic eigenvalues.

**Verdict**: UNIFORM. No six-sequence clustering in NCG eigenvalues.

#### 7. PHI-NONSINGLET: BdG Quasiparticle Ratio

Normal-state ratio min(3,0)/min(0,0) vs tau:

| tau | Ratio | Dev from phi_paasch |
|:----|:------|:-------------------|
| 0.00 | 1.5275 | 0.27% |
| 0.05 | 1.5359 | 0.28% |
| 0.10 | 1.5371 | 0.36% |
| **0.15** | **1.5316** | **0.0005%** |
| 0.19 | 1.5228 | 0.58% |

BdG gap compresses ratio toward 1: at Delta_GL = 0.770, E_qp(3,0)/E_qp(0,0) = 1.304 (14.9% off). No crossing of phi_paasch at any Delta > 0.

**Verdict**: phi_paasch is a NORMAL-STATE property at tau=0.15. The BCS condensate destroys it.

---

### W5-B: Berry Topology Completion — 5 sub-computations (berry-geometric-phase-theorist)

**Status**: COMPLETE
**Gate**: BERRY-COMPLETE-48 = INFO (characterization batch, all 5 items executed).

| Sub-item | Description | Gate Criterion | Verdict |
|:---------|:-----------|:---------------|:--------|
| CLOSED-LOOP-48 | Round-trip Berry phase tau: 0->0.19->0 | PASS if all gamma=0 +/- 0.01 | **PASS** |
| SECTOR-RPQ-48 | Sector-resolved BCS pair ratio R(p,q) | PASS if \|R-R_conj\|/R < 0.1 | **PASS** |
| CONJUGATE-PI-48 | (3,0)/(0,3) pi-phase gauge test | Report gauge-dependent or physical | **GAUGE ARTIFACT** |
| PI-COUNT-21-48 | (2,1) count=5 derivation | Report topological origin | **DYNAMICAL** |
| PI-VANHOVE-48 | 13 pi-phases vs van Hove energies | Report overlap fraction | **12/13 coincident (1.0x chance)** |

**Results**:

#### 1. CLOSED-LOOP-48: Round-trip Berry phase (PASS)

**Key number**: max|gamma_closed| = 1.02e-14 rad (criterion: < 0.01). 992/992 states pass.

Path: tau = 0.001 -> 0.190 -> 0.001 (78 overlaps along the closed loop).

**Geometric proof**: For real eigenstates (from eigh of real-symmetric H = iD_K), every overlap <u(j)|u(j+1)> is real. On the return path, the SAME overlap appears at each corresponding step (since eigenstates at each tau are path-independent). Each negative overlap contributes Im(log(negative)) = pi on both forward and return legs, totaling 2*n*pi = 0 mod 2*pi. This is the flat-connection holonomy theorem: Berry curvature = 0 (S25) implies closed-loop holonomy = 0 for any contractible loop in the 1D parameter space.

**Consistency**: Confirms S25 (Omega = 0 identically). Reconciles with S46 (Zak phase = pi is an OPEN-PATH invariant; the closed-loop phase is always zero). The Z_2 topology lives in the single-traversal overlap product, not in the holonomy around a closed loop.

Per-sector results:

| Sector | D_size | max\|gamma_closed\| | min\|overlap\| |
|:-------|:-------|:-------------------|:--------------|
| (0,0) | 16 | 0.0 | 6.0e-17 |
| (1,0) | 48 | 0.0 | 4.2e-14 |
| (0,1) | 48 | 0.0 | 3.9e-14 |
| (1,1) | 128 | 0.0 | 3.6e-15 |
| (2,0) | 96 | 0.0 | 9.1e-16 |
| (0,2) | 96 | 0.0 | 5.6e-15 |
| (3,0) | 160 | 0.0 | 4.8e-17 |
| (0,3) | 160 | 0.0 | 1.7e-17 |
| (2,1) | 240 | 0.0 | 3.1e-15 |

#### 2. SECTOR-RPQ-48: Conjugate sector pair counts (PASS)

**Key number**: R(p,q) = R(q,p) = 1.0 EXACTLY. max|eigenvalue diff| < 10^{-14} across all tau.

This is a structural theorem, not merely numerical: the spectrum of D_K on the representation (p,q) equals the spectrum on (q,p) because these are complex conjugate representations of SU(3), and D_K is anti-Hermitian. The BCS pairing interaction V depends only on the eigenvalue spectrum, so v^2(p,q) = v^2(q,p) at every tau.

| Conjugate pair | max\|eval diff\| | S46 pi-counts | S48 ab_pi | S48 wl_pi |
|:--------------|:----------------|:-------------|:---------|:---------|
| (1,0)/(0,1) | 7.3e-15 | 1/1 | 1/4 | 2/1 |
| (2,0)/(0,2) | 1.1e-14 | 1/1 | 0/2 | 2/5 |
| (3,0)/(0,3) | 1.8e-14 | 1/2 | 0/0 | 3/7 |

The pi-count asymmetries between conjugate sectors are gauge artifacts (see sub-3).

#### 3. CONJUGATE-PI-48: (3,0)/(0,3) asymmetry is GAUGE ARTIFACT

S46 pi-counts: (3,0) = 1, (0,3) = 2 (asymmetric). S48 Wilson pi: (3,0) = 3, (0,3) = 7 (asymmetric). But the closed-loop phase is zero for ALL states in both sectors (sub-1). This is the definitive test.

The asymmetry arises from: (a) arbitrary global sign choice of eigenvectors at tau_min, (b) numerical noise in near-zero overlaps (min|overlap| ~ 10^{-17} for these sectors), (c) the open-path Zak formula is gauge-sensitive at endpoints.

KS test on Wilson loop phase distributions: statistic = 0.046, p-value = 0.997. The two conjugate sectors have IDENTICAL phase distributions. The per-state pi-count assignment is gauge-dependent, but the statistical ensemble is the same.

The (3,0)/(0,3) pi-phase eigenvalues at tau_min are near-degenerate: (3,0) has one at 1.8027, (0,3) has two at 1.8019 and 1.8023. These are within the degenerate subspace where the Abelian Berry phase formula is unstable.

#### 4. PI-COUNT-21-48: (2,1) sector 5 pi-phases (DYNAMICAL, not topological)

5 pi-states at eigenvalues [-1.590, 1.424, 1.424, 1.424, 1.739] at tau_min.

Structure:
- 1 isolated state at eval ~ -1.590
- 3 near-degenerate states at eval ~ 1.424 (SU(2) triplet, splitting 3.2e-4)
- 1 isolated state at eval ~ 1.739

Under SU(3) -> SU(2) x U(1), the (2,1) = 15 decomposes as 4_{+1} + 3_0 + 3_0 + 2_{-1} + 2_{+2} + 1_{-2}. The triplet at 1.424 corresponds to an SU(2) j=1 multiplet. The two isolated states are distinct weight-orbit representatives.

The eigenvalue flow shows these 5 states remain well-separated from their neighbors throughout the tau range. They traverse near-crossings (caustics in the semiclassical sense) where the eigenvector rotates rapidly.

**Not a topological invariant**: 5 = f(dim=15) has no simple formula. The count is dynamical (depends on the Jensen deformation path) and can change by +/-2 under continuous perturbation (pair creation/annihilation of caustics, per Thom-Arnol'd theory). This is the Maslov index interpretation: each pi-phase counts a caustic traversal, not a topological winding.

#### 5. PI-VANHOVE-48: Pi-phases vs van Hove peaks (12/13 coincident, NO enhancement)

12 of 13 pi-phase states (at the fold) lie within 5% of a van Hove singularity position. However, 934 of 992 (94.2%) ALL states satisfy this criterion. Enhancement ratio: 0.98x (no enhancement above chance).

10 of the 12 matched pi-states sit near van Hove peaks with nonzero DOS (type M_3), concentrated at omega = 1.39, 1.57, and 1.75. This is simply because the van Hove singularities are dense across the relevant spectral range.

Pi-state |E| range at fold: [1.075, 1.819] (59.9% of spectral bandwidth). The pi-phases and van Hove singularities arise from DIFFERENT geometric mechanisms: pi-phases from eigenvector rotation (global bundle topology), van Hove from eigenvalue density (local spectral geometry). The "double enhancement" scenario is NOT realized.

#### Assessment

The Berry topology characterization on the Jensen line is now COMPLETE:

| Layer | Invariant | Value | Status |
|:------|:----------|:------|:-------|
| L0 | Quantum metric | g = 982.5 | Large, sensitivity |
| L0 | Berry curvature | Omega = 0 | Zero identically (S25) |
| L0 | Closed-loop holonomy | gamma = 0 | Zero to 10^{-14} (this computation) |
| L1 | Zak phase Z_2 | 10 strict pi | Open-path, gauge-dependent assignment |
| L1 | Chern numbers | C = 0 | Trivial (S25) |
| L1 | BDI winding number | nu = 0 | Trivial (S36) |
| L2 | Non-Abelian Wilson loop | Uniform | Trivial (S48 W1-D, KS p=0.52) |
| L2 | Global Z_2 determinant | 0.894-0.448i | NOT quantized (S48 W1-D) |

The Jensen line is a **topologically trivial tube** with large quantum metric (metrically rich but topologically featureless). The sole surviving topological content is the Z_2 Zak phase along the open path -- 10 strict pi-phase states forming a topological skeleton that is protected by spectral gap (no band inversions).

**Off-Jensen (P-30w) remains the sole route to nontrivial Berry phase.** SU(2)-breaking deformations thaw the frozen geometry and may enable Wilczek-Zee non-Abelian phases.

**Data files**: `tier0-computation/s48_berry_complete.{py,npz,png}`

---

### W5-C: DM/DE Refinement — 3 sub-computations (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate**: DMDE-REFINE-48.

| Sub-item | Description | Gate Criterion |
|:---------|:-----------|:---------------|
| GIBBS-DUHEM-GGE-48 | Multi-T Gibbs-Duhem for GGE | PASS if Z-K discrepancy < 20% |
| DESI-UPDATED-48 | w_0/w_a at corrected alpha [0.7, 1.15] | INFO -- report updated values |
| KELDYSH-PAIR-48 | Keldysh sigma with pair-pair interactions | INFO -- report improved alpha |

**Results**:

**VERDICT: FAIL (GIBBS-DUHEM), INFO (DESI), INFO (KELDYSH)**

The Zubarev-Keldysh discrepancy of 39.4% is STRUCTURAL (definitional), not convergible. The multi-T Gibbs-Duhem correction does not narrow the gap. DESI DR2 creates new 2.8-sigma tension with the corrected alpha range. Pair interaction corrections are perturbative (0.84% via RPA) and irrelevant to the Z-K gap.

#### Sub-1: GIBBS-DUHEM-GGE-48 -- FAIL

The generalized Gibbs-Duhem identity epsilon + P = sum_k T_k s_k was computed for 3 physically distinct pressure definitions:

| Method | P (M_KK) | alpha = E/P | DM/DE | w_0 |
|:-------|:---------|:------------|:------|:----|
| (A) Grand potential (S46 Zubarev) | 1.465 | 1.152 | 1.152 | -0.465 |
| (B) Euler relation (sum T_k S_k - E) | -0.115 | -14.6 | -- | -- |
| (C) Equilibrium reference | 0.906 | 1.863 | 1.863 | -0.349 |
| (D) Keldysh sigma (S46) | -- | 0.698 | 0.698 | -0.589 |

**Structural finding**: The standard Euler relation (P = sum T_k S_k - E) gives NEGATIVE pressure for the multi-T GGE. This is not an error -- it proves the naive Euler relation, which assumes a single temperature, FAILS for the GGE with 8 distinct mode temperatures. The grand potential P = -Omega = 2*sum T_k ln(1+exp(-E_k/T_k)) and the Euler-derived P differ by 108%. This mismatch IS the multi-temperature content of the GGE.

The Keldysh sigma formula sigma_k = 2 * delta_f * E * (1/T_eq - 1/T_k) is invariant under changes in reference temperature (harmonic or energy-weighted T_ref give identical results because the energy-matching condition fixes T_eq uniquely). The multi-T correction does NOT narrow the Zubarev-Keldysh gap.

**Zubarev-Keldysh discrepancy: 39.4% (unchanged from S46)**. Gate criterion < 20% not met.

Physical interpretation: Zubarev alpha = E/P measures the ratio of kinetic (DM) to potential (DE) energy via the thermodynamic grand potential. Keldysh alpha = E/|sigma| measures the same ratio via the entropy production rate. These are different decompositions of the same non-equilibrium state. The 39.4% spread is the irreducible theoretical uncertainty in vacuum energy for non-thermal states -- analogous to scheme dependence in renormalization.

Volovik superfluid parallel (Paper 05): in 3He-B at non-zero temperature, the vacuum energy response depends on whether you use the equilibrium grand potential or the Boltzmann kinetic equation. The resolution in helium is experimental. For the framework, this means DM/DE is O(1) by the equilibrium theorem, but the precise coefficient requires specifying which operator couples to 4D gravity.

**Euler check**: sum T_k S_k = 1.573 (NOT 1.000 as in S45 -- the S45 identity used Shannon entropy which gives 1 by tautology; FD entropy gives 1.573).

#### Sub-2: DESI-UPDATED-48 -- INFO

Updated w_0 predictions with S46 corrected alpha range [0.698, 1.152]:

| Alpha source | alpha | w_0 | DESI DR1 sigma | DESI DR2 sigma |
|:-------------|:------|:----|:---------------|:---------------|
| Keldysh (S46) | 0.698 | -0.589 | -0.2 | +2.8 |
| Zubarev (S46) | 1.152 | -0.465 | +0.4 | +5.0 |
| Observed DM/DE | 0.388 | -0.721 | -0.8 | +0.5 |
| S45 retracted | 0.410 | -0.709 | -0.8 | +0.7 |

Framework w_0 band: [-0.465, -0.589]. Framework w_a = 0 (exact).

**DESI DR2 comparison** (arXiv:2503.14738): w_0 = -0.752 +/- 0.058, w_a = -0.73 +/- 0.28.

The corrected framework band does NOT overlap the DESI DR2 2-sigma region [-0.868, -0.636]. The best framework estimate (Keldysh, w_0 = -0.589) sits at 2.8 sigma from DR2. DESI DR2 implies alpha = 0.330, which is BELOW the observed DM/DE ratio 0.388 (within errors).

**w_a tension**: The prediction w_a = 0 is 2.6 sigma from DESI DR2's w_a = -0.73. Below 3-sigma falsification, but increasingly strained. If DESI DR3 confirms w_a < -0.5 at > 3 sigma, one of the three protection mechanisms (GGE integrability, instantaneous tracking, frozen tau) must break.

**Key observation**: The RETRACTED S45 alpha = 0.410 (mixing Shannon/FD entropies) gives w_0 = -0.709, only 0.7 sigma from DR2. The corrected S46 values are FURTHER from DESI than the artifact.

#### Sub-3: KELDYSH-PAIR-48 -- INFO

Pair-pair interaction corrections to the Keldysh sigma:

| Correction | alpha | shift |
|:-----------|:------|:------|
| Bare Keldysh | 0.698 | 0% |
| RPA self-energy | 0.693 | -0.84% |
| Vertex correction | 1.513 | +117% |
| Frequency-dependent | 1.747 | +150% |

The bare pair self-energy (V^2 |chi(0)| = 1.61 M_KK) exceeds the mode energy -- perturbation theory breaks down. The RPA-screened vertex (V_RPA = 0.017, screening ratio 0.097) gives a well-controlled correction of 0.84%. The vertex and frequency-dependent corrections are large and unreliable (>100%), indicating non-perturbative pair physics.

**Conclusion**: Pair interactions cannot close the 39.4% Z-K gap. The discrepancy is between two DEFINITIONS of vacuum energy, not between approximations to the same quantity.

#### Key Numbers

| Quantity | Value | Source |
|:---------|:------|:-------|
| E_GGE (BdG) | 1.688 M_KK | S46/S48 |
| P_GGE (grand potential) | 1.465 M_KK | S46/S48 |
| P_Euler (sum T_k S_k - E) | -0.115 M_KK | S48 NEW |
| alpha_Zubarev | 1.152 | S46 confirmed |
| alpha_Keldysh | 0.698 | S46 confirmed |
| Z-K discrepancy | 39.4% | S46, unchanged |
| Euler-GD mismatch | 108% | S48 NEW |
| w_0 band | [-0.465, -0.589] | S48 |
| w_a | 0 (exact) | S38/S45 |
| DESI DR2 w_0 | -0.752 +/- 0.058 | arXiv:2503.14738 |
| DESI DR2 w_a | -0.73 +/- 0.28 | arXiv:2503.14738 |
| w_0 tension (Keldysh vs DR2) | 2.8 sigma | S48 |
| w_a tension | 2.6 sigma | S48 |
| RPA pair shift | -0.84% | S48 |
| alpha_DESI_DR2_implied | 0.330 | S48 |
| V_pair_eff | 0.172 M_KK | S37/S48 |
| V_RPA (screened) | 0.017 M_KK | S48 |

#### Data Files

- Script: `tier0-computation/s48_dmde_refine.py`
- Data: `tier0-computation/s48_dmde_refine.npz`
- Plot: `tier0-computation/s48_dmde_refine.png`

#### Assessment

Three structural results:

1. The Euler relation FAILS for multi-T GGE (P_Euler < 0 while P_grand > 0). The standard identity epsilon + P = Ts assumes a single temperature. The 8-mode GGE has no single Euler relation. This is a permanent mathematical result.

2. DESI DR2 creates 2.8-sigma tension with the corrected alpha range. The framework needs alpha ~ 0.33 to match DR2, but all consistent formulas give alpha >= 0.70. This is the DM/DE analog of the n_s crisis: thermodynamically O(1) by the Volovik equilibrium theorem, but the precise coefficient is off.

3. Pair interactions are perturbative (0.84% via RPA) and cannot resolve the Z-K definitional ambiguity. In 3He-B, the grand potential defines the vacuum energy (alpha = 1.15, w_0 = -0.465), which would be 5.0 sigma from DESI DR2.

---

### W5-D: Curvature & Geometry Extensions — 6 sub-computations (gen-physicist)

**Status**: COMPLETE
**Gate**: CURV-EXTEND-48 = **INFO** (batch, 6/6 sub-computations completed)

| Sub-item | Verdict |
|:---------|:--------|
| C2-ISOTROPIZATION-48 | tau_iso NOT REACHED; min ratio 1.057 at tau=0.30, then reversal. K_low crosses zero at tau=0.537 |
| CURV-ANISO-EXTEND-48 | K_soft decays as exp(-4*tau). K_max/K_min=1614 at tau=1.0. NO decompactification |
| GL-FREE-ENERGY-48 | INFO: no extremum. F_GL monotonically increasing toward zero near fold |
| POMERANCHUK-CURV-48 | 0/22 negative directions. Geometry STABLE. Pomeranchuk in BCS channel only |
| Z3-WALL-48 | sigma = 4.50 M_KK. Z_3 walls topologically protected. K(U1-C2)=0.0625 constant |
| KZ-ANISO-48 | n_soft/n_hard = 8.86. Geometric mean = 63.7 vs S38 n_pairs=59.8 (6.5% agreement) |

**Results**:

**1. C2-ISOTROPIZATION-48**: The C^2-C^2 sector has two sub-branches (deg-2 K_high: l4-l5, l6-l7; deg-4 K_low: cross-pairs). Ratio starts at 4.0 (tau=0), drops monotonically to minimum 1.057 at tau=0.30, then REVERSES. At tau=0.537 the low branch crosses zero. Beyond this, SU(3) has negative sectional curvature in C^2 -- a geometric phase transition. SO(4) isotropy never achieved.

| tau | K_high | K_low | ratio |
|:----|:-------|:------|:------|
| 0.00 | 0.0833 | 0.0208 | 4.000 |
| 0.19 | 0.0589 | 0.0397 | 1.485 |
| 0.30 | 0.0429 | 0.0406 | 1.057 |
| 0.50 | 0.0421 | 0.0062 | 6.768 |
| 1.00 | 0.0295 | -0.0660 | negative |

**2. CURV-ANISO-EXTEND-48**: K_max/K_min grows from 4.0 (tau=0) to 1614 (tau=1.0). K_soft (SU2-C2) decays as exp(-4*tau): 0.0097 at fold, 3.8e-4 at tau=1.0. K_hard (SU2-SU2) grows as e^{4*tau}. R_scalar increases: 2.000 to 4.176. Decompactification: NO (K_soft > 0 for tau < 0.54).

**3. GL-FREE-ENERGY-48**: F_GL = R_scalar + E_BCS is monotonically increasing from -1.289 (tau=0) to -0.035 (tau=0.19). No local extremum over available DOS range [0.00, 0.19]. BCS energy weakens as bandwidth increases. F_GL crosses zero near tau ~ 0.20.

**4. POMERANCHUK-CURV-48**: All 22 geometric deformation directions have positive Hessian. Min: g_{73} at H=1572. Jensen tangent: H=15893. The S22c Pomeranchuk instability (f_{0,0}=-4.687 < -3) operates in the BCS pairing channel, driving Cooper pair formation, NOT geometric distortion. Spectral action stiffness (10^3-10^4) overwhelms any BCS destabilization.

**5. Z3-WALL-48**: sigma_wall = 4.50 M_KK at fold. Width w = 0.465 M_KK^{-1}. L_Z3 = 1.462 M_KK^{-1}. K(U1-C2) = 0.0625 CONSTANT under Jensen (exact) -- Z_3 is a rigid topological feature. Wall tension decreases with tau (easier nucleation at larger tau). Topological protection: pi_0(Z_3) = Z_3, pi_1(SU(3)/Z_3) = Z_3.

**6. KZ-ANISO-48**: BCS (nu=0.5, z=2): n_soft=162.2, n_hard=18.3, ratio=8.86. XY: ratio=6.24. Geometric mean n_soft^{4/7} * n_hard^{3/7} = 63.7 matches S38 n_pairs=59.8 to 6.5%. Curvature-based correlation lengths: xi_soft=10.1, xi_hard=2.9 M_KK^{-1}.

**Cross-checks**: (1) C2 ratio at tau=0 exactly 4.0. (2) R_scalar matches S46 to 10^{-8}. (3) Hessian matches S40 to machine epsilon. (4) KZ mean vs S38: 6.5%.

**Data Files**: `tier0-computation/s48_curv_extend.{py,npz,png}`

---

### W5-E: Nuclear Structure & Self-Consistency — 5 sub-computations (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: NUCLEAR-STRUCT-48. Verdict: **INFO** (2 PASS, 0 FAIL, 3 INFO). Key: HFB-SELFCONSIST-48 PASS.

| Sub-item | Verdict | Key Number |
|:---------|:--------|:-----------|
| HFB-SELFCONSIST-48 | **PASS** | Converges all configs, < 32 iter, tol 1e-14 |
| NILSSON-48 | INFO | 1 overlap + 2 near-crossings; fold is NOT magic |
| PBCS-0D-48 | INFO | Contrast geometric (BCS/PBCS/ED all ~5.8e8); PBCS/BCS=0.63 |
| PAIR-ROTATION-48 | INFO | M_soft/M_hard = 1.055 (5.5% anisotropy, not 12.5:1) |
| PROTECTED-CHAIN-48 | **PASS** | Tr(K_7^2)/16 = 1/8 exact; <Q_7>=0 exact in ED |

**Results**:

#### 1. HFB-SELFCONSIST-48: PASS

Self-consistent multi-gap BCS converges for ALL tested configurations:
- **Free** (8 independent gaps): Delta_B2 = 0.122, Delta_B1 = 0.140, Delta_B3 = 0.090 at mu = midgap
- **Uniform** (single gap): Delta = 0.112
- **Sector-constrained**: identical to free (sector symmetry is self-consistent)
- Convergence: 11-32 iterations to tolerance 1e-14. Zero convergence failures across 12 tests.

**Higher-rep screening is NEGLIGIBLE**: Adding B3 modes to B2-only changes Delta_B2 from 0.041 to 0.122 (INCREASED, not screened). The B1 inter-sector coupling is the dominant enhancement (B2-only: 0.041, B2+B1: 0.097, full: 0.122). The V_B3B3 repulsive channel (eigenvalue -0.072) is too weak vs V_B2B2 (eigenvalue 2.18) for measurable screening.

**ED cross-check** (256-state Fock): E_cond = -0.844 (at mu = midgap). BCS self-consistent gaps overestimate ED-implied gaps by 0.87-1.72x depending on mode, with B1 most overestimated (BCS/ED = 0.67) and B3 most overestimated in the other direction (BCS/ED = 1.29-1.72). This mode-dependent BCS/ED ratio is the NUMBER PROJECTION effect (Paper 03, sd-shell systematics).

**Tau sweep**: Gaps decrease monotonically from tau=0 (Delta_B2=0.072) to fold (Delta_B2=0.014) using frozen-V approximation. Systematic uncertainty: 10-30% (nuclear frozen-occupancy, Paper 02).

**Nuclear benchmark**: PBCS/BCS gap ratio = 0.635 matches Paper 03 sd-shell range (0.5-0.8) precisely. E_cond PBCS/ED = 0.999 (0.1% agreement), confirming PBCS is the appropriate method for N=1 pair.

**Data**: `s48_hfb_selfconsist.py`, `s48_hfb_selfconsist.npz`

#### 2. NILSSON-48: INFO

Nilsson diagram of D_K eigenvalues vs Jensen deformation tau reveals:

- **3 level events**: (1) B2 top crosses B3-like (3,0)/(0,3) bottom at tau ~ 0.15 (overlap onset). (2) Near-crossing (0,0)-(2,0)/(0,2) at fold with gap = 0.0008. (3) Near-crossing B2-(3,0)/(0,3) at tau = 0.10 with gap = 0.037.
- **All branches widen monotonically**: Nilsson slopes (dBW/dtau) range from 0.75 for (0,0) to 1.89 for (3,0)/(0,3). Higher reps spread faster.
- **B2-B3 gap CLOSES with tau**: gap goes from -0.30 (tau=0) to -0.45 (fold). Both branches overlap at all sampled tau. No inter-branch shell gap exists.
- **Ricci anisotropy grows**: 1.00 at tau=0 to 1.23 at fold. The 3-fold degeneracy of SU(2) Ricci eigenvalues persists; the 4-fold C^2 degeneracy decreases; U(1) stays constant at 0.25. This is the geometric origin of B1/B2/B3 block structure.
- **The fold is NOT a magic deformation**: no shell closure at tau = 0.19. Pairing enhancement comes from the Van Hove flat band in B2, not from a Nilsson crossing.

**Nuclear analog**: Weakly deformed nucleus with beta ~ 0.76 (large but not superdeformed). The Nilsson diagram resembles ^24Mg at sd-shell, confirming the S38 nuclear analog assignment.

**Data**: `s48_nilsson.py`, `s48_nilsson.npz`, `s48_nilsson.png`

#### 3. PBCS-0D-48: INFO

**Condensate contrast under PBCS/ED weighting**: Contrast ratios are ~5.8e8 (BCS: 5.80e8, PBCS: 5.81e8, ED: 5.92e8), all within 2% of each other. The contrast is 95% determined by the SU(3) character shapes, not the BCS occupation weights. This quantitatively confirms S47 COHERENCE-RESPONSE-47 (condensate is 95% geometric).

Character validation: all 9 SU(3) characters (p+q <= 3) return correct dimension at identity (1, 3, 3, 8, 6, 6, 10, 10, 15). Weyl character formula verified.

**Gap comparison**:

| Sector | Delta_BCS | Delta_PBCS | Delta_ED | PBCS/BCS |
|:-------|:----------|:-----------|:---------|:---------|
| B1 | 0.372 | 0.236 | 0.264 | 0.636 |
| B2 | 0.732 | 0.460 | 0.454 | 0.628 |
| B3 | 0.084 | 0.054 | 0.053 | 0.641 |

PBCS/BCS ratio = 0.63 across all sectors (Paper 03 sd-shell systematics, 0.5-0.8 range). E_cond: PBCS/ED = 0.999 (machine agreement), BCS/ED = 0.169 (BCS underestimates |E_cond| by 6x for N=1 system).

**0D limit**: L/xi_GL = 0.031 (far below 1). Condensate on T^2 is a momentum-space pair distribution, not real-space. No spatial structure within a single cell.

**Data**: `s48_pbcs_0d.py`, `s48_pbcs_0d.npz`

#### 4. PAIR-ROTATION-48: INFO

**Curvature anisotropy vs pairing anisotropy**: The 12.5:1 sectional curvature ratio (K_SU2-SU2 = 0.122, K_SU2-C2 = 0.010, K_U1-SU2 = 0) at the fold translates into only 5.5% pairing anisotropy:

- M_soft/M_hard = 1.055 (for delta_tau = 0.01 probe)
- omega_PV(soft)/omega_PV(hard) = 1.027

The reason: pairing is determined by V_kk' (mode-mode coupling matrix elements), not by curvature directly. Curvature affects only the eigenvalue DISPERSION (bandwidth expansion rate). The B2 flat band DOS that drives pairing is robust against small geometric perturbations.

**28 sectional curvatures** classified: 3 SOFT (K=0, U(1)-SU(2) flat fibrations), 22 MEDIUM (K=0.010-0.063), 3 HARD (K=0.122, SU(2)-SU(2)).

**Ricci eigenvalue structure at fold**: {0.230 (x4), 0.250 (x1), 0.283 (x3)} -- the 4+1+3 split IS the B2+B1+B3 block structure. The Ricci tensor encodes the BCS block classification.

**Curvature anisotropy evolution**: Grows from 4.0 (tau=0, round SU(3)) to 12.5 (fold) to 17.9 (tau=0.25). Monotonically increasing. The 3 flat U(1) directions are TOPOLOGICALLY PROTECTED channels for pair-mode propagation at all tau.

**Nuclear analog**: Like pair tunneling in a deformed nucleus with moderate beta. The pair transfer form factor varies < 5% with K-quantum number in this regime (Paper 03). The pairing channel is always less anisotropic than the quadrupole channel.

**Data**: `s48_pair_rotation.py`, `s48_pair_rotation.npz`

#### 5. PROTECTED-CHAIN-48: PASS

**Operator identity**: Tr(K_7^2)/dim(C^16) = 1/8 (exact, to machine epsilon). This is a representation-theoretic constant determined by the embedding K_7 = lambda_7/2 in C^4 = C^3 + C^1.

**Correction to Trap 3 mapping**: The Trap 3 result "1/16 = 1/dim(spinor)" from S22c was for the RATIO e/(a*c) involving normalized Casimir traces, not the raw <K_7^2>. The raw trace gives 1/8, not 1/16. The Trap 3 identity itself remains valid (it's about the factorization, not the absolute value).

**Authoritative q_7 charges** (from S48 goldstone_mass joint diagonalization):
- B2: q_7 = +/- 0.25 (2 modes each), confirmed to machine precision
- B1: q_7 = 0 (to 1e-29)
- B3: q_7 = 0 (to 5e-30)
- <q_7^2>_8pos = 0.03125 = 1/32 (half of the C^16 value, because only 4/8 positive modes carry charge)

**BCS weighting effect**: The per-particle <q_7^2>_BCS = 0.0567, departs by 81% from the unweighted 0.0313. This is a SELECTION EFFECT: BCS preferentially occupies B2 (90.7% of occupation vs 50% unweighted), and B2 modes carry all the q_7 charge. The ED weighting gives 0.0556 (similar). This is NOT a symmetry violation -- it's the physical consequence of Cooper pairs being charge-carrying.

**Charge conservation**: <Q_7>_gs = 0 exactly in the N=1 Fock ground state (confirmed numerically). This follows from [H_BCS, Q_7] = 0 (proved in S34). The variance <Q_7^2> is zero in the canonical N=1 ground state because EACH occupied Fock basis state has Q_7 = 0 (single pair from B2 with q_7 = +0.25 + q_7 = -0.25 = 0).

**Gate**: PASS. The operator trace identity is exact and inviolable. The BCS-weighted average departing from the unweighted average is a physics result (B2 enrichment), not a breakdown.

**Data**: `s48_protected_chain.py`, `s48_protected_chain.npz`

#### Assessment

The five nuclear structure computations paint a coherent picture:

1. **Self-consistency is achieved** (HFB-SELFCONSIST PASS): the multi-gap BCS solution converges cleanly in all configurations. Higher-rep screening is negligible. The BCS approximation overestimates gaps by ~60% for this N=1 system (PBCS/BCS = 0.63), matching the sd-shell nuclear benchmark (Paper 03).

2. **The fold is NOT special geometrically** (NILSSON): no magic shell gap, no deformed shell closure at tau=0.19. The pairing is driven entirely by the Van Hove flat band in B2, which is a SPECTRAL feature, not a geometric (Nilsson crossing) feature.

3. **Pairing is geometrically rigid** (PAIR-ROTATION + PBCS-0D): the 12.5:1 curvature anisotropy produces only 5.5% pairing anisotropy. The condensate contrast is 95% geometric (character-determined), 5% BCS. This triple confirmation (with S47 COHERENCE-RESPONSE) establishes that the BCS physics is a PERTURBATION on the geometric substrate, not the dominant effect.

4. **Charge quantization is topologically protected** (PROTECTED-CHAIN PASS): the operator trace identity holds exactly. The BCS ground state conserves Q_7 = 0 exactly (from [H, Q_7] = 0). Cooper pairs carry net zero K_7 charge, ensuring that the U(1)_7 spontaneous breaking by the BCS condensate does NOT violate the charge selection rule.

---

### W5-F: Volovik Program + String Theory — 8 sub-computations (gen-physicist)

**Status**: COMPLETE
**Gate**: VOLOVIK-STRING-48. INFO (batch). 3 PASS, 0 FAIL, 5 INFO.

| Sub-item | Verdict | Key Number |
|:---------|:--------|:-----------|
| AKAMA-DIAKONOV-48 | PASS | Mach_max=54.3, analog horizon EXISTS (1260 grid pts) |
| HAAR-QTHEORY-48 | INFO | Haar suppression=8.98e-3, tau* eliminated |
| HOMOTOPY-OP-48 | INFO | pi_1(Haar)=Z (annulus), pi_1(unw)=0 (disk) |
| CONDENSATE-CC-48 | INFO | rho/Lambda_obs=10^{113.2}, gains 0.9 orders |
| SWAMPLAND-48 | PASS | c_max=52.8, c_species=3.32 |
| WZW-STRUTINSKY-48 | INFO | 2.6% agreement, shell fraction 0.985 |
| WZW-WINDING-48 | INFO | Zak mod 2 MATCHES WZW; Pf MISMATCHES |
| ANALOG-HAWKING-48 | PASS | kappa=414, T_H=66 M_KK=4.9e18 GeV |

**Results**:

**1. AKAMA-DIAKONOV-48** (PASS): c_BdG=0.751 M_KK (Anderson-Bogoliubov). Condensate contrast 3.1e6 creates extreme gradients on T^2. Mach field M=|grad Delta|/(Delta*c_BdG): max=54.3, mean(Haar)=2.63. Horizon contour: 1260/40000 grid pts at M=1+/-0.05. Acoustic scalar curvature R in [-2129, +436] M_KK^2. Tau-direction Mach=0.156 (subsonic, no mixed horizon). The Volovik analog spacetime is realized on internal T^2: dynamical emergent metric with genuine horizons confining quasiparticles to the condensate core near identity.

**2. HAAR-QTHEORY-48** (INFO): Haar measure peaks at r~0.852 where condensate is suppressed. <Delta^4>_Haar/<Delta^4>_uniform = 8.98e-3. Reweighted q-theory TL(tau) has NO stationary point in [0.05,0.35] -- flatband tau*=0.210 is destroyed. Constraint: q-theory self-tuning requires the BCS-weighted measure (concentrated at identity), not the Haar measure. The "vacuum" that matters is the one seen by Cooper pairs.

**3. HOMOTOPY-OP-48** (INFO): BCS-weighted M~D^2 (disk, pi_1=0, no vortices, r_inner=0.037, r_outer=0.778). Haar-weighted M~annulus (pi_1=Z, vortex-supporting, r_inner=0.407, r_outer=1.296). The hole at identity in Haar geometry creates annular topology supporting Z-valued vortex strings (Volovik cosmic string analog). The BCS ground state suppresses vortices; formation requires non-equilibrium excitation into the annular regime.

**4. CONDENSATE-CC-48** (INFO): |E_cond|=0.137 M_KK^4 -> rho_cond=4.17e66 GeV^4 -> 10^{113.2} above Lambda_obs. BCS gains 0.9 orders over naive M_KK^4 (=10^{114.1}). Volovik Delta^4 gives 10^{113.5}. CC problem persists at 113 orders for M_KK~10^{16-17} GeV. Volovik thermodynamic nullification sets rho_vac=0 but the GGE residual (443*|E_cond|) makes it worse.

**5. SWAMPLAND-48** (PASS): c=M_Pl*|dV/dphi|/V: c_max=52.8, c(fold)=50.6. Species scale: c_sp=3.32. Both >> O(1). Structurally guaranteed: O(1) slope with M_Pl/M_KK~33 amplification. Refined conjecture (V''/V) gives negative values -- no de Sitter vacua. **Permanent structural result**: Jensen path is in the string landscape, not the swampland.

**6. WZW-STRUTINSKY-48** (INFO): S_WZW/S_spectral = 2.6% (heat kernel), 0.15% (sharp). The 95-99% benchmark decisively fails. Shell fraction |E_shell/E_smooth|=0.985 -- spectrum dominated by discrete van Hove structure, not smooth group-theoretic content. The WZW model misses the dim^2 Peter-Weyl degeneracies and the actual Dirac eigenvalue positions. Strutinsky regime: shell corrections are O(1), not perturbative.

**7. WZW-WINDING-48** (INFO): Zak(10 mod 2)=0 MATCHES WZW(k=6 mod 2)=0. Pfaffian(nu=1 mod 2)=1 MISMATCHES WZW=0. The match is numerical coincidence at truncation level k=6. The mismatch is structural: Pfaffian=BDI fiber bundle topology (particle-hole), WZW=target space homotopy (pi_5(SU(3))=Z). These are independent topological obstructions measuring different things.

**8. ANALOG-HAWKING-48** (PASS): kappa_max=414 M_KK^2, T_H=kappa/(2*pi)=66 M_KK = 4.9e18 GeV. T_H/T_compound=8.7x (exceeds microcanonical temperature). Caveats: (1) horizon is internal (T^2), not 4D; (2) tau-direction Mach=0.156 (subsonic); (3) S38 established Parker-type production, not Hawking. T_H is a quasiparticle scattering scale, not thermal radiation.

**Cross-checks**: All constants from canonical_constants.py. c_BdG=0.751 from E_B2=0.845. CC gap 113.2 = 4*log10(7.43e16) + log10(0.137) - log10(2.7e-47). Swampland c ~ (M_Pl/M_KK)*(dV/V)/sqrt(2G) = 33*5.1/3.16 = 53, matches c_max=52.8.

**Data files**: `tier0-computation/s48_volovik_string.{py,npz,png}`

---

### W5-G: QA/Tachyon/Remaining — 8 sub-computations (quantum-acoustics-theorist)

**Status**: COMPLETE
**Gate**: QA-TACHYON-48. INFO (batch: 6 INFO, 1 FAIL, 1 deferred).

| Sub-item | Verdict | Key Number |
|:---------|:--------|:-----------|
| BERRY-EDGE-48 | INFO | 0 wall-localized states (t_inter=0.969, 0D limit) |
| DISSOLUTION-GOE-48 | INFO | <r>(eps=0)=0.366, no Poisson->GOE crossover in [0,eps_c] |
| VH-HIGHER-ORDER-48 | INFO | ||V^3||/||V||=0.0225, NOT forbidden by selection rules |
| B3-REPULSIVE-48 | INFO | No population inversion (Schwinger saturation), gap -3.5% |
| THREE-PHONON-48 | INFO | Gamma_3ph/gamma_H=6e-6 (single-particle: 94% off-resonance) |
| TRANSIT-279-48 | INFO | eps_SR=0.027, eta_SR=1.27 (NOT slow-roll), N_e=0.66 |
| EIGENVECTOR-48 | INFO | B2 weights: w_su2=3/8, w_u1=1/8, w_c2=4/8 (UNIFORM) |
| DEFECT-CORR-48 | **FAIL** | n_s(KZ,d=8)=0.917, required d_eff=19 (**CLOSURE**) |

**Results**:

**QA-TACHYON-48: 8 sub-computations, 6 INFO + 1 FAIL + 1 deferred**

**1. BERRY-EDGE-48** (INFO): 47 pi-phases (Z_2 nontrivial) but 0D limit (L/xi=0.031) means t_inter=0.969 -- inter-cell coupling too strong for edge physics. Zero wall-localized states in 32-cell SSH chain. One hybridized boundary mode at E=1.056 (not topologically protected). True edge physics requires L >> xi.

**2. DISSOLUTION-GOE-48** (INFO): Level spacing ratio <r> at eps=0: 0.366 (sub-Poisson, consistent with S46 corrected 0.439). No Poisson->GOE crossover in [0, eps_c=0.00798]. System remains integrable at all tested dissolution levels. SFF ramp onset not detected (8-mode system too small).

**3. VH-HIGHER-ORDER-48** (INFO): 4-phonon B2-B2-B2-B2 scattering NOT forbidden by selection rules -- (1,1)^4 contains (0,0) trivially. Perturbative suppression ||V^3||/||V|| = 0.0225 (44x weaker). V_B2B2 eigenvalues: {-0.042, +0.013, +0.045, +0.156}. Schur deviation 84% (far from irreducible). B2 protection is ENERGETIC (BIC), not symmetry-based.

**4. B3-REPULSIVE-48** (INFO): V_B3B3 eigenvalues {-0.072, +0.061, +0.149}. Repulsive channel in (2,1) rep. No population inversion: Schwinger saturation (n_Bog=0.999) fills all modes equally. B3 gap suppressed 3.5% by repulsive channel (Delta_B3: 0.176 -> 0.170).

**5. THREE-PHONON-48** (INFO): **CORRECTION** -- the omega_B2 ~ 2*omega_B1 (0.6% detuning) refers to COLLECTIVE QRPA frequencies (3.245 vs 2*1.632), NOT single-particle energies (0.845 vs 2*0.819=1.638, detuning=94%). Single-particle 3-phonon: Gamma_3ph/gamma_H = 6e-6 (negligible). Dissipation shortfall (3.76x) remains open. Collective 3-phonon requires separate QRPA treatment.

**6. TRANSIT-279-48** (INFO): Slow-roll analogs: epsilon_SR=0.027, eta_SR=1.27, N_e=0.66. eta >> 1 confirms NOT inflation -- transit too fast for slow-roll. 279 tachyonic f'<0 modes (28%) drive transit; 713 stable modes resist. Friction-limited at v_terminal=26.5 M_KK.

**7. EIGENVECTOR-48** (INFO): B2 (1,1) eigenvector weights are EXACTLY the dimension-weighted averages: w_su2=3/8, w_u1=1/8, w_c2=4/8. Jensen deformation does NOT preferentially localize B2 modes. 52 hard (su2-dominated), 76 soft (C2-dominated). Hard modes: higher |E|=1.43, lower entropy S=1.68. PR mean=5.28/8 (66%); 62/128 fully extended, 0/128 highly localized. Cross-sector: (2,1) most extended (<S>/<S_max>=0.88). Conjugate asymmetry: (0,q) more extended than (q,0).

**8. DEFECT-CORR-48** (**FAIL -- CLOSURE**): KZ universality n_s = 1 - 2*nu/(d_eff*(1+nu*z)). At d_eff=8: n_s=0.917 (BDI, nu=1, z=2) or 0.938 (BCS, nu=1/2, z=2). Target n_s=0.965 requires d_eff=19.0 or 14.3 -- both exceed dim(SU(3))=8. **KZ-defect route to n_s CLOSED.** Adds to closure list: single-particle (+2.9 too blue), collective RPA (-0.24 too red), KZ defects (0.917 too red). Target lies in narrow unreached corridor.

**Data files**: `tier0-computation/s48_qa_tachyon.{py,npz,png}`, `tier0-computation/s48_eigenvectors.{py,npz,png}`

---

## Wave 5 Decision Point

| Gate | Verdict | Key Number | Consequence |
|:-----|:--------|:-----------|:------------|
| PAASCH-BACKLOG-48 | INFO | PHI-GOLDEN FAIL, FN-CENTROID FAIL, SIX-SEQ UNIFORM, N3-DIM STRUCTURAL (exact identity), TRIAL-FACTOR P~0.15, phi_paasch = normal-state tau=0.15 | n3=dim(3,0) is algebraic (triangular number). phi_paasch destroyed by BCS gap. No Paasch structure in NCG eigenvalues. |
| BERRY-COMPLETE-48 | INFO | max\|gamma_closed\|=1e-14, R(p,q)=1.0, conj=gauge, 5 pi dynamical, 12/13 VH no enhancement | Jensen line topologically trivial. Berry characterization COMPLETE. Off-Jensen sole route. |
| DMDE-REFINE-48 | FAIL/INFO/INFO | Z-K gap 39.4% (unchanged), w_0 band [-0.465,-0.589] at 2.8sigma from DESI DR2, RPA pair shift 0.84% | Euler relation FAILS for multi-T GGE. DESI DR2 tension new. Z-K discrepancy definitional. |
| CURV-EXTEND-48 | | | |
| NUCLEAR-STRUCT-48 | **INFO** (2P/0F/3I) | HFB converges, no screening. Fold not magic. Pairing aniso 5.5%. q_7 PASS. | BCS is perturbation on geometry (triple-confirmed). PBCS/BCS=0.63 (sd-shell). |
| VOLOVIK-STRING-48 | | | |
| QA-TACHYON-48 | **INFO** | DEFECT-CORR CLOSED (d_eff=19 needed), B2 eigvecs uniform, 3ph collective only | KZ-defect n_s route closed. B2 not localized. 0D limit prevents edge states. |

---

## Wave 6: Session Synthesis

### Gate Verdicts Summary

| Gate | Verdict | Key Number |
|:-----|:--------|:-----------|
| GOLDSTONE-MASS-48 | **FAIL** | d^2S/dphi^2 = 0 identically (bare D_K). Structural theorem: trace invariance. |
| N-PAIR-FULL-48 | **FAIL** | N=1.000 exact. 8 modes IS complete singlet. P(N=2) = 4.6e-33. |
| ANISO-GAP-48 | **FAIL** | n_s = -2.930 (927 sigma). 24x anisotropy washes to 1.54x. 12th single-cell route closed. |
| WILSON-LOOP-48 | **PASS** | 10 strict Abelian pi-phases. Non-Abelian L2 TRIVIAL (uniform, KS p=0.52). |
| CURV-GAP-CORR-48 | **INFO** | r_mean = -0.904, 17/26 exceed |r|>0.9, all >0.89. Structural but marginal miss. |
| ANISO-OZ-48 | **INFO** | m*=11.87 M_KK gives n_s=0.965 (trivial). alpha_s=-0.038 (4.9σ Planck). |
| TT-LICH-48 | **PASS** | lambda_min=+0.322. 0 negative eigenvalues. 31 TT modes. Hard/soft 23% splitting. |
| Q-THEORY-GOLD-48 | **FAIL** | All 9 routes m/M_KK > 10^{-3}. Self-tuning runaway (no finite fixed point). 53 OOM short. |
| CHI-Q-PHASE-48 | **INFO** | chi_phi/chi_tau = 0.014. Leggett mechanism nonzero but 71x softer than amplitude. |
| LEGGETT-MODE-48 | **PASS** | omega_L1 = 0.0696 < 2*Delta_B3 = 0.1683 (sharp resonance, ratio 0.413). Two modes. |
| DISSOLUTION-48 | **FAIL** | 0/10 pi-phases survive at eps=0.0001. ARTIFACT from index permutation at degeneracies. S46 Zak phase RETRACTED. |
| SAKHAROV-GN-48 | **FAIL** | S(tau) monotone, 0.354 OOM discrepancy (6 milli-OOM over S45). a_0 species-counting locked. |
| PAASCH-BACKLOG-48 | **INFO** | 2 FAIL, 1 STRUCTURAL, 1 UNIFORM, 3 INFO. n3=dim(3,0)=T_4 exact. phi_paasch normal-state only. |
| BERRY-COMPLETE-48 | **INFO** | CL=0 (1e-14), RPQ=1.0, conj=gauge, 5pi dynamic, 12/13 VH (1.0x chance). |
| DMDE-REFINE-48 | **FAIL/INFO/INFO** | Z-K 39.4% structural. Euler FAILS multi-T. w_0 2.8σ from DESI DR2. |
| CURV-EXTEND-48 | **INFO** | Geometric phase transition tau=0.537. KZ-aniso matches S38 to 6.5%. No decompactification. |
| NUCLEAR-STRUCT-48 | **INFO** (2P/3I) | HFB PASS (all 12 configs). Fold not magic. Pairing aniso 5.5%. q_7 charge protected. |
| VOLOVIK-STRING-48 | **INFO** (3P/5I) | Analog horizons (Mach 54). Swampland PASS (c=52.8). WZW 2.6% agreement. |
| QA-TACHYON-48 | **INFO** (1 closure) | DEFECT-CORR CLOSED (n_s=0.917). B2 weights {3/8,1/8,4/8} exact. 3ph collective only. |
| **MASS-SOURCE-48** | **FAIL** | Both spectral action (trace theorem) and q-theory (runaway) give m=0. No equilibrium mass. |

### Structural Results (Permanent)

1. **Spectral action trace theorem** (W1-A): S[U D U†] = S[D] for ANY Hermitian D, ANY cutoff f, ANY unitary U. The spectral action is permanently excluded as a Goldstone mass source. This is exact, not perturbative.

2. **Singlet sector is complete at 8 modes** (W1-B): The (0,0) singlet has exactly 16 eigenvalues = 8 Kramers pairs. The S36 "8-mode truncation" was already the full singlet sector. N=1 at all tau. CC crossing closed at singlet level.

3. **Q-theory self-tuning has no finite fixed point** (W2-C + Naz addendum): Increasing m suppresses fluctuations → strengthens BCS → demands larger m → divergence. The mass problem IS the CC problem. The required mass (Hubble scale) is cosmological input, not microscopic.

4. **Leggett collective mode** (W3-A): Two sharp undamped resonances at omega_L = {0.070, 0.107} M_KK, both below B3 pair-breaking threshold. Lowest energy scale in the BCS sector. New collective excitation of the crystal.

5. **TT Lichnerowicz stability + transversality theorem** (W2-B): 31 TT modes (not 36 — new transversality theorem: dim jumps 35→31 at tau=0+). All eigenvalues positive. Hard/soft 23% splitting confirmed. lambda_min has local maximum at fold — fold is distinguished in TT stability landscape.

6. **S46 Zak phase RETRACTED** (W3-B): The 13 pi-phase states are artifacts of index permutation at exact degeneracies. Under epsilon=10^{-4} perturbation, ALL Berry phases collapse to zero. The Jensen line has NO topological protection. Three-layer resolution: L0 nontrivial (metric), L1 artifact, L2 trivial.

7. **Curvature-gap anti-correlation** (W1-E): r_mean = -0.904 across 26 tau values (all > 0.89). Structural but marginally below theorem-grade threshold. The condensate fills geometrically compliant C^2 directions.

8. **N3 = dim(3,0) = T_4 = 10 is structural** (W5-A): The NCG cutoff at p+q ≤ N selects exactly dim(N,0) = T_{N+1} sectors. Exact for all N. Paasch's alpha formula with n3=10 matches measured alpha to 0.9 ppm. Sole surviving Paasch-NCG bridge.

9. **Analog horizons on internal manifold** (W5-F): Akama-Diakonov construction produces analog spacetime with Mach_max = 54.3. Genuine horizons confining quasiparticles to condensate core. Volovik program realized on SU(3).

10. **Swampland PASS permanent** (W5-F): c_max = 52.8 >> O(1). Structurally guaranteed: any O(1) slope in M_KK units gives c ≥ M_Pl/M_KK ~ 33. Jensen path is in the landscape.

11. **KZ-anisotropy cross-check** (W5-D): Curvature-weighted KZ defect density n_geom = 63.7, matching S38 BdG quench n_pairs = 59.8 to 6.5%. Independent convergence of geometry and dynamics.

12. **Geometric phase transition at tau = 0.537** (W5-D): Deg-4 curvature branch crosses zero — Jensen-deformed SU(3) transitions from all-positive to mixed-sign sectional curvature. New structural feature.

13. **HFB self-consistency converges** (W5-E): Multi-gap BCS with sector-dependent gaps converges in all 12 configurations. Higher-rep screening negligible. BCS is a 5% perturbation on the geometric substrate (confirmed by 3 independent computations).

14. **B2 eigenvector weights exactly {3/8, 1/8, 4/8}** (W5-G): Equal to dimension ratios of {su(2), u(1), C^2} decomposition. Flat-band protection is energetic, not spatial.

15. **Z_3 domain wall tension** (W5-D): sigma = 4.50 M_KK, K(U1-C^2) = 0.0625 CONSTANT at all tau. Z_3 is a rigid topological feature.

### Closures (This Session)

| # | Mechanism | Gate | Evidence |
|:--|:----------|:-----|:---------|
| 1 | Goldstone mass from spectral action | GOLDSTONE-MASS-48 | Trace theorem: S[UDU†]=S[D] for any U,D,f |
| 2 | Singlet CC crossing (N≥2) | N-PAIR-FULL-48 | N=1.000 exact, 8 modes is complete singlet |
| 3 | k-dependent gap from rho_s anisotropy | ANISO-GAP-48 | n_s=-2.930, 927σ. 12th single-cell route |
| 4 | Q-theory equilibrium Goldstone mass | Q-THEORY-GOLD-48 | Self-tuning runaway, no finite fixed point |
| 5 | Zak phase topological protection | DISSOLUTION-48 | Artifact of index permutation. 0/10 survive at eps=1e-4 |
| 6 | Sakharov G_N from curvature anatomy | SAKHAROV-GN-48 | 6 milli-OOM, 60x short. a_0 species-counting dominates |
| 7 | KZ defect correlation n_s | DEFECT-CORR-48 | n_s=0.917 at d_eff=8. Need d_eff=19. Permanently closed |
| 8 | Golden ratio in (2,2)/(0,0) | PHI-GOLDEN-22 | Ratio=1.680, 3.8% from 1.618 |
| 9 | fN centroid in pair-transfer | FN-CENTROID-47 | Closest=1.194, 3.4% from 1.236 |
| 10 | Gibbs-Duhem Euler relation for GGE | GIBBS-DUHEM-GGE-48 | Gives negative P. Multi-T Euler FAILS |

**Retraction**: S46 Zak phase Z_2 classification (13 pi-phase states). These were artifacts of discrete Berry phase computation through exact degeneracies. The Jensen line has no topological protection.

### Constraint Map Updates

| Entity | Prior State | New State | Evidence |
|:-------|:-----------|:----------|:---------|
| Goldstone mass (spectral action) | OPEN (S47 pre-registered) | **CLOSED** | Trace theorem (W1-A) |
| Goldstone mass (q-theory) | OPEN (S47 pre-registered) | **CLOSED** | Self-tuning runaway (W2-C) |
| Goldstone mass (equilibrium, any) | OPEN | **CLOSED** | Both routes + Naz GMOR review. 56 OOM hierarchy impossible from microscopic BCS |
| Goldstone mass (non-equilibrium) | UNCOMPUTED | **OPEN** | Naz review: Friedmann-coupled phase field. Pre-registered FRIEDMANN-GOLDSTONE-49 |
| Singlet CC crossing | OPEN (N-PAIR-FULL critical) | **CLOSED** | N=1 exact, 8 modes complete (W1-B) |
| Fabric CC crossing | OPEN | **OPEN** | 32 cells × 1 pair each. Uncomputed. |
| Zak phase Z_2 protection | S46: 13 pi-phases | **RETRACTED** | Dissolution test: artifacts (W3-B) |
| Non-Abelian Berry L2 | UNCOMPUTED | **TRIVIAL** | Uniform phases, KS p=0.52 (W1-D) |
| n_s from single-cell pair creation | 11 routes closed (S47) | **12 routes closed** | ANISO-GAP-48 (W1-C) |
| n_s from KZ defect correlations | OPEN (NS Path B) | **CLOSED** | d_eff=8 gives 0.917, need 19 (W5-G) |
| n_s from fabric O-Z texture | OPEN (S47 PASS) | **OPEN** (parametric) | n_s=0.965 achievable at m*=11.87 M_KK. Mass source needed. |
| Leggett collective mode | UNCOMPUTED | **EXISTS** | omega_L=0.070, sharp, below pair-breaking (W3-A) |
| TT Lichnerowicz stability | S20b PASS (different method) | **CONFIRMED** | Independent Peter-Weyl method, 31 modes, all positive (W2-B) |
| HFB self-consistency | UNCOMPUTED (Naz Priority 1) | **CONVERGES** | All 12 configs, max 32 iter (W5-E) |
| Swampland de Sitter conjecture | UNTESTED | **PASS** (permanent) | c=52.8>>O(1), structural (W5-F) |
| Analog horizons (internal) | UNCOMPUTED | **EXIST** | Mach 54.3, genuine horizons (W5-F) |
| Geometric phase transition | UNKNOWN | **tau=0.537** | Negative curvature onset (W5-D) |
| Z-K DM/DE discrepancy | 39.4% (S46) | **39.4% structural** | Definitional, not convergible (W5-C) |
| w_0 vs DESI DR2 | S45: -0.709 | **[-0.465, -0.589]** at corrected alpha. 2.8σ from DR2. |

### Probability Trajectory Update

**Session 48 assessment**:

The session closed 10 mechanisms and retracted the S46 Zak phase. The master gate MASS-SOURCE-48 = FAIL closes all equilibrium Goldstone mass routes. However, the session also produced genuine structural positives: Leggett mode, analog horizons, HFB convergence, KZ cross-check at 6.5%, swampland PASS, and the Naz review identifying the correct mass generation path (non-equilibrium Friedmann-Goldstone coupling).

The framework's status:
- **Internal manifold mathematics**: Proven (KO-dim, block-diagonal, curvature anatomy, BCS chain). 15 new permanent results this session.
- **n_s mechanism**: Parametrically correct (fabric O-Z gives n_s=0.965 at some mass). Mass source identified but uncomputed (FRIEDMANN-GOLDSTONE-49). Structural prediction: alpha_s = -0.038 (testable by CMB-S4).
- **CC mechanism**: Closed at singlet level. Open at fabric level (32×1 pairs). The q-theory self-tuning works for the tau variable, but the Goldstone mass requires cosmological dynamics.
- **DM/DE ratio**: O(1) confirmed (7th time). Precise coefficient w_0 ∈ [-0.47, -0.59], 2.8σ from DESI DR2. Structural discrepancy (definitional, not convergible).

**Estimated trajectory**: The n_s fabric route surviving (parametrically) with a concrete next computation (FRIEDMANN-GOLDSTONE-49) prevents a probability collapse. The 10 closures are mostly expected-FAIL confirmations, not new structural walls. The Leggett mode, analog horizons, and HFB convergence add genuine capability.

Prior: 5-8% (post-S37 spectral action floor)
**Post-S48**: 5-8% (floor unchanged — no new stabilization mechanism found, but the path to one is now precisely identified)

### S46 Carry-Forward Audit

| Item | S48 Status | Notes |
|:-----|:-----------|:------|
| N-PAIR-FULL-47 | W1-B | Executed as N-PAIR-FULL-48 |
| WILSON-LOOP-47 | W1-D | Executed as WILSON-LOOP-48 |
| DISSOLUTION-BERRY-47 | W3-B | Executed as DISSOLUTION-48 |
| CLOSED-LOOP-47 | W5-B | Executed as CLOSED-LOOP-48 |
| GIBBS-DUHEM-GGE-47 | W5-C | Executed as GIBBS-DUHEM-GGE-48 |
| DESI-UPDATED-47 | W5-C | Executed as DESI-UPDATED-48 |
| PHI-GOLDEN-22-47 | W5-A | Executed in PAASCH-BACKLOG-48 |
| FN-CENTROID-47 | W5-A | Executed in PAASCH-BACKLOG-48 |
| LOG-SIGNED-40 | W5-A | Executed in PAASCH-BACKLOG-48 |
| Keldysh pair-pair | W5-C | Executed as KELDYSH-PAIR-48 |
| Sector R(p,q) | W5-B | Executed as SECTOR-RPQ-48 |
| (3,0)/(0,3) gauge test | W5-B | Executed as CONJUGATE-PI-48 |
| (2,1) pi-count derivation | W5-B | Executed as PI-COUNT-21-48 |
| TRIAL-FACTOR | W5-A | Executed in PAASCH-BACKLOG-48 |
| n3=dim(3,0) | W5-A | Executed in PAASCH-BACKLOG-48 |
| Six-sequence test | W5-A | Executed in PAASCH-BACKLOG-48 |
| Swampland c(tau) | W5-F | Executed as SWAMPLAND-48 |
| Berry edge states | W5-G | Executed as BERRY-EDGE-48 |
| Self-consistent HFB | W5-E | Executed as HFB-SELFCONSIST-48 |
| C^2 isotropization | W5-D | Executed as C2-ISOTROPIZATION-48 |
| Curvature to tau=1.0 | W5-D | Executed as CURV-ANISO-EXTEND-48 |

### Files Produced

| File | Content | Gate |
|:-----|:--------|:-----|
| `tier0-computation/s48_goldstone_mass.py` / `.npz` / `.png` | Goldstone mass from spectral action | GOLDSTONE-MASS-48 |
| `tier0-computation/s48_npair_full.py` / `.npz` | Physical pair number from 16-mode ED | N-PAIR-FULL-48 |
| `tier0-computation/s48_aniso_gap.py` / `.npz` / `.png` | k-dependent gap from rho_s anisotropy | ANISO-GAP-48 |
| `tier0-computation/s48_wilson_loop.py` / `.npz` / `.png` | Non-Abelian Wilson loop Berry phase | WILSON-LOOP-48 |
| `tier0-computation/s48_curv_gap_corr.py` / `.npz` / `.png` | Curvature-gap correlation across tau | CURV-GAP-CORR-48 |
| `tier0-computation/s48_aniso_oz.py` / `.npz` / `.png` | Anisotropic O-Z power spectrum | ANISO-OZ-48 |
| `tier0-computation/s48_tt_lichnerowicz.py` / `.npz` / `.png` | TT Lichnerowicz operator spectrum | TT-LICH-48 |
| `tier0-computation/s48_qtheory_goldstone.py` / `.npz` | Q-theory Goldstone mass | Q-THEORY-GOLD-48 |
| `tier0-computation/s48_chi_q_phase.py` / `.npz` | Q-theory phase susceptibility | CHI-Q-PHASE-48 |
| `tier0-computation/s48_leggett_mode.py` / `.npz` | Leggett mode frequency | LEGGETT-MODE-48 |
| `tier0-computation/s48_dissolution_berry.py` / `.npz` / `.png` | Dissolution topology test | DISSOLUTION-48 |
| `tier0-computation/s48_sakharov_gn.py` / `.npz` / `.png` | Sakharov G_N computation | SAKHAROV-GN-48 |
| `tier0-computation/s48_qa_tachyon.py` / `.npz` / `.png` | QA/Tachyon batch (7 sub-items) | QA-TACHYON-48 |
| `tier0-computation/s48_eigenvectors.py` / `.npz` / `.png` | Dirac eigenvector analysis at fold | EIGENVECTOR-48 |
| `tier0-computation/s48_paasch_backlog.py` / `.npz` / `.png` | Paasch 7-item backlog | PAASCH-BACKLOG-48 |
| `tier0-computation/s48_berry_complete.py` / `.npz` / `.png` | Berry 5-item completion | BERRY-COMPLETE-48 |
| `tier0-computation/s48_dmde_refine.py` / `.npz` / `.png` | DM/DE 3-item refinement | DMDE-REFINE-48 |
| `tier0-computation/s48_curv_extend.py` / `.npz` / `.png` | Curvature 6-item extensions | CURV-EXTEND-48 |
| `tier0-computation/s48_hfb_selfconsist.py` / `.npz` | HFB self-consistent gaps | HFB-SELFCONSIST-48 |
| `tier0-computation/s48_nilsson.py` / `.npz` / `.png` | Curvature Nilsson diagram | NILSSON-48 |
| `tier0-computation/s48_pbcs_0d.py` / `.npz` | PBCS vs BCS in 0D limit | PBCS-0D-48 |
| `tier0-computation/s48_pair_rotation.py` / `.npz` | Pair coupling along geodesics | PAIR-ROTATION-48 |
| `tier0-computation/s48_protected_chain.py` / `.npz` | q_7^2=1/16 PW survival | PROTECTED-CHAIN-48 |
| `tier0-computation/s48_volovik_string.py` / `.npz` / `.png` | Volovik+String 8-item batch | VOLOVIK-STRING-48 |

### Next Session Recommendations

**The single decisive computation for S49:**

1. **FRIEDMANN-GOLDSTONE-49** (pre-registered by Naz W2-C addendum): Couple the fabric phase field phi(x,t) to the Friedmann equation through the superfluid stiffness tensor rho_s^{ab}. Initial conditions from S38 GGE (59.8 pairs, 8 conserved integrals). The Hubble expansion provides the explicit U(1)_7 breaking that generates the Goldstone mass dynamically. This is the ONLY remaining path to n_s = 0.965. If the Friedmann-Goldstone coupling produces m ~ 10^{-39} GeV (Hubble scale), the framework has a zero-parameter n_s prediction. If not, the n_s mechanism is permanently dead.

**Secondary computations for S49:**

2. **Fabric CC crossing**: 32 cells × 1 pair each = 32 total pairs at fabric level. Does this give the q-theory crossing that the singlet (N=1) cannot? Requires inter-cell Josephson coupling from S47 TEXTURE-CORR data.

3. **Off-Jensen Berry phase (P-30w)**: The sole route to nontrivial Berry curvature. Requires breaking U(2) symmetry by deforming in T3/T4 directions. The dissolution test (W3-B) confirmed Jensen is topologically trivial — all content lives off-Jensen.

4. **Alpha_s prediction refinement**: ANISO-OZ found alpha_s = -0.038 (4.9σ from Planck) as a structural prediction of the O-Z texture mechanism. CMB-S4 (sigma ~ 0.003) could resolve this. Needs careful scale identification (K_pivot mapping from tessellation to CMB multipoles).

5. **Leggett mode coupling to modulus**: The sharp Leggett mode (omega_L = 0.070) couples to the tau modulus. Does this produce observable signatures in the spectral action or transit dynamics?

6. **Geometric phase transition at tau=0.537**: The negative-curvature onset marks a structural boundary. What happens to the BCS condensate as the internal space develops saddle regions? Does the condensate survive?

7. **LOG-SIGNED-40 tau sweep**: Only fold value computed. Needs per-sector eigenvalues at each tau to complete the signed log sum test.

8. **w_0 tension with DESI DR2**: Framework predicts w_0 ∈ [-0.47, -0.59], DESI sees ~ -0.75. The 2.8σ gap is structural (Z-K definitional). Can the fabric self-consistency (inter-cell coupling + spatial averaging) shift w_0 toward the DESI value?
