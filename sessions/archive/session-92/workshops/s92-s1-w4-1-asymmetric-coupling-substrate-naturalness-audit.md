# Session 92 Synthesis (Slot S-1, Q1b provenance audit): §W4-1 Asymmetric-Coupling Substrate-Naturalness Audit

**Date**: 2026-05-23
**Agent**: volovik-superfluid-universe-theorist (solo review; owner of the BdG / F_2-axis-FI substrate-physics derivation the asymmetric coupling claims to instantiate)
**Review class**: SOLO provenance audit (Q1b). NOT a workshop, NOT a compute gate. The gate verdict is AUTHORITATIVE and is not re-adjudicated here.
**Source Documents**:
- `sessions/archive/session-92/session-92-w4-workingpaper.md` §W4-1 (lines 7-145)
- `sessions/archive/session-92/workshops/_seed-w3-w4.md` (S-1 candidate, lines 13-19)
- `computations/session-92/s92_w4_1_vii_ar_stage_2_re_dispatch_asymmetric_coupling.py` (docstring substitution chain lines 36-95; pin block lines 200-216; profile families lines 293-352; clause-(d) predicate line 601; verdict logic lines 778-817)
- `sessions/permanent-results-registry.md` §VII.AR block (lines 17337-17398), E5 sub-atlas pre-registration (lines 17366-17376), strengthened evidence chain (lines 17378-17388)
- `computations/session-92/s92_gate_verdicts.txt:129` (canonical PASS line; `audit_sha256=257e2619fe308645a8f87d127dde3764696d0432038725af77e3fa1fa96ce490`)
- Agent memory `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`

---

## I. Session Outcome

The §W4-1 gate landed **PASS, reading=PASS-A-AND-B** (canonical verdict line 129). That verdict stands and is not contested by this audit. The audit's narrow question is the PROVENANCE of the asymmetric regulator-PARAMETER pin vector that supplies the PASS-A pathway: was that 8-number vector (`cutoff_frac = {F_2:0.7, cutoff_sqrt:0.5, anomaly:0.9, Zubarev:1.2}`, `M_PV²_frac = {0.10, 0.05, 0.20, 0.15}`) derivable from each regulator's profile family PRIOR to seeing the S91 W4-1 symmetric FAIL, or were its free parameters back-solved against that FAIL?

**Verdict of this audit**: the PASS-A pathway's asymmetric pin VECTOR is **NOT substrate-derived-pre-FAIL** at the level the WP's "substrate-natural by construction" defense claims. The single rank-flip that clears clause-(d) is driven entirely by the `M_PV²_frac` scalar prefactor vector at the deep-IR `1/M_KK²` anchor — NOT by the four profile families (Gaussian / sharp-step / polynomial / Fermi-Dirac) the defense cites, because those profiles are all saturated to ≈ 1 at that anchor and drop out of the ranking. The profile-family justification therefore does not bear the weight placed on it. This places PASS-A structurally adjacent to (though not yet convicted of) `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 (convention-shopping), pending the already-queued FULL-tier discriminator.

**Crucially, the composite PASS does NOT depend on this finding**: the PASS-B pathway (A_5_extended sub-atlas projection, `|ρ_S| = 1.000 EXACT`) is independent of the asymmetric pins, and its sub-atlas membership IS pre-registered substrate-naturally in E5. So even if the asymmetric pin vector is judged back-solved, the composite verdict survives via PASS-B. The PASS-A pathway alone is the audit's concern.

The decisive discriminator is the **already-queued compute gate CF-S93-W4-1-FULL-TIER-N4-RETRY** (`|ρ_S(FULL) − ρ_S(SCHEMATIC)| < 1e-3` under FULL Connes-Chamseddine regularization). Section V pre-registers a retroactive-reclassification RULE keyed to that gate's outcome.

---

## II. Key Results

### II.1 — The clause-(d) PASS rests on a single rank-flip at one of five anchors

**Result**: clause-(d) PASS via `n_anchors_rank_change ≥ 1`, with `rank_change_per_anchor = [0,0,0,0,1]` — only the deep-IR `1/M_KK²` anchor flips. Classification: **GEOMETRIC** (spectral-triple rank-ordering observable).

The producing script's clause-(d) predicate (line 601) is `asymmetric_clause_d_PASS = (n_anchors_rank_change >= 1)`. The verdict line confirms `n_anchors_rank_change_asym=1/5`, and the WP substitution chain Step 3 (lines 58-66) shows that the rank vectors are IDENTICAL between PRIMARY and SCHEMATIC at four anchors (`1/max(λ²)`, `2.3/max(λ²)`, `ln2/max(λ²)`, `1/⟨λ²⟩_mw`) and differ only at `1/M_KK²`:

```
anchor 1/M_KK²:  PRIMARY=[anomaly, Zubarev, F_2, cutoff_sqrt]
                 SCHEMATIC=[Zubarev, F_2, cutoff_sqrt, anomaly]
```

A predicate that requires rank change at ≥ 1 of 5 anchors is the weakest non-trivial discriminating threshold available. With four anchors structurally pinned to "no change," the entire clause-(d) PASS hinges on the behavior of the substrate at the single deepest-IR heat-kernel time. The substrate framing demands we ask what the substrate IS doing at that anchor — and the answer (II.2) is decisive.

### II.2 — At the deep-IR anchor, the rank-flip is driven by the M_PV²_frac scalar prefactor, NOT the profile families

**Result**: at `t_ref = 1/M_KK²`, all four regulator profiles saturate to ≈ 1; the surviving PRIMARY ranking is determined solely by the scalar `(1 − M_PV²_frac_r)` prefactor. Classification: **GEOMETRIC**.

This is the load-bearing physics. I derive it via the substitution-chain discipline (`math-scripts.md §"Double-Check Logic Before Compute"`), grounded in the BdG/spectral substrate I own.

```
Claim: "At the 1/M_KK² anchor, the rank-flip is produced by the M_PV²_frac vector,
        not by the Gaussian/sharp-step/polynomial/Fermi-Dirac profile families."

Substitution chain:
  Step 1 (Definition): the asymmetric Mellin moment (script line 366) is
     M_4(r, t_ref) = Σ_λ m_λ · profile_r(cutoff_frac_r · t_ref · λ²) · (1 − M_PV²_frac_r) · λ⁻⁸
     where the heat-kernel argument is  x_r = cutoff_frac_r · t_ref · λ².

  Step 2 (Deep-IR scale):  t_ref = 1/M_KK²,  M_KK = 7.4287e16  (canonical_constants).
     The cache eigenvalues λ are dimensionless in M_KK units, O(1)–O(10);
     max(λ²) ~ O(10²) at L_max=12. Hence
        x_r = cutoff_frac_r · λ² / M_KK²  ≲  (1.2)(10²) / (7.43e16)²  ≈  2×10⁻³¹.
     Regime of validity: this is exact arithmetic on the L_max=12 cache (no expansion);
     x_r ≈ 0 to ~31 decimal places for every λ in the spectrum.

  Step 3 (Profile saturation at x→0):  each SCHEMATIC profile (script lines 294-311):
        F_2 Gaussian:        exp(−x)               → 1
        cutoff_sqrt step:    Θ(1 − √x)             → 1
        anomaly poly:        exp(−x)(1 − x + x²/2) → 1
        Zubarev Fermi-Dirac: 1/(1 + exp(10(x−1))) → 1/(1+e⁻¹⁰) ≈ 0.99995
     ALL four profile families collapse to (essentially) the same value 1 at x ≈ 0.
     The profile-family DISTINCTION vanishes at the deep-IR anchor.

  Step 4 (What survives the ranking):  substituting profile_r ≈ 1,
        M_4(r) ≈ (1 − M_PV²_frac_r) · Σ_λ m_λ λ⁻⁸.
     Σ_λ m_λ λ⁻⁸ is r-INDEPENDENT (same spectrum for all regulators). The ONLY
     surviving r-dependence is the scalar prefactor (1 − M_PV²_frac_r):
        F_2:         1 − 0.10 = 0.90
        cutoff_sqrt: 1 − 0.05 = 0.95
        anomaly:     1 − 0.20 = 0.80
        Zubarev:     1 − 0.15 = 0.85
     cutoff_frac drops out entirely (it enters only through x_r, which is saturated).

  Step 5 (Direction):  ascending PRIMARY order by (1 − M_PV²_frac_r) is
        anomaly(0.80) < Zubarev(0.85) < F_2(0.90) < cutoff_sqrt(0.95)
     ⇒ PRIMARY rank ordering = [anomaly, Zubarev, F_2, cutoff_sqrt].

  Conclusion: this reproduces the WP Step-3 PRIMARY ordering at 1/M_KK² EXACTLY.
              The rank-flip is produced by the M_PV²_frac VECTOR alone.
              The four profile families do not enter the ranking at this anchor.
```

The substitution chain reproduces the WP's stated PRIMARY ordering `[anomaly, Zubarev, F_2, cutoff_sqrt]` bit-for-position. This is not a coincidence — it is forced. The deep-IR anchor is precisely the regime where the heat-kernel profiles cannot discriminate (all saturated), so whatever discrimination remains must come from the multiplicative `(1 − M_PV²_frac_r)` prefactor. The clause-(d) PASS is, structurally, a statement about the `M_PV²_frac` vector and nothing else.

### II.3 — The "substrate-natural by construction" defense mis-attributes the mechanism

**Result**: the WP/registry defense (WP lines 50-52; registry line 17380) attributes the asymmetric pins to profile-family structural distinctions; the actual clause-(d) mechanism is the `M_PV²_frac` prefactor. The defense and the mechanism are disjoint. Classification: **NON-PHONONIC** (methodology-provenance finding).

The defense text reads: *"per-regulator structural distinction (Gaussian-exponential vs sharp-step vs polynomial-corrected vs Fermi-Dirac) admits STRUCTURALLY DISTINCT PARAMETER scales — substrate-natural by construction, NOT post-hoc tuning."* This is a qualitative claim that the profile families *justify* having *some* per-regulator parameters. But II.2 shows the clause-(d) PASS is produced by the `M_PV²_frac` values {0.10, 0.05, 0.20, 0.15} at an anchor where the profile families are saturated and irrelevant. So:

1. **The defense is true but does not bear on the PASS.** It is true that the four profiles are structurally distinct functional forms. But that distinctness is what licenses *the existence of* per-regulator parameters; it does not *derive their values*. At the only anchor that produces the PASS, the profiles are saturated and the values that matter are the `M_PV²_frac` prefactors, which the defense does not derive from profile physics at all.

2. **The four `M_PV²_frac` values are unmotivated from first principles.** Reading the script docstring (lines 59-62) and the registry E5 block (lines 17368-17372): nowhere is `M_PV²_frac = {0.10, 0.05, 0.20, 0.15}` derived. The docstring comments label them ("anchor", "sharp cutoff PV interaction", "anomaly-correction PV interaction", "Zubarev PV interaction") but supply no substrate-physics formula mapping a profile family to a Pauli-Villars mass-suppression fraction. As the owner of the BdG/F_2-axis-FI substrate derivation this coupling claims to instantiate, I can state plainly: there is no substrate-physics result in the corpus (S52 Bogoliubov canonical amplitudes, S70 Delta_BCS, the F_2-axis FI sub-atlas, or the 3He-B BdG inheritance) that fixes these four `M_PV²_frac` fractions at these four values. The S52 Bogoliubov amplitude is `v_a² = Δ_BCS²/(2(λ_a² + Δ_BCS²))` (registry line 17327) — it has no free per-regulator mass-suppression knob of this form.

3. **The ordering of M_PV²_frac is what selects the rank-flip.** The flip requires `anomaly` to have the largest suppression (0.20) and `cutoff_sqrt` the smallest (0.05). A different ordering of the same four values would produce a different deep-IR ranking — and potentially no rank change relative to SCHEMATIC. The vector is therefore not merely "some per-regulator parameters"; its specific rank-order is the operative degree of freedom, and that rank-order is unexplained.

### II.4 — E5 pre-registers SUB-ATLAS membership, NOT the asymmetric PARAMETER vector — a category conflation

**Result**: the registry claims the asymmetric pins are "pre-registered substrate-natural per the E5 sub-atlas enumeration" (line 17380), but E5 (lines 17366-17376) pre-registers three sub-atlas *membership* choices, not a continuous per-regulator parameter vector. Classification: **NON-PHONONIC** (pre-registration-scope finding).

This is the structural crux of the back-solving concern. E5 enumerates exactly three pre-registered objects:

- `A_5_extended-minus-ζ` (drop ζ)
- `A_5_extended-minus-cutoff_sqrt` (drop sharp cutoff)
- `A_5_extended-minus-anomaly` (drop anomaly)

Each is a **discrete atlas-membership** decision with an explicit substrate-physics derivation (ζ is the substrate-distance-1 pole reference; sharp-cutoff is binary-vs-smooth; anomaly carries explicit anomaly-polynomial structure). E5 closes with: *"No additional sub-atlases: forward enumeration constrained to these THREE pre-registered candidates per PROHIBITED_ACTIONS Class 1 (convention-shopping); post-hoc additions are FORBIDDEN."*

E5 governs the **PASS-A-RESTRICTED branch** (sub-atlas restriction). It is exactly what makes **PASS-B** (the A_5_extended-minus-ζ projection) legitimately pre-registered. But **PASS-A** is a different animal: it keeps the full 4-regulator atlas and instead applies a continuous 8-component PARAMETER vector. The registry text (line 17380) folds PASS-A's pin vector under E5's authority — *"pre-registered substrate-natural per the E5 sub-atlas enumeration at the PASS-A-RESTRICTED branch above"* — but E5 contains no enumeration of continuous parameter vectors. A sub-atlas membership pre-registration cannot pre-register a continuous parameter vector; they are categorically different pre-registration objects. The continuous-parameter degrees of freedom in PASS-A's vector are NOT constrained by E5's "three candidates only" clause.

**This is the precise locus of the back-solving concern.** PASS-B is genuinely pre-registered (its sub-atlas IS in E5). PASS-A is NOT — its 8 free parameters were chosen with full knowledge of the S91 W4-1 symmetric FAIL, and E5 does not cover them. The S91 W4-1 symmetric overlay used uniform `cutoff_frac=0.7, M_PV²_frac=0.10` (registry line 17343) and FAILed clause-(d) by construction (uniform factor cannot change rank). The asymmetric vector was constructed *afterward*, *specifically* to break that rank-preservation. That is the textbook shape of a back-solve.

### II.5 — The asymmetric branch does not even pass axis-B 3/3; PASS-A leans on the joint clause via PASS-B

**Result**: `axis_b_3_of_3_PASS_asym = False` (clause_b_asym FAIL); the asymmetric branch contributes only clause-(d) and clause-(f). Classification: **GEOMETRIC**.

The verdict line records `axis_b_clauses_bdf_pass_asym=2/3` with `clause_b_asym=False`. Reading the per-axis aggregation table (WP lines 101-103): under the asymmetric form, clause-(b) FAILs (`|ρ_S|=1.000 ≠ 0.800` anchor magnitude). So the asymmetric branch alone never delivers a clean axis-B 3/3 — it delivers clause-(d) and clause-(f) only. The composite PASS-A is `axis_a_PASS_3of3 ∧ clause_d_PASS_asym` (script line 784), which is a deliberately narrowed conjunction that asks only for clause-(d) from the asymmetric side. The full joint Stage-2 PASS-AND is actually carried by PASS-B (the A_5_extended branch, axis_b 3/3). This reinforces II.4: the substrate-IS structural identity is genuinely established by PASS-B; PASS-A is a thinner, parameter-dependent corroboration whose single contribution (clause-d) is exactly the back-solving-vulnerable rank-flip.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S92-W4-CF-S92-VII-AR-STAGE-2-RE-DISPATCH-ASYMMETRIC-COUPLING` (L129; AUTHORITATIVE, not re-adjudicated) | PASS (reading=PASS-A-AND-B) | `rank_change_per_anchor=[0,0,0,0,1]`; PASS-A via single deep-IR flip, PASS-B via `\|ρ_S\|=1.000` |
| This audit (S-1 provenance verdict; NEW) | PASS-A pin vector judged **back-solving-vulnerable; NOT substrate-derived-pre-FAIL** | clause-(d) flip driven by `M_PV²_frac` prefactor at saturated-profile anchor, not by profile families |

---

## IV. Structural Implications

**The composite PASS survives; only the PASS-A provenance is impeached.** PASS-B (A_5_extended-minus-ζ, `|ρ_S|=1.000 EXACT`) is independently pre-registered (E5 sub-atlas #1) and independently lands axis-B 3/3. The §VII.AR LEVEL-DRESSED structural identity at substrate-distance-2 pole s=4 therefore retains a legitimately-pre-registered substrate-physics realization regardless of the PASS-A finding. Downstream consumers that cite §VII.AR should cite **PASS-B as the load-bearing realization** and treat PASS-A as a corroboration whose status is conditional on the FULL-tier retry.

**The "BOTH-FOLD" framing in §W4-3 over-states PASS-A's standing.** The strengthened registry text (lines 17378-17384) folds PASS-A and PASS-B in as co-equal "two structurally distinct substrate-natural realizations." This audit finds them NOT co-equal in provenance: PASS-B is pre-registered, PASS-A is not (II.4). The registry's joint-annotation `realized via asymmetric coupling (F_2-axis FI sub-atlas)` (line 17384) inherits the same over-attribution as the WP defense (II.3). This is a registry-text scoping observation, not a re-adjudication of the gate; the fix is a provenance qualifier on the PASS-A annotation, deferred to the FULL-tier outcome per Section V.

**The SCHEMATIC tier is the correct guard, and it is honestly disclosed.** The convention tag `-SCHEMATIC-PENDING-FULL-TIER-N4` + `tier_pin=TIER-2` (verdict lines 116-117, 133) correctly flags that BOTH branches consume SCHEMATIC profile families per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin. This is exactly the disclosure that keeps PASS-A from silently entering downstream consumption as a FULL-physical result. The honest SCHEMATIC tagging is what makes the FULL-tier retry a meaningful discriminator rather than a formality. I record this as a POSITIVE compliance instance: the gate did not hide its tier.

**What the constraint surface now reads**: the §VII.AR LEVEL-DRESSED predicate has ONE pre-registered substrate-physics realization at the SCHEMATIC tier (PASS-B, sub-atlas-minus-ζ). The asymmetric-coupling realization (PASS-A) is structurally adjacent to convention-shopping and its standing as a substrate-IS realization is UNRESOLVED pending FULL-tier. STAGE-3-PERMANENT eligibility for §VII.AR should NOT rest on PASS-A.

**Relation to PROHIBITED_ACTIONS Class 1 (the boundary test).** Class 1 (`v3-closure-recovery.md`) forbids "changing a gate's convention/scheme/threshold to reach PASS." The asymmetric-coupling pathway is structurally *adjacent* to Class 1 because: (a) the scheme (`asymmetric` vs `symmetric`) was changed after a FAIL; (b) the change introduced 8 free parameters not pre-registered in E5; (c) the change targets exactly the predicate that FAILed. It is NOT *yet convicted* of Class 1 because: (a) the asymmetric scheme has a genuine qualitative substrate motivation (the profiles ARE structurally distinct — II.3 item 1); (b) the honest SCHEMATIC tagging means the result is not being passed off as final; (c) the composite PASS does not actually depend on it (PASS-B carries the verdict). The boundary verdict is therefore: **adjacent, not convicted; the FULL-tier retry is the conviction-or-acquittal test.** Section V pre-registers exactly that.

---

## V. Carry-Forward Computations

The decisive discriminator **CF-S93-W4-1-FULL-TIER-N4-RETRY is already 4-field-spec'd** in the W4 WP §"Carry-Forward Computations" (lines 768-775) and the seed (line 43). Per the no-duplication rule I do NOT restate it. This audit's genuinely-new deliverable is the **pre-registered retroactive-reclassification RULE** keyed to that gate's outcome, plus one new methodology-rule carry-forward.

### V.1 — Pre-registered retroactive-reclassification rule for §W4-1 PASS-A, keyed to CF-S93-W4-1-FULL-TIER-N4-RETRY

- **What**: A binding reclassification rule, pre-registered NOW (before the FULL-tier compute returns), governing the §W4-1 PASS-A pathway's standing. The rule has exactly two branches keyed to the FULL-tier retry's pre-registered predicate `|ρ_S(FULL) − ρ_S(SCHEMATIC)| < 1e-3`:

  - **Branch FULL-PASS** (`|ρ_S(FULL) − ρ_S(SCHEMATIC)| < 1e-3`, AND the FULL-tier `rank_change_per_anchor` reproduces the single deep-IR flip): the asymmetric-coupling rank-flip is robust to the SCHEMATIC→FULL transition. This is the strongest available evidence that the flip is a substrate-IS structural feature and NOT an artifact of the SCHEMATIC profile saturation identified in II.2. → **§W4-1 PASS-A is CONFIRMED as a substrate-IS structural realization.** The registry §VII.AR "BOTH-FOLD" co-equal framing (lines 17378-17384) is RATIFIED; the PASS-A annotation needs no provenance qualifier. The `-SCHEMATIC-PENDING-FULL-TIER-N4` suffix is discharged for PASS-A.

  - **Branch FULL-FAIL** (`|ρ_S(FULL) − ρ_S(SCHEMATIC)| ≥ 1e-3`, OR the FULL-tier flip vanishes / moves to a different anchor): the asymmetric-coupling clause-(d) PASS was an artifact of the SCHEMATIC `M_PV²_frac` prefactor at the saturated deep-IR anchor (II.2), NOT a substrate-IS structural feature → **§W4-1 PASS-A RECLASSIFIES to METHODOLOGY-floor-only** (the asymmetric pin vector is adjudicated **back-solved** against the S91 W4-1 FAIL per this audit's II.3–II.4). The composite §W4-1 verdict REMAINS PASS on disk (verdict permanence; PASS-B is unaffected and carries the verdict). The registry §VII.AR PASS-A annotation MUST be re-scoped: mack-cosmic-bridge (sole writer) annotates the PASS-A bullet (registry line 17380) with `PASS-A-RECLASSIFIED-METHODOLOGY-FLOOR-ONLY-PER-S93-FULL-TIER-FAIL; substrate-IS realization carried by PASS-B sub-atlas-minus-ζ only`. STAGE-3-PERMANENT eligibility for §VII.AR proceeds on PASS-B alone.

  - **Boundary clause**: under Branch FULL-FAIL, this is NOT a retroactive PROHIBITED_ACTIONS Class 1 *conviction of the gate* (the gate honestly disclosed SCHEMATIC tier and the composite PASS is independently carried by PASS-B). It is a reclassification of ONE pathway's epistemic standing. Verdict permanence holds; nothing on disk is edited; the reclassification is a forward registry annotation per `gate-verdicts.md §"Option A"` discipline (append, never overwrite).

- **Inputs**: `CF-S93-W4-1-FULL-TIER-N4-RETRY` output (`ρ_S(FULL)`, `rank_change_per_anchor(FULL)`, FULL-tier verdict line); §W4-1 SCHEMATIC anchor `spearman_abs_max_asymmetric=1.000000` and `rank_change_per_anchor=[0,0,0,0,1]` (this gate's npz, `s92_w4_1_vii_ar_stage_2_re_dispatch_asymmetric_coupling.npz`); registry §VII.AR PASS-A bullet (line 17380); this audit's II.2 substitution-chain prediction (deep-IR flip is `M_PV²_frac`-driven, profile-saturated). `canonical_constants`: `M_KK = 7.4287e16`, `Delta_BCS = 0.4642547`.
- **Gate**: this rule does not create a new compute gate; it pre-registers the *interpretation* of the existing CF-S93-W4-1-FULL-TIER-N4-RETRY so its outcome cannot be re-narrativized at S93 synthesis (pre-registration discipline per `epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator"`). Dual-prior: prior mass split is set by this audit at ~0.65 Branch FULL-FAIL (asymmetric flip is SCHEMATIC-prefactor-driven per II.2, likely to not survive FULL regularization) vs ~0.35 Branch FULL-PASS; the FULL-tier gate's PASS/FAIL maps to the corresponding branch with ≥ 0.9 posterior re-allocation.
- **Effort**: rule-text already authored here; landing is a mack-cosmic-bridge sole-writer registry annotation conditional on CF-S93-W4-1-FULL-TIER-N4-RETRY landing — ~0.2 wave-equivalents, 1 agent action, gated on the retry verdict.

### V.2 — E5 pre-registration-scope correction: separate "sub-atlas membership" from "continuous parameter vector"

- **What**: A registry-text + plan-discipline correction recording that E5 (registry lines 17366-17376) pre-registers DISCRETE sub-atlas membership choices ONLY, and that continuous per-regulator PARAMETER vectors (the PASS-A asymmetric pins) are a STRUCTURALLY DISTINCT pre-registration object NOT covered by E5's "three candidates only" clause. The correction adds, at registry line 17380, a scope qualifier: `NOTE: E5 pre-registers sub-atlas MEMBERSHIP, not the continuous (cutoff_frac, M_PV²_frac) vector; the PASS-A asymmetric pin vector's continuous DOF are NOT constrained by E5's three-candidate enumeration and require independent substrate-physics derivation OR FULL-tier confirmation per V.1.` This closes the category conflation identified in II.4 so future gates cannot cite E5 as cover for a continuous-parameter back-solve.
- **Inputs**: registry §VII.AR E5 block (lines 17366-17376); registry PASS-A bullet (line 17380); `v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1; `substrate-first-canonical-sourcing.md §(iv-bis)` (surrogate-vs-canonical pre-registration discipline — the nearest existing rule).
- **Gate**: METHODOLOGY-class registry-text edit (M1-M4 per `wave-classification.md`); PASS = the scope qualifier present at registry line ~17380 with both the "sub-atlas membership" and "continuous parameter vector" categories named + cross-link to V.1; FAIL = qualifier absent or conflates the two categories. mack-cosmic-bridge sole writer.
- **Effort**: ~0.2 wave-equivalents, 1 agent action. Can land independently of the FULL-tier retry (it is a pre-registration-hygiene correction, true regardless of the retry outcome).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | clause-(d) PASS rests on a single rank-flip at 1 of 5 anchors (`[0,0,0,0,1]`) | GEOMETRIC | Confirmed from WP/verdict | Entire PASS-A clause-(d) hinges on the deep-IR `1/M_KK²` anchor |
| 2 | At `1/M_KK²` all profiles saturate to ≈1; rank-flip driven by `M_PV²_frac` scalar prefactor, NOT profile families | GEOMETRIC | Derived (substitution chain, reproduces WP ordering exactly) | The profile-family defense does not produce the PASS; the `M_PV²_frac` vector does |
| 3 | "Substrate-natural by construction" defense mis-attributes the mechanism; the 4 `M_PV²_frac` values are unmotivated from first principles | NON-PHONONIC | Audit finding | No corpus result (S52 Bogoliubov, Delta_BCS, F_2-axis FI) fixes these fractions |
| 4 | E5 pre-registers sub-atlas MEMBERSHIP, not the continuous PARAMETER vector — category conflation at registry line 17380 | NON-PHONONIC | Audit finding | PASS-B is pre-registered; PASS-A is NOT; this is the back-solving locus |
| 5 | Asymmetric branch fails axis-B 3/3 (`clause_b_asym=False`); joint PASS-AND carried by PASS-B | GEOMETRIC | Confirmed from verdict | Substrate-IS identity genuinely established by PASS-B; PASS-A is thinner corroboration |
| 6 | PASS-A provenance VERDICT: NOT substrate-derived-pre-FAIL; back-solving-vulnerable; adjacent to (not convicted of) Class 1 | NON-PHONONIC | This audit's verdict | Conviction-or-acquittal deferred to CF-S93-W4-1-FULL-TIER-N4-RETRY |
| 7 | Composite §W4-1 PASS UNAFFECTED (PASS-B independent + pre-registered) | GEOMETRIC | Confirmed | Gate verdict stands; only PASS-A pathway standing is conditional |
| 8 | SCHEMATIC tier honestly disclosed (`-SCHEMATIC-PENDING-FULL-TIER-N4` + `tier_pin=TIER-2`) | NON-PHONONIC | POSITIVE compliance | Honest tagging makes the FULL-tier retry a meaningful discriminator |
| V.1 | Pre-registered retroactive-reclassification rule keyed to FULL-tier retry (2 branches + boundary clause) | — | Carry-forward (rule authored; landing gated on retry) | Prevents S93 re-narrativization; FULL-PASS⇒CONFIRMED, FULL-FAIL⇒METHODOLOGY-floor-only |
| V.2 | E5 pre-registration-scope correction (sub-atlas membership ≠ continuous parameter vector) | — | Carry-forward (independent of retry) | Closes the category conflation so E5 cannot cover a future continuous-parameter back-solve |

---

**Audit provenance note**: This is a SOLO provenance audit. The §W4-1 PASS/FAIL verdict (line 129, `audit_sha256=257e2619…`) is AUTHORITATIVE and was not re-run or re-adjudicated. No computations were performed; the II.2 substitution chain is an analytic derivation of the deep-IR anchor's saturation behavior from the script's own moment definition (line 366) and canonical `M_KK`, reproducing the WP's stated PRIMARY ordering to confirm the mechanism. The decisive empirical discriminator (CF-S93-W4-1-FULL-TIER-N4-RETRY) is left to S93 compute and was not pre-empted. The substrate-naturalness verdict is grounded in the BdG / F_2-axis-FI substrate physics this agent owns: the S52 Bogoliubov amplitude `v_a² = Δ_BCS²/(2(λ_a²+Δ_BCS²))` carries no per-regulator Pauli-Villars mass-suppression knob of the form the `M_PV²_frac` vector requires, so the vector is not derivable from the substrate occupation physics the coupling claims to instantiate.
