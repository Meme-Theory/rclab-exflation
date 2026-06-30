# Session 95 Plan — Wave 6: Observational — PBH magnitude, BAO amplitude, falsifier-inventory + constant hygiene

**Date**: 2026-05-28
**Author**: mack-cosmic-bridge (generated per /rclab-plan per-wave swarm)
**Owner agent**: mack-cosmic-bridge (Cosmic Bridge; observational-cosmology / DM-DE interface)
**Plan source**: `sessions/session-plan/session-95-context.md` §A4 + §A8 + §C (C-A1, C-A4) + §F (W6 reading allowances)
**Working paper**: `sessions/archive/session-95/session-95-w6-workingpaper.md`
**Verdict file (canonical)**: `computations/session-95/s95_gate_verdicts.txt`

## Wave 6 Summary

Wave 6 is the observational wave. It discharges two held/forecast carry-forwards and lands three falsifier-inventory / constant-hygiene items. The two compute gates (§W6-1 PBH magnitude, §W6-2 BAO amplitude) re-use S94 machinery (no fresh diagonalization) and convert HELD/sensitivity results into substrate-physical-scale or detection-forecast statements. The four hygiene/inventory gates (§W6-3 DE joint posterior, §W6-4 w0_FW/M_KK provenance, §W6-5 LEGGETT conditional, §W6-6 f_NL row) close the mack-collab + nazarewicz-collab + transit-collab carry-forwards that touch observation.

Carry-forward sources: S94 W5 WP (`CF-S95-N-PBH-MAGNITUDE-RECOMPUTE`); S94 S-1 BAO synthesis `:148-155` (`CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT`); mack-collab §2 + §7.5 carry-forwards (DE joint posterior + provenance); nazarewicz-collab §R2 (LEGGETT-GRAV-DECAY conditional); transit-collab §V.3 (f_NL row).

**Substrate-first framing (wave-wide)**: every late-time / observable number in this wave is positioned as `D_K` spectrum → spectral moment → emergent observable → comparison-against-detector, never the reverse. The BAO rows are explicitly scale-and-channel-tagged per `phononic-framing.md §"Scale-and-channel-tagging"`: the substrate-IS observable (M_KK-internal branch-speed split) is distinct from the laboratory-IN observable (emergent BAO peak position / amplitude in the container-observer's P(k), C_ℓ), and the bridge between them is the effacement projection — NOT a borrowed ΛCDM value. The held-number guard (context §A4 / closeout §5.4) is binding: `n_PBH = 7.2761e-23 m⁻³` is ONE held number with ONE forward CF (§W6-1); it is NOT double-counted as a §25 Tier-2 + §26 genus + fresh CF, and the §VII.AX.OP-PROJ / STATE-PROJ theorem-STRUCTURE remains STAGE-3-PERMANENT regardless of this wave's magnitude verdict.

## Wave 6 Decision Point Prerequisites

Wave 6 has NO intra-S95 upstream-verdict dependency — all six gates consume S94 (or earlier) artifacts that already exist on disk, plus the knowledge MCP. The gates are mutually independent and may dispatch in parallel. Specifically:

- §W6-1 consumes `computations/session-94/s94_n_pbh_truncation_anchor.npz` (S94 W5-1, on disk) + the L=10 atlas N decomposition + `canonical_constants.py`.
- §W6-2 consumes `computations/session-94/s94_bao_peak_branch.npz` (S94 W5-3, on disk) + S43 transfer-function structure + `canonical_constants.py` + (conditionally) a fetched CMB-S4/SO forecast.
- §W6-3 / §W6-4 consume `canonical_constants.py` + knowledge MCP only (hygiene gates).
- §W6-5 / §W6-6 consume `canonical_constants.py` + the existing `falsifier-master-inventory.md` (mack-bridge sole-writer) + (W6-6) the transit-collab §V.3 canonical value.

No mechanical-closure deferral is anticipated for any W6 gate. If `mcp__paper-search__*` is unavailable at dispatch (it was DOWN in S94), §W6-2 routes to its pre-registered INFO branch (forecast computed, experiment sensitivity unavailable) — this is a verdict, not a closure.

---

## §W6-1. CF-S95-N-PBH-MAGNITUDE-RECOMPUTE

```yaml
# ---- Identity (6 fields) ----
gate_id: "CF-S95-N-PBH-MAGNITUDE-RECOMPUTE"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "GEOMETRIC"
agent_type: "mack-cosmic-bridge"
hypothesis: >
  The §VII.AX m⁻³ Level-3 magnitude, recomputed via the g-axis cardinality-cascade
  saturated tail at the substrate-singled-out anchor g_saturate=143 (L_max-INDEPENDENT,
  established at S94 W5-1), either (PASS) re-anchors the HELD m⁻³ Level-3 row to a
  substrate-physical scale under the Tier-2 dimensional-re-anchorability gate, or
  (FAIL/INFO) remains HELD because the divergent channel's truncation-invariant content
  is dimensionful (dimension and divergence occupy the same spectral slot), in which case
  no substrate-singled-out L* exists and the dimensionful magnitude is registry-PASS-INELIGIBLE.

method:
  description: >
    Saturated-tail recompute of the m⁻³ PBH number-density magnitude. (1) Load the S94 W5-1
    g-axis saturation machinery from s94_n_pbh_truncation_anchor.npz: the g-axis cardinality-
    cascade exponent, g_saturate=143, D1_frozen_sat_value_m3, n_PBH_frozen_saturation_m3,
    canonical_central_m3, the 4.1385x L10->L14 refinement factor. (2) Resolve which N the
    saturated tail uses: the L=10 atlas N=78,080 (= analytic 80,080 minus the dropped (4,4)
    sector, frozen-by-fiat) vs the saturation-converged N at g_saturate. (3) Recompute the
    m⁻³ magnitude at the g_saturate anchor and test L_max-independence (D1_g_of_K_Lmax_independent,
    D1_saturates_above_g_saturate already True in the npz; re-verify the magnitude image).
    (4) Apply the Tier-2 dimensional-re-anchorability gate (cross-pillar-bridge-anatomy.md
    §"Tier-1/Tier-2"): is the truncation-invariant content DIMENSIONLESS (Tier-2 re-anchorable
    via log-derivative / ratio / cohomology-class) or DIMENSIONFUL (Tier-2-dimensionful,
    registry-PASS-INELIGIBLE, row HELD)? The npz currently carries tier_classification=
    TIER-2-DIMENSIONFUL, invariant_is_dimensionless=True, dimension_and_divergence_same_slot=True,
    level3_m3_row=REGISTRY-PASS-INELIGIBLE-HELD, magnitude_decoupling_deferred=True. The gate
    must NOT assume that classification carries the verdict — it re-derives whether the
    g_saturate saturated-tail recompute changes the dimension/divergence-same-slot status.
  producing_script: "computations/_shared/s95_w6_1_n_pbh_magnitude_saturated_tail.py"

# ---- PRDR Checklist (8 items) ----

operator:
  type: "inequality + classification"
  form: >
    PASS  iff  |dln(n_PBH_sat)/dln L| < 1e-3 over L in {10,11,12,13,14} (L_max-INDEPENDENT
          at g_saturate)  AND  the truncation-invariant content is DIMENSIONLESS
          (invariant_is_dimensionless True AND dimension_and_divergence_same_slot False)
          ==> Tier-2 re-anchorable ==> m⁻³ Level-3 row discharged from HELD to
          substrate-physical-scale-anchored.
    HELD  iff  L_max-INDEPENDENT at g_saturate is confirmed BUT dimension and divergence
          occupy the same spectral slot (dimension_and_divergence_same_slot True) ==>
          Tier-2-DIMENSIONFUL ==> registry-PASS-INELIGIBLE ==> row stays
          NOT-SATISFIED-PENDING-substrate-physical-scale-anchor.
  notes: "Tier classification per cross-pillar-bridge-anatomy.md §'Tier-1/Tier-2 dimensional-re-anchorability gate'."

strict_PASS_boundary:
  value: "|dln(n_PBH_sat)/dln L| < 1e-3 AND dimension_and_divergence_same_slot == False"
  direction: "<"

boundary_reachable_analytically:
  bool: true
  proof_ref: >
    cross-pillar-bridge-anatomy.md §'Tier-1/Tier-2' (corpus §25): O(L,K)=W(L)·g(K) ==> only
    log-derivatives annihilate W(L); the dimensionful magnitude on a divergent channel cannot
    be re-anchored unless the truncation-invariant content is dimensionless. Inaugural occupant
    §VII.AX.OP-PROJ n_PBH (corpus §25).

reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "L in {10,11,12,13,14} integer mesh; g in {0..143} integer cardinality-cascade mesh"

machinery_pin_map:
  N_eval: "N_sat at g_saturate (resolved at runtime: L=10 atlas N=78080 vs saturation-converged N; declare which)"
  L_max: "14 (L-scan {10,11,12,13,14}; bottom-K saturation-checked, no fresh diagonalization beyond L=14 cache)"
  scan_range: "g in [0, 143] (cardinality-cascade saturation scan); L in [10, 14]"
  step_size: "Delta_g = 1 (integer cardinality), Delta_L = 1 (integer truncation)"
  tolerance: "1e-3 (L_max-independence on dln/dlnL); 1e-12 (FD floor on saturation-plateau check)"
  scheme: "g-axis-cardinality-cascade-saturated-tail"
  convention: "TIER-2-DIMENSIONAL-RE-ANCHORABILITY-GATE"
  random_seed: "N/A — deterministic"
  GPU_path: "numpy.linalg (cache-load only; no diagonalization — re-uses s94 npz arrays)"

audit_discriminators:
  audit_sha256_inputs: ["script", "canonical_constants", "s94_n_pbh_truncation_anchor.npz", "pinmap"]
  content_sha256_inputs: ["script"]

substitution_chain:
  required: true
  content: |
    Claim: "the factor-4.1385 gap between n_PBH_frozen_saturation_m3=1.758e-23 and
            canonical_central_m3=7.2761e-23 IS the L10->L14 refinement factor, so the
            magnitude is NOT L_max-independent in the naive (linear-L14) reading; the
            saturated-tail (g_saturate) reading is the L_max-independent one."
    Step 1: n_PBH_frozen_saturation_m3 = D1_frozen_sat_value_m3 = 1.7581364216177777e-23
            [npz; g-axis saturated tail at g_saturate=143]
    Step 2: canonical_central_m3       = 7.2761e-23
            [npz canonical_central_m3 = canonical_constants.py n_PBH_FW_central]
    Step 3: ratio = canonical_central_m3 / n_PBH_frozen_saturation_m3
                  = 7.2761e-23 / 1.7581364216177777e-23
    Step 4: Substitute and simplify
                  = 4.13853...                         [simplified]
            refinement_factor_L10_to_L14 (npz) = 4.138524590163934
            ratio_canonical_over_baseline (npz) = 4.138529815169166
    Step 5: ratio == refinement_factor_L10_to_L14 to 5 sig figs
            ==> the canonical_central magnitude carries the L10->L14 LINEAR refinement;
                the saturated-tail magnitude does NOT (it is the g-saturate plateau value).
    Conclusion: the two magnitudes are NOT the same observable — one is the linear-L14
                extrapolation, one is the g-axis saturation plateau. The recompute pins
                WHICH magnitude is L_max-INDEPENDENT (the saturated tail) and then asks
                whether THAT magnitude is Tier-2 re-anchorable (dimensionless invariant) or
                Tier-2-dimensionful (registry-PASS-INELIGIBLE).
    [SIGN] note: this gate has a [VERIFY] trigger, not a [SIGN] trigger — the verdict is a
                classification (re-anchorable vs HELD), not a directional prediction. No
                schema-v2 3-tuple companion row required.

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  s94_n_pbh_truncation_anchor:
    path: "computations/session-94/s94_n_pbh_truncation_anchor.npz"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^CF-S95-N-PBH-MAGNITUDE-RECOMPUTE:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/archive/session-95/session-95-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-1. CF-S95-N-PBH-MAGNITUDE-RECOMPUTE"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The saturated-tail m⁻³ magnitude is L_max-INDEPENDENT at g_saturate AND its
  truncation-invariant content is DIMENSIONLESS (re-anchorable). The §VII.AX m⁻³ Level-3 row
  is discharged from HELD NOT-SATISFIED-PENDING to a substrate-physical-scale-anchored value;
  the magnitude half of the held m⁻³ row closes (the which-anchor half having closed at S94 W5-1).
  Solution space: the PBH-number Level-3 anchor occupies a registry-PASS-eligible region.
FAIL_meaning: >
  The saturated-tail recompute does NOT yield an L_max-independent magnitude (the g_saturate
  plateau is itself L-drifting), i.e. the saturation anchor is not substrate-singled-out.
  Solution space: the m⁻³ Level-3 anchor has NO substrate-singled-out L*; the dimensionful-
  magnitude corridor is closed and the row stays HELD with no re-anchoring pathway.
INFO_meaning: >
  The magnitude is L_max-INDEPENDENT at g_saturate (saturation confirmed) BUT the truncation-
  invariant content is DIMENSIONFUL (dimension and divergence share the same spectral slot;
  npz currently flags dimension_and_divergence_same_slot=True). Per the Tier-2 gate this is
  Tier-2-dimensionful ==> registry-PASS-INELIGIBLE; the row remains HELD
  NOT-SATISFIED-PENDING-substrate-physical-scale-anchor, but the magnitude is now pinned to the
  substrate-physical g_saturate value (decoupling the magnitude question from the truncation
  question). The held-number guard (context §A4) is satisfied: this discharges the magnitude
  half WITHOUT double-counting; the theorem-STRUCTURE stays STAGE-3-PERMANENT.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w6_1_n_pbh_magnitude_saturated_tail.py"
    - "computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.npz"
    - "computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.png"
  estimated_time: "~1.0 wave-equivalent (re-uses S94 W5-1 g-axis machinery; cache-load only, no fresh diagonalization)"

substrate_framing: |
  CLASSIFICATION: GEOMETRIC (the fabric's eigenvalue-cardinality cascade, not an excitation
  spectrum). The substrate IS the g-axis cardinality cascade of the D_K spectrum on Jensen-
  deformed SU(3); the PBH number density m⁻³ is the Pillar-IX laboratory-IN image of the
  Pillar-I substrate-IS cardinality-cascade-tail observable (bridge family FWD-C5, per Row #65 /
  §VII.AX.OP-PROJ). Direction of explanation: D_K eigenvalue cardinality cascade -> g-axis
  saturation at g_saturate=143 -> saturated-tail number-density magnitude -> Pillar-IX PBH
  number density (laboratory-IN). The magnitude question is: does the cardinality cascade
  single out a substrate-physical scale (PASS/re-anchorable) or does the dimensionful magnitude
  live on a divergent channel sharing its slot with the dimension (INFO/HELD)? The held-number
  guard prevents treating this as a fresh prediction — it is the magnitude HALF of one held row.
```

---

## §W6-2. CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT

```yaml
# ---- Identity (6 fields) ----
gate_id: "CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT"
schema_version: "R3"
trigger: "[SIGN]"
classification: "PHONONIC"
agent_type: "mack-cosmic-bridge"
hypothesis: >
  The per-gapped-branch Layer-1/Layer-2 BAO sub-feature, transported through the full
  effacement projection (Gamma_effacement=0.99970 leakage; S43 A_FS=0.2045 first-sound
  imprint vs the ~1e-6 effacement floor) to an OBSERVED amplitude delta_P/P at k~0.043 Mpc⁻¹
  AND the S43 first-sound ring k1=0.0193 Mpc⁻¹, is either above (PASS) or below (INFO/FAIL) a
  named experiment's projected amplitude sensitivity — converting the S94 position-only
  SENSITIVITY bound into an amplitude DETECTION forecast.

method:
  description: >
    Amplitude transport. (1) Load the S94 W5-3 position-shift machinery from
    s94_bao_peak_branch.npz: b1_delta=0.01516 (the M_KK-internal B1 branch-speed split),
    shift_frac (=0.19 naive container-conflation), c_Gold=0.915, s84_c_T_over_c_S=2.0619,
    k_bao=0.043. (2) Compute the OBSERVED sub-feature amplitude (not just position) of the
    per-branch Layer-1/Layer-2 feature in the emergent matter power spectrum P(k) and CMB C_ell.
    The transport FORM is the effacement projection (c_b^(2)/c_Gold)^2 of the substrate split
    onto the emergent BAO (substrate-first; NOT a borrowed ΛCDM amplitude). (3) Project through
    the S43 transfer-function structure: does the substrate split imprint at the S43 A_FS~0.2045
    first-sound level or at the ~1e-6 effacement floor? Compute delta_P/P at k~0.043 Mpc⁻¹ and
    the distinct first-sound ring amplitude at k1=0.0193 Mpc⁻¹ (r1=325.3 Mpc). (4) FETCH a
    DESI DR2 / Simons Observatory / CMB-S4 P(k)-amplitude + theta_s sensitivity forecast via
    mcp__paper-search__* (DOWN in S94 — RE-CHECK availability at dispatch). (5) Compare the
    transported amplitude to the fetched/canonical sensitivity. The S94 position result is the
    upstream context: B1-dominant position shift 0.14452% (Sage-exact 0.19*17689/2325625),
    OUTSIDE DESI DR2 ruler 0.24% — so the LIVE channel is amplitude, principally the S43 ring.
  producing_script: "computations/_shared/s95_w6_2_bao_amplitude_transport.py"

# ---- PRDR Checklist (8 items) ----

operator:
  type: "inequality (forecast amplitude vs detector sensitivity)"
  form: >
    Let A_obs = transported sub-feature amplitude delta_P/P at k~0.043 (and A_ring at
    k1=0.0193); let S_exp = the named experiment's projected amplitude sensitivity.
    PASS iff A_obs >= S_exp for >=1 current/forecast experiment (decisive: detectable).
    FAIL iff A_obs < ~1e-6 effacement floor at ALL forecast detectors (structurally
    undetectable; effacement-suppressed below every horizon).
    INFO iff A_obs computed AND above the effacement floor BUT S_exp unavailable
    (paper-search down) OR A_obs below current precision but above CMB-S4 forecast (next-gen target).

strict_PASS_boundary:
  value: "A_obs(delta_P/P) >= S_exp(named experiment)  [decisive either direction per INFO/FAIL split]"
  direction: ">="

boundary_reachable_analytically:
  bool: false
  proof_ref: >
    The transport FORM (c_b^(2)/c_Gold)^2 and the S43 A_FS=0.2045 imprint are analytic; the
    detector sensitivity S_exp is empirical (fetched). Boundary is a fetched-anchor comparison,
    not an analytically-derived threshold. canonical_constants.py: Gamma_effacement=0.99970,
    c_Gold=0.915, c_B1/c_B2/c_B3/c_L (M_KK units); S43 KK-CMB-TF-43 (r1=325.3 Mpc, A_FS=0.2045).

reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous (P(k) over k-grid; two pinned scales k=0.043, k1=0.0193 Mpc⁻¹)"

machinery_pin_map:
  N_eval: "P(k) on a log-k grid spanning [1e-3, 1e-1] Mpc⁻¹; >=256 points; two pinned scales (0.043, 0.0193)"
  L_max: "N/A (Layer-2 emergent BdG branch speeds; no D_K diagonalization — re-uses s94 npz)"
  scan_range: "k in [1e-3, 1e-1] Mpc⁻¹ (log-spaced)"
  step_size: "log-uniform (>=256 pts/decade-equivalent)"
  tolerance: "RATIO; report delta_P/P to 3 sig figs (publication-precision pin; downstream comparator rel_tol >= 1e-3)"
  scheme: "effacement-amplitude-projection (c_b^2/c_Gold)^2"
  convention: "RATIO; substrate-first transport (NOT borrowed-LCDM-amplitude)"
  random_seed: "N/A — deterministic"
  GPU_path: "numpy.linalg (1D transport; cache-load only)"

audit_discriminators:
  audit_sha256_inputs: ["script", "canonical_constants", "s94_bao_peak_branch.npz", "fetched_forecast_value_or_INFO_flag", "pinmap"]
  content_sha256_inputs: ["script"]

substitution_chain:
  required: true
  content: |
    Claim: "the OBSERVED BAO sub-feature amplitude is the EFFACEMENT PROJECTION of the
            substrate two-speed split; the naive 19% is a container-thinking conflation of
            the M_KK-internal branch speed with the emergent 4D acoustic speed, and the
            transported amplitude is SMALLER than the naive split by (c_b^(2)/c_Gold)^2."
    Step 1: shift_frac (substrate, M_KK-internal) = 0.19            [npz shift_frac; B1..B3]
    Step 2: b1_delta (substrate split magnitude)  = 0.01516        [npz b1_delta]
    Step 3: transport FORM: A_obs,b = shift_b * (c_b^(2)/c_Gold)^2  [effacement projection;
            c_Gold=0.915 envelope; substrate-first, NOT borrowed ΛCDM]
    Step 4: Substitute (Reading-NS, B1-dominant): the S-1 synthesis gives the Sage-exact
            transported B1 position shift = 0.19 * 17689 / 2325625 = 0.14452% (position),
            i.e. (c_B1^(2)/c_Gold)^2 reduces 19% -> 0.14452%. The AMPLITUDE transport is the
            ANALOG projection onto delta_P/P, gated additionally by the S43 A_FS=0.2045 first-
            sound imprint vs the ~1e-6 effacement floor.
    Step 5: (c_b^(2)/c_Gold)^2 < 1 since every Layer-2 branch speed v_g <= c_Gold=0.915
            (canonical envelope) ==> A_obs,b < shift_b. DIRECTION: the transported amplitude
            is SMALLER than the naive split (effacement SUPPRESSES). The B1-position image
            0.14% < DESI DR2 ruler 0.24% confirms the suppression direction for position; the
            amplitude image inherits the same suppression sign.
    Conclusion: A_obs (transported amplitude) < naive split; effacement is a suppression, not
            an amplification. The live channel is the S43 first-sound ring (A_FS=0.2045, no
            ΛCDM counterpart), whose amplitude detectability sets the verdict.
    [SIGN] companion-row required: sign_verdict tracks whether the transported amplitude is
            BELOW the naive split (predicted: yes, effacement suppresses) AND on the correct
            side of the detector sensitivity; magnitude_verdict tracks |A_obs - S_exp|;
            regime_verdict tracks whether the fetched-forecast domain was available
            (VALID = forecast fetched; MARGINAL/BREAKDOWN = paper-search-down INFO branch).

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  s94_bao_peak_branch:
    path: "computations/session-94/s94_bao_peak_branch.npz"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w6_2_bao_amplitude_transport.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w6_2_bao_amplitude_transport.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w6_2_bao_amplitude_transport.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true
  wp_section:
    path: "sessions/archive/session-95/session-95-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-2. CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The transported sub-feature amplitude delta_P/P (at k~0.043 and/or the S43 ring k1=0.0193)
  is at or above a named experiment's projected amplitude sensitivity (DESI DR2 / Simons / CMB-S4)
  — a LIVE amplitude falsifier. Solution space: the two-speed structure is amplitude-detectable;
  the channel is promoted from sensitivity-bound to detection-forecast, decisive either direction
  (above = live test; the experiment can confirm or exclude the imprint).
FAIL_meaning: >
  The transported amplitude is below the ~1e-6 effacement floor at ALL forecast detectors —
  structurally undetectable (effacement-suppressed below every horizon). Solution space: the
  per-branch BAO amplitude channel is closed observationally; only the position-bound (already
  OUTSIDE DESI DR2) and the S43 ring (if it survives the floor) remain as channels.
INFO_meaning: >
  Forecast amplitude computed and above the effacement floor, BUT (a) the experiment sensitivity
  is unavailable (mcp__paper-search__* DOWN at dispatch — the PRE-REGISTERED INFO branch), OR
  (b) the amplitude is below current precision but above the CMB-S4 forecast (a next-gen target).
  In branch (a) the bounding-estimate CMB-S4 floor from the S94 S-1 synthesis is used and the
  structural conclusion (suppression direction, S43-ring-is-the-live-channel) is reported as
  robust without the fetched value; the fetched-forecast comparison is carried forward.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w6_2_bao_amplitude_transport.py"
    - "computations/session-95/s95_w6_2_bao_amplitude_transport.npz"
    - "computations/session-95/s95_w6_2_bao_amplitude_transport.png"
  estimated_time: "~1.0 wave-equivalent (re-uses S-1 transport + S43 transfer-function structure; new work = effacement-amplitude projection + P(k)/C_ell amplitude compute + fetched forecast)"

substrate_framing: |
  CLASSIFICATION: PHONONIC (Layer-2 acoustic excitations of the fabric; the BAO feature is an
  interference pattern of post-transit GGE acoustic excitations). SCALE-AND-CHANNEL-TAGGED per
  phononic-framing.md §"Scale-and-channel-tagging": the substrate-IS observable is the M_KK-internal
  per-branch Layer-1/Layer-2 two-speed split (M_KK units, inside the fiber); the laboratory-IN
  observable is the emergent BAO sub-feature amplitude delta_P/P at the CMB/LSS pivot k~0.043 Mpc⁻¹
  and the S43 first-sound ring k1=0.0193 Mpc⁻¹ (Mpc⁻¹, in the container-observer's P(k)/C_ell). The
  BRIDGE is the effacement projection (c_b^(2)/c_Gold)^2 + the S43 transfer function — NOT a borrowed
  ΛCDM amplitude. Direction: D_K spectrum -> Layer-2 BdG branch speeds (c_B1..c_L <= c_Gold) ->
  substrate two-speed split -> effacement projection -> emergent BAO amplitude -> detector comparison.
  Matched (scale, channel) pair: the comparison against DESI DR2 / Simons / CMB-S4 is valid ONLY at
  the emergent/pivot scale, never at the substrate/BZ scale (a category error the framework closed at
  S94 W5-3; the naive 19% is the unmatched substrate-scale number).
```

---

## §W6-3. DE-JOINT-POSTERIOR-RESOURCE

```yaml
# ---- Identity (6 fields) ----
gate_id: "DE-JOINT-POSTERIOR-RESOURCE"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "NON-PHONONIC"
agent_type: "mack-cosmic-bridge"
hypothesis: >
  The §7.1 dark-energy (w0, wa) anchors can be sourced to ONE joint (w0, wa) posterior with
  declared provenance and a single named release, replacing the current two-rows-from-two-
  compilations defect; and the 1D-marginal-vs-2D-rectangle footnote correctly scopes the
  σ-distances as 1-parameter marginals subordinate to the 2D R_842 rectangle falsifier.

method:
  description: >
    Doc-data hygiene gate (artifact-existence-style PASS predicate; per plan-compute discipline,
    pre-registered honestly as a one-fit-anchor + provenance-present check). (1) DECLARE which
    release the §7.1 anchors cite: DESI DR2 (w0=-0.752+-0.057, wa=-0.73+-0.25, rho~-0.85) OR the
    combined DES-Dovekie compilation (w0=-0.803+-0.054, wa=-0.72+-0.21). The mack-collab §2
    fidelity correction is the authoritative source: the canonical registry value is DESI DR2
    (-0.752/-0.73); the document's -0.803 is the tighter DES-Dovekie + multi-probe joint. (2)
    EMIT a single joint-posterior resource block to the WP: the chosen (w0, wa) pair from ONE fit,
    with rho, with provenance tag (release + table + paper), consumed by the doc-integration track.
    (3) VERIFY the two §7.1 rows would cite ONE fit (the defect was w0 from one compilation, wa from
    another). (4) ADD the 1D-marginal-vs-2D-rectangle footnote text. The gate OUTPUT is the sourced
    anchor + provenance tag + footnote, written to the WP §W6-3 section (NOT a doc edit to
    phonic-exflation-equation.md — that is the routed /rclab-workshop doc-integration track).
  producing_script: "computations/_shared/s95_w6_3_de_joint_posterior_resource.py"

# ---- PRDR Checklist (8 items) ----

operator:
  type: "set + existence (artifact-existence-style hygiene predicate)"
  form: >
    PASS iff (a) ONE named release is declared AND (b) the (w0, wa) pair comes from that ONE fit
    (with rho) AND (c) a provenance tag (release + table/paper) is emitted AND (d) the 1D-marginal-
    vs-2D-rectangle footnote text is present in the WP §W6-3 section AND (e) the recomputed σ-distances
    against the declared anchor match the substitution chain to 2 sig figs.

strict_PASS_boundary:
  value: "5-of-5 sub-conditions (a..e) satisfied; σ-distance match to rel_tol <= 1e-2"
  direction: "="

boundary_reachable_analytically:
  bool: true
  proof_ref: >
    σ-distance is closed-form |w_FW - w_obs|/sigma_obs; mack-collab §2 already worked it (2.13σ
    canonical, 0.73σ branch-iv against -0.803+-0.054). canonical_constants.py: w0_FW=-0.918,
    w0_FW_R842=-0.842454 (branch iv), wa_FW=0.0.

reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — discrete anchor-pair selection (one of two named releases)"

machinery_pin_map:
  N_eval: "2 branches (canonical w0_FW=-0.918; branch-iv w0_FW_R842=-0.842454) x 1 declared anchor"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "rel_tol <= 1e-2 on σ-distance reproduction"
  scheme: "doc-data-hygiene"
  convention: "1D-marginal-reported-2D-rectangle-binding"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu (arithmetic only)"

audit_discriminators:
  audit_sha256_inputs: ["script", "canonical_constants", "declared_anchor_tuple", "pinmap"]
  content_sha256_inputs: ["script"]

substitution_chain:
  required: true
  content: |
    Claim: "the σ-distances must be sourced to ONE joint fit; w0 from one compilation + wa from
            another cannot be read as a real tension because (w0, wa) are jointly constrained
            with rho ~ -0.85."
    Step 1: w0_FW (canonical)      = -0.918            [canonical_constants.py:1806, S58 four-fold lock]
    Step 2: w0_FW_R842 (branch iv) = -0.842454         [canonical_constants.py branch-(iv), W0-workshop]
    Step 3: DECLARED anchor (choose ONE):
            (A) DESI DR2:        w0_obs=-0.752, sigma=0.057, wa_obs=-0.73, sigma=0.25, rho~-0.85
            (B) DES-Dovekie+multi-probe: w0_obs=-0.803, sigma=0.054, wa_obs=-0.72, sigma=0.21, rho~-0.85
    Step 4: σ_canonical = |w0_FW - w0_obs| / sigma_obs
            under (B): = |-0.918 - (-0.803)| / 0.054 = 0.115/0.054 = 2.13σ   [matches mack-collab §2]
            σ_branch_iv = |-0.842454 - (-0.803)| / 0.054 = 0.039454/0.054 = 0.73σ  [matches §2]
            under (A): = |-0.918 - (-0.752)| / 0.057 = 0.166/0.057 = 2.91σ (canonical, DR2)
    Step 5: the (w0, wa) pair MUST come from the SAME Step-3 row (A xor B); mixing -0.803 (w0
            from B) with -0.73 (wa from A) is the defect. DIRECTION: the joint 2D R_842 rectangle
            is the binding falsifier; the 1D marginals are subordinate annotations.
    Conclusion: emit ONE row's (w0, wa, rho) + provenance; footnote the 1D-vs-2D scoping.
    [SIGN] note: [VERIFY] trigger (hygiene existence + σ-reproduction), not [SIGN]; no 3-tuple row.

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w6_3_de_joint_posterior_resource.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w6_3_de_joint_posterior_resource.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w6_3_de_joint_posterior_resource.png"
    artifact_kind: "plot"
    optional: true
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^DE-JOINT-POSTERIOR-RESOURCE:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/archive/session-95/session-95-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-3. DE-JOINT-POSTERIOR-RESOURCE"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  A single joint (w0, wa) posterior from ONE declared release is emitted with provenance tag,
  rho, and the 1D-marginal-vs-2D-rectangle footnote; the σ-distances reproduce against the
  declared anchor. The §7.1 doc-data defect (two rows, two compilations) has a sourced fix ready
  for the doc-integration track. Solution space: the DE comparison anchor is audit-traceable and
  the 2D R_842 rectangle falsifier is correctly foregrounded over the 1D marginals.
FAIL_meaning: >
  No single fit can supply both (w0, wa) with declared provenance (e.g. the chosen release does
  not publish a joint posterior, or the σ-distances do not reproduce). Solution space: the §7.1
  anchor remains un-sourced; the doc-integration track cannot proceed on the DE row.
INFO_meaning: >
  The joint posterior is declared and the footnote written, BUT a precision/release ambiguity
  remains (e.g. DR3 supersedes mid-session and the canonical anchor needs re-pinning) — the fix is
  emitted with a deferred re-pin tag.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w6_3_de_joint_posterior_resource.py"
    - "computations/session-95/s95_w6_3_de_joint_posterior_resource.npz"
  estimated_time: "minutes (verbiage + provenance + σ-reproduction check); per mack-collab §2 this is the ONE REQUIRED fidelity fix"

substrate_framing: |
  CLASSIFICATION: NON-PHONONIC (doc-data hygiene; observational-anchor sourcing). This gate does
  not compute a substrate quantity — it sources the EXTERNAL comparison anchor for the framework's
  w0_FW/wa_FW predictions (which ARE substrate-derived: w0_FW from the Volovik partition + effacement
  Gamma=0.99970, S58 four-fold lock; wa_FW=0 structural). The substrate-first discipline here is at
  the SOURCING layer (substrate-first-canonical-sourcing.md): the framework value is from D_K; the
  comparison anchor is a methodological cross-check that MUST declare its provenance, never a
  canonical replacement. The defect mack-collab §2 flags is exactly a sourcing-layer hygiene gap:
  an external anchor whose provenance is undeclared and whose (w0, wa) pair is mixed across two fits.
```

---

## §W6-4. W0-MKK-PROVENANCE

```yaml
# ---- Identity (6 fields) ----
gate_id: "W0-MKK-PROVENANCE"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "NON-PHONONIC"
agent_type: "mack-cosmic-bridge"
hypothesis: >
  PROVENANCE entries for w0_FW and M_KK can be added to the knowledge MCP via update_constant
  such that get_constant returns a non-empty PROVENANCE block for each — closing the confirmed
  hygiene gap before the DESI DR3 binding event (w0_FW binds Falsifier #1).

method:
  description: >
    Constant-hygiene gate (provenance-present PASS predicate). (1) RE-CONFIRM the gap:
    get_constant("w0_FW") -> -0.918 with "No PROVENANCE entry"; get_constant("M_KK") ->
    7.428660036284456e16 with "No PROVENANCE entry" (both confirmed this planning run). (2) Add
    PROVENANCE for w0_FW via update_constant: value=-0.918, session=S58, source=S58 four-fold-lock
    (Volovik vacuum partition + effacement Gamma_effacement=0.99970), gate references S58 derivation
    + S42 Sakharov/zeta route context, comment naming the four-fold lock + that it binds Falsifier #1
    (DESI DR3). (3) Add PROVENANCE for M_KK: value=7.428660036284456e16, session=S42,
    source=s42_constants_snapshot.npz (spectral-zeta / Newton's-constant gravity route),
    gate=CONST-FREEZE-42, comment naming the gravity route (~7.43e16 GeV) + the Kerner alternate
    (M_KK_kerner=5.04e17, 0.83 decades) so the route choice is documented. NOTE: M_KK is an alias for
    M_KK_gravity, which ALREADY carries provenance (derived_from S42, per the knowledge graph) — the
    gap is on the bare M_KK alias; the entry mirrors M_KK_gravity's provenance. (4) VERIFY: re-run
    get_constant on BOTH and confirm non-empty PROVENANCE blocks. Per math-scripts.md canonical
    write-order, these are single update_constant calls with no derivation ambiguity ==> FIX-IN-SESSION.
  producing_script: "computations/_shared/s95_w6_4_w0_mkk_provenance.py"

# ---- PRDR Checklist (8 items) ----

operator:
  type: "existence (provenance-present check on both constants)"
  form: >
    PASS iff get_constant("w0_FW") returns a non-empty PROVENANCE block AND
    get_constant("M_KK") returns a non-empty PROVENANCE block, after the two update_constant
    calls land, AND the recorded values are UNCHANGED (-0.918, 7.428660036284456e16).

strict_PASS_boundary:
  value: "2-of-2 constants carry non-empty PROVENANCE; values bit-unchanged"
  direction: "="

boundary_reachable_analytically:
  bool: true
  proof_ref: >
    Provenance routes are documented: w0_FW = S58 four-fold lock (canonical_constants.py:1806
    inline 'Volovik vacuum + effacement (S58)'); M_KK = S42 spectral-zeta/Newton's-constant gravity
    route (knowledge graph edge constants:M_KK_gravity --derived_from--> sessions:42;
    canonical_constants.py:344). No new derivation — provenance transcription only.

reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — two discrete provenance writes"

machinery_pin_map:
  N_eval: "2 (w0_FW, M_KK)"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "exact (values must be bit-unchanged: -0.918, 7.428660036284456e16)"
  scheme: "constant-hygiene"
  convention: "provenance-transcription-no-revalue"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu (MCP write + read-back only)"

audit_discriminators:
  audit_sha256_inputs: ["script", "canonical_constants", "two_provenance_strings", "pinmap"]
  content_sha256_inputs: ["script"]

substitution_chain:
  required: false
  content: |
    No directional / sign / threshold claim — this is a provenance-existence hygiene write.
    Value-invariance check (NOT a directional claim): w0_FW stays -0.918, M_KK stays
    7.428660036284456e16; update_constant adds the PROVENANCE block WITHOUT overwriting the value
    (per the update_constant contract: never overwrite existing constant values without explicit
    approval — here only provenance metadata is added).

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w6_4_w0_mkk_provenance.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w6_4_w0_mkk_provenance.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w6_4_w0_mkk_provenance.png"
    artifact_kind: "plot"
    optional: true
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^W0-MKK-PROVENANCE:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/archive/session-95/session-95-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-4. W0-MKK-PROVENANCE"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  Both w0_FW and M_KK carry non-empty PROVENANCE blocks in the knowledge MCP, values unchanged.
  Falsifier #1's binding constant (w0_FW) is audit-traceable before DESI DR3. Solution space:
  the falsifier-anchor provenance gap is closed; no audit blind-spot at the DR3 binding event.
FAIL_meaning: >
  At least one provenance write does not land OR a value is inadvertently changed. Solution space:
  the hygiene gap persists; re-dispatch the write (this is mechanical, not a physics FAIL).
INFO_meaning: >
  Provenance added but a derivation-ambiguity surfaces (e.g. w0_FW has a dual canonical: the S58
  -0.918 structural value vs the branch-(iv) -0.842454 W0-workshop promotion) — the PROVENANCE block
  documents BOTH incarnations and flags the branch-(iv) conditionality, which is the correct record.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w6_4_w0_mkk_provenance.py"
    - "computations/session-95/s95_w6_4_w0_mkk_provenance.npz"
  estimated_time: "minutes (single hygiene pass; two update_constant calls + read-back)"

substrate_framing: |
  CLASSIFICATION: NON-PHONONIC (constant-provenance hygiene). The constants ARE substrate-derived
  (w0_FW from the Volovik vacuum partition + effacement, S58 four-fold lock; M_KK from the spectral-
  zeta/Newton's-constant gravity route, S42) — this gate adds the audit-trail provenance so those
  substrate derivations are traceable from the knowledge MCP. Methodology contribution: closes an
  AMRI-adjacent gap at the canonical-constants layer (provenance belongs in canonical_constants.py +
  knowledge.db, never in agent memory) before the DESI DR3 falsifier binds. w0_FW is the binding
  constant for Falsifier #1, so the provenance must be in place before the 2026 binding event.
```

---

## §W6-5. LEGGETT-GRAV-DECAY-CONDITIONAL

```yaml
# ---- Identity (6 fields) ----
gate_id: "LEGGETT-GRAV-DECAY-CONDITIONAL"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "mack-cosmic-bridge"
hypothesis: >
  LEGGETT-GRAV-DECAY-67 (CRITICAL) can be surfaced as a STATED conditional on the Omega_DM h²=0.120
  PASS — i.e. the DM row is a PASS *given* Gamma_grav < H_0; if the gravitational decay vertex
  exceeds H_0 the Leggett DM sector collapses and the 0.120 value is meaningless — and this
  conditional lands as a falsifier-inventory annotation without re-adjudicating the PASS.

method:
  description: >
    Falsifier-inventory landing gate (mack-cosmic-bridge sole writer of falsifier-master-inventory.md
    per feedback_mack-bridge-role.md). (1) CONFIRM the knowledge-base flag: trace_entity
    ("LEGGETT-GRAV-DECAY") -> proven_1967 "If Gamma_grav > H_0, DM sector collapses (Omega_DM h²=0.120
    meaningless)", CRITICAL; gate LEGGETT-GRAV-DECAY-67 PASS (Gamma_grav < H_0); LEGGETT-GRAV-DECAY-73a
    PASS (tau_DM/t_univ = 1.13e+65). (2) STATE the conditional structure: the Omega_DM h²=0.120 PASS
    (0.7σ vs Planck 0.1186+-0.0020) is conditional on the gravitational-stability bound Gamma_grav < H_0.
    This is the SECOND delicacy on the DM sector (the FIRST being "full-DM route over-closes at 260σ;
    only Leggett-only passes"); both belong together. (3) LAND a falsifier-inventory annotation row
    (next free: Row #68) recording LEGGETT-GRAV-DECAY-67 as the stated conditional on the
    Omega_DM h²=0.120 row, citing the verdict-line audit_sha256 of the existing S67/S73a Leggett gates
    (no new value — this surfaces an existing CRITICAL gate as a conditional annotation). NO canonical
    write-order Step 2 (no NEW prediction value; this is an annotation of an existing proven result).
    The gate does NOT re-run the decay vertex — it surfaces the existing PASS as a stated conditional.
  producing_script: "computations/_shared/s95_w6_5_leggett_grav_decay_conditional.py"

# ---- PRDR Checklist (8 items) ----

operator:
  type: "existence + conditional-statement landing"
  form: >
    PASS iff (a) the LEGGETT-GRAV-DECAY-67 CRITICAL gate is confirmed PASS (Gamma_grav < H_0) in
    the knowledge base AND (b) a falsifier-inventory annotation row is landed stating the
    Omega_DM h²=0.120 PASS is conditional on Gamma_grav < H_0 AND (c) the row cites the existing
    Leggett-gate audit_sha256 (S67/S73a) AND (d) the row does NOT re-adjudicate the PASS verdict.

strict_PASS_boundary:
  value: "4-of-4 sub-conditions (a..d); existing CRITICAL gate PASS confirmed; annotation landed"
  direction: "="

boundary_reachable_analytically:
  bool: true
  proof_ref: >
    LEGGETT-GRAV-DECAY-67 PASS is established (knowledge base proven_1967; tau_DM/t_univ=1.13e+65 at
    S73a). The conditional structure is a logical statement, not a recomputation. nazarewicz-collab
    §R2 is the authoritative recommendation source.

reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — single annotation landing"

machinery_pin_map:
  N_eval: "1 (the LEGGETT-GRAV-DECAY-67 conditional annotation)"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "exact (existence of CRITICAL-gate PASS + annotation row)"
  scheme: "falsifier-inventory-conditional-annotation"
  convention: "conditional-PASS-given-Gamma_grav-lt-H_0"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu (registry write + MCP read)"

audit_discriminators:
  audit_sha256_inputs: ["script", "leggett_67_73a_audit_shas", "inventory_row_text", "pinmap"]
  content_sha256_inputs: ["script"]

substitution_chain:
  required: true
  content: |
    Claim: "the Omega_DM h²=0.120 PASS is a CONDITIONAL PASS: PASS given Gamma_grav < H_0; if
            Gamma_grav > H_0 the DM sector collapses and 0.120 is meaningless."
    Step 1: Omega_DM h²_FW (Leggett-only) = 0.120        [framework; vs Planck 0.1186+-0.0020 = 0.7σ PASS]
    Step 2: LEGGETT-GRAV-DECAY-67 gate criterion: PASS iff Gamma_grav < H_0; FAIL iff Gamma_grav > H_0
            [knowledge base proven_1967, CRITICAL]
    Step 3: at S73a, tau_DM / t_univ = 1.13e+65 >> 1  ==>  Gamma_grav = 1/tau_DM << 1/t_univ ~ H_0
            ==>  Gamma_grav < H_0  ==>  gate PASS
    Step 4: DIRECTION: tau_DM/t_univ = 1.13e+65 >> 1 means the decay is 65 orders SLOWER than a
            Hubble time ==> Gamma_grav/H_0 ~ 1e-65 << 1 ==> the conditional is SATISFIED with enormous
            margin. The Z_2 parity P_L (J-evenness of the condensate, S73a) protects the channel.
    Step 5: therefore the Omega_DM h²=0.120 PASS STANDS conditional on a bound that is satisfied by
            65 orders of magnitude; the conditional is stated (not a live risk) but MUST be surfaced
            because the document currently presents 0.120 as an unconditional clean PASS.
    Conclusion: land the stated conditional; the PASS is robust but the conditional belongs next to
            the 260σ-over-closure delicacy as the SECOND delicacy on the DM sector.
    [SIGN] note: [VERIFY] trigger (existence + conditional landing); the directional content
            (Gamma_grav << H_0 by 65 OOM) is a confirmation of an existing PASS, not a new gate;
            no schema-v2 3-tuple row (no new numerical verdict emitted).

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w6_5_leggett_grav_decay_conditional.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w6_5_leggett_grav_decay_conditional.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w6_5_leggett_grav_decay_conditional.png"
    artifact_kind: "plot"
    optional: true
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^LEGGETT-GRAV-DECAY-CONDITIONAL:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/archive/session-95/session-95-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-5. LEGGETT-GRAV-DECAY-CONDITIONAL"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The LEGGETT-GRAV-DECAY-67 CRITICAL gate is confirmed PASS (Gamma_grav < H_0 by ~65 OOM) and a
  falsifier-inventory annotation row is landed stating the Omega_DM h²=0.120 PASS as conditional on
  that bound, citing the existing S67/S73a Leggett-gate audit_sha256, without re-adjudicating the PASS.
  Solution space: the DM-sector conditional structure is now complete (260σ-over-closure delicacy +
  gravitational-stability delicacy), and the inventory records the falsifier as a STATED conditional.
FAIL_meaning: >
  The annotation cannot be landed (e.g. the CRITICAL gate's audit_sha256 is not locatable, or the
  landing would re-adjudicate the PASS). Solution space: the conditional remains unstated in the
  inventory; the DM row continues to read as an unconditional PASS (the nazarewicz-collab §R2 gap persists).
INFO_meaning: >
  The conditional is landed BUT a sub-question surfaces (e.g. whether Gamma_grav should be re-derived
  at higher precision than the S73a tau_DM/t_univ=1.13e+65) — flagged as a deferred refinement, not a
  blocker; the conditional stands on the existing margin.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w6_5_leggett_grav_decay_conditional.py"
    - "computations/session-95/s95_w6_5_leggett_grav_decay_conditional.npz"
  estimated_time: "minutes (surface existing CRITICAL gate as a stated conditional; one inventory annotation row)"

substrate_framing: |
  CLASSIFICATION: PHONONIC (the Leggett-channel DM is an inter-band coherence mode — a phononic
  excitation of the fabric, CPT-neutral, non-annihilating, integrability-protected GGE quasiparticle).
  The gravitational decay vertex <g,g|H_grav|L> couples the Leggett DM quasiparticle to the gravitational
  sector; the Z_2 parity P_L (J-evenness of the condensate, S73a) protects it, giving tau_DM/t_univ=1.13e+65.
  Direction: D_K spectrum -> Leggett inter-band coherence mode -> a_2-channel DM relic Omega_DM h²=0.120 ->
  gravitational-stability bound Gamma_grav < H_0 (the conditional). The conditional is the SECOND delicacy
  on the DM identity (the FIRST being the 260σ full-DM over-closure forcing the Leggett-only channel). Per
  feedback_mack-bridge-role.md, mack-cosmic-bridge is the SOLE writer of falsifier-master-inventory.md; this
  annotation lands there as the conditional on the existing Omega_DM h² row, NOT a new prediction value.
```

---

## §W6-6. F-NL-ROW

```yaml
# ---- Identity (6 fields) ----
gate_id: "F-NL-ROW"
schema_version: "R3"
trigger: "[SIGN]"
classification: "PHONONIC"
agent_type: "transit-dynamics-theorist"
hypothesis: >
  The framework non-Gaussianity |f_NL| <= ~1.5 (Bogoliubov sudden-quench; squeezed vacuum is
  Gaussian by Wick's theorem, phi_k≈0 kills the folded enhancement) is consistent with Planck
  f_NL^local = -0.9 +- 5.1 as a zero-free-parameter PASS-class structural result, and the
  canonical max|f_NL| = 1.505 (transit-dynamics canonical) lands as a falsifier-inventory row.

method:
  description: >
    Compute/confirm the framework f_NL bound and land the falsifier row. (1) CONFIRM the structural
    theorem: "Bogoliubov Gaussianity Preservation — f_NL = O(epsilon) regardless of squeezing"
    (S65 W5-D, PERMANENT; knowledge base). A squeezed vacuum is a Gaussian state; by Wick's theorem
    all connected 3-point functions vanish at leading order, so the bispectrum is O(epsilon) (slow-roll-
    suppressed), NOT enhanced by the squeezing. The folded-shape enhancement that a non-Gaussian
    initial state would produce is killed because phi_k≈0 (the mode-function phase). (2) CONFIRM the
    transit-collab §V.3 canonical value: max|f_NL| = 1.505 (Bogoliubov sudden-quench). Cross-check
    against the existing canonical f_NL pins (f_NL_FW_S82_equilateral=0.0547, f_NL_FW_S67_folded=0.129,
    f_NL_FW_S85_W9_3_analytic_template=0.7685) — the 1.505 is the MAX across shapes/channels, the
    envelope, NOT a replacement for the per-shape values. (3) Compare to Planck f_NL^local=-0.9+-5.1:
    |1.505 - (-0.9)|/5.1 = 0.47σ (and the per-shape values are well inside). (4) Per canonical
    write-order (math-scripts.md): Step 1 verdict line; Step 2 add max_f_NL_FW=1.505 to
    canonical_constants.py via update_constant WITH provenance (transit-dynamics canonical, Bogoliubov
    sudden-quench) — it is a NEW canonical envelope value not yet pinned; Step 3 mack-cosmic-bridge
    lands the f_NL falsifier row (next free: Row #69) citing the verdict audit_sha256 + the canonical
    constant name. NOTE on agent split: the f_NL VALUE/derivation is transit-dynamics (sudden-quench
    Bogoliubov, squeezed-vacuum Wick); the INVENTORY ROW landing is mack-cosmic-bridge (sole writer).
  producing_script: "computations/_shared/s95_w6_6_f_nl_row.py"

# ---- PRDR Checklist (8 items) ----

operator:
  type: "inequality + ratio (consistency vs Planck) + row landing"
  form: >
    PASS iff (a) max|f_NL| = 1.505 confirmed (transit canonical, Bogoliubov sudden-quench) AND
    (b) |max_f_NL_FW - f_NL_Planck| / sigma_Planck <= 1 (consistency: a squeezed-vacuum origin is
    FALSIFIED by large f_NL, so a small f_NL is the structural prediction) AND (c) the f_NL falsifier
    row is landed with both halves (framework |f_NL|<=1.5 + Planck -0.9+-5.1).

strict_PASS_boundary:
  value: "|1.505 - (-0.9)| / 5.1 = 0.47σ <= 1.0  (consistency); row landed with both halves"
  direction: "<="

boundary_reachable_analytically:
  bool: true
  proof_ref: >
    "Bogoliubov Gaussianity Preservation — f_NL = O(epsilon) regardless of squeezing" (S65 W5-D,
    PERMANENT; baseline-findings-s66 + atlas-07-permanent-results). Wick's theorem on a Gaussian
    (squeezed-vacuum) state ==> connected 3-pt = O(epsilon). transit-collab §V.3: max|f_NL|=1.505.

reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — single envelope value (1.505) + 3 existing per-shape pins (0.0547, 0.129, 0.7685)"

machinery_pin_map:
  N_eval: "4 (max envelope 1.505 + S82 equilateral 0.0547 + S67 folded 0.129 + S85 template 0.7685)"
  L_max: "N/A (Bogoliubov sudden-quench; no D_K diagonalization)"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "RATIO; σ-distance vs Planck; publication-precision 4 sig figs on 1.505 (downstream rel_tol >= 1e-4)"
  scheme: "Bogoliubov-sudden-quench"
  convention: "squeezed-vacuum-Gaussian-by-Wick"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu (analytic value + arithmetic)"

audit_discriminators:
  audit_sha256_inputs: ["script", "canonical_constants", "max_f_NL_value", "planck_f_NL_bound", "pinmap"]
  content_sha256_inputs: ["script"]

substitution_chain:
  required: true
  content: |
    Claim: "the framework f_NL is SMALL (|f_NL| <= ~1.5), consistent with Planck; a squeezed-vacuum
            origin is FALSIFIED by LARGE f_NL — so small f_NL is the structural prediction, and a
            future large-f_NL detection would falsify the squeezed-vacuum cosmogenesis."
    Step 1: GGE relic state = squeezed vacuum (Bogoliubov sudden-quench; P_exc->1.000, S65/S82)
    Step 2: Wick's theorem on a Gaussian state: <phi phi phi>_connected = 0 at leading order
            ==> bispectrum B(k1,k2,k3) = O(epsilon) (slow-roll-suppressed), NOT squeezing-enhanced
            ["Bogoliubov Gaussianity Preservation — f_NL=O(epsilon) regardless of squeezing", S65 W5-D PERMANENT]
    Step 3: max|f_NL| = 1.505                                  [transit-collab §V.3 canonical]
    Step 4: Substitute into σ-distance vs Planck f_NL^local=-0.9+-5.1:
            |max_f_NL_FW - f_NL_Planck| / sigma_Planck = |1.505 - (-0.9)| / 5.1 = 2.405/5.1 = 0.47σ
            per-shape values (0.0547, 0.129, 0.7685) are even closer (all << 1σ)
    Step 5: DIRECTION: f_NL_FW is SMALL and POSITIVE-bounded; |f_NL|<=1.505 << sigma_Planck=5.1
            ==> deep inside the Planck bound. The structural content: phi_k≈0 kills the folded
            enhancement (a non-Gaussian initial state would give |f_NL| >> 1; the squeezed vacuum
            does NOT). FALSIFIER direction: a detected |f_NL| >> 1.5 would falsify the squeezed-vacuum
            cosmogenesis ==> the row is a real (if currently-satisfied) falsifier.
    Conclusion: PASS-class structural consistency; land the row with the falsifier direction stated.
    [SIGN] companion-row required: sign_verdict = whether f_NL_FW is BOUNDED-SMALL (predicted: yes,
            |f_NL|<=1.5 by Gaussianity preservation); magnitude_verdict = the 0.47σ consistency;
            regime_verdict = whether the Bogoliubov-sudden-quench / Wick regime is valid (VALID, the
            squeezed-vacuum state is exactly Gaussian at leading order).

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w6_6_f_nl_row.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w6_6_f_nl_row.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w6_6_f_nl_row.png"
    artifact_kind: "plot"
    optional: true
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^F-NL-ROW:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true
  wp_section:
    path: "sessions/archive/session-95/session-95-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-6. F-NL-ROW"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  max|f_NL| = 1.505 confirmed (Bogoliubov sudden-quench, squeezed-vacuum Gaussian by Wick),
  consistent with Planck f_NL^local=-0.9+-5.1 at 0.47σ; the f_NL falsifier row is landed with both
  halves; max_f_NL_FW=1.505 is promoted to canonical_constants.py with provenance. Solution space:
  the non-Gaussianity channel is a zero-free-parameter structural PASS; a future large-f_NL detection
  (|f_NL| >> 1.5, e.g. CMB-S4 / 21-cm) would falsify the squeezed-vacuum cosmogenesis — a real falsifier.
FAIL_meaning: >
  The 1.505 value does not reproduce, OR the framework f_NL is NOT consistent with Planck (>1σ), OR
  the row cannot be landed with both halves. Solution space: the Gaussianity-preservation prediction
  is in tension with data, or the canonical envelope value is mis-pinned.
INFO_meaning: >
  The value and consistency are confirmed BUT a shape-channel ambiguity surfaces (e.g. which of the
  per-shape pins 0.0547/0.129/0.7685 vs the 1.505 envelope is the "headline" f_NL for the row) — the
  row lands with the envelope 1.505 as the bound and the per-shape values as the detail, flagged for
  the canonical write-order Step 2 sub-keying decision (per-shape already pinned; envelope is new).

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w6_6_f_nl_row.py"
    - "computations/session-95/s95_w6_6_f_nl_row.npz"
  estimated_time: "<1 hour (value already canonical at transit §V.3; confirm + σ-distance + canonical_constants promotion + inventory row)"

substrate_framing: |
  CLASSIFICATION: PHONONIC (the bispectrum is the 3-point correlation of post-transit GGE acoustic
  excitations — non-Gaussianity of the squeezed-vacuum relic). Direction: D_K spectrum -> Bogoliubov
  sudden-quench at the fold -> squeezed-vacuum GGE relic (P_exc->1.000) -> Wick's theorem on the Gaussian
  state kills connected 3-pt at leading order -> f_NL = O(epsilon), |f_NL| <= 1.505 -> Planck bispectrum
  comparison. The structural content (S65 W5-D PERMANENT): squeezing does NOT enhance non-Gaussianity
  because a squeezed vacuum is still Gaussian; the folded-shape enhancement is killed by phi_k≈0. The
  falsifier direction: a LARGE detected f_NL (>> 1.5) falsifies the squeezed-vacuum cosmogenesis, so the
  small predicted f_NL is a genuine (currently-satisfied) falsifier. AGENT SPLIT: the f_NL value is
  transit-dynamics (Bogoliubov sudden-quench derivation); the inventory ROW is mack-cosmic-bridge (sole
  writer of falsifier-master-inventory.md per feedback_mack-bridge-role.md) via canonical write-order Step 3.
```

---

## Wave 6 → Wave 7 Decision Point

Wave 6 produces NO output consumed by Wave 7 (W7 = the KK-internal γ_E crystallization, Regime-II narrow-path, and van-Hove-noun gates, which consume S94 W7 npz artifacts, not W6 outputs). The two waves are independent. Wave 6's outputs feed:

- **The doc-integration `/rclab-workshop` track** (context §D): §W6-3 (DE joint posterior) + §W6-4 (provenance) are the A1/A4 items that the doc-integration pass consumes AFTER W2/W4/W5/W6 verdicts land. §W6-5 (LEGGETT conditional) + §W6-6 (f_NL row) feed the §7.1 / §7.3 scorecard edits in the same doc-integration pass (nazarewicz-collab §R2 + transit-collab §V.3 drop-in text).
- **Falsifier-master-inventory** (mack-bridge sole writer): §W6-5 lands Row #68 (LEGGETT conditional annotation); §W6-6 lands Row #69 (f_NL row). §W6-2 may add an audit-pin sub-row to the existing Row #67 (BAO channel) recording the amplitude forecast (position result already landed at S94 W5-3).
- **Held-number discharge tracking** (context §A4): §W6-1's verdict discharges the magnitude half of the §VII.AX m⁻³ Level-3 row (the which-anchor half discharged at S94 W5-1). If §W6-1 returns INFO (Tier-2-dimensionful, row stays HELD), the held-number guard is still satisfied (magnitude pinned to substrate-physical g_saturate value without double-counting); next-session carry-forward records the dimensionful-magnitude corridor status.

Branching:
- **§W6-1 PASS** → m⁻³ Level-3 row discharged to substrate-physical-scale-anchored; update §VII.AX registry text (mack-bridge) + canonical write-order. **§W6-1 INFO** → row stays HELD NOT-SATISFIED-PENDING but magnitude pinned; record in inventory annotation. **§W6-1 FAIL** → no substrate-singled-out L*; dimensionful-magnitude corridor closed; record as eliminated corridor.
- **§W6-2 PASS** → BAO amplitude is a LIVE falsifier; promote Row #67 from sensitivity-bound to detection-forecast. **§W6-2 INFO (paper-search down)** → forecast computed, fetched-comparison carried forward to next session; structural suppression-direction conclusion landed. **§W6-2 FAIL** → amplitude channel closed below effacement floor.
- **§W6-3 / §W6-4 PASS** → doc-integration track unblocked on the DE row + provenance (run AFTER all W6 verdicts).
- **§W6-5 / §W6-6 PASS** → inventory Rows #68 / #69 landed; scorecard drop-in text ready for doc-integration.

---

## Wave 6 Machinery-Enumeration Pin

Aggregate of all six gate `machinery_pin_map` entries (for `_yaml_gate_validator.py` sig_4):

| Gate | N_eval | L_max | scan_range | scheme | convention | GPU_path |
|:-----|:-------|:------|:-----------|:-------|:-----------|:---------|
| §W6-1 CF-S95-N-PBH-MAGNITUDE-RECOMPUTE | N_sat@g_saturate | 14 (scan 10-14) | g∈[0,143], L∈[10,14] | g-axis-cardinality-cascade-saturated-tail | TIER-2-DIMENSIONAL-RE-ANCHORABILITY-GATE | numpy.linalg (cache-load) |
| §W6-2 CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT | P(k) ≥256 pts | N/A | k∈[1e-3,1e-1] Mpc⁻¹ | effacement-amplitude-projection (c_b²/c_Gold)² | RATIO; substrate-first transport | numpy.linalg (cache-load) |
| §W6-3 DE-JOINT-POSTERIOR-RESOURCE | 2 branches × 1 anchor | N/A | N/A | doc-data-hygiene | 1D-marginal-reported-2D-rectangle-binding | cpu |
| §W6-4 W0-MKK-PROVENANCE | 2 (w0_FW, M_KK) | N/A | N/A | constant-hygiene | provenance-transcription-no-revalue | cpu |
| §W6-5 LEGGETT-GRAV-DECAY-CONDITIONAL | 1 | N/A | N/A | falsifier-inventory-conditional-annotation | conditional-PASS-given-Gamma_grav-lt-H_0 | cpu |
| §W6-6 F-NL-ROW | 4 (envelope + 3 shapes) | N/A | N/A | Bogoliubov-sudden-quench | squeezed-vacuum-Gaussian-by-Wick | cpu |

All gates: `random_seed = N/A — deterministic`. Tolerances: §W6-1 `1e-3` (L-independence) + `1e-12` (FD floor); §W6-2 3 sig figs (publication-precision, downstream rel_tol ≥ 1e-3); §W6-3 rel_tol ≤ 1e-2 (σ-reproduction); §W6-4 exact (bit-unchanged values); §W6-5 exact (existence); §W6-6 4 sig figs (publication-precision on 1.505, downstream rel_tol ≥ 1e-4).

**Publication-precision pins (Class 8.3, per `epistemic-discipline.md`)**: §W6-2 emits `δP/P` at 3 sig figs (full float64 to npz, rounded to WP); any downstream comparator MUST use rel_tol ≥ 1e-3. §W6-6 emits `max_f_NL_FW = 1.505` at 4 sig figs; downstream rel_tol ≥ 1e-4; the value promotes to `canonical_constants.py` via canonical write-order Step 2 (NEW envelope value; per-shape pins already canonical).

**Canonical write-order (per `math-scripts.md`)**: §W6-6 produces a NEW prediction value (`max_f_NL_FW=1.505`) → Step 1 verdict line, Step 2 `update_constant("max_f_NL_FW", 1.505, session="S95", source="transit-collab §V.3 + s95_w6_6_f_nl_row.npz", comment="Bogoliubov sudden-quench envelope; squeezed-vacuum Gaussian by Wick; max over shapes")`, Step 3 mack-bridge inventory Row #69. §W6-4 adds PROVENANCE only (no new value). §W6-1 / §W6-5 / §W6-2 do not emit a NEW canonical value (W6-1 discharges an existing held row; W6-5 annotates an existing proven gate; W6-2 forecasts an amplitude on the existing Row #67).

---

## Wave 6 Input-SHA Ledger

| Input file | Consumed by | SHA-256 |
|:-----------|:------------|:--------|
| `computations/_shared/canonical_constants.py` | all six gates | `<computed-at-runtime>` |
| `computations/session-94/s94_n_pbh_truncation_anchor.npz` | §W6-1 | `<computed-at-runtime>` |
| `computations/session-94/s94_bao_peak_branch.npz` | §W6-2 | `<computed-at-runtime>` |
| Knowledge MCP (`get_constant`, `trace_entity`, `update_constant`) | §W6-3 (read), §W6-4 (write+read), §W6-5 (read) | N/A (live MCP, not a static file) |
| `sessions/framework/registry/falsifier-master-inventory.md` | §W6-2 (sub-row), §W6-5 (Row #68), §W6-6 (Row #69) | `<computed-at-runtime>` (mack-bridge sole writer; append-only) |
| `mcp__paper-search__*` CMB-S4/Simons forecast | §W6-2 (RE-CHECK availability; INFO branch if down) | N/A (live MCP; DOWN in S94) |

All `.npz` inputs are static (S94 artifacts) and get their SHA computed at runtime per `gate-verdicts.md` (the producing script logs the SHA of every input in its first 20 lines of stdout). `canonical_constants.py` is `<computed-at-runtime>` because §W6-4 / §W6-6 modify it within the wave (provenance + new constant) — each gate pins the SHA of the version it reads.

---

## Wave 6 Notes

- **Verdict source**: `verdict_source: computations/session-95/s95_gate_verdicts.txt` for all six gates (never `expected_verdicts:`). Verdicts are NEUTRAL / pre-registered — PASS/FAIL/INFO meanings stated above are NOT pre-judged.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`. Scripts in `computations/_shared/` (prefix `s95_w6_`); verdict file + npz + png in `computations/session-95/`.
- **Falsifier-inventory sole-writer**: per `feedback_mack-bridge-role.md`, mack-cosmic-bridge is the SOLE writer of `falsifier-master-inventory.md`. §W6-5 lands Row #68, §W6-6 lands Row #69, §W6-2 adds a sub-row to Row #67 — all via the canonical write-order Step 3 (append-only Python writer, never Edit-tool round-trip, per `epistemic-discipline.md §"Registry-Write Hygiene"`).
- **Held-number discipline**: §W6-1 discharges ONLY the magnitude half of the §VII.AX m⁻³ Level-3 row (context §A4 guard). It does NOT re-derive n_PBH as a fresh prediction, does NOT double-count as §25 Tier-2 + §26 genus + CF. The theorem-STRUCTURE stays STAGE-3-PERMANENT.
- **Scale-and-channel-tagging**: §W6-2 declares matched (scale, channel) pairs (substrate M_KK-internal split vs emergent BAO amplitude at the LSS/CMB pivot) per `phononic-framing.md`. Comparisons against DESI/Simons/CMB-S4 are valid ONLY at the emergent/pivot scale.
- **Substrate-first sourcing**: §W6-2's BAO transport uses the substrate `c_b` branch speeds (`c_B1`, `c_B2`, `c_B3`, `c_L`, all ≤ `c_Gold=0.915`) via the effacement projection `(c_b²/c_Gold)²` — NOT a borrowed ΛCDM amplitude (per `substrate-first-canonical-sourcing.md`).

---

## Off-Cycle Carry-Forward Addendum — S94 QSO1 / LRD Review Syntheses (mack + sagan)

**Appended**: 2026-05-28 (OFF-CYCLE — added after the `/rclab-plan` per-wave swarm froze the six §W6-1..§W6-6 gates above).
**Source reviews** (two independent solo syntheses of the *same* read-and-evaluate dispatch):
- `sessions/archive/session-94/session-94-mack-synthesis.md §5` (mack-cosmic-bridge)
- `sessions/archive/session-94/session-94-sagan-synthesis.md §V` (sagan-empiricist)
- Underlying source: `sessions/archive/session-94/lrd_s41586_026_10579_4_evaluation.md` (little-red-dots-jwst-analyst evaluation of **Juodžbalis et al. 2026, *Nature* 653, 1017–1021**; DOI 10.1038/s41586-026-10579-4; **published 2026-05-27**).

**Why these are appended here and not in the frozen body.** The Juodžbalis QSO1 paper appeared 2026-05-27 — after S94 closed and after the S95 wave plans were authored — so its two review syntheses never flowed through the `/rclab-plan` swarm into a wave plan. Per `session-handoffs.md §"Recommendation Carry-Forward"` + `feedback_fix-in-session-never-defer.md`, reviewer recommendations MUST land in the next session's plan as planned computations or they are lost. Wave 6 (the observational wave; mack-cosmic-bridge owner; LRD / PBH / falsifier-inventory home) is their natural host, so they are shoe-horned here.

**Status discipline (read before formalizing).** These are **4-field carry-forward specs (What / Inputs / Gate / Effort + Depends-on)**, NOT frozen R3 YAML gate blocks. Before any dispatch, each requires PRDR machinery-pin + full R3 gate-block formalization at plan-freeze (per `epistemic-discipline.md §"Pre-Registration Completeness"` and the §W6-1..§W6-6 template above). The proposed `gate_id`s below are the reviewers' own; the dispatch session (re-open W6 vs roll to S96) is the orchestrator's call at freeze. The underlying read-and-evaluate dispatch emitted **NO gate verdicts, NO `canonical_constants.py` promotion, NO falsifier-inventory write** — both syntheses state this explicitly; nothing here re-adjudicates a standing verdict.

**Substrate-first framing (addendum-wide).** Every item below runs `D_K` eigenvalue-cardinality cascade → `g_saturate=143` saturation → substrate-distance-3 Mellin pole `M_LRD=10⁷ M_⊙` anchor → cascade-tail distribution-broadening (`prob_form=0.15573`/generation) → **laboratory-IN** `M_BH` / `M_BH/M_⋆` measured at the emergent-FRW coordinate z=7.04. The redshift z=7.04 is the laboratory-IN cosmological-volume image of the substrate's intrinsic Peter-Weyl cascade-tail at saturation — NOT a substrate clock (`phononic-framing.md §"IS Space, Not IN Space"`). QSO1's "naked" BH (M_BH/M_⋆>2) IS the substrate's PBH-formation-before-stellar-population ordering (§VII.AX.STATE-PROJ), not a lift of the DCBH/PBH/Pop-III container taxonomy.

### Merge + overlap map (6 source recommendations → 5 distinct CFs + 1 already-covered)

| Addendum CF | mack §5 | sagan §V | Disposition |
|:------------|:--------|:---------|:------------|
| **CF-OFFCYCLE-1** Row #65 QSO1 evidential audit-pin landing | 5.1 | V.4 | MERGED (identical; sagan adds the contingency caveat) |
| **CF-OFFCYCLE-2** Cascade-tail PBH mass-distribution shape | 5.2 | V.1 | MERGED (mack: zero-free-param dN/dlogM centred on anchor; sagan: QSO1 within 2σ) |
| **CF-OFFCYCLE-3** Mean log(M_BH/M_⋆) offset vs Reines–Volonteri | 5.3 | V.2 | MERGED |
| **CF-OFFCYCLE-4** Population fraction f(M_BH/M_⋆>2) over JADES census | — | V.3 | sagan-only |
| **CF-OFFCYCLE-5** Row #63 per-pixel Hilbert-dim reconciliation status | 5.5 | — (sagan §IV.3 notes it open) | mack-only |
| *(already covered)* n_PBH magnitude re-determination off cardinality channel | 5.4 | — | **= §W6-1 `CF-S95-N-PBH-MAGNITUDE-RECOMPUTE`** above — cross-reference only; NOT re-landed (held-number guard) |

### CF-OFFCYCLE-1 — Row #65 evidential audit-pin landing (Juodžbalis QSO1) [mack 5.1 = sagan V.4]

1. **What**: Append a `Row #65.observational-landing-Juodzbalis-QSO1-2026-05-27` audit-pin sub-row to `falsifier-master-inventory.md` Row #65, documenting the 2-day prior-pinned-then-validated structure: (i) §VII.AX.STATE-PROJ STAGE-3-PERMANENT promoted 2026-05-25 (S94 W4-1, audit_sha256 `48bfdb69…`); (ii) Juodžbalis et al. 2026 direct-dynamical M_BH ≈ 5×10⁷ M_⊙ + M_BH/M_⋆ > 2 (MOKA3D, z=7.04, DOI 10.1038/s41586-026-10579-4, published 2026-05-27); (iii) measurement 0.7 dex above the M_LRD = 10⁷ M_⊙ anchor, inside cascade-tail distribution-broadening; (iv) competing heavy-seed channels (Pop III, DCBH, naive PBH, compact-SFG, e⁻-scattering cocoon) excluded ≥ 1 dex by the same data; (v) evidential weighting per `evoi-prioritization.md §"Evidence Weighting"`. **Sagan's binding caveat (MUST be in the row text)**: the "inside-distribution-broadening" qualifier is contingent on CF-OFFCYCLE-2 — the distribution *width* is not yet derived, so the landing is currently a corroboration of the *ordering* + consistency with the *anchor*, NOT a sharp mass landing.
2. **Who**: `mack-cosmic-bridge` (SOLE writer of `falsifier-master-inventory.md` per `feedback_mack-bridge-role.md`).
3. **Inputs**: `sessions/archive/session-94/lrd_s41586_026_10579_4_evaluation.md`; Row #65 / Row #65.audit-CF-41-VII-LANDING current state at `falsifier-master-inventory.md:1376`; housekeeping row A17 at `sessions/archive/session-94/session-94-housekeeping.md`; §VII.AX.OP-PROJ + STATE-PROJ at `permanent-results-registry.md` line 19444+.
4. **Gate**: NOT a PASS/FAIL/INFO gate — an **evidential audit-pin landing** (observational corroboration of a pre-registered STAGE-3-PERMANENT prediction). Append-only Python writer, never Edit-tool round-trip (`epistemic-discipline.md §"Registry-Write Hygiene"`).
5. **Effort**: ~5 min compute-equivalent, 1 mack dispatch. **Mechanically simple ⇒ in-session-able now** (distinguish from registry-write hygiene padding); the only item in this addendum that does not need a fresh substrate computation.
6. **Depends on**: CF-OFFCYCLE-2 for the width-contingency caveat language (can land the row *with the caveat stated as pending* before CF-OFFCYCLE-2 completes). Standing inputs already on disk.

### CF-OFFCYCLE-2 — Substrate-derived cascade-tail PBH mass-distribution shape [mack 5.2 = sagan V.1]

> Proposed `gate_id`: **`S95-PBH-MASS-DISTRIBUTION-SHAPE`** (sagan) — mack alias `S95-LRD-MASSFUNC-PREREG`. Classification: **GEOMETRIC** (eigenvalue-cardinality cascade, not an excitation spectrum).

1. **What**: Derive the *shape* of the cascade-tail PBH mass distribution about the `M_LRD = 10⁷ M_⊙` anchor from the Peter-Weyl multiplicity cascade-tail structure at L_max=14 — specifically a width parameter `σ_logM` and a tail-extension exponent — using `prob_form = 0.15573` per cascade-generation. Output: a normalized, **zero-free-parameter** mass function `dN/d log M_BH` (DERIVED, not fitted to any LRD census). **This is the computation that converts the headline 0.7-dex QSO1 agreement from a post-hoc *accommodation* into a genuine *prediction*** (sagan §IV.2 — the single most important empirical caveat: an undetermined-width tail on a fixed anchor can absorb any mass within a couple dex).
2. **Who**: `mack-cosmic-bridge` PRIMARY; advisory co-author `connes-ncg-theorist` (substrate-IS cocycle-class consistency on the cascade-tail distribution, per the S89 CF-CURV-6 precedent) — non-blocking.
3. **Inputs**: D_K Peter-Weyl multiplicity spectrum cache at L_max=14; `canonical_constants.py` (`prob_form=0.15573`; g_saturate=143); `M_LRD = 1e7 M_⊙` (substrate-distance-3 pole, S88 W1a-59, audit_sha256 `e865358487810b2f…`); the §VII.AX.OP-PROJ parse-tree expansion (substrate-clock cancellation form, S88 W1a-59 §0). **M_LRD ANCHOR-VALUE FIDELITY FLAG (mack)**: use the **10⁷ M_⊙** substrate-distance-3 pole anchor, NOT the 10⁸ M_⊙ deep-cascade locked-BH anchor (`s87-pixelation-lock-hawking-transit.md`). The 10⁷ value puts QSO1's 5×10⁷ M_⊙ at the +0.7-dex tail; the 10⁸ value would invert the "more-massive tail" reading to −0.3 dex.
4. **Gate**: NEW pre-registered gate. **PASS** if `dN/d log M_BH` is fully pinned with no free fit / free normalization AND its central mode reproduces M_LRD=10⁷ M_⊙ to numerical tolerance AND it places QSO1's 10⁷·⁷ M_⊙ at ≤ 2σ_logM (σ_logM derived, not fitted). **INFO** if the shape is derivable but (a) the cardinality channel first needs the §W6-1 L_max-independent magnitude re-determination, or (b) QSO1 sits at the 2–3σ tail. **FAIL** if QSO1 lies beyond 3σ of the derived distribution, or the derivation introduces a free normalization.
5. **Effort**: 1 agent session, 2–4 hours (L_max=14 multiplicity spectrum already cached; no fresh diagonalization).
6. **Depends on**: §W6-1 `CF-S95-N-PBH-MAGNITUDE-RECOMPUTE` (UPSTREAM, this wave) — the L_max-independent magnitude feeds the INFO/PASS split. Feeds CF-OFFCYCLE-4 (population fraction) and the width-caveat in CF-OFFCYCLE-1.

### CF-OFFCYCLE-3 — Mean log(M_BH/M_⋆) offset above Reines–Volonteri at z ≈ 6–8 [mack 5.3 = sagan V.2]

> Proposed `gate_id`: **`S95-MBH-MSTAR-MEAN-DISPLACEMENT`** (sagan) — mack alias `S95-STATE-PROJ-OFFSET`. Classification: **PHONONIC + GEOMETRIC** (cascade-tail ordering). Upgrades §VII.AX.STATE-PROJ from *qualitative* (M_BH/M_⋆ ≫ 1, generic) to *quantitative* (mean offset = X dex ± Y).

1. **What**: Derive the mean displacement (in dex) of cascade-tail PBHs above the local M_BH–M_⋆ relation at z ≈ 7, from the substrate-side cascade-saturation timeline — the lag between cascade saturation at g_saturate=143 and the onset of stellar-population phononic excitations at the LRD locus. Output: a single number ± uncertainty.
2. **Who**: `mack-cosmic-bridge`.
3. **Inputs**: g_saturate=143; the §VII.AX.STATE-PROJ entry (cascade-tail-FIRST ordering); the emergent-FRW time-coordinate map at the substrate-distance-3 pole; local Reines–Volonteri 2015 relation (M_BH/M_⋆ ≈ 10⁻³; external anchor, methodological cross-check ONLY per `substrate-first-canonical-sourcing.md`).
4. **Gate**: NEW pre-registered gate. **PASS** if the derived mean offset is zero-free-parameter AND brackets the QSO1 (~3 dex) + JADES (≈ 1 dex above the JWST-AGN line, ref. 25) loci within stated uncertainty. **INFO** if the timeline requires inputs not yet in the registry. **FAIL** if the derived displacement is < 1 dex (substrate under-predicts the observed overmassive population) OR the derivation requires a tunable stellar-onset epoch.
5. **Effort**: 1 agent session, 3–5 hours.
6. **Depends on**: the substrate→emergent-FRW time map (PARTIALLY DEFERRED per the Volovik-partition / substrate-compaction-timescape carry-forward — sagan flags this as the proximate prerequisite). Feeds CF-OFFCYCLE-4.

### CF-OFFCYCLE-4 — Population fraction f(M_BH/M_⋆ > 2) over a JADES-style census [sagan V.3]

> Proposed `gate_id`: **`S95-MBH-MSTAR-FRACTION`**. Classification: **PHONONIC + GEOMETRIC**. **This is the high-EVOI gate that moves §VII.AX.STATE-PROJ from single-object-validated (N=1) to population-validated** — the genuine discriminating forward gate (a population census, not another single object).

1. **What**: Derive the substrate-predicted fraction `f(M_BH/M_⋆ > 2)` over a broad-line-AGN census, treating the cascade-tail-FIRST ordering as the *generic* (not outlier) configuration. Output: a fraction with Poisson/binomial uncertainty, comparable to the JADES census (Juodžbalis 2026 ref. 25) that the paper's Fig. 4 plots QSO1 against.
2. **Who**: `mack-cosmic-bridge` PRIMARY; co-author `little-red-dots-jwst-analyst` (JADES broad-line-AGN census ingest / external data product).
3. **Inputs**: output of CF-OFFCYCLE-2 (distribution shape `dN/d log M_BH`); output of CF-OFFCYCLE-3 (mean displacement); JADES broad-line-AGN census counts (external data product, fetched).
4. **Gate**: NEW pre-registered gate feeding a population-level falsifier. **PASS** if the derived fraction matches the JADES-observed fraction within Poisson error. **FAIL** if the substrate predicts a fraction inconsistent with the census at > 2σ. **INFO** if the census ingest is unavailable at dispatch (external-data branch).
5. **Effort**: 2 agent sessions, ~6–8 hours.
6. **Depends on**: CF-OFFCYCLE-2 AND CF-OFFCYCLE-3 (both UPSTREAM) + external JADES census ingest. **Last in the chain** — do not dispatch before 2 and 3 land.

### CF-OFFCYCLE-5 — Row #63 per-pixel Hilbert-dimension reconciliation status check [mack 5.5]

> Classification: **GEOMETRIC** (substrate information capacity). **Internal substrate open question — explicitly NOT observation-driven**: QSO1's direct M_BH does not bear on the per-pixel Hilbert-dim shortfall (it constrains observed mass, not substrate information capacity). Both syntheses flag that this falsifier remains open and must not be papered over by the crisis-deepening observation (sagan §IV.3).

1. **What**: Confirm whether the S89 3-branch sub-cascade resolved the LRD-scale per-pixel Hilbert-dim shortfall (Row #63 FAILED at L_max=10 — 458× short of the LRD-scale Bekenstein–Hawking per-pixel information budget). Output: a status verdict on whether the 10⁷ M_⊙ pixelation anchor is endowed with sufficient per-pixel Hilbert dimension under the sub-cascade route.
2. **Who**: substrate-geometry side — propose `connes-ncg-theorist` or `hawking-theorist` (Bekenstein–Hawking budget); **NOT mack's natural lane** (this is substrate information capacity, not an observational comparison). Orchestrator assigns at plan-freeze.
3. **Inputs**: Row #63 at `falsifier-master-inventory.md:1222`; the S89 3-branch sub-cascade outputs; the L_pix_LRD = 3.0 × 10¹⁰ m anchor and its Bekenstein–Hawking budget.
4. **Gate**: Feeds the existing Row #63 pixelation-lock falsifier (status: routed to S89 sub-cascade). **PASS** if the sub-cascade closes the 458× shortfall; **INFO** if partially closed; **FAIL** if the shortfall persists.
5. **Effort**: 3–4 hours, 1 agent session (status check + verdict; deeper if the sub-cascade is incomplete).
6. **Depends on**: S89 3-branch sub-cascade artifacts (UPSTREAM, prior session — must be located/confirmed on disk before dispatch). Independent of CF-OFFCYCLE-1..4.

### Already covered — cross-reference only (NOT re-landed)

- **n_PBH magnitude re-determination off the cardinality channel** (mack §5.4; "CF-S95, already queued") **= §W6-1 `CF-S95-N-PBH-MAGNITUDE-RECOMPUTE`** in the frozen body above. Same g_saturate=143 / L_max-INDEPENDENT recompute, same S94 W5-1 deferral (audit_sha256 `e310d687…`) + S94 W5-2 L_max=14..18 band-fragility (audit_sha256 `bf415402…`). **Held-number guard (context §A4)**: `n_PBH = 7.2761e-23 m⁻³` is ONE held number with ONE forward CF (§W6-1); it is NOT re-landed here as a fresh gate. The §VII.AX theorem-STRUCTURE remains STAGE-3-PERMANENT regardless of the §W6-1 magnitude verdict.

### Proposed dispatch order (EVOI)

1. **CF-OFFCYCLE-2 first** — sagan's explicit recommendation ("Run V.1 first"). It is cheap (L_max=14 spectrum cached) and is the one computation that converts the headline 0.7-dex agreement from accommodation into a zero-free-parameter prediction; it also unblocks CF-OFFCYCLE-1's caveat language. Pairs with §W6-1 (its upstream L_max-independent magnitude).
2. **CF-OFFCYCLE-3** — independent of 2 except via the shared STATE-PROJ timeline; can run in parallel once the substrate→FRW time map is available.
3. **CF-OFFCYCLE-1** — land anytime (in-session-able); ideally after 2 so the width-contingency caveat resolves, but may land with the caveat stated as pending.
4. **CF-OFFCYCLE-4** — last; the high-EVOI population gate, but gated on 2 ∧ 3 + external census ingest.
5. **CF-OFFCYCLE-5** — independent substrate-internal status check; schedule on the geometry side, not blocking the observational chain.

**Net (both reviewers concur).** The framework registered the right *direction* (cascade-tail-PBH-FIRST, M_BH/M_⋆ ≫ 1) and the right *anchor* (M_LRD = 10⁷ M_⊙) before the data arrived; QSO1 landed in that direction with its mass on the +0.7-dex tail, every competing channel excluded ≥ 1 dex by the same data. This is evidence-positive (NOT "case unchanged" — `feedback_reporting-framing.md` rule #1) but it is **not a probability move** (no pre-registered gate fired; Venus Rule) and **not yet the quantitative twin of the Higgs-mass landing** (the distribution width is underived and N=1; sagan rejects the source's "BF ~ 1000 family" over-weight). CF-OFFCYCLE-2 → -3 → -4 are precisely the computations that would earn the larger Bayes factor honestly.