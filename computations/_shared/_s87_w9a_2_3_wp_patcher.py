"""
One-shot Python patcher for §W9a-2 + §W9a-3 working-paper sections.

Replaces the NOT-STARTED stubs at lines 7447-7466 (§W9a-2) and 7468-7486
(§W9a-3) with substantive content. Single-shot file rewrite avoids
Edit-tool mtime-race against parallel writers.

Pattern follows S86 W1c-5 / W1c-6 one-shot writers + W9a-1 in-place
section replacement protocol.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # (local)
WP_PATH = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"


W9A_2_NEW = """### §W9a-2. S87-A_S-SURVIVING-ROUTE-RANK-LANDING (mack-cosmic-bridge)

**Status**: COMPLETE — α_s 4-route rank-table inventory row landed at `sessions/framework/registry/falsifier-master-inventory.md` EOF; closes deferred install T7-W9-FI-4 (W-9 cluster line 883).
**Gate ID**: `S87-A_S-SURVIVING-ROUTE-RANK-LANDING`
**Trigger**: `[VERIFY]` (Level-2 METHODOLOGY-class artifact-existence-with-substantive-content predicate; rubric-graded)
**Classification**: **METHODOLOGY-class** (M1: artifact-existence predicate; M2: Write/Edit/grep/SHA-256 only; M3: verbatim L3+T3 cross-domain-converged ranked-route table from S86 W-9 R3 closure; M4: PENDING orchestrator allowlist append for `S87-A_S-SURVIVING-ROUTE-RANK-LANDING` in `.claude/rules/methodology-wave-allowlist.md` — subagent edit harness-denied per recursion-attack-closure protocol). Phononic-framing classification: PHONONIC + GEOMETRIC (the four α_s computation routes (i)-(iv) all probe substrate spectral structure). The rank ordering `(iii) ≻ (iv) ≻ (i) ≻ (ii)` reflects substrate-physical-robustness ordering, NOT external-paper authority ordering.
**Agent**: `mack-cosmic-bridge` (sole writer for `falsifier-master-inventory.md` per `feedback_mack-bridge-role.md`; W-9 CF-4 attribution column reads `mack`).
**Hypothesis**: The α_s surviving-route ranked table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` (cross-domain-converged at S86 W-9 across L3 spectral-functional + T3 transit-dynamics evaluation domains) is registry-eligible as a single-row entry in `sessions/framework/registry/falsifier-master-inventory.md` under the α_s observational-channel section. The four routes are: (i) single-pole Mellin moment; (ii) NCG-spectral-action 2-loop running; (iii) GGE-relic Bogoliubov occupation-number variance at horizon crossing — independent of single-pole assumption (STRUCTURAL ROBUSTNESS); (iv) BdG-substrate K-running near GGE saturation crossover (substrate-physical-input-driven). The ranking reflects: (iii) is single-pole-independent; (iv) draws on substrate-physical BdG inputs; (i) is single-pole-dependent (non-trivial structural constraint via BDI universality + GAP-ANTIJENSEN-65 + kinematic optical-branch suppression triple-protection); (ii) has the most upstream-dependency layers (regulator choice + (a_4/a_2) pivot-stationarity + spectral-action-hierarchy correctness) and lowest L3+T3 cross-domain convergence score per S86 W-9.
**Plan reference**: `sessions/session-plan/session-87-plan-w9a.md` §W9a-2 (Field 6 dispatch prompt; CORE WORK A 5-component anatomy).

**MCP Pre-Compute Audit**:

- `mcp__knowledge__.search_knowledge("alpha_s surviving route rank L3 T3 cross-domain converged")` → 10 hits including `s50-cross-domain` SA correlator discovery + `s76_alpha_s_reconciliation.py` Route-1/Route-2 framework + `s73b_transit_ps_lmax7.py` per-L_max alpha_s baseline. None of the hits cover the L3+T3 cross-domain rank table; gate is dispatch-eligible.
- `mcp__knowledge__.search_knowledge("S86 W-9 surviving route rank alpha_s")` → top hit identifies the SR-LO ODE side topline at `s86-alpha-s-tension-and-sign-lock.md` line 829 (verbatim: *"the surviving-route ranking is **(iii) ≻ (iv) ≻ (i) ≻ (ii)**, identical to lizzi's L3 ranking"*). This is the canonical L3+T3 cross-domain convergence text.
- File-level confirmation: `sessions/archive/session-86/workshops/s86-alpha-s-tension-and-sign-lock.md` line 829 carries the topline; lines 1591/1662 carry routes (iii)/(iv) descriptions; lines 1645-1683 carry Priority 1-6 carry-forward queue (CF-14..CF-19 source attribution). The W-9 cluster deferred-to-S87 install T7-W9-FI-4 at `falsifier-master-inventory.md` line 883 explicitly names this landing as the closure target.

**Verdict**: **PASS** -- value='4-route_rank_table_landed_to_falsifier_master_inventory' scheme=L3+T3-cross-domain-converged convention=SOURCE-DOUBLE-CITE-CO-PRIMARY L_max=N/A audit_sha256=`81dd63f045facce7268eed584071c7d4e6da2eae103a4e00ff5b75106d58131e` content_sha256=`1e72e71432a5b0fc5741fd9ee8ea827e1b67139cb4be48522e8e58771010d2db` schema_version=S84+

Companion W9a-99 dual-SHA row: `audit_sha256_short=81dd63f045facce7 content_sha256_short=1e72e71432a5b0fc`.

No `[SIGN]`-trigger 3-tuple required: `[VERIFY]`-trigger METHODOLOGY-class gate; sign_verdict=N/A; magnitude_verdict=PASS (all anatomy components match pattern set); regime_verdict=VALID.

**Results**:

PASS criterion satisfaction (per Field 9 of plan §W9a-2, all 8 conditions):

1. `falsifier-master-inventory.md` contains a 4-route ranked-table entry under an α_s observational-channel section — **PASS**: appended at EOF as new top-level `## NEW α_s observational-channel section: T7-W9-FI-4 surviving-route rank table` block (no collision with existing α_s sub-rows under Row #3 at ### level: pre-edit scan returned ##=1 [the existing α_s discriminator section header from W14-3], ###=2 [the W-2 augmentation sub-rows], ####=0).
2. Rank ordering reads exactly `(iii) ≻ (iv) ≻ (i) ≻ (ii)` — **PASS**: literal in row table at "Rank 1: (iii)", "Rank 2: (iv)", "Rank 3: (i)", "Rank 4: (ii)"; ordering markers `≻` present in the section header.
3. Each rank carries its rationale text — **PASS**: route (iii) "single-pole-independent" (STRUCTURAL ROBUSTNESS); route (iv) "substrate-physical" (BdG-input-driven); route (i) "non-trivial structural constraint" (single-pole assumption not independently validated); route (ii) "upstream-dependency layers" (most-upstream-dependent; lowest L3+T3 convergence score).
4. Cross-domain convergence pin cites both L3 AND T3 evaluation domains — **PASS**: §"Cross-domain convergence pin" cites "L3 (spectral-functional, lizzi-side) + T3 (transit-dynamics / SR-LO ODE side, volovik) cross-domain convergence at S86 W-9 R3 closure" + verbatim quote from line 829.
5. Anchor structure is SOURCE-DOUBLE-CITE-CO-PRIMARY with V_input + C_output explicitly tagged — **PASS**: §"Provenance — SOURCE-DOUBLE-CITE-CO-PRIMARY" tags ANCHOR-1 (input layer V — L3 spectral-functional evaluation domain; lizzi (a)-(d) ranking criteria) and ANCHOR-2 (output layer C — T3 transit-dynamics evaluation domain; volovik (a')-(d') SR-LO ODE side ranking criteria) with explicit STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY tag; per `.claude/rules/registry-landing.md` "Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)" all 3 conditions satisfied (sequential, non-fungible, both anchors must remain accessible).
6. Cross-citation links to CF-14..CF-19 are present — **PASS**: §"Cross-citation links to W-2 carry-forward priority queue" enumerates all six: CF-14 `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` (LANDED at S87 W2-1 with cited audit_sha256=`1f38f988...`); CF-15 `S87-ALPHA-S-CMB-S4-WATCH`; CF-16 `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE` (directly implements route iii); CF-17 `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` (directly implements route iv); CF-18 `S87-A4-A2-PIVOT-STATIONARITY-PIN` (route ii regulator-dependence pin); CF-19 `S87-PATH-H-PATH-C-INTERPOLATION` (route ii regulator-class extension).
7. `substantive_line_count(row) >= 15` — **PASS**: appended block contains channel header (1 line) + rank table (5 rows + headers ≈ 7 lines) + cross-domain convergence pin (verbatim quote + framing ≈ 5 lines) + provenance with 3 anchor declarations (≈ 6 lines) + 6-CF cross-citation block (6 bullets) + substrate framing block (≈ 5 lines) + verdict-line citation + deferred-install closure note. Total substantive line count ≈ 35 lines.
8. `audit_sha256` unique against all prior s87 verdict-file SHAs (sig_5 ladder) — **PASS**: pre-append grep of `s87_gate_verdicts.txt` confirmed `81dd63f045facce7268eed584071c7d4e6da2eae103a4e00ff5b75106d58131e` not present; uniqueness preserved against W9a-1 (`2502e00b...`) and W9b-1 (`42a79bfb...`) explicitly checked.

**4-route taxonomy ↔ substrate-IS observable cross-table**:

| Rank | Route | Substrate-IS observable | Upstream-dependency layer count |
|:----:|:------|:------------------------|:--------------------------------|
| 1 | (iii) | GGE-relic Bogoliubov mode-occupation distribution at horizon crossing; α_s = second logarithmic moment of variance | 1 (GGE-relic existence at horizon crossing) |
| 2 | (iv) | BdG spectral triple K-flow through K_sat ≈ 0.7·M_KK GGE-saturation crossover; α_s acquires δα(K)/α_FW = w_optical(K)·structural_coefficient | 2 (BdG triple correctness + K-running model framing) |
| 3 | (i) | Class I/II single-effective-pole acoustic-Goldstone propagator at substrate pivot; α_s extracted from moment-residue at u_pivot = 19649/351 in rational arithmetic | 3 (BDI universality + GAP-ANTIJENSEN-65 + kinematic optical-branch suppression triple-protection) |
| 4 | (ii) | Spectral action S(D_K, Λ) and (a_2, a_4) Seeley-DeWitt moment hierarchy; α_s extracted from 2-loop β-function for `(a_4/a_2)·(k*/Λ)²` | 4 (spectral-action hierarchy + regulator choice + (a_4/a_2) pivot-stationarity + 2-loop running consistency) |

The rank-ordering monotonically increases with upstream-dependency-layer count, providing a structural EVOI metric: lower-rank routes have fewer compounding dependency conditions whose joint satisfaction is required.

**Slot identity actually landed**: appended at EOF of `falsifier-master-inventory.md` as new top-level section after the W9a-1 audit-pin sub-rows block at lines 921-941. No rerouting required; pre-edit α_s scan ##=1, ###=2, ####=0 confirmed no parallel-writer collision. Append-only Python writer used (NOT Edit-tool round-trip per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race"); inventory pre-edit SHA `672da407bd5f26b7a1718ea8ace93271afbea0e832e8a7037ee8576d21bb5b60` → post-edit SHA `20d9a6e6cc55eff3e12ffa14e8efa312d61015dc2a206a4440c3545d7d623385`.

**Substrate framing** (per `phononic-framing.md` §"IS Space, Not IN Space"): The four α_s computation routes (i)-(iv) all probe the substrate's spectral structure on D_K's eigenvalue spectrum or its GGE-relic dynamical state — NOT properties of fields living in a container. Direction of explanation flows substrate → emergent: the substrate IS the GGE-relic Bogoliubov occupation-number variance at horizon crossing (route iii); the substrate IS the BdG spectral triple K-flow through GGE saturation (route iv); the substrate IS the single-effective-pole acoustic-Goldstone propagator at pivot (route i); the substrate IS the spectral action S(D_K, Λ) and its Seeley-DeWitt moment hierarchy (route ii). The rank `(iii) ≻ (iv) ≻ (i) ≻ (ii)` is a substrate-physical-robustness ordering — it reflects how many upstream structural assumptions each route makes. This rank-table entry is INVENTORY-only scope (a single-row anchor for downstream EVOI prioritization) — distinct from W9a-1's permanent-results-registry §VII.AH STAGE-1-CANDIDATE landing of the Joint F_2-Class Path-(c) Theorem (which requires Stage-2 two-agent independent-verify at S88+ via CF-59 before promotion to STAGE-3-PERMANENT). W9a-2 PASS does NOT place anything in `permanent-results-registry.md`; it only places the rank-table anchor in `falsifier-master-inventory.md`.

**Solution-space corridor effect**: PASS unblocks the W-2 α_s priority queue at S87+ — without this rank-table landed, downstream agents working on CF-14..CF-19 would re-derive the rank ordering ad-hoc, which would either (i) duplicate effort or (ii) silently introduce inconsistent prioritizations across parallel sessions. The single-row inventory entry is an EVOI bookkeeping anchor that prevents this drift. Specific downstream consequences: (a) CF-16 (route iii direct moment-independent computation) gets first-priority compute resources in any future α_s wave per its rank-1 status; (b) CF-17 (route iv K-running near K-sat) gets second-priority; (c) the single-pole-dependent routes (i)+(ii) — though structurally exact at substrate-pivot — get lower priority because substrate-physical robustness is the EVOI metric, not magnitude exactness alone.

**Artifacts**:

- Producing script: `computations/session-87/s87_w9a_alpha_s_route_rank.py` (~286 lines; append-only Python writer; scans ALL header levels [##/###/####] before append; computes dual-SHA over the input-pin map; sig_5 uniqueness check against W9a-1 and W9b-1 known SHAs + grep against the full verdict file)
- Inventory row: `sessions/framework/registry/falsifier-master-inventory.md` EOF block `## NEW α_s observational-channel section: T7-W9-FI-4 surviving-route rank table (S86 W-9 → S87 W9a-2)` (channel header + rank table + cross-domain convergence pin + SOURCE-DOUBLE-CITE-CO-PRIMARY provenance + 6-CF cross-citation + substrate framing + verdict-line citation + deferred-install closure note)
- Verdict line: `computations/session-87/s87_gate_verdicts.txt` canonical row + W9a-99 dual-SHA companion comment row
- Pre-edit / post-edit SHAs: inventory pre=`672da407bd5f26b7a1718ea8ace93271afbea0e832e8a7037ee8576d21bb5b60`, post=`20d9a6e6cc55eff3e12ffa14e8efa312d61015dc2a206a4440c3545d7d623385`
- Closure of deferred install T7-W9-FI-4 at `falsifier-master-inventory.md` line 883 (W-9 cluster)

**Open Questions for S88+**:

1. **M4 allowlist gap (orchestrator-only-edit)**: at runtime of this gate, `.claude/rules/methodology-wave-allowlist.md` did NOT contain `S87-A_S-SURVIVING-ROUTE-RANK-LANDING` row. Per the spawn-prompt orchestrator override: subagent edit is harness-denied per `methodology-wave-allowlist.md` §"Edit discipline" recursion-attack-closure protocol; this is flagged for orchestrator resolution. The verdict line + working-paper section + inventory row are all emitted; allowlist append is the orchestrator's residual fix-in-session task per `feedback_fix-in-session-never-defer.md`. Same situation as W9a-1; both gates need allowlist entries with `sha256_of_plan_block` over their respective §W9a-1 and §W9a-2 plan blocks.
2. **Route-iii implementation dispatch (CF-16)**: the rank-1 substrate-physical-robustness route is the next high-EVOI dispatch in the α_s observational queue. CF-16 (`S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE`) is GPU-eligible 1-2 days; PASS hardens Branch (A) to multi-route closure (route iii agreement with route i to 1e-3 absolute on `α_s_FW = -0.06896799`).

---
"""


W9A_3_NEW = """### §W9a-3. S87-DEFERRED-OPEN-Q-7-8 (mack-cosmic-bridge)

**Status**: COMPLETE — DOCUMENTATION-only stub registration of Q-7 (cross-region 4×4 partition application) + Q-8 (per-class N_breakdown observable forward-modeling) per `feedback_fix-in-session-never-defer.md` 4-field schema. NO verdict line emitted at S87 (DOCUMENTATION-only per plan §W9a-3 Field 9). Sub-decomposed gates at S88 W0 cleanup will carry their own verdict lines if scoped.
**Gate ID**: `S87-DEFERRED-OPEN-Q-7-8` (composite placeholder; sub-decomposes at S88+ to `S88-OR-LATER-Q-7-CROSS-REGION-PARTITION-APPLICATION` + `S88-OR-LATER-Q-8-PER-CLASS-N-BREAKDOWN-FORWARD-MODELING` if a successor agent commits to scoping).
**Trigger**: `N/A-at-S87` (documentation-only; sub-gates carry triggers at S88+).
**Classification**: **DOCUMENTATION-only-at-S87** (NOT METHODOLOGY-class; NOT COMPUTE-class; NOT MIXED-class — no PASS predicate is pre-registered at S87; the wave-classification audit returns NULL-classification with a documentation-only flag).
**Agent**: `mack-cosmic-bridge` (this dispatch; S88+ owner TBD per W-9 CF-7..8 source attribution — candidate owners include lizzi+transit, gen-physicist, or mack-cosmic-bridge depending on which sub-question is scoped first).
**Hypothesis**: Open-Q 7 + Open-Q 8 (per S86 W-9 carry-forward) are spec-frozen as 4-field stubs at S87 with explicit pre-conditions for S88+ dispatch, consistent with `feedback_fix-in-session-never-defer.md` requirement that every synthesis MUST produce structured carry-forward specs for genuine future work.
**Plan reference**: `sessions/session-plan/session-87-plan-w9a.md` §W9a-3 (Field 5 + Field 6 stub specifications).

**MCP Pre-Compute Audit**: N/A — this is a documentation-only stub registration, no compute or threshold evaluation. No MCP queries needed beyond the W9a-2 audit (which served as upstream context).

**Verdict**: N/A at S87 (DOCUMENTATION-only). At S88+ each sub-decomposed gate will emit its own canonical 4-tuple per its scoped pre-registration.

**Results — 4-field carry-forward stubs**:

#### Q-7 stub: cross-region 4×4 partition application

| Field | Specification |
|:------|:--------------|
| **What** | Apply the 4×4 partition template (V_4 monodromy + Klein-four sharpening from S86 W-12 CF-66 / CF-67 priority-1 / priority-2 landings) to a NEW substrate region beyond the τ_fold neighborhood. Candidate regions: (a) deep IR of D_K spectrum (lowest 20 eigenvalues at L_max=12); (b) UV cascade region near L_max=14-15 spectral-asymptotic regime (per CF-68 stratum-3 L_max scan precedent); (c) the BCS-Pomeranchuk corridor region (per S35-37 closed-mechanism chain). Goal: test whether the 4-stratum partition stability observed at τ_fold is a LOCAL feature of the fold's first-order phase transition OR a GLOBAL invariant of D_K's eigenvalue partition structure. PASS at S88+ extends V_4 partition stability from a τ_fold-local feature to a more general substrate invariant (high structural impact). |
| **Inputs** | (i) S86 W-12 V_4 monodromy + Klein-four sharpening landings (CF-66 priority-1 V_4 explicit + CF-67 priority-2 4-stratum stability + CF-68 priority-3 stratum-3 L_max scan — CHECK these have landed at S87 close before scoping Q-7 at S88); (ii) `s84_spectrum_cache_L12_tau019.npz` (existing L_max=12 spectrum cache for region (a) deep-IR application); (iii) candidate L_max=14-15 cache (NOT YET COMPUTED at S87 close; CF-10 deferred — required for region (b) UV cascade); (iv) BCS-Pomeranchuk corridor data (S35-37 closed-mechanism chain artifacts — required for region (c)); (v) `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness — Pole-Scope sub-clause" (T1-20) — pre-register pole-scope and resolution-scope at the new region BEFORE running. |
| **Gate** | At S88+ when scoped: `PASS` iff the 4×4 partition template applies cleanly at the new region (4-stratum stability with V_4 monodromy and Klein-four sharpening reproduced at the new region's substrate scale). `FAIL` iff the partition structure differs (e.g., 5-stratum or non-V_4 monodromy at the new region — indicating τ_fold-locality of the 4-stratum feature). `INFO` iff partial reproduction (4 strata observed but V_4 monodromy not crisp). The gate carries an inherent V_4-vs-Z_4 verifier-rubric Class-8.2 PRU risk per `epistemic-discipline.md` §"PRU Class-8 sub-class taxonomy formal extension" (S86 W-12 calibration); the rubric pattern set MUST be pre-registered (`V_4` as 4-element Klein four-group with element orders [1,2,2,2] vs `Z_4` cyclic with element orders [1,2,4,4]) — disjunctive "or similar" tokens FORBIDDEN. |
| **Effort** | 0.5-2.0 wave-equivalents at S88+ depending on which candidate region is scoped: (a) deep IR ~ 0.5 wave (existing L_max=12 cache; ~1 day GPU); (b) UV cascade region ~ 1.5-2.0 waves (requires L_max=14-15 cache regeneration; multi-day GPU); (c) BCS-Pomeranchuk corridor ~ 1.0-1.5 waves (requires re-running closed-mechanism chain artifacts in spectral-decomposition basis). |

#### Q-8 stub: per-class N_breakdown observable forward-modeling

| Field | Specification |
|:------|:--------------|
| **What** | Forward-model the per-class N_breakdown observable for each of the 5 L1-classes (per CF-42 W-7 CF-1 dual-prior pre-registration). N_breakdown is the SR-LO ODE breakdown e-fold count that signals the regime-of-validity boundary for the slow-roll-in-leading-order expansion (per S86 W5a-2 SR-LO BREAKDOWN regime_verdict precedent: sign_verdict=PASS / magnitude_verdict=FAIL / regime_verdict=BREAKDOWN composite). Goal: predict the SR-LO breakdown e-fold count for each L1-class as a falsifier-class observable; contrast with the canonical SR-LO breakdown at the canonical xi_E_GGE_inv = 13.642473425595973 from W4 P4 commit. PASS at S88+ closes the per-class N_breakdown observable as a falsifier-class quantity for the SR-LO BREAKDOWN regime — directly addressing the S86 W5a-2 composite that motivated the Schema-v2 verdict-vocabulary extension at `.claude/rules/gate-verdicts.md` §"S87+ canonical form". |
| **Inputs** | (i) CF-42 W-7 CF-1 per-class IC verification at xi_E_GGE_inv values (PRE-REQUISITE: CF-42 must complete at S87+ before Q-8 can be operationalized); (ii) SR-LO ODE source `computations/_shared/_sr_lo_ode_solver.py` (or equivalent S86 W5a precedent script `s86_w5a_p3_sector_1_sr_flow.py` — same 4-component coupled SR-LO ODE: ε, η, α_s, ξ²-flow); (iii) canonical xi_E_GGE_inv = 13.642473425595973 from W4 P4 commit (`canonical_constants.py` entry; verified per `substrate-first-canonical-sourcing.md` Class-(f) HARD-HALT precedent: placeholder O(10⁻²) FORBIDDEN, canonical substrate-natural anchor 59.8·Δ_BCS/K_base required); (iv) S86 W5a-2 BREAKDOWN regime_verdict audit trail (`computations/session-86/s86_gate_verdicts.txt:S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55`); (v) S86 path-(c) double-double-fail reassessment regulator-class N_breakdown values (Zubarev=∞, anomaly=0.736, F_2=0.122, cutoff_sqrt=0.178) for cross-check baseline. Cross-link to W9b-1 N_breakdown_R{i} canonical-write-order carry-forward (per W9b-1 §W9b-1 results section noting the per-L1-class extension of the regulator-class N_breakdown taxonomy). |
| **Gate** | At S88+ when scoped: `PASS` iff per-class N_breakdown forward model predicts (within pre-registered band) the per-class breakdown e-fold count when CF-42 returns the per-class IC verification data. `FAIL` iff predictions diverge from CF-42 outcomes by > 50% (BREAKDOWN regime_verdict per Schema-v2 collapse rule). `INFO` iff predictions are within order-of-magnitude but not within tight band (5-50% relative deviation; MARGINAL regime_verdict). Gate carries `[SIGN]`-trigger candidate (per-class N_breakdown forward model predicts a directional shift from canonical N_breakdown; the substitution chain MUST be written explicitly at scoping time per `math-scripts.md` §"Double-Check Logic Before Compute"). Auto-shortening clause discipline applies: the cross-check domain MUST be the full intended e-fold range or `regime_verdict = MARGINAL or BREAKDOWN` MUST be emitted (per `gate-verdicts.md` §"Auto-shortening clause discipline"). |
| **Effort** | 0.5-1.5 wave-equivalents at S88+ (pure forward-modeling — once CF-42 closes, the per-class N_breakdown computation is a single-script dispatch with per-class scan; PASS-band pre-registration is the higher-leverage discipline). GPU-eligible (SR-LO ODE with 4-component coupled state, per-class scan over 5 L1-classes; ~1-2 days). |

**Aggregate solution-space meaning** (from plan §W9a-3 Field 11):

- **At S87**: stub registration ensures Q-7 and Q-8 are NOT lost — per `feedback_fix-in-session-never-defer.md`, every synthesis MUST produce structured 4-field carry-forward specs for genuine future work. Without this stub, the S86 W-9 CF-7..8 open questions would be effectively lost (`session-handoffs.md` §"Recommendation Carry-Forward": *"If a recommendation is not planned in the next session, it is effectively lost"*).
- **At S88+ when scoped**: Q-7 PASS extends the V_4 partition stability finding from a τ_fold-local feature to a more general substrate invariant (high structural impact). Q-8 PASS closes the per-class N_breakdown observable as a falsifier-class quantity for the SR-LO BREAKDOWN regime — directly addressing the S86 W5a-2 sign_verdict=PASS / magnitude_verdict=FAIL / regime_verdict=BREAKDOWN composite that motivated the Schema-v2 verdict-vocabulary extension.
- **Solution-space corridor effect**: Both Q-7 and Q-8 expand the framework's falsifier inventory in directions orthogonal to the current S87 W-9 trio (Path-(c) successor anchor + α_s rank). Q-7 probes the 4-stratum partition's locality vs globality (substrate-structural axis); Q-8 probes the SR-LO breakdown regime's per-class structure (substrate-dynamical axis). Together they fill out the "what does the 4×4 partition framework actually predict observationally" question that the S86 W-12 V_4 / Klein-four landings opened.

**Substrate framing reminder**: Both Q-7 and Q-8 are intra-substrate (no container-thinking risk by construction):

- Q-7 partitions D_K's eigenvalue spectrum at NEW substrate regions; the partition is the substrate's own structure.
- Q-8 forward-models the SR-LO ODE on per-class IC values; the SR-LO ODE is a substrate-dynamical equation, NOT a GR-on-curved-spacetime equation.

When scoped at S88+, the producing dispatch must verify substrate-framing in the verbatim threshold text per `.claude/rules/phononic-framing.md`, and must verify substrate-first canonical-sourcing for all per-class IC values per `.claude/rules/substrate-first-canonical-sourcing.md` §(v) Class-(f) PIN-PLACEHOLDER detection.

**Prerequisite-closure tracking** (per plan §W9a-3 YAML preregistration block):

- CF-66 (priority-1 V_4 explicit) — for Q-7 substrate-anchor
- CF-67 (priority-2 4-stratum stability) — for Q-7 substrate-anchor
- CF-68 (priority-3 stratum-3 L_max scan) — for Q-7 candidate-region (b) UV cascade
- CF-10 (deferred; L_max=14 cache regeneration) — for Q-7 candidate-region (b)
- CF-42 (W-7 CF-1 per-class IC verify with dual-prior footnote) — for Q-8 input data

S88 W0 cleanup pass MUST validate the closure state of each of these prerequisites at S87-close and decide which sub-question (Q-7 vs Q-8) to scope first based on which prerequisites are closed. Decision-tree:

1. If CF-42 closed at S87+: Q-8 is dispatch-eligible (route to gen-physicist or transit-dynamics-theorist owner per dual-prior pre-registration).
2. If CF-66 + CF-67 + CF-68 all closed at S87+: Q-7 region (a) deep-IR is dispatch-eligible (route to lizzi+transit owner).
3. If CF-66 + CF-67 + CF-68 + CF-10 all closed: Q-7 region (b) UV cascade is dispatch-eligible (higher effort).
4. If only CF-66 + CF-67 closed: Q-7 partial dispatch on region (a) only with explicit "deep-IR-only scope" pre-registration.
5. If neither prerequisite chain is fully closed: Q-7 + Q-8 remain in stub state; revisit at S89+ W0.

**Artifacts**:

- §W9a-3 working-paper section (THIS section) carries the 4-field stubs for Q-7 + Q-8.
- NO verdict line at S87 (DOCUMENTATION-only).
- NO `computations/session-87/s87_w9a_*.py` script for §W9a-3 (no compute scope at S87).
- Cross-references: `feedback_fix-in-session-never-defer.md`; `output-standards.md` §"Action Items Format" 7-component; `output-standards.md` §"Carry-Forward Dependency Enumeration" T1-14 extends "Depends on" with explicit prerequisite enumeration (the prerequisite-closure tracking block above satisfies this).

**Open Questions for S88+**:

1. **S88 W0 cleanup pass on prerequisite closures**: validate which of CF-42, CF-66, CF-67, CF-68, CF-10 closed at S87-close; decide which sub-question to scope first per the decision-tree above; sub-decompose this composite gate to the appropriate `S88-OR-LATER-Q-7-CROSS-REGION-PARTITION-APPLICATION` and/or `S88-OR-LATER-Q-8-PER-CLASS-N-BREAKDOWN-FORWARD-MODELING` gates with full PRDR machinery pin (none required at S87 stub level).
2. **Owner assignment**: per dual-prior pre-registration in plan §W9a-3 Field 4, owner candidates include lizzi+transit (Q-7 cross-region), gen-physicist (Q-8 forward-modeling cross-reviewer), or mack-cosmic-bridge (carry-forward synthesis). Decision deferred to S88 plan-author once prerequisite states are known.

---
"""


def main():
    if not WP_PATH.exists():
        raise SystemExit(f"FATAL: working paper not found at {WP_PATH}")

    text = WP_PATH.read_text(encoding="utf-8")
    pre_size = len(text.encode("utf-8"))  # (local)

    # Locate the §W9a-2 stub block (from "### §W9a-2." to the next "---" line preceding §W9a-3)
    w9a2_stub_start_marker = "### §W9a-2. S87-A_S-SURVIVING-ROUTE-RANK-LANDING (mack-cosmic-bridge)"
    w9a3_stub_start_marker = "### §W9a-3. S87-DEFERRED-OPEN-Q-7-8 (mack-cosmic-bridge)"
    w9b1_start_marker = "### §W9b-1. S87-RESCALED-IC-SR-LO-RERUN"

    idx_w9a2 = text.find(w9a2_stub_start_marker)
    idx_w9a3 = text.find(w9a3_stub_start_marker)
    idx_w9b1 = text.find(w9b1_start_marker)
    if idx_w9a2 < 0 or idx_w9a3 < 0 or idx_w9b1 < 0:
        raise SystemExit("FATAL: section markers not found")

    # Replace block: from idx_w9a2 to idx_w9b1 (exclusive). The W9A_2_NEW + W9A_3_NEW
    # texts include their trailing "\n---\n" separators.
    new_block = W9A_2_NEW + "\n" + W9A_3_NEW + "\n"

    new_text = text[:idx_w9a2] + new_block + text[idx_w9b1:]
    post_size = len(new_text.encode("utf-8"))  # (local)

    WP_PATH.write_text(new_text, encoding="utf-8")
    print(f"WP patch applied: pre_size={pre_size} bytes, post_size={post_size} bytes (delta={post_size - pre_size})")
    print(f"§W9a-2 + §W9a-3 sections written in-place.")


if __name__ == "__main__":
    main()
