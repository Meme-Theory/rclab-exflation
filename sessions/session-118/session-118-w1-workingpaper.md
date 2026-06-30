# Session 118 Wave 1 — A_s Amplitude Closure (the Q23 rate-limiter) (Results Working Paper)

**Session**: 118 | **Wave**: 1 | **Plan**: session-118-plan-w1.md | **Theme**: A_s-magnitude rate-limiter (Q23) — resolve the 0.668-OOM acoustic-horizon (H̃/+0.196) vs impulse-quench (box-δ/+0.864) fork from the substrate a₂-channel hydrodynamic-IR sound speed c_s (W1-1, PRIMARY); FAIL-branch hedge = the exit-greybody wall adjudication (W1-2). Two compute gates, both `[SIGN]`, no intra-wave data dependency → parallel-dispatchable.

## Gate Sections

### §W1-1. CF-S118-AS-CS-SUBSTRATE-FIRST (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S118-AS-CS-SUBSTRATE-FIRST`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (substrate-first a₂^{ζ}-curvature-channel IR sound speed; A_s magnitude fork resolution)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The substrate-first a₂^{ζ}-channel hydrodynamic-IR sound speed c_s (post-fold GGE two-fluid first/second-sound ratio) is real, positive, two-fluid-bracketed (c_BLV ≤ c_s ≤ c_Gold), and lands in the GS-1 window [0.5163972, 0.6501056] M_KK — membership ⇒ the deg=+2 substrate→pivot transport is the SOLE carrier of the 0.668-OOM A_s fork ⇒ Q23 closes to the zero-parameter acoustic-horizon (H̃/+0.196) grid (A_s = 3.2994e-9).
**Plan reference**: `sessions/session-plan/session-118-plan-w1.md` §W1-1 (machinery pins, PASS/FAIL/INFO thresholds, substitution chain, input-SHA ledger).

**Output Artifacts** (verified on disk by content-presence regex, not line/byte counts):
- (1) `computations/session-118/s118_as_cs_substrate_first.py` — present (26367 B); `grep -c 'from canonical_constants import'` = 1, `grep -c 'print_verdict_payload'` = 2 ✓
- (2) `computations/session-118/s118_as_cs_substrate_first.npz` — present (11041 B); `c_s`, `composite=PASS`, sign/magnitude/regime keys verified ✓
- (3) `computations/session-118/s118_as_cs_substrate_first.png` — present (174722 B); dispersion λ²(C₂)+IR-slope panel + c_s-vs-window/bracket panel ✓
- (4) verdict source `computations/session-118/s118_gate_verdicts.txt` — canonical line matches `^CF-S118-AS-CS-SUBSTRATE-FIRST:.* audit_sha256=[a-f0-9]{64}`; emitted via race-safe `emit_verdict` (4 rows: canonical + dual-SHA companion + `[SIGN]` 3-tuple + regulator_pin extra row) ✓
- (5) this WP §W1-1 carries the four wp_section markers (Status→COMPLETED, Verdict→PASS, **Output Artifacts**, **MCP Pre-Compute Audit**).

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per knowledge-index query-first discipline):
- `search_knowledge("substrate sound speed c_s a2 curvature channel two-fluid GGE")` → returned S63/S64/S67 prior sound-speed work; `c_BLV=0.485` tagged "a₂-channel sound speed"; s63/s64/s67 all import `a2_fold`. NOT PRE-CLOSED — this gate is the new GGE-two-fluid IR-dispersion derivation testing GS-1 window membership.
- `get_constant`: `c_Gold`=0.915 (S52 GL-JOSEPHSON-52); `c_BLV`=0.485 (S64, BLV fabric / 3He-B 4-speed hierarchy); `tau_fold`=0.19; `T_acoustic`=0.112 (GGE acoustic relic, NOT thermal-equilibrium); `a2_fold`=2776.1654 (½ζ_D(1)); `P_exc_kz`=1.0 (saturated Parker — fixes the GGE occupation as band-uniform). `xi_KZ`→canonical `xi_KZ_FW`=0.018760052113614718.
- Window/fork constants sourced from `s117_gs1_grid_selection.npz` (CF-S117-GS-1, audit `d7f28d3e…`): `cs_req∈[0.5163972,0.6501056]`, center 0.5794072, `fork_OOM`=0.6681541, `aH_exit`=14.3110927, `l_occ`=ξ_KZ.
- Input-SHA ledger verified at runtime: all four pins MATCH the plan exactly — canonical `d884a2b5…`, s84 L12 `9e6d9cf7…`, gs1 `dbecfedd…`, spectral_action.py `2ca6d921…`.

**Verdict**: **PASS** (composite). 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=MARGINAL`. Dual-SHA: `audit_sha256=172c85bea1e5ed064c4ef1c5c5116162272f966a73bb9080c96969b0b0aa02c3`, `content_sha256=8e1e6483acc7978055efd12db3eb77180224ed18fa8e5c01435c70600fd19807`. 4-tuple: `(value=0.5685294372062244, scheme=a2-curvature-channel-GGE-two-fluid, convention=hydrodynamic-IR-first-second-sound-ratio;Delta_scale=log10(c_s/((aH)_exit*xi_KZ));poleconv-A-double, L_max=12)`.

**Results**:

*Substrate-first derivation (the precise G_ij/G_ττ decomposition).* The substrate phonon dispersion is ω² = λ² (Dirac energy², the temporal frequency²) at spatial momentum² k² = C₂(p,q) (SU(3) quadratic Casimir = fiber-Laplacian eigenvalue of the Peter-Weyl (p,q) sector; verified vs the s84 L12 cache: adjoint (1,1)→C₂=3, (12,0)→C₂=60). The hydrodynamic-IR sound speed is BY DEFINITION the long-wavelength group velocity c_s² = (dω²/dk²)|_{k→0} = d⟨λ²⟩/dC₂|_IR = **K_grad/K_inertia**, a₂^{ζ}-density × saturated-GGE weighted (Lagrangian G_ij/G_ττ convention):
- **K_grad = Cov_w(λ², C₂) = 288.31** — gradient-stiffness cross second moment (how the temporal energy² co-varies with the spatial Casimir-momentum²; the G_ij coefficient; >0, energy rises with momentum on the block-diagonal PSD D_K² spectrum).
- **K_inertia = Var_w(C₂) = 891.98** — Casimir-momentum second moment (the inertial G_ττ normalization; >0).
- weight w_j = (a₂^{ζ} density dim_j·|λ_j|⁻²) × (GGE occupation n_j). GGE occupation = **saturated Parker relic** (P_exc_kz=1.000, band-uniform: every L12 mode has λ·dt_transit ≤ 6.1e-3 ≪ 1, deep sudden regime ⇒ |β_k|² saturated; the GGE never thermalizes so the cold thermal-BE form is the wrong regime).
- IR window C₂ ∈ [C₂_min, C₂_min·e] = [1.3333, 3.6244] (432 modes; the plan's bottom-decade Casimir window for the dispersion slope).

⇒ **c_s² = K_grad/K_inertia = 0.323226, c_s = +0.568529** (gap intercept = 0.745, the condensate rest-energy, correctly separated from the slope).

*Substitution chain (executed, numbers substituted).* K_grad>0 (D_K block-diagonal ⇒ D_K² PSD ⇒ Cov of energy² with momentum² positive: energy rises with Casimir); K_inertia>0 (Var of C₂, PSD). c_s² = (+288.31)/(+891.98) = +0.323226 > 0 ⇒ c_s = +√0.323226 = 0.568529 ∈ ℝ_{>0} (principal positive root). Two-fluid bracket: first sound (in-phase) saturates at c_Gold=0.915, second sound (counter-phase) floors at c_BLV=0.485; Landau ordering ⇒ c_BLV ≤ c_s ≤ c_Gold, computed 0.485 ≤ 0.5685 ≤ 0.915 ✓ ⇒ **sign_verdict = PASS** (the substrate-first c_s lies in the straddle interior — the scale-separation-carrying direction).

*Causality orients the ratio (a [SIGN] point).* The literal "spatial-Casimir / temporal-energy" reading c_s² = ⟨C₂⟩/⟨λ²⟩ = 2.788 (c_s=1.670) is **ACAUSAL** — the bare Casimir C₂ over-runs the Jensen-deformed λ² at high (p,q) ((12,0): C₂=60 vs λ²∈[13.5,29.4]). The PROVEN causality wall c_s ≤ 1 forces the group-velocity orientation c_s² = dλ²/dC₂, which is sub-luminal and gap-separated. This is the inversion mandated by physics, computed cleanly (the acausal value is recorded in the npz as `xchk_acausal_C2_over_lam2`=1.670, explicitly rejected).

*Magnitude axis.* Δ_scale = log₁₀(c_s/((aH)_exit·ξ_KZ)) = log₁₀(0.568529/0.268477) = 0.325846; 2·Δ_scale = 0.651692; |2·Δ_scale − fork_OOM| = |0.651692 − 0.668154| = **0.016462 ≤ 0.10 (PASS-band)**; window membership c_s ∈ [0.5163972, 0.6501056] ✓ ⇒ **magnitude_verdict = PASS**. (The window center 0.5794 is exactly the deg=+2 sole-carrier point 2·Δ_scale=fork_OOM; the substrate c_s sits 0.0165 OOM from it.)

*Regime axis.* IR dispersion fit λ² = gap + b₁C₂ + b₂C₂² gives b₁=0.2883, b₂=0.00810; the gradient-expansion control a₄K⁴/a₂K² = |b₂·C₂_max|/|b₁| = **0.102 at the window edge**, ≪ the plan's explicit breakdown criterion a₄K⁴ ≳ a₂K² (≳1) — the expansion holds for the IR extraction (which lives at C₂→0). Reported **regime_verdict = MARGINAL** under the conservative 5%/50% band (breach 0.102 sits just above the 5% VALID floor; not changed post-hoc); the uniform-weighted slope is *exactly window-independent* (0.59085 across all 90 sectors) — the clean linear-acoustic signature. Composite: regime≠BREAKDOWN ∧ sign=PASS ∧ magnitude=PASS ⇒ **composite = PASS**.

*Robustness (the verdict is not estimator-engineered).* Every principled estimator lands IN the window [0.5164,0.6501]: uniform IR slope 0.59085, a₂^{ζ} full-spectrum slope 0.58495, global a₂^{ζ} phase-velocity ratio 0.59888, GGE-weighted ratio 0.59888, uniform ratio 0.60784. **Machinery validation:** the acoustic-MINIMUM branch reproduces c_BLV = 0.48510 (reldev 0.02% vs canonical 0.485 — the S64 second-sound floor / lower bracket falls out independently). The ONLY below-window results are c_BLV itself (the bracket endpoint, not the a₂-trace mixture) and the cold thermal-BE narrow-window corner (0.383, the wrong — thermal — regime for a GGE that never thermalizes). No tuning of T_acoustic (canonical), window (slope window-independent), or weighting.

*Heat-kernel validation.* FULL physical heat kernel K(t)=Tr e^{−tD_K²} via `spectral_action.py` (Chamseddine-Connes, CLASS=FULL — NOT the SCHEMATIC `_spectral_action_regulators.py`): a₂ extracted as the t⁻³ moment over the plan t-window [1e-3,1e-1]×24 is finite and positive (a₂=2.00e2). The per-mode a₂^{ζ} density (½ζ_D(1) form dim·|λ|⁻²) absolute normalization is L12-vs-canonical-different (it is the density used for moment WEIGHTING; the absolute a₂ normalization CANCELS identically in the dimensionless ratio c_s² = K_grad/K_inertia, so the c_s result is normalization-independent). Regulator pin `a_2^{ζ}`, poleconv-A-double.

*dual_prior re-allocation.* PASS ⇒ **0.9 → Track A** (scale-separation / H̃-grid / +0.196 sole-carrier): the deg=+2 substrate→pivot transport is the SOLE carrier of the 0.668-OOM fork ⇒ the A_s magnitude resolves to the acoustic-horizon (H̃, +0.196) grid, **A_s = 3.2994e-9**; **Q23 closes to a zero-free-parameter geometric prediction** (the substrate's own c_s sets the sound horizon l_horizon = c_s/(aH)_exit = 0.03970, carried by the deg=+2 transport from the substrate scale to the CMB pivot). The box-δ (+0.864) grid is demoted to a regime-diagnostic under the TWO-SPECTRA-TWO-ROLES split. No FAIL-branch routing to CF-S118-AS-PREFACTOR-SOURCE.

*Substrate-first framing (preserved).* The substrate IS the acoustic medium; c_s is its own intrinsic hydrodynamic-IR dispersion slope (group velocity of the post-fold GGE two-fluid), read off the a₂ curvature channel of the D_K² spectral action — not a "speed in a container." Direction: D_K eigenvalues (s84 L12 cache) → a₂^{ζ} Seeley-DeWitt curvature moment → first/second-sound two-fluid ratio at the GGE relic → c_s → sound horizon → Δ_scale vs the ξ_KZ occupation length → deg=+2 transport carrier test → CMB A_s. Planck's 2.1e-9 is the laboratory-IN reading the substrate PREDICTS, not a target the substrate is fitted to.

---

### §W1-2. CF-S118-ALT-GREYBODY-WALL (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S118-ALT-GREYBODY-WALL`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (exit-horizon BdG greybody Γ=|T_BdG|²; atlas-09 Item-49 structural-wall adjudication)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: The knob-free exit-greybody Γ=|T_BdG|²≤1 (BdG S-matrix unitarity) is NOT substrate-derivable sub-unity — either a 4th knob-free class (full BdG S-matrix transmission on the exit-horizon sector) reaches a target {0.137, 0.512, 0.637} within rel_dev 0.10 at M_reg ≥ λ_max (route a ⇒ greybody EXISTS, the atlas-09 wall candidate is FALSIFIED), or a structural no-go floors Γ near unity for all α ≥ 1 (route b ⇒ the candidate promotes to a STRUCTURAL WALL).
**Plan reference**: `sessions/session-plan/session-118-plan-w1.md` §W1-2 (machinery pins, two-branch route-a/route-b operator, PLAN-FROZEN composite-precedence block, substitution chain).

**Output Artifacts** (closure-verification; content presence by regex, never line/byte counts):
1. `computations/session-118/s118_alt_greybody_wall.py` — 38,665 B; `grep -c "from canonical_constants import"`=2, `grep -c "print_verdict_payload"`=4 (both must_contain ✓).
2. `computations/session-118/s118_alt_greybody_wall.npz` — 24,401 B, 44 keys (`sweep_table`, `Gamma_og_knobfree`, `route_a_hit/route_a_miss/route_b_valid_nogo`, `composite`/`outcome`, `sign/magnitude/regime_verdict`, `gamma_knobfree_floor`, `gamma_max_overall`, `unitarity_max`, …) ✓.
3. `computations/session-118/s118_alt_greybody_wall.png` — 146,735 B (left: Γ(ω) per knob-free α + α=0.5 diagnostic + tcomp bracket vs target lines; right: band-avg Γ vs M_reg with the route-b 0.637 wall line) ✓.
4. `computations/session-118/s118_gate_verdicts.txt` — canonical line matches `^CF-S118-ALT-GREYBODY-WALL:.* audit_sha256=[a-f0-9]{64}`; `value=` encodes `outcome=WALL-STRENGTHENED-4-CLASS-EMPIRICAL`; dual-SHA companion row + `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + PLAN-FROZEN `# composite-precedence:` extra-row (names the §W1-2 two-branch operator) all present — 10 rows via the race-safe `emit_verdict` MCP tool ✓.
5. This WP §W1-2 — Status→COMPLETED, Verdict→FAIL, the **Output Artifacts** + **MCP Pre-Compute Audit** headings present (four wp_section must_contain ✓).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("exit greybody factor BdG transmission acoustic horizon wall")` → **INV12-W3-4-GREYBODY-FROM-BDG FAIL** (∫Γ_derived=0.036 vs fitted 0.512; κ_eff=κ_exit=47.6146); **INV4-W1-4-EXIT-GREYBODY-A_s-NORMALIZATION FAIL** (f_grey=0.913); the `A_s = squeeze × exit-greybody filter` decomposition. Confirms the 3 prior knob-free FAILs (Pöschl-Teller / Wodzicki-moment-ratio / Connes-distance).
- `search_knowledge("CF-S117-ALT-GREYBODY structural wall candidate atlas-09 Item-49")` → atlas-09 retraction-log surface only; **no prior 4th-class (BdG S-matrix transfer-matrix) computation**. INV12-W3-4 used a `solve_ivp` ODE / closed Pöschl-Teller, NOT a transfer-matrix + PV M_reg sweep ⇒ this gate is **NOT PRE-CLOSED**.
- Constants from the canonical import `canonical_constants.py` (M_KK, A_s_CMB=2.1e-9, A_s_FW=1.536706e-8, kappa_exit=47.6146, Delta_BCS, tau_fold); all five input SHAs verified against the plan ledger (5/5 MATCH). Targets computed substrate-first (box_delta=A_s_CMB/A_s_FW=0.136656, slow_roll=10⁻⁰·¹⁹⁶¹⁷=0.636546, fit=inv12 `transmitted_fraction_fitted`=0.511872), NOT hardcoded. → proceed to compute.

**Verdict**: **FAIL** — outcome=**WALL-STRENGTHENED-4-CLASS-EMPIRICAL** (PLAN-FROZEN composite-precedence two-branch operator: `route_b_valid_nogo`=False ∧ `route_a_hit`=False ∧ `route_a_miss`=True). `[SIGN]` schema-v2 3-tuple: **sign_verdict=PASS** (Γ=|T_BdG|²≤1, the unitarity bedrock), **magnitude_verdict=FAIL** (route(a) miss — knob-free Γ at no target), **regime_verdict=VALID** (transfer-matrix on cached barrier; deterministic; unitary to 1.24e-14). audit_sha256=`66910a55…f821bd4`; content_sha256=`ddcecec1…d4b8f190`.

**Results**

*New machinery (the 4th class).* The full BdG S-matrix transmission Γ(ω)=|T_BdG(ω)|² is computed by a manifestly-UNITARY **(ψ, ψ′) slab transfer-matrix product** on the plan-pinned exit-horizon barrier `V_eff(x_tortoise)` (inv12_w3_4 npz; V_eff=V0·sech²(κ_eff·x), κ_eff=κ_exit=47.6146, 4000-pt x-grid spanning ±0.252). Each slab matrix `[[cos(qd), sin(qd)/q],[−q·sin(qd), cos(qd)]]` has det=1 ⇒ the Wronskian is preserved ⇒ **|T|²+|R|²=1 BY CONSTRUCTION** (max deviation over the whole sweep **1.24e-14**, the [SIGN] bedrock). This is structurally distinct from INV12-W3-4's `solve_ivp` ODE / closed-PT (the prior class). Cross-validation against the closed Pöschl-Teller form: max |Γ_transfer − Γ_PT| = **1.87e-7** (method-consistent ≪ 1e-3).

*PV α-sweep* (M_reg=α·λ_max; λ_max=5.4189 from s84 L12; barrier height modulated by the standard PV a₄ condensation moment V0(M_reg)=V0_marginal·[M_a4^PV(M_reg)/M_a4^bare], poleconv-A-double a₄ at pole_in_s=2/n=4; knob-free M_reg≥λ_max ⇒ M_a4^PV→M_a4^bare ⇒ the FULL physical barrier — s117 KNOB-LOCATION lineage):

| α | M_reg | V0 | Γ_sqz-wt (filter) | Γ_permode-max | best rel_dev | branch |
|---|---|---|---|---|---|---|
| 8 | 43.35 | 566.77 | **0.03627** | 0.05792 | 0.576 | knob-free |
| 4 | 21.68 | 566.55 | 0.03630 | 0.05798 | 0.576 | knob-free |
| 2 | 10.84 | 563.56 | 0.03676 | 0.05869 | 0.571 | knob-free |
| 1 | 5.42 | 536.45 | 0.04127 | 0.06575 | 0.519 | knob-free |
| 0.5 | 2.71 | 424.47 | 0.06700 | 0.10983 | 0.196 | in-bulk KNOB (DIAGNOSTIC-ONLY, EXCLUDED) |

*Route adjudication.* **route(a) MISS** — knob-free best rel_dev = **0.5189** ≫ 0.10 PASS-band (the most-transmissive knob-free reading, the α=1 per-mode-max 0.0657, is still 0.52 from the nearest target 0.137). **route(b) NOT a valid no-go** — `Γ_knobfree_floor` (squeeze-weighted) = **0.03627** is NOT > max(targets)=0.636546; the knob-free Γ floors at the OPPOSITE extreme (over-suppression). The two-branch operator (PLAN-FROZEN, §W1-2 lines 461-473) selects `route_a_miss → FAIL (WALL-STRENGTHENED-4-CLASS-EMPIRICAL)`; the generic 3-tuple collapse (sign=PASS / magnitude=FAIL / regime=VALID) yields the same FAIL — consistent, disclosed in the `# composite-precedence:` extra-row.

*Substitution chain (substituted numbers).* Def 1: Γ=|T|². Def 2: S†S=1 ⇒ |T|²+|R|²=1 (exit-horizon BdG = 1D self-adjoint scattering; κ_eff=κ_exit=47.6146). Def 3: |R|²≥0. ⇒ |T|²=1−|R|²≤1 ⇒ **Γ=|T|²≤1** (computed Γ_max=**0.10983**<1 ⇒ sign_verdict=PASS). Wall sub-claim (magnitude direction): the pre-registered chain predicted knob-free M_reg→λ_max⁺ ⇒ |R|²→0 ⇒ Γ→1 (transparent). The computation **REFUTES that direction**: the a₄ condensation moment Σ|λ|⁻⁴ is **IR-dominated** (λ_min=0.8197 ⇒ λ_min⁻⁴=2.21 dominates the 166,896-mode sum M_a4^bare=1691.5), so the standard PV at M_reg≥λ_max recovers the FULL barrier (V0→566.8=κ²/4, √V0=23.8 ≫ band [0.94,3.72]) ⇒ deeply sub-barrier ⇒ knob-free Γ floors at **0.036 (OVER-suppression)**, not at unity.

*Substrate-first assessment (IS-not-IN).* The exit greybody IS the substrate's own transmission of the squeezed GGE power through the post-fold a₄ condensation-energy barrier at the acoustic white-hole exit horizon — D_K eigenvalues (s84 L12 → λ_max; inv12 BdG ω_k) → exit-horizon BdG S-matrix |T(ω)|² → greybody Γ → A_s upper-edge factor. The unitarity bound Γ≤1 is a substrate-intrinsic identity (self-adjoint H_BdG). The substantive finding is a **two-sided wall** the operator pre-registered only one side of: the knob-free spectral geometry CANNOT supply any of the targets {0.137, 0.512, 0.637} — reaching them requires placing M_reg deep in the spectral bulk (α≪1, a sub-spectral KNOB). But the knob-free floor sits **below** the lowest target (over-suppression, 0.036), not **above** the highest (the route-b transparency phrasing). Moreover the no-go is **barrier-reading-sensitive**: the plan-pinned marginal barrier V0=κ²/4 floors at 0.036 (<0.637), while the inv12 tcomp bracket V0=T_compound²=57.43 floors at **0.836** (>0.637, which WOULD satisfy route-b); **neither** reading hits a target knob-free (marginal rel_dev 0.519; tcomp rel_dev 0.313). Because the route-b no-go is not robust across the substrate-natural barrier-energy readings, the 4th class **strengthens the empirical wall to 4 construction classes** (Pöschl-Teller, Wodzicki moment-ratio, Connes-distance, BdG S-matrix) **without** supplying a clean structural transparency no-go → FAIL, not PASS-WALL.

*dual_prior re-allocation.* The plan priors were track_A (wall) 0.55 / track_B (falsified) 0.45 with discriminator → 0.9 on a fired branch. Neither branch fired: route(a) missed and route(b) was not a valid (robust) no-go ⇒ mass moves to the un-pre-registered "FAIL — wall empirically strengthened, not structurally proven" outcome; the structural-proof attempt is reserved as a next-session carry-forward.

*Consequence (CF-S118-AS-PREFACTOR-SOURCE, next session — do NOT dispatch here).* The exit greybody is NOT a clean knob-free A_s upper-edge prefactor source: under the plan-pinned (marginal) barrier it over-suppresses (Γ≈0.036), under the tcomp bracket it over-transmits (Γ≈0.836), and neither lands at a target knob-free. The A_s upper-edge factor therefore remains the S95-fitted knob (0.512). The open structural question is the **barrier-energy reading** (V0=κ²/4 vs V0=T_compound²) — pinning it substrate-first is the prerequisite for any greybody-NOGO-PROOF; the over-suppression/over-transmission dichotomy generalizes the route-b operator to "targets ∉ knob-free Γ range across both barrier readings."

*Provenance.* Input-SHA ledger 5/5 MATCH: canonical_constants.py `d884a2b5…`, s117_alt_greybody.py `308fbf25…`, s117_alt_greybody.npz `1350f937…`, inv12_w3_4 BdG `4f51d724…`, s84 L12 cache `9e6d9cf7…`. Dual-SHA: audit_sha256=`66910a556ab0645326f789d6b5af061188fb617eb2a5c1e50fa796d93f821bd4`, content_sha256=`ddcecec18b27cd0ba374c2fa5f5d97945fd1b6148d7ac36f8dcf3025d4b8f190`. 4-tuple: (value=outcome=WALL-STRENGTHENED-4-CLASS-EMPIRICAL, scheme=BDG-S-MATRIX-TRANSMISSION-4TH-CLASS+WODZICKI-PV-MOMENT-RATIO+CONNES-DISTANCE+NO-GO, convention=knob-free-Mreg>=lammax;Gamma=|T_BdG|^2;poleconv-A-double-a2s3n2-a4s2n4, L_max=12). Artifacts: s118_alt_greybody_wall.py / .npz / .png.

---

## Wave 1 Synthesis (team-lead)

**Headline — Q23 A_s magnitude closes to a zero-free-parameter prediction.** The session's highest-EVOI gate W1-1 PASSED: the substrate's own a₂^{ζ}-curvature-channel hydrodynamic-IR sound speed **c_s = 0.568529 M_KK** (causal group velocity K_grad/K_inertia, the acausal C₂/λ²=1.670 reading explicitly rejected) lands IN the GS-1 scale-separation window [0.5163972, 0.6501056], two-fluid bracketed (c_BLV=0.485 ≤ 0.5685 ≤ c_Gold=0.915), `|2·Δ_scale − fork_OOM| = 0.0165 ≤ 0.10`. The deg=+2 substrate→pivot transport is therefore the SOLE carrier of the 0.668-OOM dominant fork ⇒ the A_s magnitude resolves to the acoustic-horizon (H̃/+0.196) grid, **A_s = 3.2994e-9** — a falsifiable zero-parameter prediction +0.196 OOM (1.57×) above Planck 2.1e-9, carried regime=MARGINAL (a₄K⁴/a₂K²=0.102 at the window edge, just above the 5% VALID floor; a robust-but-marginal PASS, caveat travels). The FAIL-branch hedge W1-2 returned **FAIL / WALL-STRENGTHENED-4-CLASS-EMPIRICAL**: the BdG-S-matrix 4th knob-free class misses every target (best rel_dev 0.519) and route-b is no valid no-go (knob-free floor 0.036 below targets, barrier-reading-sensitive), so the exit-greybody stays a fitted knob without a structural transparency proof.

**Solution-space updates:**
- **W1-1 PASS** closes the dominant A_s **scale-separation** fork (H̃/+0.196 vs box-δ/+0.864) from the substrate. This is a SCALE-SEPARATION-axis selector (the substrate's own c_s + deg=+2 transport-carrier), structurally DISTINCT from the S114 FUNCTIONAL-selection "no selector" result — the substrate DID supply a selector, on the transport-carrier axis. The box-δ/+0.864 grid is demoted to a regime-diagnostic (TWO-SPECTRA-TWO-ROLES). Remaining A_s openness lives only at the regime-MARGINAL caveat and the (sub-dominant) Parker +1.455 functional's standing under the scale-separation reading.
- **W1-2 FAIL** adds the BdG-S-matrix construction class to the empirical exit-greybody wall (now 4 classes: Pöschl-Teller, Wodzicki-PV moment-ratio, Connes-distance, BdG-S-matrix) WITHOUT proving the structural no-go. The genuinely-open sub-question is the **barrier-energy reading** (V0=κ²/4 over-suppression 0.036 vs V0=T_compound² over-transmission 0.836) — pinning it substrate-first is the prerequisite for any greybody no-go.

**Decision-point routing (plan W1→W2 table, L523-535):**
- W1-1 **PASS** → Q23 CLOSES zero-parameter (H̃/+0.196, A_s=3.2994e-9). The four pre-registered folds are effected (see Effected In-Session). **No FAIL-branch routing** to `CF-S118-AS-PREFACTOR-SOURCE` (that conditional carry-forward does NOT fire).
- W1-2 **FAIL/WALL-STRENGTHENED** → `CF-S119-GREYBODY-NOGO-PROOF` carry-forward (a structural no-go derivation; see Carry-Forward Computations).

**Capstone-hygiene 5-question gate (this wave touches a capstone-governing register → gate REQUIRED):**
- **Q1** (a(t)/effective-Friedmann gap): **NO** — W1-1 does not alter the §6.3 substrate→FRW pathway.
- **Q2** (§7 falsifier-anchor row): **YES** — the A_s falsifier anchor value/status changes → routed to `mack-cosmic-bridge` (sole writer; §7.1/§7.2 + `falsifier-master-inventory.md` row).
- **Q3** (PROVEN/CONDITIONAL/BROKEN/INFO status change): **YES** — A_s magnitude: CONDITIONAL-plurality → zero-parameter PASS (regime-MARGINAL). Capstone prose tag reconciled AGAINST Atlas D04 + the retraction log (no over-confident narration; the tag equals the register status).
- **Q4** (PROSE claim vs ledger row): **YES** — designated-writer reviewed patch (mack), NOT a bulk install-agents append.
- **Q5** (citation add/invalidate): **YES** (minor) — adds the `CF-S118-AS-CS-SUBSTRATE-FIRST` audit citation (`172c85be…`).
- Routing: Q2–Q5 fire → **in-session designated-writer fix** (housekeeping §A), effected by `mack-w1folds` (task #14). The orchestrator ran the gate (determined the reconciliation); mack applies the §7/falsifier patches.

**Effected In-Session (NON-MATH — completed by the team-lead before STOP):**

- [x] **EVOI §EVOI.BF** — A_s-liability "S118 W1 RESOLUTION" fold (c_s ∈ window PASS, zero-parameter +0.196 closure, regime-MARGINAL, greybody FAIL) — orchestrator-direct (EVOI orchestrator-maintained per `feedback_framework-hygiene.md`) — `sessions/evoi-framework.md §EVOI.BF`.
- [x] **atlas-08 Q23 — LIVE DASHBOARD (line 17)** → "A_s normalization CLOSED zero-parameter (S118 W1, regime-MARGINAL)" — orchestrator-direct (atlas freshness in place per `feedback_status-docs-current-state-first.md`) — `atlas-08-open-questions.md:17`.
- [x] **atlas-08 Q23 — VI.A Decisive-Class table (line 249)** → A_s CLOSED zero-parameter + greybody-hedge note — orchestrator-direct. *This SECOND Q23 occurrence was surfaced by `mack-w1folds`' register-sync flag* — my first atlas-08 fold caught only the dashboard row — `atlas-08-open-questions.md:249`.
- [x] **atlas-04 D04 A_s clause (line 199)** → "CONDITIONAL on CF-S117" → "CLOSED zero-parameter (S118 W1); deg=+2 𝒩 = IDENTIFIED sole carrier; 1.57× H̃/+0.196 grid; regime-MARGINAL; floor inequality >1 PERMANENT UNCHANGED" — orchestrator-direct. *Surfaced by `mack-w1folds`' flag; supersedes the plan-index "atlas-04 no-change" (which predated the W1-1 PASS — the status changed since plan-freeze, so the fold is fix-in-session)* — `atlas-04-assumptions.md:199`.
- [x] **falsifier-master-inventory.md** — new `Row #12.compute-S118-W1-AS-CS-SUBSTRATE-FIRST-FORK-CLOSURE` (0.668-OOM 410.7σ fork → resolved zero-parameter to the H̃/+0.196 grid 3.2994e-9; box-δ demoted; greybody-knob note) — `mack-cosmic-bridge` sole-writer designated patch (task #14) — **verified on disk** lines 2658–2668 (cites W1-1 audit `172c85be` + greybody `66910a55`).
- [x] **capstone §7 amplitude anchor** — §7.1 Open-gaps clause (line 556) → "RESOLVED zero-parameter (S118 W1, regime-MARGINAL)" + NEW §7.2 falsifier row #13 (line 577) — `mack-cosmic-bridge` designated patch (task #14) — **verified on disk** (Q3 prose tag = register status, no over-claim; substrate-IS frame preserved).
- [x] **c_s canonical_constants promotion** (canonical write-order Step 2) — `transit-w1` promoted **`c_s_a2curv_GGE_fold = 0.5685294372062244`** (channel-specific name) with full provenance (`computations/_shared/canonical_constants.py:477` + PROVENANCE dict L2076). The query-first `c_s2_FW=0` collision I flagged RESOLVED as a **CLEAN DIFFERENT CHANNEL** (no tension): c_s2_FW=0 is the Layer-1/topological 4D Goldstone (dispersionless, Kasparov m_Goldstone⁴ᴰ=0); c_s_a2curv_GGE_fold is the Layer-2 substrate-scale a₂-hydrodynamic dispersion of the post-fold GGE two-fluid (nonzero). Verified on disk.
- [x] **capstone "PENDING"→"SYNCED" disclosure flip** — `mack-w1folds` flipped the §7.1 + §7.2 + falsifier-inventory-row disclosures to "curated-register fold SYNCED" now that atlas-08 (dashboard + Decisive-Class) + atlas-04 D04 are folded. Verified on disk (SYNCED ×2 capstone, ×1 inventory; 0 remaining "fold PENDING").
- Self-audit: `grep -c '^- \[ \]'` over this block = **0** (all 8 Effected-In-Session items closed; the W1-1 capstone-hygiene Q3 reconciliation is complete across all governing registers).

## Carry-Forward Computations

W1-1 PASS ⇒ `CF-S118-AS-PREFACTOR-SOURCE` (W1-1-FAIL conditional) does NOT fire; `CF-S119-AS-PREFACTOR-SHARE` (W1-1-INFO conditional) does NOT fire. The single genuine math carry-forward is the W1-2-FAIL conditional:

### CF-S119-GREYBODY-NOGO-PROOF — exit-greybody two-sided structural no-go

> **Routing note**: MATH carry-forward (4-field spec) per `feedback_fix-in-session-never-defer.md`. Fires from W1-2 FAIL (WALL-STRENGTHENED-4-CLASS-EMPIRICAL). Mirrored to `session-118-housekeeping.md §B` (the housekeeping ledger is the canonical Q2 filter; this WP block is the `/rclab-plan` consumption mirror). NOT a workshop (no adversarial reading-divergence — a structural derivation with a pre-registered threshold).

1. **What**: Derive whether the substrate's knob-free spectral geometry can reach ANY sub-unity exit-greybody target {0.137, 0.512, 0.637} at M_reg ≥ λ_max — a **two-sided** no-go generalizing the route-b operator: the S118 W1-2 result shows the knob-free Γ floor is **barrier-energy-reading-dependent** (V0=κ²/4 ⇒ over-suppression Γ=0.036 < all targets; V0=T_compound²=57.43 ⇒ over-transmission Γ=0.836 > all targets), and NEITHER reading hits a target knob-free (rel_dev 0.519 / 0.313). The prerequisite is to **pin the barrier-energy reading substrate-first** (V0=κ²/4 vs V0=T_compound²); then prove targets ∉ knob-free Γ range across the pinned reading(s).
2. **Inputs**: `computations/session-118/s118_alt_greybody_wall.py` + `.npz` (4th-class BdG-S-matrix transfer-matrix machinery + both barrier readings; W1-2 audit `66910a55…`); `computations/investigation-12/inv12_w3_4_greybody_from_bdg.npz` (exit-horizon BdG dispersion, κ_exit=47.6146); `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (λ_max); `computations/session-117/s117_alt_greybody.py`/`.npz` (3 prior failed classes + targets); the substrate barrier-energy canonical (κ²/4 vs T_compound²).
3. **Gate**: `S119-GREYBODY-NOGO-PROOF` [SIGN/VERIFY]. **PASS** = a structural proof that no knob-free M_reg ≥ λ_max barrier-energy reading reaches any target (targets fall in the gap between the over-suppression floor and the over-transmission floor of the substrate-pinned barrier reading) ⇒ atlas-09 Item-49 candidate → registered STRUCTURAL WALL ("A_s upper-edge NOT substrate-derivable" a theorem). **INFO** = borderline/regime-ambiguous no-go. **FAIL** = a knob-free reading reaches a target within rel_dev 0.10 ⇒ greybody EXISTS, candidate retracted.
4. **Effort**: ~1 wave (structural derivation on the cached barrier + both readings; barrier-energy-reading substrate pin; no new diagonalization).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-29 | A_s magnitude (Q23) | 3-member functional-selection plurality {+0.196,+0.384,+0.864} OOM; dominant H̃-vs-box-δ 0.668-OOM fork OPEN | dominant fork CLOSED zero-parameter to H̃/+0.196 grid, A_s=3.2994e-9 (1.57× Planck); regime-MARGINAL; box-δ demoted to regime-diagnostic | `CF-S118-AS-CS-SUBSTRATE-FIRST` PASS — substrate c_s=0.5685 ∈ GS-1 window, deg=+2 sole carrier |
| 2026-06-29 | Exit-greybody structural wall (atlas-09 Item-49) | 3-construction-class "NOT substrate-derivable" candidate | 4-construction-class empirical wall (BdG-S-matrix added); structural no-go NOT proven (barrier-reading-sensitive) | `CF-S118-ALT-GREYBODY-WALL` FAIL / WALL-STRENGTHENED-4-CLASS-EMPIRICAL |
| 2026-06-29 | A_s functional-selection "permanent d.o.f." (S114) | CONFIRMED permanent on the functional-selection axis (no functional selector) | superseded on the dominant fork by a SCALE-SEPARATION selector (substrate c_s); zero-parameter +0.196 prediction | W1-1 selects via the transport-carrier axis (distinct from the functional axis) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict (audit_sha256) |
|:-----|:-------|:------------|:------------|:-----------------------|
| CF-S118-AS-CS-SUBSTRATE-FIRST | `computations/session-118/s118_as_cs_substrate_first.py` | `s118_as_cs_substrate_first.npz` | `s118_as_cs_substrate_first.png` | `172c85be…aa02c3` PASS (sign/mag PASS, regime MARGINAL) |
| CF-S118-ALT-GREYBODY-WALL | `computations/session-118/s118_alt_greybody_wall.py` | `s118_alt_greybody_wall.npz` | `s118_alt_greybody_wall.png` | `66910a55…f821bd4` FAIL (outcome=WALL-STRENGTHENED-4-CLASS-EMPIRICAL) |

Verdict file: `computations/session-118/s118_gate_verdicts.txt` (W1-1: canonical + dual-SHA + [SIGN] 3-tuple + regulator_pin extra row; W1-2: canonical + dual-SHA + [SIGN] 3-tuple + composite-precedence extra-row).
