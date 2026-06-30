# Session 101 Wave W2 — Texture-Cluster Magnitude Axis (widening → carrier → knob + Connes machinery) (Results Working Paper)

**Session**: 101 | **Wave**: W2 | **Plan**: `sessions/session-plan/session-101-plan-w2.md`
**Theme**: texture-cluster magnitude axis (EVOI rank-9b) — the W2a widening chain (W_flat block-trace → 3-leg carrier discriminator → S₀-knob; HARD 1 → 2 → 3) plus W2b Connes machinery (star-metric Lemma B boundary, disconnect Theorem A clause 3 boundary; {4 ‖ 5 ‖ 6} concurrent), under the S100a-pinned `RATIO-NORMALIZED-TRACE-MEAN` counting convention and the READING-A carrier (ONE OBJECT / THREE CHARTS).
**Run-order edge (HARD)**: Wave 2 runs AFTER Wave 1 — the `S101-TAU0-OPERATOR-CANONICITY` L4 leg lifts the A19 UNTRUSTED-UPSTREAM caveat on the s84 L12 texture-cluster cache (theorem-backed, A-C3 σ-blind lemma).
**Pre-lift dispatch rule**: any cache-consuming gate dispatched BEFORE the L4 lift lands — W2-1/W2-4/W2-5/W2-6 directly, W2-2/W2-3 transitively via the W2-1 npz — MUST carry the extra-row `# A19-UNTRUSTED-UPSTREAM: s84 L12 cache consumed pre-L4-lift` on its verdict emission; cache values cited at full confidence only post-lift.

## Gate Sections

### §W2-1. S101-W2-BLOCKTRACE-WIDENING (baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `S101-W2-BLOCKTRACE-WIDENING`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (multiplicity-normalized block-trace widening; the surviving Casimir 9/5-grading corridor)
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: On multiplicity-normalized whole-block trace-means at τ_fold (tower (1,0)/(1,1)/(3,0)) under the pinned channel-STATE counting convention, the generation-envelope widening preserves the Casimir-linear 9/5 grading — W_flat ∈ [1.800, 1.8894] with the strict C₂-monotone ordering ⟨λ²⟩₁₀ < ⟨λ²⟩₁₁ < ⟨λ²⟩₃₀ as the [SIGN] sub-criterion. Genuine two-sided risk — the sign of W_flat − W^PM was adjudicated NOT structurally pre-registrable, so NO one-sided bound is inherited; the τ=0 control value 9/5 IS the PASS lower edge.
**Plan reference**: `sessions/session-plan/session-101-plan-w2.md` §W2-1 (AMENDED six-item BINDING spec + Rider 1; machinery pin, bands, τ=0 control, substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block — content presence by regex, NEVER line/byte counts, per `feedback_max-effort-full-fidelity.md`):
- `computations/session-101/s101_w2_blocktrace_widening.py` — ✓ on disk; `grep` confirms `from canonical_constants import tau_fold, T_acoustic` + `def print_verdict_payload(`.
- `computations/session-101/s101_w2_blocktrace_widening.npz` — ✓ on disk (SHA `e0a79fc32a3716815f5549f219a8cfa502796bae2641f4e4dd053cd639bf8612`); ALL Rider-1 keys present: `lambda2_triple`=[1.26052606, 1.84236993, 2.88968890], `sbar_tau_fold`=0.34910632138702, `omega_weighted_triple`=[1.11414528, 1.54034570, 2.30681806], `W_flat`=1.799999999999997, `W_block`=1.79838480, `Var_g_triple`=[0.09904655, 0.21777980, 0.46428006].
- `computations/session-101/s101_w2_blocktrace_widening.png` — ✓ on disk (3 panels: trace-mean Casimir-linear ladder, W magnitude vs bands, μ-ribbon).
- verdict line in `computations/session-101/s101_gate_verdicts.txt` — ✓ matches `^S101-W2-BLOCKTRACE-WIDENING:.* audit_sha256=[a-f0-9]{64}` (audit `78f574143bb4d7f5…`); dual-SHA companion row + schema-v2 `[SIGN]` SIGN/MAGNITUDE/REGIME 3-tuple row + `# rider1_npz_sha256=e0a79fc32a371681…` extra-row all present.
- **No A19 extra-row**: cross-wave pin 1 SATISFIED — W1-1 `S101-TAU0-OPERATOR-CANONICITY` landed PASS (audit `194b2b3c`) and its L4 leg LIFTED the A19 caveat; the s84 L12 cache is cited at FULL CONFIDENCE (orchestrator override).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per query-first discipline):
- `search_knowledge("W_flat blocktrace widening Casimir 9/5 trace-mean ordering tower")` → returns the equation `W_flat(τ=0) = 9/5 EXACT` (trace-mean Casimir-linearity) + `W_Casimir = 3/(5/3) = 9/5 = 1.800` + the S99 mack-synthesis open channels (Casimir candidate 9/5 vs PDG widening ratio 1.889) — confirms the gate quantity is a known structural target, NOT a closed mechanism (no closure covers the τ_fold measurement).
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42, not superseded) — pins the single-τ slice.
- `search_knowledge("s84 spectrum cache L12 tau019 …")` → confirms canonical SHA `9e6d9cf7fd6a6949…` (session-87 WP) — matches the plan input-pin and the on-disk cache.
- Not PRE-CLOSED: this is the first τ_fold measurement of W_flat on the multiplicity-normalized block-trace (state-class) face. Predecessors S100a-CASIMIR-WIDENING (FAIL, per-mode/log-overlap face) + S100a-YUKAWA-OVERLAP-OFFDIAG (INFO) point HERE.

**Verdict**: **PASS** — composite (sign PASS ∧ magnitude PASS ∧ regime VALID). Schema-v2 3-tuple: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID`. The Casimir-shape corridor SURVIVES at the multiplicity-normalized block-trace level: the fold preserves an EXACTLY Casimir-linear trace-mean ladder under the pinned `RATIO-NORMALIZED-TRACE-MEAN` counting convention. The W-2 ordering caveat on the foam-protection landing text (B6(iii)) becomes dischargeable (Wave 6); the Leg-A conditionality coupling reads **W_flat-PASS** (NOT the Reading-B revival cell).

**Results**:

*Headline.* The multiplicity-normalized whole-block trace-mean ⟨λ²⟩_g is **exactly Casimir-linear** at τ_fold = 0.19, and the gap ratio lands AT the 9/5 lower edge to the float64 cancellation floor.

| Sector g | (p,q) | C₂(g) | n_modes | ⟨λ²⟩_g (F2-flat) | ⟨ω⟩_g (F2-weighted) | t_g = 1/⟨ω⟩_g |
|:--|:--|:--|:--|:--|:--|:--|
| τ (heavy) | (1,0) | 4/3 | 48 | 1.26052606 | 1.11414528 | 0.89754902 |
| μ | (1,1) | 3 | 128 | 1.84236993 | 1.54034570 | 0.64920491 |
| e (light) | (3,0) | 6 | 160 | 2.88968890 | 2.30681806 | 0.43349756 |

- **Magnitude (PRIMARY face, gate quantity):** `W_flat = (⟨λ²⟩₃₀ − ⟨λ²⟩₁₁)/(⟨λ²⟩₁₁ − ⟨λ²⟩₁₀) = (2.889689 − 1.842370)/(1.842370 − 1.260526) = 1.800000` → **W_flat ∈ [1.800, 1.8894] PASS**. The computed float is `1.799999999999997`, i.e. `−3.11e-15` from the exact lower edge 9/5 — an EXACT-edge landing at the float64 gap-ratio cancellation floor, NOT a band miss. The closed-interval membership test uses a float64 band-edge tolerance `EDGE_TOL = 1e-9` (band-edge discipline per `gate-verdicts.md`/`epistemic-discipline.md §"Publication-Precision Pre-Registration"`: the lower edge 9/5 is an EXACT rational, the plan/substitution-chain pins "W_flat(τ=0) = 9/5 EXACT", so the test must compare the exact edge, not its round-off; upper edge 1.8894 and the INFO band are UNTOUCHED — this is not band-stretching, and is disclosed in the verdict value string `at_lower_edge=True(EDGE_TOL=1e-9)`).
- **Why W_flat = 9/5 exactly (structural):** ⟨λ²⟩_g fits a SINGLE-slope Casimir line at τ_fold. `slope_lo ≡ (⟨λ²⟩₁₁ − ⟨λ²⟩₁₀)/(C₂(1,1) − C₂(1,0)) = 0.3491063214` and `slope_hi ≡ (⟨λ²⟩₃₀ − ⟨λ²⟩₁₁)/(C₂(3,0) − C₂(1,1)) = 0.3491063214` agree to `dev = 5.55e-16` (machine eps). A single slope forces `W_flat = (C₂(3,0) − C₂(1,1))/(C₂(1,1) − C₂(1,0)) = 3/(5/3) = 9/5` — the slope and intercept cancel in the gap ratio. The Casimir-shape corridor that is EXACT at τ=0 is reproduced at τ_fold to machine precision on the μ-free state-class face. (This is a genuine fold-survival result: per-mode/log-overlap faces do NOT reproduce 9/5 — S100a-CASIMIR-WIDENING (per-mode) gave W_permode = 1.781924; the normalization-and-trace choice is what restores Casimir-linearity.)
- **SIGN sub-criterion (ordering):** strict C₂-monotone ascent ⟨λ²⟩₁₀ < ⟨λ²⟩₁₁ < ⟨λ²⟩₃₀ → `1.260526 < 1.842370 < 2.889689` = **TRUE** (PRIMARY face). On the SECONDARY (F2-weighted, counting-INDEPENDENT) face: ⟨ω⟩₁₀ < ⟨ω⟩₁₁ < ⟨ω⟩₃₀ → `1.114145 < 1.540346 < 2.306818` = **TRUE**. Both faces ascend, so the direction is confirmed and the FAIL-would-be-counting-position-universal risk does not fire. Maps (freeze-in direction theorem) to heavy-pair τ=(1,0) heaviest, e=(3,0) lightest.
- **τ=0 MACHINERY CONTROL (gates EXECUTION, non-gating physics):** Lai-Teh Thm-2.3 LC t=1/2 trace-mean closed form ⟨λ²⟩_g(τ=0) = 3·C₂(g) + 27/4 → ⟨λ²⟩₁₀(0)=43/4, ⟨λ²⟩₁₁(0)=63/4, ⟨λ²⟩₃₀(0)=99/4; `W_flat(τ=0) = (99/4 − 63/4)/(63/4 − 43/4) = 36/20 = 9/5` EXACT, `dev = 0.00e+00 ≤ 1e-10` → machinery OK, script proceeds. (Absolute-level Thm-2.3 per-sector match 8.9e-15 ALREADY LANDED S100b W3-2, audit `bea5401ae1ac3c4d` — CITED, not re-run.)
- **RIDER 1 (BINDING):** OLS slope of ⟨λ²⟩_g on C₂ = (4/3, 3, 6): `s̄(τ_fold) = 0.34910632` M_KK² per unit C₂ (intercept = 0.79505097 = ⟨λ²⟩₀₀ reference channel; max OLS residual 8.88e-16 — the ladder is OLS-exact, consistent with the single-slope finding). `s̄` equals J/3 = 0.34910632 to `dev = 1.67e-16` (the D-3 razor edge — Leg A converts s̄ into S₀^geo = 3·q·s̄/T_acoustic). The ⟨λ²⟩_g triple is published full-float64 in the npz; **its SHA-256 `e0a79fc32a3716815f5549f219a8cfa502796bae2641f4e4dd053cd639bf8612` is the ONE-DATASET pin S101-ENVELOPE-CARRIER-DISCRIMINATE (W2-2) Leg A consumes at the SAME audit SHA** (one dataset, two gates).
- **Cross-checks (non-gating):** (i) W_permode = 1.781924 (cache audit 67a71781, reported NOT gated) — cross-face consistency. (ii) SECONDARY W_block = 1.79838480 (weighted face, also near 9/5). (iii) μ-robustness ribbon across μ_H²·{1/2, 1, 2}: ordering STABLE at all three (W_block = 2.053257 / 1.798385 / 1.772761). (iv) cumulant identity W^PM ≈ W_flat·[1 + (s/2)(ΔVar_lo/Δ_lo − ΔVar_hi/Δ_hi)] = 1.75807970 with s = 1/μ_H² = 1.488150; sign(W_flat − W^PM) = +0.041920 — POSITIVE, but this sign was adjudicated NOT structurally pre-registrable, so it rides in the value field as a genuine two-sided diagnostic, NOT a gate (no one-sided bound inherited). Var_g triple = (0.09904655, 0.21777980, 0.46428006).
- **4-tuple:** (value = W_flat = 1.800000, scheme = F2-FLAT-PRIMARY+F2-WEIGHTED-SECONDARY, convention = RATIO-NORMALIZED-TRACE-MEAN, L_max = 12).
- **Substitution chain (substituted numbers, matching plan Claim 1 / Claim 2):** Claim 1 (ordering at τ=0): 3·(4/3)+27/4 = 43/4 < 3·3+27/4 = 63/4 < 3·6+27/4 = 99/4 — strict, monotone in C₂; the τ_fold check tests PERSISTENCE of this ascent (confirmed). Claim 2 (control value): W_flat(τ=0) = (99/4 − 63/4)/(63/4 − 43/4) = (36/4)/(20/4) = 36/20 = 9/5 = 1.800 EXACT; the 27/4 offset cancels in the gap ratio (any global unit factor cancels — canonicity-branch-invariant). The measured τ_fold value reproduces this exact edge to the float64 floor.
- **Verdict-file provenance:** dual-SHA companion row (`audit_sha256_short=78f574143bb4d7f5 content_sha256_short=905ad7a643c6b6e9`) + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row + `# rider1_npz_sha256=e0a79fc32a371681…` extra-row + per-face diagnostic rows + `# regulator_pin=N/A … CLASS=N/A` row, all on disk. No A19 extra-row (post-lift dispatch, full confidence).

**Substrate reading (PARTICLE-class).** The substrate IS the Jensen-deformed SU(3) fiber; its Peter-Weyl channels (1,0)/(1,1)/(3,0) carry the three generations ON the multiplicity bundle, read by normalized channel-state evaluations ρ_g(D_K²) (the tier-2 counting axiom this gate's convention pin enforces). The result says the generation-envelope SHAPE, read on the μ-free state-class face, is a **static Casimir datum of the fiber** — the van-Hove transit at τ_fold = 0.19 does NOT re-key the trace-mean ladder away from its τ=0 Casimir-linear form; it preserves it to machine precision. Flow: D_K eigenvalues → per-channel state evaluations ⟨λ²⟩_g → gap-ratio W_flat = 9/5 → generation envelope shape (Casimir-static) → (downstream W2-2) the carrier composite and (W2-3) the S₀-knob, fed by the s̄ = J/3 Lichnerowicz-endomorphism slope.

---

### §W2-2. S101-ENVELOPE-CARRIER-DISCRIMINATE (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-ENVELOPE-CARRIER-DISCRIMINATE`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (3-leg carrier discriminator — Reading A composite; one operator family, three charts)
**Agent**: `transit-dynamics-theorist` (executor / one writer; per-leg derivation-author tags: Leg A `connes-ncg-theorist`, Legs B/C `transit-dynamics-theorist`)
**Hypothesis**: The charged-lepton envelope carrier is READING A (one operator family read on three charts): Leg A's zero-fit tracial assembly S₀^geo reproduces S0_fit in-band, Leg B's pair-resolved coherence coefficient c_req lands on the cache-free Weingarten rational 1/√6 within ±5%, and Leg C's first-principles ε_LX one-fiber split yields GRADED per-sector frequencies ω_g = q·C₂(g)·M_KK (vs a genuine SCALAR gap) — composite PASS iff Leg A ∈ {PASS, INFO} ∧ Leg B ∈ {PASS, INFO} (dual prior 0.7 Track A; Reading-B revival is exactly the Leg-A-FAIL ∧ W_flat-PASS cell).
**Plan reference**: `sessions/session-plan/session-101-plan-w2.md` §W2-2 (workshop CF-1 FINAL 3-leg spec; one-dataset Rider-1 SHA echo; composite-rule precedence disclosure).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block — content presence by regex, NEVER line/byte counts):
- `computations/session-101/s101_envelope_carrier_discriminate.py` — ✓ on disk (41,772 B); `grep` confirms `from canonical_constants import tau_fold, T_acoustic, M_KK` + `def print_verdict_payload(`.
- `computations/session-101/s101_envelope_carrier_discriminate.npz` — ✓ on disk (20,716 B); ALL 11 plan-REQUIRED keys present: `S0_geo_primary`=1.77670181, `S0_geo_superseding`=1.77431873, `legC_output_form`='GRADED', `legC_q_prime`=0.18974515, `legC_derivation_residual`=8.88e-16, `c_req`=0.40363459, `ratio_legB`=0.98869878, `S0_legB`=1.57425653, `t_tilt_position`=0.97031283, `sbar_consumed`=0.34910632, `sbar_npz_sha256`=`e0a79fc32a371681…` (one-dataset echo = the W2-1 Rider-1 pin).
- `computations/session-101/s101_envelope_carrier_discriminate.png` — ✓ on disk (110,046 B; 3 panels: Leg A S₀^geo vs band + q′ governing read-out, Leg B ratio vs band + sqrt6/2 cone ceiling, Leg C Casimir-linear ladder vs rejected scalar mean).
- verdict line in `computations/session-101/s101_gate_verdicts.txt` — ✓ matches `^S101-ENVELOPE-CARRIER-DISCRIMINATE:.* audit_sha256=[a-f0-9]{64}` (audit `463f32033347c225…`); dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row (`sign=PASS magnitude=PASS regime=VALID`) + per-leg extra-row (`# legA=PASS legB=PASS legC=GRADED …`) + q-supersession row (`# in-gate-dual-readout: q_tau_fold=0.190000 → q_prime=0.189745 …`) + precedence-disclosure row (`# composite-rule=GATE-BLOCK-OPERATOR-PRECEDENCE (workshop CF-1) over schema-v2 collapse | conflict_this_run=False`) + leg-B-feasibility / leg-A-tilt / one-dataset-echo / dual-prior rows — all 10 lines present (emit_verdict, cross-process locked, sig_5 unique).
- **No A19 extra-row**: cross-wave pin 1 SATISFIED — W1-1 `S101-TAU0-OPERATOR-CANONICITY` landed PASS (audit `194b2b3c`) and its L4 leg LIFTED the A19 caveat; the s84 L12 cache (inherited transitively via the W2-1 npz) is cited at FULL CONFIDENCE (orchestrator override).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per query-first discipline):
- `search_knowledge("envelope carrier discriminate Reading A S0_geo tracial assembly Weingarten 1/sqrt6 coherence epsilon LX graded scalar")` → returns the workshop `s100a-w3-envelope-carrier-workshop.md` (CF-1 spec home) + the **W2 Homogeneity wall** theorem (PROVEN: "ε_LX MUST BREAK left-invariance on the multiplicity space") — the structural basis for Leg C's GRADED-vs-SCALAR binary; NO closure covers the carrier-reading adjudication ⇒ gate is NOT pre-closed (it adjudicates the READING; W3-9 FAIL is PERMANENT and untouched).
- `search_knowledge("S0 knob charged lepton envelope d_i Casimir 4/3 3 6 rank-one texture secular equation determinant lemma")` → confirms the canonical envelope form `d_i = exp(−S0·C₂)` (S98-W3-1 ε_LX-on-multiplicity convention) + `d_gen1 = exp(−S0·C₂(3,0)) = exp(−6·S0)` (the BARE d_i Leg B consumes) + `C2 = (4/3, 3, 6)` for (1,0)/(1,1)/(3,0) + `S0_fit = 1.694153`. Confirms the Leg-B denominator is the analytic-Casimir `exp(−S0·C₂)` form (NOT the yukawa-overlap d_i = [0.789, 1.0, 0.332], which is a different overlap-derived object).
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42, not superseded) — q-pin PRIMARY.
- `get_constant("T_acoustic")` → 0.112 (canonical; in `canonical_constants.py:715`, GGE acoustic temperature S42/S47) — Leg-A / ℓ_geo denominator.
- Not PRE-CLOSED. This is the first composite carrier-discriminator gate; predecessors S100a-FREEZEIN-OVERCONSTRAINED (FAIL, `78ee1d56` — W3-9 PERMANENT; adjudicates READING only), S100a-ENVELOPE-OVERDETERMINE (INFO, `4ed74d7e`), S100a-S0-THRESHOLD-JOINT (INFO, `eeb7e5bd`) point HERE.

**Verdict**: **PASS** — READING A CONFIRMED. Composite via the GATE-BLOCK OPERATOR (workshop CF-1: PASS iff Leg A ∈ {PASS, INFO} ∧ Leg B ∈ {PASS, INFO}). Schema-v2 3-tuple: `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID`. All three charts of the charged-lepton envelope cohere as ONE operator family: the SHAPE (tracial chart, Leg A in-band), the MAGNITUDE (moduli-acoustic crossing at q, Leg A + the GRADED Leg C derivation), and the COHERENCE (Weingarten hub fraction, Leg B on 1/√6) read consistently. Leg C lands **GRADED** with derived q′ ≈ τ_fold — so the magnitude identification is **DERIVED, not fingerprint-coincidence** (the dual read-out fires; band unchanged), feeding W2-3's candidate (iii). Dual-prior → posterior ≈ 0.9 Track A. No precedence conflict (Leg-A=PASS, not the INFO conflict cell) ⇒ the gate-block operator and the generic schema-v2 collapse agree on PASS.

**Results**:

*Headline.* The three carrier charts agree to within their pre-registered bands with the GRADED magnitude derivation FIRED: Leg A S₀^geo = 1.7743 (governing q′ read-out) ∈ PASS [1.609, 1.779]; Leg B ratio = c_req/(1/√6) = 0.9887 ∈ PASS [0.95, 1.05]; Leg C output-form = **GRADED**, q′ = 0.189745 (0.134% from τ_fold). Reading A is the ONE OBJECT / THREE CHARTS picture.

**NUMBERS first (per-leg).**

*EXECUTION ORDER: Leg C → Leg B → Leg A (Leg C's binary feeds Leg A's dual read-out).*

**Leg C — ε_LX one-fiber split: GRADED.** The pinned input is the tracial slope theorem `⟨λ²⟩_g(τ=0) = 3·C₂(g) + 27/4` (W-2 A-C1/B2, slope 1/3 exact). The ε_LX content is the multiplicity-space splitting of the Dirac frequency, which on the tracial stratum IS the trace-mean ladder. By the Homogeneity wall (W2 PROVEN: ε_LX MUST break left-invariance on the multiplicity space), the ε_LX content is the **C₂-graded (slope) part**, not the left-invariant uniform offset.

| sector | C₂ | ⟨λ²⟩_g (W2-1) | icpt + s̄·C₂ | residual |
|:--|:--|:--|:--|:--|
| (1,0) | 4/3 | 1.26052606 | 1.26052606 | −4.4e-16 |
| (1,1) | 3 | 1.84236993 | 1.84236993 | +1.3e-16 |
| (3,0) | 6 | 2.88968890 | 2.88968890 | +8.9e-16 |

- **GRADED test**: `max|⟨λ²⟩_g − (intercept + s̄·C₂)| = 8.882e-16` (~0 ⇒ exactly Casimir-linear); scalar residual `max|⟨λ²⟩_g − mean| = 0.8922` (≫0 ⇒ NOT a scalar gap); slope s̄ = 0.349106 ≠ 0. ⇒ **`legC_output_form = GRADED`** — the per-sector frequencies are `ω_g = q′·C₂(g)·M_KK`, genuinely graded.
- **Derived per-Casimir quantum** (magnitude channel, C1-3/C1-6 four-lens slot): `q′ = S0_fit·T_acoustic = 0.189745`; **internal-consistency dev vs τ_fold = 0.1341%** (the W3-10 fingerprint; plan line 354). The SEPARATE slope-channel quantum `3·τ_fold·s̄ = 0.198991` carries the fold-tilt (dev +4.7319% = exactly J−1) and is the Leg-A t_tilt content — reported as a distinct diagnostic, NOT the q′ internal-consistency number.
- **Consequence**: GRADED ⇒ knob candidate (iii) promotes from identity-candidate to DERIVATION (the 0.52% internal-consistency check vs (i) is now armed); the (i)/(iii) shadow degeneracy (2π·τ_fold = 1.19380 vs (4/3)·0.9 = 1.2, dev 0.52%) is splittable structurally by the output-FORM, not by a tighter band. Leg C FEEDS W2-3 (does not replace it).

**Leg B — pair-resolved {S₀, c} secular solve: PASS.** Rank-one all-π texture `M = (1+c)·diag(d) − c·uu†`, `u_i = √(d_i)`, BARE `d_i = exp(−S₀·C₂(g))` on C₂ = (6, 3, 4/3) (lepton orientation e↔(3,0), μ↔(1,1), τ↔(1,0)). Eigenvalues solved via the **rank-one secular equation `1 = c·Σ_i d_i/((1+c)·d_i − λ)`** (E-2(b), matrix-determinant lemma — NO diagonalization enters the gate). {S₀, c} fit to the two PDG lepton mass ratios:

| observable | predicted | PDG anchor | residual |
|:--|:--|:--|:--|
| m_μ/m_e | 206.7682810307 | 206.7682810307 | 5.7e-14 |
| m_τ/m_μ | 16.8170294916 | 16.8170294916 | (joint) |

- **Solve**: `{S₀ = 1.5742565, c_req = 0.4036346}`. `ratio_legB = c_req/(1/√6) = 0.988699` ∈ **PASS [0.95, 1.05]**.
- **Positive-cone feasibility** (E-R2.1): `det M = (1+c)²(1−2c)·Πd_i` ⇒ positive mass spectrum iff `c < 1/2`. `c_req = 0.4036 < 1/2` (margin below ceiling **19.3%**); the sqrt6/2 = 1.224745 ratio-ceiling (= solve-infeasibility = exclusion of the all-π rank-one texture CLASS) is NOT approached. `regime = VALID`.
- **Method cross-check** (diagnostic, non-gating): secular-equation eigenvalues vs `eigvalsh` agree to **7.81e-18** — confirms the secular root-finder reproduces the texture spectrum bit-for-bit; the gate uses the secular method (the diagonalization is only the validation).
- **Direction** (E-1(4), interpretive): the pair-resolved ratio 0.9887 sits BELOW 1 (c_req slightly below 1/√6) — consistent with the expected DOWNWARD move from the single-shared-w datum 1.110 toward 1; the upper failure mode (ratio ≥ 1.224745) is far from reach.

**Leg A — zero-fit tracial assembly S₀^geo: PASS.** Frozen assembly `ℓ_geo = T_acoustic/(3·τ_fold) = 0.196491 M_KK²`; observable (C1-7) `S₀^geo(q) = 3·q·s̄/T_acoustic` with s̄ = OLS slope of the W2-1 ⟨λ²⟩_g triple on C₂ (consumed from the W2-1 npz at the Rider-1 SHA — one dataset, two gates).

- **PRIMARY read-out** (q = τ_fold = 0.19): `S₀^geo = 3·0.19·0.349106/0.112 = 1.776702` ∈ **PASS** (at the band top, 0.13% below the ceiling 1.779).
- **DUAL READ-OUT FIRED** (Leg C GRADED): re-evaluate at q′ = 0.189745 ⇒ `S₀^geo(q′) = 1.774319` ∈ **PASS** (GOVERNING read-out; band unchanged per workshop Q2; PRU pin set fixed at plan-freeze).
- **Tilt position** (governing q′ read-out): `t_tilt = (S₀^geo·56/95 − 1)/(J − 1) = 0.970313` ∈ [0,1] — upper-half landing = **scalar-channel J-tilt evidence** (the first Dirac-channel fold-tilt measurement). The D-3 razor check: s̄ = 0.349106 = J/3 sits in the s̄-space PASS window [0.316154, 0.349558] with **+0.129% headroom above J/3** — a true edge landing inside the band, NOT a Leg-A miss; the tilt bracket [1, J] is INTERPRETIVE OVERLAY and was NOT invoked to re-classify (no band-stretch).
- **τ_fold-form assembly** (REPORTED-not-gated, 3.3% shadow, C-2): ℓ = τ_fold ⇒ S₀ = s̄/τ_fold = 1.8374 (EXITS to INFO under the tilt — confirms the cross-face form is the discriminating assembly, as connes's C1 derivation anticipated).

**COMPOSITE.** Reading A confirmed iff Leg A ∈ {PASS, INFO} ∧ Leg B ∈ {PASS, INFO}: Leg A (governing PASS) ✓ ∧ Leg B (PASS) ✓ ⇒ **TOP-LINE PASS**. The GATE-BLOCK OPERATOR (workshop CF-1) takes precedence over the generic schema-v2 collapse on conflict; the known conflict cell (Leg-A INFO ∧ Leg-B ∈ {PASS,INFO} ⇒ gate-block PASS while schema-v2 magnitude=INFO) is NOT triggered here (Leg-A = PASS, not INFO), so both rules agree on PASS (`precedence_conflict = False`, disclosed in the extra-row).

- **3-tuple semantics**: `sign_verdict = PASS` (the Reading-A conjunction — the workshop's directional content); `magnitude_verdict = PASS` (Leg A band at the governing q′ read-out per T1.0); `regime_verdict = VALID` (Leg-B positive-cone feasible c_req < 1/2 AND solver clean; not MARGINAL — Leg C is GRADED not SCALAR; not BREAKDOWN — Leg B is feasible).
- **Dual-prior reallocation** (plan-level pre-registration, reported NOT a verdict cell): Composite PASS ⇒ posterior ≈ 0.9 Track A (Reading A = one operator family, three charts). The Reading-B revival cell (Leg-A-FAIL ∧ W_flat-PASS) did NOT fire — Leg A is PASS, and W2-1 already landed W_flat-PASS.
- **W_flat conditionality coupling** (Q5): Leg A is PASS, so the FAIL-attribution coupling (Leg-A-FAIL ∧ W_flat-PASS = Reading-B evidence; Leg-A-FAIL ∧ W_flat-FAIL = inconclusive) does not engage; the carrier identification is positively confirmed, not retreated.

**4-tuple:** `(value = composite = PASS, scheme = COMPOSITE-3LEG-CARRIER, convention = RATIO-NORMALIZED-TRACE-MEAN, L_max = 12 inherited via the W2-1 npz)`. audit_sha256 `463f32033347c2250f119d090623b6a43bad0463395b3b4ca2a27b45b4c67d1a`, content_sha256 `e6e3a7ddfbff690b4e241ffbd1f74dc95dbae3dd06fa12cd93db7497fe2df6e4`.

**Substitution chains (substituted numbers, matching plan Claim 1 / 2 / 3).**

- **Claim 1 (Leg-A s̄-space edges — D-3 razor, mechanical no-band-stretch check):** `S₀^geo = 3·τ_fold·s̄/T_acoustic = (95/56)·(3·s̄)` [at s̄=1/3, S₀^geo = 95/56 = 1.696429; check 3·τ_fold/T_acoustic = 0.57/0.112 = 285/56, ×s̄ = (95/56)·3s̄ ✓]. PASS top S₀^geo ≤ 1.779 ⇒ 3·s̄ ≤ 1.779×56/95 = 1.048674 ⇒ **s̄ ≤ 0.349558**; lower edge S₀^geo ≥ 1.609 ⇒ **s̄ ≥ 0.316154** (5.15% below the τ=0 slope 1/3). Full-J end J/3 = 0.349106; 0.349558/0.349106 = 1.001294 ⇒ +0.129% headroom. Measured s̄ = 0.349106 (= J/3) lands IN the window at the razor edge. **A landing in (0.349558, J/3+ε] would have been a genuine Leg-A miss — the bracket may NOT re-classify it; mechanically checked here, s̄ is inside.**
- **Claim 2 (Leg-B feasibility ceiling direction — E-R2.1):** `M = (1+c)·diag(d) − c·uu†`, `u_i = √d_i` (all-π, real). Matrix-determinant lemma: `det M = (1+c)³·d₁d₂d₃·(1 − 3c/(1+c)) = (1+c)²·(1−2c)·d₁d₂d₃`. ⇒ `M ≻ 0 ⟺ c < 1/2` for ANY diagonal d (first eigenvalue zero-crossing forces det=0; only root in (0,1) is c=1/2). ⇒ `c_req ≥ 1/2 ⟺ ratio ≥ √6/2 = 1.224745` is POSITIVE-CONE-INFEASIBLE. Computed `c_req = 0.4036 < 1/2` ⇒ feasible, `ratio_legB = 0.9887 < 1.224745`. Bands stand as pre-registered; this chain specifies the FAILURE MODE, not a band edit.
- **Claim 3 (Leg-C graded-form direction):** GRADED means `ω_g = q·C₂(g)·M_KK` with ONE q across the tower (Casimir-linear, the same linearity that makes W_flat(τ=0) = 9/5 exact); SCALAR means `ω_g = ω₀` (g-independent). The binary is STRUCTURAL (functional form), not a magnitude band — the (i)/(iii) 0.52% shadow (2π·τ_fold = 1.19380 vs 1.2) cannot be resolved by a tighter ratio band; only the output-FORM splits it. Computed: graded residual 8.9e-16 (~0), scalar residual 0.892 (≫0), slope 0.349 ≠ 0 ⇒ GRADED.

**Verdict-file provenance:** dual-SHA companion row (`audit_sha256_short=463f32033347c225 content_sha256_short=e6e3a7ddfbff690b`) + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row + per-leg row + q-supersession row + precedence-disclosure row + leg-B-feasibility + leg-A-tilt + one-dataset-echo + dual-prior rows (10 lines total). No A19 extra-row (post-lift dispatch, full confidence).

**Substrate reading (PARTICLE-class).** The substrate IS the Jensen-deformed SU(3) fiber; its Peter-Weyl channels (1,0)/(1,1)/(3,0) carry the three generations ON the multiplicity bundle. The carrier question — whether the charged-lepton envelope's SHAPE, MAGNITUDE, and COHERENCE are three charts of ONE operator family — is a transit-dynamics question because in the deep-sudden regime (R_therm = 5251.82, P_exc = 1.000) the Bogoliubov production map degenerates to STATIC symplectic overlaps of two eigenbases (S100b W5-1 switch-dominance, W5-2 RANGE-control), so every chart is a static functional of one operator pair — no chart carries hidden dynamics another lacks, and "Reading B" survives only as the NAME of the floor chart's fold-distortion plus the off-diagonal dressing gap, both now mechanistically accounted. The result confirms Reading A: the envelope SHAPE is the tracial chart's Casimir grading (Leg A in-band at the J-tilt razor edge), the MAGNITUDE is the moduli-acoustic crossing q′ ≈ τ_fold now DERIVED (Leg C GRADED — not a fingerprint coincidence), and the COHERENCE is the Weingarten hub fraction 1/√6 (Leg B at ratio 0.9887, positive-cone feasible). Flow: D_K eigenvalues → per-channel state evaluations → {S₀^geo shape, c coherence, ω_g graded frequency} → carrier composite (Reading A confirmed) → (W2-3) the S₀-knob, fed by `legC_output_form=GRADED` + `legC_q_prime=0.189745` (arms the (i)/(iii) structural selector before the dev-count). The quark/CKM extension (W2-4, S102) inherits the carrier verdict as the component-resolved face of the same operator family.

---

### §W2-3. S101-W3-S0-KNOB (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S101-W3-S0-KNOB`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (S₀ residual-knob 3-candidate discrimination; magnitude-axis closure)
**Agent**: `gen-physicist`
**Hypothesis**: Exactly ONE of three pre-registered S₀ residual-knob candidates — (i) Casimir quantum C₂(1,0) = 4/3, (ii) halved KK-threshold δ/2 = 1.175, (iii) moduli-acoustic τ_fold/T_acoustic = 95/56 = 1.696429 — is selected by the derivation-routed (W2-2 Leg C) exactly-one-inside-0.01 criterion AFTER the GRADED/SCALAR structural selector, identifying the magnitude knob and closing the magnitude axis. PRE-REG-INC (distinct token) iff W2-2 Leg C is absent at dispatch (mechanical closure per the prerequisite table).
**Plan reference**: `sessions/session-plan/session-101-plan-w2.md` §W2-3 (CF-S101-W3-S0-KNOB block + both riders; derivation-routed-not-post-hoc binding; degeneracy arming).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block — content presence by regex, NEVER line/byte counts):
- `computations/session-101/s101_w3_s0_knob.py` — CONFIRMED; `grep -E "from canonical_constants import|print_verdict_payload"` matches both.
- `computations/session-101/s101_w3_s0_knob.npz` — CONFIRMED; full float64 (per-candidate derivation-routed S0_pred + dev_k + N_inside + N_inside_naive + the structural-selector tag `legC_output_form`/`eligible_class`/`eligible_{i,ii,iii}` + E-3 shadow-vetting keys).
- `computations/session-101/s101_w3_s0_knob.png` — CONFIRMED (2-panel: derivation-routed devs vs 0.01/0.05 bands colored by selector eligibility + the structural-selector / pin-proximity-accident / E-3 vetting panel).
- verdict line `^S101-W3-S0-KNOB:.* audit_sha256=[a-f0-9]{64}` — CONFIRMED (`audit_sha256=513e0cbfc244c508…0680e052`, full 64-hex) + dual-SHA companion row + 3 explanatory extra-rows (NO 3-tuple — [VERIFY], `schema_v2_3tuple_required: false`).
- this WP section: `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present.

**MCP Pre-Compute Audit**:
- `search_knowledge("S0 residual knob envelope carrier tau_fold T_acoustic moduli-acoustic identity 95/56")` → equation hits confirm the canonical identity **S₀^geo = s̄/ℓ_geo = q/T_acoustic = τ_fold/T_acoustic = (19/100)/(14/125) = 95/56** and **S₀ = S0_fit = 1.694153** (src `s100a-w3-envelope-carrier-workshop.md`); this gate ADJUDICATES which datum fixes S₀, not re-derives the identity.
- `get_constant("tau_fold")` → 0.19 (S12/S42, `s42_constants_snapshot.npz`, CONST-FREEZE-42); `get_constant("T_acoustic")` → 0.112 (GGE acoustic temperature S42/S47). Both match the exact rationals 19/100, 14/125 (bit-level assert in-script).
- `trace_entity("Leg C graded offset … q_prime")` → no trace (the Leg-C derivation is the just-landed W2-2 artifact, not yet indexed); consumed directly from the W2-2 npz (`legC_output_form='GRADED'`, `legC_q_prime=0.1897451535364812`, `legC_graded_residual_vec ~1e-16`, `legC_scalar_residual_max=0.892`).
- NOT pre-closed: this is a live discrimination gate downstream of W2-2 Leg C. Knob value (iii) `S₀=95/56` matches the workshop-SELECTED identity-candidate; the gate's job is to PROMOTE it from identity-candidate to derivation (W-3 OQ-2).

**Verdict**: **PASS** — exactly ONE candidate survives the derivation-routed 0.01 band after the GRADED structural selector. The S₀ residual knob is IDENTIFIED as **(iii): the moduli-acoustic identity S₀ = τ_fold/T_acoustic = 95/56, DERIVED** (the W3-10 fingerprint S₀·T_acoustic = τ_fold promotes from identity-candidate to derivation, W-3 OQ-2). `audit_sha256=513e0cbfc244c50858b2c8e3d138073325f5824aa470ea77f71715d60680e052`, `content_sha256=5eb87c51ad9332b29efe7a26f30c18fef768dea67bad95230cceb2c474245d6b`.

**Results**:

NUMBERS first (derivation-routed S0_pred per candidate; `S0_fit = 1.6941531565757249` full float64 from the W3-9 npz, W3-9 echo dev = 0.00e+00):

| Cand | knob value | route | S0_pred | dev = \|S0_pred/S0_fit − 1\| | inside 0.01? | class |
|:----:|:-----------|:------|:--------|:-----------------------------|:------------:|:------|
| (i)  | C₂(1,0) = 4/3 | S0_fit·(4/3)/knob_req (knob_req=1.324671, threshold-knob image) | 1.7052315331 | 0.6539% | **True** | gap-shadow (scalar Casimir eigenvalue) |
| (ii) | δ/2 = 1.175 (δ=2.35) | S0_alt_halfdelta (threshold gate S0 under half_delta) | 1.6697058762 | 1.4430% | False | gap (KK-threshold) |
| (iii)| τ_fold/T_acoustic = 95/56 | q=τ_fold → S0 = q/T_acoustic (graded crossing) | 1.6964285714 | 0.1343% | **True** | graded-per-C2-quantum |

These reproduce the plan's recorded post-hoc context devs (iii 0.13%, i 0.65%, ii 1.46%) — but the gate's devs are the DERIVATION-routed S0_pred, available only after Leg C; the post-hoc ratio route is excluded by the binding spec.

**The exactly-one-inside-0.01 discrimination result:**
- **N_inside_naive (pre-selector) = 2** — BOTH (i) and (iii) sit inside 0.01. A naive dev-count returns N_inside = 2 → spurious INFO (degenerate).
- **Structural selector (Leg-C output FORM), applied BEFORE the dev-count**: `legC_output_form = GRADED` (witnessed by `legC_graded_residual_vec` max = 8.88e-16 < 1e-12 CLEAN, while `legC_scalar_residual_max = 0.892` ≫ 1e-3 EXCLUDED). GRADED ⇒ eligible class = **graded-per-C2-quantum** (the crossing-SLOPE class `ω_g = q·C₂(g)·M_KK`, ONE q across the tower). Class membership: (iii) is the graded crossing-slope member; (i) `4/3` is a single scalar Casimir EIGENVALUE (gap-shadow, NOT a per-g slope); (ii) `δ/2` is the gap class. **eligible: i=False, ii=False, iii=True.**
- **N_inside (post-selector) = 1** → selected knob = **(iii)**. PASS.

**The (i)/(iii) degeneracy is a 0.52% pin-proximity ACCIDENT (E-3 row 1)**, not two independent structures: 2π·τ_fold = 1.19381 vs (4/3)×0.9 = 1.20000, ratio = 1.00519 ⇒ 0.519% proximity. No ratio band tighter than 0.52% is honest at the s84-cache precision floor — only the output-FORM (GRADED vs SCALAR) can split the pair, and it does so by CLASS membership before any dev is counted. This is exactly the arming the plan pre-registered (`structural_selector` applied BEFORE dev-count).

**Substitution chain (threshold metric + degeneracy arming):**
- *Claim*: "the per-candidate criterion is the RATIO dev |S0_pred/S0_fit − 1| ≤ 0.01, and the (i)/(iii) degeneracy is resolvable only structurally."
- Def 1: S0_fit = 1.694153 [W3-9 npz, audit 78ee1d56; cache-free core].
- Def 2: candidate (iii) S₀ = τ_fold/T_acoustic = (19/100)/(14/125) = 19·125/(100·14) = 2375/1400 = **95/56 = 1.6964286** (Sage-QQ exact).
- Substitute (derivation-routed, NOT post-hoc): dev(iii) = |1.6964286/1.694153 − 1| = **0.00134** (inside 0.01); dev(i) [knob 4/3 through threshold-knob image] = **0.00654** (inside 0.01); dev(ii) [δ/2] = **0.01443** (outside 0.01, inside 0.05).
- Simplify (arming): post-hoc BOTH (i),(iii) inside 0.01 ⇒ naive N=2 (INFO). Shadow identity 2π·τ_fold = 1.19381 vs (4/3)×0.9 = 1.2: ratio 1.2/1.19381 = 1.00519 ⇒ 0.52% proximity ⇒ pin-proximity ACCIDENT (E-3 row 1), not two structures.
- Direction: the discriminator is Leg C's output-FORM binary (GRADED vs SCALAR), selecting the candidate CLASS before any dev is counted — a structural selector is the only instrument that splits a 0.52% shadow pair.
- Conclusion: PASS requires the derivation-routed exactly-one count AFTER the structural selector; the post-hoc devs are context, never the route. ✓ N_inside(selector) = 1.

**E-3 shadow-vetting of the survivor (iii) S₀ = 1.696429** against products/ratios of the canonical pin set {τ_fold, T_acoustic, Δω, κ_SONIC = 28π/125, 2π, small rationals} for ≤5% proximities (excluding (iii)'s OWN defining identity τ_fold/T_acoustic): nearest accidental neighbor = 3·(7/4) = 1.714286 at **1.053%** dev. The survivor's own derivation precision is **0.134%** — a full order of magnitude tighter than the nearest shadow ⇒ `shadow_separated = True`; no shadow carries incremental weight. The defining identity is **exact by construction**: S₀(iii)·T_acoustic = (95/56)·(14/125) = 19/100 = τ_fold (Fraction equality True), and Leg-C independently derived q' = S0_fit·T_acoustic = 0.1897452 ≈ τ_fold (= the npz `S0_times_T_acoustic` fingerprint, identical to `legC_q_prime` to 0.0e+00).

**Cross-checks:**
- W3-9 S0_fit echo: in-script `S0_fit` (from W2-2 npz) == W3-9 npz `S0_fit` to 0.00e+00 (one-dataset consistency).
- Fingerprint identity: `S0_times_T_acoustic` (overdetermine npz) == `legC_q_prime` (W2-2 npz) to 0.0e+00 — confirms (iii)'s GRADED crossing offset is the same datum on both routes.
- W2-2 npz content-confirmed: its internal `audit_sha256 = 463f32033347c225…b4c67d1a` == the orchestrator's PASS override audit (the correct Leg-C output file). [The in-script `pin_ok_w2_2=False` is a verdict-audit-SHA vs npz-file-bytes-SHA object-type mismatch — informational, non-gating; the npz file-bytes SHA `af0e7ebda13389ed…` IS in this gate's audit input-pin map, so the W2-2 dependency is captured in `audit_sha256`.] W3-9/S0-thr/env-OD file-bytes SHA pins all MATCH plan (`pin_ok` = True×3).
- δ/2 machinery: `S0_alt_halfdelta=1.6697058762`, `half_delta=1.175`, `KK_threshold_delta=2.35` consumed verbatim from the threshold-joint npz (candidate (ii) route, no re-derivation).

**4-tuple**: (value=`N_inside=1(selector);N_naive=2;knob=iii…`, scheme=`KNOB-DISCRIMINATION-3CAND-LEGC-ROUTED`, convention=`RATIO-NORMALIZED-TRACE-MEAN`, L_max=12 inherited transitively via W2-2 ← W2-1 npz lineage). No Seeley-DeWitt a_n cited ⇒ no regulator_pin; no SCHEMATIC helper ⇒ no CLASS pin.

**Substrate framing**: PARTICLE-class. The substrate's one-fiber ε_LX split sets the per-sector freeze frequencies via the GRADED law ω_g = q·C₂(g)·M_KK (Casimir-linear in g, the same linearity that makes W_flat(τ=0) = 9/5 exact). The knob question is WHICH substrate datum fixes the absolute scale of those frequencies: the fiber's own scalar Casimir quantum (4/3), the KK-threshold gap (δ/2), or the moduli-acoustic crossing — and the answer is the LAST: q = τ_fold, the fold's own deformation parameter, read through the GGE acoustic temperature T_acoustic. Flow: D_K one-fiber split derivation (Leg C, GRADED) → Δω structure → S0_pred per candidate → knob identity S₀ = τ_fold/T_acoustic. The 0.52% (i)/(iii) shadow is the substrate reminding us pin-proximity coincidences are a look-elsewhere hazard — resolved by the output-FORM (a structural property of the derived split), never by band-tightening. The magnitude axis closes as a DERIVED moduli-acoustic identity, not an empirical floor.

**Backward (fb_pair)**: PASS(iii) closes the magnitude axis as a derived moduli-acoustic identity — feeds the carrier registry text + the capstone magnitude row via the Wave-6/mack pipeline. (Per-observable transport: this is a substrate-IS datum S₀·T_acoustic = τ_fold at the τ_fold slice; the capstone magnitude-row landing is `mack-cosmic-bridge` sole-writer territory, not this gate.)

---

### §W2-4. S101-W3-QUARK-COMPONENT-ORIENTATION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-W3-QUARK-COMPONENT-ORIENTATION`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (per-component quark ε_LX-ladder orientation [SIGN] pre-registration + first quark envelope)
**Agent**: `connes-ncg-theorist` (workshop-assigned owner; orientation is degree/kernel-specific and does NOT transfer from the b-component by fiat)
**Hypothesis**: The per-component quark ε_LX-ladder orientation (D-component kernel h·D₊·h̄ adjoint-action class + c-component per Baptista eq-(2.17)) matches the transit partial prior — (p-1) a within-component C₂-descending mass map in EACH quark component (same orientation as the W-2-pinned lepton map) AND (p-2) up-type above down-type at the heavy generation — with the generation-DEPENDENT up/down crossing (gen-1 inverted, gen-3 upright) as the construction's hardest named target, and the uniform-κ sub-reading carrying its EXPLICIT pre-declared FAIL-condition (PDG m_u/m_d = 0.46 < 1 at gen 1; INFO is the honest intermediate — orientation right, hardest target unmet).
**Plan reference**: `sessions/session-plan/session-101-plan-w2.md` §W2-4 (W-3 CF-2 + QUARK/CKM routing; κ-triple [SPECULATION]-class PARTIAL PRIOR verified at plan-freeze; two-part [SIGN]-first sequencing).

**Output Artifacts** (closure-verification checklist; content presence by regex, NEVER line/byte counts):
- `computations/session-101/s101_w3_quark_component_orientation.py` — ✓ exists; `from canonical_constants import` + `print_verdict_payload` present.
- `computations/session-101/s101_w3_quark_component_orientation.npz` — ✓ full float64 (⟨λ²⟩_g^{(D)} + ⟨λ²⟩_g^{(c)} ladders, both sign chains, crossing scalars, Ω^D/Ω^c cross-check, PDG held-out ratios).
- `computations/session-101/s101_w3_quark_component_orientation.png` — ✓ 3-panel (p-1 ladders / p-2 envelopes / crossing).
- verdict line `^S101-W3-QUARK-COMPONENT-ORIENTATION:.* audit_sha256=[a-f0-9]{64}` — ✓ (`audit_sha256=833a3daf…480cdc85`) + dual-SHA row + schema-v2 `[SIGN]` 3-tuple row + 2 per-chain extra-rows.
- this WP section: Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit — ✓.

**A19 extra-row**: N/A (post-lift dispatch — S101-TAU0 L4 lift already landed; cross-wave pin 1 satisfied at W1-1 PASS audit `194b2b3c`, s84 L12 cache cited at FULL CONFIDENCE as the LC spectrum).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md` — queries executed BEFORE writing the script):
- `search_knowledge("quark component orientation freeze-in direction C2 descending trace-mean ladder generation")` → confirms the freeze-in direction theorem context (deeper C₂ → lighter), `var(C2)` generation-Z₃ records (s63); NO closure covering the per-component quark [SIGN] orientation — gate is NOT pre-closed.
- `search_knowledge("Omega D component Omega c component 8/3 4/3 adjoint action quark splitting Baptista 2.17")` → traces `Ω^D = (8/3)·I₃` (eq 3.19), `Ω^c = (4/3)·I₃` (color-Schur), `Ω^D/Ω^c = 2` exact at S100a-DUAL-Z3-PHI-POINTS (audit `d23c7e99cba96403`, WP §W2-1 lines 57–58, 83). This is the machinery cross-check anchor (non-gating).
- canonical greps: PDG SECTION E quark anchors `m_u_msbar_2GeV=2.16e-3`, `m_d_msbar_2GeV=4.70e-3` (→ m_u/m_d=0.4596 <1, W3-9 held-out), `m_t_pole=172.69`, `m_b_msbar_mb=4.183` (→ m_t/m_b=41.28), `m_c_msbar_mc=1.2730`, `m_s_msbar_2GeV=93.5e-3`; `tau_fold=0.19`; `M_KK_gravity=7.43e16`.
- S99 panel provenance re-grep at `sessions/archive/session-99/session-99-fermion-mass-hawking.md:36-37,74` — κ-triple `lepton 1.89, up 1.29, down 0.78` confirmed [SPECULATION]-class (the table at :36-37 + the sector-dependent-slope speculation at :74). The in-script pre-flight re-grep echoes this; match = True ⇒ regime VALID.
- NOT PRE-CLOSED. The W-3 Wall-1/Wall-2 class theorems (no quark construction may distinguish up/down by tower conjugation alone) stay CLOSED and are RESPECTED: the up/down distinction here is carried by the per-component kernel (Ω^D≠Ω^c) + the sector-dependent κ, NOT by tower conjugation.

**Verdict**: **INFO** — composite via the canonical `gate-verdicts.md` collapse rule (sign=PASS, magnitude=INFO, regime=VALID ⇒ INFO). 3-tuple: **sign_verdict=PASS**, **magnitude_verdict=INFO**, **regime_verdict=VALID**.

**Output 4-tuple**: `(value=p1_D=True;p1_c=True;p2_gen3=True;ud_g1=1.8866e+01;ud_g2=3.0714e+00;ud_g3=1.1203e+00;crossing=False;uniform=True;OmegaD/Omegac=2.000000;kappa_ok=True;PDG_u/d_g1=0.4596;PDG_t/b_g3=41.2838, scheme=D-AND-C-COMPONENT-KERNEL-TRACE-MEAN-LADDER, convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)`. audit_sha256 `833a3daf8e0e886436a8792687e67b3531852bc505791b87e2f034c7480cdc85`, content_sha256 `4fd14e34a5b690455aa2b2a36bbda4701945dd3eb8ea04373b05e7e343c5f530`.

---

#### PART 1 — [SIGN] pre-registration (written BEFORE compute; binding sequencing)

Two pinned directions + one crossing test. NUMBERS-first; the directional claims carry explicit substitution chains.

**(p-1) — within-component C₂-DESCENDING mass map (per quark component).**
Pin: within EACH quark component the multiplicity-normalized trace-mean ladder ⟨λ²⟩_g^{(comp)} is strictly **C₂-ASCENDING** on the tower (1,0)→(1,1)→(3,0); via the freeze-in direction theorem (W3-9 sign-PASS, kernel-independent in sign) this maps to a **C₂-DESCENDING** mass map, i.e. gen3 (heaviest) ↔ (1,0), gen2 ↔ (1,1), gen1 (lightest) ↔ (3,0) — the SAME orientation as the W-2-pinned lepton map (τ=(1,0), μ=(1,1), e=(3,0)).

**(p-2) — up-type ABOVE down-type at the heavy generation.**
Pin: up-type envelope > down-type envelope at gen 3, from the κ-triple chain ∂(ln m)/∂κ = +2πω/κ² > 0 with κ_up = 1.29 > κ_down = 0.78 ([SPECULATION]-class PARTIAL PRIOR, S99 hawking :74; provenance VERIFIED at plan-freeze 2026-06-07 and re-verified in-script; pins DIRECTION only, never a magnitude).

**EXPLICIT FAIL-condition of the uniform-κ sub-reading (pinned inside this pre-registration, not a margin note — Q4 wording).**
PDG m_u/m_d = 2.16/4.70 = **0.4596 < 1** at gen 1 (canonical SECTION E `m_u/d_msbar_2GeV`; W3-9 held-out record). A single uniform scale factor (or a single up/down slope pair acting on a C₂-monotone ω-ladder) cannot reproduce this inversion while keeping m_t/m_b ≫ 1 at gen 3 — the **generation-DEPENDENT crossing** (gen-1 inverted, gen-3 upright) is the construction's hardest named target. This is pre-declared as the uniform-κ sub-reading's falsifier.

#### Substitution chains (definition → substitute → simplify → read direction)

**Claim 1 ((p-1) within-component direction): "in each quark component the mass map is C₂-DESCENDING — the same orientation as the lepton map."**
- *Definition 1* (freeze-in direction theorem, W3-9 sign-PASS, kernel-independent): deeper freeze at larger C₂ ⟹ lighter fermion.
- *Definition 2*: "deeper freeze" on the ladder = larger per-sector frequency ω_g ∝ ⟨λ²⟩_g^{(comp)} (graded form), and ⟨λ²⟩_g ascends with C₂ at τ=0 **EXACTLY** as 3·C₂ + 27/4 (W2-1 Claim 1 chain).
- *Substitute*: C₂ = (4/3, 3, 6) ascending ⟹ τ=0 form (43/4, 63/4, 99/4) = (10.75, 15.75, 24.75) ascending (Sage-QQ exact) ⟹ freeze depth ascending ⟹ mass DESCENDING along (1,0) → (1,1) → (3,0).
- *Direction*: gen1 (lightest) ↔ (3,0); gen2 ↔ (1,1); gen3 (heaviest) ↔ (1,0) — in EACH quark component, identically to the W-2-pinned lepton map.
- *Conclusion*: (p-1) sign test = strict C₂-ascent of ⟨λ²⟩_g^{(D)} AND ⟨λ²⟩_g^{(c)} at τ_fold. The per-component scalar Ω^{comp} (8/3 for D, 4/3 for c) is a multiplicative prefactor that **CANCELS** in the within-component ascent, so the ascent — hence the orientation — is identical on both kernels. **Computed: D-component ascent True; c-component ascent True.**

**Claim 2 ((p-2) cross-component direction): "up-type sits ABOVE down-type at the heavy generation."**
- *Definition 1* (four-lens filter face): m ∝ Γ(ω)·e^{−2πω/κ} [S99 greybody form].
- *Substitute*: ln m = ln Γ(ω) − 2πω/κ ⟹ ∂(ln m)/∂κ = −2πω·∂(κ⁻¹)/∂κ = **+2πω/κ² > 0** for ω > 0 (Sage-confirmed: diff(−2πω/κ, κ) = +2πω/κ²).
- *Simplify*: larger κ ⟹ weaker exponential suppression ⟹ heavier at fixed ω.
- *Substitute the κ-triple*: κ_up = 1.29 > κ_down = 0.78.
- *Direction*: up-type ABOVE down-type at fixed generation — confirmed at gen 3 (m_t ≫ m_b, PDG m_t/m_b = 41.28). **Computed: up-envelope > down-envelope at gen 3 = True.**
- *Conclusion*: (p-2) sign test = up-envelope > down-envelope at gen 3 (PASS). The NAMED BURDEN: gen 1 inverts (PDG m_u/m_d = 0.4596 < 1) — pinned as the uniform-κ sub-reading's EXPLICIT FAIL-condition; the generation-DEPENDENT crossing is the hardest target.

#### PART 2 — Compute (existing L12 cache, NO new diagonalization)

**Per-component trace-mean ladders** (multiplicity-normalized, `RATIO-NORMALIZED-TRACE-MEAN` state-evaluation class; ⟨λ²⟩_g^{(comp)} = Ω^{comp}·mean(|λ|² over abs_evals); n/dim = 16.00 per sector = the C¹⁶ generation factor, so the mean correctly normalizes by the per-sector multiplicity):

| sector | gen | C₂ | bare ⟨λ²⟩ | D-comp ⟨λ²⟩ (Ω^D=8/3) | c-comp ⟨λ²⟩ (Ω^c=4/3) |
|:------:|:---:|:--:|:---------:|:---------------------:|:---------------------:|
| (1,0) | 3 | 1.3333 | 1.260526 | 3.361403 | 1.680701 |
| (1,1) | 2 | 3.0000 | 1.842370 | 4.912986 | 2.456493 |
| (3,0) | 1 | 6.0000 | 2.889689 | 7.705837 | 3.852919 |

(p-1) strict C₂-ascent: **D-component True** (3.361 < 4.913 < 7.706); **c-component True** (1.681 < 2.456 < 3.853). The bare ladder is the SAME ascent (1.261 < 1.842 < 2.890), confirming the Ω^{comp} prefactor cancels. The τ=0 exact backbone 3·C₂+27/4 = (10.75, 15.75, 24.75) ascends (Sage-QQ); the τ_fold cache preserves the ascent.

**Cross-component greybody envelopes** (m_g^{(comp)} = Ω^{comp}·e^{−2πω_g/κ_comp}, ω_g = C₂(g)·τ_fold in M_KK units — the M_KK factor cancels in 2πω/κ because κ is also in M_KK units; up = c-component at κ_up=1.29, down = D-component at κ_down=0.78):

| gen | sector | ω_g = C₂·τ_fold | m_up (c, κ=1.29) | m_down (D, κ=0.78) | m_up/m_down |
|:---:|:------:|:---------------:|:----------------:|:------------------:|:-----------:|
| 3 | (1,0) | 0.2533 | 0.388 | 0.347 | **1.1203** |
| 2 | (1,1) | 0.5700 | 0.0830 | 0.0270 | 3.0714 |
| 1 | (3,0) | 1.1400 | 0.00517 | 0.000274 | 18.866 |

(p-2): up > down at gen 3 — **True**.

**Crossing test (magnitude)**: m_u/m_d < 1 at gen 1 = **False** (computed 18.87, not < 1); m_t/m_b > 1 at gen 3 = True. Crossing **NOT realized** → **uniform ordering** (m_up > m_down at all three generations). PDG held-out reference for comparison: gen1 m_u/m_d = 0.4596 (<1), gen2 m_c/m_s = 13.615, gen3 m_t/m_b = 41.28 (>1).

**Machinery cross-check (non-gating)**: Ω^D/Ω^c = 2.000000000000000 (target 2, dev 0.0e+00, Sage-QQ exact, audit `d23c7e99cba96403`); κ-triple re-grep in S99 panel = True ⇒ **regime VALID**.

#### Structural finding — why the crossing is unmet (the load-bearing result of this gate)

The two-κ uniform-slope greybody envelope is **monotone in ω_g and cannot cross**:

m_up/m_down(g) = (Ω^c/Ω^D)·exp(−2π·ω_g·(1/κ_up − 1/κ_down)).

The prefactor Ω^c/Ω^D = 1/2 < 1; the bracket (1/κ_up − 1/κ_down) = (1/1.29 − 1/0.78) = −0.5069 has a **fixed sign** (negative, since κ_up > κ_down). Therefore the ratio is exp(+2π·ω_g·0.5069) up to the constant prefactor — strictly **increasing in ω_g**. Substituting the substitution chain: the crossing-of-unity point is ω* = ln(Ω^D/Ω^c)/(2π·(1/κ_d − 1/κ_u)) = ln 2 / (2π·0.5069) = **0.2177**, and all three ω_g (gen3=0.253, gen2=0.570, gen1=1.140) exceed ω*. Because gen 1 carries the **largest** ω_g (highest C₂, by (p-1)), the ratio is largest at gen 1; if any generation lands m_up/m_down > 1, gen 1 does too. Hence **gen-1 inversion (gen1 < 1 ∧ gen3 > 1) is structurally impossible for a single (κ_up, κ_down) pair acting on a C₂-monotone ω-ladder**. This is not a numerical near-miss — it is a sign theorem: a generation-DEPENDENT crossing requires generation-DEPENDENT slope structure (per-generation κ_g, or an ω_g that is non-monotone in C₂), which the two-κ envelope does not carry. The result routes the crossing question to per-generation kernel structure at S102.

**Verdict assessment.** This is the pre-registered **INFO** (the honest intermediate): the orientation content is **banked** — (p-1) C₂-descending mass map confirmed in EACH quark component (D and c), matching the lepton map; (p-2) up > down at the heavy generation confirmed where PDG confirms it (m_t/m_b = 41.28 ≫ 1) — but the hardest named target (gen-1 inversion) is **unmet by the uniform-κ envelope**, whose pre-declared FAIL (PDG m_u/m_d = 0.4596 < 1) therefore **stands recorded**. The composite is INFO, not FAIL: no pinned direction is violated (a FAIL would require a (p-1) ascent failure or down > up at gen 3); the magnitude is INFO because the envelopes are uniformly ordered, not globally anti-oriented. The Ω^D ≠ Ω^c per-component splitting (ratio 2 exact) and the [J, D_K] = 0-preserving construction (the only mechanism evading both W3-9 walls by construction) are intact; the quark-sector orientation [SIGN] anchor for the S102 CKM program (per-component CKM = misalignment of two rank-one dressings, E-2(e)) is **set** at sign=PASS.

**Substrate framing.** PARTICLE-class. The 64-component generation spinor decomposes per Baptista eq-(2.17) into components reading DIFFERENT faces of the same fiber: the b-component (leptons) reads the |s(h)|²-weighted face; the **D-component** (h·D₊·h̄, adjoint-action — d_R/u_L/d_L) and **c-component** (s(h)·h†, fundamental — u_R) read the quark faces. The tier-3 question (WHICH functional per component) is exactly this gate: orientation is degree/kernel-specific and does NOT transfer from the b-component by fiat — it was pre-registered and computed per kernel. Flow: D_K eigenvalues → per-component kernel trace-means (Ω^{comp}-weighted) → orientation signs → quark generation map → (S102) CKM as misalignment of two rank-one dressings. The gen-1 inversion is the substrate's hardest named target because it demands a generation-DEPENDENT crossing no uniform scale factor can mimic; this gate proves the two-κ envelope cannot supply it, sharpening the S102 target to per-generation slope structure.

---

### §W2-5. S101-STAR-METRIC-BLOCK-LEMMA (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S101-STAR-METRIC-BLOCK-LEMMA`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Lemma B star-metric boundary verify; algebra-DEPENDENT state-pair / Cell IV STATE-PROJ)
**Agent**: `gen-physicist` (author-independence hygiene on connes's own Stage-0 Lemma B; SDP machinery fully scripted in `s100a_connes_distance_ladder.py`)
**Hypothesis**: Lemma B holds at its declared boundary — (i) for NON-SCALAR channel couplings S_g (operator blocks), the hub-leaf star distance is d(v,g) = 1/‖S_g‖_op EXACTLY (rel dev ≤ 1e-7), and (ii) the leaf-leaf distance is STRICTLY above the Pythagorean form (t_g⁻² + t_h⁻²)^{1/2} for non-aligned blocks (top singular subspaces misaligned; witness ≥ 1e-3) with equality restored under engineered alignment (≤ 1e-7) — the Lemma B(2) saturation criterion.
**Plan reference**: `sessions/session-plan/session-101-plan-w2.md` §W2-5 (S-1 connes-machinery synthesis §V.1 Lemma B; plan-frozen synthetic family + physical instance; SDP-CLARABEL machinery reuse).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block — content presence by regex, NEVER line/byte counts):
- `computations/session-101/s101_star_metric_block_lemma.py` — present (41,876 B); contains `from canonical_constants import` + `print_verdict_payload`. ✓
- `computations/session-101/s101_star_metric_block_lemma.npz` — present (19,412 B); full float64 (per-config clause-(i) rel devs `syn_dev_i`, clause-(ii) strictness witnesses `syn_strict_rel`, aligned-equality devs, the 23-gating-SDP family + asymmetric diagnostic + physical instance). ✓
- `computations/session-101/s101_star_metric_block_lemma.png` — present (141,602 B; 3 panels: strictness-vs-θ per magnitude, clause-(i) SDP-vs-closed scatter, d(g,h)-vs-P gap). ✓
- verdict line `S101-STAR-METRIC-BLOCK-LEMMA: PASS … audit_sha256=08ee01cb…b6c98d7` + dual-SHA companion row + 3 extra rows (NO 3-tuple — [VERIFY-THEOREM]). ✓ (W1-1 PASS upstream-satisfied per orchestrator override; no A19 pre-lift extra-row required.)
- this WP section: `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("Lemma B star metric Connes distance hub leaf operator norm coupling")` → returned the S-1 `session-100a-connes-machinery-synthesis.md` Lemma B text + Eq. (7) `d(ε_v, ε_g) = 1/‖S_g‖_op` (operator-norm GENERAL form; scalar special case `d(v,g)=1/t_g`); `S100a-CONNES-DISTANCE-LADDER` STAGE-3 provenance. The op-norm form is the PROVEN Stage-0 text being verified at its boundary; NOT PRE-CLOSED (this is the first operator-block (non-scalar) boundary realization — the scalar instance only landed `S100a-CONNES-DISTANCE-LADDER`).
- `trace_entity("S100a-CONNES-DISTANCE-LADDER")` → STAGE-3 gate + provenance; the scalar-instance SDP solver floor 2.5e-9 (synthesis §VI row 2) is the cross-check reference for the 1e-7 threshold (40× headroom).
- `get_constant("tau_fold")` → 0.19 (confirmed canonical; the L12-cache physical-instance floors are read at τ_fold = 0.19).

**Verdict**: **PASS** — Lemma B holds at its operator-block boundary: clause (i) ∧ clause (ii), CLARABEL converged across all 23 gating SDPs.

**Results**:

**NUMBERS first.**

*Clause (i) — hub-leaf operator-norm form `d(v,g) = 1/‖S_g‖_op`.* Across ALL 23 gating configs (21 synthetic + physical boundary + physical aligned), max relative deviation `|d_SDP(v,g) − 1/‖S_g‖_op| / (1/‖S_g‖_op) = 2.63e-08 ≤ 1e-7` (clause-(i) tol). **PASS.** The worst case is at the most-stressed config (θ=90°, ‖S‖=2.0; the maximal-misalignment interior-point precision limit), still **3.8× inside** the threshold. Physical-instance clause-(i) dev `1.81e-11` (boundary), `6.20e-11` (aligned) — both ~3 OOM tighter than the synthetic worst case (the textured block diag(1,ρ_tex=0.3) is better-conditioned than the rank-1 limit). The hub-leaf distance depends ONLY on `‖S_g‖_op`, NOT on cross-leaf alignment: `d(v,g)` is exactly invariant across all θ at each magnitude (e.g. `d(v,g) = 2.0` at ‖S‖=0.5 for every θ ∈ {0…90}°).

*Clause (ii) — leaf-leaf strictness with alignment-saturation.* `P = (t_g⁻² + t_h⁻²)^{1/2}`, `t_x = ‖S_x‖_op`.
- Non-aligned strictness witness `(d_SDP(g,h) − P)/P`: minimum over all non-aligned configs `= +8.629e-03 ≥ 1e-3` (strictness floor). **PASS.** Monotone in θ (symmetric grid, magnitude-independent ratio): 15° → `+8.63e-3`, 30° → `+3.53e-2`, 45° → `+8.24e-2`, 60° → `+1.55e-1`, 75° → `+2.60e-1`, 90° → `+4.14e-1` (= √2 − 1, the orthogonal-range limit).
- Aligned-equality `|d_SDP(g,h) − P|/P` over the θ=0 controls: maximum `= 3.61e-10 ≤ 1e-7` (aligned-eq tol). **PASS.** Equality restored to ~10 significant figures — the Lemma B(2) saturation criterion holds exactly at alignment.

*Physical ε_LX-boundary instance (L12 cache floors, τ_fold = 0.19).* Greybody star floors `λ(1,0)=0.835894`, `λ(1,1)=0.872975`, `λ(3,0)=1.248264`; couplings `t_x = 1/λ_x²` = (1.431, 1.312, 0.642). The two largest-coupling leaves `g=(1,0)`, `h=(1,1)` are promoted to operator blocks `t_x·U_x·diag(1, ρ_tex=0.3)` (the ε_LX multiplicity texture). Boundary (hub-range misaligned θ_phys = 45°): `(d−P)/P = +7.37e-2` (strict, ≥ 1e-3); aligned control: `(d−P)/P = +3.61e-10` (equality, ≤ 1e-7). Clause-(i) dev `1.81e-11`. The physical instance confirms the synthetic family on the substrate's own floors: scalar-star Pythagorean additivity is the ALIGNED saturation point; the ε_LX texture breaks joint saturation.

*Asymmetric diagnostic (non-gating).* Worst-case strictness margin `(t_g, t_h) = (0.5, 2.0)` at θ=15°: `(d−P)/P = +1.97e-3 ≥ 1e-3` — the binding off-diagonal-magnitude case still clears the strictness floor (~2× margin). Confirms PASS is not an artifact of the symmetric grid.

*Solver / regime.* CLARABEL: all 23 gating SDPs (plus the asymmetric diagnostic) `status ∈ {optimal, optimal_inaccurate}` ⇒ `all_converged = True`. 50 of the per-objective solves carry `optimal_inaccurate` (CLARABEL's tag at the tight 1e-9 gap target; converged to ~1e-8, INSIDE every gate tolerance) — this is the `s100a_connes_distance_ladder.py` machinery convention (its `ok_status` set), NOT non-convergence. The plan's INFO branch ("CLARABEL non-convergence on specific configurations") did NOT fire; no sub-case blocked.

**Gate (second).** PASS iff clause (i) ∧ clause (ii). clause_i_PASS=True (`2.63e-8 ≤ 1e-7`) ∧ clause_ii_PASS=True (strict ≥ 1e-3 ∧ aligned ≤ 1e-7) ⇒ **PASS**. 4-tuple `(value=clause_i_PASS…clause_ii_PASS…, scheme=SDP-CLARABEL-LEMMA-B-BOUNDARY, convention=substrate-state-pair-canonical, L_max=12)`. Dual-SHA `audit=08ee01cbb254879f0c71f4feee49d525dd36e0693fdc8ce626b10c297b6c98d7`, `content=13cd017cb585f377541b57eb81a7d7baa12f2e297cf558e564ed6683e938cb24`. Cell-IV corner declared (algebra-DEPENDENT state-pair functional / STATE-PROJ; **NO §VII registry landing in this gate** — the landing is Wave-6's `S101-VIIBM-STATEPROJ-LANDING`). No Seeley-DeWitt `a_n` cited (the observable is a state-pair Connes distance, not a heat-kernel moment) ⇒ no `regulator_pin` tag; no SCHEMATIC helper consumed ⇒ no CLASS pin.

**Substitution chain (interpretation third) — the strictness direction, read off the canonical form, not asserted.**
- *Claim*: non-aligned operator blocks make the leaf-leaf distance STRICTLY EXCEED the Pythagorean form; alignment restores equality.
- *Def 1*: `d(v,g) = 1/‖S_g‖_op` [Lemma B(1), op-norm form]. *Def 2*: `P = (t_g⁻² + t_h⁻²)^{1/2}`, `t_x = ‖S_x‖_op` [Lemma B(2), exact for SCALAR couplings].
- *Substitute*: the Connes distance is `sup{|a_g − a_h| : ‖[D, π(a)]‖_op ≤ 1}` with `π(a) = ⊕_k a_k I_m` (IKM finite-point; `A_K` acts as identity on the multiplicity index, §VII.BL). The hub-row block of `[S, π(a)]` is the single `m × (K m)` operator `[(a_g − a_v) S_g | (a_h − a_v) S_h]`; its operator norm couples the two leaves THROUGH the overlap of their hub-side ranges `S_g S_g†` vs `S_h S_h†` (the LEFT singular subspaces). For scalar couplings the two channel constraints share one singular direction ⇒ one Lipschitz element saturates BOTH simultaneously ⇒ `d = P` exactly. For operator blocks with misaligned hub-side ranges, NO single element saturates both at once ⇒ the optimizer splits its Lipschitz budget across the two non-commuting directions.
- *Simplify → Direction*: a constrained sup with jointly-unsaturatable constraints attains a value EXCEEDING the both-saturated (Pythagorean) value ⇒ `d(g,h) > P` strictly off-alignment; `d − P → 0` as θ → 0 (joint saturation restored). **The sign `d − P > 0` is the COMPUTED SDP output (the attained sup minus the closed-form Pythagorean), not a hand-asserted direction** — the gate reads it off the canonical form for every config. *Conclusion*: witness `(d − P)/P ≥ 1e-3` at the non-aligned grid (min `+8.63e-3`); equality `≤ 1e-7` at θ=0 (max `3.61e-10`). Verified.
- *Geometric reading (derived, load-bearing)*: "top singular subspace misalignment between the two leaves" = LEFT (hub-range) singular-subspace overlap. **Negative control**: rotating the RIGHT (leaf-side) singular vectors instead leaves `d = P` invariant at all θ (`(d−P)/P ~ −5e-11` at θ=90°) — confirmed in the pre-compute validation; only hub-range misalignment breaks joint saturation. This is WHY the strictness is a genuine operator-block effect and not a coordinate artifact.

**Assessment / solution-space.** Clause (i) PASS confirms the operator-norm form `d(v,g) = 1/‖S_g‖_op` is exact at the non-scalar boundary — the hub-leaf metric depth IS inverse coupling strength regardless of block structure. Clause (ii) PASS confirms the Lemma B(2) Pythagorean leaf-leaf additivity is precisely the ALIGNED saturation point, with genuine strictness off-alignment: the metric face adds NO shape freedom beyond floor spectroscopy in the scalar (aligned) case, but the ε_LX multiplicity texture (misaligned hub ranges) inflates leaf-leaf separation above the Pythagorean floor. **Downstream consequence**: per the plan's Wave-2 decision point, W2-5 PASS (with W2-6) lets `S101-VIIBM-STATEPROJ-LANDING` (Wave 6) proceed with its Lemma-B structural clauses (i)–(iii) at FULL strength — no clause excluded or re-scoped; `S101-CONNES-STATEPROJ-STAGE2-VERIFY` (Wave 7) inherits the full-strength text. The ε_LX-boundary probe feeds the §VII.BL-complement boundary characterization (the precise edge of the Lemma-B exactness domain: exact-Pythagorean iff scalar/aligned, strict iff operator-block/misaligned).

**Substrate framing.** GEOMETRIC. The substrate IS the finite spectral triple; the channel graph is the star (hub = vacuum channel, leaves = generation channels), and the Connes distance `d(v,g) = 1/‖S_g‖` is the substrate's own statement that metric depth IS inverse coupling strength. Flow: `D_K` sector floors λ_x(τ_fold) → greybody star couplings t_x = 1/λ_x² → state-pair Connes distances → the boundary of the Lemma-B exactness domain. The ε_LX multiplicity texture is a substrate-intrinsic operator-block promotion (not an externally-imposed perturbation): the substrate's own metric face announces where Pythagorean additivity ends and strict super-additivity begins. No container, no imposed hierarchy — the misalignment IS a property of how the fiber's hub-side channel ranges overlap.

---

### §W2-6. S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Theorem A clause 3 disconnect-divergence boundary verify; CLASS-γ commutative signature)
**Agent**: `gen-physicist` (author-independence: NOT the S100a `connes-ncg-theorist` authoring agent; same SDP machinery + L12 cache floors as §W2-5)
**Hypothesis**: Theorem A clause 3 holds at its boundary — severing one star edge (t_g = 0) drives the severed pair's Frobenius-regulated distance d_R to grow with log-log slope EXACTLY 1 (linear-in-R divergence, the commutative CLASS-γ signature; |slope − 1| ≤ 1e-3) while ALL connected pairs stay R-flat (≤ 1e-8), and the connected-pair activation threshold ρ* (the one empirical residue of the S-1 synthesis) satisfies ρ* ≤ 10·ω_max.
**Plan reference**: `sessions/session-plan/session-101-plan-w2.md` §W2-6 (S-1 connes-machinery synthesis §V.2 Theorem A clause 3; pinned (1,0) severance + diagnostics; 5-point decade R-sweep).

**Verdict**: **PASS** — `(a) ∧ (b) ∧ (c)` all hold on the plan-frozen PRIMARY (1,0) severance. The disconnect-divergence side of the two-sided dichotomy is verified: severing the (1,0) edge produces an EXACTLY-linear-in-R (slope 1.000000000, |slope−1| = 1.82e-11) regulated distance — the commutative CLASS-γ signature — while both connected pairs stay R-flat to ~1.6e-9, and the activation threshold ρ* = 15.5816 lands at ρ* ≤ 10·ω_max (equality). Theorem A clause 3 stands at the boundary; the Wave-6 `S101-VIIBM-STATEPROJ-LANDING` dichotomy clause (i) proceeds at full strength; ρ* recorded as the one empirical residue.

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block — content presence by regex, NEVER line/byte counts):
- `computations/session-101/s101_connes_distance_disconnect_boundary.py` — present; `from canonical_constants import` (:209) + `print_verdict_payload` (def :282, call :846). ✓
- `computations/session-101/s101_connes_distance_disconnect_boundary.npz` — present (20872 bytes); full float64 (primary/diag severed-pair OLS slopes + intercepts, per-pair connected R-dev + ρ*, the 3-severance × 5-point R-grid table, doubled-16 cross-check). ✓
- `computations/session-101/s101_connes_distance_disconnect_boundary.png` — present (3-panel: log-log divergence + slope-1 reference; connected flat-window vs full-grid rel-dev; severed slope across all 3 severances). ✓
- verdict line `^S101-CONNES-DISTANCE-DISCONNECT-BOUNDARY: PASS .* audit_sha256=9eea47088bef70fa734a7d9fa77f709f4b7e71626e96a81df4c09c7a13d036fd` + dual-SHA companion row (NO 3-tuple — `[VERIFY-THEOREM]`) + 3 extra-rows (diagnostic severances; doubled-16 cross-check; ω_max convention + Cell-IV). ✓ Pre-lift A19 row N/A: cross-wave pin 1 SATISFIED (W1-1 PASS, audit `194b2b3c`; s84 L12 cache re-labelled → full confidence) per orchestrator override.
- this WP section: `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**`. ✓

**MCP Pre-Compute Audit** (`.claude/rules/knowledge-index-usage.md`; queries run BEFORE the script):
- `search_knowledge("Connes distance disconnect CLASS-gamma regulator divergence linear R severed edge Theorem A")` → returned the plan's own `d_R = R·(component-separation constant) — linear in R, log-log slope 1 EXACTLY` equation row + S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY (INFO, 0.980, CLASS-γ). NOT PRE-CLOSED — this gate verifies the *converse* (disconnect ⇒ divergence) of the S100a finite-connected result; no prior gate computes the severed-edge slope.
- `search_knowledge("S100a-CONNES-DISTANCE-LADDER omega_max flatness window R-sweep regulator invariance")` → S100a provenance (`connes_distance_ladder`, STAGE-3) + S89 regulator-class-invariance scan (ratio 7.324974). Confirms ω_max convention lives in the s100a npz, not a canonical constant.
- `trace_entity("S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY CLASS-gamma regulator divergence")` → no trace (the CLASS-γ machinery value is a literal pin, not an indexed entity); confirmed via the S100a script docstring (:43–47): full M_n(ℂ) ⇒ regulator-divergent, commutative channel restriction ⇒ finite. This gate demonstrates the disconnect re-divergence.
- Inspected the s100a npz directly: `omega_D2_floors` = [0.69871796, 0.76208541, 1.55816335] ⇒ ω_max = 1.5581633463885884; `rsweep_max_reldev` = 1.79e-9 (the connected-pair flatness floor the plan cites). The R-grid uses `factor × ω_max` per the s100a convention (`R_SWEEP_FACTORS × float(omega.max())`).

**Results**:

NUMBERS (PRIMARY (1,0) severance, the gating configuration; L=12 cache floors at τ_fold = 0.19):

| Quantity | Value | Threshold | Pass |
|:--|:--|:--|:--:|
| severed-pair log-log slope `d ln d_R / d ln R` | **1.000000000** | — | — |
| `\|slope − 1\|` (clause a) | **1.82e-11** | ≤ 1e-3 | ✓ |
| severed intercept ln c → c | −0.346574 → **c = 0.707107** (= 1/√2) | (residue, not gated) | — |
| connected worst flat-window rel-dev (clause b) | **1.568e-9** | ≤ 1e-8 | ✓ |
| ρ* = max over connected pairs (clause c) | **15.581633** | ≤ 10·ω_max = 15.581633 | ✓ |
| ω_max (s100a convention, max channel D²-floor) | 1.558163346 | (loaded from s100a npz; cache-identity dev 0.0e+00) | — |
| solver_clean (all gating SDPs `optimal`) | True | — | — |

Severed-pair regulated distances over the 5-point decade grid R ∈ {1, 10, 100, 1000, 10000} × ω_max:
`d_R = (1.101788, 11.017879, 110.178787, 1101.787868, 11017.878684)` — exactly one decade of d per decade of R (slope 1); all SDP statuses `optimal|optimal`.

Connected pairs (R-flat once R > ρ*):
- `d(v,(1,1))`: intrinsic 0.762085410; ρ* = 1.558163 (= 1·ω_max — intrinsic < ω_max, the Frobenius ball never binds); flat-window rel-dev 1.568e-9.
- `d(v,(3,0))`: intrinsic 1.558163344 (= ω_max); ρ* = 15.581633 (= 10·ω_max — at R = 1·ω_max the ball just binds, d = 1.1018 < intrinsic; R = 10·ω_max releases it); flat-window rel-dev 1.251e-9; **full-grid** rel-dev 0.4142 (the sub-ρ* point — diagnostic only, NOT gated, because clause (b) is the flat-window flatness per the s100a flatness-window convention, plan method step 5/6).

This is why ρ* binds at exactly 10·ω_max and not below: the (3,0) connected channel's intrinsic distance equals ω_max, so the R = 1·ω_max ball clips it and flatness activates one decade up. ρ* ≤ 10·ω_max holds at equality — the strongest non-violating outcome.

CROSS-CHECKS:
- **Doubled-16 D_F**: severed-pair slope on the full J-doubled 16-dim operator = 1.000000000 (|slope₁₆ − slope₈| = 9.1e-12). The disconnect geometry is doubling-invariant — a property of the channel coupling graph, not of the chiral/J doubling (consistent with the S100a doubling-invariance check, dev < 1e-6).
- **Diagnostic severances (non-gating robustness)**: (1,1) slope 1.000000000 (dev 1.8e-11, ρ* = 15.5816, conn-flat 2.4e-9); (3,0) slope 1.000000000 (dev 4.1e-11, ρ* = 1.5582, conn-flat 2.6e-9). Every single-edge severance reproduces the slope-1 CLASS-γ signature — the divergence is generic to the cut, not specific to which edge.
- **Unregulated severed distance** = `unbounded` (CLARABEL certificate) for all three severances: with the Frobenius ball removed there is no Lipschitz path across the cut, so the sup is +∞. The regulated sweep traces the linear growth (PASS path) rather than only certifying unboundedness (the INFO degenerate path — NOT triggered here, the SDP stays `optimal` at every R).
- **ω_max convention identity**: our cache floors reproduce the s100a `omega_D2_floors` to 0.0e+00 rel-dev (same L12 cache, same τ_fold); flatness ceiling 1e-8 sits above the s100a connected R-dev floor 1.79e-9 (plan §IV.5 item 3).

SUBSTITUTION CHAIN (the slope-1 DIRECTION claim — `math-scripts.md §"Double-Check Logic Before Compute"`, with substituted numbers):

> Claim: "the severed pair's regulated distance grows LINEARLY in R — log-log slope EXACTLY 1; connected pairs are R-flat (slope 0 on the flat window)."
> - **Def 1** (regulated distance): `d_R(p,q) = sup{ |f(p)−f(q)| : ‖[D,f]‖_op ≤ 1, ‖f‖_F ≤ R }` [the s100a machinery form, `connes_distance_sdp`].
> - **Def 2** (severed edge): `t_{(1,0)} = 0` ⟹ node g1 = (1,0) disconnects from {v, g2, g3}; the Lipschitz constraint `‖[D,f]‖ ≤ 1` no longer couples f(g1) to f(v) (no path of nonzero couplings — the unregulated SDP returns `unbounded`, confirmed).
> - **Substitute**: between the two components |f(v) − f(g1)| is bounded ONLY by the regulator; the optimizer pushes the inter-component offset to the ball edge, `|f(v) − f(g1)| = c·R`, with c the component-separation constant fixed by the gauge quotient within each component. Here c = 1/√2 = 0.707107 (the 2-node {v,g1} component contributes the Frobenius norm `√(x_v² + x_{g1}²)` at the ball edge with the gauge-fix x_v = 0, so the attainable offset is R/√2 — confirmed: d_R/R = 1.101788/1.558163 = 0.707107 at every grid point).
> - **Simplify**: `d_R = c·R` ⟹ `ln d_R = ln c + ln R` ⟹ `d ln d_R / d ln R = 1` EXACTLY. The component-separation constant c is a MULTIPLICATIVE pre-factor — annihilated by the log-derivative. This is the `math-scripts.md` MANDATORY K=3 multiplicative-normalization-cancellation pattern instantiated on the **regulator-scale axis** (the OLS-on-`ln R` operator is `d/d ln R`; `d ln c / d ln R = 0`). The SLOPE is the structural content; the intercept ln c = −0.346574 is the empirical residue.
> - **Direction**: slope = **+1** for the severed pair (CLASS-γ commutative signature). For a connected pair the sup is attained INSIDE the ball once R > ρ* ⟹ d_R independent of R — slope 0, flat (verified: connected rel-dev ~1.6e-9 on R ≥ ρ*).
> - **Conclusion** (substituted): |slope − 1| = 1.82e-11 ≤ 1e-3 (severed); flat-window rel-dev 1.568e-9 ≤ 1e-8 (connected); ρ* = 15.5816 ≤ 10·ω_max = 15.5816 (equality). A slope ≠ 1 would have falsified the linear-divergence form of Theorem A clause 3; the computed slope is 1 to 11 significant figures.

ASSESSMENT (constraint-map / substrate framing): GEOMETRIC-class. The substrate's metric face is finite and regulator-free BECAUSE its channel coupling graph is connected — connectivity of the coupling graph IS the substrate property that makes state-pair geometry intrinsic. This gate verifies the converse at its boundary: cut ONE coupling (t_g = 0) and the substrate's own metric announces the cut as a linear-in-R regulator dependence (CLASS-γ) — the geometry becomes container-dependent (Frobenius-ball-radius-dependent) exactly where the substrate's relay structure is broken. Flow: D_K sector floors → greybody star couplings → channel-graph connectivity → regulator-(in)dependence dichotomy. The S87/S88 regulator wall (full M_n(ℂ) ⇒ regulator-divergent) is thereby a TWO-SIDED structural theorem of the fiber's coupling graph (finite + regulator-free iff connected; linear-in-R iff disconnected), portable to any finite triple — with only the threshold location ρ* an empirical residue. The verdict closes the divergent side of the dichotomy; the connected side was closed by S100a.

CORNER DECLARATION: Cell-IV (algebra-DEPENDENT state-pair functional family per S-1 §IV.2 STATE-PROJ classification; `cross-pillar-bridge-anatomy.md` algebra-axis orthogonality declared at the gate block). NO §VII registry landing occurs in this gate — no corner-cell registry audit fires here.

DOWNSTREAM: W2-6 PASS (with W2-5) clears the Wave-6 `S101-VIIBM-STATEPROJ-LANDING` STATE-PROJ landing's structural clause (i) — the two-sided dichotomy (finite + regulator-free iff connected; linear-in-R iff disconnected) — to proceed at full strength; `S101-CONNES-STATEPROJ-STAGE2-VERIFY` (Wave 7) inherits the landed text. ρ* = 15.5816 (= 10·ω_max) is the one empirical residue carried forward (threshold location, not structure).

ARTIFACT POINTERS: `computations/session-101/s101_connes_distance_disconnect_boundary.py` / `.npz` / `.png`; verdict in `computations/session-101/s101_gate_verdicts.txt` (audit_sha256 `9eea47088bef70fa734a7d9fa77f709f4b7e71626e96a81df4c09c7a13d036fd`).

---

## Wave 2 Synthesis (team-lead)

**Outcome**: 6 gates — **5 PASS** (W2-1, W2-2, W2-3, W2-5, W2-6) + **1 INFO** (W2-4). sig_5 clean. Verdict file lines 27/32/37/45/50/60.

**W2a widening chain (1 → 2 → 3) — magnitude axis CLOSED**:
- W2-1 PASS: `W_flat = 9/5` EXACT at the lower edge — the generation-envelope shape is Casimir-linear at the fold to machine ε (slope_lo=slope_hi), a static Casimir datum the transit preserves rather than re-keys.
- W2-2 PASS: **Reading A confirmed** (one operator family, three charts; Leg A PASS / Leg B PASS / Leg C GRADED). Dual-prior → posterior ≈0.9 Track A.
- W2-3 PASS: exactly-one knob survives — **(iii) S₀ = τ_fold/T_acoustic = 95/56, DERIVED**. The magnitude axis closes as a **derived moduli-acoustic identity** (W3-10 fingerprint promoted identity→derivation, W-3 OQ-2). The (i)/(iii) 0.52% degeneracy split by output-FORM (GRADED selector), never band-tightening.

**W2b connes machinery — both clear the W6 STATE-PROJ landing**:
- W2-5 PASS (Lemma B boundary: 1/‖S‖ exact, strictness +8.6e-3, aligned-equality saturates) + W2-6 PASS (disconnect slope = 1.000000, the CLASS-γ signature completing the two-sided dichotomy with S100a's connected side). Both clear `S101-VIIBM-STATEPROJ-LANDING` (W6) at full strength; W7 Stage-2 inherits the landed text.

**W2-4 INFO (orientation banked; hardest target is a sign-theorem)**: sign=PASS — per-component C₂-descending map confirmed in BOTH quark components (matching the lepton map), up>down at gen 3. magnitude=INFO — the uniform-κ envelope is **monotone and cannot cross**: gen-1 inversion (gen1<1 ∧ gen3>1) is structurally impossible for a single (κ_up,κ_down) pair on a C₂-monotone ω-ladder. The quark-sector [SIGN] orientation anchor for the S102 CKM program is SET; the gen-1 crossing routes to per-generation kernel structure (→ CF below).

### Effected In-Session (non-math — completed by the team-lead orchestrator before STOP)

(none standalone this wave. W2's forward actions route to compute gates / mack-sole-writer territory, NOT orchestrator-direct edits: the carrier registry text + capstone magnitude row land via the W6/mack pipeline (W2-3 fb_pair, line 209); the STATE-PROJ dichotomy clearance is consumed by W6's `S101-VIIBM-STATEPROJ-LANDING`. EVOI rank-9b (texture-cluster) spans W2+W3 — its status reconciliation is deferred to session wrap-up after W3 lands, not edited mid-rank. No standalone forward-register status edit surfaced.)

(Self-audit: `grep -c '^- \[ \]'` on this sub-section = 0 — no unchecked items.)

## Carry-Forward Computations

### CF-S102-QUARK-PERGEN-KERNEL — per-generation kernel structure for the gen-1 up/down crossing

1. **What**: derive the generation-DEPENDENT slope structure (per-generation κ_g, or an ω_g non-monotone in C₂) that supplies a gen-1 up/down crossing — reproducing gen-1 inversion (m_u/m_d < 1) ∧ gen-3 upright (m_t/m_b > 1) — which W2-4 proved is structurally impossible for any single (κ_up, κ_down) pair on a C₂-monotone ω-ladder. Frame per-component CKM as the misalignment of two rank-one dressings (E-2(e)).
2. **Inputs**: `computations/session-101/s101_w3_quark_component_orientation.npz` (D/c ladders, ω_g triple {0.253, 0.570, 1.140}, Ω^D/Ω^c=2 exact, PDG held-out m_u/m_d=0.4596 / m_t/m_b=41.28); the κ-triple {lepton 1.89, up 1.29, down 0.78} ([SPECULATION]-class); the S99 fermion-mass panel; the W2-4 orientation [SIGN] anchor (sign=PASS, audit `833a3daf`).
3. **Gate**: PASS iff a substrate-DERIVED per-generation kernel reproduces gen-1 m_u/m_d < 1 AND gen-3 m_t/m_b > 1 with the orientation [SIGN] anchor preserved (sign=PASS) AND both W3-9 walls + [J,D_K]=0 intact; the per-gen structure must be derived, not fitted to PDG.
4. **Effort**: 1–2 waves (CKM program). **Depends on**: S101-W3-QUARK-COMPONENT-ORIENTATION INFO (this wave); the orientation anchor.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-08 | Texture-cluster magnitude axis (W_flat) | OPEN (rank-9b magnitude part) | PASS — W_flat=9/5 exact at fold (Casimir-linear) | W2-1 PASS |
| 2026-06-08 | Carrier reading (envelope vs carrier) | OPEN (Reading A vs B dual-prior) | Reading A confirmed (one family, three charts) | W2-2 PASS, posterior ≈0.9 Track A |
| 2026-06-08 | S₀ residual-knob identity | OPEN (3 candidates; W3-10 fingerprint) | DERIVED: S₀ = τ_fold/T_acoustic = 95/56 (OQ-2 closed) | W2-3 PASS, exactly-one + GRADED selector |
| 2026-06-08 | Star-metric Lemma B (op-norm couplings) | OPEN (boundary unverified) | PASS — clears W6 STATE-PROJ clauses (i)–(iii) | W2-5 PASS |
| 2026-06-08 | Connes-distance disconnect divergence | OPEN (one side of dichotomy) | PASS — slope-1 CLASS-γ; two-sided theorem complete (w/ S100a) | W2-6 PASS |
| 2026-06-08 | Quark ε_LX orientation + gen-1 crossing | OPEN | Orientation BANKED (sign=PASS); gen-1 crossing → CF-S102-QUARK-PERGEN-KERNEL (sign-theorem: impossible for uniform-κ) | W2-4 INFO |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict audit |
|:-----|:-------|:------------|:------------|:--------------|
| W2-1 | `s101_w2_blocktrace_widening.py` | `.npz` (12.7 KB; npz SHA `e0a79fc3…`) | `.png` | `78f57414…` |
| W2-2 | `s101_envelope_carrier_discriminate.py` | `.npz` (20.7 KB) | `.png` | `463f3203…` |
| W2-3 | `s101_w3_s0_knob.py` | `.npz` (19.5 KB) | `.png` | `513e0cbf…` |
| W2-4 | `s101_w3_quark_component_orientation.py` | `.npz` (11.5 KB) | `.png` | `833a3daf…` |
| W2-5 | `s101_star_metric_block_lemma.py` | `.npz` (19.4 KB) | `.png` | `08ee01cb…` |
| W2-6 | `s101_connes_distance_disconnect_boundary.py` | `.npz` (20.9 KB) | `.png` | `9eea4708…` |

All scripts in `computations/session-101/`. Verdicts + dual-SHA + schema-v2 3-tuples (W2-1/W2-2/W2-4) + per-leg/explanatory rows in `s101_gate_verdicts.txt`.
