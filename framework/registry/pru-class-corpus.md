# PRU Class Calibration Corpora

> **Provenance**: Lifted from `.claude/rules/epistemic-discipline.md` at S88 W9 housekeeping (gate `S88-W9-RULE-FILE-BLOAT-LIFT-OUT-EPISTEMIC`, 2026-05-06; orchestrator-direct-write per user preference + `feedback_rules-compensate-missing-structure.md` discipline). The parent rule retains the RULE STATEMENTS for each PRU sub-class (Class 8.0/8.1/8.2/8.3, Pole-Scope, Source-Reconciliation Class-(a)-(f)); this file holds the per-instance calibration corpora + K-counter advancement log that grew with each wave landing. Cross-link bidirectional: parent rule cites this file; this file's section headers reference parent rule sub-section anchors.

This registry file consolidates **4 corpora** for PRU sub-classes that the parent rule statements depend on:

1. PRU Class 8.2 (verifier-rubric pre-registration) — calibration corpus growing from W-12 instance #1 to W-8/W2-11 instance #2 (K=2; pre-MANDATORY)
2. PRU Class 8.3 (publication-precision pre-registration) — K=4 corpus (MANDATORY at S87 W8 close)
3. Pole-Scope sub-clause — K=4 corpus (MANDATORY at S88 W7a-72 close)
4. Source-Reconciliation Class-(f) PIN-PLACEHOLDER — K=4 corpus (MANDATORY at S88 W7b-83 close)

---

## §1. PRU Class 8.2 calibration corpus — verifier-rubric pre-registration failures

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)" + §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"`. The rule statement (rubric pattern set + disjunction-vs-conjunction declaration + negative-marker set + pre-registered calibration corpus pinned by SHA) lives in the parent. The K=1 → K=2 instance corpus + structural lessons live here.

### Class 8.2 status

K=5 at 2026-05-08; **MANDATORY** at plan-freeze for S88+ (promoted at S88 W-7 W2-2 V.5 + S88 W-22 W7a-74 V.3 simultaneous K=2→K=4 advancement carrying past K=3 threshold; W-21 W6b-56 V.6 boundary-direction added as Instance #5).

### Calibration corpus

#### Instance #1 — S86 W-12 "Z_4 or similar" (closed via S87 W11-1)

S86 W-12 "Z_4 or similar" admitted Klein-four V_4 via cardinality match despite element-order mismatch (V_4 = [1,2,2,2] vs Z_4 = [1,2,4,4]). Instance #1 closure: S87 W11-1 (`S87-MONODROMY-V_4-EXPLICIT`, connes-ncg-theorist) — substrate-level V_4 PARALLELOGRAM IDENTITY `A_n^(e) − A_n^(a) − A_n^(b) + A_n^(ab) = 0` tested at τ_fold=0.190, L_max=10 under natural Cartan-toral character (σ_M=(-1)^p, σ_C=(-1)^q on SU(3) Peter-Weyl indices) FAILed at max_dev=1.16; Z_4 alternative independently falsified by element-order mismatch (CC2 in W11-1 §W11-1 confirmed Sage-symbolic).

The supersession marker `supersedes=S87-MONODROMY-Z4-LANDING_per_PRU_Class_8_2` is encoded in the W11-1 verdict-line `value=` field (HIGH-DENSITY WORKSHOP TEMPLATE T2-5 multi-output decomposition slot 1).

**Class 8.2 lesson**: rubric tokens like "or similar" / "or equivalent" / "any of [...]" are unintentionally permissive on cardinality-only matches that admit structurally distinct groups via element-order signature. K-counter: 1 instance closed; promotion to MANDATORY at K=3 requires 2 more substrate-level Class-8.2 manifestations.

#### Instance #2 — S87 W-8 R3 closure / S88 W2-11 landing (2026-04-30 to 2026-05-03)

S87 W-8 R3 (workshop `s87-v4-strata-vs-cartan-relabeling.md`) closed with the finding that the V_4 character on the 4-stratum partition (2, 4, 8, 6) is STRUCTURALLY DISTINCT depending on whether the V_4 acts on (p, q)-Cartan-toral indices (W11-1 incarnation; FALSIFIED at max_dev = 1.19) or on substrate-physical stratum indices (S88 W2-3 incarnation; structurally supported by W11-2 + W11-3 + W11-meta-1 §VII.AJ.partition-stability + S88 W2-3 + S88 W2-6/W2-8/W2-9 instances).

The pre-registered rubric initially read "V_4 character on 4-stratum partition" without explicit distinction between Cartan-toral (acting on (p,q) Peter-Weyl indices) and stratum-index (acting on stratum_id ∈ {0,1,2,3}) incarnations. Both incarnations satisfy the literal rubric "V_4 character on a 4-stratum partition" — both are V_4 = (Z_2)^2 with order-(1,2,2,2) element signatures and both act on a 4-element set. The rubric admitted both via cardinality match while the substrate-physics answer requires distinguishing the two via the SUBSTRATE-IS-stratum-index vs PETER-WEYL-(p,q)-INDEX axis. This is the W-12 pattern (Z_4 vs V_4 cardinality match admitting structurally distinct groups via element-order signature), specialized to the Cartan-toral-vs-stratum-index axis within V_4 itself.

The rubric-form failure surfaced because both V_4 incarnations on a 4-element set look IDENTICAL at the abstract group-theory level (both are Klein-V_4 = Z_2 × Z_2 acting faithfully on 4 elements as a regular representation), but their ACTION on the substrate's spectral data differs structurally:

- **Cartan-toral V_4**: acts on (p,q) ∈ ℤ_≥0 × ℤ_≥0 sector labels via σ_M(p,q) = (-1)^p, σ_C(p,q) = (-1)^q. Bottom-20 at L_max=6 has only 3 sectors {(0,0), (0,1), (1,0)} → V_4 collapses to ⟨g_M, g_C⟩ ⊆ A_F automorphism inventory (W2-2 D-W8-1 FAIL with sip values (+8, +8, +20)).
- **Stratum-index V_4**: acts on stratum_id ∈ {0,1,2,3} via σ_strata1(s) = (-1)^(s mod 2), σ_strata2(s) = (-1)^(s ÷ 2). The cv = (2, 4, 8, 6) determines the action; substrate-IS group structure exists structurally (W2-3 PASS at structural level) but the Δ_n cocycle does NOT vanish at non-symmetric cv per §VII.AD Δ_0 LOCALIZATION FORMULA.

Class 8.2 K-counter: **1 → 2**; promotion to MANDATORY at K=3 still requires 1 more substrate-level Class-8.2 manifestation.

#### Instance #3 — S88 W-7 W2-2 V.5 D-W8-1 verifier-rubric pre-registration UNDERDETERMINATION (2026-05-08)

S88 W-7 W2-2 D-W8-1 verifier rubric (V_4-on-triality-mod-2 + KO=6 collapse pre-registration) admitted BOTH structural-OP-PROJ and L_max-conditional-STATE-PROJ readings via the same numerical signature. The rubric needed disambiguation between projection sides per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (MANDATORY at K=3, S88 W8-92 close), but the W2-2 D-W8-1 pre-registration was authored before that rule's MANDATORY promotion landed; the rubric admitted both projection sides without explicit suffix tagging. Forward remediation: rubrics for V_4 character constructions must distinguish substrate-physical stratum-index incarnation vs synthetic Cartan-toral incarnation AND must declare projection-side suffix per registry-landing.md §"Operator-Projection Reading-A Naming Hygiene".

#### Instance #4 — S88 W-22 W7a-74 V.3 numerical-metric-class (2026-05-08)

S88 W-22 W7a-74 verifier rubric (`spread ≤ 0.06` Spearman cross-regulator-spread metric admissibility band) admitted BOTH `full_atlas` and `f2_only_class` definitions of the spread metric without disambiguation. The rubric was authored at the substrate-distance-2 pole s=4 with the assumption that the spread metric definition was unambiguous; in fact two definitions are both compatible with the rubric's literal text. Forward remediation: rubrics whose PASS-band involves a Spearman cross-regulator spread metric MUST declare `spread_metric_definition ∈ {full_atlas, f2_only_class}` in plan-block PIN MAP. Audit-script extension at `_source_reconciliation_audit.py` Class-(g) `SPEARMAN-SPREAD-METRIC-UNDECLARED` flag with HARD-HALT remediation.

#### Instance #5 — S88 W-21 W6b-56 V.6 boundary-direction sub-check (2026-05-08)

S88 W-21 W6b-56 plan §W6b-56 substitution-chain-Step claimed "recovers 8 at τ → 5π" but the claim is structurally FALSE under direct Python verification (the τ → 5π boundary is a singularity of the HK-5 form, NOT an asymptotic limit recovering 8). The verifier rubric admitted the asymptotic-limit phrasing as a valid claim form because the rubric did not pre-register a boundary-direction substitution chain. Forward-enforcement: any plan-block claiming an asymptotic limit / boundary value MUST pre-flight Python-verify the boundary direction at plan-freeze. Audit-script extension queued at `_machinery_feasibility_audit.py` with "boundary direction substitution chain" sub-check.


#### Instance #6 — S90 W3 CF-36 α_s symbol-overload calibration corpus (2026-05-13)

> **Provenance**: S90 W3-4 (`S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING`; CF-36 / CF-S90-MACK-8); mack-cosmic-bridge sole-writer primary per `feedback_mack-bridge-role.md`; lizzi-spectral-functional-theorist alternate writer pathway per Class 8.2 PRU MANDATORY verifier-rubric pre-registration discipline (defaulted to mack at plan-freeze).
>
> **K-counter status**: documented as Class 8.2 instance #6 (verifier-rubric pre-registration discipline; the parent §1 K-counter sits at K=5 MANDATORY post-S88 W-21 W6b-56 V.6, so Instance #6 advances to K=6 — but the parent K-counter has already saturated past K_promotion=3 so the status is MANDATORY irrespective of this instance) AND a NEW sub-tracked "symbol-overload pattern" K-counter at **K=1 SUGGESTION** pending K=3 MANDATORY promotion per `feedback_rules-compensate-missing-structure.md` K=3 threshold. The symbol-overload sub-counter is distinct from the parent Class 8.2 verifier-rubric K-counter because the structural pathology is "shared symbol denotes structurally distinct numerical objects across STRUCTURALLY ORTHOGONAL axes" (algebra-axis orthogonality MANDATORY-K=3 per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`), separate from "rubric tokens admit cardinality-only matches" (Instances #1–#5 baseline).

**5-element instance template per Class 8.2 PRU MANDATORY**:

**(i) 3 distinct numerical objects sharing the symbol "α_s"**:

| # | Symbol form | Numerical value | Source / Provenance | Domain |
|:-:|:------------|:----------------|:--------------------|:-------|
| 1 | `alpha_s_MZ_obs` (or `α_s(M_Z)`, `\alpha_s(M_Z)`) | `0.1180` (PDG 2024) | `canonical_constants.py:alpha_s_MZ_obs` (line 1566 current file) | QCD strong-coupling running at M_Z; gauge-coupling axis; NOT inflationary |
| 2 | `alpha_s_inflation_framework` (legacy framework form) | `-0.068968` | `canonical_constants.py:alpha_s_inflation_framework` (line 1614 current file) `= n_s_canon**2 - 1`; `n_s_canon = planck_ns = 0.9649` is Planck-2018-anchored float (LEGACY; superseded at S88 W-15 W15-V.2 by bit-exact `n_s_FW_exact = Fraction(9561, 10000)`) | Inflationary running of scalar spectral index; CMB-inflationary axis; LEGACY Planck-anchor form |
| 3 | `α_s_canonical` (Route-B identity bit-exact) | `-0.085 872 79` = `-8587279/100000000` (Sage-QQ bit-exact in Q) | S87 α-s W2 PASS; `canonical_constants.py:n_s_FW_exact` (line 1719 current file)-derivable via `n_s_FW_exact² − 1`; S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` triple-verified | Inflationary running of scalar spectral index; CMB-inflationary axis; BIT-EXACT Route-B identity at substrate-distance-1 pole s=3 |

**Legacy laboratory-anchor pin** (for cross-axis disambiguation reference): `planck_alpha_s = -0.0045` (`canonical_constants.py:planck_alpha_s` line 1586; Planck-2018 legacy; superseded by `alpha_s_canon_2020 = +0.0023 ± 0.0063` at `canonical_constants.py:alpha_s_canon_2020` line 1600 per S86-W13 P12). These are laboratory-IN measurement values, NOT framework predictions — disambiguating axis is observational-canonical-vs-framework-substrate.

**(ii) Substitution chain cross-check** (Step-by-Step disambiguation per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1: Define 3 distinct quantities all denoted "α_s":
        q_1 = α_s(M_Z) = 0.1180                                              [QCD; canonical_constants.py:alpha_s_MZ_obs]
        q_2 = alpha_s_inflation_framework = -0.068968                        [LEGACY Planck-anchor; canonical_constants.py:alpha_s_inflation_framework]
        q_3 = α_s_canonical = -0.085872                                       [BIT-EXACT Route-B; canonical_constants.py:n_s_FW_exact-derived]

Step 2: Classification by axis:
        q_1 lies on QCD-gauge-coupling axis (strong-coupling running at M_Z ≈ 91.2 GeV)
        q_2 lies on inflationary-spectral-index-running axis (LEGACY Planck-anchor pin)
        q_3 lies on inflationary-spectral-index-running axis (BIT-EXACT Route-B identity)

Step 3: Distance pairs:
        |q_1 − q_2| = |0.1180 − (-0.068968)| = 0.186968                       [structurally unrelated; ORTHOGONAL axes]
        |q_1 − q_3| = |0.1180 − (-0.085872)| = 0.203872                       [structurally unrelated; ORTHOGONAL axes]
        |q_2 − q_3| = |(-0.068968) − (-0.085872)| = 0.016904                  [same axis; Planck-anchor drift]

Step 4: Discrimination at projected detector precision:
        CMB-S4 σ_α_s ≈ 2.3e-3: |q_2 − q_3| / σ_S4 ≈ 7.4σ                     [bit-exactness DRIFT alone discriminable at S4 if applied to q_2]
        CMB-HD σ_α_s ≈ 1.1e-3: |q_2 − q_3| / σ_HD ≈ 15σ                       [bit-exactness DRIFT decisive at HD]

Step 5: Direction of disambiguation:
        q_1 is on a DIFFERENT AXIS from q_2 and q_3 (QCD vs inflationary); cannot be conflated within framework α_s axis predictions.
        q_2 is SUPERSEDED by q_3 (bit-exactness discipline; S88 W-15 W15-V.2 landing); q_2 retained only for historical-annotation cross-link.
        Future framework computation scripts MUST use q_3 (`α_s_canonical` or `canonical_constants.py:n_s_FW_exact`-derived form).
        Future watchlist + falsifier rows MUST cite q_3 as the substrate prediction (per CF-29 Row #3 update + CF-33 / CF-34 watchlist rows).

Direction: bare "α_s" in framework documentation FORBIDDEN going forward; every citation MUST carry a qualifier disambiguating q_1 / q_2 / q_3.
```

**(iii) Structural cause** (why the symbol is overloaded):

The symbol "α_s" was independently adopted in two unrelated domains:
1. **QCD literature** (1970s-): α_s denotes the strong-coupling running of the QCD gauge coupling; canonical evaluation at M_Z (≈ 91.2 GeV); positive value O(0.1).
2. **Inflationary cosmology literature** (1990s-): α_s denotes `dn_s / d ln k`, the running of the scalar spectral index; canonical evaluation at CMB pivot scale (≈ 0.05 Mpc⁻¹); typically negative value O(10⁻²–10⁻³).

The framework's substrate-distance-1 pole s=3 Mellin observable (Route-B identity `n_s² − 1`) lands on the INFLATIONARY α_s axis (instance 3 = q_3). The framework's QCD prediction (gauge-coupling running, separately derived at substrate-distance-2 pole s=4 per S82 W1c FI chain) lands on the QCD α_s axis (instance 1 = q_1) — these are STRUCTURALLY ORTHOGONAL observables that happen to share a symbol per `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (algebra-INVARIANT spectrum-only-functional family vs algebra-DEPENDENT state-pair-functional family).

The Planck-anchor-vs-bit-exact distinction (instance 2 = q_2 vs instance 3 = q_3) is intra-axis and represents a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE pattern (Planck-2018 anchor superseded by bit-exact Route-B identity at S88 W-15 W15-V.2) per `.claude/rules/epistemic-discipline.md §"Source Reconciliation"`.

**(iv) Disambiguation rule** (forward-discipline for downstream consumers):

Per `S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH` (canonical_constants.py:alpha_s_MZ_obs line 1566 inline-comment + line 1586 inline-comment for planck_alpha_s legacy), every citation of "α_s" in framework documentation MUST be accompanied by an explicit qualifier disambiguating which of the 3 instances is meant:
- QCD: write `α_s(M_Z)` or `alpha_s_MZ_obs` (PDG canonical evaluation point)
- Inflationary LEGACY: write `alpha_s_inflation_framework` (Planck-2018-anchor; superseded; cite only for historical-annotation)
- Inflationary BIT-EXACT: write `α_s_canonical` (Route-B identity at substrate-distance-1 pole s=3; canonical for new computation scripts)

Bare "α_s" without qualifier is FORBIDDEN in framework documentation going forward (S90 W3 CF-36 landing forward-discipline pin).

**(v) Audit-script extension queue**:

Future `_alpha_s_symbol_overload_audit.py` (S91+ carry-forward, queued at plan §"Wave 3 Wrap-Up Discipline" item 1 `S91-ALPHA-S-SYMBOL-OVERLOAD-AUDIT-SCRIPT`) greps framework documentation for `\bα_s\b|\balpha[-_]s\b|\b\\alpha_s\b` patterns NOT followed by an explicit qualifier within a 20-character window; flags violations as Class 8.2 PRU verifier-rubric pre-registration failures. Until the audit script lands, plan-freeze validators manually cross-check α_s citations against this corpus instance.

**Class 8.2 verifier rubric 4-elements** (MANDATORY at plan-freeze):

1. **Pattern set** (3 symbol forms accepted with qualifiers):
   - `α_s(M_Z)` / `alpha_s_MZ_obs` / `\alpha_s(M_Z)` (Instance 1 = QCD)
   - `alpha_s_inflation_framework` (Instance 2 = LEGACY inflationary)
   - `α_s_canonical` / `alpha_s_canonical` (Instance 3 = BIT-EXACT inflationary)
2. **Disjunction declaration**: any qualifier accepted (disjunctive); bare "α_s" auto-fails.
3. **Negative-marker set**: bare `\bα_s\b|\balpha[-_]s\b|\b\\alpha_s\b` without qualifier within 20-character window.
4. **Exemplar SHA** (3 anchor SHAs):
   - S87 α-s W2 PASS (substrate-side; Instance 3 bit-exact pin)
   - S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (Sage-QQ exact triple-verification; substrate-side Instance 3)
   - S89 W4-4 `audit_sha256=e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` (joint (n_s, α_s) hypersurface; observational-side Instance 3; Class-8.5 PRU 2D verdict-line value-field calibration instance #1)

**Cross-link to existing rule-files**:
- `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (instances 2 and 3 are both derivative forms of an n_s-pin; instance 2 derives from Planck-2018-anchored `n_s_canon`; instance 3 derives from bit-exact `n_s_FW_exact`; PRIMARY canonical is `n_s_FW_exact`)
- `.claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"` MANDATORY (this corpus instance is the calibration instance #6 in §1 corpus; sub-tracked symbol-overload pattern K=1)
- `.claude/rules/regulator-pin-discipline.md` (forward extension to symbol-overload-aware regulator-pin discipline at S91+)
- `S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH` (canonical disambiguation precedent at `canonical_constants.py:alpha_s_MZ_obs` line 1566 + `:planck_alpha_s` line 1586 + `:alpha_s_inflation_framework` line 1614 inline comments)
- `canonical_constants.py` lines: `alpha_s_MZ_obs` line 1566 (Instance 1 = QCD), `planck_alpha_s` line 1586 (legacy observational), `alpha_s_canon_2020` line 1600 (Aiola+ 2020 ACT DR4 + Planck combined; current laboratory canonical), `alpha_s_inflation_framework` line 1614 (Instance 2 = LEGACY inflationary), `n_s_FW_exact` line 1719 (Instance 3 = BIT-EXACT inflationary; PRIMARY canonical)
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3 post-CF-29 update (CF-29 W2 audit `92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27` supersedes Row #3 cell from `-0.068968` to `-0.085872`)
- CF-33 `S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING` (Wave-3 sibling; audit `736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028`; cites α_s_canonical Instance 3 as substrate prediction, NOT Instance 2)
- CF-34 `S90-CMB-HD-ALPHA-S-NLO-WATCHLIST-LANDING` (Wave-3 sibling; audit `be1e362c5db63e7376c189893246f91f4c68c2592aa73868437c807b1069d5b4`; cites α_s_canonical Instance 3 + bit-exact NLO ε² recompute under `eps_H_W6` per `canonical_constants.py:eps_H_W6` line 1717; LEGACY Instance 2 `-0.068968` explicit NOT-TO-BE-USED flag)
- CF-35 `S90-3HE-B-LIAISON-WATCHLIST-LANDING` (Wave-3 sibling; audit `a1328849cbd361b01e14c210dc9cff3dff6dcba453897c53d06971f703c526b0`; structurally orthogonal axis — 3He-B BdG cocycle ratio 7.324992; α_s symbol-overload corpus instance documents cross-axis disambiguation that 3He-B vs CMB α_s share NO numerical scale)

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the substrate's intrinsic Mellin running at substrate-distance-1 pole s=3 IS `α_s_canonical = n_s_FW_exact² − 1 = -8587279/100000000` (Sage-QQ bit-exact in Q). The QCD α_s(M_Z) is a structurally DISTINCT observable (gauge-coupling running, NOT spectral-index running); the legacy `alpha_s_inflation_framework = -0.068968` is a Planck-2018-anchor-DERIVATIVE form of an earlier framework approximation (`n_s_canon` was a previous-canonical Planck-2018-anchored float, NOT the bit-exact `n_s_FW_exact = Fraction(9561, 10000)` pin landed at S88 W-15 W15-V.2).

The corpus instance documents that the shared symbol "α_s" represents three structurally distinct numerical objects; the substrate framing flows substrate → laboratory at each instance, but the LABORATORY context differs across the three (QCD-physics laboratory at instance 1; CMB-inflationary-physics laboratory at instances 2 and 3; bit-exactness discipline distinguishes instance 2 from instance 3).

Container-thinking violation FORBIDDEN: "all three α_s values live in the same parameter space"; INVERT: "the substrate has THREE structurally orthogonal predictions that share the symbol 'α_s' by historical accident; the algebra-axis orthogonality K=3 MANDATORY discipline forbids conflation between QCD and inflationary axes; the bit-exactness discipline distinguishes the Planck-anchor-DERIVATIVE legacy form from the Route-B-identity BIT-EXACT form on the inflationary axis".

#### Instance #7 — S96 W-5 D3 `dual_prior` INFO-band range-exclusion (2026-05-30)

> **Provenance**: W-5 D3 workshop (sagan-empiricist ∧ mack-cosmic-bridge, `sessions/archive/session-96/workshops/w5-d3-rank1-vs-rank2-covariance.md`; both agents agree, recorded as a process finding). Producing gate: W7-7a `S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE` (`audit_sha256=7227c8c5dc6d4fbdbf61888cf1bb74dfbc0ee9fa4c12bde26c6e2facd11dba5e`, line 159). mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`.

W7-7a pre-registered a `dual_prior` INFO band `Corr(a₀,a₂) ∈ (0.1, 0.5)`, but the producing machinery is a rank-1 outer-product covariance `Cov = s·sᵀ·Var(δH)` whose normalized correlation is `sign(s_i·s_j) ∈ {+1, 0, −1}` exactly (both magnitudes cancel; Sage-verified §W7-7a Step 4). The open interval `(0.1, 0.5)` lies entirely in the **complement** of the machinery's achievable output set — the INFO clause named an outcome the rank-1 producing machinery is structurally INCAPABLE of returning, regardless of input. This is a Class-8.2 verifier-rubric pre-registration defect of a NEW variety: not a cardinality-match (Instances #1, #2), not an underdetermination admitting two readings (Instances #3, #4), not a boundary-direction error (Instance #5), not a symbol-overload (Instance #6), but a **RANGE-EXCLUSION** — the pre-registered PASS/INFO/FAIL partition assigned a non-empty probability region to an outcome the chosen machinery's range excludes by construction. Reaching `(0.1, 0.5)` at all requires a rank-≥2 model (`|Corr| = 1/√((1+r₀)(1+r₂))`, a continuous function of the variance mix), which was NOT the pre-registered machinery. **Forward remediation**: any gate pre-registering an INFO/PASS band on a derived observable MUST pre-flight the producing machinery's ACHIEVABLE RANGE at plan-freeze (a one-line range check: does the machinery's closed form admit values in the proposed band?) and confirm the band ⊆ range. A band-vs-range mismatch is a plan-freeze Class-8.2 flag. Queued audit-script extension: `_machinery_feasibility_audit.py` "INFO-band-subset-of-machinery-range" sub-check (the range-exclusion analog of the Instance #5 boundary-direction sub-check). The defect is independent of the D3 covariance-model adjudication (rank-1 vs rank-≥2 disposition) and does not affect the W7-7a FAIL verdict (the FAIL is correct: `Corr=+1 > 0.5`).

**Class 8.2 K-counter**: parent §1 verifier-rubric counter already MANDATORY (K=5 ≥ K_promotion=3 since S88); Instance #7 advances the running tally to **K=7** (status MANDATORY irrespective). NEW sub-tracked "range-exclusion pattern" K-counter at **K=1 SUGGESTION** (distinct from the symbol-overload sub-counter of Instance #6 and from the cardinality/underdetermination baseline of Instances #1–#5; the structural pathology is "pre-registered band ⊄ producing-machinery achievable range"), pending K=3 MANDATORY promotion per `feedback_rules-compensate-missing-structure.md`.

#### K-counter advancement (S88 W-7/W-22/W-21 simultaneous)

K = 1 (W-12 baseline) + 1 (W-8 R3) + 1 (W2-2 V.5) + 1 (W7a-74 V.3) + 1 (W6b-56 V.6) = **5**. K=5 ≥ K_promotion=3 ⇒ MANDATORY promotion event triggered. Status flips from advisory (K=2 pre-S88 close) to **MANDATORY** at plan-freeze for S88+. (S90 W3 Instance #6 → running tally 6; S96 W-5 Instance #7 → running tally 7; status MANDATORY throughout.)

### Forward remediation

Pre-registered rubrics for V_4 character constructions MUST distinguish substrate-physical stratum-index incarnation vs synthetic Cartan-toral incarnation explicitly. Cross-link to S88 W2-3 (`S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION` — adopted stratum-index pre-registration discipline) and S88 W2-2 (`S88-V4-CANDIDATE-III-TRIALITY-MOD-2` — adopted D-W8-1 KO=6 collapse diagnostic FIRST gate-step to test structural independence from existing A_F automorphism inventory). Both gates demonstrate the corrected pre-registration discipline.

---

## §2. PRU Class 8.3 calibration corpus — publication-precision pre-registration (K=4 MANDATORY at S87 W8)

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"`. The rule statement (publication precision pin + verifier tolerance match + round-trip cross-check + canonical-metric pin + algebraic-equivalence audit at plan-authorship) lives in the parent. The K=4 calibration corpus instances live here.

### Class 8.3 status

K=4 (rule MANDATORY at plan-freeze 2026-04-30).

### K=4 calibration corpus

- **W1c-8 `n_s`** (S86): 10-sig-fig presentation (0.9784607074) vs full float64 (0.978460707430765); rel_tol=1e-12 < 1e-10; first instance.
- **W2-4 cluster-span** (S86): canonical-metric `|ratio − 2|` vs normalized form factor-2 mismatch at float-cancellation floor (~1e-15); first cluster-span instance; canonicalizes `|ratio − 2|` as the W0-3 metric.
- **W8-2 `max_pair_ratio_A_5`** (S87): 6-sig-fig published (9.240439e-01) vs full float64 (9.240438549812e-01); FAIL composite sign=PASS/mag=FAIL/regime=VALID; promoted `max_pair_ratio_A_5_FW = 9.240438549812e-01` to `canonical_constants.py`.
- **W8-8 `gv_canonical_difference`** (S87): 14-sig-fig plan-pinned (-40579.15004795) vs full float64 (-40579.1500479506); INFO composite (per-regulator deviation = ZERO across A_5_extended; INFO is publication-precision floor only); promoted `gv_canonical_difference_FW = -40579.1500479506`.
- **W13-3 R_842 stale-rectangle relabel** (S86, Class-(c) PIN-DRIFT-FROM-STALE-SOURCE): plan §W13-3.6 cited `R_842 = [-1.05, -0.85] × [-0.2, +0.2]`, but per `sessions/archive/session-84/session-84-w1-workingpaper.md:879` migration table, that's the **OLD R_918** rectangle; migrated R_842 is `[-0.942, -0.742] × [-0.2, +0.2]` (center -0.842 on W10-2 branch-(iv) anchor). Plan-freeze validators verify INPUT-PIN MAP rectangle labels against the most-recent migration ledger, NOT just against any rectangle in the historical record.

Plan-freeze auditors emit MANDATORY remediation on detection of tolerance < 10^(−published_sig_figs) anywhere in plan-block thresholds.

---

## §3. Pole-Scope sub-clause — K=4 calibration corpus (MANDATORY at S88 W7a-72)

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Pole-Scope sub-clause"`. The rule statement (pole-scoping declaration + pre-registered anchor-formula for pole-extension + discriminator predicate Reading_1-vs-Reading_2) lives in the parent. The K=4 calibration corpus instances + K-counter arithmetic + forward enforcement live here.

### Status: MANDATORY at K=4

Per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold, the Pole-Scope sub-clause hardens from advisory to MANDATORY at plan-freeze when N=3 distinct pole-scope calibration instances accumulate. The S88 W7a-72 landing extends the corpus from K=1 (the original S86 W-9 spectral ↔ dynamical anti-correlation at s=3) to K=4 in a single in-session advancement, carrying past the K=3 threshold. Status: **MANDATORY** for all S88+ plan-freezes; pole-scoping enforcement extends from advisory to plan-halt-on-violation.

### Calibration corpus (K=4)

- **Instance #1 (S86 W-9; original baseline)**: spectral 3-class partition ↔ Dynamical 4-class breakdown anti-correlation at substrate-distance-1 pole `s=3` — Spearman `|ρ_S| = 1.0 EXACT` at A_5 4-class projection. The pole-scoping discipline preserves the s=3 substrate-distance reading from contamination by other-pole readings. `S87-POLE-SPECIFICITY-SCAN` tests Reading_1 vs Reading_2 at s=4 (instance #4 below).

- **Instance #2 (S87 W7-1 IC-axis FAIL at s=−1)**: pole = `s=−1` (initial-condition Mellin slot, structurally distinct from substrate-distance s=3 pole). Verdict line `S87-W5A-P3-IC-PER-CLASS-VERIFY: FAIL -- value=7.985674e-01 scheme=Mellin-slot-s=-1-SCHEMATIC convention=substrate-natural-xi-E-GGE-SCHEMATIC L_max=10 audit_sha256=38b36fc0a5e5889facda9b175fa3f43c3f3f210f08518f4345af5abd786dc696` (`computations/session-87/s87_gate_verdicts.txt` line 197). PASS-on-pole-specificity: the IC-axis observable is scoped to the s=−1 pole; the FAIL at `delta_max = 0.7986 ≫ 0.20` falsifies the pole-specific reading (Reading_2 of step 3) at `s=−1` but does NOT contaminate the s=3 substrate-distance reading. Pole-scoping discipline preserves cross-pole isolation by construction — without it, the IC-axis FAIL would propagate to defeat instance #1.

- **Instance #3 (S87 W7-3 PASS-R2 integer-graded n_c at s=4)**: pole = `s=4` (substrate-distance-2 / Mellin-cone higher pole). Verdict line `S87-W6-C-GAMMA-WEAK-PER-CLASS: PASS -- value=1.145258e-01 scheme=Weyl-rescaling-Mellin convention=C-gamma-WEAK-per-L1-class-SCHEMATIC L_max=10 audit_sha256=0eb96f0536fb2d927639f8224bced41ccde74d062a9e59e0e29ae595919e3944` (`computations/session-87/s87_gate_verdicts.txt` line 209; W7-3 row in S87 results-WP table at line 6227). Pre-registered anchor-formula `n_c(s=4) := Res[M_R(s) · integer_grade_kernel; s=4]` was cited at S87 W7 plan-freeze per step (a) requirement (anchor-formula MUST be cited at plan-freeze for pole-extension; not discovered during execution per PRU-Class-8 prevention). PASS-R2 with integer-factorization residual `0.0368 ≤ 0.05` and non-trivial `{n_c} = (10, 10, 10, 11, 13)` confirms anchor-formula extension is structurally valid at the s=4 pole. Derived intermediates `Λ_global = 5.326e+14 GeV` and `profile-invariance = 1.49e-16` documented in S87 results-WP §W7-3 lines 5632-5864; verdict-line value `1.145258e-01` is the canonical PASS evidence (Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY: derived intermediates supplement, not replace, the verdict-line value).

- **Instance #4 (S87 W9b-2 |ρ_S(s=4)|=1.000 EXACT at s=4)**: pole = `s=4`. Verdict line `S87-POLE-SPECIFICITY-SCAN: PASS -- value='rho_S_s4=-1.000000;rho_S_s3_baseline=-1.000000;reading=Reading_1_PASS;cross_reg_spread=0.051317;|rho_S_s4|=1.000000' scheme=Mellin-cone-substrate-distance-0 convention=A_5-4-class-projection-W9-LCR3.2-MELLIN L_max=12 audit_sha256=30815fae79102fb9ac671fb33101029d5318253b69a2d125ea85ae5eb7396ebc` (`computations/session-87/s87_gate_verdicts.txt` line 268). The extremality at `s=4` (independent of instance #3's integer-graded n_c) is a SECOND structural correlation at the same pole, calibrating the Reading_1-vs-Reading_2 discriminator predicate of step 3. Two independent extremality witnesses at the same s=4 pole — integer-graded n_c (instance #3) AND |ρ_S|=1.000 EXACT (this instance) — confirm `Reading_1` (generic-pluralism: correlation holds at all poles) survives at this pole; the W-9 anti-correlation extends from s=3 to s=4 in this regulator-class projection. Cross-regulator spread `= 0.0513` (rank-FI but magnitude-RD layer; feeds §W7a-74 RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR).

K-counter arithmetic: `K = 1 (instance #1 S86 baseline) + 3 (instances #2, #3, #4 from S87 corpus) = 4`. K = 4 ≥ K_promotion = 3 ⇒ promotion event fires; sub-clause status := MANDATORY at plan-freeze for all S88+ gates.

### Forward enforcement (post-promotion)

- **Plan-freeze halt**: any S88+ gate citing a structural correlation across multiple Mellin-cone poles WITHOUT pole-scoping declaration triggers plan-halt with MANDATORY remediation per `_source_reconciliation_audit.py` Class-(c) extension.
- **Anchor-formula pre-registration MANDATORY**: pole-extension scripts must cite the anchor-formula in their plan-block (NOT discover during execution); enforced at PRDR via the Pre-Registration Dry-Run audit.
- **Cross-pole co-primary FORBIDDEN**: per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause + the algebra-axis orthogonality 4-corner classification at `permanent-results-registry.md §VII.U.2` clause (f), cross-pole co-primary registry-anchor structures (s=3 ↔ s=4 simultaneously as PRIMARY anchors) FAIL plan-freeze.

---

## §4. Source-Reconciliation Class-(f) PIN-PLACEHOLDER — K=4 calibration corpus (MANDATORY at S88 W7b-83)

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Source Reconciliation (Class 8.1)"` 6-class taxonomy clause (f) + `substrate-first-canonical-sourcing.md §(iv) SCHEMATIC vs full physical level pin rule`. The rule statement (placeholder pattern detection + substrate-canonical existence test + severity bands + canonical substitution remediation) lives in the parent. The K=4 calibration corpus + K-counter arithmetic + UV-conflation cross-link live here.

### Status: MANDATORY at K=4 (S88 W7b-83 close, 2026-05-05)

> **Provenance**: S88 W7b-83 (`S88-W7-LF-E-SCHEMATIC-MODULE-AUDIT`; connes-ncg-theorist PRIMARY; lizzi-spectral-functional-theorist CO-AUTHOR; sagan-empiricist ADVERSARIAL REVIEW dispatched separately by orchestrator post-this-script). Verdict at `computations/session-88/s88_gate_verdicts.txt`.

The Class-(f) PIN-PLACEHOLDER taxonomy admits a STRUCTURAL SUB-CLASS for SCHEMATIC-helper-consumption pathology: a producing script consumes a helper module whose docstring self-identifies as SCHEMATIC (e.g., `computations/_shared/_spectral_action_regulators.py` lines 23-30) without disclosing the level in the verdict-line `convention=` field. Downstream consumers (registry rows, knowledge-MCP indexing, cross-session synthesis) silently treat the output as PRIMARY (full physical regularization) — a structural class-conflation analogous to (and complementary with) the UV-regulator conflation closed by S75 ZETA-NOT-PHYSICAL-75 (`UV_REGULARIZATION_CONFLATION` PASS).

### Calibration corpus extension at S88 W7b-83 (K=4)

- **W4-2 line 513** (S86; first-witness baseline; NEGATIVE-CALIBRATION): `s86_w4_p5_sector_2_k_invariant.py` consumed `_spectral_action_regulators.py` schematic helpers; verdict `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT: FAIL ... convention=substrate-distance-1` at `computations/session-86/s86_gate_verdicts.txt:108` lacks `-SCHEMATIC` suffix; honesty disclosure landed POST-HOC at WP §VI line 513 ("the `_spectral_action_regulators.py` helpers are SCHEMATIC analogs of Connes-Chamseddine 1996 §2.2-2.3 multipliers, not the full physical regularizations"). The post-hoc disclosure preserved epistemic integrity but the rule-(2) violation (no `-SCHEMATIC` in convention tag) means the audit-trail-only consumer downstream cannot detect the level without reading the WP narrative.

- **W9b-2** (S87; NEGATIVE-CALIBRATION on rule-(2); rule-(3)-partial via comments): `s87_w9b_pole_specificity_scan.py` imports `_spectral_action_regulators` (lines 175-181) and acknowledges "schematic atlas" 17× in docstring/comments; verdict `S87-POLE-SPECIFICITY-SCAN: PASS ... convention=A_5-4-class-projection-W9-LCR3.2-MELLIN` at `computations/session-87/s87_gate_verdicts.txt:259+268+271+274` lacks `-SCHEMATIC` suffix. The 4 verdict-lines for this gate ID (PASS at `|rho_S(s=4)|=0.7746`, PASS at `|rho_S(s=4)|=1.000` Reading_1, FAIL at `cross_reg_spread=0.367544`, FAIL at `cross_reg_spread=0.894591`) ALL share the same rule-(2)-violating convention tag.

- **W9c-1** (S87; POSITIVE-CALIBRATION; canonical model): `s87_w9c_csub_axiom_cross_review.py` imports `_spectral_action_regulators` (line 182) AND declares TIER-2 SCHEMATIC explicitly in docstring lines 66-72 ("`_spectral_action_regulators.py` is SCHEMATIC per its docstring (lines 23-30: 'These are SCHEMATIC regulators ... NOT the full physical') — TIER-2 declaration"); verdict `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW: FAIL ... convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC` at `computations/session-87/s87_gate_verdicts.txt:262` carries `-SCHEMATIC` suffix; companion comment row at line 266 carries `# tier_pin=TIER-2 # ... (per .claude/rules/substrate-first-canonical-sourcing.md §iv SCHEMATIC vs full physical tier rule)`. Rule-(1)+(2)+(3) all satisfied; this is the canonical PRE-REGISTRATION model for forward S88+ gates consuming SCHEMATIC helpers.

- **W5b-2 sub-test (c)** (S86 substrate; cited by S87 W9c-1; CALIBRATION-LOCUS-EXEMPT): `s86_w5b_c16_csub_admissibility.py` (verdict `S86-W5B-C16-CSUB-ADMISSIBILITY: INFO ... convention=tau_fold_anchored` at `computations/session-86/s86_gate_verdicts.txt:138`) does NOT import `_spectral_action_regulators.py` and contains zero mentions of SCHEMATIC in its source. The W5b-2 sub-test (c) FAIL provided the DERIVATIONAL CONTEXT that S87 W9c-1's POSITIVE-CALIBRATION cross-review consumes; the calibration-instance LOCUS is the W9c-1 consumer (Instance #3 above). W5b-2 sub-test (c) is recorded as the 4th calibration-corpus locus to mark the cross-session inheritance pathway, not as a SCHEMATIC-disclosure pathology in itself.

### K-counter arithmetic

K = 4 ≥ K_promotion = 3 ⇒ promotion event triggered per `feedback_rules-compensate-missing-structure.md`. Level pin discipline at `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` is hereby promoted from SUGGESTION to MANDATORY at plan-freeze for all S88+ gates consuming SCHEMATIC helpers. See that rule's calibration-corpus table for the full per-witness audit and the 3-witness audit script `computations/session-88/s88_w7b_lf_e_schematic_module_audit.py`.

### Cross-link to UV-conflation closure

Per S75 ZETA-NOT-PHYSICAL-75 / `UV_REGULARIZATION_CONFLATION` PASS: the SCHEMATIC-vs-physical level pin discipline is structurally analogous to (and complementary with) the regulator-pin discipline at `.claude/rules/regulator-pin-discipline.md`. Both pathologies arise from silent consumption of structurally distinct regularization classes:

- **Regulator-pin**: a_n^{ζ} vs a_n^{Pauli-Villars} (UV-axis silent class-conflation)
- **Level pin**: SCHEMATIC vs FULL physical (level-axis silent class-conflation)

The two disciplines are non-redundant: a producing script may correctly tag `a_n^{Mellin}` (regulator-pin compliant) while consuming the SCHEMATIC `_spectral_action_regulators.py` Mellin helper (level-pin violator). Both pins MUST be carried in the verdict-line `convention=` field.

---

## §5. PRU Class 8.4 calibration corpus — representation-convention-pin failures

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"` row 8.4.

### Class 8.4 status

K=1 at 2026-05-08; advisory until K=3.

### Calibration corpus

#### Instance #1 — S88 W-16 W5b-50 V.5 representation-convention-pin failure

When the operator-domain dim is larger than the natural representation dim of the substrate algebra (e.g., a 16-state operator on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` whose natural representation is 14-dim; Pad-block embedding extends the rep to 16-dim), the gate MUST pre-register the embedding choice: `P_+` chirality projection / charge-conjugation doubling / spinorial extension. Pad-block convention dependence is the calibration-locus pathology: W5b-50 16×16 SDP results bifurcate algebra-INVARIANT on the `H ⊕ M_3(C)` block vs algebra-DEPENDENT on the Pad-block. The substrate-natural 14-dim representation re-run is queued as Ledger A.11 (`s88-w16-w5b-50-rank-deficiency.md §V.1`).

Forward remediation: any S88+ gate with operator-domain dim larger than the natural representation dim of `A_K` MUST pre-register the embedding choice in plan-block PIN MAP under the field `representation_convention ∈ {P_+, charge_conjugation_doubling, spinorial_extension}`.

---

## §6. PRU Class 8.5 calibration corpus — joint-hypersurface-pre-registration-form failures

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"` row 8.5.

### Class 8.5 status

K=1 at 2026-05-08; advisory until K=3.

### Calibration corpus

#### Instance #1 — S88 W-15 W4c-36 V.9 joint-hypersurface verdict-line form failure

Gates consuming substrate-IS observables through a CHILD pin (where the CHILD pin is itself a laboratory-IN observable on a different pillar — e.g., n_s pre-substrate pin in the α_s bridge map at S88 W-15 W4c-36) MUST emit the verdict-line `value=` field as a 2D hypersurface tuple `(child_pin_value, target_observable_value)`, NOT as a 1D scalar that conflates the child and target. The 1D-scalar form admits silent reading-shopping at session-end synthesis between substrate-self-consistent reading (CHILD = framework prediction at the same algebra-axis family) and external-observation reading (CHILD = laboratory measurement at the different pillar). The 2D-hypersurface form pre-registers the joint-locus discrimination at plan-freeze.

Forward remediation: any S88+ gate consuming a CHILD pin from a different pillar's bridge-anatomy element-3 MUST emit verdict-line `value=` as a 2D hypersurface tuple. Audit-script extension at `_source_reconciliation_audit.py` Class-(g) `JOINT-HYPERSURFACE-1D-SCALAR-DEGENERATE` flag with HARD-HALT remediation.

---

## §7. PRU Class 8.6 calibration corpus — layered-substitution-chain-audit failures

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"` row 8.6.

### Class 8.6 status

K=1 at 2026-05-08; advisory until K=3.

### Calibration corpus

#### Instance #1 — S88 W-17 W5b-47 V.5 Step-11 layered-substitution-chain-audit failure

When a plan substitution chain crosses §VII.U.2 corner cells (algebra-INVARIANT spectrum-only functional family vs algebra-DEPENDENT state-pair functional family corners), the substitution chain MUST pre-register a 3-layer audit pattern at plan-freeze:

1. **Arithmetic** layer (numerical-substitution validity)
2. **Parse-tree** layer (claim-form structural validity per the corner-cell algebra-axis)
3. **Operationalization** layer (substrate-physics claim-form maps to a concrete numerical-value test, with the test executable post-corner-crossing)

Without all 3 layers pre-registered, post-hoc corner-crossing claims admit Class-3 PROHIBITED_ACTIONS adjacency. W5b-47 Step-11 made an asymptotic-limit claim "recovers 8 at τ → 5π" that crossed the §VII.U.2 Corner-II ↔ Corner-IV boundary but lacked the operationalization-layer Python verification — structurally false under direct verification. Cross-link to §1 Instance #5 (boundary-direction sub-check, S88 W-21 W6b-56 V.6) — the two instances share the underlying pathology of unverified claim-form crossing structurally distinct domains.

Forward remediation: substitution chains crossing §VII.U.2 corner cells MUST pre-register all 3 layers. Audit-script extension at `_machinery_feasibility_audit.py` with "layered substitution chain corner-crossing" sub-check.

---

## §8. Source-Reconciliation Class-(c.OOM-misread) sub-class — calibration corpus

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Source Reconciliation (Class 8.1)"` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE row, sub-class `(c.OOM-misread)`.

### Class-(c.OOM-misread) status

K=1 at 2026-05-08; advisory until K=3.

### Calibration corpus

#### Instance #1 — S88 W-6 W1c-69 V.3 13-OOM Page-1976 Table-1 misread

Stale-source values that are structurally OOM wrong (vs band-drift). The §W1c-69 misread cited Page-1976 Table-1 as the canonical L_H multi-species evaporation rate at extremal-mass M=10^13 kg, but the cited table value was from a different mass-regime row that does not extrapolate cleanly under the substrate's cascade-tail T_H=1.057 MeV. Measured D_max=12.99 OOM, HARD-HALT band.

Structural distinction from band-drift Class-(c): band-drift typically D_max < 1.0 (within-band shift); OOM-misread is structurally D_max > 3.0 (HARD-HALT band) because the source value was extracted from the wrong regime entirely. Forward remediation queued as Ledger A.5 + A.6 (substrate-pinned L_H_canonical re-derivation + f(M) species-multiplicity lookup table).

---

## §9. Layer-Decomposition K-counter — definitional-datum vs derived-theorem corpus

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Layer-Decomposition" §"Definitional-datum-vs-derived-theorem K-counter at substrate ↔ methodology layer pair"`.

### Layer-Decomposition K-counter status

K=2 at 2026-05-08; advisory until K=3.

### Calibration corpus

#### Instance #1 — S86 W-13 W-1 profile-invariance

Under the layer-functor F, the substrate-IS profile-invariance reads as a **definitional datum** at the spectral-functional-codepath layer (the codepath is constructed to enforce the invariance) AND as a **derived theorem** at the algebraic-axis layer (the invariance follows structurally from algebra-axis K-counter MANDATORY at K=3). The two readings are NOT contradictory — the first is `F(definition)` at codepath layer; the second is `F(derived consequence)` at the algebra-axis layer.

#### Instance #2 — S88 W-11 W3b-15 χ_*(M_3) = 0 layer-bifurcation

The χ inheritance-morphism's M_3(C) annihilation is **TAUTOLOGICAL at the codepath layer** (the codepath constructs χ to send M_3(C) → 0; reading the codepath as evidence is circular) AND **substrate-IS at the A_F-composition layer** (independent χ' constructions on the same A_F decomposition derive M_3 annihilation as a theorem from BDI-class restriction; reading the derivation as evidence is structural). The two readings live at DIFFERENT layers of F and must not be merged into a single "evidence" claim.

Forward enforcement: future plan-blocks claiming substrate-IS evidence for an inheritance-morphism property MUST declare which layer of F the evidence sits at; codepath-layer claims are tautological-by-construction and DO NOT count as substrate-IS evidence; A_F-composition-layer claims MUST cite an independent derivation route (not the codepath that defined the morphism).

---

## §10. F(observable) vs F(trigger predicate) split — calibration corpus

> **Parent rule**: `.claude/rules/epistemic-discipline.md §"Layer-Decomposition" §"F(observable) vs F(trigger predicate) split"`.

### F-split status

K=1 at 2026-05-08; advisory until K=3.

### Calibration corpus

#### Instance #1 — S88 W-25 W7c-167 V.6

The W7c-167 plan-block's trigger predicate (the closing-paragraph-coherence rule's `covered_count ≥ N_PLANNING_DEFECT_THRESHOLD = 4` condition) is single-axis (rule-text-evidence-governed; F(trigger) admits a 1-axis read at the methodology layer). The W7c-167 substrate-physics observable (the corpus of waves whose closing-paragraph-coherence test fires) is multi-axis (substrate-IS-framing-governed; F(observable) preserves the multi-axis structural content per the algebra-axis orthogonality K-counter).

The split rule: when a plan-block contains BOTH an observable AND a trigger predicate, the layer-functor F applies DIFFERENTLY to each. Conflating them — treating the trigger's single-axis nature as evidence that the observable is single-axis, OR treating the observable's multi-axis nature as evidence that the trigger needs multi-axis pre-registration — is a Layer-Decomposition violation.

Forward enforcement: plan-block authoring discipline MUST tag observables and trigger predicates separately at plan-freeze; the layer-functor F-image is computed independently for each.

---

## §11. Surrogate-vs-Canonical at Cohomology-Class Layer (S88 W-9 W3a-18 V.5; B.12) — calibration corpus

> **Parent rule**: `.claude/rules/substrate-first-canonical-sourcing.md §iv-bis Surrogate-vs-Canonical at Cohomology-Class Layer`. The rule statement (detection pattern + MANDATORY clauses (i)-(iii) for surrogate-vs-canonical disambiguation at the cohomology-class layer) lives in the parent. The K=1 calibration corpus instance + algebraic-distance theorem live here.

### Status

K=1 at 2026-05-08; advisory until K=3.

### Calibration corpus

#### Instance #1 — S88 W-9 W3a-18 V.5 surrogate `R = (a_3_BdG − a_3_M_3(C))/(a_3_BdG + a_3_M_3(C))` algebraically-locked-to-fraction

**Algebraic-distance theorem** (Sage-verified; W-9 V.5 substitution chain):

```
R_surrogate := (a_3_BdG − a_3_M_3(C)) / (a_3_BdG + a_3_M_3(C))
            = (f − (1 − f)) / (f + (1 − f))      where f := a_3_BdG / a_3_full ∈ [0, 1]
            = 2·f − 1                            [affine function of BdG color-singlet weight fraction]
            ∈ [−1, +1]                           [range]

sign(R_surrogate) = +1  iff f > 0.5
                  = −1  iff f < 0.5

W3a-18 observation (L_max=10): f = 0.31641
⇒ R_surrogate = -0.367176370025644 (Sage exact)
⇒ R_surrogate < 0 FORCED by f < 0.5

Cross-validation: R_surrogate via direct evaluation = -0.367176370025643
                  agreement to float64 epsilon
```

**Substantive structural finding**: the surrogate's sign is mechanically locked to a Peter-Weyl partition fraction by the algebraic identity `R_surrogate = 2·f − 1` — a combinatorial constraint with NO cohomology-class content. No Hochschild cocycle, Chern character, or Connes-Karoubi pairing geometry enters this sign.

**Classification**: GEOMETRIC (the surrogate is a substrate-distance-1 spectral-moment ratio reduced to a Peter-Weyl combinatorial fraction; it is NOT a cohomology-class observable).

**Implication for the canonical Connes-Karoubi pairing**: §W3a-18 surrogate FAIL is **substantively informative on the W11-5 NON-COMPOSABILITY positive structural finding** (composability_residual = 0.887 ≫ 0.01) but is **NOT informative as a falsifier of the canonical Connes-Karoubi pairing** because the surrogate-canonical algebraic distance does not bound the canonical's sign or magnitude.

Forward enforcement: future S88+ gates whose plan-block proposes a surrogate observable for a cohomology-class quantity MUST pre-register the algebraic-distance theorem and document whether the surrogate is informative on the canonical's sign/magnitude (per the algebraic-distance theorem) OR is mechanically locked to a substrate-distance-N spectral-moment combinatorial fraction (in which case the surrogate FAIL is uninformative on the canonical and a separate canonical-evaluation gate is required). Audit-script extension queued at `_substrate_first_provenance_audit.py` cohomology-class-layer surrogate-detection clause.

### §11.1 — Surrogate sub-row taxonomy (S93 W8-3; SUGGESTION at K=1)

> **Provenance**: S93 W8-3 workshop (lizzi-spectral-functional-theorist + transit-dynamics-theorist; `sessions/archive/session-93/workshops/s93-w8-3-alpha-win-lo-floor-derivation.md`; CONVERGED, 2026-05-25). Orchestrator-landed from the FLAGGED Effected-In-Session block (subagents edit-denied on the ORCHESTRATOR-RESERVED corpus blocks). Refines the §11 parent (the `R_surr = 2f−1` algebraic-distance theorem).

A §(iv-bis) surrogate `Σ` for a SIGNED index-type canonical `C = ⟨[φ], Ch(P_0)⟩` partitions into two sub-rows by what `Σ` stands in for, with DIFFERENT firing sub-tests and DIFFERENT permanence:

- **(sub-row A) surrogate-for-the-signed-VALUE** — `Σ` stands in for `C` itself. The §(iv-bis) obstruction fires on **sub-test (ii)** (sign-lock divergence): a mechanically sign-locked `Σ` (combinatorial fraction, Cauchy-Schwarz positivity) is uninformative on `sign(C)` at ANY margin. **PERMANENT** non-promotion. Instance #1 (the §11 canonical worked example): `R_surr = 2f−1`, sign locked to `f > 1/2`.
- **(sub-row B) surrogate-for-a-MAGNITUDE-bound** — `Σ` stands in for a bound on `|C|`. The §(iv-bis) obstruction fires on **sub-test (i)** (undischarged substitution chain): the inequality `|C| ≥ Σ` is non-promotable unless the bounding step is a derived substrate identity (the trivial `|C| ≥ 0` is the only sign-lock-free derived bound, and it forbids nothing). **CONTINGENT** non-promotion — discharge-eligible if the bound is later derived. Instance #1 (S93 W8-3): `α_win_lo = s_CS/N_e` (the Regime verdict is a magnitude comparison `|α_bridge|` vs `α_req`, forcing sub-row B). Discharge-eligible at CF-S94-NARROW-PATH-WORKSHOP-6-COCYCLE-CONSTRUCTION deliverable 1.

The sub-row is FORCED by which question the canonical answers (sign vs magnitude). Both sub-rows are §(iv-bis)-non-promotable; the precedent §11 Instance #1 obstruction ("does not bound the canonical's sign OR magnitude", corpus line ~410) already covers BOTH legs, so neither sub-row is §(iv-bis)-exempt — the refinement is WHICH sub-test fires and WHETHER non-promotion is permanent. **K=1** (two instances on distinct sub-rows: `R_surr=2f−1` on A, `α_win_lo=s_CS/N_e` on B); a THIRD structurally-distinct instance advances toward MANDATORY per `feedback_rules-compensate-missing-structure.md`.

---

## §12. Substrate-first §(i) calibration corpus — K=4 NEGATIVE-CALIBRATION promotion (S88 W-15 V.5; B.13)

> **Parent rule**: `.claude/rules/substrate-first-canonical-sourcing.md §(i) When external-paper provenance is methodological vs canonical`. The rule statement (METHODOLOGICAL vs CANONICAL distinction; only METHODOLOGICAL citations allowed) lives in the parent. The K=4 calibration corpus + W5a-44 NEGATIVE-CALIBRATION instance live here.

### Status: MANDATORY at K=4 (S88 W-15 W5a-44 promotion, 2026-05-08)

K=3 implicit corpus pre-W-15 (the three worked examples in the parent §(i) text: W0c-3 vdd §VI absence; W4-2 SCHEMATIC helpers consumed as canonical; W5a-2 placeholder→canonical jump). W-15 W5a-44 promotes K=3 → K=4 NEGATIVE-CALIBRATION; per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold, the SUBSTRATE-FIRST-PROVENANCE sub-audit at plan-freeze hardens to MANDATORY status for S89+.

### Calibration corpus

#### Instance #1 (K=1, baseline) — W0c-3 vdd §VI absence

The W0c-3 plan-author drafted entry #5 with provenance "vdd §VI extraction at L_max=2" for the canonical constant `nonflat_T_correction_L2`. The cited heading "vdd §VI" does NOT exist in any of the 14 vdd papers; rerouted to substrate-first canonical at S83 W2-G24 (`computations/session-83/s83_w2_g24_nonflat_t_correction_l2.npz` correction_P1_T = 0.0). NEGATIVE-CALIBRATION on rule (1)-(2): cited external-paper heading is absent; substrate-first canonical exists.

#### Instance #2 (K=2) — W4-2 SCHEMATIC helpers consumed as canonical

`s86_w4_p5_sector_2_k_invariant.py` consumed `_spectral_action_regulators.py` SCHEMATIC helpers without disclosing the SCHEMATIC class in the verdict-line `convention=` field. Post-hoc honesty disclosure landed at WP §VI line 513. NEGATIVE-CALIBRATION on rule (3): SCHEMATIC class disclosure missing at the verdict-line layer where downstream consumers read.

#### Instance #3 (K=3) — W5a-2 `xi_E_GGE_inv` placeholder→canonical jump

Plan pin `xi_E_GGE_inv ≈ O(10⁻²)` placeholder against canonical `xi_E_GGE_inv = 13.642473425595973` from S86 W4 P4 commit; D_max = 3.13 OOM HARD-HALT band. NEGATIVE-CALIBRATION on rule (1): placeholder OOM estimate where substrate-first canonical existed.

#### Instance #4 (K=4 NEGATIVE-CALIBRATION; promotion trigger) — W5a-44 §VII.AN registry-anchor framing

W5a-44 §VII.AN registry entry's V-anchor cited "S82 W3-9 single-pole Mellin closure" as the canonical Route-A derivation source for n_s_FW = -8587279/100000000. But the cited closure script (`s82_w3_9_as_adjacent_obs.py:203`) computes `ns_framework**2 - 1.0` as a Route-B DIAGNOSTIC at line 203 — there is NO Route-A canonical numerical source in S82 W3-9. The V-anchor cite was a re-rationalization rather than an independent derivation; FAIL surfaces post-hoc at substrate-first-provenance audit.

Bit-exact arithmetic settles the question (verified Python at S88 B.1 promotion): `Fraction(9561, 10000)**2 - 1 == Fraction(-8587279, 100000000)` EXACTLY in Q. 8 candidate Route-A normalizations exhausted at L_max=12 spectrum cache; best `−f0` rel_diff = 2.85e-2 (vs PASS threshold 1e-12 — 10 OOM short). Structural verdict: Route-B is the actual canonical provenance; Route-A as described in §VII.AN/AO is a re-rationalization.

NEGATIVE-CALIBRATION on rule (1): cited external/internal-paper provenance does NOT match the substrate-first computation source; the V-anchor was canonical-form rather than methodological-form.

### K-counter advancement

K = 1 (W0c-3) + 1 (W4-2) + 1 (W5a-2) + 1 (W5a-44 NEGATIVE-CALIBRATION) = **4**. K=4 ≥ K_promotion=3 ⇒ MANDATORY promotion event triggered. The SUBSTRATE-FIRST-PROVENANCE sub-audit at plan-freeze hardens from advisory to MANDATORY status for S89+ gates.

### Forward enforcement (post-promotion)

- **Plan-freeze halt**: any S88+ plan-block whose V-anchor or C-anchor cites external-paper provenance OR internal-script provenance MUST verify the cited source actually contains the claimed substrate-first derivation. Audit script `_substrate_first_provenance_audit.py` (S87 carry-forward V.1; queued for S89 implementation) extends to verify cited closure script content at plan-authorship.
- **Cross-link to registry-landing.md**: NEGATIVE-CALIBRATION on §VII.AN W5a-37 + §VII.AO W5a-42 SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structures requires Option-A `supersedes`-tagged corrective successor entries per `gate-verdicts.md §"Option A"` (queued as Ledger B.31 + B.33).

### §12.iv — §(iv) K=4 level-pin calibration corpus — SCHEMATIC-route-discharge-re-tagged-status instance (S94 W-1; ENRICH, no K-advance)

> **Parent rule**: `.claude/rules/substrate-first-canonical-sourcing.md §(iv) SCHEMATIC vs full physical level pin rule` (the §(iv) K=4 calibration-corpus home per that rule's pointer table). The rule statement (CLASS pin SCHEMATIC + `-SCHEMATIC` convention suffix + tier_pin row + cross-class disclosure paragraph) lives in the parent. This sub-section carries the S94 W-1 ENRICH instance on the level-pin axis. Distinct from the §12 §(i) NEGATIVE-CALIBRATION sub-corpus above (Instances #1–#4): that K-counter is on the external-paper-provenance axis; THIS instance is on the SCHEMATIC-vs-FULL level-pin axis and ENRICHES the existing §(iv) K=4 corpus without advancing it (the resolution MECHANISM is identical to the prior §(iv) instances — a STRUCTURAL-ORTHOGONAL-COMPANION two-row split; only the split OBJECT differs).

**Instance**: §VII.AU.OP-PROJ `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → FULL-RECOVERED` discharge-status adjudication (S94 W-1 workshop `sessions/archive/session-94/workshops/s94-w1-vii-au-alpha-minus-3-status.md`; gate `S94-VII-AU-ALPHA-MINUS-3-LAYER-1` PASS, `computations/session-94/s94_gate_verdicts.txt:39`; connes-ncg-theorist Reading-A converged on (c) T3 + lizzi-spectral-functional-theorist Reading-B balanced joint verdict T4; landed by mack-cosmic-bridge in the S-2 closeout).

**Pattern**: a corridor-discharge STATUS re-tag to `FULL-RECOVERED` (housekeeping A9) where the producing verdict line carries `LEVEL_CLASS_PIN=SCHEMATIC tier_pin=TIER-2` (companion rows 38/44). The naive single-tag reading fires the §(iv) class-conflation pathology at the highest-leverage (registry-status) layer — a `FULL-RECOVERED` status tells every downstream consumer "recovered, full stop", erasing the SCHEMATIC class the verdict line discloses.

**Resolution (adjudicated outcome (c), two-layer split)**: the status splits into STRUCTURAL-ORTHOGONAL-COMPANION rows — Layer-1 (cohomology-class exponent) FULL-RECOVERED + Layer-2 (analytic-saturation evaluation route) SCHEMATIC-pending. The discriminating structural fact: the corridor's REGISTERED content is the Level-1 leading-term exponent `α = −(d−1) = −3` (registry-PROVEN; `get_constant("alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC")` → −3.0, Session S91, `CLASS=FULL` — INDEPENDENT of the W2-3 discharge gate), and what is SCHEMATIC is the **evaluation ROUTE** (the two-pin convergence-exponent protocol; `rho_FULL_CC_VII_AU_SAT_s3` PROVENANCE chain), NOT a distinct physical `c_continuum` observable. There is no surviving third object that is both physical and unrecovered.

**Two-axis fingerprint** (mirrors `regulator-pin-discipline.md §"four-axis orthogonality"` Level axis + the §22 2-bit anchor-vs-diagnostic fingerprint): the discharge object is `(cohomology-class-axis: FULL/PROVEN, L-INDEPENDENT) × (Level/sourcing-axis: SCHEMATIC, tier_pin=TIER-2, route-not-observable)`. A single-tag status on EITHER axis is a lossy axis-collapse: FULL-only erases the SCHEMATIC route (the bare-(a) error, WITHDRAWN by connes T3); SCHEMATIC/consistency-only erases the PROVEN exponent and understates Layer-1 (the single-row-(b) error, REJECTED). The orthogonality theorem (`STRUCTURAL-FULL(exponent) ⇏ FULL-RECOVERED(single-tag)` AND its converse `SCHEMATIC(route) ⇏ ¬FULL(exponent)`, per `regulator-pin-discipline.md §"four-axis orthogonality"`) demands two rows.

**Distinctness from prior §(iv) corpus instances (K-status: ENRICH, no advance)**: distinct from the §VII.AF.1.OP-PROJ "S91 W7" instance (SCHEMATIC-SDW vs FULL-CC residue-VALUE seam, registry ~14936–14978) and the §VII.AU.OP-PROJ "S92 W1 CF-W9-8-2" companion (SCHEMATIC convergence-exponent vs FULL-CC residue-VALUE, registry ~18280–18319) on the SPLIT-OBJECT axis: those split a SCHEMATIC-VALUE vs FULL-VALUE seam at the canonical-pin level; THIS instance splits a discharge-STATUS re-tag where the SCHEMATIC residual is the **evaluation ROUTE to a PROVEN exponent**, not a competing VALUE. But the RESOLUTION MECHANISM is the SAME (STRUCTURAL-ORTHOGONAL-COMPANION two-row split on the level-pin axis), so it ENRICHES the §(iv) K=4 corpus and does NOT advance the K-counter (the §(iv) NEGATIVE-CALIBRATION K-counter at §12 above stays K=4; the level-pin §(iv) discipline is already MANDATORY). The closeout adjudicated ENRICH-default per the W-1 verdict's own routing instruction (workshop line 120). HOME-SELECTION (no double-land): this instance is filed HERE (the §(iv) Level-axis 4-class home) and NOT additionally in the regulator-pin four-axis corpus (`cross-pillar-bridge-corpus.md` Level-axis), per the W-1 closeout-note "pick ONE home" (workshop line 125).

**Provenance**: S94 W-1 workshop `sessions/archive/session-94/workshops/s94-w1-vii-au-alpha-minus-3-status.md` (T1/T2/T3 turns + T4 JOINT VERDICT, adjudication outcome (c)); gate `S94-VII-AU-ALPHA-MINUS-3-LAYER-1` PASS (`computations/session-94/s94_gate_verdicts.txt:39`; audit_sha256=`ee28ac74b9f5fe3850caf19eecba9a3ed679f65e6b16dae46a77b1e4f9b8fade`); registry two-row split landed at `sessions/permanent-results-registry.md` §VII.AU.OP-PROJ (S-2 closeout, adjacent to the S92 W1 CF-W9-8-2 companion); landed by mack-cosmic-bridge (S-2 combined-landscape closeout; corpus sole-writer this run).

## §13. Wave-Classification Forward-Pinned-Follow-Up Wave Class (S88 W-25 W7c-167; B.17) — calibration corpus

> **Provenance**: S88 W-25 W7c-167 §V.2 (sagan-empiricist + gen-physicist closing-paragraph-coherence workshop). Two-corpora landing per Convergence #3 / Emergence #1: Corpus A retains the existing `mechanical-closure-discipline.md §"PLANNING DEFECT"` count-keyed trigger (W7c instance #1); Corpus B is the forward-pinned-follow-up wave class at `wave-classification.md` (orthogonal axis, structural-class-keyed; this file). K=1 advisory pending K=3 promotion per `feedback_rules-compensate-missing-structure.md`. Parent rule body at `wave-classification.md §"Forward-pinned-follow-up wave class"`.

### K-counter status

| K | Source | Wave | Forward-pinning structure | Item-1-clean per gate? |
|:-:|:-------|:-----|:--------------------------|:----------------------:|
| 1 | S88 W-25 (sagan-empiricist + gen-physicist) | S88 W7c (4 gates: §W7c-167, §W7c-184a, §W7c-184b, §W7c-189) | All 4 gates pre-registered with mid-session-expected machinery / data landings (W7b-79 LEVEL-2 closure substrate; cache resolution awaiting); plan §365 BLACKLIST + DPP routing instructions for prereq-block scenario | YES (per W7c WP §1 lines 866-869) |
| 2 | reserved | — | — | — |
| 3 | reserved | — | — | — |

### Forward-pinning-density observable specification

Per W-25 sagan E2 (workshop §lines 246-258), the forward-pinning-density observable on a wave plan-block at plan-freeze is multi-axis:

- **PB(W) := |{gates in W with prereq-block}|** — count of gates whose machinery pin or input-SHA pin points to mid-session-expected landings. Trigger-keyed at PB(W) ≥ 1 per Corpus B.
- **DPP_routing_count(W) := |{routing rows in W's downstream decision-point table addressing prereq-block scenarios}|** — count of explicit DPP routing instructions for prereq-block routing. Required ≥ PB(W) per item-1-clean discipline.
- **item_1_status_per_gate(W) := PASS/FAIL/INFO per gate per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 1**. ALL must PASS for Corpus B classification (otherwise routes to Corpus A only).

The Corpus B trigger predicate is structural-class-keyed (M1'-M4' per parent rule body). Corpus A (count-keyed; `mechanical-closure-discipline.md §"PLANNING DEFECT"`) and Corpus B (structural-class-keyed; `wave-classification.md §"Forward-pinned-follow-up wave class"`) are STRUCTURALLY ORTHOGONAL per the F(observable) vs F(trigger) split (this file §10 K=1 calibration); a wave may be instance-#1 of BOTH simultaneously (W7c is the canonical example).

### Forward enforcement

S89+ plan authors landing waves with PB(W) ≥ 1 SHOULD:

1. Tag wave class as "forward-pinned-follow-up" in plan-block header
2. Ensure DPP routing instructions cover ALL PB(W) gates' prereq-block scenarios
3. Verify item-1-clean per gate via `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 1 PASS predicate
4. Cross-link to this corpus §13 with K-counter advancement note

Status promotes from SUGGESTION to MANDATORY at K=3 distinct calibration instances.

## §14. Closing-Paragraph-Coherence Audit Pattern (EG1) (S88 W-25 W7c-167; B.21) — calibration corpus

> **Provenance**: S88 W-25 W7c-167 §V.8 (sagan-empiricist + gen-physicist closing-paragraph-coherence workshop). Audit-pattern specification: closing-paragraph-coherence test for rule-text composition. K=1 advisory pending K=3 promotion per `feedback_rules-compensate-missing-structure.md`. Parent rule extension at `epistemic-discipline.md §"Pre-Registration Completeness"` §"Closing-Paragraph-Coherence Audit Pattern (EG1)".

### Audit-pattern specification

For any rule-file section composed of (i) an enumerated antecedent list followed by (ii) a closing paragraph that disambiguates the rule's behavior at execution time, the audit pattern fires when:

- The closing paragraph's qualifying language ("remains acceptable AT EXECUTION TIME", "still permitted under conditions", etc.) is consistent with the antecedent list under ONLY ONE structural reading of the antecedent (literal-independent OR strict-conjunctive); AND
- The other reading produces a self-contradiction (FORBIDDEN-AT-AUTHORING-TIME ∧ acceptable-AT-EXECUTION-TIME, etc.).

The audit pattern's resolution names the structurally-coherent reading as canonical; the other reading is rejected as a reading of the rule-file as authored.

### K-counter status

| K | Source | Rule-file section audited | Reading rejected | Reading canonical |
|:-:|:-------|:--------------------------|:-----------------|:------------------|
| 1 | S88 W-25 (sagan-empiricist + gen-physicist) | `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` item 1 vs §"PLANNING DEFECT" closing paragraph (lines 30-31 vs 282-286 pre-edit) | strict-conjunctive (FORBIDDEN-AT-AUTHORING ∧ acceptable-AT-EXECUTION self-contradiction) | literal-independent (item-1-PASS by construction; closing paragraph's "remains acceptable" assumes item-1-PASS premise) |
| 2 | reserved (sweep audit per W-25 V.5 candidate `v3-closure-recovery.md PROHIBITED_ACTIONS` Class 1-7 vs Stage 1/2/3) | — | — | — |
| 3 | reserved (sweep audit per W-25 V.5 candidate `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause vs K-counter advancement criteria) | — | — | — |

### Forward enforcement

S89+ rule-file edits SHOULD apply the closing-paragraph-coherence audit when adding a new closing paragraph to a section with an enumerated antecedent list. The W-25 V.5 sweep audit on 3 candidate rule-files (`v3-closure-recovery.md`, `cross-pillar-bridge-anatomy.md`, `joint-theorem-promotion.md`) is a separate sweep gate (`S89-RULE-FILE-COHERENCE-SWEEP-AUDIT`) advancing K-counter incrementally per surfaced contradiction.

Status promotes from SUGGESTION to MANDATORY at K=3 distinct calibration instances.

## §15. Joint-Theorem Substrate-Input-Orthogonality Clause (S88 W-23 W7c-167; B.56) — calibration corpus

> **Provenance**: S88 W-23 W7c-167 §V.1 (volovik-superfluid-universe-theorist; LEVEL-2 closure + obs1 PASS-AND independence workshop). Parent rule extension at `joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check"` §"Substrate-input-orthogonality clause". K=1 advisory pending K=3 promotion per `feedback_rules-compensate-missing-structure.md`.

### Substrate-input-orthogonality predicate

For a Stage-2 verification with N ≥ 2 observables {obs_1, ..., obs_N}, the substrate-input-orthogonality predicate holds iff:

- ∃ obs_i such that the data file consumed by obs_i is loaded by exactly one cross-reviewer (NOT both).

The procedural-floor `joint-theorem-promotion.md §"Two-Agent Independent-Verify"` clause "operate WITHOUT prior workshop context" rules out shared-workshop-transcript channels but admits shared-numerical-input channels. Substrate-input orthogonality hardens the procedural floor into a structural ceiling: at least one observable's verdict is computed from data the OTHER reviewer cannot replicate.

### K-counter status

| K | Source | Stage-2 dispatch | Substrate-input overlap | Verdict |
|:-:|:-------|:-----------------|:------------------------|:--------|
| 1 | S88 W7c-167 obs1 PASS-AND (Verdict B accept-but-flag-with-calibration-caveat per W-23 §IV.3) | §VII.AH STAGE-1-CANDIDATE Stage-2 dispatch on obs1 (mack-cosmic-bridge spectral-side + connes-ncg axis-orthogonality side) | shared `s87_w7_ic_per_class_verify.npz` SHA-256 `120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f`; shared §VII.AH registered text; shared canonical_constants pins (`xi_E_GGE_inv = 13.642473`, `tau_fold = 0.190`) | calibration corpus instance #1 with substrate-input-overlap caveat; PASS-AND admissible under procedural floor but does NOT establish full structural-input independence |
| 2 | S89 W4-7 §VII.AH Stage-2 re-dispatch on obs2 + obs3 PASS 8/8 (audit_sha256=`4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a` at `s89_gate_verdicts.txt:80`; gate `S89-VII-AH-STAGE-2-RE-DISPATCH-OBS2-OBS3` per JOINT (c) + (d) clause PASS-AND verification) | §VII.AH STAGE-1-CANDIDATE Stage-2 re-dispatch on obs2 + obs3 (mack-cosmic-bridge spectral-side + connes-ncg axis-orthogonality side; obs2 + obs3 substrate-input-orthogonal per W4-7 verification) | NONE — orthogonality predicate satisfied: obs2 + obs3 each consume substrate-input loaded by exactly one cross-reviewer (NOT both); FIRST INSTANCE WITHOUT substrate-input-overlap caveat | calibration corpus instance #2 at **structural ceiling** (no overlap caveat needed); FIRST framework cross-axis joint theorem to STAGE-3-PERMANENT eligibility under substrate-input-orthogonality predicate; K=1 → K=2 advancement landed S90 W1-17 (2026-05-13); STATUS remains SUGGESTION at K=2 (promotes to MANDATORY at K=3) |
| 3 | reserved (S90+ third structurally-distinct instance with substrate-input-orthogonal observables across distinct §VII registry slot) | — | — | — |

### Forward enforcement

S89+ Stage-2 dispatches with N ≥ 2 observables MUST verify substrate-input-orthogonality at plan-freeze:

1. Enumerate per-reviewer input-pin map; verify ≥ 1 observable's data file is in exactly one reviewer's map.
2. If all observables share data files, route to remediation: add an orthogonal-data observable (e.g., volovik consumes `3HeB-inheritance-canonical.md` cohomology-asymmetry while connes consumes spectrum cache via Mellin pole interpretation NOT replicated by volovik) before Stage-2 dispatch.
3. Audit-script extension `_joint_theorem_independent_verify_audit.py` flags substrate-input-orthogonality predicate failures at plan-freeze with HARD-HALT remediation.

Status promotes from SUGGESTION to MANDATORY at K=3 distinct calibration instances.

## §16. Joint-Theorem 6th Audit Item — Cross-Reviewer Audit-Machinery Self-Citation (S88 W-23 W7c-167; B.60) — calibration corpus

> **Provenance**: S88 W-23 W7c-167 §V.8 (volovik-superfluid-universe-theorist; LEVEL-2 closure + obs1 PASS-AND independence workshop). Parent rule extension at `joint-theorem-promotion.md §"Audit at plan-freeze"` 6-item list (extended from 5 items). K=1 advisory pending K=3 promotion per `feedback_rules-compensate-missing-structure.md`.

### Audit-machinery self-citation predicate

A cross-reviewer R applies "self-authored audit machinery" iff R applies a parse-tree decision procedure / 4-corner classification / cohomology bridge map at the verdict-emission layer AND R is the sole author of that machinery (e.g., the rule-file section defining it, the registry-entry that established it).

Self-authored audit machinery at the verdict-emission layer is structurally weaker than audit machinery cross-checked by another agent: the self-author has implicit interpretive authority over edge cases that an independent cross-checker would surface.

### K-counter status

| K | Source | Stage-2 dispatch | Self-authored audit machinery | Verdict |
|:-:|:-------|:-----------------|:------------------------------|:--------|
| 1 | S88 W7c-167 connes-ncg axis-orthogonality side audit (per W-23 §IV.4 + §V.8) | §VII.AH STAGE-1-CANDIDATE Stage-2 dispatch (mack spectral + connes axis-orthogonality) | connes-ncg applies `permanent-results-registry.md §VII.U.2` 4-corner parse-tree classification (connes-authored at S87 W-2 R3) at the verdict-emission layer; admissible under joint-theorem-promotion item-3 (connes is NOT the S86 W-9 workshop author for §VII.AH itself) but structurally weaker than a non-self-authored alternative | calibration corpus instance #1 of self-citation-at-machinery-layer pattern |
| 2 | reserved (S89+ §VII.AH re-dispatch with alternate machinery route or second-reviewer cross-check on §VII.U.2 application) | — | — | — |
| 3 | reserved | — | — | — |

### Forward enforcement

S89+ Stage-2 dispatches MUST verify the new 6th audit item at plan-freeze:

1. Identify per-reviewer audit machinery applied at the verdict-emission layer (parse-tree, 4-corner classification, cohomology bridge map, etc.).
2. Cross-reference each machinery's authorship trace via `mcp__knowledge__.trace_entity(<machinery-name>)` or registry/rule-file authorship section.
3. If ANY reviewer is the sole author of the machinery they apply at verdict-emission, route to remediation: (a) apply alternate machinery route at the verdict layer, OR (b) require a SECOND reviewer cross-checks the machinery application.
4. Audit-script extension `_joint_theorem_independent_verify_audit.py` flags self-citation predicate at plan-freeze.

Status promotes from SUGGESTION to MANDATORY at K=3 distinct calibration instances.

---

## Changelog

- **2026-05-06 (S88 W9 housekeeping)**: NEW file. Lifted from `.claude/rules/epistemic-discipline.md` per `feedback_rules-compensate-missing-structure.md`: 4 corpora (Class 8.2 K=2, Class 8.3 K=4, Pole-Scope K=4, Class-(f) PIN-PLACEHOLDER K=4) consolidated here. Parent rule retains rule statements + schema + 6-class taxonomy; this file holds the per-instance calibration corpora + K-counter advancement log. Cross-link bidirectional: parent rule cites this file; this file's section headers reference parent rule sub-section anchors.
- **2026-05-08 (S88 Phase 2 corrective rework)**: User correction — epistemic-discipline.md is NOT a tracking document. Lifted Phase 2 inline prose (B.6+B.53 Class 8.2 K=2→K=5 instances #3-#5; B.7 Class 8.4 §5; B.8 Class 8.5 §6; B.42 Class 8.6 §7; B.9 Class-(c.OOM-misread) §8; B.10 Layer-Decomposition K-counter §9; B.11 F(observable) vs F(trigger) §10) from rule file to corpus file. Parent rule will be reverted to brief K-count + status + 1-line pointer per `feedback_rules-compensate-missing-structure.md` discipline.
- **2026-05-08 (S88 Phase 3 sub-clause B.12)**: Added §11 (Surrogate-vs-Canonical at Cohomology-Class Layer K=1, S88 W-9 W3a-18 V.5; algebraic-distance theorem `R_surrogate = 2·f − 1`).
- **2026-05-08 (S88 Phase 3 sub-clauses B.13/B.17/B.21/B.56/B.60 + Phase 5b B.32/B.33)**: Added §12 (substrate-first §(i) K=4 NEGATIVE-CALIBRATION promotion to MANDATORY for S89+); §13 (Wave-Classification Forward-Pinned-Follow-Up Wave Class K=1, S88 W-25 W7c-167 V.2; Corpus B parent rule at `wave-classification.md §"Forward-pinned-follow-up wave class"`); §14 (Closing-Paragraph-Coherence Audit Pattern EG1 K=1, S88 W-25 W7c-167 V.8; parent rule at `epistemic-discipline.md §"Pre-Registration Completeness"`); §15 (Joint-Theorem Substrate-Input-Orthogonality K=1, S88 W-23 W7c-167 V.1; parent rule at `joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check"`); §16 (Joint-Theorem 6th Audit Item — Cross-Reviewer Audit-Machinery Self-Citation K=1, S88 W-23 W7c-167 V.8; parent rule at `joint-theorem-promotion.md §"Audit at plan-freeze"` extended from 5 to 6 items). Phase 5b Option-A `supersedes`-tagged corrective verdict-line emissions (B.32 §W3a-18 audit_sha256=`ec6f94a0c219dc715d13117d39a28228b88d249011f8feb7f60a09fd1f30fbf8` supersedes `80405c22…`; B.33-1 §VII.AN W5a-37 audit_sha256=`58d870e9116b49e8bfad87759a11df3606ca977aca13c015f58dbda250e25ba8` supersedes `cf5ec646…`; B.33-2 §VII.AO W5a-42 audit_sha256=`e5055f10287237f17f914142f74fb3e7e86cca682a2af5b97ae965721154ac3a` supersedes `d536b674…`) emitted via `computations/session-88/s88_b32_b33_supersedes_emission.py`; sig_5 PASS (3 unique SHAs vs existing 175); n_s_FW_exact² − 1 = Fraction(−8587279, 100000000) bit-exact identity sanity-asserted before emission. B.31 (registry-side §VII.AN-CORRIGENDUM + §VII.AO-CORRIGENDUM slot landing) DEFERRED to mack-cosmic-bridge writer per `feedback_mack-bridge-role.md` (rolls to Phase 5a).
- **2026-05-08 (S88 Phase 3 sub-clause B.13)**: Added §12 (substrate-first §(i) K=4 NEGATIVE-CALIBRATION promotion; SUBSTRATE-FIRST-PROVENANCE sub-audit MANDATORY for S89+).
- **2026-05-09 (S88 atlas refresh consistency pass)**: Header normalization disclosing corpus expansion from "4 corpora" to 16 sections (5 MANDATORY at K≥3 + 11 advisory K=1-K=2). Cross-rule synchronization audit confirms all 16 sections match parent rule bodies as of 2026-05-08 close: epistemic-discipline.md §"Pre-Registration Completeness" sub-class taxonomy (8.0/8.1/8.2/8.3/8.4/8.5/8.6) + §"Source Reconciliation" 6-class taxonomy + §"Layer-Decomposition" definitional-vs-derived + F(observable)-vs-F(trigger) split, cross-pillar-bridge-anatomy.md §"Hybrid Independence Test" + §"Algebra-axis orthogonality K-counter", joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check" §"Substrate-input-orthogonality clause" + §"Audit at plan-freeze" item 6, substrate-first-canonical-sourcing.md §(i) + §(iv) + §(iv-bis), wave-classification.md §"Forward-pinned-follow-up wave class". No new corpus rows required. Aggregate K-counter status across the 16 sections: §1 K=5 MANDATORY, §2 K=4 MANDATORY, §3 K=4 MANDATORY, §4 K=4 MANDATORY, §12 K=4 MANDATORY (5 sections at MANDATORY status), §5 K=1 advisory, §6 K=1 advisory, §7 K=1 advisory, §8 K=1 advisory, §9 K=2 advisory, §10 K=1 advisory, §11 K=1 advisory, §13 K=1 advisory, §14 K=1 advisory, §15 K=1 advisory, §16 K=1 advisory (11 sections at SUGGESTION/advisory pending K=3). Total 33 distinct calibration instances tracked across the 16 sections. One outstanding internal lag observed: epistemic-discipline.md taxonomy table at §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension" row 8.2 reads "MANDATORY at K=4 (S88 W-7 + W7a-74 promotion)" but rule-body §"Class 8.2 calibration corpus" line 149 reads "K=5 at 2026-05-08" — the K=5 reading is canonical per §1 Instance #5 (W-21 W6b-56 V.6 boundary-direction); the table cell needs the same update at next epistemic-discipline.md edit pass. Cross-link to atlas-12 §IV (PRU Class 8.0–8.6 sub-class taxonomy enumeration); atlas-11 §X (Algebra-axis orthogonality K-counter parallel discipline) for the K-counter promotion mechanism this corpus embodies.

## §17. Observable-Naming-History vs Parse-Tree-Structure (S90 W-3 CF-LZ-5 sub-clause; cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter") — calibration corpus

> **Provenance**: S90 W1-7 (gen-physicist orchestrator-direct-write under /rclab-solo on session-90-plan-w1.md §W1-7; CO-AUTHOR lizzi-spectral-functional-theorist for history-vs-structure observable-naming review). Cross-link to parent rule sub-clause at `.claude/rules/cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"`.

### Status: SUGGESTION at K=2 (promotes to MANDATORY at K=3)

The Observable-Naming-History vs Parse-Tree-Structure sub-clause closes the silent state-history-label-driven corner mis-classification pathway by construction at the rule-file level. Parent rule body (§"Observable-Naming-History vs Parse-Tree-Structure" at cross-pillar-bridge-anatomy.md) carries the principle, enforcement, and substrate framing; this corpus row tracks K-counter advancement for the K=3 MANDATORY-promotion event.

### K=2 corpus (S90 W1-7 close)

| # | Instance | State-history surface name | Parse-tree closed form | Structural corner | Source |
|:-:|:---------|:---------------------------|:------------------------|:------------------|:-------|
| 1 | `Var_a(n_a^GGE)` | "GGE" suggests algebra-DEPENDENT | `Σ_a (Δ_BCS²/(2(λ_a²+Δ_BCS²)) − ⟨…⟩)²` (spectrum-only Bogoliubov) | Corner II (algebra-INVARIANT, s=4) | S89 W-3 + W-17 §V.2/V.3 |
| 2 | `α_s_canonical = n_s²−1` | "α_s_canonical" suggests coupling-class | `(Mellin-residue at s=1)² − 1` (spectrum-only) | Corner I (algebra-INVARIANT, s=3) | S87 α-s W2 PASS; §VII.U.1 line 12960 |
| 3 | (RESERVED — future calibration instance, e.g., α_s_route_3 / Δ_M) | — | — | — | (pending S91+ landing) |

K=3 promotion event will fire when a 3rd instance lands (e.g., a §VII entry citing a state-history name whose parse-tree reduces to a previously-unknown corner-cell membership).

### Forward enforcement (audit-script hook from S90 W1-8)

The audit-script hook `MISSING-PARSE-TREE-EXPANSION` at `computations/_shared/_registry_landing_audit.py` (extended in S90 W1-8 = CF-R1-3 paired) is the operational realization of the (3) Enforcement clause. Plan-freeze auditors invoke the hook on any new §VII entry; the hook regex-detects state-history label patterns and flags missing parse-tree expansion at S2 advisory severity.

### Cross-link

- Parent rule sub-clause: `.claude/rules/cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"` (S90 W1-7 LANDED).
- Audit-script enforcement: `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration for new §VII entries"` (S90 W1-8 = CF-R1-3 paired, queued for separate dispatch).
- Algebra-axis orthogonality parent K-counter: `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (S87 W-2 R3 close).
- Source observables: §VII.U.1 (α_s_canonical = n_s²−1, S87 α-s W2 PASS); §VII.U.2 (Var_a Bogoliubov closed form, S89 W-3 + W-17).

## §18. PRU Class 8.7 Degenerate-Observable Pre-Flight Check (S90 W1-12 landing; epistemic-discipline.md §"Pre-Registration Completeness") — calibration corpus

### Status: SUGGESTION at K=1 (promotes to MANDATORY at K=3)

The Degenerate-Observable Pre-Flight Check (Class 8.7) directs that when a gate's
producing script computes `Tr(P · A) − R_CM` or `ζ_D(0)` on a finite spectral
triple with degenerate dimension-spectrum, the plan-block MUST pre-register a
degeneracy-witness (coincident-root declaration + per-pole multiplicity +
compositional-corridor pin). The class lands SUGGESTION-K=1 per
`feedback_rules-compensate-missing-structure.md` K-counter promotion threshold;
promotes to MANDATORY at K=3 distinct calibration-corpus instances.

### K=1 corpus (S90 W1-12 close, 2026-05-13)

| # | Instance | Substrate-physics pattern | Detection | Pre-registration status |
|:-:|:---------|:--------------------------|:----------|:------------------------|
| 1 | S89 §W1-1 `S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION` FAIL (audit_sha256=`6db37f7c6da0768662c5afb320654a54f2e4c478882d365465712034e28a16fe`) | `S_BH^substrate(M=1e7, L_max=10) = Tr_HSS(P_HSS) − R_CM` at substrate-distance-1 pole s=3 of finite spectral triple `(A_K^≤10, H_K^≤10, D_K^≤10)`; CM-1995 §III.4 residue formula on horizon-spanning sub-triple via P_HSS projector | P1 `r'Tr.*\bP_HSS\b.*[−-].*R_CM'` fires (3 matches on plan-w1.md §W1-1) | **NO degeneracy-witness declared in S89 §W1-1 plan-block** — would have flagged Class 8.7 at S2 advisory at S89 plan-freeze had this class been pre-existing |

The S89 §W1-1 FAIL with `value='alpha=-1.590633e-116;...;Tr_HSS=38;R_CM=3.800000e+01;...;monotone=False;K_advance=1to2_BY_CONSTRUCTION'` exhibited the substrate-IS structural pathology this class detects by construction: a naive single-pole CM-1995 §III.4 corridor that discards the multiplicity structure at the LRD-horizon scale (where the dimension-spectrum is degenerate per CM-1995 regular-spectral-triple theorem applicability). The (d)∘(b) compositional corridor per S89 W-1 R3 closure is the substrate-natural disambiguator; pre-registering it as the corridor pin (clause 3 of Class 8.7) at plan-block layer prevents the naive evaluation that produced the FAIL.

### Reserved rows

| # | Reserved-for | Pattern axis |
|:-:|:-------------|:-------------|
| 2 | future instance | Tr(P · A) − R_CM at distinct substrate-distance pole (e.g., s=4 substrate-distance-2) |
| 3 | future instance | `value = ζ_D(0)` direct evaluation OR HKR-image residue trace |

### K-counter advancement

`K_substantive = 1` at S90 W1-12 close (1 distinct calibration-corpus instance: S89 §W1-1). `K_promotion = 3` per `feedback_rules-compensate-missing-structure.md`. `K_substantive < K_promotion` → status remains SUGGESTION-K=1 (advisory until K=3); audit-script emits S2 advisory severity on detected violations until K=3 promotion.

### Forward enforcement (audit-script hook)

`computations/_shared/_pru_cardinality_audit.py` `detect_class_8_7_degenerate_observable(plan_block_text, block_label)` returns structured diagnostic dict with `has_class_8_7_flag`, `severity` (S2 or NONE), `p1_matches`, `p2_matches`, `degeneracy_witness_present`, `degeneracy_witness_markers_found`, `diagnostic`. Plan-freeze auditors invoke the detector on each new gate's plan-block; flag at S2 advisory (HARD-HALT after K=3 promotion).

The detector's positive self-test (S89 §W1-1) and negative self-test (synthetic-with-witness) both PASS at S90 W1-12 close, audit_sha256=`6369a880e2f49b7ec2660e553f0ca91d29f599148b2524b5ba221c20c552e38f`.

### Cross-link

- Parent rule: `.claude/rules/epistemic-discipline.md §"Degenerate-Observable Pre-Flight Check (Class 8.7; advisory until K=3)"`.
- Sub-class taxonomy row: `.claude/rules/epistemic-discipline.md §"PRU Class 8 sub-class taxonomy"` row 8.7.
- Audit script: `computations/_shared/_pru_cardinality_audit.py` `detect_class_8_7_degenerate_observable()`.
- Self-test driver: `computations/_shared/s90_w1_pru_class_8_7_test.py`.
- K=1 calibration instance source: S89 §W1-1 FAIL at `computations/session-89/s89_gate_verdicts.txt:1`; plan-block at `sessions/session-plan/session-89-plan-w1.md` lines 50-150 (HSS-projector trace minus CM regularized mean substrate-physics pattern).
- W6-3 hygiene-gap discharge context: `sessions/archive/session-89/session-89-w6-workingpaper.md` line 363 ("Plan §1.2 listed `_pru_cardinality_audit.py` as 'hard prerequisite'. None of the three existed on disk. W6-1 was built without using `_pru_cardinality_audit.py` as template.") — `_pru_cardinality_audit.py` was created in-session at S90 W1-12 with Class 8.7 as inaugural content per `feedback_fix-in-session-never-defer.md`.

---

## §19. Composite-collapse CORE-vs-fringe override-clause (S97 W-1 mack+volovik composite-collapse adjudication; `gate-verdicts.md` schema-v2 companion) — calibration corpus

> **Provenance**: S97 W-1 iterative workshop `sessions/archive/session-97/workshops/w-1-c10-composite-collapse-adjudication.md` (mack-cosmic-bridge + volovik-superfluid-universe-theorist; converged R2). Records the K=1 calibration instance + the candidate-clause 4-guard form. The clause is a CANDIDATE methodology-rule extension also recorded as housekeeping §D row D1; this corpus section is the calibration-instance home per `feedback_rules-directive-only-no-session-info.md` (session-specific calibration provenance lives in `*-corpus.md`, NEVER in the rule file).

**Status**: **K=1 SUGGESTION** (K=3 promotion contract per `feedback_rules-compensate-missing-structure.md`). NOT minted this session. The candidate clause COMPOSES WITH the `gate-verdicts.md` schema-v2 composite-collapse rule (`elif sign_verdict == FAIL: composite = FAIL`); it does NOT modify it. A post-hoc edit of the collapse rule is a `v3-closure-recovery.md` PROHIBITED_ACTIONS Class-3 violation (the firewall was preserved this session — gate-verdicts.md UNEDITED).

**Candidate clause.** When a gate's schema-v2 3-tuple has `sign_verdict = FAIL` BUT the FAIL is a CORE-confirmed / fringe-violated split (the CORE prediction holds; only a sub-leading / conditional-antecedent / boundary-approach-direction sub-claim fails), the canonical LABEL MAY be overridden to INFO via the gate's pre-registered semantic `INFO_meaning` — provided ALL FOUR guards hold:

- **(i) CORE confirmed** — the gate's primary prediction holds.
- **(ii) conditional-antecedent falsified-not-violated** — what fails is a conditional/sub-leading antecedent, not the CORE claim.
- **(iii) magnitude bounded** — the fringe deviation is bounded, not runaway.
- **(iv) recovery-direction normalization-invariant OR observable declared** (mack's 4th guard) — the boundary-limit recovery DIRECTION (from-below vs from-above) MUST be normalization-invariant before the INFO override fires, OR the gate MUST declare WHICH observable the recovery predicate is about.

The honest 3-tuple scalar (`sign=FAIL`) and the INFO label are SEPARATE pinned objects on orthogonal axes (honest-result axis vs gate-semantic axis); neither overwrites the other; the FAIL stays byte-permanent in the verdict file. This is the (verdict-scalar, canonical-label)-pair generalization of the Option-A supersession discipline to the LABEL layer.

### Calibration instance #1 (inaugural, K=1)

`S97-W2-2-C10-N-EXPONENT` (Volovik q-theory departure exponent `n` in ρ_vac ∼ H^n; C10 discharge test). 3-tuple `sign=FAIL` (n_eff_T61 = 1.978111 < 2) / `magnitude=PASS` (|C_meas|/2 = 0.0109 < 0.05; C_meas = −0.0219) / `regime=VALID`; composite-collapse → FAIL scalar (verdict line 63, audit `b69da9f4da9da1d8…`, Option-A chain `30566894 → 0e6076f3 → b69da9f4`); canonical label INFO via gate semantic.

Four guards verified at W-1: (i) acoustic-leading VALUE n → 2 confirmed (n_leg1 = 2.0000); (ii) the falsified conditional antecedent is the STIFFNESS DIRECTION (sub-acoustic at finite q — the literal one-sided `n_eff ≥ 2` cell, violated 1.978 < 2); (iii) bounded (gap-set Jacobian ceiling dω_n/dq = 1/(2ω_n) ≤ 1/(2|λ_min|) = 0.610 across q > −λ_min² = −0.67198, + Ordered-Veil integrability); (iv) recovery-direction OBSERVABLE-DEPENDENT (from-below for the full-shape exponent `C_meas` vs from-above for the leading-order pressure-response proxy `C_T61 = +0.0297`; `|C_T61/C_meas| = 1.358` same-OOM ⇒ different-ORDER objects, NOT two estimators of one number) — the gate DECLARES it reads `C_meas`, satisfying guard (iv)'s disjunct.

K-counter advances to **K=1**; minting deferred to K=3 (two more structurally-distinct composite-collapse calibration instances required).

### Cross-link

- Companion rule (NOT modified): `.claude/rules/gate-verdicts.md` schema-v2 composite-collapse rule + Option-A supersession pathway.
- Candidate-extension ledger row: `sessions/archive/session-97/session-97-housekeeping.md §D` row D1 (M3-class methodology-rule extension; routed per `Investigating-Workshops.md` Q2, NOT a workshop — both W-1 agents agree on clause content).
- Workshop source: `sessions/archive/session-97/workshops/w-1-c10-composite-collapse-adjudication.md` (Verdict Row 1; Open Questions item 5; EMERGENCE).
- Calibration-instance home discipline: `feedback_rules-directive-only-no-session-info.md` (session calibration → corpus, never rule file).
- K=3 promotion contract: `feedback_rules-compensate-missing-structure.md`.

## §20. Counting Axis (intensive/extensive) — fifth pin-axis calibration corpus (`regulator-pin-discipline.md §"Cross-link — four-axis orthogonality"`)

**Directive home**: `regulator-pin-discipline.md §"Cross-link — four-axis orthogonality"` (fifth table row, Counting axis; Status: SUGGESTION at K=1 → MANDATORY at K=3).

**K=1 calibration instance (S100a W-2 mass-functional counting workshop, 2026-06-07)**:

- **Adjudication**: `sessions/session-100a/workshops/s100a-w2-mass-functional-counting-workshop.md` (baptista × connes, 2R; all 6 verdict topics Converged). Counting convention adjudicated to the multiplicity-normalized channel-STATE class — structural definition: state evaluation ρ_g(f(D)) with ρ_g = P_g/Tr(P_g) (the NCG state axiom; points are normalized states); operational tag `convention=RATIO-NORMALIZED-TRACE-MEAN`. The extensive block-sum (`convention=RATIO-BLOCKSUM`) is the weighted trace n_g·ρ_g(f(D)) — correct for width/degeneracy/occupation/action-moment-class observables, NOT for mass/position-class.
- **Pairwise-independence existence proof (empirical, not asserted)**: `S100a-YUKAWA-OVERLAP-OFFDIAG` (INFO, audit `871573da729c5972…`) PASSed the UV-regulator axis (dual-scheme ratios bit-identical at 2.8e-16, S100a-M0 audit `2993dbf63fcb25d9…`) while silently unpinned on counting — same cache, same scheme, same μ_H — and the heavy-pair (μ/τ) transposition fired anyway (ρ_S = 0.5 against the floor-metric route). A gate can PASS all four prior axes while counting-unpinned.
- **Substrate-analog composition (the axis is a tag, not a winner)**: S92-Var_a is extensive-CORRECT (whole-spectrum thermodynamic moment); S100a-mass is intensive-CORRECT (spectral position). Same substrate, two observable classes, two correct conventions — the axis tag closes the conflation; no counting "wins."
- **K₀-rank reading**: the two classes differ by the channel's K₀-rank factor n_g (topological); the W-2 workshop's C2 section reads the μ/τ transposition as a K₀ rank datum (ln n_g) leaking into a metric observable.
- **Downstream consumer**: the amended `CF-S101-W2-BLOCKTRACE-WIDENING` gate block (landed at `sessions/session-100a/session-100a-w2-workingpaper.md:355`, "AMENDED by W-2 workshop") carries the convention pin + heavy-pair-ordering sub-criterion as the S101 pre-registration.
- K=3 promotion contract: `feedback_rules-compensate-missing-structure.md`. K-counter advances on structurally distinct degenerate-channel functional families, not repeat citations of the Wave-2 pair.

## §21. Multiplicative-normalization cancellation — laboratory-IN pipeline-parameter signature corpus (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`; detector extension)

**Directive home**: `math-scripts.md §"Multiplicative-normalization cancellation invariants"` (MANDATORY at K=3; S94 W6-18 promotion, audit `6284d0d3ac7a85c8174f26c8d1ae8561f4ff89945ae6d86cffb4a8b8ff8fb27e`). **Detector home**: `computations/_shared/_machinery_feasibility_audit.py::detect_multiplicative_cancellation` (S101 W8a-2; three signature classes — `LOG-DERIVATIVE` / `RATIO-OF-PIPELINES` / `VARIANCE-FUNCTIONAL`).

**Axis scope (NON-K-ADVANCING)**: the rule's K-counter counts STRUCTURALLY DISTINCT *spectral-support* factorization mechanisms — `w(L_max)`-truncation (K=1) / `w(τ-moduli)`-deformation (K=2) / `w(C_2^max)`-Casimir-ceiling (K=3) — the weights of the SUBSTRATE functional. The two instances below cancel a *laboratory-IN pipeline parameter* (`G`, `S`) that enters through the emergent-physics reduction pipeline (emergent-Friedmann halo counting; survey capture), NOT through the spectral support of any `D_K` functional. This is a categorically DIFFERENT documentation axis (`cancelling_axis = LAB-IN-PIPELINE`), NOT a fourth spectral-support row. **Both rows are tagged `NON-K-ADVANCING`**: no K-advancement decision is made — the rule is already MANDATORY at K=3, and the lab-IN axis is documented here WITHOUT contaminating the spectral-support K-counter (binding CF text: "corpus append only, no K-advancement decision").

**Detector-blindness motivation**: both instances self-detected only AT EXECUTION in S100b W7 — the rule had no plan-freeze detector before W8a-2. A detector keying only on `LOG-DERIVATIVE` signatures (`d^n ln(.)/d(ln K)^n`) cannot see either: a log-RATIO-of-pipelines is not a log-derivative, and a coefficient-of-variation is not a log-derivative. The S101 W8a-2 detector adds the two NEW signature classes (severity S2 advisory — NEW classes ship at S2; the rule's S1 MANDATORY text binds the spectral-support LOG-DERIVATIVE class it was promoted on; S1-hardening of the new classes is a FUTURE K-decision NOT made here).

### Row 1 — W7-2 C2a G-cancellation (signature class: RATIO-OF-PIPELINES)

- **Gate**: `S100b-A2-HEAVY-SEED-ABUNDANCE` (`computations/session-100b/s100b_gate_verdicts.txt:127`, audit `37f64fcd7e81ef8575b1781b0385d3a0db6bd8a2ba4647790e0a81b7164455c9`).
- **Gated quantity**: `max_z |log10(n_ACH_em/n_ACH_ref)|` is EXACTLY 0 by G-cancellation under the borrowed-`(H_0, Ω, σ_8)` baseline. `M_ACH ~ 1/(G·H)`, `ρ_m,0 ~ 1/G`; the count above a FIXED `T_vir` threshold is G-free. Numerator and denominator pipelines carry the SAME G-scalings (only the em/ref `H(t)` differs); the selection criterion contributes no G ⇒ every G-factor appears identically in both legs ⇒ G cancels in the ratio.
- **Value field on disk**: `C2a_maxdlog_nACH=0.00000dex` (`≤0.5=True`); structural-identity companion row on disk.
- **Substitution chain (exact identity)**: `max_z |log10(n_ACH_em/n_ACH_ref)| == 0` IDENTICALLY in the pure shared-G channel — a STRUCTURAL IDENTITY of the pipeline pair, not an empirical constraint on the substrate.
- **Detector class**: `RATIO-OF-PIPELINES` — `|log10(X_em/X_ref)|` / named two-pipeline ratio CONJOINED with a shared LAB-IN parameter (`G`) in BOTH legs' scalings; `cancelling_axis = LAB-IN-PIPELINE`; severity S2. **Tag: NON-K-ADVANCING.**

### Row 2 — W7-3 A2 flat-S invariance (signature class: VARIANCE-FUNCTIONAL)

- **Gate**: `S100b-STRUCTURE-TIMING-TWO-AXIS` (`computations/session-100b/s100b_gate_verdicts.txt:121`, audit `25002865ff190b5598bf9aa8076d14da0e4a37c35807f05b79a242fbb791478d`).
- **Gated quantity**: a flat multiplicative capture `S` cancels exactly in the fractional count variance (`N -> S·N` leaves `σ_CV` invariant), verified in-run.
- **Substitution chain (exact identity)**: `σ_CV(N) := Std(N)/Mean(N)`; flat capture `N -> S·N` with `S` a single z-independent scalar ⇒ `σ_CV(S·N) = Std(S·N)/Mean(S·N) = (S·Std(N))/(S·Mean(N)) = Std(N)/Mean(N) = σ_CV(N)`. `σ_CV` is INVARIANT under flat `S` — the gated variance criterion carries ZERO sensitivity to the capture normalization; structural identity.
- **Detector class**: `VARIANCE-FUNCTIONAL` — coefficient-of-variation / `Std(N)/Mean(N)` / `σ_CV` CONJOINED with a flat multiplicative capture/completeness parameter in the same block; `cancelling_axis = LAB-IN-PIPELINE`; severity S2. **Tag: NON-K-ADVANCING.**

### Axis claim (why LAB-IN-PIPELINE is a distinct axis)

The rule's K-counter rows are spectral-support weights of the SUBSTRATE functional — `w(L_max)` truncation, `w(τ-moduli)` deformation, `w(C_2^max)` Casimir-ceiling. `G` and `S` enter through the LABORATORY-IN reduction pipeline, NOT the substrate spectral support. Distinct axis by inspection of WHERE the factor enters the functional; hence these rows document a NEW `cancelling_axis` value (`LAB-IN-PIPELINE`) WITHOUT advancing the spectral-support K-counter. Substrate-first direction preserved: the fabric's spectral moments are the fundamental layer; `G` and `S` are parameters of how laboratories read the emergent image, and the detector now sees cancellations on BOTH layers.

**Forward enforcement**: S102+ plan-freeze pipelines run the 3-class detector on every plan file; the `NON-K-ADVANCING` tag prevents downstream K-counter contamination; any future severity hardening of the S2 classes cites the S101 W8a-2 severity pin as the pre-registered baseline.

## §22. Selection-rule pre-flight (math-scripts.md §"Double-Check Logic Before Compute" sub-clause) -- calibration corpus

**Rule home**: `math-scripts.md §"Double-Check Logic Before Compute" -> "Selection-rule pre-flight for pre-registered nonzero matrix elements"`. **Status**: SUGGESTION at K=1 (-> MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`). **Audit hook**: `computations/_shared/_machinery_feasibility_audit.py::detect_selection_rule_preflight` (landed S101 W8a-1; verdict `S101-HK-SELECTION-RULE-PREFLIGHT-AUDIT` PASS).

### K=1 calibration instance -- S100a W2-2 (Yukawa overlap off-diagonal)

The S100a plan-w2 §W2-2 substitution chain asserted `<psi_(1,0)| |s(h)|^2 |psi_(1,1)> != 0` via the rationale "C^2 in su(3) weight connecting triality-adjacent sectors". This is **group-theoretically FALSE**: `|s(h)|^2` is a squared modulus, hence center-character (triality) 0 ALWAYS, so the SU(3) center-Z_3 selection rule annihilates the element to 0 EXACTLY. The cited connecting property belongs to `s(h)` itself (irrep (2,0), triality 2 == -1 mod 3), NOT to `|s(h)|^2`.

Full mod-3 arithmetic table (triality `t(p,q) = (p-q) mod 3`):

| quantity | irrep | triality |
|:---|:---|:---|
| bra psi_(1,0) | (1,0) | t = (1-0) mod 3 = 1 |
| ket psi_(1,1) | (1,1) | t = (1-1) mod 3 = 0 |
| s(h) | (2,0) | t = (2-0) mod 3 = 2 |
| conj(s(h)) | (0,2) | t = (0-2) mod 3 = 1 |
| operator |s(h)|^2 = s*conj(s) | -- | t = (2+1) mod 3 = 0 |

Center-character selection rule: `<a|O|b> != 0` REQUIRES `t(a) == t(b) + t(O) (mod 3)`. Substitute a=(1,0), b=(1,1), O=|s(h)|^2: `1 == 0 + 0 (mod 3)` is **FALSE** => `<(1,0)| |s(h)|^2 |(1,1)> = 0` EXACTLY. Contrast: the bare operator s(h) (t=2) DOES satisfy the necessary check for the (1,0)<->(1,1) pair (`t(1,1) = 0 == t(1,0) + t(s) = 1 + 2 = 3 == 0 mod 3`) -- the connecting property the chain mis-attributed to the squared modulus.

**Disclosure provenance**: caught in-gate and honestly disclosed at plan-freeze -- canonical line `computations/session-100a/s100a_gate_verdicts.txt:36` (gate S100a-YUKAWA-OVERLAP-OFFDIAG, audit `871573da729c59722ee060b37c70741f8d917e2560fe11ef74910f6be3bd2925`); selection-rule companion row `:40` ("literal (1,0)<->(1,1) |s|^2 element=0 exact (center-Z3/triality selection)").

**K-counter**: K=1. Advances on DISTINCT inadmissible-claim catches at plan-freeze (a new theorem / sector pair the detector flags), NOT on re-citations of the W2-2 instance.

## §23. Channel-scope suffix discipline (regulator-pin-discipline.md Extension) -- calibration corpus

**Rule home**: `regulator-pin-discipline.md §"Extension: Channel-Scope Suffix Discipline for Register Citations of Channel-/Parity-Scoped PERMANENT Theorems"`. **Status**: SUGGESTION at K=1 (-> MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`).

### K=1 calibration instance -- S100a W-4 five-surface census

Source: the S100a W-4 D5 seesaw-adjudication workshop `sessions/session-100a/workshops/s100a-w5-d5-seesaw-adjudication-workshop.md` (SHA `d7632f2c6e4e455d02e0640182933fcbac301a8fea2b082218abb2b2d67f0ca5`) -- [AGENDA-6a] FINAL draft + E4 census + V-C6 confirmation + the E-3 2/2-escaped-vs-2/2-caught split. Routing note: housekeeping-100a §D CF-S101-HK-SUFFIX.

The **five-surface census**: five register surfaces were audited for the `S41 W1-2` T-channel `S_F^Connes = 0` citation. Verdict -- the two instances that REACHED registers escaped through consolidation/aggregation steps that dropped the separable scope parenthetical (the over-broad "seesaw = 0" reading regenerated downstream); the two surfaces that carried the scope INSIDE the citation token survived intact (the 2/2-escaped vs 2/2-caught split). Structural mechanism: separable parentheticals do not survive consolidation steps, so scope-inside-the-token makes the wrong reading non-regenerable from the surviving artifact -- the register-side analog of the contrast-inside-the-output pattern.

**K-counter**: K=1. Advances on DISTINCT channel-/parity-scoped PERMANENT theorems (e.g. a new T-/P-channel or gamma9-odd/even theorem receiving the suffix treatment), NOT on repeat citations of S41 W1-2.

## §24. Plan-frozen gate-block operator precedence (gate-verdicts.md §"Composite-collapse rule" companion) -- calibration corpus

**Rule home**: `gate-verdicts.md §"Composite-collapse rule" -> "Plan-frozen gate-block operator precedence (applicability guards)"`. **Status**: SUGGESTION at K=1 (-> MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`). **Adjacent prior**: corpus §19 (Composite-collapse CORE-vs-fringe override-clause) is on a DIFFERENT axis -- §19 overrides a sign=FAIL label via four guards at the gate-semantic layer; THIS clause governs operator-vs-generic-collapse precedence at the plan-freeze layer; both compose with, neither modifies, the collapse rule.

### K=1 calibration instance -- S100b W4-1 (D_K ergodicity, Weyl-applicability guard)

Instance: S100b W4-1 (gate S100b-DK-ERGODICITY, `computations/session-100b/s100b_gate_verdicts.txt:56`, audit `273a0dc45a1e9f2500db5b7548fefed70ab6e7d82c3f4c945dcf9562f945d7ba`). The schema-v2 3-tuple at `:58` is (sign=PASS, magnitude=PASS, regime=MARGINAL); the generic `gate-verdicts.md` composite-collapse reads this via the else-branch as **PASS**. But the plan-frozen W4-1 gate-block operator pre-registered **INFO** on Weyl-applicability failure (the HM Def 2.3 Weyl law on the finite truncation) -- the GUARD, not the hypothesis. The composite-precedence extra-row was pre-declared BEFORE evaluation and is on disk at `:60`: "# composite-precedence: plan SS W4-1 gate-block operator pre-registers INFO on Weyl-applicability failure (guard, not hypothesis); generic gate-verdicts.md collapse of (PASS,PASS,MARGINAL) would read PASS; the plan-specific operator governs the composite".

**Conservative direction**: a hollow PASS was REFUSED in favor of the honest INFO -- the applicability guard failed, so the criterion never tested its hypothesis; awarding PASS would claim more than the truncated spectral functional actually demonstrated.

**K-counter**: K=1. Advances on DISTINCT pre-declared precedence invocations (a new gate whose plan-frozen operator conflicts with the generic collapse and carries the pre-declared extra-row), NOT on re-citations of W4-1.

---

## §25. S110 Investigation-Distillation Methodology-Calibration Entries (HK-METH-CORPUS + HK-W1-3-OPERATOR)

Landed S110 W0 (investigation-distillation Wave-0). Source: `sessions/investigation/_promotion-triage.md` Bucket-3 §A (HK-METH-CORPUS = inv-8 §D / HY11; HK-W1-3-OPERATOR = inv-3 B6 + inv-10 HY-J). Investigation-track calibration data recorded as methodology corpus entries (not substrate-physics promotions; `gate-verdicts.md §"Investigation-Track"`).

### §25.1 Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — inv-8 W1-3 stale 3-channel DM framing

inv-8 W1-3 surfaced a stale Ω_DM "3-channel → 0.844" framing in DM-properties prose. Current canonical: the **two-channel** decomposition (Leggett + dimer_Z2 = 0.276 ≈ Ω_DM; soft-hair = DE), landed via HK-OMEGA-DM (S110, mack). The 3-channel→0.844 is a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE (prose tracked a superseded channel decomposition). Remediation: re-pin to the 2-channel f_DM table (effected S110). Calibration datum for `epistemic-discipline.md §"Source Reconciliation"` Class-(c).

### §25.2 Multiplicative-normalization-cancellation NEGATIVE case — inv-8 W3-3 (FACTORIZATION_HOLDS = False)

inv-8 W3-3 ran the candidate `w(L_max)·g(K)` decomposition pre-flight and found **FACTORIZATION_HOLDS = False** — the L_max-dependence does NOT factor as a multiplicative spectral-support pre-factor for that observable. NEGATIVE calibration datum for `math-scripts.md §"Multiplicative-normalization cancellation invariants"` (MANDATORY at K=3): confirms the Sage-`sage_simplify` factorization pre-flight is discriminating (the log-derivative L_n is NOT automatically L_max-invariant; the FALSE branch fires correctly).

### §25.3 OBSERVATION-FREE falsifier pattern — inv-8 W2-2

inv-8 W2-2 established a falsifier whose prediction is unreachable by any instrument yet still functions as a falsifier (canonical exemplar: η_lab = 1.83e-91 EP, 73 OOM below MICROSCOPE — HK-EP). Pattern: a substrate-IS prediction can be a *falsifier* (killed by any nonzero lab detection) while being OBSERVATION-FREE (no detector reaches it), acting as a permanent structural-consistency anchor rather than a near-term test. Distinguish from detector-horizon falsifiers (which carry σ-distance + detection year).

### §25.4 Morse-non-degeneracy discriminant operator-form (HK-W1-3-OPERATOR; PRU Class-8.2)

inv-3 B6 + inv-10 HY-J. The A₂-fold germ test MUST be pre-registered as the **Morse-non-degeneracy discriminant** — `det H ≠ 0 ∧ |d²λ/dτ²| ≥ tol ∧ ¬cusp` — NOT the literal `n_zero_hess == 1` (a PRU Class-8.2 verifier-rubric operator-form defect: the integer-count form is regulator/truncation-fragile). Forward discipline: deep-truncation rigidity gates pre-register the calibration-valid small-L `Σ²/L` super-factor, NOT the unreachable `slope ≥ 0.7`. Calibration datum for `epistemic-discipline.md §"Verifier-Rubric Pre-Registration (Class 8.2)"`.

### §25.5 Width-aware-guard dispute-ADJUDICATION extension — WS-FLOQUET (S110 W1) inaugural calibration

S110 W1 WS-FLOQUET (transit-dynamics × quantum-acoustics). The S100a-W1-D-2 **width-aware-guard** is promoted in SCOPE from a guard-DESIGN heuristic to a dispute-ADJUDICATION heuristic: *for any parametric-amplification / Floquet-liveness dispute, settle the dimensional identity of whatever occupies the Mathieu-depth slot BEFORE computing the monodromy; the monodromy is confirmation, never the discriminator.* Inaugural instance: the §VII.BP Floquet-liveness dispute (inv-10 "LIVE" vs inv-12 "DEAD") was settled BEFORE any monodromy step — inv-10's `q≈0.504 = 2E_pump/ω_q` (occupation energy per pair, a POPULATED-STATE property) was mis-mapped onto the Mathieu-depth slot, which physically carries `h_par=8.3e-4` (the dimensionless fractional ω²-modulation, a DRIVE property), a ~607× over-assignment; the monodromy (`max|Tr M|=1.99999<2`, `fraction_resonance=0`) then merely CONFIRMED the depth-determined DEAD verdict. Generalizes the §25.4 operator-form discipline to the dimensional-identity-of-the-operated-slot layer (settle WHAT the slot holds before applying the operator). Status: SUGGESTION K=1 (inaugural; promotes per `feedback_rules-compensate-missing-structure.md`). Home: directive scope-extension of `math-scripts.md §"Double-Check Logic Before Compute"`; calibration instance + K-counter here.
