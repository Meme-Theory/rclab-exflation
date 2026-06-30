# Session 116 Plan — Wave 1: Q23 Transit Power Spectrum / A_s Normalization

**Date**: 2026-06-27
**Author**: transit-dynamics-theorist (per-wave planner, /rclab-plan session-mode fanout)
**Owner agent**: transit-dynamics-theorist
**Scope source**: `sessions/session-plan/session-116-context.md §"Wave 1 — Q23"` (user-supplied 9-question open-question table; Q23 = THE critical A_s residual)
**Plan source**: `sessions/session-plan/session-116-context.md` + knowledge-MCP deep-query grounding (this plan-freeze)
**Working paper**: `sessions/session-116/session-116-w1-workingpaper.md`
**Verdict file (compute gates)**: `computations/session-116/s116_gate_verdicts.txt`
**Workshop deliverables**: `sessions/session-116/workshops/{slug}.md`

---

## Wave 1 Summary

Q23 (TRANSIT-PS-67, CRITICAL) resolves α_s falsification, A_s normalization, and n_s(k) simultaneously. Two of the three legs are **closed**: α_s(CMB)→≈0 (Goldstone-pivot, S92; `alpha_s_pivot_goldstone=0`) and n_s (geometric tilt 0.9561, S85). The **A_s normalization magnitude is the sole open residual** (CF23 SPLIT, S110: the FLOOR `A_s ≥ A_s^BD` is PERMANENT/3-axis, the MAGNITUDE/upper-edge is a SCHEME-DEPENDENT FILTER = OPEN). This wave attacks the magnitude via the substrate-natural factorization

```
A_s  =  (squeeze amplitude)  ×  (exit greybody filter)
        \____ CF-B1 ____/       \____ CF-AS-2 ____/        reconciled in CF-AS-3
```

and adjudicates the long-standing H̃-branch OOM-figure conflict in a workshop. The wave's gate-type mix is **1 workshop + 3 compute** (MIXED), owner-of-math `transit-dynamics-theorist` for the two transit-Bogoliubov computes, `mack-cosmic-bridge` for the observational product-reconciliation compute and as the observational adversary in the workshop.

**Grounding the plan builds on (NOT re-derived)** — three catches the context-file framing predates:

1. **CF21 is ALREADY reconciled**. `INV12-W3-5-CF21-HTILDE-RECONCILE` (PASS): `cc3=2.000000`, `oomH_TDLI=2.3798` (H̃-space), `oomAs_TDLI=4.7595` (A_s-space), `fig238=Htilde-space`, `fig456=As-space-stale-live4.76`, `Hratio_TD_base=1.2532 ≈ sqrt(1.5712)=1.2535`. The **2.38 (H̃-space)** and **4.76 (A_s-space)** figures are the SAME divergence in two spaces, related by the CC3 identity `d(ln A_s)/d(ln H̃)=+2` (A_s ∝ H̃²); the **"4.56" was a stale rendering of the live 4.76**. They are NOT divergent figures. The atlas-04 Summary and atlas-08 CF21 entries still carry the un-reconciled "2.38 vs 4.56" — a capstone-hygiene drift the workshop documents.

2. **The live canonical A_s is the box-delta impulse-quench value**: `A_s_FW = 1.5367059962762235e-08` (S111-CF-AS3a, **NOT superseded**), only **+0.864 OOM** from Planck `A_s_CMB = 2.1e-9` — far smaller than the historical 3.15 / 4.56 figures.

3. **The route-spread is a REAL sudden↔adiabatic physical axis, PLURALISM-PERMANENT** (`S115-AS-NEWAXIS-SELECTOR`, FAIL): `spread_existing_OOM=1.2590`, `min_collapse_dist_OOM=0.6281 ≫ band 0.1` — a maxent+Connes-diam selector did NOT collapse the spread. The live A_s OOM map vs Planck:

   | Route | A_s | OOM gap | Source |
   |:------|:----|:--------|:-------|
   | TD/zeta UNIFIED-AS-79 (Branch-A) | 3.2994e-9 | +0.196 | S82 W1-2 |
   | maxent | 1.4006e-8 | +0.824 | S115 |
   | box-delta / impulse `A_s_FW` (CANONICAL) | 1.5367e-8 | +0.864 | S111-CF-AS3a |
   | Parker inv6 (S110 amplitude pair) | 5.99e-8 | +1.455 | S110 / INV6-W2-2 |
   | Connes-Parker | 7.068e-8 | +1.527 | S115 |

   Established sudden↔adiabatic axis band: **[+0.196, +1.527]**, existing-routes spread **1.259 OOM**.

---

## Wave 1 Gate-Type Manifest

| Gate ID | gate_type | Owner-of-math | Scope |
|:--------|:----------|:--------------|:------|
| S116-W1-HTILDE-RECON | workshop | transit-dynamics-theorist × mack-cosmic-bridge | Pin ONE canonical OOM figure across {2.38 H̃-space, 4.76 A_s-space, 3.15 Route-B-PW}; verdict convention-blocked vs physics-blocked |
| S116-W1-AS-CFB1 | compute | transit-dynamics-theorist | Promote the SQUEEZE A_s magnitude (box-delta sudden, ξ_KZ-normalized) from S110 registered-content to a GATED threshold + resolve POINT-vs-BAND via L_max-stability (AS3b-deferred) |
| S116-W1-AS-CF2 | compute | transit-dynamics-theorist | EXACT (non-WKB) finite-rate exit-greybody ∫Γ — validate or close the magnitude-PASS that `S110-CF-AS2-GREYBODY` found regime-invalidated (eps_WKB=7.34 BREAKDOWN) |
| S116-W1-AS-CF3 | compute | mack-cosmic-bridge | Product reconciliation A_s = squeeze × filter; regime-tag all routes; test collapse onto the workshop figure (overturn S115 PLURALISM) vs reproduce the S115 axis; n_s scheme-split consistency |

---

## Wave 1 Decision Point Prerequisites

- **S116-W1-HTILDE-RECON** (workshop): no compute prereq. Reads the registered upstream artifacts (INV12-W3-5 verdict, S110-CF-B1 npz, AMPLITUDE-NORM-66 row, S111 npz, S115 verdict). Closes by artifact-existence (no verdict line).
- **S116-W1-AS-CFB1** (compute): no intra-wave prereq. Consumes S100b box-delta npz + S110-CF-B1 npz + S111 npz + the L12 spectrum cache (all on disk). Dispatchable immediately.
- **S116-W1-AS-CF2** (compute): no intra-wave prereq. Consumes INV12-W3-4 npz (the derived-greybody FAIL) + S110-CF-AS2 npz (the dynamical-barrier regime-breakdown) + S95-W4-3 npz (the fitted 0.512). Dispatchable immediately.
- **S116-W1-AS-CF3** (compute, mack): **consumes S116-W1-AS-CFB1 npz (squeeze) + S116-W1-AS-CF2 npz (filter) + the S116-W1-HTILDE-RECON workshop md (pinned figure)**. Best dispatched AFTER those three close. Per `mechanical-closure-discipline.md`, each upstream input carries a CANONICAL FALLBACK so CF-AS-3 is NOT hard-blocked: if a fresh S116 upstream is absent at dispatch, CF-AS-3 falls back to the canonical published value (squeeze→`A_s_FW`=1.5367e-8; filter→fitted 0.512; workshop figure→INV12-W3-5 reconciled 4.76 A_s-space / 2.38 H̃-space) and tags each input as FRESH-vs-FALLBACK in the verdict `value=` field. A CF-AS-3 run on ≥1 fallback emits its verdict honestly with the fallback disclosure; it does NOT PRE-REG-INC unless ALL three upstreams are fallback (in which case it closes PRE-REG-INC per the discipline, the reconciliation being vacuous).

---

## §W1-1. S116-W1-HTILDE-RECON  [gate_type: workshop]

The H̃-branch OOM-figure conflict is a genuine math/physics adjudication (Q1-YES per `Investigating-Workshops.md`): two first-principles readings of what the OOM divergence MEANS. The reading-divergence is the workshop seed. EXACTLY 2 agents, 3 rounds (R1 steelman / R2 rebut opponent's best case / R3 converge on a STRUCTURAL VERDICT). NO verdict line; closes by artifact-existence.

```yaml
gate_id: "S116-W1-HTILDE-RECON"
schema_version: "R3"
gate_type: "workshop"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "transit-dynamics-theorist"   # workshop author-of-record; both agents below
hypothesis: "The H̃-branch OOM figures (2.38 H̃-space, 4.76 A_s-space, 3.15 Route-B-PW) admit a single canonical reading, and A_s closure is either CONVENTION-blocked (one figure selectable) or PHYSICS-blocked (irreducibly plural per the S115 sudden↔adiabatic axis)."

workshop:
  agents: ["transit-dynamics-theorist", "mack-cosmic-bridge"]
  rounds: 3
  sources:
    - "computations/investigation-12/inv12_gate_verdicts.txt"   # INV12-W3-5-CF21-HTILDE-RECONCILE PASS (cc3=2.0; 2.38 H̃-space / 4.76 A_s-space; 4.56=stale)
    - "computations/session-110/s110_cf_b1_transit_ps_promote.npz"   # two-leaf build + amplitude pair (inv5 +0.86 / inv6 +1.455)
    - "computations/session-111/s111_cf_as3a_impulse_quench.npz"   # A_s_FW=1.5367e-8 box-delta magnitude (+0.864 OOM)
    - "computations/session-115/s115_gate_verdicts.txt"   # S115-AS-NEWAXIS-SELECTOR PLURALISM (spread 1.259, no collapse 0.628)
    - "sessions/framework/Atlas/atlas-08-open-questions.md"   # §VIII CF21 (atlas carries un-reconciled 2.38 vs 4.56)
    - "sessions/framework/registry/constraint-mega-matrix.md"   # AMPLITUDE-NORM-66 FAIL (3.15 OOM Route-B Peter-Weyl)
  output_path: "sessions/session-116/workshops/s116-w1-htilde-recon.md"
  adjudication_question: |
    Given INV12-W3-5 ALREADY reconciled 2.38 (H̃-space) and 4.76 (A_s-space) as CC3-conjugate
    (A_s ∝ H̃², factor 2; the "4.56" was a stale rendering of the live 4.76), and given the
    box-delta route gives only +0.864 OOM (A_s_FW=1.5367e-8) while S115 declared the 1.259-OOM
    route-spread a REAL sudden↔adiabatic axis (PLURALISM, no collapse, min 0.628 OOM):
      (a) Is the H̃-branch TD/zeta figure (A_s=3.2994e-9, +0.196 OOM) a SEPARATE physical
          regime-point on the S115 sudden↔adiabatic axis, or the SAME Bogoliubov physics as
          the box-delta route under a different IC/normalization convention (Zubarev vs BD)?
      (b) Does the 3.15-OOM Route-B-Peter-Weyl figure (AMPLITUDE-NORM-66) reconcile with the
          4.76 A_s-space CC3 figure, or is it a third, genuinely-distinct route?
      (c) THE FORK: is A_s closure CONVENTION-blocked (a canonical horizon-exit reading selects
          ONE OOM figure) or PHYSICS-blocked (the substrate genuinely does not single out one
          A_s absent a regime-selection principle)?
    Deliverable: ONE pinned canonical OOM figure (with its declared space: H̃ or A_s) + the
    convention-vs-physics verdict + which of the three figures (if any) is retired.
  context: |
    COMPETING POSITIONS (each first-principles-backed; the workshop derives which is correct):
      TD side (transit-dynamics-theorist) — CONVENTION-BLOCKED. The 2.38/4.76/3.15 figures are
        normalization-convention images of ONE Bogoliubov divergence: 2.38↔4.76 is the exact
        CC3 factor-2 (deg(T_BZ→pivot)=+2 NON-SCALAR sets the H̃↔A_s power), and the box-delta
        +0.864 is the substrate-natural (ξ_KZ) horizon-exit reading. S115 "PLURALISM" is a
        selector-FAIL on a SPECIFIC (maxent+Connes-diam) selector, NOT a proof that no canonical
        horizon-exit reading exists. Pick the canonical reading → one figure emerges; closure is
        convention-blocked.
      Mack side (mack-cosmic-bridge) — PHYSICS-BLOCKED. Planck A_s=(2.10±0.03)e-9 is a tight
        datum; the routes predict 3.3e-9 / 1.5e-8 / 7e-8 — physically distinct, multi-σ apart.
        S115 showed no substrate principle collapses them (min 0.628 OOM ≫ 0.1 band). The
        sudden↔adiabatic spread is a real physical axis (which transit regime the CMB samples);
        calling it "convention" hides a genuine prediction gap. The "canonical horizon-exit
        reading" is itself a physics choice, not a free convention.
    NUMERIC STAKES: 2.38 (H̃-space) | 4.76 (A_s-space, =2×2.38) | 3.15 (Route-B-PW) | +0.864
      (box-delta canonical) | +0.196 (TD/zeta) | axis [+0.196,+1.527], spread 1.259.
    ADJUDICATION RULE: the verdict pins ONE OOM figure in a DECLARED space and states
      convention-blocked vs physics-blocked with the first-principles argument that decides it;
      it documents the atlas-04/atlas-08 capstone drift (un-reconciled 2.38-vs-4.56) for the
      §A/§B housekeeping route per capstone-hygiene-gate.md (Q3 status-change → reconcile prose).
    SUBSTRATE FRAMING: A_s IS the GGE-relic acoustic squeezing modulus of the post-transit
      produced state; the lab measures A_s IN a CMB container. The OOM "gap" is the substrate's
      overproduction relative to that container, NOT an inflaton-normalization mismatch.

# PRDR numeric items (2)(3)(4) = N/A for workshop (S95 non-compute clause).
operator:
  type: "set"
  form: "ONE pinned OOM figure ∈ {2.38 H̃-space, 4.76 A_s-space, 3.15 Route-B-PW, other-derived} + {convention-blocked | physics-blocked} verdict"
strict_PASS_boundary:
  value: "N/A — adjudication workshop; closes by artifact-existence (Structural Verdict present)"
  direction: "="
boundary_reachable_analytically:
  bool: false
  proof_ref: "null — two-reading adjudication, not a numerical threshold"
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — workshop"
machinery_pin_map:
  N_eval: "N/A — workshop (no producing script)"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "N/A"
  scheme: "MUKHANOV-SASAKI-HTILDE-BRANCH-ADJUDICATION"
  convention: "TWO-READING-CONVENTION-VS-PHYSICS"
  random_seed: "N/A — deterministic adjudication"
  GPU_path: "N/A — workshop"
audit_discriminators:
  audit_sha256_inputs: ["N/A — workshop closes by artifact-existence, no verdict line"]
  content_sha256_inputs: ["workshop_md"]
substitution_chain:
  required: false
  content: |
    N/A for the workshop gate itself (no producing script). The CC3-conjugacy substitution
    chain the workshop ADJUDICATES is pre-registered in §W1-4 (CF-AS-3) and was verified
    machine-ε at S82 (CC3 identity) and INV12-W3-5 (cc3=2.000000): A_s ∝ H̃²
    ⇒ OOM_A_s = 2·OOM_H̃ ⇒ 4.76 = 2 × 2.38 (exact).
input_files:
  inv12_verdicts:
    path: "computations/investigation-12/inv12_gate_verdicts.txt"
    sha256: "<computed-at-runtime>"
  s110_cf_b1_npz:
    path: "computations/session-110/s110_cf_b1_transit_ps_promote.npz"
    sha256: "<computed-at-runtime>"

PASS_meaning: "N/A (no PASS/FAIL/INFO verdict line). Closure = the workshop md exists with R1/R2/R3 + a Structural Verdict pinning ONE OOM figure + the convention-vs-physics fork resolved."
FAIL_meaning: "N/A — a workshop that fails to converge re-routes to a 2nd round of /rclab-workshop, not a FAIL verdict."
INFO_meaning: "N/A — workshop."

effort:
  files_created: ["sessions/session-116/workshops/s116-w1-htilde-recon.md"]
  estimated_time: "0.5 day (3 rounds, 2 agents sequential)"

substrate_framing: |
  PHONONIC. The substrate IS the GGE-relic acoustic squeezing modulus A_s of the post-fold
  produced state; the H̃-branch is the Mukhanov-Sasaki variable v_k'' + (k² − z''/z)v_k = 0
  with z = a·√(2ε_H)·M_Pl_eff. The OOM "divergence" is a normalization-convention question
  about WHICH horizon-exit reading of the SAME |β_k|² the lab reads — the substrate overproduces
  relative to the CMB container by an amount set by deg(T_BZ→pivot)=+2 (the H̃↔A_s power). The
  workshop decides whether that overproduction is a single convention-fixable figure (TD) or an
  irreducibly-plural physical axis (mack).

output_artifacts:
  workshop_md:
    path: "sessions/session-116/workshops/s116-w1-htilde-recon.md"
    artifact_kind: "workshop_md"
    must_contain:
      - "## Round 1"
      - "## Round 2"
      - "## Round 3"
      - "## Structural Verdict"
      - "OOM"
      - "(convention-blocked|physics-blocked)"
  # NO verdict_line (workshop closes by artifact-existence == wave-classification.md §M1).
```

---

## §W1-2. S116-W1-AS-CFB1  [gate_type: compute]

Promotes the SQUEEZE amplitude leg — which `S110-CF-B1-TRANSITPS` explicitly carried as REGISTERED CONTENT, "NOT a separate gate threshold" (s110 script line 64) — to a GATED magnitude, and resolves the POINT-vs-BAND epistemic type that `S111-CF-AS3a` DEFERRED to the AS3b FB-temp verdict (s111 script lines 58-63). The squeeze is the substrate-natural box-delta sudden-limit Bogoliubov amplitude (the MAGNITUDE source); the fold-window grid is the REGIME source (TWO-SPECTRA-TWO-ROLES, S111).

**Substitution chain** (the OOM-gap sign + band-membership claim):

```
Claim: "the squeeze A_s OOM gap is POSITIVE (substrate overproduces) and lands within the
         S115 sudden↔adiabatic axis band [+0.196, +1.527], BELOW the discredited +3.15
         Route-B-PW figure and far below the +9.37 naive-UV-extrapolation artifact."

  Step 1: A_s_squeeze = |β_{k̂}|² / (2π²) · N_norm        [S111 recipe; del Campo-Zurek 1310.1600]
          with N_norm = ξ_KZ³ (KZ coherence VOLUME), k̂ = 1/ξ_KZ = 53.30 M_KK,
          ξ_KZ = xi_KZ_FW = 0.018760052113614718,  |β_{k̂}|² from S100b box-delta SUDDEN spectrum
  Step 2: A_s_Planck = A_s_CMB = 2.1e-9                    [Planck 2018 VI; canonical_constants]
  Step 3: OOM = log10(A_s_squeeze / A_s_Planck)            [definition]
  Step 4: Substitute A_s_squeeze = 1.5367e-8 (S100b box-delta, S111-pinned), A_s_Planck = 2.1e-9
          OOM = log10(1.5367e-8 / 2.1e-9) = log10(7.318) = +0.8644
  Step 5: A_s_squeeze > A_s_Planck  ⇒  OOM > 0  (overproduction)               [sign read-off]
          +0.8644 ∈ [+0.196, +1.527]  AND  +0.8644 < +3.15 (Route-B-PW)  AND  ≪ +9.37 (UV artifact)
  Conclusion: squeeze OOM is positive, in-axis, below the discredited routes — band PASS;
              the discriminating NEW content is the L_max-stability POINT-vs-BAND resolution.
```

```yaml
gate_id: "S116-W1-AS-CFB1"
schema_version: "R3"
gate_type: "compute"
trigger: "[SIGN]"
classification: "PHONONIC"
agent_type: "transit-dynamics-theorist"
hypothesis: "The box-delta squeeze A_s magnitude (ξ_KZ-normalized) is a POSITIVE OOM-gap overproduction inside the S115 sudden↔adiabatic axis [+0.196,+1.527], and is an L_max-stable POINT (Friedrich-Bär saturated at L12), not an L_max-soft BAND."

method:
  description: |
    (1) Re-load the S100b box-delta SUDDEN-LIMIT |β_k|² spectrum (the MAGNITUDE source) + the
        S110-CF-B1 two-leaf build + the S111-CF-AS3a pinned A_s. Extract A_s_squeeze =
        |β_{k̂}|²/(2π²)·ξ_KZ³ at k̂=1/ξ_KZ by the near-flat UV-tail read (slope ~ −0.003, the
        scale-invariant sudden signature), reproducing 1.5367e-8 to published precision.
    (2) GATE the OOM gap log10(A_s_squeeze/A_s_CMB) against the S115 axis band [+0.196,+1.527]
        (PROMOTION of S110's registered-content amplitude to a gated threshold).
    (3) RESOLVE POINT-vs-BAND (AS3b-deferred): test L_max-stability of A_s_squeeze across the
        L7-equiv vs L12 truncations available in the S110 build (branch_drift_L3_L7,
        truncation_consistent) + the Friedrich-Bär saturation argument that the cosmological
        window is Casimir-saturated at L12 (new p+q≥13 sectors have |λ| above the window
        ceiling → no shift). POINT iff |ΔA_s|/A_s ≤ stability_tol; BAND otherwise.
    (4) Confirm the FLOOR A_s ≥ A_s^BD (the permanent 3-axis inequality, S_IC=1+2n_k≥1) as a
        sub-annotation (NOT the gate operator).
  producing_script: "computations/session-116/s116_w1_as_cfb1_squeeze_promote.py"

operator:
  type: "set"
  form: "(OOM ∈ [+0.196, +1.527]) AND (epistemic_type ∈ {POINT, BAND} resolved) AND (A_s_squeeze ≥ A_s_BD floor)"
strict_PASS_boundary:
  value: "OOM ∈ [+0.196, +1.527]  AND  L_max-stability |ΔA_s(L7eq→L12)|/A_s ≤ 0.05 (POINT)"
  direction: "<="
boundary_reachable_analytically:
  bool: true
  proof_ref: "S111-CF-AS3a npz (A_s_FW=1.5367e-8, +0.864 OOM, round-trips INV5 anchor rel-dev 3.9e-6); S115 axis [+0.196,+1.527] (existing-routes span); Friedrich-Bär saturation (math-scripts.md §D_K Block-Diagonality feasibility)"
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous (OOM is a log-ratio); the L_max axis is an integer mesh {7-equiv, 10, 12}"
machinery_pin_map:
  N_eval: "89 fold-window modes (REGIME source) + box-delta UV-tail grid (MAGNITUDE source, ~64 k-points)"
  L_max: "12 (L_max_operational; L7-equiv cross-check from S110 build; Friedrich-Bär saturation for L≥12)"
  scan_range: "L_max-stability over {L7-equiv, L12}; OOM band [+0.196, +1.527]"
  step_size: "N/A — discrete L_max mesh + closed-form A_s read"
  tolerance: "OOM band [+0.196,+1.527]; L_max-stability rel-dev <= 0.05 (POINT/BAND split); floor inequality strict > 1"
  scheme: "IMPULSE-QUENCH-BOGOLIUBOV"
  convention: "FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL-xiKZ"
  random_seed: "N/A — deterministic (loaded {β_k}; closed-form A_s)"
  GPU_path: "cpu-cap-OMP8 (few-mode β-sum + cache re-load; NO ≥100×100 dense diag — matches S110/S111)"
  publication_precision: "5  (A_s_squeeze cited downstream by S116-W1-AS-CF3)"
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap", "s100b_box_delta_npz", "s110_cf_b1_npz", "s111_cf_as3a_npz"]
  content_sha256_inputs: ["script"]
substitution_chain:
  required: true
  content: |
    Step 1: A_s_squeeze = |β_{k̂}|²/(2π²)·ξ_KZ³, k̂=1/ξ_KZ=53.30 M_KK, ξ_KZ=xi_KZ_FW=0.018760 [S111 recipe]
    Step 2: A_s_Planck = A_s_CMB = 2.1e-9 [Planck 2018 VI]
    Step 3: OOM = log10(A_s_squeeze/A_s_Planck) [definition]
    Step 4: Substitute A_s_squeeze=1.5367e-8, A_s_Planck=2.1e-9 → OOM=log10(7.318)=+0.8644
    Step 5: A_s_squeeze>A_s_Planck ⇒ OOM>0; +0.8644 ∈ [+0.196,+1.527] ∧ < +3.15 (Route-B-PW) ∧ ≪ +9.37 (UV artifact)
    Conclusion: positive in-axis overproduction; gate adds L_max-stability POINT-vs-BAND (AS3b-deferred, discriminating).

fb_pair:
  forward: "S100b-BOX-DELTA-BOGOLIUBOV (|β_k|² magnitude source); S111-CF-AS3a (A_s pin); S110-CF-B1-TRANSITPS (regime/two-leaf build)"
  backward: "S116-W1-AS-CF3 (squeeze leg of the product A_s = squeeze × filter); next-session A_s falsifier row (Row 8)"
dual_prior:
  track_A: "0.6 — POINT (L_max-stable; the cosmological window is Friedrich-Bär saturated at L12; the magnitude is a converged physical d.o.f.)"
  track_B: "0.4 — BAND (L_max-soft; a higher-Casimir sector at L≥13 shifts |β_{k̂}|²; the magnitude is L_max-soft)"
  discriminator: "PASS (OOM in-axis ∧ |ΔA_s|/A_s ≤ 0.05) → 0.9 to Track A (POINT); INFO (in-axis ∧ rel-dev > 0.05) → 0.9 to Track B (BAND); FAIL (OOM out-of-axis) → squeeze route mis-normalized, both tracks void."

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # edited mid-session by other waves; consumed anchors (xi_KZ_FW, A_s_CMB) unchanged → ZERO physics effect (§ii.B)
  s100b_box_delta:
    path: "computations/session-100b/s100b_box_delta_bogoliubov.npz"
    sha256: "<computed-at-runtime>"   # numpy savez zip-ts non-det; ARRAY-CONTENT verified (§ii.B)
  s110_cf_b1:
    path: "computations/session-110/s110_cf_b1_transit_ps_promote.npz"
    sha256: "<computed-at-runtime>"
  s111_cf_as3a:
    path: "computations/session-111/s111_cf_as3a_impulse_quench.npz"
    sha256: "<computed-at-runtime>"
  s84_spectrum_cache:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "<computed-at-runtime>"   # tracked/git-canonical; runtime-assert MUST match (mechanical-closure HALT on drift, per S110 line 196)

PASS_meaning: "The squeeze A_s magnitude is a POSITIVE in-axis overproduction (OOM ∈ [+0.196,+1.527]) AND an L_max-stable POINT — the squeeze factor of A_s is a converged physical d.o.f. above the permanent floor. Promotes S110's registered amplitude to a gated magnitude; resolves AS3b POINT."
FAIL_meaning: "OOM falls OUTSIDE [+0.196,+1.527] — the squeeze route recovers a discredited normalization (the +3.15 Route-B-PW or +9.37 naive-UV artifact); the box-delta ξ_KZ normalization does NOT carry, and the magnitude source is mis-identified."
INFO_meaning: "OOM in-axis but L_max-soft (|ΔA_s|/A_s > 0.05) — the squeeze magnitude is a BAND (Track B), not a POINT; the AS3b epistemic type is BAND, and the magnitude carries an L_max-soft caveat to CF-AS-3."

effort:
  files_created:
    - "computations/session-116/s116_w1_as_cfb1_squeeze_promote.py"
    - "computations/session-116/s116_w1_as_cfb1_squeeze_promote.npz"
    - "computations/session-116/s116_w1_as_cfb1_squeeze_promote.png"
  estimated_time: "0.5 day"

substrate_framing: |
  PHONONIC. The arrow: D_K eigenvalues λ_k(τ) → transit Bogoliubov {α_k, β_k} → produced
  occupation n_k = |β_k|² → post-fold acoustic squeeze A_s. The substrate IS the box-delta
  sudden-limit |β_{k̂}|² at the Kibble-Zurek coherence scale k̂=1/ξ_KZ; A_s is read off that
  frozen occupation, NOT an inflaton normalization. The L_max axis is the substrate's own
  spectral-support truncation; POINT (Friedrich-Bär saturated) vs BAND (L_max-soft) is whether
  the cosmological window's |β_{k̂}|² is a converged substrate-IS observable. The lab measures
  A_s IN a CMB container; the OOM gap is the substrate's overproduction relative to it.

output_artifacts:
  script:
    path: "computations/session-116/s116_w1_as_cfb1_squeeze_promote.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/session-116/s116_w1_as_cfb1_squeeze_promote.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-116/s116_w1_as_cfb1_squeeze_promote.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-116/s116_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S116-W1-AS-CFB1:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true   # [SIGN] trigger
  wp_section:
    path: "sessions/session-116/session-116-w1-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W1-2. S116-W1-AS-CFB1"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"
```

---

## §W1-3. S116-W1-AS-CF2  [gate_type: compute]

The exit-greybody filter (the upper-edge factor of A_s = squeeze × filter). The established CF-AS-2 lineage is the greybody: `S95-W4-3` FITTED Γ=0.511872 (sigmoid placed at the relic-band midpoint 0.9418 — the A2 tuning knob); `INV12-W3-4` derived ∫Γ=0.036265 from the static κ_exit=47.6146 Pöschl-Teller barrier (agreement 0.929 FAIL); `S110-CF-AS2-GREYBODY` (FAIL) found a DYNAMICAL substrate barrier (ω_q=2.0128 / relic_rms=2.9253) that reproduces 0.512 to `best_inband_rel_dev=0.0494` (magnitude=PASS) **but with `eps_WKB=γ_clock/κ_eff²=7.34 ≫ 1`, `domain_used_frac=0.143` → `regime=BREAKDOWN` → composite FAIL**. The magnitude is substrate-REACHABLE but WKB-INVALIDATED. This gate tests the live residual: an **EXACT (non-WKB) finite-rate** scattering treatment of the dynamical barrier — validate the magnitude-PASS or close the greybody as irreducibly fitted.

**Substitution chain** (the regime claim — why an exact treatment changes the S110-CF-AS2 verdict):

```
Claim: "the EXACT 1D BdG scattering integral ∫Γ does NOT inherit the eps_WKB=7.34 regime
         BREAKDOWN that forced S110-CF-AS2 to composite FAIL; its validity is governed by
         ODE-convergence, not near-horizon WKB adiabaticity."

  Step 1: eps_WKB(κ_eff) = γ_clock / κ_eff²              [S110-CF-AS2 auto-shortening clause]
          = 7.34 @ ω_q, 3.48 @ relic_rms  →  regime BREAKDOWN (only 14.3% of window WKB-valid)
  Step 2: the S110-CF-AS2 magnitude (∫Γ → 0.512 to 4.9%) used the CLOSED Pöschl-Teller
          transmission Γ(ω)=sinh²(πω/κ)/[sinh²(πω/κ)+cosh²(πs)], whose derivation assumes a
          STATIC barrier (adiabatic near-horizon) — invalid at eps_WKB ≫ 1
  Step 3: the EXACT treatment solves the FULL finite-rate scattering −ψ'' + V_eff(x_*,τ)ψ = ω²ψ
          (time-dependent V_eff via the supersonic τ̇(τ); a Floquet/Numerov scattering solve),
          with validity set by ODE atol/rtol convergence, NOT eps_WKB
  Step 4: regime_exact = VALID iff the exact-ODE ∫Γ converges (atol≤1e-10) over ≥95% of the
          ω-window; this is INDEPENDENT of eps_WKB (Step 1 does not enter the exact solve)
  Direction: regime_exact decouples from eps_WKB ⇒ a magnitude-PASS in the exact treatment is
          NOT auto-invalidated the way the closed-PT magnitude-PASS was
  Conclusion: PASS iff exact ∫Γ reproduces 0.512 within RATIO 10% in a VALID (ODE-converged)
          regime (greybody substrate-derived, A2 knob removed, upper-edge closes); FAIL iff the
          exact ∫Γ misses 0.512 for ALL substrate barrier scales (irreducibly fitted →
          structural-closure: A_s upper-edge is NOT substrate-derivable, magnitude is PLURALISM).
```

```yaml
gate_id: "S116-W1-AS-CF2"
schema_version: "R3"
gate_type: "compute"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "transit-dynamics-theorist"
hypothesis: "An EXACT finite-rate BdG scattering ∫Γ through the dynamical exit barrier either reproduces the fitted Γ=0.512 in a regime VALID by ODE-convergence (greybody substrate-derived, A2 knob removed) OR misses it for all substrate barrier scales (greybody irreducibly fitted, structural-closure of the A_s upper-edge)."

method:
  description: |
    (1) Re-load INV12-W3-4 (derived static-barrier ∫Γ=0.036265, κ_exit=47.6146, V0 bracket
        readings), S110-CF-AS2 (dynamical-barrier magnitude-PASS 0.0494 + the eps_WKB=7.34
        regime-breakdown), S95-W4-3 (fitted Γ=0.511872, relic band [0.94,3.72], squeeze
        weighting mult_k·β2_k).
    (2) Solve the EXACT finite-rate scattering −ψ'' + V_eff(x_*,τ)ψ = ω²ψ through the dynamical
        near-horizon barrier V_eff = V0·sech²(κ_eff x_*) with the substrate-FIXED dynamical
        scales {ω_q, relic_rms, Floquet γ_clock} (NONE placed at the band) — by an independent
        1D scattering ODE (Numerov / solve_ivp, atol≤1e-10) AND, for the time-dependent barrier,
        a Floquet-monodromy transmission. Cross-check the two to machine level. This REPLACES
        the closed Pöschl-Teller form (WKB-invalid at eps_WKB≫1).
    (3) Compute the squeeze-weighted ∫Γ_exact (same mult_k·β2_k weighting as the fitted
        comparator) and the agreement = |∫Γ_exact − 0.512|/0.512. Set regime_verdict by
        ODE-convergence f_used (atol-converged fraction of the ω-window), per the auto-shortening
        clause — INDEPENDENT of eps_WKB.
    (4) If NO substrate barrier scale yields ∫Γ_exact within RATIO 10%, emit the structural-
        closure reading: the greybody is irreducibly fitted, the A_s upper-edge is NOT
        substrate-derivable, the magnitude is PLURALISM (consistent with S115).
  producing_script: "computations/session-116/s116_w1_as_cf2_greybody_exact.py"

operator:
  type: "ratio"
  form: "agreement = |∫Γ_exact − 0.511872| / 0.511872  <=  0.10   (with regime_exact = VALID by ODE-convergence)"
strict_PASS_boundary:
  value: "0.10 (RATIO) AND regime_exact = VALID (ODE atol-converged f_used ≥ 0.95)"
  direction: "<="
boundary_reachable_analytically:
  bool: true
  proof_ref: "S95-W4-3 fitted 0.511872; INV12-W3-4 bracket {κ_exit²→0.036, T_compound²=57.43→0.836} straddles 0.512; S110-CF-AS2 dynamical magnitude rel-dev 0.0494 (eps_WKB-invalidated). Exact PT transmission Landau-Lifshitz QM §25 cross-checked to 1.025e-9 (S110 ode_vs_closed)."
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous (∫Γ is a transmission integral over the ω-window); barrier-scale candidate set is discrete {ω_q, relic_rms, γ_clock, 2Δ_BCS, κ_exit}"
machinery_pin_map:
  N_eval: "ω-window grid ~256 points (relic band [0.94,3.72] M_KK); x_* tortoise grid ~2048; Floquet period sub-steps ~512"
  L_max: "10 (relic spectrum from inv12_w3_1 lock; matches S110-CF-AS2 L_max=10)"
  scan_range: "barrier-scale candidates {ω_q=2.0128, relic_rms=2.9253, γ_clock(Floquet), 2·Δ_BCS, κ_exit=47.6146}; ω ∈ [0.94, 3.72] M_KK"
  step_size: "ODE atol≤1e-10, rtol≤1e-10 (solve_ivp Radau/Numerov); adaptive"
  tolerance: "agreement RATIO ≤ 0.10; regime f_used ≥ 0.95 (ODE-converged); cross-check ODE-vs-Floquet ≤ 1e-8"
  scheme: "BdG-fluctuation-EXACT-finite-rate-scattering"
  convention: "DYNAMICAL-near-horizon-NON-WKB-ODE-AND-FLOQUET"
  random_seed: "N/A — deterministic ODE"
  GPU_path: "cpu-cap-OMP8 (1D scattering ODE + small Floquet monodromy 2×2; NO ≥100×100 dense diag)"
  publication_precision: "4  (∫Γ_exact cited downstream by S116-W1-AS-CF3)"
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap", "inv12_w3_4_npz", "s110_cf_as2_npz", "s95_w4_3_npz"]
  content_sha256_inputs: ["script"]
substitution_chain:
  required: true
  content: |
    Step 1: eps_WKB(κ_eff)=γ_clock/κ_eff² = 7.34@ω_q (S110-CF-AS2 → regime BREAKDOWN, f_used 0.143)
    Step 2: the magnitude-PASS used the CLOSED Pöschl-Teller transmission (static/adiabatic barrier; WKB-invalid at eps_WKB≫1)
    Step 3: the EXACT solve −ψ''+V_eff(x_*,τ)ψ=ω²ψ (finite-rate, ODE atol≤1e-10) does NOT invoke WKB; validity = ODE-convergence
    Step 4: regime_exact = VALID iff ODE f_used ≥ 0.95 — INDEPENDENT of eps_WKB
    Conclusion: PASS iff ∫Γ_exact reproduces 0.512 (RATIO ≤0.10) in a VALID regime; FAIL iff missed for all substrate scales → structural-closure (greybody irreducibly fitted, upper-edge PLURALISM).

dual_prior:
  track_A: "0.4 — the exact finite-rate treatment VALIDATES the magnitude-PASS (∫Γ_exact ≈ 0.512 in a VALID regime); greybody substrate-derived, A2 knob removed, A_s upper-edge closes"
  track_B: "0.6 — the exact treatment does NOT reproduce 0.512 at any substrate scale (or remains regime-invalid); greybody irreducibly fitted, structural-closure; the A_s upper-edge is NOT substrate-derivable (magnitude PLURALISM per S115)"
  discriminator: "PASS → 0.9 to Track A (greybody substrate-derived); FAIL → 0.9 to Track B (irreducible-fitting structural-closure); INFO → unchanged (reproduces 0.512 but with a residual regime caveat)"

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # consumed anchors (kappa_exit, Delta_BCS, A_s_CMB, T_compound) unchanged → ZERO physics (§ii.B)
  inv12_w3_4_greybody:
    path: "computations/investigation-12/inv12_w3_4_greybody_from_bdg.npz"
    sha256: "<computed-at-runtime>"
  s110_cf_as2_greybody:
    path: "computations/session-110/s110_cf_as2_greybody_scan.npz"
    sha256: "<computed-at-runtime>"
  s95_w4_3_greybody:
    path: "computations/session-95/s95_w4_3_hawking_greybody_as.npz"
    sha256: "<computed-at-runtime>"

PASS_meaning: "The exact finite-rate greybody ∫Γ reproduces the fitted 0.512 (RATIO ≤ 0.10) in a regime VALID by ODE-convergence — the exit greybody is SUBSTRATE-DERIVED, the A2 tuning knob is removed, and the A_s upper-edge closes. The S110-CF-AS2 regime-breakdown was a WKB-method artifact, not a physics wall."
FAIL_meaning: "No substrate barrier scale yields ∫Γ_exact within RATIO 10% (or the exact regime remains invalid) — the greybody is IRREDUCIBLY FITTED (the A2 knob is a genuine free parameter). Structural-closure: the A_s upper-edge is NOT substrate-derivable, and the magnitude collapses to {floor + sudden↔adiabatic PLURALISM} (consistent with S115). Closes a corridor in the magnitude map."
INFO_meaning: "The exact ∫Γ reproduces 0.512 but with a residual regime caveat (ODE f_used between 0.5 and 0.95, or ode-vs-Floquet cross-check marginal) — the greybody is substrate-reachable but the finite-rate regime is MARGINAL; the upper-edge closure carries a regime caveat to CF-AS-3."

effort:
  files_created:
    - "computations/session-116/s116_w1_as_cf2_greybody_exact.py"
    - "computations/session-116/s116_w1_as_cf2_greybody_exact.npz"
    - "computations/session-116/s116_w1_as_cf2_greybody_exact.png"
  estimated_time: "1 day"

substrate_framing: |
  PHONONIC. The arrow: D_K eigenvalues λ_k(τ) → exit-horizon BdG dispersion ω_k → linearized
  fluctuation δφ_k obeys a Schrödinger scattering equation in the tortoise coordinate → the
  transmission Γ(ω)=|T(ω)|² through the near-horizon barrier IS the exit greybody that filters
  the overproduced squeeze. The substrate IS the BdG fluctuation potential; the greybody is the
  acoustic white-hole exit-horizon transmission (Steinhauer 1510.00621; Macher-Parentani
  0903.2224). The question is whether the substrate's OWN dynamical near-horizon scale produces
  the 0.512 filter (substrate-derived) or whether 0.512 lives only at the fitted band-midpoint
  (irreducibly fitted) — i.e., whether the A_s upper-edge is substrate-IS or a free knob.

output_artifacts:
  script:
    path: "computations/session-116/s116_w1_as_cf2_greybody_exact.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/session-116/s116_w1_as_cf2_greybody_exact.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-116/s116_w1_as_cf2_greybody_exact.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-116/s116_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S116-W1-AS-CF2:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false   # [VERIFY] ratio gate; sign_verdict N/A (matches S110-CF-AS2)
  wp_section:
    path: "sessions/session-116/session-116-w1-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W1-3. S116-W1-AS-CF2"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"
```

---

## §W1-4. S116-W1-AS-CF3  [gate_type: compute]

The product reconciliation: A_s = squeeze (CF-B1) × filter (CF-AS-2), collecting ALL routes, regime-tagging each (sudden vs adiabatic per the S115 axis), testing whether they COLLAPSE onto the workshop-pinned OOM figure (which would OVERTURN the S115 PLURALISM verdict) or REPRODUCE the S115 sudden↔adiabatic axis (the expected outcome). Also reconciles the n_s scheme split (0.959 sqrt-cutoff / 0.9561 framework / 0.9649 Planck) as regulator-variants with cutoff-scheme tags. Owner-of-math `mack-cosmic-bridge` (the observational reconciliation against Planck).

**Substitution chain** (the collapse-distance claim):

```
Claim: "after regime-tagging, the min collapse-distance of the routes to the workshop-pinned
         figure is SMALLER than the raw 1.259-OOM S115 spread, but the routes do NOT collapse
         to within the 0.1-OOM band — they reproduce the S115 sudden↔adiabatic two-cluster axis."

  Step 1: routes = {squeeze CF-B1 +0.864, Parker inv6 +1.455, TD/zeta UNIFIED-AS-79 +0.196}
          with OOM_route = log10(A_s_route / A_s_CMB)               [defined per route]
  Step 2: workshop_figure = S116-W1-HTILDE-RECON pinned OOM (declared space)
          [fallback INV12-W3-5: 4.76 A_s-space / 2.38 H̃-space]
  Step 3: A_s = squeeze × filter ⇒ OOM_product = OOM_squeeze + log10(filter)   [factorization]
          with filter from CF-AS-2 (substrate-derived 0.512 if PASS; else the fitted-knob band)
  Step 4: collapse_dist = min over regime-tagged routes |OOM_route − workshop_figure|
          S115 raw spread = 1.259 (TD/zeta +0.196 → Parker +1.455); regime-tagging groups
          sudden-end {+0.196,+0.824,+0.864} vs adiabatic-end {+1.455,+1.527}
  Step 5: within-cluster spread (≈0.67 sudden, ≈0.07 adiabatic) < cross-cluster spread (≈1.26)
          ⇒ collapse_dist shrinks under regime-tagging but stays > 0.1 (no single-figure collapse)
  Conclusion: PASS iff collapse_dist ≤ 0.1 (routes collapse, S115 PLURALISM overturned); INFO iff
          routes reproduce the S115 two-cluster axis (no collapse, the EXPECTED outcome given
          S115); FAIL iff routes neither collapse NOR reproduce S115 (a new inconsistency).
```

```yaml
gate_id: "S116-W1-AS-CF3"
schema_version: "R3"
gate_type: "compute"
trigger: "[SIGN]"
classification: "PHONONIC"
agent_type: "mack-cosmic-bridge"
hypothesis: "The regime-tagged A_s routes (A_s = squeeze × filter) either COLLAPSE onto the workshop-pinned OOM figure within 0.1 OOM (overturning S115 PLURALISM) or REPRODUCE the S115 sudden↔adiabatic two-cluster axis (no collapse); the n_s scheme variants (0.959/0.9561/0.9649) are regulator-consistent, not a contradiction."

method:
  description: |
    (1) Collect the route A_s/OOM set: squeeze (S116-W1-AS-CFB1 npz, fallback A_s_FW=1.5367e-8);
        Parker inv6 (5.99e-8); TD/zeta UNIFIED-AS-79 (3.2994e-9); and the product A_s = squeeze ×
        filter (filter from S116-W1-AS-CF2 npz: substrate-derived 0.512 if PASS, else the
        fitted-knob band). Compute OOM_route = log10(A_s_route/A_s_CMB) for each.
    (2) Regime-tag each route (sudden-end vs adiabatic-end per the S115 axis). Resolve the
        workshop-pinned figure from the S116-W1-HTILDE-RECON md (fallback INV12-W3-5 reconciled
        4.76 A_s-space / 2.38 H̃-space). Tag each upstream input FRESH-vs-FALLBACK.
    (3) Compute collapse_dist = min over regime-tagged routes |OOM_route − workshop_figure| and
        the cross-route spread. PASS iff collapse_dist ≤ 0.1 (S115 PLURALISM overturned); INFO
        iff the routes reproduce the S115 two-cluster axis (sudden vs adiabatic, no collapse);
        FAIL iff neither (a new inconsistency vs S115).
    (4) n_s scheme-split reconciliation: report n_s_FW_sqrt_cutoff=0.959 (sqrt-cutoff),
        n_s_framework=0.9561 (Route-B exact 9561/10000), n_s_canon=0.9649 (Planck) with explicit
        cutoff-scheme + (scale, channel) tags per scale-and-channel-tagging; the two framework
        values are regulator-variants (NOT a contradiction) iff their spread ≤ the cutoff-scheme
        band and both are RED (n_s<1). σ-distances to Planck reported (consistency sub-criterion).
  producing_script: "computations/session-116/s116_w1_as_cf3_route_reconcile.py"

operator:
  type: "set"
  form: "(collapse_dist ≤ 0.1 → PASS-collapse) XOR (routes reproduce S115 two-cluster axis → INFO-axis); AND (n_s scheme variants regulator-consistent: spread ≤ cutoff-band ∧ all RED)"
strict_PASS_boundary:
  value: "collapse_dist ≤ 0.10 OOM (PASS-collapse, overturns S115); else INFO if S115 axis reproduced (spread within tol of 1.259)"
  direction: "<="
boundary_reachable_analytically:
  bool: true
  proof_ref: "S115-AS-NEWAXIS-SELECTOR (spread_existing_OOM=1.2590, min_collapse_dist_OOM=0.6281, band 0.1); CC3 identity A_s∝H̃² (machine-ε, S82); INV12-W3-5 reconciled figure"
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous (OOM log-ratios + collapse distances)"
machinery_pin_map:
  N_eval: "route set (4-6 OOM figures) + 3 n_s scheme values"
  L_max: "12 (consistency with the squeeze/regime sources; n_s_framework Route-B exact)"
  scan_range: "route OOM set; n_s ∈ {0.959, 0.9561, 0.9649}; collapse-band 0.1"
  step_size: "N/A — closed-form reconciliation"
  tolerance: "collapse_dist ≤ 0.1 (PASS); S115-axis-reproduction spread within ±0.05 of 1.259 (INFO); n_s cutoff-scheme band; σ to Planck"
  scheme: "ROUTE-RECONCILIATION-REGIME-TAGGED"
  convention: "OOM-COLLAPSE-VS-S115-AXIS-AND-NS-SCHEME-SPLIT"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8 (scalar reconciliation; NO heavy linear algebra)"
  publication_precision: "4  (the reconciliation verdict + collapse_dist feed next-session A_s falsifier row)"
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap", "s116_w1_as_cfb1_npz_or_fallback", "s116_w1_as_cf2_npz_or_fallback", "s116_w1_htilde_recon_md_or_fallback"]
  content_sha256_inputs: ["script"]
substitution_chain:
  required: true
  content: |
    Step 1: routes = {squeeze +0.864, Parker +1.455, TD/zeta +0.196}, OOM=log10(A_s/A_s_CMB)
    Step 2: workshop_figure = S116-W1-HTILDE-RECON pinned OOM (fallback INV12-W3-5 4.76 A_s / 2.38 H̃)
    Step 3: A_s=squeeze×filter ⇒ OOM_product=OOM_squeeze+log10(filter) [filter from CF-AS-2]
    Step 4: collapse_dist=min|OOM_route − workshop_figure| after regime-tagging; S115 raw spread 1.259
    Step 5: within-cluster spread < cross-cluster ⇒ collapse_dist shrinks but stays > 0.1
    Conclusion: PASS iff collapse_dist ≤ 0.1 (S115 overturned); INFO iff S115 axis reproduced; FAIL iff neither.

fb_pair:
  forward: "S116-W1-AS-CFB1 (squeeze); S116-W1-AS-CF2 (filter); S116-W1-HTILDE-RECON (workshop figure); S111-CF-AS3a + S82 TD/zeta + S110 Parker (canonical fallback routes)"
  backward: "next-session A_s falsifier row (Row 8); atlas-08 Q23/CF21 status update; capstone §7 A_s anchor (mack sole-writer)"
dual_prior:
  track_A: "0.25 — the routes COLLAPSE (collapse_dist ≤ 0.1); a substrate principle (the workshop's canonical horizon-exit reading) singles out ONE A_s, OVERTURNING S115 PLURALISM"
  track_B: "0.75 — the routes REPRODUCE the S115 sudden↔adiabatic two-cluster axis (no collapse); PLURALISM-PERMANENT confirmed, A_s magnitude is a regime-axis not a point (EXPECTED given S115)"
  discriminator: "PASS (collapse) → 0.9 to Track A (S115 overturned); INFO (S115 axis reproduced) → 0.9 to Track B (PLURALISM confirmed); FAIL → neither, a new inconsistency requiring next-session re-derivation"

input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # consumed anchors (A_s_CMB, A_s_FW, n_s_FW_sqrt_cutoff, n_s_framework, n_s_canon) — runtime values pinned (§ii.B)
  s116_w1_as_cfb1:
    path: "computations/session-116/s116_w1_as_cfb1_squeeze_promote.npz"
    sha256: "<computed-at-runtime>"   # FRESH if CF-B1 landed; else FALLBACK A_s_FW=1.5367e-8 (disclosed in value=)
  s116_w1_as_cf2:
    path: "computations/session-116/s116_w1_as_cf2_greybody_exact.npz"
    sha256: "<computed-at-runtime>"   # FRESH if CF-AS-2 landed; else FALLBACK fitted 0.512 (disclosed in value=)
  s116_w1_htilde_recon:
    path: "sessions/session-116/workshops/s116-w1-htilde-recon.md"
    sha256: "<computed-at-runtime>"   # FRESH if workshop landed; else FALLBACK INV12-W3-5 4.76 A_s-space / 2.38 H̃-space (disclosed in value=)

PASS_meaning: "The regime-tagged routes COLLAPSE onto the workshop-pinned figure within 0.1 OOM — a substrate principle (the canonical horizon-exit reading) singles out ONE A_s, OVERTURNING the S115 PLURALISM verdict. A_s closure is convention-blocked and now achieved: the magnitude is a single prediction."
FAIL_meaning: "The routes neither collapse NOR reproduce the S115 axis — a NEW inconsistency between the squeeze×filter product and the established routes. Routes to next-session re-derivation; the A_s magnitude map has an unmapped contradiction."
INFO_meaning: "The routes REPRODUCE the S115 sudden↔adiabatic two-cluster axis (no collapse, collapse_dist > 0.1) — PLURALISM-PERMANENT is CONFIRMED across the squeeze×filter product. A_s magnitude is a physical regime-axis, NOT a single point; closure is physics-blocked (the EXPECTED outcome given S115). The n_s scheme variants are regulator-consistent."

effort:
  files_created:
    - "computations/session-116/s116_w1_as_cf3_route_reconcile.py"
    - "computations/session-116/s116_w1_as_cf3_route_reconcile.npz"
    - "computations/session-116/s116_w1_as_cf3_route_reconcile.png"
  estimated_time: "0.5 day"

substrate_framing: |
  PHONONIC. A_s IS the GGE-relic acoustic squeezing modulus; A_s = (squeeze |β|²) × (exit
  greybody filter). The substrate produces ONE relic state; the "routes" are different
  normalization/regime readings of its squeeze × filter. The reconciliation asks whether the
  substrate's own canonical horizon-exit reading singles out ONE A_s (convention-blocked,
  collapse) or whether the sudden↔adiabatic regime axis is a genuine physical degree of freedom
  the CMB samples a point of (physics-blocked, S115 PLURALISM). The lab measures A_s IN the CMB
  container; the n_s scheme variants are cutoff-scheme images of the SAME geometric tilt
  1−2ε_H, carried to the pivot by deg(T_BZ→pivot)=+2 — declared with (scale, channel) tags, not
  conflated.

output_artifacts:
  script:
    path: "computations/session-116/s116_w1_as_cf3_route_reconcile.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/session-116/s116_w1_as_cf3_route_reconcile.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-116/s116_w1_as_cf3_route_reconcile.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-116/s116_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S116-W1-AS-CF3:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true   # [SIGN] trigger (collapse-direction)
  wp_section:
    path: "sessions/session-116/session-116-w1-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W1-4. S116-W1-AS-CF3"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"
```

---

## Wave 1 → Wave 2 Decision Point

**Intra-wave ordering** (within Wave 1):
- The workshop + CF-B1 + CF-AS-2 are mutually independent → dispatch in parallel (one batch).
- CF-AS-3 consumes all three → dispatch AFTER they close (second batch). Per the prereq table, CF-AS-3 falls back to canonical values for any upstream not landed (NOT hard-blocked; ≥1 fresh input → emit with FRESH/FALLBACK disclosure; all-fallback → PRE-REG-INC).

**Branching on Wave-1 outcomes** (carry-forward, NOT gating Wave 2 — Q18b is an independent question):
- **CF-B1 PASS (POINT)** → the squeeze magnitude is a converged physical d.o.f.; promote `A_s_squeeze` to `canonical_constants.py` (Step-2 write-order) and the falsifier-inventory row (mack). **CF-B1 INFO (BAND)** → the AS3b epistemic type is BAND; carry the L_max-soft caveat to the falsifier row. **CF-B1 FAIL** → the box-delta ξ_KZ normalization is mis-identified; re-open the magnitude-source question next session.
- **CF-AS-2 PASS** → the exit greybody is substrate-derived (A2 knob removed); the A_s upper-edge closes; update CF23(b) from OPEN to CLOSED. **CF-AS-2 FAIL** → structural-closure (greybody irreducibly fitted); CF23(b) magnitude is permanently PLURALISM (floor + sudden↔adiabatic axis); retire the A2-knob upper-edge as non-substrate-derivable.
- **CF-AS-3 PASS** → S115 PLURALISM OVERTURNED; A_s magnitude is a single prediction; major Q23 closure. **CF-AS-3 INFO** → S115 PLURALISM CONFIRMED (expected); A_s magnitude is a regime-axis; Q23 closes as "α_s+n_s done, A_s = floor + sudden↔adiabatic axis." **CF-AS-3 FAIL** → new inconsistency; next-session re-derivation.
- **Workshop verdict** → pins ONE canonical OOM figure + convention/physics fork → routes the atlas-04/atlas-08 CF21 capstone-drift reconciliation to `session-116-housekeeping.md` §A (in-session prose fix, mack-cosmic-bridge for the §7/inventory surface per capstone-hygiene-gate.md Q2/Q3).

**Wave 2 (Q18b Yukawa)** is owned by `connes-ncg-theorist` and does NOT consume Wave-1 outputs (independent question). No cross-wave gating.

---

## Wave 1 Machinery-Enumeration Pin

Aggregate of all COMPUTE gate `machinery_pin_map` entries (the workshop contributes nothing — no producing script). This is what `_yaml_gate_validator.py` reads for the compute subset.

| Gate | N_eval | L_max | scan_range | tolerance | scheme | convention | GPU_path | pub_prec |
|:-----|:-------|:------|:-----------|:----------|:-------|:-----------|:---------|:---------|
| S116-W1-AS-CFB1 | 89 fold + ~64 box-delta | 12 (L7-eq cross-check; FB-sat L≥12) | L∈{L7eq,12}; OOM[+0.196,+1.527] | OOM band; L-stab ≤0.05; floor >1 | IMPULSE-QUENCH-BOGOLIUBOV | FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL-xiKZ | cpu-cap-OMP8 | 5 |
| S116-W1-AS-CF2 | ω~256, x_*~2048, Floquet~512 | 10 (relic lock) | barrier-scales {ω_q,relic_rms,γ_clock,2Δ_BCS,κ_exit}; ω[0.94,3.72] | agree RATIO ≤0.10; f_used ≥0.95; ODE-vs-Floquet ≤1e-8 | BdG-fluctuation-EXACT-finite-rate-scattering | DYNAMICAL-near-horizon-NON-WKB-ODE-AND-FLOQUET | cpu-cap-OMP8 | 4 |
| S116-W1-AS-CF3 | 4-6 routes + 3 n_s | 12 | route OOM set; n_s{0.959,0.9561,0.9649}; collapse 0.1 | collapse_dist ≤0.1; S115-axis ±0.05 of 1.259; n_s cutoff-band | ROUTE-RECONCILIATION-REGIME-TAGGED | OOM-COLLAPSE-VS-S115-AXIS-AND-NS-SCHEME-SPLIT | cpu-cap-OMP8 | 4 |

**No regulator_pin** (no gate cites a Seeley-DeWitt `a_n`; the squeeze/greybody are Bogoliubov/BdG-scattering observables, the n_s scheme variants are cutoff-SCHEMES handled by `(scale, channel)` tags, not `a_n^{regulator}` axes).
**No CLASS=SCHEMATIC pin** (no gate consumes a SCHEMATIC helper; all source spectra are FULL-physical box-delta / BdG-fluctuation evaluators).
**Feasibility**: all three are CPU-cap-OMP8 (few-mode β-sums, 1D scattering ODE, scalar reconciliation; NO ≥100×100 dense diagonalization). CF-B1's L_max-stability uses the EXISTING L12 cache + Friedrich-Bär saturation argument (NO L≥13 GT-builder re-diagonalization — math-scripts.md §D_K Block-Diagonality feasibility pre-check satisfied).

---

## Wave 1 Input-SHA Ledger

Every input file the Wave-1 COMPUTE gates consume (workshop `sources` listed for traceability; SHA advisory). All npz inputs use `<computed-at-runtime>` per `substrate-first-canonical-sourcing.md §(ii.B)` (numpy `.savez` zip-timestamp non-determinism — the load-bearing invariant is ARRAY CONTENT, verified against canonical values at runtime, NOT the byte-SHA). `canonical_constants.py` uses `<computed-at-runtime>` (edited mid-session by parallel waves; consumed anchors unchanged → ZERO physics effect). The tracked/git-canonical `s84_spectrum_cache_L12_tau019.npz` is runtime-asserted to match git (mechanical-closure HALT on drift, per S110 line 196).

| Input file | Consumed by | Plan-freeze SHA-256 (24-hex ref; runtime-pinned per §ii.B) |
|:-----------|:------------|:-----------------------------------------------------------|
| `computations/_shared/canonical_constants.py` | CFB1, CF2, CF3 | `261b117ce312968b036d3256…` (will drift; anchors stable) |
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | CFB1 | `9e6d9cf7fd6a6949d622441b…` (tracked; runtime-assert MUST match) |
| `computations/session-110/s110_cf_b1_transit_ps_promote.npz` | CFB1, workshop | `77cf08f0fa81fb11772dde4a…` |
| `computations/investigation-10/inv10_w2_transit_ps_build.npz` | CFB1 (via S110 lineage) | `a19ad05eb7d1937dedf36421…` |
| `computations/session-100b/s100b_box_delta_bogoliubov.npz` | CFB1 | `43275f5104d24305e88fd7c4…` |
| `computations/session-111/s111_cf_as3a_impulse_quench.npz` | CFB1, CF3 (fallback), workshop | `557b9c196e20c625269b6df8…` |
| `computations/investigation-12/inv12_w3_4_greybody_from_bdg.npz` | CF2 | `4f51d724945d586f603f5864…` |
| `computations/session-110/s110_cf_as2_greybody_scan.npz` | CF2 | `947c48851c06414b519cfbaa…` |
| `computations/session-95/s95_w4_3_hawking_greybody_as.npz` | CF2 | `6f9cda9bd28ad0c4cf5cb4c0…` |
| `computations/investigation-12/inv12_gate_verdicts.txt` | workshop (INV12-W3-5 reconciliation), CF3 (fallback figure) | `<computed-at-runtime>` |
| `computations/session-115/s115_gate_verdicts.txt` | workshop (S115 PLURALISM) | `<computed-at-runtime>` |
| `sessions/session-116/workshops/s116-w1-htilde-recon.md` | CF3 (FRESH; else INV12-W3-5 fallback) | `<computed-at-runtime — produced in-wave>` |
| `computations/session-116/s116_w1_as_cfb1_squeeze_promote.npz` | CF3 (FRESH; else A_s_FW fallback) | `<computed-at-runtime — produced in-wave>` |
| `computations/session-116/s116_w1_as_cf2_greybody_exact.npz` | CF3 (FRESH; else 0.512 fallback) | `<computed-at-runtime — produced in-wave>` |

**Canonical-constant pins** (consumed; values from knowledge-MCP at plan-freeze): `A_s_CMB = A_s_Planck = 2.1e-9` (S96-OBS-ANCHOR-HYGIENE); `A_s_FW = 1.5367059962762235e-8` (S111-CF-AS3a, NOT superseded); `xi_KZ_FW = 0.018760052113614718`; `n_s_FW_sqrt_cutoff = 0.959` (S103); `n_s_framework = 0.9561` (S85, exact 9561/10000); `n_s_canon = 0.9649` (Planck); `c_sub_baseline = 2.238`. Route anchors: TD/zeta UNIFIED-AS-79 A_s = 3.2994e-9 (+0.196 OOM); Parker inv6 A_s = 5.99e-8 (+1.455 OOM); fitted greybody Γ = 0.511872 (S95-W4-3). S115 axis: spread 1.259 OOM, min_collapse_dist 0.6281 (band 0.1). CC3 identity: `d(ln A_s)/d(ln H̃) = +2` (A_s ∝ H̃²; INV12-W3-5 cc3=2.000000).
