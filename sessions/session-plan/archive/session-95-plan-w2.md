# Session 95 Plan — Wave 2: One-Loop Structural Completeness (t* de-empiricization)

**Date**: 2026-05-28
**Author**: kaku-speculative-theorist (generated per /rclab-plan per-wave swarm)
**Owner agent**: kaku-speculative-theorist (cross-domain / one-functional-genre reviewer-origin)
**Plan source**: `sessions/session-plan/session-95-context.md` §B rows KAK-V1, KAK-V2, EIN-V3 + §F Wave-2 reading allowances
**Working paper**: `sessions/archive/session-95/session-95-w2-workingpaper.md`
**Verdict file (canonical)**: `computations/session-95/s95_gate_verdicts.txt`

## Wave 2 Summary

Wave 2 attacks the **one-loop structural-completeness** question raised by the kaku and einstein capstone-review collabs: is the framework's master object `S[D_K(τ), f, Λ]` complete and rigid at one loop, or does the one-loop term leave residual structure?

Three independent gates, each on a distinct facet of the same one-functional object:

- **§W2-1 `T-STAR-ONELOOP-ORIGIN`** (kaku-collab §V.1) — the framework's ledger (`phonic-exflation-equation.md §3`/§8.4) is `{τ, Λ, f₀, f₂, f₄} + t*`, where `t* = 0.08832` is the SINGLE empirical functional coupling (the admixture weight on the `e^{-x}` term in the near-canonical regulator `f*(x) = 0.9117·√x + 0.0883·e^{-x}`, gate `SPECTRAL-FUNCTIONAL-FIT-72` PASS at 1.3e-14). The conjecture (kaku §IV.4(1), §V.1): `t*` is NOT empirical — it is the coefficient forced by the one-loop threshold correction `Γ_1loop = ½ Tr ln(D_K²/Λ²)` (§1.3a), computable from the spectrum. PASS de-empiricizes the ledger to `{τ, Λ, f₀, f₂, f₄}` (drops the only empirical coupling); FAIL confirms `t*` is genuinely empirical. **Neutral by pre-registration — both outcomes are physics results.**
- **§W2-2 `EXHAUSTION-FALSIFIER`** (kaku-collab §V.2) — the §1.1 "no room for a third term" claim: trace + inner product EXHAUST the natural scalars of the spectral triple, and every interaction is an inner fluctuation `D_K ↦ D_K + A + ε'JAJ⁻¹`. Tests whether any associative `*`-product / admissible deformation of `S` exists OUTSIDE the inner-fluctuation orbit. This is the substrate analog of asking whether a Witten-`*`-product vertex exists (the SFT cubic vertex the substrate claims it does not need).
- **§W2-3 `NO-WELL-ONE-LOOP`** (einstein-collab §V.3) — the E7 Structural Monotonicity Theorem (`dS/dτ|_fold = +58,672.8 > 0`, no interior stationary point) is a TREE-LEVEL statement. Does adding `Γ_1loop = ½ Tr ln(D_K²/Λ²)` introduce an interior stationary feature in `Γ[τ] = S[D_K(τ)] + Γ_1loop(τ)` over `τ ∈ [0, τ_now]` that is absent at tree level? PASS confirms the monotone-ramp (no-landscape, no-well) picture is one-loop-robust; FAIL (consequential) means one loop creates a genuine interior well.

Carry-forward source: the 10-domain `/rclab-review` panel on `sessions/framework/phonic-exflation-equation.md` (commit 5e5d5fa9), consolidated in `…integration-plan.md §E` (KAK-V1, KAK-V2, EIN-V3 all route to W2).

**Genre framing (kaku, substrate-first)**: §W2-1 and §W2-2 are the two halves of the matrix-model-genre rigidity claim. The substrate is IKKT-adjacent, NOT string field theory (correspondence-table ANTI-bloc #19/#20/#21/#30): it has no Hagedorn tower, no S-duality, no T-duality, and — the positive content tested here — its interactions are FORCED inner fluctuations rather than an ADDED cubic vertex. §W2-1 asks whether the one functional `f`'s single free coupling is also forced (by one loop); §W2-2 asks whether the interaction content is exhausted (no stringy vertex hides outside the orbit). §W2-3 asks whether the one-loop correction respects the monotone ramp that gives the substrate "no landscape AND no stabilizing well" as two faces of E7.

## Wave 2 Decision Point Prerequisites

Wave 2 has **NO intra-S95 upstream prerequisites** — all three gates consume only static prior-session artifacts (the `s84_spectrum_cache_L12_tau019.npz` D_K spectrum cache, `canonical_constants.py`, and the structurally-pinned E7 monotonicity theorem W7/S37). Wave 2 is dispatchable in parallel with W1/W3/W4/W5 immediately at session start; it does not gate on any other S95 wave.

External dependency status (verified at plan-freeze via knowledge MCP):
- `s84_spectrum_cache_L12_tau019.npz` — EXISTS (1.34 MB; 90 Peter-Weyl sectors; L_max=12; 78,080 eigenvalues at L≤10 restriction). Static SHA pinned below.
- `tau_fold = 0.19` — `get_constant("tau_fold")` → 0.19, S12/S42, gate `CONST-FREEZE-42`, not superseded.
- `M_KK = 7.428660036284456e+16` — `get_constant("M_KK")` → present (PROVENANCE gap is W6 hygiene C-A4, NOT this wave; the value is canonical and importable).
- `mellin_f_star_f0 = 0.08832` — present in `canonical_constants.py:539` (S78 W2-D); this IS the canonical `t*` target (the f_0 Mellin moment of f* = the e^{-x} admixture coefficient).
- E7 / W7/S37 Structural Monotonicity Theorem — PROVEN (9,600/9,600 checks, ⟨λ²⟩(τ) monotone for ALL monotone f, ALL Λ, ALL sectors); `S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD` FAIL (`value = −2.04×10⁴`), confirming τ_fold is NOT a stationary point of the bare action.

If, at dispatch, any static input is missing or SHA-mismatched, the gate honestly closes per `.claude/rules/mechanical-closure-discipline.md` (FAIL/PRE-REG-INC with the named missing input), NOT a silent skip.

---

## §W2-1. T-STAR-ONELOOP-ORIGIN

```yaml
# ---- Identity (6 fields) ----
gate_id: "S95-W2-1-T-STAR-ONELOOP-ORIGIN"
schema_version: "R3"
trigger: "[CHAIN]"            # magnitude/sign comparison of computed-vs-empirical t*; substitution chain MANDATORY
classification: "GEOMETRIC"   # spectral-action regulator coefficient at single-τ-slice τ_fold; the fabric's functional, not its excitations
agent_type: "feynman-theorist"   # one-loop effective action Γ_1loop = ½ Tr ln(D²/Λ²); trace-log on the D_K spectrum cache (QFT one-loop specialty)
hypothesis: "The single empirical functional coupling t* = 0.08832 (the e^{-x} admixture weight in f*(x) = 0.9117·√x + 0.0883·e^{-x}) is the coefficient forced by the one-loop threshold correction Γ_1loop = ½ Tr ln(D_K(τ_fold)²/Λ²) projected onto the f_0 Mellin-moment channel — i.e. t* is computable from the L_max=10 spectrum, not empirically fitted to n_s."

method:
  description: >
    Load the D_K(τ_fold) spectrum from the L_max=12 cache, restrict to the L_max=10
    band (78,080 eigenvalues; sectors with p+q≤10). Form dimensionless x_k = |λ_k|²/Λ²
    with Λ = M_KK (eigenvalues are O(1) in M_KK units; min|λ|=0.82>0 so D_K has no zero
    mode at τ_fold and ln(x_k) is finite for all k). Compute the one-loop effective-action
    generator Γ_1loop = ½ Σ_k ln(x_k) (the spectral trace-log of D_K²/Λ², CM/Connes one-loop
    form, §1.3a; S62-einstein-baptista Γ_1loop = ½Tr ln(D²/Λ²)). Compute the tree-level
    spectral action per mode in the √x channel (χ_2 = Σ_k √x_k, the S77-lizzi identity
    "χ_2 IS the spectral action per mode with f(x)=√x"). Extract the e^{-x}-admixture
    coefficient t*_predicted in the PRE-REGISTERED f_0-Mellin-moment channel (the s→0 moment
    where the canonical pin mellin_f_star_f0 lives) via the operationalization pinned in
    audit_discriminators. Compare t*_predicted to canonical t* = mellin_f_star_f0 = 0.08832.
    Report which operationalization was used and the value NEUTRALLY (the gate does NOT assume
    t* is or is not the one-loop coefficient).
  producing_script: "computations/session-95/s95_w2_1_t_star_oneloop_origin.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "ratio"
  form: "|t*_predicted − t*_canonical| / t*_canonical   with t*_canonical = mellin_f_star_f0 = 0.08832"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "0.05"
  direction: "<"            # PASS iff relative deviation < 5% (RATIO tolerance, W0-9)

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: false
  proof_ref: "null"        # t*_predicted is a numerical trace-log extraction on the 78,080-eigenvalue spectrum; the 5% PASS-band is a RATIO-class tolerance pin (per W0-9 RATIO=0.5%/ABSOLUTE=5% calibration; this gate uses the looser 5% because the operationalization carries an O(few%) scheme-gap per kaku §V.1), NOT an analytically-reachable boundary

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous"   # t*_predicted is a continuous functional of the spectrum; the admissible PASS region is the open interval (0.95·t*, 1.05·t*)

# (5) machinery_pin_map — every free parameter of producing_script, pinned
machinery_pin_map:
  N_eval: "78080"                       # eigenvalues at L_max=10 restriction of the L=12 cache (sectors p+q<=10; verified at plan-freeze)
  L_max: "10"                           # operational truncation; cache holds L=12, gate restricts to p+q<=10 (the canonical n_s/f* truncation)
  scan_range: "N/A"                     # single-τ-slice at τ_fold; no scan
  step_size: "N/A — deterministic single-slice evaluation"
  tolerance: "1e-12"                    # numerical convergence floor on the trace-log sum (float64; sum of 78,080 ln-terms)
  scheme: "SA"                          # spectral-action one-loop (Γ_1loop = ½ Tr ln(D²/Λ²))
  convention: "ONELOOP-TRACE-LOG-f0-MOMENT-CHANNEL"   # the f_0 Mellin-moment extraction channel (where mellin_f_star_f0 lives); NOT the additive-sum-ratio reading
  regulator_pin: "a_n^{zeta}"           # the one-loop trace-log ½ Tr ln(D²/Λ²) is the zeta/heat-kernel-log regulator class; tagged per regulator-pin-discipline.md (NEW Seeley-DeWitt-adjacent citation). The e^{-x} (Gaussian) term is the one-loop heat-kernel generator; the √x term is the tree bosonic spectral action. The f_0 moment of f* is regulator-sensitive (sharp-cutoff FORCES f_0=1/2 for √x; canonical_constants.py:538), so the regulator class is gate-relevant and explicitly pinned.
  random_seed: "N/A — deterministic"
  GPU_path: "numpy.linalg"              # the trace-log is a vector reduction Σ ln(x_k) over 78,080 scalars — NOT a matrix op; numpy reduction on cap-OMP8 is correct (no eigendecomposition needed; eigenvalues are PRE-CACHED). cap OMP_NUM_THREADS=8 before import numpy.
  CLASS: "FULL"                         # producing script computes the trace-log DIRECTLY on the cached full D_K spectrum (NOT via the SCHEMATIC _spectral_action_regulators.py multiplicity-Casimir analog). FULL-physical per substrate-first-canonical-sourcing.md §(iv). If the cross-check arm consumes the SCHEMATIC helper, that arm carries CLASS=SCHEMATIC + -SCHEMATIC suffix + tier_pin=TIER-2 SEPARATELY (see audit_discriminators).

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]
  operationalization_enumeration: >
    The map [one-loop trace-log] -> [e^{-x}-admixture coefficient] is NOT unique; the gate
    PRE-REGISTERS the PRIMARY operationalization and TWO diagnostics, and the agent reports
    which yields the PASS/FAIL verdict (NEUTRAL — no operationalization is iterated-to-PASS):
      (PRIMARY) f_0-Mellin-moment match: t*_predicted = [f_0 moment of the one-loop e^{-x}
        generator] / [f_0 moment of (tree √x + one-loop e^{-x})], evaluated in the s->0 Mellin
        channel where canonical mellin_f_star_f0 = 0.08832 is defined. This is the channel-
        consistent comparison (compares like-to-like with the canonical pin).
      (DIAG-1) additive-weight reading: t = Σe^{-x_k} / (Σ√x_k + Σe^{-x_k}). Plan-freeze OOM
        pre-flight returns ~0.001 (≈2 OOM below target) — this confirms the verdict is NOT
        pre-judged: the naive reading MISSES, so a PASS in the PRIMARY channel would be a
        genuine structural result, not an artifact. Reported as a diagnostic only.
      (DIAG-2) leading-log matching: extract the e^{-x} coefficient that reproduces the
        leading τ-derivative of Γ_tree + Γ_1loop at τ_fold. Reported as a diagnostic.
    The PRIMARY operationalization determines the verdict; DIAG-1/DIAG-2 are emitted in the
    npz sidecar for cross-domain interpretation. SCHEMATIC-helper cross-check (if run) is a
    SEPARATE convention-tagged arm and does NOT feed the canonical verdict line.

# (7) substitution_chain — MANDATORY ([CHAIN] trigger; magnitude + sign claim)
substitution_chain:
  required: true
  content: |
    Claim: "t*_predicted (the one-loop-forced e^{-x} admixture coefficient in the f_0 channel)
            equals the empirical t* = 0.08832 to within 5%."

    Step 1 — Definitions:
      f*(x)            = (1 − t*)·√x + t*·e^{-x},  with (1−t*)=0.9117, t*=0.08832
                         [canonical_constants.py:536-539; gate SPECTRAL-FUNCTIONAL-FIT-72 PASS 1.3e-14]
      t*_canonical     = mellin_f_star_f0 = 0.08832  [canonical_constants.py:539, S78 W2-D]
                         (t* IS the f_0 Mellin moment of the e^{-x} term — the admixture weight)
      x_k              = |λ_k|² / Λ²,  Λ = M_KK,  {λ_k} = D_K(τ_fold) spectrum, L_max=10 (78,080 modes)
                         [s84_spectrum_cache_L12_tau019.npz; min|λ|=0.82 ⇒ x_k>0 ∀k ⇒ ln(x_k) finite]
      Γ_1loop          = ½ Tr ln(D_K²/Λ²) = ½ Σ_k ln(x_k)   [§1.3a; S62 einstein-baptista one-loop form]
      χ_2 (tree, √x)   = Σ_k √x_k          [S77-lizzi: χ_2 IS the spectral action per mode with f(x)=√x]
      e^{-x} generator = the Gaussian heat-kernel regulator = the one-loop trace-log generator
                         [the e^{-x} term in f* carries the one-loop content; the √x term carries tree]

    Step 2 — Substitution (PRIMARY operationalization, f_0-moment channel; no simplification):
      The Mellin f_0 moment of a regulator term g is its s→0 spectral-zeta residue/value on {x_k}.
      Decompose f* into its tree (√x) and one-loop (e^{-x}) pieces; the empirical t* is the RATIO of
      the e^{-x}-piece f_0 moment to the total f_0 moment:
        t*_canonical  =  [f_0 moment of t*·e^{-x}] / [f_0 moment of f*]      (identity by construction)
      The CONJECTURE replaces the EMPIRICAL t* on the e^{-x} side with the coefficient FORCED by
      requiring the e^{-x} piece to carry exactly the one-loop content Γ_1loop:
        t*_predicted  =  [f_0 moment of (Γ_1loop-matched e^{-x} generator)] / [f_0 moment of (χ_2 tree + Γ_1loop one-loop)]
      evaluated on the SAME 78,080-mode spectrum {x_k}.

    Step 3 — Simplification (algebra; one step per line):
      = ratio_f0 := M_{f0}[oneloop] / ( M_{f0}[tree] + M_{f0}[oneloop] )     [f_0-channel ratio]
      = a continuous functional of {x_k}, dimensionless (Λ-cancels in the ratio; x_k dimensionless)
      The relative-deviation operator is then  R := |ratio_f0 − 0.08832| / 0.08832.

    Step 4 — Direction / sign read-off:
      sign_verdict keys on sign(ratio_f0 − 0.08832): the conjecture predicts ratio_f0 ≈ 0.08832
      (the one-loop content is a SMALL admixture, consistent with the empirical 0.088 «« 0.912 tree
      weight). PASS requires ratio_f0 > 0 AND R < 0.05. A wrong SIGN (ratio_f0 < 0, impossible for a
      moment ratio of positive generators) or ratio_f0 in the WRONG OOM (R > 0.30) ⇒ t* genuinely
      empirical. The DIAG-1 additive reading (~0.001) is the FALSE operationalization whose 2-OOM
      miss proves the PRIMARY channel test is non-trivial (verdict not pre-baked).

    Conclusion (NEUTRAL): if R < 0.05 in the PRIMARY f_0 channel, t* is one-loop-computable and the
      framework's free-parameter ledger drops to {τ, Λ, f₀, f₂, f₄} (kaku §V.1, §IV.2). If R > 0.30,
      t* is genuinely empirical (the framework's single empirical coupling survives). INFO (0.05–0.30)
      = right OOM, residual scheme-gap between the f_0-moment extraction and the n_s-fit definition of t*.
      The plan ASSERTS neither outcome; the substitution chain pins the comparison so the verdict cannot
      hinge on an unpinned operationalization.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"     # recently edited (S94); recompute at execution and log in first 20 stdout lines
  spectrum_cache:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"   # precomputed at plan-freeze (static)

# ---- Output artifacts (closure-verification checklist) ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w2_1_t_star_oneloop_origin.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w2_1_t_star_oneloop_origin.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-95/s95_w2_1_t_star_oneloop_origin.png"
    artifact_kind: "plot"
    optional: false                      # plot: t*_predicted (3 operationalizations) vs canonical t*=0.08832 band
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W2-1-T-STAR-ONELOOP-ORIGIN:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true      # [CHAIN] trigger with directional pre-registration ⇒ SIGN/MAGNITUDE/REGIME 3-tuple row REQUIRED
  wp_section:
    path: "sessions/archive/session-95/session-95-w2-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W2-1. S95-W2-1-T-STAR-ONELOOP-ORIGIN"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric (3 fields) — PRE-REGISTERED, NEUTRAL ----
PASS_meaning: >
  R = |t*_predicted − 0.08832|/0.08832 < 0.05 in the PRIMARY f_0-Mellin-moment channel. t* is the
  one-loop threshold coefficient, NOT an empirical fit: it is computable from the D_K spectrum.
  Solution-space consequence: the framework's free-parameter ledger drops the SINGLE empirical
  functional coupling, collapsing to {τ, Λ, f₀, f₂, f₄} (all geometric / UV-completion data).
  This is the strongest possible de-empiricization result for the one-functional master object —
  the regulator's one free coupling becomes spectrum-derived. (kaku §V.1, §IV.2, §IV.4(1).)
FAIL_meaning: >
  R > 0.30 OR a structurally impossible sign. t* is GENUINELY empirical — the framework retains
  exactly one empirical functional coupling, and the matrix-model-genre rigidity claim (kaku §II.1)
  is bounded: the field content is forced by the algebra, but the regulator's admixture weight is
  not forced by the spectrum. This CLOSES the "t* is one-loop" corridor and confirms CF-52's
  empirical-realization half is genuinely empirical (theorem layer valid, realization layer empirical).
  A clean, informative boundary — NOT an agent failure.
INFO_meaning: >
  0.05 ≤ R ≤ 0.30 (right order of magnitude, residual scheme-gap). t*_predicted reproduces the
  e^{-x} admixture to the right OOM but not to 5%, indicating the f_0-moment extraction and the
  n_s-fit definition of t* differ at the few-tens-of-percent scheme level. Maps to: the conjecture
  is structurally supported but not closed; a tighter operationalization (DIAG-2 leading-log, or a
  full Mellin-cone evaluator at the s-pole) is the forward gate. Also fires if the trace-log carries
  a regulator-class ambiguity > 20% (a_n^{zeta} vs a_n^{Pauli-Villars} spread), per the spectral-
  moment-ratio regulator-spread sibling discriminator.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-95/s95_w2_1_t_star_oneloop_origin.py"
    - "computations/session-95/s95_w2_1_t_star_oneloop_origin.npz"
    - "computations/session-95/s95_w2_1_t_star_oneloop_origin.png"
  estimated_time: "3-4 hours (spectrum cache exists; the trace-log is a single vector reduction over 78,080 pre-cached eigenvalues; the f_0-moment extraction + 2 diagnostics are closed-form on {x_k})"

substrate_framing: |
  GEOMETRIC. The arrow runs D_K eigenvalues → spectral-action functional → the regulator's admixture
  coefficient → the question of whether that coefficient is forced or free. The fabric's internal
  geometry at τ_fold IS the spectrum {λ_k}; the spectral action Tr f(D_K²/Λ²) reads that spectrum
  through the functional f. The √x channel is the TREE bosonic spectral action (the fabric's
  leading mode-energy); the e^{-x} channel is the ONE-LOOP heat-kernel dressing (the fabric's
  quantum back-reaction on itself). The conjecture: the relative weight of the one-loop dressing
  against the tree action is not a free dial tuned to match the CMB tilt n_s — it is FIXED by the
  spectrum itself, the way the one-loop effective action is fixed by the operator in any spectral
  theory. If true, the fabric has no empirical knob in its functional at all — every number in
  S[D_K(τ), f, Λ] traces to the one operator. Cross-domain (kaku): in the matrix-model/IKKT genre,
  an O(1) coupling that resists first-principles derivation usually signals integrated-out UV modes
  dressing the effective action (the α'-correction analog); the test is whether the substrate's t*
  is that dressing, made computable because the triple is FINITE.
```

---

## §W2-2. EXHAUSTION-FALSIFIER

```yaml
# ---- Identity (6 fields) ----
gate_id: "S95-W2-2-EXHAUSTION-FALSIFIER"
schema_version: "R3"
trigger: "[VERIFY-THEOREM]"   # structural exhaustion claim verified to machine-ε / symbolic closure, not a numerical threshold
classification: "GEOMETRIC"   # the spectral-triple's scalar/deformation content — the fabric's algebraic structure, not its excitations
agent_type: "kaku-speculative-theorist"   # structural-exhaustion / cross-domain (NCG one-functional genre; SFT-vertex-vs-inner-fluctuation correspondence is kaku's standing specialty)
hypothesis: "Every admissible associative deformation of the master action S[D_K] — equivalently, every candidate *-product / cubic interaction term on the algebra A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) — is reducible to an inner fluctuation D_K ↦ D_K + A + ε'JAJ⁻¹ (A = Σ aᵢ[D_K, bᵢ]). There is NO interaction term outside the inner-fluctuation orbit: trace + inner product EXHAUST the natural scalars of the finite spectral triple (§1.1, last bullet)."

method:
  description: >
    Verify the §1.1 completeness-by-exhaustion claim adversarially. (i) Enumerate the natural
    scalar functionals of the finite spectral triple (A_K, H_K, D_K): the bosonic trace
    Tr f(D_K²/Λ²) and the fermionic inner product ⟨Jψ̃|D_K|ψ̃⟩ are the two Connes-NCG canonical
    scalars. (ii) Construct the inner-fluctuation one-form module Ω¹_D = {A = Σ aᵢ[D_K, bᵢ] :
    aᵢ, bᵢ ∈ A_K} and its real-structure completion A + ε'JAJ⁻¹ (the orbit of D_K under inner
    automorphisms). (iii) For each candidate associative deformation class — (a) a Witten-style
    mid-point *-product on A_K, (b) a generic Hochschild 2-cochain deformation of the product on
    A_K, (c) a non-inner first-order differential-operator perturbation of D_K — test via Sage-MCP
    symbolic algebra whether it is reducible to an element of Ω¹_D ⊕ JΩ¹_D, OR exhibits a residual
    NOT in the inner-fluctuation orbit. (iv) The decisive structural lever: on a FINITE triple with
    A_K a sum of matrix algebras, the first Hochschild cohomology HH¹(A_K, A_K) is the obstruction
    to all derivations being inner; A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) is a sum of SEPARABLE (matrix / division)
    algebras, every derivation of which is INNER (Whitehead's lemma / HH¹ = 0 for semisimple
    finite-dim algebras). Verify HH¹(A_K, A_K) = 0 explicitly (Sage), which forces every associative
    first-order deformation into the inner-fluctuation orbit. Report PASS (exhaustion holds — no
    non-reducible *-product) or FAIL (a non-reducible associative deformation exists).
  producing_script: "computations/session-95/s95_w2_2_exhaustion_falsifier.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set"
  form: "{ admissible associative deformations of S[D_K] } ⊆ { inner fluctuations D_K ↦ D_K + A + ε'JAJ⁻¹ } ?  AND  dim HH¹(A_K, A_K) = 0 ?"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "dim HH¹(A_K, A_K) = 0  AND  residual_outside_orbit = 0 (machine-ε / symbolic-exact) for all 3 candidate deformation classes (a),(b),(c)"
  direction: "="            # exact: exhaustion holds iff the cohomological obstruction vanishes AND no candidate exhibits an out-of-orbit residual

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "Whitehead's lemma / HH¹(semisimple finite-dim algebra)=0; verified symbolically via Sage-MCP for A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) — every derivation of a finite-dim semisimple algebra over a field of char 0 is inner. The orbit-reducibility of each candidate class is a symbolic algebra identity (Sage), not a numerical estimate."

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "discrete — HH¹ dimension is a non-negative integer (target 0); the deformation classes (a),(b),(c) are a finite enumeration, each with a symbolic-exact reducible/non-reducible verdict"

# (5) machinery_pin_map — every free parameter of producing_script, pinned
machinery_pin_map:
  N_eval: "3"                           # three candidate associative-deformation classes (a) Witten-*-product, (b) Hochschild 2-cochain, (c) non-inner 1st-order D_K perturbation
  L_max: "N/A"                          # structural/cohomological — operates on A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) (the FIXED finite algebra), NOT a spectral truncation; HH¹ is L_max-independent (algebra-level invariant)
  scan_range: "N/A"                     # no scan; finite enumeration of deformation classes
  step_size: "N/A — symbolic"
  tolerance: "1e-15"                    # machine-ε for the symbolic-numeric cross-check of orbit-residuals (Sage exact preferred; float64 fallback floor)
  scheme: "SA"                          # spectral-action / NCG-axiomatic (the 7 Connes axioms + inner-fluctuation construction)
  convention: "INNER-FLUCTUATION-ORBIT-HH1-OBSTRUCTION"   # exhaustion = (HH¹=0) ⇒ all derivations inner ⇒ all associative deformations in the orbit
  regulator_pin: "N/A — cohomological"  # HH¹(A_K,A_K) and orbit-reducibility are regulator-INDEPENDENT (algebra-level; no Seeley-DeWitt coefficient is cited — no a_n^{regulator} tag needed). The trace Tr f(D²/Λ²) appears only as the functional whose deformations are enumerated; its regulator class does not enter the exhaustion verdict.
  random_seed: "N/A — deterministic / symbolic"
  GPU_path: "numpy.linalg"              # any numeric cross-check (representing A_K generators as small matrices ℂ⊕ℍ⊕M₃(ℂ), max 3×3 blocks) is tiny — CPU; primary route is Sage-MCP symbolic. cap OMP_NUM_THREADS=8.
  sage_mcp: "true"                      # Sage-MCP sage_eval/sage_simplify carries the symbolic HH¹ computation + orbit-reducibility identities

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]
  structural_witness: >
    The decisive structural object is dim HH¹(A_K, A_K) for A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ). HH¹(A,A)=0 for
    every finite-dimensional semisimple algebra over a char-0 field (Whitehead). The audit verifies
    BOTH (i) the cohomological obstruction vanishes (HH¹=0 ⇒ all derivations inner ⇒ all first-order
    associative deformations reducible to inner fluctuations) AND (ii) each of the 3 candidate classes
    (a Witten-*-product, a generic Hochschild 2-cochain, a non-inner 1st-order D_K perturbation) is
    checked for an out-of-orbit residual. The two arms are independent: (i) is the general theorem,
    (ii) is the per-candidate constructive check. A FAIL requires EITHER HH¹≠0 OR a constructed
    non-reducible residual — both routes are reported. Cross-domain anchor (kaku): this is the
    substrate's analog of "no Witten-*-product vertex exists outside the inner-fluctuation
    interaction content" — the SFT cubic vertex requires a CHOICE (mid-point *, light-cone, Zwiebach
    polyhedral); the substrate's interaction is FORCED, so the falsifier asks whether any such CHOICE
    survives as a genuine new term.

# (7) substitution_chain — structural (no sign/magnitude numerical claim; the [VERIFY-THEOREM] structural chain)
substitution_chain:
  required: true
  content: |
    Claim: "Trace + inner product exhaust the scalars of (A_K, H_K, D_K); equivalently every
            associative deformation of S is an inner fluctuation; equivalently HH¹(A_K, A_K) = 0."

    Step 1 — Definitions:
      A_K              = ℂ ⊕ ℍ ⊕ M₃(ℂ)   [the finite spectral-triple algebra; canonical, §1.1/§1.2]
      Inner fluctuation: D_K ↦ D_K + A + ε'JAJ⁻¹,  A = Σ aᵢ[D_K, bᵢ],  aᵢ,bᵢ ∈ A_K
                         [Connes inner-fluctuation construction; the gauge/Higgs content of §1.1]
      Derivation δ of A_K: linear δ:A_K→A_K with δ(ab)=δ(a)b+aδ(b)
      Inner derivation: δ_c(a) = [c,a] for some c ∈ A_K
      HH¹(A_K,A_K)     = (derivations)/(inner derivations) = obstruction to all derivations being inner

    Step 2 — Substitution (structural reduction):
      A first-order associative deformation of the product on A_K is classified by a Hochschild
      2-cochain; its integrability/triviality is governed by HH²(A_K,A_K), and the induced
      derivation-level perturbations by HH¹(A_K,A_K). For the spectral-action functional, a
      deformation of S that changes the INTERACTION content (beyond a field redefinition) must act
      through a derivation of A_K or a new product structure. Substituting A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ):
        ℂ, ℍ (=quaternions, a division algebra), M₃(ℂ) are each finite-dim semisimple over ℝ/ℂ.
        A direct sum of semisimple algebras is semisimple.

    Step 3 — Simplification (cohomological algebra; one step per line):
      = HH¹(B,B) = 0 for any finite-dim semisimple B over a char-0 field   [Whitehead's first lemma]
      = HH¹(ℂ⊕ℍ⊕M₃(ℂ), ·) = HH¹(ℂ,·) ⊕ HH¹(ℍ,·) ⊕ HH¹(M₃(ℂ),·) = 0 ⊕ 0 ⊕ 0 = 0   [additivity on the sum]
      ⇒ every derivation of A_K is inner
      ⇒ every first-order associative deformation acting through a derivation is an inner perturbation
      ⇒ (combined with the per-candidate orbit-reducibility checks (a),(b),(c)) every admissible
        deformation of S is reducible to an inner fluctuation D_K ↦ D_K + A + ε'JAJ⁻¹.

    Step 4 — Direction / verdict read-off:
      The verdict is EXACT (symbolic), not a threshold. Exhaustion HOLDS (PASS) iff dim HH¹(A_K,A_K)=0
      AND no candidate class (a),(b),(c) exhibits an out-of-orbit residual. Exhaustion FAILS iff
      EITHER dim HH¹(A_K,A_K) > 0 (a non-inner derivation exists ⇒ a genuine new interaction direction)
      OR a constructed associative deformation has a residual provably NOT in Ω¹_D ⊕ JΩ¹_D.

    Conclusion (NEUTRAL): the plan does NOT assume exhaustion holds. It is structurally EXPECTED
      (Whitehead ⇒ HH¹=0 for semisimple A_K), but the gate is a genuine adversarial test: a FAIL
      (a non-reducible *-product) would falsify the §1.1 "no room for a third term" claim and would
      be a major structural result (the substrate would, after all, admit a stringy-vertex-like
      independent interaction term). The structural expectation does NOT pre-bake the verdict —
      the per-candidate constructive checks (a),(b),(c) can independently surface an out-of-orbit
      residual even when HH¹=0 (e.g. a non-derivation-mediated deformation), and those are computed.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"     # used only for A_K dimension cross-checks / J-operator conventions; recompute at runtime
  # No spectrum cache needed — this gate is algebra-level (A_K is fixed; HH¹ is L_max-independent).
  # Sage-MCP supplies the symbolic engine; no external data file is read.

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w2_2_exhaustion_falsifier.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w2_2_exhaustion_falsifier.npz"
    artifact_kind: "data"
    optional: false                      # stores HH¹ dim per summand + per-candidate orbit-residual verdicts
  plot:
    path: "computations/session-95/s95_w2_2_exhaustion_falsifier.png"
    artifact_kind: "plot"
    optional: true                       # structural/cohomological result — a table-figure (HH¹ per summand + 3-class verdict matrix); set optional (no continuous curve to plot)
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W2-2-EXHAUSTION-FALSIFIER:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false     # [VERIFY-THEOREM] structural — no directional/sign pre-registration; no 3-tuple row
  wp_section:
    path: "sessions/archive/session-95/session-95-w2-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W2-2. S95-W2-2-EXHAUSTION-FALSIFIER"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric (3 fields) — PRE-REGISTERED, NEUTRAL ----
PASS_meaning: >
  dim HH¹(A_K, A_K) = 0 AND all 3 candidate deformation classes are inner-fluctuation-reducible
  (no out-of-orbit residual). The §1.1 completeness-by-exhaustion claim is VERIFIED: trace + inner
  product exhaust the scalars; there is no room for a third term. Solution-space consequence: the
  matrix-model-genre rigidity claim (kaku §II.2) is structurally confirmed — the substrate's
  interactions are FORCED (inner fluctuations), not ADDED (a chosen cubic vertex), and this is
  structurally STRONGER than SFT, whose vertex requires a choice. Registers a structural FALSIFIER:
  any future claim of a non-inner associative deformation must FAIL against this verdict.
FAIL_meaning: >
  dim HH¹(A_K, A_K) > 0 OR a constructed associative deformation has a residual provably outside
  Ω¹_D ⊕ JΩ¹_D. The §1.1 "no room for a third term" claim is FALSIFIED — the substrate admits a
  genuine new interaction direction analogous to a stringy *-product vertex. Solution-space
  consequence: the one-functional master object is NOT complete; a third term (beyond trace + inner
  product) is admissible, and the free-functional content must be re-counted. Highly consequential
  and informative — would reopen the genre question (the substrate would have an SFT-like
  vertex-choice freedom after all).
INFO_meaning: >
  Ambiguous structural verdict: e.g. HH¹(A_K,A_K)=0 (derivation-level exhaustion holds) but a
  candidate class (a),(b),(c) is reducible only under an additional admissibility assumption (a
  representation-theoretic constraint on which deformations count as "physical"), so the exhaustion
  is conditional. Maps to: the exhaustion claim holds at the cohomological-obstruction level but the
  set of "admissible" deformations needs a sharper definition; the forward gate is to pin the
  admissibility criterion (e.g. order-one + first-order + real-structure-compatible) and re-test.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-95/s95_w2_2_exhaustion_falsifier.py"
    - "computations/session-95/s95_w2_2_exhaustion_falsifier.npz"
  estimated_time: "1 session, ~4-6 hours (NCG-axiomatic / cohomological; Sage-MCP for the HH¹ computation per summand + the 3-class orbit-reducibility identities; largely symbolic — the 'compute' is algebra verification, not a numerical sweep)"

substrate_framing: |
  GEOMETRIC. The arrow runs D_K (the fabric's internal operator) → its algebra A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)
  (the fabric's symmetry content) → the question of whether the fabric's interactions are exhausted.
  Inner fluctuations D_K ↦ D_K + A + ε'JAJ⁻¹ ARE the gauge fields and Higgs of the substrate — they
  are not added by hand, they are the ways the one operator can be tilted by the algebra. The
  exhaustion claim is the statement that the fabric has NO OTHER way to interact: every conceivable
  new interaction term is already one of these tilts. Structurally this is the substrate's deepest
  rigidity — and it is a property of the fabric's algebra being a sum of matrix algebras (semisimple),
  for which every derivation is inner (Whitehead). Cross-domain (kaku): a string would have a choice
  of interaction vertex (Witten mid-point, light-cone, Zwiebach); the drumhead-substrate has exactly
  one way to be perturbed, because its algebra has no outer derivations. The picture: you cannot
  invent a new way to strike the drum that is not already a combination of the strikes the algebra
  permits — and proving that is proving HH¹(A_K) = 0. If you CAN (FAIL), the substrate is secretly
  more string-like than claimed.
```

---

## §W2-3. NO-WELL-ONE-LOOP

```yaml
# ---- Identity (6 fields) ----
gate_id: "S95-W2-3-NO-WELL-ONE-LOOP"
schema_version: "R3"
trigger: "[SIGN]"             # the gate's primary content is the SIGN of dΓ/dτ across τ ∈ [0, τ_now]; substitution chain MANDATORY
classification: "GEOMETRIC"   # the effective action Γ[τ] = S[D_K(τ)] + Γ_1loop(τ) on the τ-modulus — the fabric's deformation potential, not its excitations
agent_type: "spectral-geometer"   # one-loop spectral effective action + monotonicity of a τ-trajectory functional on the D_K spectrum (heat-kernel / Seeley-DeWitt specialty)
hypothesis: "The tree-level no-interior-saddle result (E7 Structural Monotonicity Theorem: dS/dτ > 0, no stationary point for any monotone f) survives at one loop: Γ[τ] = S[D_K(τ)] + ½ Tr ln(D_K(τ)²/Λ²) has dΓ/dτ of FIXED sign (no interior extremum) over τ ∈ [0, τ_now]. The one-loop term introduces NO interior stationary feature absent at tree level."

method:
  description: >
    Construct the one-loop-corrected effective action Γ(τ) = S[D_K(τ)] + Γ_1loop(τ) on a τ-grid
    spanning [0, τ_now]. S[D_K(τ)] is the tree spectral action (E7 baseline, monotone). Γ_1loop(τ)
    = ½ Σ_k ln(λ_k(τ)²/Λ²) is the one-loop trace-log. The D_K(τ) spectrum at the τ_fold slice is
    in the L=12 cache; at other τ the spectrum is obtained by the Jensen-deformation scaling of the
    cached eigenvalues (λ_k(τ) = λ_k(τ_fold)·r(τ_fold)/r(τ), the Casimir-scaling relation |λ|_min^(p,q)(τ)
    ≈ √C_2(p,q)/r(τ) used framework-wide; producing agent uses the canonical r(τ) closed form from
    E3/the Jensen flow). Compute dΓ/dτ on the grid via finite differences (and analytically where the
    closed form of dΓ_1loop/dτ = ½ Σ_k 2 (dλ_k/dτ)/λ_k = Σ_k (d ln λ_k/dτ) is available). Test whether
    sign(dΓ/dτ) is CONSTANT over the full grid (no interior zero ⇒ no extremum) or changes sign (an
    interior stationary point ⇒ a one-loop-induced well/barrier). State the regime of validity of the
    monotone-ramp picture explicitly (the one-loop trace-log is the leading quantum correction; higher
    loops not included).
  producing_script: "computations/session-95/s95_w2_3_no_well_one_loop.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set"
  form: "{ τ ∈ [0, τ_now] : dΓ/dτ(τ) = 0 } = ∅ ?   (equivalently sign(dΓ/dτ) constant over the grid)"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "N_interior_sign_changes = 0  (no interior zero of dΓ/dτ on the τ-grid over [0, τ_now])"
  direction: "="            # PASS iff the count of interior sign changes of dΓ/dτ equals 0

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "Tree term: E7 / W7/S37 Structural Monotonicity Theorem — dS/dτ>0, no stationary point, 9,600/9,600 checks (PROVEN; analytic). One-loop term: dΓ_1loop/dτ = Σ_k d ln λ_k(τ)/dτ; with λ_k(τ) monotone in τ (each |λ|^(p,q)(τ) ∝ 1/r(τ) and r(τ) monotone from the Jensen flow), each d ln λ_k/dτ has the SAME sign ⇒ Γ_1loop is itself monotone ⇒ Γ = S + Γ_1loop is a sum of two monotone-same-sign terms. The analytic expectation is therefore no interior extremum; the gate VERIFIES this numerically over [0, τ_now] and checks the sign agreement."

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "N_interior_sign_changes is a non-negative integer (target 0); the τ-grid is a discrete mesh of >=200 points over [0, τ_now]"

# (5) machinery_pin_map — every free parameter of producing_script, pinned
machinery_pin_map:
  N_eval: "78080"                       # eigenvalues per τ-slice (L_max=10 restriction of the L=12 cache)
  L_max: "10"                           # operational truncation (Casimir-bound feasible; bottom-spectrum monotonicity is L_max-saturated per Friedrich-Bär, math-scripts.md §"D_K Block-Diagonality")
  scan_range: "[0.0, 0.6]"              # τ ∈ [0, τ_now]; τ_now upper bound 0.6 (well past τ_fold=0.19; the framework's τ_now plateau; agent pins τ_now from canonical if a tighter value exists, else 0.6 covers [0, τ_now])
  step_size: "0.003"                    # τ-grid step ⇒ 200 points over [0, 0.6]; finite-difference dΓ/dτ
  tolerance: "1e-10"                    # zero-detection tolerance on dΓ/dτ sign changes (a sign change counts only if |dΓ/dτ| crosses through < -tol to > +tol or vice versa, to reject float-noise zero-crossings)
  scheme: "SA"                          # spectral-action one-loop (Γ = S_tree + ½ Tr ln(D²/Λ²))
  convention: "EFFECTIVE-ACTION-MONOTONICITY-TREE-PLUS-ONELOOP"   # Γ = S[D_K(τ)] + Γ_1loop(τ); sign of dΓ/dτ over [0, τ_now]
  regulator_pin: "a_n^{zeta}"           # the one-loop trace-log ½ Tr ln(D²/Λ²) is the zeta/heat-kernel-log regulator class; NEW Seeley-DeWitt-adjacent citation ⇒ tagged per regulator-pin-discipline.md. The tree S uses the E7 monotone-f baseline (regulator-INVARIANT: E7 holds for ALL monotone f); the one-loop log is specifically zeta-class and gate-relevant (a Pauli-Villars one-loop would subtract a massive-regulator log — reported as a regulator-spread cross-check, not the canonical verdict).
  random_seed: "N/A — deterministic"
  GPU_path: "numpy.linalg"              # per-τ trace-log is a vector reduction over 78,080 pre-cached (Jensen-scaled) eigenvalues × 200 τ-points = 1.56e7 ln-evaluations — a CPU vector op, not a matrix op (eigenvalues pre-cached); cap OMP_NUM_THREADS=8.
  CLASS: "FULL"                         # trace-log on the FULL cached D_K spectrum (Jensen-scaled per τ), NOT the SCHEMATIC _spectral_action_regulators.py analog. FULL-physical per substrate-first-canonical-sourcing.md §(iv).

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]
  regime_of_validity_declaration: >
    The no-well-one-loop claim is a ONE-LOOP statement (leading quantum correction to the tree
    spectral action). The regime_verdict 3-tuple field MUST be set: VALID if the one-loop trace-log
    is the dominant quantum correction across [0, τ_now] (the framework's working assumption);
    MARGINAL/BREAKDOWN if the τ-grid enters a region where the Jensen-scaling eigenvalue model breaks
    (e.g. λ_k → 0 ⇒ ln divergence; min|λ|=0.82 at τ_fold but check the full grid). The Jensen-scaling
    of the cached spectrum is itself a regime assumption (exact only for the bottom-Casimir sectors;
    Friedrich-Bär-saturated at L=10) — declared as the auto-shortening axis. Cross-check arm: recompute
    dΓ_1loop/dτ analytically (Σ_k d ln λ_k/dτ) and confirm sign agreement with the finite-difference
    grid (an INDEPENDENT route to the same sign, not a self-consistency loop).

# (7) substitution_chain — MANDATORY ([SIGN] trigger; sign of dΓ/dτ)
substitution_chain:
  required: true
  content: |
    Claim: "dΓ/dτ retains a FIXED sign over τ ∈ [0, τ_now] — the one-loop correction introduces no
            interior stationary point absent at tree level."

    Step 1 — Definitions:
      S[D_K(τ)]        = tree spectral action; dS/dτ > 0 ∀τ, no interior stationary point
                         [E7 / W7/S37 Structural Monotonicity Theorem, PROVEN, 9,600/9,600 checks;
                          S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD FAIL value=−2.04e4 confirms
                          τ_fold is NOT a stationary point of bare S]
      Γ_1loop(τ)       = ½ Tr ln(D_K(τ)²/Λ²) = ½ Σ_k ln(λ_k(τ)²/Λ²) = Σ_k ln(|λ_k(τ)|/Λ)
                         [§1.3a; S62-einstein-baptista one-loop spectral-action correction]
      λ_k(τ)           = D_K(τ) eigenvalues; |λ_k|^(p,q)(τ) ∝ 1/r(τ), r(τ) the Jensen radius (monotone)
      Γ[τ]             = S[D_K(τ)] + Γ_1loop(τ)   [tree + one-loop effective action]

    Step 2 — Substitution (plug definitions into dΓ/dτ; no simplification):
      dΓ/dτ = dS/dτ + dΓ_1loop/dτ
            = dS/dτ + d/dτ [ Σ_k ln(|λ_k(τ)|/Λ) ]
            = dS/dτ + Σ_k (1/λ_k(τ)) (dλ_k/dτ)
            = dS/dτ + Σ_k d(ln|λ_k(τ)|)/dτ

    Step 3 — Simplification (algebra; one step per line):
      dλ_k/dτ : since |λ_k(τ)| ∝ 1/r(τ),  d ln|λ_k|/dτ = − d ln r(τ)/dτ  (SAME for every k — a
                global factor; r(τ) is the single Jensen radius)
      ⇒ Σ_k d ln|λ_k|/dτ = N_eval · (− d ln r/dτ)     [N_eval = 78,080; one common sign]
      ⇒ dΓ/dτ = dS/dτ  +  N_eval·(− d ln r/dτ)
      Both terms are evaluated against r(τ) monotone (E7 ⇒ dS/dτ > 0; − d ln r/dτ has a fixed sign
      because r(τ) is strictly monotone with no turning point on [0, τ_now]).

    Step 4 — Direction / sign read-off:
      dS/dτ > 0 (E7, fixed sign). The one-loop term N_eval·(−d ln r/dτ) has a fixed sign (r monotone).
      IF the two terms share sign ⇒ dΓ/dτ fixed sign ⇒ NO interior extremum ⇒ PASS.
      IF they have OPPOSITE signs ⇒ there COULD be an interior zero where the one-loop term cancels
      the tree term ⇒ the gate must compute whether the MAGNITUDE of the one-loop term ever exceeds
      the tree term on [0, τ_now] (a genuine interior well). This is the substantive numerical
      content — the SIGN claim is NOT assumed; it is the gate's measured output. (Note: dS/dτ at the
      fold is +58,672.8, very large; N_eval·|d ln r/dτ| must be compared against it — the pre-flight
      expectation is that the tree term dominates, giving PASS, but the gate VERIFIES this rather than
      asserting it.)

    Conclusion (NEUTRAL): the plan does NOT assume the one-loop term preserves monotonicity. PASS
      (no interior zero) confirms the monotone-ramp / no-landscape / no-stabilizing-well picture is
      one-loop-robust (einstein §II.2, kaku §II.3 — "no landscape AND no well are two faces of E7").
      FAIL (an interior zero ⇒ a one-loop-induced well) is consequential: it would mean the substrate
      DOES have a one-loop stabilization feature, reopening the cosmogenesis-as-transit vs settling
      question. The sign is the gate's OUTPUT.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"     # imports tau_fold, M_KK, dS_fold, and the Jensen r(τ) parameters; recompute at runtime
  spectrum_cache:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"   # precomputed at plan-freeze (static); the τ_fold-slice spectrum, Jensen-scaled across the τ-grid

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-95/s95_w2_3_no_well_one_loop.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-95/s95_w2_3_no_well_one_loop.npz"
    artifact_kind: "data"
    optional: false                      # stores τ-grid, S(τ), Γ_1loop(τ), Γ(τ), dΓ/dτ, sign-change count, regime flags
  plot:
    path: "computations/session-95/s95_w2_3_no_well_one_loop.png"
    artifact_kind: "plot"
    optional: false                      # plot Γ(τ), S(τ), Γ_1loop(τ) and dΓ/dτ over [0, τ_now]; mark any interior zero
  verdict_line:
    path: "computations/session-95/s95_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S95-W2-3-NO-WELL-ONE-LOOP:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true      # [SIGN] trigger ⇒ SIGN/MAGNITUDE/REGIME 3-tuple companion row REQUIRED (regime_verdict carries the one-loop regime-of-validity)
  wp_section:
    path: "sessions/archive/session-95/session-95-w2-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W2-3. S95-W2-3-NO-WELL-ONE-LOOP"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric (3 fields) — PRE-REGISTERED, NEUTRAL ----
PASS_meaning: >
  N_interior_sign_changes of dΓ/dτ = 0 over [0, τ_now] (regime VALID). The tree-level no-interior-
  saddle result (E7) is ONE-LOOP-ROBUST: Γ = S + ½ Tr ln(D²/Λ²) is monotone with no interior
  stationary point. Solution-space consequence: the monotone-ramp cosmogenesis (transit, not
  settling) and its two structural corollaries — NO landscape, NO stabilizing well (einstein §II.2,
  kaku §II.3, two faces of E7) — survive the leading quantum correction. The "the universe transits
  rather than settles" picture is not a tree-level artifact. Strengthens the §1.3a boundary-domination
  reading from a tree statement to a one-loop statement.
FAIL_meaning: >
  N_interior_sign_changes >= 1 (a genuine interior zero of dΓ/dτ, regime VALID). The one-loop trace-log
  creates an interior stationary feature (well or barrier) absent at tree level. Solution-space
  consequence: the no-well claim is one-loop-FRAGILE — the substrate DOES acquire a one-loop
  stabilization feature, which would reopen the cosmogenesis question (settling into a one-loop well
  becomes possible) and would qualify the "no landscape" contrast with string theory. Consequential and
  informative: it would localize a specific τ where the one-loop term overtakes the tree gradient.
INFO_meaning: >
  Either (a) an apparent interior sign change appears but only in a regime where regime_verdict =
  MARGINAL/BREAKDOWN (the Jensen-scaling eigenvalue model or the one-loop-dominance assumption breaks
  on part of the grid — e.g. domain_used_frac < 0.95), so the feature is not a trustworthy substrate
  result; OR (b) the tree and one-loop terms have opposite sign and comparable magnitude only at the
  τ=0 boundary (not an interior extremum), making the interior-saddle question boundary-sensitive. Maps
  to: the no-well result holds in the trustworthy regime but the one-loop correction needs a wider /
  higher-L_max evaluation (or a Pauli-Villars cross-check) to settle the boundary behavior. Per the
  auto-shortening clause (gate-verdicts.md), domain_used_frac is emitted and the regime band sets the
  composite collapse.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-95/s95_w2_3_no_well_one_loop.py"
    - "computations/session-95/s95_w2_3_no_well_one_loop.npz"
    - "computations/session-95/s95_w2_3_no_well_one_loop.png"
  estimated_time: "1 session, ~2-3 hours (trace-log derivative on the existing spectrum cache, Jensen-scaled across a 200-point τ-grid; finite-difference + analytic dΓ_1loop/dτ cross-check)"

substrate_framing: |
  GEOMETRIC. The arrow runs D_K eigenvalues {λ_k(τ)} → the tree spectral action S(τ) (the fabric's
  deformation energy) + the one-loop trace-log Γ_1loop(τ) (the fabric's quantum self-correction) →
  the sign of dΓ/dτ → whether the fabric's deformation has an interior resting point. The Jensen
  parameter τ is the fabric's single tightening knob; E7 says the TREE energy climbs monotonically
  with no resting point — the drumhead has no comfortable tension to settle into, so it is SWEPT
  through the fold (transit, not slow-roll). This gate asks whether the QUANTUM correction (the
  one-loop dressing) digs a dimple in that otherwise-monotone ramp. The picture: the one-loop term is
  N_eval copies of a common −d ln r/dτ (every mode scales with the one radius r(τ)), so it is itself
  monotone; the only way it could create an interior well is if its monotone pull OPPOSES the tree
  climb AND overtakes it somewhere in [0, τ_now]. At the fold the tree gradient is enormous (+58,672.8),
  so the pre-flight expectation is that the climb wins and the ramp stays monotone — but the gate
  MEASURES this, it does not assume it (einstein §II.2 explicitly flags the no-well result as a
  tree-level claim whose one-loop survival is a SEPARATE, defensible statement). If the dimple appears
  (FAIL), the substrate acquires a one-loop place to settle, and the "no landscape, no well" twin
  corollary of E7 is qualified at one loop.
```

---

## Wave 2 → Wave 3 Decision Point

Wave 2 does NOT feed any Wave-3 gate as a hard prerequisite (W3 = the a(t)-bridge cluster EIN-V1/EIN-V2/KAK-V3/transit-V5/HAW-V4, which consume the §6.3 effective-Friedmann object, not the one-loop completeness results). The W2 verdicts inform downstream interpretation but do not gate W3 dispatch. Branching for the doc-integration `/rclab-workshop` track (context §D), which runs AFTER W2/W4/W5/W6:

- **§W2-1 PASS** (`R < 0.05`): t* is one-loop-derived. Doc-integration drops `t*` from the `phonic-exflation-equation.md §3`/§8.4 free-parameter ledger → `{τ, Λ, f₀, f₂, f₄}`; the master-equation "single empirical coupling" framing is REPLACED by "zero empirical functional couplings." Update kaku-collab Summary-Table row #7 (CONJECTURE → CONFIRMED). HIGH-LEVERAGE per context §B.
- **§W2-1 FAIL** (`R > 0.30`): t* genuinely empirical. Doc-integration RETAINS the `+ t*` ledger entry and adds a sentence pinning t* as the irreducible empirical functional coupling (the framework's `Λ_QCD` analog, kaku §IV.4(1)); CF-52 empirical-realization half confirmed empirical.
- **§W2-1 INFO** (`0.05 ≤ R ≤ 0.30`): right OOM, scheme-gap. Forward carry-forward to S96: a tighter operationalization (full Mellin-cone evaluator at the s-pole, or DIAG-2 leading-log matching) as `CF-S96-T-STAR-ONELOOP-SCHEME-TIGHTEN`; ledger annotation deferred.
- **§W2-2 PASS**: exhaustion verified. Register the structural FALSIFIER in `permanent-results-registry.md` (any future non-inner associative deformation must FAIL this verdict; kaku §V.2); doc-integration adds the matrix-model-genre rigidity claim to §1.1.
- **§W2-2 FAIL**: a non-inner deformation exists. MAJOR — reopens the genre question; route to a dedicated S96 workshop (the substrate admits an SFT-like vertex-choice freedom).
- **§W2-3 PASS**: no-well is one-loop-robust. Strengthen the §1.3a / E7 registry note from "tree-level" to "one-loop-robust"; einstein §V.3 closed.
- **§W2-3 FAIL**: one-loop well exists. Consequential — route to S96 for the cosmogenesis-settling re-examination + qualify the "no landscape" string contrast.

Wave-internal independence: §W2-1, §W2-2, §W2-3 are mutually independent (no shared intermediate; the two trace-log gates W2-1/W2-3 share the spectrum cache as a read-only input but compute distinct functionals — an f_0-moment ratio vs a τ-derivative sign — so they are dispatchable in parallel).

## Wave 2 Machinery-Enumeration Pin

Aggregate of all gate `machinery_pin_map` entries in Wave 2 (per `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"` PRDR; consumed by `_yaml_gate_validator.py` for sig_4):

| Gate | N_eval | L_max | scan_range | step | tolerance | scheme | convention | regulator_pin | seed | GPU/CLASS |
|:-----|:-------|:------|:-----------|:-----|:----------|:-------|:-----------|:--------------|:-----|:----------|
| S95-W2-1-T-STAR-ONELOOP-ORIGIN | 78080 | 10 | N/A | N/A | 1e-12 | SA | ONELOOP-TRACE-LOG-f0-MOMENT-CHANNEL | a_n^{zeta} | deterministic | numpy / FULL |
| S95-W2-2-EXHAUSTION-FALSIFIER | 3 | N/A | N/A | N/A | 1e-15 | SA | INNER-FLUCTUATION-ORBIT-HH1-OBSTRUCTION | N/A (cohomological) | deterministic / symbolic | numpy+Sage / N/A |
| S95-W2-3-NO-WELL-ONE-LOOP | 78080 | 10 | [0.0, 0.6] | 0.003 | 1e-10 | SA | EFFECTIVE-ACTION-MONOTONICITY-TREE-PLUS-ONELOOP | a_n^{zeta} | deterministic | numpy / FULL |

PRDR notes:
- **Regulator-pin discipline** (`regulator-pin-discipline.md`): W2-1 and W2-3 both cite the one-loop trace-log `½ Tr ln(D²/Λ²)`, a NEW Seeley-DeWitt-adjacent citation tagged `a_n^{zeta}` (the zeta/heat-kernel-log regulator class). The e^{-x} (Gaussian) term in f* is the one-loop heat-kernel generator; the √x term is the tree bosonic action. The f_0 moment of f* is regulator-sensitive (sharp-cutoff forces f_0=1/2 for √x — `canonical_constants.py:538`), so the regulator class is gate-relevant and explicitly pinned, NOT bare. A Pauli-Villars one-loop cross-check (`a_n^{Pauli-Villars}`) is the regulator-spread sibling discriminator (reported, not the canonical verdict). W2-2 is cohomological (HH¹ is regulator-INVARIANT — no a_n citation, no tag needed).
- **SCHEMATIC vs FULL level-pin** (`substrate-first-canonical-sourcing.md §(iv)`, K=4 MANDATORY): W2-1 and W2-3 compute the trace-log DIRECTLY on the cached FULL D_K spectrum (CLASS=FULL); they do NOT consume the SCHEMATIC `_spectral_action_regulators.py` multiplicity-Casimir analog for the canonical verdict. IF an agent runs a SCHEMATIC-helper cross-check arm, that arm carries CLASS=SCHEMATIC + `convention=...-SCHEMATIC` + `# tier_pin=TIER-2` SEPARATELY and does NOT feed the canonical verdict line. The SCHEMATIC helper's SHA is pinned in the input ledger for that contingency.
- **Source-reconciliation**: `t*` target sourced from `canonical_constants.py:539 mellin_f_star_f0 = 0.08832` (S78 W2-D; substrate-first — NOT an external-paper placeholder). `tau_fold = 0.19` (S12/S42). `M_KK = 7.428660036284456e+16` (value canonical; PROVENANCE gap is W6 hygiene, not W2). E7 / `dS/dτ|_fold = +58,672.8` and `S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD value=−2.04e4` are structurally-pinned (W7/S37, S84). No pin drifts; SOURCE-RECON D_max < 0.1 (no action).
- **Substitution chains**: all three gates carry MANDATORY substitution chains (W2-1 [CHAIN] magnitude/sign; W2-3 [SIGN] sign-of-dΓ/dτ; W2-2 [VERIFY-THEOREM] structural reduction). W2-1 and W2-3 emit the schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row; W2-2 does not (structural, no directional pre-registration).

## Wave 2 Input-SHA Ledger

| Input file | Consumed by | Expected SHA-256 |
|:-----------|:------------|:-----------------|
| `computations/_shared/canonical_constants.py` | W2-1, W2-2, W2-3 | `<computed-at-runtime>` (edited S94; script logs SHA in first 20 stdout lines) |
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | W2-1, W2-3 | `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9` (static; precomputed at plan-freeze) |
| `computations/_shared/_spectral_action_regulators.py` | W2-1, W2-3 (SCHEMATIC cross-check arm ONLY, if run) | `2fc40ccbb62fcbf1851f7879f901ce6d913ab823e3da736cf8ac21e5be0f0afa` (static; SCHEMATIC helper — consumed ONLY under CLASS=SCHEMATIC-tagged cross-check, never the canonical verdict) |

Sage-MCP (W2-2) is a service, not a file input — no SHA pin; the symbolic HH¹ computation + orbit-reducibility identities are reproducible from the script's `sage_eval`/`sage_simplify` calls logged in stdout.

Cross-checked at plan-freeze by `computations/_shared/_plan_upstream_pin_validator.py`. Static SHAs verified present on disk at plan-authorship (2026-05-28); `<computed-at-runtime>` entries are dynamic (recently-edited canonical_constants) and verified at execution per `gate-verdicts.md`.

---

*End Wave 2 plan. Three gates (one-loop structural completeness: t* de-empiricization, interaction-exhaustion falsifier, one-loop no-well robustness). All pre-registered NEUTRAL — PASS, FAIL, and INFO are all physics results per `math-scripts.md §"All Results Are Good Results"`. Dispatchable: `/rclab-coordinate session-95-plan-w2.md`.*
