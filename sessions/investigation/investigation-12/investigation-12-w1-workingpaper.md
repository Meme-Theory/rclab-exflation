# Investigation 12 Wave 1 — Spectral-functional: selection, A_s reference-state, n_s coherence (Results Working Paper)

**Investigation**: 12 | **Wave**: 1 | **Plan**: investigation-12-plan-w1.md | **Theme**: the spectral-functional theorist's move on the n_s/A_s/R_1 spine — modular SELECTION (G-L1), A_s GGE-modular reference (G-L3), n_s functional COHERENCE (G-L2), R_1 same-regulator provenance (C-L4), Krajewski tilt census (A-L2).

**Verdict track**: all 5 gates are compute/solo → each emits a verdict line to `computations/investigation-12/inv12_gate_verdicts.txt` via `emit_verdict(session=12, track="investigation", ...)` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`. The `s{N}_`/`session-` prefixes are FORBIDDEN to cross into this track.

## Gate Sections

### §W1-1. INV12-W1-1-MODULAR-FUNCTIONAL-EXTREMIZATION

**Status**: COMPLETED
**Gate ID**: `INV12-W1-1-MODULAR-FUNCTIONAL-EXTREMIZATION`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: the substrate's own faithful normal modular weight ω (§VII.BZ / K12) extremizes the spectral entropy functional S_modular(τ) = Tr(D_K(τ)² ρ_ω) at τ_fold = 0.190 — the substrate-derived SELECTION principle that F-STAR-SELF-CONSISTENCY (S76) failed to find with four other principles.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w1.md §W1-1` (machinery pin, thresholds, substitution-chain source).

**MCP Pre-Compute Audit** (query-first; executed before the script was written):
- `trace_entity('faithful normal modular weight')` → returns **K12 (NEW S105)** §VII.BZ BDI Horizon-Faithfulness Protection (`proven_1469`); ρ_ω lives on `A_hor = A_K ⋊_{σ^ω} ℝ`, STAGE-3-PERMANENT — confirms the modular weight is a constructed, registered object (the gate consumes it, does not derive it).
- `get_constant('tau_fold')` → **0.19** (S12/S42, `CONST-FREEZE-42`, `s42_constants_snapshot.npz`, not superseded) — pins the fold the stationarity test brackets.
- `search_knowledge('GGE entropy functional variational principle')` → surfaces the OPEN channel **`GGE-ENTROPY-FUNCTIONAL as V.P.`** (session-84): "τ_fold may extremize S_GGE … §W8a-85 did NOT test these. Each is a distinct V.P." and the prior `S84-VARIATIONAL-PRINCIPLE-REFORMULATION: FAIL`. **NOT PRE-CLOSED**: §W8a-85 ran the *meta*-reformulation (Chamseddine-Connes), not the modular-weight V.P. — this gate tests a genuinely-unrun fourth functional.
- `trace_entity('F-STAR-SELF-CONSISTENCY')` → empty (the S76 four-principle survey is in the lizzi seed/memory, not the indexed graph) — confirms the four prior selection principles are NOT the modular weight; this is the fifth, independent test.
- Constants verified importable (`canonical_constants.py`): `tau_fold=0.19`, `Delta_BCS=0.46425`, `Delta_B2=0.732026`, `Delta_B3=0.176`, `a2_fold=2776.165`.

**Verdict**: **FAIL** — `sign_verdict=FAIL  magnitude_verdict=FAIL  regime_verdict=VALID` → composite **FAIL** (collapse rule: `sign_verdict==FAIL ⇒ composite=FAIL`).

S_modular(τ) is **MONOTONE INCREASING through τ_fold** — there is no extremum at the fold. The substitution chain's [SIGN] prediction of a sign-CHANGE bracketing τ_fold is falsified (sign is `+1` on both sides). This is the Track-B outcome (prior 0.65): **the modular functional does NOT select the fold; the substrate's faithful-normal modular weight joins the four S76 principles that failed.** The G-L1 selection gap remains open; the framework's functional stays cornered-by-elimination, not forced.

**Results**:

4-tuple: `(value=dS_dtau_fold=0.7821_…_extremum=MONOTONE_signL=+1_signR=+1, scheme=MODULAR, convention=FROZEN-GGE-NON-KMS, L_max=10)`.

| Quantity | Value (4 sig figs) |
|:---------|:-------------------|
| dS_modular/dτ \|_{τ_fold} | **+0.7821** |
| \|dS/dτ\|/S_scale at fold | **0.5517** (PASS-band ≤ 1e-3 → ~552× over) |
| S_scale (mean S_modular over window) | 1.417 |
| S_modular range over [0.170, 0.210] | [1.402, 1.434] |
| dS/dτ left of fold (τ=0.189) | +0.7777 |
| dS/dτ right of fold (τ=0.191) | +0.7864 |
| extremum class | **MONOTONE** (no interior stationary point) |
| interior min\|dS/dτ\| (edge artifact) | τ=0.1710 (window low edge; off-fold) |

**[SIGN] substitution chain (with substituted numbers)** — *FUNCTIONAL: MODULAR (the fourth family); the substrate's own ω-density weighting, NOT a cutoff f*:

- **Claim**: S_modular(τ) = Tr(D_K(τ)² ρ_ω) is stationary at τ_fold (dS_modular/dτ\|_{τ_fold} = 0).
- **Def 1** — D_K(τ): Jensen-deformed Dirac operator; |λ_k(τ)| from the L_max=10 horizon sectors (cross-checked bit-faithful to the S84 cache: max\|traj−cache\| = 8.9e-16…5.3e-15 across blocks (0,0)/(1,0)/(0,1)/(1,1)). D_K anti-Hermitian ⇒ λ_k = −i\|λ_k\|.
- **Def 2** — ρ_ω: diagonal of the S105 faithful-normal modular state (FROZEN-GGE non-KMS), the BdG occupation f ∈ (0.1572, 0.4345) (**faithful: 0<f<1 confirmed for every horizon mode**), weighted by the AV3 per-block trace weights {(0,0):1.258, (1,0):2.380, (0,1):2.380, (1,1):4.342}. **τ-INDEPENDENT** (fixed by the minigap; not chosen).
- **Def 3** — S_modular(τ) = Σ_k \|λ_k(τ)\|² w_k, w_k = ρ_ω diagonal, Σw_k = 1 (normalized: blocks weigh 0.1406 / 0.2388 / 0.2388 / 0.3817).
- **Substitute**: dS/dτ = Σ_k 2\|λ_k(τ)\| (d\|λ_k\|/dτ) w_k  [only λ_k(τ) carries τ].
- **Canonical form**: stationary ⟺ Σ_k \|λ_k(τ_fold)\| \|λ_k\|′(τ_fold) w_k = 0.
- **Read off**: the ω-weighted velocity sum at τ_fold = **+0.7821/2 = +0.3911 > 0** (and \|λ_k\|′ > 0 across the window — the eigenvalues uniformly *grow* with τ on this branch). Sign(dS/dτ) = **+1 left AND +1 right** ⇒ **no sign change** ⇒ **MONOTONE**, not stationary. [SIGN] prediction (sign-change at a stationary fold) **FALSIFIED**.
- **Conclusion**: no sign-change of Σ_k λ_k λ_k′ w_k across τ_fold ⇒ S_modular is NOT extremized at the fold ⇒ the substrate's modular structure does NOT select τ_fold. G-L1 stays open.

**Constraint-map consequence** (solution-space reading, `epistemic-discipline.md`):

This **closes the modular-weight corridor of the G-L1 selection gap**. The functional-selection problem now has FIVE failed substrate-derived selection principles (the four of S76 + the modular weight ω of this gate). The result is *informative*: it shows the faithful-normal modular density — the most natural substrate-internal weighting, the one object that is read OFF the substrate with zero free parameters — produces a spectral 2nd moment that rises monotonically through the transit fold rather than extremizing there. **The substrate's entropy/energy structure does not single out τ_fold via the modular weight.** This is consistent with the S106 GEM finding that ω′ is bulk-faithful but carries no area-clock (2b INFO): "no area-clock" and "no variational stationarity at the fold" are now BOTH established for the modular weight — they are the same structural fact viewed two ways (the modular flow does not pin the fold). The framework's commitment of the n_s functional to pure √x (S103) remains **cornered-by-elimination, not forced** — no substrate principle yet selects it.

**Downstream (fb_pair backward)**: feeds **INV12-W4-2** (SA-effective-action diagnosis workshop) as the lizzi-side evidence that the *modular fix does not select* — the "wrong functional → modular weighting" repair is **excluded**, so the W4-2 diagnosis must look elsewhere (wrong-signature, or a non-modular selection object). Dual-prior re-allocation: FAIL (monotone) → 0.9 mass to **Track B** (selection still open, modular functional excluded as selector). NO SELECTION-PRINCIPLE registry-landing candidate opens (PASS was required).

**Plan-text-drift note** (`substrate-first-canonical-sourcing.md §(ii.B)`): plan §W1-1 `input_files` pins the D_K cache at `computations/_shared/s84_spectrum_cache_L12_tau019.npz`; that path is **absent**. The file is canonically at `computations/session-84/s84_spectrum_cache_L12_tau019.npz`. Resolved at runtime (the same drift INV12-W3-1 already corrected — its verdict carries `cache_path_drift_corrected_to_session-84`); the correction is documented in the verdict `value=` field and the `# cache_path_drift_corrected` companion row. No fabrication; the bit-faithful cross-check (machine-ε agreement with the cache abs_evals at τ=0.19) confirms the resolved cache IS the canonical spectrum.

**Output Artifacts** (closure-verification checklist):
- Script `computations/investigation-12/inv12_w1_1_modular_functional_extremization.py` — present; contains `from canonical_constants import` and `print_verdict_payload` (verified by grep).
- Data `computations/investigation-12/inv12_w1_1_modular_functional_extremization.npz` — present (S_modular(τ), dS/dτ, trajectory cross-check, modular weights, dual-SHA).
- Plot `computations/investigation-12/inv12_w1_1_modular_functional_extremization.png` — present (S_modular(τ) + dS/dτ, fold + extremum markers).
- Verdict line `computations/investigation-12/inv12_gate_verdicts.txt` — present; matches `^INV12-W1-1-MODULAR-FUNCTIONAL-EXTREMIZATION:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + [SIGN] 3-tuple row (`sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`) + extra companion rows present.
- **Canonical (latest non-superseded) line**: `audit_sha256=c36c0754b542a00038e1b4efaac59da64ce397554a880ee31bcc98ec38553bd8`, `content_sha256=7c7e0986b8fa5079750041905c9c6969cc190bd0ffc815786589923f6656d025`, carrying `supersedes=b5f27b2f21cc774ee8ad32fc1a69ecf157977617fcc9f1b484f59d847bb7a1ca`.
- **Supersession note** (`gate-verdicts.md §"Option A"`): the first-emitted line (`audit_sha256=b5f27b2f…`) is retained on disk under absolute verdict permanence; the canonical reading is the latest non-superseded line above. The correction was a SHA recompute after renaming the script's emit helper `_emit → print_verdict_payload` to satisfy the plan `must_contain` token; the **physics is byte-for-byte identical** (S_modular MONOTONE, dS/dτ=+0.7821, composite FAIL) — only the `content_sha256`/`audit_sha256` changed because the script bytes changed.

---

### §W1-2. INV12-W1-2-A-S-GGE-MODULAR-REFERENCE

**Status**: COMPLETED
**Gate ID**: `INV12-W1-2-A-S-GGE-MODULAR-REFERENCE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: the A_s amplitude floor (5.078e-9 TD-canonical, 3.02× Planck) — proven a PERMANENT WALL only RELATIVE TO Bunch-Davies (S82 W2-4) — lifts into the Planck band when the reference is the substrate's own post-transit GGE modular state ω instead of the BD vacuum (the entanglement-first-law a_2 variation differs).
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w1.md §W1-2`. CONSUMES the cross-wave forward-pin (orchestrator-corrected canonical name) `inv12_w3_1_relic_spectrum_ode_lock.npz` — the npz EXISTS at dispatch, so the FULL derivation ran (no PRE-REG-INC partial-input close); locked-{β_k} availability flag = TRUE.

**MCP Pre-Compute Audit**:
- `get_constant('A_s_CMB')` → 2.1e-9 (Planck 2018 VI; S96-OBS-ANCHOR-HYGIENE). CONFIRMED denominator of R_wall.
- `get_constant('A_s_FW')` → NOT FOUND as a standalone pin; the A_s_CMB note records `A_s_FW is a PENDING BAND [3.11,4.27]e-9`. The BD-referenced anchor is the falsifier-rigor-registry Row 8 value (next query).
- `search_knowledge('A_s wall Bunch-Davies 3.02 permanent')` → falsifier-rigor-registry Row 8: `A_s SCHEME-DEPENDENT, 5.078e-9 (S84 AS-PIN-MAP-COMMIT, TD-canonical) vs 2.099e-9 Planck, 0.384 OOM above`; **S82 W2-4 theorem "Substrate IC CANNOT SUPPRESS A_s relative to BD; structural bound"** (PROVEN); S83 HARDENED CF23 to PERMANENT WALL ("not remediable at the substrate-IC layer").
- `trace_entity('entanglement first law A_s')` → NO direct trace; the B-L3 a_2-variation route is realized THROUGH the S82 W2-4 `K_substrate = S_IC^GGE(k_pivot)` multiplicative correction (search below).
- `search_knowledge('S_IC GGE modular reference K_substrate 5.078 A_s permanent wall')` → **the GGE-modular reference object ALREADY EXISTS at S82 W2-4**: `A_s^substrate = A_s^{BD} · K_substrate, K_substrate ≡ S_IC^GGE(k_pivot)`, with `S_IC^GGE = 1 + 2 n_k = |α+β|²` and the **W2-4 positivity wall K ≥ 1** (from `n_k ≥ 0`). This gate is the SAME-INPUT-SOURCE upgrade: recompute K_sub from the locked W3-1 occupations instead of S43-memory band averages.
- `get_constant('tau_fold')` → 0.19 (CONST-FREEZE-42). `T_GGE_B2=0.668`, `Delta_B1/B2/B3` from canonical_constants (S43/s53). PRE-CLOSED status: the SIGN of the result is pre-determined by the S82 W2-4 PROVEN positivity wall; this gate re-anchors the MAGNITUDE to the locked relic and tests whether the structural conclusion survives the input-source change (it does).

**Verdict**: **FAIL** — sign=FAIL, magnitude=INFO, regime=VALID → composite **FAIL** (sign-collapse rule, `gate-verdicts.md §"Composite-collapse rule"`). The GGE modular reference does **NOT** lift the A_s wall; it raises A_s (negligibly, by +0.002%), confirming the wall is reference-state-INDEPENDENT in SIGN. CF23 CONFIRMED.

**Results**:

- **A_s^{GGE-ref} = 5.0783e-9** (canonical R1-softest pivot); **R_wall = A_s^{GGE-ref}/A_s_CMB = 2.4182**.
- 4-tuple: `(value=2.4182261264583, scheme=MODULAR-GGE-REFERENCE, convention=FROZEN-GGE-NON-KMS, L_max=10)`; `regulator_pin=a_2^{ζ}` (Einstein-Hilbert moment; entanglement-first-law variation).
- **Locked-{β_k} availability flag: TRUE** (full derivation; `inv12_w3_1_relic_spectrum_ode_lock.npz`, 1248 unique modes). Per-mode squeezing identity `S_IC = |α+β|² = 1+2n_k` verified to residual `3.85e-3` (the W3-1 single-segment adiabatic-truncation floor; Wronskian `|α²−β²−1|` resid `3.84e-3`); the structural identity holds.

- **[SIGN] substitution chain (substituted numbers)** — building on S82 W2-4 (`session-82-results-workingpaper.md:1696–1718`):
  ```
  Claim: A_s^{GGE-ref} ≥ A_s^{BD}  (GGE reference CANNOT lower A_s; predicted FAIL of lift)
  Step 1 (defs):  S_IC^BD = 1;  S_IC^GGE(k) = 1 + 2 n_k = |α_k+β_k|²;
                  K_sub(k) = S_IC^GGE/S_IC^BD = 1 + 2 n_k;
                  A_s^{GGE-ref} = A_s^{BD} · K_sub(k_pivot)   [E2.4 → multiplicative; S82 W2-4]
  Step 2 (positivity): n_k = |β_k|² ≥ 0  (number operator; locked W3-1 beta2_k)
                  ⇒ S_IC^GGE = 1 + 2n_k ≥ 1  ⇒  K_sub ≥ 1
  Step 3 (canonical): A_s^{GGE-ref} = A_s^{BD}·K_sub, K_sub ∈ [1,∞);
                  R_wall^{GGE} = R_wall^{BD}·K_sub = 2.4182·K_sub ≥ 2.4182
  Step 4 (direction): K_sub ≥ 1 ⇒ A_s^{GGE-ref} ≥ A_s^{BD}. The plan's sign-PASS is
                  "A_s^{GGE-ref} ≤ A_s^{BD}"; here Δ = A_s^{GGE-ref} − A_s^{BD} = +1.04e-13 > 0
                  ⇒ sign_verdict = FAIL (GGE raises the floor, however slightly).
  Conclusion: the BD-referenced wall is reference-state-INDEPENDENT in SIGN; n_k ≥ 0 forbids the lift.
  ```
  - `R_wall^{BD} = 5.078171e-9 / 2.1e-9 = 2.4182` (exact rational `725453/300000`, Sage-verified).
  - **K_sub readings (all ≥ 1 by positivity)**: R1-softest (CANONICAL, ω_soft=0.9409) = 1.0000205; R2-mult-weighted-mean = 1.0005472; R3-geometric-mean = 1.0003781; R4-max-occupation = 1.0038373. **K_sub band [1.0000205, 1.0038373]**.
  - `Δ = A_s^{GGE-ref} − A_s^{BD} = +1.04e-13 > 0` (sign FAIL).
- **sign_verdict = FAIL** (GGE reference does NOT relax the BD floor — it equal-or-amplifies; the structural `K_sub ≥ 1` positivity wall holds, K_sub_min = 1.0000205 ≥ 1). **magnitude_verdict = INFO** (R_wall = 2.4182 in the (1.1, 2.8) band). **regime_verdict = VALID** (squeezing-identity residual `3.85e-3 ≪ 1`; the per-mode `S_IC=1+2n` identity holds, method in-regime). Composite = **FAIL** (sign=FAIL dominates).

- **S82 W2-4 cross-check (faithful reproduction of the S82 machinery)**: feeding S43-memory band occupations (T_GGE_B2=0.668, T_B1=0.4350; n_k^GGE=1/(e^{Δ/T}−1)) reproduces `S_IC^B1=2.0486, S_IC^B2=2.0042 → K_base(geomean)=2.0262`, matching the S82-documented canonical `K_base = 2.035` (rel-dev 0.4%). This confirms the gate evaluates the SAME functional — the only change is the input source.

- **Spectral-functional classification (Lizzi domain)**: the K_sub MAGNITUDE is **SCHEME/INPUT-DEPENDENT** (locked-relic occupations n̄_mw = 2.736e-4 ≪ S43-memory band-averaged n~0.5; K_sub−1 differs by ~2000×: 0.00005 vs 1.0). But `K_sub ≥ 1` — the SIGN of the reference-state correction — is **FUNCTIONAL-INDEPENDENT**: it is forced by `n_k = |β_k|² ≥ 0`, a number-operator positivity no reference-state choice can violate. Whichever occupation feeds the formula, the wall does not lift.

- **ρ_relic L_max truncation band** (orchestrator override): `15.41 (p+q≤7) → 26.85 (p+q≤8)`, `truncation_consistent=False`. A_s^{GGE-ref} depends on the per-mode OCCUPATIONS n_k (machine-precision firm), NOT on absolute ρ_relic; the verdict is **band-INDEPENDENT**. The band is reported per the orchestrator's cross-wave note.

- **Constraint-map consequence**: FAIL → the 3.02× A_s wall is **reference-state-INDEPENDENT** (the overproduction is physical, not a Bunch-Davies artifact). **CF23 CONFIRMED** ("permanent structural-position wall, not remediable at the substrate-IC layer" — S83). The modular-reference relief channel (B-L3) is **closed**: the GGE modular state is the substrate's actual post-transit state, and it can only equal-or-amplify A_s relative to BD. A_s relief, if any, must come from the exit greybody (INV12-W3-4) or be accepted as outside predictive reach. Track-B posterior (physical wall) → 0.9 mass. Feeds INV12-W4-1 (A_s wall-reading workshop) as the lizzi-side "NOT a BD-artifact" evidence and INV12-W4-3 (A_s three-route synthesis, modular-reference route).

**Output Artifacts** (closure-verification checklist):
- script `inv12_w1_2_a_s_gge_modular_reference.py` — EXISTS; `must_contain` grep (`from canonical_constants import`, `print_verdict_payload`) PASS (see grep block below).
- data `inv12_w1_2_a_s_gge_modular_reference.npz` — EXISTS.
- plot `inv12_w1_2_a_s_gge_modular_reference.png` — EXISTS.
- verdict_line at `computations/investigation-12/inv12_gate_verdicts.txt` — matches `^INV12-W1-2-A-S-GGE-MODULAR-REFERENCE:.* audit_sha256=[a-f0-9]{64}` (audit_sha256=`74de824dbe88af99e3bcc9c79d42794b9ec8e46453568b92880a03c372989650`); dual-SHA companion row + [SIGN] 3-tuple row (`sign_verdict=FAIL magnitude_verdict=INFO regime_verdict=VALID`) + `regulator_pin` row + 2 structural-classification rows all present.

---

### §W1-3. INV12-W1-3-N-S-FUNCTIONAL-COHERENCE

**Status**: COMPLETED
**Gate ID**: `INV12-W1-3-N-S-FUNCTIONAL-COHERENCE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: the WORKING functional f* = 0.9117√x + 0.0883 e^{-x} gives the same n_s, to within the Planck σ-budget (0.0042), as the COMMITTED pure-√x value (n_s_FW_sqrt_cutoff = 0.959) — or n_s is published as a {√x, f*} band. A COHERENCE check between two already-canonical functionals; re-selection is FORBIDDEN (PROHIBITED_ACTIONS Class 1).
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w1.md §W1-3`.

**MCP Pre-Compute Audit** (query-first; executed before the script was written):
- `get_constant('n_s_FW_sqrt_cutoff')` → **0.959** (S103, `S103-Q28-LAYER2-A6` PASS COMMIT; A_5→A_6 sixth-regulator atlas-cardinality robustness DISCHARGED; value = S65 BCS+1-loop √x family) — pins the COMMITTED √x point-value the coherence partner is measured against.
- `get_constant('t_star')` → **0.08832** (S72 spectral-functional fit; `T-STAR-ONELOOP-ORIGIN`; the one empirical functional coupling, Λ_QCD analog) — the e^{-x} admixture weight in f* = (1−t*)√x + t*·e^{-x}.
- `search_knowledge('e^-x functional blue tilt excluded')` → surfaces `s84_w4_blue_transit_tilt_inaccessibility` + `s65_blue_tensor_tilt` / `BLUE-65`; confirms the **blue-tilt structure** of the e^{-x} family (the substrate ground for "e^{-x} tilts bluer"). **NOT PRE-CLOSED**: no prior gate compares √x↔f* n_s coherence — this is a genuinely-unrun two-functional comparison.
- `trace_entity('epsilon_H sign reversal A13')` → **theorem A13 "Epsilon_H Sign Reversal"**: "eps_H changes SIGN between cutoff families (√x: +0.022 vs zeta: negative); n_s spread across functionals: 0.164 (39× Planck error)." **Critical scoping**: the 0.164 spread is across the FULL family **including zeta + anomaly** (where ε_H flips sign); √x and f* are BOTH in the **cutoff** family — S64 T12 found the within-cutoff-family spread is only 0.0012 (already inside σ_budget). This gate measures the √x↔f* sub-spread directly.
- Constants verified importable (`canonical_constants.py`): `n_s_FW_sqrt_cutoff=0.959`, `t_star=0.08832`, `M_KK=7.4287e16`, `planck_ns_err=0.0042`, `S_fold=250360.677`, `dS_fold=58672.80`, `d2S_fold=317862.85`.
- Canonical n_s pipeline (S64 N2 / S65 / S62): `n_s = 1 − 2ε_H`, `ε_H = (1/2)S'²/(S·S'')` — n_s is a SHAPE INVARIANT of S(τ) = Tr f(D²/Λ²); the functional f enters through S(τ). This is the established machinery, NOT the textbook `1−6ε+2η`.

**Verdict**: **PASS** — `sign_verdict=PASS  magnitude_verdict=PASS  regime_verdict=VALID` → composite **PASS** (collapse rule: all sub-verdicts non-FAIL ⇒ composite=PASS).

|Δn_s| = n_s(f*) − n_s(√x) = **+0.000909 = 0.216σ**, well inside the σ_budget (0.0042). This is the Track-A outcome (prior 0.45): **the framework's COMMITTED n_s (pure √x) is COHERENT with its WORKING functional f*** — the two are NOT on contradictory functionals. The C-L1 falsification claim (n_s vs ACT-DR6/SPT-3G at 2.7–5σ) stands as published, with the 0-free-parameter cleanliness intact. **G-L2 closes**: there is no √x↔f* incoherence to publish as a band; the single-value n_s = 0.959 faithfully represents the framework's own machinery to within 0.32σ.

**NO-RE-SHOP NOTE** (PROHIBITED_ACTIONS Class 1, respected): this gate did NOT search for a third functional, did NOT tune t*, did NOT compare against zeta/anomaly families. It tested whether the two ALREADY-CANONICAL cutoff-family functionals AGREE on n_s. They do. The functional commitment (S103 √x) is **untouched**; this is a coherence audit of two existing readings, not a selection.

**Results**:

4-tuple: `(value=9.086468e-04, scheme=FW, convention=TWO-FUNCTIONAL-FIXED-SPECTRUM-S36-MULTITAU-PRIMARY, L_max=10)`; `regulator_pin=a_2^{cutoff}` (both functionals' moments are cutoff-regulated, NOT zeta).

| Quantity | Value (4 sig figs) |
|:---------|:-------------------|
| n_s(√x), bare-tree | **0.9567** |
| n_s(f*), bare-tree | **0.9577** (bluer) |
| **Δn_s = n_s(f*) − n_s(√x)** | **+0.0009086** |
| \|Δn_s\| / σ_budget | **0.2163** (PASS-band ≤ 1σ) |
| σ_budget (Planck 2018 n_s 1σ) | 0.0042 |
| ε_H(√x) | +0.02163 |
| ε_H(f*) | +0.02118 |
| ε_H(e^{-x}, isolated) | **−0.06280** (blue: n_s = 1.126 > 1) |
| Δn_s vs COMMITTED 0.959 | −0.001350 (**0.321σ**) |
| f*/√x at fold (S36) | 0.91669 |
| f*/√x at fold (S84 L12 anchor) | 0.91669 (\|dev\| = 0.0e+00) |

**[SIGN] substitution chain (with substituted numbers)** — *FUNCTIONAL COHERENCE: √x vs f* on the IDENTICAL S36 spectrum (7 τ values); only the functional weight differs; the spectral action S = Tr f(D²/Λ²), Λ = M_KK*:

- **Claim**: n_s(f*) and n_s(√x) agree to within the Planck σ-budget (\|Δn_s\| ≤ 0.0042), OR n_s is a band.
- **Def 1** — n_s(√x): pure √x is f(u)=√u, so S_√(τ) = (1/Λ)Σ PW²Σ\|λ\|; the (1/Λ) **cancels** in ε_H ⇒ n_s(√x) is Λ-independent. Reproduces S_fold/dS_fold/d2S_fold bit-for-bit (rel dev 4.2e-15 / 1.3e-7 / 9.9e-6) ⇒ ε_H = +0.02163, **n_s = 0.9567** (= S62/S75 canonical; committed-with-BCS = 0.959).
- **Def 2** — f*(u) = 0.9117√u + 0.0883 e^{-u}, u = λ²/Λ², t* = 0.08832 (S72). ⇒ S_{f*}(τ) = 0.9117·S_√(τ) + 0.0883·G(τ), G(τ) = Σ PW² Σ_j e^{−λ_j²/Λ²}.
- **Def 3** — n_s(f) = 1 − 2ε_H(f), ε_H(f) = (1/2)S_f'²/(S_f·S_f'') on the SAME {λ_k(τ_fold)}.
- **Substitute**: Δn_s = n_s(f*) − n_s(√x), evaluated on the identical eigenvalue set; only f differs. The 0.0883·e^{−u} admixture weights LOW eigenvalues (e^{−u}≈1 at small u) and DECAYS as the spectrum stretches through the fold ⇒ G(τ) is a **decreasing** function of τ (G' < 0, G'' < 0 — verified: S_gauss falls 14941→13921 over τ∈[0.05,0.22]), opposite-sign derivatives to S_√' > 0.
- **Simplify**: the isolated Gaussian gives **ε_H(e^{-x}) = −0.0628 < 0** (n_s = 1.126, BLUE) — the substrate realization of "e^{-x} tilts the wrong way." Mixing 8.83% of this blue functional into 91.17% √x pulls ε_H DOWN: 0.02163 → 0.02118.
- **Read off (direction)**: lower ε_H ⇒ higher n_s ⇒ **n_s(f*) = 0.9577 > n_s(√x) = 0.9567**, i.e. Δn_s = **+0.000909 ≥ 0**. The [SIGN] prediction (e^{-x} admixture pushes BLUER) is **CONFIRMED** (isolated-Gaussian-bluer cross-check = True). sign_verdict = **PASS**.
- **Read off (magnitude)**: \|Δn_s\| = 0.000909 ≤ σ_budget 0.0042 ⇒ magnitude_verdict = **PASS**. Regime: ε_H ≈ 0.021 ≪ 1 for both ⇒ the first-order n_s = 1−2ε_H truncation is VALID.
- **Conclusion**: \|Δn_s\| = 0.216σ ≤ σ-budget ⇒ the committed n_s = 0.959 is coherent with the working f* ⇒ the C-L1 falsification claim stands as published, 0-free-parameter cleanliness intact. G-L2 closes. NEITHER outcome re-selects the functional.

**Functional-sensitivity classification** (lizzi domain): Δn_s = +0.000909 within the cutoff family is a **SCHEME-DEPENDENT** quantity at the value level (it is nonzero — √x and f* are distinct weightings), but **FUNCTIONAL-INDEPENDENT to within σ_budget** at the observable level — i.e. n_s is robust across the cutoff sub-family the framework actually uses. This is consistent with the S64 T12 within-cutoff-family spread (0.0012) and DISTINCT from the cross-family A13 spread (0.164, which crosses into zeta/anomaly where ε_H flips sign). The √x↔f* coherence is a within-cutoff-family result and does NOT extend to the sign-flipping zeta/anomaly families — those are excluded by the S67 FUNCTIONAL-SELECT red-tilt theorem, not by this coherence check.

**Constraint-map consequence** (solution-space reading, `epistemic-discipline.md`):

This **closes the G-L2 coherence gap**. The seed flagged that the framework committed pure √x to the falsifier surface (n_s = 0.959) while computing A_s/dynamics with f* — raising the worry that the COMMITTED and WORKING functionals give structurally different n_s the S103 commit erases. The result shows they do NOT: Δn_s = 0.216σ (like-for-like bare-tree) and 0.321σ (f* vs the committed 0.959 point-value) are both sub-σ. **The single-value n_s = 0.959 is NOT a misrepresentation of the framework's machinery** — it is faithful to within a third of the Planck error. C-L1 (the n_s-vs-ACT-DR6/SPT-3G tension at 2.7–5σ) is therefore NOT defused by a hidden functional ambiguity; the framework's red-tilt prediction is coherent across its own cutoff functionals and stands at full strength against the data. This narrows the C-L1 corridor: the n_s tension is a genuine substrate-vs-observation tension, not a functional-bookkeeping artifact.

**Downstream (fb_pair backward)**: feeds the n_s falsifier-surface row context — no {√x, f*} band needs publishing (the INFO/FAIL branch that would have required a band did NOT fire); the single-value 0.959 is confirmed coherent. Feeds **INV12-W4-1** (A_s wall-reading workshop) as the coherence-band context (n_s is single-valued, not a band, so the A_s discussion need not carry an n_s-band caveat). Dual-prior re-allocation: PASS (\|Δn_s\| ≤ 0.0042) → 0.9 mass to **Track A** (committed value coherent, C-L1 claim stands).

**Plan-vs-reality deviation** (`substrate-first-canonical-sourcing.md §(ii.B)`; honestly disclosed per `v3-closure-recovery.md` Class-1 boundary): plan §W1-3 `input_files` pins the D_K spectrum at `s84_spectrum_cache_L12_tau019.npz` — a **single-τ** cache (one `sector_evals` dict at τ=0.19). But the coherence observable n_s = 1−2ε_H requires the **τ-derivatives** of S(τ) (ε_H = S'²/(2S·S'')), which a single-τ slice CANNOT supply. The CANONICAL √x n_s pipeline (S65/S63/S62) uses the multi-τ `s36_sfull_tau_stabilization.npz` (7 τ values) — it is literally what produced `n_s_FW_sqrt_cutoff`. Resolution: S36 multi-τ cache is PRIMARY (it reproduces the canonical √x anchors bit-for-bit, confirming it IS the canonical machinery), and the S84 L12 single-τ cache is cited as a fold-slice consistency anchor (the f*/√x ratio at τ=0.19 agrees between the two caches to \|dev\| = 0.0e+00). The deviation is documented in the convention tag (`-S36-MULTITAU-PRIMARY`) and the `# plan-pin-deviation` companion row. No fabrication.

**Output Artifacts** (closure-verification checklist):
- Script `computations/investigation-12/inv12_w1_3_n_s_functional_coherence.py` — present (28027 bytes); contains `from canonical_constants import` (1 hit) and `print_verdict_payload` (2 hits) (verified by grep).
- Data `computations/investigation-12/inv12_w1_3_n_s_functional_coherence.npz` — present (10707 bytes): n_s(√x)/n_s(f*)/Δn_s, ε_H decomposition (incl. isolated Gaussian), S/S'/S'' moments per functional, footing-robustness (vs committed 0.959), cross-checks, profiles, dual-SHA.
- Plot `computations/investigation-12/inv12_w1_3_n_s_functional_coherence.png` — present (93776 bytes): (a) S_√ vs S_{f*} profiles on the same spectrum, (b) ε_H by functional (e^{-x} isolated ⇒ ε_H<0), (c) n_s coherence vs Planck 1σ band.
- Verdict line `computations/investigation-12/inv12_gate_verdicts.txt` — present; matches `^INV12-W1-3-N-S-FUNCTIONAL-COHERENCE:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) + 3 extra companion rows (regulator_pin, plan-pin-deviation, footing) present.
- `audit_sha256=59de5a1e3837dc35fd85c0c1abcfa52bb465324f99811ada49e753dac391f917`, `content_sha256=b00c9d30148850f499a859d58c09848dc525ddffe44f811439dc26cc6e9e5617`.

---

### §W1-4. INV12-W1-4-R1-SAME-REGULATOR-AUDIT

**Status**: COMPLETED
**Gate ID**: `INV12-W1-4-R1-SAME-REGULATOR-AUDIT`
**Trigger**: `[AUDIT]`
**Classification**: **GEOMETRIC**
**Agent**: `lizzi-spectral-functional-theorist` (gate_type **solo** → dispatched as positioned specialist, treated as compute; one-reasoning-thread provenance audit; emits a verdict line)
**Hypothesis**: the three inputs of R_1 = a_0·a_4/a_2² = 1.1287 are ALL ζ_D residues at their respective dimension-spectrum poles (s=4/3/2, n=8−2s) — NOT a mixed normalization where a_2 is silently the Gilkey 0.728235 coefficient (ratio ≈ 3812) — so the a_2^ζ ≡ a_2^SDW pin label does NOT corrupt R_1's FI status.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w1.md §W1-4`. Pairs with INV12-W2-2 (general a_n pole-audit) as convergence #3; gates the session-track HY2 label disambiguation.

**MCP Pre-Compute Audit**:
- `get_constant('a_0_FW_zeta')` → **6440.0**; source `S64-results + lizzi-signature-observable.md`; gate `S88-A-N-FW-CANONICALIZATION`; **non-superseded**. (ζ_D residue: a_0 = ζ_{D_K}(0) = Tr(1), mode count.)
- `get_constant('a_2_FW_zeta')` → **2776.165389**; source `S42 spectral zeta sum + S46 a_2 split`; gate `S88-A-N-FW-CANONICALIZATION`; **non-superseded**. (ζ_D residue: the spectral-zeta-SUM value = NUMERATOR of the S46 split a_2^ζ/a_2^SD = 2776.165389/0.728234972609 = 3812.18; the Gilkey 0.728 is the DENOMINATOR, a different number.)
- `get_constant('a_4_FW_zeta')` → **1350.7216**; source `s75_f_conv_spectral_output.txt:26 + baseline-findings-s66.md`; **non-superseded**. (ζ_D residue at s=2.)
- `trace_entity('R_1 Lizzi signature')` → eq_19571 (display): `R_1 = a_0·a_4/a_2² = 6440.0×1350.72/2776.165389² = 1.128653…` (Sage-exact); eq_19558: `1.128655`; the Lizzi observable identity `(m_H/v_EW)²·(Λ/M_Pl²) = R_1` is Sage-exact `42022400000000000/3723233945…`. **Confirms the canonical reproduction-target lineage (the eq_19571 "1.128653" 7-sig-fig print is itself a mis-rounding of the exact 1.1286545620 → 1.128655; see Results).**
- `search_knowledge('ZETA-NOT-PHYSICAL absolute a_n regulator artifact')` → **ZETA-NOT-PHYSICAL PROVEN theorem #24 (S75)**; "absolute a_n are scheme artifacts"; the FI ratio R_1 is the combination surviving all scheme choices; regulator-pin-discipline.md bare-a_n forbidden. **PRE-CONFIRMS the audit's premise (R_1 is FI by regulator-cancellation; absolute a_n NOT physical) — this gate VERIFIES the cancellation is realized at the constant-store level, NOT a re-derivation of ZETA-NOT-PHYSICAL.**

**Verdict**: **PASS** — `value='R1=1.1286546_regset=zeta_D_singleton_zeta=True_pole_map_ok=True_repro_canonical_1.128655=True_dlt=4.38e-07_cancel_exact=True_contam_OOM=7.2_alias=HARMLESS_ALIAS_plan_typo_1.128653_doc_patch'` scheme=ZETA convention=RATIO L_max=10 `audit_sha256=936b388433b5c4a4cb32682a8c7204522b11802d61160bdc3a23ec014f3d2b79` `content_sha256=5359f5e2013636ccd4f1ad0ecdbc289dd9ac5f564d3a5a4d1490c0f6a1c642a0` schema_version=S84+. **[AUDIT] set-membership — NO 3-tuple** (the gate is not a directional [SIGN] test).

**Results**:

*NUMBERS first.* The audit ran five set-membership / reproduction checks at the constant-definition level:

| Check | Result | Detail |
|:------|:-------|:-------|
| (1) regulator-set singleton {ζ_D} | **{zeta_D}** ✓ | all three moments are ζ_D residues; all three MCP-confirmed **non-superseded** |
| (2) dimension-spectrum pole assignment | **OK** ✓ | a_0@(s=4,n=0), a_2@(s=3,n=2), a_4@(s=2,n=4); each consistent with n = d−2s at d=8 (double-power convention) |
| (3) bit-for-bit R_1 reproduction | **PASS** ✓ | R_1 = **1.128654562** (Sage-exact `378202048000000000/335091055090500927`) vs canonical §2 **1.128655**: \|Δ\| = **4.380e-07 < 1e-6** |
| (4) regulator-cancellation identity | **EXACT** ✓ | `(c·a_0)(c·a_4)/(c·a_2)² = a_0·a_4/a_2²` for all test scalars c ∈ {0.137, 1, 7.4, 1e3, 2.5e-2}; max residual **4.44e-16** (FD floor; Sage `simplify_full` returns **0** exactly) |
| (5) Gilkey-contamination counterfactual | **EXCLUDED** ✓ | a_2 → Gilkey 0.728235 ⇒ R_1 = **1.640e7** (OOM **7.16**, meaningless) — the denominator demonstrably uses the ζ value, NOT the Gilkey coefficient |

**4-tuple**: `(value=R1=1.1286546_…, scheme=ZETA, convention=RATIO, L_max=10)`, regulator_pin = **a_n^{ζ}**.

***[AUDIT] substitution chain — the regulator-cancellation identity.*** R_1 is FUNCTIONAL-INVARIANT iff under a regulator change R → R′ each moment transforms as a_n → c·a_n with the **same** scalar c (the defining property of same-regulator residues). Then:

```
R_1′ = (c·a_0)(c·a_4) / (c·a_2)²  =  c²·a_0·a_4 / (c²·a_2²)  =  a_0·a_4/a_2²  =  R_1.
```

The c² from the numerator (a_0·a_4) exactly cancels the c² from the denominator (a_2²); R_1 is c-INVARIANT. Sage `(c*a0)*(c*a4)/(c*a2)^2 - a0*a4/a2^2 = 0` (verified exactly). **This cancellation requires all three moments drawn from the SAME regulator** — which checks (1)+(2) confirm (singleton {ζ_D}, matched poles). The Weyl-exponent identity α_0 + α_4 = 2·α_2 (lizzi-signature-observable.md §2) is the companion L-scaling cancellation (L^0); the same-regulator condition is the regulator-normalization cancellation. Both hold.

***Gilkey-contamination counterfactual.*** If a_2 in the denominator were silently the Gilkey a_2^SD = 0.728235 (the heat-kernel curvature-polynomial coefficient, a DIFFERENT normalization) while a_0, a_4 are ζ residues, the regulator would NOT cancel:

```
R_1^{contaminated} = 6440.0 × 1350.7216 / (0.728234972609)²  =  1.640e7   (OOM 7.16 — meaningless).
```

The audit confirms R_1 reproduces 1.128655 (not 1.64e7), so the denominator uses the ζ value `2776.165389`, same regulator as the numerator. The hazard is **excluded**.

***a_2^ζ ≡ a_2^SDW resolution: HARMLESS ALIAS.*** The pin `a_2_FW_zeta = 2776.165389` is the spectral-zeta-SUM value (S42), which equals the heat-kernel Seeley-DeWitt a_2 *moment* computed via DIRECT SPECTRAL SUM at the **same ζ_D regulator** — NOT the Gilkey closed-form coefficient 0.728. The "a_2^SDW" label refers to the **same number** (the mode-summed Seeley-DeWitt moment), reached by the same regulator; the Gilkey 0.728 is the perturbative curvature-polynomial coefficient on a DIFFERENT (per-unit-volume) normalization. The S46 split `a_2^ζ/a_2^SD = 2776.165389/0.728234972609 = 3812.18` is the conversion factor between the mode-summed moment and the curvature-polynomial coefficient — it is **not** evidence of a mixed normalization inside R_1, because R_1's denominator uses the mode-summed moment (a_2^ζ = a_2^SDW = 2776.165389) on every leg. **The label is a harmless alias (one regulator, two names); the Gilkey 0.728 never enters R_1's denominator.**

***Publication-precision note (the plan's "1.128653" target).*** The FW-zeta pins EXACTLY reproduce R_1 = **1.1286545620**, which rounds to **1.128655** at 7 sig figs — matching the registry §2 canonical (1.128655). The plan substitution-chain hardcodes the reproduction target as **1.128653**, which is a **7th-sig-fig mis-rounding of the same pins** (the registry §2 lineage value with a_2=2776.165, a_4=1350.722 ALSO yields 1.128655; eq_19571's "1.128653…" print is the same drop-a-digit slip). Per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"`, the verifier tolerance is anchored to the CORRECT canonical 1.128655 (\|Δ\|=4.38e-7<1e-6, PASS); tying the verdict to the typo'd 1.128653 would manufacture a FAIL (\|Δ\|=1.56e-6>1e-6) on a publication-precision artifact, masking the true **structural** PASS. The audit substance (same-regulator set-membership) is INDEPENDENT of the typo. The plan/registry "1.128653" → **1.128655** is a documentation patch (HY2), not a verdict-FAIL.

***Constraint-map consequence.*** **PASS → R_1 = 1.1287 is the genuine FI Lizzi signature** (the regulator cancels in a verified same-regulator ratio). The a_2^ζ ≡ a_2^SDW pin label is a harmless alias; R_1 is publication-safe as "the number on the cover". **C-L4/R-L2 close at the constant-definition level.** **HY2 becomes a label/doc cleanup** (disambiguate the a_2_FW_zeta comment so the SDW alias is explicitly the mode-summed-moment alias, NOT the Gilkey coefficient; correct the "1.128653" → "1.128655" reproduction target in the plan substitution-chain and eq_19571), **NOT a correction** — the lizzi-signature-observable registry stands as derived; **HY1 (FI/RD manifest) tags R_1 FI on this strength** (FI by both the Weyl-exponent identity α_0+α_4=2·α_2 AND the verified same-regulator condition). The FAIL branch (mixed regulator → R_1 ill-defined → HY2 MANDATORY → registry re-derivation) is **not** triggered. **Structural classification: R_1 same-regulator FI is FUNCTIONAL-INDEPENDENT (regulator-cancellation is realized; verified, not assumed).**

**Output Artifacts** (closure-verification checklist):
- **script** `computations/investigation-12/inv12_w1_4_r1_same_regulator_audit.py` — contains `from canonical_constants import` (Section 1) and `print_verdict_payload` (Section 7); `from canonical_constants import (a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta,)` ✓.
- **data** `computations/investigation-12/inv12_w1_4_r1_same_regulator_audit.npz` ✓ (regulator_set, R1_float, R1_exact_num/den, delta_vs_canonical, cancellation_exact, R1_contaminated, alias_resolution, verdict, dual-SHA).
- **plot** `computations/investigation-12/inv12_w1_4_r1_same_regulator_audit.png` ✓ (Panel A: three ζ_D moments + poles, Gilkey reference line; Panel B: R_1 reproduction + contamination counterfactual).
- **verdict_line** `computations/investigation-12/inv12_gate_verdicts.txt` — `INV12-W1-4-R1-SAME-REGULATOR-AUDIT: PASS …  audit_sha256=936b388433b5c4a4cb32682a8c7204522b11802d61160bdc3a23ec014f3d2b79 …` matches `^INV12-W1-4-R1-SAME-REGULATOR-AUDIT:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row + 3 detail rows (NO 3-tuple — [AUDIT] set-membership, per `schema_v2_3tuple_required: false`) ✓; audit_sha256 unique across the file (sig_5 ✓; distinct from W3-1 `7915262f…`, W1-1 `b5f27b2f…`).

---

### §W1-5. INV12-W1-5-KRAJEWSKI-TILT-CENSUS

**Status**: COMPLETED
**Gate ID**: `INV12-W1-5-KRAJEWSKI-TILT-CENSUS`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE**
**Agent**: `lizzi-spectral-functional-theorist` (carries connes-ncg context for the Krajewski-diagram enumeration)
**Hypothesis**: across the Krajewski-classified finite spectral triples, A_F = ℂ⊕ℍ⊕M_3(ℂ) is the UNIQUE SM-compatible finite geometry whose Seeley-DeWitt moment-velocities da_{2k}/dτ have the sign yielding RED tilt under an anomaly-forced functional — upgrading the functional from "cornered by elimination" (G-L1) to "forced by SM-spectrum ∧ red-tilt" (A-L2).
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w1.md §W1-5`. Leans on N7 (§VII.W-3 A_F SINGLETON, STAGE-3-PERMANENT) + the S67 W1-C anomaly-family-exclusion theorem.

**MCP Pre-Compute Audit**:
- `search_knowledge('Krajewski finite spectral triple classification')` → hit `lizzi-finite-infinite-vector-classification` registry (my own F_4 finite-vector class: zeta/SDW/cutoff/anomaly all members) + the A_F=ℂ⊕ℍ⊕M_3(ℂ) finite-triple equation set; no closure pre-empts the census.
- `search_knowledge('A_F singleton unique dim 50 NCG axioms Wedderburn W-3')` → **N7 (§VII.W-3, STAGE-3-PERMANENT, S88 W4a-17)**: A_F is the UNIQUE finite real NC algebra dim_ℝ≤50 satisfying 6 NCG axioms (Wedderburn-Artin enumeration 1/3,9). SM-compatible set is the singleton {A_F} BY THEOREM.
- `search_knowledge('da_2k dtau Seeley-DeWitt moment velocity sign red tilt epsilon_H')` → **CONSERVATION-HIERARCHY-TEST-67 (S67 W4-B, FAIL)**: "da_{2k}/dtau < 0 for all k≥1. 0/500k positive-weight samples" — the anomaly-family census was ALREADY swept exhaustively; ZERO red-admitting positive-weight triples. Also A13 (ε_H sign-reversal) + S67 critical exponent α_c=1.43.
- `search_knowledge('FUNCTIONAL-SELECT-67 anomaly red-tilt exclusion blue n_s')` → **FUNCTIONAL-SELECT-67 / Q28 / Window-7**: "S67 W1-C closed the anomaly family with a structural theorem (n_s > 1 for all φ > 0)". The anomaly family is BLUE-only on A_F.
- `get_constant('tau_fold')` → 0.19 (S12/S42, CONST-FREEZE-42, `s42_constants_snapshot.npz`). Bracketing caches at τ∈{0.18,0.20} straddle it.
- Direct npz read `s67_functional_select.npz`: canonical zeta velocities da_2/dτ=−875.622475, da_4/dτ=−609.178742 (both NEG) — the regulator-pin-correct (`a_{2k}^{ζ}`) moment velocities.
- **PRE-CLOSED status**: NOT closed, but the answer is STRUCTURALLY FORCED by N7 (SM-set={A_F}) ∧ S67 W4-B (A_F BLUE under anomaly). The census formalizes the joint constraint; the verdict was predictable from the registry (INFO), and the compute confirms it bit-for-bit.

**Verdict**: **INFO** (composite) — `card({SM-compatible ∧ red-tilt-under-anomaly}) = 0`. A_F is SM-forced (N7 singleton) but **BLUE-ONLY** under every anomaly-forced functional. 3-tuple: **sign=FAIL, magnitude=INFO, regime=VALID**.
- **value** = `card_SM_and_red=0_PASSval=1_n_SMcompat=1_n_redadmit=0_AF_blue_only=True_da2zeta=-875.62_da4zeta=-609.18_da6zeta=-353.44_all_zeta_NEG=True_powsum_POS=True_anomaly_posweight=0of500000_regpin=a2k_zeta_AL2_confirmed_boundary_red_sqrtx_non_anomaly`
- **4-tuple**: `(value=card=0, scheme=ANOMALY, convention=FINITE-GEOMETRY-CENSUS, L_max=10)`, regulator_pin `a_{2k}^{ζ}`.
- `audit_sha256=3ffa2da4c9e0d07dc5c0497f07edde36053116ddedd9758a288e8b490238b28e` `content_sha256=8622cd5733e9170f7754b623113b1bda8ade1d025417161e713d8a60e741d5bc` (supersedes the pre-helper-refactor line `5d33aeba…`; identical INFO physics, Option-A correction per `gate-verdicts.md`).

**Results**:

- **Census cardinality**: `|{SM-compatible}| = 1` ({A_F = ℂ⊕ℍ⊕M_3(ℂ)}, N7); `|{red-tilt-under-anomaly}| = 0` (∅); **`|{SM-compatible ∧ red-tilt}| = 0`** (vs the PASS-value 1). Exhaustive positive-weight anomaly scan on A_F: **0 / 500,000** red-admitting weights across 5 distributions (Exponential/Uniform/LogNormal/Gamma(0.1)/Gamma(10)) — reproducing the S67 W4-B 0/500k result.

- **[SIGN] substitution chain** (Sage-exact verified, `sage_eval`):
  ```
  Claim: "A_F is the UNIQUE SM-compatible geometry with da_{2k}/dτ of the sign
          yielding RED tilt under the anomaly functional S_anom = Σ c_{2k}(φ) a_{2k}."
  Step 1: c_{2k}(φ) > 0 ∀φ>0  (Andrianov-Lizzi 1103.0478/1001.2036; bosonic action
          DERIVED from fermionic anomaly cancellation — NOT postulated).
  Step 2: red tilt ⟺ n_s<1 ⟺ ε_H>0 ⟺ dS/dτ>0  (S67 tilt-from-action map).
  Step 3: A_F zeta moment velocities (S67 W4-B; regulator a_{2k}^{ζ}):
            da_2/dτ = −875.622475,  da_4/dτ = −609.178742,  da_6/dτ = −353.44  (ALL NEG)
          ⇒ dS_anom/dτ = Σ c_{2k}·(da_{2k}/dτ) < 0  (positive·negative)  ⇒ ε_H<0 ⇒ n_s>1 (BLUE).
  Step 4: finite-fiber factorization a_{2k}^{(M⁴×F_G)}(τ) = dim(H_{F_G})·a_{2k}^{base}(τ),
          dim(H_{F_G})>0 TAU-INDEPENDENT (τ acts on the SU(3) base, not the finite fiber)
          ⇒ sign(da_{2k}^{(G)}/dτ) = sign(da_{2k}^{base}/dτ) = NEGATIVE for EVERY G
          ⇒ the red-admitting set is EMPTY.
  Step 5 (DIRECTION): the PASS-as-stated (singleton {A_F} red-admitting) is NOT realized —
          A_F gives BLUE under the anomaly family, card=0≠1. sign_verdict = FAIL relative
          to PASS-as-stated; the structurally-correct reading is INFO (A_F SM-forced, BLUE-only).
  Conclusion: card({SM ∧ red}) = 0 ⇒ the framework's RED √x is NECESSARILY OUTSIDE the
          anomaly family (it lives in the non-perturbative branch-point / UV-dominance
          sector, α_c=1.43, S67 W4-B). A-L2's "non-arbitrary functional" credential stays
          UNEARNED; the anomaly route is CONFIRMED as a structural boundary, not a selection.
  ```

- **Per-geometry sign(da_{2k}/dτ at τ_fold) table** (under unit anomaly weights c_{2k}=1; dim(H_{F_G}) = finite-fiber Hilbert dim, TAU-INDEPENDENT; da_2^G = dim·da_2^{ζ,base}):

  | Finite geometry G | dim(H_{F_G}) | SM-compat (N7) | da_2^G/dτ | dS_anom/dτ | tilt | red-admit |
  |:------------------|:------------:|:--------------:|:----------|:-----------|:-----|:---------:|
  | **A_F = ℂ⊕ℍ⊕M_3(ℂ)** | 32 | **YES** | −2.802e4 | −5.882e4 | **BLUE** | **False** |
  | ℂ⊕ℂ | 4 | no | −3.502e3 | −7.353e3 | BLUE | False |
  | ℂ⊕ℍ | 8 | no | −7.005e3 | −1.471e4 | BLUE | False |
  | ℍ⊕M_3(ℂ) | 24 | no | −2.101e4 | −4.412e4 | BLUE | False |
  | M_2(ℂ)⊕M_3(ℂ) | 24 | no | −2.101e4 | −4.412e4 | BLUE | False |
  | ℂ⊕M_2(ℂ)⊕M_3(ℂ) | 28 | no | −2.452e4 | −5.147e4 | BLUE | False |
  | ℂ⊕ℍ⊕ℍ | 12 | no | −1.051e4 | −2.206e4 | BLUE | False |
  | ℂ⊕ℍ⊕M_2(ℂ) | 12 | no | −1.051e4 | −2.206e4 | BLUE | False |
  | M_3(ℂ) | 9 | no | −7.881e3 | −1.654e4 | BLUE | False |
  | ℂ⊕ℍ⊕M_4(ℂ) | 48 | no | −4.203e4 | −8.824e4 | BLUE | False |

  Every geometry: BLUE (dS_anom/dτ<0). The fiber dimension scales the magnitude but never flips the sign — the tilt sign is **functional-INDEPENDENT of the finite-fiber choice** within the anomaly family.

- **Regulator-class split (the load-bearing distinction; regulator-pin `a_{2k}^{ζ}`)**: the census reads the **zeta-regulated** Seeley-DeWitt residues a_{2k}^{ζ} = Res[Tr D^{−2s}; s=(d−2k)/2], which SHRINK with τ (da_{2k}^{ζ}/dτ<0). A regulator-class CONTRAST — the raw absolute power-sums Σ_j d_j|λ_j|^{2k} on the bracketing caches (τ∈{0.18,0.20}) — GROW with τ (d/dτ = +5.72e7, +1.74e9, +4.06e10; all POSITIVE). This is the OPPOSITE sign and is **NOT the anomaly functional's object**: it is the non-perturbative √x / Tr|D|^α UV-dominance sector (α_c=1.43, S67 W4-B) where the framework's red √x lives. Conflating the two is the SCHEMATIC-vs-regulator pathology (`regulator-pin-discipline.md`, `substrate-first-canonical-sourcing.md §(iv)`); the gate pins `a_{2k}^{ζ}` and reads SHRINK ⇒ BLUE. **FUNCTIONAL-INDEPENDENT** (the sign of dS_anom/dτ under any c_{2k}>0 is forced by da_{2k}^{ζ}/dτ<0); the MAGNITUDE is SCHEME-DEPENDENT (fiber dim, weight distribution).

- **Constraint-map consequence**: INFO → **A-L2 CONFIRMED as a structural boundary**. The geometry that gives the SM (A_F, N7) also forces BLUE under every anomaly-consistent functional. The framework's red-tilting √x is therefore NECESSARILY OUTSIDE the anomaly family — the "non-arbitrary functional" credential A-L2 hoped to earn from anomaly-consistency stays **UNEARNED**, and the census explains WHY (SM-spectrum ∧ anomaly-consistency ⇒ blue, not red). **G-L1 stays cornered-by-elimination** from the anomaly route; this CLOSES the speculative escape A-L2 flagged (the functional CANNOT be made anomaly-forced on A_F). Per the dual_prior discriminator: INFO → **0.85 mass to Track B** (anomaly route confirms the boundary; no selection). Feeds **INV12-W4-2** (SA-effective-action workshop) as the lizzi-side "anomaly-functional is excluded for the red tilt — the fix is NOT a different bosonic functional within the anomaly family" evidence.

- **Spectral-functional pluralism reading (Lizzi domain)**: this gate is a clean demonstration that the tilt SIGN is a property of the **regulator class**, not the geometry. Within the finite-vector F_4 class (zeta/SDW/cutoff/anomaly — all positive-moment), every SM-compatible geometry tilts BLUE. Red requires leaving F_4 for the non-perturbative branch-point class (√x, α<α_c=1.43). The choice of spectral functional is the physical degree of freedom that sets the tilt; A_F's geometry is silent on it.

**Output Artifacts** (closure-verification checklist):
- **Script** `computations/investigation-12/inv12_w1_5_krajewski_tilt_census.py` — EXISTS. `grep -c 'from canonical_constants import'` = **1**; `grep -c 'print_verdict_payload'` = **3** (both `must_contain` patterns present).
- **Data** `computations/investigation-12/inv12_w1_5_krajewski_tilt_census.npz` — EXISTS (zeta velocities, contrast power-sums, 10-row geometry table, census cardinality, input-pin SHAs).
- **Plot** `computations/investigation-12/inv12_w1_5_krajewski_tilt_census.png` — EXISTS (Panel 1: per-geometry dS_anom/dτ all-negative bars, A_F highlighted; Panel 2: regulator-class sign split zeta-NEG vs power-sum-POS).
- **Verdict line** at `computations/investigation-12/inv12_gate_verdicts.txt` — matches `^INV12-W1-5-KRAJEWSKI-TILT-CENSUS:.* audit_sha256=[a-f0-9]{64}` (latest non-superseded `audit_sha256=3ffa2da4…`); dual-SHA companion row present; **[SIGN] 3-tuple row present** (`sign_verdict=FAIL magnitude_verdict=INFO regime_verdict=VALID`); regulator_pin + composite-precedence + S67-anchor extra-rows present; `supersedes=5d33aeba…` Option-A correction documented.

---

## Wave 1 Synthesis (team-lead)

**Per-gate roll-up** (all 5 verified on disk; verdict file `computations/investigation-12/inv12_gate_verdicts.txt`):

| Gate | Verdict | Result | Constraint-map move |
|:-----|:--------|:-------|:--------------------|
| W1-1 MODULAR-FUNCTIONAL-EXTREMIZATION | **FAIL** | S_modular monotone through τ_fold (dS/dτ\|_fold=+0.7821, extremum off-fold at τ=0.171) | G-L1 modular-selection corridor CLOSED; modular weight joins the four failed S76 selection principles → Track B |
| W1-2 A-S-GGE-MODULAR-REFERENCE | **FAIL** | R_wall^GGE=2.4182 ≡ R_wall^BD; K_sub=1+2n_k ∈ [1.00002,1.00384] ≥ 1 (BD at infimum n_k=0) | A_s floor reference-state-INDEPENDENT (sign); CF23 confirmed NOT a BD-artifact → Track B 0.9 |
| W1-3 N-S-FUNCTIONAL-COHERENCE | **PASS** | Δn_s = 9.086e-4 ≪ σ-budget 0.0042 | committed √x coherent with f*; C-L1 n_s claim stands 0-free-param → Track A; NO band needed |
| W1-4 R1-SAME-REGULATOR-AUDIT | **PASS** | R_1=1.1286546 all-ζ_D singleton; Gilkey-contamination counterfactual 7.2 OOM away; cancellation exact | R_1 FI-valid; a_2^ζ≡a_2^SDW is a HARMLESS_ALIAS; caught+flagged plan typo (1.128653 → 1.1286546) |
| W1-5 KRAJEWSKI-TILT-CENSUS | **INFO** | card(SM ∧ red-under-anomaly)=0; A_F SM-forced but blue-only (all da_{2k}/dτ<0; 0/500k red-admit) | A-L2 anomaly-forced-red corridor CLOSED as a boundary; red √x necessarily non-anomaly → Track B 0.85 |

**Structural reading**: the spectral-functional spine resolved as a corridor-closing + self-consistency-confirming wave. Three gates close framework hopes cleanly (W1-1 modular-selection, W1-2 BD-artifact relief, W1-5 anomaly-forced red) and two confirm self-consistency (W1-3 n_s coherence, W1-4 R_1 regulator provenance). The high-leverage result is W1-2: the A_s 3.02× wall is **reference-state-independent in sign** (K_sub ≥ 1 forced by n_k=\|β_k\|²≥0), strengthening CF23 from "wall relative to BD" toward "wall, full stop." W1-1 + W1-2 are the same faithful-normal modular density ω seen in two lights (bulk-faithful; no area-clock; no A_s relief). Feeds: W1-2 → W4-1 (lizzi-side "NOT a BD-artifact") + W4-3; W1-1/W1-5 → W4-2 (modular/anomaly fixes scoped out).

**Effected In-Session** (non-math; investigation track is registry-quarantined per `gate-verdicts.md §"Investigation-Track Canonical Path"` — no session-track register mutation):
- [x] No in-track register edits — the W1-4-gated session-track items (HY1 FI/RD manifest authoring; HY2 a_2^ζ≡a_2^SDW label disambiguation, now licensed by W1-4 PASS = HARMLESS_ALIAS) route to session-promotion at `/rclab-investigate --investigation 12` close. Mirrored to housekeeping ledger §D.
- [x] Plan-typo observation (R_1 1.128653 → canonical 1.1286546, caught by W1-4) logged to housekeeping ledger §A — a doc-level correction, not a register value change.

## Carry-Forward Computations

No NEW compute carry-forward originates in Wave 1 — every gate closed in-session (2 PASS / 2 FAIL / 1 INFO), and the wave's outcomes feed the Wave-4 adjudication rather than queuing new computes. The session-track register items (HY1/HY2, gated on W1-4 PASS) are non-math reconciliations routed to session-promotion (housekeeping §D), not math CFs. The investigation's decisive forward computes are produced in Wave 4 (see W4 §"Carry-Forward Computations").

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-17 | A_s floor reference-dependence (CF23) | wall proven RELATIVE-TO-BD (S82 W2-4) | reference-state-INDEPENDENT in sign (W1-2 FAIL) | K_sub=1+2n_k≥1 forced; GGE-modular ref does not lift |
| 2026-06-17 | Modular-weight τ-selection (G-L1) | untested selection candidate | CLOSED (W1-1 FAIL, monotone through fold) | S_modular not extremized at τ_fold |
| 2026-06-17 | Anomaly-forced red tilt (A-L2) | speculative escape | CLOSED boundary (W1-5 INFO, A_F blue-only) | 0/500k geometries red-admit under anomaly |
| 2026-06-17 | n_s functional coherence (C-L1) | √x vs f* untested | CONFIRMED coherent (W1-3 PASS, Δn_s=9.1e-4) | within Planck σ-budget; 0-free-param stands |
| 2026-06-17 | R_1 regulator provenance (C-L4) | a_2^ζ≡a_2^SDW label ambiguity | RESOLVED HARMLESS_ALIAS (W1-4 PASS) | all-ζ_D singleton; Gilkey counterfactual 7.2 OOM |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict line |
|:-----|:-------|:------------|:------------|:------------|
| W1-1 | inv12_w1_1_modular_functional_extremization.py | ✓ | ✓ | FAIL (Option-A supersede ×1) |
| W1-2 | inv12_w1_2_a_s_gge_modular_reference.py | ✓ | ✓ | FAIL |
| W1-3 | inv12_w1_3_n_s_functional_coherence.py | ✓ | ✓ | PASS |
| W1-4 | inv12_w1_4_r1_same_regulator_audit.py | ✓ | ✓ | PASS |
| W1-5 | inv12_w1_5_krajewski_tilt_census.py | ✓ | ✓ | INFO (Option-A supersede ×1; composite-precedence row) |

All verdict lines at `computations/investigation-12/inv12_gate_verdicts.txt`; sig_5 unique across the file.
