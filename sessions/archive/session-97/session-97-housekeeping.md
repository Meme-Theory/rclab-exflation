# Session 97 Housekeeping Ledger

**Date**: 2026-05-30
**Session**: 97
**Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"`

## Q2 marker (citation)

A candidate is Q2 iff its resolution is a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation that produces a new structural claim. See the rule §"Q2" for the full marker list.

> **Population status**: Waves 1–6 ALL populated (per-wave writes at each `/rclab-coordinate` close). Session compute complete (20/20 gates); session-close items (`/weave --update`, capstone §6.3/§7.3/§8.5 designated-writer prose reconciliations) append at the closing-synthesis pass.

---

## §A. In-session resolutions (already effected; ledger only)

Per `feedback_fix-in-session-never-defer.md`: items FIXED during S97 wave compute. Each row cites the surfacing wave/gate, the resolution edit, and the gate's verdict-line audit_sha256 short.

| # | Source wave / gate | Item | Resolution (file:lines) | Verified at (audit short) |
|:--|:-------------------|:-----|:------------------------|:---------------------------------|
| A1 | W1-§W1-2 / S97-W1-XTODAY | Promote `x_fold = 85.7928` (S67 ODLRO origin) to canonical — referenced from session text; confirmed-used by 1.2. Clean single-value ⇒ fix-in-session per `math-scripts.md §"Canonical Write-Order"`. | `canonical_constants.py` SECTION E (`update_constant`); PROVENANCE added | `067fe807` |
| A2 | W1-§W1-1 / S97-W1-OMEGA-PROFILE | Promote `Omega_BA_fold = 2.241353` (S95-W4-4) to canonical; reproduced by 1.1 to rel 1.5e-4. Clean single-value ⇒ fix-in-session. | `canonical_constants.py` SECTION E (`update_constant`); PROVENANCE added | `6fee3fdf` |
| A3 | W1 cluster (1.1/1.3/1.4/1.5) | Atlas-04 C1 register row was STALE (referenced the Ω-profile gate as pending). Updated with S97 W1 findings (Ω delivered / explicit AOFT a(t) / route-sensitivity / κ consistency-pin); status HELD ASSUMED. | `sessions/framework/Atlas/atlas-04-assumptions.md:60` | n/a (register row) |
| A4 | W1 cluster (capstone-hygiene gate) | Ran the 5-question capstone-hygiene gate. **Q1=YES** (a(t) gap) → Atlas-04 C1 reconciled in-session (A3); §6.3 PROSE enrichment routed to session-close designated-writer (note below). **Q2=NO. Q3=NO** (C1 stays ASSUMED; no over-claim drift ⇒ K-counter does NOT advance). **Q4** ledger-updated-in-session. **Q5=NO.** | `session-97-housekeeping.md §A` + `session-97-w1-workingpaper.md §"Wave 1 Synthesis"` | n/a |
| A5 | W2-§W2-2 / S97-W2-2-C10-N-EXPONENT | Atlas-04 C10 row updated with the W2-2 SHARPENING (exponent-on-q=2 SUBSTRATE-DERIVED via quadratic V at the q-stationary minimum, k=+3586.5 from 992 D_K modes; relaxation-linearity = simple-fluid input; GGE correction D_K-bounded). Status HELD ASSUMED-PARTIALLY-PROVEN (no PROVEN flip — 2.2 did not clean-PASS). | `sessions/framework/Atlas/atlas-04-assumptions.md:69` | `b69da9f4` |
| A6 | W3-§W3-2 / S97-BARYOGEN-EXT-SOURCE | Atlas-04 C6 row updated: frontier #9 LOCATED → SOURCED (φ_88-Cartan non-LI δA, existence PASS, σ_supp posit-fixed). Status HELD CONDITIONAL (existence, not uniqueness). | `sessions/framework/Atlas/atlas-04-assumptions.md:65` | `b8a6e9ed` |
| A7 | W2/W3 (capstone-hygiene gates) | Ran the 5-question gate for W2 + W3. **W2 Q2=YES** (W2-3 EP-signature sign-stable + FI through N3LO) → routing recorded: mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`) to annotate the §7 EP-falsifier row, lands in the mack-owned **Wave 4** coordination. **W2 Q3=NO** (C10 held, A5). **W3 Q1/Q2/Q3=NO** (C6 evidence-update, A6, not a §7 cell; no status flip). | `session-97-housekeeping.md §A` + W2/W3 WP syntheses | n/a |
| A8 | W2/W3 (process observations) | (i) `canonical_constants.py` SHA drift `cc7d1d26→838c7145` from W1 add-only promotions (A1/A2) — flagged by W2-1 + W2-3, Class-(c) content-edit-only, consumed values canonical, benign. (ii) W2-2 + W3-2 cleaned up intra-dispatch dev-iteration verdict lines (W3-2 one a latent sig_5 duplicate) — end states orchestrator-verified sig_5-clean; W2-2 added an idempotency guard to its producing script (forward fix). (iii) W3-1 corrected a plan substitution-chain Def-3 conflation in-session (used actual S96 R_direct=Δm²₃₂/Δm²₂₁). | W2/W3 WP syntheses + Constraint-Map | n/a |
| A9 | W4 (mack §7/inventory landings) | mack-cosmic-bridge (sole writer) landed three §7-surface rows in `falsifier-master-inventory.md`: Row #7.audit-4 (127-OOM Ω_GW closure, both legs substrate-sourced, placeholder `Omega_GW_Lambda_A_LISA=1e-10` RETIRED, LISA-STERILE; supersedes #7.audit-3 PENDING-SUBSTRATE-RECOMPUTE); Row #75 (W2-3 EP-signature, NEW; Δκ^N3LO sign-stable+FI); BF_spine register annotation (W4-4, DECISIVE 2.0×10² model-class). Verified on disk lines 1618/1656/1691. | `sessions/framework/registry/falsifier-master-inventory.md:1618,1656,1691` | `71fbc18f`/`c63d3869`/`0713c964`/`8f4f9abb` |
| A10 | W4 (capstone-hygiene + designated-writer flags) | Ran the 5-question gate for W4. Q2 effected via A9 (mack inventory). Q4 — TWO capstone §7.3 NARRATIVE-PROSE items FLAGGED for the session-close designated writer (NOT orchestrator/mack-edited): (1) insert `BF_spine=2.0×10² DECISIVE` into the §7.3 scorecard narrative; (2) reconcile the §7.3 "SNR~10¹³ RETIRED" callout amplitude to `4.046e-132`. Q5 — `canonical_constants.py` PROVENANCE-comment marking `Omega_GW_Lambda_A_LISA=1e-10` SUPERSEDED flagged for the designated-writer pass (import preserved). ALSO: σ₈ channel-keyed canonical promotion (`sigma8_OZ`=0.799 vs `sigma8_growth_a2`=0.79317) routed to W6 (sub-keying ambiguity ⇒ not a single-value fix-in-session, per `math-scripts.md §"Canonical Write-Order"`). | `session-97-housekeeping.md §A` + W4 WP synthesis; capstone §7.3 flags → session-close designated-writer | n/a |
| A11 | W5-§W5-1 / S97-DK-DF-STAGE2 | §VII.BK D_K≅D_F controlled recovery PROMOTED STAGE-1-CANDIDATE → STAGE-3-PERMANENT (joint-theorem-promotion Stage 3 orchestrator registry-state edit; Component-B two-agent cross-axis Stage-2 PASS-AND both axes [connes NCG + volovik substrate], composite PASS). Header + Status block + summary-table row flipped. ALSO: the §VII.BK summary-table row was ADDED (the landing agent's body-only write left a registry-vs-table drift the VII-SLOT-AUDIT hook caught — fixed in-session, orchestrator-direct mechanical mirror per Hard-Rule-2). | `sessions/permanent-results-registry.md` (§VII.BK entry + table row) | `abd12741` (composite) |
| A12 | W5-§W5-1 (allowlist) | METHODOLOGY-class allowlist row appended for `S97-DK-DF-STAGE2` COMPONENT-A (sha256_of_plan_block `78497501f46e9e2e…`) + paired rationale; orchestrator-only edit (recursion-attack closure), classification CONFIRMED by the W5 plan §M1-M4 table; via single-shot append helper. | `methodology-wave-allowlist-ledger.md` + `methodology-wave-instances.md`; helper `computations/session-97/s97_w5_allowlist_append_helper.py` | n/a |
| A13 | W5 (capstone-hygiene + process) | Ran the 5-question gate for W5: Q1–Q5 all NO for the CAPSTONE (the §VII.BK promotion is a §VII registry-state edit per A11, not a capstone-prose change; 5.3 horizon-thermo is INFO/ratio-inherited, no §7 row). Process observations: (i) W5 WP 6-writer token-bleed race (4 gates + 2 Stage-2 reviews) — mitigated by agent marker-anchored atomic-splice writes; WP integrity orchestrator-verified (all sections intact); (ii) cosmetic ROCm `offload-arch` warning at torch init on the spaced project path (W5-2/W5-4), GPU verified working (`cuda.is_available()=True`, rank-15 result) — environment quirk, not fixable from code; (iii) slot-reroute §VII.BH→§VII.BK (plan pin occupied at runtime, fixed-in-session per Registry-Write-Hygiene). | W5 WP synthesis + Constraint-Map | n/a |
| A14 | W6-§W6-1/§W6-2 (allowlist) | Two METHODOLOGY-class allowlist rows appended: `S97-W6-1-OMDM-RHOVAC-PINS` (sha256_of_plan_block `6210658c…`) + `S97-W6-2-PETROV-ANNOTATION` (sha `efd8312e…`) + paired rationales; orchestrator-only (recursion-attack closure), classification CONFIRMED by the W6 plan §"METHODOLOGY-class classification (both gates)" M1–M3; single-shot helper. | `methodology-wave-allowlist-ledger.md` + `methodology-wave-instances.md`; helper `computations/session-97/s97_w6_allowlist_append_helper.py` | n/a |
| A15 | W6 (canonical promotions + capstone-hygiene + Petrov) | W6-1 PASS promoted 2 canonical pins (`Omega_DM_h2=0.1200` OBSERVATIONAL-ANCHOR lab-IN, DISTINCT from `Omega_DM_obs=0.264`; `rho_vac_over_rho_obs=1.032` FRAMEWORK-PREDICTION, DILUTION-CC-66, C10 conditionality carried) — `x_fold`/`Omega_BA_fold` verified-present-not-re-added, σ₈ out-of-scope. W6-2 INFO Petrov annotation resolution (b) value-field-governs (S96 canonical lines byte-for-byte untouched; `computations/session-96/s96_gate_verdicts.txt` governs-note appended). Capstone-hygiene 5-question gate (W6): Q1–Q5 — the C10 conditionality on ρ_vac/ρ_obs is CONSISTENT with the W2-2 Atlas-04 C10 sharpening (A5) + the already-routed §8.5 designated-writer flag (A4 note), no new C10 action. | `canonical_constants.py` (2 pins + PROVENANCE) + `computations/session-96/s96_gate_verdicts.txt` + W6 WP | `4ec12df8`/`cbcbbd11` |
| A16 | W-1 workshop (S97-investigate; mack+volovik composite-collapse adjudication) | **§8.5 capstone C10 prose disposition — RECOMMENDATION for the capstone designated writer** (capstone-hygiene-gate Q3/Q4): §8.5 prose tag MUST equal the register tag (Atlas-04 C10 = `ASSUMED-PARTIALLY-PROVEN`); narrate C10 as **enriched-not-closed** — INFO label, NEVER "closed"; adopt the **two-layer STRUCTURAL-ORTHOGONAL-COMPANION** framing (Layer-1 curvature-degree-2 `k=+3586.5` CONFIRMED algebra-INVARIANT / Layer-2 sub-leading-sign+BBN PENDING algebra-DEPENDENT) + the **three-object decomposition** (A curvature-degree DONE / B sub-leading-sign on CF-MK3-1 / C relaxation-closure on CF-S98-W2-2-RELAXATION-CLOSURE — only C moves the tag). Q4: this is a PROSE claim → designated-writer reviewed patch, NOT mack's edit and NOT a bulk install-agents append. mack is §7-falsifier-surface sole writer only (`feedback_mack-bridge-role.md`), NOT §8.5 prose owner — hence RECORDED here, capstone prose NOT touched this session. | recommendation recorded in §A (in-session effected: the routing note); target `sessions/framework/phonic-exflation-equation.md` §8.5 (NOT edited) | n/a (designated-writer routing, not a gate) |
| A17 | W-2 workshop (S97-investigate; connes×kk generation-blindness vs reality-axiom adjudication) | **Three NON-MATH landings effected in-session** (workshop CONVERGED R3; verdict (X)-specific TRUE, A+JAJ⁻¹ cannot split t=1/t=2, E1 STAGE-1-CANDIDATE): (1) **§VII.BL** registry slot landed via the append-protocol next-free-letter scan (highest prior §VII.BK) — Generation-Blindness Obstruction theorem (E1, Non-LI-Deformation-Necessity), classified **INTRA-PILLAR OBSTRUCTION + NON-PROMOTION-BY-HELD-NUMBER overlay** (sign-lock differentia; Level-2 NON-BINDING/structurally-exact — NOT a 5-anatomy convergence bridge, so it clears the plan-freeze HARD-HALT auditor), STAGE-1-CANDIDATE, SOURCE-DOUBLE-CITE-CO-PRIMARY on Corner I, Stage-0 clause attribution (a/b/f connes, c kk, d/e JOINT), closure SHA `656ea882…`. (2) **§28** named-precondition "Non-LI-Deformation Necessity" SUGGESTION K=2 (#7 Yukawa + #9 baryogenesis inaugural instances) landed in `cross-pillar-bridge-corpus.md` (directive + per-instance calibration in the CORPUS per `feedback_rules-directive-only-no-session-info.md`). (3) **knowledge-MCP** non-rediscovery: `R_cross_yukawa_t1_t2=1.019704` registered via `update_constant` (was absent; future "Yukawa hierarchy degeneracy" queries now resolve to §VII.BL/E1). | `sessions/permanent-results-registry.md` §VII.BL (line ~21026); `sessions/framework/registry/cross-pillar-bridge-corpus.md §28` (line ~1944); `canonical_constants.py` SECTION E (`R_cross_yukawa_t1_t2`) | `656ea882` (workshop verdict closure); registry §VII.BL header + SHA Read-verified unique on disk |

**A4 §6.3 session-close note (captured so it is not orphaned).** The capstone-hygiene gate "Run at session-close" timing means the §6.3 curated-prose reconciliation is a designated-writer reviewed patch at S97 session-close (full-session C1 evidence), NOT an orchestrator bulk append (per `feedback_framework-hygiene.md` + §Q4). No over-claim DOWN-tag is owed (§6.3 already narrates the a(t) gap as open). Required ENRICHMENT verbatim: §6.3's forward-reference "the Ω(τ) profile (S97 prerequisite gate) remains the open object that closes both…" is superseded — Ω(τ) DELIVERED (S97-W1-OMEGA-PROFILE PASS), explicit AOFT a(t) ASSEMBLED (S97-W1-1-AT-TRAJECTORY INFO), κ pinned at κ_nat (S97-COOLING-BUDGET-KAPPA-PIN PASS, consistency-identity), route-invariance FAILED (S97-W1-QOMEGA-ROUTE-INVARIANCE INFO, route-SENSITIVE). The gap is now CHARACTERIZED; the open object is the route-reconciliation (CF-S98-W1-ROUTE-RECONCILIATION). Substrate-first framing preserved.

**A4 §6.3 word-choice supplement (S-1 hawking-theorist licensing-scope synthesis, 2026-05-31).** The §6.3 a(t) seconds-normalization status word for the designated writer is **"consistency-pinned to κ_nat"** (or "pinned by M_KK-unit consistency"), NEVER bare "pinned." Reason (capstone-hygiene §Q3 register-faithfulness): the κ recovery is a unit-consistency IDENTITY (`S97-COOLING-BUDGET-KAPPA-PIN` value-string `identity_forced_by_MKK_unit_consistency=True`; both legs agree 0.0e+00 in the same M_KK unit system), NOT an independent triangulation — bare "pinned" reads as *determined* and would let an identity masquerade as a measurement. Licensing-scope findings the §6.3 prose may draw on: (i) κ_nat resolves the 1.4 a(t) trajectory's 1-parameter *seconds-SCALING* only — the 50-shape τ̇ NON-uniqueness (`taudot_unique_selection=False`, n_admissible=50) is UNTOUCHED and deferred to CF-S98-W1-ROUTE-RECONCILIATION; (ii) Wave-4 Ω_GW amplitude/IR-tail may fix κ=κ_nat because W6-5 demonstrated κ-ROBUSTNESS (not because κ is independently determined), while frequency-axis observables (CGWB peak freq, κ-dependent redshift) MUST carry the consistency-pin caveat. C1 stays ASSUMED (no up-tag from a consistency-identity). Full adjudication: `sessions/archive/session-97/session-97-hawking-theorist-synthesis.md`. Routing to mack-cosmic-bridge (sole writer of the §7 falsifier surface): any Wave-4 Ω_GW inventory row consuming κ should tag amplitude observables "κ-fixed (robust)" and frequency observables "κ-fixed (consistency-pin; carry caveat)" — recorded here for mack's pass, NOT orchestrator-edited into the §7 surface.

---

## §B. Hygiene-promotion compute carry-forwards (4-field spec; mirrored to WP CF)

> The MATH carry-forwards (NOT Q2 hygiene) live in their wave WPs and are consumed by `/rclab-plan` directly: CF-S98-W1-ROUTE-RECONCILIATION (W1 WP), CF-S98-W2-2-RELAXATION-CLOSURE (W2 WP), CF-S98-W3-1-YUKAWA-NONLI-FLUCTUATION + CF-S98-W3-2-BARYOGEN-UNIQUENESS (W3 WP), CF-S98-W4-4-OQ3-COVARIANCE (W4 WP). W5 produced no CF (all conditional CFs' triggers did not fire). The W2-3 §7 EP-falsifier annotation (A7) was a within-session routing to mack's Wave 4, not an S98 CF. One Q2-hygiene §B item:

### CF-S98-HK-SIGMA8-CHANNEL-KEYED-PINS — promote the two channel-keyed σ₈ values to canonical [Q2-hygiene]

> **Routing note**: Q2-class hygiene per `Investigating-Workshops.md §"Q2"`; surfaced by S97 W4-3. Mirrored to `session-97-w6-workingpaper.md §"Carry-Forward Computations"`. NOT a workshop.
> **Why not §A (fix-in-session)**: sub-keying ambiguity — two distinct framework σ₈ channels (`SIGMA8-OZ-50`=0.799 S50 spectral-action vs S70/S96 a₂ growth-channel=0.79317), no `sigma_8_FW` canonical pin, canonical naming/keying convention better pre-registered at S98 plan-freeze (per `math-scripts.md §"Canonical Write-Order"`: sub-keying ambiguity ⇒ carry-forward, not single-value fix-in-session).

1. **What**: promote `sigma8_OZ_50=0.799` + `sigma8_growth_a2=0.79317` to `canonical_constants.py` SECTION E with channel-distinct provenance + cross-note.
2. **Inputs**: SIGMA8-OZ-50 (S50, knowledge MCP); S70/S96 a₂ growth-channel σ₈; `s97_fsigma8_forecast_refetch.npz` (W4-3, audit `a20043e7`).
3. **Gate**: `S98-HK-SIGMA8-CHANNEL-KEYED-PINS` METHODOLOGY-class — `get_constant` resolves both with non-empty channel-distinct PROVENANCE + cross-note (allowlist row at S98 plan-freeze).
4. **Effort**: < 0.1 wave.

---

## §C. Parallel-compute-wave carry-forwards (Q3 wave-together; mirrored to WP CF)

(none)

---

## §D. Methodology-rule extensions (M1-M4 + allowlist; mirrored to WP CF)

- **D1 (S97 W-1; mack+volovik composite-collapse adjudication)** — Composite-collapse **CORE-vs-fringe override-clause CANDIDATE** (4 guards: i CORE-confirmed / ii conditional-antecedent-falsified-not-violated / iii magnitude-bounded / iv recovery-direction-normalization-invariant-OR-observable-declared). **K=1 SUGGESTION, NOT minted this session** (K=3 promotion contract per `feedback_rules-compensate-missing-structure.md`). The candidate clause COMPOSES WITH the `gate-verdicts.md` schema-v2 composite-collapse rule (`elif sign_verdict==FAIL: composite=FAIL`); it does NOT modify it — a post-hoc edit of that rule would be a `v3-closure-recovery.md` PROHIBITED_ACTIONS Class-3 violation (the firewall is preserved this session). Calibration instance #1 = `S97-W2-2-C10-N-EXPONENT` (`sign=FAIL` n_eff 1.978<2 / `magnitude=PASS` |C_meas|/2=0.0109<0.05 / `regime=VALID`; label INFO via gate semantic; all 4 guards verified) — LANDED in `sessions/framework/registry/pru-class-corpus.md §19` (calibration-instance home per `feedback_rules-directive-only-no-session-info.md`: session calibration goes to the corpus, NEVER the rule file). Classification: M3-class (methodology-rule extension); both W-1 agents AGREE on the clause content ⇒ registry-state/calibration, NOT adversarial physics — routed here per `Investigating-Workshops.md` Q2, NOT to a workshop. Allowlist: N/A (corpus calibration entry, not an allowlisted compute gate). Forward consumer: S98+ plan picks up the candidate; the clause advances toward minting only on two more structurally-distinct composite-collapse calibration instances.

(none for the dev-line-surgery recurrence (A8.ii) — covered by existing single-shot/append-once + Option-A discipline; no new rule minted. W2-2's idempotency guard is the forward fix. If a third instance recurs, promote a producing-script idempotency-guard guidance per the K=3 SUGGESTION→MANDATORY contract.)

---

## §E. Pre-compute shell waves (upstream escalation; NOT a CF)

(none — Waves 1, 2, 3 all fully executed with verdicts + artifacts on disk. Waves 4–6 not yet dispatched.)

---

## Q1 workshop seed (NOT a Q2 item — recorded for `/rclab-investigate`, do NOT filter as non-workshop)

- **W2-2 composite-collapse INFO-vs-FAIL adjudication.** S97-W2-2-C10-N-EXPONENT emitted a LIVE verdict INFO with a 3-tuple `sign=FAIL/magnitude=PASS/regime=VALID`. The mechanical composite-collapse rule (`gate-verdicts.md`) gives FAIL on `sign=FAIL`; the agent superseded FAIL→INFO via the semantic INFO_meaning rubric (the FAIL_meaning scenario — legs disagree / correction free — did NOT occur). Genuine math/physics + methodology adjudication (two competing readings of how to score a [SIGN] gate whose one-sided directional prediction "n_eff ≥ 2" was magnitude-confirmed but sign-violated by the negative anharmonic q³ correction). Routed to `/rclab-investigate` (session-close) as a Q1 workshop candidate. The C10 disposition (sharpened, held) is robust to the label. Recorded in `session-97-w2-workingpaper.md §"Wave 2 Synthesis"`.

---

## §F. Structural counts (artifact shape; not length)

| Category | Count (W1+W2+W3) |
|:---------|------:|
| §A In-session resolutions | 15 |
| §B Hygiene compute CFs (mirrored to WP) | 1 |
| §C Q3 parallel-wave CFs (mirrored to WP) | 0 |
| §D Methodology rule extensions (mirrored to WP) | 0 |
| §E Pre-compute shell waves (escalation only) | 0 |
| Q1 workshop seeds (NOT Q2; for /rclab-investigate) | 1 |
| **Total Q2-class items surfaced (W1-W6)** | 16 |

---

## Consumption pointers

- **`/rclab-investigate` (S97)**: read this file BEFORE producing candidates. Every §A entry is a non-workshop (already effected). The **Q1 workshop seed** above IS a workshop candidate (do NOT filter it out). The math CFs live in the wave WPs, not here.
- **`/rclab-plan` (S98)**: §B/§C/§D empty; the four math CFs are consumed via their WP CF blocks (W1/W2/W3 WPs).
- **`/rclab-coordinate` (S97)**: no §E shell-wave re-dispatch; the A7 §7 EP-falsifier annotation lands when Wave 4 (mack) is coordinated.

---

## S98 wave-ordering note (closeout combined-landscape overlay; for the `/rclab-plan` author)

> Source: `sessions/archive/session-97/session-97-phonon-first-cosmologist-synthesis.md §IV.4` (Slot-3 closeout S-4 combined-landscape). This is a CROSS-WAVE ordering overlay the individual WP CF blocks do not carry; it does NOT change any CF's 4-field spec. NON-MATH; effected in-session per the closeout carry-forward mandate (ledger is not a sole-writer-protected domain).

Two HARD ordering constraints on the S98 forward-compute set:

1. **CF-S98-W1-ROUTE-RECONCILIATION BEFORE CF-S98-W2-2-RELAXATION-CLOSURE.** The relaxation-closure friction ODE (`q″ + 3Hq′ + V′(q)=0`) consumes the substrate H(τ); H(τ) is route-CONDITIONAL until the AOFT canonical frame is selected (W1 SHAPE, S-2 reading (i) by a₂-uniqueness). Planning the relaxation-closure upstream of / independent of the route-reconciliation feeds it a route-ambiguous H(τ) — the CC discharge would inherit the very ambiguity the route-reconciliation resolves. (Flagged by S-1 + W-1.)

2. **The W-2 Non-LI-Deformation Necessity precondition (§VII.BL E1 + `cross-pillar-bridge-corpus.md §28`) BEFORE pinning the re-scoped CF-S98-W3-1 ε_LX PASS-gate.** The precondition establishes that the between-generation ε_LX channel is the UNIQUE viable corridor (the within-sector φ_88-Cartan channel is ILL-POSED for #7 per W-2 — generation-blind/multiplicity-scalar). Pinning the ε_LX PASS-gate before the precondition is established tests a channel whose necessity-as-unique-corridor is unestablished; pin its threshold + channel-structure only after the precondition licenses it.

Cross-wave through-lines feeding S98 EVOI (see synthesis §IV.1–IV.3): (A) the a(t) gap is ONE axis across W1 (route-sensitivity) / W2 (relaxation-closure) / W4 ({a0,a2}-dagger discount) — CF-S98-W1-ROUTE-RECONCILIATION is the EVOI-maximal keystone (one compute, three pillars: closes W1 SHAPE, enables V.2, lifts the V.6 dagger if it converts (a₀,a₂) to independent handles). (B) C10→DILUTION-CC conditionality is epoch-dependent (present-epoch sign-INSENSITIVE, lever=1, ρ_vac/ρ_obs=1.032 ROBUST; BBN-epoch from-below RELIEVES — CF-S98-MK3-2). (C) Yukawa #7 fix channel is between-generation ε_LX, NOT within-sector (CF-S98-W3-1 re-scoped).

The campaign-produced CFs (S-1's S98-KAPPA-INDEP-FROM-CGWB-FREQ; S-3's S98-A0A2-TIER2-PV-INVARIANCE; W-1's CF-MK3-1 q→0 sign test + CF-MK3-2 BBN vacuum-fraction; W-2's re-scoped CF-S98-W3-1 + widened diagnostic) are enumerated with inherited dependencies in the synthesis §V (V.7–V.10 campaign-produced, V.3/V.4 W-2 re-scoped). All are independent of the two hard orderings EXCEPT V.3 (ordering 2).

---

*End of S97 housekeeping ledger (W1–W6 population complete; session-close designated-writer + `/weave --update` items append at the closing-synthesis pass).*
