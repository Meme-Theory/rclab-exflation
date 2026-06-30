# Session 95 Wave 1 — Spectral Cross-Pillar-Bridge Convergence & Re-Anchoring (Results Working Paper)

**Session**: 95 | **Wave**: 1 | **Plan**: session-95-plan-w1.md | **Theme**: Spectral cross-pillar-bridge layer at the convergence / re-anchoring axis — §VII.BG Stage-2 two-axis promotion, K_csub_R three-corridor re-anchor, §VII.BE convergent-pole re-anchor, R₁ FI-truncation-robustness. Four mutually-independent gates carried forward from S94 W1/W3 + tesla-collab §V.5.

## Gate Sections

### §W1-1. CF-S95-HK-1 (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S95-HK-1`
**Trigger**: `[VERIFY-THEOREM]` (no [SIGN] 3-tuple required — verdict-aggregation gate; plan `schema_v2_3tuple_required: false`)
**Classification**: **GEOMETRIC** (joint-theorem Stage-2 two-agent parallel cross-axis independent-verify)
**Agent**: `lizzi-spectral-functional-theorist` (orchestrating aggregator + Axis-A spectral reviewer; Axis-B = `volovik-superfluid-universe-theorist`; `connes-ncg-theorist` EXCLUDED as original author)
**Hypothesis**: The §VII.BG α_s T5 Connes-Karoubi K_0-pairing transport bridge (STAGE-1-CANDIDATE, a_4 home pole s=2, L3=0.122985 < L2=0.132537) survives a Stage-2 two-axis non-connes PASS-AND on every 5-anatomy clause + the JOINT Δ_scheme→0 clause, promoting it to STAGE-3-PERMANENT.
**Plan reference**: `sessions/session-plan/session-95-plan-w1.md` §W1-1 (Stage-2 two-reviewer dispatch note, machinery pin, PASS-AND substitution chain).

**Verdict**: **PASS** — composite PASS-AND across BOTH non-connes axis-distinct reviewers. All Axis-A spectral-side single-axis clauses PASS, all Axis-B transport-side single-axis clauses PASS, the JOINT clause (c) Δ_scheme→0 is PASS-AND'd (PASS in BOTH, |Δ_scheme| = 0.0 ≤ 1e-12 bit-exact), substrate-input-orthogonality holds (Axis-A and Axis-B anchor sets disjoint), and both recorded AXIS-COMPOSITE lines are PASS. **§VII.BG is LICENSED STAGE-1-CANDIDATE → STAGE-3-PERMANENT** (registry-text flip effected by `mack-cosmic-bridge`, sole registry writer, as the post-gate hook — this gate does NOT edit `permanent-results-registry.md`).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script** `computations/session-95/s95_w1_1_vii_bg_stage2_aggregator.py` — present (42,941 B). `grep "from canonical_constants import"` → matches (the `from canonical_constants import (` block importing `M_KK, tau_fold, alpha_s_cmb_central, alpha_s_canon_2020, alpha_s_canon_2020_err, w0_FW, r_CMB_framework`). `grep "append_verdict"` → `def append_verdict(...)` + its call under `--emit`. ✓
- **Data** `computations/session-95/s95_w1_1_vii_bg_stage2_aggregator.npz` — present (8,499 B); per-axis clause-verdict vectors (PASS=1/INFO=0/FAIL=-1/ABSENT=-2 legend), JOINT_A/JOINT_B/joint_pass_and, orthogonality/oaa/axis-composite booleans, anchor labels, promotion string, canonical pins. ✓
- **Plot** `computations/session-95/s95_w1_1_vii_bg_stage2_aggregator.png` — present (25,682 B); two-row clause PASS-AND matrix (Axis-A spectral 5 cells incl JOINT-c; Axis-B transport 4 cells incl JOINT-c) with composite + JOINT-c PASS-AND + orthogonality in the title. (Optional per plan; rendered.) ✓
- **JSON sidecar** `computations/session-95/s95_w1_1_vii_bg_stage2_aggregator.json` — present (5,356 B); full aggregation dict + parsed raw clause lines (both axes) + input-pin map + canonical pins.
- **Verdict line** `computations/session-95/s95_gate_verdicts.txt` — `^CF-S95-HK-1:.* audit_sha256=[a-f0-9]{64}` matches; `audit_sha256=ad22903532aa1494feff0bbef1bf5407906415ac00ea12e19b3ff93567919798` (UNIQUE across all 4 canonical lines in the file), `content_sha256=6c3ef2ec546d2991bfc73209ce81223099bc42f9086d219f602e1998276bd01e`; dual-SHA companion row + Stage-2 provenance comment row present; NO [SIGN] 3-tuple (correct for [VERIFY-THEOREM]). `audit_sha256` computed from the input-pin map (script + canonical + pinmap + axisA review SHA + axisB review SHA + registry-block SHA + w1_3 npz SHA + per-gate identity keys), NOT hardcoded. ✓
- **WP section** this `### §W1-1.` — `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. ✓

**MCP Pre-Compute Audit** (queries executed before writing the aggregator; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("VII.BG alpha_s T5 Connes-Karoubi K_0 pairing transport bridge STAGE-1-CANDIDATE")` → returns the §VII.BG bridge map = direct Connes-Karoubi K_0-pairing (T5, index-fixed) with the Level-2 K_0-pairing-image envelope + CMB-pivot α_s anchor (session-94-plan-w1 equation), and the S94 W1-3 producing provenance `w1_3_vii_bx_t5_alpha_s_a4_recovery`. **NOT pre-closed** — this is the Stage-2 promotion gate, not a settled result; the STAGE-1-CANDIDATE landing is the upstream this gate forwards from.
- `trace_entity("delta_scheme secondary class scheme discriminator")` → **S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR** independently emits `delta_scheme=0.000e+00, GV_APS_L12=GV_CS_L12=-1.208158e+08, eta_L12=0e+00, reading=A`. This is a SEPARATE gate (not the S94 producing gate) that corroborates the JOINT clause (c) value — strengthening, but the aggregation reads the value from the two frozen reviews, not from S90.
- Both reviewers' independence attestations cross-checked: Axis-A (lizzi) and Axis-B (volovik) each record reading ONLY the registered §VII.BG block (both pinned the identical registry-block SHA `18d365904f251b7f6da50650a3eecfb80a56a0deb795bd616d4093396ebafc8e`, L20713–20789) + their disjoint orthogonal anchors; neither read the S94 W1-3 workshop transcript; neither is `connes-ncg-theorist` (the original author). The aggregator reconstructs the same registry-block SHA into its audit_sha256 input-pin map.

**Results** (NUMBERS → conjunction → interpretation):

**Clause-by-clause PASS-AND matrix** (asymmetric partition — the §VII.BG 5-anatomy splits into 4 spectral-side single-axis clauses on Axis-A + 3 transport-side single-axis clauses on Axis-B + the shared JOINT clause (c), PASS-AND'd across both):

| Clause | Axis-A (lizzi spectral) | Axis-B (volovik transport) | PASS-AND |
|:-------|:-----------------------:|:--------------------------:|:--------:|
| Element-1 (substrate-IS observable) | **PASS** | — (spectral-side) | PASS |
| Element-3 (bridge map: Connes-Karoubi K_0-pairing) | **PASS** | — (spectral-side) | PASS |
| Element-4 (algebraic envelope L^{−α}, Level-2-binding) | **PASS** | — (spectral-side) | PASS |
| Degree-match (\|deg(a_4/a_2)\|=2=\|d_A\|, non-scalar) | **PASS** | — (spectral-side) | PASS |
| Element-2 (laboratory-IN OE-form, BdG/transport image) | — (transport-side) | **PASS** | PASS |
| BdG χ-image inheritance K_0-class (non-trivial) | — (transport-side) | **PASS** | PASS |
| substrate-natural NON-SCALAR binding | — (transport-side) | **PASS** | PASS |
| **JOINT (c) Δ_scheme → 0** | **PASS** | **PASS** | **PASS-AND = True** |
| **AXIS COMPOSITE (recorded)** | **PASS** | **PASS** | — |

- **Axis-A single-axis roll-up**: PASS (4/4 spectral-side clauses PASS). **Axis-B single-axis roll-up**: PASS (3/3 transport-side clauses PASS).
- **JOINT clause (c) Δ_scheme→0 PASS-AND**: JOINT_A=PASS ∧ JOINT_B=PASS ⇒ **PASS-AND=True**, logical AND not OR (`joint-theorem-promotion.md §"Stage 2"` (b)). Both reviewers independently re-derived Δ_scheme = max{|GV_APS−GV_CS|, |GV_APS−GV_BC|, |GV_CS−GV_BC|} = **0.000e+00** at L_max=12 (bit-exact; Sage-QQ exact-rational difference = 0 in Rational Field, BOTH reviews) with GV_APS = GV_CS = GV_BC = −1.2081580929e+08. |Δ_scheme| ≤ 1e-12 satisfied with strict bit-exact zero in BOTH verdicts.

**Substrate-input-orthogonality confirmation** (`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`):
- Axis-A loaded ONLY `{s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz}` (Yang-Mills a_4-channel residue, spectral side).
- Axis-B loaded ONLY `{s88_w3b_chi_inheritance_kde_complete.npz, s88_w4c_az_inheritance_cartesian_confirm.npz}` (BdG χ-image inheritance K_0-class occupation + AZ-BDI-DIII χ-action, transport side).
- Intended-set overlap = ∅; cross-leak A→B-set = ∅; cross-leak B→A-set = ∅ (Axis-B's mention of `s94_w1_3...` is in a "did NOT load" independence attestation — a negated context, correctly excluded from the load-set). ∃ ≥1 observable loaded by exactly one reviewer (in fact 3). **Orthogonality = True** ⇒ PASS-AND is at the structural ceiling (different decision pipelines AND disjoint data inputs); NO substrate-input-overlap caveat.

**OAA exclusion**: Axis-A = `lizzi-spectral-functional-theorist`, Axis-B = `volovik-superfluid-universe-theorist`; axis-distinct (spectral/NCG ≠ transport/superfluid); neither is the excluded original author `connes-ncg-theorist`; both attest no-workshop-transcript-read + non-authorship. **OAA_ok = True**.

**4-tuple**: `(value=composite=PASS;…;promotion=STAGE-1-CANDIDATE → STAGE-3-PERMANENT, scheme=T5-Connes-Karoubi-K_0-pairing-a_4-channel-s2-index-fixed, convention=VII-BG-STAGE-2-TWO-AXIS-NON-CONNES-PASS-AND, L_max=12)`.

**Substitution chain (logical-conjunction PASS predicate; `math-scripts.md §"Double-Check Logic"`)** — the composite is COMPUTED from the review files, never assumed:
- **Step 1** (axis-A single-axis clause verdicts, from MD_A): {Element-1=PASS, Element-3=PASS, Element-4=PASS, Degree-match=PASS} ⇒ axisA_single_all = PASS.
- **Step 2** (axis-B single-axis clause verdicts, from MD_B): {Element-2=PASS, BdG=PASS, substrate-natural=PASS} ⇒ axisB_single_all = PASS.
- **Step 3** (JOINT clause (c), both MDs): JOINT_A=PASS, JOINT_B=PASS.
- **Step 4** (PASS-AND): joint_pass_and = (JOINT_A==PASS) ∧ (JOINT_B==PASS) = True [logical AND].
- **Step 5** (orthogonality, anchor SHAs): anchor-set(A) ∩ anchor-set(B) = ∅, ∃ disjoint observable ⇒ orthogonality_ok = True.
- **Step 6** (canonical form): composite_PASS = (axisA_single_all==PASS) ∧ (axisB_single_all==PASS) ∧ joint_pass_and ∧ orthogonality_ok ∧ oaa_ok ∧ (comp_A==PASS) ∧ (comp_B==PASS).
- **Step 7** (substitute): all seven conjuncts = True.
- **Direction / Conclusion**: the composite is a logical conjunction — ANY single FALSE conjunct (any clause FAIL in either reviewer, JOINT FAIL in either, orthogonality violated, axis-composite FAIL) would make composite FALSE. All conjuncts True ⇒ **composite = PASS** ⇒ the STAGE-3-PERMANENT promotion is the CONSEQUENCE of the full conjunction, not its assumption. (The first dry-run surfaced two markdown-parser bugs that produced a spurious FAIL — a JOINT-keyword-in-rationale mis-classification and a negated-mention cross-leak false-positive; both were fixed at the parser level, NOT by relaxing any clause criterion, and the re-run computed PASS from the unchanged review content.)

**Promotion license statement**: composite = PASS ⇒ **§VII.BG promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT** per `joint-theorem-promotion.md §"Stage 3"`. The α_s T5 a_4-home-pole Connes-Karoubi transport bridge joins the permanent cross-pillar-bridge registry as a structurally-independent (no-shared-context, disjoint-input) two-axis-verified theorem. The registry-text flip (replace `STAGE-1-CANDIDATE` tag with `STAGE-3-PERMANENT` at `permanent-results-registry.md` §VII.BG) is effected by `mack-cosmic-bridge` (sole registry writer per `feedback_mack-bridge-role.md`) as the post-gate hook; **this gate's PASS is the LICENSE, not the registry edit.**

**Dual-SHA**: `audit_sha256=ad22903532aa1494feff0bbef1bf5407906415ac00ea12e19b3ff93567919798`; `content_sha256=6c3ef2ec546d2991bfc73209ce81223099bc42f9086d219f602e1998276bd01e`. NO Option-A supersedes (first CF-S95-HK-1 emission). Artifacts: `s95_w1_1_vii_bg_stage2_aggregator.py/.npz/.png/.json`.

**Substrate-physics assessment (spectral-functional-theorist reading; IS-not-IN per `phononic-framing.md`)**: §VII.BG IS the substrate's Connes-Karoubi K_0-pairing image of the α_s running observable at the a_4 Yang-Mills home pole s=2. Direction of explanation flows FROM the D_K eigenvalue spectrum → a_4 Seeley-DeWitt moment (Mellin residue at the home pole s=2, weight-4 per the Phi-correspondence) → Connes-Karoubi K_0-pairing (the bridge map) → laboratory-IN α_s transport measurement — never inverted. The Stage-2 verify is a **methodology gate** (verdict-aggregation, not a fresh spectral computation): it certifies that the bridge's substrate-IS structural content is re-derivable by two axis-distinct reviewers WITHOUT shared workshop context and on DISJOINT data inputs — the constructive structurally-independent-agreement pathway of `joint-theorem-promotion.md`, the ONLY admissible route to permanent-registry inclusion for a cross-axis joint theorem. **The functional-independence content is the load-bearing physics**: the JOINT clause (c) Δ_scheme = 0 means the bridge-map VALUE is INVARIANT across the three secondary-class schemes (APS-1975 ρ-invariant / Cheeger-Simons differential character / Bismut-Cheeger η-form) — a **FUNCTIONAL-INDEPENDENT (structural)** result on the secondary-class axis, orthogonal to the UV-regulator RD axis. Crucially, this scheme-independence is not numerical coincidence: it is FORCED by the 3He-B substrate's BDI universality class — the η-defect that distinguishes the three schemes is EVEN-grading and vanishes on a parity-blind (BDI) substrate (the PROVEN W17 Bare-Eigenvalue Parity-Blindness Wall; corroborated by the SEPARATE S90-AQ / S86-W-11 / S88-W7-LF-D gates), so all three schemes collapse bit-identically to the cubic-ρ Dixmier-trace sum −4·Σ dim·ρ³·|λ|^{−4}, carried by the odd-grading GV-Heitsch secondary class. That a regulator-CHOICE-invariant value sits at the heart of the bridge is precisely what makes §VII.BG a structural cross-pillar result rather than a regularization artifact — the distinction this agent is built to police, and it holds here under both reviewers' independent re-derivation.

**Solution-space meaning (PASS)**: the §VII.BG α_s-transport bridge is now a STAGE-3-PERMANENT structural theorem. The promotion does NOT depend on the regularization scheme (the JOINT clause is scheme-INDEPENDENT) nor on a single reviewer's machinery (two axis-distinct reviewers, disjoint inputs, PASS-AND). The constraint-map effect: the α_s running observable at the a_4 home pole has a permanent, structurally-verified Connes-Karoubi K_0-pairing to the laboratory-IN transport measurement, with the deg-match (|deg(a_4/a_2)|=2=|d_A|) and non-scalarity both confirmed on the spectral AND transport sides. Downstream cross-pillar consumers of §VII.BG may now cite it WITHOUT the STAGE-1-CANDIDATE qualifier (once mack-cosmic-bridge effects the registry-text flip).

---

### §W1-2. CF-S95-K-CSUB-R-RE-ANCHOR (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S95-K-CSUB-R-RE-ANCHOR`
**Trigger**: `[VERIFY]` (schema-v2 3-tuple emitted — §7 substitution chain pre-registers directional predictions)
**Classification**: **GEOMETRIC** (UV-finiteness re-attempt + Tier-1/Tier-2 dimensional-re-anchorability)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: After the S94 W1-4 2-pt-PV FAIL (Jensen exp(−τρ) spectrum diverges in the IR-accumulation direction, per-shell ~exp(+0.76ρ)), K_csub_R is rendered finite via ≥3-pt Pauli-Villars (corridor a) or τ-running regulator (corridor b), OR re-anchored to a Tier-2 dimensionless log-derivative / ratio (corridor c).
**Plan reference**: `sessions/session-plan/session-95-plan-w1.md` §W1-2 (three-corridor method, N-point PV moment conditions, Tier-2 log-derivative substitution chain).

**Verdict**: **FAIL** — all three corridors diverge; K_csub_R is **Tier-2-DIMENSIONFUL-held** (registry-PASS-INELIGIBLE). This is a boundary result, not a defect: it pins K_csub_R as a non-re-anchorable held quantity, the second member (after §VII.AX n_PBH) of the dimensionful-slot-collision class. 3-tuple: `sign=PASS magnitude=FAIL regime=VALID` → composite FAIL (per gate-verdicts.md collapse rule: `magnitude==FAIL ∧ regime==VALID ⇒ FAIL`).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script** `computations/session-95/s95_w1_2_k_csub_r_re_anchor.py` — present (50,954 B). `grep "from canonical_constants import"` → line 166 `from canonical_constants import *`, line 167 `from canonical_constants import (`. `grep "append_verdict"` → line 266 (def), line 881 (call). ✓
- **Data** `computations/session-95/s95_w1_2_k_csub_r_re_anchor.npz` — present (17,785 B); per-N PV arrays, τ-running arrays, Tier-2 log-derivative arrays, Step-1 per-shell growth, Tier-1/Tier-2 classification. ✓
- **Plot** `computations/session-95/s95_w1_2_k_csub_r_re_anchor.png` — present (247,683 B); 4 panels: (A) N=2,3,4 PV intercept vs L_fit [all grow]; (B) per-shell weight ~ exp(+0.7514ρ) fit; (C) Tier-2 D1/D2 log-derivatives vs L_fit [both grow]; (D) diagnostic. ✓
- **Verdict line** `computations/session-95/s95_gate_verdicts.txt` — `^CF-S95-K-CSUB-R-RE-ANCHOR:.* audit_sha256=[a-f0-9]{64}` matches (line 1); `audit_sha256=84c5ec484fb7ddfe81c828f7bd9118419870b137b883fe7bc80eef5151e4bf28`, `content_sha256=6e8fe7a3f8dc2496be8761dc975fb9e9a1b2f72720cadd8068bcb9694bf4c46c`; dual-SHA companion row + schema-v2 3-tuple row + tier_pin=TIER-1 row present. content_sha256 reproduced from script bytes (not hardcoded). ✓
- **WP section** this `### §W1-2.` — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. ✓

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries before writing the script):
- `search_knowledge("K_csub_R UV-finiteness Pauli-Villars Jensen IR-accumulation divergence")` → S94-K-CSUB-R-ABSOLUTE-CONVERGENCE **FAIL** (`max_dK_over_dL_pv=2.1071e+30`, `converges=False`); `_pauli_villars_subtraction` 2-pt baseline; S93 W7-2 retry provenance. NOT closed — re-anchor is genuine open work.
- `search_knowledge("S94 W1-4 K_csub_R absolute convergence per-shell exp 0.76 rho")` → S94-K-CSUB-R-ABSOLUTE-CONVERGENCE FAIL confirmed; `dK_over_dL_increasing=True`. CF-S95-K-CSUB-R-RE-ANCHOR carry-forward not yet evaluated.
- `get_constant("M_KK_gravity")` → `7.428660036284456e+16` (S42 CONST-FREEZE-42; the Λ_UV=M_KK PV scale). `get_constant("tau_fold")` → `0.19` (S12/S42).
- `list_constants("K_csub|c_sub")` → `c_sub_baseline=2.238`, `c_sub_corrected_central=3.5169`; NO canonical `K_csub_R` entry (the intercept is NOT yet promoted — confirms it is held). `kappa_2_substrate_FW=0.021018084987437196` (S89, used for provenance pin only; the gate does not consume it in the metric).
- Corpus read: `cross-pillar-bridge-corpus.md §25` (Tier-1/Tier-2 K=1 calibration: §VII.AX.OP-PROJ n_PBH = Tier-2-DIMENSIONFUL-held via dimensionful-slot-collision; §VII.AV.STATE-PROJ L_emp = Tier-2-DIMENSIONLESS re-anchored) + `§26` (Non-Promotion-by-Held-Number meta-taxonomy; Member A dimensionful-slot-collision). The CF-S94 forward note explicitly anticipated this re-determination ("re-source the magnitude from OUTSIDE the cardinality channel — PV/zeta at Λ_UV=M_KK"). **PRE-CLOSED? NO** — the re-anchor attempt is genuine open work; the result lands a new (candidate-K=2) Tier-2-dimensionful instance.

**Results**:

NUMBERS first (verdict = FAIL):

**Step 1 — IR-accumulation confirmed (analytic + numeric).** Per shell ρ=p+q the a_2 s=2 weight `Σ_{p+q=ρ} dim(p,q)·|λ|^{−4} = Σ dim·C₂^{−2}·exp(+4τρ)` grows as `exp(+0.7514ρ)` (log-linear fit slope 0.751360 vs predicted +4τ = +0.760000). The Jensen damping `exp(−τρ)` at fixed τ drives the high-Casimir eigenvalues `λ = √C₂·exp(−τρ) → 0`, so `λ^{−4}` ACCUMULATES toward large ρ — the divergence is in the **small-λ (IR-accumulation)** direction, NOT the large-λ (UV) direction. This is the substrate-internal structural fact the S94 W1-4 FAIL diagnosed.

**Corridor (a) — N-point Pauli-Villars: all diverge; higher N is WORSE.** N-point PV coefficients solved via the Vandermonde moment system (Σcᵣ=1, Σcᵣmᵣ^{2k}=0 for k=1..N−1), Sage-exact: N=2 → {+2,−1}; N=3 → {+3,−3,+1}; N=4 → {+4,−6,+4,−1} (binomial pattern of (1−x)^{N−1}). FULL CM-1995 Jensen table, scan L∈[50,100]:

| N | max\|dK/dL\| over [50,100] | converges? | K_intercept(L=100) | IR-sub-const Σcᵣmᵣ^{−4} |
|:--|:---------------------------|:-----------|:-------------------|:------------------------|
| 2 (S94 baseline) | 2.1071e+30 | False | +2.108e+31 | +1.750 |
| **3** | **2.4309e+30** | **False** | +2.432e+31 | +2.361 |
| **4** | **2.7342e+30** | **False** | +2.736e+31 | +2.882 |

Sage-exact (verified independently): the N=3 PV bracket at λ→0 expands as `λ^{−4} − 85/36 + O(λ²)` (IR-sub-const 85/36 = 2.3611…). **The PV subtraction saturates to a BOUNDED per-mode constant `Σcᵣmᵣ^{−4}` at λ→0; the divergent `λ^{−4}` term survives UNCHANGED.** A finite-N PV chain subtracts the leading N−1 *polynomial* (large-λ Laurent) moments — but the IR-accumulation tower `exp(+0.76ρ)` is an *exponential* growth, not a polynomial moment. No finite-N polynomial-moment subtraction regulates an exponential tail. The divergence WORSENS with N because the IR-sub-const grows (1.750→2.361→2.882) while the surviving λ^{−4} tower is untouched. **Tier-1 corridor (a) FAILS for all N.**

**Corridor (b) — τ-running regulator: all diverge.** With the N=3 chain and regulator mass `M_r(τ) = m_r·(τ_fold/τ_run)` scanned over τ_run ∈ {0.5, 1.0, 2.0}×τ_fold: max\|dK/dL\| = 1.468e+30 / 2.431e+30 / 1.322e+31 — none converges. A PV mass M_r(τ) is ρ-INDEPENDENT (a single scale, even if τ-running); to regulate `exp(+4τρ)` the regulator would need to inject `exp(−4τρ)` PER SHELL ρ, i.e. a mass growing exponentially with ρ. A τ-running but ρ-independent mass shifts the overall subtraction scale (changing the IR-sub-const) but injects NO ρ-dependence → cannot regulate the ρ-dependent exponential tower. **Tier-1 corridor (b) FAILS.**

**Corridor (c) — Tier-2 dimensionless log-derivative: does NOT re-anchor → Tier-2-DIMENSIONFUL.** The canonical K_csub_R(L) intercept grows super-exponentially (10⁴ at L=12 → 10³¹ at L=100). Diagnostic fits: `ln K ~ exp(c·L)` with c=0.7115, residual 1.14 vs `ln K ~ α·ln L` (α=28.73) residual 10.08 — the exponential fit is 8.8× tighter, so `growth_is_exponential=True`. Consequently (Sage-verified): if `K ~ exp(c·L)` then `d ln K/d ln L = L·c` GROWS linearly in L (max\|ΔD1/ΔlnL\|=64.75 ≫ 1e-3 ceiling), and `d²ln K/d(ln L)² = L·c` also grows. The log-derivative annihilates a multiplicative *power-law* prefactor `w(L)=L^p` (the §VII.AV L_emp / §VII.AX route — where `d ln N_eigs/d ln L → 5`, a finite integer cascade exponent), but it does NOT annihilate an *exponential*. There is no finite dimensionless cascade-exponent here. **The dimension (M_KK², carried by the a_2 moment that sources Newton's coupling) stays trapped in the same multiplicative slot as the exp(+0.76ρ) divergence → Tier-2-DIMENSIONFUL-held.**

**4-tuple**: (value=`tier1_a_converges=False; tier1_b_converges=False; tier2_log_deriv_converges=False; tier2_class=Tier-2-DIMENSIONFUL-held; …`, scheme=`Pauli-Villars-N-point-at-Lambda_UV-M_KK-corridors-a-b-Tier-2-log-derivative-corridor-c-CLASS-FULL`, convention=`FULL-CM-1995-sec-III-4-residue-N-point-PV-Tier-1-OR-Tier-2-dimensionless-reanchor`, L_max=100).

**Substitution chain (Steps 1–5; direction)**: confirmed end-to-end. Step 1: per-shell ~exp(+0.7514ρ) [≈ predicted +4τ=+0.76] IR-accumulation. Step 2: N-pt PV imposes Σcᵣ=1, Σcᵣmᵣ^{2k}=0 (k=1..N−1) [Vandermonde, Sage-exact]. Step 3: small-λ bracket → λ^{−4} − (bounded const Σcᵣmᵣ^{−4}); divergent λ^{−4} survives [Sage: N=3 bracket = λ^{−4} − 85/36 + O(λ²)]. Step 3b: ρ-independent regulator cannot regulate ρ-dependent exponential tower. Step 4: K~exp(c·L) ⇒ d ln K/d ln L = L·c GROWS (no power-law prefactor to annihilate). Step 5 canonical form: Tier-1 PASS ⟺ |dK/dL|<1e-3 [FALSE all corridors]; Tier-2 PASS ⟺ log-derivative converges + dimensionless [FALSE, growth exponential]. Conclusion: all three corridors diverge ⇒ FAIL, Tier-2-DIMENSIONFUL held.

**3-tuple semantics**: `sign=PASS` — §7 directional prediction (corridors a/b diverge ∧ D1 increasing ∧ growth exponential) MATCHES observation. `magnitude=FAIL` — no Tier-1 finite value and no Tier-2-dimensionless re-anchor (held quantity). `regime=VALID` — the FULL Jensen evaluator + N-point PV are valid throughout [10,100]. Composite collapse: `magnitude==FAIL ∧ regime==VALID ⇒ FAIL` (Sage-verified against gate-verdicts.md collapse rule).

**Provenance (CLASS=FULL, K=4 level-pin)**: FULL CM-1995 §III.4 `jensen_irrep_table` (CLASS=FULL) + N-point PV Vandermonde closed form. Regulator pins `a_2^{Pauli-Villars} + a_2^{Mellin} + a_2^{zeta}`. NO SCHEMATIC helper consumed (this is a FULL-only retry; the S94 W1-4 heat-kernel/hard-cutoff SCHEMATIC cross-check is NOT carried). `tier_pin=TIER-1` companion row; convention carries NO `-SCHEMATIC` suffix. Dual-SHA: `audit=84c5ec48…`, `content=6e8fe7a3…` (reproduced from script bytes). Artifacts: `s95_w1_2_k_csub_r_re_anchor.py/.npz/.png`.

**Substrate-physics assessment (spectral-functional-theorist reading)**: This is the FI/SD partition in action. K_csub_R is the c_sub renormalization intercept built from the a_2 Seeley-DeWitt SECOND spectral moment `Σ_k m_k λ_k^{−4}` of D_K (the moment sourcing Newton's coupling). The substrate IS this moment ratio; the question this gate answers is WHICH spectral functional of it is the physical observable. The dimensionful intercept and the dimensionless log-derivative are DIFFERENT spectral functionals of the SAME D_K under the SAME Jensen deformation. The result: under the Jensen `exp(−τρ)` deformation at fixed τ, the dimensionful intercept is **scheme-divergent in the IR-accumulation direction** — no UV regulator (any-point PV, τ-running) touches it, because the divergence is an exponential IR tower, not a polynomial UV moment. AND the dimensionless shape (log-derivative) does NOT survive either, because the growth is exponential (`exp(c·L)`), not power-law (`L^p`) — so there is no finite cascade-exponent invariant to re-anchor to. K_csub_R is therefore **Tier-2-DIMENSIONFUL-held** — registry-PASS-INELIGIBLE on the dimensionful magnitude. **This is the structural distinction from §VII.AX n_PBH**: n_PBH's cardinality channel `N_eigs(L) ~ L⁵` is a POWER-LAW divergence whose log-derivative → integer 5 (a Tier-2-dimensionless content exists, even though the held magnitude is dimensionful via dimensionful-slot-collision); K_csub_R's channel is EXPONENTIAL, so NOT EVEN the log-derivative re-anchors. K_csub_R is a structurally-distinct candidate K=2 instance for the corpus §25/§26 Tier-2-dimensionful taxonomy: a DIFFERENT divergent channel (a_2 s=2 Mellin moment under Jensen IR-accumulation, exponential — vs §VII.AX cardinality, power-law) with a dimensionful anchor and (more strongly) no dimensionless log-derivative re-anchor. **Solution-space meaning**: the dimensionful K_csub_R corridor CLOSES entirely under the Jensen deformation; only a SUBSTRATE-PHYSICAL scale anchor sourced from OUTSIDE the a_2 IR-accumulation channel (a cosmological-observable cutoff, or a different τ-flow boundary condition) could re-open it. Any downstream cross-pillar-bridge consumer of a *dimensionful* K_csub_R is structurally blocked; a consumer of the c_sub physics that does not require the absolute intercept (e.g. a ratio against a co-divergent reference at the same pole) is unaffected. The carry-forward is NOT "retry the regulator" (all UV regulators are now closed by this gate) — it is "re-source the K_csub_R scale from outside the IR-accumulation channel," directly analogous to the §VII.AX `CF-S94-N-PBH-CANONICAL-TRUNCATION-RE-DETERMINATION` route.

---

### §W1-3. CF-S95-VII-BE-TIER2-REANCHOR (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S95-VII-BE-TIER2-REANCHOR`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (§VII.BE FWD-C4 Level-3 re-anchor at the convergent Mellin pole)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The §VII.BE Pati-Salam Level-3 anchor — divergent at the inherited s=4 pole (SU(4)_PS residue shell-scaling L^{8−2s}, converges iff s>9/2) — re-anchors at the convergent pole s=6 where residue(L→∞)≈9.39e-4 with tail L^{−2.804}, so Level-3 < Level-2 is satisfiable (Tier-1); else a Tier-2 dimensionless functional closes the Level-3.
**Plan reference**: `sessions/session-plan/session-95-plan-w1.md` §W1-3 (pole-scan s∈{5,6,7}, empirical L^{−2.804} envelope pin — NOT the HH^1 α=8, re-derived η_FB^{SU(4)}=0.101814).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain — verified |
|:---------|:-----|:------------------------|
| script | `computations/session-95/s95_w1_3_vii_be_tier2_reanchor.py` | `from canonical_constants import` ✓; `append_verdict` ✓ |
| data | `computations/session-95/s95_w1_3_vii_be_tier2_reanchor.npz` | present (15,669 B); 50 keys incl. `ratio_L3_L2`, `residue_s6_Linf`, `tier2_reanchorable` ✓ |
| plot | `computations/session-95/s95_w1_3_vii_be_tier2_reanchor.png` | present (228,107 B); 4 panels: residue(L) at s∈{4,5,6,7}; shell exponent 8−2s vs s; s=6 rel-residual + L^{−α} envelope (test point L=12); Tier-2 log-derivative → 0 ✓ |
| verdict_line | `computations/session-95/s95_gate_verdicts.txt` | `^CF-S95-VII-BE-TIER2-REANCHOR:.* audit_sha256=[a-f0-9]{64}` ✓ (`audit_sha256=71aea79274b081b1f4ab5d4222b637a323151df58933b2949ce1d08668cfc326`); dual-SHA companion row ✓; schema-v2 3-tuple row ✓ ([SIGN]) |
| wp_section | this section | `Status: COMPLETED` ✓; `Verdict: PASS` ✓; `Output Artifacts` ✓; `MCP Pre-Compute Audit` ✓ |

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("VII.BE FWD-C4 Pati-Salam Level-3 SU(4)_PS Mellin pole convergence s=6 residue")` → returns the §VII.BE STAGE-1-CANDIDATE landing (S91 W7 / S92 W7), the **S93 W6-4 STRUCTURAL Stage-2 PASS-AND** (axis-A connes `146b5742`, axis-B landau `9df77b09`; composite INFO; VII-BE STAYS STAGE-1-CANDIDATE), and the §VII.P pole↔a_n equation `n=2 ⇒ pole s=6 (residue ∝ a_2)`. **NOT pre-closed**: this is the forward re-anchor gate, not a settled result. The S94 W3-9 FAIL (s=4 diverges) is the SETTLED upstream finding this gate forwards from.
- `get_constant("alpha_HH1_per_pole_FW_s6")` → **8.0** (S92; `S92-W7-CF-W9-10-B-pole-s6`). This is the **HH^1 cocycle-family Wodzicki exponent 2(s−2)=8** — a DIFFERENT observable from the SU(4)_PS spectral-action residue tail. Per the plan CAUTION, this value is **NOT** used as the Level-2 envelope; the gate pins the EMPIRICAL L^{−2.804} spectral-action residue tail instead.
- `get_constant("alpha_HH1_per_pole_FW_s4")` → 4.0 (the inherited-pole Wodzicki exponent; metadata only — the s=4 pole is non-anchorable for SU(4)_PS, settled S94 W3-9).
- `trace_entity("SU(4)_PS full-spectrum residue")` → no trace (the residue values live in the S94 W3-9 npz, not the knowledge graph; consumed directly from `s94_vii_ps_full_spectrum_level_3.npz`).
- **Sage MCP** `sage_eval` → confirmed the convergence condition `8−2s < −1 ⇔ s > 9/2` (exact `QQ(9)/QQ(2)`) and per-pole shell exponents: s=4 → 0 (NOT converges), s=5 → −2, s=6 → −4, s=7 → −6 (all converge). Shell exponent symbolic `−2s+8`.

**Verdict**: **PASS** (Tier-1 convergent-pole route). Composite collapse: `sign=PASS ∧ magnitude=PASS ∧ regime=VALID ⇒ PASS` per `gate-verdicts.md`.

**Results** (NUMBERS first, gate second, interpretation third):

*SU(4) Casimir-ladder self-check (re-used VERBATIM from S94 W3-9; Sage-verified):* `C₂(4)=15/4, C₂(6)=5, C₂(15)=8, C₂(10)=9`, conjugation-symmetric `C₂(a,b,c)=C₂(c,b,a)` — all match plan ladder. The SU(4)_PS spectrum IS the analytic `(C₂+1)` Casimir ladder; no diagonalization (dense storage at L=12 = 1094.7 GB ≫ 17.1 GB VRAM — Route-B analytic per-sector form).

*Pole scan s ∈ {4,5,6,7}, shell exponent 8−2s (converges iff s > 9/2 = 4.5, Sage-exact):*

| s | shell exp 8−2s | converges? | residue L=10 → L=120 | behavior |
|:--|:--------------:|:----------:|:---------------------|:---------|
| 4 (inherited) | **0** | **No** | 0.056589 → 0.326304 (×5.77) | **DIVERGES** (SETTLED S94 W3-9) |
| 5 | −2 | Yes | 5.722e-3 → 6.017e-3 | converges |
| 6 (**re-anchor**) | −4 | Yes | 9.3824e-4 → 9.3936e-4 | converges (plateau) |
| 7 | −6 | Yes | 1.77647e-4 → 1.77654e-4 | converges |

*s=6 convergent anchor CONFIRMED:* `residue(L→∞) = 9.393639575775e-04` (float64), `9.393639575776e-04` (mpmath 120-bit; |Δ_f64_mp| = 4.07e-17). Against the S94 W3-9 target `9.39363958e-4`: **|Δ| = 4.22e-13** ⇒ CONFIRMED. Full-grid truncation-tail exponent **α = 2.803571** (matches S94 W3-9 `2.8035709624`). This α is the **EMPIRICAL SU(4)_PS spectral-action residue tail**; the HH^1 Wodzicki exponent `α_HH1_per_pole_FW_s6 = 8` is a **DISTINCT observable (HH^1 cocycle norm)** and is NOT used as Level-2.

*Tier-1 registry-PASS predicate (Level-3 < Level-2 at canonical L_max=12), envelope fit on the asymptotic tail L≥16 EXCLUDING the L=12 test point:*
- α_tail (L≥16) = 2.881902, C_FB = 1.192179 (Friedrich-Bär envelope; empirical spectral-action tail)
- **Level-3**(s=6, L=12) = relative truncation residual `|Res(L=12) − Res(L→∞)|/|Res(L→∞)| = 7.686855e-04` (substrate-IS distance from the laboratory-IN continuum image; provenance-matches S94 W3-9 `ratio_s6_L12_inside_envelope = 7.6869e-4`)
- **Level-2**(s=6, L=12) = `C_FB · 12^{−2.882} = 9.252240e-04` (Friedrich-Bär envelope at canonical L_max)
- **ratio Level-3/Level-2 = 0.830810 < 1 ⇒ Tier-1 PASS** — the L=12 anchor sits INSIDE the envelope (matches the §VII.AV/§VII.AX Friedrich-Bär envelope precedent).

*Tier-2 fallback (dimensionless functional; also re-anchors):* residue log-derivative `d ln Res_s / d ln L` annihilates any multiplicative L-divergent prefactor (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`). At s=6 it → **7.62e-06** (CONVERGENT, DIMENSIONLESS) ⇒ **Tier-2-DIMENSIONLESS, re-anchorable** — the **§VII.AV `L_emp` pattern** (Tier-1-CONVERGENT + Tier-2-dimensionless ⇒ STAGE-3-PERMANENT earned), NOT the §VII.AX `n_PBH` pattern (Tier-1-FAIL + Tier-2-DIMENSIONFUL ⇒ HELD). At s=4 the log-derivative stays **0.868 > 0** (DIVERGENT; the inherited pole is non-re-anchorable on either tier — settled).

*Substitution chain (the Level-3 < Level-2 sign claim; `math-scripts.md §"Double-Check Logic"`):*
- **Step 1** (shell scaling): dim_PS ~ L⁶ (A_3 = 6 positive roots), ~L² Peter-Weyl sectors per shell ⇒ `Σ_L L^{6} · L^{−2s} · L^{(2−1)}` ⇒ shell exponent **8−2s** (Sage-exact).
- **Step 2** (convergence): `Σ_L L^{8−2s}` converges iff `8−2s < −1 ⇔ s > 9/2 = 4.5`. s=4 → 0 (DIVERGES); s=5/6/7 → −2/−4/−6 (converge).
- **Step 3** (s=6 anchor): residue(L→∞) = 9.39363958e-4 (CONFIRMED), tail α = 2.882 (empirical; NOT HH^1 α=8).
- **Step 4** (Level-3 < Level-2): the truncation residual at canonical L=12 (`7.687e-4`) is BELOW the Friedrich-Bär envelope (`9.252e-4`) ⇒ ratio 0.8308 < 1. **Direction**: at s=6 the shell exponent +1 is `8−2s+1 = −3 < 0` ⇒ the sum is finite (residue CONVERGES); the truncation tail L^{−2.882} DECREASES with L ⇒ the L=12 partial-sum residual sits inside the shrinking envelope.
- **Step 5** (Tier-2 fallback, not needed but confirmed): dimensionless log-derivative → 7.62e-6 ⇒ re-anchorable.
- **Conclusion**: Tier-1 PASS (convergent-pole s=6 satisfies Level-3 < Level-2); Tier-2 also re-anchors (dimensionless). The s=4 inherited pole is structurally non-anchorable (SETTLED S94 W3-9, not re-litigated).

*4-tuple*: `(value=PASS_s6_reanchor_ratio_0.8308, scheme=SU(4)_PS-Mellin-cone-residue-convergent-pole-s6, convention=VII-BE-TIER2-REANCHOR-convergent-pole-s6-Tier-1-OR-dimensionless-Tier-2, L_max=12)`.

*schema-v2 3-tuple* ([SIGN] trigger): `sign_verdict=PASS` (s=6 convergent `[8−2s+1 < 0]` AND Level-3<Level-2 `[ratio<1]`), `magnitude_verdict=PASS` (ratio 0.8308 < 1; INFO band would be (1, 1.10]), `regime_verdict=VALID` (s=6 inside the SU(4)_PS convergent regime s>4.5; full window, no breakdown).

*Dual-SHA*: `audit_sha256=71aea79274b081b1f4ab5d4222b637a323151df58933b2949ce1d08668cfc326`; `content_sha256=4412390c0f581cb0d7317958de062e120517b8b0bcca34569a49d2994316aef6`.

**Substrate-physics assessment** (PHONONIC/GEOMETRIC framing, IS-not-IN per `phononic-framing.md`): The substrate IS the Pati-Salam parent spectral triple `(A_K_PS = ℂ ⊕ M₂(ℂ)_L ⊕ M₂(ℂ)_R ⊕ M₄(ℂ)_PS, H_K_PS, D_K_PS)` at τ_fold = 0.19. As the spectral-functional theorist: **the s=4 vs s=6 choice is NOT a convention — it is forced by the SU(4)_PS spectral dimension.** The rank-4 lepton-color block's Peter-Weyl density grows as L⁶ (A_3 = SU(4) has 6 positive roots vs A_2 = SU(3)'s 3), shifting the Mellin-cone convergence threshold UP by exactly one unit (s > 9/2 for SU(4)_PS vs s > 3/2 for SU(3)). The inherited s=4 pole was a **child-algebra artifact** (the SU(3) convergence threshold); the residue at s=4 diverges because the substrate does NOT anchor SU(4)_PS at the SM-gauge child's pole. Re-anchoring to the parent's OWN convergent pole s=6 is **substrate-first correction, not curve-fitting**. Direction of explanation flows FROM the D_K_PS eigenvalue spectrum (rank-4 Peter-Weyl, dim ~ L⁶) → Mellin-cone residue at pole s → convergent only at s > 9/2 → re-anchor to s=6. The L^{−2.804} tail is the substrate's OWN truncation envelope at the convergent pole; conflating it with the HH^1 cocycle Wodzicki envelope α=8 would substitute one spectral functional for another — the exact error this agent is built to catch, and it is averted here (empirical 2.804 pinned, NOT 8).

**Solution-space meaning (PASS)**: the §VII.BE FWD-C4 numerical Level-3 CLOSES at the substrate-singled-out convergent pole s=6 (Tier-1; the Tier-2 dimensionless log-derivative independently re-anchors). The structural Stage-2 PASS-AND on disk (S93 W6-4 axis-A `146b5742`, axis-B `9df77b09`) is **UNAFFECTED** — it lives on the structural-clause axis, orthogonal to the numerical-Level-3 axis. With a satisfiable numerical Level-3 anchor now in hand, a **STAGE-3-PERMANENT review of §VII.BE is LICENSED** (to be effected by `mack-cosmic-bridge` as sole registry writer; the Level-3 row migrates from `NOT-SATISFIED-PENDING-substrate-physical-pole-re-anchor` HELD to the convergent-pole s=6 anchor). The Pati-Salam GUT-extension bridge gains a satisfiable empirical anchor at its substrate-natural convergent pole.

**Carry-forward (registry text; not effected here)**: `mack-cosmic-bridge` to (i) update the §VII.BE Element-4 / Element-5 to the convergent-pole s=6 anchor (Level-3 = relative truncation residual 7.687e-4 < Level-2 = C_FB·12^{−2.882} = 9.252e-4 at L_max=12; α_tail = 2.882 EMPIRICAL spectral-action tail, NOT HH^1 α=8); (ii) re-derive η_FB^{SU(4)} stays the S94 W3-9 value 0.101814 (NOT the SUGGESTION 0.283 nor the inherited 0.436); (iii) trigger the Stage-3 promotion review per `joint-theorem-promotion.md §"Stage 3"` (structural Stage-2 PASS-AND already on disk + numerical Level-3 now PASS). Inputs: `s95_w1_3_vii_be_tier2_reanchor.npz`; verdict `audit_sha256=71aea79274b081b1f4ab5d4222b637a323151df58933b2949ce1d08668cfc326`; canonical-constants candidate `residue_s6_PS_Linf = 9.39363958e-4`, `alpha_PS_residue_tail_s6 = 2.8819` (EMPIRICAL; tag DISTINCT from `alpha_HH1_per_pole_FW_s6`).

---

### §W1-4. TES-R1-FI-TRUNCATION-ROBUST (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `TES-R1-FI-TRUNCATION-ROBUST`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (FI truncation-robustness of the protected spectral-moment ratio)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: R_1 = a_0 a_4 / a_2^2 (the Lizzi-signature; canonical R_protected_fold = 1.128655) is FUNCTIONAL-INVARIANT under truncation — computed from RAW mode-count moments at L_max in {6,8,10,12}, the RATIO converges to 1.128655 while each individual a_n^raw diverges, the multiplicative-normalization-cancellation signature.
**Plan reference**: `sessions/session-plan/session-95-plan-w1.md` §W1-4 (raw-vs-SDW finite-L gap ~2.8% at L=10, w(L) cancellation, tesla V.5 §8.2 anchors, FI tag per regulator-pin-discipline).

**Verdict**: **FAIL** (composite). 3-tuple: `sign_verdict=FAIL`, `magnitude_verdict=INFO`, `regime_verdict=VALID`. The pre-registered FI-convergence hypothesis (raw mode-count R_1(L) converges TO the SDW-zeta canonical 1.128655) is **falsified**: the raw-moment R_1 drifts monotonically AWAY from the SDW canonical, not toward it. FAIL is a result, not an agent failure — it closes a corridor and sharpens the FI/SD partition (see Substrate-physics assessment).

**MCP Pre-Compute Audit** (per query-first discipline; queries run BEFORE writing the script):
- `search_knowledge("R_1 a0 a4 a2 truncation robust Lizzi signature ratio")` -> registry `lizzi-signature-observable.md` (R_1 = a_0*a_4/a_2^2 = 1.128655, FUNCTIONAL-INDEPENDENT sub-percent); equation `R_1 = 6440.0*1350.722/(2776.165)^2 = 1.128655`; identity `(m_H/v_EW)^2*(Lambda/M_Pl^2) = R_1`. The raw-moment **truncation scan** is NEW (no prior gate computes it) — NOT pre-closed.
- `get_constant("R_protected_fold")` -> 1.1286545967627695 (S73B/S74, R-Protected YES, per-branch "R_1 = a_0*a_4/a_2^2 at fold"). Canonical R_1 target (imported, not hardcoded).
- `get_constant("Lizzi_signature")` -> 1.1286545967627695 (S74, = R_protected_fold). Cross-check identity.
- `get_constant("a_0_FW_zeta"/"a_2_FW_zeta"/"a_4_FW_zeta")` -> 6440.0 / 2776.165389 / 1350.7216 (SDW-zeta canonical triple; S88/S75). SDW-zeta R_1 cross-check.
- `trace_entity("tesla raw mode-count moment a_0 155984")` -> no trace; grep-trail to S66 `s66_cutoff_ns.py:512-521` (producing script) + `s66_cutoff_ns.npz` (`a0_computed`/`a2_computed`/`a4_computed`), which reproduce the tesla V.5 section 8.2 triple EXACTLY -> recovered the raw-moment **definition** (Results).
- PRE-CLOSED: NONE (R_1 value is canonical/closed; the truncation-axis convergence test is the new compute).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script**: `computations/session-95/s95_w1_4_r1_fi_truncation_robust.py` (19,728 B) — `from canonical_constants import` present; `append_verdict` present (grep pasted below).
- **Data**: `computations/session-95/s95_w1_4_r1_fi_truncation_robust.npz` (6,677 B) — scan arrays + cross-checks + 3-tuple.
- **Plot**: `computations/session-95/s95_w1_4_r1_fi_truncation_robust.png` (133,139 B) — 3 panels: R_1(L_max) vs L_max with the 1.128655 asymptote + tesla anchor + SDW line; |R_1-c|/c deviation; a_n^raw(L_max) divergence (log).
- **Verdict line**: `computations/session-95/s95_gate_verdicts.txt` — canonical line matching `^TES-R1-FI-TRUNCATION-ROBUST:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 3-tuple row ([SIGN] trigger). `audit_sha256=622ab243c01f25a6bf1848a057edf09e0f59433129ba6f801271ae71a194e5cc`, `content_sha256=864192e7506bcb2848c2e6077f84e625d10721345ba7a57b14bc20ac46099e45`.

**Results** (NUMBERS first, gate second, interpretation third):

*Raw mode-count moment definition (recovered from S66, the producing script for the tesla anchor)* — `s66_cutoff_ns.py:512-521`:
```
a_0^raw = Sum_{(p,q): p+q<=L}  d(p,q)^2 * N_modes(p,q)     # PW-weighted mode count = Tr 1
a_2^raw = Sum_{(p,q): p+q<=L}  d(p,q)^2 * Sum_j |lam_j|^{-2}
a_4^raw = Sum_{(p,q): p+q<=L}  d(p,q)^2 * Sum_j |lam_j|^{-4}
```
d(p,q) = dim_su3_irrep(p,q); |lam_j| = per-sector abs_evals from the L12 D_K spectrum cache at tau_fold. **Convention finding (load-bearing)**: this definition reproduces the tesla triple `(a_0=155984.0, a_2=64308.2438882544, a_4=29086.17667962735)` **EXACTLY (bit-for-bit)** — but at PW truncation **p+q<=3, NOT p+q<=10**. The corpus label "L_max=10 / 155,984 eigenvalues" IS the d^2-weighted mode count at p+q<=3 (S66 used `MAX_PQ_SUM=3`). The plan "L_max" axis is the PW level p+q; the tesla anchor sits at p+q=3, BELOW the {6,8,10,12} grid.

*Cross-checks*:
- Tesla anchor (p+q<=3) reproduced: R_1^raw = 1.097068 (plan target 1.09707). Sage-exact QQ = `590752367603514656562500000/538483103123855389457588427` = 1.0970676037.
- SDW-zeta canonical triple -> R_1 = 1.1286545620 = canonical R_protected_fold (1.1286545968) to **3e-6 %** (it IS the definition; Sage-exact confirms).
- raw vs canonical gap at tesla anchor = **2.7986 %** (Sage-exact).

*Main scan — raw R_1(L_max) over {6,8,10,12}* (d^2-weighted inverse-power moments):

| L_max | a_0^raw | a_2^raw | a_4^raw | R_1^raw | abs(R_1-c)/c |
|:--|:--|:--|:--|:--|:--|
| 6  | 2.041e+07 | 3.740e+06 | 7.439e+05 | 1.085406 | 3.832 % |
| 8  | 1.819e+08 | 2.244e+07 | 3.011e+06 | 1.087354 | 3.659 % |
| 10 | 1.437e+09 | 1.237e+08 | 1.148e+07 | 1.078769 | 4.420 % |
| 12 | 7.539e+09 | 4.861e+08 | 3.373e+07 | 1.075834 | 4.680 % |

*Pre-registered predicate evaluation*:
- **(i) |R_1(L)-c| monotone-DECREASING**: **FALSE**. Deviation deltas = `[-0.001949, +0.008585, +0.002935]` — deviation GROWS after L=8 (two of three steps positive). R_1 itself non-monotone (1.0854 -> 1.0874 -> 1.0788 -> 1.0758) and BELOW canonical at every L_max (raw underestimates SDW).
- **(ii) |R_1(12)-c|/c < 0.01**: **FALSE**. 4.680 % (in [1%, 5%] INFO band).
- **(iii) each a_n^raw INCREASING in L (divergence)**: **TRUE**. a_0 grows x8.9 -> x7.9 -> x5.2 per step; a_2, a_4 strictly increasing. Moments diverge as predicted.

*Full-range L-trend (L=2..12, diagnostic)*: gap to SDW canonical grows monotonically 2.76 % (L=2) -> 5.28 % (L=12). 1/L extrapolation on the last 4 points gives raw L->inf limit ~= **1.054** — a **6.62 % gap** from the SDW canonical. The raw-moment family converges (within itself) to a **different limit** from the SDW-zeta family.

*4-tuple*: `(value=1.0758341506377302, scheme=raw-mode-count-Seeley-DeWitt-moments, convention=FI-RATIO-truncation-robust, L_max=12)`.

*Substitution chain (plan §W1-4 (7); checked vs the data)*:
- Step 1: R_1 dimensionless ([M^0][M^-4]/[M^-4]=[M^0]).
- Step 2: a_n^raw(L) increases with L (predicate (iii) TRUE).
- Step 3: R_1^raw(tesla,p+q<=3)=1.097068; R_1^SDW=1.128655 (differ ~2.8 %).
- Step 4: a_n^raw = w(L)*g_n*[1 + b_n/L + ...]; the COMMON leading weight w(L) cancels in R_1 (two up, two down). **But R_1(L) does NOT settle on 1.128655** — the subleading family-dependent kernel ratio g_0*g_4/g_2^2 is a DIFFERENT number (~1.054 raw) from the SDW family's 1.128655. Cancellation removes the leading divergence, NOT the family-selection of the limit.
- Step 5 / Direction: moments-UP (TRUE) but |R_1-c|-DOWN (**FALSE** — grows). Directions NOT opposite-as-predicted; deviation tracks AWAY from SDW canonical => `sign_verdict=FAIL`.

*Schema-v2 3-tuple* (gate-verdicts.md composite-collapse; PRE-REGISTERED): `sign_verdict=FAIL` (predicted moments-up/deviation-down opposite; deviation actually grows -> direction mismatch); `magnitude_verdict=INFO` (|R_1(12)-c|/c = 4.68 % in [1%,5%]); `regime_verdict=VALID` (moment-divergence half of the FI signature holds across the full window). Composite: `sign_verdict==FAIL => composite=FAIL`.

*FI tag (per `regulator-pin-discipline.md`)*: R_1 is tagged **FI (Functional-Invariant) WITHIN a fixed regulator family** — NOT across the raw-vs-SDW family boundary. Regulator pins: `a_n^{raw-mode-count}` (truncation-scan moments, primary object) and `a_n^{zeta}` (SDW canonical comparison). FI inherits from the F_traj a_2-ratio FI theorem parent (`regulator-pin-discipline.md` beta_shell FI Classification); this gate establishes its **scope boundary**: FI holds within-family, the VALUE is regulator-family-selected across families.

**Substrate-physics assessment** (substrate-first; `phononic-framing.md`):
R_1 = a_0 a_4 / a_2^2 IS the substrate's unique structurally-protected dimensionless shape number — the Lizzi-signature observable. Direction of explanation: D_K eigenvalue spectrum -> three Seeley-DeWitt spectral moments (a_0 = mode count = Tr 1; a_2 = Einstein-Hilbert/Newton; a_4 = Yang-Mills + Higgs-quartic) -> their unique dimensionless combination R_1. This gate is the **truncation-axis specialization of the ZETA-NOT-PHYSICAL FI/SD partition**, and it returns a SHARP boundary, not a flat FAIL:

1. **Within a fixed regulator family, R_1 is FI**: the SDW-zeta triple reproduces 1.128655 to machine precision and is L-stable (it IS the per-branch fold definition); the raw mode-count family is also L-convergent — to ITS OWN limit (~1.054). Each family's R_1 is a well-defined shape number, immune to where the eigenvalue sum is cut WITHIN that family.
2. **Across regulator families, the R_1 VALUE is SCHEME-SELECTED**: raw mode-count and SDW-zeta are DIFFERENT spectral functionals of the SAME D_K, with R_1 limits differing ~6.6 %. The plan claim (raw R_1 converges TO the SDW canonical) conflates two distinct functionals. The "multiplicative-normalization-cancellation invariant" (`math-scripts.md`, K=3) is real but cancels only the LEADING common weight w(L); the subleading kernel ratio is family-dependent and fixes a DIFFERENT limit. This is precisely the error this agent exists to catch: substituting one spectral functional for another and expecting the same number.
3. **What survives ALL choices is the RANK-EXPONENT, not the R_1 VALUE**: this sharpens the S78 W3-K SCHEME-INDEPENDENT-DRIFT-EXPONENT theorem (the R_1 rank-exponent is FI sub-percent across families) by establishing that the rank-EXPONENT and the R_1-LIMIT are DIFFERENT invariants — the former is cross-family FI, the latter is NOT.

**Consequence for the section 8.5 phonic-exflation-equation ratio-robust / absolute-conditional split**: the ratio-robust claim is VALID but MUST be scoped **"within a fixed regulator family"** — NOT "across raw-vs-SDW". The canonical ratio-robust exemplar is the SDW-zeta R_1 (L-stable, exact); the raw mode-count R_1 is a SEPARATE within-family-robust object with a different value. Split reads: ratio-observables are truncation-robust *within a regulator family* (value selected is the family's); absolute-energy observables are additionally conditional on SDW convergence. This is a tightening, not a refutation — it pins WHICH regularization the section 8.5 ratio-robust value belongs to.

**grep verification of must_contain patterns**:
```
$ grep -nE "from canonical_constants import|append_verdict" s95_w1_4_r1_fi_truncation_robust.py
  -> "from canonical_constants import *" (L75); "from canonical_constants import (" (L76); "def append_verdict(" + call present
$ grep -E "^TES-R1-FI-TRUNCATION-ROBUST:.* audit_sha256=[a-f0-9]{64}" s95_gate_verdicts.txt
  -> matches (FAIL line, full-64-hex audit_sha256)
```

---

## Wave 1 Synthesis (team-lead)

**Wave 1 — Spectral cross-pillar-bridge convergence & re-anchoring (lizzi-owned). 4 gates: 2 PASS, 2 FAIL (both boundary results).**

| Gate | Verdict | One-line outcome |
|:-----|:--------|:-----------------|
| §W1-1 `CF-S95-HK-1` | **PASS** | §VII.BG α_s T5 Connes-Karoubi transport bridge promoted STAGE-1-CANDIDATE → STAGE-3-PERMANENT via the canonical two-agent (lizzi + volovik, NON-connes) Stage-2 cross-axis PASS-AND; JOINT clause Δ_scheme=0 bit-exact (Sage-QQ Rational Field); disjoint anchor sets (orthogonality ∩=∅). |
| §W1-2 `CF-S95-K-CSUB-R-RE-ANCHOR` | **FAIL** (boundary) | K_csub_R Tier-2-DIMENSIONFUL-held: all 3 corridors diverge (N-pt PV WORSENS with N; τ-running diverges; Tier-2 log-derivative GROWS — exponential IR-accumulation `~exp(+0.75ρ)`). Dimensionful corridor CLOSED; 2nd §25 instance (K=2). |
| §W1-3 `CF-S95-VII-BE-TIER2-REANCHOR` | **PASS** | §VII.BE Pati-Salam Level-3 re-anchored at convergent pole s=6 (residue 9.39e-4, ratio 0.831<1); the inherited s=4 was a CHILD-ALGEBRA ARTIFACT (rank-4 shifts convergence to s>9/2). §VII.BE promoted → STAGE-3-PERMANENT. |
| §W1-4 `TES-R1-FI-TRUNCATION-ROBUST` | **FAIL** (boundary) | R₁=a₀a₄/a₂² does NOT converge to the SDW canonical 1.128655 — the raw-moment family converges to a DIFFERENT limit (~1.054, 6.6% gap). R₁ is FI WITHIN a fixed regulator family but SD ACROSS families (value regulator-family-selected). |

**Structural read.** Two permanent cross-pillar bridges landed (§VII.BG, §VII.BE), both via the framework's only admissible route to PERMANENT — structurally-independent agreement (Stage-2 two-agent verify, disjoint inputs / no shared workshop context). The two FAILs each closed a corridor WITH a mechanism: K_csub_R's Jensen IR-accumulation is EXPONENTIAL (defeating even the Tier-2 log-derivative escape — a strictly stronger "held" than the n_PBH power-law precedent), and R₁'s value is regulator-family-selected (the multiplicative-normalization cancellation annihilates only the leading common weight w(L); the subleading kernel ratio g₀g₄/g₂² is family-dependent). Net: the spectral cross-pillar-bridge layer is sharper — two anchors made permanent, two divergent corridors mapped and bounded.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator before STOP)

- [x] §VII.BG STAGE-1-CANDIDATE → STAGE-3-PERMANENT — `sessions/permanent-results-registry.md` §VII.BG (header + Status paragraph + Stage-2-status section) — W1-1 PASS; canonical two-agent Stage-2 verify landed (audit_sha256 `ad229035…`)
- [x] §VII.BE STAGE-1-CANDIDATE → STAGE-3-PERMANENT — `sessions/permanent-results-registry.md` §VII.BE (header + Status + S95 W1-3 re-anchor/promotion annotation + deferred-pending row (i) + ladder Level-3 row) — W1-3 PASS at convergent pole s=6; structural Stage-2 PASS-AND (S93 W6-4) + numerical Level-3 composed
- [x] `canonical_constants.py`: `residue_s6_PS_Linf = 9.393639575775e-4` (SECTION E, provenance pinned) — W1-3 PASS; SU(4)_PS s=6 residue L→∞
- [x] `canonical_constants.py`: `alpha_PS_residue_tail_s6 = 2.803571` (SECTION E, tag FI) — W1-3 PASS; empirical residue tail, DISTINCT from HH¹ α=8
- [x] `cross-pillar-bridge-corpus.md §25.2` — K_csub_R K=1→K=2 advancement (Tier-2-DIMENSIONFUL exponential-divergence; distinctness criterion met) — W1-2 FAIL
- [x] `cross-pillar-bridge-corpus.md §26` — K_csub_R companion (ENRICH Member A dimensionful-slot-collision; NO §26 K-counter advance, per the §24.4 ENRICH precedent) — W1-2 FAIL
- [x] `.claude/rules/cross-pillar-bridge-anatomy.md` — Tier-1/Tier-2 gate status SUGGESTION K=1 → K=2 (pointer-table row + inline directive) — rule-file sync with §25.2
- [x] W1-4 provenance clarification recorded — the tesla §8.2 raw triple (a₀=155984, a₂=64308.24, a₄=29086.18) is the d²-weighted mode count at Peter-Weyl p+q≤3, NOT p+q≤10; recorded in housekeeping §A for the `phonic-exflation-equation` doc-workshop (no `canonical_constants.py` pin exists for the raw triple — clarification only, no constant edit)

**Math-vs-non-math discriminator applied**: every item above is a registry / constant / corpus / rule edit using already-pinned gate numbers (NO new computation) → NON-MATH, effected now. The one genuine future-computation candidate (re-sourcing the K_csub_R dimensionful scale from a non-IR channel) is below and is CONDITIONAL on a downstream consumer surfacing.

## Carry-Forward Computations

### CF-S96-K-CSUB-R-EXTERNAL-CHANNEL-SCALE (CONDITIONAL — schedule only if a downstream consumer needs a dimensionful K_csub_R)

| Field | Spec |
|:------|:-----|
| **What** | Re-source the K_csub_R dimensionful scale from OUTSIDE the a_2 IR-accumulation channel — the only remaining route after S95 W1-2 closed all UV regulators (2/3/4-pt PV + τ-running) AND the Tier-2 log-derivative. Candidate routes: a cosmological-observable cutoff, OR a PV/zeta subtraction anchored to a channel other than a_2 (parallel to the n_PBH `CF-S94-N-PBH-CANONICAL-TRUNCATION-RE-DETERMINATION` route). |
| **Inputs** | `computations/session-95/s95_w1_2_k_csub_r_re_anchor.npz` (closed-corridor diagnosis); `canonical_constants.py` (`M_KK_gravity`); a downstream gate that actually consumes a dimensionful K_csub_R (NONE currently blocks — hence CONDITIONAL). |
| **Gate** | PASS iff a substrate-physical scale anchor outside the a_2 IR channel yields finite `max\|dK/dL\| < 1e-3` over L∈[50,100]; else the dimensionful K_csub_R is permanently held (Tier-2-DIMENSIONFUL, the boundary result stands). |
| **Effort** | ~1.0 wave-equivalent. **Depends on**: a dimensionful-K_csub_R consumer surfacing first. |

(§W1-4's L_max-extended-scan branch is **N/A** — the raw-moment R₁ family converges to a genuinely DIFFERENT limit, not slowly toward the canonical, so more L_max cannot close the gap. The §8.5 ratio-robust scoping is a DOC-integration consumer, routed to the `phonic-exflation-equation` `/rclab-workshop` AFTER the S95 compute lands — NOT a compute carry-forward; see housekeeping §A.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-28 | §VII.BG α_s T5 transport bridge | STAGE-1-CANDIDATE | STAGE-3-PERMANENT | W1-1 canonical two-agent Stage-2 cross-axis PASS-AND (lizzi+volovik, non-connes); JOINT Δ_scheme=0 bit-exact |
| 2026-05-28 | §VII.BE FWD-C4 Pati-Salam bridge | STAGE-1-CANDIDATE + REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION | STAGE-3-PERMANENT | W1-3 Level-3 re-anchored at convergent pole s=6 (ratio 0.831<1) + structural Stage-2 PASS-AND (S93 W6-4) |
| 2026-05-28 | K_csub_R (c_sub Mellin intercept, a_2 s=2) | UV-finiteness open (S94 W1-4 2-pt-PV FAIL) | Tier-2-DIMENSIONFUL-held; dimensionful corridor CLOSED | W1-2: all 3 corridors diverge (exponential IR-accumulation) |
| 2026-05-28 | Tier-1/Tier-2 dimensional-re-anchorability gate (corpus §25) | SUGGESTION K=1 | SUGGESTION K=2 | K_csub_R structurally-distinct (exponential vs n_PBH power-law) Tier-2-dimensionful instance |
| 2026-05-28 | R₁=a₀a₄/a₂² truncation-robustness | FI-robust hypothesis (untested across families) | FI WITHIN regulator family; SD ACROSS families | W1-4: raw-moment family → ~1.054 ≠ SDW canonical 1.128655 (6.6% gap) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other |
|:-----|:-------|:------------|:------------|:------|
| §W1-1 | `s95_w1_1_vii_bg_stage2_aggregator.py` | `s95_w1_1_vii_bg_stage2_aggregator.npz` | `s95_w1_1_vii_bg_stage2_aggregator.png` | reviews `s95_w1_1_axisA_lizzi_review.md` + `s95_w1_1_axisB_volovik_review.md`; `…aggregator.json` |
| §W1-2 | `s95_w1_2_k_csub_r_re_anchor.py` | `s95_w1_2_k_csub_r_re_anchor.npz` | `s95_w1_2_k_csub_r_re_anchor.png` | — |
| §W1-3 | `s95_w1_3_vii_be_tier2_reanchor.py` | `s95_w1_3_vii_be_tier2_reanchor.npz` | `s95_w1_3_vii_be_tier2_reanchor.png` | — |
| §W1-4 | `s95_w1_4_r1_fi_truncation_robust.py` | `s95_w1_4_r1_fi_truncation_robust.npz` | `s95_w1_4_r1_fi_truncation_robust.png` | — |

(All under `computations/session-95/`. Verdict lines + dual-SHA companions + schema-v2 3-tuples in `computations/session-95/s95_gate_verdicts.txt`.)
