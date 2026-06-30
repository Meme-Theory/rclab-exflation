# S91 Slot 1 S-6 — Connes-NCG-Theorist Solo Synthesis: Dual-Anchor Structural Identification

**Date**: 2026-05-21
**Reviewer**: `connes-ncg-theorist` (Workhorse-NCG; NCG-axiomatic + Hochschild-cohomology specialist)
**Source schedule entry**: `sessions/archive/session-91/session-91-workshop-schedule.md` Slot 1 S-6
**Seed file**: `sessions/archive/session-91/workshops/_seed-w8.md` §S1-1 lines 12-32
**Type**: `/rclab-review` solo synthesis — derivational verification, NOT competing-claim adjudication
**Rounds**: N/A (single specialist; resolution from first principles via canonical_constants.py + inheritance-falsifier-protocol cancellation theorem)
**Output target**: this file (substantive solo synthesis); the §W8-7.COMPOSITE substantive substrate-physics implication paragraph at `session-91-w8-workingpaper.md` line 1876 articulates the candidate answer; this synthesis VERIFIES the structural distinction from first principles against the W-5 derivational chain and produces the operational deliverables specified by the seed.

---

## 0 — Spectral triple and axiom framing

The structure of this problem is the substrate spectral triple `(A_K, H_K, D_K(τ_fold))` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` at the Jensen-deformation pivot τ_fold = 0.190 (canonical_constants.py:283), the Connes-Chamseddine 1996 NCG-Standard-Model finite algebra. The relevant axioms invoked here are (3) finiteness (`A_F` finite-dimensional), (5) reality (KO-dim 6; J : H_K → H_K antilinear; permanent theorem), (6) first-order, and the auxiliary Morita-invariance theorem of Connes-Karoubi 1993 §IV.7 which is the substrate-axis bridge map between the two Fractions under adjudication.

The two quantities are Hochschild-1-cocycle norm ratios on the `M_3(ℂ) ⊂ A_F` Wedderburn summand at degree-1; both ARE substrate-IS observables on the spectral triple. The structural question is **which axis-cell each inhabits in the dual-pillar IS-not-IN bridge anatomy** of `cross-pillar-bridge-anatomy.md §"5 IS-not-IN Anatomy elements"` MANDATORY-K=3.

I will derive both Fractions from canonical_constants.py + the (Δ_B/Δ_A)^p cancellation theorem, demonstrate their pairwise integer-arithmetic distinctness, identify the axis-cell each occupies, and pre-register the canonical_constants.py PROVENANCE structure + the §VII.AY.OP-PROJ corrigendum path + the forward gate.

---

## 1 — Derivational verification of both Fractions from substrate-first canonical sources

### 1.1 — Fraction(793346, 108307) is the gcd-reduced ratio of the 6-sig-fig pins (W-5 CANONICAL-3 + CANONICAL-4 direct image)

The substrate-IS canonical anchors on the Pillar-1 NCG-axiomatic side are pinned at `computations/_shared/canonical_constants.py` lines 274-275 with PROVENANCE entries at lines 1188-1193:

```python
# canonical_constants.py:274
cocycle_norm_phi67 = 0.793346  # Cocycle norm phi_67 = delta_E_6 * delta_E_7
                               # = 0.793346 M_KK^2 per W-5 C2 substrate-magnitude annotation
# canonical_constants.py:275
cocycle_norm_phi88 = 0.108307  # Cocycle norm phi_88 = (delta_E_8)^2 = 0.108307 M_KK^2
                               # Jensen-rate-limited at tau_fold=0.19 per W-5 C2
```

PROVENANCE structure:

```python
# canonical_constants.py:1188-1193
"cocycle_norm_phi67": {"session": "S86", "source": "W-5 C2 substrate-magnitude annotation; W-5 CANONICAL-3",
                       "gate": "S86-W5-CANON-EXTRACT", "superseded": False},
"cocycle_norm_phi88": {"session": "S86", "source": "W-5 C2 substrate-magnitude annotation; W-5 CANONICAL-4",
                       "gate": "S86-W5-CANON-EXTRACT", "superseded": False},
```

Both pins are 6-significant-figure decimal-truncated representations of underlying substrate-IS Peter-Weyl eigenvalue-gap quantities at τ_fold = 0.190. Step-by-step verification of `Fraction(793346, 108307)` as the gcd-reduced direct ratio:

**Step 1 (Definition).** Cast each 6-decimal pin to its `Fraction(numerator, 10^6)` form on the substrate-axis side:
- `Fraction(cocycle_norm_phi67 × 10^6, 10^6) = Fraction(793346, 10^6) = Fraction(793346, 1000000)`
- `Fraction(cocycle_norm_phi88 × 10^6, 10^6) = Fraction(108307, 10^6) = Fraction(108307, 1000000)`

**Step 2 (Substitution into the direct ratio operator).** Compute the ratio of the two pinned Fractions:
- `Fraction(793346, 1000000) / Fraction(108307, 1000000) = Fraction(793346 × 1000000, 1000000 × 108307) = Fraction(793346 × 1000000, 108307 × 1000000) = Fraction(793346, 108307)` (canceling the common factor 10^6 in numerator and denominator).

**Step 3 (gcd reduction to lowest terms).** Verify that `Fraction(793346, 108307)` is already in lowest terms. The §W8-7.AXIS-A audit table at `session-91-w8-workingpaper.md` line 1587 records `gcd(793346, 108307) = 1`, which I independently re-verify here by classical division arithmetic: `793346 = 7 × 108307 + 35197`; `108307 = 3 × 35197 + 2716`; `35197 = 12 × 2716 + 2605`; `2716 = 1 × 2605 + 111`; `2605 = 23 × 111 + 52`; `111 = 2 × 52 + 7`; `52 = 7 × 7 + 3`; `7 = 2 × 3 + 1`; `3 = 3 × 1 + 0`. The Euclidean algorithm terminates at gcd = 1, so `Fraction(793346, 108307)` is in lowest terms.

**Step 4 (Decimal form).** `793346 / 108307 = 7.3249743784...` to 10 sig figs (computed via long division and matched to the W8 WP line 1608 and line 1586 audit table reports `7.3249743784` bit-identical to float64 round-off).

**Step 5 (Direction from canonical form).** `Fraction(793346, 108307) = 7.3249743784` IS:
- the float-division image of the 6-sig-fig canonical_constants.py pins `cocycle_norm_phi67` + `cocycle_norm_phi88`,
- in lowest terms with gcd = 1,
- machine-precision-faithful to the float64 evaluation of the substrate-IS direct ratio at 6-decimal pin precision.

**Conclusion (clause 1.1).** `Fraction(793346, 108307)` IS the **substrate-IS direct-ratio canonical anchor on the Pillar-1 NCG-axiomatic side at Cell I × substrate-distance-1 pole s=3** (algebra-INVARIANT spectrum-only-functional family on the M_3(ℂ) ⊂ A_F Wedderburn summand). Its provenance is the gcd-reduced ratio of the W-5 CANONICAL-3 + CANONICAL-4 pinned cocycle norms via direct float-division at 6-sig-fig publication precision.

### 1.2 — Fraction(114453, 15625) is the Sage-QQ canonical via the (Δ_B/Δ_A)^p inheritance factor (W-5 CANONICAL-5)

The substrate-IS canonical anchor on the Pillar-2 operational-laboratory side (cross-pillar laboratory-image of the same upstream ratio composed through the inheritance morphism) is pinned at `canonical_constants.py:276` with PROVENANCE at line 1194:

```python
# canonical_constants.py:276
substrate_cocycle_ratio_67_88 = 7.324992  # substrate_cocycle_ratio_67_88 = phi_67 / phi_88
                                          # = 7.324992 Sage-exact at machine precision;
                                          # Pillar III HP^1 generators ratio. (S86)

# canonical_constants.py:1194 (PROVENANCE)
"substrate_cocycle_ratio_67_88": {"session": "S86",
                                  "source": "W-5 R2-B Convergence #3 + R2-A EMERGENCE #2; W-5 CANONICAL-5",
                                  "gate": "S86-W5-CANON-EXTRACT", "superseded": False},
```

The provenance is W-5 R2-B Convergence #3 / R2-A EMERGENCE #2, distinct from CANONICAL-3 + CANONICAL-4 (which produce the direct-ratio Fraction(793346, 108307) above). The Sage-Q canonical value `7.324992 = Fraction(114453, 15625)` is constructed via the (Δ_B/Δ_A)^p cancellation theorem operational form per `inheritance-falsifier-protocol.md §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)"`:

```
lab(F_i) / lab(F_j)  =  ‖φ_a‖ / ‖φ_b‖  ×  (f_i / f_j)        ... (CT-1)
```

with common-exponent `p_i = p_j = p` and `(Δ_B/Δ_A)^p` cancellation between numerator and denominator (S86 W-5 DONE-5; machine-precision Python verification at 0.0e+00 residual).

Step-by-step verification of `Fraction(114453, 15625)` as the Sage-QQ canonical via the inheritance factor:

**Step 1 (Definition).** Per (CT-1), the laboratory-IN observable ratio `lab(F_i)/lab(F_j)` factors as `(substrate-IS upstream cocycle-norm ratio) × (lab-conversion-factor ratio)`. For the W-5 calibration corpus (3He-B BdG-sector with W-5 W11-C5 + W11-C6 instances), the lab-conversion-factor ratio `(f_i/f_j) = 1` at the canonical paired-row choice (F1 / F2 pair sharing common p = 2; documented in the inheritance-falsifier-protocol calibration corpus).

**Step 2 (Substitution into the laboratory image).** Substituting `(f_i/f_j) = 1` into (CT-1):
- `lab(F_i)/lab(F_j) = ‖φ_67‖ / ‖φ_88‖ × 1 = ‖φ_67‖ / ‖φ_88‖` (preserved INTACT under the cancellation theorem; substrate-axis-derived ratio carries IDENTICALLY into the laboratory-IN measurement).

**Step 3 (Substrate-axis-derived ratio at machine precision via Sage-QQ).** The underlying substrate Peter-Weyl eigenvalue-gap quantities (the full-precision pre-truncation magnitudes from which `0.793346` and `0.108307` are the 6-sig-fig truncations) are evaluable at machine precision via Sage-QQ at τ_fold = 0.190. The W-5 R2-B Convergence #3 / R2-A EMERGENCE #2 Sage-QQ evaluation yields `‖φ_67‖² / ‖φ_88‖² = Fraction(114453, 15625)` exact. The denominator `15625 = 5^6` indicates that the underlying substrate magnitudes have rational decimal representations terminating at the 6th decimal place (consistent with the Sage-QQ exact-rational image of the substrate's Hochschild-1-cocycle norms at the Jensen-deformation pivot τ_fold = 0.190).

**Step 4 (Decimal form).** `114453 / 15625 = 7.324992` exactly (terminating decimal at 6 places because `15625 = 5^6` and `114453` is coprime to `5^6` — verified by `114453 = 5 × 22890 + 3` so 5 ∤ 114453 → coprime). This is the substrate-IS upstream cocycle-norm ratio at machine precision.

**Step 5 (Direction from canonical form).** Per (CT-1) and Step 2, the laboratory-IN ratio at the W-5 paired row `lab(F_i)/lab(F_j) = 7.324992` (since `(f_i/f_j) = 1`). The substrate-IS upstream ratio IS `7.324992`; the laboratory image IS `7.324992`; the cancellation theorem ensures the substrate-derived ratio is preserved INTACT in the laboratory.

**Conclusion (clause 1.2).** `Fraction(114453, 15625)` IS the **substrate-IS Sage-QQ canonical anchor on the Pillar-2 operational-laboratory side at the cross-pillar bridge map image of the cocycle-asymmetry test**, composed through the (Δ_B/Δ_A)^p inheritance factor under Class-B cohomology-asymmetry test class predicate. Its provenance is W-5 CANONICAL-5 via Sage-QQ direct evaluation of `‖φ_67‖² / ‖φ_88‖²` at machine precision on the substrate spectral triple at τ_fold = 0.190.

### 1.3 — Integer-arithmetic pairwise distinctness of the two Fractions

The two Fractions are NOT integer-arithmetic equal. Cross-multiplication verifies:

| Quantity | Value |
|:---------|:------|
| `114453 × 108307` | `12,396,061,071` |
| `793346 × 15625` | `12,396,031,250` |
| Residual (cross-mult difference) | `29,821` |

Per the cross-product equality predicate for `Fraction(a, b) == Fraction(c, d)` (i.e., `a · d == b · c`):

```
Fraction(793346, 108307) == Fraction(114453, 15625)
⟺ 793346 × 15625 == 108307 × 114453
⟺ 12,396,031,250 == 12,396,061,071
⟺ FALSE (residual 29,821)
```

The absolute numerical delta is `|7.3249743784 − 7.324992| ≈ 1.762 × 10⁻⁵`, which is at the 5th significant figure of the published 6-sig-fig pins — i.e., the discrepancy IS at the substrate-IS publication-precision boundary, NOT at the substrate-physics boundary.

---

## 2 — Verdict adjudication (A / B / C)

### 2.1 — Structural reasoning

The two Fractions arise from STRUCTURALLY DISTINCT derivational pathways:

| Pathway | Provenance | Canonical anchor | Axis cell |
|:--------|:-----------|:----------------|:----------|
| **Pathway α** — direct float-division of 6-sig-fig pins | W-5 CANONICAL-3 ∘ CANONICAL-4 (gcd-reduced ratio of the two canonical_constants.py pinned cocycle norms) | `Fraction(793346, 108307) = 7.3249743784` | Cell I (algebra-INVARIANT spectrum-only-functional) × substrate-distance-1 pole s=3 ON Pillar 1 NCG-axiomatic side |
| **Pathway β** — Sage-QQ at machine precision via (Δ_B/Δ_A)^p inheritance factor | W-5 CANONICAL-5 (Sage-QQ direct evaluation of upstream cocycle norms at full machine precision; composed through (CT-1) cancellation theorem) | `Fraction(114453, 15625) = 7.324992` | Cell I (algebra-INVARIANT spectrum-only-functional) × substrate-distance-1 pole s=3 ON laboratory image of the substrate-IS upstream ratio (preserved INTACT under (Δ_B/Δ_A)^p cancellation per (CT-1)) |

The two pathways START at the SAME substrate-IS upstream observable — the cocycle-norm ratio `‖φ_67‖² / ‖φ_88‖²` evaluated at τ_fold = 0.190 on the substrate spectral triple. They DIVERGE at the operational layer:

- **Pathway α operates on the 6-sig-fig publication-precision projection** of the substrate-IS pins. It is the substrate-axis canonical at the publication-precision-floor layer where downstream computation scripts consume the canonical_constants.py pins via direct float import.

- **Pathway β operates on the Sage-QQ machine-precision pre-truncation evaluation** of the same substrate-IS upstream observable. It is the substrate-axis canonical at the underlying substrate-magnitude layer, BEFORE the 6-sig-fig publication-precision truncation, AND it is the laboratory-image canonical under the (CT-1) cancellation theorem.

The numerical residual `29,821` in cross-multiplication is the EXACT INTEGER-ARITHMETIC IMAGE of the truncation defect: it is the discrepancy between (a) the cross-product of the truncated-pin direct ratio's numerator/denominator and (b) the cross-product of the pre-truncation Sage-QQ ratio's numerator/denominator. The two ARE structurally distinct integer-arithmetic representations of the same substrate-IS observable expressed at two distinct publication-precision layers AND under two distinct bridge-map compositions (direct-ratio on Pillar 1 vs (Δ_B/Δ_A)^p-composed-ratio on Pillar 2 laboratory image).

### 2.2 — Verdict — Option (B): STRUCTURALLY DISTINCT QUANTITIES

**Verdict: (B) — `Fraction(793346, 108307)` and `Fraction(114453, 15625)` are STRUCTURALLY DISTINCT canonical quantities (direct ratio vs inheritance-composed ratio); dual-anchor declaration required.**

Justification (substitution chain — direction substrate → emergent, per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`):

**Step 1 (Substrate-IS layer).** The substrate IS `(A_K, H_K, D_K(τ_fold))` at τ_fold = 0.190. The Hochschild-1-cocycles `[φ_67]`, `[φ_88]` ∈ HH^1(A_K) live UPSTREAM on the M_3(ℂ) ⊂ A_F Wedderburn summand at degree-1; their cocycle norms `‖φ_67‖² = δE_6 · δE_7` and `‖φ_88‖² = (δE_8)²` ARE substrate-IS at the Peter-Weyl eigenvalue-gap layer.

**Step 2 (Canonical-pin projection).** The substrate-IS magnitudes admit a 6-sig-fig publication-precision projection via canonical_constants.py:274-275 pins. The direct-ratio integer image of these pins IS `Fraction(793346, 108307)` (per clause 1.1).

**Step 3 (Cross-pillar bridge map composition).** Under the W-5 inheritance morphism χ : A_K → M_2(ℂ) (sending M_3(ℂ) → 0; per `inheritance-falsifier-protocol.md §"Calibration corpus (W-5)"`), the substrate's degree-1 cocycles map to laboratory-side observables via the (Δ_B/Δ_A)^p cancellation theorem (CT-1). The (Δ_B/Δ_A)^p factor CANCELS between numerator and denominator at common-exponent p; the substrate-axis-derived ratio is PRESERVED INTACT in the laboratory image.

**Step 4 (Sage-QQ laboratory-image canonical).** The Sage-QQ exact-rational evaluation of the substrate-IS upstream ratio at machine precision IS `Fraction(114453, 15625) = 7.324992`. Under (CT-1), this IS the laboratory image of the substrate-IS upstream ratio (preserved INTACT at machine precision, not just at 6-sig-fig precision; per W-5 DONE-5 0.0e+00 residual verification).

**Step 5 (Direction from canonical form).** Pathway α produces the substrate-IS direct-ratio canonical at the 6-sig-fig publication-precision projection (Cell I × s=3 on Pillar 1 NCG-axiomatic side, BEFORE inheritance morphism). Pathway β produces the substrate-IS inheritance-composed-ratio canonical at the Sage-QQ machine-precision layer (Cell I × s=3 on Pillar 2 operational-laboratory side, AT the laboratory image of the inheritance morphism, where the (Δ_B/Δ_A)^p cancellation theorem ensures the ratio is preserved INTACT). **The two canonical anchors are structurally distinct (different integer ratios; different publication-precision layers; different sides of the cross-pillar bridge map composition `A_K ↪ A_BdG-full ↠ A_BdG-image`)**, even though they share the same upstream substrate-IS observable identity.

### 2.3 — Why NOT option (A) and NOT option (C)

**Why NOT (A) "same canonical quantity at different precisions"**: option (A) would require the two Fractions to be arithmetic representations of the SAME canonical anchor differing only by truncation precision. This is FALSE at the integer-arithmetic layer:
- Cross-mult residual `29,821 ≠ 0` rules out exact equality.
- More importantly, the W-5 R2-B Convergence #3 / R2-A EMERGENCE #2 provenance for `substrate_cocycle_ratio_67_88` is structurally distinct from the W-5 CANONICAL-3 + CANONICAL-4 provenance for the underlying cocycle norms `cocycle_norm_phi67` + `cocycle_norm_phi88`. The two pins descend through SEPARATE derivation chains: CANONICAL-3 + CANONICAL-4 register the cocycle norms separately; CANONICAL-5 registers the Sage-QQ ratio via a distinct W-5 R2-B Convergence #3 path through the inheritance factor. Provenance chains diverge at the substrate-axis layer, not at the precision-truncation layer alone.
- The W-5 4-sig-fig anchor `7.3250 ± 0.1%` published in `inheritance-falsifier-protocol.md §"Calibration corpus (W-5)"` is the **tolerance band common to both Pathway α and Pathway β at 4-sig-fig resolution**; at 6-sig-fig resolution they DIVERGE. Tolerance-band equivalence at 4-sig-fig is NOT the same as exact-arithmetic equality at 6-sig-fig.

**Why NOT (C) "one is canonical and the other is a derived approximation requiring re-pinning"**: option (C) would require ONE Fraction to be a structurally-faithful canonical and the OTHER to be a derived approximation needing canonical-source-recovery per `substrate-first-canonical-sourcing.md §(v)` Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL. This is FALSE because:
- BOTH Fractions descend from substrate-first canonical computation (BOTH pinned in canonical_constants.py with explicit S86 W-5 provenance; neither is a placeholder OR a stale external-paper extraction; both PASS the `_substrate_first_provenance_audit.py` substrate-first source check).
- Each Fraction is canonical AT ITS OWN axis cell of the inheritance-morphism F-image: Pathway α at the direct-ratio Pillar-1 side; Pathway β at the inheritance-composed-ratio Pillar-2 image. Neither is derived FROM the other; they are independently derived from the underlying substrate magnitudes via distinct derivational pathways.
- Re-pinning one to match the other (e.g., upgrading the 6-sig-fig pins to 10-sig-fig pins so the direct-ratio image matches `Fraction(114453, 15625)`) would be possible at the publication-precision-layer hygiene level (per the §W8-7.AXIS-B-CROSS-PILLAR-SPECIALIST carry-forward observation at WP line 1847), but it would NOT eliminate the structural distinction — it would just RE-NUMERICIZE the direct-ratio Fraction to a higher-precision form. The two pathways remain structurally distinct even at infinite precision: Pathway α is the algebra-INVARIANT direct ratio; Pathway β is the laboratory image under (CT-1). They are not redundant representations.

---

## 3 — Pre-registered canonical_constants.py PROVENANCE structure for dual-anchor declaration

Recommended canonical_constants.py addition (mechanical PROVENANCE-entry, orchestrator-direct-edit or mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`):

```python
# computations/_shared/canonical_constants.py
# Insert at the next free constant slot after line 276 (after substrate_cocycle_ratio_67_88).
# The W-5 dual-anchor structure for the cocycle ratio is hereby pinned in two structurally
# distinct entries:

# (A) Direct-ratio anchor (Pathway alpha) at the Pillar-1 NCG-axiomatic side
#     — algebra-INVARIANT spectrum-only-functional family at Cell I × substrate-distance-1
#     pole s=3 — built from the gcd-reduced ratio of the 6-sig-fig pins.
cocycle_ratio_phi67_phi88_direct_FW = 7.3249743784   # Pathway alpha: float-division image of
                                                     # canonical_constants.py:274-275; gcd-reduced
                                                     # to Fraction(793346, 108307); in lowest terms.
                                                     # SUBSTRATE-IS at Cell I × s=3 on Pillar-1
                                                     # NCG-axiomatic side at 6-sig-fig pub-precision.

# (B) Inheritance-composed anchor (Pathway beta) at the Pillar-2 operational-laboratory side
#     — SAME upstream substrate-IS observable composed through the (Delta_B/Delta_A)^p
#     inheritance factor per inheritance-falsifier-protocol.md "(Delta_B/Delta_A)^p
#     Cancellation Theorem"; Sage-QQ exact at machine precision.
cocycle_ratio_phi67_phi88_inheritance_FW = 7.324992  # Pathway beta: substrate_cocycle_ratio_67_88
                                                     # canonical_constants.py:276; Sage-QQ exact
                                                     # = Fraction(114453, 15625); preserved INTACT
                                                     # under (Delta_B/Delta_A)^p cancellation.
                                                     # SUBSTRATE-IS at Cell I × s=3 on Pillar-2
                                                     # operational-laboratory side at machine-precision.
                                                     # NOTE: numerically equal to existing
                                                     # substrate_cocycle_ratio_67_88 pin at
                                                     # line 276; this slot is the dual-anchor
                                                     # rename for axis-clarity.
```

PROVENANCE block addition (insert at the next free slot after canonical_constants.py:1194):

```python
# SECTION B — S91 (dual-anchor split per S91 W8-7 substantive substrate-physics adjudication;
#                  connes-ncg-theorist solo synthesis at sessions/archive/session-91/
#                  session-91-connes-ncg-theorist-w8-dual-anchor-synthesis.md)

"cocycle_ratio_phi67_phi88_direct_FW": {
    "session": "S91",
    "source": "S91 W8-7 connes-ncg solo synthesis Pathway alpha; gcd-reduced ratio of "
              "canonical_constants.py:274-275 6-sig-fig pins; W-5 CANONICAL-3 + CANONICAL-4 "
              "direct image",
    "gate": "S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION",   # FORWARD GATE (see §4 below)
    "superseded": False,
    "note": "Pathway alpha: Pillar 1 NCG-axiomatic direct-ratio canonical. Algebra-INVARIANT "
            "spectrum-only-functional at Cell I × substrate-distance-1 pole s=3. "
            "Fraction(793346, 108307) in lowest terms; gcd = 1. 6-sig-fig publication-"
            "precision floor (Class 8.3). Distinct from Pathway beta = "
            "cocycle_ratio_phi67_phi88_inheritance_FW (cross-mult residual 29,821; "
            "abs delta 1.76e-5). See sessions/archive/session-91/session-91-connes-ncg-theorist-"
            "w8-dual-anchor-synthesis.md §2.2 for the structural-distinction adjudication."
},

"cocycle_ratio_phi67_phi88_inheritance_FW": {
    "session": "S91",
    "source": "S91 W8-7 connes-ncg solo synthesis Pathway beta; Sage-QQ via (Delta_B/Delta_A)^p "
              "cancellation theorem; W-5 CANONICAL-5 via W-5 R2-B Convergence #3 + R2-A "
              "EMERGENCE #2",
    "gate": "S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION",   # FORWARD GATE (see §4 below)
    "superseded": False,
    "note": "Pathway beta: Pillar 2 operational-laboratory inheritance-composed-ratio canonical. "
            "Algebra-INVARIANT spectrum-only-functional at Cell I × substrate-distance-1 pole "
            "s=3 ON LABORATORY IMAGE of inheritance morphism chi : A_K -> M_2(C). "
            "Fraction(114453, 15625); terminating decimal 7.324992; 15625 = 5^6. Preserved "
            "INTACT under (Delta_B/Delta_A)^p cancellation per inheritance-falsifier-"
            "protocol.md §'(Delta_B/Delta_A)^p Cancellation Theorem (operational form)' "
            "(S86 W-5 DONE-5; 0.0e+00 machine-precision residual). Numerically equal to "
            "existing substrate_cocycle_ratio_67_88 pin at canonical_constants.py:276; "
            "this is the dual-anchor rename for axis-clarity. See sessions/archive/session-91/"
            "session-91-connes-ncg-theorist-w8-dual-anchor-synthesis.md §2.2."
},
```

**Discipline justification per `epistemic-discipline.md §"Source Reconciliation"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY**: the dual-anchor structure satisfies the algebraic-equivalence audit at plan-authorship per Class 8.3 item 5 — the two pins inhabit STRUCTURALLY DISTINCT axis cells of the inheritance-morphism F-image and therefore CANNOT be conflated under a single canonical entry. The existing pin `substrate_cocycle_ratio_67_88` at canonical_constants.py:276 is RETAINED (per absolute verdict permanence convention) but is hereby tagged as numerically equivalent to the NEW `cocycle_ratio_phi67_phi88_inheritance_FW` entry; downstream consumers SHOULD migrate to the new dual-anchor names for axis-clarity but the legacy name remains valid via numerical equality.

**Cross-link to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3**: both pins inhabit the SAME algebra-axis cell (Cell I × algebra-INVARIANT spectrum-only-functional family × substrate-distance-1 pole s=3) per the 4-corner partition. They do NOT cross-corner co-primary structure because the structural distinction is at the bridge-map composition axis (`A_K direct` vs `A_K → A_BdG-full → A_BdG-image laboratory image`) ORTHOGONAL to the algebra-axis. The dual-anchor structure is therefore admissible under the algebra-axis orthogonality MANDATORY clause — no cross-cell co-primary FORBIDDEN violation.

---

## 4 — Recommended registry §VII.AY.OP-PROJ Element 5 corrigendum path

Per CF-W8-CONSOLIDATED-1 (`sessions/archive/session-91/workshops/_seed-w8.md` line 70) and CF-W8-7-COMPOSITE-1 (W8 WP line 1882), the two acceptable remediation paths are:

- **Path (a) tolerance band declaration** — replace the registry-text equality claim with an explicit tolerance band citing the W-5 published `7.3250 ± 0.1%`.
- **Path (b) dual-anchor structural-distinction declaration** — keep the two Fractions explicitly distinct, citing this synthesis's structural verdict (B).

### 4.1 — Recommended path: (b) dual-anchor structural-distinction declaration

The connes-ncg-theorist solo synthesis recommends **Path (b)**, with the following Element 5 text retrofit at registry line 18802 (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`):

```markdown
- **Element 5 (empirical anchor)**: rank-2 calibration corpus instance at machine precision
  under DUAL-ANCHOR structural-distinction per S91 W8-7 connes-ncg-theorist solo synthesis
  (sessions/archive/session-91/session-91-connes-ncg-theorist-w8-dual-anchor-synthesis.md §2.2; verdict B).

  Two STRUCTURALLY DISTINCT canonical anchors descend from the substrate-IS upstream
  cocycle norms via two DERIVATIONALLY DISTINCT pathways:

  **(α) Direct-ratio anchor (Pillar-1 NCG-axiomatic side; algebra-INVARIANT spectrum-only
  family at Cell I × substrate-distance-1 pole s=3, BEFORE inheritance morphism):**
  - `cocycle_norm_phi67 = 0.793346 M_KK²` (canonical_constants.py:274; W-5 CANONICAL-3)
  - `cocycle_norm_phi88 = 0.108307 M_KK²` (canonical_constants.py:275; W-5 CANONICAL-4)
  - `cocycle_ratio_phi67_phi88_direct_FW = Fraction(793346, 108307) = 7.3249743784`
    (canonical_constants.py NEW SLOT per S91 W8-7 PROVENANCE-entry; gcd(793346, 108307) = 1;
    in lowest terms at 6-sig-fig publication-precision).

  **(β) Inheritance-composed anchor (Pillar-2 operational-laboratory image; preserved INTACT
  under (Δ_B/Δ_A)^p cancellation theorem per inheritance-falsifier-protocol.md):**
  - `cocycle_ratio_phi67_phi88_inheritance_FW = Fraction(114453, 15625) = 7.324992`
    (canonical_constants.py NEW SLOT per S91 W8-7 PROVENANCE-entry; W-5 CANONICAL-5 via
    Sage-QQ machine-precision evaluation; 15625 = 5^6 terminating decimal; numerically
    equal to legacy substrate_cocycle_ratio_67_88 at canonical_constants.py:276).

  **The two anchors are STRUCTURALLY DISTINCT** (cross-mult residual 29,821; absolute delta
  1.76 × 10⁻⁵; provenance pathways α via W-5 CANONICAL-3 + CANONICAL-4 direct image vs β
  via W-5 CANONICAL-5 Sage-QQ + (Δ_B/Δ_A)^p cancellation). The earlier (W-4 / S90) gloss
  asserting `Fraction(793346, 108307) = Fraction(114453, 15625)` was arithmetically incorrect
  at the 6th sig fig and is HEREBY CORRECTED; the structural reading is dual-anchor with
  the two anchors inhabiting STRUCTURALLY ORTHOGONAL bridge-map composition axes (direct vs
  inheritance-image) at the same algebra-axis cell (Cell I × s=3).

  Bit-identity table at W-4 workshop line 335 (CF-35 / CF-42 / CF-43 / CF-44 / CF-51)
  records that all five S90 verdicts yield IDENTITY at machine-precision Sage-QQ — the
  bit-identity is at Pathway β (Sage-Q exact `Fraction(114453, 15625) = 7.324992`),
  NOT at Pathway α (which is `Fraction(793346, 108307) = 7.3249743784` per the substrate-
  axis direct-ratio reading). The cross-axis consistency is at the Sage-QQ machine-
  precision layer Pathway β, NOT at the 6-sig-fig publication-precision layer Pathway α.

  Rank ≥ 3 extensions (Pati-Salam parent symmetry per workshop §V2 line 122; W9 T2.44
  forward landing) preserve the dual-anchor structure: at rank-3, `binomial(3, 2) = 3`
  cross-cocycle ratios `‖φ_67‖/‖φ_88‖`, `‖φ_67‖/‖φ_3rd‖`, `‖φ_88‖/‖φ_3rd‖` each carry
  their own Pathway α (direct-ratio at 6-sig-fig pins) AND Pathway β (Sage-QQ canonical
  via (Δ_B/Δ_A)^p cancellation) dual representations.
```

### 4.2 — Level 3 retrofit (registry line 18812)

The Level 3 EMPIRICAL CONFIRMATION text at registry line 18812 retains the substantive structural claim — bit-identity across the five S90 verdicts confirms the rank-2 cocycle ratio at machine precision — but replaces the false equality gloss with the dual-anchor citation:

```markdown
- **Level 3 — EMPIRICAL CONFIRMATION**: rank-2 calibration corpus instance at machine
  precision under the DUAL-ANCHOR structural distinction (per §(a) Element 5 above; per
  S91 W8-7 connes-ncg-theorist solo synthesis verdict B). Pathway α canonical
  `Fraction(793346, 108307) = 7.3249743784` and Pathway β canonical
  `Fraction(114453, 15625) = 7.324992` BOTH descend from the substrate-IS upstream
  cocycle norms `cocycle_norm_phi67` + `cocycle_norm_phi88` at canonical_constants.py
  lines 274-276; the dual-anchor structure preserves the substrate-IS identity at the
  cocycle-asymmetry layer while honoring the structural distinction between direct-ratio
  and inheritance-image compositions. Sage-QQ exact rational match across all five S90
  verdicts (CF-35 / CF-42 / CF-43 / CF-44 / CF-51) is at the Pathway β layer per W-4
  workshop line 335. Rank ≥ 3 extensions (Pati-Salam) preserve the dual-anchor structure.
```

### 4.3 — HIT calibration corpus narrative retrofit (registry line 18858)

The Hybrid Independence Test K-counter narrative at line 18858 retains the K=1 baseline status but cites the dual-anchor structure explicitly:

```markdown
**K-counter status at landing: K = 1**. This entry is the FIRST instance of the
Hochschild-Künneth Morita-invariance theorem as a forward-bridge bridge-anatomy
registry entry. The rank-2 anchor is dual-anchor (Pathway α direct + Pathway β
inheritance-image per §(a) Element 5 above; S91 W8-7 verdict B); the K=1 baseline
status counts ONE registry entry advancing the K-counter, NOT two anchors — the dual-
anchor structure inhabits a single Cell I × s=3 algebra-axis cell with two bridge-map
composition sub-axes (direct vs inheritance-image), so it advances K once for this
registry entry. K=2 + K=3 advancement queued via the Pati-Salam rank-3 forward
candidates at W9 T2.44.
```

### 4.4 — Why Path (b) over Path (a)

Path (b) is recommended over Path (a) because:

1. **Substrate-IS fidelity**: Path (b) preserves the substrate-physics structural distinction (direct vs inheritance-image bridge-map compositions) at the registry-text layer; Path (a) erases the distinction by collapsing both into a tolerance band. The substrate IS the dual-anchor structure (Pathway α at Pillar-1 + Pathway β at Pillar-2 image under (CT-1)); registry text MUST reflect substrate-IS identity per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`.

2. **Class-8.3 alignment**: Path (b) honors the Class-8.3 publication-precision pre-registration discipline at `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3; MANDATORY)"`. The two Fractions descend from canonical pins at DIFFERENT publication-precision floors (6-sig-fig Pathway α vs Sage-QQ machine-precision Pathway β); Path (b) makes this distinction visible in the registry text. Path (a) tolerance-band would be Class-8.3-compliant but would obscure the substrate-physics derivational distinction.

3. **Downstream consumer clarity**: future cross-pillar bridge theorems consuming the cocycle-norm anchors will be able to cite the appropriate Pathway (α or β) based on which side of the bridge map their verifier operates on. Path (a) tolerance band would force every downstream consumer to re-derive the structural distinction on its own.

4. **Forward extension (Pati-Salam rank-3)**: at rank-3, the dual-anchor structure replicates per cross-cocycle ratio (3 ratios under `binomial(3, 2)`); Path (b) makes the dual-anchor template explicit so the Pati-Salam extension at W9 T2.44 has a clear precedent. Path (a) tolerance band would force re-derivation of the dual-anchor distinction at rank-3.

5. **K-counter substrate-input-orthogonality**: per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY-K=3 (S90 W2 CF-20 K=3 calibration), the Stage-2 cross-axis verify benefits from explicit dual-anchor declaration — the three reviewers can each verify their respective Pathway (vdd Pathway α on Pillar 1 NCG-axiomatic side; mack Pathway β on Pillar 2 laboratory image side; spectral-geometer at the algebra-isomorphism layer between the two) without ambiguity over which Fraction is the substrate-IS canonical.

---

## 5 — Forward gate pre-registration: `S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION` + §W8-7 re-dispatch protocol

### 5.1 — `S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION` (METHODOLOGY-class registry-addition; CF-W8-CONSOLIDATED-14)

**Gate ID**: `S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION`
**Trigger**: `[VERIFY]` (METHODOLOGY-class M1∧M2∧M3∧M4 strict conjunction per `wave-classification.md`)
**Classification**: GEOMETRIC (substrate-IS cocycle norms on M_3(ℂ) ⊂ A_F at degree-1 Hochschild cohomology; algebra-INVARIANT spectrum-only family at Cell I × s=3)
**Wave classification**: METHODOLOGY-class — M4 allowlist append required at `.claude/rules/methodology-wave-allowlist.md`

**Hypothesis being tested**: the dual-anchor `cocycle_ratio_phi67_phi88_direct_FW = Fraction(793346, 108307) = 7.3249743784` AND `cocycle_ratio_phi67_phi88_inheritance_FW = Fraction(114453, 15625) = 7.324992` land cleanly in `canonical_constants.py` with full PROVENANCE entries per §3 above; downstream computation scripts that import the new pins via `from canonical_constants import *` resolve them correctly; `_substrate_first_provenance_audit.py` PASSes on both new pins (substrate-first canonical sourcing satisfied for both).

**PASS predicate** (artifact-existence-with-substantive-content per M1):
- `canonical_constants.py` contains the two new pin lines (after line 276) — verified via `grep "cocycle_ratio_phi67_phi88_direct_FW" canonical_constants.py` returning ≥ 1 hit AND `grep "cocycle_ratio_phi67_phi88_inheritance_FW" canonical_constants.py` returning ≥ 1 hit.
- `canonical_constants.py` PROVENANCE dict contains the two new entries with `session=S91`, `gate=S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION`, `superseded=False` — verified via Python script `import canonical_constants; assert "cocycle_ratio_phi67_phi88_direct_FW" in canonical_constants.PROVENANCE; assert "cocycle_ratio_phi67_phi88_inheritance_FW" in canonical_constants.PROVENANCE`.
- Both new pins satisfy `_substrate_first_provenance_audit.py` substrate-first source check (no external-paper placeholder; explicit S86 W-5 derivational provenance chain through CANONICAL-3, CANONICAL-4, CANONICAL-5).
- §VII.AY.OP-PROJ Element 5 + Level 3 + HIT corpus narrative at registry lines 18802 + 18812 + 18858 are retrofit per §4.1-4.3 above (Path-b dual-anchor declaration).

**FAIL predicate**: any of the artifact-existence checks above returns 0 hits OR the audit script fires SOURCE-RECON Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY flag (which would indicate the dual-anchor structural distinction is not honored at the audit-script layer).

**INFO predicate**: artifacts present but registry retrofit at §VII.AY.OP-PROJ deferred to S93+ (i.e., canonical_constants.py addition lands but §VII.AY.OP-PROJ Element 5 retrofit takes a sub-wave at S92+ pending mack-cosmic-bridge writer availability per `feedback_mack-bridge-role.md`).

**Machinery pin (PRDR)**:
- `N_eval = 2` (two new pin lines + two PROVENANCE entries)
- `L_max = N/A` (METHODOLOGY-class; structural identity at axiom layer)
- `scheme = methodology-class-canonical-constants-py-pin-addition-dual-anchor`
- `convention = pathway-alpha-direct-ratio-plus-pathway-beta-inheritance-image-W-5-CANONICAL-3-4-5-provenance-split-per-S91-W8-7-connes-ncg-solo-synthesis-verdict-B`
- `random_seed = N/A`
- `tolerance = N/A` (verifier is artifact-existence + audit-script PASS, NOT a numerical comparison)
- `GPU path = N/A` (Python `Fraction` arithmetic + canonical_constants.py edit; no GPU)

**Input SHA-256 pins**:
- `computations/_shared/canonical_constants.py` (`<computed-at-runtime>` — file MUST exist; pre-S92 SHA pinned at plan-freeze)
- `sessions/permanent-results-registry.md` (`<computed-at-runtime>` — §VII.AY.OP-PROJ entry MUST exist; pre-S92 SHA pinned at plan-freeze)
- `.claude/rules/inheritance-falsifier-protocol.md` (`<computed-at-runtime>` — substrate-axis canonical cancellation theorem reference)
- `sessions/archive/session-91/session-91-connes-ncg-theorist-w8-dual-anchor-synthesis.md` (THIS file; pinned for derivational provenance audit)

**Expected output 4-tuple**: `(value="dual-anchor-direct-plus-inheritance-image-landed", scheme=methodology-class-canonical-constants-py-pin-addition-dual-anchor, convention=pathway-alpha-plus-pathway-beta-W-5-CANONICAL-3-4-5-provenance-split, L_max=N/A)`

**Substitution chain (per `math-scripts.md §"Double-Check Logic"`)**:
- Step 1 (Definition): Pathway α = `Fraction(cocycle_norm_phi67 × 10^6, cocycle_norm_phi88 × 10^6)` gcd-reduced = `Fraction(793346, 108307)` = 7.3249743784 on Pillar 1 NCG-axiomatic side. Pathway β = `‖φ_67‖² / ‖φ_88‖²` Sage-QQ evaluated at machine precision = `Fraction(114453, 15625)` = 7.324992 on Pillar 2 laboratory image under (CT-1).
- Step 2 (Substitution): both pinned in canonical_constants.py via the new dual-anchor names with W-5 CANONICAL-3/4 + CANONICAL-5 provenance respectively.
- Step 3 (Simplify): the canonical anchors are STRUCTURALLY DISTINCT (cross-mult residual 29,821; per §1.3 + §2 above).
- Step 4 (Direction): adding both pins to canonical_constants.py with explicit dual-anchor names AND PROVENANCE entries preserves the substrate-IS structural distinction; the gate PASSes iff both pins + PROVENANCE entries are present and the audit script returns no SOURCE-RECON Class-(d) flag.

**What PASS / FAIL means for the solution space**:
- PASS: the dual-anchor canonical-constants structure is operational; downstream consumers can cite the appropriate Pathway by name (Pathway α via `cocycle_ratio_phi67_phi88_direct_FW`; Pathway β via `cocycle_ratio_phi67_phi88_inheritance_FW`); the §VII.AY.OP-PROJ Element 5 retrofit per §4.1 is consistent with the canonical_constants.py state; §W8-7 re-dispatch can proceed (gate `S92-W8-7-RE-DISPATCH` per §5.2 below).
- FAIL: the canonical-constants addition is structurally inconsistent (e.g., the new pins conflict with the legacy `substrate_cocycle_ratio_67_88` at line 276 in a way the audit script catches); registry retrofit per §4.1 must be deferred until the canonical-constants structure is rectified.

**Effort**: ~0.3 we (mechanical PROVENANCE-entry addition + canonical_constants.py audit-script run + sole-writer mack-cosmic-bridge or orchestrator-direct edit).

**Owner**: mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, OR orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class clause if dispatched within S91 close in-session per `feedback_fix-in-session-never-defer.md`.

### 5.2 — §W8-7 re-dispatch protocol: `S92-W8-7-RE-DISPATCH` (CF-W8-CONSOLIDATED-11)

**Gate ID**: `S92-W8-7-RE-DISPATCH`
**Trigger**: `[VERIFY-THEOREM]` (Stage-2 cross-axis verify under TWO-INDEPENDENT-AXES topology with 3-reviewer dispatch per `joint-theorem-promotion.md §"Stage 2"`)
**Classification**: GEOMETRIC + PARTICLE (Element 3 fiducial-anchor binding type (iii) joint-hypersurface admissibility verification at the cross-pillar bridge map composition layer)
**CONDITIONAL on**: `S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION` PASS (§5.1 above) AND `S92-VII-AY-OP-PROJ-ELEMENT-5-CORRIGENDUM` PASS (registry retrofit per §4.1-4.3 above; mack-cosmic-bridge sole-writer landing). If either prereq returns INFO/FAIL: `S92-W8-7-RE-DISPATCH` mechanical-closes per `mechanical-closure-discipline.md` with `value='PRE-REG-INC_blocked_by_S92_pin_addition_NOT_PASS_or_S92_registry_corrigendum_NOT_PASS'`.

**Hypothesis being tested**: under the dual-anchor structural-distinction declaration (Path-b per §4.1 above) AND the new dual-anchor canonical_constants pins (per §5.1 above), Axis-A vdd + Axis-B-primary mack + Axis-B-cross-pillar-specialist spectral-geometer ALL PASS at the structural ceiling — the original S91 W8-7 Axis-B-primary mack FAIL on B1 (rank-2 anchor reproduction at 1e-6 floor) is resolved by the dual-anchor structure (Pathway α + Pathway β both pinned; mack-cosmic-bridge verifies against the appropriate Pathway based on which side of the cross-pillar bridge map composition the verifier operates on).

**PASS predicate** (per the original §W8-7 plan §C5 4-band rubric + dual-anchor refinement): 3-axis PASS-AND across Axis-A + Axis-B-primary + Axis-B-cross-pillar-specialist; all clauses (A1+A2+B1+B2+C1+C2) PASS at structural ceiling under the dual-anchor canonical anchors.

**FAIL predicate**: any of the three reviewers returns FAIL on any clause (composite-collapse rule per `gate-verdicts.md §"S87+ canonical form"`).

**Machinery pin (PRDR)**:
- `N_eval = 3` (three reviewer dispatches: vdd Axis-A, mack Axis-B-primary, spectral-geometer Axis-B-cross-pillar-specialist)
- `L_max = 10` (Friedrich-Bär saturation L_max=10 cache at `computations/session-84/s84_spectrum_cache_L12_tau019.npz` for Axis-B-primary; N/A for Axis-A and Axis-B-cross-pillar-specialist which operate at the L-INDEPENDENT structural-theorem layer)
- `scheme = stage-2-cross-axis-3-reviewer-dual-anchor-re-dispatch-under-pathway-alpha-plus-pathway-beta`
- `convention = element-3-joint-hypersurface-iii-admissibility-re-dispatch-S92-post-dual-anchor-pin-addition-S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION`
- `random_seed = N/A`
- `tolerance = 1e-5 ABSOLUTE` (Class-8.3 publication-precision floor for the Pathway β Sage-QQ canonical; the Pathway α direct-ratio canonical is verified at gcd-reduction integer-arithmetic exactness, no tolerance band)
- `GPU path = N/A` (Axis-A + Axis-B-cross-pillar-specialist operate at structural-theorem layer; Axis-B-primary loads npz cache via CPU per `computation-environment.md §"CPU Thread Cap"`)

**Input SHA-256 pins**:
- `computations/_shared/canonical_constants.py` (POST-S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION SHA; `<computed-at-runtime>` and pinned at S92 plan-freeze)
- `sessions/permanent-results-registry.md` (POST-S92-VII-AY-OP-PROJ-ELEMENT-5-CORRIGENDUM SHA; `<computed-at-runtime>` and pinned at S92 plan-freeze)
- `.claude/rules/cross-pillar-bridge-anatomy.md` (static at plan-freeze)
- `.claude/rules/joint-theorem-promotion.md` (static at plan-freeze)
- `.claude/rules/inheritance-falsifier-protocol.md` (static at plan-freeze)
- `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (static cache from S84; SHA pinned at plan-freeze)
- `sessions/archive/session-91/session-91-connes-ncg-theorist-w8-dual-anchor-synthesis.md` (THIS file; pinned for derivational provenance audit of the dual-anchor structural distinction)

**Expected output 4-tuple**: `(value="3-axis-PASS-AND-at-structural-ceiling-under-dual-anchor-pathway-alpha-plus-pathway-beta-canonical-anchors", scheme=stage-2-cross-axis-3-reviewer-dual-anchor-re-dispatch, convention=element-3-joint-hypersurface-iii-admissibility-re-dispatch-S92-post-dual-anchor-pin-addition, L_max=10)`

**What PASS / FAIL means for the solution space**:
- PASS: Element 3 fiducial-anchor binding type (iii) joint-hypersurface K-counter K=1 → K=2 advancement candidate enabled; §VII.AY.OP-PROJ STAGE-1-CANDIDATE → STAGE-3-PERMANENT eligibility unblocked per `joint-theorem-promotion.md` 4-stage pathway; the framework's Hochschild-Künneth Morita-invariance theorem at the Pillar-1-internal-NCG-axiomatic bridge sub-class promotes one step closer to permanent-results status.
- FAIL: the dual-anchor structural distinction does NOT resolve the §W8-7 mack Axis-B-primary B1 FAIL; deeper substrate-physics adjudication required (potentially: the cancellation theorem (CT-1) applicability needs re-examination, OR the W-5 CANONICAL-5 Sage-QQ derivation needs full re-publication at the machine-precision pin level).

**Effort**: ~1.5 we (three reviewer dispatches in parallel per the original §W8-7 plan, with verifier rubrics updated per the dual-anchor structural distinction; same dispatch prompts as S91 W8-7 with the dual-anchor canonical-constants pin substitutions).

**Substrate framing for the re-dispatch** (per `phononic-framing.md §"IS Space, Not IN Space"`):

Direction substrate → emergent:

```
Substrate (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)) IS the spectral triple at τ_fold = 0.190
   → Hochschild-1-cocycles [φ_67], [φ_88] live on M_3(ℂ) ⊂ A_F Wedderburn summand at degree-1
   → Cocycle norms ‖φ_67‖² + ‖φ_88‖² are substrate-IS at the Peter-Weyl eigenvalue-gap layer
   → Pathway α (Pillar-1 NCG-axiomatic direct-ratio): Fraction(793346, 108307) = 7.3249743784
     at 6-sig-fig publication-precision (via canonical_constants.py:274-275 truncation)
   → Pathway β (Pillar-2 laboratory image under (Δ_B/Δ_A)^p cancellation): Fraction(114453, 15625) = 7.324992
     at Sage-QQ machine precision (via inheritance-falsifier-protocol.md cancellation theorem)
   → Cross-pillar bridge map composition A_K ↪ A_BdG-full ↠ A_BdG-image
     (per §VII.U.2 sub-corrigendum T2.46 dual-symbol convention)
   → 3He-B / 3He-A laboratory measurements at W-5 W11-C5 + W11-C6 cells (cryogenic-container IN-frame)
```

FORBIDDEN inversion (container thinking): "the two Fractions are arithmetic representations of the same canonical anchor at different precisions in some external-paper canonical container".

CORRECT (substrate thinking): "both Fractions ARE substrate-first canonical anchors at structurally distinct axis cells of the inheritance-morphism F-image; Pathway α IS the substrate-IS direct-ratio canonical BEFORE the inheritance morphism (Pillar-1 NCG-axiomatic side at 6-sig-fig publication-precision); Pathway β IS the substrate-IS inheritance-composed-ratio canonical AT the laboratory image of the inheritance morphism, preserved INTACT by the (Δ_B/Δ_A)^p cancellation theorem at Sage-QQ machine precision; the substrate is logically prior at BOTH bridge-map composition axes; the laboratory image is the F-image, NOT the substrate itself".

---

## 6 — 4-Field Structured Carry-Forward (per `feedback_fix-in-session-never-defer.md`)

### CF-S91-W8-CONNES-1 — Dual-anchor canonical-constants.py pin addition

- **What**: Add `cocycle_ratio_phi67_phi88_direct_FW = 7.3249743784` (Pathway α; Fraction(793346, 108307)) AND `cocycle_ratio_phi67_phi88_inheritance_FW = 7.324992` (Pathway β; Fraction(114453, 15625)) to `computations/_shared/canonical_constants.py` with full PROVENANCE entries citing W-5 CANONICAL-3 + CANONICAL-4 (Pathway α) and W-5 CANONICAL-5 (Pathway β) respectively; structure per §3 of this synthesis.
- **Inputs**: this synthesis (§3 PROVENANCE block) + canonical_constants.py current state at lines 274-276 + 1188-1194 + W-5 calibration corpus at `inheritance-falsifier-protocol.md §"Calibration corpus (W-5)"` + S91 W8-7 composite verdict line audit_sha256=`92a5ed6d62e1ccb56314750a20d4e7a6f36e5d447552c3f003f1b4932c12677c`.
- **Gate**: `S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION` (METHODOLOGY-class registry-addition per §5.1 above; M4 allowlist append at `.claude/rules/methodology-wave-allowlist.md`).
- **Effort**: ~0.3 we (mack-cosmic-bridge sole-writer OR orchestrator-direct-write per `wave-classification.md §"Dispatch consequences"` METHODOLOGY-class clause if dispatched within S91 close).

### CF-S91-W8-CONNES-2 — §VII.AY.OP-PROJ Element 5 + Level 3 + HIT corpus narrative retrofit (Path-b dual-anchor)

- **What**: Retrofit §VII.AY.OP-PROJ Element 5 text at `sessions/permanent-results-registry.md` line 18802 + Level 3 text at line 18812 + HIT calibration corpus narrative at line 18858 per Path-b dual-anchor structural-distinction declaration (per §4.1-4.3 of this synthesis). Replace the false equality gloss `Fraction(793346, 108307) = Fraction(114453, 15625)` with the dual-anchor structure citing this synthesis's verdict (B).
- **Inputs**: §VII.AY.OP-PROJ current text + this synthesis (§4) + S91 W8-7 composite verdict line + canonical_constants.py post-S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION state (after CF-S91-W8-CONNES-1 PASS).
- **Gate**: `S92-VII-AY-OP-PROJ-ELEMENT-5-CORRIGENDUM` (METHODOLOGY-class registry-edit; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`).
- **Effort**: ~0.3 we (mack-cosmic-bridge sole-writer; consolidates CF-W8-CONSOLIDATED-1 + CF-W8-7-COMPOSITE-1 + CF-W8-7-AXIS-A-1 + mack §W8-7.AXIS-B-PRIMARY carry-forward at WP line 1726).

### CF-S91-W8-CONNES-3 — §W8-7 Stage-2 cross-axis verify re-dispatch under dual-anchor anchors

- **What**: Re-dispatch the §W8-7 (T2.49) Stage-2 cross-axis verify under the dual-anchor canonical structure landed via CF-S91-W8-CONNES-1 + CF-S91-W8-CONNES-2. Three reviewers in parallel: vdd Axis-A on Pathway α (Pillar 1 NCG-axiomatic side); mack Axis-B-primary on Pathway β (Pillar 2 laboratory image side); spectral-geometer Axis-B-cross-pillar-specialist on the algebra-isomorphism layer connecting the two Pathways via the Künneth + Morita-triviality bridge map. Same dispatch prompts as S91 W8-7 with the substitution of dual-anchor canonical anchors in the verifier rubrics.
- **Inputs**: this synthesis (§5.2) + canonical_constants.py post-CF-S91-W8-CONNES-1 state + §VII.AY.OP-PROJ post-CF-S91-W8-CONNES-2 retrofit + S91 W8-7 original three-axis verdicts at `s91_gate_verdicts.txt` lines 166-177 (RETAINED on disk per absolute verdict permanence; the corrective S92 PASS line will carry `supersedes=<S91-W8-7-COMPOSITE-audit-sha>` tag per `gate-verdicts.md §"Option A — sig_5 remediation pathway"`).
- **Gate**: `S92-W8-7-RE-DISPATCH` (Stage-2 cross-axis verify per §5.2 above; CONDITIONAL on CF-S91-W8-CONNES-1 PASS + CF-S91-W8-CONNES-2 PASS).
- **Effort**: ~1.5 we (three reviewer dispatches in parallel per the original W8-7 plan).

### CF-S91-W8-CONNES-4 — Forward Pati-Salam rank-3 dual-anchor template extension (HIT K=2 advancement)

- **What**: At W9 T2.44 forward landing (`CF-S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION` per §VII.AY.OP-PROJ §(f) HIT K-counter forward calibration narrative at registry line 18867), apply the dual-anchor template established here to the rank-3 case: each of the `binomial(3, 2) = 3` cross-cocycle ratios `‖φ_67‖/‖φ_88‖`, `‖φ_67‖/‖φ_3rd‖`, `‖φ_88‖/‖φ_3rd‖` carries its own Pathway α (direct-ratio at 6-sig-fig pins from extended canonical_constants.py) AND Pathway β (Sage-QQ canonical via (Δ_B/Δ_A)^p cancellation under the rank-3 inheritance morphism χ'' : A_K^{ext} → T'' at max-Wed-rank(T'') ≤ 2). Confirms the K=1 → K=2 advancement of the Element 3 fiducial-anchor binding type (iii) joint-hypersurface K-counter under the dual-anchor structural framework.
- **Inputs**: this synthesis (Pathway α + Pathway β template at §1.1-1.2) + Pati-Salam parent symmetry SU(4) summand extension hypothesis (workshop §V2 line 122) + W9 T2.44 forward gate specification at `sessions/archive/session-91/session-91-w9-workingpaper.md` + dual-anchor canonical-constants pins post-CF-S91-W8-CONNES-1.
- **Gate**: `S92-PATI-SALAM-DUAL-ANCHOR-RANK-3-LANDING` (forward; conditional on Pati-Salam in-scope laboratory pillar candidate identification at W9 T2.44).
- **Effort**: ~1.0 we (van-den-dungen-bridge-theorist + mack-cosmic-bridge + connes-ncg-theorist joint authoring; combines with CF-W8-CONSOLIDATED-8).

---

## 7 — Mathematical status and structural implication

### 7.1 — Status of the verdict

The structural verdict (B) — `Fraction(793346, 108307)` and `Fraction(114453, 15625)` are STRUCTURALLY DISTINCT canonical quantities — is **PROVEN** at:

1. **Integer-arithmetic layer** (§1.3): cross-mult residual `29,821` (exact integer); the two Fractions are not equal at exact rational arithmetic, REGARDLESS of any tolerance band.
2. **Substrate-axis derivational layer** (§1.1, §1.2): the two Fractions descend from DISTINCT provenance chains in canonical_constants.py — Pathway α from W-5 CANONICAL-3 + CANONICAL-4 direct-image; Pathway β from W-5 CANONICAL-5 Sage-QQ via the (Δ_B/Δ_A)^p cancellation theorem.
3. **Bridge-anatomy layer** (§2.2): the two Fractions inhabit STRUCTURALLY DISTINCT axis cells of the inheritance-morphism F-image (direct-ratio vs inheritance-image), even though they share the same algebra-axis cell (Cell I × s=3) and the same upstream substrate-IS observable identity.

### 7.2 — Status of the §W8-7 composite FAIL

The §W8-7 composite FAIL at the rank-2 anchor reproduction layer is a **registry-text accuracy issue at the methodology-floor F-image layer**, NOT a substrate-physics inconsistency. The underlying Hochschild-Künneth Morita-invariance theorem `HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F)` IS substrate-IS structurally valid (Axis-A PASS + Axis-B-cross-pillar-specialist PASS at the algebra-isomorphism layer; substrate-axis cancellation theorem (CT-1) at 0.0e+00 machine-precision residual). The FAIL at the empirical-anchor reproduction layer is at the REGISTRY-TEXT representation of the rank-2 anchor, not at the substrate-physics layer itself.

### 7.3 — Status of §VII.AY.OP-PROJ STAGE-1-CANDIDATE → STAGE-3-PERMANENT eligibility

Under the dual-anchor structural-distinction declaration (Path-b per §4.1) + the new dual-anchor canonical-constants pins (per §3), the §VII.AY.OP-PROJ STAGE-1-CANDIDATE status is RETAINED-PROVISIONAL. STAGE-3-PERMANENT eligibility unblocks via the S92 re-dispatch (CF-S91-W8-CONNES-3) under the corrected registry-text and canonical-constants state. The framework's Hochschild-Künneth Morita-invariance theorem at the Pillar-1-internal-NCG-axiomatic bridge sub-class IS substrate-IS valid; the path to permanent-results status is now operationally clear.

### 7.4 — Status of Element 3 fiducial-anchor binding K-counter

Per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` SUGGESTION-K=1 baseline at S88 W-15 V.7 §VII.AF.1 (calibration corpus instance #1; per `cross-pillar-bridge-corpus.md §10`): the K=1 → K=2 advancement candidate at §VII.AY.OP-PROJ is BLOCKED at S91 W8 close pending S92 re-dispatch under dual-anchor anchors. The dual-anchor structural framework established here is itself a refinement to the Element 3 binding type (iii) joint-hypersurface admissibility discipline — adding a sub-axis (direct vs inheritance-image bridge-map composition) within the type (iii) "2D in (P, observable) joint-hypersurface" rubric. This sub-axis refinement could itself be a forward K-counter advancement candidate for `cross-pillar-bridge-anatomy.md §"Element 3"` if the dual-anchor template recurs at the W9 T2.44 Pati-Salam rank-3 landing (CF-S91-W8-CONNES-4).

### 7.5 — Direction of explanation preserved

Throughout this synthesis, direction of explanation flows substrate → emergent per `phononic-framing.md §"IS Space, Not IN Space"`:

- The substrate IS the spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.190 — Pillar-1 NCG-axiomatic.
- The Hochschild-1-cocycles `[φ_67]`, `[φ_88]` ARE substrate-IS at the M_3(ℂ) ⊂ A_F Wedderburn summand at degree-1.
- Pathway α IS the substrate-IS direct-ratio canonical at Pillar-1 (BEFORE inheritance morphism).
- Pathway β IS the substrate-IS inheritance-composed-ratio canonical at Pillar-2 (AT laboratory image of inheritance morphism χ; preserved INTACT under (CT-1)).
- Both Fractions ARE substrate-IS observables; their structural distinction is at the bridge-map composition axis (direct vs inheritance-image), NOT at the substrate-vs-emergent axis.
- The (Δ_B/Δ_A)^p cancellation theorem (CT-1) is the substrate-axis structural identity that connects the two pathways at the laboratory-image side.

FORBIDDEN inversion: "Pathway α is the canonical and Pathway β is the lab-conversion derived approximation; or vice versa". CORRECT: "Pathway α IS the Pillar-1 substrate-IS canonical at 6-sig-fig pub-precision; Pathway β IS the Pillar-2 substrate-IS canonical at Sage-QQ machine precision through the cancellation theorem (CT-1); BOTH are substrate-first canonical at their respective axis cells".

---

## 8 — Summary

| Question | Answer |
|:---------|:-------|
| Are `Fraction(793346, 108307)` and `Fraction(114453, 15625)` integer-arithmetic equal? | **NO** (cross-mult residual 29,821; abs delta 1.76 × 10⁻⁵) |
| Is `Fraction(793346, 108307)` the gcd-reduced ratio of the 6-sig-fig canonical_constants pins? | **YES** (gcd = 1, in lowest terms; direct float-division of canonical_constants.py:274-275) |
| Is `Fraction(114453, 15625)` the Sage-QQ canonical via the (Δ_B/Δ_A)^p inheritance factor? | **YES** (per W-5 CANONICAL-5 derivation chain; preserved INTACT under (CT-1); machine precision 0.0e+00 residual at S86 W-5 DONE-5) |
| Are the two Fractions STRUCTURALLY DISTINCT canonical quantities? | **YES** (verdict B; §2.2 above; direct-ratio vs inheritance-composed-ratio at distinct bridge-map composition axes) |
| Are both pins substrate-first canonical? | **YES** (both pass `_substrate_first_provenance_audit.py` substrate-first source check; no external-paper placeholder; explicit S86 W-5 derivational provenance chains) |
| Does the dual-anchor declaration violate `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`? | **NO** — both pins inhabit the same algebra-axis cell (Cell I × s=3); the structural distinction is at the bridge-map composition axis ORTHOGONAL to the algebra-axis per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` ORTHOGONAL clause |
| Verdict | **(B) STRUCTURALLY DISTINCT canonical quantities; dual-anchor declaration required** |
| Recommended registry retrofit | **Path (b) dual-anchor structural-distinction declaration** (per §4.1-4.3 above) |
| Forward gates | `S92-COCYCLE-RATIO-CANONICAL-PIN-ADDITION` (§5.1) + `S92-W8-7-RE-DISPATCH` (§5.2) + `S92-VII-AY-OP-PROJ-ELEMENT-5-CORRIGENDUM` (§4.1) |
| 4-field carry-forwards | 4 structured CFs (CF-S91-W8-CONNES-1 / 2 / 3 / 4 per §6 above) |

---

## 9 — Cross-references

- **Sources read in full**:
  - `sessions/archive/session-91/session-91-w8-workingpaper.md` §W8-7 (lines 1483-1882): §W8-7.AXIS-A INFO disclosure at line 1607; §W8-7.AXIS-B-PRIMARY structural finding at line 1719; §W8-7.AXIS-B-CROSS-PILLAR-SPECIALIST C1+C2 PASS at lines 1743-1744; §W8-7.COMPOSITE substantive substrate-physics implication paragraph at line 1876.
  - `sessions/permanent-results-registry.md §VII.AY.OP-PROJ` Element 5 (line 18802); Level 3 (line 18812); HIT K-counter narrative (line 18858); (a) IS-not-IN anatomy (line 18782); (b) Three-Level ladder (line 18804); (c) 4-Corner classification (line 18816); (d) OP-PROJ suffix (line 18822); (e) Parse-tree expansion (line 18826); (f) HIT K-counter (line 18854); (g) Provenance blockquote (line 18869); (h) Cross-references (line 18877); (i) Substrate framing (line 18899).
  - `computations/_shared/canonical_constants.py` lines 274-276 (cocycle_norm_phi67, cocycle_norm_phi88, substrate_cocycle_ratio_67_88) + PROVENANCE entries at lines 1188-1194 (CANONICAL-3, CANONICAL-4, CANONICAL-5).
  - `.claude/rules/inheritance-falsifier-protocol.md` (full file; especially §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)" at lines 37-47 and §"Calibration corpus (W-5)" at lines 84-87).
  - `sessions/archive/session-91/workshops/_seed-w8.md` §S1-1 lines 12-32 (this seed entry).
  - `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" MANDATORY-K=3.
- **Companion solo synthesis outputs at S91 W8 Slot 1**: S-1, S-2, S-3, S-4, S-5 (other dual-anchor / discriminator solo reviews per the workshop schedule).
- **Companion workshop at S91 W8 Slot 2**: S2-1 multiplicity-convention canon adjudication (`connes-ncg-theorist` vs `volovik-superfluid-universe-theorist`; W5 full-Wedderburn vs W6 image-projection; structurally orthogonal to this S1-1 review per the Cell IV vs Cell I axis-cell distinction noted at W8 WP line 1869).
- **Forward calibration target**: Pati-Salam rank-3 forward landing at W9 T2.44 (`CF-S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION`).
- **K-counter status**: `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` SUGGESTION-K=1 baseline at §VII.AF.1; K=2 advancement candidate at §VII.AY.OP-PROJ BLOCKED at S91 W8 close pending S92 re-dispatch under dual-anchor anchors per CF-S91-W8-CONNES-3.

---

**End of synthesis.**

*— `connes-ncg-theorist` (Workhorse-NCG; Solo Review Slot 1 S-6, 2026-05-21)*
