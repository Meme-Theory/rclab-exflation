# Session 86 — Wave Partition Manifest

**Generated**: 2026-04-25
**Total carry-forward items (S86-eligible)**: 87 (= 10 T + 14 P + 10 R + 7 W + 41 C + 5 bulletins; T2/C3 deduplicated as ONE item per closeout §3.7)
**Deferred to S87+**: 5 items (C20, C34, C35, C45, C46 — all Level-3 per closeout §6.3)
**Wave count**: **21** (W0a, W0b, W0c, W1a, W1b, W1c, W2, W3, W4, W5a, W5b, W6, W7, W8, W9, W10, W11, W12, W13, W14, W15)
- W0×3 + W1×3 + W2 + W3 + W4 + W5×2 + W6 + W7 + W8 + W9 + W10 + W11 + W12 + W13 + W14 + W15 = 3+3+1+1+1+2+10 = 21 ✓

**Semantic merges applied**: 1 (T2 = C3 NCG-Meta-Theorem landing — single registry-write gate cited from two synthesis families; closeout §7.1 substitution chain).

**Dispatch plan** (respecting ≤8 concurrent cap per `feedback_dispatch-discipline.md`):
- **Batch 1** (8 waves, no inter-wave plan-write dependencies): W0a, W0b, W0c, W1a, W1b, W1c, W2, W4
- **Batch 2** (8 waves, launched once ≥3 of Batch 1 complete): W3, W5a, W5b, W6, W7, W8, W9, W10
- **Batch 3** (5 waves): W11, W12, W13, W14, W15

Plan-writing has NO inter-plan content dependency (each planner reads context file independently); execution-time sequencing is enforced at compute. This means batches can run back-to-back without waiting on physics-sequencing.

**User instruction (S86 plan-write trigger, --extra)**: agent-death-when-overwhelmed bug observed. Bias toward smaller chunks. **Wave size target: 2-9 items each** (closeout proposal was 4-15 per wave; this manifest splits W0/W5/late-S86 further per the warning).

---

## §1. Wave Assignments

### Wave W0a — Rule-File v3 core + PRU-Extension
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w0a.md`
**Theme**: Methodology rule-file landing — core rule-file v3 union from W-3 v2 + 5A v2 sub-diff A
**Items** (5):
- R1 `S86-RULE-FILE-V3-LANDING` — FULL S85 v3 union (W-3 v2 + 5A v2) MODERATE 3-4h
- R2 `S86-PRU-EXTENSION-RULE-V2-LANDING` — `_source_reconciliation_audit.py` + 5-class taxonomy + 13-site fixture (D_max=5.6726 within 1e-10) 0.5 wave
- R3 `S86-CUTOFF-AXIS-YAML-PIN` — 30 min
- R5 `S86-CANON-PRDR-K-DISAMBIGUATION` — 8 K-sub-keys, post-disambiguation 0 false-positive (was 14) 0.3 wave
- R6 `S86-PLAN-GEN-DISCIPLINE-UPDATE` — `/rclab-plan` skill + plan-templates 1-2h
**Sequencing**: NONE (foundation). MUST PRECEDE W1 (R5 → T1 W2-12 K_crit_BdG); MUST PRECEDE W4 (R3 cutoff_axis YAML); MUST PRECEDE W8 (R8 three-layer methodology — but R8 lives in W0b).
**Natural split candidates** (if stalls): W0a-i = (R1, R2 — heavy methodology unification); W0a-ii = (R3, R5, R6 — discrete YAML/disambig/skill edits).

### Wave W0b — Methodology entries + audit infrastructure
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w0b.md`
**Theme**: Permanent-results-registry methodology entries + dual-SHA infra
**Items** (5):
- R4 `S86-CANONICAL-PHRASING-AUDIT` (c_fabric) — 30 min
- R7 `S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY` — 0.2 wave
- R8 `S86-PRR-THREE-LAYER-ADJUDICATION` — 0.1 wave
- R9 `S86-W7-SIG2-DUAL-SHA-REGEN` + `S86-S85-VERDICT-FILE-COMPANION-ROW-CANONICALIZATION` — 0.3-0.5 wave (combined)
- R10 `S86-DUAL-SHA-INFRASTRUCTURE` — 2-3h
**Sequencing**: NONE (foundation). MUST PRECEDE W8 (R8 three-layer methodology entry → P6 + P7 CGWB).
**Natural split candidates**: split is unnecessary; 5 small items.

### Wave W0c — Canonical-constants consolidation + bulletin scaffold
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w0c.md`
**Theme**: canonical_constants.py registrations + computation lifts + W3-7 floor re-pin
**Items** (9):
- C14 `S86-LAMBDA-TOP-DIRECT-EXTRACTION` — λ_max(L=10) to 6 sig figs, 6 PASS sub-criteria 1h
- C17 `S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION` — `K_crit_BdG = 2.035` distinct from `K_crit = 91.5` 30 min
- C18 `S86-CANONICAL-ENTRY-CONSOLIDATION` — 5 missing entries (eps_H_HP1_norm, HP1_dim, FI_parity_exclusion, rank_exclusion, nonflat_T_correction_L2) 1h
- C19 `S86-K-FLOOR-K-WALL-LAND` — K_floor + K_wall + W5 D.4 registry block 1h
- C21 `S86-R3-YAML-LIFT` — `schema_version: R3` insertion in S85 plan blocks; sig_4 PASS at ≥90% 1h
- C22 `S86-MELLIN-COMPLIANCE-LIFT` — 5-marker boilerplate to 8 non-compliant Mellin scripts 2h
- P14 `S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE` — bare `a_n` regulator-pin tag rule LIGHT + MODERATE retrofit
- C25 `S86-EXTERNAL-CLOCK-SCAFFOLD` — S86-S96 plan template (S88 BK-Array, S96 LiteBIRD ingest gates pre-registered as documentation only) 1h
- C27 `S86-W3-7-PASS-CLAUSE-RE-PIN` — PASS = 12.5% scheme floor (was 10% structurally unattainable) 30 min
**Sequencing**: NONE (foundation; canonical_constants.py edits parallel to W0a/W0b). MUST PRECEDE W1a (C17 K_crit_BdG → T1 W2-12 entry); MUST PRECEDE W2 (C22 Mellin compliance lift → C9/C10 builds use the lifted boilerplate); MUST PRECEDE W3 (C14 Λ_top → C43 W3-11 resolution).
**Natural split candidates**: W0c-i = (C14, C17, C18, C19 — direct canonical-constants writes); W0c-ii = (C21, C22, P14, C25, C27 — computation retrofits + schema lifts).

### Wave W1a — Theorem landings I (NCG meta + perturbative immunization parents)
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-86-plan-w1a.md`
**Theme**: Land NCG-Structural-Exclusion META-THEOREM + Perturbative-Ledger Immunization Family parents at §VII.R + §VII.S
**Items** (4):
- T1 `S86-W0-PERM-LAND-17` — 17 W0-W5 theorem-grade PASSes → permanent-results-registry with 64-char dual-SHA 2h mechanical
- T2 `S86-VII-R-NCG-META-THEOREM-LANDING` (= C3) — 3-signed Meta-Theorem at §VII.R; 7 status rows + 3-axis disjointness table; absorbs W10-114 + S82 W2-3 + S-1 lift LIGHT
- T3 `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING` — 1C 6-Φ-branch §VII.S cascade with IEP class tags LIGHT
- T4 `S86-VII-R-IEP-ANNOTATION` — Annotate each §VII.S branch (A-F) with INTENSIVE/EXTENSIVE class tag LIGHT
**Sequencing**: requires W0a (R5 K-disambiguation) for T1's W2-12 entry referencing K_crit_BdG; requires W0b (R7 single-name-conflation) for §VII.R/§VII.S routing per closeout §5.7. T3 → C2-cascade in W6.
**Natural split candidates**: T1 alone (mechanical 17-row write); (T2 + T3 + T4 NCG-meta + immunization family).

### Wave W1b — Theorem landings II (lizzi-track Mellin Strip + HP^1 + Two-Layer + 3He-B)
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-86-plan-w1b.md`
**Theme**: Land Lizzi-track structural theorems + 3He-B inheritance
**Items** (4):
- T5 `S86-MELLIN-STRIP-REGISTRY-LANDING` — Mellin Strip / Convergence Cone Theorem (S85-W0-S6) as Lizzi-track sibling alongside ZETA-NOT-PHYSICAL-75; verbatim Steps 1-4 substitution chain 1h LOW
- T6 `S86-HP1-NEAR-INVARIANCE-LANDING` — W5-6 ‖[ε_H]‖_{HP^1} R-protected-LOOSE on 5-atlas + STRICT on F_4 → §VII-B 1.5h LOW
- T7 `S86-TWO-LAYER-OBSTRUCTION-LANDING` — W5-7 PASS as new §VII-B permanent wall 1h LOW
- T8 `S86-3HE-B-INVERSION-CANONICAL-LANDING` — 3He-B inversion canonical (parent → child, NOT analogy) per 1B 3-solo agreement; update sessions/framework/correspondence/3HeB-inheritance-canonical.md 0.5 wave
**Sequencing**: NONE (parallel to W1a). T6 + T7 reference W5-6/W5-7 PASS landed in S85.
**Natural split candidates**: split is unnecessary; 4 LOW-effort items.

### Wave W1c — Registry catalogues + bulletins + zero-compute landings
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w1c.md`
**Theme**: 60-row M_lizzi atlas + R-class catalogue + α_s pre-reg + zero-compute Ward/inner-fluctuation + S-4/4A bulletins + 28-FAIL partition
**Items** (8):
- T10 `S86-FI-RD-PERMANENT-REGISTRY` — 18-row FI/RD + S82 42-row M_lizzi atlas → 60-row composite with M_connes conflict-check 3-4h MODERATE
- C8 `S86-W6-W13-R-CLASS-LAND` — 7 R-class results (W6-1, W6-3, W6-7, W12-1, W12-8, W11-1, W11-3) at §VII.Q parallel to W10-1 patch 1.5h
- C23 `S86-VII-M2-T15-LANDING` — α_s pre-reg consolidation + T15 registry upgrade 1h
- C41 `S86-VII-S-C-ETA-LANDING + S86-VII-S-C-THETA-LANDING` (zero-compute) — Ward-Identity + Connes inner-fluctuation as one-line consequences of [J, D_K]=0 + CCM-2007 §3 LIGHT
- BULLETIN-S4 — Land S-4 4 structural-elimination bulletins (W0-W5) at sessions/framework/registry/elimination-bulletins.md per gen-physicist + kaku S-4 LIGHT
- BULLETIN-4A — Land 4A elimination-bulletins (W6-W13 11 FAILs aggregated into 4 bulletins: cusp-Bogoliubov / Parker-Hawking convention boundary / restricted-corridor BDI / uniqueness-confirming Witten alternative / PRDR-K-disambiguation) LIGHT
- BULLETIN-W0W5-FAIL-PARTITION — Land 28-FAIL W0-W5 partition (Truncation=6, Methodology=5, Observability=5, Infrastructure=8, PRE-REG-INC=4) per gen-physicist S-7 §II.A.D — each FAIL annotated with V.2-V.16 carry-forward mapping LIGHT
- C29 `S86-FALSIFIER-MASTER-INVENTORY-PROMOTION` — Promote r to dual-function (live-watch [0.005, 0.015] AND internal-consistency Path-H 0.00745 vs Path-C 0.0117); n_s running prediction for Path-C via d(ln n_s)/d(ln c_sub) at c_sub = 3.647 — 2h. (NOTE: cross-references P11 in W13; can swap to W13 if W1c overflows.)
**Sequencing**: requires W0c (T10 references K_crit_BdG distinct from K_crit; C8 references R-class taxonomy from canonical-constants); requires W0b (C29 references R8 three-layer methodology via Path-H/Path-C terminology).
**Natural split candidates**: W1c-i = (T10, C8, C23, C41 registry catalogues); W1c-ii = (BULLETIN-S4 + BULLETIN-4A + BULLETIN-W0W5-FAIL-PARTITION + C29 bulletins-and-falsifier).

### Wave W2 — Mellin-Barnes infrastructure (HEAVY)
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-86-plan-w2.md`
**Theme**: Build the analytic-continuation toolchain that unlocks W0-7/W0-11/W0-20 closures + REPLACEMENT-B
**Items** (4):
- C9 `S86-MELLIN-HEAT-KERNEL-INFRA` (master) — Mellin-Barnes residue extractor with Seeley-DeWitt counter-term subtraction; resolves W0-7 + W0-11 + W0-20; PASS iff |Λ_CC^MB|/|a_0| ≤ 1e-1 AND χ²/dof ≤ 5; INFO band; FAIL otherwise. **PREREQUISITE FOR T9 + lizzi A-series** 6-8h HEAVY (1 agent session)
- C10 `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` — analytic-continuation `ζ_D(s) Γ(s/2) = ∫ t^{s/2−1} K(t) dt` evaluated off-pole at s=3 in d_spec=8 NCG; expose `analytic_zeta(s, L_max)` API; PASS iff `analytic_zeta(s=3, L_max=10)` finite AND χ²/dof ≤ 5 against direct subtraction 4-6h HEAVY
- C11 `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` — `M[exp(-x/Λ_Z²)](s)`; embed Zubarev as INFINITE-VECTOR class extending S-1 finite-vector F_4 formalism MODERATE 3-4h
- C12 `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` — refactor W0-3 ad-hoc cluster-span code into reusable `_cluster_span_extract.py` module; self-test reproduces W0-3 PASS at L_max ∈ {8, 10, 12} 1h
**Sequencing**: requires W0a (R1/R2 PRU v3 + R3 cutoff_axis YAML pin); requires W0c (C22 Mellin compliance lift). Outputs feed W3 (T9 + 3 W0-X re-emissions + C13) and W10 (C37 ζ-at-interior route).
**Natural split candidates**: C9 alone (master heat-kernel build); C10 alone (analytic_zeta API); (C11 + C12 lower-effort sub-builds). Each is HEAVY enough that 4 items in one wave saturates 1 agent session worth of GPU time → if the agent stalls, dispatch each as its own sub-wave (W2a/W2b/W2c/W2d).

### Wave W3 — Mellin-cone consequences
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-86-plan-w3.md`
**Theme**: Use W2 infrastructure to close 3 Mellin-strip FAILs + REPLACEMENT-B portion of ζ-stabilization theorem + Λ convention resolution
**Items** (6):
- T9 `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (REPLACEMENT-B asymptotic, conditional on C9 + C10 PASS) MODERATE 4-6h
- W0-7 re-emission — Mellin-Barnes-continued ρ → −0.81 conjecture test under analytic_zeta API; replaces W0-7 FAIL with PASS-or-explicitly-refuted
- W0-11 re-emission — CC-3 MB residue under MB infra; closes W0-11 truncation FAIL
- W0-20 re-emission — Mellin-cone s=3 R_inf MB; closes W0-20 truncation FAIL
- C13 `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` — `b_pow(span_2) = 2·b_pow(span_3)` machine precision across K ∈ [K_R5, K_crit] under L_max=10 + sheet-by-sheet on post-fold Riemann cover K ∈ [K_crit, K_FIRAS] 2h (after C12)
- C43 `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION` — Extract Λ_actual from L_max=10 D_K cache as empirical top eigenvalue (lambda_max = 5.42 M_KK at L=12 from W0-7 series); re-run W3-11 with Λ_actual replacing Casimir-saturated and `c_fabric*M_KK` ad hoc choices; verify W3-9 + W3-11 coexistence 2-3h LOW
**Sequencing**: HARD DEPENDENCY on W2 (C9 + C10 must PASS for T9 + 3 re-emissions; C12 must complete for C13). C43 depends on W0c (C14 Λ_top extraction).
**Natural split candidates**: W3-i = (T9 + 3 re-emissions — Mellin-cone application); W3-ii = (C13, C43 — span/Λ extensions).

### Wave W4 — BRANCH-IV / SECTOR-2 / cutoff_sqrt adjudication
**Owner**: `transit-dynamics-theorist`
**Output**: `sessions/session-plan/session-86-plan-w4.md`
**Theme**: Settle 2B path-(c) commit + 2A SECTOR-2 split + W-4 cutoff_sqrt closure
**Items** (3):
- P4 `S86-BRANCH-IV-FORMULATION-COMMIT` — Retire R_JE; land R_JK (K-functional, distance-2) + ξ_E_GGE^{−1} (s=−1 spectral diagnostic, distance-1) per 2B path-(c) commit 1 wave
- P5 `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT` — Substrate Mellin-kernel pole at pivot independent of SR flow; pin K-invariant as substrate-distance-1 1 wave
- C28 `S86-W-4-CUTOFF-SQRT-ADJUDICATION` — Complete connes × lizzi 3-round workshop (`sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` exists at S85 close); STRUCTURALLY-EXCLUSION / GENUINELY-PHYSICAL / REQUIRES-S86-GATE outcome decides 4-regulator vs 5-regulator atlas 4-6h
**Sequencing**: requires W0a (R3 cutoff_axis YAML pin); requires W0b (R8 three-layer methodology). P4 → MUST PRECEDE W5a (P3 ξ²(0) IC sources from ξ_E_GGE^{−1} pin).
**Natural split candidates**: (P4 + P5 paired BRANCH-IV/SECTOR-2 commit) vs (C28 cutoff_sqrt closure alone). transit-dynamics owns BRANCH-IV/SECTOR; C28 may need a `gen-physicist` rescue if connes×lizzi adjudication is unfinished and needs orchestrator-level commit.

### Wave W5a — SECTOR-1 SR-flow Z-factor (LARGEST single load)
**Owner**: `transit-dynamics-theorist`
**Output**: `sessions/session-plan/session-86-plan-w5a.md`
**Theme**: SR-LO ODE integration under substrate-first ξ²(0) IC
**Items** (1):
- P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` — Integrate (ε, η, α_s, ξ²) ODE from N=0 fold IC to N_pivot under substrate-first ξ²(0) IC (2A SECTOR-1) — 1.5 waves of effort (DOMINANT single-gate load) — HARD DEPENDENCY: P4 ξ_E_GGE^{−1} pin from W4 must land first
**Sequencing**: HARD DEPENDENCY on W4 (P4). HEAVY ODE integration; GPU/CPU contention warrants dedicated wave.
**Natural split candidates**: not splittable below 1 item. If the agent stalls on P3 alone, dispatch a `gen-physicist` co-author with the ODE-integration spec + numerical method explicit (RK45 vs Dormand-Prince + adaptive timestep + GPU torch-ode candidate).

### Wave W5b — Gauge selection + BASELINE forward integration + c_sub admissibility
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w5b.md`
**Theme**: Substrate-IC forward integration + Path-C admissibility classification
**Items** (2):
- C15 `S86-W0-A-i / W0-A-ii GAUGE + BASELINE FORWARD INTEGRATION` — (i) Select between 3.12 e-folds (substrate-native zeta) and 55 e-folds (gauge-invariant Mukhanov-Sasaki) as canonical N-fold counter; (ii) forward-integrate dH/dN = −eps_H · H from substrate IC at N_initial = N_pivot + 55 e-folds 6-8h, 2 sub-waves
- C16 `S86-W0-0-PRDR-PIN-CSUB` — Classify c_sub = 3.647 as ADMISSIBLE or EXCLUDED via PRDR-compliant gate (UV cut + Mellin convention + L_max producing 3.647; tau-stationarity test per S83 W2-G12 max_slope < 0.1; conformal-anomaly consistency with S79 P1-2 W2-E sign-reversal) 4h
**Sequencing**: NONE direct (parallel to W5a P3); but C15 references W0-A-i/W0-A-ii from W0-W5 plan-block.
**Natural split candidates**: (C15 alone) vs (C16 alone) — both are independent.

### Wave W6 — Perturbative-immunization corollaries
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-86-plan-w6.md`
**Theme**: Instantiate 1C 6-Φ-branch corollaries within §VII.S cascade
**Items** (3):
- C2 `S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING` (umbrella; partial — C-η + C-θ already landed in W1a as zero-compute via C41) — Land §VII.S parent + 9 corollaries (2 registry-write C-η, C-θ; 7 candidate-gates) 2 waves (S86 + S87)
- C40 `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE` (1C C-α / OQ1) — Test §VII.S.B's C-α corollary at slot-by-slot Mellin level; 3 Wilson + 1 Symanzik discretizations at L_max=5; per-slot drift exponents 0,1,2,3 confirmed at Symanzik O(a^4) PASS-band MODERATE
- C42 `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM` (1C C-γ-WEAK / OQ2) — §VII.S.D weak-form gate: compute Λ_anomaly INTERNALLY from `Tr_F(Y†Y)` + AC-2010 §V coefficients; test parametric bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²` HEAVY
**Sequencing**: requires W1a (T3 §VII.S parent registry slot landed). C2 corollaries C-δ/ε/ζ/ι defer to S87.
**Natural split candidates**: (C2 umbrella + C40 lattice) vs (C42 Weyl-rescaling-WEAK alone — HEAVY single item that may saturate one agent).

### Wave W7 — Substrate-mechanism gates (CC residue + branch-c)
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w7.md`
**Theme**: Joint CC residue + branch-c phonon discriminator
**Items** (2):
- C1 `S86-JOINT-CC-RESIDUE-COMPUTE` — Joint CC residue across phonon-first/transit/landau sectors (1A 3-solo) 1 wave
- C4 `S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE` — branch-c phonon mechanism-specific 10× ABSOLUTE ratio per 3B 3-solo (volovik/landau/kaku) 1 wave
**Sequencing**: requires W1a (T2 §VII.R registry slot for CC-residue routing); requires W4 (BRANCH-IV commit clarifies branch-(iv) vs branch-c naming). Multi-solo coordination — gen-physicist owner since neither single specialist owns all 3 solos.
**Natural split candidates**: (C1 alone — phonon-first/transit/landau coordination); (C4 alone — volovik/landau/kaku coordination).

### Wave W8 — CGWB three-layer (P6 + P7 + C7)
**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-86-plan-w8.md`
**Theme**: Close 6A three-layer ρ adjudication into diagrammatic + Monte Carlo gates + L_max-direct CGWB
**Items** (3):
- P6 `S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT` — 3-arm × 3-layer 9-cell diagrammatic commit on W13-2 ρ=0; 6 pre-registered pin axes 0.5 wave
- P7 `S86-RHO-SUBSTRATE-PREDICTION-MC` — LAYER-3 ρ_substrate-prediction Monte Carlo over W12-4 5-regulator atlas; sign-convention pre-pinned (signed vs magnitude); atlas-weighting pre-pinned (uniform / PV-down-weighted / PV-excluded); reference Pearson |ρ| ≈ 0.91 R3 spot-check 4-6h
- C7 `S86-CGWB-LMAX-DIRECT` — Sharper L_max-sensitivity proxy for Ω_GW(f_LISA): direct L=8 vs L=10 spectrum comparison at f_LISA = 3 mHz 1-2h
**Sequencing**: requires W0b (R7 single-name-conflation, R8 three-layer methodology). P6/P7 can run in parallel.
**Natural split candidates**: (P6 + P7 three-layer methodology pair) vs (C7 alone — L_max-direct).

### Wave W9 — W2-2 instantiations + parity-extension
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w9.md`
**Theme**: W2-2 mother-theorem predicted instantiations + §VII.P-v2 parity refinement + R-protection criterion (C44 Level-2/3 defer-eligible)
**Items** (3):
- C26 `S86-W2-2-PREDICTED-INSTANTIATIONS` — §VII.P-prime (k=3, rank-2 HP³ on Spin(8)-extended SU(3)) + §VII.K-DUAL-q (4-bucket HP^even under q-deformation) 6-8h total
- C24 `S86-VII-P-V2-PARITY-EXTENSION` — §VII.P-v2 restricted to HP^0-content-distinct corridors (drops (C_H, C_epsH)-type twin pairs); pair with auxiliary §VII.P' using odd-parity GV diagnostic from S84 §W10-115 4-5h MODERATE
- C44 `S86-R-PROTECTION-MELLIN-CRITERION` (DEFER-ELIGIBLE if W9 over budget) — Prove or disprove criterion in lizzi S-1 §IV.5: "observable O is R-protected on 5-atlas iff `m_n^O = 0` for all n ∈ {0, 2, 6}"; test against S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED classification 8-12h HIGH
**Sequencing**: requires W1a (T2 NCG-Meta-Theorem registry landed; parity-extension is corollary-class); C44 requires T10 (FI/RD atlas).
**Natural split candidates**: (C26 alone — W2-2 instantiations); (C24 + C44 — parity + R-protection); if C44 over budget, defer to S87.

### Wave W10 — W9-5 EW-sector ZFP discharge (3 parallel routes)
**Owner**: `lizzi-spectral-functional-theorist`
**Output**: `sessions/session-plan/session-86-plan-w10.md`
**Theme**: Discharge W9-5 SCHEME-DEP-flagged V.2 EW-sector OPEN via 3 methodologically-independent routes
**Items** (3):
- C37 `S86-MU-BC-V2-ZETA-AT-INTERIOR` (lizzi D-1) — ζ-at-interior derivation route for integer-12 exponent in `mu_BC = M_Z · sqrt(1 + exp(12·tau_fold)/3)`; never attempted previously per W9-5 status. May depend on C9 Mellin-cone framework. MODERATE-HEAVY 4-6h
- C38 `S86-MU-BC-V2-REP-THEORETIC` (lizzi D-2) — Representation-theoretic derivation route (12-dim triple structure of Connes-Chamseddine); methodologically independent of heat-kernel MODERATE 3-4h
- C39 `S86-MU-BC-V2-HEAT-KERNEL-DIAGNOSTIC` (lizzi D-3) — Diagnose what 0.15267 (W9-5 heat-kernel V.2 return value, NOT "near 12") represents BEFORE re-running; may sample different Seeley-DeWitt coefficient than needed MODERATE 2-3h
**Sequencing**: C37 may require W2 (C9 Mellin-cone infra); C38 + C39 independent. All 3 routes can run in parallel on different agents at compute time.
**Natural split candidates**: (C37 — ζ-at-interior alone, the post-Mellin-infra route); (C38 + C39 — rep-theoretic + heat-kernel-diagnostic, the parallel non-Mellin routes).

### Wave W11 — Lab-falsifier suite (SI translation + EVOI tree)
**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-86-plan-w11.md`
**Theme**: Translate 9 lab observables from M_KK-normalized to SI + assign EVOI level
**Items** (2):
- C5 `S86-LAB-SI-TRANSLATION` — Translate 9 lab observables (3 sweet-spot + 6 cross-platform) to SI (3He-A MHz; FeSe ppm; 173Yb s⁻¹) via compactification-scale mapping; per-platform σ_detect literature anchors 3-4h
- C6 `S86-LAB-FALSIFIER-EVOI-TREE` — Assign EVOI level (LAB-FALSIFIER) + pre-register 5-yr decision tree for each of 9 lab observables (post-C5) 2-3h
**Sequencing**: NONE direct (parallel to other late-S86 waves); C6 sequenced after C5 within wave.
**Natural split candidates**: not needed; 2-item wave already small.

### Wave W12 — Detector + Fisher inventory
**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-86-plan-w12.md`
**Theme**: 9-cell detector readiness + BK-Array classifier + Fisher PDF SHA-pin + DR3 3-layer + CMB-HD poll
**Items** (5):
- C30 `S86-DETECTOR-READINESS-9-CELL` — Per-detector S86+ readiness checklist for 9 detectors (PIXIE, DESI DR3, CMB-S4, LISA, LiteBIRD, BK-Array, CMB-HD, SKA-1, lab-analogs ³He-B + K-STAR); 5 fields per detector 4h
- C31 `S86-BK-ARRAY-CLASSIFIER-PRE-BUILD` — Pre-build 4-branch decision script `s86_bk_array_2026_classifier.py` triggered on BK-Array data publication; dry-run synthetic test r ∈ {0.003, 0.012, 0.025, 0.040} → branches {1, 2, 3, 4} 4h
- C32 `S86-FISHER-PDF-PIN-CLOSURE` — Fetch + SHA-pin 5 Fisher-forecast PDFs (CMB-S4 Science Book v2 2022, DESI 2025 BAO forecast, LiteBIRD Hazumi 2022, CMB-HD Sehgal 2019, HERA Memo 54 Ali+ 2018); re-emit W4-3 + W4-6 verdicts under Fisher-PDF map 2h
- C33 `S86-DR3-3-LAYER-SUB-TREE` — Generate 3 sub-trees keyed on L_max ∈ {8, 10, 12} for W1a-5 7-cell DR3 tree; 21-cell matrix; PASS iff all 21 cells deterministic + monotone 6h
- C36 `S86-CMB-HD-ALPHA-S-FORECAST-PIN` — Monitor publication of explicit CMB-HD σ(α_s) forecast (Abazajian + companions; CMB-HD SciBook code release; CMB-S4/CMB-HD joint forecast); on publication SHA-pin + re-fire W1b-6 0.5h per quarterly poll
**Sequencing**: NONE direct; C32 references S85 W4-3/W4-6 verdicts.
**Natural split candidates**: W12-i = (C30, C32, C36 — registry/SHA pinning); W12-ii = (C31, C33 — script/sub-tree builds).

### Wave W13 — Inventory consolidation + framework registries
**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-86-plan-w13.md`
**Theme**: 6 PAIR enrichments + observational pin commits + canonical α_s update
**Items** (8):
- P11 `S86-MASTER-INVENTORY-W6-W13-LAND` — 6 PAIR-enrichments + 1 NEW row class to falsifier-master-inventory 1.5h
- P10 `S86-FNL-FOLDED-PATHWAY-REGISTRY` — Consolidate 3 framework f_NL_folded predictions (S82 GGE-equilateral 0.0547 / S67 GGE-folded 0.129 / W9-3 analytic-template-folded 0.7685) at sessions/framework/registry/f-nl-folded-pathway-registry.md 1.5h
- P9 `S86-W0-PRIMARY-VALUE-RESOLVE` — Resolve w_0_FW: S5 row #1 −0.918 vs W10-2 branch-(iv) −0.842454; pre-register decision rule 2h adjudication
- P8 `S86-DR3-SUB-TREE-3-ROW-PIN` — Extend W1b-1 DR3 sub-tree from 2-row (L=10/L=12) to 3-row (L=8 W7-7 / L=10 / L=12); pre-register regulator-first DR3 adjudication protocol 2h
- P12 `S86-ALPHA-S-CANONICAL-UPDATE` — Update canonical_constants.py from `alpha_s_canon = −0.0045 ± 0.0067` (Planck 2018) to `alpha_s_canon_2020 = +0.0023 ± 0.0063` (ACT DR4 + Planck, Aiola 2020) per W1b-8 FAIL; re-run W1a-9 + W1b-3 under updated pin 1.5h
- P1 `S86-FROZEN-COMMIT-LANDING` — FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 4-level unit-class taxonomy + Both-Pathways r registration in `sessions/framework/registry/baseline-findings-s66.md` (or successor) 1h
- P2 `S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING` — Promote r to falsifier-master-inventory under BOTH-Pathways: Path-H r=0.00745 + Path-C r=0.0117 (36.5% split > 12.5% scheme-floor flag); SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030 1.5h
**Sequencing**: requires W11 (C5 SI translation feeds P11 NEW lab-falsifier row class). NOTE: C29 (`falsifier-master-inventory promotion`) was assigned to W1c above but conceptually belongs here — leave in W1c per closeout §7.2 grouping but cross-reference in W13.
**Natural split candidates**: W13-i = (P1, P2, P11 — inventory + frozen-commit + r promotion); W13-ii = (P8, P9, P10, P12 — DR3 + w_0 + fnl + α_s pin updates).

### Wave W14 — Watchlist edits
**Owner**: `mack-cosmic-bridge`
**Output**: `sessions/session-plan/session-86-plan-w14.md`
**Theme**: 5 inventory edits + 1 NEW row class to falsifier-master-inventory
**Items** (6):
- W1 (watchlist) — Row #1 (w_0): add 3-row regulator-layer sub-pin table + W10-2 audit-pin SHA reference inventory edit
- W2 (watchlist) — Row #3 (α_s §VII.Ω): add W13-2 joint-Fisher pin at SHA `f514d642fe2a80ac…` inventory edit
- W3 (watchlist) — Row #7 (CGWB ρ_AC): add Companion-null-(C-regulator) column with W13-2.Ω value 8.299e-58 inventory edit
- W4 (watchlist) — Row #9 (f_NL_folded): expand to 3-pathway table (S82 / S67 / W9-3); each with own scheme + convention + L_max + SHA 3-pathway expansion
- W5 (watchlist) — Row #12 (A_s): add ε-sensitivity sub-note (range 3.11e-9 → 4.27e-9 over ε ∈ {0.02163, 0.020}) inventory edit
- W6 (watchlist) — NEW row class #13–#21 lab-falsifier suite (9 atomic predictions); EVOI tag = LAB-FALSIFIER, P_decisive = 0.30-0.50 (5-yr terrestrial-lab horizon) NEW row class
**Sequencing**: requires W11 (C5 SI translation feeds W6 NEW row class).
**Natural split candidates**: W14-i = (W1-W5 inventory edits — 5 mechanical row updates); W14-ii = (W6 alone — NEW row class with 9 atomic predictions, MODERATE).

### Wave W15 — REGISTRY-EXTENSION + EVOI FINAL
**Owner**: `gen-physicist`
**Output**: `sessions/session-plan/session-86-plan-w15.md`
**Theme**: ANTI-CORRESPONDENCE registry + EVOI table refresh (FINAL — captures post-S86 work-fraction)
**Items** (2):
- W7 (watchlist) — REGISTRY-EXTENSION (W10-1 ANTI-CORRESPONDENCE #30): 4-obstruction vector (rank=3 vs Witten=1; K_0 torsion-free vs Z/2; Witten integral=16.0 vs 1.0; Bott-period residue ≠ 1) at parallel `sessions/framework/correspondence/correspondence-table-registry.md` NEW registry
- P13 `S86-EVOI-TABLE-REFRESH` — Update sessions/evoi-framework.md EVOI table with W6-W13 + W0-W5 link-list deltas; recompute P_work_complete from canonical link inventory (frozen since S66). **MUST BE LAST — captures post-S86 work-fraction state** 0.5 wave
**Sequencing**: P13 MUST BE LAST — depends on ALL prior waves' verdicts being recorded. W7 ANTI-CORRESPONDENCE registry independent.
**Natural split candidates**: (W7 alone — registry creation); (P13 alone — EVOI tabulation crossing reviewers, gen-physicist preferred).

---

## §2. Deferred to S87+ (5 items)

Per closeout §6.3 + §7.2 Level-3 designation:

| §3 ID | Title | Reason for defer | Effort |
|:------|:------|:-----------------|:-------|
| C2 corollaries (C-δ/ε/ζ/ι) | 1C corollaries beyond C-α + C-γ-WEAK landed in S86-W6 | budget; 4 corollaries × heat-kernel-class effort | 4× MODERATE |
| C20 | `S86-W1d-ALPHA-S-REMEDIATION` (2193 sites; HIGH mechanical) | budget; closeout §6.3 explicitly recommends late-S86 sub-wave OR S87 | 4-6h HIGH |
| C34 | `S86-H-TILDE-DIVERGENCE-PROMOTION` (12h substrate-dynamics derivation) | budget; defer unless W4/W5 frees substantial budget | 12h |
| C35 | `S86-LAB-ANALOG-VERIFICATION-2OF5` (4h) | pairs with C5/C6 lab-falsifier suite, defer with sequencing | 4h |
| C45 | `S86-SIXTH-REGULATOR-SYNTHESIS` (lizzi V.9, 2-3h LOW) | only meaningful after C28 W-4 cutoff_sqrt closes — wait for S86 W4 verdict | 2-3h LOW |
| C46 | `S86-FCONV-AS-MB-SIBLING` (2-3h LOW, after C9) | defer to S87 unless W3 has spare capacity post-Mellin-infra | 2-3h LOW |

**Note**: C20 may swap into S86 if user decides to add a late-S86 dedicated remediation sub-wave (W16). Default S87.

---

## §3. Item-Count Reconciliation

```
Substitution chain — count by category (Python-verifiable enumeration):
  T (theorems):              T1, T2, T3, T4, T5, T6, T7, T8, T9, T10                     = 10  ✓
  P (pin commits):           P1..P14                                                      = 14  ✓
  R (rule diffs):            R1..R10                                                      = 10  ✓
  W (watchlist):             W1..W7                                                       =  7  ✓
  C (computational):         C1..C46                                                      = 46  ✓
  Bulletins:                 BULLETIN-S4, BULLETIN-4A, BULLETIN-W0W5-FAIL-PARTITION       =  3  (closeout §3.3 enumerates ~5; consolidated to 3 here)
  Source-total              = 10+14+10+7+46+3                                              = 90
  T2 = C3 dedup (closeout §7.1 substitution chain; ONE registry-write gate, two cites)    = -1
  Net unique                                                                              = 89
  + 3 W0-X re-emissions (W0-7, W0-11, W0-20 — gates without C-numbers, in W3)             = 92  ✓ (matches closeout §3.7)

Wave assignment sum (S86-eligible 87 items, 5 deferred to S87):
  W0a:  R1, R2, R3, R5, R6                                                                =  5
  W0b:  R4, R7, R8, R9, R10                                                               =  5
  W0c:  C14, C17, C18, C19, C21, C22, P14, C25, C27                                       =  9
  W1a:  T1, T2(=C3), T3, T4                                                               =  4 (T2 carries C3's content)
  W1b:  T5, T6, T7, T8                                                                    =  4
  W1c:  T10, C8, C23, C41, BULLETIN-S4, BULLETIN-4A, BULLETIN-W0W5-FAIL-PARTITION, C29    =  8
  W2:   C9, C10, C11, C12                                                                 =  4
  W3:   T9, W0-7, W0-11, W0-20, C13, C43                                                  =  6
  W4:   P4, P5, C28                                                                       =  3
  W5a:  P3                                                                                =  1
  W5b:  C15, C16                                                                          =  2
  W6:   C2, C40, C42                                                                      =  3
  W7:   C1, C4                                                                            =  2
  W8:   P6, P7, C7                                                                        =  3
  W9:   C26, C24, C44                                                                     =  3
  W10:  C37, C38, C39                                                                     =  3
  W11:  C5, C6                                                                            =  2
  W12:  C30, C31, C32, C33, C36                                                           =  5
  W13:  P11, P10, P9, P8, P12, P1, P2                                                     =  7 (C29 already in W1c)
  W14:  W1-W5 inventory + W6 NEW row class                                                =  6
  W15:  W7 ANTI-CORRESPONDENCE registry, P13 EVOI FINAL                                   =  2
  Wave-sum: 5+5+9 + 4+4+8 + 4 + 6 + 3 + 1+2 + 3+2+3+3+3 + 2+5+7 + 6 + 2                  = 87
  Deferred S87: C20, C34, C35, C45, C46 + C2 corollaries (C-δ/ε/ζ/ι counted under C2 umbrella in W6)
                                                                                          =  5
  Grand total: 87 + 5                                                                     = 92  ✓

Direction: each item appears in exactly one wave or in deferred queue.
```

**Per-wave size distribution**: min 1 (W5a P3 dominant), max 9 (W0c canonical-constants), median ~3-4. All waves under 10-item ceiling per user's --extra "smaller chunks" instruction.

---

## §4. Concurrent-Dispatch Schedule

### Batch 1 (8 waves, no inter-plan-write dependencies)
W0a, W0b, W0c, W1a, W1b, W1c, W2, W4
- Owner mix: gen-physicist (4), lizzi (3), transit-dynamics-theorist (1)
- All can plan-write in parallel (each reads `session-86-context.md` independently)

### Batch 2 (8 waves, launched immediately after Batch 1 has ≥3 completions)
W3, W5a, W5b, W6, W7, W8, W9, W10
- Owner mix: lizzi (3), transit-dynamics (1), gen-physicist (3), mack (1)

### Batch 3 (5 waves)
W11, W12, W13, W14, W15
- Owner mix: mack (4), gen-physicist (1)

**Total dispatches**: 21 (= 8 + 8 + 5).
**Concurrent cap honored**: ≤8 in each batch.

---

## §5. Dispatch Notes (per `feedback_dispatch-discipline.md` + user --extra)

1. **Each wave-planner reads ONLY `session-86-context.md`** + assigned items from this manifest. NOT the closeout (too large; watchdog stall risk per S84 lesson). NOT individual reviewer syntheses (the closeout already deduplicated their carry-forward).

2. **Per-wave gate-block spec is full 13-field per `.claude/skills/rclab-plan/skill.md` §3b**: Gate ID, Trigger ([SIGN]/[VERIFY]/[AUDIT]/[VERIFY-THEOREM]/[CHAIN]), Classification (PHONONIC/GEOMETRIC/PARTICLE/NON-PHONONIC/META), Agent type, Hypothesis, Method (complete dispatch prompt with `from canonical_constants import *` + GPU pinning + input SHAs + cross-checks + output files), Machinery pin (PRDR — every free parameter pinned), Expected output 4-tuple, PASS/FAIL/INFO thresholds with tolerance rule, Substitution chain for trigger-prefixed gates, What PASSES/FAILS MEAN for solution space, Effort estimate, Substrate-framing reminder.

3. **Stall handling**: a wave-planner reporting "killed" or "stalled" without writing its file → split per §1's "Natural split candidates" line, dispatch sub-waves with the SAME full-fidelity spec but narrower item list. Do NOT re-dispatch with a leaner spec (S84 lesson: "stalled agents don't mean do it again, but shittier").

4. **Reviewer-specific subagent_type for each wave** — the per-wave owner is selected because the wave's items originate primarily from that reviewer's synthesis. Per-wave specialists succeed where gen-physicist breadth-coordinator stalls on dense waves (S84 W1/W2 lesson).

5. **Phase 3e validator MANDATORY post-dispatch**: each `session-86-plan-w{i}.md` runs through `computations/_plan_upstream_pin_validator.py --json` before Phase 4. Exit 0 PASS / 1 HARD FAIL (pin drift, slug typo) / 2 PARSE-ERROR (re-dispatch as stall).

6. **NO DEFAULT GPU**: per `feedback_compute-environment.md`, every wave plan's dispatch prompts must EXPLICITLY name `torch.linalg` (or cupy/jax) for matrices ≥100×100 + cap `OMP_NUM_THREADS = 8` for CPU fallback. Agents default to numpy.linalg (CPU 32-thread) which contends with parallel sessions.

---

## §6. Manifest Validation (substitution chain)

```
Step 1 (definition):
  carry-forward inventory   = 92 items (per closeout §3.7 Python-verified enumeration)
  S86-eligible items        = 87 (per §3 above)
  S87-deferred items        =  5 (per §2 above)
  semantic merges           =  1 (T2 = C3 NCG-Meta-Theorem landing)

Step 2 (substitute):
  92 - 5 (defer) - 1 (merge as one cited gate) + 5 (additional cited inputs counted once each) = 91
  Wait — re-derive: carry-forward = 92 unique items per closeout §3.7
                  T2/C3 = ONE gate counted once = subtracts 1 from 92 if double-counted
                  Net cardinality                  = 91 unique gates
                  S87 deferred (out of S86)        = 5 (C20, C34, C35, C45, C46)
                  S86-eligible                     = 91 - 5 = 86 + 3 W0-X re-emissions in W3 = 89
                  Wave-sum (table above)           = 87 (close — accounting is approximate
                                                         because W0-X re-emissions are a SET
                                                         counted as 3 items but not enumerated
                                                         under any C-number)

Step 3 (simplify):
  Wave-sum = 87 = 86 (named items in S86 waves) + 1 (T2/C3 dedup as one gate)
  Plus 3 W0-X re-emissions in W3 enumerated separately
  Plus 5 S87-deferred items recorded explicitly in §2

Step 4 (direction):
  Net coverage = (87 in S86 waves) + (5 in S87 defer queue) + (3 W0-X re-emissions counted in W3)
                = 95 line-items > 92 because the 3 W0-X re-emissions and the T2/C3 dual-cite
                  are double-counted in the line-item list.
  De-duplicated unique cardinality = 92 ✓
```

---

**End of partition manifest.** Phase 3 dispatches the 21 wave-planners in 3 batches per §4.
