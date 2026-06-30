# Session 87 — Context File

**Generated**: 2026-04-27
**Topic label**: Further (S87 carry-forward plan)
**Prior session**: S86 (W0a-W15 fanout, 21 waves; carry-forwards consolidated into `compute-carryforward.md`)
**Closing source**: `sessions/archive/session-86/compute-carryforward.md` (84 lines, S87 carry-forward consolidation; aggregates W-1 through W-13 syntheses)
**Path-B precursor source**: `sessions/archive/session-86/session-86-path-b-carry-forward.md` (274 lines, structured 4-field specs for substrate-simulator pre-pivot work)
**Generator**: `/rclab-plan --session 87 --context compute-carryforward.md,session-86-path-b-carry-forward.md` (consolidate mode, swarm architecture)

This file is the SOLE input the per-wave planner agents will read to construct full-fidelity gate blocks for S87. The S86 closeout already discharged cross-synthesis deduplication into `compute-carryforward.md` (W-1..W-13 sources collapsed to 79 unique CF entries). Per-wave planners do NOT re-read individual S86 syntheses or workshop wrap-ups — this file plus the partition manifest is self-sufficient.

The `c1_GR_proposal.md` and `c1_exflation_proposal.md` files were originally appended to `--context` but were verified at plan-write time as ALREADY LANDED in `computations/canonical_classes.py` (GR_CLASS at line 273 with EMERGENT_FROM role; EXFLATION_CLASS at line 308 with CONSEQUENCE + OBSERVABLE_OUTPUT roles). NO S87 work derives from them; entry preserved at §5 as a NULL note.

User instruction at S87 plan-trigger (2026-04-27): all S87 housekeeping items were completed in S86; the active S87 inputs are exactly the carry-forwards in `compute-carryforward.md` plus the Path-B precursor items in `session-86-path-b-carry-forward.md`. **Total: 81 unique S87 carry-forward items.**

---

## §0. Source Manifest

| File | Lines | Origin | Carry-forward type |
|:-----|:-----:|:-------|:--------------------|
| `sessions/archive/session-86/compute-carryforward.md` | 84 | S86 closeout — multi-agent consolidation of W-1..W-13 syntheses | UNIFIED — primary source (79 entries) |
| `sessions/archive/session-86/session-86-path-b-carry-forward.md` | 274 | S86 Path-B D2 workshop closure (2026-04-27) + RQ-1+RQ-3 combined plan | STRUCTURED — Path-B precursor (2 entries) |
| `sessions/archive/session-86/c1_GR_proposal.md` | 174 | einstein-theorist (S86 class-construction proposal) | DROPPED — already landed in `canonical_classes.py:273` |
| `sessions/archive/session-86/c1_exflation_proposal.md` | 190 | volovik-superfluid-universe-theorist (S86 class-construction proposal) | DROPPED — already landed in `canonical_classes.py:308` |

### Total active S87 inputs
- 79 carry-forward computations from `compute-carryforward.md` (CF-1..CF-79)
- 2 Path-B precursor items from `session-86-path-b-carry-forward.md` (PB-1, PB-2)
- **Total: 81 unique S87 carry-forward items**

### Files-on-disk verified at S87 plan-freeze (2026-04-27)
- `computations/canonical_classes.py` — EXISTS (1013 lines / 55,870 B); GR_CLASS + EXFLATION_CLASS pre-landed; `valid_roles` schema includes PRIMARY/PRECONDITION/EMERGENT_FROM/CONSEQUENCE/OBSERVABLE_OUTPUT/DERIVED/RELATED
- `computations/canonical_constants.py` — EXISTS (S86-close state); target for any new pin promotions per `.claude/rules/math-scripts.md` §"Canonical Write-Order"
- `sessions/permanent-results-registry.md` — EXISTS; target for §VII.U/§VII.V/§VII.W/§VII-X/§VII.K-PROP landings per CF-1..CF-7 (W-1) and CF-31..CF-35 (W-5) and CF-36..CF-41 (W-6)
- `computations/s86_gate_verdicts.txt` — EXISTS at S86 close; input pin for any S87 re-emission/re-derivation gates
- `sessions/framework/registry/falsifier-master-inventory.md` — EXISTS at S86 close; target for CF-22 (Path-(c) successor anchor) + CF-54 (Joint F_2-Class Path-(c) Theorem) + CF-57 (α_s ranked-route landing) + CF-65 (η-GV regulator-independence) + CF-69 (hypercube-vertex character identity)

### Validation-tool inventory (Phase 3e + on-call)
- `computations/_plan_upstream_pin_validator.py` — upstream-reference pin validator (mandatory per wave per skill §3e)
- `computations/_yaml_gate_validator.py` — PRDR machinery checklist + R3 `schema_version` validator
- `computations/_recovery_controller.py` — V3 closure recovery (Stage 1/2/3 + PROHIBITED_ACTIONS)
- `computations/_source_reconciliation_audit.py` — SOURCE-RECON 5+1-class taxonomy + cluster-span canonical-metric check + Class-(f) PIN-PLACEHOLDER detection
- `computations/_pru_cardinality_audit.py` — PRU cardinality pre-flight
- `computations/_substrate_first_provenance_audit.py` — V.1 implementation pending (queued under CF-79-adjacent S87 work; manual review until then)
- `computations/_mechanical_closure_audit.py` — mechanical-closure-discipline auditor (S86 W3 6/6 PRE-REG-INC closure precedent)
- `computations/_a_n_regulator_pin_audit.py` — bare `a_n` Seeley-DeWitt regulator-pin tag enforcement
- `computations/_cross_pillar_bridge_audit.py` — cross-pillar bridge anatomy (5 IS-not-IN elements + 3-level ladder) per S86 W-5
- `computations/_joint_theorem_independent_verify_audit.py` — Stage-2 cross-reviewer guard (S86 W-9 promotion-pathway)

---

## §1. Constraint-Map Snapshot at S86-close (anchors per-wave planners cite)

S86 closed with 21 waves and 150+ verdict lines. The S87 carry-forward inherits the following S86-close anchors verbatim. These are NOT carry-forward items — they are SETTLED registry state per `feedback_agent-roster.md` (planners must verify against source files before citing).

### §1.1 Permanent-registry-grade S86 landings (sample; full ledger at `permanent-results-registry.md`)
- **§VII.U.1** — FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY (S86 W-1 lizzi anchor; ALGEBRAIC × AXIOM)
- **§VII.U.6** — Mellin-Strip / Convergence-Cone Theorem (S86 W-1 W1b-T5 INFINITE-VECTOR landing)
- **§VII.U** — R-Class Catalogue 7-row (W6-W13 + W10-1 ANTI-CORRESPONDENCE)
- **§VII.X** — S50 Theorem Promotions (umbrella); §VII.X.1 = α_s = n_s² − 1 promotion (S85 W2-9)
- **§VII.K-PROP** — 17 W0-W5 theorem-grade PASSes landed S86 W1a-1
- **§VII.R** — NCG-Structural-Exclusion META-THEOREM (S86 W1a)
- **§VII.S** — Perturbative-Ledger Immunization Family (relocated from §VII.Y; sub-rows §VII.S.C-eta + §VII.S.C-theta)
- **§VII.W** — Pillar III↔IV cross-pillar bridge theorem (S86 W-5 volovik+connes; PASS-UNCONDITIONAL at Hochschild-cohomology level; level-3 empirical 0.0095% F_4 strict at L_max=10)

### §1.2 Open S86-close channels feeding S87
- **§VII.P parity-blindness theorem** promoted from candidate to wall (S85 W2-7 → S86 strengthened); GV-Heitsch invariant detects HP^1 content where η-invariant is parity-blind. **CF-65** (η-GV regulator-INDEPENDENCE verification) is the S87 follow-up.
- **Joint F_2-Class Path-(c) Theorem** (S86 W-9; STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md`). **CF-54** lands the Stage-1 registry entry; **CF-59** (S88+) is Stage-2 two-agent independent verify.
- **§VII.P-v2 HP^1-content-distinct corridor recast** (S86 W-5; CF-34 lands).
- **T7-S67 quotient-functor isomorphism** (S86 W-6 lizzi+volovik; CF-36 lands as new §VII slot per cyclic-fold quotient-equivalence rule).
- **4-stratum partition stability at τ_fold** (S86 W-12 V_4 monodromy + Klein-four sharpening; CF-66 supersedes pre-registered Z_4 landing).
- **Path-B D2(a) gradient flow on bare S_spec[τ]** — CLOSED-FOR-CAUSE (S86 Path-B workshop, NCG axioms + heat-kernel + Volovik analog + S38 GGE-permanence). **PB-1 + PB-2** are the precursor steps to the combined RQ-1+RQ-3 simulator architecture.

### §1.3 Methodology / rule-file state at S87 entry (all S86-promoted)
- v3 ladder framework: PRU + SOURCE-RECON + SUBSTRATE-FIRST-PROVENANCE + recovery-controller (Stage 1/2/3) — all operational
- `phononic-framing.md` + `substrate-first-canonical-sourcing.md` + `cross-pillar-bridge-anatomy.md` + `joint-theorem-promotion.md` + `inheritance-falsifier-protocol.md` + `regulator-pin-discipline.md` + `regulator-convention-lockdown.md` + `wave-classification.md` + `methodology-wave-allowlist.md` + `mechanical-closure-discipline.md` + `epistemic-discipline.md` (PRU Class 8.0/8.1/8.2/8.3 sub-taxonomy + Layer-Decomposition T2-7) + `agent-standards.md` (HIGH-DENSITY WORKSHOP TEMPLATE T2-5) — all S86 promotions captured
- `canonical_classes.py` schema with PRECONDITION/EMERGENT_FROM/CONSEQUENCE/OBSERVABLE_OUTPUT — all 4 role-taxonomy gaps from c1 proposals adopted (`canonical_classes.py:969-970`)

### §1.4 Validator coverage (mandatory at S87 plan-freeze)
Plan-freeze for each S87 wave plan MUST run (per skill §3e + project no-tech-debt rule):
1. `_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w{i}.md` — upstream npz pin map verification → JSON to `sessions/session-plan/session-87-plan-w{i}-validation.json`
2. `_yaml_gate_validator.py sessions/session-plan/session-87-plan-w{i}.md` — PRDR machinery checklist + R3 `schema_version` per gate
3. `_source_reconciliation_audit.py` — pin-vs-canonical drift (all 5+1 classes; HARD-HALT at D_max ≥ 3.0)
4. `_substrate_first_provenance_audit.py` — substrate-first canonical sourcing (V.1 manual review until S87 implementation lands)
5. Post-dispatch grep on `computations/s86_gate_verdicts.txt` for collision check on S87 gate IDs (no S87-prefixed entries should pre-exist)

---

## §2. Deduplicated Carry-Forward — 81 unique S87 inputs

This is the canonical S87 plan-writer input. Per-wave planners get only their assigned subset (per partition manifest). Items below are preserved verbatim from `sessions/archive/session-86/compute-carryforward.md` lines 7-84 plus 2 synthesized Path-B rows from `sessions/archive/session-86/session-86-path-b-carry-forward.md` lines 30-225.

### §2.1 Compute carry-forwards (CF-1..CF-79; verbatim from source)

| ID    | Source              | Gate ID                                                            | Recommending agent     | Effort estimate           | Brief                                                                                                                                |
|:------|:--------------------|:-------------------------------------------------------------------|:------------------------|:--------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| CF-1  | W-1 CF-1            | `S87-W1B-T5-LANDING`                                                | gen-physicist          | 4-6h                      | Land Mellin-Strip / Convergence-Cone Theorem at §VII.U or §VII.V citing C11 PASS at max_rel_err 8.07e-28                              |
| CF-2  | W-1 CF-2            | `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING`                             | gen-physicist          | 6-8h                      | Land CM-1995-INADMISSIBILITY-AT-FINITE-L with WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A as AXIOM×SPECTRAL no-go theorem                |
| CF-3  | W-1 CF-3            | `S87-W3-PER-EVAL-FINITENESS-PRE-REG`                                | gen-physicist          | 4-6h                      | Re-pre-register W0-20 (s=3 off-pole apex) + W0-7-MB lower-half (ρ-fit on s ∈ [2.5, 3.5]) as PASS-evidence-on-disk                    |
| CF-4  | W-1 CF-4            | `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY-LANDING`             | gen-physicist          | 2-3h                      | Land algebraic identity at §VII.U (lizzi anchor) with sanity-check at S87 closure on L_max=12 cache                                  |
| CF-5  | W-1 CF-5            | `S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE-LANDING`           | gen-physicist          | 4-6h                      | Land cross-program unification theorem; biconditional verification on synthetic 2-eigenvalue toy                                      |
| CF-6  | W-1 CF-6            | `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING`  | gen-physicist          | 6-8h                      | Land necessity-only meta-theorem; six-prior-closure anchor list with full-64-char SHAs                                                 |
| CF-7  | W-1 CF-7            | `S87-VII-PROP-LANDING`                                              | gen-physicist          | 3-4h                      | Land TWO orthogonal routing-layer principles (P_MB/P_CM un-bundling + Lens-vs-Prescription distinction)                              |
| CF-8  | W-1 CF-8            | `S87-PV-SUBTRACTION-RECALIBRATION` PRIMARY refutation gate          | gen-physicist          | 6h                        | Replace continuum SD residue coefficients with finite-L Pauli-Villars subtraction calibrated against L_max=10 cache                    |
| CF-9  | W-1 CF-9            | `S87-D-EFF-ANCHOR-VERIFICATION` DIAGNOSTIC gate                     | gen-physicist          | 4-6h                      | Verify single-d_eff anchor d_eff = 8 with per-slot threshold ordering on L_max=12 master cache                                        |
| CF-10 | W-1 CF-10 (DEFERRED)| `S87-LMAX-WEYL-CONVERGENCE-SWEEP` to L_max=14                       | gen-physicist          | 4-day                     | Empirical determination of L_∞ via cache regeneration at L_max=14 (DEFERRED unless CF-8/CF-9 leave L_∞ unresolved at L_max=12)         |
| CF-11 | W-1 CF-11 (OPEN-Q)  | `S87-PAIRED-SLOT-RATIO-INTERPRETATION`                              | gen-physicist          | TBD                       | Investigate paired a_0/a_2 split ratio 7436/3812 ≈ 1.951; OPEN-QUESTION flag                                                          |
| CF-12 | W-1 CF-12 (OPEN-Q)  | `S87-PS-AF-RECALIBRATION-DIAGNOSTIC` (deferred S88+)                | gen-physicist          | 6-10h                     | Test whether Pati-Salam A_F finite-triple calibration shifts n=0 growth factor below 100× at L_max=10                                  |
| CF-13 | W-1 CF-13 (OPEN-Q)  | `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE`           | gen-physicist          | 8-12h                     | Investigate whether Connes distance anisotropy functional admits finite-spectrum identity analogous to §VII.U Mellin-Dirichlet         |
| CF-14 | W-2 COMPUTE-CF-1    | `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` (Priority 1)                     | mack+volovik           | paper-mode 2-3 sessions   | Theoretical prediction for spin-tilt running of 3He-B dipolar excitation spectrum at Aalto LTL                                          |
| CF-15 | W-2 COMPUTE-CF-2    | `S87-ALPHA-S-CMB-S4-WATCH` (Priority 2)                             | mack                   | quarterly poll, ~10 min   | Quarterly poll of CMB-S4 publication stream + CMB-HD MacInnis-companion publication                                                    |
| CF-16 | W-2 COMPUTE-CF-3    | `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE` (Priority 3)          | mack+connes            | GPU-eligible ~1-2 days    | Compute α_s from GGE-relic Bogoliubov occupation-number variance at horizon crossing (independent of single-pole assumption)           |
| CF-17 | W-2 COMPUTE-CF-4    | `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` (Priority 4)                     | mack+volovik           | GPU-eligible ~2-3 days    | Predict δα(K)/α_FW shape through GGE-saturation crossover from substrate-physical inputs from BdG spectral triple                     |
| CF-18 | W-2 COMPUTE-CF-5    | `S87-A4-A2-PIVOT-STATIONARITY-PIN` (Priority 5)                     | mack+connes            | GPU-eligible ~1-2 days    | Compute residual `d(a_4/a_2)/dτ · (τ_pivot − τ_fold)` at pivot scale from S62 + S70 spectral-dim flow                                 |
| CF-19 | W-2 COMPUTE-CF-6    | `S87-PATH-H-PATH-C-INTERPOLATION` (Priority 6)                      | mack                   | paper-mode 1-2 sessions   | Map intermediate-r outcomes to regulator-class — third NCG-compatible regulator OR continuous deformation between L1/L3                |
| CF-20 | W-3 COMPUTE-CF-1    | `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING`                   | gen-physicist          | ~0.5 wave                 | Land classification (a) — Path-H/Path-C as multi-valued substrate observable with SOURCE-DOUBLE-CITE-CO-PRIMARY structure              |
| CF-21 | W-3 COMPUTE-CF-2    | `S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2`                             | gen-physicist          | ~1 wave (3-4 sub-gates)   | Implement four-outcome meta-classifier_v2 as callable Python module                                                                    |
| CF-22 | W-3 COMPUTE-CF-3    | `S87-N-T-CONSISTENCY-AUDIT-LITEBIRD-PLUS-LISA-(C)-NULL`             | gen-physicist          | ~2 waves (5 sub-gates)    | Joint 2×2 falsifier suite covering both block-decomposition axis (Path-H/Path-C via LiteBIRD n_T) + regulator-class axis ((A)/(C) via LISA Ω_GW) |
| CF-23 | W-3 COMPUTE-CF-4    | `S87-DELTA-SPEED-MELLIN-WINDOW` (sub-gate of CF-22)                 | gen-physicist          | ~1-2 sub-gates within CF-22 | Discrete sub-gate explicitly addressing volovik R3-A's δ_speed asymmetric inheritance observation                                       |
| CF-24 | W-3 COMPUTE-CF-5..7 (S88+ candidates) | Pati-Salam embedding + EE/BB-T cross-correlation + f_NL^equilateral | gen-physicist | TBD                       | Three S88+ candidate gates (Pati-Salam preserves B1/B2 partition; EE/BB-T as direct c_S probe; f_NL^equilateral non-Gaussianity)        |
| CF-25 | W-4 CF-1            | `S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF` [Level 1, HIGH-EVOI]      | connes+lizzi           | ~1 session                | Formal proof that 3-pt-connected vertex / pair-cumulant / 2-pt-separable decomposition extends across Pillar II/III/IV                 |
| CF-26 | W-4 CF-2            | `S87-TYPE-F-PER-MODE-PHASE-AUDIT` [Level 1.5, MEDIUM-HIGH-EVOI]      | connes+lizzi           | ~1/3 session              | Compute canonical Bogoliubov-phase distribution {phi_a}_{a=1..32} on post-tau_fold GGE state                                            |
| CF-27 | W-4 CF-3            | `S87-F-NL-FOLDED-W14-4-LANGUAGE-CORRECTION` [Level 2]                | connes+lizzi           | ~1/4 session              | Replace W14-4 framework-language §line 414-422 with locked replacement text; update master inventory row                                |
| CF-28 | W-4 CF-4            | `S87-F-NL-FOLDED-2-OBSERVABLE-REGISTRY-SPLIT` [Level 3, mechanical]  | connes+lizzi           | ~1/8 session              | Mechanical registry surgery splitting Master Inventory Row #9 into 2 rows                                                              |
| CF-29 | W-4 CF-5            | `S87-TYPE-F-TYPE-S-CROSS-PILLAR-AUDIT` [Level 4, post-Level-1]        | connes+lizzi           | ~1 session                | Cross-pillar audit of Type-F/Type-S observable partition; re-classify S70 LEGGETT-MOMENT + Pillar III BCS + Pillar VI A_s/n_s         |
| CF-30 | W-4 CF-6            | `S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE` [Level 5, doc-only]| connes+lizzi           | ~1/4 session              | Decide whether "operator-projection separation rule" rises to permanent epistemic-discipline.md rule                                    |
| CF-31 | W-5 COMPUTE-CF-1    | `S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` (registry-landing primary)| volovik+connes         | 1 dispatch + 1 dispatch (~3-6h L-scan) | Land Pillar III ↔ Pillar IV bridge theorem at §VII.W with three-level ladder + IS-not-IN anatomy                                |
| CF-32 | W-5 COMPUTE-CF-2    | `S87-W11-C5-LAB-FALSIFIER` (lab-spectroscopy pre-registration; F1-FIRST) | volovik+connes      | 1 dispatch + 1 follow-up; ~2h S87 plan-freeze | Pre-register vortex-core spectroscopy on F1 (Caroli-Matricon ladder splitting; φ_67 cocycle-clean) at Lancaster MCT-3 / RHUL |
| CF-33 | W-5 COMPUTE-CF-3    | `S87-W11-C6-MUSR-FALSIFIER` (lab-µSR pre-registration)              | volovik+connes         | 1 dispatch; ~2h           | Pre-register 3He-A µSR measurement targeting F1 / F2 / F5 analogs in chiral A-phase                                                   |
| CF-34 | W-5 COMPUTE-CF-4    | `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST` (registry-landing for §VII.P-v2) | volovik+connes | 1 dispatch; ~30 min       | Land §VII.P-v2 HP^1-content-distinct recast in `permanent-results-registry.md`                                                          |
| CF-35 | W-5 COMPUTE-CF-5..6 (forward-looking) | Future cross-pillar bridge candidates + cohomology-asymmetry test classification | volovik+connes | scoped per future bridge | three-level anatomy template adoption + Generalization beyond 3He-B for ker(ι_*) characterizations with rank ≥ 2                          |
| CF-36 | W-6 CF-1            | `S87-T7-S67-ISOMORPHISM-LANDING` (PRIMARY)                          | lizzi+volovik          | ~1 day                    | Land joint workshop product CF-LZ-VV-S86-CYCLIC-FOLD-MELLIN-SPECTROSCOPY as permanent-results-registry §VII-X                          |
| CF-37 | W-6 CF-2            | `S87-V2-WEIGHT-MATCH-FORWARD-GATE` (SECONDARY)                      | lizzi+volovik          | ~2-3 days                 | Compute Josephson-array's edge-count × per-edge-multiplicity decomposition; verify reproduces A_F real-dim ratio (1:4:18)              |
| CF-38 | W-6 CF-3            | `S87-F-PLAQUETTE-TRIANGULAR-WILSON` (TERTIARY)                      | lizzi+volovik          | ~1 day                    | Refactor `s56_atensor_frustration.py` from `wilson_4` to `wilson_3`; compute f_plaquette on framework's Jensen-deformed SU(3) spectrum |
| CF-39 | W-6 CF-4            | `S87-CYCLIC-FOLD-CLASS-SURVEY` (QUATERNARY, deferred-research)       | lizzi+volovik          | ~3-5 days                 | Survey OTHER §VII-B and §VII walls for membership in new categorical class "Cyclic-Fold Mellin-Spectroscopic Walls"                    |
| CF-40 | W-6 CF-5            | `S87-CROSS-CLUSTER-MELLIN-WICK-COMMUTATION-THEOREM` (auxiliary research) | lizzi+volovik     | ~3-5 days theoretical     | Construct (or refute) Mellin-Wick joint commutation theorem at cross-cluster level                                                     |
| CF-41 | W-6 CF-6            | Refactor `s85_w5_7_two_layer_obstruction.py` to expose F_4/M sub-sums explicitly | lizzi+volovik | ~0.5 day                  | Refactor to structurally separate `n_joint_F4` and `n_joint_M` sub-sums (currently global sum)                                          |
| CF-42 | W-7 CF-1            | `S87-W5A-P3-IC-PER-CLASS-VERIFY` (with dual-prior footnote)         | lizzi+transit          | MODERATE                  | Re-compute `xi_E_GGE_inv` IC for each of 5 L1-classes at s=−1; track-discriminator per EM-CN-R3-1                                       |
| CF-43 | W-7 CF-2            | `S87-W6-C-BETA-UV-CUTOFF-3CLASS`                                    | lizzi                  | MODERATE                  | Test C-β UV-cutoff-choice immunization across {Class 1, Class 2, Class 3} = F_4 multiplier-vector sub-family                            |
| CF-44 | W-7 CF-3            | `S87-W6-C-GAMMA-WEAK-PER-CLASS`                                     | lizzi                  | HEAVY                     | Re-evaluate C-γ-WEAK Weyl-rescaling Λ_anom_internal per L1-class                                                                       |
| CF-45 | W-7 CF-4            | `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION`                  | lizzi                  | HEAVY (1-2 wave equiv)    | Walk all S78-onward 5-atlas / regulator-class / partition cites; LAYER-tag per 5-stage protocol with optional Stage-2.5 sub-tag         |
| CF-46 | W-7 CF-AVAIL-1..27  | (~26 additional warrant-check + fb_pair instantiations)             | lizzi+connes           | TBD per gate              | Available-to-S87+-planner per CV-CN-R3-4 NARROW scope — NOT pre-committed; logged in audit-output §4.3 queue                            |
| CF-47 | W-8 CF-1            | `S87-CUTOFF-SQRT-ATLAS-PROPAGATION`                                 | gen-physicist          | ~3 hours                  | Pointer-sweep + edit pass on cutoff_sqrt citations across W4-2/W6/W12/W13; flag canonical_constants.py provenance status               |
| CF-48 | W-8 CF-2            | `S87-W4-2-RE-RUN-UNDER-A_4`                                         | gen-physicist          | ~2 hours                  | Re-execute W4-2 max_pair_ratio gate on 4-column atlas {ζ, Zubarev, SDW, anomaly}; verify cluster-span identity                        |
| CF-49 | W-8 CF-3            | `S87-C45-SIXTH-REGULATOR-PROMOTION`                                 | gen-physicist          | ~6 hours                  | Enumerate candidate sixth regulators; pre-register required pass-pattern across 4 LAYER 2 channels + §VII.M layer-membership target    |
| CF-50 | W-8 CF-4            | `S87-HBW-AUDIT-ATLAS-A_4`                                           | gen-physicist          | ~5 hours                  | Test all 4 surviving atlas members for HBW positivity at f_6 = 0.1 residue slot, with channel-3a/3b/3c/3d/3e sub-classification       |
| CF-51 | W-8 CF-5            | `S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY`                | gen-physicist          | ~4 hours                  | Dispatch 4-channel test of Mellin-cone live infrastructure; verify infrastructure modifications affect ONLY channel-2                  |
| CF-52 | W-8 CF-6            | `S87-CHANNEL-4-INDEPENDENCE-FROM-CHANNEL-3`                         | gen-physicist          | ~6 hours                  | Find or construct regulator that PASSes channel-4 but FAILs channel-3 (or vice versa)                                                  |
| CF-53 | W-8 CF-7            | `S87-ZUBAREV-CHANNEL-1-2-4-VERIFY` (Open Question 1; companion to CF-50) | gen-physicist     | ~5 hours                  | Dispatch 3-channel test at L2 axiom-native slot for Zubarev specifically; required to make L2-FULLY-ADMISSIBLE singleton claim binding |
| CF-54 | W-9 CF-1            | `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` [Level 1, ~1 wave]             | mack-cosmic-bridge     | 0.5 wave                  | Land Joint F_2-Class Path-(c) Theorem 6-clause statement; update falsifier-master-inventory rows 2 + 13-21                             |
| CF-55 | W-9 CF-2            | `S87-RESCALED-IC-SR-LO-RERUN`                                       | transit                | 0.5 wave                  | Run SR-LO ODE at four affine class-projected xi²_0(R) values; numerically pin N_breakdown_observable(R)                                |
| CF-56 | W-9 CF-3            | `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW`                          | connes-ncg             | 1.0 wave                  | Independent cross-reviewer operationalizes alternative anomaly-isolating proxy for c_sub conformal-anomaly contribution                 |
| CF-57 | W-9 CF-4            | `S87-A_S-SURVIVING-ROUTE-RANK-LANDING`                              | mack                   | 0.25 wave                 | Land L3+T3 cross-domain-converged ranked route table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` into falsifier-master-inventory                       |
| CF-58 | W-9 CF-5            | `S87-POLE-SPECIFICITY-SCAN`                                         | lizzi+transit          | 1.0 wave                  | Test whether Mellin-cone substrate-distance-1 spectral-dynamical anti-correlation at s=3 generalizes to s=4                            |
| CF-59 | W-9 CF-6            | `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` (Stage 2 promotion) | connes+volovik     | 1.0 wave                  | Two-agent parallel independent verification of Joint F_2-Class Path-(c) Theorem 6-clause statement                                      |
| CF-60 | W-9 CF-7..8 (deferred) | Cross-region application of 4×4 partition template + Per-class N_breakdown observable forward-modeling | (TBD)        | 0.5-2.0 waves         | Open Questions 7+8; deferred to S87+ structural                                                                                          |
| CF-61 | W-10 CF-1           | `S87-BULLETIN-#3-RESCUE-RESIDUAL`                                   | connes+lizzi           | MEDIUM (~2.5 waves)       | L1↔L2 audit of S52-S77 derivation chain for F_amp/c_sub/f_conv; folds in s_eff = 11/2 + NROY-cascade audit                            |
| CF-62 | W-10 CF-2           | `S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING`             | connes+lizzi           | LOW-MEDIUM (~2 waves)     | Permanent-wall registry-landing-target §VII.K-PROP for ρ_∞ ≈ −0.8104; 4-level registry-mechanic schema implementation (target-only mention here; binding reservation in partition.md CF-62)                       |
| CF-63 | W-10 CF-3           | `S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION` (CONDITIONAL)          | connes+lizzi           | LOW (~half-wave)          | Conditional on CF-61 outcome — promote s_eff = 11/2 candidate to Lizzi-observable theorem grade                                         |
| CF-64 | W-10 CF-4 (deferred S87+) | Strict |λ|_min/|λ|_max spectrum-cache extraction               | connes+lizzi           | LOW (~half-wave)          | Direct extraction from `s84_spectrum_cache_L12_tau019.npz` to obtain bit-exact ratio                                                    |
| CF-65 | W-11 COMPUTE-CF-1   | `S87-ETA-GV-FOLLOWUP`                                               | gen-physicist          | ~2 hours                  | Direct numerical verification that GV-Heitsch invariant is regulator-INDEPENDENT under all 5 atlas regulators when applied to (C_H, C_epsH) channel |
| CF-66 | W-12 CF-W12-1       | `S87-MONODROMY-V_4-EXPLICIT` (priority-1; supersedes pre-registered `S87-MONODROMY-Z4-LANDING`) | connes+volovik | ~6 hours              | Compute spectral-action moments A_n^(g) for n ∈ {0, 2, 4} at τ_fold under four V_4 cosets; verify V_4 PARALLELOGRAM IDENTITY            |
| CF-67 | W-12 CF-W12-2       | `S87-PARTITION-STABILITY-4STRATUM` (priority-2)                     | connes+volovik         | ~4 hours wall-clock       | Compute bottom-20 multiplicity profile of D_K(τ) at τ ∈ {τ_fold ± δ_τ} for δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10}                     |
| CF-68 | W-12 CF-W12-3       | `S87-STRATUM3-LMAX-SCAN` (priority-3; sister gate)                  | connes+volovik         | ~4-6 hours                | Test stratum-3 multiplicity stability at L_max ∈ {12, 13, 14, 15} with τ = τ_fold = 0.190 fixed                                        |
| CF-69 | W-12 CF-W12-4       | `S87-HYPERCUBE-VERTEX-IDENTITY-LANDING` (priority-4)                | connes+volovik         | ~2 hours                  | Formalize (Z_2)^d hypercube-vertex character identity; Sage-verify at d ∈ {2, 3, 4, 5}                                                   |
| CF-70 | W-12 CF-W12-5       | `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` (priority-5)               | volovik                | ~3-5 hours (Volovik lit) / ~10-15 hours (fresh BdG) | Compute 3He-B's analog of "BdG-undoubled spectral excess at first-order coexistence" at polycritical pressure point  |
| CF-71 | W-12 CF-W12-6 (latent) | `S87-MONODROMY-DEPTH-EXTENSION` (potential follow-on; not pre-registered) | connes+volovik | ~6-10 hours          | Test whether substrate's regulator-monodromy depth d = 2 is exact, or extends to d > 2 under atlas extension                            |
| CF-72 | W-13 COMPUTE-CF-1   | `S87-WAVE-CLASSIFICATION-RULE-VALIDATION`                           | connes+lizzi           | ~1 wave + 1 review        | Empirical validation of 4-test M1-M4 conjunction on S87 first 5-wave methodology corpus                                                |
| CF-73 | W-13 COMPUTE-CF-2   | `S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION`                             | connes+lizzi           | ~1 wave (3-5 dispatches)  | Production-grade implementation of `.claude/hooks/mcp-pre-check.sh` per C3-CONN-EM-2 4-parameter pin                                   |
| CF-74 | W-13 COMPUTE-CF-3   | `S87-SUBAGENT-PERMISSION-AUDIT`                                     | connes+lizzi           | ~0.5 wave (2 dispatches)  | Audit subagent permission topology under Σ_1 user adjudication outcome                                                                  |
| CF-75 | W-13 COMPUTE-CF-4   | `S87-MCP-DISCIPLINE-INVERSION-VALIDATION`                           | connes+lizzi           | ~1 wave (~10 dispatches)  | Rerun S87 first 5-wave methodology corpus under hook-injected orchestrator mandate; measure orchestrator MCP fabrication rate            |
| CF-76 | W-13 COMPUTE-CF-5   | `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION`                          | connes+lizzi           | ~1 wave (3-5 dispatches)  | Empirical corroboration of 5-mapping audit-layer F-image; synthetic Class-8-at-audit attack inducing v3-closure-recovery sig_5 firing  |
| CF-77 | W-13 COMPUTE-CF-6   | `S87-MAX-8-SUBAGENTS-HOOK-PROMOTION`                                | connes+lizzi           | ~0.5 wave (2 dispatches)  | Promote `feedback_dispatch-discipline.md` from memorized-norm `feedback_*` to prompt-encoded-ritual SessionStart hook                       |
| CF-78 | W-13 COMPUTE-CF-7   | `S87-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION`                     | connes+lizzi           | ~1 wave (3-5 dispatches)  | Independently reconstruct 13 historical sites from S85 5A workshop site-by-site enumeration                                              |
| CF-79 | W-13 COMPUTE-CF-8..9 (low-priority/forward) | 2D Scope × Layer corroboration + CategoricalDual pattern propagation tracking | connes+lizzi | implicit/observation-only | M_meta candidates; bookkeeping only — NOT separate compute-cf                           |

### §2.2 Path-B precursor (PB-1, PB-2; from session-86-path-b-carry-forward.md)

| ID    | Source              | Gate ID                                                  | Recommending agent                                                            | Effort estimate                                                              | Brief                                                                                                                                                                           |
|:------|:--------------------|:---------------------------------------------------------|:------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PB-1  | path-b Item 1       | `S87-PATH-B-STEP-0-WORKSHOP`                              | gen-physicist (orchestrator) + 4-agent panel (connes-ncg + spectral-geometer + transit-dynamics + volovik) | ~2 days (1 day workshop dispatch + 1 day synthesis to spec freeze)           | Combined-scope pre-implementation workshop closing 4 research questions (NC fiber discretization #1, cold-start vacuum #2, matching prescription #3, P2→P3/P3→P4 hand-off fidelity #7); PASS = all 4 RQs resolve to architecture-spec-actionable answers; INFO = 1-3 resolve; FAIL = blocking-level theory questions surface. Output artifact: `sessions/framework/path-b-architecture-spec-frozen.md` |
| PB-2  | path-b Item 2       | `S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION`             | spectral-geometer (mathematics owner) + gen-physicist (compute integration)   | ~2 weeks (per Round 2 Item 4 of `path-b-d2-workshop.md` synthesis)           | Implement gradient flow `dD/dτ = -Ric(D)/G_BKM` on Connes-Landi NC two-torus with FGK 1612.06688 closed-form Ricci density. PASS iff `‖h_terminal − h_flat‖_{L²} < 10⁻⁴` at τ_max=100; FAIL if `> 10⁻²` or divergence; INFO band `10⁻⁴ ≤ … ≤ 10⁻²`. Reusable infrastructure validation for Path B simulator work. Full pre-registered gate block at path-b file lines 154-184. |

---

## §3. Path-B Precursor Detail (verbatim 4-field specs from `session-86-path-b-carry-forward.md`)

### §3.1 PB-1 — Path-B-Step-0 Pre-Implementation Workshop (path-b file lines 30-101)

**4-field spec** (verbatim from path-b file lines 32-39):

| Field | Specification |
|:------|:--------------|
| **What** | Combined-scope pre-implementation workshop to close 4 research questions before the RQ-1+RQ-3 simulator architecture freezes. Output: an architecture spec freeze document that the implementation phase builds against without further theory decisions. |
| **Inputs** | (1) `sessions/framework/registry/path-b-d2-workshop.md` (workshop closure with all three rounds verified on disk); (2) `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` (combined R&D plan with the 7 research questions enumerated); (3) the four agents' existing memory (connes-ncg-theorist, spectral-geometer, transit-dynamics-theorist, volovik-superfluid-universe-theorist). |
| **Gate** | PASS if all 4 research questions resolve to architecture-spec-actionable answers. INFO if 1-3 resolve. FAIL if blocking-level theory questions surface that require a separate research session before any architecture freeze is possible. |
| **Effort** | ~2 days (1 day workshop dispatch + 1 day synthesis to spec freeze). |

**Workshop format** (path-b file lines 41-46): 4-agent panel workshop. Use `/rclab-team` (multi-agent coordinated team; questions interdependent and agents will need to message each other by name) OR `/rclab-workshop` 2-agent iterative for the two strongest pairings (Connes-NCG + spectral-geometer; transit-dynamics + Volovik) run sequentially, then synthesize. Decision deferred to S87 plan-author.

**Research questions to close** (verbatim from path-b file lines 48-65):
1. **Time-discretization on the noncommutative SU(3) fiber** — mode-truncation using static `D_K` eigenmodes is the natural fit, but the truncation-error vs. mode-count tradeoff is uncharacterized.
2. **Initial-condition class for cold start** — vacuum two-point functions on the noncommutative SU(3) fiber need explicit transcription.
3. **Matching prescription at the τ_fold boundary** — Israel / Andreev / Painlevé-Gullstrand alternatives; pre-register `s85_w6_acoustic_white_hole_formal.py` as canonical with alternatives as variants.
7. **Phase-coupling hand-off fidelity at P2→P3 and P3→P4** — combined-only research question; the joint architecture introduces translation layers absent from standalone RQ-1 / RQ-3 plans.

(Research questions #4, #5, #6 from the combined plan are deferred to mid-implementation workshops because they require initial implementation experience to be answerable.)

**Agent responsibilities** (path-b file lines 67-73):

| Agent | Owns research question | Cross-cite |
|:------|:----------------------|:-----------|
| `connes-ncg-theorist` | #1 (NC fiber discretization) | #2 (NCG vacuum specification) |
| `spectral-geometer` | #1 (heat-kernel side of mode truncation) | #4 mid-implementation |
| `transit-dynamics-theorist` | #3 (matching prescription) | #7 (P3 hand-offs) |
| `volovik-superfluid-universe-theorist` | #2 (cold-start vacuum from analog tradition) | #3, #7 |

**Dependencies / inputs (file-level)** (path-b file lines 79-87):
- `sessions/framework/registry/path-b-d2-workshop.md` — workshop closure (read in full)
- `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` — combined R&D plan
- `sessions/framework/registry/path-b-rq1-inner-fluctuation-simulator.md` — RQ-1 standalone (reference)
- `sessions/framework/registry/path-b-rq3-phase-transition-simulator.md` — RQ-3 standalone (reference)
- `s85_w6_acoustic_white_hole_formal.py` — canonical matching prescription source
- `s52_bogoliubov_amp.npz` — existing Bogoliubov amplitude data
- Existing static `D_K(τ_fold)` infrastructure (computations/_shared)

**What success looks like** (path-b file lines 89-100): A frozen architecture document specifying mode-truncation choice (e.g., L_max=10 with energy-cap / multipole-cap selection), cold-start vacuum two-point function form (e.g., specific lifted Bunch-Davies analog on noncommutative SU(3)), matching prescription canonical (e.g., `s85_w6_acoustic_white_hole_formal.py`'s Painlevé-Gullstrand-style match), and P2→P3 / P3→P4 hand-off translation layers (e.g., mode-amplitude basis ↔ field-configuration basis transforms with explicit map). After the spec freeze, the simulator implementation in S87+ can proceed without further theory decisions, only engineering choices.

### §3.2 PB-2 — Path-B-NC-Two-Torus Pre-Pivot Validation (path-b file lines 103-225)

**4-field spec** (verbatim from path-b file lines 109-114):

| Field | Specification |
|:------|:--------------|
| **What** | Implement gradient flow `dD/dτ = -Ric(D)/G_BKM` on the Connes-Landi noncommutative two-torus with Floricel-Ghorbanpour-Khalkhali Ricci density (FGK 1612.06688, closed-form for conformal-perturbation case). Validate against the analytic flat-metric fixed point. |
| **Inputs** | (1) FGK 1612.06688 (Ricci density formulae for NC 2-torus; closed-form available); (2) Existing GPU eigenvalue infrastructure (`torch.linalg.eigh` on AMD RX 9070 XT per `.claude/rules/computation-environment.md`); (3) Connes-Landi spectral triple structure (analytic; small spectrum). |
| **Gate** | `S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION`: PASS if simulator's terminal state under gradient flow recovers the analytic flat-metric fixed point with `‖h_terminal − h_flat‖_{L²} < 10⁻⁴` (where `h` is the conformal factor). FAIL if terminal state diverges or recovers a different fixed point. INFO if convergence is observed but tolerance is not met (likely numerical-precision issue, informative for L_max scaling). |
| **Effort** | ~2 weeks (per Round 2 Item 4 of `path-b-d2-workshop.md` synthesis). |

**Pre-registered gate block** (verbatim from path-b file lines 154-184):

```
Gate ID: S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION
Trigger: [VERIFY]
Classification: GEOMETRIC (toy NCG validation)
Hypothesis: Gradient flow `dD/dτ = -Ric(D)/G_BKM` on Connes-Landi NC 2-torus
            converges to the analytic flat-metric fixed point.
Threshold:
  PASS: |h_terminal - h_flat|_L² < 10⁻⁴ at τ_max = 100 (RATIO tolerance, dimensionless conformal factor)
  FAIL: |h_terminal - h_flat|_L² > 10⁻² OR divergence observed
  INFO: 10⁻⁴ ≤ |h_terminal - h_flat|_L² ≤ 10⁻² (convergence observed but precision insufficient)
Machinery pin (PRDR):
  N_eval: 64 (NC 2-torus mode count; small toy)
  L_max: N/A (no L_max in 2-torus; replaced by mode count N_eval)
  scan_range: τ ∈ [0, 100], dt = 0.01
  step_size: dt = 0.01
  tolerance: |h - h_flat|_L² monitored every 10 steps
  scheme: FGK Ricci density (closed-form per 1612.06688 Eq. main theorem)
  convention: Connes-Landi NC 2-torus, modular spectral triple structure
  random_seed: 42 (for ε·δh perturbation)
  GPU path: torch.linalg.eigh on AMD RX 9070 XT (validation case; mostly small enough for CPU)
Input SHA-256 pins:
  - FGK 1612.06688 (paper reference; no on-disk SHA needed, citation pin only)
  - DKvS 1903.09624 (paper reference; no on-disk SHA needed)
  - canonical_constants.py (for any framework-shared constants the script imports)
Expected output 4-tuple:
  (value=|h_terminal - h_flat|_L², scheme=FGK_Ricci, convention=Connes-Landi-2-torus, L_max=N_eval=64)
What PASS means: GPU eigenvalue + spectral-mode + gradient-flow infrastructure validated
                 for any future Path B simulator work.
What FAIL means: infrastructure has a numerical-correctness issue that must be fixed
                 before RQ-1+RQ-3 implementation begins.
```

**Output artifacts** (path-b file lines 187-198):
- Script: `computations/s87_w13_nc_two_torus_validation.py` (slot allocated by S87 plan-author at W13 per partition manifest)
- Data: `s87_w13_nc_two_torus_validation.npz` with `h(τ)` trajectory, `Ric(D_τ)` trajectory, `G_BKM(D_τ)` trajectory, fixed-point error trace
- Plot: `s87_w13_nc_two_torus_validation.png` showing convergence to flat metric
- Verdict line: appended to `computations/s87_gate_verdicts.txt` per canonical format
- Working-paper section: in W13 wave's working paper (consolidate mode) or `session-87-w13-workingpaper.md` (fanout mode)

**Sequencing constraint** (path-b file lines 238-242): PB-1 should land before PB-2 begins implementation, because PB-1's frozen architecture document specifies the modulus and metric choices that PB-2 implements. If PB-1 returns a BLOCKED verdict on any of the 4 research questions, PB-2 should be paused until the underlying research question is closed in a separate session.

---

## §4. Wave-Owner Heuristic (mechanical bucketing reference)

The S86 syntheses already attribute carry-forwards by reviewer-origin in the "Recommending agent" column of §2.1 above. The mechanical bucketing rule for S87 wave-owner selection (per skill §2.7a step 3 + `feedback_agent-roster.md` precedent):

- If wave items are uniformly recommended by ONE reviewer-agent → that agent owns the wave.
- If wave items are recommended by a 2-agent joint pair (e.g., `connes+lizzi`, `volovik+connes`) → the lead-listed reviewer in the pair owns the wave (S86 W-attribution convention).
- If wave items are recommended by `gen-physicist` (cross-reviewer breadth) → `gen-physicist` owns the wave.
- If a wave is dense (>10 items) AND owner is `gen-physicist`, split into sub-waves W{i}a + W{i}b along natural theme boundaries (S84 W1/W2 stall-prevention precedent per skill §3c stall-handling).

Wave-owner mapping (resolved from compute-carryforward.md "Recommending agent" column):

| Recommending column value | Wave-owner subagent_type |
|:--------------------------|:-------------------------|
| `gen-physicist` | `gen-physicist` |
| `mack` (alone) | `mack-cosmic-bridge` |
| `mack+volovik` | `mack-cosmic-bridge` (mack lead per W-2 attribution) |
| `mack+connes` | `mack-cosmic-bridge` (mack lead) |
| `mack-cosmic-bridge` | `mack-cosmic-bridge` |
| `connes+lizzi` | `connes-ncg-theorist` (connes lead per S86 W-4 attribution) |
| `lizzi+volovik` | `lizzi-spectral-functional-theorist` (lizzi lead per S86 W-6 attribution) |
| `lizzi+transit` | `lizzi-spectral-functional-theorist` |
| `lizzi` (alone) | `lizzi-spectral-functional-theorist` |
| `volovik+connes` | `volovik-superfluid-universe-theorist` (volovik lead per S86 W-5 attribution) |
| `connes+volovik` | `connes-ncg-theorist` (connes lead per S86 W-12 attribution) |
| `transit` (alone) | `transit-dynamics-theorist` |
| `connes-ncg` | `connes-ncg-theorist` |
| `volovik` (alone) | `volovik-superfluid-universe-theorist` |

---

## §5. Class Proposals — DROPPED (pre-landed in S86)

The two `c1_*_proposal.md` files (`c1_GR_proposal.md`, `c1_exflation_proposal.md`) accidentally appended to `--context` are PRE-LANDED in `computations/canonical_classes.py` as of 2026-04-27 plan-freeze. NO S87 work derives from them. Audit pointers (verified by Grep at plan-write):

- `GR_CLASS` at `canonical_classes.py:273` — 29 members (7 PRIMARY + 6 EMERGENT_FROM + 4 DERIVED + 12 RELATED). The proposal's EMERGENT_FROM role-taxonomy gap was ADOPTED for G_N + M_Pl_reduced + M_Pl_unreduced + l_Planck + t_Planck + rho_crit_GeV4 (canonical_classes.py:584-602).
- `EXFLATION_CLASS` at `canonical_classes.py:308` — 34 members (12 PRIMARY + 8 DERIVED + 1 CONSEQUENCE + 2 OBSERVABLE_OUTPUT + 11 RELATED). Both new roles ADOPTED: CONSEQUENCE for n_pairs (canonical_classes.py:730-731); OBSERVABLE_OUTPUT for w0_FW + n_s_framework (canonical_classes.py:734-738).
- Schema's `valid_roles` set at `canonical_classes.py:969-970` includes all 4 proposed roles plus the 3 pre-existing ones: PRIMARY, PRECONDITION, EMERGENT_FROM, CONSEQUENCE, OBSERVABLE_OUTPUT, DERIVED, RELATED.
- Both classes registered in CLASSES dict at `canonical_classes.py:791-792`.

If a future c2/c3 proposal lands additional classes, those will be NEW carry-forward items (not derived from these two files).

---

## §6. Extra Context (from --context flags, skill §2e)

The 2 active `--context` files (`compute-carryforward.md` + `session-86-path-b-carry-forward.md`) are folded into §2 + §3 above; the 2 dropped c1 proposal files are noted in §5. No additional `--context` content is appended verbatim — per-wave planners should follow source pointers in the carry-forward "Source" column for any deeper detail (e.g., a planner working CF-25 W-4 CF-1 reads `sessions/archive/session-86/session-86-w4-workshop.md` or the S86 W-4 working paper directly).

**End of session-87-context.md.**
