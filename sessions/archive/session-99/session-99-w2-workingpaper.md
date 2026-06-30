# Session 99 Wave 2 — C10 DILUTION-CC discharge cluster (Results Working Paper)

**Session**: 99 | **Wave**: W2 | **Plan**: session-99-plan-w2.md | **Theme**: C10 DILUTION-CC discharge cluster — friction-ODE relaxation closure (HARD-after Wave 1) + BBN additional relief.

## Gate Sections

### §W2-1. S99-W2-RELAXATION-CLOSURE (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S99-W2-RELAXATION-CLOSURE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (V(q)=δρ_vac is the GGE / zero-point vacuum-energy response of the D_K spectrum; q is the substrate vacuum variable; the friction ODE is the substrate's own relaxation, NOT a field rolling IN a container)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The late-time attractor slope d ln q/d ln H = 1 (⇒ rho_vac ~ H², Volovik tracking exponent n=2) emerges UNFORCED from the substrate friction ODE q″ + 3Hq′ + V′(q)=0 (V(q)=δρ_vac, k_curv=+3586.5 from the 992 D_K eigenfrequencies) integrated along the Wave-1 NON-conformally-stationary H(τ) — NOT by imposing the slow-roll quasi-static relation.
**Plan reference**: `sessions/session-plan/session-99-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source).

**Branch taken — FULL friction-ODE run (DP-W1→W2-A FIRED)**: W1-1 (`S99-W1-Q-NONRATIO-OBSERVABLE`) landed **INFO** with a VALID non-stationary backbone (`H_bare_nonstationarity_relvar = 0.38866`, **5.72 OOM** above the a_eff stationarity floor `aeff_relvar = 7.43e-7`, ≫ the >1-OOM guard). Per the plan's W1→W2 decision point this fires the FULL friction-ODE attractor computation (NOT the PRE-REG-INC mechanical closure — that branch is reserved for W1-1 = FAIL/UNCOMPUTED or a conformally-stationary backbone, neither of which occurred). The backbone `arr_H_bare_t` (shape (999,), all-positive, finite, τ ∈ [0.19026, 0.45078] monotone, total e-folds N=0.0465, H spans 0.0691→0.3056 i.e. Δln H ≈ 1.48 — ample log-log dynamic range) was loaded as the substrate H(τ) the ODE integrates against.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain (verified) |
|:---------|:-----|:------------------------|
| script | `computations/session-99/s99_w2_relaxation_closure.py` | `from canonical_constants import` ✓ ; `print_verdict_payload` ✓ |
| data | `computations/session-99/s99_w2_relaxation_closure.npz` | present (72 KB) ✓ |
| plot | `computations/session-99/s99_w2_relaxation_closure.png` | present (235 KB) ✓ |
| verdict_line | `computations/session-99/s99_gate_verdicts.txt` | `^S99-W2-RELAXATION-CLOSURE:.* audit_sha256=[a-f0-9]{64}` ✓ ; dual-SHA companion row ✓ ; schema-v2 [SIGN] 3-tuple companion ✓ |
| wp_section | this §W2-1 | Status COMPLETED ✓ ; Verdict FAIL ✓ ; Output Artifacts ✓ ; MCP Pre-Compute Audit ✓ |

`audit_sha256 = e0e16d244223a19f02cc9f36470a65a5657abf658284cdbc8c539df24b6ca1e8` (over script‖canonical‖pinmap); `content_sha256 = c27a343dd6d58ba024b362a91ce86765146f994653c3e201947230ce2ff8fa68` (over script). 4-tuple: `(value=3.4159253901686504, scheme=FW, convention=ABSOLUTE, L_max=12)`.

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `get_constant("a_0_FW_zeta")` | **6440.0** (S88, S88-A-N-FW-CANONICALIZATION; not superseded). The CC IS the a₀ zeroth Seeley-DeWitt moment; regulator_pin `a_0^{ζ}` confirmed. |
| `trace_entity("DILUTION-CC")` | DILUTION-CC-66 **PASS** (Scenario B; rho_vac~M_Pl²H², Volovik tracking; closes 114 OOM to 0.01 OOM). C10 discharge is the consumer; this gate tests its Object-C leg. |
| `search_knowledge("S98-W2-2-RELAXATION-CLOSURE PRE-REG-INC q-attractor friction ODE")` | `S98-W2-2-RELAXATION-CLOSURE` = **FAIL / PRE-REG-INC** (blocked by AOFT conformal-stationary frame, q-attractor 0/0, full-run deferred to **CF-S99**). The S98 V.2 predecessor was a mechanical closure that never ran the ODE — no prior ODE construction to inherit. **`S99-W2-RELAXATION-CLOSURE` itself NOT in the graph → cleared to compute (not pre-closed).** |

**Verdict**: **FAIL** (composite). Dual-prior → **Track B** (0.45 → 0.9 on FAIL): n=2 requires a free closure parameter; C10 Object C remains underived; C10 stays **ASSUMED-PARTIALLY-PROVEN**; capstone §8.5 stays **OPEN**. [SIGN] 3-tuple: `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN`.

**Results**:

NUMBERS first.

- **slope_BARE (UNFORCED — the PRIMARY gate value)** = **3.4159**, log-log R² = 0.0790. This is the bare-substrate friction ODE `q″ + 3H(τ)q′ + k_curv·(q−q*) = 0` with `q* = q0_ref = 0.0` const and **no imposed H-drive** — the substrate's own relaxation. With `k_curv = +3586.53` and `H ∈ [0.069, 0.306]`, the discriminant `9H² − 4k_curv ≈ −14344 < 0` ⇒ the characteristic roots are complex (`−0.75 ± 59.9i`, Sage-verified): a LIGHTLY-DAMPED oscillator about q=0 (≈2.5 oscillations over the τ-span, decay factor e^(−0.75·0.26)≈0.82). It crosses zero, so ln|q−q*| has cusps and there is **no clean monotone H-tracking tail** (R²=0.079; the 3.42 "slope" is a meaningless fit through a non-power-law). `|slope_BARE − 1| = 2.4159`.
- **slope_DRIVEN (IMPOSED linear closure q_eq(H)=c·H)** = **1.00827**, R² = 0.9590, **c-invariant** (slope@2c = 1.00827, identical to 8 sig figs). The driven ODE `q″ + 3Hq′ + k_curv·(q − c·H) = 0` with `c = dq_dH = 0.15` (the S97 "LINEAR slow-roll closure / simple-fluid input", S97 lines 419-483). The adiabatic theorem (ω_osc = √k_curv ≈ 59.9 ≫ Ḣ/H ≈ 4) makes q track the moving equilibrium q_eq = c·H, so d ln q/d ln H → 1. The c-invariance proves the slope-1 is a **structural consequence of the imposed q_eq ∝ H¹ exponent, not a tuned scale** — but the linear exponent itself is the imposed closure.
- **forced_only = True**: slope=1 (n=2) arises ONLY under the imposed linear closure.
- **k_curv = +3586.531181** (restoring-well convex curvature). Raw `d²E/dq²|₀ = −3586.531181` (energy convention, S98 `cf_s99_k_curv` + S97 `d2E_dq2_0`); S97 `k_curv = +3586.531181` (restoring-well |curv|). **sign_consistent = True** (matches the +3586.5 plan PIN).
- **domain_used_frac (bare attractor window) = 0.41** (transient_end_idx=499/999, clean-window len=205 < 0.50·intended_tail) ⇒ regime BREAKDOWN.
- **H non-stationarity relvar = 0.38866 ≫ a_eff floor 7.43e-7** (the W1→W2 non-stationarity premise holds; the backbone is genuinely non-conformally-stationary).

GATE second.

The 3-tuple maps as: **sign_verdict = PASS** — the substitution chain predicts a POSITIVE tracking exponent (slope = n/2 > 0; q grows with H); the driven (tracking) slope +1.008 > 0 confirms the predicted DIRECTION. **magnitude_verdict = FAIL** — slope=1 does NOT emerge UNFORCED; per the pre-registered FAIL_meaning (plan §W2-1 lines 239-240): "the slope=1 result only arises by imposing the slow-roll quasi-static relation / a free closure parameter ⇒ n=2 is NOT a substrate-forced attractor." **regime_verdict = BREAKDOWN** — the bare attractor window is >50% shortened (domain_used_frac=0.41 < 0.50; the bare oscillator has no clean monotone tracking tail), per the auto-shortening clause of `.claude/rules/gate-verdicts.md`. Composite collapse (pre-registered): `regime_verdict==BREAKDOWN ⇒ composite=FAIL` (and `magnitude_verdict==FAIL ∧ regime==VALID` would independently give FAIL — both routes agree).

**Substitution chain (slope = n/2 = 1), Sage-exact** — confirms the analytic target while the gate shows it is NOT unforced:

1. V(q) = ½·k_curv·(q−q*)² + const ⇒ rho_vac ∝ (q−q*)² (Volovik q-theory rho_vac = ε(q)−μq, leading quadratic part about q*).
2. Tracking law rho_vac ∝ Hⁿ (Volovik Gibbs-Duhem, n=2; session-66-mack-transit-workshop T.61).
3. Equate: (q−q*)² ∝ Hⁿ ⇒ (q−q*) ∝ H^(n/2) ⇒ **slope ≡ d ln q/d ln H = n/2**. At n=2: **slope = 1** (Sage-exact: p=n/2, p|_{n=2}=1). [The from-below n_eff=1.978110506 gives slope = 0.98906, `|slope−1|=0.01094`, also in-band — Sage-exact QQ.]

The structural point: the friction ODE faithfully TRANSMITS the exponent of q_eq(H) to the dynamical slope via adiabatic tracking (driven=1.008). It does NOT *manufacture* the exponent 1 — it inherits it from the imposed `q_eq ∝ H¹`. Per S97 (lines 419-483, `q_of_H = q_ref·H/H_ref`, explicitly labelled "LINEAR slow-roll closure / simple-fluid input"; S97 discriminator `CONSEQUENCE-on-quadratic-V_CONDITIONAL-on-fluid-closure`, sign_verdict=FAIL, joint_pass=False), the `q∝H` relation is IMPOSED, not substrate-derived. The substrate gives rho_vac(eq)=0 EXACT (Gibbs-Duhem, S95 EQUILIBRIUM-CC-WARRANT) and q=0 as the only interior equilibrium (S62 Monotonicity #19) — no substrate mechanism forces q_eq ∝ H. Hence n=2 is a CONSEQUENCE of the imposed fluid closure, not an unforced attractor of the substrate's own relaxation.

**k_curv sign sub-chain (Routh-Hurwitz; Sage-verified)** — linearize δ=q−q*: δ″ + 3Hδ′ + k_curv·δ = 0; characteristic r² + 3Hr + k_curv = 0. **k_curv > 0** (convex restoring well, +3586.53): roots `−0.75 ± 59.9i`, both Re<0 ⇒ damped-oscillatory **ATTRACTOR**. **k_curv < 0** (concave, −3586.53): roots `−60.6, +59.1`, one Re>0 ⇒ **REPELLER** ⇒ friction cannot relax q onto the tracking law ⇒ slope diverges ⇒ FAIL by construction. The convex restoring well (+|k_curv|) is the UNIQUE sign admitting a tracking attractor. **SIGN RESOLVED: k_curv = +3586.53.** (The raw d²E/dq²|₀ = −3586.53 is the energy-convention second derivative; the restoring-force curvature in V′(q)=k_curv(q−q*) is its absolute value.)

**Multiplicative-cancellation pre-flight (per `.claude/rules/math-scripts.md §"Multiplicative-normalization cancellation invariants"`): NOT-FIRED** (echo of the S98 V.2 pre-flight). The slope `d ln q/d ln H` is a log-derivative of the friction-ODE SOLUTION q(H) along the H(τ) backbone — q(H) is NOT a multiplicative-factorized trace `w(L_max)·g(K)`. The L_max=12 dependence enters ONLY through the single numeric coefficient k_curv (the 992 omega_n(q)=√(λ²+q) eigenfrequencies precomputed from the cache), not as an L_max-dependent spectral-support weight multiplying a K-kernel; no `d^n ln(·)/d(ln K)^n` operator annihilates an L_max factor here.

**Substrate-first assessment**: PHONONIC. The cosmological constant IS the a₀ zeroth spectral moment (a_0_FW_zeta=6440.0, zeta-regulated) — a DIFFERENT spectral moment than gravity (a₂). The Volovik vacuum variable q IS the substrate's own slow degree of freedom; V(q)=δρ_vac is the GGE/zero-point response of the 992 D_K eigenfrequencies. The friction ODE q″+3Hq′+V′(q)=0 is the SUBSTRATE'S OWN relaxation — NOT a scalar field rolling IN a pre-existing spacetime container. The arrow flows D_K eigenvalues → a₀ → V(q)=δρ_vac → friction-ODE attractor → rho_vac~H^n. **The substrate finding: integrated against its own non-stationary H(τ) backbone, the substrate's bare relaxation (convex well at q=0, no substrate-derived H-drive) is a lightly-damped oscillator with NO unforced H-tracking tail; the n=2 / slope=1 tracking law is recoverable ONLY when the LINEAR equilibrium closure q_eq ∝ H¹ is imposed (the S97 simple-fluid input). The exponent-on-q=2 leg is substrate-forced (quadratic V from D_K); the d ln q/d ln H = 1 leg is the imposed fluid closure, not substrate-forced.** Therefore C10 Object C (an UNFORCED tracking attractor) is NOT closed; C10 remains ASSUMED-PARTIALLY-PROVEN and capstone §8.5 stays OPEN. This is the Track-B corridor: the tracking law `rho_vac ~ M_Pl²H²` is a posited ansatz (substrate-justified in its exponent-on-q but requiring an imposed fluid closure for the H-tracking), not a derived attractor of the substrate's own cosmological relaxation. **FAIL is a valid, informative result**: it closes the corridor "n=2 as an unforced friction-ODE attractor" and pins where the residual conditionality of the DILUTION-CC discharge lives (the q∝H fluid closure).

**Carry-forward (CF-S100)**: a candidate substrate-derived H-dependent equilibrium drive `q_eq(H)` — if one can be derived from the substrate (e.g. a Hubble-sourced chemical-potential shift in the Volovik Gibbs-Duhem relation, rather than the imposed `q∝H` simple-fluid input) — would re-open the UNFORCED slope=1 test. Until then, the C10 tracking-vacuum exponent n=2 is substrate-forced only in its exponent-on-q factor; the d ln q/d ln H = 1 factor remains an imposed fluid closure (the structurally-honest reading of S97's `CONSEQUENCE-on-quadratic-V_CONDITIONAL-on-fluid-closure`).

---

### §W2-2. S99-W2-BBN-RELIEF (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S99-W2-BBN-RELIEF`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the BBN-epoch vacuum fraction is the a₀ tracking-vacuum (Volovik) evaluated at the radiation-dominated BBN epoch; rho_vac = α_V M_Pl² H^{n_eff} is the substrate a₀ response)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: An additional substrate-justified relief mechanism (larger from-below n_eff shift, epoch-dependent α_V, OR a distinct dilution channel) brings the BBN-epoch vacuum fraction from (rho_vac/rho_rad)_BBN = 0.474049 (ΔN_eff=2.0873) down to ΔN_eff(vacuum) ≤ 1 (ratio ≤ 0.227113) at the SINGLE substrate-justified lever X=ln(H_BBN/H_0)=40.2756 — NOT by scanning the lever.
**Plan reference**: `sessions/session-plan/session-99-plan-w2.md` §W2-2 (machinery pin, thresholds, substitution chain source). **INDEPENDENT of W1-1/W2-1** — consumes only the S98 V.9 / V.10 static npz outputs and dispatches regardless of the Wave-1 verdict.

**Output Artifacts** (closure-verification checklist; verified on disk):

| Artifact | Path | must_contain — verified |
|:--|:--|:--|
| script | `computations/session-99/s99_w2_bbn_relief.py` | `from canonical_constants import` ✓ ; `print_verdict_payload` ✓ |
| data | `computations/session-99/s99_w2_bbn_relief.npz` | present (14578 B) |
| plot | `computations/session-99/s99_w2_bbn_relief.png` | present (127909 B) |
| verdict_line | `computations/session-99/s99_gate_verdicts.txt` | `^S99-W2-BBN-RELIEF:.* audit_sha256=[a-f0-9]{64}` ✓ ; dual-SHA companion ✓ ; schema-v2 [SIGN] 3-tuple ✓ |
| wp_section | this §W2-2 | Status COMPLETED ✓ ; Verdict FAIL ✓ ; Output Artifacts ✓ ; MCP Pre-Compute Audit ✓ |

`audit_sha256 = 8fe0ef45395c71d0233e5509cfaf0a3b10c5ec1758997cc57ea94e96d0e08949` ; `content_sha256 = 338e6e098d17797a8f...` (full: `338e6e098d17797a8f8b977df5fdf4e5c5695075f5c2ee1d807a0c5e1c14fd6f`). Verdict emitted via the race-safe `mcp__knowledge__emit_verdict` tool (4 rows: canonical + dual-SHA companion + [SIGN] 3-tuple + `regulator_pin=a_0^{zeta}`).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:--|:--|
| `get_constant("rho_vac_over_rho_obs")` | 1.032 (DILUTION-CC-66, S97, Volovik tracking-vacuum; C10 ASSUMED-PARTIALLY-PROVEN). **Confirmed**. |
| `get_constant("a_0_FW_zeta")` | 6440.0 (S88; zeta-regulated zeroth Seeley-DeWitt moment). **Confirmed**. |
| `get_constant("rho_vac_over_rho_rad_BBN_below")` | 0.474049 (S98 V.10; from-below baseline). **Confirmed**. |
| `get_constant("delta_N_eff_vacuum_BBN_below")` | 2.0873 (S98 V.10; FAIL-side falsifier). **Confirmed**. |
| `search_knowledge("BBN N_eff vacuum fraction relief …")` | S98-MK3-2-BBN-VACUUM-FRACTION = **FAIL** (frac_below=0.4740, bound=0.2271, dNeff=2.0873, X=40.2756). `S99-W2-BBN-RELIEF` itself **NOT closed** — not in the graph. **Cleared to compute**. |
| `trace_entity("DILUTION-CC")` | DILUTION-CC-66 PASS Scenario B; closes 114-OOM gap to 0.01 OOM; rho_vac~M_Pl²H². No prior BBN-relief closure. |
| `list_constants("BBN")` | bound NOT a named canonical (T_BBN_GeV, z_BBN, g_star_BBN present); bound computed from canonical S66 formula `(7/8)(4/11)^(4/3)`. |

Not PRE-CLOSED. The S98 BBN gate is a FAIL anchor; this gate tests whether a substrate mechanism RELIEVES it.

**Verdict**: **FAIL** — composite of (sign_verdict=**PASS**, magnitude_verdict=**FAIL**, regime_verdict=**VALID**); collapse rule `magnitude FAIL ∧ regime VALID ⇒ FAIL`. The from-below relief is in the CORRECT direction (relief_factor 0.4141 < 1) but the residual ΔN_eff = 2.0873 > 1 is not closed by any **substrate-justified** mechanism. **Track B — the BBN-arm tension is STRUCTURAL** (dual_prior 0.45 Track A → 0.9 Track B on FAIL). This is a real structural finding, not a failure of execution: the Volovik tracking-vacuum's from-below sub-leading correction relieves the BBN vacuum fraction by ~2.4× (1.1447 → 0.4740) but falls ~2.087× short of the BBN/CMB ΔN_eff ≤ 1 datum, and the additional ≤0.479 factor is not delivered by any of the three candidate channels at a substrate-fixed parameter.

**Results**:

**Output 4-tuple**: `(value=2.087335415592305, scheme=FW, convention=ABSOLUTE, L_max=N/A)` (ΔN_eff at the best UNFORCED — i.e. substrate-justified — relief; none of (a)/(b)/(c) qualifies, so the value equals the from-below baseline).

**Substrate-correct lever (validated to machine precision).** The BBN-epoch vacuum fraction is

```
(rho_vac/rho_rad)_BBN = frac_base · (H_BBN/H_0)^{n_eff−2} = frac_base · exp((n_eff−2)·X),   X = ln(H_BBN/H_0) = 40.2756
```

with `frac_base = 1.144730` (n=2 baseline), `n_eff = 1.978111` (HARD from-below, S98 V.9, divergence_type=A). Reproduction: `frac_base · exp((n_eff−2)·X) = 1.144730 · 0.414115 = 0.474049` — matches the S98 V.10 canonical `frac_below = 0.474049` to **0.000e+00 residual**.

**[PLAN-TEXT lever-form discrepancy — process observation, documented not propagated].** The plan §W2-2 substitution chain WRITES the lever as `X^{n_eff−2} = 40.2756^{−0.021889} = 0.9222894`. That form **double-logs X** (X is already `ln(H_BBN/H_0)`), giving `frac_base · X^{n_eff−2} = 1.0558` and `ΔN_eff = 4.65`, which **contradicts the canonical** S98 V.10 `ΔN_eff = 2.0873`. The substrate-correct lever — the one the S98 V.10 npz actually used and that reproduces the canonical to 0.0e+00 — is `exp((n_eff−2)·X)`. The plan chain's relief **direction** logic ((n_eff−2)<0 ∧ X>0 ⇒ relief_factor<1) is correct under BOTH forms, so the [SIGN] sign_verdict is unaffected. Flagged for the team-lead constraint-map; per `epistemic-discipline.md §"Source Reconciliation"` this is a plan-text-vs-substrate-canonical drift resolved in favor of the substrate-first source (the npz lever).

**[BBN bound — substrate-first sourcing].** The bound is the canonical S66 formula `(7/8)(4/11)^{4/3} = 0.227107` (matches the S98 npz `bound = 0.227107` exactly). The plan-pinned literal `0.227113` is a rounded value (drift 5.68e-06); the exact-formula value is adopted per `substrate-first-canonical-sourcing.md`.

**[SIGN] relief-direction substitution chain (executed, NUMBERS):**

| Step | Quantity | Value | Sign |
|:--|:--|:--|:--|
| exponent | `(n_eff − 2)` | −0.021889 | NEGATIVE (n_eff < 2) |
| lever | `X = ln(H_BBN/H_0)` | +40.2756 | POSITIVE (H_BBN ≫ H_0) |
| ⇒ relief | `relief_factor = exp((n_eff−2)·X)` | 0.414115 | **< 1 ⇒ relief** |

`(n_eff−2) < 0 ∧ X > 0 ⇒ exp((n_eff−2)·X) < 1`. The from-below departure SUPPRESSES the BBN vacuum fraction — **direction CORRECT** ⇒ `sign_verdict = PASS`.

**Magnitude shortfall.** baseline `ΔN_eff = frac_below/bound = 0.474049/0.227107 = 2.0873`; additional suppression required ON TOP of the from-below relief `= bound/frac_below = 0.479080` (a further ~2.087× reduction).

**Three candidate relief mechanisms (each reaches ΔN_eff = 1 ONLY at a NON-substrate parameter):**

| Mechanism | Required parameter to hit ΔN_eff = 1 | Substrate-derived value | Substrate-justified? |
|:--|:--|:--|:--|
| **(a)** larger from-below shift Δn | `n_eff = 1.959839` (n−2 = −0.040161; **1.835×** the substrate shift) | HARD `n_eff = 1.978111` (V.9, divergence_type=A) — the sub-leading sign computation FIXES it; a 1.835× larger shift is not derived | **NO** |
| **(b)** epoch-dependent α_V | `α_V,BBN/α_V,0 = 0.479080` | DILUTION-CC-66 uses ONE α_V (single a₀ tracking normalization; z=0 lever=1 leaves rho_vac/rho_obs=1.032 unaffected); no substrate forces α_V(z) to halve at BBN | **NO** |
| **(c)** distinct dilution channel | `N_eff/992 = 0.479080` ⇒ **475 of 992** D_K modes contribute (cc-path-d D-57 mode-fraction channel) | all 992 modes gravitate (`a₀ = ζ_{D_K}(0) = Tr(1)` counts the full set); no substrate sub-selects ~475 modes at BBN | **NO** |

`any_substrate_justified = False` ⇒ `magnitude_verdict = FAIL` ⇒ composite **FAIL** ⇒ `track_B_structural = True`.

**Multiplicative-normalization cancellation pre-flight: NOT-FIRED.** The BBN ratio is a closed-form modified-Friedmann lever `frac_base·exp((n_eff−2)·X)` in the cosmological scale X, not a trace over the D_K spectrum; no L_max truncation weight is present (n_eff is pinned upstream at L_max=12), so the `math-scripts.md §"Multiplicative-normalization cancellation invariants"` annihilation is inapplicable by construction.

**Substrate-first assessment.** The BBN-epoch vacuum fraction IS the a₀ tracking-vacuum (Volovik, the spectral-action ZEROTH moment `a_0_FW_zeta=6440.0` — a DIFFERENT spectral moment than gravity a₂) evaluated at the radiation-dominated BBN epoch: arrow `D_K eigenvalues → a₀ zeroth spectral moment → rho_vac = α_V M_Pl² H^{n_eff} → (rho_vac/rho_rad)_BBN → ΔN_eff`. The from-below `n_eff < 2` is the substrate's own sub-leading correction to the tracking law (NOT a fitted parameter); the lever X is the substrate's emergent expansion history between BBN and today (single substrate-fixed rad-dom epoch, NOT scanned). DESI/Planck N_eff is the laboratory-IN falsifier; the tracking-vacuum is substrate-IS. **Falsifier consequence**: the BBN ΔN_eff bound remains a LIVE falsifier on the Volovik tracking-vacuum — `BBN-VOLOVIK-67` / `Window-8` stay OPEN at nucleosynthesis. The present-epoch DILUTION-CC closure (`rho_vac/rho_obs = 1.032`, z=0 lever=1) is UNAFFECTED — the BBN-arm tension does NOT reopen the present-epoch CC closure; it is the high-z arm of the same tracking-vacuum that the BBN N_eff datum constrains. (Per the spawn instruction, the `falsifier-master-inventory.md` BBN-row landing is a session-end orchestrator routing action — NOT written in this run.)

---

## Wave 2 Synthesis (team-lead)

**W2-1 `S99-W2-RELAXATION-CLOSURE` — FAIL** (3-tuple sign=PASS, magnitude=FAIL, regime=BREAKDOWN; DP-W1→W2-A full run on the verified non-stationary backbone). The n=2 tracking slope `d ln q/d ln H = 1` is NOT an unforced substrate attractor. The bare substrate friction-ODE (convex well `k_curv = +3586.5`, Routh-Hurwitz attractor sign) is a lightly-damped oscillator (complex roots −0.75±59.9i) with no monotone H-tracking tail (slope_bare = 3.42, R² = 0.08, domain_used_frac 0.41 → BREAKDOWN). Slope = 1 (1.0083) arises ONLY under an imposed linear fluid closure `q_eq = c·H`. The substrate gives ρ_vac(eq)=0 (Gibbs-Duhem, S95) and q=0 as the only interior equilibrium (S62 #19) — no substrate-derived H-drive. **The exponent-on-q = 2 leg IS substrate-forced** (quadratic V from the D_K eigenfrequencies); **the d ln q/d ln H = 1 leg is the imposed closure** — that split is the gate's scientific content.

**W2-2 `S99-W2-BBN-RELIEF` — FAIL** (3-tuple sign=PASS, magnitude=FAIL, regime=VALID; Track B structural). The from-below n_eff = 1.978111 relief is real and correct-direction (`relief_factor = exp((n_eff−2)·X) = 0.414`, baseline 1.1447 → 0.474) but ~2.087× too weak (ΔN_eff = 2.0873 > 1); none of the 3 candidate mechanisms (larger Δn / epoch-dependent α_V / distinct dilution channel) is substrate-justified to deliver the residual ×0.479. The BBN-arm tension is STRUCTURAL; BBN-VOLOVIK-67 / Window-8 stays a LIVE falsifier (mack §7 annotation on inventory Row #76). Present-epoch DILUTION-CC closure (ρ_vac/ρ_obs = 1.032) is UNAFFECTED.

Solution-space: the C10 DILUTION-CC discharge stays CONDITIONAL on BOTH legs — the relaxation-attractor (n=2 needs an imposed fluid closure, not substrate-forced) AND the BBN-arm (relief insufficient by ~9.2×). The discharge's residual conditionality is now precisely located: the missing substrate `q_eq(H)` drive (W2-1) and the missing BBN suppression mechanism (W2-2). C10 stays **ASSUMED-PARTIALLY-PROVEN**; capstone §8.5 stays **OPEN**. The "n=2 as an unforced friction-ODE attractor" corridor is CLOSED.

**Carry-Forward Computations (math)**: CF-S100-W2-1-QEQ-DRIVE (below). **Effected In-Session (non-math)**: (1) §W2-2 plan-text `post-hoc:` lever-form correction (`session-99-plan-w2.md` — `X^{n−2}` double-log → `exp((n−2)·X)`; verdict unaffected); (2) BBN-VOLOVIK-67 stays-live annotation (mack, inventory Row #76). Both recorded in `session-99-housekeeping.md §A`.

## Carry-Forward Computations

### CF-S100-W2-1-QEQ-DRIVE — substrate-derived q_eq(H) drive for the unforced n=2 attractor test [genuine-math]

From §W2-1 (FAIL; slope=1 only under an imposed `q_eq = c·H`). The substrate's bare friction-ODE has no monotone H-tracking tail and no substrate-derived H-drive; n=2 is a fluid-closure INPUT, not a substrate-FORCED attractor. Determine whether a substrate-internal cosmological back-reaction supplies an H-dependent equilibrium that makes the tracking slope emerge unforced.

| Field | Spec |
|:------|:-----|
| **What** | Derive a substrate-internal `q_eq(H)` drive (an H-dependent equilibrium/source from the substrate's own back-reaction — e.g. a back-reaction closure `H² = f(ρ_relic, S_SA)` per capstone §6.3, not an imposed CPL fluid law) and re-integrate the friction-ODE WITHOUT the imposed linear closure; test whether `d ln q/d ln H = 1` (n=2) then emerges unforced. |
| **Inputs** | `s99_w2_relaxation_closure.npz` (bare-ODE oscillator solution, k_curv = +3586.5, q_boundary); `s99_w1_q_nonratio_observable.npz` (`arr_H_bare_t` backbone); Volovik Gibbs-Duhem ρ_vac(eq)=0 (S95); S62 #19 (q=0 interior equilibrium); `canonical_constants.py` (a_0_FW_zeta). |
| **Gate** | `[SIGN]`: PASS iff a substrate-derived `q_eq(H)` yields `|slope − 1| ≤ 0.05` UNFORCED (C10 Object-C → substrate-forced, §8.5 OPEN→CLOSED); INFO iff slope narrows toward 1 but a residual closure parameter survives; FAIL iff no substrate `q_eq(H)` drive exists (n=2 is structurally a fluid-closure input — C10 Object-C closes STRUCTURALLY-CONDITIONAL, §8.5 stays OPEN by design). |
| **Effort** | ~1–2 waves (the substrate back-reaction `q_eq(H)` derivation is the hard part; the ODE re-run + log-log regression is cheap). |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-01 | C10 Object-C (n=2 unforced friction-ODE attractor) | ASSUMED-PARTIALLY-PROVEN (S98 V.2 PRE-REG-INC) | ASSUMED-PARTIALLY-PROVEN (unchanged; n=2-as-unforced-attractor corridor CLOSED) | S99 W2-1 FAIL: slope=1 only under imposed fluid closure; exponent-on-q=2 substrate-forced, d ln q/d ln H=1 leg imposed |
| 2026-06-01 | capstone §8.5 C10 DILUTION-CC discharge | OPEN (conditional) | OPEN (stays; both legs conditional) | S99 W2-1 FAIL + W2-2 FAIL — discharge conditional on substrate q_eq(H) drive + BBN suppression |
| 2026-06-01 | BBN-VOLOVIK-67 / Window-8 ΔN_eff falsifier | live (S67) | live (stays; structural sub-threshold tension, ~9.2× too weak) | S99 W2-2 FAIL: from-below relief correct-direction but magnitude-insufficient; no substrate-justified mechanism |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| S99-W2-RELAXATION-CLOSURE | `computations/session-99/s99_w2_relaxation_closure.py` | `s99_w2_relaxation_closure.npz` | `s99_w2_relaxation_closure.png` | FAIL (audit `e0e16d24…`) |
| S99-W2-BBN-RELIEF | `computations/session-99/s99_w2_bbn_relief.py` | `s99_w2_bbn_relief.npz` | `s99_w2_bbn_relief.png` | FAIL (audit `8fe0ef45…`) |
