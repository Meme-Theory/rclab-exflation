# Session 86 — Context File

**Generated**: 2026-04-25
**Topic label**: Can't Stop, Won't Stop (S86 carry-forward plan)
**Prior session**: S85 (W0-W5 + W6-W13 dual-campaign, 16 waves, 149 verdicts)
**Closing source**: `sessions/archive/session-85/session-85-full-s85-closeout.md` (1005 lines, gen-physicist sole writer)
**Generator**: `/rclab-plan --session 86` (consolidate mode, swarm architecture)

This file is the SOLE input the per-wave planner agents will read to construct full-fidelity gate blocks for S86. It is mechanically extracted from the S85 closeout's §3 (Plan-Writing Input Checklist), §6 (Wave-by-Wave Proposal), §7 (Level-Ordered Carry-Forward Index) — all three of which already discharged the cross-synthesis deduplication at S85 close. Per-wave planners do NOT need to read the closeout itself or any per-reviewer synthesis; this file is self-sufficient.

---

## §0. Source Manifest

The S85 closeout consolidated the following sources into the §3 / §6 / §7 tables reproduced below. Per-wave planners should NOT re-read these — the closeout already deduplicated their carry-forward sections.

| File | Lines | Origin (agent or workshop) | Carry-forward type |
|:-----|:-----:|:---------------------------|:--------------------|
| `sessions/archive/session-85/session-85-full-s85-closeout.md` | 1005 | gen-physicist (closeout) | UNIFIED — primary source |
| `sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md` | 555 | gen-physicist 9A | W6-W13 §4 + §7 |
| `sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md` | 841 | lizzi 9A | W6-W13 §6/§7/§8 (A/B/C/D/E/F items) |
| `sessions/archive/session-85/session-85-mack-synthesis-w6-13.md` | 493 | mack 9A | W6-W13 §III/§IV/§VI |
| `sessions/archive/session-85/session-85-s7-combined-landscape-gen-physicist.md` | n/a | gen-physicist S-7 | W0-W5 §V (V.1-V.24) |
| `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md` | n/a | lizzi S-7 | W0-W5 §V (CF-LZ-S86-1..14) |
| `sessions/archive/session-85/session-85-s7-combined-landscape-mack.md` | n/a | mack S-7 | W0-W5 §V (V.1-V.11) |
| Slot-1 solos (1A 3-solo, 1B 3-solo, 1C, 1D 3-solo, 3A 2-solo, 3B 3-solo, S-1 3-solo, S-2 2-solo, S-3 3-solo, S-4 2-solo, S-5 2-solo, S-6 2-solo) | per file | per agent | input-only to syntheses |
| Workshops 5/5 | per file | W-2 / W-3 / W-4 / 5A / 6A | rule-file diffs + adjudications |

### S85 verdict ledger (input pin for re-emission gates)
- `computations/s85_gate_verdicts.txt` — 52,187 B / 206 lines / 149 S85 verdicts (PASS=79, FAIL=46, INFO=18, plus 6 PENDING-EVENT/PRE-REG-INC residuals)

### Files-on-disk verified at S85 close (§7.5)
- `sessions/permanent-results-registry.md` — EXISTS (216,477 B at 2026-04-24); target for §3.1 T-series + §3.6 C8/C19/C23 landings
- `computations/canonical_constants.py` — EXISTS (86,443 B at 2026-04-24); target for §3.2 P12 + §3.6 C17/C18 updates
- `sessions/evoi-framework.md` — EXISTS (59,266 B at 2026-04-19); target for §3.2 P13 EVOI-table refresh (FROZEN since S66 per `feedback_framework-hygiene.md`)
- `sessions/framework/registry/falsifier-master-inventory.md` — TARGET, to be created/extended in late-S86 P11
- `sessions/framework/correspondence/cross-channel-correlation-matrix.md` — EXISTS (8133 B); from S85 W4-2 PASS
- `sessions/framework/registry/falsifier-watchlist.md` — EXISTS (8697 B); from S85 W4-8 REFRAMED PASS
- All 16 W0-W13 working papers (`session-85-w{0,1a,1b,1c,2,3,4,5,6,7,8,9,10,11,12,13}-workingpaper.md`) — ALL EXIST

### Validation-tool inventory (Phase 3e + on-call)
- `computations/_plan_upstream_pin_validator.py` — upstream-reference pin validator (mandatory per wave)
- `computations/_yaml_gate_validator.py` — PRDR machinery checklist + R3 schema validator
- `computations/_recovery_controller.py` — V3 closure recovery (Stage 1/2/3 + PROHIBITED_ACTIONS)

---

## §1. Constraint-Map Snapshot (S85-close anchors per-wave planners cite verbatim)

The S85 campaign produced 149 verdict lines. The constraint map decomposes into five substrate-typed registers (closeout §1 verbatim).

### §1.1 Permanent-registry-grade theorems landed S85 (35 entries — 17 W0-W5 + 18 W6-W13)

W0-W5 portion (17 PASSes — landing target T1):
W0-3 / W1a-3 (CC-5 cluster-span identity 2.000…002), W0-12 (CC-4 Dai-Freed Z/2 torsion), W0-16 (HP^1 dim-CM2008 (3,3) shift=0), W0-23 (CC-1 η=0 INFO), W2-2 (cross-session theorem family — mother-theorem + 3 corollaries + 2 predicted instantiations), W2-3 (HP^3 disjoint corridor num_nontrivial=0), W2-4 (KO-6 Higgs sign +1→−1 RG), W2-5 (KO-6 η-band 3/3 machine zero), W2-6 (quantum disjoint corridor 4-route), W2-10 (3-solo SHA reproduction `cf3b7443…`), W2-11 (triality-Jensen commutation 0.00e+00), W2-12 (BdG band CMB l_crit=1424.50, T_LB=0.113), W3-1 (CF-5 PIXIE μ K_FIRAS γ=1 lockout spread=0), W3-4 (K-regulator functorial closure-defect 2.5e−16), W3-5 (two-speed transfer c_S=f_B machine ε), W3-9 (Ginzburg-Oz validity Gi=5.50e-10), W5-7 (two-layer obstruction n_joint=0/5).

W6-W13 portion (18 PASSes — landing targets T2/T3/T8/C8/C41):
W6-1 (AWH formal κ=0.01686), W6-3 (conformal-infinity bifurcation 2 topologies), W6-5 (Mellin-cone apex universal s=3 deviation 0), W7-DRESSED-VP, W7-K-CORRIDOR-MUKHANOV, W8-2 (ConvA BdG micro 2.97e-16), W8-7 (K_R5 L_max stability deviation 0), W9-1 (`§VII.P Borel-Floor` `min S_inst/Borel=5.58e+4` 4.7465 OOM safety), W9-2 (`§VII.Q F_amp^3PI Factorization-Invariance` machine-ε identity 2.22e-16), W9-4 (Mellin-balance 16/16 closures L_max=10), W10-3 (`τ_fold=0.190 van-Hove uniqueness theorem`), W11-2 (S5 convergence audit 3-agent 0 disagreements), W11-3 (`NCG-Structural-Exclusion META-THEOREM` parity+rank+w_0 NEW-FAMILY), W11-4 (fiber-group parity preserve=8 flip=4), W11-5 (base Pontryagin parity preserve max|δ|=0), W12-3 (W12-ELIM-1 branch-(iv) inverted-Josephson L-robust D_iv ∈ {−0.989, −0.992, −0.994}), W12-4 (W12-ELIM-8 regulator-invariance taxonomy 4-class PROVEN COMPLETE: 13 INVARIANT + 0 (b)/(c) + 3 STRUCTURALLY-DIVERGENT), W13-3 (C² fiber decoupling max_delta_off=0).

### §1.2 Observational pre-registrations — 20 unified flagship pins (14 W0-W5 + 6 W6-W13)

W0-W5: W0-1 β_s=−0.1331 (CMB-S4 60.5σ), W0-8 μ=8.6949e-5 (PIXIE 8693σ), W1a-4 r_FW=0.011732 (BK-Array 2026 PENDING-EVENT), W1a-5 w_0=−0.918 w_a=0 (DESI DR3 PENDING; window opened 2026-04-23), W1a-7 LISA SNR=1.68e13, W1a-8 separation_normalized=588.78 LiteBIRD STRUCTURAL-FLOOR, W1a-9 7D Fisher log10(BF)=+827.9, W1b-2 σ_corr/σ_diag=1.1298 (13.0% widening), W1b-5 β_s joint S4×HD 41.9% tighten, W3-1 PIXIE spread=0, W4-4 falsifier-watchlist 5/5 EVOI-classified, W4-6 Fisher-discount 0.9926, W4-7 null-elim 2/5 detectable |Δ|>3σ, W4-8 unified-schema watchlist 6/6 compliant.

W6-W13: W8-4 9 lab observables (3He-A + FeSe + 173Yb; δω_K/ω_K=1.7267, K_anis/K_0=1.8226, 3-body Γ-ratio=2.8500), W9-3 SKA f_NL_folded Fisher-cosine 0.7685 (detector-sterile at SKA-1 σ=5.0→0.15σ), W9-5 M_W cross-check (cos²θ_W, M_W_pred, τ_eff_TS) = (0.99277, 80.3692 GeV, 745.68) within 0.01 of M_W_obs=80.379, W10-1 ANTI-CORRESPONDENCE #30 (rank 3 vs 1, K_0 torsion-free vs Z/2, Witten integral 16.0 vs 1.0, Bott-period residue ≠ 1), W11-1 ε_H Jensen survival min ratio 10.157431, W13-2 (α_s=−0.068968 [22.99σ vs LCDM], Ω_GW(LISA)=8.299e-58 [45 OOM null], ρ_CGWB,α_s=0, Fisher PD=1; INFO band-width-diagnostic > 20%).

### §1.3 Surviving open channels (10 — primary S86 target)

W0-W5 portion (5): W1c-5 §VII.Ω.α_s-gap (PASS but registered as STRUCTURAL OPEN CHANNEL: 9.6221σ separation, 15.3262× ratio); W5-5 non-functorial L1-AX/L2-SA → L3-OB (FAIL, 8 violations 4 mismatched pairs); W2-7 §VII.P parity-blindness FAIL-with-refinement → S86 §VII.P-v2 (HP^0-content-distinct corridors); W3-7 A_s 57% Planck-overshoot (FAIL <30%, PASS-F2 <factor-2) — adjudicated by W-2 into 4-level taxonomy + Both-Pathways FROZEN-PREDICTION-DISCIPLINE-COMMIT; W0-7 Jensen-Zubarev ρ=−1 refuted (FAIL, c_0=−0.8104).

W6-W13 portion (5): 1A joint CC residue (3-solo, value not yet pinned); 1D §VII.P meta-theorem (3-solo: w_0 CS-asymmetry awaits NEW-FAMILY meta-theorem in S86+); 3A ζ-stabilization REPLACED by REPLACEMENT-A (windowed kinematic, PROVEN at L ∈ {5,6,7,8}) + REPLACEMENT-B (asymptotic at s=4 leading residue, conditional on S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE); 3B branch-c phonon mechanism-discriminating gate; 6A CGWB ⊥ α_s three-layer adjudication (parameter / experimental-Fisher / substrate-marginalized) of W13-2 ρ=0 (LAYER-3 Pearson |ρ|≈0.91 over W12-4 5-regulator atlas).

### §1.4 Closed FAILs — 39 corridors closed (28 W0-W5 + 11 W6-W13)

All 39 are constraint-map gains (per `feedback_reporting-framing.md`); each is a corridor termination with an exclusion bulletin. W0-W5 partition: Truncation=6, Methodology=5, Observability=5, Infrastructure=8, PRE-REG-INC=4. W6-W13: W6-7 Petrov non-bd FAIL, W7 H̃ branch-B retraction + CC-6 Parker-Hawking + CC-Γ + cusp Bogoliubov, W8-1 Kfiras hidden closed-form, W8-5 BDI-TCI restricted corridor, W10-5 Witten 1998 K-theoretic alternative parents=0 → uniqueness, W12-1 falsifier-partition keyword 0.089 coverage, W12-2 14 false-positive bare-K CONTRADICTS, W13-4 R1 rank-distinguishability 1.6% asymmetric.

### §1.5 Regulator-class structural floor (closeout §1(c))

W0-W5 lizzi S-1 Regulator-Family Boundary Theorem + W6-W13 W11-3 NCG-STRUCTURAL-EXCLUSION META-THEOREM together establish a 3-axis structural floor: parity-exclusion (W10-114), rank-exclusion (S82 W2-3), Mellin-support-exclusion (S-1 lift) as three independent sub-cases of one categorical statement. Per lizzi 9A §6.4 slot-allocation: 1D NCG-Meta-Theorem → §VII.R; 1C Perturbative-Ledger Immunization Family → §VII.S (chronological-priority resolution within S85). Per lizzi S-7 §II.4: parallel **Mellin Strip / Convergence Cone Theorem** (S85-W0-S6) lands as Lizzi-track sibling alongside ZETA-NOT-PHYSICAL-75. The 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} splits into pure-a_4 family **F_4 = {ζ, Zubarev, SDW}** + mixed-support family **M = {cutoff_sqrt, anomaly}**; W12-4 empirical 5-regulator atlas (a_0/a_2/a_4 spread 0.50/1.03/0.49) is the empirical confirmation of S-1's predicted F_4/M partition.

### §1.6 P_work_complete trendline (no master-gate tally per `feedback_no-master-gate-tally.md`)

S66 baseline 0.206 → S80 close 0.216 → post-S85 bracket **0.31-0.36** (W6-W13 contribution alone 0.30-0.33; W0-W5 ≥+0.005 incremental). Direction monotone-upward across S66 → S80 → S85. Magnitude requires S86 EVOI re-derivation per P13 (carried as the FINAL late-S86 item).

---

## §2. Deduplicated Carry-Forward — 92 unique S86 inputs (verbatim from §3)

This is the canonical S86 plan-writer input. Each entry has all 4 mandatory fields (what / inputs implicit in source / gate / effort) + source citation + sequencing prerequisite. **§3.7 substitution chain (Python-verified by enumeration)**: 10 + 14 + ~5 bulletins + 7 + 10 + 46 = 92 unique items (raw 88 + ~4 cross-pairing additions). Wave-equivalent budget ≈ 35-45 → S86 + S87 + possibly S88.

### §2.1 Theorem landings (T1-T10 — 10 items, registry-write effort 0.1-0.5 wave each)

| # | Gate ID | What | Source | Effort |
|:--|:--------|:-----|:-------|:-------|
| T1 | `S86-W0-PERM-LAND-17` | Land 17 W0-W5 theorem-grade PASSes (W0-3, W0-12, W0-16, W0-23, W2-2, W2-3, W2-4, W2-5, W2-6, W2-10, W2-11, W2-12, W3-1, W3-4, W3-5, W3-9, W5-7) into permanent-results-registry with full 64-char dual-SHA provenance | gen-physicist S-7 §V.1 | 2h mechanical |
| T2 | `S86-VII-R-NCG-META-THEOREM-LANDING` | Land 3-signed NCG-Structural-Exclusion Meta-Theorem at §VII.R; 7 status rows + 3-axis disjointness table + cross-pair note to §VII.S; absorbs W10-114 parity-exclusion + S82 W2-3 rank-exclusion + S-1 lift | lizzi 9A §6.8 (B-1) | LIGHT |
| T3 | `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING` | Land 1C 6-Φ-branch §VII.S cascade with IEP class tags per §3.1 (IEP = Intensive/Extensive Partition); routed from §VII.R per chronological-collision resolution | lizzi 9A §6.8 (B-2) + gen-physicist 9A §4.3 | LIGHT |
| T4 | `S86-VII-R-IEP-ANNOTATION` | Annotate each §VII.S branch (A-F) with INTENSIVE/EXTENSIVE class tag at registry write per IEP §3.1 | lizzi 9A §6.8 (B-3) + 1C OQ11 | LIGHT |
| T5 | `S86-MELLIN-STRIP-REGISTRY-LANDING` | Land Mellin Strip / Convergence Cone Theorem (S85-W0-S6) in permanent-results-registry as Lizzi-track theorem alongside ZETA-NOT-PHYSICAL-75; cite Steps 1-4 substitution chain verbatim | lizzi S-7 §V.6 (CF-LZ-S86-6) | 1h LOW |
| T6 | `S86-HP1-NEAR-INVARIANCE-LANDING` | Land W5-6 finding ‖[ε_H]‖_{HP^1} R-protected-LOOSE on full 5-atlas (factor 2.0) and STRICT on F_4 (factor 1.031) into §VII-B as permanent registry entry | lizzi S-7 §V.7 (CF-LZ-S86-7) | 1.5h LOW |
| T7 | `S86-TWO-LAYER-OBSTRUCTION-LANDING` | Land W5-7 PASS as new §VII-B permanent wall entry "Two-Layer Obstruction Theorem"; obstruction stronger than predicted (every conjunct fails individually for every regulator) | lizzi S-7 §V.8 (CF-LZ-S86-8) | 1h LOW |
| T8 | `S86-3HE-B-INVERSION-CANONICAL-LANDING` | Land 3He-B inversion correspondence as canonical (parent → child, NOT analogy) per 1B 3-solo agreement (volovik/landau/connes); update sessions/framework/correspondence/3HeB-inheritance-canonical.md | gen-physicist 9A §4.2 | 0.5 wave |
| T9 | `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` | Land ζ-stabilization REPLACEMENT-A (windowed kinematic inequality, PROVEN at L ∈ {5,6,7,8}) + REPLACEMENT-B spec (asymptotic, conditional on T1-A1 Mellin-cone infra) per lizzi 9A §5 + spectral-geometer 3A | lizzi 9A §A-2 + gen-physicist 9A §4.7 | MODERATE 4-6h, depends on C9+C10 |
| T10 | `S86-FI-RD-PERMANENT-REGISTRY` | Land 18-row FI/RD classification (lizzi S-7 §II.1) into permanent-results-registry §VII.K-META as canonical S85 W0-W5 atlas; compose with S82 42-row M_lizzi atlas (60-row total) with M_connes conflict-check | lizzi S-7 §V.5 (CF-LZ-S86-5) | 3-4h MODERATE |

### §2.2 Pin commits (P1-P14 — 14 items, 0.5-1.5 waves each)

| # | Gate ID | Pin / commit content | Source | Effort |
|:--|:--------|:----------------------|:-------|:-------|
| P1 | `S86-FROZEN-COMMIT-LANDING` | Land FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 4-level unit-class taxonomy + Both-Pathways r registration in `sessions/framework/registry/baseline-findings-s66.md` (or successor) | mack S-7 §V.2 + W-2 workshop | 1h |
| P2 | `S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING` | Promote r to falsifier-master-inventory under BOTH-Pathways: Path-H r=0.00745 + Path-C r=0.0117 with 36.5% split > 12.5% scheme-floor flag; SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030 | mack S-7 §V.1 | 1.5h |
| P3 | `S86-SECTOR-1-SR-FLOW-Z-FACTOR` | Integrate (ε, η, α_s, ξ²) ODE from N=0 fold IC to N_pivot under substrate-first ξ²(0) IC — 2A SECTOR-1 sector-of-split. **HARD DEPENDENCY: P4 ξ_E_GGE^{−1} pin must land first** | gen-physicist 9A §4.5a + mack 9A §VI.3 | 1.5 waves (DOMINANT single-gate load) |
| P4 | `S86-BRANCH-IV-FORMULATION-COMMIT` | Retire R_JE; land both R_JK (K-functional, distance-2 tag) AND ξ_E_GGE^{−1} (s=−1 spectral diagnostic, distance-1 tag) per 2B path-(c) commit | gen-physicist 9A §4.6 + lizzi 9A §2.2 | 1 wave |
| P5 | `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT` | Substrate Mellin-kernel pole structure at pivot independent of SR flow; pin K-invariant as substrate-distance-1 quantity | gen-physicist 9A §4.5b | 1 wave |
| P6 | `S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT` | 3-arm × 3-layer (9-cell) diagrammatic commit on W13-2 ρ=0 verdict with 6 pre-registered pin axes (parameter / experimental-Fisher / substrate-marginalized-observable layers) | gen-physicist 9A §4.10a + mack 9A §IV.3 | 0.5 wave |
| P7 | `S86-RHO-SUBSTRATE-PREDICTION-MC` | Pre-register & compute LAYER-3 ρ_substrate-prediction Monte Carlo over W12-4 5-regulator atlas; sign-convention pre-pinned (signed vs magnitude); atlas-weighting pre-pinned (uniform / PV-down-weighted / PV-excluded). Reference: \|β\|² ≈ 0.91 R3 spot-check Pearson | mack 9A §VI.2 | 4-6h |
| P8 | `S86-DR3-SUB-TREE-3-ROW-PIN` | Extend W1b-1 DR3 sub-tree from 2-row (L=10/L=12) to 3-row (L=8 W7-7 / L=10 / L=12); pre-register regulator-first DR3 adjudication protocol | mack 9A §VI.6 | 2h |
| P9 | `S86-W0-PRIMARY-VALUE-RESOLVE` | Resolve w_0_FW value discrepancy: S5 row #1 −0.918 (Volovik partition) vs W10-2 branch-(iv) −0.842454 (substrate-compaction); pre-register decision rule for which is PRIMARY framework w_0 prediction | mack 9A §VI.7 | 2h adjudication |
| P10 | `S86-FNL-FOLDED-PATHWAY-REGISTRY` | Consolidate 3 framework f_NL_folded pathway predictions (S82 GGE-equilateral 0.0547 / S67 GGE-folded 0.129 / W9-3 analytic-template-folded 0.7685) at sessions/framework/registry/f-nl-folded-pathway-registry.md | mack 9A §VI.8 | 1.5h |
| P11 | `S86-MASTER-INVENTORY-W6-W13-LAND` | Apply 6 PAIR-enrichments + 1 NEW row class (lab-falsifier suite) to falsifier-master-inventory per mack 9A §III.3 | mack 9A §VI.4 | 1.5h |
| P12 | `S86-ALPHA-S-CANONICAL-UPDATE` | Update canonical_constants.py from `alpha_s_canon = −0.0045 ± 0.0067` (Planck 2018) to `alpha_s_canon_2020 = +0.0023 ± 0.0063` (ACT DR4 + Planck, Aiola 2020) per W1b-8 FAIL; re-run W1a-9 + W1b-3 under updated pin | mack S-7 §V.11 | 1.5h |
| P13 | `S86-EVOI-TABLE-REFRESH` | Update sessions/evoi-framework.md EVOI table with W6-W13 + W0-W5 link-list deltas; recompute P_work_complete from canonical link inventory (frozen since S66 per `feedback_framework-hygiene.md`). **MUST BE LAST — captures post-S86 work-fraction state** | gen-physicist 9A §7 #14 | 0.5 wave |
| P14 | `S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE` | Promote W12-4's CANON-REGULATOR-PIN-DISCIPLINE to permanent epistemic rule: every bare `a_n` citation in any computation script or WP section MUST include explicit regulator-pin tag (`a_0^{ζ}`, `a_2^{Pauli-Villars}`) | lizzi 9A §C-2 + W12-4 carry | LIGHT + MODERATE retrofit |

### §2.3 Structural-elimination bulletins (registry-only landings, NOT new gates)

- **S-4 four structural-elimination bulletins** (gen-physicist + kaku S-4 pair, W0-W5 §II.D.7 input). 4 mechanism-classes definitively closed in S85 W0-W5 with substrate-first reasoning + cross-references to FAIL gates. Land at `sessions/framework/registry/elimination-bulletins.md`.
- **4A elimination-bulletins (W6-W13 portion)** — registry-class additions; W6-W13 11 FAILs aggregated into 4 categorized bulletins (cusp-Bogoliubov / Parker-Hawking convention boundary [W7 cluster]; restricted-corridor BDI [W8-5]; uniqueness-confirming Witten alternative [W10-5]; PRDR-K-disambiguation [W12-2]).
- **28-FAIL W0-W5 partition** (Truncation=6, Methodology=5, Observability=5, Infrastructure=8, PRE-REG-INC=4) per gen-physicist S-7 §II.A.D — each carries a S86 carry-forward as already mapped to V.2-V.16 of gen-physicist S-7 §V.

### §2.4 Observational watchlist additions (W1-W7 — 7 items)

| # | Watchlist update | Source | Action |
|:--|:------------------|:-------|:-------|
| W1 | Row #1 (w_0): add 3-row regulator-layer sub-pin table (L=8 W7-7 → L=10 canonical → L=12 split) + W10-2 audit-pin SHA reference | mack 9A §III.3 #1 | inventory edit |
| W2 | Row #3 (α_s §VII.Ω): add W13-2 joint-Fisher pin at SHA `f514d642fe2a80ac…` (no value change; strengthening citation only) | mack 9A §III.3 #2 | inventory edit |
| W3 | Row #7 (CGWB ρ_AC): add Companion-null-(C-regulator) column with W13-2.Ω value 8.299e-58; document (A)/(C) discriminator structure | mack 9A §III.3 #3 | inventory edit |
| W4 | Row #9 (f_NL_folded): expand to 3-pathway table (S82 W3-4 GGE-equilateral 0.0547 / S67 GGE-folded 0.129 / W9-3 analytic-template-folded 0.7685); each with own scheme + convention + L_max + SHA | mack 9A §III.3 #4 | 3-pathway expansion |
| W5 | Row #12 (A_s): add ε-sensitivity sub-note (range 3.11e-9 → 4.27e-9 over ε ∈ {0.02163, 0.020}); note ε_pivot is S86 SECTOR-1 carry-forward | mack 9A §III.3 #5 | inventory edit |
| W6 | NEW row class **#13–#21** lab-falsifier suite (9 atomic predictions: 3 sweet-spot + 6 cross-platform); EVOI tag = LAB-FALSIFIER, P_decisive = 0.30-0.50 (5-yr terrestrial-lab horizon); each row carries δE_a / observable-magnitude / platform / SI-translation-pending status | mack 9A §III.3 #6 + W8-4 + 1B volovik | NEW row class |
| W7 | REGISTRY-EXTENSION (W10-1 ANTI-CORRESPONDENCE #30): 4-obstruction vector (rank=3 vs Witten=1; K_0 torsion-free vs Z/2; Witten integral=16.0 vs 1.0; Bott-period residue ≠ 1) at parallel `sessions/framework/correspondence/correspondence-table-registry.md` | mack 9A §II.4 + W10-1 patches | NEW registry |

### §2.5 Rule-file diffs (R1-R10 — 10 items, FULL S85 v3 = W-3 v2 + 5A v2 union)

Per lizzi 9A §7.5 (W-3 v2 + 5A v2 → v3 union substitution chain): the FULL S85 Rule-File v3 is the ADDITIVE union of W0-W5 W-3's 11 plan-layer methodology debt clauses + W6-W13 5A's 3 sub-diffs (A/B/C) addressing 7 NEW debt classes, with 2 PARENT/CHILD cross-reference annotations.

```
S85 Rule-File v3 = W-3 v2 (11 clauses across epistemic-discipline.md / math-scripts.md /
                            pru-pre-registration-template.md / rclab-plan skill)
                 + 5A v2 (3 sub-diffs):
                   A. SOURCE-RECONCILIATION sub-audit (PRU Class 8.1, NEW) →
                      .claude/rules/epistemic-discipline.md
                   B. Machinery-feasibility audit (GPU-pin envelope + root-count S1 flag) →
                      .claude/rules/math-scripts.md
                   C. PRDR keyword-window granularity (8-K-atom enumeration) +
                      sig_2 scope-correction + 5B-class scan-as-robustness INFO-mode →
                      .claude/templates/pru-pre-registration-template.md
                 + 2 PARENT/CHILD cross-references:
                   W-3 §G2 (g) keyword-context-audit ↔ 5A G4a PRDR bare-K window
                   W-3 §G2 (c) GPU-pin selectivity ↔ 5A G3 GPU-pin feasibility envelope
```

| # | Gate ID | What | Source | Effort |
|:--|:--------|:-----|:-------|:-------|
| R1 | `S86-RULE-FILE-V3-LANDING` | Land FULL S85 Rule-File v3 = W-3 v2 (11 clauses) + 5A v2 (3 sub-diffs / 7 classes) per §7.5 with 2 PARENT/CHILD cross-references; v3 changelog header documents W-3 + 5A consolidation | lizzi 9A §7 + 5A workshop | MODERATE 3-4h |
| R2 | `S86-PRU-EXTENSION-RULE-V2-LANDING` | Implement `_source_reconciliation_audit.py` per Rule-File v2 (Diff 1+2+3); 5-class taxonomy canonical in `pru-pre-registration-template.md`; 13-site retrospective fixture matches D_max=5.6726 within 1e-10 | gen-physicist 9A §4.9 + 5A workshop | 0.5 wave |
| R3 | `S86-CUTOFF-AXIS-YAML-PIN` | Add `cutoff_axis: spectral \| coherence \| both` YAML field to all S86+ gate blocks invoking a cutoff (W3-9 vs W3-11 PRU defect closure at planner-template level) | gen-physicist S-7 §V.9 | 30 min |
| R4 | `S86-CANONICAL-PHRASING-AUDIT` (c_fabric) | Drop "Λ_eff = c_fabric · M_KK" from W3 §401/§543; update canonical_constants.py c_fabric docstring to "substrate sound speed (velocity scale, NOT a momentum cutoff)"; S86 plan-level constraint that c_fabric · M_KK is never labeled "Λ" without explicit Layer-B qualification | gen-physicist S-7 §V.10 | 30 min (parallel R3) |
| R5 | `S86-CANON-PRDR-K-DISAMBIGUATION` | Split bare "K" observable in `_pru_*` classifier vocabulary into K_base / K_corridor / K_R5 / K_crit / K_substrate / K_R3 / K_FIRAS / K_pivot (8 explicit sub-keys); post-disambiguation rerun returns 0 false-positive CONTRADICTS on K-family pairs (was 14, target 0) | gen-physicist 9A §13 + W12-2 + lizzi 9A §7.4 sub-diff C | 0.3 wave |
| R6 | `S86-PLAN-GEN-DISCIPLINE-UPDATE` | Update `/rclab-plan` skill + plan-authoring templates so that plans read latest-observed verdict state rather than hardcode `expected_verdicts` lists; use canonical file paths | gen-physicist S-7 §V.24 | 1-2h |
| R7 | `S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY` | Add single-name-conflation methodology entry to permanent-results-registry per closeout §5 (4 witnesses: 2A SECTOR-split, 2B R_JK vs R_JE, 6A ρ three-layer, W12-2 bare K) | gen-physicist 9A §11 | 0.2 wave |
| R8 | `S86-PRR-THREE-LAYER-ADJUDICATION` | Methodology entry to permanent-results-registry on three-layer adjudication for joint-channel ρ verdicts; keyword "three-layer adjudication for joint-channel ρ verdicts"; generalizes to ANY future joint-channel gate quoting ρ between two observables sharing a substrate parameter | gen-physicist 9A §4.10b + mack 9A §IV | 0.1 wave |
| R9 | `S86-W7-SIG2-DUAL-SHA-REGEN` | Regenerate 7 W7 single-SHA verdict lines under W9a-99 dual-SHA template (sig_2 PASS); parallel `S86-S85-VERDICT-FILE-COMPANION-ROW-CANONICALIZATION` (lizzi 9A §C-1) for 17 W6-W13 schema-1.5 entries | gen-physicist 9A §12 + lizzi 9A §C-1 | 0.3-0.5 wave (combined orchestrator action) |
| R10 | `S86-DUAL-SHA-INFRASTRUCTURE` | Land per-session sig_5 audit script `computations/_dual_sha_uniqueness_audit.py` invoked from `v3-closure-audit.sh`; allowlist by-design re-emission patterns (REFRAME / logspace fix / regex fix) | lizzi S-7 §V.4 (CF-LZ-S86-4) | 2-3h |

### §2.6 Computational gates (C1-C46 — 46 items, 1-12 hours each)

#### From W6-W13 sources (C1-C8)

| # | Gate ID | What | Source | Effort |
|:--|:--------|:-----|:-------|:-------|
| C1 | `S86-JOINT-CC-RESIDUE-COMPUTE` | Joint CC residue across phonon-first/transit/landau sectors (1A 3-solo) | gen-physicist 9A §4.1 (1A) | 1 wave |
| C2 | `S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING` (umbrella for 13 sub-gates: C-α/β/γ/δ/ε/ζ/η/θ/ι + C-κ NEW class) | Land §VII.S parent + 9 corollaries (2 registry-write C-η, C-θ; 7 candidate-gates) | gen-physicist 9A §4.3 + 1C workshop | 2 waves (S86 + S87) |
| C3 | `S86-NCG-STRUCTURAL-EXCLUSION-META-THEOREM-LANDING` (sister to T2) | Land NCG-STRUCTURAL-EXCLUSION META-THEOREM in registry; reserve NEW-FAMILY slot for w_0 CS-asymmetry; absorb W10-114 + S82 W2-3 with cross-ref to 1D 3-solo | gen-physicist 9A §4.4 + lizzi 9A §6 | 0.5 wave |
| C4 | `S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE` | Compute branch-c phonon mechanism-specific discriminator (10× ABSOLUTE ratio) per 3B 3-solo (volovik/landau/kaku) | gen-physicist 9A §4.8 (3B) | 1 wave |
| C5 | `S86-LAB-SI-TRANSLATION` | Translate 9 lab observables (3 sweet-spot + 6 cross-platform) from M_KK-normalized ratios to laboratory units (3He-A MHz; FeSe ppm; 173Yb s⁻¹) via compactification-scale mapping; per-platform σ_detect literature anchors | mack 9A §VI.5 + W8-4 carry | 3-4h |
| C6 | `S86-LAB-FALSIFIER-EVOI-TREE` | Assign EVOI level (LAB-FALSIFIER) + pre-register 5-yr decision tree for each of 9 lab observables | mack 9A §VI.9 | 2-3h (post-C5) |
| C7 | `S86-CGWB-LMAX-DIRECT` | Sharper L_max-sensitivity proxy for Ω_GW(f_LISA): direct L=8 vs L=10 spectrum comparison at f_LISA = 3 mHz; replaces W13-2 §(f) band-width proxy that measured spectral slope | mack 9A §VI.1 | 1-2h |
| C8 | `S86-W6-W13-R-CLASS-LAND` | Catalogue 7 R-class results (W6-1 AWH-formal κ=0.017; W6-3 conformal-infinity bifurcation; W6-7 Petrov non-bd FAIL; W12-1 inverted-Josephson signs; W12-8 a_n class-(d); W11-1 Jensen-survival meta; W11-3 NCG meta-exclusion) at registry §VII.Q parallel to W10-1 patch | mack 9A §VI.10 | 1.5h |

#### From W0-W5 sources (C9-C46)

| # | Gate ID | What | Source | Effort |
|:--|:--------|:-----|:-------|:-------|
| C9 | `S86-MELLIN-HEAT-KERNEL-INFRA` (master) | Build Mellin-Barnes residue extractor with explicit Seeley-DeWitt counter-term subtraction; resolves W0-7 + W0-11 + W0-20 simultaneously; PASS iff \|Λ_CC^MB\|/\|a_0\| ≤ 1e-1 AND χ²/dof ≤ 5; INFO band; FAIL otherwise. **PREREQUISITE FOR T9 (REPLACEMENT-B) and lizzi A-series** | lizzi S-7 §V.1 (CF-LZ-S86-1) + gen-physicist S-7 §V.2 | 6-8h HEAVY (1 agent session) |
| C10 | `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (lizzi A-1, sister to C9) | Build analytic-continuation `ζ_D(s) Γ(s/2) = ∫ t^{s/2−1} K(t) dt` evaluated off-pole at s=3 in d_spec=8 NCG; expose `analytic_zeta(s, L_max)` API; PASS iff `analytic_zeta(s=3, L_max=10)` finite AND χ²/dof ≤ 5 against direct subtraction; INFO band; FAIL otherwise | lizzi 9A §A-1 + 3A REPLACEMENT-B prerequisite | 4-6h HEAVY (new infrastructure module) |
| C11 | `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` | Compute analytic Mellin transform `M[exp(-x/Λ_Z²)](s)`; embed Zubarev as INFINITE-VECTOR class extending S-1's finite-vector F_4 formalism; formalize ζ-class (finite-vector e_4) vs Zubarev-class (infinite-vector M[Schwartz]) asymmetry | lizzi 9A §A-3 + lizzi 3A §V.4 | MODERATE 3-4h |
| C12 | `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` | Refactor W0-3 ad-hoc cluster-span code into reusable `_cluster_span_extract.py` module; self-test reproduces W0-3 PASS at L_max ∈ {8, 10, 12} | gen-physicist S-7 §V.3 | 1h |
| C13 | `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` | Test `b_pow(span_2) = 2·b_pow(span_3)` at machine precision across K ∈ [K_R5, K_crit] under L_max=10 + sheet-by-sheet on post-fold Riemann cover K ∈ [K_crit, K_FIRAS] | gen-physicist S-7 §V.4 | 2h (after C12) |
| C14 | `S86-LAMBDA-TOP-DIRECT-EXTRACTION` | Direct extraction of λ_max(L=10) from D_K spectral cache; pin Λ_top to 6 sig figs; 6 PASS sub-criteria | gen-physicist S-7 §V.5 | 1h |
| C15 | `S86-W0-A-i / W0-A-ii GAUGE + BASELINE FORWARD INTEGRATION` | (i) Select between 3.12 e-folds (substrate-native zeta) and 55 e-folds (gauge-invariant Mukhanov-Sasaki) as canonical N-fold counter; (ii) forward-integrate dH/dN = −eps_H · H from substrate IC at N_initial = N_pivot + 55 e-folds | gen-physicist S-7 §V.7 | 6-8h, 2 sub-waves |
| C16 | `S86-W0-0-PRDR-PIN-CSUB` | Classify c_sub = 3.647 as ADMISSIBLE or EXCLUDED via PRDR-compliant gate (UV cut + Mellin convention + L_max producing 3.647; tau-stationarity test per S83 W2-G12 max_slope < 0.1; conformal-anomaly consistency with S79 P1-2 W2-E sign-reversal) | gen-physicist S-7 §V.8 | 4h |
| C17 | `S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION` | Promote `K_crit_BdG = 2.035` to canonical_constants.py distinct from `K_crit = 91.5` (inflationary corridor); document both with provenance; eliminates K_crit triple-collision PRU vulnerability | gen-physicist S-7 §V.11 | 30 min |
| C18 | `S86-CANONICAL-ENTRY-CONSOLIDATION` | Add 5 missing canonical entries to canonical_constants.py: `eps_H_HP1_norm = 16.197719`; `HP1_dim = 3`; `FI_parity_exclusion = 1`; `rank_exclusion = 3`; `nonflat_T_correction_L2` (extract from vdd §VI) | gen-physicist S-7 §V.12 | 1h |
| C19 | `S86-K-FLOOR-K-WALL-LAND` | Ensure sessions/permanent-results-registry.md exists; add K_floor + K_wall entries to canonical_constants.py with W5 D.4 derivation source; write W5-D.4 block to registry with dual-SHA provenance | gen-physicist S-7 §V.13 | 1h |
| C20 | `S86-W1d-ALPHA-S-REMEDIATION` (Level-3, defer-eligible) | Remediate 2193 AMBIGUOUS α_s usage sites identified by W1c-3 across 390 files; extend classifier keyword list (M_GUT/LCDM-baseline/no-running contexts; SKA/LiteBIRD/CMB-HD/CMB-S4 Fisher-forecast conventions; META-about-α_s audit-gate pattern) | gen-physicist S-7 §V.14 + lizzi S-7 §V.14 | 4-6h HIGH (mechanical voluminous) |
| C21 | `S86-R3-YAML-LIFT` | Iterate over all W0-W13 gate blocks in sessions/session-plan/session-85-plan-w*.md; insert `schema_version: R3` in each machinery pin block where absent; current 9.2% coverage; sig_4 PASS at ≥90% | gen-physicist S-7 §V.15 | 1h |
| C22 | `S86-MELLIN-COMPLIANCE-LIFT` | Apply 5-marker W6-71 boilerplate to 8 non-compliant Mellin-labeled scripts | gen-physicist S-7 §V.16 | 2h |
| C23 | `S86-VII-M2-T15-LANDING` | Land §VII.M.2 α_s pre-reg consolidation (W2-8 PASS draft) + T15 registry upgrade diff at next available §VII.X slot (W2-9 PASS draft) | gen-physicist S-7 §V.17 | 1h |
| C24 | `S86-VII-P-V2-PARITY-EXTENSION` | Land refined §VII.P-v2 restricted to HP^0-content-distinct corridors (drops (C_H, C_epsH)-type twin pairs); pair with auxiliary §VII.P' using odd-parity GV diagnostic from S84 §W10-115 | gen-physicist S-7 §V.18 + lizzi S-7 §V.11 | 4-5h MODERATE |
| C25 | `S86-EXTERNAL-CLOCK-SCAFFOLD` (S86-S96 plan template) | Register external-clock-aligned scaffold (S86 freeze, S87 extend, S88 BK-Array ingest, S89-S95 maintain, S96 LiteBIRD ingest); freeze-no-re-pin pattern; S88/S96 ingest gates pre-registered as observational-comparison gates | gen-physicist S-7 §V.19 | 1h |
| C26 | `S86-W2-2-PREDICTED-INSTANTIATIONS` (2 sub-gates) | §VII.P-prime (k=3, rank-2 HP³ on Spin(8)-extended SU(3)) + §VII.K-DUAL-q (4-bucket HP^even under q-deformation); each pre-registered in W2-2 | gen-physicist S-7 §V.20 | 6-8h total |
| C27 | `S86-W3-7-PASS-CLAUSE-RE-PIN` | Edit S85 W3-7 plan-block to set PASS = 12.5% (scheme floor), retaining FAIL = 30% (geometric midband); current 10% PASS sits below 12.5% floor and is structurally unattainable | gen-physicist S-7 §V.21 | 30 min |
| C28 | `S86-W-4-CUTOFF-SQRT-ADJUDICATION` (running into S86) | Complete connes × lizzi 3-round workshop on cutoff_sqrt status (STRUCTURALLY-EXCLUDED / GENUINELY-PHYSICAL / REQUIRES-S86-GATE); outcome decides whether atlas is 4-regulator or 5-regulator with two physical sub-families. Workshop file: `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` (3-round workshop EXISTS at S85 close) | gen-physicist S-7 §V.22 + lizzi S-7 §IV.3 (CF V.2 + V.3 pre-registered) | 4-6h |
| C29 | `S86-FALSIFIER-MASTER-INVENTORY-PROMOTION` | Promote r from "live-watch falsifier" to dual function (live-watch envelope [0.005, 0.015] AND internal-consistency Path-H 0.00745 vs Path-C 0.0117); compute n_s running prediction for Path-C via d(ln n_s)/d(ln c_sub) at c_sub = 3.647 | gen-physicist S-7 §V.23 | 2h |
| C30 | `S86-DETECTOR-READINESS-9-CELL` | Per-detector S86+ readiness checklist for 9 detectors (PIXIE, DESI DR3, CMB-S4, LISA, LiteBIRD, BK-Array, CMB-HD, SKA-1, lab-analogs ³He-B + K-STAR); 5 fields per detector | mack S-7 §V.3 | 4h |
| C31 | `S86-BK-ARRAY-CLASSIFIER-PRE-BUILD` | Pre-build 4-branch decision script `s86_bk_array_2026_classifier.py` triggered on BK-Array data publication; dry-run synthetic test r ∈ {0.003, 0.012, 0.025, 0.040} → branches {1, 2, 3, 4} | mack S-7 §V.4 | 4h |
| C32 | `S86-FISHER-PDF-PIN-CLOSURE` | Fetch + SHA-pin 5 Fisher-forecast PDFs (CMB-S4 Science Book v2 2022, DESI 2025 BAO forecast, LiteBIRD Hazumi 2022, CMB-HD Sehgal 2019, HERA Memo 54 Ali+ 2018); re-emit W4-3 + W4-6 verdicts under Fisher-PDF map | mack S-7 §V.5 | 2h |
| C33 | `S86-DR3-3-LAYER-SUB-TREE` | Generate 3 sub-trees keyed on L_max ∈ {8, 10, 12} for W1a-5 7-cell DR3 tree; 21-cell matrix replacing single 7-cell tree; PASS iff all 21 cells deterministic + monotone (no oscillation A→B→A) | mack S-7 §V.6 | 6h |
| C34 | `S86-H-TILDE-DIVERGENCE-PROMOTION` (Level-3, defer-eligible) | Promote S80 H-TILDE-DIVERGENCE-CHASE from conditional to permanent; PASS iff structurally-derived H̃ at N_pivot=55 lands within ±5% of one of {TD, LI, BASELINE} from forward substrate-dynamics integration NOT using S80 TD verdict-line as input | mack S-7 §V.7 | 12h |
| C35 | `S86-LAB-ANALOG-VERIFICATION-2OF5` (Level-3, defer-eligible) | Verify 2 ANALOG-CANDIDATE-UNVERIFIED rows in W4-5 (LiteBIRD n_T ↔ ³He-B tensor-mode spectroscopy; 21-cm folded bispectrum ↔ K-STAR 3-pt) | mack S-7 §V.8 | 4h |
| C36 | `S86-CMB-HD-ALPHA-S-FORECAST-PIN` | Monitor publication of explicit CMB-HD σ(α_s) forecast (Abazajian + companions; CMB-HD SciBook code release; CMB-S4/CMB-HD joint forecast); on publication SHA-pin + re-fire W1b-6 | mack S-7 §V.9 | 0.5h per quarterly poll |
| C37 | `S86-MU-BC-V2-ZETA-AT-INTERIOR` (W9-5 EW-sector ZFP discharge route 1) | Attempt ζ-at-interior derivation route for integer-12 exponent in `mu_BC = M_Z · sqrt(1 + exp(12·tau_fold)/3)`; never attempted previously per W9-5 status table. May depend on C9 Mellin-cone framework | lizzi 9A §D-1 | MODERATE-HEAVY 4-6h |
| C38 | `S86-MU-BC-V2-REP-THEORETIC` (W9-5 ZFP route 2, parallel) | Representation-theoretic derivation route for integer-12 exponent (12-dim triple structure of Connes-Chamseddine); methodologically independent of heat-kernel | lizzi 9A §D-2 | MODERATE 3-4h |
| C39 | `S86-MU-BC-V2-HEAT-KERNEL-DIAGNOSTIC` (W9-5 ZFP route 3, parallel) | Diagnose what 0.15267 (W9-5 heat-kernel V.2 return value, NOT "near 12") represents BEFORE re-running; may sample different Seeley-DeWitt coefficient than needed | lizzi 9A §D-3 | MODERATE 2-3h |
| C40 | `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE` (1C C-α / OQ1) | Test §VII.S.B's C-α corollary at slot-by-slot Mellin level; 3 Wilson + 1 Symanzik discretizations at L_max=5; per-slot drift exponents 0,1,2,3 confirmed at Symanzik O(a^4) PASS-band | lizzi 9A §E-1 + gen-physicist 9A §4.3 sub-gate | MODERATE |
| C41 | `S86-VII-S-C-ETA-LANDING + S86-VII-S-C-THETA-LANDING` (zero-compute) | De-facto landings of C-η Ward-Identity + C-θ Connes inner-fluctuation per 1C QN.6; one-line consequences of [J, D_K]=0 + CCM-2007 §3 inner-fluctuation invariance | lizzi 9A §E-2 + 1C QN.6 | LIGHT (registry-only) |
| C42 | `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM` (1C C-γ-WEAK / OQ2) | §VII.S.D weak-form gate: compute Λ_anomaly INTERNALLY from `Tr_F(Y†Y)` + AC-2010 §V coefficients; test parametric bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²` | lizzi 9A §E-3 | HEAVY |
| C43 | `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION` | Extract Λ_actual from L_max=10 D_K cache as empirical top eigenvalue (W0-7 series at L=12 gives `lambda_max = 5.42 M_KK`); re-run W3-11 with Λ_actual replacing Casimir-saturated and `c_fabric*M_KK` ad hoc choices; verify W3-9 + W3-11 coexistence | lizzi S-7 §V.13 | 2-3h LOW |
| C44 | `S86-R-PROTECTION-MELLIN-CRITERION` (Level-2/3, defer-eligible if W9 over budget) | Prove or disprove criterion in lizzi S-1 §IV.5: "observable O is R-protected on 5-atlas iff `m_n^O = 0` for all n ∈ {0, 2, 6}"; test against S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED classification | lizzi S-7 §V.12 | 8-12h HIGH |
| C45 | `S86-SIXTH-REGULATOR-SYNTHESIS` (Level-3, defer-eligible — only meaningful after C28) | Construct composite regulator `r_mix = α·zeta + β·cutoff_sqrt` with α + β = 1, α, β > 0; compute Mellin vector `f^{r_mix}`; test whether any (α, β) produces joint scheme-indep on f_conv AND eps_H (W5-7 obstruction clause) | lizzi S-7 §V.9 | 2-3h LOW |
| C46 | `S86-FCONV-AS-MB-SIBLING` (Level-3, defer-eligible — depends on C9) | Re-evaluate S77 finding `f_conv · P_zeta = 1.72e-9` (0.09 OOM gap) using Mellin-Barnes-continued `Lambda_CC^MB` (output of C9) replacing direct truncated a_0 | lizzi S-7 §V.10 | 2-3h LOW |

---

## §3. Sequencing Constraints (verbatim from closeout §6.4)

| Predecessor | Successor | Reason |
|:------------|:----------|:-------|
| W0 (R1+R2 PRU v3) | ALL waves | SOURCE-RECONCILIATION sub-audit must be operative at S86 plan-freeze for every subsequent wave |
| W1 (T2 + T3 registry slots) | C2-cascade wave | §VII.S parent must land before C-α/β/γ corollaries |
| W2 (C9 + C10 Mellin infra) | W3 (T9 REPLACEMENT-B) | T9 PASS-condition requires `analytic_zeta(s, L_max)` API |
| W4 (P4 BRANCH-IV ξ_E_GGE^{−1} pin) | W5 (P3 SECTOR-1 ξ²(0) IC) | Sector-1 ξ²(0) IC sources from ξ_E_GGE^{−1} pin (gen-physicist 9A §3.6) |
| W0 (R5 K-disambiguation + R8 three-layer methodology) | W1 (T1 W2-12 entry) | T1 references K_crit_BdG distinct from K_crit |
| W0 (R8 three-layer methodology) | W8 (P6 + P7 CGWB ⊥ α_s) | Three-layer methodology entry must exist before diagrammatic commit + Monte Carlo |
| ALL waves | Late-S86 P13 EVOI-table-refresh | EVOI refresh captures post-S86 work-fraction state — must be LAST |
| W2 (C9 Mellin infra) | W10 (C37 ZFP discharge) | C37 ζ-at-interior route may depend on Mellin-cone framework |

### §3.1 Dependency graph (verbatim from closeout §7.3)

```
W0 (foundation) ─┬─ R1, R2, R3, R4, R5, R6, R7, R8, R9, R10
                 ├─ C17, C18, C19, C21, C22, P14, C25, C27
                 │
                 ├─→ W1 (registry) ─┬─ T1, T2, T3, T4, T5, T6, T7, T8, T10, C8, C23, C41
                 │                   │
                 │                   ├─→ W6 (immunization corollaries) ─ C2, C40, C42
                 │                   ├─→ W7 (CC residue + branch-c) ─ C1, C4
                 │                   └─→ W9 (W2-2 + parity-extension) ─ C26, C24, C44
                 │
                 ├─→ W2 (Mellin infra) ─ C9, C10, C11, C12
                 │     │
                 │     └─→ W3 (Mellin consequences) ─ T9, W0-7/11/20 re-emissions, C13
                 │     └─→ W10 (W9-5 ZFP) ─ C37 (depends on C9)
                 │
                 ├─→ W4 (BRANCH-IV + SECTOR-2) ─ P4, P5, C28
                 │     │
                 │     └─→ W5 (SECTOR-1) ─ P3 (HARD: P4 must precede), C15, C16
                 │
                 ├─→ W8 (CGWB ⊥ α_s) ─ P6, P7, C7
                 │
                 ├─→ W10 (W9-5 ZFP, parallel routes) ─ C38, C39
                 │
                 └─→ Late-S86 (observational-watchlist consolidation, ALL prior waves) ─
                       P1, P2, P8, P9, P10, P11, P12, C5, C6, C29, C30, C31, C32, C33, C36
                       └─→ P13 EVOI-TABLE-REFRESH (FINAL — captures post-S86 work-fraction)

S87+ defer: C2 corollaries (C-δ/ε/ζ/ι), C20, C34, C35, C45, C46
```

### §3.2 Level ordering (closeout §7.2 — informs partition, NOT a probability claim)

- **LEVEL 1 (must-do)**: R1-R10, C17-C19, C21-C22, P14, C25, C27 (W0); T1-T8, T10, C8, C23, C41 (W1); C9-C12 (W2 HEAVY); T9, W0-7/11/20 re-emissions, C13 (W3); P4, P5, C28 (W4); P3, C15, C16 (W5 LARGEST single load).
- **LEVEL 2 (should-do)**: C2 + C40 + C42 (W6); C1, C4 (W7); P6, P7, C7 (W8); C26, C24, C44 (W9); C37, C38, C39 (W10); P11, P10, P9, P8, C30, C31, C32, C33, C36, P12, P1, P2, P13, C5, C6, C29 (late-S86).
- **LEVEL 3 (defer-eligible to S87+)**: C2 corollaries (C-δ/ε/ζ/ι), C20 (4-6h α_s remediation), C34 (12h), C35 (4h), C45 (after C28), C46 (after C9), C42 (if W6 over budget).

---

## §4. Methodology Debts S86-W0 Absorbs (closeout §6.5)

S86-W0 is the cleanup wave that absorbs the 7 distinct debt classes from 5A workshop (lizzi 9A §7) + 11 W-3 v2 clauses + 17 schema-1.5 entries + K_crit triple collision:
- PRU Class 8.1 (PINNED-BUT-DRIFT) → R2 + Sub-diff A (`_source_reconciliation_audit.py`).
- Machinery-feasibility envelope → Sub-diff B (`math-scripts.md`).
- PRDR keyword window granularity → Sub-diff C + R5 K-disambiguation.
- AMRI pre-flight → existing W4-8 REFRAMED as canonical pattern.
- Helper-file pre-existence check → eliminates W0-15-class FAILs.
- cutoff_axis YAML pin → R3 closes W3-9 vs W3-11 PRU defect at planner-template level.
- Keyword-context-window adjustment → R5 + lizzi G4a addresses W1c-3 over-classification.

Together these constitute the FULL S85 v3 rule-file landing per §3.5 R1.

---

## §5. What S86 Plan-Write Must NOT Include (closeout §6.6)

- Do NOT re-pin convention/scheme/threshold for any S85 verdict (FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030).
- Do NOT propose master-gate tally or PASS/FAIL ratio for S86 (per `feedback_no-master-gate-tally.md` + `feedback_reporting-framing.md`).
- Do NOT skip the SOURCE-RECONCILIATION sub-audit at S86 plan-freeze (per lizzi 9A §7 PRU Class 8.1 — D_max ≥ 3.0 hard-halt threshold).
- Do NOT attempt all 92 §3 items in a single session — explicit S87+ deferral for Level-3 items per §3.2 above.
- Do NOT cite "increases substrate confidence" or other narrative-trajectory language; report individual gate verdicts and structural-results-registry deltas only (per `.claude/rules/epistemic-discipline.md`).

---

## §6. Trigger-Phrase + Verdict-Format Reminder for Per-Wave Planners

Per `.claude/rules/math-scripts.md` "Double-Check Logic Before Compute" + `.claude/rules/gate-verdicts.md`:

### §6.1 Trigger phrases
Every gate block whose hypothesis contains any of: "increases", "decreases", "suppresses", "amplifies", "widens", "narrows", "dominates", "larger than", "smaller than", or any sign / direction / threshold claim, MUST include a **substitution chain** (definition → substitution → simplification → direction). Trigger prefixes for plan-block headers:
- `[SIGN]` — sign claim (+/−)
- `[VERIFY]` — quantitative verification via Python before commit
- `[AUDIT]` — factor-counting / OOM-estimate that must be reproducible
- `[VERIFY-THEOREM]` — structural theorem requiring proof + counterexample probe
- `[CHAIN]` — multi-step substitution that must appear inline

### §6.2 Verdict-line schema (per `.claude/rules/gate-verdicts.md` W9a-99 dual-SHA template)
```
GATE_ID|VERDICT|VALUE|SCHEME|CONVENTION|L_MAX|content_sha256:<64-hex>|audit_sha256:<64-hex>
```
- `VERDICT ∈ {PASS, FAIL, INFO, PENDING-EVENT, PRE-REG-INCOMPLETE}`. PASS/FAIL/INFO are all valid scientific outcomes (per `feedback_reporting-framing.md`). Exit code 0 regardless.
- `content_sha256` = SHA256 of the canonical-form output payload (.npz / .json / .csv).
- `audit_sha256` = `closure_hash(input_pin_map ∪ machinery_pin_map)` — computed from pins, NEVER hardcoded.
- A 16-hex companion comment row (`# audit_sha256_short=…`) accompanies each canonical line for human-scan readability per W9a-99 split.

### §6.3 Canonical-constants discipline
Every computation script MUST `from canonical_constants import *`. Local-only variables tagged `# (local)`. New constants added to `canonical_constants.py` BEFORE script imports them. Bare `a_n` citations carry explicit regulator-pin tag per P14 (e.g., `a_0^{ζ}`, `a_2^{Pauli-Villars}`).

### §6.4 GPU + threading
- Python interpreter: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`.
- For matrices ≥100×100 (eigvals / SVD / matmul / FFT): prefer `torch.linalg` on GPU (AMD RX 9070 XT, 17.1 GB VRAM, ROCm 7.2). Cite explicitly in plan dispatch prompts (per `feedback_compute-environment.md`).
- CPU-only fallback: `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`.

### §6.5 Script-prefix convention
`computations/s86_w{i}_<gate-slug>.py` (where `i` is wave number, possibly with sub-letter `a/b/c`). Output paths: `s86_w{i}_<slug>.npz`, `.png`, `.json`.

---

## §7. Wave-Equivalent Budget + Concurrent-Agent Cap

Per closeout §6.1 substitution chain:
- ~8 concurrent agents × 2h/agent ≈ **16 agent-hours/wave** (per `feedback_dispatch-discipline.md`).
- Unified §3.7 budget ≈ **35-45 wave-equivalents** (~280-360 agent-hours).
- Per session: 8-12 waves × 16 = 128-192 agent-hours.
- Conclusion: S86 alone CANNOT clear all carry-forwards. S86 = first of S86 + S87 (+ possibly S88).

Closeout proposed S86 wave count: **11 waves (W0-W10) + late-S86 sub-wave**, targeting Level-1 must-do + substantial Level-2 should-do, leaving Level-3 for S87+. **User instruction (S86 plan-write trigger)**: bias toward smaller chunks per agent-death-when-overwhelmed observation; partition phase will likely split heavy waves further (W0 16+ items → W0a+W0b; W5 LARGEST single load → W5a+W5b; late-S86 → 2-3 sub-waves).

---

## §8. Extra Context (from --context flags)

None provided in this invocation.

---

**End of context file.** Per-wave planners read this file + their assigned partition entries (from `session-86-partition.md`) and produce `session-86-plan-w{i}.md` with full 13-field gate blocks per `.claude/skills/rclab-plan/skill.md` §3b template.
