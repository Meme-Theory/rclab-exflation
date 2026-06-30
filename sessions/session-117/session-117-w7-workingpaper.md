# Session 117 Wave 7 — w0 transport-degree & categorical-wall (Results Working Paper)

**Session**: 117 | **Wave**: 7 | **Plan**: session-117-plan-w7.md | **Theme**: substrate-physics status of the dark-energy EoS `w0 = −0.918` (`w0_FW`, S58 four-fold-lock = Volovik vacuum partition + effacement Γ_eff = 0.99970) on three orthogonal axes left open by the S116 W9 cluster + the S-7/W-5 adversarial-review campaign — (7-1) the BZ→pivot transport degree `deg(T_{BZ→pivot})` (favored **deg=0 T2-VACUOUS scalar** ⇒ substrate w0 = pivot w0 = −0.918; the W9 → −1.340827 gap PROXY-ARTIFACT-typed); (7-2) the categorical-wall grade [w0 ∉ Tr f(D_K)] q-theory-model-grade → THEOREM-grade test; (7-3, OPTIONAL) the branch-iv L16 value-neutral L_max diagnostic. All three gates are `gate_type: compute` and close via a verdict line in `computations/session-117/s117_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md`). Substrate-first framing (`phononic-framing.md`): the fabric IS both its D_K vibrational spectrum AND its q-field vacuum partition; w0 = −0.918 is the *thermodynamic* facet; all three gates flow FROM the D_K spectrum / q-field partition at τ_fold = 0.190 TOWARD the emergent DESI w(z) image.

## Gate Sections

### §W7-1. CF-S117-W0-TRANSPORT-DEGREE (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-W0-TRANSPORT-DEGREE`
**Trigger**: `[SIGN]` (directional pre-registration on |deg| vs deg_tol; [VERIFY] degree-extraction + 3-scheme Δ_scheme spread carried in method)
**Classification**: **GEOMETRIC** (Level-1 single-τ-slice substrate-IS; structural property of the spectral-action BZ→pivot bridge map on the D_K spectrum at τ_fold = 0.190)
**Agent**: `volovik-superfluid-universe-theorist` (mack co-reviews the deg-conditional DR3 σ-distance consequence)
**Hypothesis**: On the fixed-scale (Λ_Z / M_KK) de-λ_max'd branch-iv representative, w0's transport degree `deg(T_{BZ→pivot})` extracts to **0** (T2-VACUOUS scalar: single-pole s=s'=3 ⇒ Wodzicki −2(s−s')=0 AND Δ_scheme→machine-zero across {APS-1975, Cheeger-Simons, Bismut-Cheeger}) ⇒ substrate w0 = pivot w0 = −0.918 and the W9 → −1.340827 gap is PROXY-ARTIFACT-typed; a CLEAN even nonzero degree instead flips w0 to a substrate-natural NON-SCALAR §23 K=3 candidate (**dual-outcome: Track-SCALAR favored, prior 0.7 / Track-NONSCALAR INFO, prior 0.3**).
**Plan reference**: `sessions/session-plan/session-117-plan-w7.md` §W7-1 (two-stage method: STAGE-1 fixed-scale de-λ_max'd representative [subsumes the former `-ANCHOR-FIDELITY` CF]; STAGE-2 §23 degree extraction; machinery pin, 6-step substitution chain, dual_prior + 4-way composite-precedence rubric).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
- (1) `computations/session-117/s117_w0_transport_degree.py` (40102 B) — `grep` hits: `from canonical_constants import` (L104), `print_verdict_payload` (def L389; calls L519, L651). PASS.
- (2) `computations/session-117/s117_w0_transport_degree.npz` (18173 B) — {running / fixed-edge / no-edge} ρ_B + w0^CAC trajectories over L∈{10..15}, `mean_Z`, `lam_max`, extracted `deg_T_w0`, `delta_scheme` over {APS,CS,BC}, gap decomposition. PASS.
- (3) `computations/session-117/s117_w0_transport_degree.png` (160281 B) — 3-panel: three-normalization w0^CAC(L); mean_Z-frozen vs λ_max-running (twin axes); deg discriminator bar (w0=0 SCALAR vs sibling +2 NON-SCALAR). PASS.
- (4) verdict line in `computations/session-117/s117_gate_verdicts.txt` matches `^CF-S117-W0-TRANSPORT-DEGREE:.* audit_sha256=[a-f0-9]{64}` (audit_sha256=`bf2698789ec47216…`) WITH the dual-SHA companion row + the schema-v2 `# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` 3-tuple row + the pre-declared `# composite-precedence: plan session-117-plan-w7.md section-W7-1 …` row. PASS.
- (5) this WP section satisfies `**Status**:.*COMPLETED`, `**Verdict**:.*(PASS|FAIL|INFO)`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**`. PASS.

**MCP Pre-Compute Audit**:
- `get_constant("w0_FW")` → −0.918 (S58 four-fold-lock, Gate:None, Superseded:False) — the transport INPUT, confirmed.
- `get_constant("deg_T_BZ_pivot")` → 2.0 (S110-CF-CV6B-DS-M4) — the deg=+2 NON-SCALAR amplitude/square sibling, the contrast anchor, confirmed.
- `get_constant("alpha_s_substrate_distance_1")` → −0.08587279 (S92-AH-TR-1) — the other deg=+2 NON-SCALAR sibling reference, confirmed.
- `search_knowledge("w0 transport degree BZ pivot deg T2-VACUOUS scalar §23")` → surfaced the §23 theorem `O^pivot = O^substrate IFF deg(T_{BZ→pivot}) is T2-VACUOUS (scalar)` (Phononic-C-Causality.md + cross-pillar-bridge-corpus.md) and S93-W7-1 (alpha_s deg_T=2.0 NON-SCALAR, delta_scheme=0.00). w0's degree was UNEVALUATED — NOT pre-closed. Gate proceeds.
- `search_knowledge("branch-iv Zubarev moment lambda_max running edge w0 -1.340827 proxy artifact")` → S116-W9-GTBUILDER-L15 (the ρ_B(L) trajectory I de-λ_max), S101-W0-BRANCH-IV-EVALUATOR INFO (derivation-inadmissible). Confirms the W9 drift lineage.

**Verdict**: **PASS — Track-SCALAR (deg = 0, T2-VACUOUS scalar).** `deg(T_{BZ→pivot})[w0] = 0` (|deg| = 0 < deg_tol 0.05) AND `Δ_scheme = 0 M_KK²` (< 1e-3) across {APS-1975, Cheeger-Simons, Bismut-Cheeger}. Composite PASS (sign=PASS, magnitude=PASS, regime=VALID); the plan §W7-1 composite-precedence and the generic 3-tuple collapse agree here. ⇒ substrate w0 = pivot w0 = **−0.918**; the W9 → −1.340827 gap is CONFIRMED PROXY-ARTIFACT (the running λ_max edge is NOT in the admissible {Wodzicki, HKR} morphism sector); **NO §23 K-counter advance** (a deg=0 confirmation is not the factorization-EXTRACTED NON-SCALAR degree the K=3 slot reserves for r/α_t). audit_sha256=`bf2698789ec472167b521a6eb782b5eed66857156474c83337548bcf5cb2af10`, content_sha256=`2f8ce72f855dde3e216a09abd222f490d6ede2e72103fe9bbb926e4c21929d11`.

**Results**:

**STAGE-1 — the de-λ_max'd representative (subsumes the former `-ANCHOR-FIDELITY` CF).** Recomputed from the S106 cache (`sector_evals_L16`, complete p+q≤15; npz-internal audit_sha256 `5af2b7cd…` verified) via the S85 W0-7 Zubarev evaluator `rho_zubarev_from_sectors` (imported VERBATIM from s105). `ρ_B(13/14/15) = −0.656884/−0.677718/−0.696174` reproduce S116-W9-GTBUILDER-L15 to 6 sig figs (xcheck PASS). Three normalizations over L∈{10..15}:

| L | ρ_run | ⟨\|λ\|⟩_Z (mean_Z) | λ_max | w0_run (drifts) | w0_fix (flat) | w0_noedge (flat) |
|:--|:------|:------|:------|:------|:------|:------|
| 10 | −0.575207 | 1.983878 | 4.670218 | −0.918000 | −0.918000 | −0.918000 |
| 12 | −0.633204 | 1.987644 | 5.418937 | −0.975997 | −0.917194 | −0.916102 |
| 15 | −0.696174 | 1.987878 | 6.542827 | −1.038968 | −0.917143 | −0.915983 |

- **mean_Z FROZEN**: total drift 4.00e-3 (**0.20% rel**) over the full window; per-shell drift COLLAPSES 2.95e-3 → 6.24e-6 (Gaussian Zubarev weight `w_Z=exp(−λ²/Λ_Z²)`, Λ_Z=1, kills the high-L additions; smallest p+q=15 eigenvalue 4.216 ⇒ w_Z≈2e-8). **λ_max RUNS** linearly (Weyl, ∂λ_max/∂L ≈ 0.375).
- **The de-λ_max'ing is clean**: spread(running)=0.120968, spread(fixed-edge)=**8.57e-4**, spread(no-edge)=2.02e-3 — both de-λ_max'd variants are FLAT ≡ −0.918 (well inside the 0.025 CAC band); de-λ_max removes **99.29%** of the running drift. NOT ILL-POSED.
- **Gap-source decomposition** (exact first-order split of ρ_B(15)−ρ_B(10) = −0.120968): the **λ_max-running term = −0.121579 (100.51%)**; the mean_Z-drift term = +0.000611 (−0.51%, slightly OPPOSING). The W9 → −1.340827 asymptote (lockdown offset; −1.342793 W9-lineage offset) is sourced ≈100% by the running edge. (The plan's illustrative "100.08%" is reproduced as the same structural fact — running edge dominant, mean_Z negligible/opposing; my exact value at L=15 is 100.51%.)

**STAGE-2 — §23 transport-degree extraction.**
- **d_A(w0) = 0**: w0 = (a₀ zeroth Seeley-DeWitt moment)/(a₂ Einstein-Hilbert moment) dressed by Γ_eff — a ratio of energy densities, DIMENSIONLESS. So the §23.0(5) factorization B = (M_KK^{d_A} scale leg) ⊙ (dimensionless morphism) has a **TRIVIAL M_KK⁰ = 1 scale leg** (the 54.04-decade BZ→pivot unit conversion is ABSENT — it only enters through a d_A=1 leg). The whole degree lives in the EVEN morphism sector.
- **Single pole ⇒ deg = 0**: w0's branch-iv route is the a₂^{Mellin} SINGLE pole s=3 (poleconv-A-double, pole_in_s=3, curvature_grade_n=2); no square/power relation (the gap to −1.341 is **ADDITIVE** −0.918 − 0.422827, NOT a factor — contrast A_s = H̃² which doubles). Hence s′=s=3 ⇒ Wodzicki **deg = −2(s−s′) = −2(3−3) = 0** (Sage-QQ exact). `deg(T_{BZ→pivot})[w0] = 0+0 = 0`, T2-VACUOUS scalar, even-mesh.
- **Δ_scheme = 0 M_KK²** across {APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger}: a degree-0 morphism's secondary class is scheme-INDEPENDENT by Wodzicki uniqueness (the noncommutative residue is the unique trace on ΨDOs up to scalar); the homogeneity exponent is index-rigid (= 0 in every scheme), so the transport is the IDENTITY and O^pivot = −0.918 under all three. This is the §18 Conjunct-1 admissibility leg (mirrors S93-W7-1 `delta_scheme=0.00`, which held even for the NON-SCALAR α_s) — Δ_scheme=0 is the admissibility signature, the DEGREE value (0 vs +2) is the scalar discriminator.
- **CONTRAST**: the canonical NON-SCALAR sibling deg_T_BZ_pivot = +2 (S110-CF-CV6B: a dimensionful return-probability amplitude P∼σ^{−d/2} carries d/2 = +2; α_s/A_s=H̃² square). w0 sits on the deg=0 SCALAR end, the sibling on the deg=+2 NON-SCALAR end — discriminator gap |deg_sib|−|deg_w0| = 2.0. Both on the even-integer mesh.

**O^pivot(w0) = −0.918 = O^substrate**: the deg-0 identity transport gives substrate w0 = pivot w0. The 6-step substitution chain (Sage-verified): (1) d_A=0; (2) B = M_KK^{d_A}⊙morphism; (3) d_A=0 ⇒ scale leg M_KK⁰=1 (54.04-decade conversion absent); (4) morphism sector EVEN-degree, −2(s−s′); (5) single pole s=3, no square ⇒ s′=s ⇒ deg=0; (6) deg=0 ⇒ T2-VACUOUS scalar ⇒ T = identity ⇒ O^pivot = O^substrate = −0.918. ∎

**4-tuple**: (value=PASS-SCALAR/deg=0, scheme=section-23-Wodzicki-same-class + secondary-class-{APS-1975,Cheeger-Simons,Bismut-Cheeger}, convention=fixed-scale-de-lambda_max + CAC-DERIVED-OFFSET, L_max=15). **schema-v2 [SIGN] 3-tuple**: sign=PASS (the scalar prediction deg→0 CONFIRMED), magnitude=PASS (|deg−0|=0 ≤ 0.05), regime=VALID (de-λ_max clean over the full {10..15} window; Δ_scheme finite). **4-way composite-precedence map** (plan §W7-1): deg=0 clean ⇒ **composite PASS = PASS-SCALAR** [realized]; clean even nonzero ⇒ INFO = PASS-NONSCALAR-K3-CANDIDATE; indeterminate ⇒ INFO = INDETERMINATE; ill-posed ⇒ FAIL.

**dual_prior posterior re-allocation**: PASS-SCALAR ⇒ 0.9 to Track-A (Track-SCALAR; prior 0.7 → posterior ≈0.9), 0.1 to Track-B (Track-NONSCALAR; prior 0.3 → ≈0.1). **Downstream (Wave 7 → Wave 8 Decision Point)**: the ONE deg-CONDITIONAL element of the W-5 verdict (BD2) RESOLVES — the DR3 σ-distances freeze vs −0.918 DIRECTLY (2.13σ vs DESI DR2 −0.803±0.054; 3.28σ vs ΛCDM −1); route to mack to remove the "computed under provisional deg=0; pending CF-S117-W0-TRANSPORT-DEGREE" tag from the §7 falsifier-surface rows. NO §23 K-counter advance. The substrate value −0.918 was the transport INPUT, never its output.

**Substrate framing (substrate-first; `phononic-framing.md`)**: GEOMETRIC, Level-1 single-τ-slice substrate-IS (τ_fold=0.190). The fabric IS its D_K spectrum; w0 is read FORWARD as the a₀/a₂ Seeley-DeWitt moment-ratio dressed by the impedance-effacement Γ_eff. Direction of explanation: D_K eigenvalues → spectral-action moments a₀/a₂ → the DIMENSIONLESS EoS ratio w0 → (under the degree-0 §23 bridge map) the emergent DESI w(z) image, which COINCIDES with the substrate value. Container-thinking is rejected: the −1.340827 asymptote is NOT "the spectral action's real w0 at high L" — it is the L→∞ artifact of a RUNNING truncation-edge normalization (λ_max), a non-substrate quantity with no continuum limit, injected by the S85 Zubarev proxy DEFINITION. The substrate IS −0.918 (the q-field partition's effacement); the detector measures its emergent transport image, the same number. The branch-iv programme tried to RELOCATE the thermodynamic value into the eigenvalue spread; the spread answered the running-edge artifact, and the substrate REFUSED the relocation.

**dual-SHA**: audit_sha256=`bf2698789ec472167b521a6eb782b5eed66857156474c83337548bcf5cb2af10`, content_sha256=`2f8ce72f855dde3e216a09abd222f490d6ede2e72103fe9bbb926e4c21929d11`. **Artifacts**: `s117_w0_transport_degree.py` / `.npz` / `.png`.

---

### §W7-2. CF-S117-W0-CATEGORICAL-WALL-GRADE (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-W0-CATEGORICAL-WALL-GRADE`
**Trigger**: `[VERIFY-THEOREM]` (structural derivation: does the static/dynamical separation force ∂(EoS)/∂(a₀)=0 partition-independently; + the `[CHAIN]` linear-response substitution chain)
**Classification**: **PHONONIC** (the EoS-response side IS the q-field vacuum-partition effacement, DILUTION-CC two-fluid w=−1[vacuum]+w=0[GGE]) ⊕ GEOMETRIC (the static a₀ side = zeroth Seeley-DeWitt spectral moment)
**Agent**: `volovik-superfluid-universe-theorist` (connes co-reviews the a₀-as-Tr f(D_K) spectral-moment side)
**Hypothesis**: Wall (ii-a) [w0 ∉ Tr f(D_K): the EoS response is the q-field vacuum partition's effacement, not a static D_K spectral moment] upgrades from q-theory-model-grade to THEOREM-grade because the static-CC-magnitude (a₀^{ζ} zeroth Seeley-DeWitt moment, an ADDITIVE constant in the q-field free energy) vs dynamical-w(z)-response (a FIRST-derivative linear-response functional of the q-field 4-form) functional-type separation FORCES ∂(EoS response)/∂(a₀ static moment) = 0 independent of the specific Volovik partition (independent of the Γ_eff=0.99970 value). (**EXPECTED landing INFO — the VD2b two-grade reading: placement (ii-a) theorem-grade / value (ii-b) Γ_eff model-contingent.**)
**Plan reference**: `sessions/session-plan/session-117-plan-w7.md` §W7-2 (closed-form q-theory structural derivation + Sage-symbolic ∂w/∂a₀; N≥5 partition-family Γ(λ;θ) scan; 6-step substitution chain; OPERATOR-DISTINCTNESS guard).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
- (1) `computations/session-117/s117_w0_categorical_wall_grade.py` — PRESENT; `grep -E "from canonical_constants import|print_verdict_payload"` → `from canonical_constants import (` (imports `w0_FW`, `Gamma_effacement`, `Delta_BCS`) AND `def print_verdict_payload(...)` + its call. ✓
- (2) `computations/session-117/s117_w0_categorical_wall_grade.npz` — PRESENT (11,108 B): the arbitrary-`F_dyn` + 5-member partition-family ∂w/∂a₀ symbolic certificates, the symbolic-zero flags (`A_dyn_zero`, `C_eff_zero`, `selftune_zero`, `fam_dw_da0_allzero`), the partition-family Γ / `w_eff` / exact-rational arrays, `r_eff=409877/1377`, and the operator-distinctness expressions. ✓
- (3) `computations/session-117/s117_w0_categorical_wall_grade.png` — PRESENT (98,263 B; the plan marks it OPTIONAL): panel-1 partition-family `w_eff(Γ)` scan (value varies −0.870→−0.971 across 5 members, Γ_eff=0.99970 → −0.918 anchor); panel-2 `|∂w/∂a₀|` (dynamical `w_dyn` and effacement `w_eff` = 0 EXACT vs the static-ratio contrast NONZERO). ✓
- (4) verdict line in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-W0-CATEGORICAL-WALL-GRADE:.* audit_sha256=[a-f0-9]{64}` — PRESENT; `audit_sha256=e7fd9d20da481e39…504f8839`, `content_sha256=d67eb629342b2596…0d1e7d`; dual-SHA companion row PRESENT; `# regulator_pin=a_0^{zeta} …` companion row PRESENT; `# composite-precedence: [VERIFY-THEOREM] …` companion row PRESENT; NO schema-v2 [SIGN] 3-tuple row (correct — [VERIFY-THEOREM] trigger). ✓
- (5) this WP section satisfies the four must_contain markers — **Status**: COMPLETED / **Verdict**: INFO / **Output Artifacts** / **MCP Pre-Compute Audit**. ✓ (Verification by content presence, never line/byte counts.)

**MCP Pre-Compute Audit**:
- `search_knowledge("w0 categorical wall Tr f(D_K) spectral derivability VD2b two-grade")` → top hit `sessions/session-116/workshops/s116-w0-spectral-derivability.md` (the W-5 workshop, R3-FINAL-CLOSED); equations `eq_1256`/`eq_1257` `offset_A = w0_FW − ρ_B(10)`. NOT PRE-CLOSED: the gate is the W-5 forward compute (NEW from W-5, VD2b-sharpened) upgrading wall (ii-a) grade; no closure covers it.
- `get_constant("w0_FW")` → −0.918 (S58 four-fold-lock = Volovik vacuum partition + effacement Γ_eff=0.99970; **Gate: None**; Superseded: False) — the EoS VALUE (ii-b).
- `get_constant("Gamma_effacement")` → 0.99970 (S37 canonical impedance-transmission; (1−Γ)=3e-4) — the model-contingent VALUE = wall (ii-b).

**Verdict**: **INFO** — the pre-registered VD2b two-grade reading: placement (ii-a) is **THEOREM-grade** (`∂w/∂a₀ = 0` partition-independently) ∧ value (ii-b) Γ_eff=0.99970 is **model-contingent** ⇒ wall (ii) carries TWO grades, not one. `audit_sha256=e7fd9d20da481e39fd2e79169120ba91ba1f110bba79e5585493f142504f8839`; `content_sha256=d67eb629342b25963fdce5fc50f81256ad4fa11ffc528ab69a756cc38f0d1e7d`. Composite-collapse: [VERIFY-THEOREM] characterization gate — the `∂w/∂a₀=0` test PASSES (so (ii-a) IS theorem-grade), but the composite lands INFO because the deliverable is the *grade-structure* of wall (ii) and the value remains partition-contingent (a flat PASS would over-claim wall (ii) is entirely theorem-grade). This is the expected landing pre-registered in the hypothesis line.

**Results**:

**Headline.** The static-CC-MAGNITUDE / dynamical-EoS-RESPONSE functional-type separation FORCES `∂w/∂a₀ = 0` and the vanishing is **partition-independent** — confirmed (a) symbolically for the entire function-space of `F_dyn` (arbitrary dynamical free energy) and (b) numerically across all 5 effacement partition-family members. The categorical PLACEMENT of wall (ii-a) [w0 ∉ Tr f(D_K)] therefore upgrades to **THEOREM-grade**. The specific VALUE w0 = −0.918 stays Γ_eff-contingent (wall (ii-b), exactly what DESI tests), so wall (ii) is a **two-grade wall** (VD2b).

**The numbers (Sage-QQ-exact, sympy-reproduced; `s117_w0_categorical_wall_grade.py`).**

| Quantity | Result | Reading |
|:---------|:-------|:--------|
| `∂w_dyn/∂a₀` (arbitrary `F_dyn`) | `0` EXACT | (ii-a) theorem-grade, full function-space |
| `∂w_static/∂a₀` (static ratio) | `−q F_dyn'/(qF'−F)² ≠ 0` | the CONTRAST — static magnitude IS seen |
| `∂w_eff/∂a₀` (5 partition members) | `0` for ALL 5 | (ii-a) partition-independent |
| `w_eff(Γ)` over the family | {−0.870, −0.894, **−0.918**, −0.944, −0.971} | (ii-b) VALUE varies; spread 0.1007 |
| `w_eff(Γ_eff=0.99970)` | **−0.918000** = `w0_FW` | anchors the family to the canonical value |
| `r_eff` (QQ-exact) | `409877/1377` = 297.659405 | the GGE/vacuum deviation ratio at the anchor |
| equilibrium `ρ_vac\|_eq` | `0` ∀ a₀ | self-tuning absorbs a₀ (Paper 13 Eq. 12) |

**6-step substitution chain (substituted numbers; all Sage-QQ / sympy exact).**
- **Step 1** — `ε_Λ = a₀^{ζ}` (zeroth Seeley-DeWitt moment of `Tr f(D_K/Λ)`, n=0) enters the q-field free energy ADDITIVELY: `F(q) = F_dyn(q) + ε_Λ`. (regulator_pin `a_0^{ζ}`; DILUTION-CC a₀/a₂ two-fluid split.)
- **Step 2** — EoS response `w = p/ρ` with `p = −F`, `ρ = qF'−F` (Volovik q-theory thermodynamic identities, Paper 13 Eq. 4/9; Papers 13/23/25).
- **Step 3** — Substitute `F = F_dyn + ε_Λ` ⇒ `F' = F_dyn'` (the additive constant has ZERO q-derivative).
- **Step 4** — The DYNAMICAL response is taken about q_eq: `w(z) = δp/δρ = (dp/dq)/(dρ/dq) = −F'/(qF'') = −F_dyn'/(q F_dyn'')` — a ratio of q-DERIVATIVES.
- **Step 5** — `∂w/∂a₀ = ∂[−F_dyn'/(qF_dyn'')]/∂a₀ = 0` EXACT: the additive a₀ is annihilated by BOTH the response-derivative AND the δ-perturbation (`δε_Λ = 0`). CONTRAST: the static ratio `w_static = −F/(qF'−F)` keeps a₀ in numerator AND denominator, so `∂w_static/∂a₀ = −qF_dyn'/(qF'−F)² ≠ 0` — this is the static-magnitude sensitivity that makes the bare-CC problem hard, and precisely the functional type w0 is NOT.
- **Step 6** — Partition-independence: Step 5 used ONLY that ε_Λ is ADDITIVE in F and that w is a derivative-RESPONSE; it never used the Γ_eff=0.99970 value or any specific `F_dyn`/`Γ` form ⇒ `∂w/∂a₀ = 0` for ALL partition members. The 5-member effacement family confirms it (w_eff = `−Γ/(Γ+(1−Γ)r)` is manifestly a₀-FREE), while the VALUE w_eff varies with Γ (ii-b). ∎

**Volovik equilibrium-theorem cross-check (the lab-grounding for theorem-grade).** Paper 13 (Klinkhamer-Volovik 2008, PRD 77 085015) Eq. 4 gives the gravitating density `ρ_vac(q) = ε(q) − q dε/dq`; with `ε = ε_dyn + a₀` the script's quadratic instance yields equilibrium `q₀(a₀) = ±√(2a₀+k)/√k` and `ρ_vac|_{q₀} = 0` for ALL a₀ (Eq. 12 self-tuning) — the static a₀ MAGNITUDE is absorbed into the equilibrium point and **does not gravitate**. Paper 04 (Volovik 2005, gr-qc/0405012) §III states the deepest form: shifting the energy reference by α sends `H → H + αN` but the proper potential `H − μN` is INVARIANT because `μ → μ + α` (the µ-cancellation), holding for fermionic 3He AND bosonic 4He "irrespective of details." That **irrespective-of-details** clause IS the partition-independence, and the 3He/4He realizability IS the lab-grounding — together they make (ii-a) theorem-grade rather than q-theory-program-contingent. The observed dark energy is the DEVIATION from this self-tuned equilibrium (the effacement residual, Γ_eff = 0.99970); its EoS is a ratio of perturbations (q-derivatives), so it inherits the a₀-blindness.

**OPERATOR-DISTINCTNESS guard (plan §W7-2; `math-scripts.md §"Scope boundary"`).** This gate's operator is the q-field linear response-derivative `∂/∂q`: on `g(q)+c` it returns `g'(q)` — the additive-in-FREE-ENERGY constant is ANNIHILATED (`∂/∂q[g+c]−∂/∂q[g] = 0`, verified). The S116 W-4 operator is the K-LOG-derivative `d²/d(ln K)²` acting on `ln(·)`: on an additive-in-TRACE term it does NOT cancel (`d²/d(ln K)²[ln(g+c)] − d²/d(ln K)²[ln g] ≠ 0`, verified nonzero). DIFFERENT operators, OPPOSITE annihilation on DIFFERENT additive structures — both correct; the W-4 additive-IN-TRACE-SURVIVAL result is therefore NOT evidence against this gate's additive-in-free-energy VANISHING and is NOT cited as such.

**VD2b two-grade decomposition (the structural verdict).**
- **(ii-a) PLACEMENT — THEOREM-grade**: "w0 is a dynamical q-field linear-response EoS, not a static D_K spectral moment" — `∂w/∂a₀ = 0` partition-independently; lab-grounded in Volovik's 3He-B/4He equilibrium theorem; as permanent/regulator-invariant as the Weyl-forced −1 wall (i).
- **(ii-b) VALUE — model-contingent**: the specific number w0 = −0.918 is set by Γ_eff = 0.99970 (the S58 four-fold-lock); the partition family shows the value sweeping −0.870 → −0.971 as Γ deforms. This is exactly the DESI-testable content.
- ⇒ **wall (ii) carries TWO grades, not one** — the §5 EVOI categorical-wall register must record (ii) as a two-grade wall, and the branch-iv CLOSED-WITH-RESULT disposition strengthens (the categorical placement leg is now theorem-grade alongside the Weyl leg (i); only the −0.918 magnitude column stays model-grade).

**4-tuple.** `(value=INFO_VD2b_two-grade [dw/da0=0 partition-indep (ii-a THEOREM) + w_eff(Γ_eff=0.99970)=−0.918=w0_FW (ii-b model-contingent, spread=0.1007)], scheme=q-theory-linear-response+Volovik-equilibrium-theorem(Paper05), convention=static-a0-MAGNITUDE-vs-dynamical-EoS-RESPONSE, L_max=N/A)`. Companion rows: `# regulator_pin=a_0^{zeta}` (MANDATORY — the static CC magnitude IS the zeta-regulated n=0 Seeley-DeWitt moment) + `# composite-precedence: [VERIFY-THEOREM] … INFO = VD2b two-grade`. Dual-SHA: `audit=e7fd9d20da481e39…`, `content=d67eb629342b2596…`.

**Substrate framing (`phononic-framing.md`).** PHONONIC (the w(z) response IS the q-field vacuum partition effacing) ⊕ GEOMETRIC (the static a₀ IS the zeroth spectral moment of D_K). Direction of explanation: D_K eigenvalues → `a_0^{ζ}` static moment (a NUMBER, additive in F) ; q-field 4-form perturbation-response → w(z) (a RATIO of first derivatives of F). A derivative annihilates an additive constant ⇒ the EoS is BLIND to the static magnitude. The −1 the branch-iv moment converged to was never a failed spectral derivation — it was the substrate REFUSING the relocation of a THERMODYNAMIC observable (w0) into the VIBRATIONAL spectrum (Tr f(D_K)). Container-thinking is avoided: w(z) is not quintessence rolling in an FRW box; it IS the substrate's partition effacing, and the detector measures the emergent EoS image of that effacement.

**Output Artifacts**: `computations/session-117/s117_w0_categorical_wall_grade.py` (11.5 KB), `…/s117_w0_categorical_wall_grade.npz` (11,108 B), `…/s117_w0_categorical_wall_grade.png` (98,263 B).

---

### §W7-3. CF-S117-BRANCH-IV-L16 (baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `CF-S117-BRANCH-IV-L16`
**Trigger**: `[SIGN]` (decrement-deceleration sign |d(15→16)| < |d(14→15)|; **composite forced INFO by the `# composite-precedence:` row — corridor CLOSED-WITH-RESULT**)
**Classification**: **GEOMETRIC** (Level-1 single-τ-slice substrate-IS; the branch-iv Zubarev moment ρ_B is a spectral moment of D_K at τ_fold; the p+q=16 FB-bounded shell build is KK-geometry / irrep construction)
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: Extending the branch-(iv) CAC spread to the sliding window {14,15,16} (build the p+q=16 FB-bounded shell) continues the |d| ~ 1/λ_max² decrement-deceleration (|d(15→16)| < |d(14→15)| = 0.018456) and the sliding-window spread keeps narrowing (spread_CAC{14,15,16} < spread_CAC{13,14,15} = 0.0392902) — a **VALUE-NEUTRAL L_max diagnostic** certifying ρ_B is a smooth convergent sequence → −1, which does NOT reopen the CLOSED-WITH-RESULT branch-iv corridor. (**OPTIONAL / descopable without blocking 7-1; INFO-by-construction — the corridor is CLOSED-WITH-RESULT per W-5; a genuine FAIL is reserved for SCRIPT BREAKAGE only.**)
**Plan reference**: `sessions/session-plan/session-117-plan-w7.md` §W7-3 (FB-bounded p+q=16 shell build [GT-pure (16,0)/(0,16) + Casimir-projection of 15 mixed sectors]; Zubarev moment ρ_B(16) + CAC spread; 5-step substitution chain; composite-precedence INFO-by-construction).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
- (1) `computations/session-117/s117_branch_iv_l16.py` (42206 B) — `grep` hits: `from canonical_constants import` (L117), `print_verdict_payload` (def L248; calls L377, L646). PASS.
- (2) `computations/session-117/s117_branch_iv_l16.npz` (15989 B) — the p+q=16 shell spectrum (17 sectors, `shell_keys`) + ρ_B(13/14/15/16) + `spread_CAC`{14,15,16} + `d_15_16`/`d_14_15` + `lam_max_16`/`mean_Z_16`/`b_slope` + `conj_sentinel_max`/`shell_herr_max` + the INV13 contrast + the 1/λ_max² law residual. PASS.
- (3) `computations/session-117/s117_branch_iv_l16.png` (129063 B) — 3-panel: ρ_B(L) trajectory through L=16 (with the INV13 FB-bottom-K artifact line at ρ_B(15)); w0^CAC(L) sliding window vs w0_FW; |d(L→L+1)| decrement-deceleration. PASS.
- (4) verdict line in `computations/session-117/s117_gate_verdicts.txt` (L135) matches `^CF-S117-BRANCH-IV-L16:.* audit_sha256=[a-f0-9]{64}` (audit_sha256=`aec1f966f758ba8a…`) WITH the dual-SHA companion row (L136) + the schema-v2 `# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` 3-tuple row (L137) + the MANDATORY pre-declared `# composite-precedence: session-117-plan-w7.md §W7-3 + …(W-5 R3-FINAL closure)` row (L138). PASS.
- (5) this WP section satisfies `**Status**:.*COMPLETED`, `**Verdict**:.*(PASS|FAIL|INFO)`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**`. PASS.

**MCP Pre-Compute Audit**:
- `search_knowledge("branch-iv w0 L16 GTBUILDER spread_CAC Zubarev rho_B trajectory")` → surfaced `S116-W9-GTBUILDER-L15` (INFO; spread_CAC{13,14,15}=0.0392902; the {13,14,15} trajectory + (4,4)-filled lineage this gate extends) and `INV13-W1-3-BRANCH-IV-W0-L1516-DR3` (FAIL; spread_CAC{12,13,14,15,16}=0.0629703). **NOT PRE-CLOSED**: INV13 SET ρ_B(16)≡ρ_B(15) by the bottom-K Friedrich-Bär saturation argument (`rho16_eq_15=0.0`) — VALID for the bottom-K floor but STRUCTURALLY WRONG for the λ_max-driven branch-iv moment; the genuine p+q=16 shell was NEVER built (the S106 two-tier FB fallback left the 17 level-16 sectors as `fb_bounded_sectors` placeholders, `L16_operational=15`). This gate BUILDS the shell. Gate proceeds.
- `trace_entity("branch-iv w0 spread_CAC")` → no trace at that cross-pillar name; the gate-level entities surfaced via `search_knowledge`.
- canonical-import provenance (runtime-verified in-script): `w0_FW=−0.918` (S58 four-fold-lock), `tau_fold=0.190` (S12/S42), `Gamma_effacement=0.99970`, `N_cells`. S106 cache npz-internal `audit_sha256=5af2b7cd…` integrity-verified at runtime.

**Verdict**: **INFO — value-neutral L_max diagnostic delivered (INFO-by-construction; corridor CLOSED-WITH-RESULT per W-5).** The full p+q=16 shell was BUILT (17/17 sectors, `complete_16=True`; NOT FB-assumed). Both [SIGN] directional sub-claims CONFIRM: |d(15→16)|=0.0164603 < |d(14→15)|=0.0184563 (decelerating, margin +0.0019961) AND spread_CAC{14,15,16}=0.0349166 < spread_CAC{13,14,15}=0.0392902 (narrowing). Schema-v2 3-tuple: sign=PASS / magnitude=PASS / regime=VALID. The generic collapse would read composite PASS; **OVERRIDDEN to INFO** by the pre-declared `# composite-precedence:` row (the branch-iv corridor is CLOSED-WITH-RESULT and is NOT reopenable by a value-neutral diagnostic — the spread is offset-invariant, certifying ρ_B→−1 smoothly, NOT support for −0.918). `audit_sha256=aec1f966f758ba8a25b9614b47172f897367f66763e07cbc351917d79a4ba703`, `content_sha256=c3eb821e3187f207a346effe237c36892a74ad38e1bb2737fbc6c3f25eade822`.

**Results**:

**Headline.** Built the genuine p+q=16 shell and computed **ρ_B(16) = −0.712634671571781** — NOT INV13's FB-assumed −0.696174. The per-shell decrement DECELERATES and the sliding-window spread NARROWS: ρ_B is a smooth convergent sequence → −1. Both directional sub-claims confirmed; the corridor disposition (CLOSED-WITH-RESULT, W-5) is UNCHANGED (value-neutral).

**The shell build (GT-pure + Casimir-projection; conjugate-CPT halved).** All 17 level-16 sectors built via the s105/s116-W9 validated route — GT bosonic-ladder for (16,0)/(0,16) (never forms 3¹⁶); `get_irrep` Casimir-projection for the mixed sectors (GT-monkeypatched Sym^p parents). Exploiting the CPT identity |λ(p,q)|≡|λ(q,p)|, only the 9 upper-triangle (p≥q) sectors were constructed (1184.3 s GPU total); the 8 conjugates inherited the spectrum. Certification: `complete_16=True` (17/17), `herm_err_max=7.78e-16` (< floor 2.40e-14), **conjugate sentinel = 3.55e-14** (the LIVE (0,16)-vs-mirror-(16,0) check, < 1e-10). Largest block (8,8) dim 729 → D=11664 (272 s); central long pole (9,7) 286 s.

| L | ρ_B(L) | λ_max(L) | mean_Z(L) | n_modes | w0^CAC(L) |
|:--|:-------|:---------|:----------|:--------|:----------|
| 14 | −0.677718044738 | 6.168115 | 1.987872 | 323136 | −1.020511 |
| 15 | −0.696174388058 | 6.542827 | 1.987878 | 434112 | −1.038968 |
| **16** | **−0.712634671572** | **6.917603** | **1.987879** | 573648 | **−1.055428** |

- **λ_max-DRIVEN (the key physics)**: λ_max(16) = **6.917603** is set by the GT-pure (0,16) sector (C₂=304/3, the proven Casimir-max of the shell; `lam_max_from_gt=True`). It RAISES the denominator from λ_max(15)=6.542827 (slope b = ∂λ_max/∂L = 0.374776, Weyl-linear). **mean_Z is FROZEN**: 1.987878 → 1.987879, a shift of **8.86e-07** — the level-16 modes (|λ|_min ≈ 4.50) are Zubarev-suppressed (w_Z=exp(−λ²) ≈ 2e-9). So ρ_B(16)=mean_Z/λ_max(16)−1 moves almost entirely through the denominator.
- **ρ_B(15)/(14) on the merged set reproduce W9 bit-exact** (1.11e-16): the level-16 shell does NOT enter the L≤15 truncation cuts — lineage continuity confirmed.

**Decrement-deceleration (PRIMARY [SIGN] sub-claim) + the 1/λ_max² law.** d(14→15)=−0.01845634, d(15→16)=**−0.01646028** (both negative, monotone-decreasing). |d(15→16)| < |d(14→15)| ⇒ **decelerating=True**, margin +0.00199606. Analytic finite-difference d(15→16)=mean_Z·(1/λ_max(16)−1/λ_max(15))=−0.01646042 vs empirical −0.01646028 ⇒ **law residual = 1.35e-07**: the deceleration law (|d|=μb/λ_max², μ frozen) holds at sub-1e-7.

**Spread narrowing.** spread_CAC{14,15,16}=max−min=ρ_B(14)−ρ_B(16)=**0.034916626834** < spread_CAC{13,14,15}=0.039290236 ⇒ **narrows=True**. Offset-cancellation residual = 1.11e-16 (the CAC offset cancels exactly; spread_CAC≡spread_ρ). This offset-invariance is precisely why the diagnostic is **value-neutral**: the spread certifies ρ_B → −1 (the bare-moment limit), NOT support for −0.918 — which lives entirely in the CAC `offset_B = w0_FW − ρ_B(10) = −0.342793384865` (w0^CAC(10)=−0.918 EXACTLY, resid 0.0).

**INV13 contrast (the structural correction this gate makes).** INV13-W1-3 SET ρ_B(16) ≡ ρ_B(15) = −0.696174 by the bottom-K Friedrich-Bär saturation argument — valid for the bottom-K floor (the p+q=16 |λ|_min ≈ 4.50 ≫ the bottom-20 ceiling 0.845, so the shell cannot enter the bottom-K) but STRUCTURALLY WRONG for the λ_max-DRIVEN branch-iv moment (the shell RAISES λ_max). The genuine λ_max-driven shift INV13 missed is **0.016460** (|−0.712635 − (−0.696174)|). This IS the S116-W9 stated orthogonality: "bottom-K Friedrich-Bär-saturated … ORTHOGONAL to λ_max-driven w0 moment shift."

**5-step substitution chain (substituted numbers).**
- Step 1: d(L→L+1) = ρ_B(L+1)−ρ_B(L). [W9: d(13→14)=−0.020834, d(14→15)=−0.018456.]
- Step 2: ρ_B(L) = mean_Z(L)/λ_max(L) − 1; mean_Z FB-saturated (μ=1.987879, frozen), λ_max Weyl-linear (b=0.374776).
- Step 3: d(L→L+1) ≈ μ(1/λ_max(L+1) − 1/λ_max(L)) = −μb/λ_max² (μ frozen).
- Step 4: |d| = μb/λ_max² ~ 1/L² (Weyl λ_max~L). [empirical−analytic residual 1.35e-07.]
- Step 5: λ_max(16)=6.917603 > λ_max(15)=6.542827 ⇒ |d(15→16)|=0.016460 < |d(14→15)|=0.018456 ⇒ decelerates; spread narrows. Per W-5 this convergence is TO −1 (bare-moment), value-neutral, and does NOT reopen the corridor. ∎

**4-tuple.** `(value=INFO_value-neutral [ρ_B(16)=−0.712635; spread_CAC{14,15,16}=0.0349166<0.0392902 narrows; d(15→16)=−0.016460, |·|<0.018456 decel; λ_max-driven, mean_Z frozen 8.9e-07; INV13-contrast shift 0.016460], scheme=zeta [+Zubarev w_Z], convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max=16)`. **schema-v2 [SIGN] 3-tuple**: sign=PASS (decel + monotone + offset-cancel), magnitude=PASS (spread narrows), regime=VALID (all guards hold). Companion rows: `# composite-precedence:` (INFO-by-construction; plan §W7-3 + W-5 closure) + `# regulator_pin=a_2^{Mellin} poleconv-A-double (pole_in_s=3, curvature_grade_n=2)` + `# lambda_max-DRIVEN …`.

**Substrate framing (substrate-first; `phononic-framing.md`)**: GEOMETRIC, Level-1 single-τ-slice substrate-IS (τ_fold=0.190). The branch-iv Zubarev moment ρ_B(L)=mean_Z(L)/λ_max(L)−1 IS a spectral moment of D_K at τ_fold — the substrate's own vibrational spectrum read through the Zubarev occupation weight, NOT a field "in" a container. Direction of explanation: D_K eigenvalues at τ_fold → the FB-bounded p+q=16 shell → the Zubarev moment ρ_B(16) → the CAC-anchored w0^CAC(16). Container-thinking rejected: λ_max(L) is the RUNNING truncation EDGE (sup-norm of the retained spectrum), a non-substrate quantity with no continuum limit; the moment's smooth convergence to −1 is the substrate telling us w0 does NOT live in the eigenvalue spread (the W-5 categorical wall (ii)). This gate does NOT search for a hidden spectral derivation of −0.918 — it certifies the moment converges smoothly to its OWN limit (−1), a value-neutral presentation-hygiene fact, leaving the closed-form thermodynamic value −0.918 (the q-field partition's effacement) exactly where W-5 placed it. Forward status: presentation-normalization hygiene (select a non-drifting off-anchor costume so a downstream consumer is not shown a proxy drifting to −1.055/−1.341).

**dual-SHA**: audit_sha256=`aec1f966f758ba8a25b9614b47172f897367f66763e07cbc351917d79a4ba703`, content_sha256=`c3eb821e3187f207a346effe237c36892a74ad38e1bb2737fbc6c3f25eade822`. **Artifacts**: `s117_branch_iv_l16.py` (42206 B) / `.npz` (15989 B) / `.png` (129063 B); resume cache `s117_branch_iv_l16_shell_resume.npz` (223706 B, the deterministic 17-sector shell spectra).

---

## Wave 7 Synthesis (team-lead)

All three Wave-7 gates closed. The wave settles the substrate-physics status of the dark-energy EoS **w0 = −0.918** on three orthogonal axes — and the unifying result is that the S116 W9 branch-iv "**−1.341 gap**" is a **proxy-artifact**, not a competing substrate value.

### (a) Numerical revisions
- 7-1: deg(T_{BZ→pivot})[w0] = **0** (|deg|<0.05); Δ_scheme = 0 M_KK² across {APS,CS,BC}; de-λ_max removes 99.29% of the running drift (spread 0.121→8.6e-4); the −1.341 asymptote is 100.51% running-λ_max-edge-sourced (mean_Z term −0.51%, opposing). DR3 σ-distances vs −0.918: **2.13σ vs DESI DR2 (−0.803±0.054), 3.28σ vs ΛCDM (−1)**.
- 7-2: ∂w/∂a₀ = 0 EXACT, partition-independent (symbolic for arbitrary F_dyn + numeric across 5 effacement-partition members); partition-family w_eff varies −0.870→−0.971 (Γ_eff=0.99970 → −0.918 anchor).
- 7-3: rho_B(16) = **−0.7127** BUILT (17/17 sectors, λ_max(16)=6.9176 @ GT-pure (0,16)); [SIGN] DECEL (|d(15→16)|=0.01646 < |d(14→15)|=0.01846) ∧ NARROWS (spread{14,15,16}=0.0349 < 0.0393); 1/λ_max² law residual 1.35e-07.

### (b) Structural changes
- **The W9 −1.341 gap is PROXY-ARTIFACT-typed** (7-1, epistemic-TYPE): the BZ→pivot transport is degree-0 (T2-VACUOUS scalar — w0 is dimensionless d_A=0, single pole s=3, no square ⇒ Wodzicki −2(s−s')=0), so substrate w0 = pivot w0 = −0.918 *directly* (the transport is the identity). The −1.341 asymptote is the L→∞ artifact of a RUNNING truncation-edge (λ_max) normalization — a non-substrate quantity with no continuum limit, injected by the S85 Zubarev proxy *definition*. The substrate REFUSED the branch-iv relocation of the thermodynamic value into the eigenvalue spread. NO §23 K-counter advance (deg=0 is not the factorization-extracted NON-SCALAR degree reserved for r/α_t).
- **w0 ∉ Tr f(D_K) is a TWO-GRADE wall (VD2b)** (7-2): the categorical PLACEMENT (ii-a) [the EoS response is the q-field vacuum partition's effacement, NOT a static D_K spectral moment] upgrades from q-theory-model-grade to **THEOREM-grade** — the static-CC-magnitude (a₀, additive constant) vs dynamical-EoS-response (first-derivative linear-response functional) functional-type separation FORCES ∂w/∂a₀=0 independent of the partition. The VALUE (ii-b) Γ_eff=0.99970 → −0.918 stays model-contingent — exactly the DESI-testable part.
- **INV13-W1-3 corrected** (7-3): it had set rho_B(16)≡rho_B(15) by bottom-K FB-saturation — valid for bottom-K but WRONG for the λ_max-driven branch-iv moment (missed shift 0.01646). The L16 corridor disposition is UNCHANGED (value-neutral; the offset cancels exactly, certifying rho_B→−1, NOT support for −0.918).

### Wave 7 → Wave 8 decision point
The W-5 deg-CONDITIONAL element (BD2) RESOLVES (deg=0): DR3 σ-distances freeze vs −0.918 directly. No constraint on W8 (independent).

## Carry-Forward Computations

No carry-forwards: all Wave-7 outcomes closed in-session. The w0 status is settled on all three axes (deg=0 scalar; two-grade wall; L16 corridor closed-with-result). The pre-registered FAIL-branch CF (normalization redesign IFF 7-1 ILL-POSED) did not trigger — 7-1 de-λ_max'd cleanly (PASS-SCALAR). The standing DESI tension (2.13σ DR2) is an observational-watch item on the falsifier surface (mack), not a compute gate.

## Effected In-Session / routed to session-close

Non-math §7-falsifier / registry / atlas updates (route to mack sole-writer / session-close; executed before STOP):
- §7 falsifier-surface (7-1): REMOVE the "computed under provisional deg=0; pending CF-S117-W0-TRANSPORT-DEGREE" tag from the w0 DR3 rows; FREEZE the σ-distances directly vs −0.918 (2.13σ vs DESI DR2; 3.28σ vs ΛCDM). (mack)
- registry/atlas (7-1): annotate that the branch-iv −1.341 asymptote is a running-λ_max-edge PROXY-ARTIFACT (not a substrate w0); substrate w0 = pivot w0 = −0.918 via the deg=0 identity transport. (registry)
- §5 EVOI / wall register (7-2): wall (ii) [w0 ∉ Tr f(D_K)] is a TWO-GRADE wall — placement (ii-a) THEOREM-grade (∂w/∂a₀=0 partition-independent), value (ii-b) Γ_eff-contingent. (registry; capstone-hygiene Q3 if the capstone narrates this wall.)
- (7-3 INV13-W1-3 correction is documented in §W7-3; INV13 is an investigation-track result (not session-canonical), so no session-registry edit — the corridor disposition is value-neutral/UNCHANGED.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-28 | w0 BZ→pivot transport (7-1) | W9 −1.341 gap open (deg unevaluated) | deg=0 SCALAR; substrate=pivot=−0.918; −1.341 = proxy-artifact | 7-1 PASS-SCALAR |
| 2026-06-28 | w0 categorical wall (ii) (7-2) | q-theory-model-grade | TWO-GRADE: placement (ii-a) THEOREM-grade (∂w/∂a₀=0), value (ii-b) Γ_eff-contingent | 7-2 INFO (VD2b) |
| 2026-06-28 | branch-iv L16 corridor (7-3) | INV13: rho_B(16)≡rho_B(15) (bottom-K FB-sat) | rho_B(16)=−0.7127 BUILT; DECEL+NARROWS; corridor closed-with-result (→−1) | 7-3 INFO; INV13 corrected |
| 2026-06-28 | w0 DR3 σ-distance falsifier | deg-conditional (provisional) | frozen vs −0.918: 2.13σ DESI DR2, 3.28σ ΛCDM | 7-1 deg=0 resolves the condition |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| 7-1 | `s117_w0_transport_degree.py` | `.npz` | `.png` | PASS-SCALAR (+[SIGN] 3-tuple) |
| 7-2 | `s117_w0_categorical_wall_grade.py` | `.npz` | `.png` | INFO (VD2b two-grade) |
| 7-3 | `s117_branch_iv_l16.py` | `.npz` | `.png` | INFO (+[SIGN] 3-tuple; corridor closed-with-result) |
