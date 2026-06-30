# Investigation 5 Wave 3 — Cross-Vantage Joints (a₄ truncation / two-effective-actions / Higgs-residual) (Results Working Paper)

**Investigation**: 5 | **Wave**: 3 | **Plan**: investigation-5-plan-w3.md | **Theme**: spectral-geometer's heat-kernel adjudication of the two joints where all three investigation-1 surveys converge — the un-protected a₄ L_max-tail, the spectral-action-as-free-energy adversarial workshop, and the three-vantage Higgs-residual synthesis.

This wave is **MIXED**: 3 type-distinct gates — 1 `compute` (INV5-W3-1) + 1 `workshop` (INV5-W3-2) + 1 `review` (INV5-W3-3). The **closure semantics differ by `gate_type`** per `gate-verdicts.md §"Investigation-Track Canonical Path"`:

- **INV5-W3-1 (`compute`)** closes on a **verdict line** (`emit_verdict(session=5, track="investigation", ...)` → `computations/investigation-5/inv5_gate_verdicts.txt`) + dual-SHA companion row + a `[SIGN]` 3-tuple companion row, PLUS its WP section. It is the ONLY gate of the wave that emits a verdict line.
- **INV5-W3-2 (`workshop`)** and **INV5-W3-3 (`review`)** close by **artifact-existence-with-content** — their deliverable is a markdown document, NOT a numerical verdict; they emit **NO verdict line** (the same closure semantic as a METHODOLOGY-class wave per `wave-classification.md §M1`). A `landed`/`not-landed` outcome, NOT a substrate-physics PASS/FAIL: a missing-section `not-landed` remediates by re-dispatching the gate, not a numerical re-run.

## Gate Sections

### §W3-1. INV5-W3-1 (compute — spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV5-W3-1`
**Gate type**: `compute` (one subagent runs the producing script; closes on a VERDICT LINE + WP section)
**Trigger**: `[SIGN]` (directional prediction: the un-protected a₄ truncation tail DECREASES with L_max toward the continuum)
**Classification**: **GEOMETRIC** (a₄ is the fourth Seeley-DeWitt coefficient of the heat trace `Tr exp(−t D_K²)` — a spectral moment of D_K, the fabric's own spectral content at τ_fold, not an excitation of it)
**Agent**: `spectral-geometer`
**Hypothesis**: The un-protected (extensive) fourth Seeley-DeWitt coefficient a₄ of D_K² at τ_fold, scanned on the Peter-Weyl truncation axis max_pq_sum (= L_max) ∈ {3,4,5,(6)}, has a truncation tail that is monotone-DECREASING toward a continuum limit, with the L_max=3→6 tail-fraction matching the +5.36% m_H residual — i.e. the m_H +5.36% / 38.5σ miss IS the a₄ extensive truncation tail at L_sat≈6 (RESOLVABLE), NOT a physical floor.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w3.md` §W3-1 (machinery pin, two-part PASS-truncation/INFO-physical threshold, substitution chain source).

**MCP Pre-Compute Audit** (queries run BEFORE writing the script; NOT pre-closed — this is the first landing of INV5-W3-1, and the result is structurally pre-figured by the R-Protection theorem, see below):

- `search_knowledge("a_4 Seeley-DeWitt coefficient L_max convergence truncation")` → returns `a_4(fold)=1350.72`, `a_2(fold)=2776.17` (baseline-findings-s66); critical hit **session-60-bap-collab**: "The raw PW spectral sum Tr(|D_K|^n) is NOT the Seeley-DeWitt coefficient a_n. The former diverges; the latter is a finite curvature integral. This distinction was invisible at L ≤ [small]." `s95 TES-R1-FI-TRUNCATION-ROBUST` = FAIL (a related FI-ratio truncation gate).
- `search_knowledge("R-Protection theorem extensive coefficient a_4 multiset {8,4} unbalanced")` → `alpha_net = d+r+k = 8+2+2 = 12 for a_2 (R-fragile/extensive)`; confirms individual a_k are L_max-FRAGILE/EXTENSIVE, only the ratios R_n are R-protected.
- `search_knowledge("m_H Higgs +5.36% residual KK threshold 131.8 a_4 tail")` → `m_H_FW_KK_threshold=131.8`, `m_H_obs=125.1`, `r_KK = 67/1251 = +0.0535571` (Sage-exact +5.356%); `a_4_FW_zeta=1350.7216` = YM+Higgs-quartic moment.
- `get_constant("a_4_FW_zeta")` → **1350.7216** (S75; zeta-regulated 4th SD coeff of D_K² at τ_fold). `get_constant("a_2_FW_zeta")` → 2776.165389. `get_constant("tau_fold")` → **0.19** (CONST-FREEZE-42).
- `trace_entity("R-Protection")` → gates `S84-R-PROTECTION-K-AUDIT` (PASS, ratio-level), `S86-R-PROTECTION-MELLIN-CRITERION` (FAIL); confirms R-protection lives at the *ratio* layer, NOT the individual-coefficient layer.
- Spectral-geometer memory **Heat-Kernel Validity Tiers (Tier 2)** + **R-Protection theorem S76**: the extracted heat-trace t²-coefficient (the `a_4_FW_zeta=1350.72` lineage) is the EXTENSIVE / UV-dominated object with Weyl exponent `α_4 = d+r+4 = 14 > 0` — it GROWS with L_max, it does NOT relax toward a finite continuum. **Branch**: NOT pre-closed (no prior gate scans the a₄ *magnitude* on the L_max axis at τ_fold); the gate is computed, and the structural prediction is that the plan's PASS-truncation direction (Δa₄ < 0) will FAIL — the measured tail INCREASES.

**Verdict**: **INFO** (INFO-physical) — composite `[SIGN]` 3-tuple `sign=FAIL · magnitude=INFO · regime=MARGINAL`, collapsed per `gate-verdicts.md §"Composite-collapse rule"` (sign mismatch under VALID/MARGINAL regime is the INFO-physical outcome; FAIL is reserved for regime=BREAKDOWN, which did not occur). The un-protected EXTENSIVE a₄ is measured **monotone-INCREASING** with L_max (Δa₄ = +196, +1597, +4367 — all strictly positive over L=3→4→5→6), the OPPOSITE of the plan's predicted decreasing tail; `tail_fraction = 1.044` lies far outside the PASS-band `[0.0268, 0.0804]`. **The m_H +5.36% residual is NOT the a₄ extensive truncation tail** — it is a PHYSICAL residual that must be sourced elsewhere (routes to the INV5-W2-3 Pekker-Varma continuum self-energy / the Γ_eff effacement as a derived screening). Track-B (PHYSICAL-FLOOR) gets the 0.85 posterior mass per the gate's dual_prior discriminator.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — verified by content presence, grep evidence pasted below):

- [x] `computations/investigation-5/inv5_w3_1_a4_lmax_convergence.py` exists (23045 bytes) — must_contain `from canonical_constants import` + `print_verdict_payload` (def + call). Grep:
  ```
  $ grep -nE "from canonical_constants import|def print_verdict_payload|print_verdict_payload\(" inv5_w3_1_a4_lmax_convergence.py
  105:from canonical_constants import tau_fold, m_H_FW_KK_threshold, m_H_obs  # framework constants
  174:def print_verdict_payload(verdict, value, audit_sha, content_sha,
  468:    payload = print_verdict_payload(
  ```
- [x] `computations/investigation-5/inv5_w3_1_a4_lmax_convergence.npz` exists (full float64 a₄(L_max), Δa₄ slope, tail-fraction). `ls -la` → 8324 bytes; keys include `a4`, `delta_a4`, `tail_fraction`, `a4_spread`, `a0`, `a2`, `fit_resid`, `monotone`, `all_positive`.
- [x] `computations/investigation-5/inv5_w3_1_a4_lmax_convergence.png` exists (a₄(L_max) curve + Δa₄ slope + tail-fraction vs +5.36% band). `ls -la` → 69613 bytes.

**Verdict-Line Closure Checklist** (compute gate — emits a verdict line; emitted via `emit_verdict(session=5, track="investigation", ...)`, NOT a raw `open("a")` append, per `gate-verdicts.md §"Race-Safe Emission"`; 8 rows appended, cross-process locked, sig_5 unique):

- [x] canonical line present (full 64-char `audit_sha256=9673cfffe9faec061e4260322293a316f604f28ad6615613932d688890c674cc`). Grep:
  ```
  $ grep -E '^INV5-W3-1:.* audit_sha256=[a-f0-9]{64}' inv5_gate_verdicts.txt
  INV5-W3-1: INFO -- value='tail_fraction=1.0438;...;all_pos=True;dA=[+1.959e+02,+1.597e+03,+4.367e+03];a4=[-2.5864e+02,-6.2728e+01,1.5347e+03,5.9018e+03];L_op=6;L_plan=6;canon_drift=True' scheme=FW convention=EXTENSIVE-a4-MAGNITUDE-a_4^{zeta} L_max=6 audit_sha256=9673cff…74cc content_sha256=cce063b6…1abdaa schema_version=S84+
  ```
- [x] dual-SHA companion comment row present: `# audit_sha256_short=9673cfffe9faec06 content_sha256_short=cce063b6bf2c9c48 # INV5-W3-1 dual-SHA companion row` (`audit_sha256` over `["script","canonical","pinmap"]`, `content_sha256` over `["script"]`).
- [x] `[SIGN]` 3-tuple companion row present: `# sign_verdict=FAIL magnitude_verdict=INFO regime_verdict=MARGINAL # INV5-W3-1 3-tuple annotation (schema-v2); …`. (`sign_verdict=FAIL`: measured Δa₄(L) > 0, opposite to predicted < 0; `magnitude_verdict=INFO`: tail_fraction 1.044 outside band; `regime_verdict=MARGINAL`: worst heat-kernel fit_resid 5.74e-3.)
- [x] `regulator_pin` companion annotation `# regulator_pin=a_4^{zeta}` carried (zeta-regulated fourth Seeley-DeWitt coefficient; `regulator-pin-discipline.md`). `CLASS=FULL` companion row also carried.
- [x] verdict-line `audit_sha256` unique across the file (sig_5; `emit_verdict` accepted the append — distinct from the W1-1 `687d9c9d…`, W2-2 `cd6e2297…` SHAs already in the file).

**Results**:

**a₄(max_pq_sum) — EXTENSIVE, zeta-regulated, at τ = τ_fold = 0.190** (heat-kernel t²-coefficient of t⁴·K(t) via `spectral_action.extract_seeley_dewitt_robust`, robust 3-t-range mean; n_evals = block eigenvalue count, no PW factor):

| `max_pq_sum` (= L_max) | a₄ (extensive) | a₄ 3-range spread | a₀ | a₂ | fit_resid | n_ev |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | **−2.586×10²** | 3.7×10² | 0.0936 | +4.535 | 2.25e-3 | 1232 |
| 4 | **−6.273×10¹** | 2.5×10³ | 1.864 | −66.97 | 9.68e-4 | 2912 |
| 5 | **+1.535×10³** | 9.2×10³ | 7.174 | −318.2 | 2.34e-3 | 6048 |
| 6 | **+5.902×10³** | 2.3×10⁴ | 16.65 | −830.0 | 5.74e-3 | 11424 |

**Per-step slope Δa₄(L) = a₄(L) − a₄(L−1)** (the [SIGN] observable):

| step | Δa₄(L) | sign |
|:---:|:---:|:---:|
| L=3→4 | **+1.959×10²** | **+** |
| L=4→5 | **+1.597×10³** | **+** |
| L=5→6 | **+4.367×10³** | **+** |

→ `monotone = True`, **`all_positive (INCREASING) = True`**, `all_negative (decreasing) = False`.

**Tail-fraction**: tail = a₄(L_max=6) − a₄(L=3) = +6.161×10³; `tail_fraction = |tail| / |a₄(L_max)| = 6160.5/5901.8 = 1.0438`. Compared to `residual_mH = (131.8 − 125.1)/125.1 = 0.053557` (PASS-band [0.0268, 0.0804]): **`tail_in_band = False`**, `delta_to_residual = +0.9903`. The tail is ~19.5× the upper band edge.

**Two-part threshold readout** (plan strict_PASS_boundary): (i) `sign(Δa₄(L)) < 0` strict for every L-step → **FAILS** (all three steps are `> 0`); (ii) `|tail_fraction − 0.0536| ≤ 0.0268` → **FAILS** (|1.0438 − 0.0536| = 0.990 ≫ 0.0268). Both parts of PASS-truncation fail → **INFO-physical** (per the plan INFO_meaning: tail monotone but the residual-fraction is outside the band).

**[SIGN] 3-tuple & composite** (`gate-verdicts.md §"Composite-collapse rule"`): `sign_verdict = FAIL` (predicted direction Δa₄ < 0; measured Δa₄ > 0 — direction MISMATCH), `magnitude_verdict = INFO` (tail_fraction outside band), `regime_verdict = MARGINAL` (worst heat-kernel small-t fit residual 5.74e-3, in [1e-3, 1e-2) — the t² coefficient is resolvable but the fit degrades as the eigenvalue count grows at L=6). Collapse: regime ≠ BREAKDOWN, sign = FAIL under VALID/MARGINAL regime → there is no "wrong-answer" physics FAIL (FAIL is reserved for regime=BREAKDOWN per plan FAIL_meaning), so the sign-mismatch IS the **INFO-physical** outcome → **composite = INFO**.

**[SIGN] substitution chain WITH substituted numbers** (plan §W3-1 substitution_chain):
- Def 4: `residual_mH = (m_H_FW − m_H_obs)/m_H_obs = (131.8 − 125.1)/125.1 = +0.053557` ✓ (live canonical, MCP-verified).
- Predicted (plan Step c–d): `a₄(L) = a₄^cont + tail(L)`, `tail(L) ~ C·L^{−p}` with `p>0` ⇒ `Δa₄(L) = C·(L^{−p} − (L−1)^{−p}) < 0 ⇔ C > 0` (truncation over-counts a₄ and relaxes downward).
- **Measured**: `Δa₄ = {+195.9, +1597.4, +4367.1}` all `> 0` ⇒ `sign(Δa₄) > 0 ⇔ C < 0` ⇒ the heat-trace a₄ does NOT relax to a finite continuum; it GROWS. This is the R-Protection / Tier-2 structural expectation made quantitative: the EXTENSIVE coefficient has Weyl exponent `α₄ = d+r+4 = 8+2+4 = 14 > 0` (individual a_k are L_max-FRAGILE per S76; only the ratios R_n cancel). The plan's PASS-truncation premise (decreasing tail toward a finite `a₄^cont`) is the wrong model for this object — `a₄^cont` for the spectral-sum a₄ is not a finite number (the continuum heat-trace t²-coefficient diverges; the finite continuum value is the Gilkey *curvature integral*, a DIFFERENT object per session-60-bap-collab).
- **Direction conclusion**: `tail_fraction = 1.0438 ≫ residual_mH = 0.0536` AND the tail INCREASES ⇒ the **+5.36% m_H residual is NOT the a₄ extensive truncation tail** → PHYSICAL (routes to INV5-W2-3 Pekker-Varma continuum self-energy / the Γ_eff = 0.99970 effacement as a derived screening).

**L_max disclosure**: `L_max_plan = 6`, `L_max_operational = 6` (no graceful-degradation drop; all four irrep builds at p+q ≤ 6 completed, total ~8.3s, well within the timeslot — confirming the Casimir-bound + Friedrich-Bär feasibility argument of `math-scripts.md §"D_K Block-Diagonality"` scoped to L ≤ 6, far below the p+q ≥ 13 ceiling).

**4-tuple**: `(value=tail_fraction=1.0438, scheme=FW, convention=EXTENSIVE-a4-MAGNITUDE-a_4^{ζ}, L_max=6)`.

**Dual-SHA**: `audit_sha256=9673cfffe9faec061e4260322293a316f604f28ad6615613932d688890c674cc` (over `{script, canonical, pinmap}`), `content_sha256=cce063b6bf2c9c48fa78c41315983665b630a02aff807279ff2e9e2d551abdaa` (over `{script}`).

**Plan-text drift disclosed** (`substrate-first-canonical-sourcing.md §(ii.B)`): the plan-pinned `canonical_constants.py` SHA `e6829db0…` differs from the runtime SHA `8505153a…` (file updated between plan-freeze 2026-06-14 and this run). The LIVE file was consumed; the three consumed constants (`tau_fold=0.19`, `m_H_FW_KK_threshold=131.8`, `m_H_obs=125.1`) were independently verified via `mcp__knowledge__.get_constant` — all match. Drift is logged in the verdict `value=` (`canon_drift=True`) and a dedicated companion row.

**Artifacts**: `computations/investigation-5/inv5_w3_1_a4_lmax_convergence.py` (23045 B) / `.npz` (8324 B, full float64) / `.png` (69613 B — left: a₄(L_max) with spread error bars; right: Δa₄ slope bars (all red/positive = increasing) + tail-fraction line vs the +5.36% gold band).

**Solution-space reading**: This INFO-physical verdict CLOSES the a₄-truncation corridor for the m_H +5.36% residual. The corridor "the +5.36% is a resolvable finite-L_max artifact that vanishes as the substrate's spectrum is resolved" is **eliminated**: the extensive a₄ magnitude does the opposite of vanishing — it grows ~23× over L=3→6 and never approaches a finite continuum, because it is an un-protected (multiset {8,4} ≠ {6,6}, NOT weight-balanced) coefficient with α₄ = 14 > 0. The residual is therefore PHYSICAL and must be sourced by a substrate observable that survives the continuum limit. Feeds the INV5-W3-3 review's PHYSICAL leg; corroborates the INV5-W2-2 finding (substrate phase-stiffness dominates) and routes to the INV5-W2-3 Pekker-Varma self-energy. NOTE on spectral-geometer C4/R4 (the "a₄ varying 28.65% across τ ⇒ +5.36% is the a₄ tail at L_sat=6" reading the gate was set up to test): C4/R4 conflated the τ-axis variation of a₄ (S77 R_1-trajectory: a₄ varies 28.65% across τ ∈ [0,0.5]) with an L_max-axis convergence tail. On the L_max axis at fixed τ_fold, a₄ does not converge to a continuum at all (it diverges UV-dominated) — the two axes are structurally distinct, exactly the inv-3 INV3-W2-2 vs INV5-W3-1 distinction the plan flagged. The +5.36% is not on either axis an a₄ truncation artifact.

**Substrate framing** (GEOMETRIC, `phononic-framing.md`): the object under test is a₄ — the fourth Seeley-DeWitt coefficient of `Tr exp(−t D_K²)` — a spectral moment of D_K, the fabric's own spectral content at τ_fold. Arrow: `D_K eigenvalues → the heat-kernel small-t limb → the a₄ moment (the weight-4 Phi(a₄)=Σ₃ load-bearing YM+Higgs-quartic term) → the emergent m_H`. The +5.36% is read substrate-first: the finite Peter-Weyl truncation at L_max=3 IS the substrate AS-COMPUTED, and the question is whether the substrate's OWN a₄ relaxes toward its continuum value fast enough that the residual at L_sat≈6 IS the +5.36% — the substrate IS the truncation tail, with no container-side "correction" invoked. The un-protected EXTENSIVE character (multiset {8,4} ≠ {6,6}, not weight-balanced) is why a₄ — unlike the intensive R-protected ratios — carries a non-cancelling tail at all: the substrate's geometry, not an external regulator, sets the convergence.

---

### §W3-2. INV5-W3-2 (workshop — connes-ncg-theorist ↔ landau-condensed-matter-theorist)

**Status**: LANDED (artifact-existence closure; NO verdict line) — **STRUCTURAL VERDICT: SCOPED** (Reading-1 Layer A / Reading-2 Layer B; S72 two-layer split structurally forced by Wall #6 + S35 Kosmann). Deliverable verified on disk.
**Gate ID**: `INV5-W3-2`
**Gate type**: `workshop` (EXACTLY-2-agent adversarial adjudication, 2 rounds, sequential, shared document; closes by artifact-existence, **NO verdict line**)
**Trigger**: `[VERIFY-THEOREM]` (the workshop produces a STRUCTURAL VERDICT — a derived structural claim — not a numerical gate)
**Classification**: **GEOMETRIC** (the adjudicated object is the spectral action `Tr f(D²)` — a functional of the D_K eigenvalue spectrum — and its relation to the substrate's free energy)
**Owner (neutral planner, NOT a participant)**: `gen-physicist`
**Workshop participants (EXACTLY 2)**: `connes-ncg-theorist` ↔ `landau-condensed-matter-theorist`
**Deliverable description (one-line)**: the ONE genuine Q1a adversarial adjudication of inv-5 — is the spectral action `Tr f(D²)` the substrate's effective action / free energy (same functional, different variables) OR a categorically-distinct functional (a one-particle spectral moment) with a domain disjoint from the order-parameter / Gibbs-Duhem free energy — the two advocates co-citing the SAME S37 93×-BCS-wrong-sign result from opposite domains, converging on a STRUCTURAL VERDICT + the single decisive forward compute.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w3.md` §W3-2 (`workshop:` block — agents, rounds, sources, the neutrally-stated (a)/(b)/(c) sub-questions, the adjudication rule).

**MCP Pre-Compute Audit**: the advocates' knowledge-MCP queries are recorded in their turn sections of the deliverable `workshops/two-effective-actions.md` (each turn's source-citations anchor to S35/S37/S64/S65 ledger entries + `get_constant` values verified at draft time, e.g. Δ_BCS=0.4642547, E_cond=−0.13685, Wall #6 dS/dμ|_0=0). Workshop gate closes by artifact-existence; no orchestrator-side compute pre-audit.

**Workshop structure** (from plan `workshop:` block): R1 = each advocate states their first-principles reading of the SAME shared evidence into the shared document (connes C-3/A-2/R-3: SA authority preserved by fixing f, by the a₄-anomaly CC channel, or by proving SA = Volovik Gibbs-Duhem free energy as the same functional in different variables; landau U-1: the wrong-sign is CATEGORICAL — the order-parameter free energy is not the one-particle spectral sum, the two-layer S72 architecture is itself an assumption); R2 = each rebuts the opponent's R1 and the pair converges on a STRUCTURAL VERDICT + the decisive forward gate. Three sub-questions, each stated NEUTRALLY (neither reading pre-favored): **(a)** is the S37 +12.76 anti-trapping (93×) evidence that the SA is the WRONG functional for the order-parameter sector (categorically-distinct Landau-Ginzburg / Gibbs-Duhem free energy required), or merely that the SA is a spectral MOMENT not a total energy, reconcilable as the SAME functional in different variables? **(b)** does the a₄-anomaly CC channel (Weyl² + trace-anomaly sub-term of a₄, INV5-W1-2) RECOVER SA authority over the vacuum-energy sector, or is the CC irreducibly a Volovik / Gibbs-Duhem thermodynamic object (DILUTION-CC-66 ρ_vac/ρ_obs = 1.032, OUTSIDE the SA)? **(c)** what SINGLE compute DECIDES it — the one pre-registerable forward gate whose PASS/FAIL discriminates "same functional, different variables" from "categorically-distinct functionals with disjoint domains," with the discriminating prediction each reading makes? Cited evidence (NOT a participant): spectral-geometer G4 — a_2^{SD} = 0.728235 vs ζ_D(1) = 2776.17 differ by factor ~3812 on the truncated d=8 spectrum, a worked instance of "two objects both correctly named a₂ in their own functional."

**Structural-verdict target**: a derived STRUCTURAL VERDICT — **Reading-1 same-functional-different-variables** (the BCS condensation energy is a Fock-space quantity, the SA a one-particle spectral sum, coincident under a change of variables) vs **Reading-2 categorically-distinct-functionals-with-disjoint-domains** (the order-parameter free energy is a different functional of the same substrate that the spectral-moment sum does not reach) — plus the named decisive forward compute of sub-question (c). If the two advocates do NOT converge within 2 rounds, the Wrap-Up records BOTH readings with their decisive forward gates and tags the verdict CONVERGENCE-DEFERRED (still a LANDED artifact). The verdict resolves the competing claims into a NEW pinned position; it does NOT queue a computation in place of a verdict.

**Artifact-Existence Closure Checklist** (workshop closure == `wave-classification.md §M1`; **NO verdict line, NO dual-SHA, NO closure SHA** — closure is artifact-existence-with-content of the `workshop.output_path` deliverable):

*(pending — confirm the deliverable md exists (`ls sessions/investigation/investigation-5/workshops/two-effective-actions.md`) AND paste `grep -E '<pattern>' <path>` output for every must_contain pattern below. An absent file OR any must_contain regex returning empty means the workshop did not properly close — orchestrator MUST then SendMessage continuation to the workshop dispatch per `feedback_dispatch-discipline.md`. Closure is purely by content presence (regex match), NEVER by line/byte counts per `feedback_max-effort-full-fidelity.md`. This is a `landed`/`not-landed` outcome, NOT a substrate-physics PASS/FAIL: a missing-section `not-landed` remediates by re-dispatching the workshop, NOT a numerical re-run — and routes per `mechanical-closure-discipline.md` to the inv-5 close.)*

- [x] `sessions/investigation/investigation-5/workshops/two-effective-actions.md` exists (verified on disk)
- [x] must_contain: `## Wrap-Up` (line 526) — derived position resolving (a)/(b)/(c)
- [x] must_contain: `STRUCTURAL VERDICT` (line 508) — **SCOPED** (Reading-1 Layer A / Reading-2 Layer B) + decisive forward gate `INV5-CC-MU-DEPENDENCE-DISCRIMINATOR`
- [x] must_contain: `Effected In-Session` (line 553) — three `[→investigate]` session-promotion routes (atlas-04 S3 re-scope, capstone down-tag, S72 standing); 0 unchecked checkboxes (correct — no investigation-track edits)
- [x] must_contain: `Carry-Forward Computations` (line 567) — the decisive ∂/∂μ + ∂/∂V gate as a 4-field carry-forward

**Substrate framing** (GEOMETRIC, `phononic-framing.md`; preserved neutral to the outcome): the adjudicated object is the spectral action `Tr f(D²/Λ²)` — a functional of the D_K eigenvalue spectrum — and whether THAT spectral-moment functional IS the substrate's free energy. The substrate-first arrow holds on BOTH readings: `D_K eigenvalues → spectral moments (a₀/a₂/a₄) → emergent action`; the workshop adjudicates whether the SAME spectral data, read as a free energy / effective action, governs the order-parameter (BCS / Fock-space) sector, or whether the order-parameter free energy is a DIFFERENT functional of the same substrate (a Fock-space / Gibbs-Duhem object) that the spectral-moment sum does not reach. Neither reading inverts into container thinking — both keep the substrate (the D_K spectral content) logically prior; the disagreement is over which functional OF that substrate is the effective action for which sector. spectral-geometer's G4 (a_2^{SD} vs ζ_D(1), factor 3812) is the worked example that the SAME substrate spectrum already supports two distinct correctly-named functionals — supplied as evidence, not as a third position. FORBIDDEN inversion (neither advocate may invoke): "the SA is set by an external thermodynamic container the substrate lives in" — both readings keep the D_K spectrum prior.

---

### §W3-3. INV5-W3-3 (review — gen-physicist, neutral synthesizer)

**Status**: LANDED (artifact-existence closure; NO verdict line) — full three-way Higgs-residual synthesis (NOT prereq-blocked; all of W1-1/W2-3/W3-1 present). Joint picture: the +5.36% residual is PHYSICAL-but-UNDERIVED (both removal mechanisms falsified). Deliverable verified on disk (23,266 B).
**Gate ID**: `INV5-W3-3`
**Gate type**: `review` (N independent synthesizers — here 1, the neutral question owner; closes by artifact-existence-with-content, **NO verdict line**)
**Trigger**: `[VERIFY]` (independent-synthesis review — Q1b "synthesize / characterize X")
**Classification**: **GEOMETRIC** (the synthesized observable is the m_H residual, a derived consequence of the a₄ weight-4 spectral moment of D_K)
**Agent**: `gen-physicist` (1 neutral synthesizer)
**Deliverable description (one-line)**: synthesize the THREE independent readings of the m_H +5.36% residual — connes' Pati-Salam quadratic-fluctuation Higgs quartic (INV5-W1-1), landau's Pekker-Varma continuum self-energy (INV5-W2-3), spectral-geometer's a₄ L_max truncation-tail (INV5-W3-1) — into one picture: do they AGREE on SIGN and MAGNITUDE, and is the residual TRUNCATION (resolvable, an artifact of finite L_max) or PHYSICAL (a derived screening that survives the continuum limit)? Characterize the joint picture; do NOT force a single winner.
**Plan reference**: `sessions/investigation/investigation-5/investigation-5-plan-w3.md` §W3-3 (`review:` block — the neutral synthesizer, the two-axis (sign/magnitude) + (truncation/physical) characterization frame, the PREREQ-BLOCKED handling).
**Prerequisite (gated)**: INV5-W1-1 (connes Pati-Salam quartic) + INV5-W2-3 (landau Pekker-Varma self-energy) + INV5-W3-1 (this wave's a₄ L_max-tail compute). **If any prereq is unmet at dispatch**, the review synthesizes the AVAILABLE subset, explicitly flags the missing leg(s), and tags the deliverable PARTIAL-PENDING-`<missing-gate(s)>` — closing per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` (PRE-REG-INC, blocked-by-`<prereq>`, deferred to inv-5 close). It does NOT block the wave and does NOT emit a verdict line (review gates never do).

**MCP Pre-Compute Audit**: the synthesizer read the three source verdicts (grep INV5-W1-1/W2-3/W3-1 in the inv5 ledger) + their WP sections + the three survey Higgs sections, recorded in the deliverable `investigation-5-higgs-residual-synthesis.md`. Review gate closes by artifact-existence; the synthesis does not recompute the source gates (it characterizes them), so no orchestrator-side compute pre-audit.

**Review structure** (from plan `review:` block): a single synthesis md comparing the THREE Higgs-residual derivations head-to-head along two axes — **SIGN** (does each reading predict a POSITIVE shift of m_H above 125.1, the framework's 131.8 sitting above the PDG value, or a NEGATIVE screening pulling 131.8 back toward 125.1?) and **MAGNITUDE** (does each reading's number match the +5.36% / +6.7 GeV / 38.5σ residual?). The three readings: **(1) connes — Pati-Salam quartic** (the +5.36% is a PROPERTY of the geometric Higgs quartic λ from a₄/a₂, not a correction TO it, if m_H^PS lands at 131.8 within the eps_H band); **(2) landau — Pekker-Varma self-energy** (the −5.36% is a DERIVED Landau screening, Re Σ_continuum from the |S|²-mode coupling to the B2/B3 two-quasiparticle continuum, converting the fitted Γ_eff = 0.99970 effacement into a derived self-energy); **(3) spectral-geometer — a₄ L_max truncation tail** (the +5.36% is the un-protected a₄ extensive truncation tail at L_sat≈6, a RESOLVABLE finite-truncation artifact that vanishes as L_max → continuum). The synthesis question: do the three AGREE (e.g. truncation and self-energy are the SAME effect in two regulators, with the quartic setting the leading-order value) or CONFLICT (truncation says the residual VANISHES at the continuum while self-energy says it is a PHYSICAL screening that PERSISTS)? State explicitly, per reading, whether it makes the +5.36% TRUNCATION (resolvable) or PHYSICAL (survives the continuum limit), and whether the three are mutually consistent under that classification.

**Artifact-Existence Closure Checklist** (review closure == `wave-classification.md §M1`; **NO verdict line, NO dual-SHA, NO closure SHA** — closure is artifact-existence-with-content of the `review.output_paths` deliverable):

*(pending — confirm the deliverable md exists (`ls sessions/investigation/investigation-5/investigation-5-higgs-residual-synthesis.md`) AND paste `grep -E '<pattern>' <path>` output for every must_contain pattern below. An absent file OR any must_contain regex returning empty means the review did not properly close — orchestrator MUST then SendMessage continuation to the review dispatch per `feedback_dispatch-discipline.md`. Closure is purely by content presence (regex match), NEVER by line/byte counts per `feedback_max-effort-full-fidelity.md`. This is a `landed`/`not-landed` (or PARTIAL-PENDING) outcome, NOT a substrate-physics PASS/FAIL: a missing-section `not-landed` remediates by re-dispatching the review, NOT a numerical re-run — and a prereq-blocked dispatch closes per `mechanical-closure-discipline.md` and routes to the inv-5 close.)*

- [x] `sessions/investigation/investigation-5/investigation-5-higgs-residual-synthesis.md` exists (verified, 23,266 B)
- [x] must_contain: `## ` — sectioned structure (§I–§IX, 9 hits)
- [x] must_contain: `INV5-W1-1` — the connes Pati-Salam quartic reading (7 hits)
- [x] must_contain: `INV5-W2-3` — the landau Pekker-Varma self-energy reading (5 hits)
- [x] must_contain: `INV5-W3-1` — the spectral-geometer a₄ truncation reading (5 hits)
- [x] must_contain: `truncation` — the truncation-vs-physical classification axis (14 hits)
- [x] N/A — NOT prereq-blocked: all three prerequisites (W1-1/W2-3/W3-1) landed, so the full three-way synthesis was written (no PARTIAL-PENDING tag needed)

**Substrate framing** (GEOMETRIC, `phononic-framing.md`): the synthesized observable is the m_H residual — a derived consequence of the a₄ weight-4 spectral moment of D_K (the |S|² KK-threshold mode, a₄-dressed). The substrate-first arrow holds across all three readings: `D_K eigenvalues → spectral moments (a₄/a₂ → the Higgs quartic) → the emergent m_H → the measured +5.36% over PDG`. The review keeps the direction one-way: it asks whether the residual IS the substrate's own finite-truncation tail (the substrate AS-COMPUTED at finite L_max — spectral-geometer), the substrate's own derived self-energy (a Pekker-Varma screening intrinsic to the substrate's two-quasiparticle continuum — landau), and/or the value of the substrate's own geometric quartic (connes) — three substrate-IS readings of the SAME number, never a container-side correction TO an external m_H. The truncation-vs-physical classification is itself substrate-first: "truncation" = the residual is an artifact of reading the substrate at finite L_max and vanishes as the substrate's OWN spectrum resolves toward the continuum; "physical" = the residual is a genuine substrate observable (a derived screening) that survives the continuum limit.

---

## Wave 3 Synthesis (team-lead)

The terminal wave supplied spectral-geometer's heat-kernel adjudication of the two joints where all three inv-1 surveys converged. Three type-distinct gates: 1 compute (W3-1 INFO-physical), 1 workshop (W3-2 LANDED SCOPED), 1 review (W3-3 LANDED). They resolve the investigation's two headline cross-wave tensions.

**Resolution 1 — the m_H +5.36% residual is real, physical, and mechanistically UNDERIVED (W3-1 + W3-3).** W3-1: the extensive a₄ is monotone-**increasing** on the L_max axis (Δa₄ = {+196, +1597, +4367}, tail_fraction 1.044 ≈ 19.5× the PASS band) — it does NOT converge to a continuum tail; it *diverges* (Weyl exponent α₄ = d+r+4 = 14 > 0). So the residual is NOT a resolvable a₄ truncation artifact — it is PHYSICAL. The W3-3 review then synthesized all three readings: the naive "truncation-vanishes vs self-energy-persists" conflict the seed feared *does not materialize* — both *removal* mechanisms are falsified (W3-1 doesn't vanish-it-diverges; W2-3 wrong sign), and they even share a genus (both shift up/over-counting, the wrong side for the down/screening the −5.36% needs). W1-1's PASS means the SA quartic *gives* 131.8 — the residual is a property of the geometric quartic, not a correction. **Net: the +5.36% is real and physical but its exact value is UNDERIVED** (three session-track carry-forwards specced by the review: quartic-scheme derivation, 169-direction A_quad diagonalization, independent Γ_eff derivation).

**Resolution 2 — the two-effective-actions tension is SCOPED, and the S72 two-layer split is a structural truth (W3-2 workshop).** The connes↔landau adjudication converged (genuinely — connes withdrew blanket Reading-1 on the strength of his own S35 Kosmann theorem) on a **SCOPED verdict**: Reading-1 (SA *is* the effective action) holds for **Layer A** (spectral/geometry — n_s, a₂-gravity, H₀, the dimensionless shapes, functionals of {λ_k} alone); Reading-2 (categorically-distinct functionals) holds for **Layer B** (order-parameter + vacuum/CC — a μ-dependent Gibbs-Duhem functional on the (μ,V) domain disjoint from the spectral triple). The S72 two-layer architecture is therefore NOT a workaround but a **structural truth forced by domain-disjointness**: the sector boundary *is* the content of Wall #6 (μ=0 forced by PH symmetry) + the S35 Kosmann theorem (V ∉ triple). Sub-(a): the 93× wrong-BCS-sign is the theorem-forced kinetic-vs-binding mismatch (SA is a correct summand, not the selecting Landau-Ginzburg functional). Sub-(b): W1-5's functional-dependence CONFIRMS the CC is f-undetermined within {Tr f}, μ-selected outside it. Sub-(c): the decisive gate is `INV5-CC-MU-DEPENDENCE-DISCRIMINATOR` (∂/∂μ + ∂/∂V).

### What Changed

#### (a) Numerical revisions
- a₄(L_max) = {−258.6, −62.7, +1534.7, +5901.8} (monotone-increasing, tail_fraction 1.044); the SA quartic m_H = 135.01 → 131.8 (W1-1); the two-layer boundary pinned at the μ=0 (Wall #6) + V∉triple (Kosmann) disjointness.

#### (b) Structural changes
- **m_H +5.36% residual**: OPEN-three-vantage → **PHYSICAL but UNDERIVED** (truncation reading falsified — a₄ diverges, not converges; self-energy reading falsified — wrong sign; quartic *gives* 131.8, doesn't derive the residual).
- **two-effective-actions**: implicit/festering → **SCOPED VERDICT** (SA = effective action for Layer A; categorically-distinct on Layer B); S72 two-layer split is structural-truth-not-assumption.
- **a₄ extensive axis**: → **PHYSICAL-FLOOR / divergent** (R-Protection confirmed quantitatively — only the protected ratios converge; the extensive coefficient diverges).

### Effected In-Session (non-math)
None investigation-effectable — all session-track curated-register edits, routed to `/rclab-investigate --investigation 5`:
- [→investigate] **atlas-04 S3 re-scope** — "SA-is-the-effective-action ASSUMED" → "scoped to Layer A (spectral/geometry); categorically-distinct on Layer B (order-parameter/CC) per INV5-W3-2" (capstone-hygiene Q3/Q4, designated-writer prose patch per `feedback_framework-hygiene.md`).
- [→investigate] capstone §-prose down-tag of any SA-as-total-free-energy claim to the Layer-A scope; the S72 two-layer architecture's epistemic standing upgraded from "assumed decoupling" to "structurally forced by Wall #6 + Kosmann".

## Carry-Forward Computations

### CF-INV5-W3-A — INV5-CC-MU-DEPENDENCE-DISCRIMINATOR (the W3-2 decisive forward gate)
| Field | Spec |
|:------|:-----|
| **What** | Settle the SCOPED verdict's Layer-B claim with the discriminating numbers: `∂(vacuum energy)/∂μ` (Gibbs-Duhem slope = −⟨N⟩) for the vacuum half and `∂(condensation)/∂V` for the order-parameter half. Both zero ⇒ SA-reachable (Reading-1); non-zero on either ⇒ irreducibly Fock/grand-canonical (Reading-2). The SA-side null predictions (∂[Tr f]/∂μ = 0, ∂[Tr f]/∂V = 0) are anchored by Wall #6 + the Kosmann theorem. (Mirror of the workshop's own `## Carry-Forward Computations` block.) |
| **Inputs** | the L_max=10 D_K spectrum cache; the BdG/Kosmann pairing machinery (S35); Δ_BCS=0.4642547, E_cond=−0.13685; the entropy/cutoff functionals; Wall #6 μ=0 PH-symmetry construction. |
| **Gate** | ∂(vacuum)/∂μ and ∂(condensation)/∂V emitted with sign; zero-on-both ⇒ Reading-1, non-zero-on-either ⇒ Reading-2 (the verdict-bearing discriminator). |
| **Effort** | low–moderate (existing cache; two finite-difference scans + a 1-D gap solve). |

### CF-INV5-W3-B — Higgs-residual derivation (the underived +5.36%, 3 routes from the W3-3 review)
| Field | Spec |
|:------|:-----|
| **What** | Derive the exact +5.36% (= 67/1251) m_H residual, now established PHYSICAL-but-underived. Three session-track routes the W3-3 synthesis specced: (i) the geometric-quartic scheme derivation (why a₄/a₂ gives exactly this value); (ii) the 169-direction A_quad explicit diagonalization (harden W1-1's RMS-bound magnitude leg); (iii) an independent Γ_eff=0.99970 derivation (is the 0.03% effacement related, or distinct as W2-3 found?). |
| **Inputs** | `inv5_w3_1_a4_lmax_convergence.py`, `inv5_w1_1_*.py`, `inv5_w2_3_*.py`; the session-46 169-direction A_quad module; a₄/a₂ at L12; Γ_eff. |
| **Gate** | a route reproduces +5.36% from first principles (no fitted screening), OR the residual is shown irreducible at this order. |
| **Effort** | ~1.5 wave-equiv (the 169-direction diagonalization is the main cost). |

(W3-1's INFO-physical closes the truncation reading — no L_max-refinement CF, the divergence is structural. W3-3 landed full three-way, not PARTIAL-PENDING — no re-synthesis CF.)

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:---------|:-------|
| 2026-06-15 | m_H +5.36% residual nature | OPEN-three-vantage | PHYSICAL-but-UNDERIVED (not truncation, not self-energy, quartic gives-not-derives) | W3-1 a₄ diverges + W3-3 synthesis (both removal mechanisms falsified) |
| 2026-06-15 | two-effective-actions tension (atlas-04 S3) | "SA-is-the-effective-action ASSUMED"; implicit/festering | SCOPED — Reading-1 Layer A / Reading-2 Layer B; S72 split structural-not-assumed | W3-2 workshop converged verdict (Wall #6 + Kosmann disjointness) |
| 2026-06-15 | a₄ extensive-axis L_max convergence | OPEN (resolvable-truncation vs physical-floor) | PHYSICAL-FLOOR / divergent (α₄=14>0; only protected ratios converge) | W3-1 monotone-increasing, tail_fraction 1.044 |

## Files Produced

| Artifact | Role | Status |
|:---------|:-----|:-------|
| `computations/investigation-5/inv5_w3_1_a4_lmax_convergence.py` / `.npz` / `.png` | INV5-W3-1 compute (a₄(L_max), Δa₄ slope, tail-fraction) | ✓ on disk |
| `computations/investigation-5/inv5_gate_verdicts.txt` | INV5-W3-1 verdict line (the wave's ONLY verdict line — workshop + review emit none) | ✓ (line 1; audit 9673cfff…) |
| `sessions/investigation/investigation-5/workshops/two-effective-actions.md` | INV5-W3-2 workshop deliverable (SCOPED verdict; artifact-existence closure) | ✓ on disk |
| `sessions/investigation/investigation-5/investigation-5-higgs-residual-synthesis.md` | INV5-W3-3 review deliverable (23,266 B; artifact-existence closure) | ✓ on disk |
| `sessions/investigation/investigation-5/investigation-5-w3-workingpaper.md` | this working paper | ✓ on disk |
