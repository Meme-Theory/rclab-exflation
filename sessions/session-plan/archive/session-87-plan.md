# Session 87 — Compute Plan (Master, Consolidated)

## §0. Session Metadata

**Session**: 87 | **Date**: 2026-04-28 | **Format**: compute | **Waves**: 17 (14 original + 3 W9 sub-waves from §3c stall-handling)
**Generator**: `/rclab-plan --session 87 --context compute-carryforward.md,session-86-path-b-carry-forward.md`
**Mode**: consolidate | **Total carry-forwards**: 81 (CF-1..CF-79 from S86 + PB-1 + PB-2)
**Source manifest**: `sessions/session-plan/session-87-context.md` + `sessions/session-plan/session-87-partition.md`
**Skill**: `/rclab-plan` (consolidate mode + swarm architecture per skill spec §3 + §4.5)

## §0.5 Plan Dependencies

- **Canonical constants**: `computations/canonical_constants.py` (S86-close state)
- **Canonical classes**: `computations/canonical_classes.py` — GR_CLASS at line 273 + EXFLATION_CLASS at line 308 are pre-landed; PRECONDITION/EMERGENT_FROM/CONSEQUENCE/OBSERVABLE_OUTPUT roles in `valid_roles` set at line 969-970
- **§VII slot allocation**: `sessions/permanent-results-registry.md` summary table — VERDICT=PASS at plan-write 2026-04-27 (9/9 reservations A_REGISTERED_AND_MATCHED, 0 defects across B/C/D/E classes; sync brought registry from 27→66 table entries closing 39 pre-existing E_DRIFT plus 3 introduced-by-plan B/C findings)
- **S86 verdict file**: `computations/s86_gate_verdicts.txt` (input pin for any S87 re-emission gates)
- **S87 verdict file (target)**: `computations/s87_gate_verdicts.txt` (compute-time append-only writes per `.claude/rules/gate-verdicts.md` §"Canonical Verdict-File Path")

## §0.10 PRU Pre-Registration

All 17 wave plans carry `schema_version: R3` and `verdict_source: computations/s87_gate_verdicts.txt` per gate. Compute-time pipeline order per `.claude/rules/epistemic-discipline.md` §"PRU pipeline composition order":

```
PRU (cardinality pre-flight) → SOURCE-RECON (value drift) → SUBSTRATE-FIRST-PROVENANCE (source-existence) → PRDR (machinery enumeration) → gate execution → v3-recovery audit
```

## §0.11 Validator Coverage (Phase 3e summary)

Upstream-pin validator results across all 17 wave plans:

| Wave | Validator Verdict | Notes |
|:-----|:-----------------:|:------|
| W1a | **HARD-FAIL** | Missing-npz forward-references to upstream-S87-produced artifacts; accepted as runtime canonical-path rescue per `.claude/rules/gate-verdicts.md` runtime-canonical-path rule |
| W1b | **PASS** | All upstream npz references resolve |
| W2 | **HARD-FAIL** | Forward-refs to W5/W8 outputs (`s86_w11_eta_gv_residual.npz`, `s86_w11_c5_lab_falsifier.npz`) + S38-era theorem-only npz; runtime rescue accepted |
| W3 | **PASS** | All upstream npz references resolve |
| W4 | **PASS** | All upstream npz references resolve |
| W5 | **PASS** | All upstream npz references resolve |
| W6 | **PASS** | All upstream npz references resolve |
| W7 | **PASS** | All upstream npz references resolve |
| W8 | **HARD-FAIL** | Forward-refs to in-wave dependencies; runtime rescue accepted |
| W9a | **PASS** | All upstream npz references resolve |
| W9b | **HARD-FAIL** | Forward-refs to W7 CF-42 IC per-class output; runtime rescue accepted |
| W9c | **PASS** | All upstream npz references resolve (post-fix: L10→L12 slug typo corrected) |
| W9d | **PASS** | All upstream npz references resolve |
| W10 | **PASS** | All upstream npz references resolve |
| W11 | **PASS** | All upstream npz references resolve |
| W12 | **PASS** | All upstream npz references resolve |
| W13 | **PASS** | All upstream npz references resolve (PB-2 cites FGK 1612.06688 + DKvS 1903.09624 paper references — citation-only, no on-disk SHA needed) |

**Aggregate**: 13 PASS / 4 HARD-FAIL / 0 PARSE-ERROR across 17 wave plans.

§VII slot allocation audit: VERDICT=PASS (9/9 reservations A_REGISTERED_AND_MATCHED, 0 defects).

The 4 HARD-FAIL waves are accepted under skill §3e option (b): runtime canonical-path rescue with documented rationale. Each missing npz reference is a forward-reference to an artifact produced by an upstream S87 gate (e.g., W2 cites `s86_w11_c5_lab_falsifier.npz` which does not yet exist on disk — it will be produced by W5 CF-32 at compute time) OR an S38-era theorem reference where no canonical npz was ever produced (`s38_gge_permanence_theorem.npz` — S38 algebraic GGE permanence theorem is registry-grade, theorem-only, no npz). Runtime npz-ground-truth resolution at dispatch time will resolve each pin per the canonical-path rule in `.claude/rules/gate-verdicts.md`.

## §I. Theme + Structural Position

S87 inherits **81 carry-forward computations** from S86's W-1..W-13 syntheses (79 from `sessions/archive/session-86/compute-carryforward.md` consolidation) plus **2 Path-B precursor items** (Step-0 4-agent panel workshop + NC two-torus FGK fixed-point validation from `sessions/archive/session-86/session-86-path-b-carry-forward.md`).

The wave structure decomposes by reviewer-origin specialty per `feedback_agent-roster.md` and `feedback_mack-bridge-role.md` precedents:

- **Mellin-cone / Mellin-Dirichlet** (W1a-W1b gen-physicist) — 13 W-1 items split into algebraic-side identities + axiom×spectral no-go theorems (W1a, 7 items) and PV/d_eff/L_max sweep + open-questions (W1b, 6 items)
- **α_s observational + lab** (W2 mack-cosmic-bridge) — 6 W-2 priority-ranked items: 3He-B Aalto LTL lab analog, CMB-S4 watch, GGE-relic moment-independent route, K-running near saturation, a_4/a_2 pivot stationarity, Path-H/Path-C interpolation
- **Path-H/Path-C falsifier suite** (W3 gen-physicist) — 5 W-3 items: SOURCE-DOUBLE-CITE-CO-PRIMARY registry landing, BK-Array meta-classifier_v2, joint LiteBIRD-LISA 2×2 falsifier suite with δ_speed sub-gate, S88+ candidates
- **Cross-pillar + Type-F + f_NL surgery** (W4 connes-ncg-theorist) — 6 W-4 items spanning Level 1 cross-pillar 3-channel theorem proof through Level 5 epistemic-discipline rule-promotion decision
- **Pillar III↔IV bridge + 3He-B lab + §VII.P-v2** (W5 volovik-superfluid-universe-theorist) — 5 W-5 items including `_cross_pillar_bridge_audit.py` 5-element IS-not-IN anatomy + 3-level ladder + 3He-B lab pre-registrations on F1/F2/F5 falsifier rows
- **T7-S67 isomorphism + cyclic-fold + plaquette** (W6 lizzi-spectral-functional-theorist) — 6 W-6 items adopting `agent-standards.md` §"Quotient-functor pre-registration discipline" T1-6
- **IC per-class + UV-cutoff + retroactive audit** (W7 lizzi-spectral-functional-theorist) — 5 W-7 items including dual-prior pre-registration + Layer-1-2 retroactive audit
- **cutoff_sqrt + sixth regulator + HBW + η-GV** (W8 gen-physicist) — 8 items (W-8 7 + W-11 1) on regulator-class extension + channel-independence
- **Path-(c) successor + α_s ranked + pole specificity** (W9a-W9d split, originally W9 mack/transit/connes/volovik) — 7 W-9 items now in 4 sub-waves after stall-handling: W9a mack registry trio (CF-54+CF-57+CF-60), W9b transit IC+pole pair (CF-55+CF-58), W9c connes cross-proxy adjudication (CF-56), W9d connes Stage-2 verify gate-spec (CF-59)
- **Bulletin rescue + ρ_∞ wall** (W10 connes-ncg-theorist) — 4 W-10 items
- **V_4 monodromy + 4-stratum + 3He-B excess** (W11 connes-ncg-theorist) — 6 W-12 items including PRU Class 8.2 V_4-supersedes-Z_4 calibration
- **Methodology validation + MCP hooks** (W12 connes-ncg-theorist) — 8 W-13 items
- **Path-B precursor** (W13 gen-physicist orchestrator) — 2 PB items: Step-0 4-agent panel workshop + NC two-torus FGK fixed-point validation

## §II. Wave-by-Wave Breakdown — Pointer Table

The wave-by-wave content is preserved verbatim in the per-wave plan files. Each wave is independently dispatchable via `/rclab-coordinate sessions/session-plan/session-87-plan-w{i}.md`. Master-plan §II is implemented as a pointer table to preserve the per-wave file structure (skill §4.5 verbatim-concatenation deviation per `feedback_rules-compensate-missing-structure.md` — 17 waves × ~800-1660 lines = ~14,500 total lines combined; per-wave dispatchability + audit reproducibility preserved by pointer-only structure).

| Wave | Owner | Items (CF-IDs) | File | Lines | Gate sections |
|:-----|:------|:---------------|:-----|:-----:|:-------------:|
| W1a | gen-physicist | CF-1..CF-7 (Mellin-Strip / CM-1995 / Mellin-Dirichlet) | [`session-87-plan-w1a.md`](session-87-plan-w1a.md) | 1031 | 7 |
| W1b | gen-physicist | CF-8..CF-13 (PV / d_eff / L_max sweep / Open-Q) | [`session-87-plan-w1b.md`](session-87-plan-w1b.md) | 1450 | 6 |
| W2 | mack-cosmic-bridge | CF-14..CF-19 (α_s observational + lab) | [`session-87-plan-w2.md`](session-87-plan-w2.md) | 735 | 6 |
| W3 | gen-physicist | CF-20..CF-24 (Path-H/Path-C + LiteBIRD/LISA) | [`session-87-plan-w3.md`](session-87-plan-w3.md) | 1138 | 4 (+5 sub-gates internal) |
| W4 | connes-ncg-theorist | CF-25..CF-30 (Cross-pillar + Type-F + f_NL) | [`session-87-plan-w4.md`](session-87-plan-w4.md) | 898 | 6 |
| W5 | volovik-superfluid-universe-theorist | CF-31..CF-35 (Pillar III↔IV bridge + 3He-B lab) | [`session-87-plan-w5.md`](session-87-plan-w5.md) | 595 | 5 |
| W6 | lizzi-spectral-functional-theorist | CF-36..CF-41 (T7-S67 isomorphism + cyclic-fold) | [`session-87-plan-w6.md`](session-87-plan-w6.md) | 804 | 6 |
| W7 | lizzi-spectral-functional-theorist | CF-42..CF-46 (IC per-class + UV-cutoff + audit) | [`session-87-plan-w7.md`](session-87-plan-w7.md) | 1660 | 5 |
| W8 | gen-physicist | CF-47..CF-53 + CF-65 (cutoff_sqrt + 6th regulator + HBW + η-GV) | [`session-87-plan-w8.md`](session-87-plan-w8.md) | 1256 | 8 |
| W9a | mack-cosmic-bridge | CF-54 + CF-57 + CF-60 (Path-(c) anchor + α_s rank + S88 deferred) | [`session-87-plan-w9a.md`](session-87-plan-w9a.md) | 860 | 3 |
| W9b | transit-dynamics-theorist | CF-55 + CF-58 (Rescaled IC + pole-specificity) | [`session-87-plan-w9b.md`](session-87-plan-w9b.md) | 497 | 2 |
| W9c | connes-ncg-theorist | CF-56 (c_sub axiom-side cross-review) | [`session-87-plan-w9c.md`](session-87-plan-w9c.md) | 611 | 1 |
| W9d | connes-ncg-theorist | CF-59 (Stage-2 verify gate-spec, S88+ dispatch) | [`session-87-plan-w9d.md`](session-87-plan-w9d.md) | 451 | 1 |
| W10 | connes-ncg-theorist | CF-61..CF-64 (Bulletin rescue + ρ_∞ wall) | [`session-87-plan-w10.md`](session-87-plan-w10.md) | 451 | 4 |
| W11 | connes-ncg-theorist | CF-66..CF-71 (V_4 monodromy + 4-stratum + 3He-B excess) | [`session-87-plan-w11.md`](session-87-plan-w11.md) | 841 | 6 |
| W12 | connes-ncg-theorist | CF-72..CF-79 (Methodology validation + MCP hooks) | [`session-87-plan-w12.md`](session-87-plan-w12.md) | 671 | 8 |
| W13 | gen-physicist (orchestrator) | PB-1 + PB-2 (Path-B Step-0 workshop + NC two-torus FGK validation) | [`session-87-plan-w13.md`](session-87-plan-w13.md) | 684 | 2 |

**Totals**: 17 wave files / ~14,633 lines / ~78 gate sections (with W3 contributing 5 additional internal sub-gates within CF-22 for the joint LiteBIRD-LISA falsifier suite).

## §III. Decision Points

Inter-wave decision points are documented in each wave's `Wave {i} → Wave {i+1} Decision Point` section. Key cross-wave dependencies:

- **W1a CF-7 §VII.PROP landing → W4 CF-25 cross-pillar 3-channel theorem** (CF-25 cites §VII.PROP routing-layer principles as substrate-IS observable axis; non-blocking)
- **W2 CF-19 Path-H/Path-C interpolation → W9a CF-54 Path-(c) successor anchor** (NON-blocking; CF-19 paper-mode feeds CF-54's STAGE-1-CANDIDATE registry text)
- **W5 CF-31 Pillar III↔IV bridge land → W5 CF-32+CF-33 lab falsifiers** (CF-32+CF-33 cite the bridge's substrate-IS prediction; CF-31 PRECEDES at compute-time)
- **W7 CF-42 IC per-class verify → W9b CF-55 rescaled IC SR-LO rerun** (CF-55 consumes CF-42's class-projected ξ²₀(R) values)
- **W11 CF-66 V_4 monodromy → W11 CF-71 monodromy depth extension** (CF-71 uses V_4 as d=2 baseline)
- **W10 CF-61 Bulletin #3 rescue → W10 CF-63 lizzi-observable promotion** (CONDITIONAL on CF-61 outcome per `.claude/rules/mechanical-closure-discipline.md` mechanical-closure protocol on FAIL path)
- **W13 PB-1 workshop → W13 PB-2 NC two-torus implementation** (PB-1 frozen architecture document specifies modulus + metric choices PB-2 implements; per path-b file lines 238-242 sequencing constraint)
- **W9a CF-54 STAGE-1-CANDIDATE land → W9d CF-59 STAGE-2 verify** (Stage-2 dispatch is S88+ per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway; W9d emits gate-spec only at S87)

## §IV. Working-Paper Shell Spec

The Phase 5 prompter generates `sessions/archive/session-87/session-87-results-workingpaper.md` per `.claude/templates/workingpaper.md` shape — one §W{i}-{n} section per gate, all 17 waves consolidated. Pre-execution shell shape: 7-line header + 2 pending blocks per gate (Status: NOT STARTED / Gate ID / Trigger / Classification / Specialist agent / Hypothesis (one-line paraphrase) / Plan reference / Verdict (pending) / Results (pending with include: list per skill §5c).

## §V. Constraint-Map Updates Expected

S87 close is expected to generate the following registry-grade landings (subject to gate verdicts):

- 7 W1a §VII slot landings (Mellin-Strip §VII.U.6 / CM-1995 no-go meta-theorem / Mellin-Dirichlet §VII.U / R-protection-failure unification / M2-residual necessity / VII-PROP routing-layer 2-principle)
- 6 W4 §VII.AC sub-row landings (cross-pillar 3-channel theorem proof + Type-F per-mode phase audit + f_NL surgery)
- 5 W5 §VII.AF sub-row landings (Pillar III↔IV bridge level-3 ladder + lab falsifier pre-regs + §VII.AF.2 §VII.P-v2 recast)
- 6 W6 §VII.AG sub-row landings (T7-S67 quotient-functor isomorphism + cyclic-fold class survey + Z_3 plaquette signature)
- 4 W10 §VII.K-PROP-W10-4 sub-row landings (Bulletin #4 ρ_∞ permanent wall + 4-level registry-mechanic schema)
- 6 W11 §VII.AJ sub-row landings (V_4 monodromy + partition-stability + hypercube identity + depth extension; §VII.AJ.partition-stability sub-row pre-allocated)
- 8 W12 methodology rule extensions (wave-classification validation + MCP pre-check.sh + permission audit + audit-leg verification + max-8-subagents hook promotion)
- 2 W13 Path-B-architecture-spec-frozen.md output + NC two-torus FGK validation script + reusable Path-B simulator infrastructure

## §VI. Session Summary

**Total wave count**: 17 (W1a, W1b, W2, W3, W4, W5, W6, W7, W8, W9a-d split from W9 stall, W10, W11, W12, W13)
**Total gate count**: ~78 main gate sections + ~5 W3 internal sub-gates
**Total computations**: 81 carry-forward items (79 from compute-carryforward.md + 2 Path-B)
**Effort estimate**: 30-45 wave-equivalents (Mellin-cone-heavy W1a/W1b/W3/W8 + cross-pillar W4/W5 + methodology W12 + Path-B W13 each ~3-5 waves)
**Validator coverage at plan-freeze**: 13/17 PASS + 4/17 HARD-FAIL accepted as runtime canonical-path rescue + 9/9 §VII slot reservations A_REGISTERED_AND_MATCHED

## §VII. Master Index

| Wave | Theme | Owner | Gates | File |
|:----:|:------|:------|:-----:|:-----|
| W1a | Mellin-Strip / CM-1995 / Mellin-Dirichlet | gen-physicist | 7 | session-87-plan-w1a.md |
| W1b | PV / d_eff / L_max sweep / Open-Q | gen-physicist | 6 | session-87-plan-w1b.md |
| W2 | α_s observational + lab | mack-cosmic-bridge | 6 | session-87-plan-w2.md |
| W3 | Path-H/Path-C + LiteBIRD/LISA suite | gen-physicist | 4 (+5 sub) | session-87-plan-w3.md |
| W4 | Cross-pillar + Type-F + f_NL surgery | connes-ncg-theorist | 6 | session-87-plan-w4.md |
| W5 | Pillar III↔IV bridge + 3He-B lab | volovik-superfluid-universe-theorist | 5 | session-87-plan-w5.md |
| W6 | T7-S67 isomorphism + cyclic-fold + plaquette | lizzi-spectral-functional-theorist | 6 | session-87-plan-w6.md |
| W7 | IC per-class + UV-cutoff + retroactive audit | lizzi-spectral-functional-theorist | 5 | session-87-plan-w7.md |
| W8 | cutoff_sqrt + sixth regulator + HBW + η-GV | gen-physicist | 8 | session-87-plan-w8.md |
| W9a | Path-(c) anchor + α_s rank + S88 deferred | mack-cosmic-bridge | 3 | session-87-plan-w9a.md |
| W9b | Rescaled IC + pole-specificity | transit-dynamics-theorist | 2 | session-87-plan-w9b.md |
| W9c | c_sub axiom-side cross-review | connes-ncg-theorist | 1 | session-87-plan-w9c.md |
| W9d | Stage-2 verify gate-spec | connes-ncg-theorist | 1 | session-87-plan-w9d.md |
| W10 | Bulletin rescue + ρ_∞ wall | connes-ncg-theorist | 4 | session-87-plan-w10.md |
| W11 | V_4 monodromy + 4-stratum + 3He-B excess | connes-ncg-theorist | 6 | session-87-plan-w11.md |
| W12 | Methodology validation + MCP hooks | connes-ncg-theorist | 8 | session-87-plan-w12.md |
| W13 | Path-B precursor (Step-0 + NC two-torus) | gen-physicist (orchestrator) | 2 | session-87-plan-w13.md |

**Next step**: `/rclab-coordinate sessions/session-plan/session-87-plan.md` (consolidate-mode dispatcher; sequentially dispatches each wave per skill §"compute mode") OR per-wave individually via `/rclab-coordinate sessions/session-plan/session-87-plan-w{i}.md`.

**End of session-87-plan.md (consolidated master).**
