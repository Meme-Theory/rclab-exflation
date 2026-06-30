# Session 87 — Wave Partition Manifest

**Generated**: 2026-04-27
**Total carry-forward items**: 81 (= 79 from `compute-carryforward.md` CF-1..CF-79 + 2 from `session-86-path-b-carry-forward.md` PB-1..PB-2)
**Wave count**: **14** (W1a, W1b, W2, W3, W4, W5, W6, W7, W8, W9, W10, W11, W12, W13)
- W1×2 (split per S84 stall-prevention precedent: 13 gen-physicist items at W-1 → W1a 7 + W1b 6) + W2 + W3 + W4 + W5 + W6 + W7 + W8 + W9 + W10 + W11 + W12 + W13 = 2 + 12 = 14 ✓

**Semantic merges applied**: 0 (compute-carryforward.md was authored as the cross-synthesis dedupe; CF-IDs are already unique gate-IDs).

**Dropped items**: 2 (the 2 c1_*_proposal.md files were verified PRE-LANDED in `computations/canonical_classes.py:273` and `:308`; class-construction wave dropped from partition).

**Dispatch plan** (respecting ≤8 concurrent cap per `feedback_dispatch-discipline.md`):
- **Batch 1** (8 waves, no inter-wave plan-write dependencies): W1a, W1b, W2, W3, W4, W5, W6, W7
- **Batch 2** (6 waves, launched once ≥3 of Batch 1 complete): W8, W9, W10, W11, W12, W13

Plan-writing has NO inter-plan content dependency (each planner reads the context file independently); execution-time sequencing is enforced at compute-mode dispatch. This means batches can run back-to-back without waiting on physics-sequencing.

**Wave size target**: 4-8 items each (skill §2.7a step 4 says 6-15; but `feedback_dispatch-discipline.md` + S84 stall-prevention precedent + agent-death-when-overwhelmed observation push toward smaller chunks; S86 used 2-9 per wave). 14 waves × ~5.8 items/wave avg = 81 items mapped. **Smallest waves** (W10 = 4 items; W13 = 2 items) are accepted as specialty waves where item-count is set by source-cardinality rather than a target.

---

## §1. Wave Assignments

### Wave W1a — Mellin-Strip / CM-1995 / Finite-Spectrum Mellin-Dirichlet (W-1 split-a)
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-87-plan-w1a.md`
**Theme**: Land 7 W-1 lizzi-anchor / connes+lizzi joint registry-grade theorems and meta-theorems at §VII.U / §VII.V / §VII.PROP slots; algebraic-side identities + axiom×spectral no-go theorems
**Items** (7):
- CF-1 `S87-W1B-T5-LANDING` — Land Mellin-Strip / Convergence-Cone Theorem at §VII.U or §VII.V citing C11 PASS at max_rel_err 8.07e-28 (4-6h)
- CF-2 `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` — Land CM-1995-INADMISSIBILITY-AT-FINITE-L with WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A as AXIOM×SPECTRAL no-go theorem (6-8h)
- CF-3 `S87-W3-PER-EVAL-FINITENESS-PRE-REG` — Re-pre-register W0-20 (s=3 off-pole apex) + W0-7-MB lower-half (ρ-fit on s ∈ [2.5, 3.5]) as PASS-evidence-on-disk (4-6h)
- CF-4 `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY-LANDING` — Land algebraic identity at §VII.U (lizzi anchor) with sanity-check at S87 closure on L_max=12 cache (2-3h)
- CF-5 `S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE-LANDING` — Land cross-program unification theorem; biconditional verification on synthetic 2-eigenvalue toy (4-6h)
- CF-6 `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING` — Land necessity-only meta-theorem; six-prior-closure anchor list with full-64-char SHAs (6-8h)
- CF-7 `S87-VII-PROP-LANDING` — Land TWO orthogonal routing-layer principles (P_MB/P_CM un-bundling + Lens-vs-Prescription distinction) (3-4h)
**Sequencing**: NONE for plan-write. At compute-time, CF-1 (Mellin-Strip §VII.U landing) feeds CF-4 (FINITE-SPECTRUM identity at §VII.U) — same registry section; collision-check at runtime. CF-2 (no-go meta-theorem) cross-cites W-1 W2 connes work; CF-6 anchor list ties to `permanent-results-registry.md` SHA queries.
**Natural split candidates** (if W1a planner stalls): W1a-i = (CF-1 + CF-4 + CF-7 — direct §VII.U/§VII.PROP registry landings); W1a-ii = (CF-2 + CF-5 + CF-6 — meta-theorem landings); W1a-iii = (CF-3 — pre-registration).

### Wave W1b — PV Subtraction / d_eff Anchor / L_max Sweep / Open-Q (W-1 split-b)
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-87-plan-w1b.md`
**Theme**: 6 W-1 gen-physicist refutation/diagnostic gates + open-question forward studies on Pauli-Villars subtraction, d_eff anchor verification, L_max convergence sweep, paired-slot ratio interpretation, Pati-Salam A_F recalibration, Connes distance finite-spectrum identity
**Items** (6):
- CF-8 `S87-PV-SUBTRACTION-RECALIBRATION` (PRIMARY refutation gate) — Replace continuum SD residue coefficients with finite-L Pauli-Villars subtraction calibrated against L_max=10 cache (6h)
- CF-9 `S87-D-EFF-ANCHOR-VERIFICATION` (DIAGNOSTIC gate) — Verify single-d_eff anchor d_eff = 8 with per-slot threshold ordering on L_max=12 master cache (4-6h)
- CF-10 `S87-LMAX-WEYL-CONVERGENCE-SWEEP` to L_max=14 (DEFERRED unless CF-8/CF-9 leave L_∞ unresolved at L_max=12) — Empirical determination of L_∞ via cache regeneration at L_max=14 (4-day; conditional)
- CF-11 `S87-PAIRED-SLOT-RATIO-INTERPRETATION` (OPEN-Q) — Investigate paired a_0/a_2 split ratio 7436/3812 ≈ 1.951; OPEN-QUESTION flag (TBD)
- CF-12 `S87-PS-AF-RECALIBRATION-DIAGNOSTIC` (OPEN-Q; deferred S88+) — Test whether Pati-Salam A_F finite-triple calibration shifts n=0 growth factor below 100× at L_max=10 (6-10h)
- CF-13 `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE` (OPEN-Q) — Investigate whether Connes distance anisotropy functional admits finite-spectrum identity analogous to §VII.U Mellin-Dirichlet (8-12h)
**Sequencing**: CF-10 is conditional on CF-8/CF-9 outcomes (skill admits conditional pre-registration; emit pre-registered IF/ELSE per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness"). CF-11/CF-12/CF-13 OPEN-Q items get full 4-field specs with INFO-band thresholds per `feedback_arbitrary-gates.md`.
**Natural split candidates** (if W1b planner stalls): W1b-i = (CF-8 + CF-9 + CF-10 — refutation/diagnostic/sweep trio on L_max convergence); W1b-ii = (CF-11 + CF-12 + CF-13 — three OPEN-Q forward studies).

### Wave W2 — α_s Observational + Lab Pre-Registration (W-2)
**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-87-plan-w2.md`
**Theme**: 6 W-2 mack/volovik/connes joint observational + lab gates on α_s; Aalto LTL 3He-B equivalent + CMB-S4 watch + GGE-relic moment-independent route + K-running near saturation + a_4/a_2 pivot + Path-H/Path-C interpolation
**Items** (6):
- CF-14 `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` (Priority 1) — Theoretical prediction for spin-tilt running of 3He-B dipolar excitation spectrum at Aalto LTL (paper-mode 2-3 sessions; mack+volovik joint)
- CF-15 `S87-ALPHA-S-CMB-S4-WATCH` (Priority 2) — Quarterly poll of CMB-S4 publication stream + CMB-HD MacInnis-companion publication (quarterly poll, ~10 min; mack)
- CF-16 `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE` (Priority 3) — Compute α_s from GGE-relic Bogoliubov occupation-number variance at horizon crossing (independent of single-pole assumption) (GPU-eligible ~1-2 days; mack+connes)
- CF-17 `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` (Priority 4) — Predict δα(K)/α_FW shape through GGE-saturation crossover from substrate-physical inputs from BdG spectral triple (GPU-eligible ~2-3 days; mack+volovik)
- CF-18 `S87-A4-A2-PIVOT-STATIONARITY-PIN` (Priority 5) — Compute residual `d(a_4/a_2)/dτ · (τ_pivot − τ_fold)` at pivot scale from S62 + S70 spectral-dim flow (GPU-eligible ~1-2 days; mack+connes)
- CF-19 `S87-PATH-H-PATH-C-INTERPOLATION` (Priority 6) — Map intermediate-r outcomes to regulator-class — third NCG-compatible regulator OR continuous deformation between L1/L3 (paper-mode 1-2 sessions; mack)
**Sequencing**: NONE for plan-write. At compute-time CF-19 (Path-H/Path-C interpolation) feeds CF-54 (W9 Path-(c) successor anchor landing) — same observable family. CF-14 is paper-mode (long-form, no compute slot).
**Natural split candidates** (if W2 planner stalls): W2a = (CF-14 + CF-15 — observational watches, paper-mode/poll); W2b = (CF-16 + CF-17 + CF-18 — three GPU compute gates); W2c = (CF-19 — Path-H/Path-C interpolation).

### Wave W3 — Path-H/Path-C + LiteBIRD/LISA Falsifier Suite (W-3)
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-87-plan-w3.md`
**Theme**: 5 W-3 gen-physicist gates landing Path-H/Path-C multi-valued classification, BK-Array meta-classifier_v2, joint LiteBIRD-LISA 2×2 falsifier suite (with δ_speed sub-gate), and S88+ Pati-Salam / EE/BB-T / f_NL^equilateral candidate gates
**Items** (5):
- CF-20 `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` — Land classification (a) — Path-H/Path-C as multi-valued substrate observable with SOURCE-DOUBLE-CITE-CO-PRIMARY structure per `.claude/rules/registry-landing.md` (~0.5 wave)
- CF-21 `S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2` — Implement four-outcome meta-classifier_v2 as callable Python module (~1 wave; 3-4 sub-gates)
- CF-22 `S87-N-T-CONSISTENCY-AUDIT-LITEBIRD-PLUS-LISA-(C)-NULL` — Joint 2×2 falsifier suite covering both block-decomposition axis (Path-H/Path-C via LiteBIRD n_T) + regulator-class axis ((A)/(C) via LISA Ω_GW) (~2 waves; 5 sub-gates)
- CF-23 `S87-DELTA-SPEED-MELLIN-WINDOW` (sub-gate of CF-22) — Discrete sub-gate explicitly addressing volovik R3-A's δ_speed asymmetric inheritance observation (~1-2 sub-gates within CF-22)
- CF-24 `S87-S88-PLUS-CANDIDATES` (3 deferred candidate gates) — Pati-Salam embedding + EE/BB-T cross-correlation + f_NL^equilateral non-Gaussianity (TBD; S88+ candidates with 4-field placeholder specs per `feedback_fix-in-session-never-defer.md`)
**Sequencing**: At compute-time CF-23 is structurally a sub-gate of CF-22 (joint suite); planner emits CF-22 with CF-23 nested as one of 5 sub-gates. CF-21 meta-classifier_v2 module is consumed by CF-22's sub-gates as callable.
**Natural split candidates** (if W3 planner stalls): W3a = (CF-20 — registry landing); W3b = (CF-21 — meta-classifier_v2 build); W3c = (CF-22 + CF-23 — LiteBIRD-LISA suite); W3d = (CF-24 — S88+ candidates).

### Wave W4 — Cross-Pillar 3-Channel Theorem + Type-F Audit + f_NL Surgery (W-4)
**Owner**: `connes-ncg-theorist`
**Output**: `sessions/session-plan/session-87-plan-w4.md`
**Theme**: 6 W-4 connes+lizzi joint gates: cross-pillar 3-channel theorem proof + Type-F per-mode phase audit + f_NL framework-language correction + 2-observable registry surgery + Type-F/Type-S cross-pillar audit + operator-projection separation rule promotion decision
**Items** (6):
- CF-25 `S87-CROSS-PILLAR-3-CHANNEL-THEOREM-PROOF` [Level 1, HIGH-EVOI] — Formal proof that 3-pt-connected vertex / pair-cumulant / 2-pt-separable decomposition extends across Pillar II/III/IV (~1 session)
- CF-26 `S87-TYPE-F-PER-MODE-PHASE-AUDIT` [Level 1.5, MEDIUM-HIGH-EVOI] — Compute canonical Bogoliubov-phase distribution {phi_a}_{a=1..32} on post-tau_fold GGE state (~1/3 session)
- CF-27 `S87-F-NL-FOLDED-W14-4-LANGUAGE-CORRECTION` [Level 2] — Replace W14-4 framework-language §line 414-422 with locked replacement text; update master inventory row (~1/4 session)
- CF-28 `S87-F-NL-FOLDED-2-OBSERVABLE-REGISTRY-SPLIT` [Level 3, mechanical] — Mechanical registry surgery splitting Master Inventory Row #9 into 2 rows (~1/8 session)
- CF-29 `S87-TYPE-F-TYPE-S-CROSS-PILLAR-AUDIT` [Level 4, post-Level-1] — Cross-pillar audit of Type-F/Type-S observable partition; re-classify S70 LEGGETT-MOMENT + Pillar III BCS + Pillar VI A_s/n_s (~1 session)
- CF-30 `S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE` [Level 5, doc-only] — Decide whether "operator-projection separation rule" rises to permanent epistemic-discipline.md rule (~1/4 session)
**Sequencing**: At compute-time CF-25 (Level 1 theorem proof) PRECEDES CF-29 (Level 4 cross-pillar audit consuming the theorem). CF-26 (per-mode phase audit) PRECEDES CF-29's Type-F partition decisions. CF-27 + CF-28 are mechanical registry edits (parallel to compute work).
**Natural split candidates** (if W4 planner stalls): W4a = (CF-25 + CF-26 — Level-1/1.5 theorem-proof + per-mode audit); W4b = (CF-27 + CF-28 — Level-2/3 registry surgeries); W4c = (CF-29 + CF-30 — Level-4/5 cross-pillar audit + rule-promotion decision).

### Wave W5 — Pillar III↔IV Bridge + 3He-B Lab Pre-Registration + §VII.P-v2 (W-5)
**Owner**: `volovik-superfluid-universe-theorist`
**Output**: `sessions/session-plan/session-87-plan-w5.md`
**Theme**: 5 W-5 volovik+connes joint gates: Pillar III↔IV bridge theorem permanent landing at §VII.W with three-level ladder + IS-not-IN anatomy; W11-C5 vortex-core spectroscopy + W11-C6 µSR lab pre-registrations on F1/F2/F5 falsifier rows; §VII.P-v2 HP^1-content-distinct recast; forward-looking cross-pillar bridge candidates + cohomology-asymmetry test classification
**Items** (5):
- CF-31 `S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` (registry-landing primary) — Land Pillar III ↔ Pillar IV bridge theorem at §VII.W with three-level ladder + IS-not-IN anatomy per `.claude/rules/cross-pillar-bridge-anatomy.md` (1 dispatch + 1 dispatch ~3-6h L-scan)
- CF-32 `S87-W11-C5-LAB-FALSIFIER` (lab-spectroscopy pre-registration; F1-FIRST) — Pre-register vortex-core spectroscopy on F1 (Caroli-Matricon ladder splitting; φ_67 cocycle-clean) at Lancaster MCT-3 / RHUL (1 dispatch + 1 follow-up ~2h S87 plan-freeze)
- CF-33 `S87-W11-C6-MUSR-FALSIFIER` (lab-µSR pre-registration) — Pre-register 3He-A µSR measurement targeting F1 / F2 / F5 analogs in chiral A-phase (1 dispatch ~2h)
- CF-34 `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST` (registry-landing for §VII.P-v2) — Land §VII.P-v2 HP^1-content-distinct recast in `permanent-results-registry.md` (1 dispatch ~30 min)
- CF-35 `S87-CROSS-PILLAR-FORWARD-CANDIDATES` (forward-looking) — three-level anatomy template adoption + Generalization beyond 3He-B for ker(ι_*) characterizations with rank ≥ 2 (scoped per future bridge)
**Sequencing**: At compute-time CF-31 (bridge theorem land) PRECEDES CF-32 + CF-33 (lab falsifiers cite the bridge's substrate-IS prediction). CF-34 (§VII.P-v2 recast) is mechanical registry edit; CF-35 is forward-looking template-adoption (paper-mode planning, not compute).
**Natural split candidates** (if W5 planner stalls): W5a = (CF-31 — bridge theorem permanent landing); W5b = (CF-32 + CF-33 — lab falsifier pre-registrations); W5c = (CF-34 + CF-35 — §VII.P-v2 recast + forward template).

### Wave W6 — T7-S67 Isomorphism + Cyclic-Fold + Plaquette Refactor (W-6)
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-87-plan-w6.md`
**Theme**: 6 W-6 lizzi+volovik joint gates: T7-S67 cyclic-fold quotient-functor isomorphism landing as new §VII slot; Josephson-array V2-weight match forward gate; F-plaquette triangular Wilson refactor; cyclic-fold class survey; cross-cluster Mellin-Wick commutation theorem; F_4/M sub-sums refactor
**Items** (6):
- CF-36 `S87-T7-S67-ISOMORPHISM-LANDING` (PRIMARY) — Land joint workshop product CF-LZ-VV-S86-CYCLIC-FOLD-MELLIN-SPECTROSCOPY as permanent-results-registry §VII-X (or next-free §VII slot per quotient-functor pre-registration discipline; `.claude/rules/agent-standards.md` §"Quotient-functor pre-registration") (~1 day)
- CF-37 `S87-V2-WEIGHT-MATCH-FORWARD-GATE` (SECONDARY) — Compute Josephson-array's edge-count × per-edge-multiplicity decomposition; verify reproduces A_F real-dim ratio (1:4:18) (~2-3 days)
- CF-38 `S87-F-PLAQUETTE-TRIANGULAR-WILSON` (TERTIARY) — Refactor `s56_atensor_frustration.py` from `wilson_4` to `wilson_3`; compute f_plaquette on framework's Jensen-deformed SU(3) spectrum (~1 day)
- CF-39 `S87-CYCLIC-FOLD-CLASS-SURVEY` (QUATERNARY, deferred-research) — Survey OTHER §VII-B and §VII walls for membership in new categorical class "Cyclic-Fold Mellin-Spectroscopic Walls" (~3-5 days)
- CF-40 `S87-CROSS-CLUSTER-MELLIN-WICK-COMMUTATION-THEOREM` (auxiliary research) — Construct (or refute) Mellin-Wick joint commutation theorem at cross-cluster level (~3-5 days theoretical)
- CF-41 `S87-S85-W5-7-F4-M-SUBSUM-REFACTOR` — Refactor `s85_w5_7_two_layer_obstruction.py` to expose F_4/M sub-sums explicitly (separate `n_joint_F4` and `n_joint_M` from current global sum) (~0.5 day)
**Sequencing**: CF-36 (PRIMARY landing) PRECEDES CF-39 (class survey extending the new categorical class). CF-37 + CF-38 + CF-41 are independent compute gates; CF-40 is theoretical (no compute prerequisite).
**Natural split candidates** (if W6 planner stalls): W6a = (CF-36 — PRIMARY landing); W6b = (CF-37 + CF-38 — Josephson-array compute + plaquette refactor); W6c = (CF-39 + CF-40 — survey + Mellin-Wick theorem); W6d = (CF-41 — F_4/M sub-sums refactor).

### Wave W7 — IC Per-Class Verify + UV-Cutoff 3-Class + Layer-1-2 Retroactive Audit (W-7)
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-87-plan-w7.md`
**Theme**: 5 W-7 lizzi(+transit/+connes) gates: per-class IC verify with dual-prior footnote; C-β UV-cutoff-choice immunization across F_4 multiplier-vector sub-family; C-γ-WEAK Weyl-rescaling per L1-class; Layer-1-2 retroactive audit; ~26 latent warrant-check + fb_pair instantiations available-to-planner
**Items** (5):
- CF-42 `S87-W5A-P3-IC-PER-CLASS-VERIFY` (with dual-prior footnote per `.claude/rules/epistemic-discipline.md` §"Dual-prior pre-registration") — Re-compute `xi_E_GGE_inv` IC for each of 5 L1-classes at s=−1; track-discriminator per EM-CN-R3-1 (MODERATE; lizzi+transit)
- CF-43 `S87-W6-C-BETA-UV-CUTOFF-3CLASS` — Test C-β UV-cutoff-choice immunization across {Class 1, Class 2, Class 3} = F_4 multiplier-vector sub-family (MODERATE; lizzi)
- CF-44 `S87-W6-C-GAMMA-WEAK-PER-CLASS` — Re-evaluate C-γ-WEAK Weyl-rescaling Λ_anom_internal per L1-class (HEAVY; lizzi)
- CF-45 `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION` — Walk all S78-onward 5-atlas / regulator-class / partition cites; LAYER-tag per 5-stage protocol with optional Stage-2.5 sub-tag (HEAVY; 1-2 wave equiv; lizzi)
- CF-46 `S87-LATENT-WARRANT-CHECK-QUEUE` (~26 additional warrant-check + fb_pair instantiations) — Available-to-S87+-planner per CV-CN-R3-4 NARROW scope — NOT pre-committed; logged in audit-output §4.3 queue (TBD per gate; lizzi+connes). The S87 plan SHOULD pre-register a HEAD-OF-QUEUE 4-field spec per the available list, with explicit decision-rule for which subset gets compute slots vs. deferred to S88+.
**Sequencing**: CF-42 (IC per-class) feeds CF-43 + CF-44 (per-L1-class C-β + C-γ-WEAK use the same 5-class structure). CF-45 (retroactive audit) is mechanical/audit-mode, parallel to compute. CF-46 head-of-queue is plan-author's decision per dual-prior pre-reg discipline.
**Natural split candidates** (if W7 planner stalls): W7a = (CF-42 + CF-43 + CF-44 — per-L1-class compute trio); W7b = (CF-45 — retroactive audit); W7c = (CF-46 — latent queue head specification).

### Wave W8 — Cutoff_sqrt Atlas / Sixth Regulator / HBW Audit / Mellin-Cone Live + η-GV (W-8 + W-11)
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-87-plan-w8.md`
**Theme**: 7 W-8 gen-physicist + 1 W-11 gen-physicist gates on cutoff_sqrt atlas propagation, W4-2 re-run under a_4, sixth-regulator promotion, HBW positivity audit, Mellin-cone live channel-2 localization, channel-4 independence from channel-3, Zubarev channel-1-2-4 verification, plus η-GV regulator-INDEPENDENCE follow-up from W-11
**Items** (8):
- CF-47 `S87-CUTOFF-SQRT-ATLAS-PROPAGATION` — Pointer-sweep + edit pass on cutoff_sqrt citations across W4-2/W6/W12/W13; flag canonical_constants.py provenance status (~3 hours)
- CF-48 `S87-W4-2-RE-RUN-UNDER-A_4` — Re-execute W4-2 max_pair_ratio gate on 4-column atlas {ζ, Zubarev, SDW, anomaly}; verify cluster-span identity per `.claude/rules/epistemic-discipline.md` §"Canonical-metric pin extension" (~2 hours)
- CF-49 `S87-C45-SIXTH-REGULATOR-PROMOTION` — Enumerate candidate sixth regulators; pre-register required pass-pattern across 4 LAYER 2 channels + §VII.M layer-membership target (~6 hours)
- CF-50 `S87-HBW-AUDIT-ATLAS-A_4` — Test all 4 surviving atlas members for HBW positivity at f_6 = 0.1 residue slot, with channel-3a/3b/3c/3d/3e sub-classification (~5 hours)
- CF-51 `S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY` — Dispatch 4-channel test of Mellin-cone live infrastructure; verify infrastructure modifications affect ONLY channel-2 (~4 hours)
- CF-52 `S87-CHANNEL-4-INDEPENDENCE-FROM-CHANNEL-3` — Find or construct regulator that PASSes channel-4 but FAILs channel-3 (or vice versa) (~6 hours)
- CF-53 `S87-ZUBAREV-CHANNEL-1-2-4-VERIFY` (Open Question 1; companion to CF-50) — Dispatch 3-channel test at L2 axiom-native slot for Zubarev specifically; required to make L2-FULLY-ADMISSIBLE singleton claim binding (~5 hours)
- CF-65 `S87-ETA-GV-FOLLOWUP` (W-11 single item folded into W8 by recommending-agent match) — Direct numerical verification that GV-Heitsch invariant is regulator-INDEPENDENT under all 5 atlas regulators when applied to (C_H, C_epsH) channel (~2 hours)
**Sequencing**: At compute-time CF-47 + CF-48 PRECEDE CF-49 (sixth-regulator promotion uses the propagated cutoff_sqrt + a_4-atlas state). CF-50 + CF-51 + CF-52 + CF-53 are channel-by-channel sub-suite; can run in parallel after CF-48. CF-65 is independent (post-W2-7 superseded canonical per `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 calibration").
**Natural split candidates** (if W8 planner stalls): W8a = (CF-47 + CF-48 — atlas propagation + re-run); W8b = (CF-49 + CF-50 — sixth regulator + HBW audit); W8c = (CF-51 + CF-52 + CF-53 — Mellin-cone live + 3-channel sub-suite); W8d = (CF-65 — η-GV follow-up).

### Wave W9 — Path-(c) Successor + Rescaled IC + α_s Ranked + Pole Specificity (W-9)
**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-87-plan-w9.md`
**Theme**: 7 W-9 mack/transit/connes/lizzi+transit/connes+volovik joint gates: Path-(c) successor anchor landing (Stage-1 of joint theorem promotion); rescaled IC SR-LO rerun; W5b C16 axiom-side c_sub cross-review; α_s surviving-route rank landing; pole-specificity scan; S88+ Stage-2 promotion gate; CF-7..8 deferred (cross-region partition + per-class N_breakdown)
**Items** (7):
- CF-54 `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` [Level 1, ~1 wave] — Land Joint F_2-Class Path-(c) Theorem 6-clause statement (STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md`); update falsifier-master-inventory rows 2 + 13-21 (0.5 wave; mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`)
- CF-55 `S87-RESCALED-IC-SR-LO-RERUN` — Run SR-LO ODE at four affine class-projected xi²_0(R) values; numerically pin N_breakdown_observable(R) (0.5 wave; transit)
- CF-56 `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` (cross-proxy adjudication per epistemic-discipline §"Verifier-Rubric Pre-Registration extension — Cross-Proxy Adjudication") — Independent cross-reviewer operationalizes alternative anomaly-isolating proxy for c_sub conformal-anomaly contribution (1.0 wave; connes-ncg)
- CF-57 `S87-A_S-SURVIVING-ROUTE-RANK-LANDING` — Land L3+T3 cross-domain-converged ranked route table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` into falsifier-master-inventory (0.25 wave; mack)
- CF-58 `S87-POLE-SPECIFICITY-SCAN` (per epistemic-discipline §"Pole-Scope sub-clause") — Test whether Mellin-cone substrate-distance-1 spectral-dynamical anti-correlation at s=3 generalizes to s=4 (1.0 wave; lizzi+transit)
- CF-59 `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` (Stage 2 promotion per joint-theorem-promotion §Stage 2) — Two-agent parallel independent verification of Joint F_2-Class Path-(c) Theorem 6-clause statement; assigned cross-reviewers connes-ncg-theorist (axis-A) + volovik-superfluid-universe-theorist (axis-B) (1.0 wave; connes+volovik)
- CF-60 `S87-DEFERRED-OPEN-Q-7-8` — Cross-region application of 4×4 partition template + Per-class N_breakdown observable forward-modeling (0.5-2.0 waves; TBD owner)
**Sequencing**: CF-54 (Stage-1 land) PRECEDES CF-59 (Stage-2 verify; structurally a S88 dispatch). CF-55 (rescaled IC) feeds CF-58 (pole-specificity uses the rescaled-IC class projections). CF-56 (cross-review) is independent; CF-57 (rank landing) is independent (mack sole writer).
**Natural split candidates** (if W9 planner stalls): W9a = (CF-54 + CF-57 — two registry landings, mack sole-writer); W9b = (CF-55 + CF-58 — rescaled IC + pole-specificity, transit/lizzi+transit); W9c = (CF-56 — cross-review, connes-ncg); W9d = (CF-59 + CF-60 — Stage-2 verify + S88+ deferred).

### Wave W10 — Bulletin #3 Rescue + Bulletin #4 ρ_∞ Wall (W-10)
**Owner**: `connes-ncg-theorist`
**Output**: `sessions/session-plan/session-87-plan-w10.md`
**Theme**: 4 W-10 connes+lizzi joint gates: Bulletin #3 rescue residual (L1↔L2 audit of S52-S77 derivation chain); Bulletin #4 irrational ρ_∞ permanent-wall registry landing; Bulletin #3 lizzi-observable promotion (conditional); strict |λ|_min/|λ|_max spectrum-cache extraction
**Items** (4):
- CF-61 `S87-BULLETIN-#3-RESCUE-RESIDUAL` — L1↔L2 audit of S52-S77 derivation chain for F_amp/c_sub/f_conv; folds in s_eff = 11/2 + NROY-cascade audit (MEDIUM ~2.5 waves)
- CF-62 `S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING` — Permanent-wall registry landing at §VII.K-PROP for ρ_∞ ≈ −0.8104; 4-level registry-mechanic schema implementation (LOW-MEDIUM ~2 waves)
- CF-63 `S87-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION` (CONDITIONAL on CF-61 outcome) — Promote s_eff = 11/2 candidate to Lizzi-observable theorem grade (LOW ~half-wave)
- CF-64 `S87-STRICT-LAMBDA-RATIO-EXTRACTION` (deferred S87+) — Direct extraction from `s84_spectrum_cache_L12_tau019.npz` to obtain bit-exact ratio (LOW ~half-wave)
**Sequencing**: CF-61 (rescue residual) PRECEDES CF-63 (lizzi-observable promotion is conditional on CF-61 outcome). CF-62 (ρ_∞ wall) is independent. CF-64 is deferred (parse from spectrum cache).
**Natural split candidates** (if W10 planner stalls): W10a = (CF-61 — rescue residual); W10b = (CF-62 — ρ_∞ wall landing); W10c = (CF-63 + CF-64 — conditional promotion + strict extraction).

### Wave W11 — V_4 Monodromy + 4-Stratum Stability + 3He-B Excess + Hypercube-Vertex (W-12)
**Owner**: `connes-ncg-theorist`
**Output**: `sessions/session-plan/session-87-plan-w11.md`
**Theme**: 6 W-12 connes+volovik joint gates: V_4 monodromy explicit (supersedes pre-registered Z_4); 4-stratum partition stability at τ_fold ± δ_τ; stratum-3 L_max scan; (Z_2)^d hypercube-vertex character identity; 3He-B excess inheritance comparison at polycritical pressure point; monodromy depth d>2 extension
**Items** (6):
- CF-66 `S87-MONODROMY-V_4-EXPLICIT` (priority-1; supersedes pre-registered `S87-MONODROMY-Z4-LANDING` per W-12 RULE-W12-1 PRU Class 8.2 calibration) — Compute spectral-action moments A_n^(g) for n ∈ {0, 2, 4} at τ_fold under four V_4 cosets; verify V_4 PARALLELOGRAM IDENTITY (~6 hours)
- CF-67 `S87-PARTITION-STABILITY-4STRATUM` (priority-2) — Compute bottom-20 multiplicity profile of D_K(τ) at τ ∈ {τ_fold ± δ_τ} for δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10} (~4 hours wall-clock)
- CF-68 `S87-STRATUM3-LMAX-SCAN` (priority-3; sister gate) — Test stratum-3 multiplicity stability at L_max ∈ {12, 13, 14, 15} with τ = τ_fold = 0.190 fixed (~4-6 hours)
- CF-69 `S87-HYPERCUBE-VERTEX-IDENTITY-LANDING` (priority-4) — Formalize (Z_2)^d hypercube-vertex character identity; Sage-verify at d ∈ {2, 3, 4, 5} per `.claude/rules/math-scripts.md` §Sage discipline (~2 hours)
- CF-70 `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` (priority-5) — Compute 3He-B's analog of "BdG-undoubled spectral excess at first-order coexistence" at polycritical pressure point (~3-5 hours Volovik lit / ~10-15 hours fresh BdG; volovik recommended)
- CF-71 `S87-MONODROMY-DEPTH-EXTENSION` (priority-6; latent / not pre-registered in W-12 source) — Test whether substrate's regulator-monodromy depth d = 2 is exact, or extends to d > 2 under atlas extension (~6-10 hours)
**Sequencing**: CF-66 (V_4 monodromy explicit) PRECEDES CF-71 (depth extension uses V_4 as the d=2 baseline). CF-67 + CF-68 are sister stability gates (parallel). CF-69 is algebraic (Sage-verified, no compute prerequisite). CF-70 is volovik-specialty (literature lookup OR fresh BdG compute).
**Natural split candidates** (if W11 planner stalls): W11a = (CF-66 — V_4 monodromy primary); W11b = (CF-67 + CF-68 — partition stability sister gates); W11c = (CF-69 + CF-71 — hypercube identity + depth extension); W11d = (CF-70 — 3He-B excess, volovik specialty).

### Wave W12 — Methodology Validation + MCP Hooks + Audit-Leg Verification (W-13)
**Owner**: `connes-ncg-theorist`
**Output**: `sessions/session-plan/session-87-plan-w12.md`
**Theme**: 8 W-13 connes+lizzi joint gates: wave-classification rule validation; MCP pre-check hook implementation; subagent permission audit; MCP discipline inversion validation; layer-functor audit-leg verification; max-8-subagents hook promotion; W0a-2a 13-site reconstruction; CategoricalDual M_meta candidates (bookkeeping)
**Items** (8):
- CF-72 `S87-WAVE-CLASSIFICATION-RULE-VALIDATION` — Empirical validation of 4-test M1-M4 conjunction on S87 first 5-wave methodology corpus per `.claude/rules/wave-classification.md` (~1 wave + 1 review)
- CF-73 `S87-MCP-PRE-CHECK-HOOK-IMPLEMENTATION` — Production-grade implementation of `.claude/hooks/mcp-pre-check.sh` per C3-CONN-EM-2 4-parameter pin (~1 wave; 3-5 dispatches)
- CF-74 `S87-SUBAGENT-PERMISSION-AUDIT` — Audit subagent permission topology under Σ_1 user adjudication outcome (~0.5 wave; 2 dispatches)
- CF-75 `S87-MCP-DISCIPLINE-INVERSION-VALIDATION` — Rerun S87 first 5-wave methodology corpus under hook-injected orchestrator mandate; measure orchestrator MCP fabrication rate (~1 wave; ~10 dispatches)
- CF-76 `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION` — Empirical corroboration of 5-mapping audit-layer F-image; synthetic Class-8-at-audit attack inducing v3-closure-recovery sig_5 firing per `.claude/rules/v3-closure-recovery.md` (~1 wave; 3-5 dispatches)
- CF-77 `S87-MAX-8-SUBAGENTS-HOOK-PROMOTION` — Promote `feedback_dispatch-discipline.md` from memorized-norm `feedback_*` to prompt-encoded-ritual SessionStart hook (~0.5 wave; 2 dispatches)
- CF-78 `S87-W0A-2A-INDEPENDENT-13-SITE-RECONSTRUCTION` — Independently reconstruct 13 historical sites from S85 5A workshop site-by-site enumeration (~1 wave; 3-5 dispatches)
- CF-79 `S87-2D-LEVEL-LAYER-CORROBORATION` (low-priority/forward bookkeeping) — 2D Scope × Layer corroboration + CategoricalDual pattern propagation tracking (M_meta candidates; bookkeeping only — implicit/observation-only)
**Sequencing**: CF-72 (M1-M4 validation) feeds CF-75 (discipline-inversion validation uses the same first-5-wave corpus). CF-73 (mcp-pre-check.sh implementation) feeds CF-75 (the inversion validation runs UNDER the implemented hook). CF-74 (permission audit) is independent. CF-76 (layer-functor audit-leg) consumes the F-image substrate ↔ methodology pair from `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" T2-7.
**Natural split candidates** (if W12 planner stalls): W12a = (CF-72 + CF-75 — wave-classification + discipline-inversion validation pair); W12b = (CF-73 + CF-77 — hook implementation + max-8 promotion); W12c = (CF-74 + CF-76 + CF-78 — permission audit + audit-leg verification + 13-site reconstruction); W12d = (CF-79 — bookkeeping).

### Wave W13 — Path-B Precursor: Step-0 Workshop + NC Two-Torus FGK Validation (path-b)
**Owner**: `gen-physicist` (orchestrator; sub-dispatches to specialist agents per Path-B file recommendations)
**Output**: `sessions/session-plan/session-87-plan-w13.md`
**Theme**: 2 Path-B precursor items: Step-0 4-agent panel workshop closing 4 research questions before RQ-1+RQ-3 simulator architecture freezes; NC two-torus FGK fixed-point validation as reusable Path-B simulator infrastructure validation
**Items** (2):
- PB-1 `S87-PATH-B-STEP-0-WORKSHOP` — Combined-scope pre-implementation workshop closing 4 research questions (NC fiber discretization #1, cold-start vacuum #2, matching prescription #3, P2→P3/P3→P4 hand-off fidelity #7); PASS = all 4 RQs resolve to architecture-spec-actionable answers; INFO = 1-3 resolve; FAIL = blocking-level theory questions surface. Output: `sessions/framework/path-b-architecture-spec-frozen.md`. Workshop format: 4-agent panel via `/rclab-team` (multi-agent coordinated) OR `/rclab-workshop` 2-agent iterative for 2 strongest pairings (Connes-NCG + spectral-geometer; transit-dynamics + Volovik) run sequentially. (~2 days; gen-physicist orchestrator + 4-agent panel: connes-ncg-theorist + spectral-geometer + transit-dynamics-theorist + volovik-superfluid-universe-theorist)
- PB-2 `S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION` — Implement gradient flow `dD/dτ = -Ric(D)/G_BKM` on Connes-Landi NC two-torus with FGK 1612.06688 closed-form Ricci density. PASS iff `‖h_terminal − h_flat‖_{L²} < 10⁻⁴` at τ_max=100; FAIL if `> 10⁻²` or divergence; INFO band `10⁻⁴ ≤ … ≤ 10⁻²`. Reusable infrastructure validation for any future Path B simulator work. Full pre-registered gate block in context file §3.2. (~2 weeks; spectral-geometer mathematics owner + gen-physicist compute integration)
**Sequencing**: PB-1 PRECEDES PB-2 implementation (PB-1's frozen architecture document specifies modulus and metric choices that PB-2 implements). If PB-1 returns BLOCKED on any of 4 RQs, PB-2 is paused until the underlying RQ is closed in a separate session.
**Natural split candidates** (if W13 planner stalls): W13a = (PB-1 — 4-agent workshop dispatch spec); W13b = (PB-2 — NC two-torus FGK validation script + gate block). PB-2 is naturally a 2-week effort; if PB-1 returns BLOCKED at PB-1 close, PB-2 is automatically deferred (do NOT split-and-shrink the spec; the regular split is by item not by reduction).

---

## §2. Concurrency Plan (≤8 concurrent agents per `feedback_dispatch-discipline.md`)

### Batch 1 — 8 wave planners launched simultaneously
| Wave | Owner | Items | Estimated planner runtime |
|:-----|:------|:------|:--------------------------|
| W1a  | gen-physicist | 7 | ~10-15 min |
| W1b  | gen-physicist | 6 | ~10-15 min |
| W2   | mack-cosmic-bridge | 6 | ~10-15 min |
| W3   | gen-physicist | 5 | ~8-12 min |
| W4   | connes-ncg-theorist | 6 | ~10-15 min |
| W5   | volovik-superfluid-universe-theorist | 5 | ~8-12 min |
| W6   | lizzi-spectral-functional-theorist | 6 | ~10-15 min |
| W7   | lizzi-spectral-functional-theorist | 5 | ~8-12 min |

### Batch 2 — 6 wave planners launched once ≥3 of Batch 1 complete
| Wave | Owner | Items | Estimated planner runtime |
|:-----|:------|:------|:--------------------------|
| W8   | gen-physicist | 8 | ~12-18 min |
| W9   | mack-cosmic-bridge | 7 | ~12-18 min |
| W10  | connes-ncg-theorist | 4 | ~8-12 min |
| W11  | connes-ncg-theorist | 6 | ~10-15 min |
| W12  | connes-ncg-theorist | 8 | ~12-18 min |
| W13  | gen-physicist | 2 | ~10-15 min (workshop spec is heavier per-item than typical compute gates) |

### Concurrency profile
- **Batch 1**: 8 agents concurrent (cap-saturated)
- **Batch 2**: 6 agents concurrent (under cap; cap allows 8)
- **Batch transition**: triggered when ≥3 of Batch 1 complete (per skill §3a; partial overlap is allowed but ≤8 total concurrent)

---

## §3. Stall-Handling Protocol (per skill §3c)

If any per-wave planner reports `killed` or `stalled` without writing its file:

1. **Do NOT re-dispatch with leaner spec.** A stall is an infrastructure event, not a signal to degrade the specification (S84 2026-04-18 precedent: "stalled agents don't mean do it again, but shittier").
2. **Split the wave** along the per-wave "Natural split candidates" line above.
3. **Re-dispatch each sub-wave** with the SAME full-fidelity 13-field per-gate-block spec but narrower item list and reviewer-specific subagent_type matching the sub-wave's homogeneous theme.

Per-wave natural-split tables are inline at each wave block §1 above. **No exceptions**: even W13 (2-item Path-B wave) splits into W13a (PB-1 workshop) + W13b (PB-2 validation) before re-dispatch.

---

## §4. Phase 3e Validation Plan (per skill §3e)

After each wave plan file is written, the orchestrator runs:

```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" \
  computations/_plan_upstream_pin_validator.py --json \
  "sessions/session-plan/session-87-plan-w{i}.md" \
  > "sessions/session-plan/session-87-plan-w{i}-validation.json"
```

Interpretation:
- **Exit 0 (PASS)** — all upstream npz files exist and pin values match payloads → proceed to Phase 4
- **Exit 1 (HARD FAIL)** — slug typo OR pin drift; either edit plan to correct OR document runtime canonical-path rescue rationale per `.claude/rules/gate-verdicts.md` runtime-canonical-path rule
- **Exit 2 (PARSE-ERROR)** — plan structurally malformed; treat as planner-stall-equivalent, split-and-redispatch per §3 above

JSON validator outputs are stored at `sessions/session-plan/session-87-plan-w{i}-validation.json` for each wave; Phase 4 user-checkpoint report reads these files and surfaces non-zero exits verbatim.

Companion validators (orchestrator decides per wave content):
- `_yaml_gate_validator.py` for PRDR machinery checklist + R3 `schema_version` per gate
- `_source_reconciliation_audit.py` for pin-vs-canonical drift across all 5+1 classes
- `_pru_cardinality_audit.py` for cardinality pre-flight
- Manual SUBSTRATE-FIRST-PROVENANCE review (V.1 audit script implementation pending; `.claude/rules/substrate-first-canonical-sourcing.md`)

---

## §5. Reviewer-Origin → Wave-Owner Resolution (per `compute-carryforward.md` "Recommending agent" column)

Mechanical mapping table reproduced from context file §4 for plan-author convenience:

| Recommending column value | Wave-owner subagent_type |
|:--------------------------|:-------------------------|
| `gen-physicist` | `gen-physicist` (W1a, W1b, W3, W8, W13) |
| `mack` (alone) | `mack-cosmic-bridge` (W2, W9) |
| `mack+volovik` | `mack-cosmic-bridge` (W2; mack lead) |
| `mack+connes` | `mack-cosmic-bridge` (W2; mack lead) |
| `mack-cosmic-bridge` | `mack-cosmic-bridge` (W9) |
| `connes+lizzi` | `connes-ncg-theorist` (W4, W10, W12; connes lead) |
| `lizzi+volovik` | `lizzi-spectral-functional-theorist` (W6; lizzi lead) |
| `lizzi+transit` | `lizzi-spectral-functional-theorist` (W7) |
| `lizzi` (alone) | `lizzi-spectral-functional-theorist` (W7) |
| `volovik+connes` | `volovik-superfluid-universe-theorist` (W5; volovik lead) |
| `connes+volovik` | `connes-ncg-theorist` (W11; connes lead) |
| `transit` (alone) | `transit-dynamics-theorist` (sub-dispatch within W9 if W9 splits) |
| `connes-ncg` | `connes-ncg-theorist` (W9 sub-dispatch CF-56) |
| `volovik` (alone) | `volovik-superfluid-universe-theorist` (W11 sub-dispatch CF-70) |

The wave-owner is the planner agent (writes the wave plan file). At compute-mode dispatch, individual gates within the wave may be assigned to OTHER specialist agents (e.g., W11 owned by connes-ncg-theorist as planner, but CF-70 dispatched to volovik for execution; W9 CF-55 dispatched to transit-dynamics-theorist; etc.). The planner-agent ↔ executor-agent distinction is preserved.

---

## §6. Wave-Write Targets Pre-Allocated (no collision between waves)

All wave plan files write to `sessions/session-plan/session-87-plan-w{i}.md` per skill §1b. Output paths:
- `sessions/session-plan/session-87-plan-w1a.md`
- `sessions/session-plan/session-87-plan-w1b.md`
- `sessions/session-plan/session-87-plan-w2.md`
- `sessions/session-plan/session-87-plan-w3.md`
- `sessions/session-plan/session-87-plan-w4.md`
- `sessions/session-plan/session-87-plan-w5.md`
- `sessions/session-plan/session-87-plan-w6.md`
- `sessions/session-plan/session-87-plan-w7.md`
- `sessions/session-plan/session-87-plan-w8.md`
- `sessions/session-plan/session-87-plan-w9.md`
- `sessions/session-plan/session-87-plan-w10.md`
- `sessions/session-plan/session-87-plan-w11.md`
- `sessions/session-plan/session-87-plan-w12.md`
- `sessions/session-plan/session-87-plan-w13.md`

Validator JSON outputs (one per wave):
- `sessions/session-plan/session-87-plan-w{i}-validation.json` (i ∈ {1a, 1b, 2, …, 13})

Wave-collision check at plan-write: Phase 3d/3e verifies each file exists with non-stub content (>15 lines per gate block, file-total ≥ 6×items), greps the expected gate IDs (one per assigned CF), and runs upstream-pin validator. Missing gates trigger sub-wave re-dispatch per §3 stall-handling.

---

**End of session-87-partition.md.**
