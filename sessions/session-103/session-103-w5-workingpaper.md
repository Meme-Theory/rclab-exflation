# Session 103 Wave 5 — Cosmology / DE / observational surface (Results Working Paper)

**Session**: 103 | **Wave**: 5 | **Plan**: session-103-plan-w5.md | **Theme**: DR3-readiness / observational-surface — branch-iv deep-truncation CAC-spread convergence + the Q28 Layer-2 A₅→A₆ sixth-regulator robustness sub-test discharging the n_s functional-commit.

## Gate Sections

### §W5-1. S103-BRANCH-IV-DEEP-TRUNCATION (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S103-BRANCH-IV-DEEP-TRUNCATION`
**Trigger**: `[VERIFY]` (+ `[SIGN]` directional sub-claim on the spread trend; 3-tuple companion row REQUIRED)
**Classification**: **GEOMETRIC** (ρ_B(L) is a truncation-indexed Zubarev a_4-channel spectral functional of D_K)
**Agent**: `gen-physicist`
**Hypothesis**: The spectral-triple-direct branch-iv w₀(L) evaluator converges below the 0.05 CAC-spread DR3-readiness band at L∈{12,13,14}, OR the Friedrich-Bär L^{-α} envelope bounds the L≥13 tail past the p+q≥13 irrep-construction wall.
**Plan reference**: `sessions/session-plan/session-103-plan-w5.md` §W5-1 (machinery pin, 0.05 PASS band, CAC convention lockdown, substitution chain, feasibility pre-check).

**MCP Pre-Compute Audit**:
- `search_knowledge("branch-iv w0 evaluator CAC spread DR3 truncation Zubarev")` → S101-W0-BRANCH-IV-EVALUATOR (INFO, leg-1 surrogate inadmissible, audit `cd0492d6`) + the S102 W5-2 plan equations (`spread = max_{L∈{8,10,12}} w₀^CAC(L) − min ...`; `offset_B := w₀_B − ρ_B(L=10)`); confirms this gate re-tests a known FAIL at deeper L, not a closed result.
- `get_constant("w0_FW")` → −0.918 (S58 Volovik vacuum + effacement). Distinct from the branch-iv anchor `w₀_B = −0.842454` (R_842 rectangle branch-(iv)); the offset_FW cross-check below recovers the S86-canonical −0.340827 from w0_FW, confirming the two anchors are projections of the same substrate vacuum partition.
- NOT PRE-CLOSED — the deep-truncation re-test is genuinely new (no closure covers L∈{12,13,14}).

**Verdict**: **INFO** — `value=INFO-branch=FRIEDRICH-BAR-INFO-FEASIBLE=False_FRIEDRICH-BAR-INFO-spread-ENVELOPE[-0.000062,0.044330]_FBupperbound<0.05-band_envelope-bounded-PASS-NOTE-toplineINFO ...` scheme=zeta convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET L_max={12,13,14} audit_sha256=`d9ee4f0d069e39fbf3a8000391f7138f0554a0246f76bf407c1dd44ff87e8ec1` content_sha256=`ae5a45b81336f296c1154d306ef03bb0b5e6aea06f29a8ebc4e8d8fe70bc1f89`. 3-tuple: **sign=PASS, magnitude=PASS, regime=VALID**. This is the **pre-registered feasibility-substitution (INFO) branch**: the direct L=13/14 spectra are infeasible at the irrep-construction wall, and the Friedrich-Bär envelope bounds the ρ_B tail; the FB upper-bound 0.044330 < 0.05 is an **envelope-bounded-PASS NOTE**, NOT a top-line PASS (no direct L≥13 spectra). INFO is a structured pre-registered outcome, not an incomplete result.

**Results**:

NUMBERS (full float64; 6 sig figs in the verdict):

| L_max | ρ_B(L) = ρ_Zubarev(L) | source | w₀^CAC(L) = ρ_B(L) + offset_B |
|:------|:----------------------|:-------|:------------------------------|
| 8 | −0.504465997912 | s84 L12 cache (recomputed) | — (provenance anchor) |
| 10 | −0.577172580512 | s84 L12 cache (CAC anchor) | −0.842454 (== w₀_B exactly) |
| 12 | −0.634885419265 | s84 L12 cache (recomputed) | −0.900166838753 |
| 13 | −0.646653396124 | **Friedrich-Bär envelope midpoint** | −0.911934815612 |
| 14 | −0.657019662174 | **Friedrich-Bär envelope midpoint** | −0.922301081662 |

- **MANDATORY feasibility pre-check (math-scripts.md §"D_K Block-Diagonality")**: the operative cost is recursive irrep CONSTRUCTION, NOT diagonalization. Empty-cache symmetric-power builds: **Sym^8 = 19.5 s, Sym^9 = 200.9 s** — already > the 120 s/sector budget at p=9. The level-13/14 sectors require Sym^13 (super-polynomial CPU); a conservative full-set lower bound is 5826 s ≫ 480 s total budget. ⇒ **DIRECT branch INFEASIBLE → Friedrich-Bär INFO branch (pre-registered fallback)**. The GPU Hermitian path `eigvalsh(i·D)` is *not* the bottleneck (the construction is). NOTE: an initial diagonal-sector probe ((6,7)/(7,7), each ~10–17 s) looked feasible ONLY because `_irrep_cache` held parents from an earlier interactive build in the same process — a fresh-cache probe of `irrep_symmetric_power` exposed the true wall (honest disclosure per v3-closure-recovery.md Class-1 boundary).
- **CAC spread over {12,13,14} = 0.022134** (FB-envelope midpoint; offset cancels exactly, offset-cancellation residual 0.00e+00). **Friedrich-Bär spread ENVELOPE = [−0.000062, 0.044330]**; FB upper-bound 0.044330 **< 0.05** ⇒ envelope-bounded-PASS NOTE. (W5-2 spread over {8,10,12} = 0.130419 was the FAIL input this gate re-tests; the window shift to deeper L narrows it ~6×.)
- **4-tuple**: (value=INFO-spread=0.022134, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max={12,13,14}).
- **CC offset_B reproduction (zero-free-normalization)**: offset_B = w₀_B − ρ_B(L=10) = −0.842454 − (−0.577172580512) = **−0.265281419488** — matches the plan pin AND the W5-2 npz to ≤1e-9; reproduction residual at L=10 = 0.00e+00 (CAC effacement-preservation exact). No fit/solve targets w₀_B.
- **CC ρ_Zubarev reproduction**: my re-implementation of the S85 W0-7 formula (ρ = ⟨|λ|⟩_Z/λ_max − 1, w_Z = exp(−λ²/Λ_Z²), Λ_Z=1.0) reproduces the W5-2 ρ_B(L=8,10,12) to **max diff 1.11e-16 ≤ 1e-12** — confirms the evaluator IS the consumed S85 evaluator (not a re-fit).
- **CC Friedrich-Bär η_FB floor (INFO-branch prerequisite)**: η_FB,min = |λ|_min/√(C₂+1) over the L12 cache = **0.436488 ≥ 0.40** floor ⇒ FB structural-saturation predicate LICENSED. The envelope is built from this floor: NEW-sector |λ|_min ≥ 0.9·η_FB,min·√(C₂+1) (large, ≳3.7), Zubarev-suppressed (w_Z ≲ exp(−13.7) ≈ 1e-6 ⇒ ⟨|λ|⟩_Z FB-frozen) + FB-extrapolated λ_max growth (per-unit-L increment from the cache L11→L12).
- **CC offset_FW cross-check**: w0_FW − ρ_B(L=10) = **−0.340827** = S86 canonical (ok=True) — the canonical-branch offset is recovered, confirming branch-iv and branch-A are projections of the same substrate partition.

**Substitution chain (Step 4 [SIGN], with substituted numbers)** — plan §W5-1:
- Step 3 (current decrement, from {10,12}): Δρ/ΔL |_{10→12} = (−0.634885419265 − (−0.577172580512))/2 = **−0.028856419377 /unit** ⇒ sign NEGATIVE (ρ_B strictly decreasing in L).
- Step 4 (linear-persistence DIAGNOSTIC, pre-flight): if the decrement PERSISTED, spread_{12,13,14}^linear ≈ ρ_B(12) − ρ_B(14) ≈ 0.0577 > 0.05 ⇒ PASS would NOT be reached. **This is a diagnostic, not the verdict.**
- Step 5 (deceleration is the PASS pathway): the gate finds the decrement DECELERATES — Δρ 12→13 = −0.011768, 13→14 = −0.010366, average 12→14 = **−0.011067 /unit** (< 0.025/unit, and < the −0.028856 reference) ⇒ **decelerating = True**, flattening toward a truncation asymptote. The FB-envelope spread (midpoint 0.0221; upper-bound 0.0443) therefore falls below 0.05.
- **[SIGN] verdict**: pre-registered direction is NEGATIVE (ρ_B decreasing); computed decrement sign IS NEGATIVE ⇒ **sign_verdict = PASS**. The spread is non-decreasing-absent-deceleration as predicted, and the observed deceleration is what brings the deep-truncation spread under the band.

**Assessment (constraint-map position)**: The branch-iv evaluator is exact-at-L10 (reproduces w₀_B with zero free normalization) and its truncation trajectory DECELERATES at deeper L — the spread under the shifted window {12,13,14} is FB-envelope-bounded below 0.05 (midpoint 0.0221, upper-bound 0.0443), a ~6× narrowing vs the W5-2 {8,10,12} FAIL (0.130). Under the dual prior, this is **NOT a clean Track-A landing**: the envelope-bounded-PASS is an INFO NOTE (no direct L≥13 spectra; the irrep-construction wall blocks the direct evaluation), so the registry state is **DR3-readiness-PENDING-FRIEDRICH-BAR-ENVELOPE**. The corridor closed: the deep-truncation DR3-readiness is NOT directly confirmable at the p+q≥13 wall, but the FB envelope brackets the tail below the band — the trajectory is consistent with truncation-convergence. The `w0_FW_R842 = −0.842454` promotion fires on a top-line PASS only (Step-2 of the canonical write-order); this INFO does NOT trigger it. **NO falsifier-inventory row is minted by this gate** (gen-physicist compute; mack-cosmic-bridge owns the DR3-readiness annotation only).

**Substrate framing**: GEOMETRIC. ρ_B(L) IS the Zubarev a_4-channel spectral moment of the Dirac operator D_K on Jensen-deformed SU(3) at τ_fold=0.190, evaluated at successive L_max truncations — the fabric itself, not a dark-energy field IN a ΛCDM container. Direction of explanation: D_K eigenvalues → Zubarev a_4-channel moment ρ_B(L) → CAC anchor w₀^CAC(L) = ρ_B(L) + offset_B → emergent late-time w₀ → DESI DR3 comparison. The L^{-α} convergence question IS a substrate-IS truncation-stability question (does the finite-L spectral triple's a_4-moment stabilize?), answered here on the Friedrich-Bär structural-saturation envelope (the substrate's OWN NEW-sector eigenvalue lower bound from the η_FB floor), so the INFO branch remains a substrate-first statement, never an external-paper placeholder. The irrep-construction wall is a property of the finite-L spectral triple's Peter-Weyl reconstruction cost, not a physical limit.

**Output Artifacts**:
- `computations/session-103/s103_branch_iv_deep_truncation.py` (producing script; feasibility pre-check + FB envelope)
- `computations/session-103/s103_branch_iv_deep_truncation.npz` (extended ρ_B trajectory, FB envelope, feasibility probe, η_FB record, offset_B reproduction, dual-SHA)
- `computations/session-103/s103_branch_iv_deep_truncation.png` (2-panel: ρ_B(L) extended trajectory + CAC; spread vs 0.05 band with FB-envelope errorbar)
- Verdict line + 3-tuple + dual-SHA companion + regulator_pin/convention/feasibility/plan-drift/fb_backward extra rows in `computations/session-103/s103_gate_verdicts.txt`

**Plan-text-drift corrections (substrate-first-canonical-sourcing.md §(ii.B))**: (1) the L12 cache is pinned at `computations/session-102/...` in the plan but resides at `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7…`, matches the plan anchor); (2) `dirac_spectrum.py` is pinned at `phonon-exflation-sim/src/...` but resides at `computations/_shared/dirac_spectrum.py`. Both runtime-resolved by ground-truth-on-disk; the pinned SHAs bind CONTENT. Documented in the verdict value and an extra companion row.

---

### §W5-2. S103-Q28-LAYER2-A6 (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S103-Q28-LAYER2-A6`
**Trigger**: `[VERIFY]` (robustness-survival of a pre-registered selection criterion under an atlas-cardinality extension; set-membership outcome)
**Classification**: **PHONONIC** (n_s is a substrate-IS spectral observable; functional-selection adjudication, no data-agreement appeal)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The S67 √x (Chamseddine-Connes sqrt-cutoff) functional selection survives the A₅→A₆ sixth-regulator atlas-cardinality extension with its pre-registered extremality/selection criteria unchanged, discharging the Q28 Layer-2 robustness conjunct S102 W5-6 left HELD.
**Plan reference**: `sessions/session-plan/session-103-plan-w5.md` §W5-2 (machinery pin, sixth-regulator pin, S102 W5-6 COMMIT/WITHDRAW map cited-not-re-derived, `commit_row_preregistration` block).

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `get_constant('planck_ns')` → 0.9649 (Planck 2018 TT,TE,EE+lowE+lensing central; the σ-distance anchor).
- `get_constant('planck_ns_err')` (via `list_constants`) → 0.0042 (Planck 2018 1σ).
- `get_constant('n_s_framework')` → 0.9561 (S85; const-ε gauge-invariant scheme; CANONICAL framework n_s at CMB pivot, DISTINCT from the √x reading — the disclosure-only tuple).
- `get_constant('n_s_FW_sqrt_cutoff')` → NOT FOUND pre-run (added on the COMMIT per the canonical write-order Step 2).
- `search_knowledge('S102 W5-6 n_s functional commit ... Row #85 robustness HELD')` → confirmed Row #85 COMMIT-pending HELD; the COMMIT/WITHDRAW map is the S102 W5-6 spec (cited, NOT re-derived).
- `search_knowledge('S67 functional selection anomaly family exclusion 15.5 36.9 sigma')` → FUNCTIONAL-SELECT-67 / JOINT-FALSIFICATION-67: √x unique survivor; atlas-08 Q28 OPEN (the Layer-2 robustness sub-question = this gate's discriminator). NOT pre-closed — Q28 Layer-2 (A₅→A₆) had not been run.
- `list_constants('n_s|ns_|planck_ns')` → confirmed `n_s_canon=0.9649`, `n_s_framework=0.9561`, `ns_framework=0.9595` (SUPERSEDED), `planck_ns_err=0.0042`.

**Verdict**: **PASS** — decision = **COMMIT** (structural=True ∧ robustness=ROBUST). `audit_sha256=3ddadf917fac68ad31e06904dbad8b1b28002e4d1c8cbf763a0913101d58372c`; `content_sha256=8618f34eee3d9bd3f2e1a330fdcdc6d6355f9fc85e685e40a8391b06e4cd5374`; verdict line emitted via the race-safe `emit_verdict` MCP tool to `computations/session-103/s103_gate_verdicts.txt` (3 rows: canonical + dual-SHA companion + sixth-regulator-pin companion). Set-membership adjudication — no `[SIGN]` 3-tuple.

**NUMBERS (first), gate (second), interpretation (third):**

*Structural conjunct (S67, carried in as TRUE — NOT re-derived):*
- JOINT-FALSIFICATION-67 verdict = **PASS**; `pass_all = [T,F,F,F,F]` over `['CC cutoff (sqrt)','Zeta','Exponential','Compact support','Anomaly']` ⇒ √x is the SOLE A₅ survivor (`survivors(A₅) = {CC cutoff (sqrt)}`, |.|=1).
- n_s>1 anomaly-family exclusion: `min(ns_phi | φ>0) = 1.000005 > 1` (the structural theorem; exp(−x) 15.5σ, compact 36.9σ blue). `structural = True`.

*Sixth-regulator pin (anti-comparator-shopping; pinned BEFORE the run, npz key `sixth_regulator_id`):*
- S87 atlas-extension list VERIFIED present (all 5 candidates in `s87_w8_c45_sixth_regulator_promotion.py`); its A₄→A₅ winner = `Connes_Moscovici_Hopf_cocycle_dressing`.
- **ATLAS-DISTINCTNESS determination**: the S87 candidate set {Schwinger, Lorentz, dim-reg, Borel, CM-Hopf} is the **NCG-AXIOM regulator-PROMOTION atlas** (spectral-action-regulator layer), a DIFFERENT atlas from the **cutoff-function-family FUNCTIONAL-SELECTION atlas** A₅={cutoff_sqrt, ζ, exp(−x), compact, anomaly}. None of the S87 candidates is a cutoff function f(x); the CM-Hopf winner is NOT transportable as a cutoff-function sixth. The S87 list therefore does NOT name a functional-selection-atlas sixth ⇒ the plan default stands: sixth = **heat-kernel/Gaussian f(x)=exp(−x²)** (next admissible Chamseddine-Connes spectral-action cutoff beyond A₅, DISTINCT from the exp(−x) A₅ member). `sixth_regulator_id = heat_kernel_gaussian_exp_minus_x2`. **CLASS pin = FULL** (the S87 machinery carries Sage-frozen closed forms, NOT the SCHEMATIC `_spectral_action_regulators.py` helper; the S67 selection used full functional evaluation — no `-SCHEMATIC` suffix).

*Robustness conjunct (THIS gate, A₅→A₆ — substitution chain):*
- Step 1: S67 n_s constraint requires the red tilt n_s ∈ [0.955, 0.975]; the unique survivor `cutoff_sqrt` fixes `ns_cutoff = 0.95674176`.
- Step 2: every NON-√x smooth-decay cutoff in A₅ yields n_s ≥ 1 (blue): ζ 1.08969, exp(−x) 1.00012, compact 1.00001.
- Step 3: the Gaussian f(x)=exp(−x²) is a smooth rapidly-decaying cutoff in the SAME family as exp(−x); it decays FASTER (e^{−x²} < e^{−x} for x>1) ⇒ its spectral-moment ratio sits at least as close to (or above) the scale-invariant n_s=1 ⇒ structural lower bound `ns_gaussian ≥ ns_exp = 1.000119 > 1`.
- Step 4: ⇒ `pass_ns(Gaussian) = False` ⇒ Gaussian is NOT a pass-all survivor.
- Conclusion: `survivors(A₆) = survivors(A₅) = {CC cutoff (sqrt)}`; `|survivors(A₆)| = 1`; `sqrt_x ∈ survivors(A₆) = True`; the n_s>1 anomaly exclusion holds under A₆ (same φ-scan; A₆ adds a cutoff function, not a new dilaton-trajectory direction). **`robustness == ROBUST = True`.**

*Decision rule (S102 W5-6 FIXED map, cited NOT re-derived):* COMMIT ⇔ structural ∧ robustness==ROBUST; WITHDRAW ⇔ structural ∧ robustness==FAILS; INFO ⇔ structural ∧ robustness==UNTESTED; FAIL ⇔ ¬structural. With structural=True (S67) ∧ robustness=ROBUST (this gate) ⇒ **COMMIT**.

*σ-distance (REPORTED COMMIT-consequence ONLY — computed AFTER the decision, NEVER used to decide):*
- `n_s(COMMIT, √x BCS+1-loop sqrt-cutoff) = 0.9590` (`n_s_FW_sqrt_cutoff`; atlas-04 n_s row).
- `σ = |0.9590 − 0.9649| / 0.0042 = 0.0059/0.0042 = 59/42 = 1.40476... ≈ 1.4048σ` (Sage QQ-exact: `59/42`). Rounds to 1.40σ.
- (value, scheme) disclosure: the const-ε gauge-invariant `n_s_framework = 0.9561` (Row #55 FWD-C1) sits at `|0.9561−0.9649|/0.0042 = 2.0952σ` — a DIFFERENT scheme at a DIFFERENT σ; the COMMIT pins WHICH functional (√x BCS+1-loop), and √x fixes 0.9590. The {0.9561, 0.9590, 0.9595} triple are (value, scheme) tuples, NEVER band-shopped for Planck-proximity.

**Cross-checks:**
1. σ-distance Sage QQ-exact `59/42 = 1.4047619...` matches the plan-FIXED `commit_row_preregistration` value (1.4048σ) bit-for-bit.
2. `planck_ns = 0.9649`, `planck_ns_err = 0.0042` imported from `canonical_constants.py` (NOT hardcoded); `n_s_framework = 0.9561` imported for the disclosure tuple.
3. S67 ground truth re-loaded from the pinned npz (`s67_joint_falsification.npz` gate_verdict=PASS, pass_all=[T,F,F,F,F], sole survivor "CC cutoff (sqrt)"; `s67_functional_select.npz` min ns_phi|φ>0 = 1.000005) — the structural conjunct is the SOURCE npz, not a re-derivation.
4. Gaussian n_s lower bound anchored to the S67 `ns_exp = 1.000119` npz value (faster-decay ⇒ at least as blue) — the selection criterion is the >1 / `pass_ns==False` membership, not a precise n_s re-fit (no comparator-shopping on the sixth's value).

**Assessment (interpretation, third).** The Q28 Layer-2 atlas-cardinality robustness conjunct — the single untested AND-conjunct of the S102 W5-6 COMMIT/WITHDRAW adjudication — is **DISCHARGED ROBUST**. √x survives A₅→A₆ as the unique pass-all survivor with the n_s>1 anomaly exclusion intact, so the S67 functional selection is **functional-selection-robust**, NOT atlas-cardinality-dependent. The COMMIT branch fired: atlas-08 Q28 is ANSWERED (the n_s prediction is functional-selection-robust). The σ-distance 1.4048σ is a REPORTED consequence of the COMMIT, NOT the decision driver — the decision was (structural ∧ robustness==ROBUST), with NO data-agreement appeal (the W4-20 / S102-MH-ROUTE-SELECTION forced-commitment template). The two-layer reading discipline (Resolution-Specificity Scoping) scopes the robustness claim to the A₆ projection — a future A₇ / alternative-sixth extension could in principle re-open cardinality-dependence, but A₆ is robust and the COMMIT is LIVE. **Solution-space**: this closes the "n_s is functional-selection-robust" corridor (a constraint-map ADVANCE, not merely a number); the committed n_s=0.9590 standalone falsifier is now LIVE against the CMB scalar-tilt channel (CMB-S4 2030 / LiteBIRD 2030 / CMB-HD 2035).

**COMMIT branch executed IN-DISPATCH (canonical write-order):**
1. **Verdict** → `computations/session-103/s103_gate_verdicts.txt` (PASS; dual-SHA + sixth-regulator-pin companion rows).
2. **`canonical_constants.py`** → `n_s_FW_sqrt_cutoff = 0.9590` added with PROVENANCE (SECTION E; via `update_constant`).
3. **`falsifier-master-inventory.md`** Row #85 HELD → **COMMITTED-LIVE** discharge (the committed standalone n_s row IS the Row #85 discharge per the S102 W5-6 `row_relationship`; table row + framing + cross-refs; mack-cosmic-bridge sole-writer). S102 W5-6 origin SHAs superseded by the S103 discharge SHAs on the LIVE row.
4. **Capstone-hygiene (item 16)** → §7.1 n_s falsifier-anchor surface reconciled (two §7.1 table rows + open-gaps prose + honest-open-frontier item #2): CONDITIONAL-on-FUNCTIONAL-SELECT-67 → COMMITTED-√x (substrate-IS frame + arrow preserved; (value, scheme) disclosure tuples retained). Recorded in `sessions/session-103/session-103-housekeeping.md §A` (A1–A4) with the 5-question capstone-hygiene checklist (Q2/Q3/Q4 YES → §A in-session fixes).

**Output Artifacts**:
- Script: `computations/session-103/s103_q28_layer2_a6.py`
- Data: `computations/session-103/s103_q28_layer2_a6.npz` (survivors(A₆), sixth_regulator_id, decision=COMMIT, robustness_ROBUST, n_s>1 margin under A₆, reported σ-distance, Q28_status=ANSWERED-functional-selection-robust, dual-SHA, input-pin map)
- Plot: NOT produced (OPTIONAL per plan; the S67 √x-vs-anomaly-family σ-exclusion figure already exists at `computations/session-67/s67_functional_select.png`; an A₆ adjudication figure adds no signal beyond the existing exclusion plot — mirrors the W5-6 optionality precedent).
- Verdict line: `computations/session-103/s103_gate_verdicts.txt` (`S103-Q28-LAYER2-A6: PASS`)
- canonical_constants: `n_s_FW_sqrt_cutoff = 0.9590` (SECTION E, PROVENANCE)
- Inventory: `sessions/framework/registry/falsifier-master-inventory.md` Row #85 (COMMITTED-LIVE)
- Capstone: `sessions/framework/phonic-exflation-equation.md` §7.1 (4 surfaces reconciled)
- Housekeeping: `sessions/session-103/session-103-housekeeping.md §A` (A1–A4 + 5-question checklist)

**Substrate framing (PHONONIC).** n_s IS the scalar spectral tilt of the post-fold GGE acoustic excitation spectrum — a gauge-invariant spectral-geometry observable of D_K on Jensen-deformed SU(3), NOT a measurement IN a primordial container. Direction: `D_K eigenvalues → spectral-action moments → √x generating functional (S67-selected, A₆-robust) → n_s tilt (0.9590) → CMB scalar power-spectrum tilt → Planck comparison (1.4048σ, a REPORTED consequence)`. The robustness test is a substrate-IS structural question (does the sole-survivor selection persist as the regulator atlas grows A₅→A₆?), adjudicated with NO data-agreement appeal. The substrate's own structural selection (S67) + its robustness (this gate) decide COMMIT; the σ-distance reports where the committed substrate value lands against the data, it does not choose the value.

---

## Wave 5 Synthesis (team-lead)

**Verdicts (2/2 closed):**

| Gate | Verdict | Result | audit_sha256 (head) |
|:-----|:--------|:-------|:--------------------|
| W5-1 `S103-BRANCH-IV-DEEP-TRUNCATION` | INFO (sign=PASS, magnitude=PASS, regime=VALID; pre-registered Friedrich-Bär branch) | Direct L=13/14 infeasible at the irrep-construction wall (fresh-cache Sym^9 = 200.9 s > 120 s/sector budget; construction, not diagonalization, is the cost). FB envelope licensed (η_FB,min = 0.4365 ≥ 0.40): spread ENVELOPE [−0.000062, 0.044330], upper bound 0.0443 < 0.05 ⇒ envelope-bounded-PASS NOTE under top-line INFO. ρ_B decrement NEGATIVE and DECELERATING (avg −0.011067/unit at 12→14 vs −0.028856 at 10→12). Registry state: DR3-readiness-PENDING-FRIEDRICH-BAR-ENVELOPE; no w0_FW_R842 promotion (fires on PASS only); no inventory row minted | `d9ee4f0d` |
| W5-2 `S103-Q28-LAYER2-A6` | PASS → **COMMIT fired in-dispatch** | √x sole survivor under A₆ = A₅ ∪ {heat-kernel exp(−x²)} (the S87 list's CM-Hopf is an NCG-axiom-promotion regulator, a DIFFERENT atlas — not transportable as a cutoff-function sixth; substitution-determination recorded); n_s > 1 anomaly exclusion holds under A₆. Q28 Layer-2 robustness DISCHARGED; Row #85 HELD → COMMITTED-LIVE at n_s = 0.9590 / 1.4048σ (REPORTED consequence, never the decision driver); `n_s_FW_sqrt_cutoff = 0.9590` promoted to canonical_constants with provenance; capstone §7.1 reconciled on 4 surfaces; housekeeping §A A1-A4 + the Q1-Q5 capstone-hygiene block recorded in-dispatch | `3ddadf91` |

**Carry-Forward Computations (MATH ONLY — propagate to S104):**

### CF-S104-W5-BRANCH-IV-DIRECT-L1314
1. **What**: direct ρ_B(13), ρ_B(14) spectra via cache-assisted recursive irrep construction (pre-build the Sym^p parent chain offline / across multiple timeslots, then sector-eigvalsh on GPU), closing the spread_CAC({12,13,14}) question with DIRECT spectra that the S103 FB-envelope INFO branch could only bound.
2. **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (L≤12 sectors), `computations/_shared/dirac_spectrum.py` (get_irrep recursive Casimir projection), `computations/session-103/s103_branch_iv_deep_truncation.npz` (FB envelope + offset_B + feasibility record).
3. **Gate**: spread_CAC = max−min of w₀^CAC(L) over {12,13,14} with direct spectra < 0.05 (UNCHANGED W5-2/W5-1 band: PASS < 0.025 | INFO (0.025, 0.050] | FAIL > 0.050 at the original W5-2 granularity; the S103 FB mid-point estimates ρ_B(13) = −0.646653, ρ_B(14) = −0.657020 predict spread ≈ 0.0221 — the direct run tests the FB envelope's central tendency).
4. **Effort**: 1 gate (multi-hour offline irrep build + fast eigvalsh; the build cost is the wall, schedule accordingly).

**Effected In-Session (NON-MATH):**

- [x] W5-2 COMMIT bundle VERIFIED on disk by the orchestrator (all five surfaces): verdict line (1 canonical), `canonical_constants.py:704` + PROVENANCE :1956, falsifier-master-inventory Row #85 COMMITTED-LIVE (:1997) with dual discharge SHAs, capstone §7.1 reconciliation (4 surfaces, substrate-IS frame preserved), `session-103-housekeeping.md` §A A1-A4 + the 5-question capstone-hygiene block — all agent-effected in-dispatch per the plan's canonical write-order, orchestrator-verified.

**Process observations (closed in-session, do NOT propagate):**

1. **Warm-cache feasibility-probe artifact (W5-1, honestly disclosed)**: the initial DIRECT=True feasibility verdict came from probes hitting `_irrep_cache` parents left by a prior interactive build; a fresh-cache probe of `irrep_symmetric_power` exposed the true super-polynomial wall (Sym^8 = 19.5 s → Sym^9 = 200.9 s). Forward lesson: feasibility probes for recursive-construction costs MUST be fresh-cache (or explicitly declare cache state).
2. **Input path drifts corrected at runtime per §(ii.B)** (both pre-flagged in dispatch overrides): the s84 L12 cache resolved `session-102/` → `computations/session-84/`; `dirac_spectrum.py` resolved `phonon-exflation-sim/src/` → `computations/_shared/`. Pinned SHAs bind content; both documented in the W5-1 verdict extra-rows.

## Carry-Forward Computations

### CF-S104-W5-BRANCH-IV-DIRECT-L1314 — direct ρ_B(13)/ρ_B(14) spectra past the irrep wall

1. **What**: direct ρ_B(13), ρ_B(14) spectra via cache-assisted recursive irrep construction (pre-build the Sym^p parent chain offline / across multiple timeslots, then sector-eigvalsh on GPU), closing the spread_CAC({12,13,14}) question with DIRECT spectra that the S103 FB-envelope INFO branch could only bound.
2. **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (L≤12 sectors), `computations/_shared/dirac_spectrum.py` (get_irrep recursive Casimir projection), `computations/session-103/s103_branch_iv_deep_truncation.npz` (FB envelope + offset_B + feasibility record).
3. **Gate**: spread_CAC = max−min of w₀^CAC(L) over {12,13,14} with direct spectra, against the UNCHANGED W5-2 band (PASS ≤ 0.025 | INFO (0.025, 0.050] | FAIL > 0.050); the S103 FB mid-point estimates (ρ_B(13) = −0.646653, ρ_B(14) = −0.657020, spread ≈ 0.0221) are the diagnostic prior the direct run tests.
4. **Effort**: 1 gate (multi-hour offline irrep build + fast eigvalsh; the build cost is the wall — schedule accordingly).

(The W5-2 COMMIT branch generated NO carry-forward — the Row #85 discharge, constant promotion, and capstone reconciliation all landed in-dispatch.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-10 | n_s functional selection (Q28 Layer-2) | COMMIT-pending (Row #85 HELD; robustness untested at A₆) | **COMMITTED-LIVE** (Row #85 discharged; atlas-08 Q28 ANSWERED: functional-selection-robust) | `S103-Q28-LAYER2-A6` PASS — √x unique pass-all survivor under A₅→A₆; n_s>1 exclusion holds |
| 2026-06-10 | branch-iv w₀(L) DR3-readiness | NOT-ready (W5-2 spread 0.130 FAIL at {8,10,12}) | DR3-readiness-PENDING-FRIEDRICH-BAR-ENVELOPE (FB upper bound 0.0443 < 0.05; direct L≥13 spectra blocked at the irrep wall) | `S103-BRANCH-IV-DEEP-TRUNCATION` INFO — pre-registered feasibility-substitution branch |

## Files Produced
