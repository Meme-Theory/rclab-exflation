# Session 87 Plan — Wave 1b: PV / d_eff / L_max sweep / Open-Q (W-1 split-b)

**Generated**: 2026-04-27
**Wave owner**: `gen-physicist` (cross-domain refutation/diagnostic; 6 W-1 carry-forwards CF-8..CF-13)
**Verdict file (canonical)**: `computations/s87_gate_verdicts.txt`
**Script prefix**: `s87_w1b_<gate-slug>.py` (in `computations/`)
**Schema**: R3 (`schema_version: R3` in every gate block)
**Source carry-forwards**: `sessions/archive/session-86/compute-carryforward.md` rows CF-8..CF-13 (verbatim Brief column preserved in §W1b-1..§W1b-6 below)

---

## Wave 1b Summary

W1b is the second half of the S86 W-1 split — the refutation/diagnostic/open-question half of the gen-physicist carry-forward stack. W1a covers the 7 registry-landing CF-1..CF-7 items (Mellin-Strip / Mellin-Cone no-go / W3-per-eval / lizzi anchor / cross-program unification / M2 necessity / VII.PROP routing). W1b covers the 6 follow-on diagnostic + open-question CF-8..CF-13 items.

**Gate-by-gate map:**

| § | Gate ID | CF | Trigger | Classification | Verdict band |
|:--|:--------|:---|:--------|:--------------|:-------------|
| §W1b-1 | `S87-PV-SUBTRACTION-RECALIBRATION` | CF-8 | [VERIFY] [SIGN] | GEOMETRIC | PASS / INFO / FAIL — directional |
| §W1b-2 | `S87-D-EFF-ANCHOR-VERIFICATION` | CF-9 | [VERIFY] [AUDIT] | GEOMETRIC | PASS / INFO / FAIL — ordering |
| §W1b-3 | `S87-LMAX-WEYL-CONVERGENCE-SWEEP` (CONDITIONAL) | CF-10 | [VERIFY] | GEOMETRIC | PASS / INFO / FAIL — convergence |
| §W1b-4 | `S87-PAIRED-SLOT-RATIO-INTERPRETATION` (OPEN-Q) | CF-11 | [AUDIT] | GEOMETRIC | INFO-band (OPEN-Q decision rule) |
| §W1b-5 | `S87-PS-AF-RECALIBRATION-DIAGNOSTIC` (OPEN-Q) | CF-12 | [VERIFY] | GEOMETRIC | PASS / INFO / FAIL — magnitude |
| §W1b-6 | `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE` (OPEN-Q) | CF-13 | [AUDIT] | GEOMETRIC | INFO-band (OPEN-Q decision rule) |

**Substrate framing**: All W1b gates probe spectral-action-moment / Seeley-DeWitt / Mellin-cone substrate observables on the Jensen-deformed `D_K` finite spectrum. The fabric IS its eigenvalue spectrum at L_max ∈ {10, 12, 14}; the gates do not test "QFT-in-curved-spacetime regularizations" but the substrate's own spectral-moment structure under different finite-L projections. Pauli-Villars subtraction is reframed as a finite-L spectral-mode subtraction (a substrate operation on the eigenvalue cache), NOT a continuum-QFT regulator imported from a container.

---

## Wave 1b Decision Point Prerequisites

W1b's six gates are organized as a directed sub-graph:

```
§W1b-1 (CF-8 PV recal)            \
                                    \
§W1b-2 (CF-9 d_eff anchor)         --->  §W1b-3 (CF-10 L_max sweep, CONDITIONAL)
                                    /
                                   /

§W1b-4 (CF-11 paired ratio OPEN-Q)
§W1b-5 (CF-12 PS A_F OPEN-Q)
§W1b-6 (CF-13 Connes-distance OPEN-Q)
```

- **§W1b-1 + §W1b-2 are independent** and can dispatch in parallel (both consume the L12 master cache `s84_spectrum_cache_L12_tau019.npz`; PV recalibration also references L_max=10 cache regenerated in-script if absent).
- **§W1b-3 fires CONDITIONALLY** — the trigger is computed inside §W1b-1 and §W1b-2 (see §W1b-3 trigger pin below). If both upstream gates resolve L_∞ to within ABSOLUTE tolerance 1e-3 at L_max ∈ {10, 12}, §W1b-3 closes as PRE-REG-INC mechanically per `.claude/rules/mechanical-closure-discipline.md` (no L_max=14 cache regeneration). If either upstream gate leaves L_∞ unresolved (spread `|value(L=10) − value(L=12)| > 1e-3`), §W1b-3 dispatches the L_max=14 sweep.
- **§W1b-4, §W1b-5, §W1b-6 are independent OPEN-Q** gates with INFO-band decision rules. They can dispatch in parallel with §W1b-1 and §W1b-2.

**Concurrent-dispatch cap**: ≤8 agents (per `feedback_dispatch-discipline.md`). W1b's 6 gates fit comfortably under the cap; default dispatch is all-6-parallel except §W1b-3 which gates on §W1b-1 and §W1b-2 close.

**Upstream L12 cache pin** (input-SHA computed at runtime by each script):
- `computations/s84_spectrum_cache_L12_tau019.npz` (1340660 B; verified on disk at plan-freeze 2026-04-27)
- `computations/canonical_constants.py` (S86-close state)

**Knowledge MCP pre-checks** (each agent runs at dispatch start per `CLAUDE.md` MANDATORY rule):
- `search_knowledge("Pauli-Villars finite-L subtraction")` (CF-8 / §W1b-1)
- `get_constant("d_eff")` and `search_knowledge("d_eff anchor spectral-action substrate")` (CF-9 / §W1b-2)
- `search_knowledge("paired slot ratio a_0 a_2 7436 3812")` (CF-11 / §W1b-4)
- `search_knowledge("Pati-Salam A_F finite-triple")` (CF-12 / §W1b-5)
- `search_knowledge("Connes distance anisotropy finite spectrum identity")` and `trace_entity("Connes distance")` (CF-13 / §W1b-6)

---

## §W1b-1. S87-PV-SUBTRACTION-RECALIBRATION

**Field 1 — Gate ID**: `S87-PV-SUBTRACTION-RECALIBRATION`

**Field 2 — Trigger**: `[VERIFY] [SIGN]` (substitution-chain + directional sign-pre-registration; Schema-v2 3-tuple required per `.claude/rules/gate-verdicts.md` §"S87+ canonical form")

**Field 3 — Classification**: GEOMETRIC (substrate spectral-mode subtraction; not particle / non-phononic)

**Field 4 — Agent type**: `gen-physicist` (cross-domain executor; orchestrator-direct dispatch for the wave-owner gen-physicist split)

**Field 5 — Hypothesis being tested**:
> Replacing the continuum Seeley-DeWitt residue coefficients (used in S86 W-1 W1b-T5 cone-residue evaluations) with a finite-L Pauli-Villars subtraction calibrated against the L_max=10 cache PRESERVES the §VII.U Mellin-Dirichlet identity at PASS-evidence-on-disk numerical level (max_rel_err < 1e-12), AND the recalibrated PV residue at L_max=12 is closer to the L→∞ limit than the continuum-SD residue (the SD residue is a leading-order approximation; PV finite-L subtraction is the substrate-faithful refinement).

**Field 6 — Method (full dispatch prompt)**:

```text
You are gen-physicist executing S87 W1b-1 carry-forward CF-8.

GOAL: Implement finite-L Pauli-Villars subtraction calibrated against the
L_max=10 spectral cache, then verify (a) §VII.U Mellin-Dirichlet identity
holds under PV at max_rel_err < 1e-12 (existing S86 W-1 C11 ceiling at
8.07e-28; PV must not regress), and (b) the PV-residue under L_max=12 is
closer to the empirical L_max-extrapolated limit than the continuum-SD
residue.

Knowledge MCP pre-check:
  - search_knowledge("Pauli-Villars finite-L subtraction")
  - search_knowledge("Mellin-Dirichlet identity §VII.U")
  - search_knowledge("Seeley-DeWitt continuum residue")
  - get_constant("M_KK")
  - get_constant("tau_fold")

Output files:
  - computations/s87_w1b_pv_subtraction_recalibration.py
  - computations/s87_w1b_pv_subtraction_recalibration.npz
    (keys: lambda_L10, lambda_L12, pv_residue_L10, pv_residue_L12,
     sd_residue_continuum, mellin_dirichlet_lhs, mellin_dirichlet_rhs,
     max_rel_err, sign_dpv_L12_minus_continuum)
  - computations/s87_w1b_pv_subtraction_recalibration.png
    (panel A: PV vs SD residue across L_max; panel B: Mellin-Dirichlet identity max_rel_err
     vs L_max; panel C: directional sign of (PV_L12 − SD_continuum))

Compute path:
  Use the GPU torch.linalg path on the AMD RX 9070 XT for the L_max=12
  master cache (already on disk). For L_max=10 cache regeneration, GPU
  is preferred but CPU fallback (OMP_NUM_THREADS=8 BEFORE numpy import)
  is acceptable for the 70k-eigenvalue L=10 cache. PV mass-scale set to
  M_KK (canonical_constants.py); no scan over PV mass — single-mass-scale
  subtraction calibrated AT M_KK by construction.

Pre-registration:
  Imports: from canonical_constants import *
  Inputs:  s84_spectrum_cache_L12_tau019.npz (verified on disk)
           s85_spectrum_cache_L10_tau019.npz (regenerate in-script if missing)
           canonical_constants.py
  Output 4-tuple: (value=max_rel_err_PV, scheme=Pauli-Villars-finite-L,
                   convention=substrate-mass-scale-M_KK, L_max=12)

  3-tuple Schema-v2 annotation (REQUIRED — [SIGN] trigger):
     sign_verdict pre-registered direction:
       sign_pred = +1   (PV_L12 − SD_continuum > 0; PV residue larger
                         in absolute value than continuum SD residue
                         because finite-L truncation undercounts UV
                         contribution)
     magnitude_verdict bands:
       PASS:  max_rel_err_PV < 1e-12 AND |PV_L12 − SD_continuum| > 1e-6
       INFO:  1e-12 ≤ max_rel_err_PV ≤ 1e-9 OR
              |PV_L12 − SD_continuum| ∈ [1e-9, 1e-6]
       FAIL:  max_rel_err_PV > 1e-9 OR |PV_L12 − SD_continuum| < 1e-9
              (no detectable PV-SD distinction → PV is degenerate to SD)
     regime_verdict: VALID iff PV mass-scale M_KK is bounded inside
       the L_max=12 spectrum's max-eigenvalue range; MARGINAL if M_KK
       within 5%-50% of max_eigenvalue; BREAKDOWN if M_KK > max_eigenvalue
       (PV subtraction not effective).

Tolerance rule: RATIO for max_rel_err_PV (1e-12 ceiling); ABSOLUTE for
  |PV_L12 − SD_continuum| (1e-6 floor). Sign-direction is the SIGN
  trigger.

Substitution chain (REQUIRED for the SIGN claim):
  Step 1 (definitions):
    Λ(L)         = sum-over-eigenvalues spectral-action moment at cutoff L
    Λ_PV(L; M)   = Λ(L) − Λ(L)|_{λ → λ + M^2}^{Pauli-Villars subtraction}
    Λ_SD         = continuum Seeley-DeWitt expansion of Λ via heat-kernel
                   coefficients (a_0, a_2, a_4, ...)
    R_PV(L; M)   = residue of Λ_PV(L; M) at the Mellin pole s = s_*
                   (substrate-distance-1 pole)
    R_SD         = continuum SD residue at s = s_*
    R_∞          = L → ∞ limit of R_PV(L; M)

  Step 2 (substitution into the sign target):
    sign_target  = sign(R_PV(L=12; M_KK) − R_SD)

  Step 3 (simplification via Seeley-DeWitt asymptotic expansion):
    R_PV(L; M) = R_SD + δR_finite-L(M)
    where δR_finite-L(M) = -sum_{λ > L^2} (residue contribution of modes
    above truncation, with PV mass-scale M_KK reweighting). The truncation
    REMOVES UV modes from R_∞; PV ADDS BACK a finite subtraction that is
    LESS than the missing UV contribution (PV is a regulator, not a full
    L-extension), so the residue of Λ_PV is LARGER in absolute value
    than R_SD (which would have included the full continuum integral).

  Step 4 (direction):
    R_PV(L; M_KK) > R_SD                        (positive direction)
    => sign(R_PV(L=12; M_KK) − R_SD) = +1       (sign_pred = +1)

What PASSES means (solution-space): the framework's continuum SD residue
  used in S86 W-1 C11 was a leading-order approximation; the substrate-
  faithful PV finite-L subtraction calibrated at M_KK reproduces the
  Mellin-Dirichlet identity to better-than-1e-12 precision AND its residue
  is positively offset from SD as predicted. This UPGRADES §VII.U from a
  CM-1995-leading-order anchor to a PV-recalibrated-finite-L anchor.

What FAILS means (solution-space): the PV subtraction either (a) fails to
  preserve the Mellin-Dirichlet identity (rel_err blows up), indicating
  the PV scheme is incompatible with the algebraic identity (likely
  because PV breaks an assumed ζ-regularization), or (b) the PV-SD offset
  is below detection threshold, indicating PV at M_KK is degenerate with
  the continuum SD scheme at this finite-L truncation. Either FAILURE
  closes the corridor: the §VII.U identity must be cited under continuum-SD
  scheme only, and a finite-L PV recalibration is not available at this
  L_max.

What INFO means: identity preserved up to 1e-9 (not 1e-12), OR sign
  matches but magnitude in [1e-9, 1e-6] band. INFO documents that PV
  recalibration is a viable but non-decisive refinement; downstream
  §VII.U citations may continue to reference SD scheme.

Verdict line emission: use the computation-script template's append_verdict()
  helper (atomic open("a")) per .claude/rules/gate-verdicts.md and
  .claude/rules/mechanical-closure-discipline.md. Emit BOTH companion
  rows (dual-SHA + Schema-v2 3-tuple).

Working-paper section: §W1b-1 in sessions/archive/session-87/session-87-w1b-workingpaper.md
  (≥15 substantive lines; verdict line at top, then numbers, substitution chain
  reproduced, solution-space interpretation, artifact pointers).

Substrate framing: PV subtraction is a substrate operation on the finite-L
  eigenvalue cache, NOT a continuum-QFT regulator imported from a container.
  The fabric IS its finite-L eigenvalue projection; PV reweights modes
  above the truncation by adding a virtual mass-shifted spectrum at M_KK.
  Direction of explanation flows D_K eigenvalues → spectral moments →
  Mellin-cone residue under PV recalibration. No reference to "QFT-in-
  curved-spacetime" container framings.
```

**Field 7 — PRDR machinery pin**:
- `N_eval`: 155984 (L_max=12 eigenvalue count); 70000 (L_max=10 regenerate target)
- `L_max`: 12 (primary); 10 (calibration anchor)
- `scan_range`: PV mass-scale fixed at `M_KK` (single-mass; no scan)
- `step_size`: N/A (algebraic identity verification, not ODE)
- `tolerance`: RATIO 1e-12 (max_rel_err); ABSOLUTE 1e-6 (PV-SD offset)
- `scheme`: `Pauli-Villars-finite-L` (regulator-pin tag per `.claude/rules/regulator-pin-discipline.md`); citation of `a_n` references MUST use `a_n^{Pauli-Villars}` form
- `convention`: `substrate-mass-scale-M_KK`
- `random_seed`: 42 (only relevant if eigenvector subspace random projections are used)
- `GPU path`: `torch.linalg.eigvalsh` on AMD RX 9070 XT; CPU fallback `OMP_NUM_THREADS=8` BEFORE numpy import

**Field 8 — Expected output 4-tuple**:
`(value=max_rel_err_PV, scheme=Pauli-Villars-finite-L, convention=substrate-mass-scale-M_KK, L_max=12)`

**Field 9 — PASS/FAIL/INFO with tolerance rule + Schema-v2 3-tuple**:

| Verdict | Condition |
|:--------|:----------|
| PASS | `max_rel_err_PV < 1e-12` AND `|R_PV(L=12) − R_SD| > 1e-6` AND `sign_verdict=PASS` AND `regime_verdict=VALID` |
| INFO | `max_rel_err_PV ∈ [1e-12, 1e-9]` OR `|R_PV − R_SD| ∈ [1e-9, 1e-6]` (sign correct, magnitude in INFO band) |
| FAIL | `max_rel_err_PV > 1e-9` OR `|R_PV − R_SD| < 1e-9` OR `sign_verdict=FAIL` OR `regime_verdict=BREAKDOWN` |

Schema-v2 3-tuple:
- `sign_verdict`: PASS iff `sign(R_PV(L=12; M_KK) − R_SD) == +1` (substitution-chain Step 4 prediction)
- `magnitude_verdict`: PASS / INFO / FAIL per the |R_PV − R_SD| band table
- `regime_verdict`: VALID iff M_KK ≤ max(λ_L=12); MARGINAL if M_KK ∈ [0.5·max(λ), 0.95·max(λ)]; BREAKDOWN if M_KK > max(λ_L=12)

Composite collapse rule: standard collapse per `gate-verdicts.md` Schema-v2.

**Field 10 — Substitution chain** (full chain reproduced in agent prompt above; summary):
- Λ_PV(L; M) = Λ(L) − Λ(L)|_{λ → λ+M²}
- R_PV = R_SD + δR_finite-L(M)
- δR_finite-L(M_KK) > 0 (PV adds back UV reweighting that SD truncation removes)
- ⇒ R_PV(L=12; M_KK) > R_SD; sign = +1

**Field 11 — Solution-space meaning**:
- **PASS**: §VII.U upgrades from continuum-SD scheme to PV-recalibrated-finite-L scheme. Substrate-faithful regularization scheme is now available for downstream Mellin-cone gates. Closes the corridor "is the SD residue a leading-order artifact?" with a finite-L refinement.
- **INFO**: PV recalibration is a viable but non-decisive refinement; SD scheme remains the canonical for §VII.U citations. The corridor remains open at lower precision.
- **FAIL**: PV scheme is incompatible with the §VII.U algebraic identity (likely a ζ-regularization artifact assumed by the identity), OR PV at M_KK is degenerate with SD at L_max=12. The SD scheme remains the only canonical for §VII.U; PV-recalibrated-finite-L is closed as a non-viable refinement.

**Field 12 — Effort**: 6h (single-script execution; L_max=12 cache already on disk; L_max=10 regeneration adds ~1h GPU)

**Field 13 — Substrate-framing reminder**:
> The PV finite-L subtraction is a substrate operation on the eigenvalue cache, NOT a continuum-QFT regulator. The fabric IS its finite-L spectrum; PV reweights truncated modes via a virtual mass-shifted spectrum at the substrate mass scale M_KK. Direction of explanation: D_K eigenvalues → PV-reweighted spectral moments → Mellin-cone residue. NO container framing.

**YAML block**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-PV-SUBTRACTION-RECALIBRATION
trigger: VERIFY-SIGN
classification: GEOMETRIC
agent: gen-physicist
schema_v2_3tuple_required: true
input_pins:
  - computations/s84_spectrum_cache_L12_tau019.npz
  - computations/s85_spectrum_cache_L10_tau019.npz  # regenerate-if-missing
  - computations/canonical_constants.py
machinery:
  N_eval: 155984
  L_max: 12
  scheme: Pauli-Villars-finite-L
  convention: substrate-mass-scale-M_KK
  scan_range: M_KK_single_mass_no_scan
  tolerance:
    max_rel_err: 1e-12
    pv_sd_offset: 1e-6
  GPU_path: torch.linalg.eigvalsh
```

---

## §W1b-2. S87-D-EFF-ANCHOR-VERIFICATION

**Field 1 — Gate ID**: `S87-D-EFF-ANCHOR-VERIFICATION`

**Field 2 — Trigger**: `[VERIFY] [AUDIT]`

**Field 3 — Classification**: GEOMETRIC (substrate effective-dimension audit on the finite-L spectrum)

**Field 4 — Agent type**: `gen-physicist` (cross-domain audit executor)

**Field 5 — Hypothesis being tested**:
> The single-d_eff anchor `d_eff = 8` (W-1 carry-forward CF-9 anchor) HOLDS as a per-slot threshold ordering on the L_max=12 master spectrum cache, in the sense that for each of the 4-stratum partition slots {stratum-0, stratum-1, stratum-2, stratum-3} the empirical Weyl-counting-function-derived effective dimension `d_eff,stratum_k` lies in a band consistent with d_eff=8 AND the per-stratum ordering is monotone (d_eff,0 ≤ d_eff,1 ≤ d_eff,2 ≤ d_eff,3 OR strictly-equal-to-8 within tolerance).

**Field 6 — Method (full dispatch prompt)**:

```text
You are gen-physicist executing S87 W1b-2 carry-forward CF-9.

GOAL: Verify d_eff=8 anchor on the L_max=12 master spectrum cache by
computing per-stratum effective dimension via Weyl counting function
fits AND verifying per-slot threshold ordering on the 4-stratum
partition.

Knowledge MCP pre-check:
  - search_knowledge("d_eff anchor spectral-action substrate")
  - get_constant("d_eff") (if pinned in canonical_constants.py)
  - search_knowledge("Weyl counting function L=12 4-stratum partition")
  - search_knowledge("4-stratum partition tau_fold V_4 monodromy")
  - trace_entity("4-stratum partition")

Output files:
  - computations/s87_w1b_d_eff_anchor_verification.py
  - computations/s87_w1b_d_eff_anchor_verification.npz
    (keys: lambda_L12_sorted, weyl_count_lambda, d_eff_global,
     d_eff_stratum_0, d_eff_stratum_1, d_eff_stratum_2, d_eff_stratum_3,
     stratum_membership_indices, ordering_pass_mask, anchor_d_eff = 8)
  - computations/s87_w1b_d_eff_anchor_verification.png
    (panel A: Weyl counting function N(λ) vs λ on log-log; panel B: per-
     stratum d_eff bar chart with ±tolerance; panel C: ordering check)

Compute path:
  GPU torch.linalg path is NOT needed (cache is precomputed; computation
  is a Weyl-fit on the eigenvalue list). Use CPU with OMP_NUM_THREADS=8
  set BEFORE numpy import.

Pre-registration:
  Imports: from canonical_constants import *
  Inputs:  s84_spectrum_cache_L12_tau019.npz (verified on disk)
           canonical_constants.py
  Output 4-tuple: (value=max(|d_eff_stratum_k − 8|),
                   scheme=Weyl-counting-function-fit,
                   convention=substrate-stratum-partition-V4,
                   L_max=12)

  3-tuple Schema-v2 annotation:
     sign_verdict: N/A (audit gate; no directional pre-registration)
     magnitude_verdict bands:
       PASS:  max(|d_eff_stratum_k − 8|) < 0.10  (per-stratum within 1.25%)
              AND ordering monotone: d_eff_0 ≤ d_eff_1 ≤ d_eff_2 ≤ d_eff_3
       INFO:  max(|d_eff_stratum_k − 8|) ∈ [0.10, 0.50]  (within 6.25%)
              OR ordering breaks at one stratum-pair
       FAIL:  max(|d_eff_stratum_k − 8|) > 0.50  OR ordering breaks at
              ≥ 2 stratum-pairs
     regime_verdict: VALID iff Weyl-fit χ² per d.o.f. < 5; MARGINAL if
       χ² ∈ [5, 50]; BREAKDOWN if χ² > 50 (Weyl fit not converged).

Tolerance rule: ABSOLUTE on |d_eff − 8| (since d_eff is dimensionless).
  Ordering is THEOREM-style boolean.

Substitution chain (audit-style; check the anchor):
  Step 1 (definitions):
    N(λ)     = Weyl counting function = #{eigenvalues ≤ λ}
    d_eff    = local-Weyl exponent: N(λ) ~ C · λ^(d_eff/2) for λ → ∞
    stratum_k = k-th 4-stratum partition slot (k ∈ {0,1,2,3}; per S86 W-12
                V_4 monodromy)
    d_eff,k  = d_eff fitted on stratum_k subset of eigenvalues

  Step 2 (substitution):
    For each stratum_k:
      log N_k(λ) = log C_k + (d_eff,k / 2) · log λ
    Linear fit slope = d_eff,k / 2 ⇒ d_eff,k = 2 · slope_k

  Step 3 (anchor check):
    target = d_eff_anchor = 8
    deviation_k = |d_eff,k − 8|

  Step 4 (verdict):
    audit PASS iff max_k(deviation_k) < 0.10 AND ordering monotone.

What PASSES means (solution-space): d_eff = 8 is the substrate's effective
  dimension at L_max=12, structurally AND across all 4 stratum-partition
  slots. The §VII.U identity, the §VII.W cross-pillar bridge, and any
  downstream gate citing d_eff=8 as substrate-canonical are AUDIT-PASS.

What FAILS means (solution-space): the d_eff=8 anchor either does not
  hold per-stratum (some stratum has d_eff ≠ 8 outside tolerance) OR
  the ordering theorem is broken. This indicates either (a) a finite-L
  truncation effect (some strata are not yet asymptotic at L_max=12),
  or (b) a structural gap in the d_eff=8 anchor that the W-1 sequence
  did not detect. Either FAILURE forces W1b-3 (L_max=14 sweep) to
  fire UNCONDITIONALLY.

What INFO means: d_eff=8 holds globally but per-stratum has spread
  in [0.10, 0.50] band. INFO documents that the 4-stratum partition
  is approaching but not yet at asymptotic d_eff=8 uniformly; the
  global anchor is still defensible for citations but per-stratum
  audits should use the stratum-specific d_eff,k value.

Verdict line emission: computation-script template append_verdict() with
  dual-SHA companion. Schema-v2 3-tuple optional but recommended (this
  is a [VERIFY] gate; the [AUDIT] sub-trigger does not require sign-
  verdict, but magnitude+regime are required).

Working-paper section: §W1b-2 in session-87-w1b-workingpaper.md (≥15
  substantive lines; verdict + per-stratum table + ordering pass mask +
  artifact pointers).

Substrate framing: d_eff is the substrate's effective dimension as
  read off the Weyl counting function on its OWN finite-L spectrum.
  Not a "spectral dimension of a continuum manifold". The fabric IS
  its eigenvalue density; d_eff is what that density encodes.
```

**Field 7 — PRDR machinery pin**:
- `N_eval`: 155984 (L_max=12 spectrum)
- `L_max`: 12
- `scan_range`: λ-fit window: [λ_min_per_stratum, 0.95·λ_max_per_stratum] (avoid finite-L cutoff edge)
- `step_size`: N/A (linear fit)
- `tolerance`: ABSOLUTE 0.10 on `|d_eff − 8|` (PASS); 0.50 (INFO ceiling); ordering boolean
- `scheme`: `Weyl-counting-function-fit`; `a_n` regulator tag: this gate does NOT cite `a_n` directly (it cites the Weyl-leading-coefficient via `d_eff`); not subject to `a_n` regulator-pin tagging
- `convention`: `substrate-stratum-partition-V4` (per S86 W-12 V_4 monodromy partition)
- `random_seed`: 42 (only for any bootstrap re-fit)
- `GPU path`: not needed; CPU `OMP_NUM_THREADS=8`

**Field 8 — Expected output 4-tuple**:
`(value=max(|d_eff_stratum_k − 8|), scheme=Weyl-counting-function-fit, convention=substrate-stratum-partition-V4, L_max=12)`

**Field 9 — PASS/FAIL/INFO**:

| Verdict | Condition |
|:--------|:----------|
| PASS | `max(|d_eff_k − 8|) < 0.10` AND ordering monotone AND `regime_verdict=VALID` |
| INFO | `max(|d_eff_k − 8|) ∈ [0.10, 0.50]` OR ordering breaks at exactly 1 stratum-pair |
| FAIL | `max(|d_eff_k − 8|) > 0.50` OR ordering breaks at ≥ 2 stratum-pairs OR `regime_verdict=BREAKDOWN` |

Schema-v2 3-tuple:
- `sign_verdict`: N/A (audit gate)
- `magnitude_verdict`: per the table
- `regime_verdict`: VALID iff Weyl-fit χ²/d.o.f. < 5; MARGINAL [5, 50]; BREAKDOWN > 50

**Field 10 — Substitution chain** (audit form):
- `N(λ) ~ C · λ^(d_eff/2)`, fit per stratum gives `d_eff,k = 2·slope_k`
- Anchor: `d_eff_anchor = 8`; deviation_k = |d_eff_k − 8|
- Audit PASS iff max_k(deviation_k) < 0.10 AND monotone ordering

**Field 11 — Solution-space meaning**:
- **PASS**: substrate is uniformly d_eff=8 at L_max=12 across all 4 stratum slots; downstream §VII.U / §VII.W citations are audit-grade. §W1b-3 closes mechanically as PRE-REG-INC (L_max=14 sweep not needed).
- **INFO**: substrate is globally d_eff=8 but per-stratum spread is detectable; downstream citations should disambiguate global vs per-stratum d_eff. §W1b-3 conditional trigger evaluates against the spread.
- **FAIL**: d_eff=8 anchor is broken at L_max=12; §W1b-3 fires UNCONDITIONALLY. Downstream §VII.U / §VII.W citations are flagged for review against L_max=14 data when available.

**Field 12 — Effort**: 4-6h (cache already on disk; 4-stratum partition is a known partition from S86 W-12 V_4 monodromy synthesis)

**Field 13 — Substrate-framing reminder**:
> d_eff is the substrate's effective dimension as encoded in its OWN finite-L eigenvalue density. NOT "the spectral dimension of a continuum manifold the substrate lives in". The 4-stratum partition is the V_4 monodromy partition of the substrate's spectrum, not a partition of a container. Direction: D_K eigenvalues → Weyl counting function → d_eff per stratum.

**YAML block**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-D-EFF-ANCHOR-VERIFICATION
trigger: VERIFY-AUDIT
classification: GEOMETRIC
agent: gen-physicist
schema_v2_3tuple_required: true
input_pins:
  - computations/s84_spectrum_cache_L12_tau019.npz
  - computations/canonical_constants.py
machinery:
  N_eval: 155984
  L_max: 12
  scheme: Weyl-counting-function-fit
  convention: substrate-stratum-partition-V4
  d_eff_anchor: 8
  tolerance:
    pass_band: 0.10
    info_band: 0.50
  GPU_path: not_required
```

---

## §W1b-3. S87-LMAX-WEYL-CONVERGENCE-SWEEP (CONDITIONAL)

**Field 1 — Gate ID**: `S87-LMAX-WEYL-CONVERGENCE-SWEEP`

**Field 2 — Trigger**: `[VERIFY]` (conditional; fires iff trigger predicate holds)

**Field 3 — Classification**: GEOMETRIC (L_max-axis convergence sweep on substrate spectrum)

**Field 4 — Agent type**: `gen-physicist` (cross-domain executor; this is a long-running cache-regeneration gate)

**Field 5 — Hypothesis being tested**:
> The L_∞ limit of the substrate effective-dimension d_eff (and the §VII.U Mellin-Dirichlet residue) is empirically determinable by extending the spectrum cache to L_max=14, IF AND ONLY IF the L=10/L=12 spread leaves L_∞ unresolved at PASS-band tolerance.

**Field 6 — Conditional trigger predicate (PRE-REGISTERED)**:

This gate fires iff EITHER of the following holds (computed inside §W1b-1 and §W1b-2 as part of their npz outputs):

```
TRIGGER_FIRES iff (
    abs(value_W1b1_L10 − value_W1b1_L12) > 1e-3   # PV residue L_∞ unresolved
    OR
    max_k(abs(d_eff_k_L10 − d_eff_k_L12)) > 0.10  # d_eff per-stratum spread
                                                    unresolved
)
```

Where `value_W1b1_L10` is the §W1b-1 PV residue evaluated at L_max=10
and `value_W1b1_L12` at L_max=12 (both written to the W1b-1 npz under
the keys `pv_residue_L10` and `pv_residue_L12`); and the d_eff per-stratum
values come from the §W1b-2 npz keys.

If TRIGGER_FIRES is FALSE, §W1b-3 closes MECHANICALLY per
`.claude/rules/mechanical-closure-discipline.md` with:

```
S87-LMAX-WEYL-CONVERGENCE-SWEEP: FAIL -- value='PRE-REG-INC_blocked_by_W1b-1_L_inf_resolved_W1b-2_d_eff_anchor_resolved'
   scheme=Weyl-counting-and-PV-recalibration convention=substrate-mass-scale-M_KK
   L_max=12 audit_sha256=... content_sha256=... schema_version=S84+
```

The mechanical-closure script is `computations/s87_w1b_lmax_sweep_mechanical_closure.py` and is invoked ONLY if the trigger predicate is FALSE after both upstream gates close. The corresponding working-paper §W1b-3 records the mechanical closure with full status / verdict / substrate-framing blocks per the `mechanical-closure-discipline.md` audit-trail signature.

**Field 6b — Method (full dispatch prompt; FIRES ONLY IF TRIGGER IS TRUE)**:

```text
You are gen-physicist executing S87 W1b-3 carry-forward CF-10
(CONDITIONAL — verify TRIGGER_FIRES==TRUE before dispatch by reading
W1b-1.npz pv_residue_L{10,12} and W1b-2.npz d_eff_stratum_{0..3} and
applying the trigger predicate).

GOAL: Regenerate the substrate spectrum cache at L_max=14, then refit
the Weyl counting function and §VII.U Mellin-Dirichlet identity to
empirically determine the L_∞ limit.

Knowledge MCP pre-check:
  - search_knowledge("L_max=14 spectrum cache regeneration")
  - search_knowledge("Weyl convergence sweep substrate finite-L")
  - get_constant("M_KK")
  - get_constant("tau_fold")

Output files:
  - computations/s87_w1b_lmax_weyl_convergence_sweep.py
  - computations/s87_spectrum_cache_L14_tau019.npz
    (eigenvalue cache; ~330k eigenvalues at L=14; ~10 GB on GPU)
  - computations/s87_w1b_lmax_weyl_convergence_sweep.npz
    (keys: d_eff_global_L{10,12,14}, d_eff_stratum_k_L{10,12,14},
     pv_residue_L{10,12,14}, l_inf_extrapolation, fit_residual,
     l_inf_fit_form = "richardson_3_point" or "1/L_max series fit")
  - computations/s87_w1b_lmax_weyl_convergence_sweep.png
    (3-panel: d_eff convergence; PV residue convergence; Richardson extrapolation)

Compute path:
  GPU MANDATORY: torch.linalg.eigvalsh on AMD RX 9070 XT (17.1 GB VRAM).
  At L=14, dense storage of D_K^2 hits ~10 GB; verify ≤ 0.5·VRAM = 8.5 GB
  per machinery-feasibility-audit; if it exceeds, FAIL_BY_FEASIBILITY (do
  NOT attempt CPU fallback at this scale).

Pre-registration:
  Imports: from canonical_constants import *
  Inputs:  s84_spectrum_cache_L12_tau019.npz
           s85_spectrum_cache_L10_tau019.npz (regenerated by W1b-1)
           computations/s87_w1b_pv_subtraction_recalibration.npz
             (input from §W1b-1)
           computations/s87_w1b_d_eff_anchor_verification.npz
             (input from §W1b-2)
           canonical_constants.py
  Output 4-tuple: (value=L_inf_extrapolation_residual,
                   scheme=Richardson-extrapolation-3-point,
                   convention=substrate-L-axis-asymptotic,
                   L_max=14)

  Verdict bands:
       PASS:  L_inf_extrapolation_residual < 1e-4  AND
              d_eff_global converges to 8.000 ± 0.01 at L=14  AND
              PV residue converges to PV_∞ at < 1e-6 fit residual
       INFO:  L_inf_extrapolation_residual ∈ [1e-4, 1e-2]  OR
              d_eff converges to band [7.95, 8.05] at L=14
       FAIL:  L_inf_extrapolation_residual > 1e-2  OR
              d_eff_global at L=14 outside [7.5, 8.5] OR
              VRAM-feasibility breach (machinery-feasibility-audit hard-halt)

Tolerance rule: ABSOLUTE on extrapolation residual; absolute on d_eff
  band.

Substitution chain (Richardson extrapolation):
  Step 1 (definitions):
    f(L)        = the convergent quantity (d_eff(L) or PV_residue(L))
    f_∞         = lim_{L→∞} f(L)
    R_3pt(L_3)  = Richardson 3-point extrapolation:
                  f_∞ ≈ [L_3³ · f(L_3) − L_2³ · f(L_2) + L_1³ · f(L_1)]
                        / [L_3³ − L_2³ + L_1³]   (assuming f(L) − f_∞ ~ L^{-3})

  Step 2 (substitution):
    L_1=10, L_2=12, L_3=14
    f_∞ ≈ R_3pt(14)

  Step 3 (residual):
    extrapolation_residual = |f(14) − R_3pt(14)|

  Step 4 (verdict): PASS iff residual < 1e-4 AND d_eff_∞ ∈ [7.99, 8.01].

What PASSES means (solution-space): the substrate's L_max-axis is
  empirically converged at L=14; all upstream §VII.U / §VII.W /
  §W1b-1 / §W1b-2 citations are L_∞-grade. Closes the L_max convergence
  question for S87 entirely.

What FAILS means (solution-space): the L_max axis has not converged at
  L=14; the substrate's effective dimension may still be transient at
  this scale, OR the L=14 cache regeneration hit a numerical-precision
  floor on GPU. Either FAILURE escalates to S88+ for an L_max=15 or
  L_max=16 sweep AND flags downstream citations of d_eff=8 / §VII.U
  for L-dependence audit.

What INFO means: L=14 converges to within 1% but not to PASS-band; the
  L_∞ limit is provisional. Citations may continue but should annotate
  "provisional L=14 fit".
```

**Field 7 — PRDR machinery pin** (only relevant if trigger fires):
- `N_eval`: ~330000 (L=14); regenerated in-script
- `L_max`: 14 (target); 10, 12 as anchors
- `scan_range`: L ∈ {10, 12, 14}; Richardson 3-point extrapolation
- `step_size`: N/A
- `tolerance`: ABSOLUTE 1e-4 (extrapolation residual); ABSOLUTE 0.01 (d_eff band)
- `scheme`: `Richardson-extrapolation-3-point` (paired with Weyl-counting-fit and PV-finite-L from upstream)
- `convention`: `substrate-L-axis-asymptotic`
- `random_seed`: 42
- `GPU path`: `torch.linalg.eigvalsh`; **MANDATORY** with VRAM-feasibility check (FAIL-BY-FEASIBILITY if dense storage > 8.5 GB)

**Field 8 — Expected output 4-tuple** (only if trigger fires):
`(value=L_inf_extrapolation_residual, scheme=Richardson-extrapolation-3-point, convention=substrate-L-axis-asymptotic, L_max=14)`

**Field 9 — PASS/FAIL/INFO** (only if trigger fires):

| Verdict | Condition |
|:--------|:----------|
| PASS | residual < 1e-4 AND `d_eff_∞ ∈ [7.99, 8.01]` AND PV residue convergent |
| INFO | residual ∈ [1e-4, 1e-2] OR `d_eff_∞ ∈ [7.95, 8.05]` |
| FAIL | residual > 1e-2 OR `d_eff_∞ ∉ [7.5, 8.5]` OR VRAM-feasibility breach |

If trigger does NOT fire: mechanical-closure FAIL with `value='PRE-REG-INC_blocked_by_W1b-1_L_inf_resolved_W1b-2_d_eff_anchor_resolved'` per `mechanical-closure-discipline.md`.

**Field 10 — Substitution chain** (Richardson):
- `f_∞ ≈ R_3pt(L_3)` where R_3pt assumes `f(L) − f_∞ ~ L^{-3}` (Weyl-asymptotic)
- residual = `|f(L=14) − R_3pt(14)|`
- PASS iff residual < 1e-4

**Field 11 — Solution-space meaning**:
- **PASS**: L_max axis converged at L=14; downstream substrate observables (d_eff, §VII.U, PV residue) are L_∞-grade.
- **INFO**: provisional L=14 convergence; 1% band achieved but not 0.01% band; downstream citations annotate provisional.
- **FAIL**: L=14 has not closed convergence; S88+ L=15+ sweep needed; downstream citations flagged for L-dependence audit.
- **MECHANICAL-FAIL** (trigger=FALSE): L=10/L=12 already resolves L_∞ within tolerance; L=14 sweep is unnecessary at S87.

**Field 12 — Effort**: 4-day (L=14 cache regeneration on GPU is the dominant cost; ~3 days of GPU-time + 1 day fit/analysis/writeup). If trigger=FALSE, mechanical closure is ~30 min.

**Field 13 — Substrate-framing reminder**:
> The L_max axis is a regulator-axis on the substrate's OWN finite-L spectral truncation, NOT a "lattice spacing" or "UV cutoff" of a continuum container. The L→∞ limit is the substrate's full spectrum, which by construction is the fabric in toto. Direction: D_K eigenvalues at L=14 → Weyl + PV refits → Richardson L_∞ extrapolation.

**YAML block**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-LMAX-WEYL-CONVERGENCE-SWEEP
trigger: VERIFY-CONDITIONAL
classification: GEOMETRIC
agent: gen-physicist
schema_v2_3tuple_required: false  # AUDIT-style; sign N/A
conditional_trigger:
  predicate: "(abs(W1b1.pv_residue_L10 − W1b1.pv_residue_L12) > 1e-3) OR (max(abs(W1b2.d_eff_stratum_k_L10 − W1b2.d_eff_stratum_k_L12)) > 0.10)"
  on_false: mechanical_closure_PRE-REG-INC
  on_true: dispatch_compute
input_pins:
  - computations/s84_spectrum_cache_L12_tau019.npz
  - computations/s85_spectrum_cache_L10_tau019.npz
  - computations/s87_w1b_pv_subtraction_recalibration.npz
  - computations/s87_w1b_d_eff_anchor_verification.npz
  - computations/canonical_constants.py
machinery:
  N_eval: 330000
  L_max: 14
  scheme: Richardson-extrapolation-3-point
  convention: substrate-L-axis-asymptotic
  scan_range: "L ∈ {10, 12, 14}"
  tolerance:
    extrap_residual_pass: 1e-4
    extrap_residual_info: 1e-2
    d_eff_band_pass: 0.01
  GPU_path: torch.linalg.eigvalsh_MANDATORY
  vram_feasibility_check: "dense_storage <= 8.5 GB"
```

---

## §W1b-4. S87-PAIRED-SLOT-RATIO-INTERPRETATION (OPEN-Q)

**Field 1 — Gate ID**: `S87-PAIRED-SLOT-RATIO-INTERPRETATION`

**Field 2 — Trigger**: `[AUDIT]` (open-question audit; structural classification of an empirical ratio)

**Field 3 — Classification**: GEOMETRIC (paired-slot a_0/a_2 split structural audit; OPEN-QUESTION)

**Field 4 — Agent type**: `gen-physicist` (open-question explorer; cross-domain interpreter)

**Field 5 — Hypothesis being tested** (OPEN-Q form):
> The empirical paired a_0/a_2 split ratio `7436/3812 ≈ 1.9507866...` observed in the W-1 paired-slot tabulation arises from one of three structural identities (to be enumerated by the gate's audit), AND the gate's task is to identify which of the three (if any) is the substrate-canonical interpretation.

The OPEN-Q decision rule is pre-registered: this gate produces an INFO verdict with a structured 4-class classification (CLASS-A: 2:1 hypercube-vertex pairing; CLASS-B: a_0/a_2 Seeley-DeWitt mass-ratio expansion; CLASS-C: other-substrate-identity; CLASS-D: numerical-coincidence-no-structural-source). Promotion to a fixed-form S88+ gate fires if AND ONLY IF the audit identifies a UNIQUE class with substrate-canonical evidence pinned in `canonical_constants.py` or knowledge MCP.

**Field 6 — Method (full dispatch prompt)**:

```text
You are gen-physicist executing S87 W1b-4 carry-forward CF-11 (OPEN-Q).

GOAL: Investigate the paired a_0/a_2 split ratio 7436/3812 ≈ 1.95079 by
enumerating its possible structural sources via 4-class classification,
then determining whether the empirical value uniquely matches one class.

Knowledge MCP pre-check:
  - search_knowledge("paired slot ratio 7436 3812 a_0 a_2")
  - search_knowledge("hypercube vertex character identity")
    (per CF-69 W-12 hypercube-vertex landing)
  - search_knowledge("Seeley-DeWitt mass-ratio expansion")
  - get_constant("a_0_FW") (if pinned)
  - get_constant("a_2_FW") (if pinned)
  - oeis lookup: mcp__oeis__lookup_by_values(values=[7436, 3812],
                                              max_results=10)
                 (check whether 7436 or 3812 are members of canonical
                  combinatorial sequences)

Output files:
  - computations/s87_w1b_paired_slot_ratio_interpretation.py
  - computations/s87_w1b_paired_slot_ratio_interpretation.npz
    (keys: paired_slot_ratio_observed = 7436/3812,
     class_A_predicted_value, class_A_match_residual,
     class_B_predicted_value, class_B_match_residual,
     class_C_candidates_list, class_C_match_residuals,
     class_D_residual_band,
     verdict_class, verdict_unique_match)
  - computations/s87_w1b_paired_slot_ratio_interpretation.png
    (4-panel: per-class predicted ratio vs observed; residual histogram;
     OEIS lookup hits if any; classification flowchart)

Compute path:
  CPU only (small algebraic computation; no spectrum needed).
  OMP_NUM_THREADS=8 BEFORE numpy import.

Pre-registration:
  Imports: from canonical_constants import *
  Inputs:  canonical_constants.py
           any S86 W-1 W1b-T5 paired-slot tabulation file
             (search the W-1 working paper sessions/archive/session-86/session-86-w1-workingpaper.md
              for the source of 7436 and 3812 — typically appears in a §W1b-T5 sub-section)
  Output 4-tuple: (value=class_match_residual_min,
                   scheme=4-class-paired-slot-classification,
                   convention=substrate-paired-slot-w1b-T5-anchor,
                   L_max=12)

  4-class enumeration (PRE-REGISTERED; the audit MUST enumerate exactly
  these 4 classes — this is the OPEN-Q decision rule):

    CLASS-A: Hypercube-vertex pairing
       Predicted ratio: 2 (i.e., 2:1 vertex pairing on (Z_2)^d, per
       CF-69 W-12 hypercube-vertex character identity at d ∈ {2,3,4,5})
       Match residual: |observed − 2| = |1.9507866 − 2| = 0.04921

    CLASS-B: Seeley-DeWitt mass-ratio expansion at a_0/a_2
       Predicted ratio: dimensionful ratio depending on M_KK and
       tau_fold; computed from canonical_constants.py
       Match residual: |observed − r_predicted_B|

    CLASS-C: Other-substrate-identity
       Open enumeration: Schur-orthogonality 2-row sums, Weyl-character
       branching ratios, Connes-Karoubi pairing weights, etc. Each
       candidate produces a residual; the class is CLASS-C iff one
       candidate matches < 1e-3.

    CLASS-D: Numerical-coincidence-no-structural-source
       The observation is incidental at L_max=12 and does not survive
       L_max=14 (cross-check via §W1b-3 if available).
       Match residual: > 1e-1 across all CLASS-A/B/C candidates.

  Verdict band (OPEN-Q INFO-band decision rule):
       INFO (CLASS-A unique): CLASS-A residual < 1e-2, all other
              residuals > 1e-1 ⇒ promote to S88 gate
              "S88-HYPERCUBE-VERTEX-PAIRED-SLOT-IDENTITY-VERIFY"
              (substrate-canonical: 2:1 hypercube vertex pairing)
       INFO (CLASS-B unique): CLASS-B residual < 1e-2, all others > 1e-1
              ⇒ promote to S88 gate
              "S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY"
       INFO (CLASS-C unique): CLASS-C identifies a single substrate
              identity ⇒ promote to S88 gate with that identity pinned
       INFO (CLASS-D): residuals > 1e-1 across all classes ⇒ no
              promotion; carry-forward to S88+ as deferred-research
              with a tighter L_max=14 cross-check
       INFO (multi-class match): two or more classes have residual
              < 1e-2 ⇒ ambiguous; carry-forward to S88+ as deferred-
              research with a structural disambiguation gate

  This gate ALWAYS verdicts INFO (per OPEN-Q discipline; no PASS/FAIL).
  The INFO sub-classification (A/B/C/D/multi) IS the structural output.

Tolerance rule: ABSOLUTE 1e-2 on per-class residual; ABSOLUTE 1e-1 on
  exclusion of other classes.

Substitution chain (4-class enumeration):
  Step 1 (definitions):
    r_obs = 7436 / 3812 (verify Sage QQ exactness)
    r_class_A = 2  (hypercube-vertex 2:1 pairing)
    r_class_B = (M_KK_a0_factor) / (M_KK_a2_factor)  (compute from
       canonical_constants.py provenance entries for a_0/a_2)
    {r_class_C_i} = enumerated candidates (Schur, Weyl-branching,
       Connes-Karoubi, ...)

  Step 2 (substitution): residual_X = |r_obs − r_class_X|

  Step 3 (uniqueness test):
    unique_class = X if residual_X < 1e-2 AND residual_Y > 1e-1 ∀ Y ≠ X

  Step 4 (verdict): INFO with sub-classification per the band table.

What INFO with unique class means (solution-space):
  the paired-slot ratio is identified as a substrate-canonical structural
  identity. S88+ gets a fixed-form verify gate at the identified class.

What INFO with CLASS-D means: the ratio is not a substrate-structural
  identity at L=12; either it is a finite-L artifact (cross-check at
  L=14 in §W1b-3) or it is a numerical coincidence with no structural
  parent. Carry-forward to S88+ as a deferred-research item.

Verdict line emission: computation-script template append_verdict() with
  verdict_class = INFO and a 3-tuple companion row encoding the
  sub-classification (sign_verdict=N/A; magnitude_verdict=PASS for
  CLASS-A/B/C unique, INFO for multi-class, FAIL for CLASS-D;
  regime_verdict=VALID).

Working-paper section: §W1b-4 in session-87-w1b-workingpaper.md (≥15
  substantive lines; verdict + per-class residual table + Sage QQ
  exactness check on 7436/3812 + OEIS lookup outcome + sub-classification
  promotion path).

Substrate framing: 7436 and 3812 are paired-slot integer counts
  emerging from the substrate's OWN spectral structure at L_max=12;
  the ratio 7436/3812 is an empirical observation on the substrate.
  Direction: D_K eigenvalues → spectral-action expansion → paired-slot
  tabulation → ratio. NO container framing.
```

**Field 7 — PRDR machinery pin**:
- `N_eval`: small (4-class algebraic enumeration)
- `L_max`: 12 (the L_max at which 7436/3812 was observed)
- `scan_range`: 4-class enumeration {A, B, C, D}; CLASS-C internal candidate list ≤ 10
- `step_size`: N/A
- `tolerance`: ABSOLUTE 1e-2 (per-class match); ABSOLUTE 1e-1 (other-class exclusion)
- `scheme`: `4-class-paired-slot-classification`
- `convention`: `substrate-paired-slot-w1b-T5-anchor` (per S86 W-1 W1b-T5 paired-slot tabulation)
- `random_seed`: 42
- `GPU path`: not needed; CPU `OMP_NUM_THREADS=8`

**Field 8 — Expected output 4-tuple**:
`(value=class_match_residual_min, scheme=4-class-paired-slot-classification, convention=substrate-paired-slot-w1b-T5-anchor, L_max=12)`

**Field 9 — INFO-band decision rule** (OPEN-Q; no PASS/FAIL by design — `feedback_arbitrary-gates.md` discipline; INFO is the structured outcome):

| Sub-classification | Condition | Promotion path |
|:-------------------|:----------|:---------------|
| INFO (CLASS-A unique) | A residual < 1e-2; others > 1e-1 | S88: `S88-HYPERCUBE-VERTEX-PAIRED-SLOT-IDENTITY-VERIFY` |
| INFO (CLASS-B unique) | B residual < 1e-2; others > 1e-1 | S88: `S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY` |
| INFO (CLASS-C unique) | C residual < 1e-2; others > 1e-1 | S88: gate-form depending on identified C-candidate |
| INFO (CLASS-D) | All residuals > 1e-1 | Carry-forward to S88+ deferred-research with L=14 cross-check |
| INFO (multi-class) | ≥ 2 classes < 1e-2 | Carry-forward to S88+ disambiguation gate |

**The OPEN-Q to S88+ gate-spec promotion rule (PRE-REGISTERED)**: the gate IS converted from OPEN-Q to fixed-form S88+ gate iff a single class has residual < 1e-2 AND all other classes have residual > 1e-1. Otherwise, the OPEN-Q remains a deferred-research carry-forward.

**Field 10 — Substitution chain** (4-class):
- `r_obs = 7436/3812 = 1929/953 + ...` (Sage QQ-exact form)
- residual_X = |r_obs − r_X| for X ∈ {A, B, C_i, D}
- unique_class iff one residual < 1e-2 AND others > 1e-1
- INFO sub-class per the band table

**Field 11 — Solution-space meaning**:
- **INFO (unique class)**: paired-slot ratio identified as substrate-structural; S88+ gets fixed-form verify gate. Closes the OPEN-Q.
- **INFO (CLASS-D)**: ratio not a substrate-canonical identity at L=12; OPEN-Q deferred; possible finite-L artifact.
- **INFO (multi-class)**: classes are not orthogonal at this L_max; OPEN-Q deferred to disambiguation.

**Field 12 — Effort**: TBD (per CF-11 source); estimated 3-5h for the 4-class enumeration + Sage QQ exactness check + OEIS lookup.

**Field 13 — Substrate-framing reminder**:
> 7436/3812 is an empirical paired-slot count ratio on the substrate's OWN spectrum at L=12. The 4-class enumeration tests whether this ratio arises from substrate-internal structure (hypercube-vertex pairing, SD mass ratio, Schur-orthogonality, etc.). Direction: D_K spectral structure → paired-slot tabulation → ratio classification.

**YAML block**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-PAIRED-SLOT-RATIO-INTERPRETATION
trigger: AUDIT-OPEN-Q
classification: GEOMETRIC
agent: gen-physicist
schema_v2_3tuple_required: true  # for INFO sub-classification encoding
open_q_decision_rule:
  classes: ["A_hypercube_vertex", "B_SD_mass_ratio", "C_other_substrate_identity", "D_numerical_coincidence"]
  uniqueness_test: "single_class_residual_lt_1e-2_AND_others_gt_1e-1"
  promotion_target_on_unique: "S88-{CLASS}-PAIRED-SLOT-IDENTITY-VERIFY"
  on_class_D_or_multi: "carry-forward_to_S88+_deferred_research"
input_pins:
  - computations/canonical_constants.py
  - sessions/archive/session-86/session-86-w1-workingpaper.md  # paired-slot tabulation source
machinery:
  L_max: 12
  scheme: 4-class-paired-slot-classification
  convention: substrate-paired-slot-w1b-T5-anchor
  tolerance:
    pass_residual: 1e-2
    exclusion_residual: 1e-1
  GPU_path: not_required
```

---

## §W1b-5. S87-PS-AF-RECALIBRATION-DIAGNOSTIC (OPEN-Q)

**Field 1 — Gate ID**: `S87-PS-AF-RECALIBRATION-DIAGNOSTIC`

**Field 2 — Trigger**: `[VERIFY]` (open-question diagnostic)

**Field 3 — Classification**: GEOMETRIC (Pati-Salam A_F finite-triple recalibration; OPEN-QUESTION; deferred-S88+-eligible)

**Field 4 — Agent type**: `gen-physicist` (cross-domain executor; PS embedding diagnostic)

**Field 5 — Hypothesis being tested** (OPEN-Q form):
> Whether the Pati-Salam A_F finite-triple recalibration `A_F = M_2(H) ⊕ M_4(C)` (instead of the SM A_F `= C ⊕ H ⊕ M_3(C)`) shifts the n=0 spectral-action growth factor below the 100× threshold currently observed at L_max=10. The OPEN-Q decision rule pre-registers PASS / INFO / FAIL bands on the n=0 growth factor under PS recalibration.

**Field 6 — Method (full dispatch prompt)**:

```text
You are gen-physicist executing S87 W1b-5 carry-forward CF-12 (OPEN-Q;
deferred-S88+-eligible if the diagnostic returns INFO with structural
ambiguity).

GOAL: Recalibrate the substrate's finite-spectral-triple A_F from the
Standard-Model algebra `A_F = C ⊕ H ⊕ M_3(C)` to the Pati-Salam algebra
`A_F = M_2(H) ⊕ M_4(C)`. Recompute the n=0 spectral-action growth
factor at L_max=10 under the recalibrated A_F. Compare against the
SM-A_F baseline (the 100× factor that motivated the diagnostic).

Knowledge MCP pre-check:
  - search_knowledge("Pati-Salam A_F finite-triple")
  - search_knowledge("n=0 spectral-action growth factor")
  - search_knowledge("Connes-Chamseddine 1996 finite spectral triple")
  - get_constant("M_KK")
  - trace_entity("finite spectral triple A_F")

Output files:
  - computations/s87_w1b_ps_af_recalibration_diagnostic.py
  - computations/s87_w1b_ps_af_recalibration_diagnostic.npz
    (keys: A_F_SM_dim, A_F_PS_dim, n0_growth_SM_baseline,
     n0_growth_PS_recalibrated, ratio_PS_over_SM,
     L_max=10_eigenvalue_count_SM, L_max=10_eigenvalue_count_PS,
     verdict_under_100x_threshold)
  - computations/s87_w1b_ps_af_recalibration_diagnostic.png
    (3-panel: A_F dimension comparison; n=0 growth factor side-by-side;
     PS-vs-SM ratio histogram across multiplet structure)

Compute path:
  GPU torch.linalg.eigvalsh on AMD RX 9070 XT (M_2(H) ⊕ M_4(C) gives
  finite-spectrum dimension 8 ⊕ 16 = 24, similar L_max=10 expansion
  scale to SM A_F's 4 ⊕ 18 = 22 — comparable cost). VRAM-feasibility
  check: dense storage <= 8.5 GB at L=10 PS.

Pre-registration:
  Imports: from canonical_constants import *
  Inputs:  s85_spectrum_cache_L10_tau019.npz (SM-A_F baseline; from W1b-1)
           canonical_constants.py
           Connes-Chamseddine 1996 finite-triple structure references
             (cited for PS A_F = M_2(H) ⊕ M_4(C); not on-disk SHA pin)
  Output 4-tuple: (value=n0_growth_PS_over_SM_ratio,
                   scheme=Pati-Salam-finite-triple-recalibration,
                   convention=A_F-M2H-M4C,
                   L_max=10)

  3-tuple Schema-v2 annotation:
     sign_verdict: N/A initially (hypothesis is bidirectional: PS could
       INCREASE or DECREASE the growth factor; the diagnostic determines
       which — no pre-registered direction)
     magnitude_verdict bands:
       PASS:  n0_growth_PS / 100x_baseline < 1  (PS shifts BELOW 100×)
              AND |n0_growth_PS − n0_growth_SM| > 0.01·n0_growth_SM
              (non-trivial shift)
       INFO:  n0_growth_PS / 100x_baseline ∈ [1, 5]  (PS shifts but not
              below 100×) OR shift magnitude < 1% (PS effectively
              degenerate with SM at the diagnostic's resolution)
       FAIL:  n0_growth_PS / 100x_baseline > 5  (PS shifts ABOVE,
              by factor 5 or more — opposite direction; or PS recalibration
              breaks finite-spectral-triple admissibility per
              Connes-Chamseddine 1996 axioms)
     regime_verdict: VALID iff PS A_F satisfies all 6 NCG axioms at
       finite-L=10 (the gate must verify this in-script per
       _connes_chamseddine_axiom_check); MARGINAL if 1 axiom marginal;
       BREAKDOWN if 2+ axioms fail.

Tolerance rule: RATIO on n0_growth_PS / 100x_baseline; ABSOLUTE on shift
  magnitude.

Substitution chain (PS A_F recalibration):
  Step 1 (definitions):
    A_F_SM   = C ⊕ H ⊕ M_3(C)         (real-dimension 4 ⊕ 4 ⊕ 18 = 22 -- but
                                        the relevant ratio is 1:4:18 per
                                        S86 W-6 CF-37)
    A_F_PS   = M_2(H) ⊕ M_4(C)        (real-dimension 8 ⊕ 32 = 40)
    n=0 growth factor under SM at L_max=10 = 100× baseline (CF-12 anchor)
    n0_PS    = n=0 growth factor recomputed under PS A_F at L_max=10
    ratio    = n0_PS / 100×

  Step 2 (substitution):
    The n=0 growth factor depends on the trace structure of A_F:
      n=0 ~ Tr(A_F) · (zeroth-spectral-moment of D_K|_{A_F})
    For SM:  Tr(A_F_SM) ~ 22 effective real-dim contribution
    For PS:  Tr(A_F_PS) ~ 40 effective real-dim contribution
    Naive ratio: n0_PS / n0_SM ~ 40/22 ~ 1.818 (ABOVE 100× baseline,
      not below)
    BUT: the PS A_F also REORGANIZES multiplet structure, so the
      effective trace on the active spectral subspace at L=10 may be
      either reduced or amplified depending on multiplet-mass alignment.
      The diagnostic's actual computation is required.

  Step 3 (verdict): comparison of computed n0_PS to 100× baseline.

  Step 4 (no pre-registered direction; this is the diagnostic's purpose).

What PASSES means (solution-space): PS A_F recalibration shifts n=0
  growth factor BELOW 100×. The substrate's finite-L truncation effects
  are partly attributable to the SM A_F choice; PS A_F is a viable
  alternative for finite-L convergence. S88+ gate "S88-PS-FULL-SPECTRAL-
  ACTION-RECOMPUTATION" promotes from this OPEN-Q.

What FAILS means (solution-space): either PS A_F shifts n=0 in the wrong
  direction (5×+ above), OR PS A_F violates Connes-Chamseddine 1996
  axioms at finite-L=10. PS recalibration is closed as a non-viable
  refinement; SM A_F remains canonical.

What INFO means: PS shift detectable but not below 100× threshold (in
  [1, 5] band) OR shift magnitude < 1%. PS recalibration is non-decisive;
  carry-forward to S88+ for L_max=12 PS recomputation.

Verdict line emission: computation-script template append_verdict() with dual-
  SHA + Schema-v2 3-tuple companion. Sign verdict = N/A (no pre-registered
  direction).

Working-paper section: §W1b-5 in session-87-w1b-workingpaper.md (≥15
  substantive lines; verdict + n=0 PS vs SM table + Connes-Chamseddine
  axiom check results + promotion path on PASS).

Substrate framing: A_F is the substrate's OWN finite-spectral-triple
  algebra at the substrate-IS level. Recalibrating from SM-A_F to PS-A_F
  is a structural-algebra choice on the substrate, NOT a "GUT extension
  of QFT in curved spacetime". The substrate IS its A_F; the recalibration
  asks which A_F the substrate IS at the finite-L truncation.
```

**Field 7 — PRDR machinery pin**:
- `N_eval`: ~70k (L=10 SM); ~125k (L=10 PS, scaled by Tr(A_F) ratio)
- `L_max`: 10 (target; matches CF-12 anchor at 100× baseline)
- `scan_range`: A_F ∈ {SM, PS}; no other scans
- `step_size`: N/A
- `tolerance`: RATIO on `n0_PS / 100×_baseline`; ABSOLUTE 0.01 on shift magnitude
- `scheme`: `Pati-Salam-finite-triple-recalibration`
- `convention`: `A_F-M2H-M4C` (vs SM `A_F-C-H-M3C`)
- `random_seed`: 42
- `GPU path`: `torch.linalg.eigvalsh`; VRAM-feasibility check

**Field 8 — Expected output 4-tuple**:
`(value=n0_growth_PS_over_SM_ratio, scheme=Pati-Salam-finite-triple-recalibration, convention=A_F-M2H-M4C, L_max=10)`

**Field 9 — PASS/FAIL/INFO**:

| Verdict | Condition |
|:--------|:----------|
| PASS | `ratio < 1` (PS below 100×) AND shift > 1% AND `regime_verdict=VALID` |
| INFO | `ratio ∈ [1, 5]` OR shift < 1% |
| FAIL | `ratio > 5` OR Connes-Chamseddine axiom breach (`regime_verdict=BREAKDOWN`) |

Schema-v2 3-tuple:
- `sign_verdict`: N/A (no pre-registered direction; bidirectional diagnostic)
- `magnitude_verdict`: per the band table
- `regime_verdict`: VALID iff PS A_F satisfies Connes-Chamseddine 1996 axioms; MARGINAL if 1 axiom marginal; BREAKDOWN if 2+ fail

**Field 10 — Substitution chain**:
- `n=0 ~ Tr(A_F) · zeroth-moment(D_K|_{A_F})`
- `Tr(A_F_SM) ~ 22`; `Tr(A_F_PS) ~ 40`
- naive ratio `~1.818`, but multiplet-realignment can reduce effective Tr on active L=10 subspace
- diagnostic measures actual ratio against 100× baseline

**Field 11 — Solution-space meaning**:
- **PASS**: PS A_F is a viable refinement; S88+ promotes to fixed-form gate `S88-PS-FULL-SPECTRAL-ACTION-RECOMPUTATION`.
- **INFO**: non-decisive; carry-forward to S88+ at L=12 recomputation.
- **FAIL**: PS A_F closed as non-viable; SM A_F canonical.

**Field 12 — Effort**: 6-10h (PS A_F recalibration + n=0 recompute + Connes-Chamseddine axiom check at L=10; GPU path is comparable to SM-A_F at L=10).

**Field 13 — Substrate-framing reminder**:
> A_F is the substrate's finite-spectral-triple algebra at the substrate-IS level. Recalibration is a structural choice on the substrate, NOT a "GUT extension". Direction: D_K |_{A_F} eigenvalues → spectral-action zeroth moment → n=0 growth factor under the chosen A_F.

**YAML block**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S87-PS-AF-RECALIBRATION-DIAGNOSTIC
trigger: VERIFY-OPEN-Q
classification: GEOMETRIC
agent: gen-physicist
schema_v2_3tuple_required: true
open_q_decision_rule:
  promotion_on_PASS: "S88-PS-FULL-SPECTRAL-ACTION-RECOMPUTATION"
  carry_forward_on_INFO: "S88-PS-AF-L12-RECALIBRATION"
  closed_on_FAIL: "PS A_F non-viable as finite-L refinement"
input_pins:
  - computations/s85_spectrum_cache_L10_tau019.npz  # regenerated by W1b-1
  - computations/canonical_constants.py
machinery:
  L_max: 10
  scheme: Pati-Salam-finite-triple-recalibration
  convention: A_F-M2H-M4C
  baseline: 100x_SM_n0_growth_factor_at_L10
  tolerance:
    ratio_pass: 1.0
    ratio_info_ceiling: 5.0
  GPU_path: torch.linalg.eigvalsh
  vram_feasibility_check: "dense_storage <= 8.5 GB"
  axiom_check: connes_chamseddine_1996_six_axioms_at_finite_L10
```

---

## §W1b-6. S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE (OPEN-Q)

**Field 1 — Gate ID**: `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE`

**Field 2 — Trigger**: `[AUDIT]` (open-question conjecture investigation)

**Field 3 — Classification**: GEOMETRIC (Connes-distance anisotropy functional; OPEN-QUESTION conjecture)

**Field 4 — Agent type**: `gen-physicist` (open-question explorer; conjectural identity audit)

**Field 5 — Hypothesis being tested** (OPEN-Q conjecture form):
> The Connes distance anisotropy functional `d_C(p, q; D_K^{<=L})` admits a finite-spectrum algebraic identity analogous to the §VII.U Mellin-Dirichlet identity, in the sense that there exists a closed-form expression `d_C(p, q; D_K^{<=L}) = F(λ_1, ..., λ_N_eval)` (purely algebraic in the eigenvalue list) that holds at PASS-evidence-on-disk numerical level (max_rel_err < 1e-9) for at least one canonical pair of states (p, q) on the substrate's finite spectral triple at L=12.

The OPEN-Q decision rule pre-registers a 3-class outcome: CLASS-α (identity found and verified at < 1e-9 → S88 promotes to fixed-form verify gate); CLASS-β (identity conjectured but residual in [1e-9, 1e-3] → carry-forward to S88+ algebraic refinement); CLASS-γ (no identity found → conjecture closed as non-existent at L=12 finite spectrum).

**Field 6 — Method (full dispatch prompt)**:

```text
You are gen-physicist executing S87 W1b-6 carry-forward CF-13 (OPEN-Q
conjecture; gate ID is S88-prefixed because the conjecture investigation
typically lands its candidate identity in S88 as a follow-on verify gate).

GOAL: Investigate whether the Connes distance functional on the
substrate's finite spectral triple admits a finite-spectrum algebraic
identity analogous to §VII.U Mellin-Dirichlet. The investigation
enumerates candidate identities and tests each numerically.

Knowledge MCP pre-check:
  - search_knowledge("Connes distance anisotropy functional")
  - search_knowledge("finite spectrum identity algebraic")
  - search_knowledge("Mellin-Dirichlet identity §VII.U")
  - trace_entity("Connes distance")
  - trace_entity("§VII.U Mellin-Dirichlet")

Output files:
  - computations/s87_w1b_connes_distance_finite_spectrum_identity.py
  - computations/s87_w1b_connes_distance_finite_spectrum_identity.npz
    (keys: candidate_identities_list, residuals_per_identity,
     best_residual, best_identity_form, canonical_state_pairs_tested,
     eigenvalues_L12, verdict_class, conjecture_status)
  - computations/s87_w1b_connes_distance_finite_spectrum_identity.png
    (panel A: residual histogram per candidate; panel B: best-fit identity
     form; panel C: state-pair coverage)

Compute path:
  GPU torch.linalg path for eigenvalue + Connes-distance computation
  at L=12 (155k eigenvalues; matrix ops on full spectrum). VRAM-feasibility
  check.

Pre-registration:
  Imports: from canonical_constants import *
  Inputs:  s84_spectrum_cache_L12_tau019.npz
           sessions/permanent-results-registry.md (§VII.U Mellin-Dirichlet
             identity for analogy template)
           canonical_constants.py
  Output 4-tuple: (value=best_residual,
                   scheme=Connes-distance-finite-spectrum-identity-conjecture,
                   convention=substrate-state-pair-canonical,
                   L_max=12)

  Candidate identity enumeration (PRE-REGISTERED enumeration; the audit
  MUST test these candidates in order):

    Candidate-1: d_C(p, q; D_K^{<=L}) = sup_{a ∈ A, ‖[D_K, a]‖<=1} |a(p) − a(q)|
                 (Connes 1996 original definition; numerical evaluation
                  via SDP on the finite-L commutator algebra)
    Candidate-2: d_C(p, q) = sum_{n} c_n · λ_n^{-α(p,q)}
                 (Mellin-Dirichlet-analog: finite Dirichlet sum over
                  eigenvalues with state-pair-dependent exponent)
    Candidate-3: d_C(p, q) = ‖[D_K, π(a_pq)]‖^{-1}
                 (commutator-norm form; pinned to a state-pair-defining
                  algebra element a_pq)
    Candidate-4: d_C(p, q) = √(Tr_H[Q_pq · D_K^{-2}])
                 (heat-kernel-trace form; first-Mellin-moment analog)

  Canonical state pairs (p, q) to test (PRE-REGISTERED — at least 3 pairs):
    Pair-1: (vacuum, n=0 quasiparticle excitation)
    Pair-2: (B1 acoustic mode minimum, B1 acoustic mode maximum)
    Pair-3: (Cartan eigenstate at root α_1, Cartan eigenstate at root α_2)

  Verdict band (OPEN-Q; INFO is the structured outcome):
       INFO (CLASS-α): best_residual < 1e-9 across ≥2 canonical state pairs
              ⇒ promote to S88 gate
              "S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-VERIFY"
              with the identity pinned at the verifying candidate form
       INFO (CLASS-β): best_residual ∈ [1e-9, 1e-3] across at least one
              canonical state pair ⇒ carry-forward to S88+ algebraic
              refinement; the candidate is structurally promising but
              not numerically tight at L=12
       INFO (CLASS-γ): best_residual > 1e-3 across all candidates and
              all state pairs ⇒ conjecture closed as non-existent at
              L=12 finite spectrum; the §VII.U Mellin-Dirichlet identity
              is structurally specific, not generic to all substrate
              algebraic functionals.

Tolerance rule: ABSOLUTE 1e-9 on residual (PASS-evidence-on-disk standard
  per §VII.U C11 8.07e-28 ceiling).

Substitution chain (conjecture template):
  Step 1 (definitions; reading off §VII.U structure):
    §VII.U identity (template): there exists F: spectrum → R such that
      Mellin_residue(D_K, s_*) = F({λ_n}_{n=1..N_eval})
      with max_rel_err < 1e-12 at L=12 (verified S86 W-1 C11)
    Conjecture: by analogy, there exists G: spectrum × state-pair → R
                such that
      Connes_distance(p, q; D_K^{<=L}) = G({λ_n}, p, q)
      with max_rel_err < 1e-9 at L=12

  Step 2 (substitution; testing candidates):
    For each candidate-k and each state-pair-j:
      LHS_kj = Connes_distance(p_j, q_j; D_K^{<=L})  (computed via
        Connes 1996 SDP)
      RHS_kj = G_k({λ_n}, p_j, q_j)  (candidate-k closed form)
      residual_kj = |LHS_kj − RHS_kj| / |LHS_kj|

  Step 3 (uniqueness): identity holds iff some k satisfies
    max_j(residual_kj) < 1e-9 across ≥2 canonical state pairs

  Step 4 (verdict):
    INFO with sub-classification per the band table.

What INFO with CLASS-α means: substrate Connes distance admits a finite-
  spectrum identity, structurally analogous to §VII.U. New permanent-
  registry entry candidate at §VII.{next-letter}; promote to S88 verify
  gate with identity pinned.

What INFO with CLASS-β means: candidate identity is structurally
  promising but numerically loose at L=12; either (a) finite-L
  truncation effect (re-test at L=14 in §W1b-3), or (b) candidate
  form needs refinement. Carry-forward to S88+ algebraic refinement.

What INFO with CLASS-γ means: §VII.U Mellin-Dirichlet identity is
  structurally specific, NOT generic to all substrate algebraic
  functionals. Conjecture closed as non-existent at L=12.

Verdict line emission: computation-script template append_verdict() with
  dual-SHA + Schema-v2 3-tuple companion (sign N/A; magnitude per
  CLASS-α/β/γ; regime VALID iff Connes-distance SDP converges).

Working-paper section: §W1b-6 in session-87-w1b-workingpaper.md (≥15
  substantive lines; verdict + per-candidate residual table + state-pair
  coverage + promotion path on CLASS-α / carry-forward on CLASS-β / closure
  on CLASS-γ).

Substrate framing: Connes distance is a substrate-internal metric on
  state-space, computed from the finite-L Dirac operator's commutator
  algebra. NOT "a metric on a manifold the substrate lives in". The
  substrate IS its commutator algebra; d_C is the substrate's natural
  state-distance functional. Direction: D_K eigenvalues + commutator
  → SDP over A_F → d_C(p, q).
```

**Field 7 — PRDR machinery pin**:
- `N_eval`: 155984 (L=12)
- `L_max`: 12
- `scan_range`: 4 candidates × 3 canonical state-pairs = 12 evaluations
- `step_size`: N/A (algebraic identity test); SDP solver tolerance 1e-12
- `tolerance`: ABSOLUTE 1e-9 (PASS-evidence-on-disk); 1e-3 (INFO CLASS-β ceiling)
- `scheme`: `Connes-distance-finite-spectrum-identity-conjecture`
- `convention`: `substrate-state-pair-canonical` (with 3 pre-registered pairs)
- `random_seed`: 42 (for SDP starting point)
- `GPU path`: `torch.linalg` for eigenvalue ops + commutator-norm; SDP via cvxpy CPU (commutator algebra at L=12 is small enough for CPU SDP)

**Field 8 — Expected output 4-tuple**:
`(value=best_residual, scheme=Connes-distance-finite-spectrum-identity-conjecture, convention=substrate-state-pair-canonical, L_max=12)`

**Field 9 — INFO-band decision rule** (OPEN-Q):

| Sub-class | Condition | Promotion path |
|:----------|:----------|:---------------|
| INFO (CLASS-α) | `best_residual < 1e-9` across ≥2 state pairs | S88: `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-VERIFY` |
| INFO (CLASS-β) | `best_residual ∈ [1e-9, 1e-3]` at ≥1 state pair | Carry-forward to S88+ algebraic refinement |
| INFO (CLASS-γ) | `best_residual > 1e-3` across all candidates and all state pairs | Conjecture closed as non-existent at L=12 |

**The OPEN-Q to S88+ gate-spec promotion rule (PRE-REGISTERED)**: CLASS-α promotes to fixed-form S88 verify gate with identity pinned at the verifying candidate form. CLASS-β carries forward as deferred-research. CLASS-γ closes the conjecture as non-existent.

**Field 10 — Substitution chain** (analogy template):
- §VII.U: `Mellin_residue = F({λ_n})` at < 1e-12 (verified S86 W-1)
- Conjecture: `Connes_distance(p,q) = G({λ_n}, p, q)` at < 1e-9
- For each candidate k: `residual_kj = |LHS_kj − RHS_kj| / |LHS_kj|`
- Identity holds iff `max_j(residual_kj) < 1e-9` for some k, across ≥2 canonical state-pairs

**Field 11 — Solution-space meaning**:
- **INFO (CLASS-α)**: Connes-distance admits a finite-spectrum identity; new §VII.{next-letter} registry entry; structural analog of §VII.U widens the substrate-canonical algebraic-functional family. S88 promotes.
- **INFO (CLASS-β)**: candidate is structurally promising but numerically loose; carry-forward to algebraic refinement.
- **INFO (CLASS-γ)**: §VII.U Mellin-Dirichlet is structurally specific to its functional family; Connes-distance does NOT admit an analogous identity at L=12; conjecture closed.

**Field 12 — Effort**: 8-12h (4 candidates × 3 state-pairs × SDP-solve at L=12; main cost is the SDP convergence on the commutator algebra at this scale).

**Field 13 — Substrate-framing reminder**:
> Connes distance is a substrate-internal state-space metric, computed from the finite-L Dirac commutator algebra. NOT a metric on an external manifold. The substrate IS its commutator algebra at finite-L; d_C is the substrate's natural state-distance. Direction: D_K eigenvalues + commutator algebra → SDP → d_C(p, q).

**YAML block**:
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
gate_id: S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE
trigger: AUDIT-OPEN-Q
classification: GEOMETRIC
agent: gen-physicist
schema_v2_3tuple_required: true
open_q_decision_rule:
  classes: ["alpha_identity_verified", "beta_promising_loose", "gamma_no_identity"]
  promotion_on_alpha: "S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-VERIFY"
  carry_forward_on_beta: "S88+_algebraic_refinement"
  closed_on_gamma: "conjecture_non-existent_at_L12"
input_pins:
  - computations/s84_spectrum_cache_L12_tau019.npz
  - sessions/permanent-results-registry.md  # §VII.U analogy template
  - computations/canonical_constants.py
machinery:
  L_max: 12
  scheme: Connes-distance-finite-spectrum-identity-conjecture
  convention: substrate-state-pair-canonical
  candidates: 4
  state_pairs: 3
  tolerance:
    pass_residual: 1e-9
    info_ceiling: 1e-3
  GPU_path: torch.linalg_for_eig_plus_cpu_SDP_via_cvxpy
```

---

## Wave 1b → Wave 2 Decision Point

W1b's 6 gates feed into the W2 decision graph as follows:

**Direct downstream consumers** (gates that consume W1b npz outputs):

- **§W1b-1 PV recalibration** → consumed by §W1b-3 (trigger predicate); ALSO by W2 §VII.U registry-landing audit (consumes recalibrated PV residue if PASS).
- **§W1b-2 d_eff anchor** → consumed by §W1b-3 (trigger predicate); ALSO by all S87+ gates that cite d_eff=8 (downstream §VII.U / §VII.W / §W1b-5 PS).
- **§W1b-3 L_max sweep** → consumed by S87 closeout's L_∞-grade audit on §W1b-1, §W1b-2, §W1b-4 (paired-slot ratio cross-check at L=14 if CLASS-D).
- **§W1b-4 paired-slot ratio** → if CLASS-A/B/C unique, promotes to fixed-form S88 verify gate; if CLASS-D, cross-checks against §W1b-3 L=14 cache.
- **§W1b-5 PS A_F** → if PASS, promotes to S88 `S88-PS-FULL-SPECTRAL-ACTION-RECOMPUTATION`; if INFO, carry-forward to S88+ at L=12; if FAIL, closes PS A_F refinement.
- **§W1b-6 Connes-distance conjecture** → if CLASS-α, promotes to S88 verify gate; if CLASS-β, carry-forward to S88+ algebraic refinement; if CLASS-γ, closes conjecture.

**Promotion paths to S88**:

| W1b verdict | S88+ gate spec |
|:------------|:---------------|
| §W1b-4 INFO CLASS-A | `S88-HYPERCUBE-VERTEX-PAIRED-SLOT-IDENTITY-VERIFY` |
| §W1b-4 INFO CLASS-B | `S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY` |
| §W1b-4 INFO CLASS-C | `S88-{CLASS-C-form}-PAIRED-SLOT-IDENTITY-VERIFY` |
| §W1b-5 PASS | `S88-PS-FULL-SPECTRAL-ACTION-RECOMPUTATION` |
| §W1b-5 INFO | `S88-PS-AF-L12-RECALIBRATION` |
| §W1b-6 INFO CLASS-α | `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-VERIFY` |

**No-promotion paths** (carry-forward as deferred-research):

- §W1b-4 INFO CLASS-D / multi-class
- §W1b-5 INFO (carry-forward path)
- §W1b-6 INFO CLASS-β

**Closure paths** (no further work; corridor closed):

- §W1b-1 FAIL → PV recalibration closed
- §W1b-2 FAIL → d_eff=8 anchor flagged for L=14 audit (escalates §W1b-3)
- §W1b-3 FAIL → L_max axis still convergent; S88+ L=15+ sweep
- §W1b-5 FAIL → PS A_F closed as non-viable
- §W1b-6 INFO CLASS-γ → Connes-distance identity conjecture closed as non-existent

---

## Wave 1b Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR machinery enumeration:

| Gate | N_eval | L_max | Scheme | Convention | Tolerance | GPU/CPU |
|:-----|:------:|:-----:|:-------|:-----------|:----------|:--------|
| §W1b-1 PV recal | 155984 (L=12); 70k (L=10) | 12 | Pauli-Villars-finite-L | substrate-mass-scale-M_KK | RATIO 1e-12 (rel_err); ABSOLUTE 1e-6 (PV-SD offset) | GPU torch.linalg.eigvalsh |
| §W1b-2 d_eff audit | 155984 | 12 | Weyl-counting-function-fit | substrate-stratum-partition-V4 | ABSOLUTE 0.10 (PASS); 0.50 (INFO) | CPU OMP=8 |
| §W1b-3 L=14 sweep (CONDITIONAL) | 330000 | 14 | Richardson-extrapolation-3-point | substrate-L-axis-asymptotic | ABSOLUTE 1e-4 (residual); 1e-2 (INFO) | GPU MANDATORY + VRAM check |
| §W1b-4 paired-slot ratio (OPEN-Q) | small | 12 | 4-class-paired-slot-classification | substrate-paired-slot-w1b-T5-anchor | ABSOLUTE 1e-2 (per-class); 1e-1 (other-class exclusion) | CPU OMP=8 |
| §W1b-5 PS A_F (OPEN-Q) | ~125k (L=10 PS) | 10 | Pati-Salam-finite-triple-recalibration | A_F-M2H-M4C | RATIO `< 1` (PASS); `[1, 5]` (INFO); `> 5` (FAIL) | GPU torch.linalg.eigvalsh + axiom check |
| §W1b-6 Connes-dist conjecture (OPEN-Q) | 155984 | 12 | Connes-distance-finite-spectrum-identity-conjecture | substrate-state-pair-canonical | ABSOLUTE 1e-9 (CLASS-α); 1e-3 (CLASS-β/γ split) | GPU torch.linalg + CPU SDP cvxpy |

**Random seed pin**: 42 across all 6 gates (only relevant for §W1b-1 if eigenvector subspace random projections are used; §W1b-3 L=14 cache regeneration; §W1b-6 SDP starting point).

**Regulator-pin tag enforcement** (per `.claude/rules/regulator-pin-discipline.md`):
- §W1b-1 cites PV scheme → all `a_n` references in script use `a_n^{Pauli-Villars}` form
- §W1b-2 does NOT cite `a_n` (Weyl-leading-coefficient via `d_eff`); not subject to a_n tagging
- §W1b-3 cites scheme = Richardson-extrapolation; if any `a_n` cited internally, use `a_n^{Pauli-Villars}` (inherited from W1b-1) or `a_n^{ζ}` if alternative scheme is invoked — script must declare
- §W1b-4 does NOT cite `a_n` directly (paired-slot integer-count ratio)
- §W1b-5 cites PS A_F finite-spectral-triple recalibration; any `a_n` reference uses scheme matching the underlying spectral computation (typically `a_n^{ζ}` baseline)
- §W1b-6 does NOT cite `a_n` directly (Connes-distance is a metric functional, not a spectral-action moment)

---

## Wave 1b Input-SHA Ledger

Files referenced as input pins (SHAs computed at runtime by each script per `.claude/rules/gate-verdicts.md` MANDATORY full-64-hex):

| File | Purpose | On-disk verified at plan-freeze |
|:-----|:--------|:-------------------------------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | L=12 master cache (W1b-1, W1b-2, W1b-3, W1b-6) | YES (1340660 B; 2026-04-19) |
| `computations/s85_spectrum_cache_L10_tau019.npz` | L=10 calibration anchor (W1b-1 regenerates if missing; W1b-3, W1b-5 consume) | NO (regenerate-if-missing pin in §W1b-1) |
| `computations/canonical_constants.py` | M_KK, tau_fold, d_eff, A_F constants | YES (S86-close state) |
| `computations/s87_w1b_pv_subtraction_recalibration.npz` | §W1b-3 trigger predicate input | runtime-produced by §W1b-1 |
| `computations/s87_w1b_d_eff_anchor_verification.npz` | §W1b-3 trigger predicate input | runtime-produced by §W1b-2 |
| `sessions/archive/session-86/session-86-w1-workingpaper.md` | §W1b-4 paired-slot tabulation source | YES (S86-close state; agent reads §W1b-T5 sub-section) |
| `sessions/permanent-results-registry.md` | §W1b-6 §VII.U Mellin-Dirichlet analogy template | YES (S86-close state) |

**Closure SHA pin** (per gate, MANDATORY full 64-char per `gate-verdicts.md`): each script computes `closure_hash(input_pin_map)` at runtime via the `script-template.py append_verdict()` helper. NEVER hardcode; NEVER copy-paste.

**Script-bytes immutability**: per `.claude/rules/mechanical-closure-discipline.md`, after first execution the §W1b-3 mechanical-closure script (if trigger=FALSE) should be made read-only OR a frozen snapshot committed alongside the verdict file.

---

## Wave 1b Plan-Freeze Validation Checklist

Per the validator inventory (context §1.4) — these MUST run at plan-freeze before dispatch:

1. `python computations/_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w1b.md`
   → produces `sessions/session-plan/session-87-plan-w1b-validation.json`
2. `python computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w1b.md`
   → checks PRDR machinery checklist + R3 `schema_version` per gate
3. `python computations/_source_reconciliation_audit.py`
   → 5+1 class taxonomy; HARD-HALT at D_max ≥ 3.0
4. `python computations/_substrate_first_provenance_audit.py` (V.1 manual review until S87 implementation lands per CF-79-adjacent)
5. Post-dispatch grep on `computations/s86_gate_verdicts.txt` confirming no `S87-` or `S88-` prefixed verdict lines pre-exist
6. Post-dispatch grep on `computations/s87_gate_verdicts.txt` confirming W1b gate IDs not pre-emitted

**End of session-87-plan-w1b.md.**
