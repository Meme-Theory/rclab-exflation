# Session 31Ca Synthesis: Nuclear Structure Methods, Foam Diagnostics, and the Shape of What Remains

**Date**: 2026-03-02
**Sub-session**: 31Ca (Nazarewicz Nuclear Structure Computations + Quantum Foam Diagnostics)
**Agents**: naz (nazarewicz-nuclear-structure-theorist), bap (baptista-spacetime-analyst), sim (phonon-exflation-sim), coord (coordinator)
**Document type**: Definitive sub-session record -- 12 gate verdicts, 12 computations, 1 nuclear DFT review
**Source plan**: `sessions/session-plan/session-31Ca-prompt.md` (v.3: 9 nuclear structure + 3 foam diagnostics)
**Prerequisites**: Sessions 31Aa (adversarial review), 31Ba (K-1, I-1, B-31nck)
**Motivation**: Nazarewicz's collaborative review of Sessions 31Aa and 31Ba identified nine computable proposals importing nuclear many-body methodology (density-dependent pairing, BCS convergence, Kapitza-BCS interference, Bayesian NCG-KK, GCM configuration mixing, odd-even staggering, self-consistent cranking, instanton-driven effective frequency, Bayesian three-fold convergence) plus three quantum foam diagnostics (spectral dimension, domain-boundary phase shift, holographic DOF count). All use existing .npz archives. No new eigenvalue computations.

---

## I. Executive Summary

Session 31Ca applied six decades of nuclear DFT methodology to the SU(3) Dirac spectrum's pairing landscape -- the most systematic test of whether the K-1e BCS obstruction (Session 23a) is a truncation artifact or a structural feature. The answer is unambiguous: **the obstruction is structural**. All nine nuclear structure gates returned negative results. The two decisive gates (N-31Cc-G: BCS-Kapitza interference; N-31Ch-G: instanton-driven effective frequency) both returned negative. The sole conditional pass came from the foam domain-boundary phase shift (F-2-G), establishing that the Planck popcorn picture survives Perlman observational bounds at a physically reasonable coherence scale.

### Gate Verdicts Dashboard

| # | Gate | Type | Verdict | Key Number |
|:--|:-----|:-----|:--------|:-----------|
| 1 | N-31Ca-G | Structural | **FAIL** | M_max <= 0.275 (3.6x below threshold) |
| 2 | N-31Cb-G | Structural | **FAIL** | M_inf = 0.110 (10x below threshold) |
| 3 | N-31Cc-G | DECISIVE | **DOES NOT FIRE** | M_max = 0.117 (8.6x below threshold) |
| 4 | N-31Cd-G | Assessment | **INCONCLUSIVE** | D_KL = 0.23 nats, BF = 0.163 |
| 5 | N-31Ce-G | Structural | **FAIL** | <sin^2_tw> = 0.086 (650x worse than grid) |
| 6 | N-31Cf-G | Diagnostic | **FEATURELESS** | No gap-edge features |
| 7 | N-31Cg-G | Structural | **FAIL** | 0 fixed points, V concave |
| 8 | N-31Ch-G | DECISIVE | **FAIL** | delta_crit does not exist |
| 9 | N-31Ci-G | Assessment | **NO SIGNAL** | BF = 2.28 (threshold: 10) |
| 10 | F-1-G | Diagnostic | **NO CDT CONNECTION** | d_s ~ 6.5 (Weyl), not ~2 |
| 11 | F-2-G | Structural | **PASS (CONDITIONAL)** | l_coh_crit = 5.3e13 l_P |
| 12 | F-3-G | Diagnostic | **INFORMATIVE** | alpha = 4.01 at tau=0.18 |

**Aggregate**: 0 unconditional PASS, 1 conditional PASS, 5 FAIL, 2 DOES NOT FIRE, 1 FEATURELESS, 1 NO SIGNAL, 1 INCONCLUSIVE, 1 INFORMATIVE.

### Key Numbers Summary

| Computation | Central Result | Implication |
|:------------|:--------------|:------------|
| Density-dep pairing | Enhancement ratio = 1.000 | V_matrix already gap-edge concentrated |
| BCS convergence | Truncation error < 3% | N_max=6 is sufficient; K-1e is converged |
| BCS-Kapitza | Enhancement 0.5% avg | Kapitza cannot bridge factor-7 gap |
| Bayesian NCG-KK | D_KL = 0.23 nats | B-31nck is real but statistically soft |
| GCM moduli | PR/N = 0.002 | Wave function at wrong minimum |
| Odd-even stagger | S(tau) peaks at 0.50 | No pairing structure at tau~0.18 |
| Cranking | d^2V/dtau^2 = -0.54 | V concave at preferred tau |
| Instanton freq | delta_crit = DNE | No Kapitza minimum at any frequency |
| Bayesian 3-fold | BF = 2.28 | Convergence narrative not supported |
| Spectral dim | d_s = 6.5 | Standard Weyl, no CDT flow |
| Domain phase | l_coh = 5.3e13 l_P | Sub-nuclear threshold, reasonable |
| Holographic DOF | alpha = 4.01 | Intermediate, Jensen reduces alpha |

---

## II. Per-Computation Results

### II.1 N-31Ca: Density-Dependent Pairing on SU(3)

**Agent**: naz. **Gate**: N-31Ca-G = **FAIL**.

**Result**: 11 envelope functions (4 exponential alpha in {1,2,5,10}, 3 Gaussian beta in {1,5,10}, 4 hard-window x_cut in {1.5,2,3,5}) tested at 9 tau values x 6 mu values each. All envelopes give max|eig(V_eff)| <= 0.275 at every tau. At tau=0.20 (three-fold convergence region): constant coupling max|eig(V)| = 0.173; best density-dependent envelope: 0.173 (identical). Hard-window at x_cut >= 1.5 passes all 16 modes (all have |lambda|/lambda_min < 1.43). Exponential and Gaussian cutoffs REDUCE pairing by down-weighting legitimate modes. mu_crit = inf at all tau for all envelopes.

**Gate classification**: FAIL. mu_crit >= 0.95*lambda_min for ALL envelopes at ALL tau. No density-dependent coupling produces condensation within the gap.

**Physical interpretation**: The nuclear surface/volume pairing distinction (Nazarewicz Paper 02) requires a large separation between gap-edge modes and bulk modes. On SU(3), the 16 singlet-sector modes span |lambda|/lambda_min in [1.0, 1.43] -- too compressed for any envelope to discriminate. The V_matrix is already a "surface" object. The enhancement mechanism that works in nuclei near drip lines (concentrating pairing at the Fermi surface by removing deep-hole/high-particle contributions) has nothing to concentrate here.

**Self-consistency loop**: This computation establishes that the BCS obstruction is not a coupling-distribution problem. The obstacle is absolute scale: ||V|| ~ 0.1-0.28, structurally insufficient regardless of how the coupling is distributed among modes.

**Files**: `tier0-computation/s31Ca_density_dep_pairing.{py,npz,png}`

---

### II.2 N-31Cb: BCS Convergence with Truncation Level

**Agent**: naz. **Gate**: N-31Cb-G = **FAIL**.

**Result**: M_max(mu=0) computed at N_eff = {2, 10, 16} (modes from representations with p+q <= N_max_eff). Using constant coupling (per N-31Ca-G FAIL). At all tau: monotonically increasing with N_eff (first condition met). Convergence rapidly decelerating: (M_16-M_10)/(M_10-M_2) = 0.013-0.098. Extrapolated M_inf at tau=0.20: 0.110 (10x below threshold). max|eig(V)| converges to 0.16-0.28; V_10 to V_16 increment only 1-3%.

**Critical finding**: At N_eff=2, M_max = 0 for all tau > 0. The two gap-edge modes have ZERO pairing in isolation: V(gap,gap) = 0 exactly (selection rule, confirmed independently of Session 23a). All pairing comes from intermediate modes (N=3-16).

**Gate classification**: FAIL. M_max monotonically increases (first condition met) but M_inf = 0.110 << 0.5 (second condition fails).

**Physical interpretation**: The Berggren contour analog (Papers 02, 03): truncation at N_max=6 captures >97% of the pairing. The SU(3) spectrum behaves like a doubly-magic nucleus (e.g., 208-Pb): the spectral gap is so large relative to the pairing force that superfluidity cannot develop regardless of basis size. The truncation is NOT the problem -- the physics is converged.

**Truncation error bar**: This result provides the definitive truncation error estimate for ALL BCS-based computations in the project: < 3% at N_max=6. The K-1e result (M_max = 0.077-0.149) is robust.

**Files**: `tier0-computation/s31Cb_bcs_convergence.{py,npz,png}`

---

### II.3 N-31Cc: BCS-Kapitza Interference Diagnostic

**Agent**: sim. **Gate**: N-31Cc-G = **DOES NOT FIRE** (DECISIVE).

**Result**: For orbit centers tau_0 in {0.15, 0.18, 0.21} and amplitudes A in {0.02, 0.05, 0.08}: best time-averaged enhancement <M>/M_static = 1.005 (need >1.2). Best peak M_max(mu=0) over orbit: 0.117 (need >1.0, actual is 8.6x below). T3 and instanton frequencies produce identical M_max profiles (M_max depends on tau only, not frequency). Enhancement: 0.5% average, 10.9% peak.

At mu=+lambda_min (diagnostic): M_max = 7.7-15.0 (always above threshold), confirming the obstruction is Wall 3 (spectral gap requiring mu > 0).

**Gate classification**: DOES NOT FIRE. Neither condition met (time-averaged M_max does not exceed 1.2*static; peak M_max does not reach 1.0).

**Physical interpretation**: Nuclear Coriolis anti-pairing analog (Paper 08): trying to induce backbending in 208-Pb by cranking it. The problem is not the cranking frequency -- there is no superfluid to destroy. Backbending requires a preexisting condensate (Delta > 0). On SU(3) at mu=0, Delta = 0 identically. The Kapitza oscillation modulates a quantity (M_max ~ 0.08-0.15) that is structurally subcritical everywhere in the tau domain.

**Self-consistency loop**: The Kapitza-BCS link is structurally blocked at mu=0. The loop cannot close through BCS unless an external mechanism provides mu > 0.

**Files**: `tier0-computation/s31Cc_bcs_kapitza.{py,npz,png}`

---

### II.4 N-31Cd: Bayesian NCG-KK Scale Tension Assessment

**Agent**: bap. **Gate**: N-31Cd-G = **INCONCLUSIVE**.

**Result**: Lambda_SA = 1.02e22 GeV at tau=0.21. At reference sigma=3: BF = 0.163, D_KL = 0.23 nats. Neither threshold met (D_KL < 1 nat, BF > 0.01). At sigma=1 (tightest tolerance): BF = 1.9e-5, D_KL = 1.88 nats (both thresholds met). Posterior mode: log10(M_KK) = 18.0 (upper prior boundary). SM unification scale 10^13 GeV sits 9 decades below Lambda_SA.

**Gate classification**: INCONCLUSIVE at reference tolerance. The B-31nck FAIL (Lambda_SA/M_KK = 10^6) is physically decisive but statistically soft under the log-uniform prior [10^14, 10^18] because the prior doesn't reach the likelihood peak at 10^22.

**Physical interpretation**: The Skyrme fitting paradox (Paper 06): when theoretical model error dominates, individual measurements provide weak Bayesian evidence. The NCG-KK tension is real (the ratio is 10^6), but the information content is diluted by the generous prior and tolerance. A more informative prior centered on the GUT scale would yield BF << 0.01.

**Files**: `tier0-computation/s31Cd_bayesian_ncgkk.{py,npz,png}`

---

### II.5 N-31Ce: GCM Configuration Mixing for Moduli Space

**Agent**: bap. **Gate**: N-31Ce-G = **FAIL**.

**Result**: Hill-Wheeler equation on 441-point grid (21x21, tau x eps). Norm kernel N_ij = exp(-d_ij^2/(2*sigma^2)). Ground state f_0 strongly localized at V_total minimum: (tau, eps) = (0.60, 0.15). PR/N = 0.002 (localized). <sin^2_tw>_GCM = 0.086 (|diff from SM| = 0.145; 650x worse than best grid point 0.2308). <phi_30>_GCM = 1.288 (far from 1.532). Excitation gap E_1 - E_0 = 0.025. FAIL at all sigma values (0.5x, 1x, 2x default). Jensen-only GCM also fails: <sin^2_tw> = 0.083, PR = 1.04/21.

**Gate classification**: FAIL. <sin^2_tw>_GCM = 0.086 is farther from 0.231 than the best single grid point (0.2308). Quantum averaging degrades SM agreement.

**Physical interpretation**: Anti-shape-coexistence. In superheavy nuclei (Paper 10, 13), GCM delocalization occurs when the PES is flat (competing shapes within 0.5-2 MeV). Here, V_total has a 2-unit range across the grid -- enough structure to localize the wave function at the classical minimum. But that minimum (tau=0.60, eps=0.15) is the WRONG geometry for SM physics. The GCM correctly finds the lowest-energy configuration; the problem is the landscape, not the method.

**Self-consistency loop**: The GCM ground state at tau=0.60 is incompatible with the three-fold convergence at tau~0.18. The self-consistency loop requires a mechanism to PREVENT the modulus from rolling to large tau. GCM does not provide this mechanism; it confirms the modulus prefers large tau.

**Files**: `tier0-computation/s31Ce_gcm_moduli.{py,npz,png}`

---

### II.6 N-31Cf: Odd-Even Staggering Diagnostic

**Agent**: naz. **Gate**: N-31Cf-G = **FEATURELESS**.

**Result**: Delta^(3)(N,tau) = (-1)^N*[lambda_{N+1} - 2*lambda_N + lambda_{N-1}]/2 computed for N=1,...,14 at 9 tau values. Gap edge at N=0 (boundary condition). max|Delta^(3)| = 0.05-0.17 at N~10 (deep in spectrum), monotonically increasing with tau. No sharp features at gap edge. Integrated staggering S(tau) = sum_N |Delta^(3)(N)| peaks at tau=0.50, not in the [0.15, 0.25] window.

**Gate classification**: FEATURELESS. No sharp Delta^(3) peak or sign change at the gap edge in the preferred tau range.

**Physical interpretation**: The nuclear odd-even mass staggering (Paper 03) shows sharp features at magic numbers where the pairing gap drops to zero. The SU(3) spectrum shows no such features -- the eigenvalue spacing is smooth and regular. In nuclear terms, this is a deformed nucleus in the middle of a shell with uniformly spaced Nilsson levels: no sub-shell closures, no enhanced pairing at specific mode numbers.

**Files**: `tier0-computation/s31Cf_odd_even_stagger.{py,npz,png}`

---

### II.7 N-31Cg: Self-Consistent Cranking Check

**Agent**: bap. **Gate**: N-31Cg-G = **FAIL**.

**Result**: omega_out vs omega_in computed across omega^2 in [0.5, 12.0]. V_Jensen curvature at tau=0.18: d^2V/dtau^2 = -0.54 (CONCAVE -- imaginary effective frequency). Maximum omega_out/omega_in = 4.5 (overshoots diagonal but no fixed-point crossing). Zero self-consistent solutions.

**Gate classification**: FAIL. No self-consistent cranking fixed point at any omega^2 in [0.5, 12.0].

**Physical interpretation**: In cranked HFB (Paper 08), self-consistency requires omega and J to satisfy omega = dE/dJ simultaneously. On SU(3), the V_Jensen potential is concave at tau=0.18, meaning the "restoring force" has the wrong sign. The Kapitza ponderomotive mechanism requires a convex potential to create a well; it cannot function on a concave landscape. This is structural: the curvature sign is set by the Seeley-DeWitt coefficients, which are monotone (Wall 4).

**Files**: `tier0-computation/s31Cg_selfconsistent_cranking.{py,npz,png}`

---

### II.8 N-31Ch: Instanton-Driven Effective Frequency

**Agent**: bap. **Gate**: N-31Ch-G = **FAIL** (DECISIVE).

**Result**: V_Kapitza(tau; A=0.08, omega_eff) evaluated at omega_eff^2 = T3 - delta for delta in linspace(0, 5, 21). omega_eff^2 reduced from 8.326 to 3.326. No interior V_Kapitza minimum at ANY delta. delta_crit does not exist. Gamma_inst^2 values at tau~0.18 range up to 51 (at coupling ratio r=0.1), but this is irrelevant -- the V_Jensen shape fundamentally prevents Kapitza minimum formation at any frequency.

**Gate classification**: FAIL. delta_crit does not exist, so the condition delta_crit <= Gamma_inst^2 cannot be satisfied.

**Physical interpretation**: The instanton "backbending" hypothesis: does the instanton gas provide a frequency soft enough for the K-1 extended scan to find a Kapitza minimum? The answer is that the problem is not frequency but curvature sign. V_Jensen is concave at tau=0.18 (N-31Cg confirms d^2V/dtau^2 = -0.54). No amount of frequency softening creates a minimum in a concave potential. The Kapitza formula V_Kapitza = <V> + (1/4*omega^2)*<(dV/deps)^2> adds a positive-definite correction, but this correction is too small (0.27 max, vs V_total range 1.76) to overcome the bare descent.

**Self-consistency loop**: The instanton -> mu_eff -> BCS link is blocked. The instanton gas provides energy (S_inst < 0), but this energy cannot create a Kapitza well at tau~0.18 because the landscape is concave there.

**Files**: `tier0-computation/s31Ch_instanton_eff_freq.{py,npz,png}`

---

### II.9 N-31Ci: Bayesian Three-Fold Convergence Quantification

**Agent**: naz. **Gate**: N-31Ci-G = **NO SIGNAL**.

**Result**: BF = 2.28 for signal (three observables converge at same tau) vs null (independent random tau). Below threshold of 10 for INFORMATIVE, below 3 for weak evidence. Three observables peak at: phi_30 deviation at tau~0.15, sin^2_tw deviation at tau~0.09, instanton ratio at tau=0.181. Factor-2 spread. Combined proximity function peaks at tau~0.03. Sensitivity: BF ranges 1.09-2.69 across sigma choices. Corrected from initial BF=2.17 (used raw Gamma instead of ratio Gamma/omega); verdict unchanged.

**Gate classification**: NO SIGNAL. BF = 2.28 consistently below threshold of 10.

**Physical interpretation**: Paper 06 methodology applied rigorously. The "three-fold convergence at tau~0.18" (cited since Session 31Ba as the most structurally suggestive feature) is not confirmed statistically. The three observables are spread over a factor-2 range in tau. Human pattern recognition in low-dimensional projections (three curves on one plot) systematically overestimates correlations. The BF provides the honest answer.

**Files**: `tier0-computation/s31Ci_bayesian_convergence.{py,npz,png}`

---

### II.10 F-1: Heat Kernel Spectral Dimension Over Tau Distribution

**Agent**: sim. **Gate**: F-1-G = **NO CDT CONNECTION**.

**Result**: K(t) = Sum_k exp(-t*lambda_k^2) computed at each tau on the Jensen curve, then averaged over: (a) uniform tau distribution in [0, 0.55] (incoherent popcorn), (b) Gaussian centered on tau=0.18 (coherent), (c) single tau=0.18 (control). d_s(t) = -2*d(ln K)/d(ln t) via finite differences.

UV (small t): d_s -> 0.046 (truncation artifact -- bounded spectrum |lambda| < 4.1 causes K(t) -> const). Mid-range (t ~ 0.3-3): d_s ~ 6.5 (correct Weyl for dim=6). Large t: d_s diverges (near-gap degeneracy). Tau-averaging produces negligible change: incoherent d_s = 6.44 vs single d_s = 6.49 at mid-range.

**Gate classification**: NO CDT CONNECTION. d_s ~ 2 at small t not reproduced. The CDT prediction requires UV physics beyond fixed-truncation Dirac spectra (foliation constraint, Lifshitz scaling, or equivalent).

**Physical interpretation**: The QFoam synthesis (Section III.2) anticipated that d_s ~ 2 is "not automatic" from the popcorn picture. This computation confirms: tau-averaging over random internal geometries does not produce spectral dimension reduction. The framework's internal geometry is spectrally standard (Weyl scaling) at all probed scales. The CDT connection remains a theoretical aspiration, not a computational result.

**Files**: `tier0-computation/s31Ca_foam_spectral_dim.{py,npz,png}`

---

### II.11 F-2: Domain-Boundary Phase Shift Estimate

**Agent**: sim. **Gate**: F-2-G = **PASS (CONDITIONAL)**.

**Result**: For tau_0 = 0.18 and delta_tau in linspace(0.001, 0.05, 20): eigenvalue mismatch delta_k/k = 0.002 at delta_tau = 0.027. Total phase shift per boundary: delta_phi_total = sqrt(sum_k delta_phi_k^2). Cumulative phase fluctuation Delta_L vs Perlman bound (Delta_L < 10^{-15} m at d = 1 Gpc).

l_coh_crit = 5.33e13 l_P = 0.86 fm (sub-nuclear scale). With RMS mismatch: l_coh_crit = 6.2e15 l_P (still sub-nuclear). Popcorn survives Perlman bounds if coherence length exceeds this threshold.

**Gate classification**: PASS (CONDITIONAL). l_coh_crit = 5.3e13 l_P < 10^6 l_P (well within the pass condition). The coherence requirement is physically reasonable -- sub-nuclear scale, far below any cosmological problem.

**Physical interpretation**: The QFoam synthesis (Section III.3) noted that incoherent popcorn (random tau at each Planck cell) predicts random-walk scaling excluded by Perlman at >3 sigma, but the coherence transition saves the model. This computation quantifies the threshold: l_coh > 0.86 fm suffices. This is a weak requirement compared to the cosmologically-large domains feared in the QFoam assessment. The per-boundary phase mismatch is tiny because the SU(3) eigenvalues change smoothly with tau (Lipschitz continuity of D_K eigenvalues). The popcorn's Perlman survival does not constrain the framework significantly.

**Files**: `tier0-computation/s31Ca_foam_domain_phase.{py,npz,png}`

---

### II.12 F-3: Holographic DOF Count on Jensen-Deformed SU(3)

**Agent**: sim. **Gate**: F-3-G = **INFORMATIVE**.

**Result**: N(Lambda) = #{k : |lambda_k| < Lambda} fitted to power law A*Lambda^alpha:
- tau=0.00: alpha = 5.31 (near spinor Weyl on 6D: alpha = dim/2 + spinor correction)
- tau=0.18: alpha = 4.01 (intermediate)
- tau=0.35: alpha = 2.97
- tau=0.50: alpha = 2.47

Jensen deformation induces monotonic decrease in alpha. Not holographic (alpha >> 2/3 Ng prediction) but not pure volume-law either. Cross-reference with F-1: mid-range d_s ~ 6.5 is consistent with alpha ~ 4-5 at tau=0-0.18 (discrepancy reflects different probing regimes -- Weyl counting vs heat kernel).

**Gate classification**: INFORMATIVE. Alpha = 4.01 at tau=0.18 establishes the DOF scaling regime. The internal manifold violates holographic bounds at the Planck scale (alpha >> 2/3), but the Jensen-driven alpha reduction means the violation ameliorates with increasing tau.

**Physical interpretation**: Weyl's law on 6D SU(3) predicts alpha = 3 for scalar modes. The measured alpha = 4-5 at small tau reflects spinor multiplicities (rank(S) = 16) inflating the count. The monotonic decrease of alpha with tau is a novel structural finding: Jensen deformation effectively reduces the dimensionality of the eigenvalue count, even without any quantum gravity mechanism. At tau=0.50, alpha = 2.47, approaching the CDT value alpha_CDT = 2 (for d_s = 4 in 4D). This is suggestive but may be coincidental.

**Files**: `tier0-computation/s31Ca_foam_holo_dof.{py,npz,png}`

---

## III. Cross-Computation Analysis

### III.1 Density-Pairing Chain: N-31Ca -> N-31Cb -> N-31Cc

N-31Ca-G FAIL determined that Tier 2 (N-31Cb, N-31Cc) used constant coupling. Did the coupling choice matter?

**No.** N-31Ca showed that density-dependent reweighting provides exactly zero enhancement (ratio = 1.000). The V_matrix is already gap-edge concentrated. Using constant coupling for Tier 2 was not a restriction -- it was the optimal choice (any reweighting reduces pairing). The entire density-pairing chain returned the same answer at each link: M_max ~ 0.08-0.15 at mu=0, structurally subcritical, converged at N_max=6.

The chain quantifies the K-1e obstruction with increasing precision:
- **K-1e (Session 23a)**: M_max = 0.077-0.149, constant coupling, N_max=6
- **N-31Ca (this session)**: M_max <= 0.275, 11 coupling envelopes, N_max=6
- **N-31Cb (this session)**: M_inf = 0.110, extrapolated to N_max -> infinity
- **N-31Cc (this session)**: M_max = 0.117, time-averaged over Kapitza orbits

Four independent approaches, same conclusion: M_max is 7-13x below threshold at mu=0.

### III.2 GCM vs BCS: N-31Ce vs N-31Ca/N-31Cb

Does quantum averaging of the modulus produce a different pairing landscape?

**Yes, but in the wrong direction.** The GCM ground state localizes at (tau=0.60, eps=0.15), where sin^2_tw = 0.086 and phi_30 = 1.288. At this geometry, the BCS pairing would be evaluated at a different tau than the three-fold convergence point (tau~0.18). The GCM does not help BCS -- it moves the effective tau FURTHER from the SM-compatible region.

The GCM result also reveals a tension with the Kapitza mechanism. The Kapitza orbit assumes the modulus oscillates around a preferred tau_0. But the GCM ground state says the quantum-preferred geometry is at tau=0.60, not tau=0.18. The Kapitza mechanism would need to fight against the quantum potential to maintain orbits at tau~0.18.

### III.3 Information Content: N-31Cd + N-31Ci

The Bayesian gates provide complementary information:
- **N-31Cd** (NCG-KK): BF = 0.163 -- the B-31nck tension is physically real but statistically soft under the generous prior. The information is diluted by the prior volume, not enhanced by it.
- **N-31Ci** (three-fold convergence): BF = 2.28 -- the claimed convergence at tau~0.18 is not statistically significant.

Combined: neither the scale tension nor the convergence claim carries decisive Bayesian weight. The framework's most positive-seeming feature (three-fold convergence) and its most negative-seeming feature (NCG-KK incompatibility) are both statistically modest. This is the Paper 06 lesson: narrative coherence is not evidence.

### III.4 Convergence Assessment: Truncation Error Bar

N-31Cb provides the definitive truncation error bar for all BCS-based computations:

| N_max | % of converged M_max captured | Source |
|:------|:------------------------------|:-------|
| 2 (gap-edge only) | 0% (V(gap,gap) = 0) | N-31Cb |
| 6 (Session 23a) | > 97% | N-31Cb |
| 10 | > 99% | N-31Cb |
| infinity (extrapolated) | 100% (M_inf = 0.110) | N-31Cb |

This error bar applies to: K-1e (Session 23a), N-31Ca (this session), N-31Cc (this session), and all future BCS computations at mu=0 on the SU(3) singlet sector. The truncation is not the bottleneck. The physics is converged.

### III.5 Kapitza Mechanism Assessment: N-31Cg + N-31Ch + N-31Cc

Three independent tests of the Kapitza stabilization channel, all negative:

| Test | Result | Reason for Failure |
|:-----|:-------|:------------------|
| N-31Cg (cranking) | No fixed points | V concave (d^2V/dtau^2 = -0.54) at tau=0.18 |
| N-31Ch (instanton freq) | delta_crit DNE | No Kapitza minimum at any reduced frequency |
| N-31Cc (BCS-Kapitza) | M_max 8.6x below | Kapitza cannot bridge factor-7 structural gap |

The Kapitza mechanism is constrained on three fronts: (1) the potential curvature has the wrong sign for self-consistent oscillation, (2) the instanton frequency softening cannot create a minimum in a concave landscape, and (3) even if the orbit existed, the BCS gap would remain subcritical by a factor of 7. These are independent obstructions. The Kapitza channel survives only if the full 5D Hessian (not yet computed) has a soft mode with omega^2 < 5 AND the landscape is convex in that direction.

---

## IV. Nazarewicz Nuclear DFT Review

The nuclear DFT interpretation (Nazarewicz, full review received after all 12 computations):

### IV.1 N-31Ca vs Nuclear Surface/Volume Pairing (Paper 02)

The nuclear surface pairing enhancement works because nuclei have a clear bulk/surface separation: states deep below the Fermi energy contribute to the pairing integral but dilute Cooper pair coherence. Suppressing bulk contributions via density-dependent coupling (G -> G*(1 - eta*rho)) concentrates pairing at the nuclear surface where level density peaks, improving odd-even mass staggering by 20-40%.

On SU(3), this separation does not exist. The 16 singlet modes span |lambda|/lambda_min in [1.0, 1.43] -- all modes are "surface" modes. There is no bulk to suppress. The nuclear enhancement mechanism requires a range of mode energies spanning several lambda_min; on SU(3), the range is less than half of lambda_min.

### IV.2 N-31Cb vs Berggren Continuum Completeness (Papers 02, 03)

The fast convergence (< 3% truncation error at N_max=6) is the signature of a system far from the "drip line." In nuclear physics, continuum coupling matters for weakly-bound nuclei near the neutron drip line, where the last occupied states scatter into the continuum. The SU(3) spectral gap (2*lambda_min = 1.644) is analogous to a deeply-bound nucleus where continuum effects are negligible. The Berggren contour has nothing to add.

The V(gap,gap) = 0 selection rule is analogous to vanishing two-body matrix elements between spin-orbit partners in specific coupling schemes. This is structural, not numerical.

### IV.3 N-31Cc vs Coriolis Anti-Pairing (Paper 08)

Nuclear backbending requires a preexisting superfluid condensate that the Coriolis force can disrupt. The Mottelson-Valatin formula Delta(omega) = Delta_0*sqrt(1 - (omega/omega_c)^2) starts from Delta_0 > 0. On SU(3) at mu=0, Delta = 0 identically. Attempting to induce backbending in the SU(3) "nucleus" at mu=0 is like trying to induce backbending in doubly-magic 208-Pb -- there is no superfluid to destroy.

### IV.4 N-31Cd vs Skyrme Fitting Paradox (Paper 06)

The BF = 0.163 reflects the Paper 06 lesson: when theoretical model uncertainty (here: the prior width) dominates, individual measurements produce weak Bayesian evidence. The NCG-KK tension is physically devastating (10^6 ratio) but statistically soft under the chosen prior. This is not a failure of the computation -- it is a correct application of Bayesian methodology to a problem where the prior choice matters as much as the data.

### IV.5 N-31Ce vs Shape Coexistence (Papers 10, 13)

In superheavy nuclei, GCM delocalization occurs when the PES is flat (competing shapes within 0.5-2 MeV). The SU(3) V_total has a 2-unit range -- too structured for delocalization. The GCM correctly finds the lowest-energy configuration, but that configuration is at the wrong tau for SM physics. This is the opposite of nuclear shape coexistence: not multiple competing shapes, but a single dominant minimum at the wrong geometry.

### IV.6 N-31Cf vs Nuclear Mass Staggering (Paper 03)

A featureless Delta^(3) means the eigenvalue spacing is smooth and regular -- no magic numbers or shell closures within the 16-mode spectrum. In nuclear terms: a deformed nucleus mid-shell with uniformly spaced Nilsson levels.

### IV.7 Overall Assessment

**All six nuclear structure methods reinforce K-1e.** The SU(3) spectrum at mu=0 behaves like a doubly-magic nucleus: large gap, small pairing, featureless level density near the gap edge. The BCS channel at mu=0 is constrained by 6 independent computations (K-1e + 4 nuclear reinforcements + V(gap,gap) selection rule). The remaining escape route is finite-density (mu > 0) physics requiring a mechanism to generate mu.

---

## V. Quantum Foam Interface Assessment

### V.1 F-1 Spectral Dimension: No CDT Connection

The internal geometry of SU(3) produces standard Weyl spectral dimension (d_s ~ 6.5) at all scales above the gap. Tau-averaging (incoherent popcorn) produces negligible change (delta d_s ~ 0.05). The CDT universal prediction d_s -> 2 at the Planck scale is NOT reproduced.

This result was anticipated by the QFoam synthesis (Section III.2): "d_s ~ 2 is not automatic from the popcorn picture -- it requires a specific dynamical mechanism." The computation confirms this assessment. The CDT connection remains theoretical aspiration, not computational result. The spectral dimension flow, if it exists in this framework, must come from physics not captured by averaging D_K eigenvalues over a tau distribution -- likely from the coupling between internal and external geometry (the M^4 x SU(3) Wheeler-DeWitt equation), which has not been computed.

### V.2 F-2 Domain-Boundary Constraint: Perlman Survival

The Planck popcorn picture survives Perlman observational bounds with the weakest possible constraint: l_coh > 5.3e13 l_P (sub-nuclear scale). This is qualitatively different from the QFoam synthesis's concern that "macroscopic domains" might be required.

The per-boundary eigenvalue mismatch is tiny (delta_k/k = 0.002) because the D_K eigenvalues depend smoothly (Lipschitz continuously) on tau. Even at the maximum tested delta_tau = 0.05, the phase shift per boundary is small enough that only the cumulative random-walk amplification (sqrt(d/l_coh) factor for d = 1 Gpc) poses a challenge. The coherence scale l_coh = 0.86 fm is comparable to the proton radius -- the popcorn needs only to be coherent on sub-nuclear scales to survive all existing Perlman-class constraints.

This is the session's sole positive result.

### V.3 F-3 Holographic DOF Count: Jensen Dimensional Reduction

The Weyl exponent alpha decreasing from 5.3 (tau=0) to 2.5 (tau=0.50) is a novel structural finding: Jensen deformation of the SU(3) metric induces effective dimensional reduction in the eigenvalue counting function, without any quantum gravity mechanism. This is purely a consequence of the metric anisotropy -- as tau increases, the effective number of eigenvalues below a cutoff grows more slowly because the spectrum becomes increasingly gapped and stretched.

The alpha = 4.01 at tau=0.18 is intermediate between the volume law (alpha=3 for scalar Weyl on 6D) and the spinor-enhanced count (alpha=5.3 at tau=0). The internal manifold violates holographic bounds (alpha >> 2/3) at the Planck scale, as the QFoam synthesis anticipated. However, the amelioration by Jensen deformation means the violation is less severe at the physically preferred tau values.

**Cross-reference F-1 and F-3**: The mid-range d_s ~ 6.5 from F-1 is consistent with alpha ~ 4-5 from F-3 (d_s probes the local density of states; alpha probes the cumulative count; they agree within the expected regime-dependent discrepancy). Neither shows holographic scaling. The combined F-1 + F-3 result: the popcorn picture is holographically inconsistent at R_K ~ l_P but not catastrophically so -- the violation is order-2 (alpha ~ 4 vs holographic alpha ~ 2), not order-3 (alpha ~ 6 vs alpha ~ 2/3).

### V.4 Wheeler Connection: Is This Computable Foam?

The QFoam synthesis asked whether S_inst < 0 constitutes a computable realization of Wheeler's 1957 foam program on internal dimensions. Session 31Ca provides partial answers:

| Wheeler criterion | Status | Evidence |
|:-----------------|:-------|:---------|
| Planck-scale fluctuations | YES | S_inst < 0 (I-1 PASS, Session 31Ba) |
| Coherent macroscopic limit | NOT TESTED | GCM localizes at wrong tau (N-31Ce) |
| Observational survival | CONDITIONAL | l_coh > 0.86 fm (F-2 PASS) |
| Spectral dimension flow | NO | d_s ~ 6.5 standard Weyl (F-1) |
| Holographic consistency | PARTIAL | alpha ~ 4 (F-3), not holographic |
| Particle emergence | BLOCKED | M_max 7-13x below BCS threshold (N-31Cc) |

The foam program is computationally alive (observational constraints are weak, coherence threshold is low) but physically blocked (no particle emergence mechanism at mu=0). Wheeler's vision requires the foam -> coherence -> particles chain. Session 31Ca establishes that the last link (particles via BCS) is constrained at mu=0 by 6 independent methods.

### V.5 Amelino-Camelia Step 2 Progress

The QFoam synthesis (Section IV.3) noted that the framework is at "step 1.5" of the 4-step program. Session 31Ca advances to step 2 (derive observable consequences):

| Step | Status | Session 31Ca contribution |
|:-----|:-------|:------------------------|
| 1. State hypothesis | DONE | Instanton condensate produces particles |
| 2. Derive consequences | PARTIAL | F-2 (phase shift scaling), F-3 (DOF count) |
| 3. Identify experiments | PARTIAL | Perlman (HST, Chandra) already constrains |
| 4. Compare with data | NOT STARTED | Requires step 2 completion |

Remaining for step 2: tau-tau correlation function (GPE simulation), external metric coupling (spectral action on M^4 x SU(3)), domain-growth dynamics.

### V.6 Foam-Popcorn Structural Comparison

Against the Carlip program (QFoam synthesis Section III.1):
- **Shared strategy**: Planck-scale dynamics producing macroscopic coherence
- **Divergence 1**: Carlip on external metric (CC hiding via destructive interference); popcorn on internal modulus (particle emergence via constructive interference)
- **Divergence 2**: Carlip mechanism is generic (any foam); popcorn requires specific instanton gas dynamics

Session 31Ca does not change this assessment. The GCM result (N-31Ce) weakens the "constructive interference" claim: the quantum ground state localizes at the wrong tau, suggesting the popcorn does not naturally phase-lock at tau~0.18 without an external mechanism.

### V.7 Post-31C Foam Gates

| Gate | Status after 31Ca | Next step |
|:-----|:-----------------|:----------|
| F-CC-G (Carlip transmission) | NOT TESTED | Requires M^4 x SU(3) Einstein equations |
| F-SG (stochastic gap) | NOT TESTED | Requires mu > 0 dynamics |
| Tau correlation (GPE) | NOT TESTED | GPE simulation with 31C parameters |

---

## VI. Forward Implications

### VI.1 Gates That Opened New Channels

| Gate | Channel | Next computable step |
|:-----|:--------|:--------------------|
| F-2-G (CONDITIONAL PASS) | Perlman survival at l_coh > 0.86 fm | GPE tau correlation function to compute l_coh from dynamics |
| F-3-G (INFORMATIVE) | Jensen-driven alpha reduction | Off-Jensen alpha(tau, eps) map on U(2)-invariant grid |

### VI.2 Gates That Reinforced Existing Walls

| Gate | Wall reinforced |
|:-----|:---------------|
| N-31Ca-G (FAIL) | Wall 3 (spectral gap) -- density-dependent coupling provides zero enhancement |
| N-31Cb-G (FAIL) | Wall 3 -- truncation is not the problem; BCS converged at N_max=6 |
| N-31Cc-G (DOES NOT FIRE) | Wall 3 + Wall 4 -- Kapitza drive cannot bridge factor-7 gap at mu=0 |
| N-31Ce-G (FAIL) | Wall 4 -- GCM localizes at wrong minimum; quantum averaging worsens SM agreement |
| N-31Cg-G (FAIL) | Wall 4 -- V concave at tau=0.18; no self-consistent Kapitza solution |
| N-31Ch-G (FAIL) | Wall 4 -- Instanton frequency softening cannot create Kapitza minimum |
| N-31Cf-G (FEATURELESS) | Wall 3 -- no hidden pairing structure at gap edge |
| N-31Ci-G (NO SIGNAL) | Three-fold convergence not statistically confirmed |
| F-1-G (NO CDT CONNECTION) | No spectral dimension reduction from tau averaging |

### VI.3 Impact on Surviving Channels

**Kapitza channel**: Constrained on 3 fronts (N-31Cg concavity, N-31Ch no delta_crit, N-31Cc factor-7 gap). Survives ONLY in the untested full 5D landscape (soft mode with omega^2 < 5 AND convex curvature in that direction).

**P2b route (finite-density spectral action, mu != 0)**: Unchanged by Session 31Ca. All computations at mu=0 reinforce the obstruction. The mu=lambda_min diagnostic in N-31Cc shows M_max = 7.7-15.0 (well above threshold). The central question remains: what mechanism provides mu > 0?

**5D U(2)-breaking surface**: Not tested in Session 31Ca. The GCM result (N-31Ce) shows the quantum ground state at (tau=0.60, eps=0.15), suggesting that U(2)-breaking directions (nonzero eps) are energetically preferred. Whether the full 5D landscape contains soft modes and convex curvature at tau~0.18 remains the decisive untested question.

**Instanton-condensate self-consistency loop**: 5 of 6 links constrained or blocked:

| Loop Link | Status | Session 31Ca result |
|:----------|:-------|:-------------------|
| Curvature -> instanton | CONFIRMED | I-1 PASS (Session 31Ba) |
| Instanton -> mu_eff | BLOCKED | N-31Ch: no Kapitza minimum at any frequency |
| mu_eff -> BCS | BLOCKED at mu=0 | N-31Ca/Cb/Cc: M_max 7-13x below threshold |
| BCS -> stabilization | BLOCKED | N-31Ce: GCM at wrong minimum |
| Stabilization -> curvature | UNTESTED | Requires self-consistent tau |
| Loop closure | BLOCKED | N-31Cg: no cranking fixed point |

The self-consistency loop cannot close with the ingredients tested in Session 31Ca. The sole surviving path requires: (1) a mechanism to generate mu > 0 from instanton energy deposition, AND (2) a soft mode in the full 5D landscape that creates a convex Kapitza well.

### VI.4 Next Computations (if warranted)

| Priority | Computation | Prerequisite | Rationale |
|:---------|:-----------|:-------------|:----------|
| 1 | Full 5D transverse Hessian at tau~0.18 | Medium cost (~1 hr) | Determines whether soft modes (omega^2 < 5) exist |
| 2 | mu-generation from instanton energy | Theoretical | Can S_inst < 0 fund an effective chemical potential? |
| 3 | GPE tau correlation function | GPE simulation setup | Determines l_coh from dynamics (F-2 follow-up) |
| 4 | Off-Jensen alpha(tau, eps) map | Low cost | F-3 follow-up, Jensen-induced dimensional reduction |

---

## VII. Deliverable Inventory

### Scripts (12)
| File | Computation | Agent |
|:-----|:-----------|:------|
| `tier0-computation/s31Ca_density_dep_pairing.py` | N-31Ca | naz |
| `tier0-computation/s31Cb_bcs_convergence.py` | N-31Cb | naz |
| `tier0-computation/s31Cc_bcs_kapitza.py` | N-31Cc | sim |
| `tier0-computation/s31Cd_bayesian_ncgkk.py` | N-31Cd | bap |
| `tier0-computation/s31Ce_gcm_moduli.py` | N-31Ce | bap |
| `tier0-computation/s31Cf_odd_even_stagger.py` | N-31Cf | naz |
| `tier0-computation/s31Cg_selfconsistent_cranking.py` | N-31Cg | bap |
| `tier0-computation/s31Ch_instanton_eff_freq.py` | N-31Ch | bap |
| `tier0-computation/s31Ci_bayesian_convergence.py` | N-31Ci | naz |
| `tier0-computation/s31Ca_foam_spectral_dim.py` | F-1 | sim |
| `tier0-computation/s31Ca_foam_domain_phase.py` | F-2 | sim |
| `tier0-computation/s31Ca_foam_holo_dof.py` | F-3 | sim |

### Data Archives (12)
| File | Computation |
|:-----|:-----------|
| `tier0-computation/s31Ca_density_dep_pairing.npz` | N-31Ca |
| `tier0-computation/s31Cb_bcs_convergence.npz` | N-31Cb |
| `tier0-computation/s31Cc_bcs_kapitza.npz` | N-31Cc |
| `tier0-computation/s31Cd_bayesian_ncgkk.npz` | N-31Cd |
| `tier0-computation/s31Ce_gcm_moduli.npz` | N-31Ce |
| `tier0-computation/s31Cf_odd_even_stagger.npz` | N-31Cf |
| `tier0-computation/s31Cg_selfconsistent_cranking.npz` | N-31Cg |
| `tier0-computation/s31Ch_instanton_eff_freq.npz` | N-31Ch |
| `tier0-computation/s31Ci_bayesian_convergence.npz` | N-31Ci |
| `tier0-computation/s31Ca_foam_spectral_dim.npz` | F-1 |
| `tier0-computation/s31Ca_foam_domain_phase.npz` | F-2 |
| `tier0-computation/s31Ca_foam_holo_dof.npz` | F-3 |
| `tier0-computation/s31Ca_instanton_kapitza.npz` | IK (addendum) |

### Plots (13)
| File | Computation |
|:-----|:-----------|
| `tier0-computation/s31Ca_density_dep_pairing.png` | N-31Ca |
| `tier0-computation/s31Cb_bcs_convergence.png` | N-31Cb |
| `tier0-computation/s31Cc_bcs_kapitza.png` | N-31Cc |
| `tier0-computation/s31Cd_bayesian_ncgkk.png` | N-31Cd |
| `tier0-computation/s31Ce_gcm_moduli.png` | N-31Ce |
| `tier0-computation/s31Cf_odd_even_stagger.png` | N-31Cf |
| `tier0-computation/s31Cg_selfconsistent_cranking.png` | N-31Cg |
| `tier0-computation/s31Ch_instanton_eff_freq.png` | N-31Ch |
| `tier0-computation/s31Ci_bayesian_convergence.png` | N-31Ci |
| `tier0-computation/s31Ca_foam_spectral_dim.png` | F-1 |
| `tier0-computation/s31Ca_foam_domain_phase.png` | F-2 |
| `tier0-computation/s31Ca_foam_holo_dof.png` | F-3 |

### Session Documents (2)
| File | Description |
|:-----|:-----------|
| `tier0-computation/s31Ca_gate_verdicts.txt` | All 12 gate verdicts with justification |
| `sessions/archive/session-31/session-31Ca-synthesis.md` | This document |

---

## VIII. Addendum: Instanton-Kapitza V_Kapitza (Post-Hoc Computation)

After the 12 pre-registered gates were classified, sim ran an additional zero-cost computation: the instanton-driven V_Kapitza, replacing the Hessian-derived transverse frequencies (omega^2 = 8.326, 9.893) with tau-dependent instanton frequencies (omega_eff^2 = Gamma_inst(tau)^2 from I-1 data at 6 coupling ratios r = {0.1, 0.3, 0.5, 1.0, 2.0, 5.0}).

### VIII.1 Result: First Positive Dynamical Signal

**Interior minimum at tau* = 0.196** with r=5.0, A=0.15. d2V/dtau2 = 1628 (stiff, well-defined). Additional minima near the three-fold convergence region:

| A | tau* | d2V/dtau2 | omega_eff^2(tau*) |
|:--|:-----|:----------|:------------------|
| 0.02 | 0.159 | 1887 | 0.296 |
| 0.12 | 0.163 | 2778 | 0.292 |
| 0.15 | **0.196** | **1628** | 0.265 |

Constant-omega variant at r=5.0 (omega^2=0.278): tau* = 0.100 and 0.389.

This is the first time in the project's history that a dynamical stabilization mechanism has produced an interior minimum near the physically preferred tau window [0.15, 0.21].

### VIII.2 Caveats (Two Substantial)

**Caveat 1: I-1 Tension (anti-correlation between instanton rate and Kapitza softness)**

Minima appear ONLY at r=5.0, which is the one coupling ratio where I-1 FAILED (Gamma_inst/omega_tau = 0.71, below the threshold of 3). At r <= 2.0, where the instanton gas is dynamically relevant (I-1 PASSES with ratios 3.5-9.6), the effective frequency omega_eff^2 > 1.5 is too stiff for Kapitza minimum creation.

This creates a structural anti-correlation:
- r < 2: instanton gas active (I-1 PASS), but Kapitza frequency too stiff (no minimum)
- r = 5: Kapitza frequency soft enough (minimum at tau ~ 0.16-0.20), but instanton gas conventionally rare (I-1 FAIL)

The instanton rate and Kapitza softness requirements cannot be simultaneously satisfied at the same coupling ratio r. However, this anti-correlation applies to the single-instanton dilute gas approximation. At r=5.0, S_inst = -R + 5*K = -2.000 + 5*0.531 = +0.655 > 0 (instantons ARE exponentially suppressed, but only mildly: exp(-0.655) = 0.52). The instanton gas is not absent at r=5 -- it is rare but not negligible. Whether a rate of 0.52*omega_tau is sufficient to maintain a Kapitza orbit is a dynamical question not answered by the I-1 gate (which tested the threshold ratio 3, not the minimum viable ratio).

**Caveat 2: Kapitza Formula Validity (large correction regime)**

V_corr/V_range ~ 1.02 at r=5.0. The Kapitza correction is comparable to the total potential range. The time-averaging formula:

```
V_Kapitza = <V> + (1/4*omega^2)*<(dV/deps)^2>
```

is derived assuming the correction term is small compared to the bare potential (the adiabatic separation: fast oscillation + slow drift). When V_corr ~ V_range, the orbit period is comparable to the dynamical timescale of the potential, and the time-averaging approximation breaks down. The minimum is real WITHIN the Kapitza formula but may not survive a full dynamical integration.

**Caveat 3: Geometric Inaccessibility (Baptista assessment)**

Baptista assessed the KK geometry constraint on the physical coupling ratio r = alpha_YM/alpha_grav. From Paper 14 eq 2.93: alpha_1 ~ 0.16, alpha_2 ~ 0.12 at tau=0.21, with alpha_grav = 1 in the I-1 convention. This constrains the physical r to O(0.1), NOT r=5.

At the physical coupling r ~ 0.1:
- Gamma_inst^2 ~ 50-110 (TOO STIFF for Kapitza minimum -- omega_eff^2 >> 5)
- S_inst ~ -2.0 (instantons copious, but frequency much too high)

At r=5 where the minimum exists:
- S_inst = +0.655 (instantons suppressed)
- Gamma/omega_tau = 0.71 (I-1 FAILS)
- The coupling ratio is 50x above the geometric value

**The Kapitza minimum at tau*=0.196 is real as a mathematical feature of the Kapitza formula but resides at a geometrically inaccessible coupling ratio.** The physical r ~ 0.1 gives omega_eff^2 ~ 50-110, far beyond where any minimum can form.

**Escape route**: If alpha_grav differs from 1 (its physical value has NOT been derived from the 12D action -- the I-1 convention alpha_grav = 1 is an assumption, not a derivation), the effective instanton rate changes. If alpha_grav << 1, the physical Gamma_inst could be softened into the Kapitza-minimum regime even at r ~ 0.1. This is the remaining open question.

### VIII.3 Classification

**Status**: Post-hoc computation. NOT among the 12 pre-registered gates. Per the project's evidence discipline, this is noted as assembled AFTER the pre-registered computation was complete. It is not treated as pre-registered evidence.

**Assessment**: CONDITIONAL. The instanton-Kapitza minimum is mathematically real but physically inaccessible at the geometric coupling ratio r ~ 0.1. Three caveats prevent unconditional classification: (1) the I-1 rate/Kapitza softness anti-correlation, (2) the Kapitza formula operating outside its validity regime, and (3) the geometric inaccessibility of r=5.0 (Baptista assessment). The mechanism is proven to work IN PRINCIPLE but not shown to work AT THE GEOMETRIC COUPLING.

The appropriate next steps (in priority order):
1. Derive alpha_grav from the 12D action (determines whether r=5 is physically accessible)
2. If alpha_grav << 1: full dynamical ODE integration at the resulting physical r
3. If alpha_grav ~ 1: the Kapitza-instanton channel is geometrically inaccessible and the minimum at tau*=0.196 is a mathematical curiosity

### VIII.4 Impact on Self-Consistency Loop

The instanton-Kapitza result partially reopens the self-consistency loop assessment:

| Loop Link | Status (pre-addendum) | Status (post-addendum) |
|:----------|:---------------------|:----------------------|
| Curvature -> instanton | CONFIRMED | CONFIRMED |
| Instanton -> mu_eff | BLOCKED | **CONDITIONAL** (minimum at r=5.0, but r~0.1 is geometric value) |
| mu_eff -> BCS | BLOCKED at mu=0 | BLOCKED at mu=0 (unchanged) |
| BCS -> stabilization | BLOCKED | **CONDITIONAL** (minimum exists at tau*=0.196, inaccessible at r~0.1) |
| Stabilization -> curvature | UNTESTED | UNTESTED |
| Loop closure | BLOCKED | **CONDITIONAL** (requires alpha_grav derivation + dynamical verification) |

Two obstructions remain:
1. **Geometric coupling**: The Kapitza minimum requires r=5.0 but the KK geometry constrains r ~ 0.1 (50x too small). Unless alpha_grav << 1 in the 12D action, the minimum is inaccessible.
2. **BCS at mu=0**: Even with a Kapitza minimum at tau*=0.196, BCS condensation requires mu > 0, which the instanton-Kapitza mechanism does not provide. Particle emergence still requires the finite-density route (P2b).

### VIII.5 Files

`tier0-computation/s31Ca_instanton_kapitza.{py,npz,png}`

---

*Synthesis assembled by coord (coordinator) from: computation results reported by naz (N-31Ca, N-31Cb, N-31Cf, N-31Ci), bap (N-31Cd, N-31Ce, N-31Cg, N-31Ch), sim (N-31Cc, F-1, F-2, F-3), plus post-hoc instanton-Kapitza (sim). Nuclear DFT review by naz (Nazarewicz). Gate verdicts classified before interpretation. Numbers from computation outputs, not re-derived. All 12 pre-registered gates evaluated against their stated conditions. Addendum (Section VIII) documents the post-hoc instanton-Kapitza result with caveats. This document is the definitive Session 31Ca record.*
