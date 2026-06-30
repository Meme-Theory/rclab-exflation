# Session 88 W18 Synthesis: GEOMETRIC-RESUMMATION ANSATZ vs FIRST-ORDER-LINEAR-ONLY (W6a-51 Closed Form)

**Date**: 2026-05-07
**Agent**: lizzi-spectral-functional-theorist (PRIMARY) — workshop-style adversarial synthesis vs connes-ncg-theorist (counter-position represented from the seed)
**Source Documents**:
- `sessions/archive/session-88/session-88-w6a-workingpaper.md` (lines 1–866)
- `sessions/session-plan/session-88-plan-w6a.md` (lines 1–641)
- `sessions/archive/session-88/workshops/_seed-w6a.md` (lines 1–69; Workshop 1 specification)
- `sessions/permanent-results-registry.md` (slot allocation through §VII.AQ S88 W7b-79; §VII.AR is next-free)
- Agent memory: `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

Authoritative gate verdicts (§W6a-51 INFO; §W6a-52 PASS) are taken as fixed; this synthesis adjudicates the STRUCTURAL READING of the §W6a-51 closed form `slope_A(τ) = c₀/(1−τ/(5π))` — geometric-resummation as substrate-IS structural identity (lizzi reading A) vs first-order-linear-only ansatz with extrapolation pending second-order verification (connes reading B). The discriminator is a pre-registered cross-validation gate at τ = 2·τ_fold = 0.38 with substrate-derived residual predictions distinct between the two readings.

---

## I. Session Outcome

The W6a-51 closed form `slope_A(τ) = c₀/(1−τ/(5π))` lands as STAGE-1-CANDIDATE at registry slot **§VII.AR — STAGE-1-CANDIDATE**, but with a STRUCTURALLY OPEN QUESTION on the geometric-resummation reading. The Workshop-1 verdict adjudicates: (i) the form is **algebra-INVARIANT** (spectrum-only functional family per algebra-axis orthogonality MANDATORY at K=3), but its all-orders extension to `1/(1−ε)` is structurally EARNED only at first order in τ from CM-1995 §III.4 + CM-1995 Proposition III.6 pole-LOCATION stability; (ii) at the present empirical residual `5.23e-05` at τ_fold = 0.19, neither pure-linear (predicted 1.46e-3 upper bound; ratio 0.036) nor pure-geometric-cubic (predicted 1.77e-5; ratio 2.96) is canonically selected — the residual lies BETWEEN the two predictions; (iii) the discriminator at τ = 2·τ_fold = 0.38 cleanly separates the readings via the residual ratio `R(0.38)/R(0.19)`: Reading A (geometric) predicts ratio = 8; Reading B (linear-only) predicts ratio = 4. **GO** on STAGE-1-CANDIDATE landing at §VII.AR with the closed form recorded under DUAL-READING-PARAMETERIZED form, an INFO-band caveat naming the τ=0.38 cross-validation gate as the structural decider, and a `slope_A_FW` canonical_constants entry as a parameterized closed-form pin with explicit Level-2 algebraic-envelope validity declaration `O(τ²) ≤ ε²·c₀ ≈ 1.46e-3` at τ_fold.

---

## II. Key Results

### II.1 Algebra-axis classification of the geometric-resummation form (Workshop-1 Adjudication Question (b))

**Result**: The closed form `slope_A(τ) = c₀/(1−τ/(5π))` is **algebra-INVARIANT** (spectrum-only functional family). Classification: GEOMETRIC.

The form's coefficients (`c₀ ∈ {10, 5}`, `5π`) are PURE GROUP-THEORETIC numbers from SU(3) Lie theory (Peter-Weyl `(dim+rank)/2`) and the Plancherel/Haar measure on the compact symmetric space SU(3)/T (Helgason Ch. X). They are determined entirely by the spectrum `{λ_k(τ), m_k(τ)}` of `D_K(τ)` via CM-1995 §III.4 residue extraction; no state-pair functional on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` enters the closed-form coefficients. Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (MANDATORY at K=3 per S87 W-2 R3 close), this places the form in the **algebra-INVARIANT corner** of the 4-corner classification — extends pole-universally; extends to all algebra families that share the same SU(3) Cartan-root system.

What the algebra-INVARIANT classification DOES guarantee: regulator-class invariance is structurally exact at finite spectral triples (verified empirically at `regulator_invariance_residual = 0.000e+00` Sage-symbolic; verified structurally at clause (f) of W6a-51 connes co-sign via Hardy-Littlewood / Apostol Ch. 11 Dirichlet-series uniqueness on finite spectral data). The closed form's coefficients are FORCED by group-theoretic data, not chosen by regulator convention.

What the algebra-INVARIANT classification DOES NOT guarantee: that the geometric-resummation `1/(1−ε)` extends to all orders in τ. Algebra-INVARIANT is a property of the FUNCTIONAL FAMILY, not of the SUMMATION FORM. The substrate may admit a closed form `slope_A(τ) = (sum over multi-root corrections)` whose leading τ→0 behavior is `c₀·[1 + ε + κ_2·ε² + κ_3·ε³ + …]` with `κ_n ≠ 1` for `n ≥ 2`. The geometric resummation `1/(1−ε)` corresponds to the SPECIAL CASE `κ_n = 1` for all n. Whether this special case is physically realized is the substantive Workshop-1 tension.

### II.2 Substitution-chain step-level analysis at WP §10 Step 6 (Workshop-1 Adjudication Question (c))

**Result**: The transition `linear → geometric_resummation` at WP §10 Step 6 is a **NOTATIONAL SHORTCUT** at first order in τ; the structural identity at the spectral-triple level requires explicit second-order resolvent verification. PARTIAL_STRUCTURAL identity, not full structural identity.

Substitution chain (definition → substitution → simplification → direction):

```
Definition 1: ε(τ) := τ/(5π)
Definition 2: F_lin(τ) := c₀·(1 + ε)                            [CM-1995 §III.4 first-order resolvent only]
Definition 3: F_geom(τ) := c₀/(1 − ε)                            [geometric-resummation closed form]
Definition 4: F_substrate(τ) := c₀·[1 + ε + κ_2·ε² + κ_3·ε³ + …] [substrate-IS Taylor expansion]

Step 1 — Taylor expansion of F_geom in ε:
  F_geom(τ) = c₀·(1 + ε + ε² + ε³ + …)        (geometric series for |ε| < 1)

Step 2 — Substrate-IS multi-root corrections at higher order:
  CM-1995 §III.4 first-order resolvent gives only ε¹ coefficient = 1.
  The ε² coefficient in F_substrate requires the SECOND-order resolvent expansion
  (CM-1995 Proposition III.6 stabilizes pole LOCATIONS but not pole RESIDUES at all orders).
  ⇒ κ_2_substrate is NOT determined by CM-1995 §III.4 first-order alone.

Step 3 — Match-test: F_geom = F_substrate iff κ_n = 1 for all n ≥ 2.
  κ_2 = 1 is consistent with geometric resummation.
  κ_n = 1 for all n is the SPECIAL CASE.

Step 4 — Direction (substrate-IS):
  F_geom and F_lin agree at O(ε¹); they DIFFER starting at O(ε²).
  The transition `F_lin → F_geom` at WP §10 Step 6 is justified ONLY at first order.
  At second order, the identity holds STRUCTURALLY iff κ_2_substrate = 1; otherwise the
  "geometric resummation" is a notational shortcut to a DIFFERENT closed form that agrees
  only at O(ε¹).

Conclusion: the transition is NOTATIONAL-SHORTCUT-AT-FIRST-ORDER; the structural identity
at the spectral-triple level requires explicit second-order resolvent computation
(CF-1 `S89-JENSEN-DIM-SPECTRUM-HIGHER-ORDER-RESOLVENT`) to determine κ_2_substrate.
```

This conclusion does NOT invalidate the §W6a-51 INFO landing — the empirical residual `5.23e-5` is consistent with a small-but-nonzero deviation from the strict geometric form, and INFO is the correct verdict for "approximately matches but with structural truncation correction at O(τ²)" per plan §11. It DOES qualify the closed form: at its current epistemic status, `slope_A(τ) = c₀/(1−τ/(5π))` is a **leading-order substrate prediction** with O(τ²) Jensen-deformation correction, not yet a substrate-IS exact closed form.

### II.3 Discriminating predicate at τ = 2·τ_fold = 0.38 (Workshop-1 Adjudication Question (d))

**Result**: The empirical residual ratio `R(0.38)/R(0.19)` discriminates the two readings at machine-discriminable precision. Pre-registered S89 cross-validation gate.

Substitution chain (verified via Python):

```
Definition 1: ε_τ := τ/(5π)
Definition 2: residual(τ) := |closed_form(τ) − HKR-bridge-image(τ)|
Definition 3: A-reading: residual scales as ε³·c₀  (geometric-cubic ⇒ O(τ³))
Definition 4: B-reading: residual scales as ε²·c₀  (linear-only ⇒ O(τ²))

Step 1 — At τ = 0.19, ε(0.19) = 1.2096e-2 (verified Python).
  Observed residual_A = 5.230238e-05.
  ε² · c₀ = 1.463e-3                 ⇒ κ_2 = 0.0357 (Reading-B pin)
  ε³ · c₀ = 1.770e-5                 ⇒ κ_3 = 2.96   (Reading-A pin)

Step 2 — At τ = 0.38, ε(0.38) = 2·ε(0.19) = 2.4192e-2 (verified Python).
  Reading-A predicted residual at 0.38: κ_3 · ε(0.38)³ · c₀ = 4.184e-04 (verified)
  Reading-B predicted residual at 0.38: κ_2 · ε(0.38)² · c₀ = 2.092e-04 (verified)

Step 3 — Ratio R(0.38)/R(0.19):
  Reading-A: 2³ = 8.000  (geometric-cubic; ε scales linearly with τ)
  Reading-B: 2² = 4.000  (linear-only; ε scales linearly with τ)

Step 4 — Discriminator threshold pre-registration:
  PASS-A   (Reading-A wins): |ratio − 8.0| < 1.0
  PASS-B   (Reading-B wins): |ratio − 4.0| < 0.5
  INFO-band (intermediate): ratio ∈ (5, 7)
  FAIL-band (neither reading): ratio outside [3.5, 9.0]

Direction: the substrate prediction is unambiguous at the ratio level — observation at
τ = 0.38 either matches the geometric-cubic scaling (Reading A wins; geometric-resummation
form is empirically supported at second order) or the linear-only scaling (Reading B wins;
the closed form must be downgraded to linear-LO + O(τ²) caveat).
```

The two readings make EMPIRICALLY DISCRIMINABLE predictions (ratio 8 vs ratio 4; predicted-residual gap at τ=0.38 is `4.184e-4 − 2.092e-4 = 2.092e-4`, nominally a 100% gap on the residual at the same τ point). The Reading-A predicted residual at τ=0.38 is empirically SMALLER (4.18e-4) than Reading-B's (2.09e-4) is FALSE — Reading-A is LARGER (4.18e-4 > 2.09e-4) because R∝ε³ vs R∝ε² and ε is small but the κ pins differ more in magnitude (κ_3≈2.96 vs κ_2≈0.0357; the ε³·κ_3 term dominates ε²·κ_2 at the κ-ratio scale ~83 versus ε-ratio ~0.024). Since both readings are pinned to the SAME observed residual at τ=0.19, the discriminator is simply the SCALING (ratio 8 vs 4), not the absolute predicted value at the new τ point.

### II.4 STAGE-1-CANDIDATE eligibility and §VII.AR registry text (Workshop-1 Adjudication Question (e))

**Result**: STAGE-1-CANDIDATE eligibility is **PRESERVED** for the closed form, but the STAGE-1 entry text MUST encode the dual-reading parameterization. The JOINT clause (c)+(d) "closed-form `slope_A(τ)` derivation matching W1b-3 anchors" remains valid — both readings agree at first order, so the W1b-3 anchor match at INFO band is satisfied under EITHER reading.

The structural reason STAGE-1-CANDIDATE survives Reading-B is: the closed form `slope_A(τ) = c₀·(1 + τ/(5π) + O(τ²))` (Reading B's first-order-linear-only form) ALSO matches the W1b-3 anchor at INFO band (residual 5.23e-5 at τ_fold). Reading B is a STRICTLY SHORTER closed form than Reading A — it claims less, not more — so it satisfies all W6a-51 verdict criteria identically. STAGE-1-CANDIDATE is the LEADING-ORDER substrate prediction; both readings produce the same leading-order content. The DISTINCTION between readings only matters at O(ε²) and higher, which is precisely what the §VII.AR caveat names.

What the §VII.AR registry text MUST include:
1. Closed-form expression with explicit DUAL-READING parameterization (Reading A: geometric resummation `1/(1−ε)` valid to all orders; Reading B: linear-LO `1+ε` valid to first order, with O(τ²) caveat)
2. Algebra-axis classification: algebra-INVARIANT (spectrum-only functional family) per cross-pillar-bridge-anatomy.md K=3 MANDATORY
3. INFO-band cross-validation gate `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD` pre-registered in the registry-row text with the discriminating ratio threshold (PASS-A: ratio ≈ 8 ± 1; PASS-B: ratio ≈ 4 ± 0.5)
4. Empirical anchor: residuals 5.23e-5 (Conv-A) / 2.62e-5 (Conv-B) within INFO band [1e-9, 1e-3]
5. Joint authorship attribution per W6a-51 plan §4: clauses (a)/(c)/(d)/(e) lizzi-side or JOINT, clauses (b)/(f) connes-side
6. Substrate-IS Level-2 (moduli-deformation) tag per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`

### II.5 Updated `slope_A_FW` canonical_constants entry specification

**Result**: Promote as **PARAMETERIZED CLOSED-FORM PIN** with explicit regime-of-validity declaration, NOT a scalar pin at τ=τ_fold. Classification: GEOMETRIC.

The canonical_constants entry recommended specification:

```python
slope_A_FW_Conv_A_LO       = "10.0 * (1 + tau/(5*pi))"     # First-order linear-LO
slope_A_FW_Conv_A_GEOMETRIC = "10.0 / (1 - tau/(5*pi))"    # Geometric-resummation (Reading A)
slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384            # Sage-symbolic CM-1995 §III.4 evaluation at τ_fold
                                                          # = 10.0 / (1 - 0.19/(5*pi))
                                                          # Conv-B counterparts: divide by 2.

# Regime of validity:
#   |ε| := |τ/(5π)| ≪ 1 (substrate-IS small-deformation regime)
#   At τ_fold = 0.19, ε ≈ 0.012 (well within unit radius)
#   First-order accuracy: O(τ²) ≤ ε²·c₀ ≈ 1.46e-3 at τ_fold
#   Second-order accuracy (Reading A): O(τ³) ≤ ε³·c₀ ≈ 1.77e-5 at τ_fold (UNVERIFIED)

# Reading-discriminator status (S88 W6a-51 INFO; pending S89 cross-validation at τ=0.38):
#   Reading A (geometric-resummation): R(τ) ∝ ε³·c₀  (predicts ratio R(0.38)/R(0.19) = 8)
#   Reading B (linear-only):           R(τ) ∝ ε²·c₀  (predicts ratio R(0.38)/R(0.19) = 4)
#   Empirical residual at τ_fold = 5.230238e-05 (Conv-A) / 2.615119e-05 (Conv-B)
#   Discriminator gate: S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD (CF V.3 below)
```

The parameterized form preserves both readings at the canonical-constants level while pinning the actual numerical evaluation at τ_fold to the value computed via Sage-symbolic CM-1995 §III.4 (which is the agreed value across both readings at first order). Downstream consumers cite `slope_A_FW_Conv_A_AT_TAU_FOLD` for τ=τ_fold; consumers needing τ-functional dependence cite the parameterized form explicitly with a regime caveat.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W6a-51 `S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION` | INFO (sign=PASS · magnitude=INFO · regime=VALID) | anchor_residual_A = 5.230238e-05 (in INFO band [1e-9, 1e-3]); regulator_invariance_residual = 0.000e+00 EXACT; doubling_identity_residual = 0.000e+00 EXACT; closed form `slope_A(τ) = c₀/(1−τ/(5π))` with c₀ ∈ {10, 5}; audit_sha256 = 574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e |
| §W6a-52 `S88-DIM-PLUS-RANK-OVER-2-PREFACTOR-DERIVATION` (cross-link, not adjudicated here) | PASS (sign=PASS · magnitude=PASS · regime=VALID) | formula_residual = 0.000e+00 EXACT in ℚ[N]; SU(N) closed form `(N−1)(N+2)/2`; audit_sha256 = 05c4cabb0952bb27ef8466f2d068300866347f1b2d1b6e32b49578c1a9d34593 |
| **Workshop-1 Structural Verdict** (this synthesis) | **STAGE-1-CANDIDATE LANDING APPROVED at §VII.AR with dual-reading parameterization + S89 discriminator gate pre-registered** | Reading-A predicted residual at τ=0.38: 4.18e-4 (ratio 8); Reading-B predicted residual at τ=0.38: 2.09e-4 (ratio 4); discriminator threshold `|ratio−8| < 1.0` (Reading A wins) or `|ratio−4| < 0.5` (Reading B wins) |

The §W6a-51 + §W6a-52 verdicts are taken as authoritative from source documents and not re-adjudicated here. The Workshop-1 STRUCTURAL VERDICT is the new pinned position from this synthesis: the closed form's STAGE-1-CANDIDATE eligibility survives Reading-B; the registry-text MUST encode dual-reading parameterization; the discriminator at τ=0.38 is the empirical decider.

---

## IV. Structural Implications

### IV.1 §VII.AR registry slot allocation

The §VII registry is allocated through §VII.AQ (S88 W7b-79 STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE). Next-free top-level letter is **§VII.AR** (verified via Grep on `permanent-results-registry.md` for `^## §VII\.A[R-Z]` returning no matches; `^## §VII\.[B-Z][A-Z]` returns only `§VII.PROP` outside the AA–AQ alphabet sweep). Mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` performs the §VII.AR registry edit at the carry-forward landing.

The §VII.AR entry is a CO-PRIMARY landing per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"`:
- ANCHOR-1 (input layer V): CM-1995 §III.4 dimension-spectrum residue formula + Cartan-positive-root sum on SU(3) hypercharge (`Σ_{α∈Δ⁺} ⟨α,Y⟩²/|α|² = 1`) + Plancherel/Haar measure on SU(3)/T (Helgason Ch. X)
- ANCHOR-2 (output layer C): Wiener-Ikehara tauberian theorem on `N(L; τ) ~ A·L^{slope_A(τ)}` + first-order resolvent expansion `(D_can + τK)^{−2s} = D_can^{−2s} − 2sτ·D_can^{−2s−1}·K + O(τ²)`
- STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY (sequential V→C chain; V supplies the substrate-IS group-theoretic premise, C supplies the analytic theorem extracting the bulk-Weyl exponent from the perturbed spectrum)
- Closure SHA pin: §W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e`

### IV.2 Three-Level structural-confidence ladder per cross-pillar-bridge-anatomy.md

The W6a-51 closed form participates in the **FWD-C1 Pillar I ↔ Pillar II forward bridge candidate** per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates for S88+ dispatch"`. Three-Level annotation for the §VII.AR registry text:

- **Level 1 (cohomology-class identity)**: regulator-invariant identity at the axiom layer. Empirical Sage-symbolic `regulator_invariance_residual = 0.000e+00` confirms regulator-class invariance is structurally exact at finite spectral triples (Hardy-Littlewood / Apostol Ch. 11 Dirichlet-series uniqueness; no Mellin / Pauli-Villars / zeta variation in the closed-form coefficients). Identity: `slope_A(τ) = c₀/(1−τ/(5π))` with c₀ ∈ {10, 5} regulator-class-invariant by construction.
- **Level 2 (algebraic envelope)**: O(τ²) correction term magnitude bound. At τ_fold = 0.19, `ε² · c₀ = 1.463e-3` (linear-LO upper bound, Reading B); `ε³ · c₀ = 1.77e-5` (geometric-cubic prediction, Reading A). The empirical residual 5.23e-5 sits BETWEEN these two bounds; it satisfies the linear-LO envelope (5.23e-5 < 1.46e-3, ratio 0.036) but EXCEEDS the geometric-cubic prediction (5.23e-5 > 1.77e-5, ratio 2.96). The Level-2 envelope status is therefore **READING-DEPENDENT**: under Reading B, the empirical residual lies safely below the algebraic envelope; under Reading A, the empirical residual exceeds the geometric-cubic prediction by a factor ~3, indicating sub-leading multi-root corrections (κ_3 = 2.96 ≠ 1 in the Reading-A pin).
- **Level 3 (empirical anchor at canonical L_max)**: residuals 5.230238e-05 (Conv-A) and 2.615119e-05 (Conv-B) at L_max=14 Richardson `L^{-3}` extrapolation. Both within INFO band; Conv-A = 2·Conv-B exact (doubling identity preserved at residual level).

Per cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction (S88 W8-88 hardening)": this is **Level-2-binding** (the algebraic envelope `ε² · c₀` describes the convergence rate of the HKR `L_max → ∞` map binding the substrate-IS finite-L closed form to the Pillar-II laboratory-IN Richardson extrapolation; not a substrate-internal Mellin-truncation rate). Registry-PASS criterion `Level-3 < Level-2 envelope at canonical L_max` HOLDS under Reading B (linear-LO envelope) and is INDETERMINATE under Reading A (geometric-cubic prediction is a tighter inner-envelope ratio that the empirical residual exceeds, but Reading A admits sub-leading multi-root corrections that absorb the discrepancy).

### IV.3 Constraint-map updates (extension of WP §"Constraint-Map Updates")

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:--------------|:------------|:----------|:-------|
| 2026-05-07 | W6a-51 closed-form structural reading | UNDETERMINED between Reading A (geometric resummation as substrate-IS structural) vs Reading B (first-order-linear-only ansatz) | DUAL-READING-PARAMETERIZED — both readings produce the same leading-order content matching W1b-3 anchor at INFO band; discriminator at τ=0.38 pre-registered as S89 cross-validation gate | Workshop-1 (this synthesis) substitution-chain analysis: F_geom and F_lin agree at O(ε¹); differ at O(ε²); empirical residual at τ_fold = 5.23e-5 sits between the two predictions |
| 2026-05-07 | Algebra-axis classification of `slope_A(τ)` | UNDECLARED | algebra-INVARIANT (spectrum-only functional family) per cross-pillar-bridge-anatomy.md K=3 MANDATORY | Group-theoretic coefficients (c₀ from Peter-Weyl, 5π from Cartan-root sum + Plancherel) are determined by spectrum alone; no state-pair functional enters |
| 2026-05-07 | §VII.AR registry slot | unallocated | RESERVED for STAGE-1-CANDIDATE landing of joint theorem `slope_A(τ) = c₀/(1−τ/(5π))` with dual-reading parameterization + S89 discriminator gate pre-registered | Workshop-1 STRUCTURAL VERDICT; mack-cosmic-bridge sole-writer landing CF V.1 |
| 2026-05-07 | `slope_A_FW` canonical_constants entry specification | OPEN (carry-forward CF-6 from W6a synthesis) | PARAMETERIZED CLOSED-FORM PIN with explicit regime-of-validity declaration (NOT scalar pin at τ_fold) | Workshop-1 II.5; preserves both readings at canonical-constants level; downstream consumers cite parameterized form with regime caveat |
| 2026-05-07 | Discriminator at τ = 2·τ_fold = 0.38 | UNDEFINED | Pre-registered as `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD` (CF V.3) with PASS-A: |ratio−8| < 1.0 (Reading A wins); PASS-B: |ratio−4| < 0.5 (Reading B wins); INFO-band: ratio ∈ (5,7); FAIL: outside [3.5, 9.0] | Workshop-1 II.3; substrate-derived predictions at machine-discriminable gap |

### IV.4 What this changes about the FWD-C1 unblocking claim (cross-link to Workshop-3 of seed)

Workshop-1's structural verdict (this synthesis) is INDEPENDENT of Workshop-3's Class-(f) vs PRU Class 8.3 adjudication. Both readings (A and B) produce the same INFO-band landing for §W6a-51; both readings produce the same `slope_A_FW(τ_fold) = 10.122438748384` (Conv-A) substrate-first canonical at the τ_fold evaluation point. The Workshop-3 question (does Class-(f) substitution suffice for FWD-C1 unblocking when D_max = 4.12 OOM HARD-HALT band against the plan-pre-registered `≈4e-9`?) is structurally orthogonal to Workshop-1's reading-discriminator question.

That said, the dual-reading parameterization recommended in this synthesis (II.5) is COMPATIBLE with both Workshop-3 readings:
- Under mack reading (Class-(f) substitution sufficient): the parameterized canonical pin is canonical-promotable at INFO; downstream FWD-C1 retry consumes the parameterized form
- Under lizzi reading (PRU Class 8.3 HARD-HALT bypass requires Workshop-1 closure first): Workshop-1 IS THIS SYNTHESIS, and the CF V.3 discriminator at τ=0.38 is the structural decider; once the discriminator returns, the canonical pin is updated to the winning reading; FWD-C1 retry then consumes the winning-reading-specific canonical

The dual-reading parameterization defers Workshop-3's binary choice (mack INFO-eligible vs lizzi HARD-HALT) by encoding both readings at the canonical-constants level until the discriminator returns. This is structurally honest about the open Workshop-1 question without blocking the FWD-C1 unblocking pathway under either Workshop-3 reading.

---

## V. Carry-Forward Computations

V.1. **Land §VII.AR STAGE-1-CANDIDATE registry entry for W6a-51 closed form (DUAL-READING-PARAMETERIZED)**
   - **What**: Land §VII.AR STAGE-1-CANDIDATE entry at `sessions/permanent-results-registry.md` for the joint theorem `slope_A(τ) = c₀/(1−τ/(5π))` with explicit dual-reading parameterization (Reading A: geometric-resummation as substrate-IS structural identity, requires κ_2_substrate = 1 verification at second order; Reading B: first-order-linear-only ansatz, valid to O(τ¹), with O(τ²) caveat). Registry text MUST include: (i) algebra-axis classification (algebra-INVARIANT, spectrum-only family); (ii) Three-Level ladder annotation (Level 1: cohomology-class identity regulator-invariant; Level 2: algebraic envelope reading-dependent; Level 3: empirical anchor 5.23e-5 / 2.62e-5 in INFO band); (iii) S89 discriminator gate pre-registered; (iv) joint clause attribution per W6a-51 plan §4; (v) substrate-IS Level-2 (moduli-deformation) tag.
   - **Inputs**: §W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e` + content_sha256 `612cc1d44dc2d62339922fc84dba7a773bd859d331b9becd46a963f60d140a1b`; connes-ncg co-sign verdict at WP lines 278–411; cross-link to §W6a-52 STAGE-1-CANDIDATE per cross-gate algebraic chain `5π = (dim+rank)/2 · π_Plancherel`; this Workshop-1 synthesis SHA (computed at landing); registry-landing.md SOURCE-DOUBLE-CITE-CO-PRIMARY structure; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`.
   - **Gate**: `S89-W6A-51-DUAL-READING-STAGE-1-LANDING` PASS criterion = §VII.AR entry contains all 5 required elements (i)–(v) above AND STAGE-1-CANDIDATE tag on theorem-name line AND SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure verbatim per registry-landing.md AND the discriminator gate `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD` is explicitly pre-registered in the registry-row text with PASS-A / PASS-B / INFO-band / FAIL thresholds.
   - **Effort**: ~0.3 wave-equivalents (mack-cosmic-bridge single-row write, registry-row text only; no new computation).

V.2. **Pre-register `slope_A_FW` parameterized canonical_constants entry (DUAL-READING)**
   - **What**: Promote `slope_A_FW_Conv_A` and `slope_A_FW_Conv_B` to `canonical_constants.py` as PARAMETERIZED CLOSED-FORM PINS (string expressions evaluable at runtime: `"10.0 * (1 + tau/(5*pi))"` for linear-LO; `"10.0 / (1 - tau/(5*pi))"` for geometric; Conv-B = Conv-A / 2) PLUS scalar pins at τ_fold (`slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384`, `slope_A_FW_Conv_B_AT_TAU_FOLD = 5.061219374192`). PROVENANCE block MUST cite Workshop-1 synthesis SHA + §W6a-51 audit_sha256 + dual-reading regime-of-validity declaration + Reading-A/Reading-B distinction at O(τ²).
   - **Inputs**: §W6a-51 INFO verdict; Workshop-1 II.5 specification; `update_constant` MCP call with provenance keyword `S88-W6A-51-WORKSHOP-1-DUAL-READING`; existing `tau_fold = 0.19` canonical pin.
   - **Gate**: `S89-SLOPE-A-FW-CANONICAL-PROMOTION` PASS criterion = canonical_constants.py contains parameterized pins + scalar-at-τ_fold pins + PROVENANCE block citing both readings + regime-of-validity declaration; verified via `mcp__knowledge__get_constant("slope_A_FW_Conv_A")` returning the parameterized expression; downstream import test `from canonical_constants import slope_A_FW_Conv_A_AT_TAU_FOLD` succeeds.
   - **Effort**: ~0.2 wave-equivalents (single canonical_constants.py edit + provenance entry + import test).

V.3. **S89 discriminator cross-validation gate at τ = 2·τ_fold = 0.38**
   - **What**: Compute the §W6a-51 closed-form `slope_A(0.38) = c₀/(1−0.38/(5π))` and the laboratory-IN HKR-bridge image (Richardson `L^{−3}` extrapolation of finite-L bulk-Weyl exponent) at τ = 0.38 via the same protocol as S87 W1b-3 (spectrum cache regen at τ = 0.38 at L_max ∈ {10, 11, 12, 14}; Richardson extrapolation; bulk-Weyl exponent extraction). Compute residual `R(0.38) = |slope_A_closed_form(0.38) − slope_A_richardson(0.38)|` and ratio `R(0.38)/R(0.19)`. Adjudicate Reading A (geometric) vs Reading B (linear-only) per pre-registered thresholds. Verified Python predictions: Reading A predicted residual at τ=0.38 = 4.184e-4 (ratio 8); Reading B predicted residual at τ=0.38 = 2.092e-4 (ratio 4). Substitution chain: see §II.3 of this synthesis.
   - **Inputs**: §W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e`; W1b-3 Richardson protocol at S87 audit `e2f924e52689630b…` + `237a2d590b05c273…`; spectrum cache regeneration script `s88_w6a_jensen_dim_spectrum_first_principles.py` modified to evaluate at τ = 0.38; `tau_fold = 0.19` canonical pin (× 2 for τ = 0.38 substitution); `slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384` baseline; `kappa_3_lizzi_pin = 2.9554` and `kappa_2_connes_pin = 0.0357` (verified Python; substitution chain II.3); empirical Reading-A and Reading-B prediction values at τ = 0.38 (4.184e-4 / 2.092e-4 verified Python).
   - **Gate**: `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD` with PASS-A: `|ratio − 8.0| < 1.0` (Reading A wins; geometric resummation empirically supported at second order; STAGE-1-CANDIDATE registry text revised to state Reading A wins; canonical_constants `slope_A_FW_Conv_A` retains geometric form); PASS-B: `|ratio − 4.0| < 0.5` (Reading B wins; closed form downgraded to linear-LO + O(τ²) caveat; STAGE-1-CANDIDATE registry text revised to state Reading B wins; canonical_constants `slope_A_FW_Conv_A` retains linear-LO form only); INFO-band: ratio ∈ (5,7) (intermediate; Workshop-1 returns to R3 round with sub-leading multi-root corrections κ_2, κ_3 simultaneously fit; routes to CF-1 `S89-JENSEN-DIM-SPECTRUM-HIGHER-ORDER-RESOLVENT` pre-completion); FAIL: ratio outside [3.5, 9.0] (closed-form structurally invalidated; routes to STAGE-1-CANDIDATE demotion + diagnostic deferral). Trigger: `[VERIFY]`.
   - **Effort**: ~1.0 wave-equivalents (spectrum cache regen at new τ = 0.38 point at L_max ∈ {10, 11, 12, 14} per S87 W1b-3 protocol; Richardson extrapolation; bulk-Weyl exponent extraction; ratio computation; verdict-line emission per S87 schema-v2 dual-SHA + 3-tuple companion).

V.4. **Higher-order resolvent expansion at O(τ²) per CF-1 of W6a synthesis (cross-link)**
   - **What**: Compute the O(τ²) Jensen-deformation coefficient `κ_2_substrate` in the second-order resolvent expansion `(D_can + τK)^{−2s} = D_can^{−2s} − 2sτ·D_can^{−2s−1}·K + (τ²/2)·d²/dτ²[(D_can+τK)^{−2s}]_{τ=0} + O(τ³)`. Apply CM-1995 §III.4 residue extraction at second order to derive the corresponding correction to `slope_A(τ)` at O(τ²). Specifically: derive whether κ_2_substrate = 1 (geometric-resummation reading wins at second order) or κ_2_substrate ≠ 1 (linear-LO ansatz needs explicit corrections beyond geometric form).
   - **Inputs**: §W6a-51 audit_sha256 `574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e`; CM-1995 §III.4 + Proposition III.6 (pole-LOCATION stability under bounded perturbation); s84 spectrum cache `s84_spectrum_cache_L12_tau019.npz` for cross-validation; Sage MCP `sage_eval` + `sage_simplify` for second-order resolvent algebra; canonical_constants pins `dim_SU3 = 8`, `rank_SU3 = 2`, `delta_plus_SU3 = 3`, Cartan-positive-root sum identity `Σ_{α∈Δ⁺} ⟨α,Y⟩²/|α|² = 1` on SU(3) hypercharge.
   - **Gate**: `S89-JENSEN-DIM-SPECTRUM-HIGHER-ORDER-RESOLVENT` with PASS-A criterion = `|κ_2_substrate − 1| < 1e-9` (geometric-resummation form holds at second order, Reading A confirmed); PASS-B criterion = `|κ_2_substrate − 1| ≥ 1e-3 AND κ_2_substrate is determinate` (linear-LO form must add explicit O(τ²) correction term `c₀·κ_2_substrate·ε²`, Reading B confirmed); INFO criterion = `κ_2_substrate ∈ [1−1e-3, 1−1e-9]` (geometric-resummation approximately holds at second order with sub-leading corrections); FAIL = computation does not converge or gives inconsistent results across regulator schemes.
   - **Effort**: ~0.8 wave-equivalents (Sage-symbolic complexity at second order in τ; pole-by-pole residue extraction at s ∈ {(d−n)/2 : n ∈ {0,2,4,6,8}}; cross-regulator verification {zeta, Pauli-Villars, Mellin-Barnes}).

V.5. **Stage-2 cross-axis independent-verify of §VII.AR STAGE-1-CANDIDATE**
   - **What**: Stage-2 PASS-AND verification per `joint-theorem-promotion.md §"Stage 2"` of the §VII.AR STAGE-1-CANDIDATE registry entry. TWO independent cross-reviewers, ONE per axis: (Axis A spectral-functional) audits clauses (a) + (c) JOINT + (d) JOINT + (e); (Axis B NCG-axiomatic) audits clauses (b) + (c) JOINT + (d) JOINT + (f). NEITHER cross-reviewer is lizzi-spectral-functional-theorist (PRIMARY of W6a-51) or connes-ncg-theorist (CO-AUTHOR); both receive ONLY the registered §VII.AR text + relevant input files; do NOT receive the W6a-51 workshop / WP transcripts or this Workshop-1 synthesis. Cross-reviewers operate WITHOUT prior workshop context per Stage-2 protocol.
   - **Inputs**: §VII.AR STAGE-1-CANDIDATE registry entry text (landed via CF V.1); W6a-51 plan §10 substitution chain Steps 1–8 (the steps, not the WP transcripts); canonical_constants.py SU(N) Lie-theory pins (DIM_SU3, RANK_SU3, DELTA_PLUS_SU3, PREFACTOR_CONV_B_BASELINE_SU3, slope_A_FW parameterized pin); CM-1995 §III.4 + Proposition III.6 source paper; Sage MCP for symbolic verification.
   - **Gate**: `S89-OR-LATER-W6A-51-INDEPENDENT-VERIFY` PASS criterion = BOTH cross-reviewers PASS on JOINT clauses (c)+(d) (logical AND) AND PASS on per-axis clauses; FAIL on either cross-reviewer routes back to STAGE-1-CANDIDATE with INFO-band carry-forward and the failing clauses route to next-session remediation. Cross-reviewer pool: connes-ncg-theorist FORBIDDEN (CO-AUTHOR); lizzi-spectral-functional-theorist FORBIDDEN (PRIMARY); plausible candidates: gen-physicist (spectral-functional-axis cross-reviewer), van-den-dungen-bridge-theorist (NCG-axiomatic-axis cross-reviewer), phonon-first-cosmologist, kitaev-information-theorist (whichever team-member has not been previously dispatched on §W6a-51 content). Per `joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check"`.
   - **Effort**: ~1.0 wave-equivalents (Stage-2 protocol overhead; 2 parallel cross-reviewer dispatches; both must return verdicts independently).

V.6. **FWD-C1 retry with parameterized `slope_A_FW` canonical (consume Workshop-1 dual-reading + Workshop-3 Class-(f) adjudication)**
   - **What**: Re-derive the FWD-C1 Pillar I↔II substrate-cosmology bridge `c_sub` canonical via the substrate-first parameterized `slope_A(τ_fold)` closed form (consumed from CF V.2 `slope_A_FW_Conv_A_AT_TAU_FOLD` at τ_fold; or from the parameterized form for τ-functional dependence). FWD-C1 candidate is queued from the W6a synthesis CF-6 `S89-FWD-C1-RETRY-WITH-SLOPE-A-CANONICAL`; this Workshop-1 carry-forward extends the W6a synthesis CF-6 by specifying the dual-reading-parameterized canonical pin as the input. Compatible with Workshop-3 mack reading (consumes parameterized canonical at INFO directly) and Workshop-3 lizzi reading (consumes parameterized canonical post-discriminator at PASS-A or PASS-B winner).
   - **Inputs**: CF V.2 parameterized `slope_A_FW_Conv_A` canonical entry; CF V.1 §VII.AR STAGE-1-CANDIDATE landing; CF V.3 discriminator outcome (if completed in S89; else use parameterized form with INFO caveat); cross-pillar-bridge-anatomy.md §"Forward template-adoption" §FWD-C1 candidate framework; Workshop-3 adjudication outcome (Class-(f) sufficient OR PRU Class 8.3 HARD-HALT bypass closure).
   - **Gate**: `S89-FWD-C1-RETRY-WITH-SLOPE-A-CANONICAL` (consumes from W6a synthesis CF-6) PASS criterion = `c_sub_FW(τ_fold)` substrate-first canonical lands in canonical_constants.py with provenance citing CF V.2 parameterized pin; cross-link to §VII.AF.1 Pillar III↔IV bridge (calibration instance #1 of cross-pillar-bridge-anatomy.md K-counter; status MANDATORY at K=3 per S88 W4a-17 close 2026-05-04); FWD-C1 promoted from "PARTIAL-LANDING" status (W6a synthesis CF-6 declaration) to "STAGE-1-CANDIDATE" status (5-anatomy + 3-level ladder declared in registry text per cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"). FAIL routes to FWD-C1 BLOCKED status until Workshop-1 discriminator (CF V.3) returns.
   - **Effort**: ~0.8 wave-equivalents (substrate-first re-derivation of c_sub via the Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR `L_max → ∞` image of the substrate scalar spectral moment; depends on n_s_FW substrate-first c_sub completion at S88+).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Algebra-axis classification of `slope_A(τ) = c₀/(1−τ/(5π))` | GEOMETRIC | algebra-INVARIANT (spectrum-only family) per cross-pillar-bridge-anatomy.md K=3 MANDATORY | Closed-form coefficients are PURE group-theoretic numbers (Peter-Weyl `(dim+rank)/2`, Cartan-root sum, Plancherel measure); regulator-class invariance structurally exact at finite spectral triples |
| 2 | Substitution-chain analysis at WP §10 Step 6 transition `linear → geometric_resummation` | GEOMETRIC | NOTATIONAL-SHORTCUT-AT-FIRST-ORDER; structural identity at second order requires κ_2_substrate = 1 verification | Reading A (geometric) and Reading B (linear-only) agree at O(ε¹); differ at O(ε²); empirical residual 5.23e-5 is consistent with EITHER reading at the leading order |
| 3 | Discriminating predicate at τ = 2·τ_fold = 0.38 | GEOMETRIC | Pre-registered S89 cross-validation gate `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD` with PASS-A: |ratio−8|<1.0 (geometric); PASS-B: |ratio−4|<0.5 (linear) | Discriminator threshold at machine-discriminable precision; ratio measurement at L_max=14 Richardson is the structural decider |
| 4 | STAGE-1-CANDIDATE eligibility at §VII.AR | GEOMETRIC | PRESERVED under both readings; registry text encodes DUAL-READING parameterization | Closed form is the leading-order substrate prediction matching W1b-3 anchor at INFO band; both readings agree at this level |
| 5 | `slope_A_FW` canonical_constants entry specification | GEOMETRIC | PARAMETERIZED CLOSED-FORM PIN (NOT scalar at τ_fold) with explicit regime-of-validity declaration | Preserves both readings at canonical-constants level; downstream consumers cite parameterized form with regime caveat; scalar pin at τ_fold available for downstream consumers needing point evaluation |
| 6 | §VII.AR registry slot allocation | GEOMETRIC | RESERVED for STAGE-1-CANDIDATE landing per CF V.1 (mack-cosmic-bridge sole writer; SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure) | Next-free top-level letter verified via Grep on permanent-results-registry.md (§VII.AQ at S88 W7b-79 is current latest; §VII.AR is next-free) |
| 7 | Three-Level structural-confidence ladder annotation | GEOMETRIC | Level 1 (cohomology-class identity, regulator-invariant) ✓; Level 2 (algebraic envelope) READING-DEPENDENT; Level 3 (empirical anchor 5.23e-5 / 2.62e-5 in INFO band) ✓ | Level-2-binding per cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction (S88 W8-88 hardening)"; Registry-PASS criterion holds under Reading B; INDETERMINATE under Reading A pending CF V.3 discriminator |
| 8 | FWD-C1 unblocking compatibility with both Workshop-3 readings | GEOMETRIC | Dual-reading parameterization defers Workshop-3 binary choice (mack INFO-eligible vs lizzi HARD-HALT) by encoding both readings at canonical-constants level | Workshop-1 STRUCTURAL VERDICT is INDEPENDENT of Workshop-3 adjudication; both readings produce same INFO landing for §W6a-51 and same `slope_A_FW(τ_fold)` evaluation |
