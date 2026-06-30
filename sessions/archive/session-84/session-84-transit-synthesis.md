# Session 84 Synthesis: Transit Dynamics — Bogoliubov Pump, Two-Speed Tilt, Kinetic Pole, and Van Hove Reframing

**Date**: 2026-04-19
**Agent**: transit-dynamics-theorist
**Source Documents**:
- `sessions/archive/session-84/session-84-synthesis-collation.md` (verbatim collation of W1-W10 syntheses)

This synthesis is from the non-equilibrium-particle-production / Bogoliubov-pump perspective: which S84 results bear on the impulsive transit through the van Hove fold, on the squeezed-state amplitude A_s, on the kinematic regime of the Mukhanov-Sasaki equation, and on the GGE relic spectrum. The orchestrator-level "session synthesis" is for tesla; this is the dynamics view.

---

## I. Session Outcome

S84 reframes the entire post-S83 A_s closure problem from a "dynamics rescue" search into a **baseline H̃ derivation problem inside a 0.89% log-window**, while simultaneously identifying that the pre-S84 variational language at τ_fold (Chamseddine-Connes Gaussian stationarity) was a plan-defect: **τ_fold is a van Hove cusp of ρ(λ; τ), not a critical point of any bare spectral action** (W8a-85 unanimous 3-agent audit). The dynamics-side of A_s is structurally walled (W1a-2 F_supp_max = 1.044 against 1.10; 6 channels × 44-1400× short per S83); the baseline side is open but narrow with the canonical TD anchor sitting 1.57× above the band centre (Δ_OOM = +0.196). Two new transit-dynamics-relevant theorems land: the two-speed tensor-tilt identity n_T = -r·c_T/(8·c_S) (W4-39, GEOMETRIC) and the Borel-floor confirmation min(S_inst) = 2.42×10⁵ at 4.7 OOM safety above the threshold 4.34 (W10-121, GEOMETRIC). The kinetic crossover at K_crit ≈ 91.5 (W5-55) restricts the corridor where the Mukhanov-Sasaki acoustic approximation is even applicable. Branch (iv) of the w_0 ledger is **retracted at SV2** — a textbook Bogoliubov-truncation failure where the L_max=5 anchor is a non-convergent sample of its own tower (R_JE drifts 0.45 → 4.99 over L_max ∈ {5,6,7,8}).

---

## II. Key Results

### W1 — A_s Rate-Limiter Relocated to Baseline H̃ (PASS)

**Result**: H̃ ∈ [4.599×10⁻³, 4.830×10⁻³] PASS-1.05 window with 0.8901% log-measure; CC3 identity d(ln A_s)/d(ln H̃) = +2 verified to 1.835×10⁻¹². Classification: PHONONIC (substrate Hubble parameter sets the squeezed-state amplitude through the Bogoliubov pump |β_k|² ∝ H̃²).

The dynamics-rescue corridor for A_s is now structurally closed. W1a-2 returned F_supp_max = 1.0438 against the 1.10 threshold — 56 ppt short — and the 6-channel joint ceiling was both pre-registered and Python-verified. The substitution chain from F_supp to A_s is multiplicative-in-log: F_supp < 1.10 with PASS-target ratio 1.57 means even maxed-out dynamics dressing closes at most ~10% of the log-gap. The closure problem is therefore **moved**, not solved: S85+ baseline derivations of H̃ from the substrate spectral structure must land inside the 0.89% log-window.

The CC3 identity is the load-bearing structural fact for transit dynamics:
- **Definition**: P_ζ ∝ H̃²/(ε_H · M_Pl²) under canonical Mukhanov normalization with z² = 2 ε_H a² M_Pl² (Mukhanov-Sasaki convention, Birrell-Davies §3.3).
- **Substitution**: A_s = (k³/2π²) · |v_k|²/z² evaluated at horizon-crossing pin.
- **Simplification**: at fixed ε_H and dressing, ln A_s = 2 ln H̃ + const ⇒ d(ln A_s)/d(ln H̃) = +2 (exact).
- **Direction**: a 2.38 OOM gap in H̃ at the canonical/branch-B endpoint propagates linearly to a 4.76 OOM gap in A_s. **Verified numerically: 2 × 2.38 = 4.76.**

The TD anchor H̃ = 5.9076×10⁻³ sits 1.57× above the band centre 3.78×10⁻³ (Δ_OOM = +0.196); the LI endpoint H̃ = 2.464×10⁻⁵ produces A_s = 5.74×10⁻¹⁴ (Δ_OOM = -4.56). The TD/LI divergence chase is now the rate-limiting open question for A_s closure, not a cosmetic ledger discrepancy.

### W1 — Branch (iv) Retracted at SV2 (Truncation-Tower Failure)

**Result**: Branch (iv) w_0 = -0.842 anchor at L_max=5 retracted; w_0 canonical declared UNSPECIFIED pending S85 re-audit. Classification: GEOMETRIC (spectral functional convergence on the L_max-truncated tower).

This is structurally the most weighty finding of W1 from the transit perspective. SV1 reproduced w_0 = -0.842454 cleanly at L_max=5 (|Δ| = 2.76×10⁻⁷, four OOM inside tolerance); SV2 then scanned L_max ∈ {5,6,7,8} and found:
- R_JE = ξ_J/ξ_E_GGE drifts monotonically: 0.4536 → 1.041 → 2.411 → 4.985 (factor 11× over the scan).
- Connes-Moscovici s=3 residue differences are 1.91×10⁴ → 3.11×10⁴ → 3.84×10⁴ — **not monotone-decaying** ⇒ Mellin-cone Cauchy decay fails.

The physical mechanism is exactly the kind of failure mode a Bogoliubov-aware analyst should flag: ζ-weighted energy moment S_ζ_E grows polynomially in L_max (multiplicity × linear-λ weight ~ L⁴) while Zubarev-weighted S_Zub_E saturates Gaussian-fashion beyond λ ~ 1. Their ratio ξ_E_GGE drops by 11× from L=5 to L=8; ξ_J (TB-pinned at 0.008911) is L-independent, so R_JE inherits the divergence.

**At L_max=8 the Josephson sector dominates the GGE sector** — the ordering inverts. The L=5 anchor is a pre-asymptotic snapshot of a divergent integral; the physical w_0 at the asymptotic spectral limit is in a different branch family than what was pinned in S58/S82/S83. Retraction is the correct response to a transfer-matrix calculation whose "matched" eigenmode ladder is non-convergent in its own truncation parameter. Per plan reversion protocol: branch (iv) struck; SV3+SV4 aborted (parameter sensitivity scans of a retracted branch are vacuous).

### W4-39 — Two-Speed Tensor Tilt n_T = -r·c_T/(8·c_S) (PASS)

**Result**: n_T(k_CMB) = -3.024×10⁻³ matching the ε_H-flow-transfer benchmark to 2.36×10⁻⁵; classification: GEOMETRIC (ratio of spectral moments a_2/a_0 of the Dirac operator).

This is the substrate's first-principles correction to the slow-roll consistency relation, and it goes the right direction for the impulsive transit. Substitution chain (verified numerically):
- **Definition** (single-speed slow-roll): n_T = -r/8 from the consistency relation P_t/P_ζ = 16 ε_H = r combined with n_T = -2 ε_H. At r = 0.0117 this gives n_T_single = -1.4625×10⁻³.
- **Substitution** (two-speed substrate, c_T ≠ c_S): n_T = -r·(c_T/c_S)/8 with c_T/c_S = a_2/a_0 = 2.062 (spectral moment ratio of D_K, not a regulator choice).
- **Simplification**: n_T_two = -0.0117 × 2.062 / 8 = -3.0157×10⁻³.
- **Direction**: c_T/c_S > 1 makes |n_T_two| > |n_T_single| by exactly the ratio. **MORE NEGATIVE by factor 2.062. Verified: |n_T_two|/|n_T_single| = 2.062.**

What this means physically: the transit through the van Hove fold modifies the dispersion relation for the tensor mode differently from the scalar mode (different spectral moments of D_K control them). The tensor mode propagates at c_T = √(a_2/Vol) while the curvature mode propagates at c_S = √(a_0/Vol) (schematic; full normalization in W4 source). The two-speed metric is *forced* by the spectral triple's distinct second-moment-vs-zeroth-moment structure — it is not a free dial. W4-48 flags this as a ZFP (zero-free-parameter) channel: c_T/c_S derives from spectral moments, not regulator shopping. The downstream W4-37 result (LiteBIRD+CMB-S4 σ(n_T)_joint_3yr = 0.0654) means the framework's predicted |n_T| sits 654× below 1σ — the prediction is detector-inaccessible for the 2030-2040 window per W4-41 EVOI=0 registration. This is a structural-permanent inaccessibility result.

### W5-55 — Kinetic Crossover at K_crit ≈ 91.5 Restricts the Mukhanov-Sasaki Corridor (FAIL)

**Result**: max |Δn_s| = 23.85 along the K-corridor; ε_eff = 0.02223 · K/K_anchor crosses unity near K ≈ 91.5; for K > K_crit the Mukhanov-Sasaki derivation is inapplicable. Classification: PHONONIC (acoustic mode equation regime boundary).

This is exactly the regime-of-validity diagnosis a non-equilibrium QFT specialist must enforce. The Mukhanov-Sasaki equation u_k'' + (k² c_s² − z''/z) u_k = 0 has a slow-roll regime of validity bounded by ε_H ≪ 1; once ε_eff crosses unity the mode equation is no longer governed by the slow-roll potential expansion and the n_s formula derived from it is meaningless in the kinetic sub-corridor. W5-66's Landau classification (N_OP = 8 vs Volovik 3He-B's N = 5) holds **conditionally** on this restriction.

The substantive consequence for the framework: the K-corridor is multi-sub-phase. The inflationary sub-corridor K ∈ [K_R5 = 1.922, K_crit ≈ 91.5] is where MS-derived n_s is well-defined; K > K_crit is the kinetic sub-corridor where the framework owes either a different mode equation or a re-derivation of n_s in the relevant kinematic regime. Per the regime-of-validity discipline (every approximation states its regime), the W5-65 K_FIRAS = K_FIRAS K = 3.68×10⁵ "identity" residual 3.50% is in the kinetic phase and is therefore a coincidence diagnostic, not a closed-form physical identity.

### W5-58 + W5-66 — 3He-B Inheritance Upgraded (PASS + INFO)

**Result**: K_* = coth(1) = 1.3130 matches measured 3He-B to 1.13% (W5-58 PASS at ratio 0.01133); framework G/H gives N_OP = 8 vs Volovik N = 5 (W5-66 INFO). Classification: PHONONIC (analog-gravity laboratory inheritance).

This is the cleanest analog-gravity / parent-child inheritance result of the session. The framework's spectral triple is a **superset** of the 3He-B BCS structure: framework AZ class BDI sits inside Volovik's 3He-B BDI-TCI submanifold; framework adds 3 SU(3)-internal directions to Volovik's 5 native order-parameter components. K_* = coth(1) is the laboratory observable corridor boundary. Any p-wave BCS superfluid Δ/k_B T_c measurement tests the framework's K_* pin to ~1% precision via its inherited 3He-B sector.

The transit-dynamics relevance: 3He-B is an analog of the substrate transit, and the substrate is the parent — **inheritance is parent → child, not analogy** (per project memory `project_3heb-inheritance.md`). Any GGE quasiparticle relic computation done in 3He-B language has a corresponding substrate computation; the 3-extra SU(3) directions are where the framework's predictions exceed the laboratory analog.

### W6-50 + W6-51 + W6-52 — Three-Channel Observational Discriminator on Branch (PASS×3)

**Result**: branch-ambiguity (H_TD vs H_mixed-C vs H_LI) discriminable on three independent detector grids. Classification: PHONONIC (squeezed-state amplitude propagating into observable channels).

- W6-50 (LISA/DECIGO/BBO, ~2035): Ω_GW max ρ_AC = 2.10 decades; h_c^(A)(3 mHz) = 7.17×10⁻¹² is 11 OOM above LISA floor.
- W6-52 (CMB-S4, ~2030): α_s = n_s² − 1 = -0.069 at 34.48σ on CMB-S4, 53.05σ on CMB-HD, 64.31σ joint.
- W6-51 (multi-observable joint): 3 observables {A_s, P_t, μ} carry the H̃² prefactor; rank-3 joint σ improvement √3.

This converts the branch-divergence (which transit-dynamics has been chasing since S78 W1-1 W3-E branch decision) from an internal-bookkeeping ambiguity into a calendar-year detector-decidable question. The W̃² prefactor scaling is the squeezed-state amplitude pump — the same Bogoliubov factor that determines |β_k|² in the post-transit GGE relic. Three channels mean the framework cannot dodge any single detector failure; it must pass on all three or be falsified.

### W6-67 vs W6-68/69/70 — A_s Renormalization Closed Except at the f_conv Slot

**Result**: A_s amplitude is renormalization-regulator-independent, T4-theorem-consistent, dual-expansion convergent (W6-69 + W6-70 + S83-G35 + S80-G16) — but the Z_R counterterm DOES NOT extend from f_conv to a_2 (W6-67 cluster_Z_a2 = 107466, growing with L_max). Classification: PHONONIC.

From the transit-dynamics perspective: the renormalization obstruction is **vertical** (regulator-dependent a_2 at one Mellin slot), NOT **perturbative** (no 1/N divergence). W6-69 PASS: F_amp^3PI is clause-(b) FI at machine epsilon — the 3PI self-energy and Mukhanov z_R² normalization are inverse counterparts in A_s reconstruction (product_ratio = 1 across {ζ, Zubarev, SDW, dim-reg, lattice-BR}). W6-70 PASS: 1/N_field convergence at 2,445× margin below ε_H. Combined, this means the canonical A_s = 5.08×10⁻⁹ pin-map (W3-34) is structurally clean as a Bogoliubov amplitude — the multiplicative renormalization at the field-sector level converges. The stuck slot is f_conv, where Z_R is structural (not numerical), and S83-G28's cluster=1766 is now correctly recognized as **structural regulator obstruction** rather than an un-dressed-coupling artifact.

### W7b-75 / W7b-76 — b_power Drifts to Weyl Asymptote d_int − 1 = 7

**Result**: b_power drifts 4.681 (L≤8) → 4.988 (L≤12) → 5.016 (all); SDW prediction matches drift analytically. Asymptote is the Weyl coefficient d_int − 1 with d_int = 8 (since d_total = 12 at KO-dim=6, internal dimension = 8). Classification: GEOMETRIC.

This is a structural strengthening, not a setback. The W7b-75 FAIL was anticipated as a PASS but the W7b-76 SDW symbolic match upgrades the framework's position from "b = 4.681 locked (could fall at L=16)" to "b interpolates a_4 → a_2 → Weyl-7 with explicit symbolic formula." The IKKT b=1 alternative is now excluded **analytically** via Weyl d_int − 1 = 1 ⇒ d_int = 2, incompatible with d_total = 12 at KO-dim=6. From the transit-dynamics view: the spectral functional's heat-kernel asymptotics are governed by the Weyl coefficient at the internal-dimension upper bound; the transit through the fold occurs within this convergence corridor and is not an artifact of pre-asymptotic finite-L₁₂ truncation.

### W8a-85 (Audit) — τ_fold IS NOT a Critical Point of the Bare Spectral Action

**Result**: 3-agent unanimous audit (connes-ncg + baptista + spectral-geometer) classifies the W8-85 FAIL as PLAN-DEFECT not framework-defect. **τ_fold = 0.190 is a van Hove cusp of ρ(λ; τ)**, not a critical point of the bare Chamseddine-Connes Gaussian spectral action. Classification: GEOMETRIC.

This is the structurally most important reframing of the session for the transit picture. The substrate-language convention has always been "Jensen deformation parameter τ driving spectral action gradient dS/dτ = +58,673" (per `phononic-framing.md`). The W8-85 plan asked "is dS/dτ = 0 at τ_fold?" — but the framework explicitly answers "no, it is +58,673" (substrate-language equivalent of "the inflaton is rolling supersonically through the fold"). The plan was **algebraically self-contradictory** between its hypothesis and its cross-check.

What actually selects τ_fold is a **van Hove singularity of the spectral density**: ρ(λ; τ) develops a square-root cusp at a level-crossing in the Jensen-deformed D_K spectrum. The transit is impulsive (Mach ≈ 13.75 per substrate-language ledger) precisely because τ_fold sits at a cusp where the spectral density's λ-derivative diverges. This is the substrate analog of crossing a van Hove fold in a tight-binding spectrum: the density of states diverges, the dispersion linearizes locally, and a sound mode becomes critical. **The Bogoliubov coefficients computed at τ_fold are governed by a cusp passage, not by a saddle-point through a smooth potential.** This is exactly the regime where the sudden / diabatic approximation applies (delta_t → 0 limit), and where the Bogoliubov |β_k|² is bounded by the cusp's scaling exponent rather than by an exponential WKB factor.

S85 carry-forward S85-VAN-HOVE-CUSP-THEOREM (HIGH priority) should formalize this — the variational principle is on ρ(λ; τ), not on the bare spectral action.

### W8-87b + W8-89 — A_F Singleton + Mellin Cone Universality (PASS-THEOREM × 2)

**Result**: A_F = ℂ⊕ℍ⊕M_3(ℂ) unique under {KO-dim=6, first-order, orientability, Poincaré duality, CCM admissibility, SM hypercharge}; Mellin cone empty-gap [1.5, 2.5] holds across 3 framework-independent positive-measure spectral triples. Classification: GEOMETRIC + PARTICLE.

The transit-dynamics reading: the spectral triple is now uniquely pinned (Birkhoff-classification) at the algebra level; the Mellin cone separating R-protected vs NOT-R-protected observables is **inheritable from any positive-measure spectral triple** (commutative S¹, NC torus, ℝ⊕M_2⊕M_3 all reproduce span = 1 exactly for R-protected and ≥ 14.6× for NOT-R-protected). This means the framework's A_s pin-map structure is a **universal feature** of positive-measure variational forms, not a framework-quirk. The squeezed-state amplitude calculation can be ported to any positive-measure spectral triple; the cusp-scaling of the Bogoliubov coefficients at τ_fold inherits from the universal cone bounds.

### W8-86 — α_s = n_s² − 1 as Ornstein-Zernike Identity (PASS at machine ε)

**Result**: rel_err = 1.23×10⁻¹⁵; the S50 identity is an algebraic consequence of any single-pole rational propagator P(K) = T/[J_eff·K² + m²] — a property of OZ critical fluctuations, not framework-specific. Classification: PHONONIC.

This is the deepest structural finding for the squeezed-state spectrum. The transit through the fold produces a GGE relic whose two-point function has a single-pole OZ form near criticality; α_s = n_s² − 1 is then **forced** algebraically. Substitution chain (per W10-123): with u := m²/(J K²), (n_s − 1)(n_s + 1) = n_s² − 1 = -4u/(1+u)² = α_s; u eliminates. New zero-free-parameter prediction registered: β_s = -0.1331 (running of the running, 3rd-order Taylor coefficient) pre-registered against CMB-S4. The W8-88 result is the safeguard: ∂Λ_CC/∂τ = 0 exactly (S44 permanent a_0 τ-independence) means α_s and CC are **structurally independent** — the CMB-S4 34σ α_s discriminator is robust against any CC-regulator disagreement.

### W10-121 — Borel Floor Confirmed (PASS, min(S_inst) = 2.42×10⁵, 4.7 OOM safety)

**Result**: min(S_inst) over Jensen-τ ∈ [0.05, 0.35] = 2.42×10⁵; Borel threshold 4.34; ratio = 5.58×10⁴ ⇒ log₁₀(2.42e5/4.34) = 4.75 OOM safety margin. Classification: GEOMETRIC.

**Verified numerically**: log₁₀(2.42e5 / 4.34) = 4.7463, matches the claimed 4.7 OOM. The §W2-HARMONIC-NOT-INSTANTON theorem (W1b-10) retains full applicability domain: the Jensen-τ flow inside [0.05, 0.35] has NO genuine bound saddle; the only τ-stationary point is at τ* = 0.3746 (just past the upper scan boundary). For transit dynamics this means: there is no instanton-mediated tunneling alternative to the impulsive transit; the supersonic crossing of the cusp is the only relevant trajectory in the Borel-summable saddle landscape. The S_inst = 0.203 small-saddle that S82-G7 flagged is Gaussian quadratic, not WKB tunneling — reinforced by W1b-10's PERMANENT theorem.

### W10-119 — τ_fold Unique Under Γ6 (Cubic-BC), Not Under Γ1' (Same Reframing as W8-85)

**Result**: 0/2001 mesh points satisfy Γ1' near-stationarity criterion, but Γ6 (cubic-BC) alone picks τ = 0.190 uniquely (1/2001). The Γ1' criterion |dS/dτ|/|dS_fold| < 0.134% is **structurally incompatible** with τ_fold's definition as a van Hove singularity / first-order transit point with definitionally NONZERO dS_fold = +58,672.80. Classification: GEOMETRIC.

Same structural fact as W8a-85 audit, surfacing in a different gate. The framework's τ_fold uniqueness is correctly diagnosed under the cubic-BC Mellin-mesh constraint Γ6; the stationarity-based predicate Γ1' is the broken predicate. From the transit-dynamics view this is the clean confirmation that the fold is a kinematic boundary (cusp, first-order), not a potential extremum.

---

## III. Gate Verdicts

Filtered to gates that bear directly on transit-dynamics (mode equation, Bogoliubov amplitude, GGE spectrum, regime-of-validity, parametric amplification). Verdicts copied verbatim from collation; not re-adjudicated.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W1a-1 BASELINE-HTILDE-SENSITIVITY | PASS | log-measure 0.8901% in [4.599e-3, 4.830e-3]; CC3 +2 to 1.835e-12 |
| W1a-2 DYNAMICS-DRESSING (anti-) | FAIL | F_supp_max = 1.0438 vs 1.10 |
| W1a-3 SV2 (branch iv) | FAIL | R_JE drift 0.45 → 4.99 over L_max ∈ {5..8} |
| W1b-7 ALPHA-S-PRE-REGISTRATION | PASS | α_s = -0.068968; 9.62σ from Planck, 34.48σ from CMB-S4 null |
| W4-37 LB-CMBS4-JOINT-SIGMA-NT | FAIL | σ(n_T) = 0.0654 vs 0.06 ceiling |
| W4-38 ALPHA-F-NL-FRAMEWORK-PRED | FAIL | α_f_NL = -0.143 (\|α\| < 0.30); sign NEGATIVE 3 channels |
| W4-39 N_T-CMB-TRANSFER (two-speed) | PASS | n_T = -3.024×10⁻³; matches ε_H benchmark to 2.36×10⁻⁵ |
| W4-41 BLUE-TRANSIT-INACCESSIBILITY | PASS | EVOI = 0; R_realized = 1.53×10⁻³ (654× below 1σ) |
| W4-43 SKA-1 ALPHA SNR | FAIL | SNR = 0.0279 (71.8× below 2) |
| W4-46 G51-LMAX-CONVERGENCE (w_0) | structural FAIL | split factor 6.22× over L=5→9 |
| W4-47 UHF-GW-THRESHOLD | PASS | physical gap +18.74 OOM above framework |
| W5-53 NNLO-ΔF_amp | INFO | F_amp(N3LO) = 1.016, 3.16× short of 0.4454 |
| W5-54 K-FLOOR-REGULATOR | FAIL | Zub/ζ factor 50.9× |
| W5-55 N_S-CORRIDOR-MONOTONICITY | FAIL | kinetic-pole at K_crit ≈ 91.5 |
| W5-58 K_*-LAB-FRAMEWORK-MATCH | PASS | ratio 1.13% (3He-B inheritance) |
| W5-59 BRANCH-B-AS-FLOOR | INFO | A_s_floor = 5.74×10⁻¹⁴ (4.56 OOM below Planck) |
| W5-62 ALPHA_S-LEGGETT-PARTITION | PASS | \|Δα_s\|/\|α_s\| = 1.56×10⁻³ (32× inside) |
| W5-63 K-FLOOR-REACHABILITY | FAIL | 0/5 targets in 4-hull [1.922, 2.185] |
| W5-66 LANDAU-SYMMETRY-CLASS | INFO | N_OP = 8 (3He-B + 3 framework-unique) |
| W6-50 CGWB ABSOLUTE P_t | PASS | h_c(3mHz) = 7.17×10⁻¹² (11 OOM above LISA) |
| W6-51 SIBLING OBSERVABLES | PASS | 3 observables H̃²-prefactored |
| W6-52 ALPHA_S-CMB-S4 | PASS | 34.48σ CMB-S4, 53.05σ CMB-HD |
| W6-67 Z_R COUNTERTERM | FAIL | cluster_Z_a2 = 107466, growing with L_max |
| W6-69 F_AMP^3PI FI | PASS | product_ratio span = 1.0 (machine ε) |
| W6-70 FIELD-EXPANSION CONVERGENCE | PASS | NLO = 8.85×10⁻⁶ (2,445× below ε_H) |
| W7b-75 B-POWER-STABILITY | FAIL | b drifts 4.68 → 5.02 over L ∈ {8..12} |
| W7b-76 SDW-B-PREDICTION | PASS | b_asymp → 7 (Weyl d_int − 1) |
| W7b-83 §VII.O REGISTRY LANDING | PASS | rank-6 gear-master with two-scale b predicate |
| W8-85 (3-AGENT AUDIT) | FAIL (PLAN-DEFECT) | τ_fold IS a van Hove cusp, NOT a SA critical point |
| W8-86 ALPHA_S-OZ-IDENTITY | PASS (machine-ε) | rel_err = 1.23e-15 |
| W8-87b A_F BIRKHOFF | PASS-THEOREM | 1/3,907 algebra survives 6 axioms |
| W8-89 MELLIN CONE UNIVERSALITY | PASS-THEOREM | 3/3 framework-independent triples |
| W8-95 CMPP PETROV INVARIANCE | PASS | Type-D static, Type-G dynamic across 8 τ-points |
| W10-119 GEAR-GAMMA-1' (anti-) | FAIL (predicate) | 0/2001; Γ6 alone picks τ = 0.190 |
| W10-121 BOREL-SUMMABILITY-FLOOR | PASS | min(S_inst) = 2.42×10⁵; 4.7 OOM above 4.34 |
| W10-123 ALPHA_S AXIOMATIC | PASS | n_aux = 0; α_s = n_s² − 1 from {CCM A1-A6, KO-6, A_F singleton, Mellin} |

---

## IV. Structural Implications

### What Closed for Transit Dynamics

1. **Dynamics-rescue corridor for A_s** (W1a-2 + S83 W2 6-channel exhaustion). The squeezed-state amplitude cannot be fixed via dressing; it must be derived via the baseline H̃ pump term in the Mukhanov-Sasaki normalization. This is structurally clean from the Bogoliubov perspective: |β_k|² ∝ H̃² and no amount of post-pump dressing can change this scaling.

2. **τ_fold as variational stationary point of the bare SA** (W8a-85 unanimous audit + W10-119). The substrate's τ-driver dS/dτ = +58,673 is a defining nonzero quantity, not zero. The fold is a kinematic boundary (van Hove cusp), not a potential minimum. This finally aligns the variational language with the substrate-framing convention codified in `phononic-framing.md`.

3. **Branch (iv) at L_max=5 as a w_0 canonical** (W1a-3 SV2). The L=5 anchor was a non-convergent sample of its own spectral tower; ξ_J/ξ_E_GGE inverts at L_max=8. Any pre-S84 calculation that propagated the -0.842 anchor through Bogoliubov dynamics needs to be flagged as conditional on S85 re-audit.

4. **K > K_crit ≈ 91.5 as a physical corridor** (W5-55 + W5-66). Beyond this kinematic-pole, ε_eff > 1 and the Mukhanov-Sasaki acoustic approximation is inapplicable. The K-corridor is sub-phased.

5. **IKKT b=1 alternative** (W7b-76 analytic). Excluded by Weyl d_int − 1 = 7, requiring d_int = 8 = d_total − 4 at KO-dim=6.

### What Opened

1. **Baseline H̃ derivation inside 0.89% log-window** (W1a-1). The transit-dynamics task is now: derive H̃ from substrate first principles to land within [4.599×10⁻³, 4.830×10⁻³]. The TD anchor is +0.196 OOM above the band centre; a 1.57× downward correction is needed. Rate-limiting open question for A_s closure.

2. **Van Hove cusp variational principle** (S85 carry-forward from W8a audit). Reformulate τ_fold selection as a critical-point of ρ(λ; τ), not S(τ).

3. **Three observational discriminator channels** on H̃ branch (W6-50/51/52). LISA, CMB-S4, multi-observable joint — calendar-year decision points 2030-2035.

### What Shifted (Constraint-Map Refinement)

- **K-floor wall is triply supported** (W5-54 regulator + W5-59 floor + W5-63 hull) ⇒ K-FLOOR-WALL-JOINT registry candidate. The squeezed-state amplitude pump cannot reach the low-K corridor [1.0, 1.7] at any of the 4 conventions.
- **w_0 is permanently SCHEME-DEPENDENT** (W4-46 structural). The framework does not make a single-value ZFP prediction for w_0. R_842 [-0.942, -0.742] DR3 rectangle pre-registration locked but its centre is now formally branch-conditional.
- **f_NL channel hierarchy**: equilateral -0.038, folded-Bogoliubov -0.080 (3× SR, substrate-unique), multi-branch -0.025 — total -0.143. Folded-Bogoliubov is the **unique substrate signature** (pair production at the cusp; no scalar-field analog). Amplitude too small for SKA-1 (W4-43 SNR = 0.028); 21-cm folded-SHAPE template at l_max ~10⁵ is the surviving channel (CF-43.1).
- **Three-layer regulator theorem** sits at §VII.N with two structural exceptions (r_max layer-interface, a_2-cluster meta-observable). Layer choice produces ~2 OOM ambiguity on A_s/μ/σ_8 — not a bookkeeping convention.
- **A_s renormalization closed at field-theory level** EXCEPT at f_conv (W6-67 FAIL). Vertical (slot-specific) obstruction, not perturbative divergence.

### Cross-Wave Conflicts Flagged

- **W4-44 DR3 rectangle vs W4-46 w_0 scheme-dependence** (collation §VII.3 W4): R_842 was centred on -0.842 (branch iv), now retracted at SV2. W4-44 is frozen by lockout; the binary containment rule fires 2026-04-23 regardless, but the physical interpretation of inside/outside is conditional on S85 re-audit. Internally consistent under "infrastructural commitment vs physical anchoring" distinction; flag it explicitly so downstream readers do not misinterpret a containment PASS as a physical PASS.
- **W6-71 mellin-template at 0/16 baseline** (W6 §B.4) vs **W3-25 + W3-31 PASS** (W3 §1). The W6-71 FAIL is a coverage-floor measurement; the W3 PASSes are genuine physics-on-template. Not a contradiction; flagging because the same "Mellin balance" vocabulary appears in both with different resolution.
- **W5-65 K_FIRAS = S_IC^cap residual 3.50%** (W5 §B.7). INFO; the 3.50% residual is **flat across L ∈ {5,7,9}** so it is persistent, not UV-shrinking. Flagged because the K_FIRAS = 3.68×10⁵ is in the kinetic sub-corridor (K > K_crit ≈ 91.5 per W5-55) — coincidence diagnostic value is degraded by the regime-of-validity violation.

---

## V. Carry-Forward Computations

V.1. **S85-VAN-HOVE-CUSP-THEOREM**
- **What**: Reformulate τ_fold selection as a critical-point of the spectral density ρ(λ; τ), not S(τ). Derive the cusp scaling exponent γ from the Jensen-deformed D_K spectrum near the level-crossing. Predict the local linearization c_s(τ → τ_fold) and the Bogoliubov |β_k|² scaling under the resulting impulsive (sudden) transit.
- **Inputs**: D_K eigenvalue cache at L_max ∈ {5, 7, 9, 10}; Jensen ansatz spectrum from baptista audit (3-exp form, c_a ∈ {+1, -1, -1/2}, log-slope range theorem [-1, +1]); W8a-85 audit notes; S82 G7 dS_fold = +58,672.80.
- **Gate**: S85-VAN-HOVE-CUSP PASS iff (a) cusp identified at τ_fold ∈ [0.189, 0.191] in ρ(λ; τ) at L_max=10 with cusp exponent γ ∈ [0.4, 0.6] (square-root universality class), AND (b) Bogoliubov |β_k|² scales as expected for sudden cusp passage (∝ k^{-3+2γ}). FAIL if no cusp at τ_fold or wrong universality class. INFO if cusp present but at shifted τ.
- **Effort**: 1 session (HIGH priority).

V.2. **S85-BASELINE-HTILDE-DERIVATION (TD-vs-LI divergence chase)**
- **What**: Derive H̃ from substrate first principles using two independent routes (TD canonical: Connes-Marcolli zeta; LI: Zubarev). Reconcile factor 240× divergence. Target: land H̃ inside [4.599×10⁻³, 4.830×10⁻³] (W1a-1 PASS-1.05 window, 0.89% log-DC).
- **Inputs**: W1a-1 PASS window; canonical_constants.py (planck_ns, A_s_target_Planck = 2.1×10⁻⁹); Branch-A and Branch-B H̃ canonicals; CC3 identity d(ln A_s)/d(ln H̃) = +2.
- **Gate**: A_s within factor 1.05 of Planck after baseline H̃ landing. PASS iff TD or LI route lands in the window. INFO if a third route emerges. FAIL if both routes structurally exclude the window.
- **Effort**: 2-3 sessions (HIGH priority; rate-limiting for A_s closure).

V.3. **S85-W_0-RE-AUDIT-AT-L8 (post-branch-iv-retraction)**
- **What**: Enumerate w_0 branches at L_max = 8 where ξ_J ~ ξ_E_GGE ordering is **inverted** (Josephson-dominant vs S58/S82/S83's Bogoliubov-dominant ordering). Identify branch family that admits stable convergence to L_max → ∞.
- **Inputs**: W1a-3 SV2 npz (R_JE drift 0.45 → 4.99); ξ_J = 0.008911 (TB-pinned); S_ζ_E and S_Zub_E spectra at L_max = 8.
- **Gate**: S85-W_0-BRANCH-V PASS iff a single branch family converges (R_JE stable within 10%) at L_max ∈ {8, 9, 10}. INFO if multiple competing branches. FAIL if no convergent branch identified.
- **Effort**: 1.5 sessions (HIGH priority; reopens DR3 R_842 interpretation).

V.4. **S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE**
- **What**: Compute the substrate-unique folded-Bogoliubov bispectrum SHAPE template (not amplitude) at 21-cm scales l_max ~ 10⁵; test discriminability against ΛCDM at SKA-2 / HERA / SKA-1-extended sensitivities.
- **Inputs**: W4-38 npz (folded channel α = -0.080); 21-cm forecasts; substrate squeezed-state two-point function from W3-34 A_s pin-map.
- **Gate**: SHAPE template distinguishable from ΛCDM at SNR ≥ 2 on at least one detector. PASS = surviving shape channel; FAIL = amplitude AND shape both inaccessible.
- **Effort**: 2 sessions (MEDIUM-HIGH priority; sole surviving f_NL channel).

V.5. **S85-CUSP-BOGOLIUBOV-COEFFICIENT-CALCULATION**
- **What**: Compute |α_k|², |β_k|² for the impulsive cusp passage at τ_fold using the van Hove-cusp linearized dispersion. Cross-check unitarity |α|² − |β|² = 1 mode-by-mode. Compare against the canonical S82 G7 F_amp_lin = 1.026 / S78 W1-C F_amp^sc = 48 bracket.
- **Inputs**: V.1 cusp scaling exponent γ; mode equation u_k'' + (k²c_s²(τ) − z''/z) u_k = 0 with c_s(τ) linearized about τ_fold; Bogoliubov boundary conditions (BD vacuum at τ → -∞, GGE relic at τ → +∞).
- **Gate**: Unitarity ε ≤ 1e-12; F_amp^cusp ∈ [1.0, 50] (bracketing S82+S78 results). PASS = within bracket and unitary.
- **Effort**: 2 sessions (HIGH priority once V.1 lands).

V.6. **S85-K-CORRIDOR-MUKHANOV-VALIDITY-AUDIT**
- **What**: Audit every W5-55, W5-57, W5-65 result that was computed at K > K_crit ≈ 91.5 (kinetic sub-corridor). Reclassify which numerical "INFO" results are physical signal vs kinetic-phase artifacts of using MS outside its regime.
- **Inputs**: W5-55 ε_eff = 0.02223 K/K_anchor scan; S63 MUKHANOV-SASAKI-63 theorem applicability bounds; W5-66 Landau-sub-phase classification.
- **Gate**: S85-K-CORRIDOR-AUDIT PASS iff every K > 91.5 W5 INFO is reclassified as either (a) physical with non-MS derivation, (b) kinetic-phase artifact, or (c) regime-overlap requires extended treatment.
- **Effort**: 0.5 session (LOW priority but housekeeping).

V.7. **S85-Z_R-2-LOOP-OR-F_CONV-SCHEME-CERTIFICATION**
- **What**: Extend W6-67 to 2-loop heat-kernel expansion seeking a counterterm structure that simultaneously balances f_conv and a_2; OR formally certify f_conv as physically scheme-dependent (G48 falsifier class extension).
- **Inputs**: W6-67 data + L_max ∈ {3,5,7} scan; Connes-Chamseddine a_2 regulator-invariance theorem; spectral-action RG flow from S80.
- **Gate**: PASS = multiplicative+additive Z_R structure balancing cluster_Z_a2 < 2.5 at 2-loop. Alternative PASS = formal scheme-dependence certificate. FAIL = neither found and S83-G28 cluster=1766 stands as permanent obstruction.
- **Effort**: 3-4 sessions (HIGH effort, MEDIUM-HIGH priority).

V.8. **S85-BETA_S-CMB-S4-PREREG**
- **What**: Lock β_s = -0.1331 (running of the running, 3rd-order Taylor coefficient from W8-86 OZ identity) as zero-free-parameter pre-registered prediction against CMB-S4. Apply same scheme-lockout discipline as W1b-7 α_s pre-registration.
- **Inputs**: W8-86 OZ derivation chain; CMB-S4 forecast for β_s sensitivity; pre-registration template.
- **Gate**: Pre-registration document landed in `sessions/framework/pre-registered-observations.md`; payload SHA-pinned with 6 lockouts.
- **Effort**: 0.5 session (MEDIUM priority).

V.9. **S85-DRESSED-V.P. (matter-dressed spectral action)**
- **What**: Test whether a matter-dressed spectral action V.P. (substrate + GGE entropy contribution) DOES select τ_fold as a critical point, even though the bare V.P. does not.
- **Inputs**: §W8-90 carry-forward; matter-dressed action expansion; substrate-action coupling to GGE quasiparticles.
- **Gate**: PASS if dressed S(τ) has critical point at τ ∈ [0.189, 0.191] AND second variation positive. FAIL = dressed V.P. also misses τ_fold (then van Hove cusp via V.1 is the only selection mechanism).
- **Effort**: 1.5 sessions (HIGH EVOI per W8 carry-forward).

V.10. **S85-LITEBIRD-N_T-RESCUE-PATHS**
- **What**: Test whether external A_lens prior (LSST κκ) tightens W4-37 σ(n_T)_joint below 0.04 PASS. Also test extended 6-7 yr LB mission and >50% delensing as alternative paths.
- **Inputs**: W4-37 Fisher construction; LSST κκ forecast; 7-yr LB extended mission specs.
- **Gate**: σ(n_T)_joint+prior < 0.04 PASS, OR re-confirm 654× inaccessibility under all rescue paths.
- **Effort**: 1 session (LOW priority — already structurally accommodated by W4-41 EVOI=0).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | A_s baseline H̃ window 0.89% log-DC (W1a-1) | PHONONIC | PASS | Rate-limiting open question relocated to baseline derivation; TD anchor +0.196 OOM above band centre |
| 2 | Dynamics-rescue corridor closed (W1a-2) | PHONONIC | FAIL (confirmation) | F_supp_max 1.044 vs 1.10; closure must come from H̃, not from dressing |
| 3 | Branch (iv) w_0 retracted at SV2 (W1a-3) | GEOMETRIC | FAIL (truncation tower) | R_JE inverts at L_max=8; w_0 canonical UNSPECIFIED pending S85 |
| 4 | α_s = -0.069 pre-registered (W1b-7) | PHONONIC | PASS | 9.62σ from Planck, 34.48σ from CMB-S4 null; scheme-locked |
| 5 | Two-speed n_T = -r·c_T/(8·c_S) (W4-39) | GEOMETRIC | PASS | n_T more negative than slow-roll by factor c_T/c_S = 2.062 |
| 6 | LiteBIRD n_T inaccessibility permanent (W4-37+41) | GEOMETRIC | FAIL+PASS | 654× below 1σ for 2030-2040 window |
| 7 | f_NL amplitude too small for SKA-1 (W4-38+43) | PHONONIC | FAIL+FAIL | Folded-Bogoliubov SHAPE template at 21-cm is sole surviving channel |
| 8 | w_0 permanently SCHEME-DEPENDENT (W4-46) | GEOMETRIC | structural FAIL | Split factor 6.22× over L=5→9; no single ZFP prediction |
| 9 | UHF-GW physical gap +18.74 OOM (W4-47) | GEOMETRIC | PASS | C5 structural WALL; no near-horizon migration |
| 10 | K_crit ≈ 91.5 kinetic-pole (W5-55+66) | PHONONIC | FAIL+INFO | MS regime restricted to K ∈ [1.922, 91.5] |
| 11 | 3He-B inheritance to 1.13% (W5-58+66) | PHONONIC | PASS+INFO | Framework superset of 3He-B; +3 SU(3) directions; K_*=coth(1)=1.3130 |
| 12 | α_s = n_s² − 1 partition-invariant (W5-62) | PHONONIC | PASS | Permanence upgrade from single-parameter to single-parameter+partition-invariant |
| 13 | K-FLOOR-WALL-JOINT triply supported (W5-54/59/63) | PHONONIC | FAIL×3 | Low-K corridor [1,1.7] structurally excluded |
| 14 | Three observational branch discriminators (W6-50/51/52) | PHONONIC | PASS×3 | LISA 2035, CMB-S4 2030, multi-obs joint — calendar decisions |
| 15 | A_s renormalization closed except at f_conv (W6-67/69/70) | PHONONIC | FAIL+PASS+PASS | Vertical (slot) obstruction at f_conv; field-sector clean |
| 16 | b_power Weyl asymptote d_int−1 = 7 (W7b-75/76) | GEOMETRIC | FAIL+PASS | IKKT b=1 excluded analytically |
| 17 | τ_fold IS van Hove cusp, NOT SA critical point (W8a-85 audit) | GEOMETRIC | FAIL→PLAN-DEFECT | 70 sessions of substrate-language ledger vindicated; new V.P. ansatz needed |
| 18 | A_F singleton (W8-87b) | GEOMETRIC | PASS-THEOREM | 1/3,907 surviving algebra; MG-2 promoted permanent |
| 19 | Mellin cone universality (W8-89) | GEOMETRIC | PASS-THEOREM | Inheritable from any positive-measure spectral triple |
| 20 | α_s = n_s² − 1 as OZ identity (W8-86 + W10-123) | PHONONIC | PASS at machine ε | Algebraic consequence of single-pole rational propagator; n_aux = 0 |
| 21 | Borel-summability floor (W10-121) | GEOMETRIC | PASS | min(S_inst) = 2.42×10⁵; 4.7 OOM safety; no instanton alternative to impulsive transit |
| 22 | Γ6 alone picks τ = 0.190 (W10-119) | GEOMETRIC | FAIL (predicate) | Same reframing as W8a-85; cubic-BC selection is correct |
| 23 | rank-universality theorem (W10-111) | GEOMETRIC | PASS | R_1 = a_0·a_4/a_2² distinguishes G_2 from F_4 (rank), not A_3 from C_3 |
| 24 | C² block decoupling (W9b-106) | PARTICLE | PASS-THEOREM | Δsin²θ_W[C²] = 0.0 EXACT (Cartan trace); rep-independent |
| 25 | Spectral dimension d_spec = 4.895 (W9b-105) | GEOMETRIC | FAIL (diagnostic) | μ_BC route via "12 = 4·d_spec" not supported at L_max=10 |
| 26 | V3 methodology ladder NON-COMPLIANT (W9-98) | NON-PHONONIC | structural FAIL | Physics verdicts intact; methodology closure deferred to S85 |
