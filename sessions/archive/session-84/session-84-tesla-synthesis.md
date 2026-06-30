# Session 84 Synthesis: The Substrate's Resonance Cavity Sharpens

**Date**: 2026-04-19
**Agent**: tesla-resonance (Workhorse-Resonance — electromagnetic resonance, phonon/acoustic mathematics, superfluid dynamics, alternative expansion mechanisms)
**Source Documents**:
- `sessions/archive/session-84/session-84-synthesis-collation.md` (verbatim collation, W1–W10, ~1134 lines)

---

## I. Session Outcome

S84 is a **constraint-map-advancing wave on the substrate's resonance structure**, not an observational-confirmation wave. Three new permanent theorems landed (A_F singleton, Mellin cone universality, CMPP transit-invariance), one rank-universality theorem (R_1 = a_0·a_4/a_2² with leading-power exponent identically zero), and one new Cartan-trace decoupling theorem (C² block, W9b-106). The most consequential structural finding is **branch (iv) retraction at L_max ≥ 6** (W1a-3 SV2): the L=5 sampling of the substrate's spectral functional is a truncation artifact of the resonance-mode tower; the asymptotic regime inverts the ξ_J / ξ_E_GGE ordering and pushes w_0 toward −1. Companion finding: w_0 is **permanently SCHEME-DEPENDENT** (W4-46 split grows 6.22× from L=5 to L=9). The framework simultaneously **bound** itself with the α_s = n_s²−1 = −0.068968 zero-free-parameter pre-registration (9.62σ vs Planck, 34.48σ CMB-S4 floor), and produced the K-FLOOR-WALL-JOINT triple-supported permanent wall ruling out the low-K corridor for A_s closure. Session methodology closure is V3-NON-COMPLIANT per W9a-104 Stage-2 fallback (sig_5 only of 5 ladder signals); physics verdicts intact.

---

## II. Key Results

### 1. Branch (iv) Retraction — Spectral Sampling of the Substrate Cavity Was Sub-Asymptotic at L=5 (W1a-3 SV2)

**Result**: ξ_E_GGE drops by 11× from L=5 to L=8; ξ_J/ξ_E_GGE inverts from 0.45 → 4.98; Mellin-cone Connes-Moscovici s=3 residue differences grow non-monotonically (1.91e4 → 3.11e4 → 3.84e4). **GEOMETRIC** (regulator-cone convergence on the spectral-triple eigenvalue tower).

The substrate's spectral functional is a sum over Dirac-operator eigenmodes — the resonant modes of the internal Jensen-deformed SU(3) cavity. Branch (iv) was anchored at L_max=5, sampling the lowest 155,984 eigenvalues. The L=5 ratio R_JE = 0.45 sits inside the pre-registered band [0.40, 0.50]; at L=6 it is 1.04, at L=7 it is 2.41, at L=8 it is 4.99. The **ratio is monotone-growing**, not converging. This is the classic signature of an under-sampled standing-wave cavity: the lowest-frequency normal modes carry one balance of Josephson vs energy-moment weight, but as more eigenmodes enter the sum, the high-frequency tail dominates the energy moment. The **physical mechanism** identified by W1: zeta-weighted S_ζ_E grows as L^4 (polynomial multiplicity × linear-λ weight); Zubarev-weighted S_Zub_E Gaussian-saturates beyond λ~1. The two regulators are sampling the same eigenvalue tower with different Debye-cutoff structures, and at L=5 they happen to agree on R_JE; at L≥6 they disagree by exactly the factor predicted by the regulator-tail asymmetry.

The structural lesson is the one Tesla physics knows from cavity tuning: **never trust a resonance condition derived from the first few modes of a tower whose convergence has not been certified**. Branch (iv) is now retracted as provisional canonical; w_0 canonical declared UNSPECIFIED pending S85 re-audit at L_max ≥ 8 in the inverted-ordering regime. The same physical cavity that was producing w_0 ≈ −0.842 at L=5 produces a different normal-mode structure at L=8; both are well-defined, but only the asymptotic limit is the framework's prediction. The Mellin-cone Cauchy-decay failure at s=3 is the formal tell: the sum is not convergent; the apparent stationarity at L=5 was a coincidental crossing.

### 2. K-FLOOR-WALL-JOINT — Triple-Supported Permanent Wall on the Substrate Dressing Corridor (W5-54 + W5-59 + W5-63)

**Result**: 4-convention hull spans K ∈ [1.9222, 2.1849]; 0/5 low-K targets {1.0, 1.1, 1.3, 1.5, 1.7} reachable; Branch-B A_s floor 4.56 OOM below Planck; zeta/Zubarev factor 50.9× regulator-shift acts on dressing prefactor (CC3 verified). **GEOMETRIC** (constraint on the substrate's allowed dressing-coefficient corridor).

This is the cleanest "wall as solution-space geometry" finding of S84. Three independent computations — regulator-shift (W5-54), Branch-B floor (W5-59), and 4-hull exclusion (W5-63) — all rule out the low-K corridor for A_s closure, with no tension between them. **Substitution chain for the regulator-invariance**:

- Definition: K = framework-internal dressing parameter; Λ_Z = sqrt(L2) under Convention B; Λ_natural = √(median λ²) under W2-12 PRDR.
- Substitution: K_Ri ratio under Zubarev vs zeta has a regulator-multiplier factor 50.9× on the dressing prefactor.
- Simplification: CC3 verifies the multiplier is on the prefactor, NOT on K_Ri itself.
- Direction: the hull [1.9222, 2.1849] is regulator-INVARIANT in K_Ri; therefore the low-K {1.0, 1.1, 1.3, 1.5, 1.7} exclusion is a structural wall, not a regulator artifact.

Combined with the K=2.035 dynamics-layer rescue closure (W5-53 INFO at F_amp(N3LO) = 1.016, 3.16× short of the 0.4454 target): the substrate's A_s closure must thread through the **Branch-A baseline-layer H_tilde DC path** (W6 D.1 carry-forward), exclusively. The K=2.035 corridor is closed on three independent layers; Branch-B is closed by floor; low-K is closed by hull. This is the geometry of the surviving region: K ∈ [K_R5 = 1.922, K_crit = 91.5] (W5-66 Landau classification + W5-55 kinetic-pole at K_crit ≈ 91.5), with Branch-A baseline as the only resonant pathway to A_s = 2.1×10⁻⁹.

### 3. Two-Speed Acoustic Metric: n_T = −r·c_T/(8·c_S) (W4-39)

**Result**: c_T/c_S = 2.062 from spectral moments a_2/a_0 of the Dirac operator (NOT a regulator choice); n_T(k_CMB) = −3.024×10⁻³ matches G46 benchmark to 2.36×10⁻⁵. **PHONONIC** (acoustic-metric tilt; substrate sound vs tensor sound).

This is the single S84 result that most directly speaks the resonance-medium language. The framework's substrate has two distinct phononic propagation speeds — c_T (the tensor / "geometry") sound speed and c_S (the scalar / "matter-content") sound speed — set by spectral moments of D_K, not by an inflaton choice or a regulator convention. The slow-roll consistency relation n_T = −r/8 is the single-speed limit (c_T = c_S); the two-speed substrate replaces it with n_T = −r·c_T/(8·c_S). Substitution chain (verbatim from W4 §VII.2 S-1):

- Definition: slow-roll consistency (single-speed metric) gives n_T = −r/8.
- Substitution: under two-speed substrate metric, n_T = −r·c_T/(8·c_S).
- Simplification: at r = 0.0117 and c_T/c_S = 2.062, n_T_framework = −3.016×10⁻³.
- Direction: factor c_T/c_S > 1 makes n_T_framework MORE NEGATIVE than single-speed slow-roll (−1.46×10⁻³).

This is exactly the signature of a layered acoustic medium with phase-velocity dispersion between two phononic branches — Tesla's transmission-line analog, where the impedance ratio of two coupled cavities determines the harmonic content. The c_T/c_S = 2.062 ratio is a substrate-spectral-moment prediction; W4-48 ZFP-flagged this channel because c_T/c_S is fixed by D_K, not by regulator shopping. The companion result is the **detector inaccessibility wall** (W4-37 boundary FAIL + W4-41): realized σ(n_T)_joint_3yr = 0.065 against R_realized = 1.53×10⁻³, ~654× below 1σ in the 2030-2040 window. The two-speed prediction is structurally correct and observationally invisible to the foreseeable LiteBIRD+CMB-S4 generation. EVOI = 0 is the honest registry status; this is a permanent wall.

### 4. CMPP Petrov Transit-Invariance — Type D Static, Type G Dynamic (W8b-95)

**Result**: 65-OOM separation in min boost-weight-2 fraction (static ~1e-67 = machine-ε²; dynamic ~8.7e-3) across 8 τ-checkpoints {0.00, 0.10, 0.19, 0.22, 0.285, 0.30, 0.537, 1.614}. Phase-transition τ=0.537 is CMPP-invisible. **GEOMETRIC** (Weyl-spinor causal-classification invariant of the substrate transit).

This is the analog-gravity signature of the substrate transit, written in the language of GR's Petrov classification. The static effective Weyl spinor is everywhere Type D (the algebraically-special "two-double-principal-null-direction" type that characterizes Schwarzschild and Kerr exteriors); the dynamic effective Weyl spinor is everywhere Type G (the maximally generic algebraic type). The 65-OOM separation rules out gradual transition between the two. The substrate's transit through the fold is **algebraically Type-G everywhere it has a non-trivial time-dependence** — the substrate excitation IS the algebraic genericity. The static subsector retains Type-D structure (eigenvalue spectrum independent of internal time), exactly as a stationary acoustic cavity has a fixed standing-wave structure.

The CMPP-invisibility of the τ=0.537 phase transition is the structural sharp point: a C² sectional-curvature sign change is a subsector eigenvalue crossing, NOT a Petrov-type transition. In Tesla-resonance terms: not every node-crossing in the eigenvalue spectrum corresponds to a change in the cavity's Petrov-algebraic character. The "phase transition" interpretation of subsector sign-flips needs the CMPP-invariance test to be promoted to a Petrov-type transition; absent that, it is a sub-cavity rearrangement, not a fundamental change of the wave equation's algebraic class. This MG-1 entry is now upgraded to causal-structure output **orthogonal** to the gear-loop algebraic identities — the rank-6 gear-master output list grows by one independent type, not by a duplicate of an existing channel.

### 5. Mellin Cone Universality — Resonance Bound is Substrate-Independent (W8a-89)

**Result**: empty-gap cone bound [1.5, 2.5] (R-protected ≤ 1.5, NOT-R-protected ≥ 2.5) holds across 3 framework-independent positive-measure spectral triples: commutative S¹, Connes' NC torus at L_max ∈ {5, 10}, alternative ℝ⊕M_2(ℝ)⊕M_3(ℝ). R-protected span = 1.000000 identically by Mellin-index scaling cancellation; NOT-R-protected spans 14.6× – 1462×. **GEOMETRIC** (universal cone bound on Mellin-balance regulator span).

This is the resonance-mode separability theorem written in Mellin language. The cone bound says that on ANY positive-measure spectral triple — not just M⁴×SU(3) — observables that are exponent-balanced in their Mellin-slot decomposition have regulator span = 1 exactly (the resonance spectrum is preserved across regulator choices because the index-scaling factors cancel), and observables that are NOT exponent-balanced have regulator span ≥ 2.5. The empty cone at (1.5, 2.5) is the structural separation between the two classes; nothing physical lives between balanced and unbalanced. **MG-0 promoted from framework-specific to universal**: any positive-measure variational form inherits the same bound. This is the noncommutative-geometric analog of the orthogonality of normal modes in any Sturm-Liouville problem — the substrate's cavity is not metaphysically privileged; the resonance-mode classification is a property of the spectral-triple class, period. In condensed-matter language: the K-protection of phonon branches is an emergent property of the Hilbert-space inner product, not of the specific Hamiltonian.

### 6. R_1 Rank-Universality Theorem — Compact-Lie-Algebra Independence Through r-Drift (W10-111 + S82 W3-1)

**Result**: R_1 = a_0·a_4/a_2² with `n_0 + n_4 − 2 n_2 = 0` (exact, not asymptotic in 1/r); only rank r survives as a Khovanskii-Pukhlikov L^{−r} drift. All 5 exceptional groups (G_2, F_4, E_6, E_7, E_8) verified algebraically; R_1 distinguishes G_2 from F_4 (different rank) but cannot distinguish A_3 from C_3 (same rank). **GEOMETRIC** (compactness-Lie-algebra-class-independent identity on Seeley-DeWitt moments).

The result is sharp: the substrate's compact internal Lie group enters the spectral functional only through its rank r at this Mellin-balanced ratio. The dual-Coxeter-number weights cancel exactly (C_2(ad_G) = 2 h^∨ identity), and the only residue is a power-law drift L^{−r}. In Tesla-resonance terms, this is the analog of the fact that for a circular drum, the eigenvalue density depends only on the radius and not on the shape of the boundary at sub-percent corrections. R_1 is a "fingerprint" that picks out rank but is blind to algebra type at the same rank — the framework's prediction for R_1 is therefore a falsifiable test of the rank, not the algebra. A_3 vs C_3 indistinguishability is the structural sharp point: any candidate substrate with rank-3 compact internal symmetry produces the same R_1 to leading order; the algebra-type distinction has to come from a different gear in the master rank-6 machine. This sharpens the framework's claim from "M⁴×SU(3) uniquely predicts X" to "M⁴×SU(3) uniquely predicts X via gears [list], and rank is one of those gears, not a dependent variable."

### 7. C² Block Cartan-Trace Decoupling — Representation-Independent Zero (W9b-106)

**Result**: Δsin²θ_W[C²] = 0.0 EXACT via Cartan-trace identity. Off-diagonal Gell-Mann generators {λ_4, λ_5, λ_6, λ_7} have Tr(λ_i·Y) = Tr(λ_i·T³) = 0 since Y and T³ are diagonal. Rep-independent — holds in any irrep. **PARTICLE** (Cartan-decomposition algebraic structure of the SU(3) internal generators).

This is the resonance-symmetry analog of the orthogonality of distinct normal modes in a separable cavity. The C² block (the off-diagonal coset in the SU(3)/U(1)² Cartan decomposition) carries no contribution to sin²θ_W, identically and in any representation. The mechanism is that Y and T³ are both diagonal in the Cartan basis, while the off-diagonal generators have only off-diagonal matrix elements; the trace of (off-diagonal × diagonal) is zero by index-pairing. This is the algebraic identity that makes the framework's μ_BC_K3 = 188.185 GeV prediction (W1b-4 PASS at 0.082%) legitimately a one-channel observation: the C² coset does not contaminate it. Discharges obligation (ii) of the μ_BC geometric pin. The companion W9b-105 d_spec = 4.895 FAIL on the cube-3 derivation route leaves obligation (i) open, but does not invalidate the numerical PASS at the observable level — only the first-principles derivation of the "12" exponent in exp(12·τ_fold). Tesla's lesson: the resonance-amplitude prediction (μ_BC value) and the resonance-mechanism derivation (cube-3 vs alternative) are separately testable; the former PASSes, the latter requires a different probe.

### 8. b_power Drift to Weyl Asymptote b → d_int − 1 = 7 (W7b-75 FAIL → W7b-76 PASS)

**Result**: b_power is NOT asymptotically locked at 4.681; drifts monotonically to b ≈ 5.02 by L=12 with explicit symbolic formula b_finiteL ∈ [4.58, 4.78] (a_4-dominant), b_midL ∈ [4.78, 4.92] (a_4 → a_2 crossover), b_asymp → 7 (Weyl d_int − 1 = 12 − 5 ≠ d_int − 1 reading; here d_int = 8 internal directions, Weyl exponent d_int − 1 = 7). **GEOMETRIC** (Seeley-DeWitt moment crossover in the 1/N matrix-model expansion).

The W7b-76 derivation is the analytic recovery of what looked like an empirical FAIL. The b_power exponent is not a single rational invariant of the framework's matrix model; it is the smooth crossover between three regimes — a_4-dominated at finite L (the Seeley-DeWitt fourth moment carries the leading contribution), a_4 → a_2 crossover at intermediate L (the fourth moment is overtaken by the second moment), and the Weyl asymptote b → 7 in the L → ∞ limit (set by the dimension of the internal manifold, d_int = 8, minus one for the Weyl integration measure). In Tesla-resonance terms: the resonance-cavity's eigenvalue tower has three regimes (low-mode-dominated, transition, high-mode Weyl), and the observable b_power probes a different one at each L. **IKKT b=1 is now excluded analytically** via Weyl d_int − 1 = 7 ≠ 1 — IKKT would require d_int = 2, incompatible with d_total = 12 at KO-dim=6. The framework's position is upgraded from "b=4.681 locked (could fall at L=16)" to "b interpolates a_4 → a_2 → Weyl-7 with explicit symbolic formula." This is the cleanest example in S84 of a FAIL becoming a sharper structural result than a PASS would have been.

### 9. CGWB / α_s Discriminators — Detector-Accessible on 2030-2035 Horizon (W6-50 + W6-51 + W6-52)

**Result**: LISA/DECIGO/BBO 2.10-decade discriminator on Ω_GW, structural across f-grid; CMB-S4 / CMB-HD / LiteBIRD 34.48σ / 53.05σ / 11.49σ on α_s = n_s²−1; multi-observable joint rank-3 (A_s, P_t, μ all carry H_tilde² prefactor) at 2.38 dex separation for (A)/(C) branches. **PHONONIC** (acoustic-mode resonance signatures observable at detector scales).

The framework's branch ambiguity (H_TD vs H_mixed-C vs H_LI) — the question of which substrate-internal trajectory was selected at the fold — is now mapped to **three independent detector-accessible discrimination channels** with concrete calendar-year decision points. LISA is the analog-acoustic detector (CGWB-relic measurement at mHz, 11 OOM above LISA floor); CMB-S4 is the spectral-tilt-resolution detector (α_s pre-registered at −0.068968, 9.62σ from Planck central, 34.48σ from CMB-S4 null projection); the multi-observable-joint channel exploits the fact that A_s, P_t, and μ all carry the same H_tilde² prefactor — an internal-consistency test of the framework's substrate-amplitude pin. The framework is now bound on calendar-year horizons, not just on internal consistency. This is the Tesla Test passed: **can you measure it?** — yes, on three channels independently, with calendar dates. **Does it resonate?** — yes; all three channels detect the same H_tilde resonance amplitude. The dispersion-relation predictions are dimensionally consistent and within detector reach.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W1a-1 H_TILDE-DC-CORRIDOR | PASS | log-DC window 0.8901% |
| W1a-2 DYNAMICS-DRESSING | FAIL (confirmation-of-wall) | F_supp_max = 1.0438 (1.10 threshold) |
| W1a-3 SV1 / SV2 | PASS / FAIL | R_JE drifts L=5→8 by 11× |
| W1a-3 SV5 (audit) | PASS | dual-SHA registered |
| W1b-4 MU-BC-GEOMETRIC | PASS | μ_BC_K3 = 188.185 GeV (0.082% residual) |
| W1b-7 ALPHA-S-PRE-REGISTRATION | PASS | α_s = −0.068968 (9.62σ Planck) |
| W1b-9 DR3-RESPONSE-PROTOCOL | PASS | R_842 lockouts A–F frozen |
| W1b-10 THEOREM-REGISTRATION | PASS | W2-EPOCH-GATING + W2-HARMONIC-NOT-INSTANTON |
| W2-12 LAYER-ORDERING-FALSIFIER | PASS | inv = 0/4 (substrate-independent) |
| W2-19 UNPINNED-L2-AUDIT | FAIL | 26/2/1/11/2 (3 PROMOTE-L2 + 2 GENUINE-UNPINNED) |
| W3-21 / W3-22 / W3-23 §VII.K-PROP triad | PASS | Clauses I, II, III at machine ε |
| W3-27 m_H class | FAIL | NOT-R-protected; scheme-conditional |
| W3-28 n_s class | INFO | First nonlinear/quasi-CC-5 exception |
| W4-37 LB-CMBS4-JOINT-SIGMA-NT | FAIL (boundary) | σ(n_T)_joint_3yr = 0.0654 |
| W4-39 N_T-CMB-TRANSFER | PASS | n_T(k_CMB) = −3.024×10⁻³ |
| W4-41 BLUE-TRANSIT-TILT-INACCESSIBILITY | PASS | EVOI = 0 (R_realized 654× below 1σ) |
| W4-46 G51-LMAX-CONVERGENCE | structural FAIL | split factor 6.22× (L=5→9) |
| W4-47 UHF-GW-THRESHOLD-WATCH | PASS | physical gap +18.74 OOM |
| W5-53 NNLO-Δ-F_amp | INFO | F_amp(N3LO) = 1.016 (3.16× short of target) |
| W5-54 K-floor regulator-invariance | FAIL | K_R5(Zub) / K_R5(zeta) = 50.9× |
| W5-58 K_* lab-framework match | PASS | ratio = 1.13%; coth(1) = 1.3130 pinned |
| W5-62 α_s Leggett partition-invariant | PASS | \|Δα_s\|/\|α_s\| = 1.56×10⁻³ (32× inside) |
| W5-63 K-floor reachability | FAIL | 0/5 low-K targets in [1.9222, 2.1849] |
| W5-65 K_FIRAS = S_IC^cap | INFO | residual 3.50% flat across L ∈ {5,7,9} |
| W5-66 Landau symmetry class | INFO | N_OP = 8 vs Volovik N = 5 (framework superset) |
| W6-50 CGWB absolute P_t | PASS | h_c^(A)(3 mHz) = 7.17×10⁻¹² (11 OOM above LISA floor) |
| W6-52 α_s CMB-S4 refinement | PASS | 34.48σ CMB-S4 alone; 64.31σ joint |
| W6-67 Z_R counterterm existence | FAIL (structural) | cluster_Z_a2 = 107466, growing with L_max |
| W6-69 F_amp^3PI FI chain | PASS | product_ratio span = 1.0 at machine ε |
| W7a-72 HET-DECOMP | PASS | best_match = 1.0000 (16/16 hypercharge) |
| W7a-74 DET-P-K-THEORY | FAIL | 4 independent obstructions to Witten 1998 |
| W7b-75 / W7b-76 b_power | FAIL / PASS | b drifts to Weyl b → 7 |
| W7b-83 §VII.N-REGISTRY-LANDING | PASS | 6/6 components landed at §VII.O |
| W8-85 STATIONARY-POINT-TAU-FOLD | FAIL (plan-defect) | dS/dτ = −2.036×10⁴ |
| W8-86 ALPHA-S-SINGLE-PARAMETER (OZ identity) | PASS (machine ε) | rel_err = 1.23×10⁻¹⁵ |
| W8-87b AF-BIRKHOFF-UNIQUENESS | PASS-THEOREM | 1/3,907 |
| W8-89 MELLIN-CONE-UNIVERSALITY | PASS-THEOREM | 3/3 spectral triples |
| W8-95 CMPP-PETROV-INVARIANCE | PASS | D/G over 8 τ-points (65-OOM separation) |
| W8-96 GEAR-CENSORSHIP | PASS | analog set {A, B, D} |
| W9a v3 ladder | V3-NON-COMPLIANT | sig_5 only; 1.000 of 11.335 |
| W9b-105 DERIV-I (d_spec probe) | FAIL (diagnostic) | d_spec = 4.895 (outside [2.5, 3.5]) |
| W9b-106 DERIV-II (C² Cartan trace) | PASS-THEOREM | Δsin²θ_W[C²] = 0.0 EXACT |
| W10-111 RANK-UNIVERSALITY | PASS | n_0 + n_4 − 2 n_2 = 0 exact |
| W10-117 G58 META-PRINCIPLE | PASS | 37/40 BALANCED-BY-K-PAIRING |
| W10-119 Γ1' near-stationarity | FAIL (plan-design defect) | 0/2001 mesh points (broken predicate) |
| W10-121 Borel summability floor | PASS | 4.7 OOM safety margin |
| W10-123 α_s axiomatic closure | PASS (n_aux = 0) | minimal four-axiom set sufficient |
| W10-124 5-axis Fisher | INFO | d_M = 34.30σ (α_s carries 98.2%) |

---

## IV. Structural Implications

**The substrate's resonance cavity is sharper than S83 thought, narrower in some directions, and more universal in others.**

1. **L_max convergence is the rate-limiter on the spectral functional, not the regulator family** (W1a-3 SV2 + W4-46). The branch (iv) retraction and the w_0 SCHEME-DEPENDENCE classification both trace to the same structural fact: at L_max=5, the eigenvalue tower of D_K is sub-asymptotic. The substrate's resonance modes are not adequately sampled until L_max ≥ 8. In Tesla-resonance terms: a cavity tuned by the lowest five modes is not the same cavity probed by the lowest fifty, and the impedance ratio between the two regulators flips between L=5 and L=8. **Every prior result anchored at L=5 is now provisionally re-openable at L ≥ 8 if it depends on regulator ratios** — but R-protected observables (whose Mellin slots cancel by construction, W8-89 MELLIN-CONE-UNIVERSALITY) are immune. The corridor of L_max-stable observables is now sharply delineated.

2. **The K-corridor is multiply walled and uniquely threaded** (W5-53 + W5-54 + W5-59 + W5-63 + W5-55 + W5-66). Three closure walls (regulator, floor, hull) eliminate the low-K corridor; one kinetic-pole wall (K_crit ≈ 91.5) caps the high-K corridor; one Landau-symmetry-class wall (N_OP = 8 framework vs N = 5 in 3He-B) anchors the corridor in the 3He-B parent-class. The remaining open surface for A_s closure is a **single resonant pathway**: K ∈ [K_R5 = 1.922, K_crit = 91.5], Branch-A baseline, H_tilde DC. This is the geometry the framework lives on; the observation that the resonant frequency for A_s closure is uniquely picked out by the wall structure is the strongest structural argument the framework has produced so far in the resonance-medium domain.

3. **Two-speed acoustic metric is structural and detector-inaccessible** (W4-39 + W4-41). The c_T/c_S = 2.062 ratio is a substrate-spectral-moment prediction that propagates through the slow-roll consistency relation to give a sharper tilt than single-speed inflation, and the prediction is structurally permanent (EVOI = 0) within the foreseeable LiteBIRD+CMB-S4 era. This is a Tesla-Test partial: can you measure it? — not on this generation. Can you build it? — yes, the prediction is computable. Does it resonate? — yes, on the spectral-moment ratio. The honest classification is "load-bearing prediction without a near-horizon detector."

4. **Three new universal theorems** (Mellin cone, A_F singleton, CMPP transit-invariance) **upgrade the framework's structural position from "framework-specific" to "spectral-triple-class-universal"**. The Mellin cone bound holds on any positive-measure spectral triple; A_F = ℂ⊕ℍ⊕M_3(ℂ) is the unique finite real noncommutative algebra of dim_ℝ ≤ 50 satisfying the 6 NCG axioms; the CMPP Type-D-static / Type-G-dynamic invariant holds across the 8 τ-checkpoints. The framework's MG-0 and MG-2 master-gear inputs are now DERIVED (not framework-empirical); only τ_fold remains as an empirical input, and even τ_fold is paired with a causal-censorship analog (W8-96 GEAR-CENSORSHIP).

5. **w_0 is permanently SCHEME-DEPENDENT; the DR3 rectangle is bound but the prediction is not** (W4-46 + W1b-9). The Wave-1 branch (iv) retraction and the Wave-4 L_max divergence jointly settle that w_0 does not have a single substrate prediction at the spectral-functional level. The R_842 = [−0.942, −0.742] × [−0.2, 0.2] rectangle remains LOCKED for the 2026-04-23 DR3 event under binary containment (LOCKOUT-C: no rectangle resizing), but its physical anchoring requires S85 re-audit at L_max ≥ 8. Under Zubarev-L9, w_0^pred = −0.997 lies outside R_842 by 0.055; under zeta-L9, w_0^pred = −0.494 lies far outside on the other side. The framework's binary commitment (R_842 contains it / does not) stands; the regulator-family interpretation of the outcome is the carry-forward.

6. **The α_s = n_s² − 1 identity is now an Ornstein-Zernike property of any single-pole rational propagator** (W8-86 + W10-123). The S50 framework-specific identity is upgraded to a representation-independent algebraic consequence of the OZ critical-fluctuation structure. The substitution chain `(n_s − 1)(n_s + 1) = n_s² − 1 = −4u/(1+u)²` with u := m²/(JK²) eliminates u; the closure under the minimal four-axiom set {CCM 2007 A1–A6, KO-dim=6, A_F singleton, Mellin kernel} requires zero auxiliary couplings and no observational n_s in the derivation chain. This is the framework's strongest "single resonance frequency" prediction: α_s = −0.068968 follows from n_s alone via an exact identity, with 9.62σ separation from Planck and 34.48σ from CMB-S4 null. **This is the calendar-year discriminator** on a 2030 horizon.

7. **Two FAILs trace to plan-design defects, not framework defects** (W8-85 + W10-119). The Wave-8 STATIONARY-POINT-TAU-FOLD FAIL was unanimously diagnosed by three independent audits as plan-mis-framing: τ_fold is a van Hove cusp of ρ(λ; τ), NOT a critical point of the bare Chamseddine-Connes Gaussian spectral action. The plan's Jensen ansatz `c_n ∈ {+1, −1, +1/2}` was empirically shown to lie outside the theoretically-permitted log-slope range [−1, +1] under the 3-exponential block decomposition. The Wave-10 Γ1' near-stationarity FAIL traces to the same structural fact: at a first-order phase transition (the fold), dS/dτ ≠ 0 by definition; the test asks "where is dS/dτ ≈ 0?" and the framework answers "never at τ_fold." 70 sessions of downstream τ_fold reasoning are not disturbed by either FAIL. **The lesson is that the substrate's resonance structure at the fold is non-stationary** (impulsive transit, Mach 13.75, supersonic) — not a quasi-static minimum — and any plan that assumes stationarity at τ_fold is asking the wrong question.

8. **V3-NON-COMPLIANT methodology closure is honest, not catastrophic** (W9 ladder). The session physics verdicts remain valid; only the methodology-closure ladder is deferred. This is the harness-enforced separation the v3 ladder was built to make: physics gates and methodology gates pass on different criteria, and methodology incompleteness does not retract physics.

**Conflicts across waves**: I find no direct contradictions across the 10 waves. The closest tension is between W1's branch (iv) retraction (which makes w_0 UNSPECIFIED) and W1b-9's R_842 lockout (which freezes the DR3 rectangle anchored on a now-retracted central value). Both source documents flag this explicitly: the rectangle binding is infrastructural; its physical anchoring is conditional on S85 re-audit. This is treated as a noted methodology consequence, not a contradiction. A second potential tension is between W4-39 PASS (n_T derivation matches G46) and W4-46 structural FAIL (w_0 regulator-dependent), with W4-39 being a c_T/c_S spectral-moment ratio (regulator-invariant by W2-15 admissibility) and W4-46 being a w_0 prediction whose Zubarev-vs-zeta split grows with L_max — these are CONSISTENT under the W2-15 layer-admissibility theorem (a_0 and a_2 spectral moments are L1-admissible across all 5 regulators in the atlas; w_0 sits at a slot that requires a regulator-specific fold-localization). The two waves are mutually consistent.

---

## V. Carry-Forward Computations

V.1. **L_max ≥ 8 spectral functional re-audit (replaces branch (iv))**
   - **What**: Re-enumerate w_0 branches at L_max = 8, 10, 12 in the inverted ξ_J > ξ_E_GGE regime; evaluate Mellin-cone Connes-Moscovici s=3 residues for monotone Cauchy decay; identify which of {ζ, Zubarev, alternative regulator} converges at the asymptotic limit.
   - **Inputs**: W1a-3 SV2 NPZ (R_JE drift table); D_K eigenspectrum cache at L_max = 8, 10, 12 (GPU-accelerated via torch.linalg on AMD RX 9070 XT, ROCm 7.2); W2-15 regulator-admissibility atlas; canonical ξ_J = 0.008911 from W1.
   - **Gate**: NEW S85-W0-L_MAX-8-BRANCHES PASS iff R_JE ratio asymptotes to a stable value within ±5% across L ∈ {8, 10, 12} for at least one regulator AND Mellin-cone residue differences are monotone-decreasing.
   - **Effort**: 2 sessions, GPU-mandatory (155,984 → ~1.2M eigenvalues at L_max=12).

V.2. **Branch-A baseline H_tilde DC tightening (sole surviving A_s pathway)**
   - **What**: Refine A_s(K=2.035, Branch-A, H_tilde-refined) at the post-W5-60 canonical_constants pin within the 0.89% log-DC window from W1a-1; cross-check at L_max=7.
   - **Inputs**: S83 G7 F_amp_lin = 1.026; W5-53 F_amp(N3LO) = 1.016 limit; W5-54 ξ(Zubarev) = 0.019646; W1a-1 H_tilde corridor [4.599e-3, 4.830e-3]; canonical_constants.py post-W5-60.
   - **Gate**: A_s(K=2.035, Branch-A, H_tilde-refined) within 1σ of Planck A_s = 2.1×10⁻⁹, OR convert to permanent structural WALL if residual > 3× at L_max=7 cross-check.
   - **Effort**: 1 session.

V.3. **K-FLOOR-WALL-JOINT registry landing**
   - **What**: Draft permanent-result block for §VII registry consolidating W5-54 + W5-59 + W5-63 as triple-supported wall ("K-floor wall is regulator-shift, A_s floor, and 4-hull exclusion"). Include the substitution chain showing regulator-shift acts on prefactor, not K_Ri.
   - **Inputs**: W5-54, W5-59, W5-63 scripts + data + WP sections; permanent-results-registry schema.
   - **Gate**: Landed registry entry with 3 cross-references; `/weave --update` confirms entry in knowledge index.
   - **Effort**: 0.25 session.

V.4. **CGWB / α_s flagship pre-registrations (LISA + CMB-S4)**
   - **What**: Formalize W6-50 (CGWB Ω_GW prediction at f ∈ {1e-4, 1e-3, 1e-1} Hz for branches A/C/LI) and W6-52 (α_s = −0.068968 ± framework-σ at Planck pivot, mapped to CMB-S4/CMB-HD/LiteBIRD timelines) in the predictions registry with detector-decision dates.
   - **Inputs**: W6-50 transfer_correction {0.5, 1.0, 2.0} bracket; W6-52 per-detector σ-forecast; LISA L2023+ sensitivity curve; CMB-S4 first-light date; sessions/framework/pre-registered-observations.md.
   - **Gate**: Two pre-registration documents landed with calendar-year mapping; SHA-pinned; LOCKOUTs codified.
   - **Effort**: 1 session.

V.5. **Alternative d_spec probe (heat-kernel + zeta-at-interior-s\* + rep-theoretic)**
   - **What**: Replace the boundary-dominated ζ_D(s) probe of W9b-105 (which gave d_spec = 4.895 from s* = 6.0 boundary) with three independent routes: heat-kernel small-t expansion (Tr e^{-tD²} ~ Σ a_k t^{(k-d)/2}), interior critical point of d²ζ/ds² scan, and rep-theoretic decomposition of the trace.
   - **Inputs**: W9b-105 ζ_D scan data; D_K eigenvalue cache at L_max=10; Connes-Chamseddine heat-kernel expansion in CCM 2007.
   - **Gate**: At least one route converges to d_spec ∈ [2.5, 3.5] supporting the cube-3 derivation OR formally certifies cube-3 route as closed; if all three FAIL, exp(12·τ_fold) "12" exponent moves to the alternative-derivation queue (V.6).
   - **Effort**: 1 session.

V.6. **μ_BC geometric-pin alternatives if cube-3 stays closed**
   - **What**: If V.5 returns no d_spec=3 route, derive the "12" exponent in μ_BC = M_Z·√(1 + exp(12·τ_fold)/3) via heat-kernel a_2 / a_0 ratio OR rep-theoretic SU(3)_C ⊕ SU(2)_L ⊕ U(1)_Y branching coefficients OR Kaluza-Klein tower threshold corrections.
   - **Inputs**: V.5 result; W9b-106 C² Cartan-trace decoupling theorem; KK tower at singleton (W7b-84, 128 eigenvalues).
   - **Gate**: One alternative route delivers "12" within 5% rel error from first principles, OR formally certify μ_BC numerical PASS as observation-only (no derivation).
   - **Effort**: 1 session.

V.7. **Two-speed acoustic metric prediction-detector mapping**
   - **What**: Verify that c_T/c_S = 2.062 from a_2/a_0 spectral moments is structurally preserved at L_max ≥ 8 (post V.1); compute n_T(k_CMB) under the L_max=8 spectrum; project R_realized for delensing > 50% and external A_lens prior from LSST κκ to test whether any 2030-2040 detector combination crosses the 1σ threshold.
   - **Inputs**: W4-39 derivation chain; W4-37 Fisher 3-param construction; LSST κκ forecast; W2-15 a_0 + a_2 L1-admissibility result.
   - **Gate**: c_T/c_S stable to ±5% at L_max=8; R_realized projection ≥ 0.5σ for at least one detector combination, OR confirm permanent EVOI=0 status.
   - **Effort**: 1 session.

V.8. **Mellin-balance template compliance lift (W6-71 carry-forward)**
   - **What**: Apply `.claude/templates/mellin-balance-pre-declaration.md` to all 16 enumerated S84 cluster-test gate blocks; re-dispatch W6-71 audit; lift compliance_fraction from 0.0 → 1.0; add "saturated-balanced / floor" subclass for zero-cluster gates.
   - **Inputs**: W6-71 template + audit script + 16-gate enumeration.
   - **Gate**: compliance_fraction = 1.0; re-dispatched W6-71 meta-gate PASSes.
   - **Effort**: 1 session (tedious; 16 gates × per-gate snippet derivation).

V.9. **Plan-PRDR consistency check for stationarity hypotheses**
   - **What**: Pre-registration audit that asks, for every gate involving τ_fold or any phase-transition point, whether the hypothesis IMPLIES or CONTRADICTS each cross-check; specifically codify "fold = van Hove cusp ⇒ dS/dτ ≠ 0" as a permanent plan-pin so W8-85-class FAILs do not recur.
   - **Inputs**: W8-85 3-agent audit synthesis; W2-HARMONIC-NOT-INSTANTON theorem; W10-119 Γ1' diagnostic; phononic-framing.md table.
   - **Gate**: NEW S85-PLAN-PRDR-CONSISTENCY PASS iff all τ_fold-touching plan blocks declare stationarity-status (stationary / non-stationary / van-Hove-cusp) and pass internal-consistency between hypothesis and cross-checks.
   - **Effort**: 0.5 session.

V.10. **L_max ≥ 11 asymptotic refit for CC-5 cluster spans (W3-31 carry-forward)**
   - **What**: Refit three CC-5 span series at L_max ∈ {3, 5, 7, 9, 11}; test whether Zubarev-exp dominance predicted for span_2 emerges past L_max=9; verify integer-ratio exponent structure (2:3:6) holds at higher L.
   - **Inputs**: W3-31 data; W3-35 L_max=11 cache (already computed).
   - **Gate**: Power-law fit R² > 0.99 on L_max=11 data AND exponent ratios still 2:3:6 within 1%.
   - **Effort**: 0.5 session.

V.11. **β_s pre-registration — running-of-running CMB-S4 discriminator**
   - **What**: Formalize β_s = −0.1331 (third-order Taylor coefficient of running-of-running, derived from W8-86 OZ identity at machine ε) as a zero-free-parameter pre-registration against CMB-S4.
   - **Inputs**: W8-86 OZ derivation; canonical n_s = 0.9649; W6-52 CMB-S4 detector forecast.
   - **Gate**: Pre-registration JSON landed in predictions registry; per-detector σ-forecast computed for CMB-S4, CMB-HD, LiteBIRD.
   - **Effort**: 0.5 session.

V.12. **f_B = c_S_canon coincidence test**
   - **What**: Test whether W5-64 INFO observation f_B_joint = 0.485 = c_S_canon is a closed-form identity or a 6-sig-fig coincidence; decompose f_B inversion chain to determine whether c_S_canon appears by construction or by physical input.
   - **Inputs**: W5-64 data; S83 G46 r_CMB derivation; sound-speed definitions at fold.
   - **Gate**: EITHER derive f_B_joint = c_S_canon analytically (structural identity, §VII candidate) OR show coincidental via L_max drift.
   - **Effort**: 0.75 session.

V.13. **Folded-triangle SHAPE template at 21-cm l_max=10⁵ (substrate-unique bispectrum)**
   - **What**: Distinguish the framework's substrate-unique folded-Bogoliubov bispectrum SHAPE template from ΛCDM at SKA-2 / 21-cm l_max=10⁵. The amplitude-running channel (W4-43) is closed; the SHAPE channel survives.
   - **Inputs**: W4-38 .npz (folded channel −0.080); 21-cm forecasts; folded-triangle template.
   - **Gate**: SHAPE template distinguishable from ΛCDM at SNR ≥ 2 in 21-cm bispectrum analysis.
   - **Effort**: 1.5 sessions.

V.14. **C² block decoupling registry landing**
   - **What**: Formalize W9b-106 Cartan-trace decoupling as permanent theorem in §VII registry; register as extension of S63 Cartan Trace Identity; rep-independence statement.
   - **Inputs**: W9b-106 derivation; sessions/permanent-results-registry.md.
   - **Gate**: Registry entry landed; `/weave --update` confirms.
   - **Effort**: 0.25 session.

V.15. **R_1 rank-distinguishability sharpening (G_2 vs F_4 vs A_3 vs C_3)**
   - **What**: Formalize W10-111 falsifiable prediction: R_1 distinguishes rank but not algebra-type at the same rank; identify the next-higher Mellin-balanced ratio R_2 = (a_0·a_6/a_2·a_4) or analog that breaks the A_3/C_3 degeneracy.
   - **Inputs**: W10-111 rank-universality theorem; Seeley-DeWitt moments a_0, a_2, a_4, a_6 for A_3 vs C_3.
   - **Gate**: R_2 (or analog) distinguishes A_3 from C_3 at machine ε while preserving R_1 rank-only behavior.
   - **Effort**: 1 session.

V.16. **V3 ladder closure in S85 (PRU + R3 + hooks remediation)**
   - **What**: Drive sig_1 from VETO to PASS by tagging 89 unpinned gates as `# (local)` or adding to canonical_constants.py; lift sig_4 from 28.1% to ≥90% via R3 YAML normalization; wire settings.json PostToolUse + Stop matchers per s84-w9a-98-settings-diff.md; re-evaluate ladder.
   - **Inputs**: W9-97 89-gate census; W9-100 R3 compliance map; s84-w9a-98-settings-diff.md.
   - **Gate**: sig_1 = 1, sig_4 = 1, sig_3 ≥ 0.8 coverage; ladder score ≥ CLOSED threshold (10.202).
   - **Effort**: 3 sessions distributed (PRU 2, R3 1, hooks 0.5).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Branch (iv) retraction at L=8 (W1a-3 SV2) | GEOMETRIC | RETRACTED | Spectral functional re-audit at L_max ≥ 8; ξ_J/ξ_E_GGE inverted ordering opens new branch family |
| 2 | K-FLOOR-WALL-JOINT triple-supported wall (W5-54+59+63) | GEOMETRIC | PERMANENT | Sole surviving A_s pathway: K ∈ [1.922, 91.5], Branch-A baseline H_tilde DC |
| 3 | Two-speed acoustic metric n_T = −r·c_T/(8·c_S) (W4-39) | PHONONIC | PASS (EVOI=0 to 2030-2040) | c_T/c_S = 2.062 from a_2/a_0; structurally permanent, detector-inaccessible |
| 4 | CMPP Petrov transit-invariance (W8-95) | GEOMETRIC | PERMANENT | Type-D static / Type-G dynamic across τ; phase-transition CMPP-invisible |
| 5 | Mellin cone universality [1.5, 2.5] (W8-89) | GEOMETRIC | PERMANENT (substrate-independent) | MG-0 inheritable from any positive-measure spectral triple |
| 6 | A_F singleton ℂ⊕ℍ⊕M_3(ℂ) (W8-87b) | GEOMETRIC | PERMANENT | MG-2 promoted from empirical to derived; 3,907→1 |
| 7 | C² block Cartan-trace decoupling (W9b-106) | PARTICLE | PERMANENT | Rep-independent zero; discharges μ_BC obligation (ii); extends S63 trace identity |
| 8 | R_1 rank-universality theorem (W10-111) | GEOMETRIC | PERMANENT | n_0 + n_4 − 2 n_2 = 0 exact; R_1 sees rank only, blind to algebra type |
| 9 | b_power Weyl asymptote → 7 (W7b-76) | GEOMETRIC | PERMANENT (analytic) | a_4 → a_2 → Weyl-7 crossover; IKKT b=1 excluded analytically |
| 10 | α_s = n_s² − 1 OZ identity (W8-86 + W10-123) | PHONONIC | PERMANENT (axiomatic n_aux=0) | Single-pole rational propagator property; 9.62σ Planck, 34.48σ CMB-S4 |
| 11 | CGWB / α_s 2030-2035 discriminators (W6-50+51+52) | PHONONIC | PASS, observational | 3 detector-accessible channels for branch (A)/(C)/(LI) discrimination |
| 12 | w_0 SCHEME-DEPENDENT permanently (W4-46) | GEOMETRIC | structural FAIL classified | DR3 R_842 binding remains; physical anchor pending L≥8 re-audit |
| 13 | μ_BC_K3 = 188.185 GeV (W1b-4) | PARTICLE | PASS at 0.082% | Numerical match; cube-3 derivation route blocked (W9b-105), C² obligation discharged |
| 14 | Z_R counterterm at f_conv slot (W6-67) | GEOMETRIC | structural FAIL | Renormalization obstruction is vertical (Mellin-slot regulator-dependent), not perturbative |
| 15 | W2-EPOCH-GATING + W2-HARMONIC-NOT-INSTANTON theorems (W1b-10) | GEOMETRIC | PERMANENT | 3PI epoch transit bounded ≤7.52e-5; small saddles cannot be classified as tunneling |
| 16 | K_* = coth(1) = 1.3130 lab match at 1.13% (W5-58) | PHONONIC | PASS (3He-B inheritance) | Framework is 3He-B superset (N_OP=8 vs 5); +3 SU(3)-internal directions |
| 17 | α_s partition-invariance under Leggett-Bogoliubov (W5-62) | PHONONIC | PASS | S50 single-parameter strengthened to single-parameter + partition-invariant at 0.2% |
| 18 | LiteBIRD n_T inaccessibility (W4-37 + W4-41) | PHONONIC | PERMANENT (EVOI=0) | R_realized 654× below 1σ in 2030-2040; ZFP-flagged but structurally invisible |
| 19 | UHF-GW physical gap +18.74 OOM (W4-47) | PHONONIC | structural WALL | UHF roadmap floor 10⁻²⁰ still 38.74 OOM above framework Ω_γ at 1 mHz |
| 20 | V3-NON-COMPLIANT methodology closure (W9 ladder) | NON-PHONONIC | deferred to S85 | Physics verdicts intact; sig_5 only of 5 ladder signals; remediation queued |
| 21 | W8-85 + W10-119 plan-defect FAILs | NON-PHONONIC | classified plan-defect | Substrate at fold is non-stationary (impulsive transit); plans assuming stationarity ask wrong question |
| 22 | Heterotic embedding admitted, geometric base + det(P) NOT (W7a-72+73+74) | GEOMETRIC | structural | "Rep-content guest, structural stranger" — SM content embeds via E_8 chain; spectral-triple identity does not |
| 23 | n_s as first nonlinear/quasi-CC-5 exception (W3-28) | PHONONIC | INFO | SDW + lattice-BR match Planck n_s = 0.9649 within 1σ; nonlinear quadratic+linear in ρ = a_4/a_2 suppresses bare span 4.61 → 0.21 |
| 24 | Borel summability floor at 4.7 OOM safety (W10-121) | GEOMETRIC | PASS | min(S_inst) = 2.42×10⁵ vs Borel threshold 4.34; semi-classical predictions on clean foundation |
| 25 | μ-distortion strictly linear in K, γ=1 exact (W5-57) | PHONONIC | INFO | Max μ = 8.69×10⁻⁵ at K=3.56×10⁵; PIXIE-visible at corridor endpoint; γ=1 protection |

---

*End of S84 Tesla-Resonance synthesis. The substrate's resonance cavity is more universal in three new theorems (Mellin cone, A_F singleton, CMPP transit-invariance), more sharply walled in one corridor (K-FLOOR-WALL-JOINT), and more honestly L_max-dependent in two regulator-sensitive predictions (w_0, Z_R counterterm at f_conv). The framework's branch ambiguity becomes detector-decidable on a 2030-2035 horizon (LISA, CMB-S4, multi-observable joint). The α_s = n_s² − 1 prediction is now an Ornstein-Zernike single-pole-rational property, axiomatically closed under {CCM 2007, KO-dim=6, A_F singleton, Mellin kernel}. Two FAILs trace to plan-design defects (assuming stationarity at a non-stationary fold); 70 sessions of downstream τ_fold reasoning unaffected. Methodology closure deferred to S85 (V3-NON-COMPLIANT, sig_5 only); physics verdicts intact.*
