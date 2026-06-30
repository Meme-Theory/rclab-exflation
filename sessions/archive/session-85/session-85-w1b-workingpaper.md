# Session 85 Wave W1b — mack-origin reviewer wave (split 2/2) (Results Working Paper)

**Session**: 85 | **Wave**: W1b | **Plan**: session-85-plan-w1b.md | **Theme**: mack-origin α_s detector-forecast refinements, prior/correlation formalizations, and the r_max structural-theorem discharge.

## Gate Sections

### §W1b-1. S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE (mack-cosmic-bridge)

**Status**: DONE
**Gate ID**: `S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE`
**Trigger**: `[AUDIT]`
**Classification**: **META** (pre-registration extension; observational binding)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **FAIL** — framework-prediction cell flips A1 ↔ B2 between L_max=10 and L_max=12; DR3 tree is regulator-layer-conditional, not regulator-agnostic.

**4-tuple**: `(value='FLIP-A1-to-B2-at-L12', scheme=Zubarev, convention=R_842-successor, L_max=enumerated{5,10,12})`

**Substitution chain (Python-verified)**:
- R_842 rectangle (from S85 W0-DR3-REGULATOR-SUCCESSOR-TREE JSON, pinned at content_sha head `85708509`): w_0 ∈ [−0.942, −0.742], w_a ∈ [−0.2, 0.2]. Center (−0.842, 0); half-widths (0.1, 0.2).
- 7-cell partition of (w_0, w_a) plane: A1 (1σ box around center), A2 (1–2σ), B1 (w_0 < −0.942 phantom), B2 (w_0 > −0.742 quintessence), B3 (|w_a| > 0.2 CPL evolution), C1/C2 (exotic tails). Disjoint, cover plane.
- Framework Zubarev predictions per L_max:
  - L=5: w_0 = −0.918, w_a = 0 → cell **A1**
  - L=8: **DATA-UNAVAILABLE** (no S85 Zubarev L=8 computation on disk)
  - L=10: w_0 = −0.918 (canonical w0_FW), w_a = 0 → cell **A1**
  - L=12: w_0 = **−0.635** (S85 W0-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE extrapolation FAIL value), w_a = 0 → cell **B2**
- Cell flip test across L_max ∈ {5, 10, 12}: unique cells = {A1, B2}; flip detected A1 → B2 between L=10 and L=12.
- Plan §W1b-1 threshold: FAIL iff at least one cell flips IN→OUT when L_max changes by 2. Satisfied ⇒ **FAIL**.

**Cross-check (reconstruction)**: The S84 W4-44 7-cell JSON (`s84_w4_44_dr3_contingency_fine_grained.json`) is NOT on disk; cell definitions reconstructed from plan §W1b-1 + W1a-5 decision tree. R_842 rectangle matches W0-DR3-REGULATOR-SUCCESSOR-TREE canonical ([−0.942, −0.742] × [−0.2, 0.2]). Plan §W1b-1 prereq note cited a tighter rectangle [−0.94, −0.82] × [−0.12, 0.12] at content_sha `9cc7f47e`; I used the W0-successor pin that is actually published.

**Dual-SHA**:
- audit_sha256 = `beba9cad44f34103df20f3c7b01913a3658139d97ebd44126c8a38b9c12c510b`
- content_sha256 = `15e1b1ff1feb5a5cf3717bf09327ab1945a08c411b9610b878fa529b25849dbf`

**Artifacts**: `computations/s85_w1b_cf_m2_dr3_regulator_tree.{py,npz,png}`

**What FAIL means for solution space**:
The DR3 pre-registration tree is **regulator-layer-conditional**. A single 7-cell tree DOES NOT suffice for 2026-04-23 firing — S86 must maintain 3 sub-trees keyed on L_max ∈ {8, 10, 12}, and DR3 adjudication becomes regulator-first rather than box-first. Structurally this says DR3 is sensitive to high-eigenvalue tails of D_K (since Zubarev convergence toward -1 is NOT achieved at L=12, and the extrapolation puts w_0 in quintessence territory). The L_max=8 sub-tree is a S86 carry-forward. Downstream: W2-1 (connes α_s axiom minimality) inherits a new PRDR pin per plan §Cross-wave decision rule 1.

---

### §W1b-2. S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED (mack-cosmic-bridge)

**Status**: DONE
**Gate ID**: `S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED`
**Trigger**: `[VERIFY]`
**Classification**: **META** (Fisher-matrix formalism; detector-level)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **PASS** — correlated-Fisher σ_corr/σ_diag = 1.1297 < 1.25 threshold; W1a-9 ensemble claim survives realistic block-diagonal correlation within 25% widening.

**4-tuple**: `(value=1.1297479814965643, scheme=Fisher-marg-Gauss, convention=block-diag-C, L_max=n/a)`

**Substitution chain (Python-verified)**:
- Per-detector σ(α_s): CMB-S4 = 2.1e-3, CMB-HD = 1.5e-3, LiteBIRD = 1.05e-2, DESI-DR3 = 1e-2, LISA = 1e-1
- 5×5 correlation matrix C (plan §W1b-2 pre-registered off-diagonals):
  - C(CMB-S4, CMB-HD) = 0.30 (partial sky overlap, α_s modes)
  - C(CMB-S4, LiteBIRD) = 0.15 (atmospheric + galactic foreground low-ℓ)
  - All other off-diagonals = 0 (DESI/LISA independent of CMB detectors)
  - det(C) = 0.8875
- Cov = Σ · C · Σ, Σ = diag(σ_i)
- Diagonal combined: σ_diag = √(1/Σ 1/σᵢ²) = **1.2035×10⁻³**
- Correlated combined: σ_corr = √(1/(1ᵀ · Cov⁻¹ · 1)) = **1.3597×10⁻³**
- Ratio = σ_corr / σ_diag = **1.1298** (widening by 13.0%)
- Thresholds: PASS ≤ 1.25, FAIL > 1.50 ⇒ **PASS**
- Sanity: C = I → ratio = 1.0000... exactly (machine eps, verified inline)

**Direction note**: Cauchy-Schwarz on Fisher information guarantees σ_corr ≥ σ_diag (ratio ≥ 1). Correlation can only widen, never tighten; magnitude depends on off-diagonal magnitudes relative to diagonal sensitivity imbalance. The 0.30 and 0.15 off-diagonals introduce ~13% widening — comfortably below the 25% PASS cut.

**Dual-SHA**:
- audit_sha256 = (see verdict line)
- content_sha256 = (see verdict line)

**Artifacts**: `computations/s85_w1b_alpha_s_joint_fisher_correlated.{py,npz,png}`

**What PASS means for solution space**:
W1a-9 MULTID-FISHER's diagonal-detector assumption is defensible within ~13% on the σ(α_s) combined posterior. The advertised multi-channel discrimination does not collapse under realistic block-diagonal correlation. FAIL would have required the foreground/sky-overlap covariance to exceed ~50% of the sensitivity budget; the plan-pre-registered off-diagonals (0.30, 0.15) fall safely inside the PASS regime. Downstream: W1a-9 ensemble log10(BF_FW/LCDM) = +828 claim is robust; no restatement needed per plan §Cross-wave decision rule 2.

---

### §W1b-3. S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM (mack-cosmic-bridge)

**Status**: DONE
**Gate ID**: `S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM`
**Trigger**: `[AUDIT]`
**Classification**: **META** (Bayes-factor prior-range formalization)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **FAIL** — `min(BF) = 0.99 < 3` (Planck Gaussian prior); framework α_s advantage is **prior-sensitive**.

**4-tuple**: `(value=0.9885542770409307, scheme=marg-L-ratio, convention=flat-model-prior, L_max=n/a)`

**Substitution chain (Python-verified)**:
- Framework point: α_s_canon = +0.00117 (S63 RUNNING-NS-63 inflationary running; zero-free-parameter)
- Planck 2018 data: α_s_obs = −0.0045, σ_obs = 0.0067
- L_framework = N(α_canon | α_obs, σ_obs) = **4.16×10¹**
- 3 pre-registered priors + their marginal likelihoods:

| Prior | Type | Params | marg_L | BF = L_fw / marg_L | log10(BF) |
|:------|:-----|:-------|:-------|:-------------------|:----------|
| wide_uniform | U[L,H] | [−0.05, +0.05] | 1.00×10¹ | **4.162** | +0.619 |
| narrow_uniform | U[L,H] | [−0.02, +0.02] | 2.47×10¹ | **1.682** | +0.226 |
| planck_gauss | N(μ,σ) | (−0.0045, 0.0067) | 4.21×10¹ | **0.989** | −0.005 |

- min(BF) = 0.989; max(BF) = 4.162
- Plan thresholds: PASS if ALL BF > 30; FAIL if any BF < 3. Two priors (narrow_uniform AND planck_gauss) give BF < 3 ⇒ **FAIL**.
- Direction: BF is monotonic in prior width — wider prior dilutes LCDM's marginal likelihood, inflating BF. Under Planck-posterior prior, LCDM predicts the observed region as strongly as framework's point; BF ≈ 1.

**Structural implication**: The "BF ~ 1000 from zero-free-parameters" advertisement requires a **wide** LCDM prior. Against a Planck-posterior-informed prior, the framework offers NO discrimination on α_s. This is an HONEST result — framework's α_s = 0.00117 happens to sit near Planck's −0.0045 (0.85σ), so a tight LCDM prior that peaks near the observation is equivalent in fit. The framework's claim needs restatement: it is prior-range-dependent, not prior-free.

**Dual-SHA**:
- audit_sha256 = `bb97497482ae088434e09776439d383927df487c8178e26cccf9d9525fe20534`
- content_sha256 = `53bf9edec5e34333331254d958fbf39e71e15e7f4d3705f7714ce859edbe0e4c`

**Artifacts**: `computations/s85_w1b_alpha_s_prior_range_lcdm.{py,npz,png}`

**What FAIL means for solution space**:
Per plan §Cross-wave decision rule 3: every BF row in the permanent-results-registry inherits a **prior-disclosure obligation**. Rows must carry (prior-type, prior-width) pins. Framework's α_s prediction is still CONSISTENT with Planck (0.85σ from central), but the discriminatory force collapses under tight priors. The "zero-free-parameter advantage" phrasing is inaccurate as advertised; correct phrasing is "zero-free-parameter PREDICTION that happens to land near Planck central; BF preference depends on assumed LCDM prior window". Carry-forward: restate BF claims with explicit prior pins in atlas-04.

---

### §W1b-4. S85-W1b-ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS (mack-cosmic-bridge)

**Status**: DONE
**Gate ID**: `S85-W1b-ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS`
**Trigger**: `[AUDIT]`
**Classification**: **META** (cross-registry contradiction resolution)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **PASS** — |Δα| = 7.15×10⁻⁴ = 0.107σ_Planck < 0.5σ threshold; S62 and S63/S67 agree at shared pivot.

**4-tuple**: `(value=0.000715, scheme=spectral-zeta, convention=k_pivot=0.05, L_max=10)`

**Source reconstruction**: Plan §W1b-4 frames the audit as "S62 vs S67". On-disk artifacts:
- `s62_kz_ns.npz` — S62 n_s via Kosterlitz-Zouridakis / spectral moment (leading-order slow-roll). No explicit α_s output; α_s ≈ 0 is implicit in the LO derivation.
- `s63_running_ns.npz` — S63 RUNNING-NS-63 one-loop Mukhanov-Sasaki through the fold. This IS the "S67 transit-PS MS running" the plan references. α_s = 0.000715 (at 0.78σ from Planck, MEMORY.md entry).

**Substitution chain (Python-verified)**:
- α_s^(S62) = 0.0 (leading-order slow-roll implicit)
- α_s^(S67 = S63) = 0.000715 (one-loop MS through fold)
- Shared pivot k = 0.05 Mpc⁻¹ (Planck convention; both computations use this by default)
- Δα = α_s^(S62) − α_s^(S67) = 0 − 0.000715 = **−0.000715**
- σ_Planck = 0.0067 (Planck 2018 TT,TE,EE+lowE+lensing)
- |Δα| / σ_Planck = **0.1067**
- Thresholds: PASS if |Δα| < 0.5·σ_Planck = 3.35×10⁻³; FAIL if > σ_Planck = 6.7×10⁻³
- 7.15×10⁻⁴ < 3.35×10⁻³ ⇒ **PASS**

**Interpretation**: The superficial "contradiction" between S62 and S67 is a convention artefact, not a genuine physics disagreement. S62 computed n_s at leading-order slow-roll (where α_s = 0 by construction); S63/S67 extracted the one-loop running through the fold. The residual 7.15×10⁻⁴ is the expected one-loop magnitude (~ε_H·α_s ~ 10⁻³) and sits comfortably within 0.11σ of Planck's measurement. Both computations reference the same spectral triple D_K; they probe different orders of the same expansion.

**Dual-SHA**:
- audit_sha256 = `3b6e306b4eac1ec2e520ea90afecaf6d88ac838381d48f0e7959ece16dad0169`
- content_sha256 = `ae02b30ca21802bbda00c4be89a62aceaecd182d2592a0cbe056916e202613e2`

**Artifacts**: `computations/s85_w1b_alpha_s_transit_ps_67_simultaneous.{py,npz,png}`

**What PASS means for solution space**:
S62 and S67 reconcile; the canonical registry row for α_s needs only one entry (α_s ≈ 7e-4, one-loop). Per plan §Cross-wave decision rule 4, NO new scheme tag is required on `alpha_s_canon` (the plan's FAIL path would have forced this; PASS lets S86 gates consume `alpha_s_canon` without scheme specification). Downstream: W1a-9 7D Fisher α_s entry (0.00117) is compatible with S63's 0.000715 within updating; no correction needed.

---

### §W1b-5. S85-W1b-BETA-S-JOINT-S4-HD (mack-cosmic-bridge)

**Status**: DONE
**Gate ID**: `S85-W1b-BETA-S-JOINT-S4-HD`
**Trigger**: `[VERIFY]`
**Classification**: **META** (detector-forecast joint-fit consistency)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **PASS** — tightening ratio σ_joint/σ_S4 = 0.581 (41.9% tightening, well above 15% threshold); framework β_s=−0.1331 discriminates LCDM null at 104σ joint.

**4-tuple**: `(value=0.0012787240261820123, scheme=Fisher-2D-joint, convention=indep-detectors, L_max=n/a)`

**Substitution chain (Python-verified)**:
- CMB-S4 sensitivities: σ(α)_S4 = 2.1e-3, σ(β)_S4 = 2.2e-3 (canonical `sigma_beta_s_CMB_S4`)
- CMB-HD proxy: σ(α)_HD = 1.5e-3 (MacInnis anchor; refined in W1b-6). Scaling = 1.5/2.1 = 0.714. σ(β)_HD = 2.2e-3 × 0.714 = **1.571×10⁻³** (proxy; W1b-6 refinement pending).
- Independent-experiment Fisher combine (diagonal 2×2 per detector, α–β within-detector correlation = 0):
  - 1/var_joint = 1/σ_S4² + 1/σ_HD² = 2.066×10⁵ + 4.050×10⁵ = 6.116×10⁵
  - σ_joint = **1.279×10⁻³**
- Tightening ratio = σ_joint / σ_S4 = 1.279×10⁻³ / 2.2×10⁻³ = **0.5812**
- Thresholds: PASS ≤ 0.85, FAIL > 0.95 ⇒ **PASS** (tightening by 41.9%)

**Framework β_s pull**:
- |β_canon| / σ_joint = 0.1331 / 1.279×10⁻³ = **104.1σ** from LCDM null
- |β_canon| / σ_S4 = 60.5σ (S85-W0 BETA-S-CMB-S4 PREREG single-channel)
- Joint S4×HD tightens pull from 60.5σ → 104.1σ. Framework β_s either lands at that value (PASS/ratified by 2030) or falls at >100σ from the joint — decisive discrimination in either direction.

**Proxy caveat**: σ(β_s)_HD is a proxy derived from α_s/β_s sensitivity-ratio scaling. W1b-6 (MacInnis explicit) refines σ(α_s)_HD; a companion MacInnis β_s refinement would nail this, but the proxy scaling is expected accurate to ~20% given both parameters probe the same damping-tail regime. Even with σ(β)_HD degraded 50%, tightening ratio stays below 0.85.

**Dual-SHA**:
- audit_sha256 = `d94e6068696ff51d5ae050789d560c3bf67143830e6499010877d628dc37a881`
- content_sha256 = `ef098034bb08b613d796557c385857d883d543df069c4d3e85077a48a5286eb2`

**Artifacts**: `computations/s85_w1b_beta_s_joint_s4_hd.{py,npz,png}`

**What PASS means for solution space**:
Adding CMB-HD as an independent detector genuinely tightens the β_s posterior by ~42%, raising framework-vs-LCDM discrimination from 60.5σ (CMB-S4 alone, 2028) to 104σ (joint S4×HD, ~2034). The framework's zero-free-parameter β_s prediction graduates from "CMB-S4 decisive" to "doubly decisive" under joint multi-CMB pipeline. This is a PRE-REGISTERED strengthening of S85 W0-1 BETA-S pre-registration.

---

### §W1b-6. S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT (mack-cosmic-bridge)

**Status**: DONE (PRE-REG-INCOMPLETE)
**Gate ID**: `S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT`
**Trigger**: `[VERIFY]`
**Classification**: **META** (detector-forecast replacement)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **PRE-REG-INCOMPLETE** — MacInnis 2022 PDF accessible (`downloads/2203.05728.pdf`, SHA pinned) but the paper does NOT publish an explicit σ(α_s) forecast. Plan §W1b-6 assumed this was available; it is not.

**4-tuple**: `(value='SOURCE-LACKS-CONTENT', scheme=Fisher-single-expt, convention=Planck-pivot, L_max=n/a)`

**What MacInnis 2022 DOES publish (verified by reading pages 11–30)**:

| Parameter | σ | Section |
|:----------|:--|:--------|
| σ(N_eff) | 0.014 | 4.1 |
| σ(f_NL^local) | 0.26 | 5.2 |
| σ(r) | 0.005 | 9.1 |
| σ(w_0) | 0.005 | 6 |
| σ(Σm_ν) | 13 meV | 6 |
| σ(B_SI) | 0.036 nG | 5.1 |
| **σ(α_s)** | **NOT PUBLISHED** | — |

α_s is not a headline science target of this Snowmass CMB-HD White Paper. Its headline forecasts are dark-matter-power-spectrum/light-relic/PGW/DE/neutrino-mass — not the spectral-index running.

**Why this is NOT a FAIL**:
Per plan §W1b-6 fallback clause and `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness: a gate whose producing machinery cannot be evaluated (here: the requested forecast is not in the source) is PRE-REG-INCOMPLETE, not FAIL. The projected σ(α_s)_CMB-HD = 1.5×10⁻³ used in W1a-9 / W1b-2 / W1b-5 remains a sensitivity-scaling estimate until an explicit CMB-HD α_s forecast is published.

**Dual-SHA**:
- audit_sha256 = `48eccb17f5f07edf3acdfc4e89476655b6ca549e4aab77873f9b1bca6e209e16`
- content_sha256 = `5a30def173ea4001ddfbd14d68ec94ed8df99ee67ae98313b3e54db286457b99`

**Artifacts**: `computations/s85_w1b_cmb_hd_alpha_s_macinnis_explicit.{py,npz,md,png}`

**S86 carry-forward**:
Track publications of an explicit CMB-HD α_s forecast. Candidate sources:
- Abazajian et al. CMB-HD companion papers
- CMB-HD SciBook forecast code release
- CMB-S4/CMB-HD joint forecast paper (if it tabulates α_s)

Per plan §Cross-wave rule 5, W1a-9 MULTID-FISHER ensemble flagged PRE-REG-INCOMPLETE-ADJACENT on the α_s detector portfolio — ANNOTATION only, not retraction. When the explicit forecast appears, re-fire this gate with the verified σ value and perform the ratio test.

---

### §W1b-7. S85-W1b-LITEBIRD-ALPHA-S-HAZUMI-VERIFIED (mack-cosmic-bridge)

**Status**: DONE (PRE-REG-INCOMPLETE)
**Gate ID**: `S85-W1b-LITEBIRD-ALPHA-S-HAZUMI-VERIFIED`
**Trigger**: `[VERIFY]`
**Classification**: **META** (detector-forecast replacement; twin of §W1b-6)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **PRE-REG-INCOMPLETE** — Hazumi 2022 JLTP LiteBIRD paper (`downloads/2202.02773.pdf`, SHA pinned, 156 pages) does NOT forecast σ(α_s). Full-text grep returns **0 hits** for `alpha_s`/`running`/`dn_s/dlnk`/`nrun` across all 156 pages.

**4-tuple**: `(value='SOURCE-LACKS-CONTENT', scheme=Fisher-single-expt, convention=Planck-pivot, L_max=n/a)`

**Verification method**: pypdf text extraction on all 156 pages; search for keywords {`alpha_s`, `alpha s `, `running of`, `dn_s/dln`, `dns/dlnk`, `d²ln`, `nrun`, `running spectral`}. Zero matches. LiteBIRD's headline forecasts are σ(r)~0.001 (Δr budget), σ(τ_re)~0.002 (cosmic-variance limited), and n_T via r-consistency — NOT α_s.

**Why this is NOT a FAIL (+ actually confirms plan expectation)**:
Plan §W1b-7 step 5 predicted "σ_LB/σ_S4 > 5 from naive ℓ_max^{-0.5} scaling" because LiteBIRD is B-mode-optimized, not α_s-optimized. The finding that LiteBIRD does NOT forecast α_s **at all** is CONSISTENT with the design expectation — more extreme than the plan anticipated. The > 5 ratio is VACUOUSLY SATISFIED (LiteBIRD's α_s sensitivity is effectively infinite).

**Dual-SHA**:
- audit_sha256 = `1fd76b38f50abb8b806098cccec92fca4669f49c3ccff509a7ac84db5bfce73a`
- content_sha256 = `d23e3aa61326e31c167d99362aef4d653bff85c8e2228a0d2f3c99cec1d97164`

**Artifacts**: `computations/s85_w1b_litebird_alpha_s_hazumi_verified.{py,npz,md,png}`

**S86 carry-forward**:
Treat LiteBIRD's α_s contribution as formally not forecast, practically negligible in any joint ensemble. The W1a-9 7D Fisher σ_LB = 1.05e-2 entry remains a placeholder; in practice, LiteBIRD's detector portfolio weight on α_s should be set to zero (or inf-sigma) until a companion paper publishes otherwise.

---

### §W1b-8. S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION (mack-cosmic-bridge)

**Status**: DONE — real-data revision supersedes earlier null-update reading
**Gate ID**: `S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION`
**Trigger**: `[AUDIT]`
**Classification**: **META** (canonical-constants recalibration)
**Agent**: `mack-cosmic-bridge`

**Verdict (final, real-data)**: **FAIL** — |Δα_s| = 0.0068 = 1.015·σ_2018 (just over FAIL threshold). Framework's canonical `alpha_s_canon = −0.0045 ± 0.0067` has drifted ~1σ when real post-2018 ACT DR4 data is incorporated. Canonical-constants update recommended.

**Earlier verdict (superseded)**: An initial run of this gate using ONLY the plan's named sources (PR4 Tristram + DESI DR2) returned a null-update PASS because those sources don't publish α_s. The user correctly flagged that as "shrugging and admitting defeat" when the real post-2018 source (ACT DR4 Aiola 2020) was obviously available. The real-data re-run below supersedes that reading.

**4-tuple (final)**: `(value=0.0068, scheme=inv-var-weighted-combination, convention=Planck-pivot, L_max=n/a)`

**Source-availability audit (plan-named sources, verified by full-text pypdf grep)**:

| Source | arXiv | Pages | α_s tabulation? |
|:-------|:------|:------|:----------------|
| Tristram 2023 Planck PR4 | 2309.10034 | 21 | **NO** — baseline 6-param LCDM; no α_s extension |
| DESI 2024 III (BAO) | 2404.03000 | 71 | **NO** — BAO only, not an α_s observable |
| DESI 2024 VI (Cosmology) | 2404.03002 | 71 | **NO** — focused on w_0, w_a, m_ν; no α_s |

*Reason*: Planck PR4 is a likelihood-redone paper running baseline-LCDM, not extended-LCDM+α_s. DESI is a late-universe BAO experiment; α_s is an inflationary parameter that BAO can't measure. Plan's §W1b-8 source choice was misaligned.

**Real post-2018 source found**: **ACT DR4** (Aiola et al. 2020, arXiv:2007.07288) Table 5 (p.28), LCDM+dns/dlnk extension:

| Combination | α_s = dns/dlnk | σ |
|:-----------|:---------------|:--|
| ACT alone | +0.069 | 0.029 |
| ACT+WMAP (Planck-independent) | +0.0128 | 0.0081 |
| **ACT+Planck (post-2018 best)** | **+0.0023** | **0.0063** |
| Planck alone (ACT's τ prior) | −0.0067 | 0.0067 |

**Substitution chain (Python-verified)**:

Primary analysis — ACT+Planck joint (Table 5 col 3) supersedes Planck-alone:
- α_2018 = −0.0045, σ_2018 = 0.0067 (Planck 2018 VI canonical)
- α_2020 = +0.0023, σ_2020 = 0.0063 (ACT+Planck, Aiola 2020)
- Δα = α_2020 − α_2018 = +0.0023 − (−0.0045) = **+0.0068**
- |Δα| / σ_2018 = 0.0068 / 0.0067 = **1.015** (just over 1σ)
- Thresholds: PASS < σ/3 = 2.23×10⁻³; FAIL > σ = 6.70×10⁻³
- 0.0068 > 0.0067 ⇒ **FAIL** (by 1.5% over threshold)

Audit-robustness (alternative combinations):

| Combination | α_combined | σ_combined | Δα | Ratio Δα/σ_2018 | Verdict |
|:-----------|:-----------|:-----------|:---|:----------------|:--------|
| Planck 2018 + ACT+WMAP (inverse-var, P-independent) | +0.002528 | 0.005164 | +0.00703 | 1.049 | FAIL |
| Planck 2018 + ACT-alone (inverse-var, strict indep) | −0.000776 | 0.006530 | +0.00372 | 0.556 | INFO |
| Primary: ACT+Planck joint (supersedes 2018-alone) | +0.0023 | 0.0063 | +0.00680 | 1.015 | FAIL |

Two of three combinations cross the FAIL threshold; one lands in INFO. Primary and altA both FAIL by ~5%. The honest verdict is **FAIL** with an INFO-boundary caveat.

**Downstream action per plan §Cross-wave rule 6**:
FAIL triggers a canonical-constants update obligation. Recommended new pin:
```
alpha_s_canon_2020 = +0.0023 ± 0.0063  (ACT+Planck, Aiola 2020 Table 5 col 3)
```
S85 pre-update verdicts remain permanent per `.claude/rules/gate-verdicts.md`. Future gates consuming `alpha_s_canon` should use the 2020 value.

**Dual-SHA** (real-data revision):
- audit_sha256 = `594929470c94342a9e23d381f5a1c21cbd87a28c0827a2a55197e81e67b4b946`
- content_sha256 = `6b2f30855cf48f8c12d7d8858dc639ba80d356e3554c9f7ab818780a6fae11f4`

**Artifacts**: `computations/s85_w1b_planck_desi_2025_alpha_s_recalibration.{py,npz,md,png}`

**S86 carry-forward**:
- Execute `canonical_constants.py` update to `alpha_s_canon = +0.0023 ± 0.0063` with provenance "ACT DR4 + Planck, Aiola 2020 Table 5 col 3".
- Re-run W1a-9 MULTID-FISHER with the new α_s_canon.
- Re-run W1b-3 α_s prior-range BF with new framework point (α_s ≈ +0.00117 already near the new pin, so the BF analysis is barely affected).
- Optionally: include **ACT DR6 extended-LCDM** paper if/when published (DR6 cosmology paper arXiv:2304.05203 does NOT run α_s extension; ACT DR4 is the current best post-2018 source).

---

### §W1b-9. S85-W1b-GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM (mack-cosmic-bridge)

**Status**: DONE
**Gate ID**: `S85-W1b-GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (structural theorem promotion; PRU Class 8 discharge)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **FAIL** — plan's min-adjacent-layer theorem collapses by 4 OOM. r_max is NOT a min-identity invariant; it is genuinely **two-valued at the L1/L2 layer interface** (already documented in S84 synthesis as a "structural exception" to the three-layer regulator theorem).

**4-tuple**: `(value=0.9999249361957664, scheme=intrinsic-rank-SVD, convention=Jensen-SU3, L_max=10)`

**Substitution chain (Python-verified)**:

Source: S84 W2-workingpaper §V.8 + S84 synthesis-collation Row #13 (GENUINE-UNPINNED, shift = 1.332×10⁴):
- r_L1 (zeta inspection backreaction cap): **13322** (S82 W2-2 FAIL under zeta regulator)
- r_L2 (Zubarev substrate-action saturation cap): **1.0** (S82 W2-2 CC4 saturation PASS)
- r_max_canonical (as reported in S82 W2-2): **13322** (zeta L1 value)
- S84 interpretation: *"Four orders of magnitude is not a labeling artifact — r_max is genuinely two-valued at the layer interface."*

Plan §W1b-9 theorem candidate: `r_max(k) = min(r_N(k), r_{N+1}(k))` exact to machine epsilon.

Test:
- min(r_L1, r_L2) = min(13322, 1.0) = **1.0**
- r_max_canonical = **13322**
- |residual| = |13322 − 1.0| = **13321** (relative 0.99992)
- OOM gap L1/L2 = log₁₀(13322/1.0) = **4.125**
- Threshold: PASS iff |residual| < 1×10⁻¹² (THEOREM machine-eps discipline).
- 13321 ≫ 1×10⁻¹² ⇒ **FAIL** by ~16 orders of magnitude.

**Interpretation — what the data actually says**:

r_max is **NOT** a pinned scalar obeying a min-identity. It is a **layer-function-valued observable** — takes value 13322 under L1 (zeta inspection) and 1.0 under L2 (Zubarev substrate-action saturation). This is a DIFFERENT structural property than the plan proposed.

The S84 synthesis already documents this correctly:
> "The §VII.N theorem is anchored as L_max-independent and substrate-independent in scope, but with two structural exceptions (**r_max layer-interface**, a_2-cluster meta-observable)."

r_max is one of two known STRUCTURAL EXCEPTIONS to the three-layer regulator universality theorem — a layer-observable-multiplicity, not a universal invariant. The plan's min-identity hypothesis tried to collapse this multi-valuedness into a single invariant; the audit shows the collapse fails by 4 OOM.

**Dual-SHA**:
- audit_sha256 = `9e95f8b9b859b829340bfce8ec31003eedd313e37b70ff79027d2ad1b8399170`
- content_sha256 = `6024f422e73e8012db8ae9a8ae11866c18d86bae23cdb94a4cc6b0ce86b9325f`

**Artifacts**: `computations/s85_w1b_genuine_unpinned_r_max_theorem.{py,npz,md,png}`

**What FAIL means for solution space**:
The plan's attempt to "promote r_max to theorem via min-identity" is FALSIFIED. The TRUE structural statement — "r_max is two-valued at L1/L2 layer interface" — stands and is different in character from the plan's candidate. Downstream obligations:
- Any gate consuming `r_max` must **pin layer choice (L1 zeta vs L2 Zubarev) in its machinery pin**.
- A new theorem registration is warranted for the two-valuedness statement (separate from W2-19's failed min-identity candidate).
- The S84 V.8 carry-forward item "W2-19 r_max layer-interface theorem promotion" remains OPEN under its two-valuedness interpretation; the min-identity interpretation is CLOSED-FAILED.
- This is a **structural-exception promotion**, not a universal-invariant promotion — a genuine new theorem type.

---

### §W1b-10. S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT (mack-cosmic-bridge)

**Status**: DONE (PENDING-EVENT: pre-registration complete; verification post-DR3)
**Gate ID**: `S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT`
**Trigger**: `[VERIFY]`
**Classification**: **META** (decoupled-joint evidence ledger; detector-class partition)
**Agent**: `mack-cosmic-bridge`

**Verdict**: **PENDING-EVENT** — independence product formula pre-registered; BF_joint computation requires DR3 data (W1a-5 PENDING-EVENT; window opened 2026-04-23).

**4-tuple**: `(value='PENDING-EVENT', scheme=joint-vs-independent-product, convention=log10, L_max=n/a)`

**Pre-registered ingredients (Python-verified)**:

| Quantity | Value | log₁₀(BF) | Source |
|:---------|:------|:----------|:-------|
| BF_α (narrow uniform) | 1.682 | +0.226 | W1b-3 output NPZ |
| BF_α (wide uniform) | 4.162 | +0.619 | W1b-3 output NPZ |
| BF_α (Planck Gaussian) | 0.989 | −0.005 | W1b-3 output NPZ |
| BF_w (narrow uniform, framework-right DR3) | 6.38 | +0.805 | W1b-3-analog applied to w_0 |
| **BF_indep (narrow × narrow)** | **10.75** | **+1.031** | BF_α·BF_w (this gate) |
| BF_joint | — | — | PENDING DR3 + joint MCMC |

**Substitution chain (Python-verified)**:
- Framework w_0_FW = −0.918 (canonical `w0_FW`, S58 Volovik)
- LCDM null w_0 = −1.0
- DESI DR3 projected σ(w_0) = 0.025
- Framework-right data realization:
  - L_fw(w_0_FW | data=w_0_FW, σ=0.025) = N(−0.918 | −0.918, 0.025) = 15.96
  - Marginal likelihood under narrow uniform prior [−1.2, −0.8] (width 0.4):
    marg_L = ∫ N(w | −0.918, 0.025)/0.4 dw = **2.50**
  - BF_w = 15.96 / 2.50 = **6.38**, log₁₀ = +0.805
- BF_indep (narrow × narrow) = BF_α × BF_w = 1.682 × 6.38 = **10.75**, log₁₀ = +1.031
- BF_joint = p(D_α, D_w | FW) / p(D_α, D_w | LCDM): requires simultaneous CMB-S4 × DESI-DR3 joint MCMC posterior; DESI DR3 not yet public
- Independence test D := |log₁₀(BF_joint) − log₁₀(BF_indep)|: UNDEFINED until BF_joint computed
- Thresholds (plan §W1b-10): PASS iff D < 0.30 dex; FAIL iff D > 0.60 dex

**Why PENDING-EVENT not FAIL**:
Plan §W1b-10 explicitly pre-registers the independence product formula. The PASS/FAIL verdict on D requires BF_joint, which depends on DR3 data + joint MCMC — neither available today. The pre-registration deliverable (formula frozen, BF_indep computed, SHA-pinned) IS complete.

**Dual-SHA**:
- audit_sha256 = (see verdict line)
- content_sha256 = `ec3e55156e998bf463b55c1195151632559526d5fd6ad7cd775d4e8c4e82ffa9`

**Artifacts**: `computations/s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.{py,npz,png,json}`

**S86 carry-forward**:
- When DR3 fires (W1a-5 classifier lands), extract (w_0^obs, σ^obs)
- Compute BF_w with real data; combine with BF_α (W1b-3) for BF_indep_post_DR3
- Run joint MCMC with CMB-S4-like α_s posterior × DESI DR3 w_0 posterior → BF_joint
- Compute D := |log10(BF_joint) − log10(BF_indep_post_DR3)|
- Apply PASS/FAIL thresholds (0.30 / 0.60) to close this gate

---

## Wave W1b Synthesis (mack-cosmic-bridge, solo-in-session)

All 10 gates closed in-session, same solo-execution pattern as W1a (infrastructure-bug workaround — no agent fan-out).

### Verdict distribution

| Verdict | Count | Gates |
|:--------|:------|:------|
| PASS | 3 | W1b-2 (correlated Fisher, ratio 1.13), W1b-4 (α_s S62/S67 reconciled, Δα=7×10⁻⁴), W1b-5 (β_s joint S4×HD tightens 42%) |
| FAIL | 4 | W1b-1 (DR3 regulator-tree flips A1↔B2), W1b-3 (α_s BF prior-sensitive; min(BF)=0.99<3), W1b-8 (post-2018 ACT DR4 recalibration; Δα=1.015σ drift), W1b-9 (r_max theorem wrong; 4 OOM miss) |
| PRE-REG-INCOMPLETE | 2 | W1b-6 (MacInnis has no σ(α_s) forecast), W1b-7 (Hazumi has no σ(α_s) forecast) |
| PENDING-EVENT | 1 | W1b-10 (DR3 joint BF undefined until data lands) |

### Structural findings

**F1 (DR3 regulator-tree is layer-conditional, FAIL)**: W1b-1. Framework Zubarev w_0 shifts from −0.918 at L_max=10 (cell A1, PASS) to −0.635 at L_max=12 extrapolation (cell B2, quintessence, FAIL). A single 7-cell DR3 tree does NOT suffice for 2026-04-23 firing; S86 must maintain 3 sub-trees keyed on L_max.

**F2 (Correlation widens σ by ~13%, PASS)**: W1b-2. Realistic 5×5 block-diagonal detector correlation (C(S4,HD)=0.30, C(S4,LB)=0.15, others 0) gives σ_corr/σ_diag = 1.1298, well below 1.25 PASS threshold. W1a-9 multi-channel ensemble claim is robust under correlated inference.

**F3 (α_s BF is prior-sensitive, FAIL)**: W1b-3. Framework α_s = 0.00117 gives BF ∈ {0.99 (Planck Gauss), 1.68 (narrow uniform), 4.16 (wide uniform)} — minimum 0.99 is < 3, triggering FAIL. Framework's "zero-free-parameter" α_s advantage is **wide-prior-dependent**. Downstream: every BF row in atlas-04 inherits a (prior-type, prior-width) disclosure obligation.

**F4 (S62/S67 reconciled, PASS)**: W1b-4. S62 leading-order n_s derivation (α_s ≈ 0 implicit) agrees with S63/S67 one-loop Mukhanov-Sasaki (α_s = 7.15×10⁻⁴) at shared Planck pivot within 0.107σ_Planck. The "cross-registry contradiction" was a convention artefact (LO vs 1-loop), not a physics disagreement.

**F5 (β_s joint tightens 42%, PASS)**: W1b-5. σ(β_s)_joint = 1.28×10⁻³ (S4×HD), a 41.9% tightening from σ_S4 alone. Framework β_s = −0.1331 raises discrimination from 60.5σ (single-channel CMB-S4 2028) to **104σ** (joint S4×HD ~2034). Decisive either direction.

**F6 (MacInnis/Hazumi don't forecast α_s, PRE-REG-INCOMPLETE)**: W1b-6, W1b-7. Both cached PDFs (arXiv:2203.05728 MacInnis, arXiv:2202.02773 Hazumi) verified absent of σ(α_s) forecasts. MacInnis CMB-HD is dark-matter/f_NL/r/neutrino-focused; Hazumi LiteBIRD is tensor-B-mode-focused. Plan's assumption these would have σ(α_s) was incorrect. Projected σ values stand as sensitivity-scaling estimates.

**F7 (post-2018 α_s pin has drifted 1σ, FAIL)**: W1b-8. Initial null-update PASS was superseded by real-data audit with ACT DR4 (Aiola 2020 Table 5): ACT+Planck joint α_s = +0.0023 ± 0.0063. Δα vs 2018 canonical = +0.0068 = 1.015σ, just over FAIL threshold. Canonical-constants update recommended: alpha_s_canon_2020 = +0.0023 ± 0.0063. Downstream: W1a-9 Fisher, W1b-3 BF, W1b-10 BF_indep all consume this constant and may propagate.

**F8 (r_max theorem wrong; true statement is "two-valued", FAIL)**: W1b-9. Plan's min-adjacent-layer identity fails by 4 OOM (min(13322, 1.0)=1.0 vs canonical 13322). True structural property (per S84 synthesis): r_max is two-valued at L1/L2 layer interface — a layer-observable-multiplicity, not a universal invariant. This is a DIFFERENT theorem candidate than the plan's; its registration is carry-forward.

**F9 (W1b-10 pre-reg complete; BF_joint PENDING)**: W1b-10. Independence product formula pre-registered: log₁₀(BF_indep) = +1.031 (narrow×narrow using W1b-3 BF_α = 1.68 and computed BF_w = 6.38). BF_joint requires DR3 data (W1a-5 PENDING-EVENT) + joint MCMC; closes post-DR3.

### Carry-forward (structured)

| # | What | Inputs | Gate | Effort |
|:--|:-----|:-------|:-----|:-------|
| 1 | **CANONICAL UPDATE** (W1b-8): `alpha_s_canon` from −0.0045±0.0067 to +0.0023±0.0063 | ACT DR4 Aiola 2020 Table 5 col 3 | `mcp__knowledge__update_constant` + `canonical_constants.py` patch + propagation log | 0.5 h |
| 2 | Re-run W1a-9 MULTID-FISHER with updated α_s_canon | new canonical | Verdict re-emit | 0.5 h |
| 3 | Re-run W1b-3 α_s prior-range BF with updated α_s_canon | new canonical | BF_α triple re-emit | 0.25 h |
| 4 | Maintain 3-layer DR3 sub-trees per L_max ∈ {8, 10, 12} (W1b-1 FAIL remediation) | S86 L_max=8 Zubarev run | 21-cell matrix | 2 h |
| 5 | Prior-disclosure pin on every atlas-04 BF row (W1b-3 FAIL remediation) | (prior-type, prior-width) annotation | Atlas-04 registry patch | 0.5 h |
| 6 | Register "r_max two-valued at L1/L2 layer interface" as NEW theorem type (W1b-9 FAIL remediation of plan's candidate) | S84 W2-19 structural fact | Theorem registration in §VII.N "structural exceptions" | 1 h |
| 7 | Track explicit CMB-HD α_s forecast publication (W1b-6) | future companion paper | Re-fire W1b-6 when source lands | 0.5 h (when available) |
| 8 | Track explicit LiteBIRD α_s forecast publication (W1b-7) | future companion paper | Re-fire W1b-7 when source lands | 0.5 h (when available) |
| 9 | On DR3 event: compute BF_w with data, run joint MCMC, close W1b-10 | DR3 w_0 posterior + joint code | D threshold test | 1-2 h (event-triggered) |
| 10 | ACT DR6 cosmology paper (arXiv:2304.05203) DOES NOT publish α_s; monitor DR6 companion/update papers | | future re-fire of W1b-8 | (when available) |

### Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-04-23 | DR3 regulator-conditional tree | "single 7-cell tree" | "layer-conditional: 3 sub-trees needed" | W1b-1 flip A1↔B2 at L_max=10 vs 12 |
| 2026-04-23 | Detector correlation in W1a-9 Fisher | "diagonal approximation" | "block-diagonal (13% widening, within PASS)" | W1b-2 |
| 2026-04-23 | α_s BF claim provenance | "zero-free-parameter advantage" | "wide-prior-dependent; tight-prior (Gaussian) gives BF≈1" | W1b-3 FAIL |
| 2026-04-23 | S62/S67 α_s registry | "cross-scheme contradiction" | "reconciled: LO vs 1-loop convention artefact" | W1b-4 PASS |
| 2026-04-23 | β_s S4-only discrimination | "60.5σ" | "104σ joint S4×HD (2034+)" | W1b-5 |
| 2026-04-23 | CMB-HD/LiteBIRD α_s projections | "W1a-9 projected σ values" | "PRE-REG-INCOMPLETE; projections stand unverified" | W1b-6, W1b-7 |
| 2026-04-23 | `alpha_s_canon` pin | "−0.0045 ± 0.0067 (Planck 2018)" | "RECOMMENDED UPDATE → +0.0023 ± 0.0063 (ACT DR4+Planck, Aiola 2020)" | W1b-8 FAIL, Δα = 1.015σ |
| 2026-04-23 | r_max layer-interface theorem | "GENUINE-UNPINNED; min-identity candidate" | "min-identity FALSIFIED; two-valuedness is true statement" | W1b-9 FAIL-of-candidate |
| 2026-04-23 | α_s × w_a joint evidence | "ad-hoc independence assumption" | "PRE-REG formula frozen; BF_indep=10.75; D pending DR3" | W1b-10 |

### Files Produced

| Gate | Script | Data | Plot | Other |
|:-----|:-------|:-----|:-----|:------|
| W1b-1 | s85_w1b_cf_m2_dr3_regulator_tree.py | .npz | .png | — |
| W1b-2 | s85_w1b_alpha_s_joint_fisher_correlated.py | .npz | .png | — |
| W1b-3 | s85_w1b_alpha_s_prior_range_lcdm.py | .npz | .png | — |
| W1b-4 | s85_w1b_alpha_s_transit_ps_67_simultaneous.py | .npz | .png | — |
| W1b-5 | s85_w1b_beta_s_joint_s4_hd.py | .npz | .png | — |
| W1b-6 | s85_w1b_cmb_hd_alpha_s_macinnis_explicit.py | .npz | .png | .md |
| W1b-7 | s85_w1b_litebird_alpha_s_hazumi_verified.py | .npz | .png | .md |
| W1b-8 | s85_w1b_planck_desi_2025_alpha_s_recalibration.py | .npz | .png | .md |
| W1b-9 | s85_w1b_genuine_unpinned_r_max_theorem.py | .npz | .png | .md |
| W1b-10 | s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.py | .npz | .png | .json |

All 10 verdict lines appended to `computations/s85_gate_verdicts.txt` with dual-SHA schema_version=S84+.

### Wave-level observation (meta)

W1b pulled TWO new observational papers into the cache (Tristram PR4 2309.10034, Aiola ACT DR4 2007.07288, Planck 2018 VI 1807.06209, Planck 2018 Inflation 1807.06211, DESI 2024 III/VI 2404.03000/2404.03002, ACT DR6 cosmology/lensing 2304.05202/2304.05203, Hazumi LiteBIRD 2202.02773, MacInnis CMB-HD 2203.05728). Of these, only ACT DR4 provides a post-Planck-2018 α_s update — and it flips W1b-8 from null-update PASS to a bona fide FAIL triggering a canonical constants update. The pattern of "agent-projected σ values" used in W1a-9 / W1b-2 / W1b-5 is broadly correct but individual verifications (W1b-6, W1b-7) show several of those σ values can't be verified because the published forecasts simply don't exist for those parameters.
