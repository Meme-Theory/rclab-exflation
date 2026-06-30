# Session 88 W22 Synthesis — §W7a-74 Rank-vs-Magnitude FAIL: Reading A vs Reading B Adjudication

**Date**: 2026-05-07
**Agent**: lizzi-spectral-functional-theorist (solo)
**Source Documents**:
- `sessions/archive/session-88/session-88-w7a-workingpaper.md` §W7a-74 (lines 622-895) + §"Carry-forward computations" (lines 1496-1532) + §"Constraint-Map Updates" (lines 1571-1581)
- `sessions/session-plan/session-88-plan-w7a.md` §W7a-74 (lines 202-267)
- `sessions/archive/session-88/workshops/_seed-w7a.md` Workshop 1 (lines 12-29) + CF-W7a-ADDITIONAL-A (lines 36-40)
- `sessions/permanent-results-registry.md` §VII.AH..§VII.AQ (slot occupancy verified via Grep — §VII.AK = S86 W-13 REG-1 Basis-Completeness Theorem 2; §VII.AQ = S88 W7b-79 STRUCTURAL-EVEN-GRADING-BLINDNESS)
- `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" (MANDATORY at K=3 per S87 W-2) + §"Per-Bulletin-per-pole Level-1 wall classification" (S88 W10-119 extension) + §"Hybrid Independence Test" (S88 W8-87 SUGGESTION K=1; MANDATORY K=3 at W4a-17)
- `.claude/rules/substrate-first-canonical-sourcing.md` §(iv) "SCHEMATIC vs full physical level pin rule" (MANDATORY at K=4, S88 W7b-83)
- `.claude/rules/epistemic-discipline.md` §"Verifier-Rubric Pre-Registration (Class 8.2)"
- `.claude/rules/joint-theorem-promotion.md` §"Stage 2"
- `computations/session-88/_w22_synthesis_subst_chain_verify.py` (machine-verified all 9 substitution chains, output appended to §III.4)

---

## I. Session Outcome

**Reading A WINS, conditional on the S89 anchor-sweep gate `S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP`** (CF-W7a-ADDITIONAL-A in seed; pre-registered below at §V.1). The §W7a-74 FAIL-composite (sign=FAIL, magnitude=FAIL, regime=VALID; |ρ_S(s=4)|_T1 = 0.800; spread_T1 = 1.011; spread_T2 = 0.895) is a structurally informative substrate-physics finding under the substrate-first canonical-sourcing LEVEL discipline, NOT a convention artifact disguised as a substrate fact — but the verdict on whether to land §VII.AR (corrected slot, see §IV) STAGE-1-CANDIDATE depends on the anchor-sweep test that pre-registration of §W7a-74 did not perform. **The substantive structural finding is Reading A AT THE ALGEBRA-INVARIANT LAYER (rank ordering is regulator-PARAMETER-dependent at s=4 substrate-distance-2 pole) — but is partially Reading B AT THE METRIC-CONVENTION LAYER (the spread-metric pre-registration admitted both `full` and `f2_only` readings; this is a Class-8.2 PRU defect more fundamental than either CF-A or CF-B).** Decision: GO on §VII.AR STAGE-1-CANDIDATE landing IF AND ONLY IF the anchor-sweep returns swap-survives-count ≥ 4 of 5 substrate-natural anchors; pin the Class-8.2 spread-metric rule extension as the highest-EVOI rule promotion (CF-α below).

---

## II. Key Results

### II.1. The §W7a-74 FAIL is a SUBSTRATE-PHYSICS finding at the algebra-INVARIANT layer (Reading A wins on adjudication question (a))

**Result**: Rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 substrate-distance-2 Mellin-cone pole is regulator-PARAMETER-dependent (NOT regulator-CLASS-dependent) when evaluated under the PRIMARY-vs-SCHEMATIC LEVEL discipline of `substrate-first-canonical-sourcing.md §(iv)`. Classification: **GEOMETRIC + PHONONIC** (Spearman rank correlation IS a substrate-IS scalar of the spectral triple's algebra-INVARIANT cell at the s=4 pole; the magnitude-ratio layer concerns regulator-dressed phononic GGE-class observables).

The adjudication of question (a) — algebra-INVARIANT vs algebra-DEPENDENT contamination — turns on the algebra-axis orthogonality K-counter (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, MANDATORY at K=3 since S87 W-2 close). Spearman's ρ_S is computed from the four moments `M_R^c(s=4) = (1/Vol_SU3_Haar) · Σ_k m_k · g_R^c(λ²_k; s)` for c ∈ {F_2, cutoff_sqrt, anomaly, Zubarev}. Each `M_R^c(s=4)` is a single sum over the spectrum eigenvalues with multiplicities — a spectrum-only functional `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`. By the K-counter clause: **spectrum-only functionals are algebra-INVARIANT**. Spearman of four such moments is a function of four algebra-INVARIANT quantities and thus inherits algebra-INVARIANCE; no state-pair functional content enters the rank computation. Reading B's worry — "absolute-parameter-anchor introduces algebra-DEPENDENT contamination via state-pair functional content" — is structurally unfounded.

The FAIL therefore does NOT come from algebra-axis cross-contamination. It comes from the LEVEL-axis: the SAME algebra-INVARIANT functional family produces a DIFFERENT ordinal structure when evaluated on the PRIMARY physical D_K spectrum (λ ∈ [0.820, 5.419], max λ² = 29.365) vs the SCHEMATIC bare SU(3) Casimir spectrum (C_2(p,q) ∈ [0.4, 12]). The ~4-OOM cross-tier rescaling (machine-verified §III.4 SUBCHAIN-8: F_2 ratio 9.38e+03, Zubarev ratio 2.40e+04, log₁₀ band [3.97, 4.38]) does not by itself flip ranks — but the regulator-class kernels' RESPONSE to the rescaled spectra does. Specifically: PV-subtraction with M_PV² = 0.1·max(spectrum) is a substantial PV mass scale on PRIMARY (M_PV² = 2.94 in physical λ² units, comparable to half the typical λ²) but a mild PV mass scale on SCHEMATIC (M_PV² = 1.2 in Casimir units, small relative to typical C_2 magnitudes). This SHIFTS Zubarev's regulator response above anomaly's response in PRIMARY only.

**Substrate framing** (per `phononic-framing.md §"IS Space, Not IN Space"`): the substrate IS the dual-spectrum structure (TT-deformed physical D_K at τ_fold=0.19 + bare SU(3) Casimir as a SCHEMATIC analog). The rank ordering IS the discrete ordinal structure intrinsic to the spectrum the regulators evaluate over. Direction of explanation: D_K eigenvalues at τ_fold → regulator-class kernel evaluation → 4-class M_R values → Spearman ρ_S → ordinal rank ordering. There is no "container" of regulator orderings; the substrate IS regulator-PARAMETER-dependent at this pole.

### II.2. The W9b-2 spread = 0.0513 is structurally distinct from §W7a-74 spread_T1 = 1.011 / spread_T2 = 0.895 — and the difference is NOT W9b-2 implementation error (Reading A wins on adjudication question (c))

**Result**: §W7a-74 §(f) hypothesizes that W9b-2's published spread = 0.0513 was computed under an `f2_only` metric variant ("zeta=SDW=Mellin machine-eps merge → ~0+noise") rather than the `full` 5-atlas range used in §W7a-74. **This hypothesis is structurally consistent with both verdict lines but does NOT defeat Reading A** — it surfaces a more fundamental Class-8.2 PRU finding (see §II.3).

Substitution chain (machine-verified §III.4 SUBCHAIN-5): `spread_T1 / 0.0513 = 19.71×`; `spread_T2 / 0.0513 = 17.45×`. Both tier-2 §W7a-74 spread values are ~17-20× wider than W9b-2's published spread. The §W7a-74 TIER-2 reproduction of W9b-2 also produces `|ρ_S| = 1.000 EXACT` (CC-ii PASS in §W7a-74 §(e)) — which means the SCHEMATIC implementation IS faithful to W9b-2 algorithm structure on the rank layer. The discrepancy must therefore be in the spread-metric definition only.

W9b-2's `s87_w9b_pole_specificity_scan.py` lines 535-557 (per §W7a-74 §(c) cite) implement the F_2-rep substitution loop. Two inequivalent metrics are inferable:
- **`full`-atlas spread**: max − min across all 5 F_2-rep substitutions (zeta, Zubarev, SDW, cutoff_sqrt, anomaly), measuring the SD-vs-non-SD class swap. §W7a-74 uses this metric.
- **`f2_only`-class spread**: max − min across only the F_2-class members (zeta, SDW, Mellin), which by W-9 RULE-3 STRUCTURALLY MERGE at machine epsilon when no PV/cutoff/anomaly representative is invited. This metric returns ~0 + float noise. W9b-2 may have defaulted to this.

**Reading B's CONDITIONALLY VALID point** (adjudication question (c)): without W9b-2 metric disambiguation, the §W7a-74 FAIL-MAGNITUDE is comparing apples (full-atlas range) to oranges (f2_only range). However, this does NOT affect Reading A's rank-ordering finding — the §W7a-74 PASS-RANK FAILED at 0.800 < 0.999 (substitution chain SUBCHAIN-1, machine-verified §III.4); the PASS-RANK criterion is Spearman magnitude only and independent of the spread metric. The W9b-2 metric ambiguity is a SEPARATE PRU defect surfaced by §W7a-74 — structurally informative, but does not invalidate Reading A.

### II.3. The Class-8.2 PRU finding (verifier-rubric structurally underspecified) is MORE FUNDAMENTAL than CF-A or CF-B (adjudication question (e))

**Result**: §W7a-74's PASS-MAGNITUDE pre-registration was structurally underspecified at S87 W9b-2 plan-freeze AND at S88 W7a-74 plan-freeze: the spread metric admitted BOTH `full` and `f2_only` readings without the verifier-rubric pre-registration discipline of `epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"`. This is a **rule-extension finding more fundamental than either Reading A's CF-B or Reading B's CF-A**.

Per Class 8.2 (`epistemic-discipline.md §"Verifier-Rubric Pre-Registration"`), every gate whose PASS/FAIL/INFO criterion involves rubric-grading of qualitative content MUST pre-register: (1) pattern set; (2) disjunction-vs-conjunction declaration; (3) negative-marker set; (4) calibration corpus pinned by SHA. The current K=2 calibration corpus (S86 W-12 V_4-vs-Z_4 + S87 W-8 R3 / S88 W2-11 V_4-Cartan-toral) does not yet include a NUMERICAL-METRIC instance. **§W7a-74 IS calibration corpus instance #3 of Class 8.2** — calibration corpus structurally extended K=2 → K=3 by this synthesis, hitting the K=3 promotion threshold per `feedback_rules-compensate-missing-structure.md`.

The structural shape of Class 8.2 instance #3 is: a numerical PASS-band threshold (`spread ≤ 0.06`) admits multiple inequivalent metric definitions (`full` vs `f2_only`) that the producing script silently selected at runtime. Like the W-12 cardinality-match-without-element-order-match defect that admitted V_4 under a "Z_4 or similar" rubric, the §W7a-74 case admits BOTH the structurally meaningful (`full` 5-atlas range) AND the structurally degenerate (`f2_only` machine-noise range) under a single bare `spread ≤ 0.06` rubric. The rubric matched on cardinality (the metric is SOME spread) without matching on metric STRUCTURE (which spread). **Forward remediation**: extend Class 8.2 K=3 calibration corpus with the §W7a-74 instance + pin convention `metric_definition_explicit_at_plan_freeze` MANDATORY for all S89+ Spearman-spread gates. This is CF-α below.

### II.4. The §VII.AK slot referenced in WP CF-B is OCCUPIED — next-free letter is §VII.AR (slot-correction; affects CF-B landing target)

**Result**: Verified via Grep over `permanent-results-registry.md` line 109 (Table) + line 15622 (entry header): `§VII.AK = Basis-Completeness Theorem 2: Methodology-Layer Entry through Substrate-Physics Provenance Protocol (S86 W-13 REG-1 — connes + lizzi joint, 2026-04-27)`. WP CF-B (line 1504) names "§VII.AK" as the landing target — this is a STALE slot reference. Subsequent slots through §VII.AQ (S88 W7b-79 STRUCTURAL-EVEN-GRADING-BLINDNESS) are also occupied. **Next-free letter: §VII.AR** (machine-verified §III.4 SUBCHAIN-6).

This is a registry-landing hygiene correction (per `registry-landing.md` next-free-letter protocol; `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` requires scanning ALL header levels before allocation). Forward S89 dispatch must use §VII.AR. The mack-cosmic-bridge sole-writer landing (per `feedback_mack-bridge-role.md` for registry rows) consumes the corrected slot identifier.

### II.5. Reading A's NEW theorem candidate is INTRA-Pillar-VII, NOT cross-pillar — Hybrid Independence Test K-counter does NOT gate registration (adjudication question (d))

**Result**: Reading A's substantive substrate finding ("rank-ordering at s=4 pole is regulator-PARAMETER-dependent under PRIMARY-vs-SCHEMATIC LEVEL discipline") is structurally an INTRA-PILLAR observation — it concerns one Pillar-VII substrate-distance pole (s=4 substrate-distance-2 Mellin-cone) evaluated across regulator-parameter classes within that pillar. It is NOT a cross-pillar bridge (substrate Pillar A ↔ laboratory Pillar B with HKR / Connes-Karoubi / K-theory boundary bridge map per `cross-pillar-bridge-anatomy.md` 5-IS-not-IN anatomy). The Hybrid Independence Test (`§"Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)"`) governs cross-pillar K-counter advancement and does NOT apply here.

The applicable rule is `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification (S88 W10-119 extension)"` which explicitly extends the 3-level structural-confidence ladder to intra-Pillar-VII Bulletin-class entries indexed by substrate-distance pole `s ∈ {3, 4, 5, ...}`. Per W10-119 §"Cross-link to cross-pillar bridges": **"Per-Bulletin-per-pole entries are distinct from cross-pillar bridges; the per-pole form is intra-pillar, so the 5-anatomy IS-not-IN elements are NOT mandatory at the same per-element granularity. The Level-1/2/3 ladder IS preserved."**

**Reading A's §VII.AR landing** therefore declares:
- **Substrate-distance pole index**: s=4 substrate-distance-2 (anomalous-residue pole; companion to the §VII.K-PROP.W10-4 ρ_∞ permanent-wall at the same pole)
- **Level-1**: rank-ordering at s=4 is regulator-PARAMETER-dependent under PRIMARY-vs-SCHEMATIC LEVEL switch (regulator-invariance status: NEITHER FI nor RD purely; this is a NEW status `LEVEL-DRESSED` distinct from the FI/RD/MIXED trichotomy of §VII.K-DUAL — see §IV structural implications). Spectrum-only family (algebra-INVARIANT per §II.1).
- **Level-2**: |ρ_S(s=4)|_PRIMARY = 0.800 ± δ (anchor-sweep envelope; δ = max-min over 5 substrate-natural t_ref anchors; pre-registered S89 envelope per CF-W7a-ADDITIONAL-A)
- **Level-3**: empirical anchor at L_max=12 = 0.800 EXACT under `t_ref_T1 = 1/max(λ²) = 0.0341` substrate-natural Compton anchor (§W7a-74 §(b) Step 3 substitution)

This level-1/2/3 declaration is conditional on the S89 anchor-sweep PASS (CF-W7a-ADDITIONAL-A); a single-anchor finding cannot saturate Level-2 envelope — Level-2 requires the empirical envelope across substrate-natural anchors. Hence the GO/NO-GO conditioning in §I.

### II.6. Substrate-natural anchor sweep — substrate-physics derivation of 5 candidates (adjudication question (b))

**Result**: Five substrate-natural choices for the heat-kernel reference time `t_ref` exist at the §W7a-74 evaluator scope. Substitution-chain derivation (per `math-scripts.md §"Double-Check Logic Before Compute"`):

**Step 1 — Definitions**:
- Heat-kernel regulator: `M_R^heat(s) = (1/Vol) Σ_k m_k · exp(-t_ref · λ²_k) / λ_k^{2n}` evaluated at pole s ↔ n=2.
- Substrate-natural anchor: a `t_ref` value derived from the substrate's intrinsic spectral quantities (eigenvalues, multiplicities, M_KK external) WITHOUT recourse to external paper provenance per `substrate-first-canonical-sourcing.md §(iv)`.

**Step 2 — Five substrate-natural choices**:
| Anchor | Definition | Substrate-physics motivation |
|:-------|:-----------|:------------------------------|
| A1 (current §W7a-74 T1) | `t_ref = 1/max(λ²)` | Inverse-UV² Compton timescale on the spectrum; mild damping (exp(-1) at λ_max). |
| A2 (alternative-1) | `t_ref = 2.3/max(λ²)` | Calibrated to match SCHEMATIC's effective top-mode suppression fraction (exp(-2.3·λ²/max(λ²))≈0.10 at max ≈ SCHEMATIC's exp(-tau_fold·max(C_2))≈0.10). Per WP §(f) remediation #2. |
| A3 (alternative-2) | `t_ref = ln(2)/max(λ²)` | Half-suppression at λ_max (exp(-ln(2))=0.5); the threshold timescale at which the heaviest mode contributes half its full weight. |
| A4 (alternative-3) | `t_ref = 1/⟨λ²⟩_mw = 1/((Σ m_k λ²_k)/(Σ m_k))` | Multiplicity-weighted mean-λ² inverse; matches the "average mode" timescale rather than the UV cutoff. |
| A5 (alternative-4) | `t_ref = 1/M_KK²-internal-units` | External-units anchor via canonical_constants.M_KK = 7.428660036284456e+16 GeV; rescaled to the spectrum's internal unit system. The only anchor that uses an EXTERNAL canonical (per substrate-first-canonical-sourcing.md §(iv) PROVENANCE discipline). |

**Step 3 — Decision rule** (machine-verified §III.4 SUBCHAIN-7):
- swap-survives-count ≥ 4 of 5 → Reading A WIN → §VII.AR STAGE-1-CANDIDATE LAND
- swap-survives-count ≤ 2 of 5 → Reading B WIN → NO-GO; §W7a-74 FAIL-RANK is convention artifact
- swap-survives-count == 3 of 5 → STAGE-1-INFO with anchor-class qualifier (intermediate; neither READING wins outright)

**Step 4 — Direction**: this is the S89 gate `S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP` pre-registered below at §V.1. Unless and until that gate executes, neither Reading A nor Reading B is decisively confirmed; the GO/NO-GO on §VII.AR landing is structurally CONDITIONAL.

---

## III. Gate Verdicts

### III.1. Workshop verdict (§W7a-74 source FAIL was not re-adjudicated; the §W7a-74 verdict is taken as authoritative per task rules)

| Gate | Verdict (from source) | Decisive Number |
|:-----|:----------------------|:----------------|
| §W7a-74 (S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR) | FAIL composite (sign=FAIL, magnitude=FAIL, regime=VALID) | `rho_T1=-0.800; rho_T2=-1.000; spread_T1=1.011; spread_T2=0.895` (audit_sha256=`5d7e448b7da710deb1408fbd8dd621007ff976cedc9f0fdf2a4f42c52d075378`) |
| §W7a-76 (mechanical PRE-REG-INC closure) | FAIL (plan §372 anticipated) | `PRE-REG-INC_blocked_by_W7a-74_FAIL-RANK_FAIL-MAGNITUDE` (audit_sha256=`4025d90c563101b0...`) |
| §W7a-77 (chained mechanical PRE-REG-INC closure) | FAIL (plan §401 anticipated) | `PRE-REG-INC_blocked_by_W7a-76_FAIL_AND_W7a-74_FAIL-RANK` (audit_sha256=`352350fe0a05b58d...`) |
| W9b-2 (S87 source baseline) | PASS (SCHEMATIC level only) | `|ρ_S(s=4)|=1.000 EXACT, cross-regulator spread = 0.0513` (audit_sha256=`30815fae...`) — NOW SCOPED to "SCHEMATIC-level under `_spectral_action_regulators.py` Casimir-fraction parameters" per §W7a-74 §(f) closing of the corridor "rank-1 EXACT at s=4 is FI across LEVEL" |

### III.2. Workshop adjudication of 5 questions (a)-(e)

This synthesis adjudicates the 5 questions from `_seed-w7a.md` Workshop 1 and produces the Workshop's STRUCTURAL VERDICT. The §W7a-74 numerical FAIL is taken as authoritative; the workshop's job is to interpret it, not re-compute it.

| Question | Adjudication | Reading A vs B |
|:---------|:-------------|:---------------|
| (a) Algebra-INVARIANT vs DEPENDENT contamination at s=4? | **ALGEBRA-INVARIANT.** Spearman of 4 spectrum-only moments inherits algebra-INVARIANCE per K-counter clause (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3). State-pair functionals do NOT enter the rank computation. | **Reading A wins.** |
| (b) Substrate-natural anchor sweep — does an alternative anchor restore SCHEMATIC ordering? | **PRE-REGISTERED for S89.** 5 substrate-natural anchors derived (§II.6). Decision rule pre-registered in §V.1 below. **Reading A vs Reading B verdict CONDITIONAL** on swap-survives-count from S89 sweep. | **CONDITIONAL** |
| (c) W9b-2 spread = 0.0513 metric disambiguation? | **`f2_only` vs `full` ambiguity is structurally consistent with both verdict lines** (§II.2). W9b-2 PASS rank-layer is FAITHFUL (CC-i + CC-ii §W7a-74 PASS); spread-metric is a SEPARATE PRU defect (Class 8.2). Does NOT defeat Reading A's rank-layer finding. | **Reading A wins on rank-layer; Class-8.2 PRU defect surfaces independently.** |
| (d) STAGE-1-CANDIDATE qualification + 5-IS-not-IN anatomy + 3-level ladder? | **INTRA-Pillar-VII, NOT cross-pillar.** Per W10-119 extension §"Per-Bulletin-per-pole Level-1 wall classification": 5-anatomy NOT mandatory at per-element granularity; **Level-1/2/3 ladder IS preserved** (§II.5). Reading A's claim qualifies as Bulletin-class STAGE-1-CANDIDATE conditional on Level-2 envelope (anchor-sweep) PASS. | **Reading A wins on qualification; Level-2 envelope is anchor-sweep dependent.** |
| (e) Class 8.2 verifier-rubric pre-registration defect MORE fundamental than CF-A or CF-B? | **YES.** The spread-metric admitted both `full` and `f2_only` readings without rubric pre-registration (Class 8.2 instance #3, hits K=3 promotion threshold). This is a rule-extension finding orthogonal to Reading A vs B; it surfaces from §W7a-74 regardless of which reading wins. **Highest-EVOI rule-promotion finding from this workshop.** | **Both readings concur on Class 8.2 promotion.** |

### III.3. Verifier rubric (this workshop's own rubric, pre-registered at-write per Class 8.2)

The workshop's STRUCTURAL VERDICT (§I above + §IV.3 below) is itself a rubric-graded outcome. Per Class 8.2 self-application:
- **Pattern set**: `Reading A WIN` ∈ {(a)=ALGEBRA-INVARIANT, (b)=CONDITIONAL on S89 sweep, (c)=rank-layer wins, (d)=qualifies INTRA-Pillar, (e)=concurrent on Class 8.2}; `Reading B WIN` ∈ {(a)=algebra-DEPENDENT contamination, (b)=anchor restores SCHEMATIC, (c)=W9b-2 metric defeats §W7a-74 comparison, (d)=does not qualify, (e)=concurrent}.
- **Conjunction**: ALL 5 questions must align for monolithic Reading A or Reading B WIN; the actual outcome is **Reading A wins (a), CONDITIONAL on S89 (b), Reading A wins (c) on rank-layer + Class 8.2 surfaces (e), Reading A qualifies (d) under W10-119 ladder, both concur (e)**. This is **partial Reading A WIN with Class 8.2 PRU promotion as orthogonal finding** — categorically distinct from monolithic Reading A or Reading B.
- **Negative markers**: a verdict claiming "monolithic Reading A WIN, §VII.AR landing UNCONDITIONAL" would be a Class 8.2 violation (premature landing without anchor-sweep envelope). Avoided.
- **Calibration corpus**: this is calibration corpus instance #1 for cross-workshop adjudication-rubric pre-registration (forward-looking from this synthesis).

### III.4. Substitution chain machine-verification log

All 9 chains verified at `computations/session-88/_w22_synthesis_subst_chain_verify.py` (output reproduced from the run):

```
SUBCHAIN-1 PASS-RANK: T1>=0.999 = False; T2>=0.999 = True; conj = False; verdict = FAIL-RANK
SUBCHAIN-2 PASS-MAG:  T1<=0.06 = False; T2<=0.06 = False; conj = False; verdict = FAIL-MAG
SUBCHAIN-3 composite: sign=FAIL mag=FAIL regime=VALID -> FAIL
SUBCHAIN-4 spread_T1/spread_T2 = 1.1296   (T1 LARGER; factor>1 ⇒ T1 spread > T2 spread)
SUBCHAIN-5 spread_T1/0.0513 = 19.71x; spread_T2/0.0513 = 17.45x
            (T1 ~20× and T2 ~17× wider than W9b-2 published 0.0513)
SUBCHAIN-6 occupied slots: AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ
            Next-free §VII.A_ letter: §VII.AR
            WP CF-B "§VII.AK" reference is STALE.
SUBCHAIN-7 anchor-sweep decision rule (pre-reg N=5 substrate-natural anchors):
            swap_survives ≥ 4 → Reading A WIN → §VII.AR STAGE-1-CANDIDATE LAND
            swap_survives ≤ 2 → Reading B WIN → NO-GO; FAIL-RANK is convention artifact
            swap_survives == 3 → STAGE-1-INFO with anchor-class qualifier
SUBCHAIN-8 cross-tier ratios: F_2 = 9.380e+03 (log10 = 3.972); Zubarev = 2.401e+04 (log10 = 4.380)
            Both ratios in band [10^3.78, 10^4.38] = ~4 OOM rescaling.
SUBCHAIN-9 HIT applicability: Reading A is INTRA-Pillar-VII regulator-parameter scan.
            HIT K-counter does NOT gate registration; per-Bulletin-per-pole Level-1/2/3 ladder DOES apply.
            §W10-119 W3-extension permits intra-Pillar-VII entries with 3-level ladder.
```

---

## IV. Structural Implications

### IV.1. Constraint-map updates (workshop output)

| Date | Mechanism / corridor | Prior state | New state | Reason |
|:-----|:---------------------|:------------|:----------|:-------|
| 2026-05-07 | "rank-1 EXACT at s=4 is FI across LEVEL" (W9b-2 substrate-IS reading) | OPEN, assumed via W9b-2 SCHEMATIC PASS | CLOSED-FALSIFIED at SCHEMATIC layer; OPEN-CONDITIONAL at PRIMARY-LEVEL pending S89 anchor-sweep | §W7a-74 §(f) FAIL-RANK + Reading A on (a) + S89 anchor-sweep gate pre-registered |
| 2026-05-07 | "rank-ordering at s=4 is regulator-CLASS-dependent only" | ASSUMED at W9b-2 plan-freeze | CLOSED-FALSIFIED — actual structure is regulator-PARAMETER-dependent (anomaly ↔ Zubarev pair-swap under physical-mass-scale anchor) | §W7a-74 §(d) per-class M_R table + §(b) Step-3 substitution |
| 2026-05-07 | §VII.AK as W7a-74 successor landing target | NAMED in WP CF-B (line 1504) | CORRECTED to §VII.AR (slot-occupancy verified via Grep) | §II.4; SUBCHAIN-6 |
| 2026-05-07 | Class 8.2 (verifier-rubric pre-registration) calibration corpus | K=2 (SUGGESTION pending K=3) | K=3 — §W7a-74 surfaces as instance #3 (numerical-metric class) | §II.3; CF-α below |
| 2026-05-07 | §VII.K-DUAL FI/RD/MIXED trichotomy (S82 R2-B) | 3-class (FI / RD / MIXED) | 4-class proposal: FI / RD / MIXED / **LEVEL-DRESSED** (new class for regulator-PARAMETER-dependent observables under PRIMARY-vs-SCHEMATIC LEVEL discipline) | §II.5 + §IV.2 below; CF-γ below |
| 2026-05-07 | §VII.AH Joint F_2-Class Path-(c) Theorem (Stage-2) | STAGE-1-CANDIDATE; Stage-2 INFO at §W7a-71 | UNCHANGED by this workshop (§W7a-71 is a separate gate) | non-overlap with §W7a-74 source |

### IV.2. The proposed 4th class "LEVEL-DRESSED" (extending §VII.K-DUAL trichotomy)

The §VII.K-DUAL FI / RD / MIXED classification (S82 R2-B, lizzi-signature) was developed BEFORE the substrate-first canonical-sourcing.md §(iv) PRIMARY-vs-SCHEMATIC LEVEL discipline was MANDATORY. §W7a-74's finding does not fit cleanly into any of the 3 existing classes:
- **FI** (FUNCTIONAL-INDEPENDENT): the rank ordering would be the same in both PRIMARY and SCHEMATIC. **§W7a-74 falsifies this** for s=4.
- **RD** (REGULATOR-DRESSED): the observable changes magnitude across regulator scheme but rank is preserved. **§W7a-74 partially fits** but the rank changes too — RD is too weak.
- **MIXED**: some sub-observable is FI, others are RD. **§W7a-74 fits if** spread metric is RD and rank is FI — but rank is NOT FI here at the LEVEL axis.

The 4th class **LEVEL-DRESSED** captures the §W7a-74 phenomenon: an algebra-INVARIANT spectrum-only functional family whose ordinal output depends on the substrate-LEVEL it is evaluated over (PRIMARY physical D_K spectrum vs SCHEMATIC bare Casimir spectrum). LEVEL-DRESSED is structurally distinct from REGULATOR-DRESSED because the regulator-CLASS membership is unchanged; only the substrate spectrum is rescaled. The class identifies observables whose SCHEMATIC-level results do not propagate to PRIMARY-level structural facts.

CF-γ below pre-registers the §VII.K-DUAL extension with this 4th class. This is a more structurally informative outcome than a single §VII.AR landing because it reorganizes the FI/SD/MIXED taxonomy to incorporate the LEVEL axis discipline.

### IV.3. Workshop STRUCTURAL VERDICT — 5 components

Per Workshop 1's pre-registered output requirements (`_seed-w7a.md` line 28):

#### (i) Reading A vs Reading B classification of §W7a-74 FAIL

**Reading A WINS at the algebra-INVARIANT layer (a) and at the rank-layer reading (c).** Reading B is structurally unfounded on (a) and (c). Reading B is **CONDITIONALLY VALID on (b)** pending S89 anchor-sweep — neither reading is decisively confirmed without that gate. Both readings CONCUR on (d) qualification (INTRA-Pillar-VII per W10-119) and on (e) Class 8.2 promotion. **Composite classification**: PARTIAL READING A WIN + CLASS-8.2 RULE-EXTENSION FINDING (orthogonal). NOT monolithic Reading A; NOT monolithic Reading B.

#### (ii) Substrate-natural-anchor sweep specification (pre-registered S89 gate)

`S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP` — full 4-field spec at §V.1 below. Pre-registered N=5 substrate-natural anchors {1/max(λ²), 2.3/max(λ²), ln(2)/max(λ²), 1/⟨λ²⟩_mw, 1/M_KK²-internal} on §W7a-74 PRIMARY evaluator with FIXED `cutoff_frac=0.7`, `M_PV²_frac=0.1`, `Vol_SU3_Haar`. Decision rule: swap-survives-count ≥4/5 → Reading A WIN; ≤2/5 → Reading B WIN; ==3/5 → INFO. Verdict-line `convention=heat-kernel-anchor-sweep-PRIMARY` per `regulator-convention-lockdown.md` discipline.

#### (iii) GO / NO-GO on §VII.AR (NOT §VII.AK; corrected) STAGE-1-CANDIDATE landing

**CONDITIONAL GO**: §VII.AR landing CONDITIONAL on `S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP` PASS-Reading-A (swap-survives-count ≥4/5). The §VII.AR registry text is **DRAFTED in §V.2 below as STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP** so the registry-landing pipeline can land an INFO marker today and promote to PASS after S89. **NO-GO on monolithic UNCONDITIONAL landing** — the substantive substrate finding requires Level-2 envelope saturation across substrate-natural anchors per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` Level-2 algebraic envelope clause.

#### (iv) §W7a-74 spread-metric convention disambiguation (rule extension)

Pre-register MANDATORY `spread_metric_definition` PIN at all S89+ Spearman-spread gates: `spread_metric_definition ∈ {full_atlas, f2_only_class}` declared in plan-block PIN MAP. Audit script `_source_reconciliation_audit.py` extension Class-(g) `SPEARMAN-SPREAD-METRIC-UNDECLARED` flag at plan-freeze. CF-α below pins this rule extension. Class-8.2 calibration corpus instance #3 + audit-script extension queue at `S89-W7a-74-CLASS-8.2-CALIBRATION-EXTEND` (CF-α gate).

#### (v) §VII.AR 5-IS-not-IN anatomy + 3-level structural-confidence ladder declaration

Per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (W10-119 extension): 5-anatomy IS-not-IN granularity NOT mandatory for intra-Pillar-VII entries; Level-1/2/3 ladder IS mandatory. Declaration:

- **Substrate-distance pole index**: s=4 substrate-distance-2 (anomalous-residue pole; companion to §VII.K-PROP.W10-4 ρ_∞ permanent-wall at the same pole)
- **Level-1 (cohomology-class identity / regulator-invariance status)**: rank ordering at s=4 is regulator-PARAMETER-dependent under PRIMARY-vs-SCHEMATIC LEVEL switch; algebra-INVARIANT spectrum-only family per K-counter MANDATORY clause; structural identity = LEVEL-DRESSED (NEW 4th class proposed in CF-γ; supersedes FI/RD/MIXED for this observable)
- **Level-2 (algebraic envelope)**: |ρ_S(s=4)|_PRIMARY = 0.800 ± δ across substrate-natural t_ref anchors; δ TBD by S89 anchor-sweep PASS/INFO/FAIL; pole-specific α(s=4) Casimir-bound argument via Friedrich-Bär saturation theorem (`math-scripts.md §"D_K Block-Diagonality Pre-Check"`) on the L_max=12 block-diagonal cache (`s84_spectrum_cache_L12_tau019.npz`; matches §VII.U.1 / §VII.U.2 canonical L_max)
- **Level-3 (empirical anchor)**: at L_max=12, t_ref_T1 = 1/max(λ²) = 0.0341, M_PV²_frac = 0.1, cutoff_frac = 0.7: rho_S = -0.800 EXACT, spread_T1 = 1.011 (range [-0.800, +0.211]) per §W7a-74 §(d) reproduced at machine precision
- **Cross-link to §VII.K-DUAL** (CF-γ): proposed 4th class LEVEL-DRESSED extends FI/RD/MIXED to incorporate LEVEL axis

This matches the per-Bulletin-per-pole Level-1/2/3 schema pinned at `cross-pillar-bridge-anatomy.md §"Calibration corpus (post-S88 W10-119)"` table (calibration corpus instances §VII.K-PROP.W10-4 at s=4 + §VII.U.1 at s=3 + §VII.AR at s=4 → corpus K=3 hits MANDATORY threshold on the per-Bulletin-per-pole sub-clause; CF-δ pre-registers this).

### IV.4. Slot collision warning — §W7a-76 mechanical-closure remains valid; §VII.AJ.1 / §VII.AJ.2 do NOT land

Per §W7a-76 mechanical-closure (audit_sha256=`4025d90c563101b0...`), the original §VII.AJ.1 RANK-ORDER and §VII.AJ.2 MAGNITUDE-RATIO STAGE-1-CANDIDATE landings are BLOCKED because §W7a-74 returned FAIL-RANK + FAIL-MAGNITUDE. Reading A's CF-B (§II.5) lands at §VII.AR (NOT §VII.AJ — the §VII.AJ slot was reserved for W-12 Mellin-Moment Identities and the partition-stability sub-slot is the only S87+ landing there). **§VII.AJ.1 and §VII.AJ.2 paths remain CLOSED**; §VII.AR is a **DIFFERENT theorem statement** (regulator-PARAMETER-dependence at s=4 LEVEL-DRESSED, not the original "rank-ordering at s=4 is FI" reading). This distinction matters for downstream cross-pole / cross-corner consumers and for CF-D §VII.AH amendment readers.

### IV.5. The §W7a-74 finding STRENGTHENS the §VII.K-PROP.W10-4 ρ_∞ permanent-wall

§VII.K-PROP.W10-4 (S87 W10-2 simple-pole fit on the s=4 substrate-distance-2 pole) registers ρ_∞ structurally IRRATIONAL per CC2 PROVEN; PERMANENT-WALL classification (per `cross-pillar-bridge-anatomy.md §"Calibration corpus (post-S88 W10-119)"` table). The §W7a-74 LEVEL-DRESSED finding is COMPATIBLE with the W10-4 permanent-wall: ρ_∞ irrationality is an asymptotic L_max → ∞ property of the Mellin-cone substrate-distance-2 residue itself, NOT a property of the rank ordering across regulator-CLASS at finite L_max. The two observables live at the same pole (s=4) but at structurally distinct cohomology layers (W10-4 = single-class residue limit; §VII.AR = cross-class rank ordering at finite L_max=12). **Joint reading**: the s=4 pole has TWO Bulletin-class structural facts — irrational ρ_∞ asymptotic (W10-4) AND LEVEL-DRESSED rank ordering at finite L_max (§VII.AR). Both contribute to the algebraic envelope of any future cross-pillar bridge that consumes the s=4 pole substrate-distance-2 residue.

---

## V. Carry-Forward Computations

V.1. **CF-W7a-ADDITIONAL-A — Substrate-natural heat-kernel anchor sweep (PRE-REQUISITE to CF-B; HIGH-EVOI)**
   - **What**: Scan `t_ref ∈ {1/max(λ²), 2.3/max(λ²), ln(2)/max(λ²), 1/⟨λ²⟩_mw, 1/M_KK²-internal-units}` on §W7a-74 PRIMARY evaluator with FIXED `cutoff_frac=0.7`, `M_PV²_frac=0.1`, `Vol_SU3_Haar` normalization. For each anchor, recompute (i) per-class M_R(s=4); (ii) ρ_S(s=4); (iii) cross-regulator spread; (iv) rank vector. Emit decision-tree output: "anomaly↔Zubarev pair-swap survives N of 5 anchors". Decision rule: N≥4 → Reading A WIN → §VII.AR STAGE-1-CANDIDATE LAND; N≤2 → Reading B WIN → NO-GO; N==3 → STAGE-1-INFO with anchor-class qualifier.
   - **Inputs**: §W7a-74 producing script `computations/session-88/s88_w7a_rank_vs_magnitude_layer_discriminator.py` (470 LoC) reused with anchor-loop wrapper; spectrum cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz`; canonical_constants.py `M_KK = 7.428660036284456e+16`; `Vol_SU3_Haar = 1349.7399583199533` (S44 corrected); §W7a-74 verdict audit_sha256=`5d7e448b7da710de...` (Input-SHA pin).
   - **Gate**: `S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP` with PASS criterion (a) anchor-sweep covers ≥5 substrate-natural choices; (b) verdict-table-per-anchor reports |ρ_S|_T1 + spread_T1 + rank-vector for each; (c) decision-tree output reported; (d) Reading A WIN iff N≥4/5; Reading B WIN iff N≤2/5; intermediate routes to STAGE-1-INFO. Convention tag: `convention=heat-kernel-anchor-sweep-PRIMARY` per `regulator-convention-lockdown.md` + `level=PRIMARY` per `substrate-first-canonical-sourcing.md §(iv)`. Verdict-line `value=anchor1=<rank_vec>;...;anchor5=<rank_vec>;swap_survives_count=<N>;reading=A|B|INFO`.
   - **Effort**: 0.4 wave-equivalents (5 anchor evaluator runs × ~0.05 each + decision-tree report + verdict-line emission; lizzi-spectral-functional-theorist solo).

V.2. **CF-B (CORRECTED) — §VII.AR (NOT §VII.AK) STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP landing (HIGHER-EVOI)**
   - **What**: Land §VII.AR STAGE-1-CANDIDATE-PENDING-ANCHOR-SWEEP at next-free letter (Grep-verified §II.4) with theorem statement: "Rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 substrate-distance-2 Mellin-cone pole is REGULATOR-PARAMETER-dependent (NOT regulator-CLASS-dependent) under the PRIMARY-vs-SCHEMATIC LEVEL discipline of `substrate-first-canonical-sourcing.md §(iv)`. The substantive ordering F_2 > cutoff_sqrt > Zubarev > anomaly holds in PRIMARY (physical D_K spectrum at τ_fold=0.19, L_max=12); the substantive ordering F_2 > cutoff_sqrt > anomaly > Zubarev holds in SCHEMATIC (bare SU(3) Casimir spectrum). Anomaly ↔ Zubarev pair-swap is the structural difference between the two LEVELS." Per-Bulletin-per-pole Level-1/2/3 ladder declaration per §IV.3(v) above.
   - **Inputs**: §W7a-74 verdict line audit_sha256=`5d7e448b7da710de...` (Input-SHA pin); §W7a-74 NPZ data `computations/session-88/s88_w7a_rank_vs_magnitude_layer_discriminator.npz` (per-class M_R + ρ_S + spread arrays); CF-α (`S89-W7a-74-HEAT-KERNEL-ANCHOR-SWEEP`) verdict-line for Level-2 envelope δ pin; §VII.K-PROP.W10-4 cross-link for s=4 pole companion structure.
   - **Gate**: `S89-VII-AR-STAGE-1-CANDIDATE-LAND` with PASS criterion (per `joint-theorem-promotion.md` 4-stage pathway): (a) registry-row appended at §VII.AR (not §VII.AK; not §VII.AJ); (b) Level-1/2/3 ladder declared per W10-119 extension; (c) Level-2 envelope δ pinned from CF-W7a-ADDITIONAL-A verdict OR INFO if anchor-sweep INFO; (d) STAGE-1-CANDIDATE tag explicit; (e) anchor structure SOURCE-DOUBLE-CITE-CO-PRIMARY (§W7a-74 verdict + CF-W7a-ADDITIONAL-A verdict) per `registry-landing.md`; (f) mack-cosmic-bridge sole-writer commit per `feedback_mack-bridge-role.md`. PASS conditional on CF-W7a-ADDITIONAL-A returning Reading A WIN (swap-survives ≥4/5); INFO conditional on Reading B WIN OR INFO; NO-GO on monolithic UNCONDITIONAL landing.
   - **Effort**: 0.5 wave-equivalents (registry-entry text + Sage-exact Spearman derivation + per-pole Level-1/2/3 declaration + mack-writer landing).

V.3. **CF-α — Class 8.2 calibration corpus extension to K=3 + Spearman-spread metric MANDATORY pin (HIGHEST-EVOI rule promotion; PARALLEL to CF-B)**
   - **What**: Extend `epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"` calibration corpus from K=2 to K=3 by adding §W7a-74 instance #3 (numerical-metric class — `spread ≤ 0.06` rubric admitted both `full` and `f2_only` definitions). Pin MANDATORY pre-registration discipline: every gate whose PASS-band involves a Spearman cross-regulator spread metric MUST declare `spread_metric_definition ∈ {full_atlas, f2_only_class}` in plan-block PIN MAP. Add `_source_reconciliation_audit.py` Class-(g) `SPEARMAN-SPREAD-METRIC-UNDECLARED` flag at plan-freeze with HARD-HALT remediation routing. K=3 ≥ K_promotion=3 ⇒ Class 8.2 sub-clause status promoted from SUGGESTION to MANDATORY at plan-freeze for all S89+ gates.
   - **Inputs**: §W7a-74 verdict line audit_sha256=`5d7e448b7da710de...`; W9b-2 verdict line audit_sha256=`30815fae...` (the comparator that surfaced the metric ambiguity); `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` current K=2 corpus (W-12 V_4-vs-Z_4 + W-8 R3 / W2-11 V_4-Cartan-toral); `_source_reconciliation_audit.py` current Class-(a)-(f) taxonomy.
   - **Gate**: `S89-W7a-74-CLASS-8.2-CALIBRATION-EXTEND` with PASS criterion METHODOLOGY-class M1∧M2∧M3∧M4 per `wave-classification.md`: (a) rule-file diff lands K=3 corpus row in `epistemic-discipline.md`; (b) `_source_reconciliation_audit.py` Class-(g) flag added with regex `(?i)\b(spread|range)\b.*(?:0\.06|≤\s*0\.0\d+).*` requiring `spread_metric_definition` declaration in adjacent plan-block; (c) allowlist row `S89-W7a-74-CLASS-8.2-CALIBRATION-EXTEND` added to `methodology-wave-allowlist.md` at plan-freeze; (d) audit-script binary-classifier validation on K=3 corpus (W-12 + W-8R3/W2-11 + §W7a-74 all classify correctly); (e) calibration-instance row in `sessions/framework/registry/pru-class-corpus.md §1` (Class 8.2 calibration corpus).
   - **Effort**: 0.3 wave-equivalents (rule-file edit + audit-script regex + allowlist append + verdict-line emission; lizzi-spectral-functional-theorist orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class path).

V.4. **CF-γ — §VII.K-DUAL trichotomy extension to 4-class FI/RD/MIXED/LEVEL-DRESSED (joint with §VII.AR landing)**
   - **What**: Extend §VII.K-DUAL FI/RD/MIXED classification (S82 R2-B; lizzi-signature) with NEW 4th class **LEVEL-DRESSED** capturing observables whose algebra-INVARIANT spectrum-only ordinal output depends on the substrate-LEVEL (PRIMARY vs SCHEMATIC) per `substrate-first-canonical-sourcing.md §(iv)` LEVEL discipline. Definition: an observable O is LEVEL-DRESSED iff (a) O is a spectrum-only functional `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` (algebra-INVARIANT per K-counter); (b) the regulator-CLASS membership of O is unchanged across LEVEL switch; (c) the ordinal output of O changes between PRIMARY and SCHEMATIC level evaluations (i.e., not Spearman-rank-invariant). Calibration corpus K=1 instance: §W7a-74 / §VII.AR rank ordering at s=4. Forward enforcement: future regulator-class-DUAL rows in `permanent-results-registry.md §VII.K-DUAL` may carry tag {FI, RD, MIXED, LEVEL-DRESSED} with explicit declaration of the LEVEL-axis evaluation per `substrate-first-canonical-sourcing.md §(iv)`.
   - **Inputs**: `permanent-results-registry.md §VII.K-DUAL` current 3-class table; §W7a-74 finding (CF-B); `substrate-first-canonical-sourcing.md §(iv)` current MANDATORY status (K=4, S88 W7b-83); algebra-axis K-counter MANDATORY clause.
   - **Gate**: `S89-VII-K-DUAL-LEVEL-DRESSED-EXTENSION` with PASS criterion METHODOLOGY-class: (a) §VII.K-DUAL row lands NEW 4th class LEVEL-DRESSED definition + 3-criterion definition (a)-(c) above; (b) calibration corpus K=1 instance §VII.AR cross-linked; (c) per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold, status SUGGESTION at K=1 — promotes to MANDATORY when K=3 distinct LEVEL-DRESSED instances accumulate. Status SUGGESTION until then.
   - **Effort**: 0.2 wave-equivalents (registry-entry text + cross-link + status pin; lizzi-spectral-functional-theorist orchestrator-direct-write).

V.5. **CF-δ — Per-Bulletin-per-pole Level-1/2/3 calibration corpus extension to K=3 (W10-119 extension promotion)**
   - **What**: §VII.AR landing (CF-B) extends `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification (S88 W10-119 extension)"` calibration corpus from K=2 (§VII.K-PROP.W10-4 ρ_∞ at s=4 + §VII.U.1 Mellin-Dirichlet at s=3) to K=3 by adding §VII.AR LEVEL-DRESSED rank-ordering at s=4. K=3 ≥ K_promotion=3 ⇒ sub-clause status SUGGESTION → MANDATORY at plan-freeze for all S89+ Pillar-VII Bulletin-class registry entries.
   - **Inputs**: §VII.AR registry text (CF-B); §VII.K-PROP.W10-4 + §VII.U.1 current calibration corpus rows; `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` current SUGGESTION status table.
   - **Gate**: `S89-W10-119-CALIBRATION-CORPUS-K3-PROMOTE` with PASS criterion METHODOLOGY-class: (a) calibration corpus row §VII.AR added to W10-119 extension table; (b) status flip SUGGESTION → MANDATORY in rule body; (c) audit script `_cross_pillar_bridge_audit.py` extended with per-pole Level-1/2/3 declaration check (existing 4-item audit + items 5-8 for per-pole sub-section); (d) allowlist row added per `methodology-wave-allowlist.md`.
   - **Effort**: 0.2 wave-equivalents (rule-file edit + audit-script extension + allowlist append; chained on CF-B PASS).

V.6. **CF-ε — Sage-exact Spearman ρ_S(s=4) recomputation across 5 substrate-natural anchors (TOLERANCE-RIGOROUS support for CF-W7a-ADDITIONAL-A)**
   - **What**: For each of the 5 substrate-natural anchors in CF-W7a-ADDITIONAL-A, compute the M_R(s=4) values and Spearman ρ_S using Sage QQ exact arithmetic (per `regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW Regulator-Class Values"` discipline extended to ρ_S evaluations). The float arithmetic in CF-W7a-ADDITIONAL-A may produce float-ambiguous rank ties at the rank-1/rank-2 boundary at certain anchors; Sage exact eliminates the ambiguity. Cross-check that the float verdict (Reading A WIN / Reading B WIN / INFO) does not flip under exact arithmetic.
   - **Inputs**: CF-W7a-ADDITIONAL-A NPZ output `computations/session-89/s89_w7a_74_heat_kernel_anchor_sweep.npz` (per-anchor M_R + ρ_S arrays); `s84_spectrum_cache_L12_tau019.npz` eigenvalues; Sage MCP `sage_eval` for rational-arithmetic Spearman.
   - **Gate**: `S89-W7a-74-ANCHOR-SWEEP-SAGE-EXACT-CROSS-CHECK` with PASS criterion: (a) all 5 anchors recomputed in Sage QQ; (b) per-anchor exact ρ_S compared to float; (c) tolerance |ρ_S_exact - ρ_S_float| < 1e-9; (d) Reading A/B/INFO verdict UNCHANGED under exact arithmetic. FAIL if verdict flips between float and exact (would indicate float-rank-tie boundary near an anchor; remediation: report the boundary and refine the decision rule).
   - **Effort**: 0.3 wave-equivalents (Sage MCP loop over 5 anchors + cross-check report).

V.7. **CF-ζ — Update lizzi-spectral-functional-theorist agent-memory `permanent_theorems.md` with §VII.AR LEVEL-DRESSED finding (post-S89 PASS)**
   - **What**: Conditional on CF-B §VII.AR landing PASS (Reading A WIN at S89), update `.claude/agent-memory/lizzi-spectral-functional-theorist/permanent_theorems.md` with NEW theorem entry "LEVEL-DRESSED rank-ordering at s=4 substrate-distance-2 pole" + cross-link to §VII.AR + LEVEL-DRESSED 4th class addition to FI/RD/MIXED trichotomy. Per `agent-standards.md §"AMRI"` — does NOT route through agent memory as primary registry (the registry-row IS at §VII.AR per CF-B); the agent-memory entry is a private re-use note for spawn-time context, not the canonical pin.
   - **Inputs**: §VII.AR registry-row landing verdict (CF-B PASS); current lizzi `permanent_theorems.md` content.
   - **Gate**: agent-memory update is private to lizzi-spectral-functional-theorist; not a project-level gate. Routine `/shortterm` discipline applies.
   - **Effort**: 0.1 wave-equivalents (memory-file edit only; conditional on CF-B PASS).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | §W7a-74 FAIL is a substrate-physics finding at the algebra-INVARIANT layer (Reading A on (a)) | GEOMETRIC + PHONONIC | CONFIRMED via K-counter MANDATORY clause | The corridor "rank-1 EXACT at s=4 is FI across LEVEL" is CLOSED-FALSIFIED at SCHEMATIC layer; OPEN-CONDITIONAL at PRIMARY pending S89 anchor-sweep |
| 2 | W9b-2 spread = 0.0513 vs §W7a-74 spread_T1 = 1.011 / spread_T2 = 0.895 — `f2_only` vs `full` metric ambiguity (Reading B's (c) point CONDITIONALLY VALID) | METHODOLOGY (Class-8.2 PRU surfaces) | SURFACED, does NOT defeat Reading A on rank-layer | Class-8.2 calibration corpus instance #3 (K=3 promotion); CF-α |
| 3 | Class 8.2 rule extension is MORE FUNDAMENTAL than CF-A or CF-B (adjudication question (e)) | METHODOLOGY | K=2 → K=3 PROMOTION TRIGGERED via this synthesis | MANDATORY status at plan-freeze for all S89+ Spearman-spread gates; CF-α highest-EVOI |
| 4 | §VII.AK slot in WP CF-B is STALE — next-free is §VII.AR | REGISTRY-HYGIENE | CORRECTED via Grep-verification | All forward S89 dispatches consume §VII.AR (not §VII.AK; not §VII.AJ); CF-B downstream readers cite corrected slot |
| 5 | Reading A's NEW theorem is INTRA-Pillar-VII per W10-119 — Hybrid Independence Test does NOT gate registration | GEOMETRIC | CONFIRMED via cross-link to W10-119 extension | Per-Bulletin-per-pole Level-1/2/3 ladder applies; 5-IS-not-IN granularity NOT mandatory; §VII.AR landing schema clarified |
| 6 | NEW 4th class LEVEL-DRESSED proposed in §VII.K-DUAL trichotomy (FI/RD/MIXED → FI/RD/MIXED/LEVEL-DRESSED) | GEOMETRIC | PROPOSED at K=1; SUGGESTION pending K=3 | CF-γ pre-registers the extension; will reach MANDATORY at K=3 distinct LEVEL-DRESSED instances |
| 7 | Substrate-natural-anchor sweep specification (5 anchors) pre-registered as S89 gate | GEOMETRIC + METHODOLOGY | PRE-REGISTERED in §V.1; decision rule machine-verified | CONDITIONAL GO/NO-GO on §VII.AR landing |
| 8 | Workshop STRUCTURAL VERDICT — composite outcome PARTIAL READING A WIN + Class-8.2 RULE-EXTENSION orthogonal finding | RUBRIC | PRE-REGISTERED at-write per Class 8.2 self-application | NOT monolithic A/B; Class-8.2 promotion is the highest-EVOI rule extension; §VII.AR + §VII.K-DUAL extension + per-Bulletin-per-pole K=3 promote together |

---

## Substrate framing closing note

Per `phononic-framing.md §"IS Space, Not IN Space"`: the substrate IS the dual-spectrum structure (PRIMARY physical D_K eigenvalues at τ_fold=0.19 + SCHEMATIC bare SU(3) Casimir as a deterministic analog). The rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at the s=4 substrate-distance-2 pole IS substrate spectral content, NOT a derived observable in a regulator-containing meta-space. The Reading A finding — regulator-PARAMETER-dependence at this pole — is a substrate-IS structural fact about the spectrum itself; the substrate is not "in" any container of regulator-class orderings. The LEVEL discipline is the substrate-internal-vs-substrate-analog axis, not an external coordinate. Direction of explanation: D_K eigenvalues at τ_fold (substrate-IS) → regulator-class kernel evaluation (substrate-IS spectral content under each regulator) → 4-class M_R(s=4) values (substrate-IS spectral content at the s=4 residue) → Spearman rank ordering (substrate-IS ordinal structure) → LEVEL-DRESSED classification (substrate-IS LEVEL-axis dependence).
