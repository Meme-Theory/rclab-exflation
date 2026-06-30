# Session 116 Plan — Wave 7: Q33 §VII.AJ.STATE-PROJ derivation

**Date**: 2026-06-27
**Author**: volovik-superfluid-universe-theorist (per-wave planner, /rclab-plan session-mode swarm)
**Owner agent**: volovik-superfluid-universe-theorist (3He-B inheritance authority; substrate-IS BCS state)
**Mode**: SESSION (session-116 namespace), MIXED gate types (1 compute + 1 workshop)
**Plan source**: `sessions/session-plan/session-116-context.md §"Wave 7 — Q33"` + `sessions/session-plan/session-116-partition.md §"Wave 7"`
**Working paper**: `sessions/session-116/session-116-w7-workingpaper.md`
**Verdict file (compute only)**: `computations/session-116/s116_gate_verdicts.txt`

## Wave 7 Summary

Wave 7 resolves open question **Q33** — the `§VII.AJ.STATE-PROJ` companion slot, OPEN (NEEDS-COMPUTATION) since S88 W7+W10. The §VII.AJ entry split into two structurally-orthogonal projection-side readings after the S87 W11-5 REGISTRY-FAIL (`S87-3HEB-EXCESS-INHERITANCE-COMPARISON`, FAIL at ratio_mismatch ≈ 1.03):

- **`§VII.AJ.OP-PROJ`** (STAGE-1-CANDIDATE; algebra-INVARIANT): a multiplicity-weighted Mellin-pole-window **spectrum-only count** observable that saturates monotonically to a universal `R_∞ ≈ −1.892 ± 0.001` as `L_max → ∞`. NEGATIVE; volovik-defended; NOT a lab-gap-asymmetry image.
- **`§VII.AJ.STATE-PROJ`** (OPEN; algebra-DEPENDENT): a **BCS-occupation state-pair functional** of algebraic shape `(a−b)/(a+b)` whose substrate-IS image must reproduce the laboratory `R_3HeB_lit = +0.03536` — the 3He A/B-phase gap-square asymmetry at the polycritical pressure `P_pc = 21.22 bar`. POSITIVE.

This wave carries TWO gates:

1. **`S116-W7-STATEPROJ-BCS`** (compute) — derive the substrate-IS STATE-PROJ observable `R_STATE = (a−b)/(a+b)` from the substrate's BdG BCS occupation distribution / condensation-energy state-pair functional, and pre-register whether it reproduces `+0.03536` and — the load-bearing discriminator — whether the substrate gap ratio that drives it is a **substrate-first** q-theory prediction (genuine, Track A) or the **lab strong-coupling ratio re-expressed** (consistency-check / circular, Track B).
2. **`S116-W7-ALGEBRA-AXIS`** (workshop, volovik × landau) — adjudicate whether STATE-PROJ (algebra-DEPENDENT, `R = +0.03536`) is a genuine substrate-IS observable **ORTHOGONAL** to OP-PROJ (algebra-INVARIANT, `R_∞ ≈ −1.892`) under the algebra-axis orthogonality K-counter (cross-corner co-primary FORBIDDEN), or whether the two projection-side readings **collapse** to one (which would be a finding against the K-counter conjecture).

The sign flip (OP-PROJ negative, STATE-PROJ positive) is the headline structural input to the workshop.

## Wave 7 Gate-Type Manifest

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W7-STATEPROJ-BCS | compute | BCS-grounded substrate-IS image of `R_3HeB = +0.03536` at `P_pc = 21.22 bar`; `(a−b)/(a+b)` state-pair shape; PASS vs published 4-sig-fig precision AND substrate-first-provenance Track-A discriminator |
| S116-W7-ALGEBRA-AXIS | workshop | volovik × landau: is STATE-PROJ (algebra-DEPENDENT) ORTHOGONAL to OP-PROJ (algebra-INVARIANT `R_∞ ≈ −1.892`) or do they collapse |

## Wave 7 Decision Point Prerequisites

- **`S116-W7-STATEPROJ-BCS`** consumes (all extant at S116 entry — no in-session prereq-block):
  - `Delta_BCS = 0.4642547394830737` (canonical, R-protected, gate `BCS-GAP-CANONICAL-70`).
  - `s84_spectrum_cache_L12_tau019.npz` (the cached D_K(τ_fold) sector spectrum; canonical substrate truncation L_max=10/12).
  - `computations/session-87/s87_w11_3heb_excess_inheritance_comparison.npz` (the S87 lab anchor `R_3HeB_lit` + OP-PROJ `R_substrate ≈ −1.2122` reference; the FAILED comparison that motivated the split).
  - The 3He-B polycritical literature anchors (`SC_corr_A = 1.151`, `SC_corr_B = 1.111`, `P_pc = 21.22 bar`, `T_pc = 2.273 mK`) — **NOT yet in `canonical_constants.py`** (see SOURCE-RECON note in the gate block; must be added with provenance before script import).
- **`S116-W7-ALGEBRA-AXIS`** (workshop) reads the two registry texts (atlas-07 §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ) + the algebra-axis orthogonality rule + the `S116-W7-STATEPROJ-BCS` output (the sign + value of `R_STATE`, the sign-flip evidence). The workshop dispatches AFTER the compute gate so it has `R_STATE`; its STRUCTURAL verdict is independently derivable from the registry texts (the orthogonality is an algebra-axis classification, not a numerical claim), so a compute INFO/FAIL does NOT block the workshop.

---

## §W7-1. S116-W7-STATEPROJ-BCS

```yaml
# ---- Identity (7 fields) ----
gate_id: "S116-W7-STATEPROJ-BCS"
schema_version: "R3"
gate_type: "compute"
trigger: "[SIGN]"                         # R_STATE = (a-b)/(a+b) > 0 directional claim
classification: "PHONONIC"                # BCS occupation of the substrate BdG state inherited via iota
agent_type: "volovik-superfluid-universe-theorist"   # 3He-B inheritance + substrate-IS BCS state owner; nazarewicz-nuclear-structure-theorist is the math cross-check for the strong-coupling gap equation
hypothesis: "The substrate's BdG BCS occupation distribution admits an algebra-DEPENDENT state-pair functional R_STATE = (a-b)/(a+b) (a,b = condensation-energy / pairing-occupation weights of the two inherited gap sectors) that reproduces the laboratory R_3HeB_lit = +0.03536 at the polycritical point, and the controlling gap ratio is a substrate-first q-theory prediction (Track A) rather than the lab strong-coupling ratio re-expressed (Track B)."

method:
  description: >
    Construct the substrate-IS STATE-PROJ observable as a state-pair functional on the
    3He-B BdG BCS ground state inherited from (A_K, H_K, D_K) via iota : C+H+M3(C) -> M2(C).
    The state-pair quantities a, b are the BCS condensation-energy weights of the two
    coexisting gap sectors at the polycritical point: a = |E_cond^A| = (1/2) N(0) Delta_A^2,
    b = |E_cond^B| = (1/2) N(0) Delta_B^2, evaluated as rho_BCS(P_A . H_pair) and
    rho_BCS(P_B . H_pair) with rho_BCS the BCS ground state and P_A, P_B the algebra-sector
    central projections (THIS is the algebra-DEPENDENT content distinguishing STATE-PROJ from
    the algebra-INVARIANT OP-PROJ spectrum-only count). Equivalently, on the substrate D_K
    spectrum, a, b are gap-weighted pairing-occupation moments Sum_k u_k v_k . Delta_sector /
    E_k(Delta_sector). At A-B coexistence (common N(0)) the form reduces to
    R_STATE = (Delta_A^2 - Delta_B^2)/(Delta_A^2 + Delta_B^2). The PRIMARY deliverable is NOT
    the numerical reproduction (which the form near-reproduces by construction) but the
    PROVENANCE of the substrate gap ratio Delta_B/Delta_A: the producing script MUST report
    whether Delta_B/Delta_A is computed from the substrate's OWN q-theory Volovik-partition
    strong-coupling correction (Track A, genuine 0-parameter prediction) or inherited as the
    3He lab strong-coupling ratio SC_corr_B/SC_corr_A = 1.111/1.151 (Track B, consistency-check).
  producing_script: "computations/session-116/s116_w7_stateproj_bcs.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "track-discriminator + ratio reproduction"
  form: >
    PRIMARY: provenance_of(Delta_B/Delta_A) in {SUBSTRATE_FIRST_QTHEORY (Track A),
    LAB_SC_RATIO (Track B)}.  SECONDARY (necessary, not sufficient):
    |R_STATE - R_3HeB_lit| / |R_3HeB_lit| <= 0.05.
    Composite = PASS iff (secondary holds AND Track A); INFO iff (secondary holds AND Track B);
    FAIL iff secondary fails.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "|R_STATE - R_3HeB_lit|/|R_3HeB_lit| <= 0.05  AND  Track == A (substrate-first gap ratio)"
  direction: "<="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "R_STATE = (Delta_A^2-Delta_B^2)/(Delta_A^2+Delta_B^2) closed form (condensation energy ∝ Delta^2); R_3HeB_lit = (SC_A^2-SC_B^2)/(SC_A^2+SC_B^2) = +0.035356 (substitution_chain below; weak-coupling factor cancels)"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — single-point evaluation at the polycritical (P_pc, T_pc); discriminator is a 2-branch provenance set, not a numerical mesh"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "78080"                         # unique D_K eigenvalues at L_max=10 (cached); occupation v_k^2 computed per mode. N/A if executor uses the closed-form (Delta_A^2-Delta_B^2)/(...) reduction
  L_max: "10"                             # canonical substrate truncation (matches OP-PROJ + S87)
  scan_range: "N/A — single polycritical point (P_pc=21.22 bar, T_pc=2.273 mK)"
  step_size: "N/A"
  tolerance: "5e-2"                       # secondary numerical band (relative); matches S87 ratio_mismatch PASS band
  scheme: "STATE-PROJ-BCS-condensation-energy-state-pair"
  convention: "(a-b)/(a+b)-A-B-coexistence-condensation-energy + STATE-PROJ"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8"                # occupation v_k^2 is a closed-form vector map on the cached spectrum; torch.linalg only if per-sector BdG 2x2 blocks are explicitly diagonalized
  publication_precision: "4"             # R_3HeB_lit published at 4 sig figs (+0.03536); downstream verifier rel_tol >= 1e-4 (Class 8.3)
  # CLASS: "FULL"                         # DECLARE iff producing_script imports _spectral_action_regulators.py (a SCHEMATIC helper, as the S87 script did). If the STATE-PROJ BCS occupation is built from canonical_constants + the cached spectrum ONLY, no SCHEMATIC helper is consumed and CLASS=FULL (no -SCHEMATIC suffix). If the executor reuses _enumerate_sectors/casimir_su3 from _spectral_action_regulators.py, CLASS=SCHEMATIC + convention=...-SCHEMATIC + `# tier_pin=TIER-2` companion row are MANDATORY (substrate-first-canonical-sourcing.md §(iv)).
  # regulator_pin: "N/A"                  # condensation energy ∝ Delta^2 is not a Seeley-DeWitt a_n; tag a_n^{ζ} ONLY if an a_2/a_4 spectral moment enters the occupation weight (regulator-pin-discipline.md)

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap", "s84_spectrum_cache", "s87_comparison_npz"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain — MANDATORY ([SIGN] trigger)
substitution_chain:
  required: true
  content: |
    Claim: "R_STATE = (a-b)/(a+b) > 0 (the substrate A-analog condensation energy exceeds the
            B-analog at the polycritical point), reproducing R_3HeB_lit = +0.03536."

    Def 1: a := |E_cond^A| = (1/2) N(0) Delta_A^2
           [BCS condensation energy of the A-phase-analog sector; a STATE functional
            <H>_BCS - <H>_normal on the substrate BdG state rho_BCS = algebra-DEPENDENT]
    Def 2: b := |E_cond^B| = (1/2) N(0) Delta_B^2
           [B-phase-analog condensation energy; common N(0) at A-B coexistence (polycritical)]
    Def 3: Delta_A = (pi e^{-gamma}) . SC_A,  Delta_B = (pi e^{-gamma}) . SC_B
           [weak-coupling BCS gap ratio (pi e^{-gamma} = 1.763869) x strong-coupling correction]
           SC_A = 1.151, SC_B = 1.111   [Serene-Rainer 1983 / Volovik 2003 Ch.7 at P_pc; OR
                                         the substrate q-theory Volovik-partition prediction]

    Substitute Def 1, Def 2 into R_STATE = (a-b)/(a+b):
           R_STATE = ( (1/2)N(0)Delta_A^2 - (1/2)N(0)Delta_B^2 )
                     / ( (1/2)N(0)Delta_A^2 + (1/2)N(0)Delta_B^2 )
    Simplify ((1/2)N(0) cancels):
           = (Delta_A^2 - Delta_B^2)/(Delta_A^2 + Delta_B^2)
    Substitute Def 3 ((pi e^{-gamma})^2 cancels):
           = (SC_A^2 - SC_B^2)/(SC_A^2 + SC_B^2)
           = (1.151^2 - 1.111^2)/(1.151^2 + 1.111^2)
           = (1.324801 - 1.234321)/(1.324801 + 1.234321)
           = 0.090480 / 2.559122
    Canonical form: R_STATE = +0.0353564
    Direction: SC_A = 1.151 > SC_B = 1.111  =>  SC_A^2 > SC_B^2  =>  numerator > 0  =>  R_STATE > 0
    Conclusion: R_STATE = +0.03536 > 0 reproduces R_3HeB_lit = +0.03536 in sign AND magnitude.
                The sign is OPPOSITE to §VII.AJ.OP-PROJ (R_∞ ≈ -1.892 < 0): a spectrum-only count
                excess is negative; a condensation-energy occupation asymmetry is positive. The
                sign flip is structural evidence the two projection-side observables are orthogonal
                (different sign, different algebra-axis corner) — input to the W7-2 workshop.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  s84_spectrum_cache:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "<computed-at-runtime>"
  s87_comparison_npz:
    path: "computations/session-87/s87_w11_3heb_excess_inheritance_comparison.npz"
    sha256: "<computed-at-runtime>"
  volovik_paper_03:
    path: "researchers/Volovik/03_2008_Volovik_Emergent_Physics_Fermi_Point.md"
    sha256: "<computed-at-runtime>"   # methodological cross-check (substrate-first-canonical-sourcing.md §i)

# ---- Conditional blocks ----
fb_pair:
  forward: "S87-3HEB-EXCESS-INHERITANCE-COMPARISON (the FAILED comparison motivating the OP/STATE split); §VII.AJ.OP-PROJ STAGE-1-CANDIDATE (companion); Delta_BCS canonical (BCS-GAP-CANONICAL-70); the substrate q-theory Volovik-partition gap ratio"
  backward: "§VII.AJ.STATE-PROJ registry-slot landing (conditional on PASS); S116-W7-ALGEBRA-AXIS workshop (consumes R_STATE sign + value); the algebra-axis orthogonality K-counter; future 3He-B polycritical falsifier rows"

dual_prior:
  track_A: "Genuine substrate-first 0-parameter prediction: Delta_B/Delta_A computed from the substrate's OWN q-theory Volovik-partition strong-coupling correction, INDEPENDENT of the 3He lab SC corrections. Prior 0.5."
  track_B: "Consistency-check / circular: Delta_B/Delta_A = the 3He lab strong-coupling ratio SC_corr_B/SC_corr_A = 1.111/1.151 re-expressed; then R_STATE = R_3HeB_lit by construction (a tautology, NOT a prediction). Prior 0.5."
  discriminator: "PASS (numerical reproduction within band AND Track A provenance) -> 0.85 to Track A. INFO (numerical reproduction within band AND Track B provenance) -> 0.85 to Track B. FAIL (no numerical reproduction, >0.25 relative) -> the BCS-occupation state-pair functional does NOT image the lab gap-asymmetry; STATE-PROJ slot mis-specified. The producing script MUST explicitly trace the provenance of every factor in Delta_B/Delta_A and emit the Track label in the verdict value string."

# composite-precedence (plan-frozen operator; gate-verdicts.md §"Plan-frozen gate-block operator precedence"):
#   The generic 3-tuple collapse (sign=PASS, magnitude=PASS, regime=VALID => composite PASS)
#   is OVERRIDDEN by the dual_prior track discriminator: composite = PASS iff (3-tuple PASS AND
#   Track A); composite = INFO iff (3-tuple PASS AND Track B); composite = FAIL iff magnitude FAIL.
#   The producing script MUST emit a `# composite-precedence: dual_prior-track-discriminator
#   (W7-1; generic-collapse PASS overridden to INFO under Track B)` companion row, DECLARED here
#   before evaluation. This closes the load-and-compare-to-self / vacuous-margin failure mode:
#   the gate's content is the PROVENANCE discriminator, NOT the near-tautological numerical match.

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-116/s116_w7_stateproj_bcs.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/session-116/s116_w7_stateproj_bcs.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/session-116/s116_w7_stateproj_bcs.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/session-116/s116_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^S116-W7-STATEPROJ-BCS:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true       # [SIGN] trigger
  wp_section:
    path: "sessions/session-116/session-116-w7-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W7-1. S116-W7-STATEPROJ-BCS"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  Solution space: the substrate's BCS-occupation state-pair functional reproduces the lab
  polycritical gap-asymmetry +0.03536 AND the controlling gap ratio is a substrate-first
  q-theory prediction. §VII.AJ.STATE-PROJ is registry-PASS-eligible as a genuine 0-parameter
  substrate-IS image (algebra-DEPENDENT corner), orthogonal companion to the algebra-INVARIANT
  OP-PROJ. Land the slot with the 5-anatomy + 3-level ladder (see registry-landing block below).
FAIL_meaning: >
  Solution space: the BCS-occupation state-pair functional does NOT image the lab gap-asymmetry
  (>0.25 relative). The STATE-PROJ slot as a (a-b)/(a+b) condensation-energy form is mis-specified;
  the substrate's image of the lab polycritical asymmetry lives elsewhere (re-open Q33 with a
  different state-pair observable). §VII.AJ.STATE-PROJ stays OPEN.
INFO_meaning: >
  Solution space: the form reproduces +0.03536 BUT only because Delta_B/Delta_A is the lab SC
  ratio re-expressed (Track B) — a consistency-check, not a prediction. §VII.AJ.STATE-PROJ is
  RESERVED as REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (cross-pillar-bridge-anatomy.md): the
  slot is well-defined (algebra-DEPENDENT state-pair functional) but its substrate-first
  prediction content awaits an independent substrate derivation of the strong-coupling
  corrections SC_corr_A, SC_corr_B (the refinement pathway is a substrate q-theory / spectral-
  action strong-coupling computation). Carry-forward CF-S117-STATEPROJ-SC-FROM-SUBSTRATE.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-116/s116_w7_stateproj_bcs.py"
    - "computations/session-116/s116_w7_stateproj_bcs.npz"
    - "computations/session-116/s116_w7_stateproj_bcs.png"
  estimated_time: "0.5-1 day (BCS occupation closed-form + provenance trace of the gap ratio; the depth is the Track-A/B discrimination, not the arithmetic)"

substrate_framing: |
  The substrate IS the BdG BCS ground state on (A_K, H_K, D_K); the 3He-B cell is NOT a
  container the substrate lives in but a controlled realization of the same BDI universality
  class (parent->child inheritance morphism iota, NOT analogy; sessions/framework/correspondence/
  3HeB-inheritance-canonical.md). Direction of explanation: D_K eigenvalues -> BdG occupation
  v_k^2 in the BCS state -> condensation-energy state-pair functional rho_BCS(P_sector . H_pair)
  -> R_STATE = (a-b)/(a+b) -> the lab measures R_3HeB_lit = (Delta_A^2-Delta_B^2)/(...) IN the
  cryostat at the polycritical point. STATE-PROJ is algebra-DEPENDENT: it is a state-pair
  functional on the algebra A_K (it weights the BCS state ρ against the sector central
  projections P_A, P_B), structurally distinct from the algebra-INVARIANT OP-PROJ spectrum-only
  count F({λ_k, m_k}) = Σ_k m_k g(λ_k). The positive sign (A-analog more deeply paired) is the
  substrate's prediction direction; it is opposite to the negative OP-PROJ count excess.
```

### §W7-1 registry-landing block (CONDITIONAL on PASS) — 5-anatomy + 3-level ladder

If `S116-W7-STATEPROJ-BCS` returns **PASS** (Track A), the executor lands `§VII.AJ.STATE-PROJ` in `sessions/permanent-results-registry.md` carrying the full discipline (`cross-pillar-bridge-anatomy.md` + `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` — the slot already carries the mandatory `.STATE-PROJ` suffix). On **INFO**, the slot is tagged `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` (S2 advisory; slot RESERVED, not registry-PASS). On **FAIL**, the slot stays OPEN.

**5 IS-not-IN anatomy elements**:
1. **Substrate-IS observable** — `R_STATE = (a−b)/(a+b)`, the BCS condensation-energy / pairing-occupation **state-pair functional** `a = ρ_BCS(P_A · H_pair)`, `b = ρ_BCS(P_B · H_pair)` on the substrate BdG state inherited from `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. **Level-1 tag (single-τ-slice)**: τ_fold = 0.190.
2. **Laboratory-IN observable** — `R_3HeB_lit = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²)` measured at the polycritical point `P_pc = 21.22 bar`, `T_pc = 2.273 mK` IN a 3He cryostat (Greywall 1986 + Serene-Rainer 1983 strong-coupling). **OE-form**: `R_3HeB_lit = [Tr(P_A ρ_pair) − Tr(P_B ρ_pair)] / [Tr(P_A ρ_pair) + Tr(P_B ρ_pair)]` (state-pair trace; degenerate ∑ for the two-sector finite rank).
3. **Bridge map** — inheritance morphism `ι_* : A_K = ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)` (BDI→BdG child) ∘ `(Δ_B/Δ_A)^{p=0}` cancellation (ratio observable ⇒ `p=0` trivial cancellation; NOT "analogous to"). **algebra-DEPENDENT** corner ⇒ regulator-INVARIANT (IR-self-regularized by the gap `|Δ|`; algebra-axis sibling discriminator).
4. **Algebraic envelope (Level 2)** — because the observable is an algebra-DEPENDENT state-pair functional on a GAPPED occupation distribution, it is regulator-INVARIANT; the Level-2 envelope is **binding** via the BCS gap-equation self-consistency band on `Δ_B/Δ_A` (NOT an `L^{−α}` truncation envelope). Declare the binding `c_continuum` = the lab `R_3HeB_lit` and the band = the substrate q-theory gap-ratio precision.
5. **Empirical anchor (Level 3)** — `R_STATE` reproduces `+0.03536` within the published 4-sig-fig precision; Level-3 residual `< ` Level-2 band ⇒ registry-PASS.

**Algebra-axis corner declaration** (MANDATORY, `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`): STATE-PROJ = **algebra-DEPENDENT** (state-pair functional on `A_K`). Companion OP-PROJ = algebra-INVARIANT (spectrum-only). **Cross-corner co-primary FORBIDDEN** — STATE-PROJ and OP-PROJ are structural-orthogonal companions, NEVER co-primary anchors of a single theorem.

---

## §W7-2. S116-W7-ALGEBRA-AXIS

```yaml
# ---- Identity ----
gate_id: "S116-W7-ALGEBRA-AXIS"
schema_version: "R3"
gate_type: "workshop"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "volovik-superfluid-universe-theorist"    # wave owner; workshop participant (Axis: substrate / superfluid-universe)
hypothesis: "§VII.AJ.STATE-PROJ (R = +0.03536, algebra-DEPENDENT state-pair functional) and §VII.AJ.OP-PROJ (R_∞ ≈ -1.892, algebra-INVARIANT spectrum-only functional) are STRUCTURALLY ORTHOGONAL substrate-IS observables (different algebra-axis corners; cross-corner co-primary FORBIDDEN), NOT two readings of one observable that collapse."

# ---- workshop block (REQUIRED for gate_type: workshop) ----
workshop:
  agents: ["volovik-superfluid-universe-theorist", "landau-condensed-matter-theorist"]
  rounds: 3                               # R1 steelman / R2 respond to opponent's best case / R3 converge -> STRUCTURAL VERDICT
  sources:
    - "sessions/framework/Atlas/atlas-07-permanent-results.md (§VII.AJ.OP-PROJ STAGE-1-CANDIDATE R_∞ ≈ -1.892, algebra-INVARIANT; §VII.AJ.STATE-PROJ OPEN R_3HeB_lit = +0.03536, algebra-DEPENDENT)"
    - ".claude/rules/cross-pillar-bridge-anatomy.md (§\"Algebra-axis orthogonality K-counter\" MANDATORY at K=3; §\"Regulator-behavior sibling discriminator\")"
    - ".claude/rules/registry-landing.md (§\"Operator-Projection Reading-A Naming Hygiene\" — OP-PROJ / STATE-PROJ suffix discipline)"
    - "computations/session-87/s87_w11_3heb_excess_inheritance_comparison.py (the S87 R_substrate ≈ -1.2122 NEGATIVE spectral count vs R_3HeB_lit = +0.03536 POSITIVE lab asymmetry; the FAIL that split §VII.AJ)"
    - "computations/session-116/s116_w7_stateproj_bcs.npz (the W7-1 R_STATE result + sign + Track-A/B provenance)"
  output_path: "sessions/session-116/workshops/s116-w7-algebra-axis.md"
  adjudication_question: |
    Is §VII.AJ.STATE-PROJ (R = +0.03536; algebra-DEPENDENT state-pair functional on the BCS
    occupation) a genuine substrate-IS observable ORTHOGONAL to §VII.AJ.OP-PROJ (R_∞ ≈ -1.892;
    algebra-INVARIANT spectrum-only multiplicity-weighted Mellin-pole-window count), or do the
    two projection-side readings COLLAPSE to one observable?
    Sub-questions:
    (a) PARSE-TREE STRUCTURE: does STATE-PROJ parse to a state-pair functional ρ(P · A) (Corner
        III/IV, algebra-DEPENDENT) and OP-PROJ to a spectrum-only F({λ_k, m_k}) (Corner I/II,
        algebra-INVARIANT), placing them in DISTINCT corners of the §VII.U.2 4-corner partition?
    (b) SIGN FLIP: is the OP-PROJ-negative / STATE-PROJ-positive sign flip evidence of orthogonality
        (two physically different observables), or evidence that the OP-PROJ spectral count is a
        MIS-SPECIFIED image of the lab gap-asymmetry (landau's steelman: only STATE-PROJ is the
        correct substrate image; OP-PROJ is spurious, so there is really ONE observable, not two)?
    (c) BCS MEAN-FIELD COLLAPSE: does the BCS gap equation LINK the spectral count (OP-PROJ) and the
        occupation asymmetry (STATE-PROJ) so tightly that in the mean-field limit they are the same
        observable measured two ways (collapse), or does the gap-self-regularization of the
        state-pair functional (regulator-INVARIANT) vs the regulator-DEPENDENT spectrum count
        (algebra-axis sibling discriminator) keep them structurally separate (orthogonal)?
  context: |
    GENUINE adversarial tension (Q1 math/physics adjudication per Investigating-Workshops.md):
    - volovik position (ORTHOGONAL): STATE-PROJ and OP-PROJ are in DIFFERENT corners of the
      algebra-axis 4-corner partition. OP-PROJ is a spectrum-only count F({λ_k, m_k}) = Σ m_k g(λ_k)
      (algebra-INVARIANT, regulator-DEPENDENT, NEGATIVE topological/spectral excess). STATE-PROJ is a
      state-pair functional ρ_BCS(P_sector · H_pair) (algebra-DEPENDENT, regulator-INVARIANT / gap-
      self-regularized, POSITIVE occupation asymmetry). Per the K-counter (MANDATORY at K=3), the two
      families are STRUCTURALLY ORTHOGONAL in identity-class membership; cross-corner co-primary is
      FORBIDDEN. The wildly different values (-1.892 vs +0.03536) and the SIGN FLIP are EXPECTED —
      they measure different physical quantities on the same nominal (algebra, projector, pole)
      triple but differ in projection side. This is the inaugural physical (3He-B) instance of the
      orthogonality conjecture.
    - landau position (COLLAPSE / steelman the adversary): the two are the SAME 3He-B gap-anisotropy
      observable measured two ways; a spectral count and an occupation asymmetry are LINKED by the
      BCS gap equation (the occupation v_k^2 IS a functional of the same D_K spectrum the count uses),
      so in the mean-field limit they are not independent. The -1.892 vs +0.03536 split is then a
      SIGN that the OP-PROJ spectral count is a mis-specified image of the lab asymmetry (only
      STATE-PROJ is correct), collapsing §VII.AJ to ONE genuine observable plus one spurious one —
      NOT two orthogonal substrate-IS observables. If landau prevails, the algebra-axis orthogonality
      K-counter takes a hit at its first physical-realization test.
    Numeric stakes: OP-PROJ R_∞ ≈ -1.892 ± 0.001 (algebra-INVARIANT, Mellin-pole-window saturation);
    STATE-PROJ R = +0.03536 (algebra-DEPENDENT, polycritical gap-asymmetry); S87 substrate count
    R_substrate ≈ -1.2122 (L_max=10, the value extrapolated to OP-PROJ); ratio_mismatch ≈ 1.03 (the
    S87 FAIL). Adjudication rule: resolve from FIRST PRINCIPLES which reading is correct (the 4-corner
    parse-tree classification + the regulator-response sibling discriminator + the BCS gap-equation
    linkage), producing a STRUCTURAL VERDICT (orthogonal vs collapse) that either CONFIRMS the
    algebra-axis K-counter at its first physical instance or registers a structural exception.

# ---- Output artifacts (workshop closure = artifact-existence; NO verdict line) ----
output_artifacts:
  workshop_md:
    path: "sessions/session-116/workshops/s116-w7-algebra-axis.md"
    artifact_kind: "workshop_md"
    must_contain:
      - "## R1"
      - "## R2"
      - "## R3"
      - "## Structural Verdict"

# ---- Verdict rubric (artifact-existence; the STRUCTURAL VERDICT is the deliverable) ----
PASS_meaning: "N/A (workshop). Closes by artifact-existence: the workshop md exists with R1/R2/R3 rounds + a ## Structural Verdict resolving orthogonal-vs-collapse from first principles."
FAIL_meaning: "N/A (workshop)."
INFO_meaning: "N/A (workshop)."

# ---- Effort + framing ----
effort:
  files_created:
    - "sessions/session-116/workshops/s116-w7-algebra-axis.md"
  estimated_time: "0.5 day (3-round 2-agent adjudication)"

substrate_framing: |
  Both projection-side observables are substrate-IS on (A_K, H_K, D_K); the workshop decides
  whether they are orthogonal companions or a collapse. Direction preserved: D_K eigenvalues ->
  {spectrum-only count (OP-PROJ) | BCS-state occupation asymmetry (STATE-PROJ)} -> lab 3He-B
  observables. The 4-corner algebra-axis partition is the structural arbiter; the BCS gap equation
  is the candidate collapse mechanism landau must wield, the regulator-response sibling
  discriminator is the candidate separation mechanism volovik must wield.
```

---

## Wave 7 → Session Decision Point

- **`S116-W7-STATEPROJ-BCS` PASS (Track A)** → land `§VII.AJ.STATE-PROJ` registry value (5-anatomy + 3-level, STATE-PROJ suffix); the `S116-W7-ALGEBRA-AXIS` workshop then confirms the orthogonal-companion structure (OP-PROJ ⊥ STATE-PROJ) and advances the algebra-axis K-counter at its first physical instance. Promote `R_STATE_FW` to `canonical_constants.py` (canonical write-order: verdict → canonical → inventory).
- **`S116-W7-STATEPROJ-BCS` INFO (Track B)** → slot RESERVED `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`; carry-forward `CF-S117-STATEPROJ-SC-FROM-SUBSTRATE` (independent substrate derivation of `SC_corr_A`, `SC_corr_B` from the q-theory / spectral-action strong-coupling partition). The workshop still adjudicates orthogonality (structural, registry-text-grounded).
- **`S116-W7-STATEPROJ-BCS` FAIL** → `§VII.AJ.STATE-PROJ` stays OPEN; re-open Q33 with a different state-pair observable; the workshop's verdict on whether OP-PROJ alone survives becomes load-bearing.
- **`S116-W7-ALGEBRA-AXIS` Structural Verdict = ORTHOGONAL** → confirms the algebra-axis orthogonality K-counter; OP-PROJ + STATE-PROJ registered as structural-orthogonal companions (never co-primary).
- **`S116-W7-ALGEBRA-AXIS` Structural Verdict = COLLAPSE** → registers a structural exception to the K-counter at its first physical test; routes a methodology carry-forward to re-examine the conjecture's physical-realization scope.

## Wave 7 Machinery-Enumeration Pin

Aggregate of COMPUTE-gate `machinery_pin_map` entries (the workshop gate contributes nothing — no producing script):

| Gate | N_eval | L_max | scheme | convention | tolerance | publication_precision | GPU_path |
|:-----|:-------|:------|:-------|:-----------|:----------|:----------------------|:---------|
| S116-W7-STATEPROJ-BCS | 78080 (or N/A closed-form) | 10 | STATE-PROJ-BCS-condensation-energy-state-pair | (a−b)/(a+b)-A-B-coexistence + STATE-PROJ | 5e-2 | 4 | cpu-cap-OMP8 |

**SOURCE-RECON / SUBSTRATE-FIRST-PROVENANCE flag (MANDATORY pre-step)**: the 3He-B polycritical literature anchors `SC_corr_A = 1.151`, `SC_corr_B = 1.111`, `P_pc = 21.22 bar`, `T_pc = 2.273 mK`, and the derived target `R_3HeB_lit = +0.035356` are **NOT in `canonical_constants.py`** (verified via `get_constant` + grep at plan-freeze). They are external-paper **laboratory-IN** anchors (Greywall 1986 PRB 33 7520; Serene-Rainer 1983; Volovik 2003 Ch.7). Per `math-scripts.md` ("add new constants to `canonical_constants.py` FIRST if they don't exist") and the canonical write-order, the executor MUST add them to `canonical_constants.py` with explicit literature provenance BEFORE the producing script imports them (the S87 script carried them as `# (local)` literals — acceptable historically, but a NEW S116 script using them in a 2nd location crosses the 3-script threshold and they belong in the canonical module). The substrate q-theory gap ratio (if Track A) is substrate-first and needs no external anchor; `Delta_BCS = 0.4642547394830737` is already canonical (R-protected). This pre-step is the Class-(f) PIN-PLACEHOLDER remediation analog: substitute the canonical (here: ADD the canonical with provenance) before the gate runs.

## Wave 7 Input-SHA Ledger

| Input file | Consumer gate | SHA pin |
|:-----------|:--------------|:--------|
| `computations/_shared/canonical_constants.py` | S116-W7-STATEPROJ-BCS | `<computed-at-runtime>` |
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | S116-W7-STATEPROJ-BCS | `<computed-at-runtime>` |
| `computations/session-87/s87_w11_3heb_excess_inheritance_comparison.npz` | S116-W7-STATEPROJ-BCS | `<computed-at-runtime>` |
| `researchers/Volovik/03_2008_Volovik_Emergent_Physics_Fermi_Point.md` | S116-W7-STATEPROJ-BCS (methodological) | `<computed-at-runtime>` |
| `sessions/framework/Atlas/atlas-07-permanent-results.md` | S116-W7-ALGEBRA-AXIS (workshop source; advisory) | `<computed-at-runtime>` |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | S116-W7-ALGEBRA-AXIS (workshop source; advisory) | `<computed-at-runtime>` |
| `computations/session-87/s87_w11_3heb_excess_inheritance_comparison.py` | S116-W7-ALGEBRA-AXIS (workshop source; advisory) | `<computed-at-runtime>` |
| `computations/session-116/s116_w7_stateproj_bcs.npz` | S116-W7-ALGEBRA-AXIS (workshop source; produced by W7-1) | `<computed-at-runtime>` |
