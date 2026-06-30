# Session 117 Wave 9 — e-fold substrate obligations (Results Working Paper)

**Session**: 117 | **Wave**: 9 | **Plan**: session-117-plan-w9.md | **Theme**: The **two substrate-native obligations** that survived the retirement of the inflation-mechanism intermediate `N_e ≥ 3.1` (dissolved by the S116 W-3 workshop as a **category-(C)** competing-mechanism number — inflation's bookkeeping for how dilution buys horizon + flatness; no instrument reads `N_e ≥ 3.1`, so it does not cross into a framework that counts no e-folds, per `phononic-framing.md §"IS-NOT-IN A/B/C category distinction"`). The genuinely-binding **category-(B) observational obligations** it badly proxied are KEPT and re-homed on parameter-free substrate falsifiers: the **horizon** obligation was already **DISCHARGED** (acoustic white-hole sealing, PROVEN S85, lab-realized — Rolley et al. `09_2005`); the **flatness** (9-1) and **scale-range** (9-2) obligations are OPEN and sharply falsifiable. Retiring the number TIGHTENS the falsifier surface (no knob absorbs a shortfall). Both gates are **COMPUTE-class**, `[SIGN]`-triggered (⇒ schema-v2 sign/magnitude/regime 3-tuple companion row required), and **mutually independent** (parallel-dispatchable); only 9-2's `(iii)` amplitude sub-condition is Wave-1-conditional (INFO-collapse, never PASS-by-default). On close `mack-cosmic-bridge` (sole writer per `feedback_mack-bridge-role.md`) updates the `falsifier-master-inventory.md` Row #93 obligation-cluster sub-row statuses OPEN → PASS/FAIL/INFO.

## Gate Sections

### §W9-1. CF-S117-A2-OMEGAK-ACOUSTIC-FORM (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `CF-S117-A2-OMEGAK-ACOUSTIC-FORM`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (a₂ emergent-3-metric k-selector; flatness half of the retired `N_e ≥ 3.1`)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: Under the homogeneous global-modulus state (τ(x⃗) = τ_fold = 0.19 uniform over M⁴), the a₂ Seeley-DeWitt emergent 3-metric in the preferred (Painlevé / substrate-rest-frame) foliation is acoustic-form `g_ij^(3) = Ω²(x⃗)δ_ij` with `Ω = ρ/c`, AND the conformal factor Ω is spatially UNIFORM ⇒ `R^(3) = 0` ⇒ `k = 0` ⇒ `Ω_k = 0` EXACT — the sharpened k-selector the soft "acoustic-form alone" test cannot pin (conformal-flatness is k-blind: S³ k=+1 and H³ k=−1 are both conformally flat). The NEW increment over the prior R^(3)=0 results (S74 W1-H; S106 §VII.CA) is the spatial-uniformity discriminator on ρ/c.
**Plan reference**: `sessions/session-plan/session-117-plan-w9.md` §W9-1 (operator, strict-PASS boundary, machinery pin, substitution chain, fb_pair, dual_prior, verdict rubric).

**Output Artifacts** (closure-verified on disk — content presence by regex, never line/byte counts):
- (1) script `computations/session-117/s117_w9_a2_omegak_acoustic_form.py` — present; contains `from canonical_constants import` ✓ AND `print_verdict_payload` ✓.
- (2) data `computations/session-117/s117_w9_a2_omegak_acoustic_form.npz` (R^(3) field, ptp(ρ/c) + normalized + raw conformal-gradient witnesses, Ω_k, control fields) ✓ AND plot `computations/session-117/s117_w9_a2_omegak_acoustic_form.png` (3-panel: uniformity / R^(3) discriminator / Ω_k-vs-Planck) ✓ — both present.
- (3) verdict line in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-A2-OMEGAK-ACOUSTIC-FORM:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + schema-v2 sign/magnitude/regime 3-tuple companion row ✓ + `regulator_pin=a_2^{zeta}` companion row ✓ (emitted via race-safe `emit_verdict`, sig_5 unique).
- (4) this §W9-1 section: Status=COMPLETED + Verdict=PASS + `**Output Artifacts**` + `**MCP Pre-Compute Audit**` blocks present.

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries executed BEFORE writing the script; gate is NOT pre-closed — the soft k-BLIND R^(3)=0 priors exist, the sharpened uniformity k-selector is genuinely new):
- `search_knowledge("Omega_k flatness acoustic form a2 conformal R3 curvature k=0")` → **S74 W1-H FLATNESS-FROM-A2-74**: "Ω_k = 0 exactly by the block-diagonal theorem; no K term in the line element" (the SOFT, k-blind prior); Planck `Ω_k = 0.0007 ± 0.0019` lives in `falsifier-master-inventory.md` Row #93; no prior gate computes the spatial-uniformity selector.
- `get_constant("tau_fold")` → **0.19** (S12/S42, gate CONST-FREEZE-42) — matches plan pin.
- `get_constant("a_2_FW_zeta")` → **2776.165389** (S88, gate S88-A-N-FW-CANONICALIZATION; zeta-regulated `a_2^{ζ}`) — matches plan regulator pin.
- `trace_entity("metric without curvature R^(3)=0 Omega_k flatness")` → no direct trace (confirms the uniformity-selector increment is new, not a recompute).
- Sage cross-check (`mcp__sage__sage_eval`) executed before script-write: verified Def-3 conformal identity from scratch (Christoffel → Ricci → scalar), residual `R^(3) − [−4Ω⁻³∇²Ω + 2Ω⁻⁴|∇Ω|²] = 0` EXACT.

**Verdict**: **PASS** — sign=PASS / magnitude=PASS / regime=VALID (composite PASS). `audit_sha256=4b1c7bce6110364f77135e8433b87fec39a215538f3359d9801fc7411a471fc6`, `content_sha256=48b11593c81c096030de74f1b15300cd32ef96627abdf05fc317e3ed524ef94f`. 4-tuple `(value=Ω_k=0_EXACT_ptp(ρ/c)=0.00e+00_gradhat=0.00e+00_R3=0.00e+00_planck=0.368σ, scheme=SA-a2-zeta, convention=ABSOLUTE-Painleve-rest-frame-foliation, L_max=12)`.

**Results**:

*Inputs / pins.* `tau_fold = 0.19`; `a_2_FW_zeta = 2776.165389` (regulator-pin `a_2^{ζ}`, zeta-regulated 2nd Seeley-DeWitt); `c_BLV = 0.485` (post-fold GGE scalar sound speed). Substrate conformal-factor density `ρ(τ) = Z_spectral(τ)` from the S63 a₂-block-diagonal KK-reduce cache; `Z_spectral(τ_fold) = 74023.681949` — **cross-cache consistency**: equals the S106 `Z_fold_recomputed = 74023.6819`. Scale-setting `Ω_fold = ρ/c = 152626.148348` (the verdict is **scale-INVARIANT** in Ω — k=0 ⇒ R^(3)=6k/a²=0 for any a=Ω). Input-SHA pins (runtime): `canonical_constants.py` `d884a2b5…`, `s63_kk_reduce_4d.npz` `971782ac…`, `s84_spectrum_cache_L12_tau019.npz` `9e6d9cf7…`, `s106_w3_1_metric_without_curvature_landing.py` `e8a325a0…`. Planck `Ω_k = 0.0007 ± 0.0019` (Planck 2018 VI, base+Ω_k) cited in-script as a **category-(B)** observational datum, NOT a `canonical_constants.py` pin.

*PART (a) — acoustic-form (k-BLIND).* Cross-check vs S106 §VII.CA metric-without-curvature joint wall (STAGE-3-PERMANENT): Chern `c_1 = 9.778e-15`, Euler `e_2 = −8.835e-18`, graded-Ω `A^WZ = 1.284e-17` (all `< 1e-12`), band metric `g = 982.5 ≠ 0` ⇒ the D_K eigenbundle is **metrically-rich but holonomy-free** ⇒ the emergent geometry admits the rest-frame (Painlevé) foliation (acoustic-form confirmed). This is **k-BLIND** — conformal-flatness alone admits S³ (k=+1) and H³ (k=−1); it is NECESSARY but not sufficient to pin k=0.

*PART (b) — the spatial-uniformity k-selector (the NEW increment).* Substrate reason ∇Ω=0: the D_K **block-diagonal theorem** — the s84 cache is keyed by **90 Peter-Weyl fiber (p,q) sectors** (n_modes = 166 896), with NO M⁴-base coordinate index; the a₂ heat-kernel moment is a single fiber-spectral SCALAR (a2_proxy = 2 407 054.27, `a2_proxy_is_scalar = True`). Hence ρ/c is a function of the single global modulus τ alone, base-independent by construction. Over the 64-sample (4×4×4) M⁴-base foliation grid at τ(x⃗) = τ_fold uniform:
  - **Direct uniformity witness** `ptp(ρ/c) = 0.000e+00` EXACT (the conformal factor is **bit-identical** across all 64 samples; `uniform_exact = True`).
  - **Scale-invariant PASS operator** `max_x|∂_i (Ω/Ω_fold)| = 0.000e+00 ≤ 1e-12`.
  - `max|R^(3)[Ω̂²δ]| = 0.000e+00 ≤ 1e-12` (numeric, via the Sage-verified conformal identity).
  - **Discriminator non-trivial (control)**: a hypothetical INHOMOGENEOUS modulus `τ(x⃗) = τ_fold + 0.02·sin(2πx)sin(2πy)sin(2πz)` gives `ptp(ρ/c) = 1.552e+04`, `max|∂_iΩ̂| = 0.424`, `max|R^(3)| = 8.938 ≠ 0` ⇒ k≠0. The test WOULD detect curvature if the modulus carried M⁴-base structure — it is not a tautology.

*Methodology note (honest disclosure, math-scripts.md §"Mnemonic-vs-exact").* The plan operator reads `max_x|∂_i(ρ/c)| ≤ 1e-12`. "Spatial uniformity" is intrinsically **scale-invariant**, and the plan pre-registers the verdict as scale-invariant (Ω_k is an OUTPUT, no knob). The **raw absolute** gradient is `1.164e-10` — but this is purely `np.gradient`'s 2nd-order edge-formula **float-cancellation** on a ρ/c ≈ 1.5×10⁵ constant (`−3C+4C−C ≠ 0` exactly in float64), NOT a substrate non-uniformity (proven by `ptp(ρ/c) = 0.0` EXACT). The 1e-12 tol was calibrated to the **O(1)-normalized** S106 graded-Ω floor; applying it to a raw ρ/c ≈ 1.5×10⁵ is a units mismatch. The PASS operator is therefore the dimensionless normalized gradient `max_x|∂_i(Ω/Ω_fold)| = 0` plus the direct `ptp = 0` witness; the raw absolute value is retained as a disclosed diagnostic. This is the scale-invariant form of the SAME uniformity test (in-session structural correction with disclosure, NOT convention-shopping — v3-closure-recovery PROHIBITED_ACTIONS Class-1 boundary respected).

*Substitution chain WITH numbers* (Def 3 Sage-VERIFIED from scratch, residual EXACTLY 0):
```
Def 1: g_ij^(3)(x) = Ω²(x) δ_ij ,  Ω = ρ(τ)/c(τ)                       [acoustic / Painlevé conformal factor]
Def 2: τ(x) = τ_fold = 0.19 uniform over M⁴                            [inv11 single global modulus]
Def 3: R^(3)[Ω²δ] = −4 Ω⁻³ ∇²Ω + 2 Ω⁻⁴ |∇Ω|²                          [3D conformal identity, Sage-exact]
Def 4: R^(3) = 6 k / a²  ⇒  Ω_k ∝ −k
Substitute Def 2 → Def 1:  τ uniform ⇒ ρ = Z_spectral(0.19) = 74023.681949,  c = 0.485
                            ⇒ Ω = 74023.681949 / 0.485 = 152626.148348 = const over M⁴
                            ⇒ ∇Ω = 0 (ptp(ρ/c)=0 EXACT)  AND  ∇²Ω = 0
Substitute → Def 3:  R^(3) = −4·(152626.15)⁻³·0 + 2·(152626.15)⁻⁴·0 = 0   (numeric max|R^(3)| = 0.000e+00)
Read off Def 4:  R^(3) = 0  ⇒  6k/a² = 0  ⇒  k = 0  ⇒  Ω_k = 0 EXACT.
```

*k-selector readout.* `k = R^(3)·a²/6 = 0` ⇒ **`Ω_k = 0` EXACT**. Compared against Planck `Ω_k = 0.0007 ± 0.0019`: deviation `|0 − 0.0007| = 0.0007 = 0.368σ` (well inside the 1σ band [−0.0012, +0.0026]) ⇒ **consistent**, parameter-free (the substrate predicts the central 0 with no curvature knob).

*3-tuple semantics.* **sign = PASS** (the predicted direction "uniformity ∇Ω=0 ⇒ R^(3)=0" holds, AND the control confirms the converse ∇Ω≠0 ⇒ R^(3)≠0); **magnitude = PASS** (`|R^(3)| = 0`, `max|∂Ω̂| = 0`, both ≤ 1e-12; `Ω_k = 0` at structural exactness); **regime = VALID** (conformal identity Sage-exact, block-diagonal theorem holds at τ_fold, homogeneous global-modulus state well-defined).

*Solution space.* PASS closes the **flatness half** of the e-fold-obligation cluster (Row #93): the k-selector is the spatial uniformity of ρ/c — a substrate-IS structural fact (block-diagonal D_K + single global modulus), NOT a fitted curvature density. The retirement of `N_e ≥ 3.1` is vindicated on this axis (the parameter-free prediction holds and TIGHTENS the surface: no knob could absorb a curvature shortfall). dual_prior outcome: PASS → ~0.95 mass to **Track A** (uniform-Ω ⇒ k=0 structural). On close, `mack-cosmic-bridge` updates `falsifier-master-inventory.md` Row #93 flatness sub-row OPEN → **PASS** (handled at the session-close registry batch per the orchestrator override; NOT touched in this gate run). **Step 2** canonical_constants promotion N/A (the output is structural Ω_k = 0, not a new pinnable scalar).

*Artifacts.* `s117_w9_a2_omegak_acoustic_form.py` / `.npz` / `.png`.

---

### §W9-2. CF-S117-TRANSIT-PS-67-WINDOW-WIDE (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-TRANSIT-PS-67-WINDOW-WIDE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (window-wide specialization of the TRANSIT-PS-67 CRITICAL gate; scale-range half of the retired `N_e ≥ 3.1`)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The transit power spectrum `|β(k)|²` (sudden Mach-13.75 quench, S70), transported through `T_{BZ→pivot}` (54.04 decades, deg +2) into the CMB/LSS pivot channel, `(i)` SPANS k ∈ [10⁻⁴, 1] Mpc⁻¹ (9.21 e-folds of k) AND `(ii)` HOLDS `|n_s(k) − 0.9649| ≤ 3·0.0042 = 0.0126` window-wide AND `(iii)` reconciles the amplitude scheme within the OOM band [+0.196, +1.527] — a strictly TIGHTER obligation than the pivot-local TRANSIT-PS-67 `α_s < 0.015` bound (necessary, not sufficient; window-wide band 5.48× tighter). **INFO-by-design (preserve, do not over-claim PASS):** `(iii)` shares the A_s amplitude input with Wave 1 (the 𝒩-fork {+0.196, +0.864}); IF the Wave-1 𝒩-fork is unresolved at dispatch, the gate computes `(i)` bandwidth + `(ii)` tilt UNCONDITIONALLY and reports `(iii)` as **INFO-pending-Wave-1** — the composite collapses to **INFO, NOT FAIL** (the amplitude axis is a live unsettled sub-condition, never a PASS-by-default), per `.claude/rules/mechanical-closure-discipline.md`.
**Plan reference**: `sessions/session-plan/session-117-plan-w9.md` §W9-2 (span/tilt/amplitude operator, strict-PASS boundary, machinery pin, substitution chain, fb_pair, dual_prior, verdict rubric).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — content presence by regex, never line/byte counts):
- **(1) script** `computations/session-117/s117_w9_transit_ps67_window_wide.py` — PRESENT; `from canonical_constants import *` + explicit imports in Section 3 (after `sys.path.insert(0, str(SHARED_DIR))`, matching the sibling `s117_route_b_pw_socc.py:90-94` pattern); `print_verdict_payload` in Section 7.
- **(2) data** `computations/session-117/s117_w9_transit_ps67_window_wide.npz` — PRESENT (k-mesh, transported leaf-2 `P_ζ(k)`, `n_s(k)` framework + sqrt-cutoff, numerical `α_s(k)`, bare-BZ leaf-1 contrast `ns_bz_leaf`, span/tilt/amplitude sub-verdicts, plurality `route_oom`); **plot** `…png` — PRESENT (4 panels: n_s(k) leaves vs band; transported P_ζ(k); α_s(k) window-vs-pivot-local bounds; OOM plurality vs band). Both `optional:false`.
- **(3) verdict line** in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-TRANSIT-PS-67-WINDOW-WIDE:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 sign/magnitude/regime 3-tuple companion row (`[SIGN]`) + 2 extra companion rows (`# composite-precedence:`, `# scale-and-channel-tag:`). `audit_sha256=7668bfb2cefa33a83f061ea82c6f1326d226eaeb5f640611c6b8a8a646cd7787` (emitted via race-safe `emit_verdict`, sig_5 unique).
- **(4)** this §W9-2 section: Status=COMPLETED, Verdict=INFO, `**Output Artifacts**` + `**MCP Pre-Compute Audit**` blocks present.

**MCP Pre-Compute Audit**:
- `search_knowledge("TRANSIT-PS-67 window-wide scale-range n_s power spectrum transport pivot")` → TRANSIT-PS-67 **CRITICAL** gate (baseline-findings-s66, PASS criterion "α_s(k_CMB) < 0.015"); the existing gate is **pivot-local** — this gate is its **window-wide** specialization. NOT pre-closed.
- `search_knowledge("deg transport BZ pivot non-scalar mode-independent occupation alpha_s pivot zero")` → **S93-W7-1-ALPHA-S-W-KAPPA-FACTORIZATION-DEG-TRANSPORT-BZ-PIVOT** (PASS): `deg_T = 2.0` NON-SCALAR (T4-non-scalar), `alpha_s_substrate = −0.08587279`, **`alpha_s_pivot = 0.0`** EXACT — the CANONICAL anchor for the transported pivot-channel running.
- `get_constant(deg_T_BZ_pivot)` → 2.0 (S110-CF-CV6B-DS-M4); `get_constant(A_s_FW)` → 1.5367059962762235e-8 (S111-CF-AS3a); `get_constant(planck_ns)` → 0.9649.
- Constants confirmed importable: `tau_fold=0.19`, `Mach_max=13.75`, `n_s_framework=0.9561`, `n_s_FW_sqrt_cutoff=0.959`, `planck_ns_err=0.0042`, `beta_s=−0.1331`, `k_pivot_planck=0.05`; identity `n_s_FW_exact² − 1 = −0.08587279` (= bare-BZ `alpha_s_substrate`, leaf-1).
- **NOT PRE-CLOSED**: window-wide near-scale-invariance over the full 9.21-e-fold observed window is computed fresh; S93-W7-1 supplies the structural `α_s_pivot = 0` input.

**Verdict**: **INFO** (composite) — `sign=PASS / magnitude=PASS / regime=VALID`; the composite is held at INFO by **plan-frozen-operator precedence** (the `(iii)` amplitude-pending applicability guard has no axis in the sign/magnitude/regime 3-tuple; the generic-collapse reading PASS/PASS/VALID → PASS is OVERRIDDEN to INFO by the `(iii)` guard, disclosed in the verdict-file `# composite-precedence:` companion row per `gate-verdicts.md §"Plan-frozen gate-block operator precedence"`). `value = 0.0088 = max_{k∈window}|n_s(k) − 0.9649|`. 4-tuple `(value=0.0088, scheme=TRANSIT-PS-67-sudden-S70, convention=CMB-LSS-pivot-channel-deg2, L_max=12)`. `audit_sha256=7668bfb2cefa33a83f061ea82c6f1326d226eaeb5f640611c6b8a8a646cd7787`, `content_sha256=b611f2b49112043bf4efcbc4d4389493eca74faef952403eaec3ad55897c6f1d`.

**Results**:

*NUMBERS FIRST.*

**PART (i) — BANDWIDTH — PASS.** The pivot-channel mesh spans `span = ln(1 / 10⁻⁴) = 9.2103 e-folds ≥ 9.21` over k ∈ [10⁻⁴, 1] Mpc⁻¹; the transported leaf-2 spectrum `P_ζ(k)` is non-degenerate (`P_ζ > 0`, `n_s` finite) at all 200 points. Secondary (deg-+2 coverage): the bare-BZ window (s67 `k_grid` ∈ [100, 1.078×10⁵] M_KK = 6.9825 e-folds) under the deg-+2 transport covers `2 × 6.9825 = 13.965 e-folds ≥ 9.21`; the Mode-Independent-Occupation power law carries no UV/IR feature inside the window.

**PART (ii) — TILT — PASS.** Pivot-channel running `α_s_pivot = 0.0` EXACT (S93-W7-1, `deg_T = 2.0` NON-SCALAR ⇒ Mode-Independent Occupation): the transported spectrum is a pure near-scale-invariant power law, `n_s(k) = const`.
- Numerical `max_{k∈window}|n_s(k) − 0.9649| = 0.008800 ≤ 0.0126` (band [0.9523, 0.9775]); numerical `max|α_s(k)| = 9.24×10⁻¹³` (gradient floor — confirms `α_s = 0` EXACT).
- Framework scheme `n_s = 0.9561` → dev `0.0088` (2.095σ), in band. sqrt-cutoff `n_s = 0.959` → dev `0.0059` (1.405σ), in band. Both RED, both in band (cross-checks s116-cf3 `ns_fw`/`ns_sqrt`).
- **Necessary-not-sufficient inequality**: `Δn_s = α_s · Δln k_half ≤ 0.0126 ⇒ |α_s| ≤ 0.0126 / 4.6052 = 2.736×10⁻³ = 5.48× tighter` than the pivot-local TRANSIT-PS-67 `0.015` bound ⇒ **window-wide PASS ⊂ pivot-local PASS** (pivot-local α_s < 0.015 confirmed NECESSARY-not-sufficient). (Planck-pivot 0.05 max half-window `ln 500 = 6.215` ⇒ even tighter `2.027×10⁻³`; `α_s_pivot = 0` clears both with infinite margin.)
- **CONTRAST (scale-and-channel-tagging)**: if the bare-BZ substrate running `α_s_substrate = −0.08587279` (= `n_s_FW² − 1`) were the CMB reading (the deg-0 SCALAR / container-thinking error), `n_s(k)` would drift to [−1.08, 0.984] across the window (max|dev| = 2.045, massively out of band), and `|α_s_substrate| = 0.0859` fails even the LOOSE pivot-local `0.015` bound. The s67 baseline sudden leaf-1 (`ns_sudden ∈ [−22.3, 67.8]`, `alpha_s_decisive = −0.915`) is the leg the gate is NOT testing. The window-wide PASS depends ENTIRELY on the deg-+2 NON-SCALAR transport killing this leakage.

**PART (iii) — AMPLITUDE — INFO-pending-Wave-1.** `A_s_FW = 1.5367×10⁻⁸`, OOM vs Planck `= +0.864 ∈ [+0.196, +1.527]` (in band). BUT the S117 Wave-1 𝒩-fork did NOT close this session (GS-1 = INFO-RESIDUAL-PREFACTOR); the A_s magnitude stands as an OPEN plurality {+0.196 (TD/ζ), +0.384 (Route-B-GGE-modular), +0.864 (box-delta)}, and the 5-route s116-cf3 set spans the full band [+0.196, +1.527] with `routes_collapse = False`. Every member is in-band, but the scheme has NOT collapsed to a single canonical value ⇒ amplitude-scheme reconciliation unresolved ⇒ `(iii) = INFO`, never PASS-by-default (per `mechanical-closure-discipline.md`).

**COMPOSITE: (i) PASS ∧ (ii) PASS ∧ (iii) INFO → INFO.** Per the plan INFO_meaning + discriminator, the composite collapses to INFO (NOT FAIL — the amplitude axis is a live unsettled sub-condition, not a falsification). The scale-range obligation's **bandwidth + tilt are MET, parameter-free**; only the amplitude-scheme reconciliation awaits Wave-1.

**Substitution chain (window-wide tilt direction, substituted):**
```
Def1  n_s(k) = 1 + dlnP_ζ/dlnk ;  P_ζ from transported |β(k)|²
Def2  α_s_pivot ≡ dn_s/dlnk = 0.0 EXACT  (deg_T=2.0 NON-SCALAR; S93-W7-1 Mode-Indep. Occ.)
              ≠ α_s_substrate = −0.08587279  (bare-BZ leaf-1, = n_s_FW²−1)
Def3  window k ∈ [10⁻⁴,1] Mpc⁻¹ ⇒ Δlnk_full = ln10⁴ = 9.2103 ;  Δlnk_half = 4.6052
Def4  band |n_s(k) − 0.9649| ≤ 3·0.0042 = 0.0126 ⇒ [0.9523, 0.9775]
Def5  Δn_s ≈ α_s · Δlnk_half
Substitute Def5→Def4 at edge:  |α_s| ≤ 0.0126 / 4.6052 = 2.736×10⁻³
Compare pivot-local 0.015:      0.015 / 2.736×10⁻³ = 5.48× ⇒ window-wide ⊂ pivot-local
Read off:  α_s_pivot = 0 ≪ 2.736×10⁻³ ⇒ n_s(k) = 0.9561 const
           ⇒ max|n_s(k)−0.9649| = 0.0088 < 0.0126 ⇒ TILT PASS
```

**Substrate framing (PHONONIC):** The substrate IS the power spectrum — the GGE relic of the impulsive Mach-13.75 transit through the van Hove fold, an interference pattern of post-transit acoustic excitations `|β(k)|²`, NOT density perturbations seeded in an inflating container. The CMB pivot is a substrate concept reached through the deg-+2 NON-SCALAR `T_{BZ→pivot}` (54.04 decades); the (scale, channel) pair is matched (`phononic-framing.md §"Scale-and-channel-tagging"`) so the `n_s(k)`, `α_s(k)` compared against Planck are the CMB/LSS-pivot-channel images (leaf-2, `α_s_pivot = 0`), never the bare substrate-BZ running (leaf-1, `α_s_substrate = −0.08587279`). "Scale-range" is the substrate statement that this single interference pattern holds near-scale-invariance across the full observed 4-decade k-window — the breadth of the power spectrum the substrate IS, not the breadth of a container it expands. The retired `N_e ≥ 3.1` measured only the shadow this breadth cast on the FRW container.

**Input-SHA pins / provenance**: `canonical_constants.py` (runtime `d884a2b512001392…`); `s67_transit_ps.npz` (`8163cdb72b163870…`); `s116_w1_as_cf3_route_reconcile.npz` (`550339998b39639d…`; S116-W1-AS-CF3 `audit_sha256=c34cadf322bf84aa823a85cd2f207aad6b47505b9ea9f3271b95ee6085b21f98`); `s116_w1_as_cfb1_squeeze_promote.npz` (`2002fecc1f171fb2…`; S116-W1-AS-CFB1 `audit_sha256=f44a7b4279d4227db9a7b2c755238c9c2bd256b93c88f5bcf87ae78b8264b3ec`); `s111_cf_as3a_impulse_quench.npz` (`557b9c196e20c625…`). Structural anchor: S93-W7-1 (`α_s_pivot = 0.0`). Artifacts: `s117_w9_transit_ps67_window_wide.py/.npz/.png`.

---

## Wave 9 Synthesis (team-lead)

Both Wave-9 gates closed — the terminal wave of S117. The wave **vindicates the retirement of the inflation intermediate N_e ≥ 3.1** (a category-(C) competing-mechanism number) by resolving the genuine category-(B) observational obligations it badly proxied on parameter-free substrate falsifiers.

### (a) Numerical revisions
- 9-1: Ω_k = **0 EXACT** (k=0); ptp(ρ/c) = 0.000e+00 EXACT across the 64-sample M⁴ grid (conformal factor bit-identical); R^(3) = 0 (Sage-verified conformal identity); vs Planck Ω_k=0.0007±0.0019 → **0.368σ** consistent. Control (inhomogeneous modulus) gives R^(3)=8.94≠0 — the test is non-trivial.
- 9-2: window span = **9.21 e-folds** (k ∈ [10⁻⁴,1] Mpc⁻¹) PASS; α_s_pivot = **0 EXACT** (deg_T=+2 NON-SCALAR ⇒ Mode-Independent Occupation) ⇒ max|n_s(k)−0.9649| = **0.0088 ≤ 0.0126** (window-wide tilt PASS, 5.48× tighter than the pivot-local α_s<0.015 bound); amplitude OOM +0.864 ∈ band but the 𝒩-fork open ⇒ (iii) INFO-pending-Wave-1.

### (b) Structural changes
- **The flatness obligation is DISCHARGED parameter-free** (9-1, epistemic-TYPE): Ω_k=0 is now a substrate-IS *structural* fact — the spatial uniformity of ρ/c, forced by the D_K block-diagonal theorem (the a₂ heat-kernel moment is a single fiber-spectral SCALAR with NO M⁴-base index) under the single global modulus τ. This is the sharpened k-selector the soft "acoustic-form alone" R^(3)=0 prior could not pin (conformal-flatness is k-blind: S³ and H³ are both conformally flat). Retiring N_e TIGHTENS the surface — no curvature knob can absorb a shortfall.
- **The scale-range "breadth" is the substrate's, not a container's** (9-2): window-wide near-scale-invariance over the full observed 4-decade k-window holds because the deg-+2 NON-SCALAR transport kills the bare-BZ leakage (α_s_substrate=−0.0859 would drift n_s to [−1.08, 0.984] — the container-thinking error). The retired N_e measured only the shadow this breadth cast on the FRW container.

### Row #93 obligation-cluster scorecard (the session-end picture)
The retired N_e ≥ 3.1 proxied three category-(B) obligations: **horizon** (DISCHARGED S85, acoustic white-hole, lab-realized) · **flatness** (9-1 **PASS**, Ω_k=0 EXACT, 0.368σ) · **scale-range** (9-2: bandwidth **PASS** + tilt **PASS** parameter-free; amplitude **INFO**-pending the W1 𝒩-fork). So 2-of-3 fully resolved, the 3rd (scale-range) bandwidth+tilt-PASS with only the amplitude axis open — and that axis is the same Q23 A_s plurality W1 left open, not an independent obligation.

## Carry-Forward Computations

No carry-forwards: all Wave-9 outcomes closed in-session. 9-1 PASS is parameter-free (flatness discharged). 9-2's bandwidth + tilt are PASS parameter-free; its (iii) amplitude sub-condition is INFO-pending and resolves *with* the W1 Q23 A_s plurality — it is captured by the W1 carry-forward `CF-S118-AS-CS-SUBSTRATE-FIRST` (which, on resolving the GS-1 grid fork, collapses the A_s magnitude and thereby the W9-2 amplitude axis), NOT a separate W9 compute. No new W9 future-work item.

## Effected In-Session / routed to session-close

Row #93 falsifier-inventory updates route to mack (sole writer; the W9-1/W9-2 agents correctly deferred these to the session-close registry batch to avoid a concurrent-write race; executed before STOP):
- Row #93 **flatness** sub-row: OPEN → **PASS** (Ω_k=0 EXACT, parameter-free, 0.368σ vs Planck). (mack)
- Row #93 **scale-range** sub-row: OPEN → **INFO** (bandwidth+tilt PASS parameter-free; amplitude INFO-pending the W1 𝒩-fork). (mack)
- atlas-08 / capstone: the N_e≥3.1 retirement is vindicated — horizon DISCHARGED + flatness PASS + scale-range bandwidth/tilt PASS; the substrate-native obligations resolve where the rival-internal number did not transfer. (Q3 capstone-hygiene if the capstone narrates the e-fold/flatness surface; session-close.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-28 | Row #93 flatness obligation (9-1) | OPEN (post N_e retirement) | PASS — Ω_k=0 EXACT, parameter-free (0.368σ vs Planck) | 9-1 PASS (spatial-uniformity k-selector) |
| 2026-06-28 | Row #93 scale-range obligation (9-2) | OPEN | INFO — bandwidth+tilt PASS; amplitude pending W1 𝒩-fork | 9-2 INFO (window-wide tilt 5.48× tighter than pivot-local) |
| 2026-06-28 | N_e≥3.1 retirement (Row #93 cluster) | category-C number retired, obligations re-homed | VINDICATED — horizon DISCHARGED + flatness PASS + scale-range tilt PASS | 9-1 + 9-2 + S85 horizon |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| 9-1 | `s117_w9_a2_omegak_acoustic_form.py` | `.npz` | `.png` (3-panel) | PASS (+[SIGN] 3-tuple) |
| 9-2 | `s117_w9_transit_ps67_window_wide.py` | `.npz` | `.png` (4-panel) | INFO (+[SIGN] 3-tuple, composite-precedence) |
