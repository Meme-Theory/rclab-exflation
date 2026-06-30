# Session 88 W23 Synthesis: W7b-82 LEVEL-2 closure + W7c-167 obs1 PASS-AND — what "structurally-independent agreement" means under shared substrate inputs

**Date**: 2026-05-07
**Agent**: volovik-superfluid-universe-theorist (vlk)
**Source Documents**:
- `sessions/archive/session-88/session-88-w7b-workingpaper.md`
- `sessions/archive/session-88/session-88-w7c-workingpaper.md`
- `sessions/session-plan/session-88-plan-w7b.md`
- `sessions/session-plan/session-88-plan-w7c.md`
- `sessions/archive/session-88/workshops/_seed-w7b.md`
- `sessions/archive/session-88/workshops/_seed-w7c.md`
- `sessions/permanent-results-registry.md` §VII.AH (lines 15399-15479) + §VII.AQ (W7b-79 landed slot)
- `.claude/rules/joint-theorem-promotion.md`
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`

---

## I. Session Outcome

The two pre-registered Stage-2 successes that W7b/W7c delivered — §W7b-82 LEVEL-2 odd-grading closure at `GV_rel_sep = 1.000e+00` and §W7c-167 obs1 first-ever cross-axis PASS-AND on §VII.AH — both PASS their pre-registered thresholds correctly, but neither satisfies a substrate-input-orthogonality criterion that the joint-theorem-promotion.md procedural floor does not currently demand. The synthesis routes (a) §W7c-167 obs1 PASS-AND as **calibration-corpus instance #1 with explicit calibration caveat (Verdict B, accept-but-flag)**, (b) §VII.AQ LEVEL-2 closure as **OPERATIONAL at L_max=10 cache resolution under canonical-import binding** with explicit cache-resolution-status disclosure required in the registry text, and (c) a NEW substrate-input-orthogonality clause for `joint-theorem-promotion.md §"Stage 2"` requiring at least one orthogonal-data observable in any Stage-2 verification before the calibration corpus advances. The §VII.AQ STAGE-1-CANDIDATE Stage-2 dispatch in S89+ is NOT BLOCKED on chirality-resolved spectrum recompute, but the registry-text Level-3 anchor block MUST carry the cache-resolution caveat.

---

## II. Key Results

### Result 1 — Procedural-floor independence is NECESSARY but not SUFFICIENT (Workshop 1, primary verdict)

**Result**: The current `joint-theorem-promotion.md §"Two-Agent Independent-Verify"` independence guarantee — *"the two cross-reviewers operate WITHOUT prior workshop context"* (Stage 2, item 4) — is a **procedural floor on shared workshop transcripts**, NOT a substrate-input-orthogonality test. It rules out one channel of shared output (re-derivation along the workshop's own narrative) but admits another (independent verdicts driven by the same numerical inputs). Classification: **METHODOLOGY**.

The §W7c-167 obs1 PASS-AND is a clean instance of the procedural floor being satisfied while the substrate-input-overlap channel remains structurally open. Both cross-reviewers consumed:

- the same successor data file `s87_w7_ic_per_class_verify.npz` (SHA-256 `120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f`) — same numerical `M_at_s_neg1` 5-vector `[0.158101, 0.158101, 0.111003, 0.031847, 0.154446]`, same `xi_per_class = [13.642, 13.642, 9.578, 2.748, 13.327]`, same `posterior_A = 1.82e-216`, same `posterior_B = 1.0`;
- the same registered §VII.AH STAGE-1-CANDIDATE entry text (`sessions/permanent-results-registry.md` lines 15399-15479);
- the same canonical_constants pins `xi_E_GGE_inv = 13.642473`, `tau_fold = 0.190`, `M_KK = 7.43e16`.

The two reviewers' verdicts diverge on derivation-machinery — mack-cosmic-bridge runs through `M_R(s=-1)` 5-tuple × within-F_2-branch unitarity residuals; connes-ncg runs through §VII.U.2 4-corner parse-tree decision + Bayesian `log10_BF_BA = 215.56` — but both verdicts *consume the same data file's bit-identical numerical fields*. The substitution chain that yields `posterior_B = 1.0` is shared; the verdict-statement language differs.

**Substitution chain — what the procedural floor actually rules out vs admits**:

```
Step 1 (Definition): "shared context" in joint-theorem-promotion.md §"What
        Counts as Evidence" item 2 = (i) read same workshop R1/R2/R3 transcripts
        ∨ (ii) consume same authored derivation chain ∨ (iii) consume same
        numerical inputs ∨ (iv) cross-cite each other's authored sub-statements.

Step 2 (Procedural floor; current rule): the protocol prohibits (i) explicitly
        ("cross-reviewers receive ONLY the registered Stage-1 entry text +
        relevant input files; do NOT receive workshop transcripts").

Step 3 (Substitutions for §W7c-167 obs1):
        - (i) workshop R1/R2/R3 NOT read by either reviewer ✓ rule complies.
        - (ii) lizzi/transit ORIGINAL authored derivation chain — connes-ncg
              audits §VII.U.2 4-corner machinery he authored at S87 W-2 R3;
              mack audits clauses (a)+(c)+(d)+(e) without authoring them.
              Mixed compliance: connes self-cites his own §VII.U.2 axiom set;
              mack does not self-cite.
        - (iii) numerical inputs SAME (SHA-256 pin verified on
              s87_w7_ic_per_class_verify.npz; both scripts list it as input).
        - (iv) connes-side audit text is a parse-tree application of §VII.U.2
              clause (e) (which is connes-authored at the rule-file level).
              mack-side does not cross-cite §VII.U.2 outside its registry
              quotation.

Step 4 (Direction): the procedural floor cleanly rules out channel (i) only.
        Channels (ii), (iii), (iv) are partially or fully present.

Conclusion: the §W7c-167 obs1 PASS-AND satisfies the LITERAL Stage-2 protocol
            but only weakly satisfies the STRUCTURAL "without shared context"
            intent. The structurally-independent-confirmation reading of the
            calibration-corpus instance #1 needs a substrate-input
            orthogonality clause to harden the procedural floor into a
            structural ceiling.
```

The structural reading: **substrate-input orthogonality** — at least one observable in the Stage-2 verification consumes a data file the OTHER reviewer DID NOT consume — is the load-bearing additional clause. It is not currently in `joint-theorem-promotion.md`.

### Result 2 — LEVEL-2 closure is OPERATIONAL at L_max=10 cache resolution under canonical-import binding (Workshop 1 secondary verdict)

**Result**: §W7b-82's `GV_rel_sep = 1.000e+00` PASS verdict is structurally correct against its pre-registered threshold; the 1.000 figure is sourced from the canonical-import pin `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 promoted at full per-sector chirality fidelity). The substrate-natural compute on the L_max=10 cache `s84_spectrum_cache_L12_tau019.npz` returns `Δ_GV_natural = 0` because the cache stores `abs_evals` per (p,q)-sector with uniform 8d:8d chirality split — the H-block C_epsH parity-flip is realized at a sub-grading layer the cache averages over. Classification: **GEOMETRIC**.

This is **NOT** a verdict defect. The canonical-import IS the substrate-IS substantive value (computed at full chirality fidelity in S87 W8-8); consuming it at L_max=10 cache evaluation is faithful to PRU Class 8.3 publication-precision pre-registration discipline (W8-8 published at 14 sig figs; the W7b-82 verifier consumes that pin). What the cache-resolution diagnostic Result (2) at WP §W7b-82 actually surfaces is a structural distinction: the `Tr_{M_2(C)}(P_eta-...)` Element-2 OE-form per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` (W7a-73 hardening, MANDATORY at K=2) is **operationally validated by canonical-pin floor** at the current cache, NOT by substrate-natural compute. Both validation routes are admissible per the rule's calibration corpus, but they entail different epistemic states that the Level-3 empirical anchor block currently conflates.

**Substitution chain — substrate-natural vs canonical-import as Level-3 anchors under cross-pillar-bridge-anatomy.md Level-2-binding**:

```
Step 1 (Definitions, per cross-pillar-bridge-anatomy.md §"Level-2 Layer
        Distinction"):
        Level-2-binding envelope = HKR(c_L) → c_continuum convergence rate;
        Level-3 empirical anchor = numerical evaluation at canonical L_max
        (here L_max=10).

Step 2 (Substitutions for §VII.AQ post-W7b-79 lift):
        c_L (substrate-IS finite-L cocycle) = R_universal Hochschild pairing
        on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}) per W-5 calibration corpus.
        c_continuum (laboratory-IN BZ-trace) = Pillar IV continuum BZ
        quantum-metric Tr g_ab.
        For §VII.AQ specifically, the Element-2 OE-form is
        Tr_{M_2(C)}(P_eta-projector × ...) on the BdG sub-algebra.

Step 3 (Two distinct Level-3 anchors):
        Anchor route A (canonical-import binding): Δ_GV at full per-sector
        chirality fidelity = -40579.1500479506 (S87 W8-8 published).
        Substrate-IS at the level the cache layer averages over.
        Anchor route B (substrate-natural binding): Δ_GV computed by the
        W7b-82 producing script on the consumed L_max=10 cache returns 0
        because abs_evals + uniform 8d:8d chirality split averages the
        H-block sub-grading.

Step 4 (Both routes satisfy the rule):
        Both A and B are Level-3 candidates; they are LITERALLY DIFFERENT
        NUMBERS at L_max=10 cache resolution (-40579.15 vs 0.0). The
        structural identity holds (W-11 STRENGTHENED) at the axiom level
        but separates at the operational level by cache-resolution.

Direction: under cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"
        item 5 + item 6 (S88 W8-88 hardening), the entry MUST declare
        which Level-2 sub-class (Level-2-binding vs Level-2-non-binding)
        it occupies. §VII.AQ post-W7b-79 inhabits Level-2-binding (the
        envelope is the HKR `L_max → ∞` map convergence) but the
        Level-3 anchor is route A (canonical-import) NOT route B
        (substrate-natural-on-cache). Both routes are admissible; the
        registry text MUST disclose which route is consumed.

Conclusion: §VII.AQ Level-3 empirical anchor block is
        PASS-via-canonical-import-pin under the cache resolution the
        producing script actually instantiates. Substrate-natural-compute
        validation route exists but is NOT the route §W7b-82 takes.
        Both are admissible per the rule; explicit disclosure of which
        route is the operational one is required.
```

This is structurally a **Level-3 sub-classification** — not a Level-1/Level-2 issue. The W-11 STRENGTHENED axiom-level identity (clause η = 0 across the parity-twin pair) holds at Level-1 unconditionally; the L^{-3} Level-2 envelope holds; the Level-3 anchor satisfies its floor by canonical-import. Substrate-natural compute on the L_max=10 cache validates the η-NULL prediction (`eta_diff = 0.0` matches structurally) but yields zero discrimination on GV at the cache layer — that is a CACHE-resolution feature, not a substrate-physics feature.

### Result 3 — Bayesian log10_BF_BA = 215.56 is partially-orthogonal evidence-substantiation, not double-counting (Workshop 1 sub-verdict)

**Result**: The Bayesian factor `log10_BF_BA = 215.56` (verified Python: `math.log10(1.60e-5 / 4.36e-221) = 215.56463349`) computed by connes-ncg-side at obs1 IS derived from data fields (`likelihood_A = 4.36e-221`, `likelihood_B = 1.60e-05`) that mack-side ALSO loaded from `s87_w7_ic_per_class_verify.npz`. However, the two sides apply the data through structurally distinct decision channels:

- mack-side uses the `M_at_s_neg1` 5-vector + `cc_zeta/cc_sdw` unitarity residuals to construct a **per-class IC verification** verdict (substrate-distance-1 spectral content read as F_2-class identity preservation at machine-ε);
- connes-ncg-side uses the same likelihood fields to construct a **Bayesian-posterior decision** between the F_2 = {ζ, SDW} hypothesis and the A_5-equal-weight hypothesis.

These are two DIFFERENT structural readings of the same numerical observation. Classification: **METHODOLOGY**.

The double-counting risk surfaces only if the JOINT clause's PASS-AND aggregation requires BOTH legs to be independent of the underlying data — which is structurally impossible for any numerical-substantiation clause. What is required is that the two legs apply the data through structurally-distinct decision pipelines (different functional-class machinery, different verdict-output type). At obs1: spectral-side PASS-EXTENDED on the F_2 identity at s=-1 (substrate-distance scope-extension claim) is structurally distinct from axis-orthogonality-side PASS-CORNER-I (Corner-cell parse-tree assignment + Bayesian numerical substantiation). The two channels share the substrate but differ in the structural-output type. This is partial orthogonality, not full orthogonality — sufficient for Stage-2 PASS under the procedural floor, insufficient for substrate-input orthogonality.

### Result 4 — §VII.AQ Stage-2 dispatch is NOT blocked on chirality-resolved spectrum recompute (Workshop 1 conditional verdict)

**Result**: `S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE` is queued at S89+ with effort ~1.5 wave-equivalents. It is structurally **NOT BLOCKING** for §VII.AQ Stage-2 dispatch under the canonical-import-binding reading. Classification: **GEOMETRIC**.

Reason: §VII.AQ is registered as a STAGE-1-CANDIDATE entry per `joint-theorem-promotion.md` 4-stage pathway. The Stage-2 cross-reviewer protocol (per Stage-2 §"Two-Agent Independent-Verify" item 4: *cross-reviewers operate WITHOUT prior workshop context, reading only the registered Stage-1 entry + relevant input files*) consumes whatever the registry text declares as the Level-3 empirical anchor + whatever input files the registered theorem cites. If the registry text consumes the canonical-import pin `gv_canonical_difference_FW`, the Stage-2 reviewers verify the AXIOM-LEVEL identity (W-11 STRENGTHENED η = 0) + the ANCHOR FLOOR (`|GV_diff − gv_canonical_difference_FW| < 6.257e-10`) and the chirality-resolved spectrum recompute is not on the critical path.

If the registry text adds a cache-resolution caveat in the Level-3 anchor block (recommended; see §V.4), then the Stage-2 reviewers know the operational route consumed and can verify accordingly. The chirality-resolved recompute upgrades the Level-3 anchor from canonical-import-binding to substrate-natural-binding — a structural strengthening, not a Stage-2 prerequisite.

### Result 5 — §VII.AH STAGE-1-CANDIDATE plan vs S88 actual cross-reviewer assignment is itself a substrate-input non-orthogonality (Workshop 1 verifier observation)

**Result**: The §VII.AH STAGE-1-CANDIDATE registry text (lines 15453-15454) pre-registers Stage-2 cross-reviewer assignments: **connes-ncg-theorist as spectral-side reviewer auditing clauses (a)+(c)+(d)+(e); volovik-superfluid-universe-theorist as transit-side reviewer auditing clauses (b)+(c)+(d)+(f)**. The S88 W7c-167 dispatch substituted **mack-cosmic-bridge for connes-ncg on the spectral side** (per `feedback_mack-bridge-role.md`; the §VII.AH text marks volovik as "alternate spectral-side per S86 W-9 workshop") and **moved connes-ncg to a newly-named "axis-orthogonality side" auditing clauses (b)+(c)+(d)+(f)** (i.e., the originally-volovik clauses). Classification: **METHODOLOGY**.

This is a structurally significant shift, not just a name-relabel:

- The original Stage-2 protocol pre-registered cross-axis = (spectral-functional + transit-dynamics). The S88 dispatch reframed it as (spectral-functional + algebra-axis-orthogonality) — different cross-axis pair entirely.
- volovik (originally pre-registered as transit-side) is now BLACKLISTED for §VII.AH Stage-2 dispatch (per plan §365 BLACKLIST: "lizzi-spectral-functional-theorist, transit-dynamics, gen-physicist") because volovik's transit-dynamics-theorist role is conflated with the original transit-side authorship — but volovik was NOT a workshop author of S86 W-9. The BLACKLIST was tightened in plan §365 without explicit verifier-rubric for who is structurally an "original workshop author."
- connes-ncg's NEW axis-orthogonality assignment audits §VII.U.2 4-corner classification — which connes-ncg himself authored at S87 W-2 R3. This is a structural self-citation at the audit machinery level. Per `joint-theorem-promotion.md §"Two-Agent Independent-Verify"` item 3 (*"They cannot be the original workshop authoring agents"*), connes is admissible for §VII.AH because he was not the S86 W-9 author. But the audit machinery he applies (§VII.U.2) is his own work; the parse-tree decision procedure is connes-side both at authoring and at application.

Substrate-input non-orthogonality at obs1 = (i) shared numerical data + (ii) shared registry text + (iii) authors-cite-own-machinery. The §W7c-167 obs1 PASS-AND under the procedural floor is correct against `joint-theorem-promotion.md` as written; the registered §VII.AH protocol substitution itself constitutes a structural deviation that should be acknowledged in the calibration corpus.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W7b-82 LEVEL-2 closure (canonical-import binding admissibility) | **PASS-OPERATIONAL-WITH-DISCLOSURE** | `GV_rel_sep = 1.000e+00` (canonical-import) at audit_sha256 `6b5bdb7f7ae02634...`; substrate-natural Δ_GV_natural = 0 at L_max=10 cache (cache-averaging diagnostic, NOT substrate-physics defect) |
| §W7c-167 obs1 PASS-AND counts as calibration-corpus instance #1 | **VERDICT B (accept-but-flag-with-calibration-caveat)** | Both axes PASS at obs1 under procedural floor; substrate-input overlap (shared `120435cbfd5ef313...` SHA + shared registry + shared canonical pins) requires explicit caveat in `joint-theorem-promotion.md §"Calibration corpus"` |
| §VII.AQ Stage-2 dispatch blocked on `S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE`? | **NO-GO-FOR-BLOCKING** | Recompute is structural strengthening (Level-3 substrate-natural-binding upgrade), not Stage-2 prerequisite; canonical-import binding is admissible per cross-pillar-bridge-anatomy.md §"Level-2-binding" sub-class |
| Level-2-binding sub-class declaration for §VII.AQ Level-3 anchor | **PASS-via-canonical-import-pin** with mandatory cache-resolution caveat in registry text | `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 promoted at full per-sector chirality fidelity) consumed; cache-averaging diagnostic in WP §W7b-82 Result (2) NOT yet in registry text |
| Substrate-input-orthogonality clause for `joint-theorem-promotion.md §"Stage 2"` | **REQUIRED** | New rule-file clause: every Stage-2 verification must include ≥1 observable on a data file consumed by exactly one reviewer; PASS-AND across orthogonal-data observables hardens the calibration corpus |

These verdicts are derived from the source-document gate verdicts; nothing is re-adjudicated. The W7b-82 PASS at audit_sha256 `6b5bdb7f7ae02634...` and the W7c-167 obs1 PASS-AND at audit_sha256 `44665980fba0af17...` (mack) + `e9116c06a12ba8d7...` (connes-ncg) stand. The structural classifications above operate over those PASS verdicts at the rule-file layer.

---

## IV. Structural Implications

### 1. The "agreement among agents" exclusion has a procedural-floor reading and a substrate-input reading

`epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2 forbids "agreement among agents" because *"shared context produces shared outputs, not independent confirmation."* The current `joint-theorem-promotion.md` Stage-2 protocol operationalizes this as "no shared workshop transcripts." The §W7c-167 obs1 instance shows this is a procedural floor — the literal protocol can be satisfied while the structural intent (independent-of-shared-numerical-input verdicts) is partially violated.

The constructive complement: a Stage-2 verification produces structurally-independent agreement IFF (i) procedural-floor holds (no shared workshop transcripts) AND (ii) substrate-input orthogonality holds (≥1 observable in the verification consumes a data file that only one reviewer loaded). Without (ii), Stage-2 PASS-AND establishes structural-output-type independence (different decision pipelines on the same data) but not structural-input independence (the data itself is shared).

This refinement does NOT contradict `epistemic-discipline.md §"What Counts as Evidence"`; it sharpens what "independent" means in the Stage-2 calibration corpus.

### 2. §VII.AQ STAGE-1-CANDIDATE → STAGE-3-PERMANENT pathway is operational at canonical-import fidelity

The §VII.AQ post-W7b-79 lift can proceed via Stage-2 dispatch at S89+ as a canonical-import-binding verification. The Stage-2 cross-reviewers (per joint-theorem-promotion.md Stage-2 protocol) verify:

- Level-1 axiomatic identity: η-NULL across (C_H, C_epsH) parity-twin pair via W-11 STRENGTHENED structural argument (regulator-INDEPENDENT, axiom-layer);
- Level-2 envelope: HKR `L_max → ∞` map (Level-2-binding per cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction" S88 W8-88 hardening);
- Level-3 anchor: `|GV_diff − gv_canonical_difference_FW| < 6.257e-10` publication-precision floor satisfied at L_max=10 cache resolution under canonical-import-pin consumption.

What the Stage-2 cross-reviewers should NOT have to verify: substrate-natural recompute on chirality-resolved spectrum (that is `S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE`'s job). The current §VII.AQ Level-3 block needs explicit cache-resolution status text so the Stage-2 reviewers know which route is consumed.

### 3. The §W7c-167 calibration corpus instance #1 of `joint-theorem-promotion.md` is a structurally-meaningful precedent — under caveat

Treating obs1 PASS-AND as *unconditional* instance #1 risks downstream cross-pillar bridges chaining Stage-2 success precedent off it without inheriting the substrate-input-overlap context. This is the highest-leverage methodological risk surfaced by W7c-167: future Stage-2 verifications will read the calibration corpus as "this protocol works at one observable when both reviewers operate without prior workshop context" without inheriting the substrate-input-overlap caveat, and the next theorem chain may inherit the structural blind spot.

The mitigation: explicit calibration-corpus row + caveat text + new substrate-input-orthogonality clause for forward verifications. Volovik concurs with the procedural-floor compliance and registers the calibration caveat in the same rule-file edit.

### 4. Stage-2 cross-reviewer assignment substitution at S88 W7c-167 (volovik → mack as spectral-side; connes-ncg → axis-orthogonality-side) is itself a structural deviation worth recording

The §VII.AH STAGE-1-CANDIDATE registry text pre-registered (connes-ncg, volovik) as the cross-reviewer pair with (spectral, transit) axes; S88 W7c-167 dispatched (mack, connes-ncg) with (spectral, axis-orthogonality) axes. This shift is admissible under the Stage-2 protocol (item 3 forbids only "original workshop authoring agents"; both mack and connes-ncg pass that test for §VII.AH = S86 W-9), but the (mack, connes-ncg) configuration has different shared-context structure than the (connes-ncg, volovik) configuration the registry text pre-registered. Specifically: connes-ncg authored §VII.U.2 4-corner classification at S87 W-2 R3 — the audit machinery he applies on the axis-orthogonality side IS his own work. This is structurally weaker than the (connes-ncg spectral + volovik transit) configuration in which neither reviewer's audit machinery is self-authored.

For substrate-input orthogonality going forward, the §VII.AH Stage-2 re-dispatch at S89+ on obs2 + obs3 should consider: (i) volovik (this agent) on transit-side or substrate-natural-recompute side (untouched-by-prior-workshop substrate-IS axis); (ii) explicit sequestration of whose-machinery-is-applied-by-whom; (iii) at least one observable on a data file the OTHER reviewer DID NOT consume.

### 5. cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction" (S88 W8-88 hardening) provides a clean sub-class taxonomy for the W7b-82 closure question

Per `cross-pillar-bridge-anatomy.md` (this rule-file's §"Level-2 Layer Distinction" hardened S88 W8-88), Level-2 envelopes split into Level-2-binding (HKR-image of substrate-IS finite-L cocycle binding to laboratory-IN continuum) vs Level-2-non-binding (bare-decomposition convergence rate with no HKR image). §VII.AQ post-W7b-79 inhabits Level-2-binding: the envelope is the `L_max → ∞` HKR map taking the substrate-IS Hochschild pairing R_universal to the laboratory-IN continuum BZ-trace (W-5 calibration corpus instance #1). The cache-resolution diagnostic at WP §W7b-82 Result (2) is operationally an artifact of the L_max=10 truncation taken AT FIXED canonical-import pin — it is not a Level-2-non-binding signal.

### 6. Two non-redundant pin disciplines at the verdict-line `convention=` field

§W7b-83 promoted the SCHEMATIC-vs-FULL physical level pin from SUGGESTION (K=1) to MANDATORY (K=4) at plan-freeze. §W7b-82 as a clean PASS uses canonical-import binding at full per-sector chirality fidelity (W8-8 substrate-IS published value); the substrate-natural cross-check IS disclosed in WP §W7b-82 Result (2). The W7b-82 verdict-line `convention=cheeger_simons_odd_grading_proxy_canonical_aps1975` does not currently encode the "canonical-import-vs-substrate-natural" axis as a third pin. §V.5 below proposes adding this distinction as forward-looking calibration discipline (NOT as a new MANDATORY rule pending K=3 corpus).

---

## V. Carry-Forward Computations

V.1. **Substrate-input-orthogonality clause for `joint-theorem-promotion.md §"Stage 2"`**
- **What**: Edit `.claude/rules/joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check"` to add a substrate-input-orthogonality clause: "every Stage-2 verification with ≥2 observables MUST include ≥1 observable on a data file consumed by exactly one reviewer; PASS-AND across orthogonal-data observables is the structural ceiling for the procedural-floor independence guarantee." Add explicit calibration corpus row marking S88 W7c-167 obs1 PASS-AND as **calibration-corpus instance #1 with substrate-input-overlap caveat** (Verdict B from this synthesis); pre-register S89+ §VII.AH Stage-2 re-dispatch on obs2 + obs3 as the discipline-validation gate. Cross-link to `epistemic-discipline.md §"What Does NOT Count as Evidence"` item 2 and to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 as the precedent for orthogonality-as-structural-criterion.
- **Inputs**: `.claude/rules/joint-theorem-promotion.md` (current text); §VII.AH STAGE-1-CANDIDATE registry text lines 15399-15479; §W7c-167 obs1 PASS-AND audit SHAs `44665980fba0af17` (mack) and `e9116c06a12ba8d7` (connes-ncg); shared-input file `s87_w7_ic_per_class_verify.npz` SHA-256 `120435cbfd5ef313...`; calibration corpus tracking via `feedback_rules-compensate-missing-structure.md` K-counter.
- **Gate**: `S89-JOINT-THEOREM-PROMOTION-SUBSTRATE-INPUT-ORTHOGONALITY-CLAUSE`. PASS iff (i) rule-file edit lands with explicit substrate-input-orthogonality clause text + calibration-corpus row for W7c-167 obs1 + Verdict-B caveat; (ii) `_joint_theorem_independent_verify_audit.py` extension landed verifying ≥1 orthogonal-data observable per Stage-2 dispatch; (iii) §VII.AH S89+ Stage-2 re-dispatch on obs2 + obs3 has obs2 and/or obs3 data file(s) NOT shared between the two reviewers' input-pin maps; FAIL if any of (i)-(iii) absent.
- **Effort**: 0.5 wave-equivalents.

V.2. **§VII.AQ Level-3 empirical anchor block: cache-resolution caveat text amendment**
- **What**: mack-cosmic-bridge (sole writer for `permanent-results-registry.md` cross-pillar entries per `feedback_mack-bridge-role.md`) edits §VII.AQ Level-3 empirical anchor block to add explicit cache-resolution status: *"Level-3 anchor PASS-via-canonical-import-pin against `gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 published at full per-sector chirality fidelity); substrate-natural compute on the L_max=10 cache `s84_spectrum_cache_L12_tau019.npz` returns `Δ_GV_natural = 0` due to uniform 8d:8d chirality split per (p,q)-sector — cache-averaging diagnostic, not substrate-physics defect (W-11 STRENGTHENED η-NULL at axiom level holds; W7b-82 audit_sha256 `6b5bdb7f7ae02634...`). Substrate-natural-binding upgrade route at `S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE` (~1.5 wave-equivalents); upgrade is structural strengthening, NOT Stage-2 prerequisite."*
- **Inputs**: §VII.AQ post-W7b-79 registry text (current); W7b-82 WP §W7b-82 Result (2) text (cache-averaging diagnostic); canonical_constants.py `gv_canonical_difference_FW`; cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction" S88 W8-88 hardening.
- **Gate**: `S89-VII-AQ-LEVEL3-CACHE-RESOLUTION-CAVEAT-AMEND`. PASS iff (i) registry text edited with cache-resolution caveat present in §VII.AQ Level-3 block; (ii) cross-pillar-bridge-anatomy.md §"Audit at plan-freeze" item 5 + 6 satisfied (Level-2 sub-class declared, HKR bridge map cited explicitly); (iii) §VII.AQ stage-2 dispatch text references the canonical-import binding route AND links to chirality-fidelity recompute as upgrade path.
- **Effort**: 0.2 wave-equivalents.

V.3. **§VII.AQ S89+ Stage-2 cross-axis independent-verify under canonical-import binding (with substrate-input orthogonality)**
- **What**: Two-agent parallel Stage-2 verification on §VII.AQ STAGE-1-CANDIDATE per `joint-theorem-promotion.md` Stage-2. Cross-reviewer assignment: connes-ncg-theorist (NCG-axiomatic spectral-side — audits W-11 STRENGTHENED η-NULL axiom; clauses CC1-CC8) + volovik-superfluid-universe-theorist (this agent; substrate-IS transit-physics side — audits 5-anatomy IS-not-IN block + Level-1/2/3 ladder + GV-Heitsch cocycle ratio per `inheritance-falsifier-protocol.md` Class B; clauses CC9-CC13). Substrate-input orthogonality enforced: connes consumes `s84_spectrum_cache_L12_tau019.npz` + `gv_canonical_difference_FW` pin; volovik consumes 3He-B cohomology-asymmetry ratio `‖φ_67‖/‖φ_88‖ = 7.3250` from `sessions/framework/correspondence/3HeB-inheritance-canonical.md` + `‖φ‖`-derived parity-twin spec (W7b-80 calibration). Joint clauses (Level-1 axiom + Level-3 anchor) PASS-AND'd across both reviewers.
- **Inputs**: §VII.AQ post-W7b-79 registry text (post-V.2 amendment SHA); §W7b-82 odd-grading-proxy data .npz SHA `6c38cf2120225df8`; canonical_constants.py `gv_canonical_difference_FW = -40579.1500479506`; `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949...`; `sessions/framework/correspondence/3HeB-inheritance-canonical.md` content SHA at plan-freeze; `joint-theorem-promotion.md` post-V.1-amendment text.
- **Gate**: `S89-VII-AQ-STAGE-2-INDEPENDENT-VERIFY-WITH-ORTHOGONALITY`. PASS iff BOTH cross-reviewers PASS on their respective axis clauses AND on the joint Level-1+Level-3 ladder AND substrate-input orthogonality holds (volovik consumes 3HeB-inheritance file connes does NOT load; connes consumes spectrum cache via Mellin pole interpretation volovik does NOT replicate). Promotes §VII.AQ to STAGE-3-PERMANENT on full PASS-AND.
- **Effort**: 1.0 wave-equivalent (canonical-import path; expedited because the chirality-fidelity recompute is OFF the critical path per §IV.4).

V.4. **§VII.AH S89+ Stage-2 re-dispatch on obs2 + obs3 with substrate-input orthogonality**
- **What**: Re-dispatch S88 W7c-167 Stage-2 on obs2 (`s87_anomaly_s4_s2_data.npz` or successor) + obs3 (`s87_mellin_residue_s3_s4_data.npz` or successor) per §V.1 substrate-input-orthogonality clause. Cross-reviewer assignment honors §VII.AH registry text pre-registration where structurally clean: connes-ncg-theorist (spectral-side, but audits CLAUSES (a) + (e) NOT (b) + (f); avoids self-citation of §VII.U.2 by routing the connes-ncg audit through different parse-tree machinery) + volovik-superfluid-universe-theorist (transit-side; audits clauses (b) + (f) per the §VII.AH original pre-registration). One observable (proposed: obs3 Mellin-residue-ratio) consumed by exactly one reviewer's input-pin map; the other reviewer cross-consumes a derivative quantity.
- **Inputs**: §VII.AH STAGE-1-CANDIDATE registry text post-V.1 (cite calibration-corpus instance #1 + Verdict-B caveat); `s87_w7_ic_per_class_verify.npz` (obs1 carryover for re-validation at substrate-input-overlapped instance); obs2 + obs3 successor data files from `S89-OBSERVABLE-2-ANOMALY-DATA-LANDING` (CF#7 of W7c) + `S89-OBSERVABLE-3-MELLIN-RESIDUE-DATA-LANDING` (CF#8 of W7c); BLACKLIST resolution per V.1 clarification (volovik admissible for transit-side; original-workshop-author test independent of agent role).
- **Gate**: `S89-VII-AH-STAGE-2-MULTI-OBSERVABLE-RE-DISPATCH-ORTHOGONALITY`. PASS iff (i) all 3 observables PASS-AND across both axes; (ii) ≥1 observable satisfies substrate-input orthogonality per V.1; (iii) connes-ncg's audit at one observable applies §VII.U.2 parse-tree decision NOT cross-citing his own authored 4-corner taxonomy at the verdict-emission level. Promotes §VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT.
- **Effort**: 1.5 wave-equivalents (3 observables × 2 axes; orthogonality-clause compliance check; pending V.1 + W7c CF#7 + CF#8 prereqs).

V.5. **Verdict-line `convention=` third pin: canonical-import vs substrate-natural binding (forward-looking K=1 calibration)**
- **What**: Pre-register a third orthogonal pin axis at the verdict-line `convention=` field for §VII-class registry-landing gates: `-CANONICAL-IMPORT-BINDING` (consume canonical_constants pin computed at higher-fidelity prior session) vs `-SUBSTRATE-NATURAL-BINDING` (compute the Level-3 anchor from the consumed cache without canonical-import). This is forward-looking calibration corpus K=1 (W7b-82 = first identified instance); status SUGGESTION pending K=3 promotion. Cross-link to `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` 2-axis comparison table to add a third axis. Not yet MANDATORY; tracked as compute carry-forward to allow further calibration corpus instances to surface.
- **Inputs**: §W7b-82 verdict line `convention=cheeger_simons_odd_grading_proxy_canonical_aps1975` (current); WP §W7b-82 Result (2) cache-averaging diagnostic; `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` 2-axis table; `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold.
- **Gate**: `S89-CONVENTION-PIN-CANONICAL-VS-NATURAL-BINDING-K1`. PASS iff (i) calibration corpus row added to `regulator-pin-discipline.md` cross-link table identifying canonical-import-vs-substrate-natural axis with W7b-82 as instance #1; (ii) forward-looking convention-suffix grammar registered (`-CANONICAL-IMPORT-BINDING` / `-SUBSTRATE-NATURAL-BINDING`); (iii) status declared SUGGESTION at K=1 with promotion path to K=3 MANDATORY.
- **Effort**: 0.3 wave-equivalents.

V.6. **calibration-corpus row addition to `permanent-results-registry.md §VII.U.2` clause (e) on cache-resolution-vs-canonical-import as NEW algebra-axis layer distinction**
- **What**: Per the workshop brief Output (vi), add a calibration-corpus row to `permanent-results-registry.md §VII.U.2` clause (e) (parse-tree decision procedure) that distinguishes substrate-natural-binding evaluations (substrate-IS-on-cache) from canonical-import-binding evaluations (substrate-IS-at-prior-fidelity-pinned). Cross-reference to `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` Level-2-binding sub-section. The new row notes that parse-tree-INVARIANT classification (clause (e)) holds for BOTH binding routes, but operational evaluation at L_max=10 cache may yield DIFFERENT numerical anchors at the same Corner — these are NOT cross-corner instances but sub-class layers within the same corner. This clarifies (for downstream consumers) that §VII.AQ's Level-3 anchor at canonical-import binding does NOT contradict §VII.U.2's Corner-cell INVARIANT classification; it inhabits the same corner under a sub-class binding route.
- **Inputs**: `permanent-results-registry.md` §VII.U.2 entry text; cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction" S88 W8-88 hardening text; W7b-82 WP §W7b-82 Result (2); §VII.AQ post-V.2 cache-resolution caveat text.
- **Gate**: `S89-VII-U-2-CALIBRATION-CORPUS-ROW-CACHE-VS-CANONICAL-IMPORT`. PASS iff registry-text edit lands with new calibration-corpus row + cross-link to cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction" + explicit declaration that sub-class binding routes do NOT trigger cross-corner classification.
- **Effort**: 0.3 wave-equivalents (mack-cosmic-bridge sole writer; routine registry edit).

V.7. **`S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE` deferred but tracked (substrate-natural-binding upgrade for §VII.AQ)**
- **What**: Per W7b-82 Result (11) carry-forward (already pre-registered in W7b §7 CF#1 and overlapping with W7c-CF #11 path), build chirality-resolved spectrum cache that retains H-action sub-grading (instead of L_max=10 cache uniform 8d:8d split) + 3-proxy recompute (CS, GV, η_CS) + cross-validate against W8-8 canonical pin. This upgrades §VII.AQ Level-3 anchor from canonical-import-binding to substrate-natural-binding. NOT BLOCKING for §VII.AQ Stage-2 dispatch (per §IV.4); tracked here as the structural-strengthening route. If Stage-2 PASS-AND lands at canonical-import binding (V.3) AND chirality-fidelity recompute lands subsequently, §VII.AQ accumulates BOTH binding routes and reaches the strongest Level-3 anchor form.
- **Inputs**: substrate spectrum builder (NEW; queue with substrate-physics agent); current `s84_spectrum_cache_L12_tau019.npz` (cross-check anchor); `gv_canonical_difference_FW` canonical pin; `tau_fold = 0.190` Jensen slice; (η=0, GV≠0) joint-signature spec from W7b-82.
- **Gate**: `S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE`. PASS iff `Δ_CS_natural` and `Δ_eta_CS_natural` achieve `rel_sep > 1e-3` independently AND substrate-natural GV cross-validates the W8-8 canonical pin at publication-precision floor 6.257e-10.
- **Effort**: ~1.5 wave-equivalents (spectrum builder + 3-proxy recompute + cross-validation).

V.8. **Stage-2 cross-reviewer-machinery-self-citation audit clause for `joint-theorem-promotion.md §"Audit at plan-freeze"`**
- **What**: Add a sixth audit item to `joint-theorem-promotion.md §"Audit at plan-freeze"` (currently 5 items; promote to 6): *"6. Cross-reviewer's audit machinery is NOT structurally self-authored. If reviewer R applies a parse-tree decision procedure / 4-corner classification / cohomology bridge map at the verdict-emission layer, R is NOT the sole author of that machinery. If R is the sole author, an alternate machinery route MUST be applied at the verdict layer OR a second reviewer cross-checks the machinery application."* Calibration corpus: §W7c-167 connes-ncg axis-orthogonality side audits §VII.U.2 4-corner classification (connes-authored at S87 W-2 R3) — under V.8, future Stage-2 dispatches may NOT have connes apply §VII.U.2 at the verdict-emission layer without an alternate machinery route. Status: SUGGESTION at K=1; harden to MANDATORY at K=3 calibration-corpus instances.
- **Inputs**: `joint-theorem-promotion.md §"Audit at plan-freeze"` (5-item current list); §VII.U.2 authorship trace (connes-ncg PRIMARY at S87 W-2 R3); §W7c-167 connes-ncg axis-orthogonality side audit text (lines 626-679 of W7c WP); `_joint_theorem_independent_verify_audit.py` extensibility hook.
- **Gate**: `S89-JOINT-THEOREM-AUDIT-MACHINERY-SELF-CITATION-CLAUSE-K1`. PASS iff (i) 6th audit item lands; (ii) calibration corpus row at K=1 with W7c-167 instance; (iii) audit-script extension queued for K=3 promotion.
- **Effort**: 0.4 wave-equivalents.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Procedural-floor independence in `joint-theorem-promotion.md` Stage-2 is necessary but not sufficient — substrate-input orthogonality is the structural ceiling | METHODOLOGY | NEW RULE-FILE CLAUSE PROPOSED (V.1) | All future Stage-2 verifications require ≥1 orthogonal-data observable; §VII.AH calibration corpus instance #1 carries Verdict-B caveat |
| 2 | §W7b-82 LEVEL-2 closure is OPERATIONAL at L_max=10 cache resolution under **canonical-import-binding** route; substrate-natural compute returns 0 due to cache 8d:8d uniform chirality split (cache-averaging diagnostic, not substrate-physics defect) | GEOMETRIC | PASS-VERDICT-CORRECT-WITH-DISCLOSURE-REQUIRED (V.2) | §VII.AQ Level-3 anchor block must declare cache-resolution status; chirality-fidelity recompute is structural strengthening, not Stage-2 prerequisite |
| 3 | Bayesian `log10_BF_BA = 215.56` is partially-orthogonal evidence-substantiation (different decision pipeline on shared data), not full evidence-double-counting | METHODOLOGY | INFO (Verdict-B caveat applies but full FAIL not warranted) | Sub-clause of V.1 calibration corpus; structural-output-type independence ≠ structural-input independence |
| 4 | §VII.AQ Stage-2 dispatch admissible under canonical-import binding; `S89-CS-GV-FULL-CHIRALITY-FIDELITY-RECOMPUTE` is structural strengthening, NOT prerequisite | GEOMETRIC | NO-GO ON BLOCKING; Stage-2 dispatched at canonical-import fidelity (V.3) | §VII.AQ STAGE-1-CANDIDATE → STAGE-3-PERMANENT pathway operational at S89+ |
| 5 | §VII.AH Stage-2 cross-reviewer assignment substitution at S88 W7c-167 (volovik → mack as spectral; connes → axis-orthogonality) shifted cross-axis pair from (spectral, transit) to (spectral, axis-orthogonality); connes audits §VII.U.2 he authored — structural self-citation at machinery layer | METHODOLOGY | NEW AUDIT CLAUSE PROPOSED (V.8) | Stage-2 audit at plan-freeze gains 6th item; §VII.AH S89+ re-dispatch on obs2+obs3 should restore (spectral, transit) cross-axis pair where structurally clean |
| 6 | Level-2-binding sub-class for §VII.AQ is L^{-3} HKR `L_max → ∞` envelope (Level-2-binding per cross-pillar-bridge-anatomy.md S88 W8-88); cache-resolution diagnostic is L_max=10 truncation feature, not Level-2-non-binding signal | GEOMETRIC | PASS-LEVEL-2-BINDING-DECLARED in registry text (V.2) | §VII.AQ entry passes cross-pillar-bridge-anatomy.md §"Audit at plan-freeze" item 5+6 (S88 W8-88 hardening) under canonical-import-binding declaration |
| 7 | Forward-looking third orthogonal pin axis: canonical-import-binding vs substrate-natural-binding at verdict-line `convention=` field; calibration corpus K=1 at W7b-82 | METHODOLOGY | SUGGESTION at K=1 (V.5); promotes to MANDATORY at K=3 | Future S89+ Stage-2 verdicts gain pin-suffix discipline; non-redundant with regulator-pin and SCHEMATIC-level pin |
| 8 | New calibration-corpus row at `permanent-results-registry.md §VII.U.2` clause (e): cache-resolution-vs-canonical-import as sub-class binding route within Corner I (NOT cross-corner) | METHODOLOGY | SUGGESTED REGISTRY-TEXT EDIT (V.6) | Clarifies for downstream consumers that §VII.AQ canonical-import-binding does not trigger §VII.U.2 cross-corner FORBIDDEN clause |

---

**End of W23 Synthesis.** Output covers brief Items (i)-(vi) inclusive: substrate-input-orthogonality requirement (V.1) NEW vs procedural-no-workshop-context floor (CURRENT); LEVEL-2 OPERATIONAL at canonical-import binding (Result 2) with cache-resolution caveat (V.2); registry-text amendment to §VII.AQ Level-3 anchor block (V.2 + V.6); GO-with-caveat = Verdict-B accept-but-flag-with-calibration-caveat on obs1 PASS-AND counting as instance #1 (Result 1, §V.1); definition of substrate-input-orthogonality test (V.1) + audit-machinery-self-citation clause (V.8); calibration-corpus row at §VII.U.2 clause (e) (V.6). Mandatory carry-forward §V structured to 4-field discipline per `feedback_fix-in-session-never-defer.md`. The §VII.AQ STAGE-1-CANDIDATE → STAGE-3-PERMANENT pathway is unblocked at S89+ under canonical-import-binding Stage-2 dispatch with substrate-input orthogonality enforced at one observable; the §VII.AH calibration corpus instance #1 remains pinned with Verdict-B caveat pending S89+ multi-observable orthogonality re-dispatch.
