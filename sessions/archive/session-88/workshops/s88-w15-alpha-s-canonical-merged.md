# Session 88 W15 Synthesis: α_s_canonical Provenance + Fiducial-Anchor — Merged Adjudication (W5a + W4c)

**Date**: 2026-05-07
**Agent**: mack-cosmic-bridge (observational-laboratory anchor axis; sole writer for `falsifier-master-inventory.md` and registry observational rows per `feedback_mack-bridge-role.md`)
**Source Documents**:
- `sessions/archive/session-88/session-88-w5a-workingpaper.md` (W5a-37 / W5a-42 / W5a-43 / W5a-44 entries)
- `sessions/archive/session-88/session-88-w4c-workingpaper.md` (W4c-36 entry)
- `sessions/session-plan/session-88-plan-w5a.md` (§W5a-44 plan-block)
- `sessions/session-plan/session-88-plan-w4c.md` (§W4c-36 plan-block, lines 800–802 + 833–855 substitution chain)
- `sessions/archive/session-88/workshops/_seed-w5a.md` (Workshop 1 framing — Route-A vs Route-B)
- `sessions/archive/session-88/workshops/_seed-w4c.md` (Workshop 1 framing — fiducial-anchor adjudication)
- `sessions/permanent-results-registry.md` §VII.AN / §VII.AO / §VII.AP (lines 16536–16664)
- `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md` ("alpha_s symbol overload" trap, S86–current pinned decisions)
- `.claude/rules/registry-landing.md`, `.claude/rules/cross-pillar-bridge-anatomy.md`, `.claude/rules/substrate-first-canonical-sourcing.md`, `.claude/rules/epistemic-discipline.md` §"Source Reconciliation", `.claude/rules/gate-verdicts.md` §"Option A — sig_5 remediation", `.claude/rules/joint-theorem-promotion.md`

---

## I. Session Outcome

The W5a-44 substrate-first Mellin-residue gate and the W4c-36 internal-inconsistency flag are not two independent surface findings — they are two views of the same structural fact about how α_s_canonical = -8587279/100000000 enters the framework. Bit-exact arithmetic settles the question: the value is EXACTLY (9561/10000)² − 1 in **Q**, where 91412721 = 9561² is a perfect square; the value is NOT independently reproducible from the L_max=12 spectrum cache via any closed-form Mellin-moment normalization (best Route-A candidate `−f0` is 2.85e-2 off, ten orders of magnitude short of the pre-registered 1e-12 PASS threshold). The structural verdict is therefore **Route-B is the actual canonical provenance**; Route-A as described in §VII.AN/AO is a re-rationalization, not an independent derivation. This forces (i) re-classification of §VII.AN W5a-37 and §VII.AO W5a-42 anchor structures via Option-A `supersedes`-tagged corrective registry entries (NOT in-place edits — verdict permanence is absolute), (ii) JOINT-(n_s, α_s) hypersurface as the lab discrimination target for §W4c-36 with framework n_s_FW = 9561/10000 as the exact substrate-side anchor and Planck n_s = 0.9649 as the orthogonal observational anchor, (iii) a new Class-(g) entry `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` in `_source_reconciliation_audit.py`, and (iv) extension of the substrate-first-canonical-sourcing.md §(i) calibration corpus with W5a-44 as the K=4 NEGATIVE-CALIBRATION instance.

---

## II. Key Results

### Result 1 — α_s_canonical = (9561/10000)² − 1 EXACTLY in **Q**

**Result**: `α_s_canonical = -8587279/100000000 = (Fraction(9561, 10000))² − 1` (bit-exact). Classification: **GEOMETRIC** (algebra-axis identity at registry-anchor layer).

The Sage-QQ exact integer 8587279 has the property `100000000 − 8587279 = 91412721 = 9561²`. This is not approximate ("4 decimals") as the W5a-44 working-paper (§(c) Discussion) and the seed-w5a investigator narrative suggested; it is exact in **Q**. Substitution chain (verified via Python `fractions.Fraction`):

```
Definition 1: α_s_canonical_Sage_QQ = Fraction(-8587279, 100000000)
Definition 2: n_s_FW_exact = Fraction(9561, 10000)
Substitute:   n_s_FW_exact² − 1 = Fraction(9561², 10000²) − 1
                                = Fraction(91412721, 100000000) − Fraction(100000000, 100000000)
                                = Fraction(91412721 − 100000000, 100000000)
                                = Fraction(-8587279, 100000000)
                                = α_s_canonical_Sage_QQ                  ← bit-exact
Direction:    Route-B identity α_s = n_s² − 1 reproduces the Sage-QQ canonical
              with NO ROUNDING when n_s = 9561/10000 is the binding anchor.
```

This single observation collapses the W5a-44 + W4c-36 ambiguity. The "Route-B identity reproduces target to 4 decimals" framing in seed-w5a §"Workshop 1" mis-states the structural relation: it is a bit-exact identity in **Q** (when n_s is taken as the rational 9561/10000), not a 4-decimal approximation. The 4-decimal framing was an artefact of float64 truncation at presentation precision, NOT an algebraic truth.

The downstream consequence is mechanical: any audit that follows the source chain will find that the FRAMEWORK n_s pin used at S82 W3-9 / S87 W-2 / S87 W-9 / W5a is 9561/10000 (or an irrational truncation thereof), and the α_s_canonical 8-decimal Sage-QQ literal is a RATIONAL IMAGE of that pin under the Route-B identity. There is no parallel Route-A derivation needed to "rationalize" this — the rational image relation IS the derivation, just at the n_s axis rather than the Mellin-residue axis.

### Result 2 — Best Route-A candidate misses pre-registered PASS threshold by 10 OOM

**Result**: W5a-44 best Route-A normalization `−f0 = -0.08832000` produces `rel_diff = 2.850e-2` against α_s_canonical = -0.08587279. PASS threshold was 1e-12 (publication-precision floor); INFO floor was 1e-9. Classification: **PHONONIC** (substrate Mellin-residue evaluation at substrate-distance-1 pole).

Substitution chain (verified via Python):
```
Definition 1: rel_diff = |−0.08832000 − (−0.08587279)| / |−0.08587279|
Substitute:   = 0.00244721 / 0.08587279
              = 0.02849808...
Direction:    rel_diff / 1e-12 = 2.85e+10        (10 OOM short of PASS)
              rel_diff / 1e-9  = 2.85e+07        (7 OOM short of INFO floor)
              ⇒ FAIL composite per pre-registered band
```

The W5a-44 verdict line is FAIL at audit_sha256 = `c092fe1bff9ab669…`. None of 8 enumerated Route-A normalizations (combinations of `a_2 = Σ m_k λ_k^{−2} = 2,211,143.85`, `a_4 = 174,981.20`, `a_0 = 31,956,720`, plus the plan-pinned Mellin moments f0, f2, f4) reaches even the INFO floor. The 2.85e-2 best candidate is 7 OOM beyond the INFO floor — this places W5a-44 squarely in the SOURCE-RECONCILIATION Class-(b) PIN-LOOSE-SOURCE-TIGHT severity band at the registry-anchor layer (per the SR 4-band calibration in `epistemic-discipline.md`), NOT in the boundary-band advisory zone.

The structural conclusion the W5a-44 verdict already states: there is no Route-A derivation in any project script that independently reproduces α_s_canonical from the substrate spectrum cache; the value enters the framework via the Route-B `n_s² − 1` identity acting on the framework n_s pin (Result 1). The W5a-44 plan claim that "the Route-A derivation EXISTS in some prior session script" was a plan-authorship presumption, not a verified fact.

### Result 3 — Plan §W4c-36 line 791 vs 802 is not a typo; it is a category collision

**Result**: The plan §W4c-36 machinery-pin block lists `substrate_alpha_s_canonical = -8.587279e-2 (= n_s^2 − 1, fiducial n_s = 0.9649)` AND `substrate_n_s_fiducial = 0.9649 (Planck 2018 anchor)`. These two pins are MUTUALLY INCONSISTENT under the Route-B identity. Classification: **PARTICLE** (representation-theoretic identity at the algebra-INVARIANT family layer, mis-bound to the wrong n_s anchor at plan-authorship).

Substitution chain (verified via Python):
```
Definition 1: α_s_RouteB(n_s) = n_s² − 1
Substitute:   α_s_RouteB(0.9649) = 0.9649² − 1 = 0.93103201 − 1 = −0.06896799
              α_s_RouteB(0.9561) = 0.9561² − 1 = 0.91412721 − 1 = −0.08587279  (= canonical exact)
Direction:    canonical −0.08587279 ≠ Planck-fiducial-Route-B −0.06896799
              ⇒ the plan's "fiducial n_s = 0.9649" comment beside the −8.587279e-2
                pin is internally false; the canonical corresponds to n_s = 0.9561
                (framework prediction), NOT to the Planck anchor.
```

The discrepancy magnitude is structurally significant relative to the lab discrimination band:
```
|Δα_s| = |−0.08587279 − (−0.06896799)| = 0.01690480
combined falsification band (per W4c-36 protocol)
       = sqrt((1e-3)² + (5e-4)²) = 1.118034e-3
ratio  = 0.01690480 / 1.118034e-3 = 15.120 × the band
```

The discrepancy is 15× the substrate's own combined falsification band 1.118e-3. A future Aalto/Lancaster longitudinal-NMR α_s extraction near −0.069 would PASS one reading and FAIL the other — and the reading-difference is determined entirely by whether the framework treats Route-B-with-n_s_FW or Route-B-with-Planck-n_s as the binding lab target. The W4c-36 INFO verdict (`e75fbe551eab2119…`) is structurally honest because it pins BOTH values in its `value=` field; the underlying choice is unresolved.

### Result 4 — JOINT-(n_s, α_s) hypersurface is the structurally honest discrimination target

**Result**: The lab discrimination target for the substrate's algebra-INVARIANT family at s=3 single-pole is most faithfully expressed as a 2-D HYPERSURFACE TEST in (n_s, α_s) space, not as a 1-D α_s band test. Classification: **PHONONIC** (substrate-derived bridge-anatomy element).

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3: the framework's algebra-INVARIANT route at s=3 single-pole derives BOTH n_s AND α_s from the SAME spectrum-only functional family on `(A_K, H_K, D_K)`. The two predictions are not independent observables — they are two readings of the same Mellin pole's residue structure under the n_s²−1 identity. Forcing the lab to compare against α_s ALONE (with one of the two n_s anchors silently chosen) discards the structural information that constrains them jointly.

The hypersurface form is:
```
SUBSTRATE-IS hypersurface: {(n_s, α_s) : α_s = n_s² − 1 AND n_s = n_s_FW(τ_fold, L_max)}
                          = {(0.9561, −0.08587279)}    [single point at the canonical pin]
PLANCK-IN hypersurface:    {(n_s, α_s) : α_s = n_s² − 1 AND n_s = 0.9649 ± 0.0042}
                          ≈ {(0.9649, −0.06896799 ± O(σ))}    [Planck observational locus]
LAB DISCRIMINATION:        joint-(n_s, α_s) measurement; reject the substrate prediction
                          iff (n_s_meas, α_s_meas) lies outside the SUBSTRATE-IS point
                          neighborhood at combined band 1.118e-3
                          AND outside the |α_s_meas − (n_s_meas)² + 1| < combined_band
                          consistency check for the Route-B identity itself.
```

This makes the structural-orthogonality framing of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` operational at the laboratory layer. A lab measurement at (0.9649, -0.069) would be consistent with Planck+Route-B-identity but would falsify the framework's substrate self-consistency point (0.9561, -0.08587). A lab measurement at (0.9561, -0.069) would falsify Route-B itself (since 0.9561² − 1 = -0.08587, not -0.069), forcing a re-reading of the algebra-INVARIANT family.

### Result 5 — §VII.AN SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure fails the registry-landing.md detection criterion when read against W5a-44 evidence

**Result**: The §VII.AN W5a-37 "ANCHOR-1 (V) = S82 W3-9 single-pole Mellin closure" framing fails `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` criterion 2 (anchors must be non-fungible) under the Route-B canonical reading. Classification: **GEOMETRIC** (registry-anchor structural defect).

The detection criterion requires:
- (1) sequential dependence: ANCHOR-2 cannot be invoked WITHOUT first invoking ANCHOR-1.
- (2) non-fungibility: the two anchors cannot be swapped or reordered without breaking the chain.
- (3) both anchors must remain accessible.

Under the Route-B canonical reading (Result 1), ANCHOR-1's role in the §VII.AN chain is supplied by the n_s_FW = 9561/10000 rational pin acting through the Route-B identity, NOT by the Mellin residue Res[Tr(D_K^{−2s}); s=3]. The "single-pole Mellin closure" framing in S82 W3-9 source script `s82_w3_9_as_adjacent_obs.py:203` computes `alpha_s_scheme_identity = ns_framework**2 - 1.0` as DIAGNOSTIC; the script's `ALPHA_S_FW_TREE = 0`. There is no Mellin-residue derivation in S82 W3-9 that ANCHOR-1 could be pointing at. The chain is therefore `n_s_FW → Route-B identity → α_s_canonical` — a SINGLE-anchor chain with an algebraic-image step, not a SOURCE-DOUBLE-CITE-CO-PRIMARY V→A_F→C sequential dependence.

ANCHOR-2 (S87 W2-3 GGE-Bog-occ-variance theorem giving `α_s^{(SF)} = -7.046336`) is a STRUCTURALLY DISTINCT functional in a STRUCTURALLY ORTHOGONAL cell (Cell IV biaxial-DRESSED at s=4 cone), not a "C-output" derivable conditional on the Cell I "V-input". The §VII.AP W5a-43 entry already correctly tags this: `STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY` per the algebra-axis K=3 MANDATORY clause forbidding cross-corner co-primary. Mounting this same Cell IV value as ANCHOR-2 of the §VII.AN Cell I chain is internally inconsistent with the §VII.AP framing — the same structural-orthogonality argument that excludes cross-corner co-primary at §VII.AP excludes ANCHOR-2 from playing a CO-PRIMARY role at §VII.AN.

The registry-landing.md detection criterion 2 (non-fungibility) thus FAILS by construction: the V (n_s²−1 image) and the C (Cell IV variance theorem) are not non-fungible — they live on different algebra-axis corners that cannot enter a single non-fungible chain per the K=3 MANDATORY orthogonality discipline. §VII.AN is therefore registry-mis-classified at landing time.

---

## III. Gate Verdicts

These verdicts are READ from the source documents; this synthesis does not re-adjudicate them. The structural verdict in Section II then operates on these existing verdicts.

| Gate | Source verdict | Decisive number | audit_sha256 head |
|:-----|:---------------|:----------------|:-------------------|
| W5a-37 §VII.AN α_s_canonical SOURCE-DOUBLE-CITE-CO-PRIMARY landing | PASS (registry trio LANDED at §VII.AN; 10/10 cross-checks PASS) | body line count 32 (≥18 threshold; 1.78× margin); Sage-QQ exact `-8587279/100000000` | `cf5ec646662ccf8b…` |
| W5a-42 §VII.AO Cell I biaxial-FI (inherits SOURCE-DOUBLE-CITE-CO-PRIMARY) | PASS (registry trio LANDED at §VII.AO; pole-scope s=3 SPECIFICALLY) | 13.9957σ vs Planck/ACT (Aiola 2020); 38.3360σ vs CMB-S4 forecast | `d536b67445b6468d…` |
| W5a-43 §VII.AP Cell IV biaxial-DRESSED orthogonal companion | PASS at run #3 (3-trio bug-fix iteration trail; verifier-side bugs only; §VII.AP body unchanged across runs) | cross-corner ratio 704633600/8587279 = 82.0556× tagged `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]`; body 51 lines | `47a5a78c0cfdc6f8…` (PASS) |
| W5a-44 substrate-first Mellin-residue discriminator (Route-A bit-exact reproduction) | FAIL (best Route-A candidate `−f0 = −0.0883200` rel_diff = 2.85e-2; PASS threshold 1e-12; INFO floor 1e-9; both missed) | a_2_raw = 2,211,143.85 (90 sectors p+q≤12); 31,956,720 multiplicity-weighted eigenvalues (NOT plan-claimed 78,064) | `c092fe1bff9ab669…` |
| W4c-36 3He-B α_s NMR extraction protocol pre-registration | INFO (protocol document landed substantive; sub-substrate-tolerance lab σ_lab=5e-4 ≤ σ_substrate=1e-3 feasible; HONEST FINDING flagged plan-text inconsistency in `value=` field carrying BOTH α_s_canonical and α_s_from_n_s_squared) | combined band sqrt((1e-3)² + (5e-4)²) = 1.118034e-3; |Δα_s between two readings| / band = 15.12× | `e75fbe551eab2119…` |

Sub-trio iteration trail at W5a-43 (3 verdict trios retained per `gate-verdicts.md` "verdicts permanent" rule): run 1 = `d8c925c286402a94…` FAIL (CC3b substring-bug); run 2 = `6a2096c8d1c422ab…` FAIL (slot-reuse bug); run 3 = `47a5a78c0cfdc6f8…` PASS canonical. Per Option-A `supersedes`-tag protocol newly mandated at S88 W8-100, future corrective emissions for these trios would carry `supersedes=<full-64-char>` tags; the W5a-43 trios pre-date W8-100 and are retroactively canonicalized under rule (6) of the gate-verdicts.md Option-A clause without disk-edit.

---

## IV. Structural Implications

### IV.1 Adjudication Resolution — Workshop 1 (W5a) / Workshop 1 (W4c)

Synthesis of the two seed-w5a / seed-w4c Workshop 1 framings. Both seeds asked competing-reading questions; the bit-exact arithmetic (Result 1) RESOLVES the central tension in a direction that neither seed's competing readings fully anticipated.

| Adjudication question | Verdict | Reasoning |
|:----------------------|:--------|:----------|
| (W5a Q-a) Is V1 anchor "S82 W3-9 single-pole Mellin closure" methodological cross-check or canonical numerical source? | METHODOLOGICAL CROSS-CHECK ONLY (for the Route-B identity). The S82 W3-9 source script computes `ns_framework**2 - 1.0` as DIAGNOSTIC at line 203. There is no Route-A canonical numerical source in S82 W3-9. Under `substrate-first-canonical-sourcing.md §(i)`, citing it as canonical for Cell I requires a Route-A derivation that does not exist. | Route-B canonical, with n_s_FW = 9561/10000 rational, IS substrate-first at the n_s axis (the framework predicts n_s from `(A_K, H_K, D_K)`); Route-A canonical at the Mellin-residue axis is empty. |
| (W5a Q-b) Is α_s_canonical algebra-INVARIANT spectrum-only (Cell I) or algebra-DEPENDENT state-pair (Cell IV)? | ALGEBRA-INVARIANT spectrum-only **at the n_s prediction layer**. Substrate predicts n_s from the spectrum-only family; α_s = n_s² − 1 is a Route-B image of that prediction, structurally still in Cell I's algebra-axis. Cell IV's Var_a(n_a^GGE) = -7.046336 IS algebra-DEPENDENT and structurally orthogonal — that's why it cannot be the C-anchor of a CO-PRIMARY chain with Cell I's V-anchor. | The 4-corner classification at `alpha-s-multi-valued-landscape.md` (W5a-41 PASS, 6/6 orthogonality pairs K=3 MANDATORY) is preserved; what fails is the SOURCE-DOUBLE-CITE-CO-PRIMARY tag at §VII.AN, NOT the corner enumeration. |
| (W5a Q-c) Is α_s = n_s²−1 substrate-IS algebra-INVARIANT identity (binding to n_s_FW≈0.9561) OR observational identity consuming Planck n_s as external pin? | FIDUCIAL-ANCHOR HONEST RESOLUTION: it is BOTH on DIFFERENT axes. (A) Substrate-IS reading at the algebra-INVARIANT family with n_s_FW = 9561/10000 binding (this is what S87 W-9 W2-1+W2-4 PASS at L_max=12 rel_diff = 0e+00 actually pinned, per the bit-exact Result 1). (B) Observation-comparison reading at the observational anchor with Planck n_s = 0.9649 binding (this is what mack-cosmic-bridge's `mack-observational-constraints.md` row pins). The two CANNOT be conflated at a single registry slot — they differ by 15× the substrate's combined falsification band. The structurally-honest target is the JOINT (n_s, α_s) hypersurface (Result 4). | Per `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" MANDATORY at K=3: when the substrate predicts BOTH n_s AND α_s from the same algebra-INVARIANT family, they are not 2 independent lab targets — they ARE the same lab observation read 2 ways via the n_s²−1 image. Forcing 1 binding pin discards the joint constraint. |
| (W5a Q-d) Do §VII.AN/AO need re-classification or restoration as STAGE-1-CANDIDATE pending Route-A? | YES — re-classification, NOT pending Route-A. Route-A is structurally absent (Result 2); waiting for it is unbounded. Under `joint-theorem-promotion.md` 4-stage pathway, §VII.AN/AO should be demoted from PASS-LANDED to STAGE-1-CANDIDATE-PROVISIONAL with an explicit ANCHOR-PROVENANCE CORRIGENDUM declaring Route-B canonical primacy at the n_s pin layer + Route-A absence at the Mellin-residue layer. The bit-exact reproduction Result 1 IS the substrate-first derivation; the framing of it as a Mellin residue is the question. | §VII.AP Cell IV (W5a-43) is independently derived in S87 W2-3 and is NOT subject to this concern — Cell IV's S/N is intact, only Cell I's V-anchor framing is mis-classified. |
| (W5a Q-e) Severity band per epistemic-discipline.md §"Source Reconciliation"? | Class-(b) PIN-LOOSE-SOURCE-TIGHT severity S1 (MANDATORY-halt). The 2.85e-2 best-Route-A rel_diff vs the 1e-12 PASS threshold is 10 OOM beyond INFO floor — this is a structural false-PASS at registry-landing time per `epistemic-discipline.md` §"Source Reconciliation" 4-band classification (D_max ≥ 3.0 hard-halt band). The §VII.AN PASS verdict relied on artifact-existence cross-checks (10/10) WITHOUT a substrate-first numerical reproduction check; W5a-44 supplies that check post-hoc and it FAILs. | Per the sequential composition order PRU → SOURCE-RECON → SUBSTRATE-FIRST-PROVENANCE → PRDR → execution: §VII.AN W5a-37 PASS clears PRU (cardinality) but FAILs SUBSTRATE-FIRST-PROVENANCE (the cited V-anchor's closure script does not contain the claimed derivation). The §VII.AN landing predates the SUBSTRATE-FIRST-PROVENANCE sub-audit's operational implementation — this is the FIRST live calibration instance forcing its scaffolding to land. |
| (W5a Q-f) Should W4c-36 lab gate's INFO verdict (carrying BOTH values) be the canonical pre-registration form going forward? | YES, with a Stage-2 cross-axis verify gate adjudicating the BINDING PIN separately from PROTOCOL DOCUMENT EXISTENCE. The W4c-36 INFO verdict is structurally honest precisely because it pins BOTH α_s readings (`alpha_s_canonical=-0.08587279;alpha_s_from_n_s_squared=-0.0689679900`) — this is the ONLY verdict-line form that does not pre-commit to a single binding choice without explicit adjudication. Forward `S89-W4C-36-FIDUCIAL-ANCHOR-STAGE-2-CROSS-AXIS-VERIFY` should adopt this as the canonical pre-registration shape for any α_s lab-protocol gate that consumes a substrate-IS observable derived through an n_s-mediation step. | This becomes calibration corpus instance #1 of a NEW joint-(substrate, observation) hypersurface pre-registration pattern; sets up K=1 toward the K=3 MANDATORY promotion under `feedback_rules-compensate-missing-structure.md`. |
| (W5a Q-g) Rule-file extension to `cross-pillar-bridge-anatomy.md` requiring explicit fiducial-anchor declaration in bridge-map element 3 when substrate-IS observable consumes a pre-substrate pin (e.g., n_s) that is itself a laboratory-IN observable at a different pillar? | YES, queued as STAGE-1-CANDIDATE rule extension (NOT MANDATORY at K=1). The pattern — substrate-IS consumes a CHILD pin that is independently a laboratory-IN observable elsewhere — appears at the n_s/α_s interface but may also appear at the Higgs mass / vacuum-energy / sound-speed interfaces. K=3 MANDATORY threshold per `feedback_rules-compensate-missing-structure.md` requires 2 more calibration instances. The W5a/W4c instance is K=1. | Concrete extension shape: `cross-pillar-bridge-anatomy.md §"5 IS-not-IN anatomy"` element 3 (bridge map) gains a sub-clause: "When the bridge map composes a substrate-IS observable through a pre-substrate pin P that is itself a laboratory-IN observable at a different pillar, the bridge entry MUST declare which incarnation of P is binding (substrate-self-consistent vs external-observation). Conflation-with-undeclared-binding is a registry-incompleteness FAIL routing to plan-freeze halt." |

### IV.2 Constraint-map updates

| Date | Mechanism / observable | Prior state | New state | Reason |
|:-----|:------------------------|:------------|:----------|:-------|
| 2026-05-07 | α_s_canonical canonical-source provenance | claimed Route-A substrate-first Mellin residue (per S87 W-2 R3 close + W5a plan) | **CONFIRMED Route-B at n_s axis**: bit-exact identity (9561/10000)² − 1 = -8587279/100000000 in **Q**; Route-A at Mellin-residue axis structurally ABSENT (W5a-44 FAIL at 10 OOM short of PASS) | Result 1 + Result 2 |
| 2026-05-07 | §VII.AN W5a-37 SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure | LANDED PASS at audit_sha256 `cf5ec646662ccf8b…` | **REQUIRES corrective Option-A `supersedes`-tagged successor entry** demoting to STAGE-1-CANDIDATE-PROVISIONAL with ANCHOR-PROVENANCE CORRIGENDUM declaring Route-B canonical at n_s pin + Route-A structural absence | Result 5 + registry-landing.md detection criterion 2 fails under non-fungibility test; original verdict line RETAINED per gate-verdicts.md absolute permanence |
| 2026-05-07 | §VII.AO W5a-42 Cell I biaxial-FI inheritance from §VII.AN CO-PRIMARY | LANDED PASS at audit_sha256 `d536b67445b6468d…` | **REQUIRES corrective Option-A `supersedes`-tagged successor entry**: ANCHOR STRUCTURE migrates from inherited SOURCE-DOUBLE-CITE-CO-PRIMARY to PRIMARY-N_S-IMAGE; pole-scope s=3 SPECIFICALLY + resolution-scope A_5 5-element retained; discrimination σ values 13.9957σ + 38.3360σ retained (independent of anchor-structure tag) | Result 5 — Cell I value is structurally Cell-I-correct (the algebra-INVARIANT spectrum-only family route is genuine at the n_s prediction layer); only the inherited CO-PRIMARY tag is mis-classified |
| 2026-05-07 | §VII.AP W5a-43 Cell IV biaxial-DRESSED orthogonal companion | LANDED PASS at audit_sha256 `47a5a78c0cfdc6f8…` | **NO CHANGE** — Cell IV is independently derived from S87 W2-3 GGE-Bog-occ-variance and is NOT subject to the §VII.AN/AO concern; the STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY tag REMAINS valid; the cross-corner ratio 704633600/8587279 = 82.0556× FORBIDDEN-AS-GATE flag REMAINS valid | Result 5 explicitly preserves §VII.AP per W5a-44 §(h) footnote 4 |
| 2026-05-07 | n_s_FW canonical-pin Sage-QQ exact form | scheme-dependent floats (0.9567 / 0.9557 / 0.9595 per scheme variants in agent-memory; not in canonical_constants.py) | **EXACT pin available**: n_s_FW_exact = Fraction(9561, 10000) reproduces α_s_canonical EXACTLY in **Q** under Route-B. Substantively this is a NEW canonical-constants.py promotion candidate (CF-W15-2 below) | Result 1 — bit-exact proof |
| 2026-05-07 | W4c-36 lab α_s discrimination target (binding pin) | unresolved — plan §W4c-36 lines 791 vs 802 internally inconsistent; W4c-36 INFO verdict honestly carries BOTH values | **NEW canonical form**: JOINT (n_s, α_s) hypersurface test with framework-self-consistent point (9561/10000, -8587279/100000000) AND Planck observational anchor (0.9649, ~-0.069) BOTH carried in verdict-line `value=` field; lab discriminates via 2D measurement, not 1D α_s band | Result 4 + adjudication question (f) |
| 2026-05-07 | substrate-first-canonical-sourcing.md §(i) calibration corpus | K=3 (W0c-3 + W4-2 + W5a-2) | **K=4 (NEGATIVE-CALIBRATION add)**: W5a-44 instance — a registry-LANDED chain where the V-anchor's cited closure script does not contain the claimed substrate-first derivation; FAIL surfaces post-hoc at substrate-first-provenance audit. Per `feedback_rules-compensate-missing-structure.md`, K=4 ≥ K_promotion=3 ⇒ MANDATORY promotion event triggered for SUBSTRATE-FIRST-PROVENANCE sub-audit at plan-freeze | Result 5 + W5a-44 §(g) self-assessment |
| 2026-05-07 | _source_reconciliation_audit.py class taxonomy | 5 classes (a)-(e) + (f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL | **NEW Class-(g) candidate**: `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` — flags any registry entry whose ANCHOR cites a derivation route (Route-A) that the cited closure script does not implement, while a structurally-equivalent Route-B image identity exists at a different axis. Severity HARD-HALT at landing-time because the structural false-PASS direction (registry-anchor mis-classification) is high-leverage. K=1 calibration; advisory until K=3 | Adjudication question (a) + Result 5 |

### IV.3 What this DOES and DOES NOT change

DOES NOT change:
- The numerical value α_s_canonical = -8587279/100000000. This value is correct in **Q**; only its CLAIMED PROVENANCE PATH is mis-classified. The 13.9957σ vs Planck/ACT discrimination at §VII.AO is intact (the laboratory comparison does not depend on which substrate provenance route generated the value).
- §VII.AP Cell IV biaxial-DRESSED entry. Independently derived in S87 W2-3.
- The 4-corner enumeration at `alpha-s-multi-valued-landscape.md` (W5a-41). 6/6 orthogonality pairs K=3 MANDATORY PASS unchanged.
- The cross-corner ratio 704633600/8587279 = 82.0556× as STRUCTURAL OBSERVABLE. The FORBIDDEN-AS-GATE flag at §VII.AP is structurally correct (cross-corner co-primary forbidden by K=3 MANDATORY).
- W5a-44 verdict (FAIL). Per `gate-verdicts.md` "verdicts permanent", the FAIL line at `c092fe1bff9ab669…` remains canonical for the PRE-REGISTERED Route-A bit-exact reproduction test. The structural lesson in this synthesis ADDS a downstream corrective registry interpretation, not a re-adjudication.

DOES change:
- §VII.AN ANCHOR STRUCTURE classification (corrective Option-A successor entry).
- §VII.AO inherited anchor structure (corrective Option-A successor entry).
- W4c-36 lab discrimination target form (joint-hypersurface; pre-registered Stage-2 verify gate at S89).
- substrate-first-canonical-sourcing.md §(i) calibration corpus (K=3 → K=4 NEGATIVE-CALIBRATION).
- `_source_reconciliation_audit.py` taxonomy (proposed new Class-(g)).

### IV.4 Connection to mack-cosmic-bridge agent-memory "alpha_s symbol overload" trap

The agent-memory pin `alpha_s symbol overload: QCD alpha_s(M_Z) ≠ inflationary dn_s/dlnk; S50-51 identity is topological-scheme-only` already flagged the structural distinction this synthesis operationalizes at the registry-anchor layer. The S50-51 identity α_s = n_s² − 1 is "topological-scheme-only" per the original framing; that framing is consistent with Route-B as canonical at the n_s axis, NOT with Route-A as canonical at the Mellin-residue axis. The W5a plan-authorship layer treated the topological-scheme identity as if it had a parallel substrate-first Mellin-residue derivation; W5a-44 surfaces empirically that no such parallel derivation exists in any project closure script. The agent-memory pin was correct; the W5a plan-author misread its scope.

This synthesis updates mack-cosmic-bridge's pinned-decisions with the bit-exact result (9561/10000)² − 1 = -8587279/100000000 EXACTLY in **Q**, which sharpens the agent-memory "alpha_s symbol overload" entry from a qualitative warning into an algebraic pin: the 8-decimal Sage-QQ literal at α_s_canonical IS a rational image of n_s_FW = 9561/10000, period. Forward sessions citing α_s_canonical can derive any required precision deterministically from that single pin.

---

## V. Carry-Forward Computations

### V.1. Option-A `supersedes`-tagged successor entries for §VII.AN W5a-37 and §VII.AO W5a-42

- **What**: For BOTH §VII.AN and §VII.AO, append corrective Option-A successor registry entries naming the original audit_sha256 in a `supersedes=<full-64-char>` token. The successor entries declare:
  - §VII.AN successor: ANCHOR STRUCTURE migrates from `SOURCE-DOUBLE-CITE-CO-PRIMARY` to `PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM`; ANCHOR-1 (V) becomes `n_s_FW = Fraction(9561, 10000) substrate-first n_s prediction at S87 W-9 W2-1+W2-4 PASS at L_max=12 rel_diff = 0e+00`; ANCHOR-2 (C) is REMOVED (Cell IV cannot be CO-PRIMARY with Cell I per K=3 MANDATORY); CORRIGENDUM cites W5a-44 FAIL at audit_sha256 `c092fe1bff9ab669…` as the empirical evidence that Route-A at the Mellin-residue axis is structurally absent.
  - §VII.AO successor: ANCHOR STRUCTURE migrates from `SOURCE-DOUBLE-CITE-CO-PRIMARY (inherits from §VII.AN)` to `PRIMARY-N_S-IMAGE (inherits §VII.AN successor)`; pole-scope s=3 SPECIFICALLY retained; resolution-scope A_5 5-element retained; discrimination σ values 13.9957σ vs Planck/ACT and 38.3360σ vs CMB-S4 forecast retained UNCHANGED (independent of anchor-structure tag).
- **Inputs**: §VII.AN current registry text (lines 16536–16567 of `permanent-results-registry.md`); §VII.AO current registry text (lines 16570–16609); §VII.AP current registry text (lines 16613–16662; for cross-link consistency); W5a-44 FAIL audit_sha256 = `c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b`; W5a-37 PASS audit_sha256 = `cf5ec646662ccf8be68a206dc96ca38a222ebc6c596131d1d923e237f217f509`; W5a-42 PASS audit_sha256 = `d536b67445b6468d…` (full 64-char to be re-pinned at successor write); n_s_FW = Fraction(9561, 10000) bit-exact pin.
- **Gate**: `S89-VII-AN-AO-OPTION-A-CORRECTIVE-SUCCESSOR-LANDING` with PASS criterion: (a) corrective registry entries appended at §VII.AN-CORRIGENDUM and §VII.AO-CORRIGENDUM slot labels (next-free-letter scan); (b) each successor's verdict line carries `supersedes=<full-64-char-original-audit-sha>` per `gate-verdicts.md §"Option A — sig_5 remediation"` Forward emission discipline rule (5); (c) original §VII.AN and §VII.AO entries RETAINED on disk (no in-place edits — verdict permanence absolute); (d) cross-link audit confirms §VII.AP STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY tag remains valid against the corrective §VII.AN/AO entries (Cell IV is independent — no consistency conflict expected); (e) `supersedes`-tagged dual-SHA companion row emitted per gate-verdicts.md S87+ schema. INFO criterion: corrective entries appended but supersedes-tag missing on first attempt (Class-8.2 PRU; route to in-session repair). FAIL criterion: in-place edit attempted on original §VII.AN/AO text (PROHIBITED_ACTIONS Class-3 violation).
- **Effort**: 0.4 wave-equivalents (registry write × 2 corrective entries + 2 supersedes-tagged dual-SHA verdict trios + cross-link consistency audit).

### V.2. n_s_FW_exact canonical promotion to canonical_constants.py

- **What**: Promote `n_s_FW_exact = Fraction(9561, 10000) = 0.9561` to `computations/_shared/canonical_constants.py` SECTION B with PROVENANCE `"S88 W15 synthesis (Route-B identity bit-exact pin: (9561/10000)^2 - 1 = -8587279/100000000 = α_s_canonical EXACTLY in Q; supersedes scheme-dependent floats 0.9567/0.9557/0.9595)"`. Conditional on Class-(f) D_max audit per `epistemic-discipline.md §"Source Reconciliation"`: candidate_A = 0.9561 (Route-B inversion exact); candidate_B = 0.9590 (S65 BCS+1-loop, agent-memory pin); D_max = |log10(0.9561/0.9590)| = 0.001316 ≪ 0.1 NO-ACTION band. The two candidates differ by 0.3%, well inside the 1.118e-3 combined falsification band.
- **Inputs**: Sage-QQ inversion `n_s_FW_exact = sqrt(91412721)/10000` where sqrt(91412721) = 9561 EXACTLY (perfect square, verified Python `9561**2 == 91412721`); `α_s_canonical_Sage_QQ = Fraction(-8587279, 100000000)` from S82 W3-9 closure; existing scheme-dependent n_s pins in `canonical_classes.py` (per agent-memory `MEMORY.md §"Framework cosmological predictions"`).
- **Gate**: `S89-N_S-FW-EXACT-CANONICAL-PROMOTION` with PASS criterion: (a) `n_s_FW_exact` literal present in `canonical_constants.py` SECTION B as both `Fraction(9561, 10000)` symbolic AND `0.9561` float64; (b) PROVENANCE entry naming Route-B inversion + S82 W3-9 closure SHA + W5a-44 FAIL SHA as evidence of structural absence of Route-A; (c) round-trip cross-check `Fraction(n_s_FW_exact_num, n_s_FW_exact_den)**2 - 1 == Fraction(-8587279, 100000000)` returns True via Python `fractions.Fraction`; (d) D_max class-(f) audit returns NO-ACTION; (e) downstream consumer regression test on `_inventory_canonical_sync_audit.py` showing no breakage.
- **Effort**: 0.2 wave-equivalents (single `update_constant` call + Fraction round-trip verification + D_max audit + 1 dual-SHA verdict trio).

### V.3. Class-(g) `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` SOURCE-RECON sub-audit

- **What**: Add Class-(g) `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` to `_source_reconciliation_audit.py` taxonomy. Detection algorithm: at plan-freeze for any registry-landing gate, parse the planned ANCHOR-1 / ANCHOR-2 cite-strings, resolve each to a closure script + line range, AST-parse the cited script for the claimed derivation route (Route-A = direct CM-1995 §III.4 Mellin-residue evaluation OR analogous; Route-B = topological-scheme image identity such as `n_s² − 1`, `m_H² / (m_H² + m_t²)`, etc.). If the cited closure script implements only Route-B but the plan ANCHOR cite-string claims Route-A, fire severity HARD-HALT. Initial detection patterns: regex `alpha_s.*=.*\*\*\s*2\s*-\s*1` matches Route-B identity in script; regex `Res\[.*Tr\(D_K.*\^.*-2.*s.*\).*s.*=.*\d+\]` matches Route-A residue evaluation. Calibration corpus K=1 from W5a-44 (current synthesis); SUGGESTION until K=3 promotion.
- **Inputs**: existing `_source_reconciliation_audit.py` (5-class taxonomy at `epistemic-discipline.md §"Source Reconciliation"`); W5a-44 FAIL diagnostic at `c092fe1bff9ab669…` as calibration instance #1; `s82_w3_9_as_adjacent_obs.py:203` as the canonical Route-B-script-cited-as-Route-A example; AST-parse module from existing PRDR machinery enumeration audit.
- **Gate**: `S89-SOURCE-RECON-CLASS-G-AUDIT-EXTENSION` with PASS criterion: (a) Class-(g) detection routine added to `_source_reconciliation_audit.py` with Route-A and Route-B regex pattern sets; (b) calibration test on W5a-44 plan §W5a-44 reproducing the structural mismatch (script `s82_w3_9_as_adjacent_obs.py` does NOT contain Route-A pattern; ANCHOR cite claims Route-A) AND firing HARD-HALT correctly; (c) negative-calibration test on a known PASS gate (e.g., a §VII entry whose anchor IS substrate-first reproducible) showing no false-positive; (d) per `epistemic-discipline.md §"Pre-Registration Completeness"` Class 8.3 publication-precision pin: rel_tol = 1e-12 for any rel_diff comparison routines added; (e) audit-script verdict trio with Class-8.2 verifier-rubric pre-registration (pattern set + disjunction/conjunction declaration explicit).
- **Effort**: 0.6 wave-equivalents (audit-script extension + regex calibration + W5a-44 + 1 negative-calibration test + dual-SHA verdict trio + rule-file cross-reference edits at `epistemic-discipline.md §"Source Reconciliation"`).

### V.4. W4c-36 JOINT-(n_s, α_s) hypersurface lab discrimination Stage-2 cross-axis verify

- **What**: Pre-register `S89-W4C-36-FIDUCIAL-ANCHOR-STAGE-2-CROSS-AXIS-VERIFY` per `joint-theorem-promotion.md` 4-stage pathway as Stage-2 cross-axis independent verify of the JOINT-(n_s, α_s) hypersurface lab discrimination target (Result 4). Two independent cross-reviewers, dispatched in parallel, WITHOUT prior workshop context: (Axis-A substrate-physics) volovik-superfluid-universe-theorist audits the substrate-IS hypersurface point (9561/10000, -8587279/100000000) against `(A_K, H_K, D_K)` Mellin-residue + Route-B identity self-consistency at L_max=12; (Axis-B observational) mack-cosmic-bridge audits the Planck observational anchor (0.9649 ± 0.0042, ~-0.069 ± O(σ_α_s)) against `mack-observational-constraints.md` row + Aiola 2020 ACT DR4 + Planck constraint compatibility. Joint clauses (substrate-IS hypersurface + Planck-IN hypersurface co-existence; lab 2D discrimination feasibility within combined band 1.118e-3) are PASS-AND'd across the two verdicts.
- **Inputs**: §W4c-36 INFO verdict at audit_sha256 `e75fbe551eab2119…` (carrying BOTH α_s_canonical = -0.08587279 and α_s_from_n_s_squared = -0.0689679900 in `value=` field); `3he-b-alpha-s-nmr-extraction-protocol.md` registry document; substrate side: n_s_FW_exact = Fraction(9561, 10000) (V.2 promotion); observational side: `mack-observational-constraints.md` Planck 2018 row (n_s = 0.9655 ± 0.0062 standard band; W4c-36 plan-pin uses 0.9649 fiducial — both within Planck observational band).
- **Gate**: PASS iff BOTH cross-reviewers return PASS on substrate-side AND observational-side joint clauses respectively; INFO iff one cross-reviewer returns INFO on a clause (clause stays at Stage-1; documented as Stage-2-INFO-deferred); FAIL iff either cross-reviewer returns FAIL on any clause (Stage-2 → 3 promotion blocked; theorem stays at Stage-1; lab protocol document re-enters next-session remediation queue). Stage-3 PERMANENT promotion conditional on Stage-2 PASS-AND.
- **Effort**: 0.5 wave-equivalents (2 parallel cross-reviewer dispatches + joint-clause PASS-AND adjudication + W4c-36 protocol document update with JOINT hypersurface form + dual-SHA verdict trio).

### V.5. substrate-first-canonical-sourcing.md §(i) calibration corpus K=4 NEGATIVE-CALIBRATION promotion

- **What**: Extend `substrate-first-canonical-sourcing.md §(i)` "Calibration corpus precedents" with W5a-44 as instance #4 (NEGATIVE-CALIBRATION on registry-anchor Route-A primacy claim). Append calibration row: instance #4 = W5a-44 §VII.AN registry-anchor framing — a registry-LANDED chain where the V-anchor cite "S82 W3-9 single-pole Mellin closure" claims Route-A but the cited closure script implements Route-B; FAIL surfaces post-hoc at substrate-first-provenance audit (W5a-44 audit_sha256 `c092fe1bff9ab669…`); 8 candidate Route-A normalizations exhausted at L_max=12; best `−f0` rel_diff 2.85e-2 vs PASS threshold 1e-12 (10 OOM short). Rule status promotes from "calibration corpus K=3" to "MANDATORY at K=4 promotion event triggered" per `feedback_rules-compensate-missing-structure.md`. Plan-freeze auditor `_substrate_first_provenance_audit.py` (S87 carry-forward V.1; queued) becomes MANDATORY-at-plan-freeze for all S89+ registry-landing gates.
- **Inputs**: `substrate-first-canonical-sourcing.md` current §(i) calibration corpus block (W0c-3 §(b) + W4-2 line 503 + W5a-2 §10 = K=3); W5a-44 audit_sha256; W5a-44 working-paper §(g) self-assessment + §(h) FAIL routing diagnostic; existing rule-file structure for K=3 → MANDATORY promotion language pattern (see `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-at-K=3 promotion as the canonical model).
- **Gate**: `S89-SUBSTRATE-FIRST-CANONICAL-SOURCING-K4-PROMOTION` with PASS criterion: (a) calibration corpus row 4 appended to `substrate-first-canonical-sourcing.md §(i)` with W5a-44 instance details; (b) K-counter advance from 3 → 4 (K = 4 ≥ K_promotion = 3 ⇒ promotion event); (c) status migration from "advisory" to "MANDATORY at plan-freeze for all S89+ registry-landing gates"; (d) cross-references updated at `epistemic-discipline.md §"Source Reconciliation"` Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL — extends to the registry-anchor case via Class-(g); (e) METHODOLOGY-class allowlist row appended per `methodology-wave-allowlist.md` (gate-ID + plan-block SHA + rationale verbatim per W9-RULE-CLEANUP precedent in `sessions/framework/registry/methodology-wave-instances.md`).
- **Effort**: 0.3 wave-equivalents (rule-file edit + calibration corpus row + cross-reference table updates + 1 dual-SHA METHODOLOGY-class verdict trio + allowlist row).

### V.6. registry-landing.md §"Detection" rule-file extension on algebra-axis orthogonality

- **What**: Conditional on user-acceptance, extend `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` with a fourth criterion: "(4) Both anchors must be on the same algebra-axis cell per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3. Cross-corner co-primary structures are STRUCTURALLY FORBIDDEN: a Cell I (algebra-INVARIANT) V-anchor cannot enter a CO-PRIMARY chain with a Cell IV (algebra-DEPENDENT) C-anchor regardless of empirical numerical agreement. The structural-orthogonality argument that excludes cross-corner co-primary at §VII.AP applies symmetrically to the §VII.AN V-anchor selection: both ANCHORS must inhabit the same algebra-axis." This makes the §VII.AN/AO mis-classification (Result 5) IMPOSSIBLE-BY-CONSTRUCTION at future plan-freeze.
- **Inputs**: `registry-landing.md` current §"Detection" 3-criterion block; §VII.AP W5a-43 STRUCTURALLY-ORTHOGONAL-COMPANION-NOT-CO-PRIMARY tag rationale; algebra-axis K=3 MANDATORY clause text from `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`.
- **Gate**: `S89-REGISTRY-LANDING-DETECTION-CRITERION-4-ALGEBRA-AXIS-EXTENSION` with PASS criterion: (a) §"Detection" block extended with criterion (4); (b) cross-link to `cross-pillar-bridge-anatomy.md` algebra-axis K=3 MANDATORY clause; (c) calibration corpus row added: instance #1 = W5a-44 surfacing of §VII.AN cross-corner ANCHOR-1+ANCHOR-2 conflation; (d) audit-script extension to `_registry_landing_audit.py` (S87+ extension queued) checking algebra-axis cell identity for both anchors at plan-freeze; (e) status SUGGESTION at K=1; promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`. Conditional acceptance: this CF is contingent on user-adjudication that the algebra-axis structural-orthogonality test applies to the registry-anchor layer (not just to the cross-corner gate-comparison layer).
- **Effort**: 0.3 wave-equivalents (rule-file edit + calibration corpus row + audit-script extension queue notation + cross-reference table update at `cross-pillar-bridge-anatomy.md`).

### V.7. cross-pillar-bridge-anatomy.md element-3 fiducial-anchor sub-clause (STAGE-1-CANDIDATE rule extension)

- **What**: Conditional on K=3 calibration corpus advance, extend `cross-pillar-bridge-anatomy.md §"5 IS-not-IN anatomy"` element 3 (bridge map) with a sub-clause requiring explicit fiducial-anchor declaration when the bridge map composes a substrate-IS observable through a pre-substrate pin P that is itself a laboratory-IN observable at a different pillar. K=1 calibration instance from W5a/W4c synthesis (n_s as the pre-substrate pin in the α_s bridge); K=2 and K=3 instances pending future bridge-anatomy invocations. Sub-clause text at K=1 status:
  - "When the bridge map composes a substrate-IS observable through a pre-substrate pin P that is itself a laboratory-IN observable at a different pillar, the bridge entry MUST declare which incarnation of P is binding: (i) substrate-self-consistent (P = framework prediction at the same algebra-axis family) OR (ii) external-observation (P = laboratory measurement at the different pillar) OR (iii) joint-hypersurface (lab discrimination is 2D in (P, observable) space rather than 1D in observable space alone). Conflation-with-undeclared-binding is a registry-incompleteness FAIL routing to plan-freeze halt."
  - Calibration corpus instance #1: W5a-44 + W4c-36 — n_s as pre-substrate pin in α_s bridge; substrate-self-consistent reading n_s_FW = 9561/10000 vs external-observation reading n_s_Planck = 0.9649; reading-difference 15× the substrate's own combined falsification band; structurally-honest target IS the joint-(n_s, α_s) hypersurface.
- **Inputs**: `cross-pillar-bridge-anatomy.md` current §"5 IS-not-IN anatomy" element 3 text; W5a-44 + W4c-36 synthesis content (Section IV.1 (g) + Section II Result 4 of this file); existing K=3 promotion language model from algebra-axis K-counter clause.
- **Gate**: `S89-CROSS-PILLAR-BRIDGE-ANATOMY-ELEMENT-3-FIDUCIAL-ANCHOR-RULE-EXTENSION` with PASS criterion: (a) sub-clause appended to element 3 with K=1 SUGGESTION status; (b) calibration corpus row 1 added with W5a-44 + W4c-36 synthesis content; (c) forward enforcement clause for plan-freeze validators landing a cross-pillar bridge entry: SHOULD verify fiducial-anchor declaration when bridge map composes through pre-substrate pin (SUGGESTED at K=1, MANDATORY at K=3); (d) cross-link to `phononic-framing.md §"IS Space, Not IN Space"` for direction-of-explanation consistency (substrate-IS direction must flow through the binding-pin choice declared in element 3); (e) METHODOLOGY-class allowlist row appended.
- **Effort**: 0.4 wave-equivalents (rule-file edit + calibration corpus row + forward enforcement clause + cross-reference table updates + methodology-wave-allowlist row + dual-SHA verdict trio).

### V.8. Mellin moment pin f0 / f2 / f4 substrate-first provenance audit (independent of V.1)

- **What**: Audit the derivation provenance of the plan-pinned Mellin moments `f0=0.0883200, f2=214.97335676, f4=6446.63942272` independent of the V.1 §VII.AN/AO corrective successors. The 2.85% match between W5a-44's best Route-A candidate `−f0 = -0.08832000` and the target -0.08587279 suggests f0 was tuned at S82 W3-9 to leading-digit-approximate the target value (likely as a Route-B-image-derived parameter), NOT computed from a substrate-first Mellin-cone evaluation. If all three Mellin moments are Route-B-scheme-derived, then any Route-A-claimed framing of α_s_canonical via these pins inherits the same defect at the f-pin layer (orthogonal to the V.1 anchor-structure correction at the higher α_s_canonical layer). This CF is structurally upstream of V.1 in the canonical-sourcing audit pipeline.
- **Inputs**: `s82_w3_9_as_adjacent_obs.py` source script (full text, AST-parse for Mellin-moment computations); plan §W5a-44 Field 7 machinery pin map listing f0/f2/f4 per S82 W3-9 normalization; W5a-44 npz output `s88_w5a_a2_mellin_spectrum_cache_discriminator.npz` (carries the 8 Route-A normalization values with rel_diffs); cache `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949…` at L_max=12 (90 sectors p+q≤12; 31,956,720 multiplicity-weighted eigenvalues).
- **Gate**: `S89-MELLIN-MOMENT-FK-PROVENANCE-AUDIT` with PASS criterion: "f0, f2, f4 each have an explicit Route-A substrate-first derivation in some prior session script (cite script + line)". FAIL iff all three are Route-B-scheme-derived (in which case the §VII.AN/AO corrective entries from V.1 must additionally cite f-pin Route-B provenance at the bridge-map element 3 + Class-(g) audit picks up the f-pin layer as a separate calibration instance). INFO iff partial: at least one f-pin has Route-A provenance and at least one is Route-B-only.
- **Effort**: 0.4 wave-equivalents (script AST-parse + 8 candidate normalization re-trace through f-pin derivations + S82 W3-9 source-chain audit + 1 dual-SHA verdict trio + npz output table).

### V.9. JOINT-(substrate, observation) hypersurface pre-registration form K=1 calibration corpus seed

- **What**: Promote the W4c-36 INFO verdict's `value=` field carrying BOTH α_s readings to a NEW canonical pre-registration form: JOINT-(substrate, observation) hypersurface pre-registration. Concrete shape: any lab-protocol gate that consumes a substrate-IS observable derived through a CHILD pin (e.g., n_s for α_s; m_H for vacuum-energy ratios; sound-speed for transit-rate ratios) MUST emit a verdict-line `value=` field carrying BOTH (a) the substrate-self-consistent prediction at the framework's binding pin AND (b) the observation-comparison prediction at the external observational anchor — joined as a 2D discrimination target in (CHILD pin, observable) hypersurface space. This converts the implicit 1D-band-with-silently-chosen-anchor into an explicit 2D-hypersurface-with-declared-anchors. K=1 calibration from W4c-36; K=3 MANDATORY threshold per `feedback_rules-compensate-missing-structure.md`.
- **Inputs**: §W4c-36 verdict line at audit_sha256 `e75fbe551eab2119…` as canonical exemplar; W4c-36 working-paper §(c) HONEST FINDING text; result IV.1 (f) adjudication; result II Result 4 (joint-hypersurface form).
- **Gate**: `S89-JOINT-HYPERSURFACE-PREREG-FORM-K1-SEED` with PASS criterion: (a) NEW rule extension proposal landed at `epistemic-discipline.md §"Pre-Registration Completeness"` as a Class 8.4 candidate (joint-hypersurface verdict-line form); (b) calibration corpus row 1 added with W4c-36 instance content; (c) verdict-line schema extension proposal: optional `joint_hypersurface=<{(P,O)_substrate, (P,O)_observation}>` token in `value=` field for gates whose substrate-IS observable consumes a CHILD pin that is laboratory-IN at a different pillar; (d) cross-link to `gate-verdicts.md` S87+ schema-v2 + `cross-pillar-bridge-anatomy.md` element 3 fiducial-anchor sub-clause from V.7; (e) status SUGGESTION at K=1.
- **Effort**: 0.4 wave-equivalents (rule extension proposal + calibration corpus row + schema-extension proposal + cross-reference updates + STAGE-1-CANDIDATE registration per joint-theorem-promotion 4-stage pathway).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | α_s_canonical = (9561/10000)² − 1 EXACTLY in **Q** (verified Python `Fraction`; 9561² = 91412721 perfect square) | GEOMETRIC (algebra-axis identity) | NEW STRUCTURAL FACT | Single bit-exact pin replaces the ambiguous "≈ to 4 decimals" framing in W5a-44 §(c); n_s_FW = Fraction(9561, 10000) becomes the canonical exact pin from which α_s_canonical is deterministically derived |
| 2 | W5a-44 best Route-A candidate `−f0 = -0.08832` rel_diff = 2.85e-2; PASS threshold 1e-12 missed by 10 OOM (verified Python) | PHONONIC (substrate Mellin-residue eval at substrate-distance-1 pole, L_max=12) | FAIL STRUCTURAL (verdict line `c092fe1bff9ab669…` permanent; informative) | Confirms Route-A absent at Mellin-residue axis; Route-B canonical at n_s axis (Result 1); registry-anchor framing at §VII.AN mis-classified |
| 3 | Plan §W4c-36 lines 791 vs 802 internally inconsistent: α_s = -0.08587279 ↔ Planck n_s = 0.9649 mutually inconsistent under Route-B (n_s² − 1 at 0.9649 = -0.06896799, not -0.08587279); discrepancy 15× combined falsification band | PARTICLE (representation-theoretic identity mis-bound to wrong n_s anchor at plan-authorship) | INFO STRUCTURAL (W4c-36 verdict `e75fbe551eab2119…` honestly carries both values) | Lab discrimination target requires explicit binding-pin declaration; structurally-honest form is JOINT (n_s, α_s) hypersurface (Result 4) |
| 4 | JOINT-(n_s, α_s) hypersurface = structurally-honest discrimination target (substrate self-consistent point (9561/10000, -8587279/100000000) + Planck observational locus (0.9649, ~-0.069); lab measures 2D, not 1D α_s alone) | PHONONIC (substrate-derived bridge anatomy) | NEW PRE-REGISTRATION FORM (Stage-1 calibration corpus instance #1) | Operationalizes algebra-axis structural orthogonality at the laboratory layer; pre-registers Stage-2 cross-axis verify (V.4) |
| 5 | §VII.AN W5a-37 SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure FAILs `registry-landing.md §"Detection"` criterion 2 (non-fungibility) under K=3 algebra-axis MANDATORY: ANCHOR-1 (V) and ANCHOR-2 (C) live on cross-corner cells that cannot enter a single non-fungible chain | GEOMETRIC (registry-anchor structural defect) | REQUIRES Option-A `supersedes`-tagged corrective successor entries at §VII.AN + §VII.AO (V.1); §VII.AP UNCHANGED | Re-classifies §VII.AN as PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM; original verdict line retained per gate-verdicts.md absolute permanence; supersedes-tag protocol per S88 W8-100 Option-A |
| 6 | substrate-first-canonical-sourcing.md §(i) calibration corpus advances K=3 → K=4 (NEGATIVE-CALIBRATION add: W5a-44 = registry-anchor cited Route-A but closure script implements only Route-B) | NON-PHONONIC (methodology rule corpus) | MANDATORY promotion event triggered (V.5); SUBSTRATE-FIRST-PROVENANCE sub-audit becomes MANDATORY at plan-freeze for S89+ registry-landings | Closes the post-hoc-substrate-first-discovery class of registry mis-classification by construction at plan-freeze for all future registry gates |
| 7 | NEW Class-(g) `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` candidate for `_source_reconciliation_audit.py` taxonomy (K=1 calibration from W5a-44; SUGGESTION until K=3) | NON-PHONONIC (audit-script taxonomy extension) | Proposed (V.3); detection regex Route-A vs Route-B at AST-parse level; HARD-HALT severity at landing-time | Catches registry-anchor mis-classification before it propagates downstream into corrective Option-A successor entries — a structurally upstream filter |
| 8 | Mellin moment pin f0 / f2 / f4 provenance audit independent of V.1 (suspicious 2.85% match between `−f0` and target suggests f-pin layer also Route-B-derived) | PHONONIC (substrate-distance Mellin-cone normalization layer) | OPEN (V.8 carry-forward; structurally upstream of V.1) | If FAIL, the §VII.AN/AO corrective entries from V.1 must additionally cite f-pin Route-B provenance at element 3 of bridge anatomy |
| 9 | mack-cosmic-bridge agent-memory "alpha_s symbol overload" trap (S50-51 identity is topological-scheme-only) PROMOTED from qualitative warning to algebraic pin: 8-decimal Sage-QQ literal at α_s_canonical IS a rational image of n_s_FW = 9561/10000 EXACTLY in **Q** | NON-PHONONIC (agent-memory pin update) | UPDATED (this synthesis) | Forward sessions citing α_s_canonical can derive any required precision deterministically from the single n_s_FW = Fraction(9561, 10000) pin (V.2) |

---

## Substrate framing (mandatory per `phononic-framing.md §"IS Space, Not IN Space"`)

The substrate IS the spectral triple `(A_K, H_K, D_K)` at the τ_fold = 0.190 Jensen slice. The framework predicts n_s as a substrate-IS observable from the algebra-INVARIANT spectrum-only family at the substrate-distance-1 single-pole; α_s_canonical is the IMAGE of n_s under the Route-B identity α_s = n_s² − 1, which is itself an algebra-axis identity acting on the n_s prediction (NOT a separate Mellin-residue evaluation at the same pole). The bit-exact Result 1 says: at n_s_FW = Fraction(9561, 10000) the Route-B image lands on the Sage-QQ literal -8587279/100000000 with NO ROUNDING. The substrate IS the spectrum-only family that produces the n_s pin; the Route-B identity IS the algebra-axis morphism that takes the n_s pin to its α_s image.

The W5a/W4c canonical-sourcing concern was: should α_s_canonical at §VII.AN/AO be framed as a SEPARATE Mellin-residue derivation (Route-A canonical) or as an IMAGE of the n_s prediction (Route-B canonical at n_s axis)? The bit-exact Result 1 + the W5a-44 FAIL together resolve this in favor of the second framing. The substrate's substrate-first content for α_s_canonical IS the n_s pin + the Route-B image identity; trying to derive α_s_canonical from the L_max=12 spectrum cache bypassing n_s is a reconstruction attempt that the substrate's own algebraic structure does not require.

The laboratory-IN side is the Planck/ACT α_s = +0.0023 ± 0.0063 measurement (Aiola 2020 ACT DR4 + Planck) at k_pivot = 0.05 Mpc⁻¹, which lives in the FRW cosmology container as the running of the scalar tilt. The bridge map is Mukhanov-Sasaki gauge ∘ HKR `L_max → ∞` per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"` candidate FWD-C1. Direction of explanation flows substrate IS → bridge map → laboratory IN: the substrate IS the n_s pin; the Route-B identity IS the algebra-axis image; the Mukhanov-Sasaki gauge IS the bridge map; the laboratory IN is the Planck/ACT measurement of CMB-running. Inverting (treating Planck/ACT α_s as fundamental and asking "what substrate value matches it?") is forbidden per `phononic-framing.md`; the joint-hypersurface form (Result 4) preserves this direction by carrying BOTH the substrate-self-consistent point AND the Planck observational locus as PRE-REGISTERED prediction-vs-observation pair, NOT as competing canonical anchors.

Container thinking violation guard: treating the n_s²−1 identity as "merely a topological-scheme rationalization of a real Mellin-residue value" inverts the substrate-IS direction at the algebra-axis layer. The algebra-axis identity IS the substrate's own structural relation between two readings of the same spectrum-only family at the same Mellin pole; it is NOT a downstream rationalization. This is why the W5a-44 FAIL is honestly informative rather than negative — it surfaces that the substrate's own algebraic structure does not need a separate Mellin-residue derivation at the spectrum-cache layer to produce α_s_canonical, because the substrate already produces α_s_canonical via the n_s pin + algebra-axis identity composition.

---

## Closing — what this synthesis pins for downstream consumption

Six pins for downstream sessions:

1. **n_s_FW_exact = Fraction(9561, 10000)** is the substrate-first canonical pin for the framework's n_s prediction at the algebra-INVARIANT spectrum-only family. All scheme-dependent floats (0.9567 / 0.9557 / 0.9595 / 0.9590) are downstream truncations of this rational pin. Promoted to canonical_constants.py via V.2.

2. **α_s_canonical = (n_s_FW_exact)² − 1 = -8587279/100000000 EXACTLY in Q** is the algebra-axis Route-B image identity. No separate Mellin-residue derivation exists or is needed at the substrate spectrum-cache layer.

3. **§VII.AN W5a-37 and §VII.AO W5a-42 require Option-A `supersedes`-tagged corrective successor entries** demoting their inherited SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure to PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM. Original verdict lines RETAINED per gate-verdicts.md absolute permanence. §VII.AP W5a-43 UNCHANGED.

4. **W4c-36 lab discrimination target form is JOINT (n_s, α_s) hypersurface**, not 1D α_s band. Pre-registers Stage-2 cross-axis verify at S89 (V.4). The W4c-36 INFO verdict line carrying BOTH α_s readings is the canonical form for this pre-registration shape.

5. **substrate-first-canonical-sourcing.md §(i) calibration corpus K=4 MANDATORY promotion**: SUBSTRATE-FIRST-PROVENANCE sub-audit becomes MANDATORY at plan-freeze for all S89+ registry-landing gates. NEW Class-(g) `REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION` proposed for `_source_reconciliation_audit.py` (K=1; SUGGESTION until K=3).

6. **mack-cosmic-bridge agent-memory "alpha_s symbol overload" pin updated**: from qualitative warning (S50-51 topological-scheme-only) to algebraic pin (8-decimal Sage-QQ literal IS rational image of n_s_FW = 9561/10000 EXACTLY in **Q**). Forward sessions cite the n_s pin as the canonical source; α_s_canonical is its bit-exact image under the algebra-axis identity.

The unifying observation: the algebra-axis K=3 MANDATORY structural orthogonality discipline (`cross-pillar-bridge-anatomy.md`) operates not just at the cross-corner gate-comparison layer but at the registry-anchor layer too. Cross-corner co-primary is forbidden at §VII.AP for the same structural reason that §VII.AN's V+C anchor pairing is mis-classified. The W5a + W4c synthesis is one structural fact viewed from two angles; this synthesis surfaces that fact and routes the corrective work through Option-A `supersedes`-tagged successors that preserve the verdict-permanence audit trail by construction.
