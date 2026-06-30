# Session 88 Plan — Wave 4b: FWD-C1/C2/C3 cross-pillar bridge landings + K=3 promotion auto-flip

> **Author**: planner-w4b (mack-cosmic-bridge orchestrator role)
> **Theme**: Land the three forward cross-pillar bridge candidates (FWD-C1, FWD-C2, FWD-C3) pre-registered at S87 W5-5 in `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)", and pre-register the K=3 auto-flip gate that promotes the cross-pillar-bridge-anatomy SUGGESTION to MANDATORY upon the third FWD-candidate landing.
> **Writer**: mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`)
> **Verdict source**: `computations/s88_gate_verdicts.txt`
> **Script prefix**: `s88_w4b_<slug>.py`

## Wave 4b Summary

Wave 4b lands the FWD-C1 (Pillar I ↔ Pillar II, substrate ↔ cosmology measurement, n_s spectral-action), FWD-C2 (Pillar II ↔ Pillar V, Mellin-cone ↔ BdG spectral triple), and FWD-C3 (Pillar IV ↔ Pillar V, substrate cocycles ↔ 3He-B/3He-A laboratory observables) cross-pillar bridge candidates pre-registered as design SUGGESTIONS at S87 W5-5 close. Each candidate is registry-landed under the 5-element IS-not-IN anatomy + 3-level structural-confidence ladder, with the registry-PASS criterion (Level-3 empirical anchor < Level-2 algebraic envelope at canonical L_max) explicitly evaluated.

Wave 4b also pre-registers the K=3 auto-flip gate (`S88-OR-LATER-CF-D-K3-PROMOTION-AUTO-FLIP`): when the third FWD-candidate landing fires (any of #21/#22/#23 PASSing the registry-landing criterion), the orchestrator promotes `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)" from SUGGESTION (K=2 at S87 close) to MANDATORY in the same dispatch. The auto-flip is structurally triggered (instance count), not narratively argued, per the `feedback_fix-in-session-never-defer.md` discipline.

The K-counter at S87 close is K=2: instance #1 = S86 W-5 Pillar III ↔ Pillar IV bridge theorem (LANDED §VII.AF.1; volovik PRIMARY + connes CO-AUTHOR); instance #2 = S87 W11-5 FWD-C3 sub-instance (REGISTRY-FAIL Level-3 ratio_mismatch=1.029 violates Level-2 envelope 0.05 by ~21×; structural cause = M_3(C) Cartan-zone weight non-negligible at L_max=10). K=2 < K_promotion=3 ⇒ rule-status SUGGESTION at S88-open.

Wave 4b is the K=3 saturation event PROVIDED at least one of FWD-C1/C2/C3 lands as registry-PASS (Level-3 < Level-2). REGISTRY-FAIL landings still count toward K (per W11-5 precedent: REGISTRY-FAIL is a valid calibration-corpus instance, the structural pattern is exercised). Each gate's verdict either advances K-counter or remains at the prior K state if the gate is BLOCKED on upstream prerequisites that cannot land in S88.

### Wave 4b registry-anchor structure

All four gates use **SOURCE-DOUBLE-CITE-CO-PRIMARY** anchor structure per `.claude/rules/registry-landing.md`. The V_input layer supplies the substrate-IS observable provenance (a computations/_shared script + canonical_constants pin); the C_output layer supplies the bridge-map theorem (cross-pillar-bridge-anatomy.md §"Audit at plan-freeze" + the relevant Pillar-pair structural derivation). Neither layer alone fixes the conclusion: V_input alone gives a substrate quantity without a laboratory image; C_output alone gives a bridge structure without a substrate anchor.

### Wave 4b classification per `wave-classification.md` §M1-M4

- **#21 / #22 / #23** (FWD-C1/C2/C3 bridge landings) — **GEOMETRIC** class (per `phononic-framing.md` classification guide: registry entries on the spectral triple structure / cross-pillar bridge map / algebraic envelope are GEOMETRIC, not PHONONIC excitation-class results). Wave-classification: **COMPUTE-class** (M1 violated: PASS predicate is `Level-3 < Level-2` numerical comparison, not artifact-existence). Producing operations: computation script + npz data + verdict line + working-paper section + registry-entry append.
- **#24** (K=3 auto-flip) — **METHODOLOGY** class (rule-file edit only, no numerical computation). Wave-classification: **METHODOLOGY-class** per M1 (artifact-existence-with-substantive-content predicate: "rule-file diff exists, mode marker `MANDATORY` present, K-counter row =3"), M2 (`Edit` on `.claude/rules/cross-pillar-bridge-anatomy.md`), M3 (verbatim sub-diff from W5-5 pre-registration + W11-5 registry-FAIL instance + Wave-4b instance #3), M4 (allowlist append required at plan-freeze; see Wave 4b methodology-allowlist append below).

### Methodology-allowlist append (M4 substrate for #24)

The orchestrator appends the following row to `.claude/rules/methodology-wave-allowlist.md` AT PLAN-FREEZE TIME (recursion-attack closure: only orchestrator edits; subagents harness-denied):

```
| W4b-24 | S88 | S88-OR-LATER-CF-D-K3-PROMOTION-AUTO-FLIP (cross-pillar-bridge-anatomy.md §"Forward template-adoption" K-counter SUGGESTION → MANDATORY auto-flip on 3rd FWD-candidate landing; verbatim sub-diff from W5-5 pre-registration + W11-5 + Wave-4b instance #3 calibration corpus) | <pinned at plan-freeze> |
```

## Wave 4b Decision Point Prerequisites

Wave 4b dispatch fires conditional on **all** of the following S88-prior-wave landings:

1. **S88 W6 #51 (c_sub canonical pin)** — Jensen-derivation of c_sub completes; canonical_constants.py:c_sub_canonical entry promoted with substrate-first provenance per `.claude/rules/substrate-first-canonical-sourcing.md`. **BLOCKS #21 (FWD-C1)**: Level-3 anchor for n_s_FW requires the c_sub multiplier per S86 W5a SR-flow Z-factor pivot.
   - **PRE-REG-INC fallback**: if W6 #51 lands as INFO/FAIL, gate #21 closes mechanically per `.claude/rules/mechanical-closure-discipline.md` with `value='PRE-REG-INC_blocked_by_c_sub_canonical_<status>'`; deferred to S89+.

2. **S88 W2 Mellin-cone closure** — §VII.U/V Mellin-Dirichlet identity family + §VII.U.2 4-corner classification structural-theorem land; cluster-span PASS at L_max ≥ 12 per S87 W2 pre-registration. **BLOCKS #22 (FWD-C2)**: Level-3 anchor requires Pillar-II → Pillar-V Mellin-residue / BdG-band-edge match at canonical L_max.
   - **PRE-REG-INC fallback**: if Mellin-cone closure remains open, gate #22 closes mechanically with `value='PRE-REG-INC_blocked_by_mellin_cone_closure_<status>'`.

3. **#21 + #22 + #23 verdict landings (any K-counter advance)** — gate #24 (K=3 auto-flip) fires conditional on at least one of the three FWD-candidate gates landing in S88; if all three land BLOCKED-PRE-REG-INC, K remains at 2 and #24 closes mechanically with `value='PRE-REG-INC_blocked_by_no_K_counter_advance'`.

4. **Lancaster MCT-3 + Aalto LTL data availability** (for #23 only) — per S87 CF-32 + CF-33 pre-registrations. Multi-year experimental cycle; if data not yet available at S88-open, gate #23 closes mechanically with `value='PRE-REG-INC_blocked_by_lab_data_pending'` and the landing waits for the experimental cycle.

## §W4b-21. S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING

### 21.1 Gate ID
`S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING`

### 21.2 Trigger phrase
`[VERIFY]` — registry-landing gate with numerical PASS predicate (Level-3 < Level-2 at canonical L_max=10).

### 21.3 Classification
**GEOMETRIC** (registry entry on the cross-pillar bridge anatomy of n_s spectral-action prediction; not a PHONONIC excitation-class result; the substrate IS the spectral moment, the laboratory measures n_s IN the FRW container).

### 21.4 Agent
**mack-cosmic-bridge** (sole writer per `feedback_mack-bridge-role.md`; mack's domain is the substrate-IS / laboratory-IN bridge anatomy where Planck/DESI/BICEP-Keck observational anchors enter).

### 21.5 Hypothesis
The substrate-IS observable `n_s_FW = 0.9561` (S65 BCS+1-loop spectral-action prediction at canonical L_max=10, per `canonical_constants.py:planck_ns` provenance) lies within Level-2 algebraic envelope `L^{-3} = 0.001 = 0.10%` at L_max=10 of the Planck 2018 laboratory-IN observable n_s = 0.9649 ± 0.0042 (TT,TE,EE+lowE+lensing pivot k_pivot = 0.05 Mpc⁻¹). Bridge map = Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR `L_max → ∞` image of the substrate scalar spectral moment, factoring through c_sub conformal-anomaly multiplier per S86 W5a Z-factor machinery.

### 21.6 Method (full dispatch prompt)

```
[VERIFY] You are mack-cosmic-bridge. Land cross-pillar bridge candidate FWD-C1
(Pillar I ↔ Pillar II, substrate ↔ cosmology measurement) at registry slot
§VII.AK in `sessions/permanent-results-registry.md` per the 5-anatomy IS-not-IN
+ 3-level structural-confidence ladder discipline of
`.claude/rules/cross-pillar-bridge-anatomy.md`.

REGISTRY-ANCHOR STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY per
`.claude/rules/registry-landing.md`. Both anchors at co-primary weight; neither
decoration; sequential V_input → C_output chain.

  ANCHOR-1 (V_input layer, substrate-IS source):
    `computations/sN_n_s_spectral_action_BCS_1loop.py` (S65 substrate
    derivation of n_s_FW = 0.9561 from D_K spectral moments; canonical_constants
    pin: planck_ns = 0.9590 [historical, see comment]; n_s_FW pinned via
    canonical_constants.py:n_s_FW provenance entry).
  ANCHOR-2 (C_output layer, bridge-map theorem):
    `.claude/rules/cross-pillar-bridge-anatomy.md` §"FWD-C1" (Mukhanov-Sasaki
    gauge-invariant mode-function transfer ∘ HKR `L_max → ∞` image; substrate-
    first SR-flow Z-factor c_sub pivot per S86 W5a; W6 #51 Jensen-derived
    c_sub canonical pin).
  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: V (substrate scalar spectral moment) → c_sub multiplier
                    → C (Mukhanov-Sasaki HKR transfer) → conclusion (n_s_FW
                    Level-3 vs Planck Level-3-target anchor).
  Closure SHA pin: <computed via script-template.py append_verdict
                   from input-pin map at runtime>

5-ANATOMY IS-NOT-IN (mandatory per cross-pillar-bridge-anatomy.md §"Audit at
plan-freeze"):

  1. Substrate-IS observable: n_s_FW = 0.9561 (substrate scalar spectral
     moment of band-0 sector at τ_fold = 0.190 from D_K eigenmoments on
     (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}); the substrate IS this spectral
     moment — NOT "n_s in inflaton field space").
  2. Laboratory-IN observable: Planck 2018 CMB scalar spectral index
     n_s = 0.9649 ± 0.0042 measured IN the FRW cosmology container as the
     slope of the temperature power spectrum near k_pivot = 0.05 Mpc⁻¹
     (TT,TE,EE+lowE+lensing).
  3. Bridge map: Mukhanov-Sasaki gauge-invariant mode-function transfer
     ∘ HKR `L_max → ∞` image of the substrate scalar spectral moment.
     Factors through c_sub conformal-anomaly multiplier (S86 W5a Z-factor).
  4. Algebraic envelope: L^{-3} at d=4 inherited from Pillar III ↔ IV
     (W-5 calibration); Level-2 canonical envelope 0.001 = 0.10% at L_max=10.
  5. Empirical anchor: |n_s_FW - n_s_Planck| / n_s_Planck =
     |0.9561 - 0.9649| / 0.9649 = 0.00912 = 0.912% at canonical L_max=10
     under substrate-first IC.

3-LEVEL STRUCTURAL-CONFIDENCE LADDER (mandatory per cross-pillar-bridge-
anatomy.md §"Three-Level Structural-Confidence Ladder"):

  Level 1 — Substrate-IS Structural Identity:
    [n_s_FW]_HKR = ⟨[scalar moment of D_K^{≤10}], [Mukhanov-Sasaki kernel]⟩
    regulator-invariant; L-independent at the cohomology-class level.
  Level 2 — Algebraic Convergence Envelope:
    L^{-3} = 0.001 = 0.10% at L_max=10.
  Level 3 — Empirical Anchor at Canonical L_max:
    |n_s_FW - n_s_Planck| / n_s_Planck = 0.00912 = 0.912% at L_max=10.

REGISTRY-PASS CRITERION:
  Level-3 < Level-2 at canonical L_max ⇒ 0.912% < 0.10% is FALSE.
  Bridge entry FAILs registry-PASS at L_max=10.
  Level-3 EXCEEDS Level-2 envelope by ~9×.

This is a STRUCTURAL FAIL of the registry-PASS criterion: the empirical
observation does NOT lie inside the algebraic prediction at L_max=10. Per
the cross-pillar-bridge-anatomy.md §"Registry-PASS criterion", the entry
is registered with FAIL status; the structural cause must be analyzed
(candidate causes: (a) c_sub canonical pin from W6 #51 differs from the
S65 historical n_s_FW=0.9561 input (re-evaluation needed under current
canonical); (b) L^{-3} envelope is Pillar III ↔ Pillar IV calibration —
Pillar I ↔ Pillar II may have a different α exponent (the Mukhanov-Sasaki
transfer adds slow-roll-parameter dependence not present in W-5
quantum-metric trace); (c) k-pivot scale separation between substrate
transit-scale and CMB-scale (54.04 decades per agent memory) introduces
multiplicative factors not captured in the L^{-α} envelope).

INHERITANCE KERNEL RANK: rank(ker ι_*) = 1 (single n_s scalar
observable; rank-2 generalization clause not applicable).

PRE-REG-INC PATHWAY: if S88 W6 #51 (c_sub canonical pin) returns INFO/FAIL,
this gate closes mechanically per `.claude/rules/mechanical-closure-
discipline.md` with `value='PRE-REG-INC_blocked_by_c_sub_canonical_W6_51_
<status>'`; deferred to S89+ pending Jensen-derivation completion.

WORKING-PAPER SECTION: write `sessions/archive/session-88/session-88-w4b-results-
workingpaper.md §W4b-21` with substantive content (>15 lines) covering:

  - Header: gate ID, classification (GEOMETRIC), trigger ([VERIFY]),
    sponsor (mack-cosmic-bridge sole writer)
  - 5-anatomy IS-not-IN block (5 elements with explicit values)
  - 3-level ladder block (3 levels with explicit values + regulator-invariance
    note for Level 1)
  - Registry-PASS evaluation (Level-3 vs Level-2 numerical comparison)
  - Verdict (FAIL composite; structural-cause analysis with three candidates)
  - Substrate framing note (the substrate IS the scalar spectral moment;
    laboratory measures n_s IN the FRW container; direction of explanation
    flows substrate → bridge → laboratory per `phononic-framing.md`)
  - Methodology lineage (S65 BCS+1-loop n_s computation; S86 W5a SR-flow
    Z-factor pivot; W-5 calibration of L^{-3} envelope; this gate as the
    first Pillar I ↔ Pillar II bridge instance under the 5-anatomy +
    3-level discipline)
  - K-counter advancement (this is calibration-corpus instance #3 toward
    K=3 promotion of cross-pillar-bridge-anatomy.md SUGGESTION →
    MANDATORY; see #24 W4b-24 for the auto-flip gate)
  - PRE-REG-INC fallback declaration (if W6 #51 BLOCKED)
  - Forward carry-forward to S89+ if registry-FAIL stands at L_max=10
    (re-evaluation under refined α exponent; structural-cause-(b)
    investigation)

VERDICT-LINE EMISSION: append to `computations/s88_gate_verdicts.txt`
per `.claude/rules/gate-verdicts.md` dual-SHA discipline:

  S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING: FAIL -- value=level3_0.00912_vs_level2_0.001_ratio_9.12 \
    scheme=mukhanov-sasaki-HKR-L_max-10 \
    convention=substrate-IS-scalar-spectral-moment-band-0-tau-fold \
    L_max=10 \
    audit_sha256=<computed> content_sha256=<computed> schema_version=S84+

REGISTRY-ENTRY APPEND: append to `sessions/permanent-results-registry.md`
§VII.AK with full 5-anatomy + 3-level block + SOURCE-DOUBLE-CITE-CO-PRIMARY
structure tag + closure SHA pin + sponsor + anchor list.

CITE: `.claude/rules/cross-pillar-bridge-anatomy.md` §"FWD-C1"; S65 spectral-
action n_s computation; canonical_constants.py:n_s_FW + planck_ns; S86 W5a
SR-flow Z-factor pivot; this gate's working-paper section.
```

### 21.7 Machinery pin (PRDR per `.claude/templates/pru-pre-registration-template.md`)

| Pin name | Value | Provenance |
|:---------|:------|:-----------|
| `n_s_FW` | 0.9561 (or current canonical_constants.py value) | S65 BCS+1-loop spectral-action; canonical_constants.py:planck_ns provenance |
| `n_s_Planck` | 0.9649 ± 0.0042 | Planck 2018 TT,TE,EE+lowE+lensing |
| `c_sub` | <pinned from S88 W6 #51 Jensen-derivation> | substrate-first canonical per `.claude/rules/substrate-first-canonical-sourcing.md` |
| `L_max` | 10 (canonical) | W-5 + W11-5 calibration |
| `level_2_envelope` | 0.001 (L^{-3} at L_max=10, d=4) | W-5 calibration inherited |
| `level_3_anchor_formula` | `\|n_s_FW - n_s_Planck\| / n_s_Planck` | publication-precision pin: float64 (no sig-fig truncation) |
| `registry_slot` | §VII.AK (next-free at S88) | S87 used through §VII.AJ |
| `bridge_map` | Mukhanov-Sasaki HKR `L_max → ∞` ∘ c_sub multiplier | C_output anchor |
| `inheritance_kernel_rank` | 1 (single n_s scalar) | rank-2 clause not invoked |

### 21.8 Pre-registered 4-tuple

| Field | Value |
|:------|:------|
| convention | substrate-IS-scalar-spectral-moment-band-0-tau-fold |
| scheme | mukhanov-sasaki-HKR-L_max-10 |
| L_max | 10 |
| schema_version | S84+ |

### 21.9 PASS / FAIL / INFO criterion

- **PASS** iff Level-3 anchor < Level-2 envelope at L_max=10 (i.e., `|n_s_FW - n_s_Planck| / n_s_Planck < 0.001`). Anticipated: FAIL by ~9× since 0.00912 > 0.001. Pre-registered FAIL with structural-cause analysis is the expected verdict.
- **FAIL** iff Level-3 ≥ Level-2 at L_max=10 (registry entry is registered with FAIL status; structural-cause analysis required in working-paper section; K-counter advances regardless of PASS/FAIL — REGISTRY-FAIL is a valid calibration-corpus instance per W11-5 precedent).
- **INFO** iff one of (a) c_sub canonical pin pending (W6 #51 BLOCKED) — closes via mechanical-closure-discipline.md PRE-REG-INC pathway; (b) n_s_FW substrate-first canonical re-evaluation surfaces D_max ≥ 1.0 OOM per `.claude/rules/substrate-first-canonical-sourcing.md` Class-(f) — closes via SOURCE-RECON MANDATORY remediation.

### 21.10 Substitution chain (mandatory per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute")

```
Claim: Level-3 anchor ≥ Level-2 envelope at L_max=10 ⇒ registry-FAIL.

Required substitution chain:
  Step 1: n_s_FW = 0.9561                                      [substrate-IS observable, S65 spectral-action]
  Step 2: n_s_Planck = 0.9649 ± 0.0042                         [laboratory-IN observable, Planck 2018]
  Step 3: Level-3(L=10) := |n_s_FW - n_s_Planck| / n_s_Planck    [empirical anchor formula]
  Step 4: Substitute: Level-3 = |0.9561 - 0.9649| / 0.9649
                            = 0.0088 / 0.9649
                            = 0.009120 (full float64)            [direct algebra]
  Step 5: Level-2(L=10, d=4) := L^{-3} = 10^{-3} = 0.001          [algebraic envelope; W-5 calibration]
  Step 6: Level-3 / Level-2 = 0.009120 / 0.001 = 9.120              [ratio]
  Step 7: Level-3 > Level-2 ⇔ 9.120 > 1                             [direction from canonical form]
  Conclusion: registry-PASS criterion FALSE; entry registered with FAIL.
```

### 21.11 What PASS / FAIL / INFO MEAN (substrate framing per `phononic-framing.md`)

- **PASS** ⇒ The Pillar I ↔ Pillar II bridge map (Mukhanov-Sasaki HKR transfer) is empirically supported at canonical L_max=10. The substrate scalar spectral moment IS the n_s prediction; the laboratory measures n_s IN the FRW container; the algebraic envelope captures the convergence rate of the substrate-IS image to the laboratory-IN value. (Note: PASS at L_max=10 is not anticipated; the Level-3 anchor exceeds Level-2 by ~9×.)
- **FAIL** ⇒ The bridge map's algebraic envelope at d=4 (L^{-3}) inherited from Pillar III ↔ Pillar IV does NOT capture the Pillar I ↔ Pillar II convergence rate. Three candidate structural causes: (a) c_sub canonical pin from W6 #51 differs from S65 historical input (re-evaluation under current canonical); (b) Pillar I ↔ Pillar II has a different α exponent than Pillar III ↔ Pillar IV (Mukhanov-Sasaki transfer adds slow-roll-parameter dependence not in W-5 quantum-metric trace); (c) k-pivot scale separation (54.04 decades transit-to-CMB) introduces multiplicative factors not captured in L^{-α}. Forward investigation: S89+ refined-α-exponent computation.
- **INFO** ⇒ Either c_sub canonical pin pending (W6 #51 BLOCKED) or substrate-first canonical re-evaluation triggered SOURCE-RECON MANDATORY remediation. Bridge entry deferred to S89+ pending upstream landing.

The substrate IS the scalar spectral moment. The laboratory measures n_s IN the FRW container. The bridge map (Mukhanov-Sasaki HKR transfer) explains substrate → emergent cosmology, not the inverse. Direction-of-explanation discipline preserved per `phononic-framing.md` §"IS Space, Not IN Space — Mandatory Reframe".

### 21.12 Effort

~0.7 wave-equivalents (registry-landing gate; computation script + npz + working-paper section + registry-entry append + verdict-line emission). BLOCKED on S88 W6 #51 (c_sub canonical pin).

### 21.13 Substrate framing per `phononic-framing.md` IS-not-IN

Substrate IS the scalar spectral moment of band-0 sector at τ_fold on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}). Laboratory measures n_s IN the FRW cosmology container. Bridge map (Mukhanov-Sasaki HKR transfer) connects them; direction substrate → emergent cosmology. NEVER write "n_s in inflaton field space" or "primordial perturbations created in curved spacetime" — these are container-thinking violations. Write "fiber's eigenvalue spectrum reorganizes at the fold; the post-transit interference pattern of GGE acoustic excitations IS the n_s observable."

## §W4b-22. S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING

### 22.1 Gate ID
`S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING`

### 22.2 Trigger phrase
`[VERIFY]` — registry-landing gate with numerical PASS predicate (Level-3 < Level-2 at canonical L_max=10).

### 22.3 Classification
**GEOMETRIC** (registry entry on the cross-pillar bridge anatomy of Mellin-Barnes residue ↔ BdG spectral-triple observable; substrate IS the Mellin-residue cocycle, laboratory measures BdG band structure IN the Brillouin-zone container).

### 22.4 Agent
**mack-cosmic-bridge** (sole writer per `feedback_mack-bridge-role.md`).

### 22.5 Hypothesis
The substrate-IS observable (Pillar-II Mellin-Barnes residue at substrate-distance s ∈ {3, 4} on the Mellin-cone, evaluated against ζ-regulated Hochschild moments of D_K) lies within Level-2 algebraic envelope `L^{-α}` with α ∈ {2, 3} of the laboratory-IN observable (BdG spectral-triple observable in a self-consistent BCS lattice with Pf = -1 BDI topology; 3He-B child realization). Bridge map = Connes-Karoubi pairing ∘ K-theory boundary map between Pillar-II Mellin pole structure and Pillar-V finite-rank BdG K_0(M_2(ℂ)) image; companion to W-6 quotient-functor framework. Inheritance kernel rank ≥ 2 expected (Mellin-cone carries multiple residue generators); invokes `.claude/rules/inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B" rank-2 case (binomial(rank, 2) cross-cocycle ratios).

### 22.6 Method (full dispatch prompt)

```
[VERIFY] You are mack-cosmic-bridge. Land cross-pillar bridge candidate FWD-C2
(Pillar II ↔ Pillar V, Mellin-cone ↔ BdG spectral triple) at registry slot
§VII.AL in `sessions/permanent-results-registry.md` per the 5-anatomy IS-not-IN
+ 3-level structural-confidence ladder discipline of
`.claude/rules/cross-pillar-bridge-anatomy.md` AND the rank-2 inheritance-
falsifier-protocol per `.claude/rules/inheritance-falsifier-protocol.md`
§"Generalization beyond 3He-B".

REGISTRY-ANCHOR STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY per
`.claude/rules/registry-landing.md`.

  ANCHOR-1 (V_input layer, substrate-IS source):
    `computations/sN_mellin_residue_substrate_distance_s_3_4.py` (S88 W2
    Mellin-cone closure; Pillar-II Mellin-Barnes residue evaluated against
    ζ-regulated Hochschild moments of D_K; cluster-span PASS at L_max ≥ 12;
    canonical_constants pin: mellin_residue_s3, mellin_residue_s4 promoted
    in-session per S88 W2).
  ANCHOR-2 (C_output layer, bridge-map theorem):
    `.claude/rules/cross-pillar-bridge-anatomy.md` §"FWD-C2" + W-6 quotient-
    functor framework (Connes-Karoubi pairing ∘ K-theory boundary map;
    Pillar-II Mellin pole structure ↔ Pillar-V finite-rank BdG K_0(M_2(ℂ))
    image; companion theorem from S86 W-6).
  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: V (Mellin-Barnes residue at s ∈ {3, 4})
                    → Connes-Karoubi pairing (bridge map)
                    → C (K-theory boundary map onto BdG sector)
                    → conclusion (Level-3 Mellin-residue / BdG-band-edge match
                       at canonical L_max=10).

5-ANATOMY IS-NOT-IN:

  1. Substrate-IS observable: Mellin-Barnes residue at substrate-distance
     s ∈ {3, 4} on the Pillar-II Mellin-cone, evaluated against ζ-regulated
     Hochschild moments of D_K. The substrate IS the Mellin-residue cocycle —
     NOT a "Mellin transform of physical signal".
  2. Laboratory-IN observable: BdG (Bogoliubov-de Gennes) spectral-triple
     observable in a self-consistent BCS lattice — measured IN the Brillouin-
     zone container as the BdG band structure with Pf = -1 BDI topology
     (3He-B child realization; Volovik 2003 §6).
  3. Bridge map: Connes-Karoubi pairing ∘ K-theory boundary map between
     Pillar-II Mellin pole structure and Pillar-V finite-rank BdG K_0(M_2(ℂ))
     image. Companion to W-6 quotient-functor framework (cross-pillar-bridge-
     anatomy.md §"Quotient-functor pre-registration").
  4. Algebraic envelope: L^{-α} with α ∈ {2, 3} under spectral-distance
     scaling; α pinned post-Mellin-pole-closure at S88 W2 cluster-span PASS.
  5. Empirical anchor: Pillar-II → Pillar-V Mellin-residue / BdG-band-edge
     match at canonical L_max=10; substrate-first cocycle norms ‖φ‖
     Sage-exact (per W-5 phi67/phi88 calibration).

3-LEVEL STRUCTURAL-CONFIDENCE LADDER:

  Level 1 — Substrate-IS Structural Identity:
    [Mellin-residue]_HKR = ⟨[ζ-regulated Hochschild moment of D_K], [BdG K_0
    pairing kernel]⟩ regulator-invariant; L-independent at the cohomology-class
    level (Connes-Moscovici 1995 §III.4 dim-spectrum residue formula).
  Level 2 — Algebraic Convergence Envelope:
    L^{-α} with α ∈ {2, 3}; pinned post-S88 W2 closure.
  Level 3 — Empirical Anchor at Canonical L_max:
    |Mellin_residue(L=10) - BdG_band_edge(L=10)| / |BdG_band_edge|
    at L_max=10 with substrate-first cocycle norms.

REGISTRY-PASS CRITERION:
  Level-3(L=10) < Level-2(L=10) at canonical L_max ⇒ entry registers with PASS.
  Otherwise registers with FAIL + structural-cause analysis (analogous to
  W11-5 REGISTRY-FAIL precedent for FWD-C3 instance #2).

INHERITANCE KERNEL RANK ≥ 2: Mellin-cone carries multiple residue generators
(at least s=3 and s=4 substrate-distance poles). Per `.claude/rules/
inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B", the
cohomology-asymmetry test class includes ALL binomial(rank, 2) cross-cocycle
ratio predictions. For rank=2 (s=3, s=4 dual), pre-register the substrate-
derived ratio:
    R_FWD-C2 := Mellin_residue(s=3) / Mellin_residue(s=4)
with Sage-exact substrate value (computed in S88 W2 cluster-span closure).

(Δ_B/Δ_A)^p CANCELLATION THEOREM applicability: declare per the 5-step pre-
registration discipline of inheritance-falsifier-protocol.md §"Pre-registration
discipline". For Pillar-II Mellin residues sharing a common (Δ_B/Δ_A)^p
exponent under Pillar-V BdG inheritance, cancellation preserves R_FWD-C2
INTACT in the laboratory measurement. Verify (Δ_B/Δ_A)^p exponent matching
between s=3 and s=4 cocycles.

PRE-REG-INC PATHWAY: if S88 W2 Mellin-cone closure does not land (cluster-
span FAILs at L_max ≥ 12, or §VII.U/V Mellin-Dirichlet identity family does
not close), this gate closes mechanically per `.claude/rules/mechanical-
closure-discipline.md` with `value='PRE-REG-INC_blocked_by_mellin_cone_
closure_W2_<status>'`; deferred to S89+.

WORKING-PAPER SECTION: write `sessions/archive/session-88/session-88-w4b-results-
workingpaper.md §W4b-22` with substantive content (>15 lines) covering:

  - Header: gate ID, classification (GEOMETRIC), trigger ([VERIFY]),
    sponsor (mack-cosmic-bridge sole writer)
  - 5-anatomy IS-not-IN block
  - 3-level ladder block
  - Rank-2 inheritance generalization block (binomial(2,2)=1 cross-cocycle
    ratio; (Δ_B/Δ_A)^p cancellation applicability declaration; substrate-
    derived R_FWD-C2 with Sage-exact tolerance band)
  - Registry-PASS evaluation
  - Verdict (PASS or FAIL composite with structural-cause analysis)
  - Substrate framing note
  - Methodology lineage (S86 W-6 quotient-functor framework; S88 W2 Mellin-
    cone closure; W-5 ‖φ_67‖/‖φ_88‖ Sage-exact calibration; this gate as the
    first Pillar II ↔ Pillar V bridge instance with rank-2 generalization)
  - K-counter advancement
  - PRE-REG-INC fallback declaration (if W2 Mellin-cone BLOCKED)
  - Forward carry-forward to S89+ if registry-FAIL stands

VERDICT-LINE EMISSION: append to `computations/s88_gate_verdicts.txt`:

  S88-FWD-C2-MELLIN-BDG-BRIDGE-LANDING: PASS|FAIL -- value=level3_<v>_vs_level2_<v>_ratio_<v> \
    scheme=connes-karoubi-K-theory-boundary-L_max-10 \
    convention=substrate-IS-mellin-residue-zeta-regulated-hochschild-moment \
    L_max=10 \
    audit_sha256=<computed> content_sha256=<computed> schema_version=S84+

REGISTRY-ENTRY APPEND: append to `sessions/permanent-results-registry.md`
§VII.AL with full 5-anatomy + 3-level block + rank-2 inheritance generalization
sub-block + (Δ_B/Δ_A)^p cancellation declaration + SOURCE-DOUBLE-CITE-
CO-PRIMARY structure tag.

CITE: `.claude/rules/cross-pillar-bridge-anatomy.md` §"FWD-C2";
`.claude/rules/inheritance-falsifier-protocol.md` §"Generalization beyond
3He-B"; S86 W-6 quotient-functor framework; S88 W2 Mellin-cone closure;
this gate's working-paper section.
```

### 22.7 Machinery pin

| Pin name | Value | Provenance |
|:---------|:------|:-----------|
| `mellin_residue_s3` | <pinned from S88 W2 cluster-span closure> | S88 W2 substrate-first canonical |
| `mellin_residue_s4` | <pinned from S88 W2 cluster-span closure> | S88 W2 substrate-first canonical |
| `R_FWD-C2_substrate` | <Sage-exact ratio mellin_residue_s3 / mellin_residue_s4> | substrate-derived cohomology-asymmetry |
| `BdG_band_edge` | <substrate-derived BdG sector observable at canonical L_max> | Pillar-V finite-rank K_0(M_2(ℂ)) image |
| `level_2_alpha` | α ∈ {2, 3} | pinned post-S88 W2 closure |
| `level_3_anchor_formula` | `\|mellin_residue - BdG_band_edge\| / \|BdG_band_edge\|` | publication-precision pin: float64 |
| `registry_slot` | §VII.AL | next-free at S88 |
| `bridge_map` | Connes-Karoubi pairing ∘ K-theory boundary map | C_output anchor |
| `inheritance_kernel_rank` | ≥ 2 (Mellin-cone multi-pole) | rank-2 generalization invoked |
| `delta_p_cancellation_applicability` | <verified in-script>: common (Δ_B/Δ_A)^p exponent for s=3 and s=4 cocycles | inheritance-falsifier-protocol §"(Δ_B/Δ_A)^p Cancellation Theorem" |
| `L_max` | 10 | canonical |

### 22.8 Pre-registered 4-tuple

| Field | Value |
|:------|:------|
| convention | substrate-IS-mellin-residue-zeta-regulated-hochschild-moment |
| scheme | connes-karoubi-K-theory-boundary-L_max-10 |
| L_max | 10 |
| schema_version | S84+ |

### 22.9 PASS / FAIL / INFO criterion

- **PASS** iff Level-3 anchor < Level-2 envelope at L_max=10 (numerical comparison post-S88 W2 closure).
- **FAIL** iff Level-3 ≥ Level-2 at L_max=10; entry registered with FAIL status; structural-cause analysis required (per W11-5 REGISTRY-FAIL precedent for FWD-C3 instance #2).
- **INFO** iff (a) S88 W2 Mellin-cone closure BLOCKED — closes via mechanical-closure-discipline.md PRE-REG-INC pathway; (b) substrate-first canonical for mellin_residue_s3 or s4 pending — closes via substrate-first-canonical-sourcing.md Class-(f) MANDATORY remediation.

### 22.10 Substitution chain

```
Claim: Level-3(L=10) < Level-2(L=10) ⇒ registry-PASS.

Required substitution chain:
  Step 1: mellin_residue_s3 := Res[M_R(s) · ζ-regulated Hochschild moment; s=3]
                                                                [substrate-IS, Pillar-II]
  Step 2: mellin_residue_s4 := Res[M_R(s) · ζ-regulated Hochschild moment; s=4]
                                                                [substrate-IS, Pillar-II]
  Step 3: BdG_band_edge := substrate-derived BdG sector observable from
                            Pillar-V finite-rank K_0(M_2(ℂ)) image
                                                                [laboratory-IN image]
  Step 4: R_FWD-C2_substrate := mellin_residue_s3 / mellin_residue_s4
                                                                [cohomology-asymmetry; Sage-exact]
  Step 5: Level-3(L=10) := |bridge_map(mellin_residue) - BdG_band_edge|
                          / |BdG_band_edge|                       [empirical anchor formula]
  Step 6: Level-2(L=10, α) := L^{-α} with α ∈ {2, 3} pinned at S88 W2 closure
                                                                [algebraic envelope]
  Step 7: Compare Level-3 vs Level-2 numerically at L_max=10        [registry-PASS criterion]
  Conclusion: PASS or FAIL by direct numerical comparison.
```

### 22.11 What PASS / FAIL / INFO MEAN

- **PASS** ⇒ Pillar II ↔ Pillar V bridge map (Connes-Karoubi pairing ∘ K-theory boundary map) is empirically supported at canonical L_max=10. The substrate IS the Mellin-residue cocycle; the laboratory measures BdG band edges IN the Brillouin-zone container; the algebraic envelope captures convergence. Rank-2 cohomology-asymmetry test (R_FWD-C2 ratio) preserved INTACT under (Δ_B/Δ_A)^p cancellation if applicable.
- **FAIL** ⇒ Bridge map's algebraic envelope does NOT capture Pillar II ↔ Pillar V convergence at L_max=10. Structural causes: (a) α exponent pinning differs from algebraic prediction; (b) Mellin-cone carries higher-rank kernel structure than rank-2; (c) BdG sector inheritance-kernel rank requires extended generalization.
- **INFO** ⇒ Either S88 W2 Mellin-cone closure pending or substrate-first canonical for Mellin residues triggered MANDATORY remediation. Bridge entry deferred.

Substrate IS Mellin-residue cocycle. Laboratory measures BdG band structure IN Brillouin-zone container. Bridge map (Connes-Karoubi K-theory pairing) explains substrate → emergent superfluid laboratory; direction preserved.

### 22.12 Effort

~1.0 wave-equivalents (registry-landing + rank-2 inheritance generalization sub-block + (Δ_B/Δ_A)^p cancellation verification + computation script + npz + working-paper section + registry-entry append + verdict-line emission). BLOCKED on S88 W2 Mellin-cone closure.

### 22.13 Substrate framing per `phononic-framing.md` IS-not-IN

Substrate IS the Mellin-Barnes residue at substrate-distance s ∈ {3, 4}, evaluated against ζ-regulated Hochschild moments of D_K. Laboratory measures BdG band edges IN the Brillouin-zone container. Bridge map (Connes-Karoubi pairing) connects them; direction substrate → emergent BdG laboratory. NEVER write "Mellin transform of physical signal" or "BdG bands on a manifold" — these are container-thinking violations.

## §W4b-23. S88-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING

### 23.1 Gate ID
`S88-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING`

### 23.2 Trigger phrase
`[VERIFY]` — registry-landing gate with numerical PASS predicate (Level-3 < Level-2 at canonical L_max=10).

### 23.3 Classification
**GEOMETRIC** (registry entry on the cross-pillar bridge anatomy of substrate cocycle pair (φ_67, φ_88) ↔ 3He-B/3He-A laboratory observables; substrate IS the cocycle pair, laboratory measures Caroli-Matricon ladder asymmetry / µSR chirality discrimination IN cryostat container).

### 23.4 Agent
**mack-cosmic-bridge** (sole writer per `feedback_mack-bridge-role.md`).

### 23.5 Hypothesis
The substrate-IS observable (substrate-resident HP^1 cocycle norms ‖φ_67‖ = 0.793346 M_KK² and ‖φ_88‖ = 0.108307 M_KK², Sage-exact; ratio R_FWD-C3 = 7.324992) maps via inheritance morphism ι_*: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) (BDI → BdG sector child) to laboratory-IN observable (3He-B vortex-core Caroli-Matricon ladder asymmetry per W11-C5 + 3He-A µSR chirality discrimination per W11-C6). Level-2 envelope is structural-exact (cohomology-asymmetry ratio preservation 7.3250 ± 0.1% per S86 W-5 Gate-2 pre-registered band; not L^{-α} algebraic). Bridge map = inheritance morphism ι_* ∘ (Δ_B/Δ_A)^p lab-conversion factor; (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual) preserves ‖φ_a‖/‖φ_b‖ INTACT.

### 23.6 Method (full dispatch prompt)

```
[VERIFY] You are mack-cosmic-bridge. Land cross-pillar bridge candidate FWD-C3
(Pillar IV ↔ Pillar V, substrate cocycles ↔ 3He-B / 3He-A laboratory
observables) at registry slot §VII.AM in `sessions/permanent-results-
registry.md` per the 5-anatomy IS-not-IN + 3-level structural-confidence ladder
discipline of `.claude/rules/cross-pillar-bridge-anatomy.md` AND the rank-2
inheritance-falsifier-protocol per `.claude/rules/inheritance-falsifier-
protocol.md` §"Four-Gate Structure".

NOTE: This gate FULL-LANDS FWD-C3 (W11-5 was a sub-instance of FWD-C3 that
REGISTRY-FAILed at substrate spectral-excess level due to M_3(C) Cartan-zone
weight non-negligible at L_max=10; FWD-C3 in cocycle-pair form preserves
‖φ_67‖/‖φ_88‖ = 7.324992 INTACT under (Δ_B/Δ_A)^p cancellation theorem
S86 W-5 DONE-5 verified at 0.0e+00 residual). FULL-LANDING requires lab data
from Lancaster MCT-3 vortex-core spectroscopy (W11-C5) AND Aalto LTL µSR
(W11-C6); S87 CF-32 + CF-33 pre-registrations queued. If lab data not yet
available at S88-open, gate closes mechanically with PRE-REG-INC pending
multi-year experimental cycle.

REGISTRY-ANCHOR STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY.

  ANCHOR-1 (V_input layer, substrate-IS source):
    `computations/s86_w5_phi67_phi88_sage_exact.py` (W-5 cocycle norms
    Sage-exact; ‖φ_67‖ = 0.793346 M_KK², ‖φ_88‖ = 0.108307 M_KK², ratio
    7.324992; canonical_constants pin: phi67_norm_FW, phi88_norm_FW,
    cocycle_ratio_67_88_FW = 7.324992).
  ANCHOR-2 (C_output layer, bridge-map theorem):
    `.claude/rules/cross-pillar-bridge-anatomy.md` §"FWD-C3" + `.claude/rules/
    inheritance-falsifier-protocol.md` §"Four-Gate Structure" + S86 W-5
    DONE-5 (Δ_B/Δ_A)^p cancellation theorem (0.0e+00 residual; substrate-
    derived ratio preserved INTACT in lab measurement under common p
    exponents; CANCELLATION THEOREM operational form: lab(F_i)/lab(F_j)
    = ‖φ_a‖/‖φ_b‖ × (f_i/f_j)).
  STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
  Derivation chain: V (substrate cocycle pair (φ_67, φ_88) at L_max=10)
                    → inheritance morphism ι_*: ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)
                    → (Δ_B/Δ_A)^p cancellation (preserves ratio INTACT)
                    → C (laboratory ratio measurement on common-p F-rows)
                    → conclusion (Level-3 lab ratio vs Level-2 substrate
                       7.3250 ± 0.1% band).

5-ANATOMY IS-NOT-IN:

  1. Substrate-IS observable: substrate-resident HP^1 cocycle norms
     ‖φ_67‖ = 0.793346 M_KK² (chiral pair) and ‖φ_88‖ = 0.108307 M_KK²
     (Cartan hypercharge), Sage-exact at machine precision; evaluated on
     the BdG-restricted spectral-triple sub-algebra of (A_K, H_K, D_K).
     The substrate IS the cocycle pair — these are intrinsic structural
     numbers, NOT BdG band-structure derivatives.
  2. Laboratory-IN observable: 3He-B vortex-core Caroli-Matricon ladder
     asymmetry (W11-C5; Lancaster MCT-3 / Helsinki ROTA cells) AND
     3He-A µSR chirality discrimination (W11-C6; Aalto LTL).
     Lab measures these IN the helium cryostat container under (p, T)
     sweep over 0–34 bar.
  3. Bridge map: Inheritance morphism ι_*: A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)
     (BDI → BdG sector child) ∘ (Δ_B/Δ_A)^p lab-conversion factor.
     Cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual) preserves
     ‖φ_a‖/‖φ_b‖ INTACT in the lab measurement under common p.
  4. Algebraic envelope: Cohomology-asymmetry test — ratio preservation
     7.3250 ± 0.1% (S86 W-5 Gate-2 pre-registered band). Level-2 envelope
     is the STRUCTURAL-EXACT form, NOT an L^{-α} algebraic bound; the
     regulator-invariant ratio replaces the convergence envelope for
     this candidate class.
  5. Empirical anchor: lab measurement of Caroli-Matricon ladder asymmetry
     ratio (W11-C5 F-row pair) AND µSR chirality ratio (W11-C6 F-row
     pair) — substrate-derived prediction NULL on F1/F2/F5 + ratio
     7.3250 ± 0.1% on any non-NULL detection.

3-LEVEL STRUCTURAL-CONFIDENCE LADDER:

  Level 1 — Substrate-IS Structural Identity:
    [‖φ_a‖/‖φ_b‖]_HKR = 7.324992 Sage-exact at machine precision;
    regulator-invariant; L-independent; preserved INTACT under (Δ_B/Δ_A)^p
    cancellation theorem (S86 W-5 DONE-5).
  Level 2 — Algebraic Convergence Envelope (STRUCTURAL-EXACT form):
    7.3250 ± 0.1% (S86 W-5 Gate-2 pre-registered band).
  Level 3 — Empirical Anchor at Canonical L_max=10:
    lab(F_i)/lab(F_j) on common-p F-row pair from Lancaster MCT-3 + Aalto
    LTL data; falsifier 4-gate structure per inheritance-falsifier-
    protocol.md §"Four-Gate Structure".

REGISTRY-PASS CRITERION:
  Level-3(lab ratio) within Level-2 band (7.3250 ± 0.1%) at L_max=10 ⇒ PASS.
  Otherwise registers with FAIL + structural-cause analysis.

INHERITANCE KERNEL RANK = 2 (φ_67 chiral pair + φ_88 Cartan hypercharge);
DIRECTLY invokes inheritance-falsifier-protocol.md §"Generalization beyond
3He-B" rank-2 case. binomial(2, 2) = 1 cross-cocycle ratio: R_FWD-C3 =
‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact substrate-derived).

(Δ_B/Δ_A)^p CANCELLATION THEOREM applicability: S86 W-5 DONE-5 verified
at 0.0e+00 residual; common (Δ_B/Δ_A)^p exponent for F1+F2+F5 F-rows on
3He-B side. Verify common-p applicability extends to W11-C5 + W11-C6
combined F-row table.

FOUR-GATE STRUCTURE per inheritance-falsifier-protocol.md:
  - Gate 1 (kernel-signature decisive F-rows): NULL on F1+F2+F5 (W11-C5
    Caroli-Matricon ladder asymmetry + W11-C6 µSR chirality decisive
    triplet). Per-row substrate prediction: F1 = 0.573193 M_KK² S/N margin.
  - Gate 2 (cohomology-asymmetry cross-cocycle ratio): 7.3250 ± 0.1% on
    any non-NULL detection. Sage-exact substrate prediction.
  - Gate 3 (kernel-signature supporting F-rows): NULL on F3+F4 (supporting).
  - Gate 4 (slope-discrimination on cocycle-degenerate row F4): multi-
    pressure slope over 0–34 bar; Jacobi-cubic vs φ_88-linear discrimination.

PRE-REG-INC PATHWAY: if lab data from W11-C5 AND/OR W11-C6 not yet
available at S88-open (multi-year experimental cycle), this gate closes
mechanically per `.claude/rules/mechanical-closure-discipline.md` with
`value='PRE-REG-INC_blocked_by_lab_data_pending_W11_C5_W11_C6'`; deferred
to S89+ pending experimental data landing.

WORKING-PAPER SECTION: write `sessions/archive/session-88/session-88-w4b-results-
workingpaper.md §W4b-23` with substantive content (>15 lines) covering:

  - Header
  - 5-anatomy IS-not-IN block
  - 3-level ladder block (Level-2 in STRUCTURAL-EXACT form, NOT L^{-α})
  - Rank-2 inheritance generalization block (binomial(2,2) = 1 ratio;
    (Δ_B/Δ_A)^p cancellation theorem applicability)
  - Four-gate falsifier structure block
  - Distinction from W11-5 sub-instance (W11-5 was substrate spectral-
    excess level FAIL; this gate is cocycle-pair level via (Δ_B/Δ_A)^p
    cancellation theorem — different structural axis)
  - Registry-PASS evaluation
  - Verdict (PASS or FAIL or PRE-REG-INC composite)
  - Substrate framing note
  - Methodology lineage (S86 W-5 cocycle Sage-exact computation; W-5
    DONE-5 cancellation theorem; W11-5 REGISTRY-FAIL precedent;
    S87 CF-32 + CF-33 lab pre-registrations; this gate as the FULL
    landing of FWD-C3 in cocycle-pair form)
  - K-counter advancement (instance #3 if PASS or FAIL; INFO if BLOCKED)
  - PRE-REG-INC fallback declaration
  - Forward carry-forward to S89+ if PRE-REG-INC

VERDICT-LINE EMISSION:

  S88-FWD-C3-COCYCLE-3HE-BRIDGE-LANDING: PASS|FAIL|INFO -- value=level3_<v>_within_level2_<v> \
    scheme=inheritance-morphism-delta-cancellation-L_max-10 \
    convention=substrate-IS-cocycle-pair-phi67-phi88-Sage-exact \
    L_max=10 \
    audit_sha256=<computed> content_sha256=<computed> schema_version=S84+

REGISTRY-ENTRY APPEND: append to `sessions/permanent-results-registry.md`
§VII.AM with full 5-anatomy + 3-level (STRUCTURAL-EXACT) + rank-2 generalization
+ four-gate falsifier structure + (Δ_B/Δ_A)^p cancellation declaration +
SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag.

CITE: `.claude/rules/cross-pillar-bridge-anatomy.md` §"FWD-C3" +
`.claude/rules/inheritance-falsifier-protocol.md` §"Four-Gate Structure" +
S86 W-5 cocycle Sage-exact + S86 W-5 DONE-5 cancellation theorem + W11-5
REGISTRY-FAIL precedent (substrate spectral-excess level) + S87 CF-32 +
S87 CF-33 lab pre-registrations + this gate's working-paper section.
```

### 23.7 Machinery pin

| Pin name | Value | Provenance |
|:---------|:------|:-----------|
| `phi67_norm_FW` | 0.793346 M_KK² (Sage-exact) | S86 W-5 substrate-derived |
| `phi88_norm_FW` | 0.108307 M_KK² (Sage-exact) | S86 W-5 substrate-derived |
| `cocycle_ratio_67_88_FW` | 7.324992 (Sage-exact) | S86 W-5 substrate-derived; canonical |
| `level_2_band` | 7.3250 ± 0.1% (STRUCTURAL-EXACT form) | S86 W-5 Gate-2 pre-registered |
| `level_3_anchor_formula` | `lab(F_i)/lab(F_j)` from Lancaster MCT-3 + Aalto LTL | publication-precision pin: float64 |
| `delta_p_cancellation_residual` | 0.0e+00 (S86 W-5 DONE-5 verified) | substrate-derived theorem |
| `inheritance_kernel_rank` | 2 (φ_67 chiral pair + φ_88 Cartan hypercharge) | rank-2 directly invoked |
| `falsifier_gates` | Gate1 (NULL F1+F2+F5), Gate2 (ratio 7.3250 ± 0.1%), Gate3 (NULL F3+F4), Gate4 (slope F4) | inheritance-falsifier-protocol.md four-gate structure |
| `registry_slot` | §VII.AM | next-free at S88 |
| `bridge_map` | ι_*: A_K → M_2(ℂ) ∘ (Δ_B/Δ_A)^p | C_output anchor |
| `lab_data_status` | <pinned at dispatch>: Lancaster MCT-3 + Aalto LTL availability | S87 CF-32 + CF-33 |
| `L_max` | 10 | canonical |

### 23.8 Pre-registered 4-tuple

| Field | Value |
|:------|:------|
| convention | substrate-IS-cocycle-pair-phi67-phi88-Sage-exact |
| scheme | inheritance-morphism-delta-cancellation-L_max-10 |
| L_max | 10 |
| schema_version | S84+ |

### 23.9 PASS / FAIL / INFO criterion

- **PASS** iff lab Level-3 ratio within Level-2 STRUCTURAL-EXACT band 7.3250 ± 0.1% at L_max=10 (i.e., `|lab_ratio - 7.3250| / 7.3250 < 0.001`); AND four-gate falsifier structure NULL on F1+F2+F5 (Gate 1) + ratio match (Gate 2) + NULL on F3+F4 (Gate 3) + slope discrimination (Gate 4).
- **FAIL** iff Level-3 ratio outside band OR any of Gate 1/2/3/4 fails its substrate-derived prediction. Structural-cause analysis required.
- **INFO** iff lab data from W11-C5 AND/OR W11-C6 not yet available — closes via mechanical-closure-discipline.md PRE-REG-INC pathway pending experimental cycle.

### 23.10 Substitution chain

```
Claim: Level-3 (lab ratio) within Level-2 STRUCTURAL-EXACT band 7.3250 ± 0.1%
       at L_max=10 ⇒ registry-PASS.

Required substitution chain:
  Step 1: ‖φ_67‖ = 0.793346 M_KK²                         [substrate-IS, Sage-exact]
  Step 2: ‖φ_88‖ = 0.108307 M_KK²                         [substrate-IS, Sage-exact]
  Step 3: R_substrate := ‖φ_67‖ / ‖φ_88‖ = 7.324992        [cohomology-asymmetry; Sage-exact]
  Step 4: Apply (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5):
          lab(F_i) / lab(F_j) = ‖φ_a‖ / ‖φ_b‖ × (f_i / f_j)  [operational form]
          For common p_i = p_j = p, (Δ_B/Δ_A)^p cancels exactly between
          numerator and denominator; substrate-derived ratio preserved INTACT
                                                              [bridge map step]
  Step 5: lab(F_i) / lab(F_j) = R_substrate × (f_i / f_j) = 7.324992 × (f_i / f_j)
                                                              [bridge image]
  Step 6: Level-2(STRUCTURAL-EXACT) = 7.3250 ± 0.1%           [band; not L^{-α}]
  Step 7: Level-3 := |lab_ratio_observed - 7.3250| / 7.3250
                    from Lancaster MCT-3 + Aalto LTL data    [empirical anchor]
  Step 8: Compare Level-3 vs Level-2 numerically                [registry-PASS criterion]
  Conclusion: PASS iff Level-3 < 0.001 (band tolerance); FAIL otherwise.
```

### 23.11 What PASS / FAIL / INFO MEAN

- **PASS** ⇒ Pillar IV ↔ Pillar V bridge map (inheritance morphism ι_* ∘ (Δ_B/Δ_A)^p cancellation) is empirically supported at canonical L_max=10. The substrate IS the cocycle pair (φ_67, φ_88); the laboratory measures Caroli-Matricon ladder asymmetry / µSR chirality IN the cryostat container. Substrate-derived ratio 7.324992 preserved INTACT in laboratory measurement under (Δ_B/Δ_A)^p cancellation. Four-gate falsifier structure (Gate 1 NULL F1+F2+F5, Gate 2 ratio match, Gate 3 NULL F3+F4, Gate 4 slope discrimination) all confirmed.
- **FAIL** ⇒ Bridge map FAILed at one or more of: (a) ratio outside 7.3250 ± 0.1% band; (b) Gate 1 NULL violated (non-NULL detection on F1, F2, or F5 outside cohomology-asymmetry constraint); (c) Gate 3 NULL violated; (d) Gate 4 slope discrimination FAILed Jacobi-cubic vs φ_88-linear pattern. Each FAIL pattern points to a specific structural cause; W11-5 REGISTRY-FAIL precedent (substrate spectral-excess level) is structurally distinct from cocycle-pair level.
- **INFO** ⇒ Lab data from W11-C5 (Lancaster MCT-3) AND/OR W11-C6 (Aalto LTL) not yet available at S88-open; multi-year experimental cycle. Bridge entry deferred to S89+ pending lab data landing.

Substrate IS cocycle pair (φ_67, φ_88) at L_max=10 BdG-restricted spectral-triple sub-algebra. Laboratory measures ladder asymmetry / chirality IN cryostat container under (p, T) sweep. Inheritance morphism connects them; direction substrate → emergent superfluid laboratory.

### 23.12 Effort

~1.2 wave-equivalents (registry-landing + four-gate falsifier structure block + (Δ_B/Δ_A)^p cancellation re-verification + computation script + npz + working-paper section + registry-entry append + verdict-line emission). BLOCKED on lab data from W11-C5 + W11-C6; multi-year experimental cycle.

### 23.13 Substrate framing per `phononic-framing.md` IS-not-IN

Substrate IS the cocycle pair (φ_67, φ_88) — Sage-exact intrinsic structural numbers on the BdG-restricted spectral-triple sub-algebra. Laboratory measures Caroli-Matricon ladder asymmetry / µSR chirality discrimination IN the helium cryostat container under (p, T) sweep. Inheritance morphism + (Δ_B/Δ_A)^p cancellation theorem connect them; direction substrate → emergent superfluid laboratory measurement. NEVER write "cocycle pair lives in HP^1 cohomology space" — the substrate IS the cocycle pair, not "in" some external cohomology container.

## §W4b-24. S88-OR-LATER-CF-D-K3-PROMOTION-AUTO-FLIP

### 24.1 Gate ID
`S88-OR-LATER-CF-D-K3-PROMOTION-AUTO-FLIP`

### 24.2 Trigger phrase
`[AUDIT]` — methodology-class gate; monitors K-counter advancement and triggers rule-file auto-flip when K reaches 3.

### 24.3 Classification
**METHODOLOGY** (rule-file edit only; no numerical computation; PASS predicate is artifact-existence-with-substantive-content per `wave-classification.md` §M1).

### 24.4 Agent
**mack-cosmic-bridge** (orchestrator-direct edit per `wave-classification.md` §"Dispatch consequences"; methodology-class waves SKIP `/rclab-coordinate` compute-mode, orchestrator writes rule-file edits directly).

### 24.5 Hypothesis
The cross-pillar-bridge-anatomy.md §"Forward template-adoption (calibration-corpus tracking)" K-counter advances from K=2 (S87 close: instance #1 W-5 LANDED + instance #2 W11-5 REGISTRY-FAIL) to K=3 upon the third FWD-candidate landing in S88 (any of #21/#22/#23 PASS or FAIL, regardless of which FWD-candidate; REGISTRY-FAIL counts toward K per W11-5 precedent). At K=3, the rule's promotion threshold (per `feedback_rules-compensate-missing-structure.md` K=3 ladder) is structurally reached; the orchestrator MUST auto-flip the rule-file's §"Forward template-adoption" sub-section from SUGGESTION to MANDATORY in the same dispatch as the third landing.

### 24.6 Method (full dispatch prompt)

```
[AUDIT] You are mack-cosmic-bridge in orchestrator-direct-edit mode (per
wave-classification.md §"Dispatch consequences", methodology-class waves
SKIP /rclab-coordinate compute-mode; orchestrator writes rule-file edits
directly).

MONITOR Wave 4b verdicts for #21, #22, #23. Compute current K-counter
based on which gates landed:

  K_current = 2 (S87 close baseline)
            + count(W4b-21 verdict ∈ {PASS, FAIL})  [INFO does NOT count]
            + count(W4b-22 verdict ∈ {PASS, FAIL})  [INFO does NOT count]
            + count(W4b-23 verdict ∈ {PASS, FAIL})  [INFO does NOT count]

K-counter advancement rule (verbatim from cross-pillar-bridge-anatomy.md):
  REGISTRY-FAIL counts toward K (per W11-5 precedent: REGISTRY-FAIL is a
  valid calibration-corpus instance, the structural pattern IS exercised).
  PRE-REG-INC (mechanical closure on upstream BLOCKED) does NOT count
  toward K (the structural pattern is NOT yet exercised).

If K_current >= 3:
  AUTO-FLIP triggered. Edit `.claude/rules/cross-pillar-bridge-anatomy.md`
  §"Forward template-adoption (calibration-corpus tracking)" as follows:

  (a) Replace the "Status: SUGGESTION (NOT MANDATORY) at K=2" header with:
      "Status: MANDATORY at K=3 (promoted at S88 via W4b-24 auto-flip)"

  (b) Update the calibration-corpus table to mark all FWD-C1/C2/C3
      instances landed in S88:
      - Row #1: S86 W-5 (existing; LANDED §VII.AF.1)
      - Row #2: S87 W11-5 FWD-C3 sub-instance (existing; REGISTRY-FAIL §VII.AJ)
      - Row #3: S88 W4b-21/22/23 third instance (one of FWD-C1/C2/C3; cite
        the specific gate ID and verdict that triggered K=3 saturation)

  (c) Replace "K = 2  <  K_promotion = 3  ⇒  status = SUGGESTION (NOT
      MANDATORY)" with "K = 3 (saturation reached at S88) ⇒ status =
      MANDATORY".

  (d) Update §"Audit at plan-freeze (forward-looking)" sub-clause #4 from
      "SHOULD adopt SUGGESTED at K=1; will be MANDATORY at K=3" to
      "MANDATORY at K=3 (achieved at S88 W4b-24)".

  (e) Update §"Calibration-corpus tracking (forward-looking)" instance #3
      entry from "SUGGESTED next-after-#2" to the specific S88 W4b instance
      and its registry slot.

  (f) Append a new §"Promotion event ledger" sub-section below the existing
      §"Calibration-corpus tracking (forward-looking)" with the verbatim
      promotion record:
        - K=1 → K=2 advancement: S87 W11-5 (REGISTRY-FAIL FWD-C3 sub-instance)
        - K=2 → K=3 advancement: S88 W4b-<XX> (PASS or FAIL FWD-<C1|C2|C3>;
          cite gate ID + verdict + registry slot)
        - SUGGESTION → MANDATORY promotion: S88 W4b-24 auto-flip
          (orchestrator-direct edit; per wave-classification.md §"Dispatch
          consequences"; per `feedback_fix-in-session-never-defer.md`)

If K_current < 3 (i.e., all of W4b-21/22/23 closed as INFO/PRE-REG-INC):
  AUTO-FLIP NOT triggered. Close gate W4b-24 with INFO via mechanical-
  closure-discipline.md PRE-REG-INC pathway:
    value='PRE-REG-INC_blocked_by_no_K_counter_advance_W4b_21_22_23_all_INFO'
  Carry-forward to S89+: re-evaluate at next FWD-candidate landing.

VERDICT-LINE EMISSION:

  Case 1 (auto-flip triggered, K=3 reached):
    S88-OR-LATER-CF-D-K3-PROMOTION-AUTO-FLIP: PASS -- value=K_3_reached_via_W4b_<XX>_<verdict>_FWD_<C1|C2|C3>_rule_file_promoted_SUGGESTION_to_MANDATORY \
      scheme=orchestrator-direct-edit-methodology-class \
      convention=cross-pillar-bridge-anatomy-md-K-counter-promotion \
      L_max=N/A \
      audit_sha256=<computed over input-pin map: cross-pillar-bridge-anatomy.md content_sha + W4b-21/22/23 verdict-lines content_sha + methodology-allowlist W4b-24 row content_sha> \
      content_sha256=<computed over rule-file diff post-edit> \
      schema_version=S84+

  Case 2 (auto-flip NOT triggered):
    S88-OR-LATER-CF-D-K3-PROMOTION-AUTO-FLIP: INFO -- value=PRE-REG-INC_blocked_by_no_K_counter_advance \
      scheme=orchestrator-direct-edit-methodology-class \
      convention=cross-pillar-bridge-anatomy-md-K-counter-monitor \
      L_max=N/A \
      audit_sha256=<computed> content_sha256=<computed> schema_version=S84+

WORKING-PAPER SECTION: write `sessions/archive/session-88/session-88-w4b-results-
workingpaper.md §W4b-24` with substantive content (>15 lines) covering:

  - Header: gate ID, classification (METHODOLOGY), trigger ([AUDIT]),
    sponsor (mack-cosmic-bridge orchestrator-direct-edit)
  - K-counter computation block (S87 baseline K=2 + W4b verdicts)
  - Auto-flip trigger evaluation (K_current ≥ 3?)
  - Case 1 vs Case 2 branching
  - Rule-file diff summary (which §-anchors edited; before/after status)
  - Methodology-allowlist row append (W4b-24 row with computed plan-block SHA)
  - Promotion event ledger entry (K=1 → K=2 → K=3 trajectory)
  - Substrate framing note (this is methodology-layer F-image of substrate
    K-counter advancement; layer-functor F per epistemic-discipline.md
    §"Layer-Decomposition")
  - Methodology lineage (W5-5 K=2 baseline; W11-5 K=2 registry-FAIL precedent;
    W4b instance #3 saturation)
  - K=3 forward implications (subsequent S89+ FWD-candidates land under
    MANDATORY-status discipline; absence of 5-anatomy + 3-level routes to
    plan-freeze halt)

CITE: `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-
adoption (calibration-corpus tracking)"; `feedback_rules-compensate-missing-
structure.md` K=3 ladder; `feedback_fix-in-session-never-defer.md`; W4b-21,
W4b-22, W4b-23 verdict-lines (input-pin map); methodology-wave-allowlist.md
W4b-24 row (recursion-attack closure).
```

### 24.7 Machinery pin

| Pin name | Value | Provenance |
|:---------|:------|:-----------|
| `K_counter_baseline_S87` | 2 (W-5 instance #1 + W11-5 instance #2) | S87 close per `cross-pillar-bridge-anatomy.md` |
| `K_promotion_threshold` | 3 | per `feedback_rules-compensate-missing-structure.md` K=3 ladder |
| `auto_flip_trigger` | K_current >= 3 | `wave-classification.md` §"Dispatch consequences" |
| `rule_file_target` | `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption" | rule-file edit target |
| `methodology_allowlist_row` | W4b-24 row append | `methodology-wave-allowlist.md` recursion-attack closure |
| `sub_section_edits` | (a) header / (b) corpus table / (c) K-counter line / (d) audit at plan-freeze / (e) corpus-tracking instance #3 / (f) promotion event ledger | enumerated in dispatch prompt |
| `verdict_lines_input_pin` | W4b-21, W4b-22, W4b-23 verdict-lines (post-landing) | input-pin map for audit_sha256 |
| `K_increment_rule` | PASS counts +1; FAIL counts +1; INFO/PRE-REG-INC counts +0 | per W11-5 REGISTRY-FAIL precedent |

### 24.8 Pre-registered 4-tuple

| Field | Value |
|:------|:------|
| convention | cross-pillar-bridge-anatomy-md-K-counter-promotion |
| scheme | orchestrator-direct-edit-methodology-class |
| L_max | N/A |
| schema_version | S84+ |

### 24.9 PASS / FAIL / INFO criterion

- **PASS** iff K_current >= 3 AND rule-file diff applied AND all 6 sub-section edits (a)-(f) verified present AND methodology-allowlist W4b-24 row appended with computed plan-block SHA. Auto-flip event recorded in promotion event ledger.
- **FAIL** iff K_current >= 3 but rule-file edit fails (e.g., file write error, sub-section edits missing, allowlist row append fails). Triggers v3-closure-recovery Stage-1 remediation.
- **INFO** iff K_current < 3 (all of W4b-21/22/23 closed as INFO/PRE-REG-INC). Auto-flip NOT triggered; gate closes mechanically with carry-forward to S89+.

### 24.10 Substitution chain

```
Claim: K_current = 3 ⇒ rule-file SUGGESTION → MANDATORY auto-flip triggered.

Required substitution chain:
  Step 1: K_baseline = 2                                      [S87 close baseline]
  Step 2: Define ΔK := count(verdicts ∈ {PASS, FAIL}) over {W4b-21, W4b-22, W4b-23}
                                                              [advancement rule]
  Step 3: ΔK ∈ {0, 1, 2, 3}                                    [bounded by 3 gates]
  Step 4: K_current = K_baseline + ΔK = 2 + ΔK                 [substitution]
  Step 5: Auto-flip predicate := (K_current >= 3) <=> (ΔK >= 1) [direct algebra]
  Step 6: Auto-flip triggered iff at least ONE of W4b-21/22/23 lands as
          PASS or FAIL                                          [direction from canonical form]
  Conclusion: Trigger fires on first FWD-candidate landing (PASS or FAIL);
              ALL 3 INFO closures means trigger does not fire and gate closes
              with PRE-REG-INC.
```

### 24.11 What PASS / FAIL / INFO MEAN

- **PASS** ⇒ K-counter saturation reached at S88; cross-pillar-bridge-anatomy.md §"Forward template-adoption" SUGGESTION promoted to MANDATORY in same dispatch as the third FWD-candidate landing. Future S89+ cross-pillar bridge candidates MUST adopt 5-anatomy + 3-level discipline; absence routes to plan-freeze halt. Methodology lineage: W5-5 baseline (K=2) + W11-5 registry-FAIL instance (K=2) + W4b instance #3 (K=3) = saturation.
- **FAIL** ⇒ K_current >= 3 reached but rule-file edit failed (file write error, sub-section edit missing, allowlist row append error). Triggers v3-closure-recovery Stage-1 remediation per PROHIBITED_ACTIONS Class 4 ban on ansatz-forced PASS.
- **INFO** ⇒ K_current remains at 2 (all of W4b-21/22/23 closed as INFO/PRE-REG-INC; no FWD-candidate registry-landing took place in S88). Auto-flip NOT triggered; rule-file SUGGESTION status preserved. Carry-forward to S89+ at next FWD-candidate landing opportunity.

This is methodology-layer F-image of the substrate K-counter advancement (per `epistemic-discipline.md` §"Layer-Decomposition" layer-functor F). The substrate-physics K-counter is the "agreement among 3 distinct calibration instances" axis; the methodology image is the rule-file MANDATORY-status promotion. Layer-functor F preserves K-counter invariants between substrate and methodology layers.

### 24.12 Effort

~0.4 wave-equivalents (methodology-class; orchestrator-direct edit; rule-file diff + allowlist row append + verdict-line emission + working-paper section). Conditional on at least one of W4b-21/22/23 landing PASS or FAIL.

### 24.13 Substrate framing per `phononic-framing.md` IS-not-IN

K-counter advancement IS the methodology-layer F-image of substrate calibration-corpus instance count. The rule-file MANDATORY-status promotion IS the F-image of substrate K-saturation event. Direction: substrate K-counter advances → F maps to methodology K-counter row update → rule-file status promotion. NEVER frame this as "we are deciding to make the rule mandatory" — the rule-file status IS structurally promoted by F-image; the orchestrator-direct edit is the mechanical execution of the F-image, not a decision.

## Wave 4b → Wave 4c Decision Point

If all 4 Wave-4b gates close cleanly (3 of 4 PASS/FAIL on registry-landings + #24 PASS on auto-flip OR INFO on no-K-advance):
  → proceed to Wave 4c (next theme: TBD per S88 plan main file).

If any of W4b-21/22/23 closes as INFO/PRE-REG-INC due to upstream BLOCKED:
  → carry-forward to S89+ via 4-field spec per `feedback_fix-in-session-never-defer.md`:
    - **What**: re-attempt FWD-C<X> registry-landing
    - **Inputs**: upstream landing (W6 #51 / S88 W2 Mellin closure / lab data)
    - **Gate**: same Level-3 < Level-2 PASS predicate
    - **Effort**: same as #21/#22/#23 (~0.7-1.2 wave-equivalents)

If #24 closes as INFO (no K-advance):
  → carry-forward to next session with FWD-candidate landing opportunity:
    - **What**: re-evaluate K-counter advancement
    - **Inputs**: any future W-X-Y FWD-candidate landing verdict
    - **Gate**: K_current >= 3 auto-flip trigger
    - **Effort**: 0.4 wave-equivalents (orchestrator-direct edit only)

If #24 FAILs (rule-file edit error):
  → trigger v3-closure-recovery Stage-1 remediation per PROHIBITED_ACTIONS;
    NOT a carry-forward; same-session fix-in-session per `feedback_fix-in-
    session-never-defer.md`.

## Wave 4b Machinery-Enumeration Pin (§0.11)

Per PRDR pre-registration discipline (`.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness"):

### #21 (FWD-C1) machinery enumeration

All free parameters of `computations/s88_w4b_fwd_c1_n_s_bridge.py`:
- `n_s_FW` ← canonical_constants.py:planck_ns (or n_s_FW promotion if S88 W6 #51 promotes a new canonical) — pinned
- `n_s_Planck` ← Planck 2018 TT,TE,EE+lowE+lensing → pinned constant
- `c_sub` ← S88 W6 #51 Jensen-derivation canonical — pinned (BLOCKED on W6 #51)
- `L_max` ← 10 (canonical) — pinned
- `level_2_alpha` ← 3 (W-5 Pillar III ↔ IV calibration; assumed inherited; if α differs per Pillar I ↔ II structural reading, FAIL surfaces structural-cause-(b)) — pinned
- `level_3_anchor_formula` ← `|n_s_FW - n_s_Planck| / n_s_Planck` — pinned
- `registry_slot` ← §VII.AK — pinned
- `bridge_map` ← Mukhanov-Sasaki HKR transfer ∘ c_sub multiplier — pinned
- `inheritance_kernel_rank` ← 1 — pinned

### #22 (FWD-C2) machinery enumeration

All free parameters of `computations/s88_w4b_fwd_c2_mellin_bdg_bridge.py`:
- `mellin_residue_s3` ← S88 W2 Mellin-cone closure canonical — pinned (BLOCKED on W2)
- `mellin_residue_s4` ← S88 W2 Mellin-cone closure canonical — pinned (BLOCKED on W2)
- `R_FWD-C2_substrate` ← Sage-exact ratio — pinned
- `BdG_band_edge` ← Pillar-V K_0(M_2(ℂ)) image canonical — pinned
- `level_2_alpha` ← α ∈ {2, 3} pinned post-S88 W2 closure — pinned
- `level_3_anchor_formula` ← float64 — pinned
- `registry_slot` ← §VII.AL — pinned
- `bridge_map` ← Connes-Karoubi pairing ∘ K-theory boundary map — pinned
- `inheritance_kernel_rank` ← rank ≥ 2 — pinned
- `delta_p_cancellation_applicability` ← verified in-script for s=3 + s=4 cocycle pair — pinned (diagnostic)
- `L_max` ← 10 — pinned

### #23 (FWD-C3) machinery enumeration

All free parameters of `computations/s88_w4b_fwd_c3_cocycle_3he_bridge.py`:
- `phi67_norm_FW` ← canonical_constants.py:phi67_norm_FW (S86 W-5 Sage-exact) — pinned
- `phi88_norm_FW` ← canonical_constants.py:phi88_norm_FW (S86 W-5 Sage-exact) — pinned
- `cocycle_ratio_67_88_FW` ← canonical_constants.py:cocycle_ratio_67_88_FW = 7.324992 — pinned
- `level_2_band` ← 7.3250 ± 0.1% (S86 W-5 Gate-2 pre-registered) — pinned
- `level_3_anchor_formula` ← float64 — pinned
- `delta_p_cancellation_residual` ← 0.0e+00 (S86 W-5 DONE-5) — pinned (diagnostic)
- `inheritance_kernel_rank` ← 2 — pinned
- `falsifier_gates` ← Gate1/2/3/4 per inheritance-falsifier-protocol four-gate structure — pinned
- `registry_slot` ← §VII.AM — pinned
- `bridge_map` ← ι_*: A_K → M_2(ℂ) ∘ (Δ_B/Δ_A)^p — pinned
- `lab_data_status` ← <pinned at dispatch> Lancaster MCT-3 + Aalto LTL availability (S87 CF-32 + CF-33) — pinned (BLOCKED on multi-year experimental cycle)
- `L_max` ← 10 — pinned

### #24 (K=3 auto-flip) machinery enumeration

All free parameters of orchestrator-direct edit:
- `K_counter_baseline_S87` ← 2 (W-5 + W11-5) — pinned
- `K_promotion_threshold` ← 3 — pinned
- `auto_flip_trigger` ← K_current >= 3 — pinned
- `rule_file_target` ← `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption" — pinned
- `methodology_allowlist_row` ← W4b-24 — pinned
- `sub_section_edits` ← (a)-(f) enumerated — pinned
- `verdict_lines_input_pin` ← W4b-21, W4b-22, W4b-23 verdict-lines content_sha at runtime — pinned (`<pinned at dispatch>`)
- `K_increment_rule` ← PASS=+1, FAIL=+1, INFO=+0 — pinned (per W11-5 precedent)

## Wave 4b Input-SHA Ledger

(Computed at plan-freeze; pinned at dispatch for runtime SHAs)

| Pin source | Type | SHA pin |
|:-----------|:-----|:--------|
| `.claude/rules/cross-pillar-bridge-anatomy.md` | rule-file | <pinned at plan-freeze> |
| `.claude/rules/inheritance-falsifier-protocol.md` | rule-file | <pinned at plan-freeze> |
| `.claude/rules/registry-landing.md` | rule-file | <pinned at plan-freeze> |
| `.claude/rules/wave-classification.md` | rule-file | <pinned at plan-freeze> |
| `.claude/rules/methodology-wave-allowlist.md` | rule-file (post-W4b-24 row append) | <pinned at plan-freeze> |
| `.claude/rules/phononic-framing.md` | rule-file | <pinned at plan-freeze> |
| `.claude/rules/substrate-first-canonical-sourcing.md` | rule-file | <pinned at plan-freeze> |
| `.claude/rules/mechanical-closure-discipline.md` | rule-file | <pinned at plan-freeze> |
| `computations/canonical_constants.py` | canonical pin (n_s_FW, planck_ns, phi67_norm_FW, phi88_norm_FW, cocycle_ratio_67_88_FW) | <pinned at plan-freeze> |
| `sessions/permanent-results-registry.md` (pre-W4b state) | registry | <pinned at plan-freeze> |
| `sessions/archive/session-88-context.md` | context | <pinned at plan-freeze> |
| Wave 4b verdict lines (W4b-21, W4b-22, W4b-23) | verdict-line content_sha | <pinned at dispatch> (runtime; for #24 only) |

audit_sha256 for each gate is computed via `script-template.py append_verdict()` from input-pin map at runtime per `.claude/rules/gate-verdicts.md` dual-SHA discipline.

---

## Wave 4b dispatch sequence

Sequential dispatch (not parallel) per `feedback_dispatch-discipline.md` ≤8 cap and per Wave 4b's BLOCKED dependencies:

1. **#21 (FWD-C1)** — dispatch conditional on S88 W6 #51 PASS (else mechanical-closure PRE-REG-INC).
2. **#22 (FWD-C2)** — dispatch conditional on S88 W2 Mellin-cone closure (else mechanical-closure PRE-REG-INC).
3. **#23 (FWD-C3)** — dispatch conditional on lab data availability from W11-C5 + W11-C6 (else mechanical-closure PRE-REG-INC pending multi-year experimental cycle).
4. **#24 (K=3 auto-flip)** — dispatch AFTER #21, #22, #23 complete (PASS/FAIL/INFO); orchestrator computes K_current and either fires auto-flip or closes with PRE-REG-INC.

All 4 gates produce verdict lines in `computations/s88_gate_verdicts.txt`; #21/#22/#23 also emit registry-entry appends to `sessions/permanent-results-registry.md` §VII.AK/AL/AM; #24 emits rule-file diff to `.claude/rules/cross-pillar-bridge-anatomy.md`.

## Wave 4b carry-forward template (S89+)

If any of W4b-21/22/23 closes as INFO/PRE-REG-INC, the 4-field carry-forward spec per `feedback_fix-in-session-never-defer.md`:

| # | Carry-forward gate ID | What | Inputs | Gate (PASS predicate) | Effort |
|:--|:----------------------|:-----|:-------|:----------------------|:-------|
| CF-?1 | S89-FWD-C1-N-S-BRIDGE-RETRY | Re-attempt FWD-C1 landing | S88 W6 #51 c_sub canonical pin landed | Level-3 < Level-2 at L_max=10 | ~0.7 wave-eq |
| CF-?2 | S89-FWD-C2-MELLIN-BDG-BRIDGE-RETRY | Re-attempt FWD-C2 landing | S88 W2 Mellin-cone closure landed | Level-3 < Level-2 at L_max=10 | ~1.0 wave-eq |
| CF-?3 | S88+-FWD-C3-COCYCLE-3HE-BRIDGE-RETRY | Re-attempt FWD-C3 landing | Lancaster MCT-3 + Aalto LTL data landed | Level-3 within Level-2 band 7.3250 ± 0.1% | ~1.2 wave-eq |
| CF-?4 | S89-OR-LATER-CF-D-K3-PROMOTION-AUTO-FLIP-RETRY | Re-evaluate K-counter advancement | Any future FWD-candidate landing | K_current >= 3 auto-flip trigger | ~0.4 wave-eq |

Each carry-forward retains the 5-anatomy + 3-level discipline, registry slot allocation, SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure, and substrate framing per `phononic-framing.md` IS-not-IN.

---

**End of session-88-plan-w4b.md**

Wave 4b: 4 gates, GEOMETRIC × 3 (FWD-C1/C2/C3 registry-landings) + METHODOLOGY × 1 (K=3 auto-flip).
Total effort: ~3.3 wave-equivalents (conditional on upstream landings).
mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`.
Verdict source: `computations/s88_gate_verdicts.txt`.
Script prefix: `s88_w4b_<slug>.py`.
