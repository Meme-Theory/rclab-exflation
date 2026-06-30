# Session 85 Plan — Wave W4: little-red-dots-origin reviewer wave

**Generated**: 2026-04-21
**Wave ID**: W4
**Theme**: little-red-dots-origin single-reviewer wave — independence certification + falsifier-watchlist discipline
**Owner (planner)**: little-red-dots-jwst-analyst
**Item count**: 8
**Output (this file)**: `sessions/session-plan/session-85-plan-w4.md`
**Execution file targets**:
  - Verdicts: `computations/s85_gate_verdicts.txt` (canonical path, MANDATORY per `.claude/rules/gate-verdicts.md`)
  - Scripts: `computations/s85_w4_<slug>.py`
  - Data/plots: `computations/s85_w4_<slug>.npz` and `.png`

---

## Wave W4 Summary

W4 is the **observational-pipeline-independence** and **falsifier-watchlist** slice of S84 carry-forward. Seven of eight items are methodological pre-registrations that harden the observational forecast infrastructure already seeded in S83–S84; one item (NULL-RESULT-ELIMINATION-MAP) is a pre-registration of what each detector's null outcome would eliminate from the substrate-parameter map. No new spectral-triple eigenvalue computation is required — the wave operates on **existing** canonical constants plus published detector forecasts.

The substrate framing is *pipeline-level*: each high-z JWST LRD, each CMB-S4 α_s channel, each DESI DR3 w_0 channel is an **acoustic probe** of the fabric's fiber-transition behavior. "Independence" in this wave is the independence of *probes* in the acoustic sense: do two detectors touch the same eigenvalue-spectrum moment, or different ones? A correlated channel is one where two pipelines sample the **same** fiber-eigenvalue partition; an independent channel probes a **distinct** partition. Cross-channel correlation is therefore a substrate-geometric property, not a detector-artifact property.

### Item roster (from session-85-partition.md §W4)

| # | Slug (short) | Full gate ID | Agent | Item class |
|--:|:-------------|:-------------|:------|:-----------|
| 1 | CMB-S4-INDEP-AUG | S85-CMB-S4-ALPHA-S-FLAGSHIP-PRE-REGISTRATION-INDEPENDENCE-AUGMENT | mack-cosmic-bridge | pre-reg augment |
| 2 | XCORR-MATRIX | S85-CROSS-CHANNEL-CORRELATION-MATRIX-FORMALIZATION | mack-cosmic-bridge | pipeline formalization |
| 3 | DESI-DR3-INDEP | S85-DESI-DR3-INDEPENDENCE-DISCOUNT-EXPLICITATION | mack-cosmic-bridge | pipeline explicitation |
| 4 | FALSIFIER-WATCH-CERT | S85-FALSIFIER-WATCHLIST-INDEPENDENCE-CERTIFICATION | mack-cosmic-bridge | certification |
| 5 | KSTAR-3HEB-LAB-INDEP | S85-KSTAR-3HEB-LABORATORY-INDEPENDENCE-LEVEL-CERTIFICATION | mack-cosmic-bridge | cross-lab certification |
| 6 | MULTI-D-JFD | S85-MULTI-D-JOINT-FISHER-INDEPENDENCE-DISCOUNT | mack-cosmic-bridge | Fisher-matrix disc |
| 7 | NULL-ELIM-MAP | S85-NULL-RESULT-ELIMINATION-MAP-PRE-REGISTRATION | mack-cosmic-bridge | pre-reg |
| 8 | WATCHLIST-UPDATE | S85-WATCHLIST-MEMORY-UPDATE | mack-cosmic-bridge | memory update |

Agent-type policy per §W4-N below: all 8 items dispatch to mack-cosmic-bridge. All eight items are CPU-only (no heavy linear algebra; symbolic/text-plus-small-matrix work).

---

## Wave W4 Decision Point Prerequisites

W4 depends on the following artifacts already produced in or before S84. Each is read-only from W4's perspective:

| Prerequisite | Source | SHA-pin requirement |
|:-------------|:-------|:--------------------|
| W4 CF list (this plan's seed) | `sessions/session-plan/session-85-partition.md` §W4 | at runtime |
| S84 LRD-JWST reviewer synthesis | `sessions/archive/session-84/session-84-s4-lrd-falsifier-synthesis.md` | at runtime |
| S84 Mack S4 synthesis (detector reach) | `sessions/archive/session-84/session-84-s4-mack-falsifier-synthesis.md` | at runtime |
| CMB-S4 α_s flagship v0 (from W0/W1a) | `sessions/session-plan/session-85-plan-w0.md` §CMB-S4-ALPHA-FLAGSHIP block | at runtime |
| Permanent-results-registry | `sessions/framework/permanent-results-registry.md` | at runtime |
| EVOI framework | `sessions/evoi-framework.md` | at runtime |
| Canonical constants module | `computations/canonical_constants.py` | at runtime |
| baseline-findings S66 (for w_0, α_s centrals) | `sessions/framework/baseline-findings-s66.md` | at runtime |
| LRD watchlist (current agent memory) | `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` | at runtime |

**Decision rule for W4 launch**: W4 fires under `/rclab-coordinate` when (a) this plan file is present and (b) `computations/s85_gate_verdicts.txt` exists (may be empty). W4 does NOT wait for W0 to complete its own verdicts — W4 items are **methodology formalizations**, and they pin the **structure** of the independence audit that W0's α_s flagship will invoke, not the α_s numeric. The W0 flagship and W4-1 augment are concurrent sibling artifacts.

---

## §W4-1. S85-CMB-S4-ALPHA-S-FLAGSHIP-PRE-REGISTRATION-INDEPENDENCE-AUGMENT

**1. Gate ID**: `S85-W4-1-CMB-S4-INDEP-AUG`

**2. Trigger**: `[AUDIT]` — augments an existing pre-registration document with an *independence* section (methodology gate, not sign/direction).

**3. Classification**: NON-PHONONIC — methodology pre-registration. Detector-level independence is a pipeline property. (The α_s value it pre-registers is PHONONIC, but THIS gate only gates the *augment section*, not the α_s number.)

**4. Agent type**: mack-cosmic-bridge.

**5. Hypothesis**: The CMB-S4 α_s flagship pre-registration document (produced in W0 under CMB-S4-ALPHA-FLAGSHIP) is currently **silent** on the correlation structure between the CMB-S4 α_s channel and the 4 other discriminator channels on the watchlist (DESI DR3 w_0, LiteBIRD n_T, CMB-HD α_s, 21-cm folded-bispectrum). If left silent, the reader cannot distinguish "5 independent channels all PASS" from "5 channels with shared foreground nuisance all PASS" — a Bayes-factor inflation of up to ~N_channels on the joint. The augment closes that silence by explicitly listing what correlations are plausible and how they discount the joint evidence.

**6. Method**:

- `canonical_constants`: import `v_ew, m_H_obs, alpha_s_MZ_obs, planck_ns, w0_FW, M_KK, tau_fold` (read-only; no new constants introduced). Observation-side quantities (`sigma_alpha_s_CMB_S4`, `sigma_alpha_s_CMB_HD`, `sigma_n_T_LiteBIRD`, etc.) come from W0 flagship document; if missing, flagged to W0 and the gate registers PRE-REG-INCOMPLETE.
- `GPU/CPU policy`: CPU-only; workload is text transformation + a 5x5 correlation matrix. `OMP_NUM_THREADS=2`.
- `SHAs`: hash (a) the current W0 flagship draft, (b) the S84 mack-falsifier and LRD-falsifier syntheses, (c) permanent-results-registry, (d) baseline-findings-s66. Embed all four SHA-256 pins as the first 20 lines of script stdout.
- Script: `computations/s85_w4_cmbs4_indep_aug.py` — reads the W0 flagship markdown, parses the §Independence scaffold (or inserts one if absent), writes the augment. Emits `s85_w4_cmbs4_indep_aug.npz` carrying the 5x5 correlation matrix metadata (qualitative tags: `INDEPENDENT`, `PARTIALLY_CORRELATED`, `COMMON_MODE`) with justification strings. Emits `s85_w4_cmbs4_indep_aug.png` rendering the matrix as a heatmap.
- Output markdown append-target: `sessions/session-plan/session-85-plan-w0.md` (the W0 flagship block). W4 is the DESIGNATED WRITER for the §Independence subsection only; the rest of the W0 block remains W0's to write.

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1              # one pass through the flagship draft
L_max: N/A             # no spectral computation
scan_range: N/A
step_size: N/A
tolerance: coverage_threshold=5/5 channels addressed
scheme: "observational-pipeline"
convention: "channel-list-frozen-to-W0-flagship"
random_seed: 42        # only used for tie-breaking in qualitative tag selection, recorded for audit
GPU path: N/A (CPU-only)
input_pin_map:
  w0_flagship_draft: <computed-at-runtime>
  s84_mack_synth: <computed-at-runtime>
  s84_lrd_synth: <computed-at-runtime>
  permanent_results_registry: <computed-at-runtime>
  baseline_findings_s66: <computed-at-runtime>
```

**8. Expected output 4-tuple**:

```
(value=<correlation_matrix_coverage_fraction>, scheme=observational-pipeline,
 convention=channel-list-frozen-to-W0-flagship, L_max=NA)
```

with `correlation_matrix_coverage_fraction = (n_pairs_addressed / n_pairs_required)` where `n_pairs_required = C(5,2) = 10`. Value ∈ [0, 1].

**9. PASS / FAIL / INFO**:

- **PASS** if `correlation_matrix_coverage_fraction == 1.0` AND the augment cites the published Fisher-forecast paper for each cross-channel correlation.
- **FAIL** if `correlation_matrix_coverage_fraction < 1.0` AND no WARRANT tag is emitted (some pairs silently skipped).
- **INFO** if `correlation_matrix_coverage_fraction < 1.0` AND every skipped pair carries an explicit WARRANT-DEFERRED tag citing the missing Fisher-paper source; the gate passes its format check but defers physics-closure to a next-session follow-up.

**10. Substitution chain (SIGN / VERIFY)**:

Claim: "Omitting the §Independence section inflates the joint Bayes factor."

```
Step 1: Definition — for N channels each with individual BF_i, the JOINT
        Bayes factor under independence is BF_joint = prod_i BF_i.
Step 2: Definition — under full correlation (common-mode systematics),
        the JOINT reduces to BF_joint_corr ~ max_i BF_i (the single most
        informative channel carries essentially all the evidence; the others
        are redundant).
Step 3: Substitute N = 5, BF_i ~ k for all i (illustrative, uniform):
          BF_joint_indep = k^5
          BF_joint_corr  = k
          Ratio          = BF_joint_indep / BF_joint_corr = k^4
Step 4: Simplify: for k = 3 (a typical per-channel BF), k^4 = 81.
Step 5: Direction — reporting BF_joint_indep while the channels are actually
        correlated over-states the evidence by factor ~81. The augment
        prevents this overstatement by pinning each pair's correlation
        classification.
Conclusion: Omission inflates BF. Augment is a DEFLATIONARY correction
             (values above are illustrative; actual k per-channel is fixed
             by the W0 flagship, not by this gate).
```

**11. PASS / FAIL implications**:

- PASS — the CMB-S4 α_s flagship pre-registration is independence-aware; a future post-data Bayes-factor computation can cite the pinned correlation structure instead of assuming independence.
- FAIL — the flagship remains silent on independence; a pre-reg violation that must be remediated before the 2030 CMB-S4 data release.
- INFO — coverage incomplete but transparently deferred; the gate does not close but is not a discipline violation.

**12. Effort**: S (small, <1 hour of agent time). No heavy computation; the expensive part is reading the W0 flagship and the two S84 syntheses carefully.

**13. Substrate framing**: The 5 channels (CMB-S4 α_s, DESI DR3 w_0, LiteBIRD n_T, CMB-HD α_s, 21-cm folded-bispectrum) probe **five distinct eigenvalue-moment measurements** of the same Dirac spectrum on the fiber. "Independence" between two channels means they access non-overlapping spectral moments; "correlation" means they share a common moment. The correlation matrix is therefore a **substrate-geometric invariant**, not a detector-artifact — though in practice the pipeline-level correlation also includes CMB foreground systematics that are NON-PHONONIC. The augment documents both.

---

## §W4-2. S85-CROSS-CHANNEL-CORRELATION-MATRIX-FORMALIZATION

**1. Gate ID**: `S85-W4-2-XCORR-MATRIX`

**2. Trigger**: `[AUDIT]` — formalize the matrix that §W4-1 consumed. The matrix is a **standalone artifact** that future sessions cite; W4-1 is its first consumer.

**3. Classification**: NON-PHONONIC — pipeline-level metadata artifact. Contains PHONONIC content (fiber-eigenvalue-moment mapping) but the gate itself evaluates format compliance.

**4. Agent type**: mack-cosmic-bridge.

**5. Hypothesis**: The current 5-channel watchlist (CMB-S4 α_s, DESI DR3 w_0, LiteBIRD n_T, CMB-HD α_s, 21-cm folded-bispectrum) lacks a single canonical file that names, for each pair, (i) the correlation classification, (ii) the Fisher-paper or CMB-forecast source, (iii) which substrate-eigenvalue moment each channel probes, (iv) the post-data correlation-dependent Bayes-factor formula. Without the canonical file, each future session re-derives the matrix from memory — exactly the S58 pattern of a 100x signal being dismissed as "marginal."

**6. Method**:

- `canonical_constants`: import `alpha_s_MZ_obs, planck_ns, w0_FW` (read-only).
- `GPU/CPU policy`: CPU-only. No linear algebra; this is a markdown + YAML write.
- Script: `computations/s85_w4_xcorr_matrix.py` — constructs the matrix from a dictionary defined in the script's header; writes (a) `sessions/framework/cross-channel-correlation-matrix.md` (new file, W4 is sole writer), (b) `computations/s85_w4_xcorr_matrix.npz` containing the machine-readable matrix, (c) `computations/s85_w4_xcorr_matrix.png` (5x5 heatmap).
- The machine-readable `.npz` fields: `channels` (array of str), `correlation_tag` (5x5 str array), `source_citation` (5x5 str array), `substrate_moment` (1D str array of length 5), `bf_formula` (str).
- SHAs pinned: baseline-findings-s66, permanent-results-registry, S84 mack + LRD syntheses.

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1
L_max: N/A
scan_range: N/A
step_size: N/A
tolerance: ABSOLUTE (matrix is 5x5 = 25 cells; 100% cell-fill required for PASS)
scheme: "observational-pipeline"
convention: "5-channel-watchlist-frozen-2026-04-21"
random_seed: N/A (deterministic construction)
GPU path: N/A (CPU-only)
input_pin_map:
  baseline_findings_s66: <computed-at-runtime>
  permanent_results_registry: <computed-at-runtime>
  s84_mack_synth: <computed-at-runtime>
  s84_lrd_synth: <computed-at-runtime>
  evoi_framework: <computed-at-runtime>
```

**8. Expected output 4-tuple**:

```
(value=<filled_cell_count>/25, scheme=observational-pipeline,
 convention=5-channel-watchlist-frozen-2026-04-21, L_max=NA)
```

**9. PASS / FAIL / INFO**:

- **PASS** if `filled_cell_count == 25` AND every non-diagonal cell cites either a published Fisher paper or an explicit `FIRST-PRINCIPLES-REASONING` tag; AND every diagonal cell states the channel's substrate-moment probe.
- **FAIL** if `filled_cell_count < 25`.
- **INFO** — not used; this gate is binary on format.

**10. Substitution chain (SIGN / VERIFY)**:

Not applicable — no sign/direction/threshold claim. The gate is a **cell-count format check**; the only quantitative claim is "25 cells must be filled," which is a cardinality statement, not a physical sign.

**11. PASS / FAIL implications**:

- PASS — future sessions have a canonical correlation matrix to cite; deduplicates the S58-style re-derivation pattern.
- FAIL — structural carry-forward into S86 W1; the matrix must exist before any joint Bayes-factor computation is trusted.

**12. Effort**: S. One-script, one-session artifact.

**13. Substrate framing**: Each diagonal entry names the **fiber-eigenvalue moment** the channel probes:
- CMB-S4 α_s → running of the spectral tilt; probes the **second derivative** of the scalar transfer function at k_pivot (substrate: d²S_fold / dk² at the fold-scale projection)
- DESI DR3 w_0 → late-time dark-energy equation-of-state; probes the **zeroth spectral moment** a_0 ~ Volovik partition
- LiteBIRD n_T → tensor tilt; probes the **tensor sector** of the Dirac-spectrum (substrate: the r = 16ε relation is known INAPPLICABLE here — the phononic-framing rule pins this)
- CMB-HD α_s → independent running measurement; probes the **same** moment as CMB-S4 α_s (high diagonal correlation expected)
- 21-cm folded-bispectrum → non-Gaussianity shape; probes a **3-point** spectral moment, distinct from the 2-point α_s

The off-diagonal pattern that emerges: CMB-S4 α_s ↔ CMB-HD α_s is strongly correlated (same moment, different detectors); all other pairs are weakly correlated through common CMB foreground nuisance only.

---

## §W4-3. S85-DESI-DR3-INDEPENDENCE-DISCOUNT-EXPLICITATION

**1. Gate ID**: `S85-W4-3-DESI-DR3-INDEP`

**2. Trigger**: `[VERIFY]` — quantifies a specific numerical discount factor on joint evidence.

**3. Classification**: NON-PHONONIC — pipeline-level Fisher-matrix arithmetic. (The underlying w_0 prediction is PHONONIC; this gate evaluates detector-combination arithmetic only.)

**4. Agent type**: **mack-cosmic-bridge** (detector-Fisher-matrix domain). W4 planner (LRD) delegates this to mack because the correlation coefficient is determined by BAO-galaxy-clustering Fisher overlap with CMB, a detector-physics calculation.

**5. Hypothesis**: The DESI DR3 w_0 channel and the Planck 2018 + ACT CMB w_0 channel share a partial correlation through the BAO-CMB acoustic scale ladder. The *effective* independence factor — the "discount" applied when combining DR3 w_0 with a CMB-prior w_0 in a joint Bayes factor — is currently uncited in any S84 synthesis. This gate computes it.

**6. Method**:

- `canonical_constants`: import `w0_FW, tau_fold, M_KK`. No new constants added — the correlation coefficient ρ is an **observational input**, not a framework constant.
- `GPU/CPU policy`: CPU-only. Matrix inversion on a 2x2 correlation matrix is trivial.
- Script: `computations/s85_w4_desi_dr3_indep.py`. Input: published DESI DR3 Fisher-forecast paper (if available at runtime — if not, the script emits PRE-REG-INCOMPLETE and defers); CMB Fisher forecast (Planck 2018 public chain). Computes effective independence factor `f_indep = (1 - ρ²)^{1/2}` for the joint σ_w0.
- Output: `s85_w4_desi_dr3_indep.npz` with (ρ, f_indep, σ_w0_solo_DESI, σ_w0_solo_CMB, σ_w0_joint_corrected).
- Plot: `s85_w4_desi_dr3_indep.png` — 1-parameter curve `f_indep vs ρ` with the measured ρ marked.

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1
L_max: N/A
scan_range: ρ ∈ [0, 1] (for the plot; the point-value uses the published Fisher-paper ρ)
step_size: Δρ = 0.01 for the scan
tolerance: ABSOLUTE tolerance on f_indep = 1e-4
scheme: "observational-pipeline"
convention: "Fisher-matrix-BAO-CMB-cross-correlation"
random_seed: N/A (deterministic)
GPU path: N/A
input_pin_map:
  desi_dr3_fisher_paper: <computed-at-runtime>    # if absent → PRE-REG-INCOMPLETE
  planck_2018_fisher_chain: <computed-at-runtime>
  w0_FW_canonical: <computed-at-runtime>
  baseline_findings_s66: <computed-at-runtime>
```

**8. Expected output 4-tuple**:

```
(value=<f_indep>, scheme=observational-pipeline,
 convention=Fisher-matrix-BAO-CMB-cross-correlation, L_max=NA)
```

**9. PASS / FAIL / INFO**:

- **PASS** if the script runs to completion with a published ρ and emits f_indep ∈ (0, 1) with the 4-tuple tag. The gate does not test a physical threshold — it *pins* the discount for future joint-Bayes computations.
- **FAIL** — used only if the script errors out (e.g., the Fisher-paper SHA is present but the file is malformed).
- **INFO** — the Fisher paper is unavailable; the script emits `PRE-REG-INCOMPLETE` per `.claude/rules/gate-verdicts.md`. This is **not a FAIL** — it is an unpinned-machinery state that future sessions can resolve when DR3 publishes the Fisher paper.

**10. Substitution chain (SIGN / VERIFY)**:

Claim: "For correlated channels, f_indep < 1; the joint σ_w0 is LARGER than the naive quadrature-independent value."

```
Step 1: Definition — σ_joint_indep = (1/σ_1² + 1/σ_2²)^(-1/2)     [independent inverse-variance]
Step 2: Definition — σ_joint_corr  = (1/σ_1² + 1/σ_2² − 2ρ/(σ_1·σ_2))^(-1/2)  [correlated form
                                                                              with ρ-correction]
        Equivalently, σ_joint_corr ≥ σ_joint_indep for ρ > 0.
Step 3: Substitute σ_1 = σ_2 = σ:
          σ_joint_indep = σ / √2
          σ_joint_corr  = σ / √(2 − 2ρ) = σ · (2(1−ρ))^(-1/2)
Step 4: Simplify ratio:
          f_indep ≡ σ_joint_indep / σ_joint_corr
                 = √(2 − 2ρ) / √2
                 = √(1 − ρ)                                  [NOT √(1−ρ²); see Step 4a]
Step 4a: NOTE — the common "√(1−ρ²)" form applies to the CORRELATION COEFFICIENT of
         a single 2D Gaussian marginal. The INVERSE-VARIANCE joint discount for
         equal-σ correlated measurements simplifies to √(1−ρ) (equal-variance case)
         or must be kept in full 2x2-inverse form (unequal σ). The script MUST
         use the full 2x2 inverse-covariance computation; the analytic chain above
         is illustrative for equal σ only.
Step 5: Direction — for ρ ∈ (0, 1), √(1 − ρ) < 1, so f_indep < 1, which means
        σ_joint_indep < σ_joint_corr.
        Therefore a correlated joint has a LARGER error bar than the
        independence-assumed joint, i.e. LESS evidence, i.e. a SMALLER
        Bayes factor.
Conclusion: ρ > 0 ⇒ DISCOUNT applies (BF_corr < BF_indep). The claim's sign is verified.
            The specific discount magnitude is the script's output, NOT asserted here.
```

**Python verification** (to run during execution; included in script):

```python
# sanity check the direction claim above
rho = 0.3  # (local) illustrative
import numpy as np
Sigma_indep = np.array([[1.0, 0.0], [0.0, 1.0]])
Sigma_corr  = np.array([[1.0, rho], [rho, 1.0]])
Finv_indep = np.linalg.inv(Sigma_indep)
Finv_corr  = np.linalg.inv(Sigma_corr)
# 1D joint marginal variance via w^T C w with equal weights
w = np.array([0.5, 0.5])
var_indep = w @ Sigma_indep @ w
var_corr  = w @ Sigma_corr  @ w
assert var_indep < var_corr, "direction claim broken: independent σ must be SMALLER"
```

**11. PASS / FAIL implications**:

- PASS — the canonical correlation matrix (§W4-2) has a pinned numerical entry for the DESI-DR3 ↔ CMB-Planck cell.
- INFO (Fisher-paper unavailable) — the cell carries a `WARRANT-DEFERRED` tag; the matrix still passes §W4-2 format check because the tag is explicit.
- FAIL — only if the script errors out; unlikely.

**12. Effort**: S-M (small to medium, ~1-2 hours). The arithmetic is trivial; the complexity is in parsing the Fisher-paper notation and extracting the correct cross-correlation coefficient.

**13. Substrate framing**: The CMB acoustic scale and the BAO acoustic scale are **the same fiber-eigenvalue ruler**, measured at different cosmic epochs. Their substrate-level correlation is therefore ~1 (near-perfect common mode) on the ruler itself; what dis-correlates them is the different redshift-evolution history of nuisance foregrounds (Planck dust vs DESI galaxy bias). The numerical ρ that falls out is the pipeline-level correlation, which is a mixture of the substrate-ruler correlation (~1) diluted by independent nuisance parameters (< 1).

---

## §W4-4. S85-FALSIFIER-WATCHLIST-INDEPENDENCE-CERTIFICATION

**1. Gate ID**: `S85-W4-4-FALSIFIER-WATCH-CERT`

**2. Trigger**: `[AUDIT]` — certifies that every item on the 5-channel falsifier watchlist has a pinned independence classification.

**3. Classification**: NON-PHONONIC — pipeline-level certification gate.

**4. Agent type**: mack-cosmic-bridge.

**5. Hypothesis**: The "falsifier watchlist" — the live set of detectors that will deliver α_s, w_0, n_T, and folded-bispectrum measurements in the 2026–2030 window — is currently tracked across several places (LRD MEMORY, mack MEMORY, evoi-framework, baseline-findings-s66) without a single certification that each channel has a pinned independence classification. This gate produces that certification as a checklist.

**6. Method**:

- `canonical_constants`: import `w0_FW, alpha_s_MZ_obs, planck_ns`.
- `GPU/CPU policy`: CPU-only.
- Script: `computations/s85_w4_falsifier_watch_cert.py`. Inputs: `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md`, `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md`, `sessions/evoi-framework.md`, `sessions/framework/baseline-findings-s66.md`, and (if present after §W4-2) `sessions/framework/cross-channel-correlation-matrix.md`.
- For each of the 5 watchlist channels, the script writes a certification row: (channel, detector, expected-data-year, σ prediction pinned, independence classification from §W4-2 matrix, EVOI from evoi-framework).
- Output: `s85_w4_falsifier_watch_cert.npz` (structured array), `s85_w4_falsifier_watch_cert.png` (tabular visualization).

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1
L_max: N/A
scan_range: 5 channels
step_size: N/A
tolerance: coverage_threshold=5/5 channels certified
scheme: "observational-pipeline"
convention: "5-channel-watchlist-v2026-04-21"
random_seed: N/A
GPU path: N/A
input_pin_map:
  lrd_memory: <computed-at-runtime>
  mack_memory: <computed-at-runtime>
  evoi_framework: <computed-at-runtime>
  baseline_findings_s66: <computed-at-runtime>
  xcorr_matrix_file: <computed-at-runtime>   # from §W4-2, may be INCOMPLETE
```

**8. Expected output 4-tuple**:

```
(value=<n_certified>/5, scheme=observational-pipeline,
 convention=5-channel-watchlist-v2026-04-21, L_max=NA)
```

**9. PASS / FAIL / INFO**:

- **PASS** if `n_certified == 5` AND the xcorr matrix is available (§W4-2 PASS).
- **INFO** if `n_certified == 5` but the xcorr matrix is incomplete (§W4-2 INFO); certification is format-complete but one or more independence cells are WARRANT-DEFERRED.
- **FAIL** if `n_certified < 5`.

**10. Substitution chain (SIGN / VERIFY)**: Not applicable. Pure coverage count.

**11. PASS / FAIL implications**:

- PASS — the watchlist has a sealed certification entry that new sessions cite rather than re-derive. Closes the recurring "which detectors are we watching?" query in agent memory.
- INFO — certification passes format but cites a deferred xcorr cell; acceptable.
- FAIL — new watchlist rows must be added to the certification before close.

**12. Effort**: S.

**13. Substrate framing**: Each watchlist channel is a **future acoustic-probe measurement** of the substrate eigenvalue spectrum. The certification is the registry entry that tells future agents: "this detector touches THIS fiber-moment, has THIS independence status, and has THIS predicted signal." It is the substrate-measurement equivalent of a particle-physics experimental plan: what we will listen to, in what frequency band, with what cross-talk from neighboring bands.

---

## §W4-5. S85-KSTAR-3HEB-LABORATORY-INDEPENDENCE-LEVEL-CERTIFICATION

**1. Gate ID**: `S85-W4-5-KSTAR-3HEB-LAB-INDEP`

**2. Trigger**: `[AUDIT]` — certifies the independence level between CMB-cosmological channels and **laboratory** (K-STAR, ³He-B) analog-substrate channels.

**3. Classification**: PHONONIC — a cross-lab certification is a direct statement about how laboratory acoustic-fiber probes relate to cosmological-acoustic probes. This is the substrate-inheritance claim made explicit.

**4. Agent type**: mack-cosmic-bridge.

**5. Hypothesis**: Laboratory analogs (K-STAR tokamak density-cascade, ³He-B Leggett-mode spectroscopy) probe the **same spectral triple** as cosmological CMB-S4 / DESI at vastly different energy scales. They are therefore **structurally correlated at the substrate level** (same eigenvalue problem) but **pipeline-independent** (different detectors, different nuisance systematics). The gate classifies this compound independence level as `SUBSTRATE-CORRELATED + PIPELINE-INDEPENDENT` for each of the 5 watchlist channels.

**6. Method**:

- `canonical_constants`: import `tau_fold, Delta_BCS, v_ew, M_KK, c_fabric`.
- `GPU/CPU policy`: CPU-only.
- Script: `computations/s85_w4_kstar_3heb_lab_indep.py`. For each of the 5 cosmological channels, identify the corresponding laboratory analog (if any), name the fiber-moment the analog probes, and classify the substrate-level correlation as `HIGH/MED/LOW` and the pipeline-level independence as `INDEPENDENT/PARTIALLY-INDEPENDENT`.
- Output: `s85_w4_kstar_3heb_lab_indep.npz` (structured certification table), `.png` (bipartite graph: cosmo channels ↔ lab analogs).

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1
L_max: N/A
scan_range: 5 cosmological × 2 lab-analog domains
step_size: N/A
tolerance: coverage_threshold=5 channels with explicit analog or explicit NO-ANALOG tag
scheme: "lab-cosmo-analog"
convention: "3HeB-primary + KSTAR-secondary"
random_seed: N/A
GPU path: N/A
input_pin_map:
  volovik_convergence_doc: <computed-at-runtime>     # project_volovik-convergence.md
  substrate_inheritance_doc: <computed-at-runtime>   # project_3heb-inheritance.md
  lrd_memory: <computed-at-runtime>
  permanent_results_registry: <computed-at-runtime>
```

**8. Expected output 4-tuple**:

```
(value=<n_analogged>/5, scheme=lab-cosmo-analog,
 convention=3HeB-primary+KSTAR-secondary, L_max=NA)
```

**9. PASS / FAIL / INFO**:

- **PASS** if every channel either has a named analog or an explicit `NO-ANALOG` tag with justification.
- **FAIL** if any channel is silent on its analog status.
- **INFO** if a channel's analog is uncertain (candidate analog exists but experimental parameter-match uncomputed); tagged `ANALOG-CANDIDATE-UNVERIFIED` and passed through.

**10. Substitution chain (SIGN / VERIFY)**:

Claim: "Substrate-correlated but pipeline-independent channels give MORE joint evidence than purely pipeline-independent ones."

```
Step 1: Definition — two channels are substrate-correlated if they probe the
        SAME eigenvalue-moment of D_K but via different experimental pipelines.
Step 2: Definition — for Bayesian joint evidence, what matters is the
        LIKELIHOOD correlation, which is driven by SHARED NUISANCE PARAMETERS
        (detector systematics), NOT by the underlying theory parameter.
Step 3: Substitute — two substrate-correlated, pipeline-independent channels
        have identical THEORY-parameter response but INDEPENDENT nuisance
        parameters.
        Therefore their likelihood functions on the theory parameter MULTIPLY
        cleanly (up to tightly-correlated theory response, which acts as a
        single stronger constraint).
Step 4: Simplify — for a single theory parameter θ with two substrate-correlated
        channels i=1,2:
          L_joint(θ) = L_1(θ | nuisance_1) × L_2(θ | nuisance_2)
        with nuisance_1 ⊥ nuisance_2 by assumption of pipeline-independence.
        This is THE SAME multiplicative structure as two independent
        measurements — so the effective information content doubles.
Step 5: Direction — substrate-correlated + pipeline-independent channels give
        EFFECTIVELY INDEPENDENT evidence at the JOINT level (noise-independent),
        even though they probe the same physics parameter.
        This is STRONGER than two purely pipeline-independent channels probing
        different theory parameters, because the shared theory parameter
        combines linearly in log-likelihood (additive information).
Conclusion: lab-analog cross-correlation is a JOINT-EVIDENCE MULTIPLIER when
            the pipelines are nuisance-independent. The sign of the effect is
            POSITIVE on joint BF.
```

**11. PASS / FAIL implications**:

- PASS — the certification names laboratory analogs that amplify joint evidence for 5 cosmological predictions.
- INFO — candidate analogs exist but need lab-parameter matching (future session).
- FAIL — fundamental gap in cross-lab documentation; blocks LRD watchlist discipline.

**12. Effort**: M. Requires careful reading of `project_3heb-inheritance.md` and `project_volovik-convergence.md` to map each cosmological channel to the correct laboratory analog.

**13. Substrate framing**: This gate is the **most fundamentally phononic** of the W4 items. The claim that a K-STAR density-cascade experiment and a DESI DR3 w_0 measurement probe the **same eigenvalue moment** of D_K — one in the laboratory, one across cosmic epochs — is the statement that the substrate inheritance holds. Failure here would indicate the laboratory-cosmology bridge (established across S59-S60) is less tight than previously claimed. PASS confirms it.

---

## §W4-6. S85-MULTI-D-JOINT-FISHER-INDEPENDENCE-DISCOUNT

**1. Gate ID**: `S85-W4-6-MULTI-D-JFD`

**2. Trigger**: `[VERIFY]` — Fisher-matrix arithmetic for N-channel joint evidence.

**3. Classification**: NON-PHONONIC — Fisher-matrix arithmetic.

**4. Agent type**: **mack-cosmic-bridge** (detector-Fisher-matrix specialty).

**5. Hypothesis**: The 5-channel (or, more generally, N-channel) joint Fisher matrix for the substrate parameter vector θ = (τ_fold, M_KK, K_substrate, convention-A tag, ...) has an **off-diagonal structure** that, when inverted, gives joint-parameter uncertainties significantly tighter than the per-channel diagonal would suggest. This gate computes the inversion and emits the per-parameter joint-σ vector plus the independence-discount factor vector.

**6. Method**:

- `canonical_constants`: import `tau_fold, M_KK` (read-only); no new constants introduced.
- `GPU/CPU policy`: CPU-only. 5×5 (or up to 10×10) Fisher-matrix inversion is trivial on CPU.
- Script: `computations/s85_w4_multi_d_jfd.py`. Input: published Fisher matrices from each detector (CMB-S4, DESI DR3, LiteBIRD, CMB-HD, 21-cm). Cross-correlation entries come from §W4-2. Constructs the full N-channel × M-parameter Fisher matrix, inverts, extracts per-parameter joint σ.
- Output: `s85_w4_multi_d_jfd.npz` (F_full matrix, F_inv, σ_joint, σ_per_channel, discount_factor_vector), `s85_w4_multi_d_jfd.png` (bar chart: σ_per_channel / σ_joint per parameter).

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1                          # one inversion
L_max: N/A
scan_range: N_channels ∈ {3, 4, 5} (progressive-inclusion robustness check)
step_size: +1 channel
tolerance: ABSOLUTE 1e-6 on F_full @ F_inv = I
scheme: "observational-pipeline"
convention: "Fisher-matrix-joint-GAUSSIAN-marginal"
random_seed: N/A
GPU path: N/A (numpy.linalg.inv on 5x5 matrix, CPU sufficient)
input_pin_map:
  cmbs4_fisher_paper: <computed-at-runtime>
  desi_dr3_fisher_paper: <computed-at-runtime>
  litebird_fisher_paper: <computed-at-runtime>
  cmb_hd_fisher_paper: <computed-at-runtime>
  hera_21cm_fisher_paper: <computed-at-runtime>
  xcorr_matrix_file: <computed-at-runtime>   # §W4-2
```

**8. Expected output 4-tuple**:

```
(value=<geometric_mean_discount_factor>, scheme=observational-pipeline,
 convention=Fisher-matrix-joint-GAUSSIAN-marginal, L_max=NA)
```

**9. PASS / FAIL / INFO**:

- **PASS** if the inversion completes with the identity check below 1e-6 AND all 5 Fisher papers are available. Emit the discount vector as the pinned joint-evidence calibration.
- **INFO** if ≥ 1 Fisher paper is unavailable; script emits a partial N-channel joint and flags `WARRANT-DEFERRED` for the missing channels.
- **FAIL** if the inversion numerically fails (singular Fisher matrix) — would indicate a cross-correlation entry outside the valid Fisher regime; diagnostic signal.

**10. Substitution chain (SIGN / VERIFY)**:

Claim: "For N-channel joint Fisher with positive-definite off-diagonals, the joint σ is LESS THAN OR EQUAL TO any single-channel σ, with equality only when all other Fisher contributions are zero."

```
Step 1: Definition — F_full is the symmetric positive-semidefinite Fisher matrix
        on N channels × M parameters (for a single parameter, F is N × N with
        Fisher eigenvalues strictly positive for any real detector).
Step 2: Definition — σ_joint(θ_j) = [F_inv]_{jj}^(1/2)
Step 3: Definition — σ_single_i(θ_j) = [F_single_i]_{jj}^(-1/2) where F_single_i is
        the sub-Fisher from channel i alone.
Step 4: Substitute — because F_full = Σ_i F_single_i (for diagonal-prior-independent
        channels), adding any positive-definite F_single_i increases F_full in
        the positive-semidefinite sense, which DECREASES the diagonal of F_inv.
Step 5: Simplify — if F_full − F_single_i ≥ 0 (PSD ordering), then
        [F_full^{-1}]_{jj} ≤ [F_single_i^{-1}]_{jj}, so
        σ_joint(θ_j) ≤ σ_single_i(θ_j).
Step 6: Direction — joint-Fisher σ is ≤ single-channel σ.
        Discount factor = σ_joint / σ_single_i ≤ 1.
Conclusion: The discount factor vector has all entries ≤ 1; its geometric
            mean is the scalar summary this gate emits. The equality case
            applies only in degenerate Fisher contributions.
```

**Python verification** (to run in script):

```python
import numpy as np
F1 = np.diag([100.0, 50.0])
F2 = np.diag([80.0, 60.0])
F_full = F1 + F2
s_joint  = np.sqrt(np.diag(np.linalg.inv(F_full)))
s_single = np.sqrt(np.diag(np.linalg.inv(F1)))
assert np.all(s_joint <= s_single + 1e-12), "joint must be <= single"
```

**11. PASS / FAIL implications**:

- PASS — pinned discount factors let §W4-7 write its null-result elimination map with correct per-parameter σ-budgets.
- INFO — partial Fisher coverage; next-session carry-forward entry to refresh when the missing detector forecasts publish.
- FAIL — signals a degeneracy in the constructed cross-correlation, i.e. a methodological error in §W4-2; escalate to W4-2 re-run.

**12. Effort**: M. The complexity is in extracting Fisher entries from published papers; the arithmetic is 10 lines of numpy.

**13. Substrate framing**: The multi-D Fisher matrix is the **joint acoustic sensitivity** of the detector ensemble to the substrate parameter vector. Each eigenvalue of F_full is a joint-mode sensitivity — a linear combination of substrate parameters that the ensemble measures most tightly. The discount vector tells us which substrate-parameter directions (τ_fold? M_KK?) become sharply constrained by joint observation, and which remain loosely constrained even after combining all 5 channels.

---

## §W4-7. S85-NULL-RESULT-ELIMINATION-MAP-PRE-REGISTRATION

**1. Gate ID**: `S85-W4-7-NULL-ELIM-MAP`

**2. Trigger**: `[AUDIT]` — pre-registers what each detector's NULL result would eliminate from substrate-parameter space.

**3. Classification**: NON-PHONONIC (pre-registration artifact); the ELIMINATIONS it catalogs are PHONONIC.

**4. Agent type**: mack-cosmic-bridge.

**5. Hypothesis**: If CMB-S4 reports `α_s = -0.003 ± 0.002` at 2030 — essentially the LCDM value, far from the framework's −0.069 ± 0.008 prediction — the framework's prediction is falsified at ~8σ. If DESI DR3 reports `w_0 = -1.000 ± 0.015` — no deviation from LCDM — the Volovik-partition prediction w_0 = −0.918 is falsified at ~5σ. Similar null-result implications exist for each of the 5 channels. Pre-registering these null-result consequences BEFORE the data arrives is standard falsifier discipline.

**6. Method**:

- `canonical_constants`: import framework centrals (`w0_FW`, `alpha_s_MZ_obs`, `planck_ns`) and observational centrals.
- `GPU/CPU policy`: CPU-only.
- Script: `computations/s85_w4_null_elim_map.py`. For each of 5 channels, computes: framework prediction `x_FW ± σ_FW`, LCDM central `x_LCDM`, null-result σ-distance `(x_FW − x_LCDM) / σ_detector_forecast`. Emits elimination table.
- Output: `s85_w4_null_elim_map.npz` (table), `s85_w4_null_elim_map.png` (σ-distance bar plot).

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1
L_max: N/A
scan_range: 5 channels
step_size: N/A
tolerance: coverage_threshold=5/5 channels with null-sigma entry
scheme: "falsifier-sigma-distance"
convention: "framework-minus-LCDM-over-detector-sigma"
random_seed: N/A
GPU path: N/A
input_pin_map:
  baseline_findings_s66: <computed-at-runtime>
  permanent_results_registry: <computed-at-runtime>
  evoi_framework: <computed-at-runtime>
  xcorr_matrix_file: <computed-at-runtime>        # from §W4-2
  multi_d_jfd_file: <computed-at-runtime>         # from §W4-6 for joint-σ inputs
```

**8. Expected output 4-tuple**:

```
(value=<n_channels_with_null_sigma_pinned>/5,
 scheme=falsifier-sigma-distance,
 convention=framework-minus-LCDM-over-detector-sigma, L_max=NA)
```

**9. PASS / FAIL / INFO**:

- **PASS** if all 5 channels have computed null-result σ-distance, AND each σ-distance carries a pre-registered falsifier consequence (e.g., "if null, the Volovik-partition branch is closed").
- **INFO** if <5 channels populated but remainder carry `WARRANT-DEFERRED` with named detector-forecast-paper pending.
- **FAIL** if <5 channels AND no deferral tag.

**10. Substitution chain (SIGN / VERIFY)**:

Claim: "A framework prediction x_FW that differs from LCDM by n_σ detector-σ is falsified at n_σ confidence if the detector null-result hits the LCDM value."

```
Step 1: Definition — the detector's 1σ error on the measured value is σ_detect.
Step 2: Definition — a null result is measured value = x_LCDM with uncertainty σ_detect.
Step 3: Substitute — the tension between x_measured = x_LCDM and x_FW is:
          Δ = (x_FW − x_LCDM) / σ_detect
Step 4: Simplify — |Δ| is the number of σ by which the framework prediction
        differs from the null central. Under the null, the framework is
        disfavored at |Δ|-σ in a gaussian likelihood.
Step 5: Direction — larger |x_FW − x_LCDM| or smaller σ_detect BOTH increase |Δ|,
        BOTH increase falsification strength. This is the standard σ-distance
        falsifier logic.
Conclusion: The sign convention is: positive |Δ| ⇔ framework distinguishable
            from null ⇔ falsifiable. The table uses signed Δ to preserve
            directionality (framework above/below LCDM).
```

**11. PASS / FAIL implications**:

- PASS — pre-registered null-elimination map is locked in; agent memory carries it forward; post-2030 null results trigger automatic branch closure.
- INFO — partial coverage; acceptable if missing entries are deferred to published Fisher papers.
- FAIL — falsifier discipline failure; blocks W4-4 certification from going to PASS.

**12. Effort**: S-M.

**13. Substrate framing**: The null-result elimination map is the **falsifier geometry** of the substrate parameter space. Each σ-distance entry marks how far the framework's pinned eigenvalue-moment prediction lives from the LCDM null, measured in units of detector acoustic-sensitivity. A large σ-distance means the framework has staked out a falsifiable region; a small σ-distance means the detector cannot distinguish framework from LCDM. The map is the substrate-discrimination survey of the 2026–2030 observational window.

---

## §W4-8. S85-WATCHLIST-MEMORY-UPDATE

**1. Gate ID**: `S85-W4-8-WATCHLIST-UPDATE`

**2. Trigger**: `[AUDIT]` — agent-memory housekeeping gate.

**3. Classification**: NON-PHONONIC — metadata / agent-memory update.

**4. Agent type**: mack-cosmic-bridge.

**5. Hypothesis**: The LRD-JWST-analyst agent memory (`MEMORY.md` and topic files) currently tracks 5 live observational tests (w_0, w_a, g_1/g_2, α_s, proton lifetime, H_0) but the format has drifted: some entries carry σ-distance, others don't; some cite Fisher papers, others don't; the xcorr classification produced in §W4-2 is not yet in memory. This gate audits and updates memory to the uniform post-W4 format.

**6. Method**:

- `canonical_constants`: not imported (this is a memory-file operation, not a physics computation).
- `GPU/CPU policy`: CPU-only (file I/O).
- Script: `computations/s85_w4_watchlist_update.py`. Reads current memory, applies the unified format (every channel row carries: prediction, σ prediction, detector, detector-σ, σ-distance, xcorr classification, EVOI, Fisher-paper SHA or WARRANT-DEFERRED). Writes the updated memory file and an audit diff file.
- Output: `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` (updated by this gate; THIS GATE IS SOLE WRITER), `.claude/agent-memory/little-red-dots-jwst-analyst/project_watchlist-v85.md` (new detail file), `s85_w4_watchlist_update.npz` (pre/post diff), `s85_w4_watchlist_update.png` (diff visualization).

**7. Machinery pin (PRDR)**:

```yaml
schema_version: R3
N_eval: 1
L_max: N/A
scan_range: N_watchlist_items (currently 5, may extend to 6 if proton-lifetime or H_0 is promoted)
step_size: N/A
tolerance: coverage_threshold=100% format-compliance after update
scheme: "agent-memory-format-v85"
convention: "unified-row-schema"
random_seed: N/A
GPU path: N/A
input_pin_map:
  lrd_memory_current: <computed-at-runtime>
  xcorr_matrix_file: <computed-at-runtime>        # from §W4-2
  falsifier_cert_file: <computed-at-runtime>      # from §W4-4
  null_elim_map_file: <computed-at-runtime>       # from §W4-7
```

**8. Expected output 4-tuple**:

```
(value=<rows_compliant>/<rows_total>, scheme=agent-memory-format-v85,
 convention=unified-row-schema, L_max=NA)
```

**9. PASS / FAIL / INFO**:

- **PASS** if rows_compliant / rows_total = 1.0 post-update AND the diff file records the pre-state for audit.
- **INFO** — not applicable (pure format gate).
- **FAIL** if any row fails format compliance post-update; signals a bug in the updater script.

**10. Substitution chain**: Not applicable (format gate, no physical claim).

**11. PASS / FAIL implications**:

- PASS — agent memory is now unified with the wave's new artifacts (xcorr matrix, falsifier cert, null-elim map); future LRD sessions start from the same ground state.
- FAIL — carry-forward diagnostic: the updater script needs a fix.

**12. Effort**: S.

**13. Substrate framing**: The watchlist is the **acoustic-probe roster** — the set of measurements that will interrogate the substrate's fiber-transition behavior between 2026 and 2030. Keeping the roster in a unified format across agent-memory is the minimum discipline for the "Eddington bias test + selection effect test + alternative explanation test" methodology that the LRD-JWST-analyst role owes to the framework.

---

## Wave W4 → Wave W5 Decision Point

**Decision artifacts from W4 (required by subsequent waves)**:

| Artifact | Consumer | Consumed how |
|:---------|:---------|:-------------|
| `sessions/framework/cross-channel-correlation-matrix.md` (§W4-2) | W0 α_s flagship; W5 Lizzi wave; all future joint-Bayes-factor work | cited |
| `s85_w4_desi_dr3_indep.npz` (§W4-3) | W1a-b Mack waves (DESI-DR3 live-watch, successor tree); all w_0 joint reasoning | matrix entry |
| `s85_w4_falsifier_watch_cert.npz` (§W4-4) | W1a Mack wave (falsifier-monitor CF-M5); W13 Tesla (CGWB/α_s preregs) | citation |
| `s85_w4_multi_d_jfd.npz` (§W4-6) | W1b Mack wave (multi-D Fisher); W7 transit wave (cross-scale audits) | Fisher-inv |
| `s85_w4_null_elim_map.npz` (§W4-7) | W1a Mack wave; W13 Tesla wave; agent memory refresh | pre-registered null |
| Updated LRD agent memory (§W4-8) | All future LRD-JWST-analyst dispatches | startup context |

**W5 launch condition**: W5 (lizzi-origin) is independent of W4 artifacts (no theme overlap with observational pipelines); W5 may launch in parallel with W4 without waiting on W4 verdicts, per the Batch-1 concurrent-dispatch plan in session-85-partition.md §Dispatch batching.

**Downstream consumers (post-Batch-2)**: Batch 2 waves W7–W13 that cite W4 artifacts MAY start before W4 final verdicts if they treat the artifacts as `WARRANT-DEFERRED` placeholders and log a carry-forward note. Agents dispatched in Batch 2 are instructed (in their prompts) to query the W4 verdict file and either read the pinned artifact or tag the missing artifact citation accordingly.

---

## Wave W4 Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness (PRDR), this block enumerates every free parameter across all 8 gates to prevent PRU Class 8 vulnerability.

| Gate | Free parameter | PIN value |
|:-----|:---------------|:----------|
| W4-1 | N_eval | 1 |
| W4-1 | tolerance | coverage_threshold=5/5 |
| W4-1 | convention | channel-list-frozen-to-W0-flagship |
| W4-1 | scheme | observational-pipeline |
| W4-1 | random_seed | 42 (tie-break only) |
| W4-2 | tolerance | ABSOLUTE cell-count=25 |
| W4-2 | convention | 5-channel-watchlist-frozen-2026-04-21 |
| W4-3 | scan_range (plot) | ρ ∈ [0, 1] |
| W4-3 | step_size | Δρ = 0.01 |
| W4-3 | tolerance | ABSOLUTE 1e-4 on f_indep |
| W4-3 | convention | Fisher-matrix-BAO-CMB-cross-correlation |
| W4-4 | tolerance | coverage_threshold=5/5 |
| W4-4 | convention | 5-channel-watchlist-v2026-04-21 |
| W4-5 | tolerance | coverage_threshold=5/5 with NO-ANALOG allowed |
| W4-5 | convention | 3HeB-primary + KSTAR-secondary |
| W4-6 | scan_range | N_channels ∈ {3, 4, 5} |
| W4-6 | tolerance | ABSOLUTE 1e-6 on F @ F_inv = I |
| W4-6 | convention | Fisher-matrix-joint-GAUSSIAN-marginal |
| W4-7 | tolerance | coverage_threshold=5/5 |
| W4-7 | convention | framework-minus-LCDM-over-detector-sigma |
| W4-7 | scheme | falsifier-sigma-distance |
| W4-8 | tolerance | coverage_threshold=100% post-update |
| W4-8 | convention | unified-row-schema |
| W4-8 | scheme | agent-memory-format-v85 |

**PRU audit expectation**: After W4 execution, `computations/_pru_cardinality_audit.py` should report `D_PRU_raw = 0` for all 8 W4 gates. If any gate reports `D_PRU_raw > 0`, the V3 Stage-1 recovery procedure from `.claude/rules/v3-closure-recovery.md` applies (max 2 re-dispatches per signal).

---

## Wave W4 Input-SHA Ledger

SHA-256 pins for every file read by ≥1 W4 gate (all `<computed-at-runtime>` in the scripts themselves; this table names the files):

| File | Read by gates |
|:-----|:--------------|
| `sessions/session-plan/session-85-plan-w0.md` (W0 α_s flagship block) | W4-1 |
| `sessions/archive/session-84/session-84-s4-mack-falsifier-synthesis.md` | W4-1, W4-2 |
| `sessions/archive/session-84/session-84-s4-lrd-falsifier-synthesis.md` | W4-1, W4-2, W4-4 |
| `sessions/framework/permanent-results-registry.md` | W4-1, W4-2, W4-4, W4-5, W4-7 |
| `sessions/framework/baseline-findings-s66.md` | W4-1, W4-2, W4-4, W4-7 |
| `sessions/evoi-framework.md` | W4-1, W4-4, W4-7 |
| `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` | W4-4, W4-8 |
| `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md` | W4-4 |
| `computations/canonical_constants.py` | W4-1, W4-2, W4-3, W4-5, W4-6, W4-7 |
| Published DESI DR3 Fisher-forecast paper (runtime-dependent) | W4-3, W4-6 |
| Published Planck 2018 Fisher chain | W4-3 |
| Published CMB-S4 Fisher paper | W4-6 |
| Published LiteBIRD Fisher paper | W4-6 |
| Published CMB-HD Fisher paper | W4-6 |
| Published 21-cm HERA Fisher paper | W4-6 |
| `sessions/framework/cross-channel-correlation-matrix.md` (created by W4-2) | W4-4, W4-6, W4-7, W4-8 |
| `.claude/agent-memory/little-red-dots-jwst-analyst/project_volovik-convergence.md` | W4-5 |
| `.claude/agent-memory/little-red-dots-jwst-analyst/project_3heb-inheritance.md` | W4-5 |
| `computations/s85_w4_xcorr_matrix.npz` (created by W4-2) | W4-6 |
| `computations/s85_w4_multi_d_jfd.npz` (created by W4-6) | W4-7 |
| `computations/s85_w4_falsifier_watch_cert.npz` (created by W4-4) | W4-8 |
| `computations/s85_w4_null_elim_map.npz` (created by W4-7) | W4-8 |

**Internal W4 dependency graph** (producers → consumers):

```
W4-2 (xcorr matrix) ──┬──► W4-4 (falsifier cert)
                      ├──► W4-6 (multi-D Fisher)
                      └──► W4-7 (null-elim map)
                                   │
W4-6 (multi-D Fisher) ─────────────┤
                                   ▼
W4-4 (falsifier cert) ────────►  W4-8 (watchlist memory update)
W4-7 (null-elim map)  ────────►  W4-8
W4-1, W4-3, W4-5  stand alone (no internal dependencies beyond canonical)
```

Execution order under `/rclab-coordinate`: W4-2 must PASS before W4-4, W4-6, W4-7 launch. W4-8 is last (consumes W4-4, W4-6, W4-7). W4-1, W4-3, W4-5 are launchable in the first parallel batch alongside W4-2. This fits within the CONCURRENCY_CAP=8 envelope comfortably.

---

**End of Wave W4 plan.**
