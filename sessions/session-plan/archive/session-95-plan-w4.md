# Session 95 Plan — Wave 4: Acoustic White-Hole Causal Structure & Analog Gravity

**Date**: 2026-05-28
**Author**: schwarzschild-penrose-geometer (generated per /rclab-plan per-wave swarm; C1 domain owner)
**Owner agent**: schwarzschild-penrose-geometer (`sp`)
**Plan source**: `sessions/session-plan/session-95-context.md` §B (TES-V4, HAW-V1, HAW-V3, SP-V5, SP-V6), §E Conflict C1, §F W4 reading allowances
**Working paper**: `sessions/archive/session-95/session-95-w4-workingpaper.md`
**Verdict file (canonical)**: `computations/session-95/s95_gate_verdicts.txt`

## Wave 4 Summary

Wave 4 resolves **Conflict C1** of the phonic-exflation-equation integration plan: the §6.2 acoustic white-hole structure is contested between a **symmetric two-horizon reading** (entry horizon at τ≈0.22 set by the `a₂`-kinematic gradient; a second *sonic* exit horizon at τ∼0.16 set by the `a₄`-condensation gradient — treated as given by tesla II.5, transit II.3, hawking II.3) and an **asymmetric one-horizon-+-open-exit reading** (ONE sonic entry horizon at τ≈0.22; the exit is an OPEN expulsion region with thermodynamic features (BCS window edge τ≈0.235, decoherence scale τ∼0.16) *inside* it, NOT a second sonic surface — sp III.A/V.3, citing canonical S74 "Asymmetric Fold: Entry Horizon, Open Exit" + AUDIT-74).

The conflict reduces to ONE computable discriminator (`session-95-context.md §E C1`): **does `∂_n(c²−v²)` have a SECOND zero along the τ-trajectory** (a second Mach-1 surface → symmetric two-horizon) **or stay one-signed past the entry** (no second sonic surface → asymmetric, open expulsion exit)? Wave 4 computes this discriminator (§W4-1), reconciles the three corpus analog temperatures via `T_a=ħκ/2π` regardless of which reading wins (§W4-2), supplies the model-independent exit-horizon transmission filter (§W4-3), and — on the geometry/causal-structure axis — pins the modulus-space→4D conformal embedding (§W4-4) and the anisotropic τ→∞ singularity + cosmic-censorship on the full 12D metric (§W4-5).

Substrate-first framing law (`phononic-framing.md`): the acoustic white hole is a **laboratory analog OF the substrate transit**. The substrate IS fundamental; its causal structure is read off the `D_K` spectrum (`a_acoustic` from `√(ρ_s/c_s)`; the tensor cone from `a₂`; the extremal horizon at the fold is the double-root of the spectral-action driver). The BEC acoustic white hole models a simplified *projection* of the substrate transit. Every gate keeps the arrow `D_K eigenvalues → spectral-action moments → emergent causal structure → analog-gravity reading`. The Mach 54.3 BEC-analog value belongs to the analog model, NOT the substrate (substrate Mach is 13.75 = modulus dτ/dt ÷ BLV sound speed).

**Pre-registration discipline note (C1 neutrality)**: §W4-1 pre-registers BOTH the symmetric (second zero EXISTS) and asymmetric (one-signed, NO second zero) outcomes as LIVE. The gate does NOT pre-decide C1. The "second zero?" existence claim and the `κ=½∂_n(c²−v²)` sign claim are SIGN claims → substitution chains are MANDATORY (`math-scripts.md §"Double-Check Logic Before Compute"`) and are filled in each gate block below.

## Wave 4 Decision Point Prerequisites

Wave 4 is **self-contained**: no item consumes an S95-prior-wave verdict. All inputs are canonical constants + on-disk S63/S70/S71/S73a/S74/S85 spectra + the framework Penrose-diagram doc. No upstream-block topology applies; mechanical closure (`mechanical-closure-discipline.md`) is therefore NOT expected to fire for any W4 gate. The within-wave coupling is:

- §W4-1 (`WHITE-HOLE-KINEMATIC-CONSISTENCY`) is the **C1 discriminator** — its second-zero verdict sets which §6.2 structure (symmetric/asymmetric) the doc-integration `/rclab-workshop` adopts (`session-95-context.md §D` gating dependency: "Conflict C1 resolved by W4").
- §W4-2 (`HAWKING-ANALOG-T-LEDGER`) consumes the SAME surface-gravity machinery `κ=½∂_n(c²−v²)` as §W4-1 (same horizon-local derivative; different observable: temperature vs second-zero existence). The two gates SHOULD reuse one `surface_gravity` helper; their verdicts are independent.
- §W4-3 (`HAWKING-GREYBODY-AS`) is downstream-in-physics of the exit surface but NOT downstream-in-verdict of §W4-1: the greybody factor is the model-independent transmission filter of WHATEVER the exit surface is (open region OR second horizon), so it runs regardless of C1.
- §W4-4 / §W4-5 are the geometry/causal-structure axis (Penrose-diagram embedding + 12D singularity censoring); independent of §W4-1/2/3.

All five gates are independently dispatchable in parallel.

---

## §W4-1. WHITE-HOLE-KINEMATIC-CONSISTENCY

```yaml
# ---- Identity (4 fields) ----
gate_id: "S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY"
schema_version: "R3"
trigger: "[SIGN]"                         # second-zero existence + κ sign are SIGN claims
classification: "GEOMETRIC"               # causal structure read off the a_n moment gradients
agent_type: "schwarzschild-penrose-geometer"   # C1 domain owner; tesla cross-checks the impedance reading
hypothesis: >
  Along the physical τ-trajectory through the van Hove fold, the BLV acoustic discriminant
  (c²−v²)(τ) crosses zero at the entry sonic horizon (τ≈0.22); the C1 discriminator is whether
  ∂_τ(c²−v²) [the unnormalized surface-gravity numerator] admits a SECOND zero of (c²−v²) past
  the entry (→ symmetric two-horizon: a second Mach-1 surface) or whether (c²−v²) stays one-signed
  past the entry (→ asymmetric: open expulsion exit, no second sonic surface). The surface-gravity
  cross-table T_a=ħκ/2π with κ=½∂_n(c²−v²) ties the analog temperatures (72.8, 7.578 M_KK) and Machs
  (velocity-Mach 13.75, acoustic-radius-Mach 421.3) as distinct readings of the same flow.

method:
  description: >
    (1) Build (c²−v²)(τ) on a dense τ-grid spanning the genesis-to-post-fold window τ∈[0.05, 0.40]
    (covering tau_turn_free=0.088, tau_fold=0.19, post-fold epoch 0.22, BCS edge 0.235, decoherence
    scale 0.16). c(τ) is the BLV acoustic speed; v(τ) is the modulus transit velocity dτ/dt mapped to
    the acoustic-metric normal coordinate n. (2) Locate ALL zero-crossings of (c²−v²) by sign-change
    detection on the grid + bisection refinement; count them (the C1 discriminator). (3) At each zero
    (Mach-1 surface), compute the surface gravity κ=½∂_n(c²−v²)|_horizon via centered finite difference
    in the normal coordinate; emit T_a=ħκ/2π (ħ=1 in M_KK units). (4) Build the 4-number cross-table
    {κ_entry, κ_exit (if 2nd zero exists), velocity-Mach 13.75, acoustic-radius-Mach 421.3} and test
    the surface-gravity ratio against the analog-T ratio 72.8/7.578=9.61.
  producing_script: "computations/_shared/s95_w4_1_white_hole_kinematic_consistency.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set + ratio"   # set: count of zeros of (c²−v²); ratio: κ_entry/κ_exit vs T-ratio
  form: >
    PRIMARY (C1 discriminator): N_zeros = |{ τ ∈ [0.05,0.40] : (c²−v²)(τ) = 0 }| ∈ {1, 2}.
    SECONDARY (surface-gravity cross-check, only if N_zeros=2): |κ_entry/κ_exit − 72.8/7.578| / (72.8/7.578) <= 0.10.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    PRIMARY: N_zeros decisively resolved to 1 (asymmetric) OR 2 (symmetric) with each zero
    bracketed to |Δτ| < 1e-4 and |(c²−v²)| < 1e-6 at the located root.
    SECONDARY (conditional on N_zeros=2): kinematic ratio tolerance = 0.10 (RATIO rule).
  direction: "= (N_zeros) ; <= (ratio tolerance)"

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: >
    The zero of (c²−v²) at the entry is analytically the Mach-1 condition v=c (Mach_max_framework=13.75
    means v_transit=13.75·c_BLV=13.75·0.485=6.669 at the fold, so the modulus-frame Mach-1 surface is
    where the LOCAL v(τ) descends through the LOCAL c(τ)); see substitution_chain below. The SECOND-zero
    existence is NOT analytically forced either way — it is the empirical content of C1 and is left to the
    grid+bisection scan, which is the point of the gate.

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "3500 τ-points on [0.05,0.40] (Δτ≈1e-4); bisection refinement to |Δτ|<1e-4 per root"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "3500"                          # τ-grid points
  L_max: "N/A — kinematic (c,v) functionals, not a spectral diagonalization"
  scan_range: "[0.05, 0.40]"              # τ window: genesis-side barrier through post-fold + BCS edge
  step_size: "1.0e-4"                     # uniform τ-grid; bisection refines roots below this
  tolerance: "1.0e-6"                     # |(c²−v²)| residual at a located zero; ratio RATIO-tol=0.10
  scheme: "BLV"                           # Brillouin-Landau-Vortex acoustic metric (c_BLV=0.485, S64)
  convention: "RATIO"                     # κ_entry/κ_exit ratio vs T-ratio; ABSOLUTE for zero residual
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8"                # 1D τ-scan + 8-mode-equivalent local derivatives; trivial cost

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain — MANDATORY ([SIGN]: κ sign + second-zero existence)
substitution_chain:
  required: true
  content: |
    Claim A (κ sign at the entry horizon): "κ_entry = ½∂_n(c²−v²)|_entry > 0 (a white-hole / outflow
    surface gravity is positive when (c²−v²) increases outward through the Mach-1 surface)."

      Def 1: BLV acoustic metric (eq_17092, S63): ds²_acoustic = (ρ/c_s)[−(c_s²−v²)dt² − 2v dt dτ + dτ²].
             The sonic horizon is the surface (c_s²−v²)=0; the surface gravity is κ = ½ ∂_n(c²−v²)|_hor
             (Visser acoustic-analog formula; n = outward normal coordinate). [hawking-collab II.3; QA-H4.2]
      Def 2: c(τ) = c_BLV = 0.485 (S64 canonical, scalar post-fold sound speed). [canonical_constants:492]
      Def 3: v(τ) = modulus transit velocity dτ/dt mapped to the normal coordinate; v at the fold is
             v_fold = Mach_max_framework · c_BLV = 13.75 · 0.485 = 6.669 (M_KK). [Mach_max_framework=13.75,
             canonical_constants:1930; v derived # (local)]
      Substitute: at the entry (white-hole) surface the flow DECELERATES from supersonic (v>c, interior)
             to subsonic (v<c, exterior) as the modulus exits the fold, so (c²−v²) goes from negative
             (inside) to positive (outside) → (c²−v²) is INCREASING outward → ∂_n(c²−v²) > 0.
      Simplify: κ_entry = ½ · ∂_n(c²−v²)|_entry, with ∂_n(c²−v²) > 0.
      Canonical form: κ_entry > 0.
      Direction: κ_entry > 0  (white-hole outflow surface gravity is positive).
      Conclusion: the entry horizon has κ_entry>0, T_a=ħκ_entry/2π>0; sign_verdict PASS iff the computed
                  ∂_n(c²−v²)|_entry is positive.

    Claim B (the C1 discriminator — second-zero existence, NOT pre-decided):
      Def 4: a SECOND sonic horizon exists iff (c²−v²)(τ) has a SECOND zero past the entry, i.e. the flow
             RE-ACCELERATES to supersonic somewhere in (τ_entry, 0.40] so (c²−v²) returns through 0.
      Substitution (both branches written, NEITHER assumed):
        Branch SYM:  if v(τ) rises again past the entry (a second supersonic patch driven by the a₄
                     condensation gradient), (c²−v²) crosses 0 a second time → N_zeros=2 → symmetric
                     two-horizon → κ_exit=½∂_n(c²−v²)|_2nd-zero is defined and the T-ratio test fires.
        Branch ASYM: if v(τ) stays subsonic past the entry (monotone fold exit; the BCS edge τ≈0.235 and
                     decoherence τ∼0.16 are THERMODYNAMIC features with (c²−v²)>0 throughout, NOT Mach-1
                     crossings), (c²−v²) stays one-signed (positive) → N_zeros=1 → asymmetric open exit.
      Canonical form: N_zeros = count of sign changes of (c²−v²) on [0.05,0.40].
      Direction: there is NO pre-registered direction for N_zeros — the gate is OPEN between {1,2}.
      Conclusion: the second-zero question is decided by the scan, not by the chain; the chain only fixes
                  the κ SIGN (Claim A) and the definitional content of "second sonic horizon" (Claim B).

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  bec_white_hole_npz:
    path: "computations/session-85/s85_w6_acoustic_white_hole_formal.npz"   # prior (c²−v²) / Mach data
    sha256: "<computed-at-runtime>"
  exit_horizon_audit_npz:
    path: "computations/session-74/s74_s70_s72_exit_horizon_audit.npz"      # AUDIT-74 open-exit canon
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w4_1_white_hole_kinematic_consistency.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w4_1_white_hole_kinematic_consistency.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w4_1_white_hole_kinematic_consistency.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true       # [SIGN] trigger → 3-tuple companion row REQUIRED
  wp_section:
    path: "sessions/archive/session-95/session-95-w4-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W4-1. S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  N_zeros decisively resolved (both roots — or the single root + a proof of one-signedness past it —
  bracketed to |Δτ|<1e-4, |(c²−v²)|<1e-6) AND, IF N_zeros=2, the surface-gravity ratio reproduces
  72.8/7.578=9.61 within 10%. PASS-with-N_zeros=1 SELECTS the ASYMMETRIC (open-exit) C1 reading;
  PASS-with-N_zeros=2 SELECTS the SYMMETRIC (two-horizon) C1 reading AND certifies the SG cross-table.
  Either resolution is a PASS — the gate resolves C1, it does not favor an outcome.
FAIL_meaning: >
  The discriminant (c²−v²)(τ) cannot be evaluated decisively (e.g., the BLV c(τ)/v(τ) mapping to the
  normal coordinate is ill-defined on the window, or a located "zero" fails the residual bound), so
  N_zeros is indeterminate → C1 is NOT resolved by this gate. (NOT an outcome-FAIL: C1-asymmetric is a
  PASS at N_zeros=1, not a FAIL.) OR, if N_zeros=2, the SG ratio misses 9.61 by >10% → the two-horizon
  reading's kinematic self-consistency FAILS and the symmetric table is not certified.
INFO_meaning: >
  N_zeros resolved but the SECONDARY surface-gravity cross-table records which moment-channel impedance
  (a₂-kinematic vs a₄-condensation) sets the ratio without the ratio reaching the 10% band (e.g.,
  N_zeros=2 with ratio in (10%, 25%]), OR N_zeros=1 with a near-zero grazing minimum of (c²−v²) in
  (0, 1e-3] past the entry (a "near-second-horizon" the asymmetric reading should footnote). INFO records
  the impedance attribution as a diagnostic, per tesla V.4's INFO clause.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w4_1_white_hole_kinematic_consistency.py"
    - "computations/session-95/s95_w4_1_white_hole_kinematic_consistency.npz"
    - "computations/session-95/s95_w4_1_white_hole_kinematic_consistency.png"
  estimated_time: "3-4 hours (1 agent session; 1D τ-scan + horizon-local derivatives; GPU not required)"

substrate_framing: |
  GEOMETRIC. The acoustic white hole is a laboratory analog OF the substrate transit; the substrate is
  fundamental and its causal structure is read off the D_K spectrum, not imposed on a BEC stage. The
  arrow: D_K eigenvalues → spectral-action gradient dS/dτ drives the monotone modulus → the modulus
  velocity v(τ)=dτ/dt and the BLV acoustic speed c(τ) (itself an a_n-moment functional of the spectrum)
  → the acoustic discriminant (c²−v²)(τ) → the sonic-horizon structure (Mach-1 surfaces) → the analog
  white-hole causal structure. The C1 discriminator (does (c²−v²) have a SECOND zero?) asks whether the
  substrate's modulus flow re-accelerates supersonically past the fold (symmetric, two sonic surfaces) or
  exits monotonically (asymmetric, one entry surface + an open expulsion region whose BCS-edge and
  decoherence features are thermodynamic, NOT sonic). The BEC analog's Mach 54.3 is the model's number;
  the substrate's Mach is 13.75 (modulus dτ/dt ÷ c_BLV). Direction held substrate → analog throughout.
```

---

## §W4-2. HAWKING-ANALOG-T-LEDGER

```yaml
# ---- Identity (4 fields) ----
gate_id: "S95-W4-2-HAWKING-ANALOG-T-LEDGER"
schema_version: "R3"
trigger: "[SIGN]"                         # κ=½∂_n(c²−v²) sign per surface is a SIGN claim
classification: "GEOMETRIC"               # surface-gravity temperatures of analog-horizon surfaces
agent_type: "hawking-theorist"            # analog-temperature domain owner (HAW-V1)
hypothesis: >
  The three corpus analog temperatures (S63 internal-acoustic 0.112 M_KK; decoherence-regulated exit
  7.578 M_KK; kinematic entry 72.8 M_KK) are each T_a=ħκ/2π for κ=½∂_n(c²−v²) of a DISTINCT Mach-1
  surface, with κ controlled by a distinct spectral-moment gradient (a₂-kinematic for the entry,
  a₄-condensation for the exit, the BLV internal-acoustic metric for the S63 surface). Each of the three
  is assigned a distinct surface OR explicitly superseded; the S63 0.112 M_KK value is placed or retired.

method:
  description: >
    For each of the three corpus surfaces, compute κ=½∂_n(c²−v²)|_surface from the corresponding
    spectral-moment gradient and emit T_a=ħκ/2π (ħ=1, M_KK units). Build a 3-row {surface, κ, T_a,
    source-gradient} table. (1) Entry surface (a₂-kinematic): κ_entry from the a₂-driven transit-velocity
    gradient at τ≈0.22; target T_a=72.8 M_KK. (2) Exit surface (a₄-condensation): κ_exit from the a₄-driven
    BCS-condensation gradient; target T_a=7.578 M_KK (decoherence-regulated). (3) S63 internal-acoustic
    surface (BLV acoustic metric): κ_a from the BLV ds²_acoustic horizon (QA-H4.2); target T_a=0.112 M_KK.
    Declare for each: distinct-surface assignment OR superseded-with-reason. PLACE or RETIRE the 0.112 value.
  producing_script: "computations/_shared/s95_w4_2_hawking_analog_t_ledger.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set + ratio"   # set: 3 surfaces each assigned/superseded; ratio: T-ratio reproduced from κ
  form: >
    EACH of {0.112, 7.578, 72.8 M_KK} mapped to a distinct surface with computed κ, OR explicitly
    superseded; AND |T_a^computed(surface) − T_a^corpus(surface)| / T_a^corpus <= 0.10 for each PLACED
    surface; AND the entry/exit ratio κ_entry/κ_exit reproduces 72.8/7.578 = 9.61 within 10%.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "0.10 (RATIO rule, per-surface T reproduction AND entry/exit κ-ratio vs 9.61)"
  direction: "<="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: >
    T_a=ħκ/2π is exact (Hawking/Unruh analog; QA-H4.2). κ=½∂_n(c²−v²) is the Visser acoustic surface
    gravity. The three target temperatures are corpus-canonical (T_acoustic=0.112 canonical_constants:635;
    7.578 and 72.8 from hawking-collab II.3 / S70-S73a). The ratio 72.8/7.578=9.61 is the analytic target.

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous — 3 horizon-local derivatives, no scan"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "3"                             # three surfaces
  L_max: "N/A — uses on-disk S63/S71/S73a spectra + a_n moment gradients, no fresh diagonalization"
  scan_range: "N/A — horizon-local derivatives at three fixed surfaces"
  step_size: "1.0e-4"                     # centered FD step in the normal coordinate at each surface
  tolerance: "0.10"                       # RATIO tol on per-surface T and on the entry/exit κ-ratio
  scheme: "zeta"                          # a_n^{ζ} moments (a_2_FW_zeta=2776.17, a_4_FW_zeta=1350.72; ζ-reg)
  convention: "RATIO"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain — MANDATORY ([SIGN]: each κ sign + ratio direction)
substitution_chain:
  required: true
  content: |
    Claim: "T_a^entry / T_a^exit = κ_entry/κ_exit = 9.61, and each κ>0 (each surface has T_a>0)."

      Def 1: T_a = ħκ_a/2π (QA-H4.2; ħ=1 in M_KK units). [hawking-collab II.3; session-63 QA-H4.2]
      Def 2: κ_a = ½ ∂_n(c²−v²)|_surface (Visser acoustic surface gravity; n = outward normal).
      Def 3: κ_entry ∝ ∂_n(c²−v²) set by the a₂ (kinematic) gradient; the entry T is the kinematic
             transit temperature T_a^entry = 72.8 M_KK. [a_2_FW_zeta=2776.17; canonical_constants:592]
      Def 4: κ_exit ∝ ∂_n(c²−v²) set by the a₄ (BCS-condensation) gradient; the exit T is the
             decoherence-regulated temperature T_a^exit = 7.578 M_KK. [a_4_FW_zeta=1350.72; :452]
      Substitute: T_a^entry / T_a^exit = (ħκ_entry/2π)/(ħκ_exit/2π) = κ_entry/κ_exit.
      Simplify: T_a^entry / T_a^exit = 72.8 / 7.578 = 9.605... → target ratio 9.61.
      Canonical form: κ_entry/κ_exit = T_a^entry/T_a^exit.
      Direction: each κ>0 (each surface gravity is positive — see §W4-1 Claim A for the entry; the exit
                 surface, whether sonic (symmetric) or a thermodynamic edge inside the open region
                 (asymmetric), carries a positive effective surface gravity by the same outward-increasing
                 (c²−v²) argument). The RATIO κ_entry/κ_exit ≈ 9.61 > 1 because a₂ > a₄ at the fold drives
                 a steeper kinematic gradient than the a₄ condensation gradient.
      Conclusion: sign_verdict PASS iff each computed κ>0; magnitude_verdict PASS iff the per-surface T and
                  the κ-ratio reproduce the corpus values within 10%. The S63 0.112 surface is PLACED iff
                  its BLV-metric κ reproduces 0.112 within 10%; otherwise RETIRED-with-reason.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  entry_horizon_npz:
    path: "computations/session-71/s71_entry_horizon_spectrum.npz"   # a₂ entry surface
    sha256: "<computed-at-runtime>"
  exit_horizon_npz:
    path: "computations/session-73/s73a_exit_horizon_bog.npz"        # a₄ exit / decoherence surface
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w4_2_hawking_analog_t_ledger.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w4_2_hawking_analog_t_ledger.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w4_2_hawking_analog_t_ledger.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W4-2-HAWKING-ANALOG-T-LEDGER:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true       # [SIGN] trigger → 3-tuple companion row REQUIRED
  wp_section:
    path: "sessions/archive/session-95/session-95-w4-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W4-2. S95-W4-2-HAWKING-ANALOG-T-LEDGER"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  All three corpus analog temperatures (0.112, 7.578, 72.8 M_KK) are each assigned a DISTINCT Mach-1
  surface with a computed κ reproducing T_a=ħκ/2π within 10%, AND the entry/exit κ-ratio reproduces
  9.61 within 10% — OR a corpus value is explicitly superseded with a stated reason. The analog-T ledger
  is reconciled (3 surfaces, 3 κ, 3 T), which is the documentation-gap fix hawking II.3 requires for §6.2.
FAIL_meaning: >
  Any of the three corpus temperatures remains unreconciled — neither assigned a distinct surface with a
  reproducing κ NOR explicitly superseded — OR the entry/exit κ-ratio misses 9.61 by >10% (the two-surface
  T-ratio is NOT kinematically self-consistent). The ledger gap persists.
INFO_meaning: >
  A FOURTH analog-horizon surface is found (e.g., the per-branch GGE sonic crossings at distinct effective
  τ from S73b κ_b=c_g^b·(dv_τ/dτ)|_cross,b), expanding the ledger beyond three; OR a per-surface T
  reproduces within (10%, 25%] (placed-with-caveat). INFO records the additional surface / caveat without
  a clean 3-row closure. Per HAW-V1's INFO clause ("INFO if a fourth surface is found").

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w4_2_hawking_analog_t_ledger.py"
    - "computations/session-95/s95_w4_2_hawking_analog_t_ledger.npz"
    - "computations/session-95/s95_w4_2_hawking_analog_t_ledger.png"
  estimated_time: "3-4 hours (1 agent session; uses existing npz spectra, no new spectral compute)"

substrate_framing: |
  GEOMETRIC. Each analog temperature is read off the substrate spectrum, not assigned to a BEC stage.
  Arrow: D_K eigenvalues → the a_n^{ζ} spectral-action moments (a₂ = Einstein-Hilbert/kinematic gradient;
  a₄ = Yang-Mills+Higgs/condensation gradient) → distinct surface gravities κ=½∂_n(c²−v²) at distinct
  Mach-1 surfaces → distinct analog temperatures T_a=ħκ/2π. The three corpus values index three distinct
  spectral-gradient origins (a₂-entry, a₄-exit, BLV-internal-acoustic for S63), exactly as a rotating vs
  charged black hole carries distinct κ. This is the "T_a of WHAT surface?" reconciliation hawking II.3
  flags; it holds regardless of C1 (the entry surface is sonic in both readings; the a₄ "exit" surface is
  sonic under the symmetric reading and a thermodynamic edge inside the open region under the asymmetric
  reading, but carries a well-defined effective κ either way). The S63 0.112 value is the BLV
  internal-acoustic-metric horizon, a distinct observable from the kinematic-transit horizon — placed if
  its BLV-metric κ reproduces 0.112, retired-with-reason otherwise. Direction held substrate → analog.
```

---

## §W4-3. HAWKING-GREYBODY-AS

```yaml
# ---- Identity (4 fields) ----
gate_id: "S95-W4-3-HAWKING-GREYBODY-AS"
schema_version: "R3"
trigger: "[VERIFY]"                       # transmission-filter functional; no signed-direction pre-reg
classification: "PHONONIC"                # the escaping squeeze (would-be A_s) is a phononic excitation
agent_type: "hawking-theorist"            # greybody/analog-transmission domain owner (HAW-V3)
hypothesis: >
  The exit horizon acts as a frequency-dependent transmission filter — the analog greybody factor Γ(ω) ∈
  [0,1] — so the escaping scalar amplitude is A_s = (produced squeeze at the fold) × ∫Γ(ω)dω, NOT the
  produced squeeze itself. This is the model-independent transmission statement (a horizon transmits
  frequency-dependently); it is EXPLICITLY NOT the retracted S73B dispersive-group-velocity mechanism.
  Test whether applying Γ(ω) narrows the band-cited A_s ∈ [3.11, 4.27]×10⁻⁹ (which remains pending ε_pivot).

method:
  description: >
    (1) Build the produced-squeeze spectrum at τ_fold from the entry-horizon BdG dispersion ω_k (the
    broad-spectrum squeeze produced at the fold). (2) Construct the exit-horizon greybody factor Γ(ω) as
    the model-independent transmission coefficient of the exit surface: Γ(ω) = |T(ω)|² from the
    potential-barrier transmission of the exit-horizon effective potential (decoherence-regulated, T≈7.578
    M_KK characteristic scale), with Γ(ω)→1 (transparent) at high ω and Γ(ω)→0 (reflective) at low ω — the
    standard greybody monotone profile, NOT a group-velocity-dispersion filter. (3) Form A_s = (produced
    squeeze) × ∫Γ(ω)dω and report whether the resulting A_s band narrows relative to [3.11,4.27]×10⁻⁹.
    Do NOT claim PASS for A_s itself (ε_pivot open).
  producing_script: "computations/_shared/s95_w4_3_hawking_greybody_as.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "inequality"   # band-width comparison (does Γ-filtered A_s band narrow?)
  form: >
    width(A_s^{Γ-filtered}) < width(A_s^{band-cited} = [3.11,4.27]×10⁻⁹) ; AND Γ(ω) ∈ [0,1] ∀ω
    (physical transmission coefficient); AND Γ(ω) monotone-increasing in ω (standard greybody profile,
    NOT a dispersive group-velocity filter).

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    INFO-band gate (per HAW-V3: "does NOT claim PASS, ε_pivot still open"). The decisive sub-check is the
    structural one: Γ(ω) ∈ [0,1] ∀ω AND monotone in ω (transmission-filter physicality). Band-narrowing is
    the INFO observable, not a PASS threshold.
  direction: "<= (Γ≤1) ; >= (Γ≥0) ; monotone (dΓ/dω≥0)"

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: >
    Γ(ω)=|T(ω)|² ∈ [0,1] is the exact range of a transmission coefficient (unitarity: |T|²+|R|²=1). The
    monotone greybody profile (Γ→1 high-ω transparent, Γ→0 low-ω reflective) is the model-independent
    horizon-transmission statement [hawking-collab II.3]; the analytic anchor is the potential-barrier
    transmission, not a group-velocity dispersion relation (the latter is the RETRACTED S73B mechanism).

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "512 ω-grid points over the produced-squeeze support; ∫Γ(ω)dω by trapezoidal quadrature"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "512"                           # ω-grid for Γ(ω) and the squeeze spectrum
  L_max: "N/A — uses the on-disk entry-horizon BdG dispersion + exit-horizon decoherence data"
  scan_range: "[0, omega_max]"            # ω over the produced-squeeze support (omega_max from BdG dispersion)
  step_size: "adaptive"                   # ω-grid set by the BdG dispersion support; trapezoidal ∫
  tolerance: "1.0e-3"                     # Γ(ω) physicality bound residual (|Γ−clip(Γ,0,1)|)
  scheme: "FW"                            # framework BdG dispersion + exit-horizon decoherence scale
  convention: "ABSOLUTE"                  # A_s band-width comparison is absolute
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain — required (the A_s = squeeze × ∫Γ relation, and the Γ monotone profile)
substitution_chain:
  required: true
  content: |
    Claim: "A_s = (produced squeeze at fold) × ∫Γ(ω)dω with Γ(ω) ∈ [0,1] monotone-increasing in ω; the
    Γ-filtered A_s band is NARROWER than the produced-squeeze band."

      Def 1: produced squeeze P(ω) = the broad-spectrum scalar amplitude produced at the fold (entry-horizon
             BdG; would-be A_s before exit filtering). [hawking-collab II.3; entry-horizon BdG ω_k]
      Def 2: Γ(ω) = |T(ω)|² = transmission coefficient of the exit-horizon effective potential; unitarity
             gives |T|²+|R|²=1 ⟹ Γ(ω) ∈ [0,1]. [model-independent horizon transmission]
      Def 3: greybody monotone profile: Γ(ω) → 0 as ω → 0 (low-frequency modes reflected by the barrier);
             Γ(ω) → 1 as ω → ∞ (high-frequency modes transmitted). [standard greybody; NOT S73B dispersion]
      Substitute: A_s = ∫ P(ω) Γ(ω) dω ≤ ∫ P(ω) dω (since 0 ≤ Γ ≤ 1) = produced squeeze total.
      Simplify: because Γ(ω) ≤ 1 everywhere and Γ(ω) < 1 on a set of positive ω-measure (the reflected
             low-ω band), the filtered amplitude is STRICTLY less than the produced total, and the SPREAD
             of the filtered amplitude over the surviving (transmitted) band is NARROWER than the produced
             spread.
      Canonical form: A_s^{filtered} = ∫P(ω)Γ(ω)dω < ∫P(ω)dω; width(filtered) ≤ width(produced).
      Direction: the exit horizon SUPPRESSES the escaping amplitude (Γ≤1) and NARROWS its band (low-ω
             reflection) → the band-cited A_s [3.11,4.27]×10⁻⁹ should narrow under the filter.
      Conclusion: INFO gate — the structural Γ∈[0,1]-monotone check is the decisive sub-check; whether the
             band narrows below the cited width is the INFO observable. A_s itself is NOT PASS (ε_pivot open).

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  exit_horizon_npz:
    path: "computations/session-73/s73a_exit_horizon_bog.npz"   # exit-horizon decoherence + dispersion
    sha256: "<computed-at-runtime>"
  entry_horizon_npz:
    path: "computations/session-71/s71_entry_horizon_spectrum.npz"   # produced-squeeze BdG spectrum
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w4_3_hawking_greybody_as.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w4_3_hawking_greybody_as.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w4_3_hawking_greybody_as.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W4-3-HAWKING-GREYBODY-AS:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false      # [VERIFY] trigger, no signed-direction pre-reg
  wp_section:
    path: "sessions/archive/session-95/session-95-w4-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W4-3. S95-W4-3-HAWKING-GREYBODY-AS"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  RESERVED — not the target outcome. A_s cannot PASS here because ε_pivot is open (HAW-V3 explicit). If the
  Γ(ω) physicality + monotone-profile structural check holds AND the band demonstrably narrows, the gate
  closes as INFO (band-narrowed), not PASS. PASS is reserved for a future gate that also pins ε_pivot.
FAIL_meaning: >
  The constructed Γ(ω) violates physicality (Γ(ω)∉[0,1] for some ω) OR is non-monotone in a way that
  requires a dispersive group-velocity mechanism (which would revive the RETRACTED S73B mechanism — a
  FAIL by construction, since this gate asserts ONLY the model-independent transmission filter). A FAIL
  means the exit surface cannot be given a model-independent greybody reading.
INFO_meaning: >
  Γ(ω) ∈ [0,1] monotone-increasing (physical transmission filter confirmed) AND the Γ-filtered A_s band is
  reported — INFO if it narrows relative to [3.11,4.27]×10⁻⁹, INFO-no-narrowing if it does not. Either way
  the gate is INFO (ε_pivot open). Records the model-independent greybody filter for the §6.2 clause
  (hawking II.3's "produced squeeze × exit greybody factor, not the produced squeeze itself").

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w4_3_hawking_greybody_as.py"
    - "computations/session-95/s95_w4_3_hawking_greybody_as.npz"
    - "computations/session-95/s95_w4_3_hawking_greybody_as.png"
  estimated_time: "4-6 hours (1 agent session; greybody transmission construction + ω-quadrature)"

substrate_framing: |
  PHONONIC. The escaping scalar amplitude A_s is a phononic excitation of the substrate — the squeeze
  produced when the D_K eigenvalue spectrum reorganizes at the van Hove fold. Arrow: D_K eigenvalues →
  entry-horizon BdG dispersion ω_k → produced squeeze P(ω) (broad-spectrum, at the fold) → exit-horizon
  effective potential (decoherence-regulated) → transmission coefficient Γ(ω)=|T(ω)|² (the analog greybody
  factor) → escaping A_s = ∫P(ω)Γ(ω)dω. The horizon "determines what escapes, not what is produced"
  (the document's own phrase): the exit surface filters the produced phononic squeeze frequency-by-
  frequency. CRITICAL retraction boundary (per HAW-V3 + the hawking-theorist memory's Permanent
  Retraction): this gate asserts ONLY the model-independent statement that a horizon transmits
  frequency-dependently (Γ∈[0,1] monotone). It does NOT revive the retracted S73B dispersive
  group-velocity greybody MECHANISM — the producing script MUST construct Γ(ω) from a potential-barrier
  transmission coefficient, NOT from a group-velocity dispersion relation, and the WP §W4-3 MUST state
  this distinction explicitly. Direction held substrate → analog.
```

---

## §W4-4. SP-CONFORMAL-EMBED

```yaml
# ---- Identity (4 fields) ----
gate_id: "S95-W4-4-SP-CONFORMAL-EMBED"
schema_version: "R3"
trigger: "[VERIFY]"                       # conformal-factor reproduction within a pre-reg q-range
classification: "GEOMETRIC"               # conformal embedding of two causal structures
agent_type: "schwarzschild-penrose-geometer"   # conformal-compactification domain owner (SP-V5)
hypothesis: >
  There exists an explicit conformal factor Ω(τ) embedding the derived 1+1D modulus-space causal structure
  (Diagram B: genesis ℐ⁻-boundary at τ=0, extremal horizon at τ_fold=0.19, τ→∞ censored singularity) into
  the 4D product-spacetime causal structure (Diagram A), such that Ω(τ) reproduces the effective scale
  factor a_eff(τ)=(a₂(τ)/a₂(today))^{1/2} within the SCALE-FACTOR-54 q-range, and the embedding maps the
  fold extremal horizon to a 4D causal feature. This is the causal-geometry piece of the §6.3 a(t) bridge.

method:
  description: >
    (1) Construct the modulus-space conformal structure from Diagram B's flat 1+1D metric ds²=−dt²+G_mod dτ²
    (G_mod=5.0, c_τ=1/√5=0.447) with the labeled landmarks (τ=0 genesis boundary, τ_fold=0.19 extremal
    horizon, τ→∞ singularity). (2) Construct the proxy effective scale factor a_eff(τ)=(a₂(τ)/a₂(today))^{1/2}
    from the E3 R_K(τ) curvature and a₂(τ) (a_2_FW_zeta=2776.165389 at the fold). (3) Solve for the conformal
    factor Ω(τ) relating ds²_B = Ω²(τ) ds²_4D-causal so the conformal structures coincide; verify Ω(τ)
    reproduces a_eff(τ) within the SCALE-FACTOR-54 q-range (q: −0.97→+0.81). (4) Verify the embedding maps the
    fold extremal horizon (κ=0 double-root) to a 4D causal feature. Sage-verify Ω(τ) symbolically where the
    closed form admits it.
  producing_script: "computations/_shared/s95_w4_4_sp_conformal_embed.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "inequality"   # Ω(τ) reproduces a_eff(τ) within the SCALE-FACTOR-54 q-range
  form: >
    q_Ω(τ) := −Ω''(τ)Ω(τ)/Ω'(τ)² (the conformal-factor deceleration parameter) lies within the
    SCALE-FACTOR-54 range [−0.97, +0.81] across the physical window τ∈[0.19, 0.40] ; AND the embedding
    maps the τ_fold extremal horizon (κ=0) to a 4D null/causal feature (a finite conformal-boundary or
    horizon image, NOT a coordinate-singular artifact).

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    q_Ω(τ) ∈ [−0.97, +0.81] (SCALE-FACTOR-54 q-range; INCLUSIVE) across τ∈[0.19,0.40] AND the fold
    extremal-horizon image is a well-defined 4D causal feature (finite Ω at the horizon, Ω' encoding the
    κ=0 double-root as a 4D causal degeneracy).
  direction: "within-band ([−0.97 <= q_Ω <= +0.81])"

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: >
    Diagram B is a FLAT 1+1D Minkowski metric (Phononic-Penrose-Diagrams §Diagram B: ds²=−dt²+G_mod dτ²,
    G_mod=5.0, c_τ=0.447) — conformally flat by construction. a_eff(τ)=(a₂(τ)/a₂(today))^{1/2} is the proxy
    scale factor (SP-V5 inputs). SCALE-FACTOR-54 provides a(τ) from Connes distance with q∈[−0.97,+0.81].
    The conformal factor relating two conformally-flat 1+1D structures is analytically Ω=a_eff up to a
    multiplicative constant; the q-range is the analytic target.

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "1000 τ-points on [0.19, 0.40] (physical window); Sage symbolic check of Ω(τ) closed form"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "1000"                          # τ-grid on the physical window
  L_max: "N/A — geometric construction from E3 R_K(τ) closed form + a₂(τ), no diagonalization"
  scan_range: "[0.19, 0.40]"              # physical window: fold extremal horizon to post-fold epoch
  step_size: "2.1e-4"                     # uniform τ-grid on [0.19,0.40]
  tolerance: "1.0e-6"                     # symbolic-vs-numeric Ω(τ) agreement; q-range is the gate band
  scheme: "zeta"                          # a₂(τ) = a_2^{ζ} (zeta-regularized); a_2_FW_zeta=2776.165389
  convention: "RATIO"                     # a_eff = (a₂(τ)/a₂(today))^{1/2} is a ratio
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8"                # 1D τ-construction; Sage MCP for symbolic Ω(τ)

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain — required (the Ω = a_eff conformal-factor identification + q-direction)
substitution_chain:
  required: true
  content: |
    Claim: "The conformal factor Ω(τ) embedding Diagram B into Diagram A equals the effective scale factor
    a_eff(τ)=(a₂(τ)/a₂(today))^{1/2} up to a constant, and its deceleration q_Ω(τ) lies in the
    SCALE-FACTOR-54 range [−0.97,+0.81]."

      Def 1: Diagram B metric: ds²_B = −dt² + G_mod dτ², G_mod=5.0 (FLAT 1+1D Minkowski; conformally flat).
             [Phononic-Penrose-Diagrams §Diagram B]
      Def 2: 4D causal structure (Diagram A factor): ds²_4D = a_eff(τ)²(−dη² + dx²) in conformal time η
             (FRW-like; the 12D product diagram is conformally the 4D diagram with stiff matter w≥1).
             [Phononic-Penrose-Diagrams §Diagram A, line 135]
      Def 3: a_eff(τ) = (a₂(τ)/a₂(today))^{1/2}; a₂(τ) the second Seeley-DeWitt moment (a_2_FW_zeta=2776.17
             at the fold). [canonical_constants:592; SP-V5 inputs]
      Substitute: a conformal embedding ds²_B = Ω²(τ) ds²_4D between two conformally-flat structures requires
             Ω²(τ) · a_eff(τ)² = (modulus-frame factor), so Ω(τ) ∝ 1/a_eff(τ) · (modulus factor) — pinning
             Ω(τ) as the conformal factor that carries Diagram-B's flat structure onto Diagram-A's
             a_eff-warped structure.
      Simplify: with the modulus factor normalized at τ_today, Ω(τ) reproduces a_eff(τ) up to the constant.
      Canonical form: q_Ω(τ) = −Ω''Ω/Ω'² evaluated on a_eff(τ).
      Direction: the physical epoch is DECELERATING (stiff matter w≥1, Diagram A "resembles decelerating
             FRW not de Sitter", line 135) → q_Ω > 0 in the matter era; SCALE-FACTOR-54 records q crossing
             from −0.97 (accelerating) to +0.81 (decelerating) — so q_Ω(τ) ∈ [−0.97,+0.81] is the admissible
             band, and the gate PASSES iff the computed q_Ω stays within it across [0.19,0.40].
      Conclusion: Ω(τ) is the conformal factor; PASS iff q_Ω ∈ [−0.97,+0.81] AND the fold-horizon image is a
             4D causal feature; INFO iff Ω derivable but M_KK⁻¹→s normalization stays open; FAIL iff no
             consistent Ω exists (conformal INEQUIVALENCE of the bi-metric structures).

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  scale_factor_54_npz:
    path: "computations/session-54/s54_scale_factor.npz"   # SCALE-FACTOR-54 a(τ) + q-range
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w4_4_sp_conformal_embed.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w4_4_sp_conformal_embed.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w4_4_sp_conformal_embed.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W4-4-SP-CONFORMAL-EMBED:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false      # [VERIFY] trigger
  wp_section:
    path: "sessions/archive/session-95/session-95-w4-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W4-4. S95-W4-4-SP-CONFORMAL-EMBED"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  An explicit conformal factor Ω(τ) is constructed; its deceleration q_Ω(τ) lies in the SCALE-FACTOR-54
  range [−0.97,+0.81] across the physical window AND the embedding maps the fold extremal horizon to a 4D
  causal feature. The modulus-space→4D conformal embedding is delivered — the causal-geometry piece of the
  §6.3 a(t)/K_pivot bridge that SP-V5 names. (a(t) normalization M_KK⁻¹→s may still be open; that is INFO.)
FAIL_meaning: >
  No consistent conformal embedding exists — Ω(τ) cannot be found relating the two conformal structures
  (the bi-metric scalar/tensor structures are conformally INEQUIVALENT). Per SP-V5 this would indicate a
  DEEPER obstruction than the open a(t) normalization, and the FAIL itself would need adjudication.
INFO_meaning: >
  The conformal factor Ω(τ) is derivable AND reproduces a_eff(τ) in the q-range, but the a(t) normalization
  (the M_KK⁻¹→seconds dimensional map) remains open — the embedding is conformally pinned but the physical
  scale factor a(t) is not yet dimensionful. Per SP-V5's INFO clause. This is the EXPECTED outcome if the
  embedding succeeds conformally but C2/K_pivot stays open.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w4_4_sp_conformal_embed.py"
    - "computations/session-95/s95_w4_4_sp_conformal_embed.npz"
    - "computations/session-95/s95_w4_4_sp_conformal_embed.png"
  estimated_time: "1 agent session (geometric construction + Sage verification of Ω(τ))"

substrate_framing: |
  GEOMETRIC. The conformal embedding is read off the substrate spectrum, not imposed between two stages.
  Arrow: D_K eigenvalues → E3 curvature R_K(τ) and the a₂^{ζ} moment → the effective scale factor
  a_eff(τ)=(a₂(τ)/a₂(today))^{1/2} → the conformal factor Ω(τ) embedding the DERIVED modulus-space causal
  structure (Diagram B, which IS derived from e^{−S} monotonicity + COSMIC-CENSORSHIP-49) into the 4D
  product causal structure (Diagram A). The modulus-space conformal structure is fundamental and derived;
  the 4D-spacetime conformal structure is emergent; the embedding Ω(τ) is the undelivered map between them
  — the same a(t) bridge §6.3 names, but posed precisely as a conformal-factor construction rather than a
  vague "derive Friedmann." Substrate-first: τ IS the substrate's intrinsic deformation parameter (Level-2
  moduli-deformation substrate-IS per phononic-framing.md), NOT a coordinate on a meta-container; the
  modulus-space Penrose diagram is the substrate's own causal structure, and the 4D diagram is what it
  projects to. Direction held substrate → emergent.
```

---

## §W4-5. SP-12D-SINGULARITY-CENSOR

```yaml
# ---- Identity (4 fields) ----
gate_id: "S95-W4-5-SP-12D-SINGULARITY-CENSOR"
schema_version: "R3"
trigger: "[SIGN]"                         # NEC sign along the trajectory + anisotropic timelike/spacelike character
classification: "GEOMETRIC"               # 12D curvature invariant + energy-condition + causal-character
agent_type: "schwarzschild-penrose-geometer"   # singularity-theorem / cosmic-censorship domain owner (SP-V6)
hypothesis: >
  On the EXACT 12D product metric ds²₁₂ = −dt² + a(t)²dx₃² + g_ab(τ(t))dyᵃdyᵇ, the Kretschmann scalar
  diverges as τ→∞ with a DIRECTION-DEPENDENT causal character (timelike in the SU(2) block which contracts
  R→0, spacelike in the ℂ²/U(1) block which expands), AND the censoring barrier (NEC) holds along the
  PHYSICAL trajectory up to the overshoot turnaround τ=1.614 — upgrading the fiber-only result
  (CONFORMAL-TRANSITION-49) to a full-spacetime weak-cosmic-censorship statement.

method:
  description: >
    (1) Build the exact 12D product metric ds²₁₂ = −dt² + a(t)²dx₃² + g_ab(τ(t))dyᵃdyᵇ with the Jensen
    fiber metric g_ab carrying exponents (2,−6,4)/8 (u(1)→e^{2τ}, su(2)→e^{−2τ}, ℂ²→e^{τ} per the canonical
    Jensen convention; SU(2) contracts, ℂ²/U(1) expand). (2) Compute the 12D Kretschmann scalar K₁₂ =
    R_abcd R^abcd on a τ-grid spanning [0.19, ∞) (numerically [0.19, 5.0] with the e^{4τ} divergence
    confirmed asymptotically). (3) Classify the causal character of the τ→∞ singularity per block: SU(2)
    block (contracting, Weyl divergent) → TIMELIKE (i⁺ analog, infinitely far conformally); ℂ²/U(1) blocks
    (expanding, Weyl 2.582/1.291 finite) → SPACELIKE (r=0 analog, finite conformal distance). (4) Compute
    the Null Energy Condition T_μν k^μ k^ν ≥ 0 along the physical trajectory τ(t) from genesis through the
    overshoot turnaround τ=1.614 (35/35 negative Hessian; tau_turn=0.088/0.218; v_crit=219.3).
  producing_script: "computations/_shared/s95_w4_5_sp_12d_singularity_censor.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set + inequality"   # set: per-block causal character {timelike, spacelike}; inequality: NEC ≥ 0
  form: >
    PRIMARY (singularity character): K₁₂(τ)→∞ as τ→∞ with per-block causal character matching
    {SU(2): TIMELIKE, ℂ²/U(1): SPACELIKE} (the CONFORMAL-TRANSITION-49 fiber signature reproduced on the
    full 12D metric). SECONDARY (censoring): NEC residual min_{τ∈[0.19,1.614]} T_μν k^μ k^ν ≥ 0 along the
    physical trajectory (the WEC/DEC also checked as in COSMIC-CENSORSHIP-49).

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    PRIMARY: per-block causal character matches {SU(2): timelike, ℂ²/U(1): spacelike} (conformal-distance
    sign: SU(2) infinite, ℂ²/U(1) finite). SECONDARY: NEC residual ≥ 0 with tolerance −1e-9 (numerical
    floor; a residual ≥ −1e-9 counts as NEC-holds) across τ∈[0.19, 1.614].
  direction: ">= (NEC) ; set-match (causal character)"

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: >
    The Jensen exponents (2,−6,4)/8 are exact (canonical Jensen convention; MEMORY §2). The e^{4τ}
    Kretschmann divergence and the SU(2)-timelike / ℂ²U(1)-spacelike fiber signature are CONFORMAL-
    TRANSITION-49 (PASS); the τ→∞ Weyl values 2.582 (ℂ²) / 1.291 (U(1)) finite vs SU(2) divergent are
    Phononic-Penrose-Diagrams lines 284-288. The NEC/WEC/DEC-hold result on the physical trajectory is
    COSMIC-CENSORSHIP-49 (PASS, tau_turn=0.088/0.218, v_crit=219.3). This gate LIFTS the fiber-only result
    to the 12D metric; the analytic targets are the fiber-level signs.

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "2000 τ-points on [0.19, 5.0] (K₁₂ + per-block Weyl); NEC on [0.19, 1.614] at 1000 points"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "2000"                          # τ-grid for K₁₂ and per-block curvature
  L_max: "N/A — exact 12D product metric (4D FRW × 8D Jensen fiber); analytic curvature invariants"
  scan_range: "[0.19, 5.0]"               # τ window: fold to deep-Zone-II (e^{4τ} divergence asymptote)
  step_size: "2.4e-3"                     # uniform τ-grid on [0.19,5.0]; NEC sub-grid Δτ≈1.4e-3 on [0.19,1.614]
  tolerance: "1.0e-9"                     # NEC residual numerical floor (residual ≥ −1e-9 ⟹ NEC holds)
  scheme: "FW"                            # framework Jensen fiber metric, exponents (2,−6,4)/8
  convention: "ABSOLUTE"                  # NEC is an absolute ≥0 inequality; causal character is set-match
  random_seed: "N/A — deterministic"
  GPU_path: "torch.linalg"                # 12×12 metric Riemann tensor contractions; torch eig/contractions

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain — MANDATORY ([SIGN]: NEC ≥ 0 + per-block timelike/spacelike character)
substitution_chain:
  required: true
  content: |
    Claim A (anisotropic singularity character): "As τ→∞ the 12D Kretschmann K₁₂ diverges; the SU(2) block
    is TIMELIKE (conformal distance infinite) and the ℂ²/U(1) blocks are SPACELIKE (conformal distance
    finite)."

      Def 1: Jensen fiber metric g_ab with exponents (2,−6,4)/8: u(1)→e^{2τ}, su(2)→e^{−2τ}(×3),
             ℂ²→e^{τ}(×4) (canonical Jensen convention; MEMORY §3). [MEMORY.md §3 Conventions]
      Def 2: 12D product metric ds²₁₂ = −dt² + a(t)²dx₃² + g_ab(τ(t))dyᵃdyᵇ. [SP-V6; Diagram A]
      Def 3: conformal distance to τ→∞ in a block = ∫^∞ dτ / (scale factor of that block). SU(2) scale
             e^{−2τ}→0 (contracts) ⟹ ∫^∞ e^{2τ}dτ DIVERGES ⟹ infinite conformal distance ⟹ TIMELIKE
             (i⁺ analog). ℂ²/U(1) scale e^{τ}/e^{2τ}→∞ (expand) ⟹ ∫^∞ e^{−τ}dτ CONVERGES ⟹ finite
             conformal distance ⟹ SPACELIKE (r=0 analog). [Phononic-Penrose-Diagrams lines 284-288]
      Substitute: K₁₂ ~ (e^{4τ} from the dominant Jensen exponent); diverges as τ→∞.
      Canonical form: per-block conformal-distance sign: SU(2) → ∞ (timelike); ℂ²/U(1) → finite (spacelike).
      Direction: SU(2) TIMELIKE, ℂ²/U(1) SPACELIKE (the anisotropic Kasner-type signature, no GR analog).
      Conclusion: PRIMARY PASS iff the 12D per-block causal character reproduces this fiber signature.

    Claim B (censoring — NEC sign along the physical trajectory): "T_μν k^μ k^ν ≥ 0 along the physical
    trajectory τ(t) up to the overshoot turnaround τ=1.614."

      Def 4: NEC: for every null k^μ, T_μν k^μ k^ν ≥ 0. Via Einstein eq (a₂ channel), T_μν k^μ k^ν =
             (1/8πG) R_μν k^μ k^ν, so NEC ⟺ R_μν k^μ k^ν ≥ 0 (the null Raychaudhuri focusing condition).
      Def 5: physical trajectory τ(t) runs genesis (τ=0) → physical epoch (τ≈0.22) → ... up to the
             counterfactual turnaround τ=1.614 (tau_overshoot=1.614; 35/35 negative Hessian, S77).
             [tau_overshoot=1.614 canonical; COSMIC-CENSORSHIP-49 NEC/WEC/DEC hold, tau_turn=0.088/0.218]
      Substitute: COSMIC-CENSORSHIP-49 established R_μν k^μ k^ν ≥ 0 on the FIBER along [0.19, 1.614]
             (NEC/WEC/DEC hold, SEC transient); this gate evaluates the SAME contraction on the full 12D
             null cone (which includes the 4D x₃ directions + the fiber directions).
      Canonical form: min_{τ∈[0.19,1.614]} R_μν k^μ k^ν ≥ −1e-9 (numerical floor).
      Direction: NEC residual ≥ 0 (holds) — the censoring barrier is present; the singularity at τ→∞ is
             UNREACHABLE from the physical epoch (weak cosmic censorship). A residual < −1e-9 anywhere on
             the physical trajectory would mean NEC VIOLATED → a naked-singularity pathway → directly
             contradicts CONFORMAL-TRANSITION-49, so a FAIL would itself need adjudication (per SP-V6).
      Conclusion: SECONDARY PASS iff NEC residual ≥ −1e-9 across [0.19, 1.614]; sign_verdict PASS iff the
             NEC residual sign is non-negative on the physical trajectory.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  cosmic_censorship_49_npz:
    path: "computations/session-49/s49_cosmic_censorship.npz"        # NEC/WEC/DEC data, tau_turn, v_crit
    sha256: "<computed-at-runtime>"
  conformal_transition_49_npz:
    path: "computations/session-49/s49_conformal_transition.npz"     # fiber-level anisotropic signature
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w4_5_sp_12d_singularity_censor.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w4_5_sp_12d_singularity_censor.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w4_5_sp_12d_singularity_censor.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W4-5-SP-12D-SINGULARITY-CENSOR:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true       # [SIGN] trigger → 3-tuple companion row REQUIRED
  wp_section:
    path: "sessions/archive/session-95/session-95-w4-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W4-5. S95-W4-5-SP-12D-SINGULARITY-CENSOR"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  On the full 12D metric: the τ→∞ Kretschmann divergence is direction-dependent with the SU(2)-timelike /
  ℂ²U(1)-spacelike signature AND the NEC holds along the physical trajectory up to the overshoot turnaround
  τ=1.614. This UPGRADES the genesis-singularity claim from a fiber-only statement to a full-spacetime weak-
  cosmic-censorship result (SP-V6): the genuine singularity exists at τ→∞, is anisotropic, and is censored
  — the framework's analog of Penrose's 1965 program landing on the right side, now on the 12D metric.
FAIL_meaning: >
  The 12D NEC is VIOLATED on the physical trajectory (residual < −1e-9 somewhere in [0.19,1.614]) — this
  would open a naked-singularity pathway and directly CONTRADICT CONFORMAL-TRANSITION-49 (PASS). Per SP-V6,
  a FAIL would itself need adjudication (a 12D NEC violation against an established fiber-level censorship
  result signals either a metric-construction error or a genuine 12D-vs-fiber tension to be resolved).
INFO_meaning: >
  The anisotropic SU(2)/ℂ²U(1) singularity signature is confirmed on the 12D metric BUT the censoring (NEC)
  is verified only at the fiber level, not the full 12D null cone (e.g., the 4D x₃-direction null
  contractions are not decisively evaluated). Per SP-V6's INFO clause ("signature confirmed but censoring
  is only fiber-level"). The singularity character is upgraded; the censoring upgrade is partial.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/_shared/s95_w4_5_sp_12d_singularity_censor.py"
    - "computations/session-95/s95_w4_5_sp_12d_singularity_censor.npz"
    - "computations/session-95/s95_w4_5_sp_12d_singularity_censor.png"
  estimated_time: "1 agent session (12D curvature-invariant + energy-condition computation, Sage/torch)"

substrate_framing: |
  GEOMETRIC. The singularity and its censoring are read off the substrate's own Jensen-deformed geometry,
  not imposed on a spacetime container. Arrow: D_K eigenvalues → the Jensen fiber metric g_ab(τ) with
  exponents (2,−6,4)/8 → the 12D product curvature K₁₂(τ) → the anisotropic τ→∞ singularity (SU(2) block
  contracts R→0 ⟹ Weyl diverges ⟹ timelike i⁺-analog; ℂ²/U(1) blocks expand ⟹ Weyl finite 2.582/1.291 ⟹
  spacelike r=0-analog) → the NEC focusing condition along the physical trajectory → the censoring barrier
  (the singularity is UNREACHABLE from the physical epoch τ≈0.22, doubly bounded by COSMIC-CENSORSHIP-49
  below and the τ=1.614 overshoot turnaround above). Substrate-first: τ→∞ is the substrate's own intrinsic
  deformation limit (Level-2 moduli-deformation substrate-IS), NOT a far corner of a pre-existing
  container; the anisotropic Kasner-type singularity has NO standard GR analog precisely because it is the
  substrate's internal geometry diverging, not an external spacetime crunch. The honest statement is the
  STRONGER cosmic-censorship one (SP-V6): "genuine singularity at τ→∞, anisotropic, censored," replacing
  the over-selling "singularity-free." Direction held substrate → emergent causal structure.
```

---

## Verdict source

All Wave 4 gates append to the ONE canonical verdict file:

```
verdict_source: computations/session-95/s95_gate_verdicts.txt
```

Per `.claude/rules/gate-verdicts.md`, this is the canonical location; the variants `computations/_shared/s95_gate_verdicts.txt`, `sessions/archive/session-95/s95_gate_verdicts.txt`, and `sessions/session-plan/s95_gate_verdicts.txt` are FORBIDDEN. Never use `expected_verdicts: [...]` — use the `verdict_source` pointer. Each gate block's `output_artifacts.verdict_line.path` pins the same canonical path; the SIGN-trigger gates (S95-W4-1, S95-W4-2, S95-W4-5) additionally require the schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row per `gate-verdicts.md §"Schema-v2 canonical form"`.

## Wave 4 → Doc-Integration Decision Point

Wave 4 produces NO downstream S95 compute wave (it is the last causal-structure wave). Its verdicts gate the **doc-integration `/rclab-workshop`** (`session-95-context.md §D`), NOT an S95 successor compute gate. Branching on the §W4-1 C1 discriminator:

- **§W4-1 PASS with N_zeros = 1 (asymmetric SELECTED)** → the §6.2 doc-integration adopts sp V.3's ASYMMETRIC redraw (ONE entry horizon + open expulsion exit; the BCS edge τ≈0.235 and decoherence τ∼0.16 are thermodynamic features INSIDE the open region, ingoing-null-ray direction stated). The transit V.6 "two distinct horizons" STRENGTHEN clause (`integration-plan §6.2`, "contingent: only if C1 keeps two horizons") is DROPPED. §W4-2's three-surface ledger still holds (the a₄ "exit" surface is a thermodynamic edge with a well-defined effective κ inside the open region).
- **§W4-1 PASS with N_zeros = 2 (symmetric SELECTED)** → the §6.2 doc-integration KEEPS the symmetric two-horizon table; the transit V.6 Wronskian-licensing STRENGTHEN clause is RETAINED; §W4-2 certifies the entry/exit κ-ratio = 9.61 cross-table; §W4-1's SECONDARY surface-gravity ratio is the certification.
- **§W4-1 INFO (impedance attribution recorded, N_zeros resolved but ratio in 10–25% band, or grazing near-second-horizon)** → the doc-integration adopts the resolved N_zeros structure with the impedance-attribution footnote; the §6.2 redraw notes the near-degeneracy.
- **§W4-1 FAIL (N_zeros indeterminate)** → C1 is NOT resolved by compute; the doc-integration §6.2 edit STAYS BLOCKED and a 2-agent sp-vs-(transit/hawking) `/rclab-workshop` is required (the fallback `integration-plan §G` names). This is the only branch that does not unblock §6.2.

§W4-2 / §W4-3 (analog-T ledger + greybody) feed the §6.2 STRENGTHEN clauses regardless of the C1 branch. §W4-4 / §W4-5 feed the §5.2/§6.3 geometry edits (cosmic-censorship restatement V.1; conformal-embedding a(t)-bridge piece) independent of C1.

## Wave 4 Machinery-Enumeration Pin

Aggregate of all five gate `machinery_pin_map` blocks (the sig_4 v3-ladder source; consumed by `computations/_shared/_yaml_gate_validator.py`):

| Gate | N_eval | L_max | scan_range | step_size | tolerance | scheme | convention | seed | GPU_path |
|:-----|:-------|:------|:-----------|:----------|:----------|:-------|:-----------|:-----|:---------|
| S95-W4-1 | 3500 | N/A | [0.05,0.40] | 1.0e-4 | 1.0e-6 / RATIO 0.10 | BLV | RATIO | det | cpu-cap-OMP8 |
| S95-W4-2 | 3 | N/A | N/A | 1.0e-4 | 0.10 (RATIO) | zeta | RATIO | det | cpu-cap-OMP8 |
| S95-W4-3 | 512 | N/A | [0,omega_max] | adaptive | 1.0e-3 | FW | ABSOLUTE | det | cpu-cap-OMP8 |
| S95-W4-4 | 1000 | N/A | [0.19,0.40] | 2.1e-4 | 1.0e-6 / q-band | zeta | RATIO | det | cpu-cap-OMP8 |
| S95-W4-5 | 2000 | N/A | [0.19,5.0] | 2.4e-3 | 1.0e-9 | FW | ABSOLUTE | det | torch.linalg |

All gates: `random_seed = N/A — deterministic`. All `audit_sha256_inputs = [script, canonical, pinmap]`; `content_sha256_inputs = [script]`. No L_max diagonalization in any W4 gate (all use on-disk spectra + a_n moments + analytic curvature invariants), so the `D_K Block-Diagonality + Recursive-Casimir-Projection` feasibility pre-check (`math-scripts.md`) is N/A — no irrep construction. `torch.linalg` pinned for §W4-5 only (12×12 metric Riemann contractions; well under the 17.1 GB VRAM cap, dense storage trivial).

## Wave 4 Input-SHA Ledger

Every input file the W4 gates consume, with SHA-256 status per `gate-verdicts.md`. The canonical-constants module is shared by all five gates. All inputs are STATIC on-disk files but their SHAs are computed at runtime (the producing scripts log the SHA of every input in the first 20 lines of stdout per `gate-verdicts.md §"During computation"`; plan-freeze cross-check by `computations/_shared/_plan_upstream_pin_validator.py`).

| Input file | Consumed by | SHA-256 |
|:-----------|:------------|:--------|
| `computations/_shared/canonical_constants.py` | all 5 | `<computed-at-runtime>` |
| `computations/session-85/s85_w6_acoustic_white_hole_formal.npz` | W4-1 | `<computed-at-runtime>` |
| `computations/session-74/s74_s70_s72_exit_horizon_audit.npz` | W4-1 | `<computed-at-runtime>` |
| `computations/session-71/s71_entry_horizon_spectrum.npz` | W4-2, W4-3 | `<computed-at-runtime>` |
| `computations/session-73/s73a_exit_horizon_bog.npz` | W4-2, W4-3 | `<computed-at-runtime>` |
| `computations/session-54/s54_scale_factor.npz` | W4-4 | `<computed-at-runtime>` |
| `computations/session-49/s49_cosmic_censorship.npz` | W4-5 | `<computed-at-runtime>` |
| `computations/session-49/s49_conformal_transition.npz` | W4-5 | `<computed-at-runtime>` |

**Runtime path-resilience note**: the npz input filenames are the canonical provenance names from the knowledge MCP (`s85_w6_acoustic_white_hole_formal`, `s74_s70_s72_exit_horizon_audit`, `s73a_exit_horizon_bog`, etc.). If a producing script finds a npz absent at its pinned path, it MUST resolve via the knowledge-MCP provenance entry (the `provenance` table maps script→npz) before falling back to a recompute, per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction. Any path correction is documented in the verdict-line `value=` field (`runtime_canonical_path_corrected_from_<plan>_to_<runtime>`).

## Wave 4 Canonical-Constants Pins (substrate-first provenance)

All numerical pins below are sourced from `computations/_shared/canonical_constants.py` (substrate-first; SUBSTRATE-FIRST-PROVENANCE audit-clean). No external-paper provenance is treated as canonical; the hawking-collab / sp-collab corpus values that lack a canonical pin are flagged:

| Constant | Value | Source | Used by |
|:---------|:------|:-------|:--------|
| `tau_fold` | 0.19 | canonical (S12/S42, CONST-FREEZE-42) | W4-1, W4-2, W4-4, W4-5 |
| `c_BLV` | 0.485 | canonical (S64, s64_sound_speed) | W4-1, W4-2 |
| `c_fabric` | 209.974 | canonical (S42) | W4-1 (acoustic-radius Mach context) |
| `Mach_max_framework` | 13.75 | canonical (`Mach_max_framework`; default `Mach_max`) | W4-1, W4-2 |
| `Mach_max_analog` | 54.3 | canonical (BEC-analog; NOT substrate — guard) | W4-1 (guard only) |
| `a_2_FW_zeta` | 2776.165389 | canonical (S88; a₂^{ζ}) | W4-2, W4-4 |
| `a_4_FW_zeta` | 1350.7216 | canonical (S75; a₄^{ζ}) | W4-2 |
| `T_acoustic` | 0.112 | canonical (S42/S47; the S63 internal-acoustic T_a) | W4-2 |
| `tau_overshoot` | 1.614 | canonical (S77) | W4-5 |
| `v_crit` | 219.3 | canonical (COSMIC-CENSORSHIP-49) | W4-5 |
| `G_mod` | 5.0 | Phononic-Penrose-Diagrams §Diagram B (modulus 1+1D metric) | W4-4 |

**NON-CANONICAL corpus values requiring runtime derivation or substrate-first sourcing** (flagged per `substrate-first-canonical-sourcing.md §(i)`):

- **`v_transit` (modulus dτ/dt at the fold = 6.669 M_KK)**: NOT a standalone canonical constant. DERIVED as `Mach_max_framework · c_BLV = 13.75 · 0.485 = 6.669` (substitution chain in §W4-1 / §W4-2). Tag `# (local)` in the producing script (computed intermediate, not a framework constant). Cross-checked against the Phononic-Penrose-Diagrams glossary value `v_transit = 6.67 M_KK` (line 50).
- **`T_a^entry = 72.8 M_KK` and `T_a^exit = 7.578 M_KK`**: corpus values from hawking-collab II.3 (S70/S71/S72/S73a). NOT in `canonical_constants.py`. §W4-2 COMPUTES κ for each surface and reproduces these as TARGETS (RATIO tol 0.10); they are pre-registered comparison targets sourced from the collab corpus, NOT canonical pins consumed as inputs. If §W4-2 PASSES, the canonical-write-order (`math-scripts.md`) applies: emit verdict → promote `T_a_entry_FW`/`T_a_exit_FW` to `canonical_constants.py` with provenance → inventory row. This is a single `update_constant(...)` per value with no sub-keying ambiguity → FIX-IN-SESSION.
- **`c_BdG ≈ 0.751` (S70 BdG sound speed, MEMORY.md)**: NOT in `canonical_constants.py`. NOT consumed by any W4 gate as written (W4-1/W4-2 use the canonical `c_BLV=0.485` scalar sound speed for the acoustic discriminant). If a producing agent finds the BdG sound speed is the physically-correct c for a per-branch crossing (the S73b κ_b construction), that is an INFO-4th-surface finding for §W4-2, and `c_BdG` must be promoted to canonical with provenance BEFORE use, not hardcoded.
- **`A_s ∈ [3.11, 4.27]×10⁻⁹` (band-cited, pending ε_pivot)**: §7.1 band, NOT canonical. §W4-3 uses it as the band-width comparison baseline ONLY (INFO observable), does NOT claim PASS against it (ε_pivot open per HAW-V3).

---

*End Wave 4 plan. C1 discriminator (§W4-1) pre-registers BOTH symmetric and asymmetric outcomes as live; no outcome is pre-decided. All five gate blocks carry the full 8-item PRDR checklist, schema_version=R3, the verdict rubric, effort, substrate_framing, and `verdict_source: computations/session-95/s95_gate_verdicts.txt`. SIGN-trigger gates (W4-1, W4-2, W4-5) carry mandatory substitution chains and require the schema-v2 3-tuple companion row.*
