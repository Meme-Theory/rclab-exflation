# Session 90 — Solo Synthesis S-6: §VII.AV Refinement Pathway

**Agent**: volovik-superfluid-universe-theorist (solo independent synthesis)
**Slot**: S-6 of `sessions/archive/session-90/session-90-workshop-schedule.md`
**Format**: `/rclab-review`-style solo synthesis (NO --type, NO --rounds, 1 agent writing
independently; not an adversarial workshop, not a competing-reading rebuttal target;
the W-5 workshop "CF-61 BCS phase transition reading volovik vs connes adversarial"
consumes this solo as upstream input)
**Date**: 2026-05-15

**Substrate framing reminder (per `phononic-framing.md §"IS Space, Not IN Space"`)**:
the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))` at the fixed
single-τ-slice level (Level 1). The BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`
is INTRINSIC to that finite spectral triple — not "in" any container. The BCS gap
equation IS substrate-physics on the L_max-truncated D_K² spectrum; the operational
machinery used to solve it (scalar-Δ fixed-point bisection vs multi-branch s52
Bogoliubov ED) is the methodology-floor F-image of that substrate physics, NOT the
substrate itself. The direction of explanation throughout this synthesis flows FROM
the substrate (BdG sub-algebra Corner-IV K-window log-derivative on `M_2(ℂ)`) →
bridge map (HKR `L_max → ∞`; Connes-Karoubi pairing per CM-1995 §III.4) →
laboratory (Pillar V continuum 3He-B BdG-sector mutual-friction measurement).

---

## §1. Substrate-IS framing of the L_max ≤ 10 BCS phase transition

CF-61's FULL BdG re-derivation across L_max ∈ {6..12} at canonical
(V_BCS = 2.447 × 10⁻⁷ M_KK⁻¹, T = T_fold = 0.640 M_KK) is the highest-leverage
substrate-physics finding of Wave 8. The structural reading lives entirely on the
substrate side; the question is which substrate-side reading is correct.

### §1.1 The data (substrate-IS layer)

The L_max-truncated D_K² spectrum has multiplicity-weighted eigenvalue counts
ranging from 9.9M (L_max=6) to 32.0M (L_max=12). The bottom-eigenvalue
|λ|_min = 0.819741 is L_max-INVARIANT for L_max ≥ 6 — the (0,0) and low-(p,q)
sectors saturate the IR floor; the Casimir-bound feasibility passes at every
L_max (η_min = 0.4365 at sector (1,1) ≥ η_FB_lower = 0.40 per the S87 W11-3
Friedrich-Bär saturation theorem); irrep construction succeeds at every L_max.
Substrate-IS: the spectral triple's finite-L truncation is well-defined and
geometrically faithful at every L_max ∈ {6..12} EXAMINED.

The BCS gap-equation
`inv_V_BCS = Σ_a m_a · tanh(E_a/(2T)) / (2 E_a)` with `E_a = √(λ_a² + Δ²)`
at the canonical pin (V_BCS, T_fold) admits ONLY the trivial Δ=0 solution
for L_max ∈ {6, 7, 8, 9, 10}; only L_max ∈ {11, 12} produce a finite gap
(Δ(11) = 0.1062; Δ(12) = 0.4643 by construction). The transition between
the two regimes is a **structural phase boundary** of the gap equation,
NOT a numerical convergence artifact: the gap-equation residual is
large-negative throughout the bracketing scan at L_max ≤ 10
(−2.68e+06 at L=6; −1.22e+05 at L=10) and converges to 0⁻ smoothly within
the bracketing tolerance at L=11/12. The convergence iteration count
remains finite at every L_max (≤ 2903 iterations at L_max=10; ≤ 87 at
L_max=11/12); the gap-equation is operationally well-behaved at every
truncation. The Δ=0 solution at L_max ≤ 10 is a TRUE fixed point of the
self-consistency map under the canonical pin, NOT a failure of
optimization.

### §1.2 The substrate-physics reading (volovik framing)

This is BCS phase-boundary physics on a finite-rank Bogoliubov sub-algebra
under spectral truncation, evaluated at a single fixed coupling pin
(V_BCS, T_fold). The reading is direct and lives at the substrate layer:

(1) **Spectral support determines BCS critical coupling**. For the BCS gap
equation on the finite-L spectrum to admit a non-trivial fixed point at
fixed (V_BCS, T), the spectral kernel `Σ_a m_a · tanh(E_a/(2T)) / (2 E_a)`
must reach the threshold value `1/V_BCS`. The kernel is a sum of positive
contributions across the substrate's multiplicity-weighted eigenvalue set;
truncating the high-(p,q) sectors at L_max ≤ 10 removes 4.3% of the UV
weight from the kernel sum. At the canonical V_BCS calibrated to the FULL
L_max=12 spectrum, this 4.3% UV deficit pushes the kernel BELOW threshold
at L_max ≤ 10 — the truncated coupling lies BELOW the BCS critical
coupling, the condensate cannot form, and the only fixed point is Δ=0
(the normal-state phase).

This IS substrate-physics, not a regularization artifact. The substrate
WITH its L_max=10 truncation IS in the normal state under the canonical
pin; the substrate WITH its L_max=12 truncation IS in the BCS-paired
state. The transition L_max=10 → L_max=11 IS the substrate's own
spectral-cutoff phase boundary at this specific (V_BCS, T_fold) pin.

(2) **The continuous-interpolation ansatz is an artifact of the SCHEMATIC
proxy, not of the substrate**. The §W5-3 Casimir-bound SCHEMATIC proxy
`Δ_eff(L) = Δ_static · √((C_2(L,L)+1)/(C_2(12,12)+1))` continuously
interpolates between L_max=12 and lower L_max via the Casimir-eigenvalue
ratio — it presupposes that Δ_eff has a smooth functional dependence on
L_max determined only by the largest Casimir admitted at that truncation.
This is an ANSATZ; the substrate's gap equation does not obey it.
FULL BdG re-derivation reveals the structural step.

The corridor "Casimir-bound SCHEMATIC proxy IS a faithful image of the
FULL gap-equation L_max-dependence at canonical (V_BCS, T_fold)" is
STRUCTURALLY FALSE. The §W5-3 proxy SMOOTHED OVER a real phase boundary.

(3) **No PROHIBITED_ACTIONS Class 1 (convention-shopping) license to
modify the pin**. The substrate-natural (V_BCS, T_fold) pin is calibrated
to reproduce Δ_BCS = 0.4643 at L_max=12 (the canonical S70 anchor), and
T_fold = 0.640 is the substrate-natural temperature at τ_fold (canonical
S70). Adjusting either to soften the phase transition would be a
convention-shopping violation per `regulator-convention-lockdown.md`. The
substrate's gap-equation behavior at the canonical pin IS what the
substrate physics reports; the FAIL is substrate-physics-faithful.

### §1.3 The container-thinking forbidden inversion

FORBIDDEN reading (container thinking): *"the BCS phase transition at
L_max ≤ 10 means the substrate goes through a phase transition as we
move it through L_max coordinate space"*. Inverted (substrate-IS): *"L_max
is the substrate's own truncation refining toward the cohomology-class
image; the BCS phase transition at L_max=10/11 IS substrate-IS
information about the operational gap-equation solution path on the
finite-L spectral triple at the canonical pin, NOT a phase transition of
the substrate in some external L_max-parameter container"*.

The substrate IS the spectral triple AT each L_max simultaneously
(the L_max → ∞ tower is the substrate's own continuum closure under HKR);
moving along L_max is not a dynamical evolution of the substrate but a
refinement of which substrate-IS observables are resolved at which
truncation level.

### §1.4 Conclusion of §1

The BCS phase transition at L_max ≤ 10 IS a **substrate-IS structural
phenomenon at the spectral-cutoff axis**, evaluated at a specific
substrate-natural coupling pin (V_BCS, T_fold). Substrate-physics
sub-claim: at the canonical (V_BCS, T_fold), the FULL gap equation on
the L_max-truncated spectrum is sub-critical for L_max ≤ 10 and
super-critical for L_max ≥ 11. The §W5-3 SCHEMATIC proxy's smooth
interpolation hid this structural boundary; CF-61 surfaces it.

This finding closes one corridor in the constraint map: the Casimir-bound
SCHEMATIC proxy is **NOT** a faithful Level-2-binding HKR-image envelope
for Corner-IV at canonical (V_BCS, T_fold). The refinement-pathway
specification of §VII.AV must pivot accordingly.

---

## §2. Substrate-IS framing of the FULL-BdG anchor mismatch direction

The CF-61 L_max=12 anchor mismatch is the second high-leverage finding:
`L_emp(L_max=12, FULL BdG re-derivation) = −5.6188` vs canonical
`L_emp(∞) = −7.0463` (§W5-2 anchor), an absolute deviation of 1.428 M_KK²
units against a tolerance of 1e-9. The FULL re-derivation does NOT
reproduce the §W5-2 canonical anchor at L_max=12 even though Δ(L_max=12)
is bit-close to Δ_BCS by V_BCS-calibration construction
(`|Δ(12) − Δ_BCS| = 1.85e-11`).

### §2.1 The structural mismatch (substrate-IS layer)

The two routes evaluate the SAME substrate-IS observable (variance of
Bogoliubov occupation at the K-window horizon, on the BdG sub-algebra
`M_2(ℂ) ⊂ A_K`) on DIFFERENT operational machineries:

- **§W5-2 route**: multi-branch s52 Bogoliubov ED with Δ_per_mode_static
  (`B1 = 0`, `B2 = 0.7704`, `B3 = 0.176`) determined directly by the 256-state
  Hilbert-space exact diagonalization. The Δ_per_mode_static carries
  three distinct gap values across the three Bogoliubov branches;
  the structure is encoded in the multi-mode ED solution.

- **CF-61 route**: FULL gap-equation self-consistency with a SINGLE
  scalar Δ(L_max), uniformly rescaled across all 8 BdG modes by the ratio
  Δ(L_max)/Δ_static = 0.6026 at L_max=12 (since Δ_static = 0.7704 ≠
  Δ_BCS = 0.4643). The multi-branch structure is collapsed to a scalar.

Both routes are substrate-IS-faithful in the sense that both compute a
single-summand-projection trace on `M_2(ℂ) ⊂ A_K` (Type-F observable per
the layer-separability carve-out classification at `mechanical-closure-
discipline.md §"Layer-separability carve-out"` L3); the substrate-IS
observable IDENTITY is the SAME (Element-1 disambiguation per CF-62
confirms K-window log-derivative on `M_2(ℂ)` as canonical). They differ
in the operational reduction of the substrate's multi-band Bogoliubov
structure: §W5-2 preserves it, CF-61 collapses it to a scalar via the
gap-equation closure.

### §2.2 Two structurally distinct readings of the mismatch

The 1.428-unit gap admits two structurally distinct diagnoses. This is
the crux of the (route ii) vs (route iii) decision in the §VII.AV
refinement pathway space.

**Reading O (Operational mismatch)**: the discrepancy is an
operational-machinery artifact, NOT a regularization-physics statement.
The canonical anchor `L_emp(∞) = −7.0463` was constructed against the
multi-branch ED machinery; the FULL gap-equation route gives a
DIFFERENT scalar Δ(L_max=12) = 0.4643 ≠ Δ_static = 0.7704, hence a
different rescale of the BdG amplitudes, hence a different K-window
log-derivative value at L_max=12. The substrate-IS observable identity
is the same; the EVALUATION pathway differs. The fix is to identify
the canonical K-window normalization that makes the two routes bit-match
at L_max=12, OR to re-pin the anchor against the gap-equation route.

→ Route (iii) **K_canonical pin uniqueness** is the structural fix
under Reading O.

**Reading R (Regularization-physics insufficiency)**: the discrepancy
reflects the SCHEMATIC Casimir-bound proxy's structural inadequacy at
the substrate's actual Mellin regularization layer. The FULL gap
equation on a single-scalar-Δ closure smooths over the multi-band
Bogoliubov structure that the substrate's spectral action a_2
Seeley-DeWitt coefficient (substrate-distance-2 pole `s=4`) genuinely
carries. A FULL Connes-Chamseddine 1996 §2.2-2.3 physical
Pauli-Villars regularization at Λ_UV = M_KK would replace the scalar-Δ
gap closure with the correct multi-mode regulated trace; the resulting
K-window log-derivative should reproduce the §W5-2 canonical anchor.

→ Route (ii) **FULL Connes-Chamseddine 1996 physical multipliers** is the
structural fix under Reading R.

### §2.3 The volovik substrate-physics diagnosis (Reading O is the
substrate-natural diagnosis at S91 entry; Reading R is forward-promotable)

Substrate-physics reading direct from the BCS / Bogoliubov side:

(1) **Δ_BCS and Δ_per_mode_static are NOT the same physical quantity**.
The S70 BCS-GAP-CANONICAL anchor `Δ_BCS = Δ_0_OES = 0.4643` IS the
**global pair-addition energy** from the 256-state Hilbert-space ED
(the BCS canonical gap aliased to the OES = "one-electron-state"
addition energy). The s52 Bogoliubov Δ_per_mode is the **per-branch gap
spectrum** carrying B1=0/B2=0.7704/B3=0.176 across the three Bogoliubov
branches; `max |Δ_per_mode| = 0.7704` is the B2-branch gap, distinct
from the global BCS canonical Δ_BCS.

These two quantities are related by the substrate's multi-band
Bogoliubov problem (`Δ_per_mode^{(i)} = Δ_BCS · √(ω^{(i)}_relative)` in
the symmetric weighting; the B2-branch carries the largest spectral
weight at τ_fold). They are NOT interchangeable in K-window log-
derivative calculations on the truncated spectrum. The FULL gap-equation
route's uniform rescale-by-0.6026 destroys this multi-branch structure;
that is the proximate source of the 1.428-unit mismatch.

(2) **The substrate's natural anchor IS the multi-branch ED anchor**.
The §W5-2 anchor used Δ_per_mode_static directly because the substrate's
BdG sub-algebra `M_2(ℂ) ⊂ A_K` carries the multi-band Bogoliubov
structure intrinsically; the s52 ED solves the substrate's actual
Bogoliubov problem rather than imposing a scalar-gap simplification.
The CF-61 FULL gap-equation route is a methodology-floor F-image of the
substrate physics — useful as a self-consistency check on the BCS
canonical gap, but NOT the substrate-natural K-window log-derivative
evaluation pathway.

The substrate-natural pathway is multi-branch ED; the scalar-Δ
self-consistency is a derivative (and STRICTLY LOSSY) reduction.

(3) **The Casimir-bound SCHEMATIC proxy's inadequacy at L_max ≤ 10 is a
SEPARATE structural finding from the L_max=12 anchor mismatch**. The
phase-transition finding (§1 above) closes the "smooth interpolation
ansatz" corridor; the anchor mismatch finding (§2) reveals that even at
L_max=12 (above the BCS phase boundary), the scalar-Δ machinery does
NOT reproduce the multi-branch substrate-IS anchor. These are two
distinct corridors closed by CF-61, not one.

### §2.4 Conclusion of §2

The anchor mismatch direction at L_max=12 is **substrate-naturally
diagnosed as Reading O (operational machinery mismatch between
scalar-Δ gap closure and multi-branch s52 Bogoliubov ED)**. Substrate
sub-claim: the §W5-2 canonical anchor `L_emp(∞) = −7.0463` IS the
substrate-IS K-window log-derivative when the substrate's multi-band
Bogoliubov structure is preserved (s52 ED route); the CF-61 value
−5.6188 IS the substrate-IS K-window log-derivative when the multi-band
structure is collapsed via scalar-Δ self-consistency (gap-equation
route). Both values are mathematically faithful images of the
substrate's BdG sub-algebra trace under different operational
reductions; they evaluate the same Type-F single-summand projection
observable on `M_2(ℂ)` but at different reductive resolutions of the
substrate's multi-branch structure.

This routes the §VII.AV refinement-pathway space toward **route (iii)
K_canonical pin uniqueness as the substrate-natural primary diagnosis**;
route (ii) FULL Connes-Chamseddine 1996 multipliers remains
forward-promotable as a deeper structural test (Reading R) IF and ONLY
IF route (iii) PASSes empirically — confirming that the §W5-2 anchor
is reproducible by careful multi-branch evaluation — and the residual
disagreement (if any) between the multi-branch evaluation and the
FULL physical PV pipeline could be a TRUE regularization-physics
finding rather than a methodology-machinery artifact.

The substrate-natural ordering of pathway priority is therefore:

(iii) K_canonical pin uniqueness FIRST (Reading O test), THEN
(ii) FULL Connes-Chamseddine multipliers (Reading R test) IF (iii) PASSes.

This is the OPPOSITE of the carry-forward priority implied by CF-70
effort (2.0 wave-equivalents) vs CF-71 effort (1.0 wave-equivalent).
CF-71 is the substrate-natural primary; CF-70 is the deeper backstop.

---

## §3. Pre-registered discriminator-gate spec for S91+

The orchestrator's task spec asks for a discriminator gate that
PASS/FAILs cleanly between routes (ii) and (iii) WITHOUT requiring both
to be computed. The substrate-natural ordering identified in §2 above
suggests CF-71 (K_canonical pin uniqueness) IS itself the
discriminator. Below I pre-register a SHARPENED CF-71 variant
(designate `CF-71D` for "discriminator") with substrate-IS predicates
that PASS the route-iii diagnosis OR FAIL it (forcing route ii without
its own compute).

### §3.1 Gate ID and identity

**Gate ID**: `S91-VII-AV-K-CANONICAL-PIN-UNIQUENESS-DRY-RUN-DISCRIMINATOR`
(SHARPENED variant of CF-71; structurally satisfies the orchestrator's
"PASS/FAIL cleanly between (ii) and (iii) without computing both" spec)

**Trigger**: `[VERIFY-THEOREM]` + `[SIGN]` (directional pre-registration)

**Classification**: GEOMETRIC + PHONONIC (Corner-IV K-window log-
derivative substrate-IS observable on BdG sub-algebra `M_2(ℂ) ⊂ A_K`;
operational-machinery discriminator between scalar-Δ gap closure and
multi-branch s52 Bogoliubov ED at L_max=12 truncation)

**Agent**: volovik-superfluid-universe-theorist PRIMARY (substrate-
superfluid axis: multi-branch Bogoliubov ED on truncated D_K² spectrum;
K-window log-derivative substrate-IS observable identity); connes-ncg-
theorist CO-AUTHOR (Type-F single-summand-projection trace verification
per `mechanical-closure-discipline.md §"Layer-separability carve-out"`);
lizzi-spectral-functional-theorist adversarial REVIEW (regulator-class
neutrality on the K_canonical pin derivation).

### §3.2 Substrate-IS predicates (Steps 1-6 substitution chain)

**Definitions**:

- `Δ_per_mode_static := (B1=0, B2=0.7704, B3=0.176)` per s52 8-mode
  Bogoliubov ED (substrate-natural multi-branch gap spectrum at τ_fold)
- `Δ_BCS := 0.4642547395` (S70 BCS-GAP-CANONICAL-70; global pair-addition
  energy from 256-state Hilbert-space ED, aliased to Δ_0_OES, M_KK units)
- `K_canonical := K_window pin at which the s52 multi-branch K-window
  log-derivative evaluates to L_emp(∞) = −7.046336474406761 at L_max=12`
- `L_emp_full_route(L_max=12) := −5.6187816150 ± 1.851e−11` (CF-61
  output under uniform scalar-Δ rescale; REFERENCE-ONLY)
- `L_emp_multi_branch(L_max=12) := L_emp(∞) by construction at the
  canonical K_canonical pin per the substrate-natural anchor` (§W5-2)
- `K_uniqueness_predicate := |K_canonical_derived − K_canonical_§W5-2|
  < 1e-9` where `K_canonical_derived` is independently derived from the
  substrate's BdG energy gap at τ_fold under CF-62 disambiguation
  (K-window log-derivative as canonical Element-1 per Type-F admissibility).

**Step 1 (Substitution; Reading O hypothesis)**: under Reading O the
§W5-2 anchor IS substrate-IS-faithful and corresponds to a uniquely
derivable K_canonical pin from the substrate's BdG energy gap at
τ_fold (NO regularization-physics defect at this layer). The
discriminator predicate IS:

```
PASS_iii (Reading O confirmed):
  K_canonical_derived UNIQUELY determined from BdG energy gap
                      ∧ |L_emp(multi-branch ED, L_max=12) − (−7.046336)| < 1e-9
                      ∧ Δ_K_canonical_pin < 1e-9
                      ⟹ §VII.AV PROXY-REFINEMENT route (iii) is the
                         structural fix; route (ii) is NOT structurally
                         forced
```

**Step 2 (Substitution; Reading R hypothesis)**: under Reading R the
§W5-2 anchor's reproducibility by multi-branch ED is consistent with
Reading O AT THE METHODOLOGY-FLOOR LAYER but does not yet rule out a
TRUE regularization-physics residual at the substrate's Mellin
regularization layer. However, if K_canonical_derived is NOT
uniquely determined (multiple equally substrate-natural derivations
giving different K values), OR multi-branch ED does NOT reproduce
−7.046336 to machine precision, the structural conclusion flips:

```
FAIL_iii (Reading O falsified → Reading R structurally forced):
  K_canonical_derived AMBIGUOUS (multiple substrate-natural derivations
                                 give substantively different K values,
                                 |ΔK| ≥ 1e-9)
                      ∨ |L_emp(multi-branch ED) − (−7.046336)| ≥ 1e-9
                      ⟹ §VII.AV PROXY-REFINEMENT route (iii) FAILs;
                         route (ii) FULL Connes-Chamseddine multipliers
                         is structurally FORCED as the only remaining
                         refinement direction
```

**Step 3 (Substitution; INFO band)**: a structurally-intermediate
outcome (K_canonical_derived uniquely determined BUT |L_emp − (−7.046)|
in the band [1e-9, 1e-6]) routes to INFO, indicating route (iii) is
PARTIALLY substrate-natural — the K_canonical pin is unique but the
multi-branch evaluation carries small residual systematics (likely
finite-L_max ED truncation effects rather than a Reading R / Reading O
discrimination). In the INFO band BOTH routes remain forward-promotable;
the discriminator does not cleanly fire.

**Step 4 (Simplification)**: per `cross-pillar-bridge-anatomy.md §"Level-2
sub-class (binding vs non-binding)"` SUGGESTION K=1, the Level-2-binding
admissibility test is that the HKR `L_max → ∞` image MUST bind the
Level-1 cohomology-class identity to the laboratory-IN observable. A
PASS_iii verdict above CONFIRMS the substrate-IS HKR-image bridge from
multi-branch ED at L_max=12 to the §W5-2 anchor; this admits §VII.AV
to STAGE-1-CANDIDATE promotion via route (iii). A FAIL_iii verdict
FORCES the refinement pathway to route (ii) without requiring route
(iii)'s own forward compute.

**Step 5 (Direction)**: the discriminator's verdict structure is:

```
PASS_iii ⟹ §VII.AV STAGE-1-CANDIDATE via route (iii)
            ∧ CF-70 (route (ii) FULL Connes-Chamseddine) becomes
              OPTIONAL backstop / Reading R deeper test (still
              forward-promotable but no longer route-blocking)
FAIL_iii ⟹ §VII.AV remains REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT
            until CF-70 PASSes
            ∧ CF-70 (route (ii)) becomes MANDATORY refinement pathway
INFO_iii ⟹ §VII.AV remains REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT
            ∧ BOTH CF-70 + CF-71 remain forward-promotable; the
              discriminator did not fire cleanly
```

**Step 6 (Conclusion)**: the discriminator PASSes route (iii) cleanly,
FAILs cleanly (routing to (ii)), or returns INFO (both pathways open).
This satisfies the orchestrator's spec "PASS/FAILs cleanly between
(ii) and (iii) WITHOUT requiring both to be computed" — the FAIL_iii
branch FORCES route (ii) without computing it (CF-70 dispatch is
mandated downstream); the PASS_iii branch CLOSES the refinement-
pathway question via route (iii) and demotes CF-70 to optional.

### §3.3 The dry-run feasibility (substrate framing)

The CF-71D variant is termed "dry-run" because the substrate-physics
K_canonical pin derivation can be carried out WITHOUT a new L_max scan:

(i) The §W5-2 anchor source script computes `L_emp(L_max=12) =
−7.0463` via multi-branch s52 Bogoliubov ED with a specific K_canonical
pin value — that pin is recoverable by direct read of the §W5-2 source
artifact (`sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md`
referenced source workshop is for §VII.AQ on a DIFFERENT observable;
the §W5-2 actual source is the S89 W5-2 producing script, located via
`s88-pending-edits-ledger.md` theorem-rerouting action preserving the
−7.046336 anchor as SOLE Corner-IV calibration source).

(ii) The "uniqueness" question is whether the K_canonical value
derives uniquely from the substrate's BdG energy gap at τ_fold under
CF-62 disambiguation, or whether multiple substrate-natural derivations
give different K values. The substrate-natural derivation IS the
K-window centered on the BdG gap scale; the BdG gap at τ_fold is
calibrated to Δ_BCS = 0.4643. The candidate K_canonical pins:
- K = Δ_BCS (BCS gap as K-window center): natural BCS calibration
- K = max |Δ_per_mode| = 0.7704 (B2-branch gap): natural multi-branch
  calibration
- K = (Δ_per_mode_weighted)^{1/2} = some mean over modes
- K = T_fold = 0.640 (substrate-natural temperature)
- K = 1.0 (M_KK unit baseline)

Each of these is substrate-natural at a different reductive layer;
the discriminator requires identification of WHICH one is the canonical
choice under CF-62 disambiguation (K-window log-derivative as canonical
Element-1 on `M_2(ℂ)`). The CF-71D dry-run audits the §W5-2 producing
script + applies the CF-62 Type-F admissibility test to the K_canonical
candidates.

(iii) Effort estimate: 0.5 wave-equivalents (no new L_max scan; read
source script + 5-candidate audit + multi-branch ED re-evaluation at
L_max=12 only).

### §3.4 PASS/FAIL/INFO bands (pre-registered numerical thresholds)

```
PASS_iii:    K_canonical UNIQUE
             ∧ |L_emp(multi-branch ED, L_max=12) − (−7.046336474406761)|
                < 1e-9 (machine-precision bit-match required)
             ∧ K_candidate set narrowed to exactly 1 substrate-natural choice
             ⟹ §VII.AV STAGE-1-CANDIDATE promotion licensed via route (iii)

INFO_iii:    K_canonical UNIQUE
             ∧ |L_emp(multi-branch ED, L_max=12) − (−7.046336)|
                ∈ [1e-9, 1e-6) (mild residual systematics; substrate-
                                 natural but finite-L_max ED truncation
                                 effects)
             ⟹ §VII.AV remains REGISTRY-INCOMPLETE-PENDING-PROXY-
                REFINEMENT; both routes (ii) and (iii) remain
                forward-promotable

FAIL_iii:    K_canonical AMBIGUOUS (≥ 2 substrate-natural K_candidates
                                    with substantively distinct |Δ K| ≥ 1e-9)
             ∨ |L_emp(multi-branch ED, L_max=12) − (−7.046336)| ≥ 1e-6
             ⟹ route (iii) closed; route (ii) STRUCTURALLY FORCED;
                CF-70 promotes from forward-promotable to MANDATORY
                refinement pathway

3-tuple schema-v2 annotation (S87+):
  sign_verdict     := PASS iff K_unique ∧ L_emp_match
  magnitude_verdict := PASS iff |L_emp − (−7.046336)| < 1e-9
  regime_verdict    := VALID iff substrate-natural K_canonical derivation
                       carried out under CF-62 disambiguation
                       (Type-F single-summand-projection trace; no
                       container-thinking inversion)
```

### §3.5 Substrate framing of the discriminator outcome (forward-looking)

Under volovik's reading: PASS_iii is the substrate-natural expected
outcome. The §W5-2 anchor was constructed at the substrate's BdG sub-
algebra layer with the multi-branch Bogoliubov ED structure preserved;
the K_canonical pin is most likely K = Δ_BCS or K = max |Δ_per_mode|
under one of the substrate-natural calibrations; the §W5-2 producing
script is reproducible at L_max=12 to machine precision. The
discriminator is LIKELY to fire PASS_iii.

IF PASS_iii fires, §VII.AV promotes to STAGE-1-CANDIDATE via route (iii)
and Stage-2 cross-axis independent-verify per `joint-theorem-promotion.md
§"Stage 2"` becomes dispatchable in S91+ (CF-68 currently BLOCKED on
§VII.AV STAGE-1-CANDIDATE absence — a CF-71D PASS unblocks it).

IF FAIL_iii fires, the substrate's BdG sub-algebra K-window log-
derivative carries a TRUE regularization-physics layer above the
multi-branch ED layer; route (ii) FULL Connes-Chamseddine 1996
multipliers becomes the structurally-mandated refinement pathway. This
is a deeper substrate-physics finding than the current CF-61 phase-
transition closure (which closes the SCHEMATIC Casimir-bound proxy
corridor without yet identifying the substrate-natural alternative
machinery).

The discriminator does NOT require dispatching CF-70 to make the
decision; the FAIL_iii branch FORCES the route (ii) dispatch
downstream but the choice itself is made by CF-71D alone.

---

## §4. Substrate-IS framing of §VII.AV STAGE-1-CANDIDATE promotion
eligibility under each route

### §4.1 Route (iii) PASS path

Under CF-71D PASS_iii, the substrate's K_canonical pin uniqueness is
confirmed and the multi-branch s52 Bogoliubov ED reproduces the §W5-2
anchor to machine precision at L_max=12. The Level-2-binding admissibility
test (per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding
vs non-binding)"`) is satisfied:

- The HKR `L_max → ∞` image IS the multi-branch ED limit; the
  substrate's BdG sub-algebra trace converges in `L_max` to the §W5-2
  anchor at d=4 substrate-distance-2 pole `s=4`.
- The bridge map BINDS the Level-1 cohomology-class identity (Cell IV
  Corner-IV K-window log-derivative on `M_2(ℂ) ⊂ A_K`) to the
  laboratory-IN observable (Pillar V continuum 3He-B BdG-sector
  mutual-friction).
- The convergence envelope `L^{-3}` at d=4 is empirically extractable
  from the multi-branch ED L_max scan (NOT the scalar-Δ scan that
  CF-61 attempted; the multi-branch route bypasses the BCS phase
  transition because Δ_per_mode_static is L_max-INDEPENDENT — the
  per-branch gaps are determined by the substrate's 256-state ED
  solution, not by self-consistent gap-equation closure on the
  truncated spectrum).

§VII.AV STAGE-1-CANDIDATE promotion is LICENSED under this route. The
registry text updates as follows:

- `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` → `STAGE-1-CANDIDATE`
- Level-2 envelope realization tag: `multi-branch-s52-bogoliubov-ED-L-max-scan`
  (replaces the SCHEMATIC `Casimir-bound-proxy` tag)
- Bridge-map citation: HKR `L_max → ∞` via multi-branch ED + CM-1995
  §III.4 finite-spectral-triple residue formula
- α exponent: extracted from multi-branch ED L_max scan (forward gate
  CF-71D-FOLLOWUP at S91+ to do the L_max scan once the K_canonical
  pin is confirmed; effort 0.5 wave-equivalent)
- HIT K-counter advances K=4 → K=5 (route (iii) PASS at distinct
  algebraic-envelope class from CF-64's K=4 instance; Hybrid
  Independence Test passes via clause (iv) independent algebraic envelope
  for multi-branch ED vs the FWD-C1 Hochschild pairing envelope of
  §VII.AU.OP-PROJ)
- Level-2-binding K-counter advances K=1 → K=2 (route (iii) PASS is
  the second positive calibration instance after §VII.AF.1 W-5 baseline)

The promotion-eligibility under route (iii) is structurally clean: one
calibration corpus instance per K-counter advance; bridge-anatomy 5
elements all satisfied; substrate-IS direction-of-explanation preserved
(substrate IS the multi-branch BdG sub-algebra at τ_fold → bridge HKR
L_max → ∞ → laboratory Pillar V continuum).

### §4.2 Route (ii) PASS path

Under CF-71D FAIL_iii forcing CF-70 dispatch, OR under CF-70 voluntarily
dispatched alongside a PASS_iii CF-71D (the optional-backstop case):

The FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers route
deploys the 2-point Pauli-Villars regularization at Λ_UV = M_KK with
coefficients `c_1 = +2`, `c_2 = −1` and regulator masses `M_1 = M_KK`,
`M_2 = M_KK · √2` per the canonical PRIMARY implementation at
`computations/_pauli_villars_subtraction.py` (S88 W13-159; CF-66
confirmed this as the canonical FULL physical PV pipeline at
substrate-distance-2 pole s=4 ADVISORY band).

The Level-2-binding admissibility test under this route requires:

- The FULL physical PV-regulated K-window log-derivative IS the
  substrate-IS observable; the SCHEMATIC Casimir-bound proxy
  (§W5-3) is the methodology-floor F-image
- HKR `L_max → ∞` image converges to the §W5-2 anchor under PV
  regularization (this requires that the §W5-2 anchor itself IS a
  FULL physical PV evaluation, not just multi-branch ED — a question
  the CF-71D dry-run answers)
- The convergence envelope `L^{-3}` extracts cleanly under the FULL PV
  L_max scan

§VII.AV STAGE-1-CANDIDATE promotion under route (ii) is structurally
clean BUT carries an additional layer of UV-regulator commitment that
route (iii) does not: under route (ii), the §VII.AV substrate-IS
observable identity is explicitly tied to the FULL Connes-Chamseddine
1996 physical multipliers (not just the substrate's intrinsic multi-
branch ED). The promotion semantics under route (ii):

- `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` → `STAGE-1-CANDIDATE`
- Level-2 envelope realization tag: `full-Pauli-Villars-CC1996` (replaces
  SCHEMATIC `Casimir-bound-proxy`)
- Convention tag on Element 3 fiducial-anchor binding (per
  `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`
  S90 W7-4 CF-57 axis β SUGGESTION-K=1): scheme suffix
  `-FULL-CC1996-MULTIPLIERS` recommended on the verdict-line
  `convention=` field per `regulator-pin-discipline.md §"K=4 SCHEMATIC
  level-pin promotion"` MANDATORY at K=4 (S88 W7b-83 close)
- Cross-link to FULL-tier PV pipeline at S61/S78
- HIT K-counter K=4 → K=5 (same algebraic-envelope-independence reasoning)
- Level-2-binding K-counter K=1 → K=2 (under route ii rather than route iii)

### §4.3 Comparative substrate-IS reading

Both routes are substrate-IS-faithful at PASS; both license §VII.AV
STAGE-1-CANDIDATE promotion. They differ in the **substrate-natural
ordering of regularization layers**:

- Route (iii) treats the substrate's intrinsic multi-branch Bogoliubov
  ED as the canonical evaluation layer; the s52 ED IS substrate-natural
  for the BdG sub-algebra K-window log-derivative. UV regularization
  enters only at the finite-L_max truncation choice (which is the
  substrate's own spectral-cutoff axis, not an external regulator).
- Route (ii) treats the FULL Connes-Chamseddine 1996 physical
  Pauli-Villars regularization at Λ_UV = M_KK as the canonical
  evaluation layer; the multi-branch ED IS still present but
  regularized at the UV scale by a substrate-external regulator
  (M_PV = M_KK is substrate-natural at the compactification scale,
  but the PV pair is an additional regularization layer beyond the
  substrate's intrinsic finite-L_max truncation).

Under volovik substrate-physics ordering, route (iii) is the
substrate-natural primary because the substrate's BdG sub-algebra
carries the multi-branch structure intrinsically; the multi-branch ED
solution IS the substrate-natural observable evaluation. Route (ii)
is a DEEPER structural test that becomes mandated only if route (iii)
fails to reproduce the canonical anchor — which would imply a TRUE
regularization-physics layer above the substrate's intrinsic
multi-branch ED.

The S91+ plan-freeze priority ordering for CF-70 vs CF-71 dispatch
follows directly:

1. CF-71D (sharpened K_canonical pin uniqueness discriminator):
   FIRST, 0.5 wave-equivalents, substrate-natural primary diagnosis.
2. CF-71D outcome → conditional CF-70 dispatch:
   - PASS_iii: CF-70 demoted to OPTIONAL backstop (deeper-layer test;
     forward-promotable but not route-blocking).
   - FAIL_iii: CF-70 promoted to MANDATORY refinement pathway,
     2.0 wave-equivalents.
   - INFO_iii: BOTH CF-70 + CF-71D-FOLLOWUP forward-promotable.

This ordering is the OPPOSITE of the carry-forward effort estimates
(CF-71 = 1.0 wave-eq, CF-70 = 2.0 wave-eq) AND the OPPOSITE of the
W8 carry-forward numbering (CF-70 listed first as the "post-CF-61 FAIL
pivot"). Substrate-physics priority routes CF-71D first.

---

## §5. Level-1 vs Level-2 substrate-IS layer assignment for the BCS
phase transition phenomenon

Per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-
IS levels"` K=2 MANDATORY since S88 W-7 V.4: substrate-IS observables
inhabit TWO STRUCTURALLY ORTHOGONAL substrate-IS levels — Level 1
(single-τ-slice substrate-IS at fixed τ) and Level 2 (moduli-deformation
substrate-IS across τ-extension).

### §5.1 The phenomenon at Level 1 (single-τ-slice at τ_fold = 0.19)

At τ_fold = 0.19 (fixed; the canonical S12/S42 CONST-FREEZE-42 pin),
the BCS phase transition at L_max ≤ 10 IS a Level-1 single-τ-slice
substrate-IS phenomenon. The substrate at τ_fold IS the spectral triple
`(A_K, H_K, D_K(τ_fold = 0.19))`; the BdG sub-algebra `M_2(ℂ) ⊂ A_K`
is intrinsic to that fixed-τ-slice spectral triple; the BCS gap equation
on the L_max-truncated D_K² spectrum at this fixed τ IS sub-critical for
L_max ≤ 10 and super-critical for L_max ≥ 11.

This Level-1 reading is structurally well-defined and is the
substrate-IS framing recorded in the CF-61 working-paper section
(WP §W8-3 line 514): the substrate IS the spectral triple at
τ_fold = 0.19; the BCS phase transition IS substrate-IS information
about the gap-equation solution path on the finite-L spectral triple
at the canonical (V_BCS, T_fold) pin; it is NOT a phase transition of
the substrate moving through some L_max-coordinate space.

### §5.2 The phenomenon at Level 2 (moduli-deformation across τ)

A Level-2 moduli-deformation substrate-IS reading would ask:
does the BCS phase transition L_max threshold (currently L_max=10/11 at
τ_fold = 0.19) lift under τ-extension to τ ∈ {0.18, 0.19, 0.20}?
Specifically, at neighboring τ values, does the same canonical
(V_BCS, T) pin produce a different L_max critical threshold, or does
the L_max=10/11 boundary persist as a τ-invariant substrate-IS
structural property?

This Level-2 question is queued at CF-69 (Level-2 moduli-deformation
substrate-IS extension for §VII.AU, PRE-REGISTERED in plan line 2316)
but framed in CF-69 as scoped to §VII.AU rather than §VII.AV.
Substrate-physics reading: the analogous CF-69 extension for §VII.AV
would re-evaluate CF-61's full BdG re-derivation at L_max ∈ {6..12}
across τ ∈ {0.18, 0.19, 0.20}; if the BCS phase boundary persists as
L_max=10/11 INVARIANT across this τ-window, the substrate has a
Level-2 moduli-invariant spectral-cutoff critical truncation; if the
boundary shifts substantively with τ (e.g., L_max=9/10 at τ=0.18 and
L_max=11/12 at τ=0.20), the phenomenon is Level-1-specific and the
Level-2 moduli-deformation lift carries non-trivial dependence.

### §5.3 The substrate-IS layer assignment for CF-61's FAIL

CF-61's verdict-line `convention=corner-iv-K-window-log-derivative-
substrate-IS` and the §VII.AV registry-text Level-1 single-τ-slice
MANDATORY tag (registry line 17918) BOTH place the substrate-IS
observable at Level 1 single-τ-slice at τ_fold = 0.19. The CF-61
finding IS recorded as a Level-1 substrate-IS property of the
spectral triple at the fixed τ_fold pin.

The Level-2 moduli-deformation extension is a SEPARATE substrate-IS
question; its answer is NOT determined by CF-61's Level-1 result alone.
Two structurally distinct Level-2 outcomes are consistent with
CF-61's Level-1 FAIL:

(α) **Level-2-INVARIANT outcome**: the L_max=10/11 BCS phase boundary
    persists at all τ ∈ {0.18, 0.19, 0.20}; the substrate has a
    τ-INVARIANT spectral-cutoff critical truncation under canonical
    (V_BCS, T_fold). This would be a STRONGER substrate-IS structural
    finding than CF-61 alone: a substrate-intrinsic moduli-invariant
    BCS-critical-L_max property. The §VII.AV refinement pathway space
    might invert — the phase transition IS a τ-invariant substrate-IS
    fact about the BdG sub-algebra, and the refinement direction
    becomes "embrace the L_max ≥ 11 admissible window as the
    substrate-natural Level-2-binding extraction window" rather than
    "smooth over the phase boundary".

(β) **Level-2-DEFORMABLE outcome**: the L_max critical threshold shifts
    with τ; the canonical τ_fold = 0.19 happens to lie near the
    L_max=10 / L_max=11 boundary; nearby τ values shift the boundary
    monotonically. This would indicate the phase-transition is a
    Level-1-specific accident at τ_fold; the Level-2 extension would
    reveal continuous τ-dependence in the L_max-critical-coupling
    structure, and the substrate-natural refinement direction would be
    "find the τ-band where the BCS phase is super-critical at all
    L_max ∈ {6..12}" or equivalently "re-pin V_BCS at a substrate-
    natural value that lifts the τ_fold = 0.19 truncation entirely
    into the super-critical band".

### §5.4 Conclusion of §5: the CF-61 finding is canonically Level 1; a
Level-2 lift is forward-promotable

The CF-61 BCS phase transition IS canonically a Level-1 single-τ-slice
substrate-IS phenomenon at τ_fold = 0.19. The §VII.AV registry text
correctly tags this at the Level-1 layer. A Level-2 moduli-deformation
extension (analogous to CF-69 for §VII.AU but scoped to §VII.AV) is
forward-promotable and would advance the
`phononic-framing.md §"Single-τ-slice vs moduli-deformation"` K-counter
toward saturation; it would also discriminate between outcomes (α) and
(β) above, with substrate-physics implications for the refinement
pathway selection.

This Level-2 extension does NOT block §VII.AV STAGE-1-CANDIDATE
promotion via CF-71D PASS_iii or CF-70 PASS at the Level-1 layer; the
Level-2 question is INDEPENDENT structural enrichment, not a
prerequisite. The promotion semantics route through Level-1 (which
CF-71D / CF-70 address); the Level-2 extension is a subsequent
refinement.

---

## §6. Carry-forward (4-field spec per `feedback_fix-in-session-never-defer.md`)

### CF-71D — §VII.AV K_canonical pin uniqueness DRY-RUN DISCRIMINATOR
(SHARPENED variant of W8 WP CF-71)

- **What**: Pre-registered substrate-IS DISCRIMINATOR gate
  `S91-VII-AV-K-CANONICAL-PIN-UNIQUENESS-DRY-RUN-DISCRIMINATOR`. PASS_iii
  certifies the §VII.AV K_canonical pin uniqueness and route (iii) as
  the structural fix for the CF-61 anchor mismatch; FAIL_iii forces
  route (ii) (FULL Connes-Chamseddine 1996 multipliers) as the only
  remaining refinement pathway WITHOUT requiring route (ii) to be
  computed at this gate. INFO_iii leaves both routes forward-promotable.
  Verdict structure: 3-tuple schema-v2 (`sign_verdict`,
  `magnitude_verdict`, `regime_verdict`); 5-candidate K_canonical
  substrate-natural audit; multi-branch s52 Bogoliubov ED reproduction
  test at L_max=12 only.
- **Inputs**:
  - §W5-2 source producing script for the L_emp(L_max=12) = −7.046336
    canonical anchor (locate via `s88-pending-edits-ledger.md`
    theorem-rerouting action; the original §W5-2 W5 producing script
    in `computations/session-87/` (per W5-2 line 619 reference in CF-62
    audit-log table)
  - CF-61 output `s90_w8_corner_iv_full_bdg_rederive_per_lmax.npz`
    (audit_sha = `6357ab9650615732363c24d89e588569dc5c37f04bef7362e538b1677335b716`;
    REFERENCE-ONLY since CF-61 FAILed)
  - CF-62 output `s90_w8_fwd_c2_substrate_is_disambiguation.npz`
    (audit_sha = `8b4bfdee600fceb771caf30fe0c8ce99a1c4c210264a9e738edf67e12d328b58`;
    Type-F admissibility test pin)
  - canonical_constants.py: `Delta_BCS = 0.4642547394830737` (line per
    S70 BCS-GAP-CANONICAL-70); `tau_fold = 0.19`; `T_BCS = 0.64`;
    `M_KK = 7.428660036284456e16`
  - L_max=12 master spectrum cache `s84_spectrum_cache_L12_tau019.npz`
    (substrate-IS eigenvalue cache; not the canonical multi-branch ED
    cache which is at `s52_bogoliubov_amp` provenance)
  - 5-candidate K_canonical substrate-natural set: {Δ_BCS,
    max|Δ_per_mode|, weighted-Δ-mean, T_fold, 1.0 M_KK-baseline}
  - mechanical-closure-discipline.md §"Layer-separability carve-out"
    L1-L4 (Type-F admissibility predicate)
  - cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs
    non-binding)" (Level-2-binding admissibility)
  - phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-
    IS levels" (Level-1 single-τ-slice tag)
  - regulator-pin-discipline.md §"K=4 SCHEMATIC level-pin promotion"
    (UV-regulator axis & Binding-axis convention-tag discipline)

- **Gate**: PASS_iii iff (K_canonical UNIQUELY DERIVED from BdG energy
  gap at τ_fold = 0.19 under CF-62 disambiguation; 5-candidate audit
  narrows to exactly 1 substrate-natural choice) ∧ (|L_emp(multi-branch
  s52 ED at L_max=12, K = K_canonical_derived) − (−7.046336474406761)|
  < 1e-9). INFO_iii iff K_unique ∧ |L_emp residual| ∈ [1e-9, 1e-6).
  FAIL_iii iff (K_canonical ambiguous, ≥ 2 substrate-natural candidates
  with |ΔK| ≥ 1e-9 OR |L_emp residual| ≥ 1e-6). Composite verdict per
  `gate-verdicts.md §"S87+ canonical form"` collapse rule:
  `sign_verdict=PASS ⇒ composite=PASS; sign_verdict=FAIL ⇒ composite=FAIL`.
  Routing: PASS_iii → §VII.AV STAGE-1-CANDIDATE; FAIL_iii → CF-70
  promotes to MANDATORY refinement pathway; INFO_iii → both routes
  forward-promotable.

- **Effort**: 0.5 wave-equivalents (no new L_max scan; read source
  script + 5-candidate K_canonical substrate-natural audit + multi-
  branch ED re-evaluation at L_max=12 only). PRIORITY: HIGH —
  substrate-natural primary diagnosis; FIRST dispatch in the §VII.AV
  refinement-pathway resolution chain at S91+; ordering precedence
  OVER CF-70 per substrate-physics ordering identified in §2-3 above.

### CF-AV-L2-MODULI — §VII.AV Level-2 moduli-deformation extension
(SUBORDINATE forward gate; CF-71D analog for §VII.AV substrate-IS
moduli-deformation layer)

- **What**: Extend CF-61's FULL BdG re-derivation from Level-1
  single-τ-slice at τ_fold = 0.19 to Level-2 moduli-deformation across
  τ ∈ {0.18, 0.19, 0.20}. Discriminate Level-2-INVARIANT (α) vs
  Level-2-DEFORMABLE (β) outcomes per §5.3 above. Forward-promotable
  whether CF-71D PASSes (Level-2 extension as deeper structural
  enrichment) or FAILs (Level-2 extension as additional diagnostic on
  the route (ii) refinement pathway).
- **Inputs**: CF-61 output (REFERENCE; audit_sha
  `6357ab9650615732...`); L_max=12 master spectrum caches at
  τ = 0.18 + τ = 0.20 (NEW — would require building if not extant);
  canonical V_BCS calibration at each τ (substrate-natural;
  V_BCS(τ) calibrated to reproduce Δ_BCS(τ) at L_max=12);
  CF-71D verdict + K_canonical pin determination;
  phononic-framing.md §"Single-τ-slice vs moduli-deformation".
- **Gate**: PASS iff Level-2-INVARIANT BCS phase boundary (L_max=10/11
  threshold persists across τ-window). INFO iff boundary shifts within
  ±1 L_max across the window. FAIL iff boundary shifts ≥ 2 L_max
  across the window. Routing: PASS → substrate-IS Level-2 moduli-
  invariant BCS critical truncation theorem candidate;
  INFO → continuous τ-dependence noted; FAIL → Level-1-accident
  reading (boundary is a Level-1 accidental property of τ_fold = 0.19
  choice; refinement direction is V_BCS re-pin).
- **Effort**: 2.0 wave-equivalents (3 × τ-value L_max scan; each
  τ-extension carries its own L_max ∈ {6..12} compute; canonical V_BCS
  re-calibration per τ; 8-mode Bogoliubov ED at each (τ, L_max)
  combination). PRIORITY: MEDIUM — substrate-IS Level-2 enrichment;
  subordinate to CF-71D resolution.

### CF-70-CONDITIONAL — §VII.AV proxy-refinement via Connes-Chamseddine
1996 physical multipliers (CONDITIONAL on CF-71D FAIL_iii; per
substrate-physics ordering identified in §2-3 above)

- **What**: Carry-forward of W8 WP CF-70 with substrate-physics
  conditional structure: CF-70 dispatch MANDATORY iff CF-71D FAIL_iii;
  OPTIONAL backstop iff CF-71D PASS_iii (deeper-layer Reading R test
  for residual UV-regulator dependence beyond multi-branch ED);
  forward-promotable iff CF-71D INFO_iii. Substantive content
  unchanged from W8 WP CF-70: deploy
  `computations/_pauli_villars_subtraction.py` 2-point Pauli-Villars
  pipeline at Λ_UV = M_KK with `M_1 = M_KK`, `M_2 = M_KK · √2`,
  `c_1 = +2`, `c_2 = −1` per Connes-Chamseddine 1996 §2.2-2.3;
  evaluate FULL physical PV-regulated K-window log-derivative on the
  L_max-truncated BdG sub-algebra; reproduce §W5-2 canonical anchor at
  L_max=12 to machine precision; extract α exponent at substrate-
  distance-2 pole `s=4`; verdict-line convention tag carries
  `-FULL-CC1996-MULTIPLIERS` scheme suffix per
  `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`
  SUGGESTION-K=1 advancement.
- **Inputs**: `computations/_pauli_villars_subtraction.py`
  (S88 W13-159 canonical PRIMARY 2-point PV; input_sha
  `eaf98037ddc2a4d7…` per CF-66 audit); §W5-2 canonical anchor
  `L_emp(L_max=12) = −7.046336474406761`; CF-61 output (REFERENCE-
  ONLY); CF-71D verdict (PASS_iii / INFO_iii / FAIL_iii); s84
  L_max=12 master spectrum cache; canonical_constants.py
  `Λ_UV = M_KK = 7.428660036284456e16`.
- **Gate**: PASS iff `α ∈ [2.5, 3.5]` AND `R² ≥ 0.95` AND
  `|L_emp(L_max=12, FULL PV CC1996) − (−7.046336)| < 1e-9` under
  Connes-Chamseddine multipliers. PASS triggers §VII.AV PROXY-
  REFINEMENT → STAGE-1-CANDIDATE via route (ii); advances
  Level-2-binding K-counter K=1 → K=2 (under route ii). Routing
  conditional on CF-71D upstream verdict: MANDATORY dispatch under
  CF-71D FAIL_iii; OPTIONAL-BACKSTOP under CF-71D PASS_iii;
  FORWARD-PROMOTABLE under CF-71D INFO_iii.
- **Effort**: 2.0 wave-equivalents (FULL physical PV pipeline at
  Λ_UV = M_KK; L_max scan L_max ∈ {6..12}; α extraction with R² test;
  L_max=12 anchor bit-match verification). PRIORITY: HIGH iff
  CF-71D FAIL_iii; MEDIUM iff CF-71D PASS_iii; MEDIUM iff CF-71D
  INFO_iii.

---

## §7. Audit trail closure for this synthesis

**Conclusions feed into**:

- S91 plan-freeze priority ordering for CF-70 vs CF-71 dispatch
  → CF-71D (sharpened) FIRST, substrate-natural primary diagnosis
  → CF-70-CONDITIONAL conditional on CF-71D outcome
  → CF-AV-L2-MODULI subordinate to CF-71D resolution
- W-5 workshop "CF-61 BCS phase transition reading volovik vs connes
  adversarial" (S91+ workshop schedule item)
  → This solo synthesis IS upstream input to W-5; the connes-side
    reading of the BCS phase transition + L_max=12 anchor mismatch
    is the W-5 workshop's adversarial counterpart; W-5 R1 dispatches
    volovik (with this synthesis pre-loaded) + connes (with their own
    independent reading) on the substrate-physics adjudication

**Substrate-IS direction-of-explanation audit** (per `phononic-framing.md
§"IS Space, Not IN Space"` audit pattern):

- Substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))` at
  Level-1 single-τ-slice; the BdG sub-algebra `M_2(ℂ) ⊂ A_K` is
  INTRINSIC.
- Bridge map IS HKR `L_max → ∞` (Connes-Karoubi pairing per CM-1995
  §III.4 finite-spectral-triple residue formula on the BdG sub-algebra
  restriction).
- Laboratory IN Pillar V continuum 3He-B BdG-sector mutual-friction
  measurement (intrinsic-to-laboratory: helium cryostat container OR
  Lancaster MCT-3 / Helsinki ROTA cells per inheritance-falsifier
  calibration corpus).
- Container-thinking forbidden inversions guarded against:
  - "the substrate moves through L_max coordinate space" → INVERT:
    "L_max is the substrate's own truncation refining toward the
    cohomology-class image"
  - "BCS phase transition IN spectral-cutoff container" → INVERT:
    "the BCS phase transition IS substrate-IS information about the
    operational gap-equation solution path at the canonical pin"
  - "FWD-C2 inhabits a Pillar II Mellin-cone state-space container" →
    INVERT: "the substrate IS the spectral triple; the BdG sub-algebra
    IS an intrinsic single-summand of A_K; the K-window log-derivative
    IS a single-summand-projection trace at the operator-algebra layer"
    (per CF-62 disambiguation §V Step 6)

**Solo synthesis dispatch parameters**: 1 agent (volovik-superfluid-
universe-theorist), no --rounds, no --type, no competing-reading
rebuttal target; this synthesis IS upstream input to the S91+ W-5
workshop CF-61 adversarial review per the slot S-6 task spec.

**File**: `sessions/archive/session-90/session-90-volovik-s6-vii-av-pathway-
synthesis.md` (this file).

**No verdict-line emission** (this is a solo synthesis, not a
computation gate; no compute artifacts; the S91 plan author consumes
this synthesis as priority-ordering input for the §VII.AV refinement-
pathway dispatch chain).
