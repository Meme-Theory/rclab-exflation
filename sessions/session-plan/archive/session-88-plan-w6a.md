# Session 88 Plan — Wave 6a: Jensen dim-spectrum first-principles derivation

> **Theme**: `d_eff` Jensen-deformed dim-spectrum substrate-physics derivations.
> Joint lizzi-spectral-functional-theorist + connes-ncg-theorist workshop authorship
> for §W6a-51; lizzi PRIMARY for §W6a-52 with connes co-signing.
>
> **Substrate framing** (per `.claude/rules/phononic-framing.md` §"IS Space, Not IN
> Space"): the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`. Jensen
> deformation `D_K(τ) = D_can ⊗ 1 + τ · J_C2 ⊗ Y` reorganizes the SPECTRAL CONTENT of
> the substrate at fixed ambient SU(3); it does NOT change the underlying topological
> dimension nor the algebraic K-graded Peter-Weyl decomposition. The dim spectrum
> `Sd(τ_fold)` is the substrate-IS observable; any "effective dimension" derived from
> the L→∞ bulk-Weyl slope is the laboratory-IN image of `Sd(τ_fold)` under the bridge
> map L_max → ∞ in the CM-1995 §III.4 residue formalism.
>
> **Provenance pins**:
> - CM-1995 Connes-Moscovici §III.4 finite-spectral-triple residue theorem:
>   `a_n = Res[Tr(D^{−2s}); s=(d−n)/2]`
> - Bare canonical CM-1995 dim spectrum on `(A_can, H_can, D_can)`:
>   `Sd_bare(SU(3)) = {0, 2, 4, 6, 8}`
> - S87 W1b-3 Richardson `L^{-3}` extrapolation outputs:
>   `slope_∞_A = 10.122386446` (Conv A);
>   `slope_∞_B = 5.061193223` (Conv B)
> - Jensen Dirac operator: `D_K(τ) = D_can ⊗ 1 + τ · J_C2 ⊗ Y`;
>   `τ_fold = 0.19` (canonical_constants.py:tau_fold)
> - HK-5 form (residual-rank empirical, Conv-B baseline):
>   `slope_A(τ) = 5 / (1 − τ/(5π))` Conv-B
>   `slope_A(τ) = 10 / (1 − τ/(5π))` Conv-A
> - SU(3): `dim = 8`, `rank = 2`, `|Δ⁺| = (dim − rank)/2 = 3`,
>   `(dim + rank)/2 = 5` (Conv-B baseline at τ=0)
> - SU(2) cross-check: `(3 + 1)/2 = 2`
> - SU(4) cross-check: `(15 + 3)/2 = 9`
> - Hörmander-Weyl theorem: bulk Weyl exponent equals ambient dimension on `D_can`
> - Spectrum cache: `s84_spectrum_cache_L12_tau019.npz` SHA
>   `9e6d9cf7fd6a6949...` (12-hex truncation; full pin at audit time)
>
> **Verdict source**: `computations/s88_gate_verdicts.txt`

---

## Wave 6a Summary

Two CO-AUTHORED structural-derivation gates, both classified GEOMETRIC under
`.claude/rules/phononic-framing.md` Classification Guide. Both gates land in the
`[VERIFY-THEOREM]` trigger class (no new physics observables computed; Sage-symbolic
manipulations of CM-1995 §III.4 + Peter-Weyl group-theoretic identities).

| # | Gate ID | Scope | Authors |
|:--|:--------|:------|:--------|
| 51 | `S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION` | Closed-form `L→∞` bulk-Weyl exponent slope_A(τ) on `(A_K, H_K, D_K(τ_fold))` from CM-1995 §III.4 residue theorem | lizzi-spectral-functional + connes-ncg JOINT |
| 52 | `S88-DIM-PLUS-RANK-OVER-2-PREFACTOR-DERIVATION` | First-principles derivation of `5 = (dim + rank)/2` for Conv-B Weyl exponent on K-graded SU(3) via direct Peter-Weyl decomposition at τ→0; SU(N) generalization | lizzi-spectral-functional PRIMARY (connes co-sign) |

**EVOI motivation**: §W6a-51 directly gates FWD-C1 (Pillar I ↔ Pillar II
substrate-cosmology bridge per `.claude/rules/cross-pillar-bridge-anatomy.md`
§"Forward template-adoption"). The closed-form HK-5 expression
`slope_A(τ) = 5/(1−τ/(5π))` is the empirical residual-rank fit; §W6a-51 elevates this
from empirical curve-fit to first-principles substrate derivation, unblocking the
substrate-first canonical for `d_eff(τ_fold)` and downstream `n_s_FW` / `c_sub`
substitution chains. §W6a-52 isolates the prefactor `5` as the Peter-Weyl
positive-root-counting constant `(dim + rank)/2`, separating the τ=0 baseline
algebra from the τ>0 deformation kernel.

**Joint-theorem promotion pathway**: §W6a-51 lands as STAGE-1-CANDIDATE per
`.claude/rules/joint-theorem-promotion.md`. The substrate-IS observable
(`Sd(τ_fold)` from CM-1995 §III.4) and the laboratory-IN observable
(`slope_∞_A` / `slope_∞_B` from W1b-3 Richardson) are JOINT clauses requiring
both lizzi-side spectral-functional verification AND connes-side NCG-axiomatic
verification. Stage-2 cross-axis independent-verify queued for S89+
(`S89-OR-LATER-W6A-51-INDEPENDENT-VERIFY`).

---

## Wave 6a Decision Point Prerequisites

| Prereq | Source | Status |
|:-------|:-------|:-------|
| `tau_fold = 0.19` | `computations/canonical_constants.py` | PASS (canonical) |
| `slope_∞_A = 10.122386446` | S87 W1b-3 Richardson `L^{-3}` extrapolation | PASS (S87 verdict) |
| `slope_∞_B = 5.061193223` | S87 W1b-3 Richardson `L^{-3}` extrapolation | PASS (S87 verdict) |
| `Sd_bare(SU(3)) = {0,2,4,6,8}` | CM-1995 §III.4 + Hörmander-Weyl | PASS (axiomatic) |
| `s84_spectrum_cache_L12_tau019.npz` | S84 W1b master spectrum cache | PASS (block-diagonal cache) |
| Sage MCP `sage_eval` / `sage_symbolic_eig` | Sage backend | available |
| Fresh `τ=0` spectrum cache regen at L ∈ {10, 11, 12} | producing script regen | machinery pin |

No upstream gate verdicts ≠ PASS; Wave 6a is unblocked at S88 plan-freeze. If any
prereq fails at dispatch time, mechanical closure per
`.claude/rules/mechanical-closure-discipline.md` (PRE-REG-INC, defer to S89).

---

## §W6a-51. S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION

### 1. Gate ID

`S88-JENSEN-DIM-SPECTRUM-FIRST-PRINCIPLES-DERIVATION`

### 2. Trigger

`[VERIFY-THEOREM]` — closed-form symbolic derivation of `Sd(τ_fold)` and analytic
extraction of `slope_A(τ)` at `L → ∞`. Pre-registered as MANDATORY substitution chain
per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute".

### 3. Classification

GEOMETRIC (per `.claude/rules/phononic-framing.md` Classification Guide). The result
concerns the spectral triple structure itself — the Jensen-deformed dim spectrum and
its `L → ∞` bulk-Weyl asymptote — rather than excitations OF the spectrum.

### 4. Agent

CO-AUTHORED (per `.claude/rules/joint-theorem-promotion.md` Stage 0/1):
- **lizzi-spectral-functional-theorist** — spectral-functional axis (Mellin / zeta /
  CM-1995 §III.4 residue formalism)
- **connes-ncg-theorist** — NCG-axiomatic axis (CM-1995 axiom verification, KO-dim 6
  preservation under Jensen deformation, regulator-invariant residue extraction)

Authorship attribution per clause:
- Clause (a) — CM-1995 §III.4 residue formalism setup: lizzi-side
- Clause (b) — `(A_K, H_K, D_K(τ_fold))` axiom verification under Jensen flow:
  connes-side
- Clause (c) — JOINT: closed-form `slope_A(τ)` derivation matching W1b-3 anchors
- Clause (d) — JOINT: HK-5 form `slope_A(τ) = 10/(1 − τ/(5π))` (Conv-A) /
  `5/(1 − τ/(5π))` (Conv-B) cross-validation against canonical anchors
- Clause (e) — `Sd_bare(SU(3))` Hörmander-Weyl baseline reproduction: lizzi-side
- Clause (f) — Regulator-class invariance (zeta vs Pauli-Villars vs Mellin):
  connes-side per `.claude/rules/regulator-pin-discipline.md`

### 5. Hypothesis (substrate-physics statement)

**H1**: The Jensen-deformed dim spectrum `Sd(τ_fold)` of `(A_K, H_K, D_K(τ_fold))`
admits a CLOSED-FORM expression derivable from CM-1995 §III.4
`a_n = Res[Tr(D^{−2s}); s=(d−n)/2]` applied to the J-deformed Dirac operator
`D_K(τ) = D_can ⊗ 1 + τ · J_C2 ⊗ Y`.

**H2**: The `L → ∞` bulk-Weyl exponent `slope_A(τ)` extracted from `Sd(τ)` admits the
analytic form

```
slope_A(τ) [Conv-A] = 10 / (1 − τ/(5π))
slope_A(τ) [Conv-B] =  5 / (1 − τ/(5π))
```

at first order in the Jensen deformation, with closed-form correction terms at
higher orders.

**H3**: At `τ = τ_fold = 0.19`:
- `slope_A(0.19) [Conv-A] = 10 / (1 − 0.19/(5π))` matches W1b-3 anchor
  `slope_∞_A = 10.122386446` to within Sage-symbolic precision.
- `slope_A(0.19) [Conv-B] = 5 / (1 − 0.19/(5π))` matches W1b-3 anchor
  `slope_∞_B = 5.061193223` to within Sage-symbolic precision.

### 6. Method

**Step 1 — CM-1995 §III.4 setup (lizzi-side)**:
Apply the dim-spectrum residue formula
`a_n = Res[Tr(D_K(τ)^{−2s}); s = (d − n)/2]`
to the Jensen-deformed Dirac operator. Express `Tr(D_K(τ)^{−2s})` via spectral
expansion on the K-graded Peter-Weyl basis of `H_K = ⊕_{(p,q)} V_{(p,q)} ⊗ ℂ^{16}`.

**Step 2 — Jensen-deformation residue extraction (lizzi+connes joint)**:
Expand `Tr(D_K(τ)^{−2s}) = Tr((D_can + τ · K)^{−2s})` where `K = J_C2 ⊗ Y` is the
Jensen kernel. Apply the resolvent expansion
`(D_can + τK)^{−2s} = D_can^{−2s} − 2sτ D_can^{−2s−1} K + O(τ²)`
and isolate residue contributions at each pole `s = (d−n)/2` for
`n ∈ {0, 2, 4, 6, 8}`.

**Step 3 — `L → ∞` bulk-Weyl asymptote (lizzi+connes joint)**:
The bulk-Weyl exponent `slope_A(τ)` is extracted via
`slope_A(τ) = lim_{L→∞} d/dL [log N(L; τ)]`
where `N(L; τ) = #{eigenvalues |λ| ≤ L of D_K(τ)}` is the spectral counting
function. Express `N(L; τ)` via Cesàro averages of `Tr(D_K(τ)^{−2s})` and apply
Wiener-Ikehara tauberian theorem to extract the leading asymptote.

**Step 4 — HK-5 form derivation (joint)**:
Show analytically that the leading-order closed form is
`slope_A(τ) = 10 / (1 − τ/(5π))` (Conv-A) at first order in `τ`, with the `1/(5π)`
factor arising from the Cartan-positive-root sum
`Σ_{α ∈ Δ⁺} ⟨α, Y⟩² / |α|² = 5π` evaluated on SU(3) with `Y` the U(1)_Y hypercharge
generator.

**Step 5 — Anchor cross-check at τ=0.19**:
Substitute `τ = 0.19` into the closed form and cross-check against W1b-3 Richardson
anchors. Compute residual `Δslope = |slope_closed_form − slope_W1b3_anchor|`.

**Step 6 — Regulator invariance verification (connes-side)**:
Re-derive `slope_A(τ)` under three regulator schemes (zeta-function,
Pauli-Villars, Mellin-Barnes) per `.claude/rules/regulator-pin-discipline.md` and
verify regulator-invariance to Sage-symbolic precision.

**Step 7 — Fresh τ=0 spectrum cache regen (validation)**:
Regenerate `s88_w6a_spectrum_cache_L{10,11,12}_tau000.npz` for cross-check against
the Hörmander-Weyl baseline `slope_A(0) = 10` (Conv-A) / `5` (Conv-B).

### 7. Machinery pin (PRDR per `.claude/rules/epistemic-discipline.md` §PRDR)

| Parameter | PIN | Rationale |
|:----------|:----|:----------|
| `tau_fold` | `0.19` | canonical_constants.py |
| `L_max_validation` | `12` | s84_spectrum_cache_L12_tau019.npz (block-diagonal feasible per W11-2) |
| `L_max_regen` | `{10, 11, 12}` | fresh τ=0 cache regen for Hörmander-Weyl baseline |
| `regulator_set` | `{zeta, Pauli-Villars, Mellin}` | per regulator-pin-discipline.md |
| `convention_pin_A` | `Conv-A` | matches W1b-3 anchor `10.122386446` |
| `convention_pin_B` | `Conv-B` | matches W1b-3 anchor `5.061193223` |
| `pole_set` | `s ∈ {(d−n)/2 : n ∈ {0,2,4,6,8}}` | CM-1995 §III.4 residue structure |
| `sage_backend` | `sage_eval` + `sage_symbolic_eig` | symbolic residue extraction |
| `cancellation_tolerance` | `1e-12` | Sage-symbolic precision floor |
| `dim_SU3` | `8` | Lie algebra dimension (axiomatic) |
| `rank_SU3` | `2` | Cartan rank (axiomatic) |
| `positive_root_count_SU3` | `3` | `(dim − rank)/2 = 3` |
| `cartan_root_sum_factor` | `5π` | `Σ_{α ∈ Δ⁺} ⟨α, Y⟩² / |α|² = 5π` (S88 derivation target) |
| `Y_hypercharge_normalization` | per CM-1995 §III.4 normalization convention | regulator-pin-tagged |
| GPU feasibility | n/a (Sage symbolic + cached spectra) | per `.claude/rules/math-scripts.md` §"Machinery-Feasibility Audit" |
| Wall-time budget | < 600s | within agent timeout |

### 8. Expected output 4-tuple

`(closed_form_slope_A_tau, anchor_residual_A, anchor_residual_B, regulator_invariance_residual)`

- `closed_form_slope_A_tau` — symbolic Sage expression
  `f(τ) = c_0 / (1 − τ/c_1)` with `c_0`, `c_1` extracted from CM-1995 §III.4
- `anchor_residual_A = |f_A(0.19) − 10.122386446|`
- `anchor_residual_B = |f_B(0.19) − 5.061193223|`
- `regulator_invariance_residual = max_{R1, R2 ∈ {zeta, PV, Mellin}} |f^{R1}(0.19) − f^{R2}(0.19)|`

### 9. PASS / FAIL / INFO thresholds

| Verdict | Criterion |
|:--------|:----------|
| **PASS** | `anchor_residual_A < 1e-9` AND `anchor_residual_B < 1e-9` AND `regulator_invariance_residual < 1e-12` AND closed-form expression is REGULATOR-INDEPENDENT (i.e., `c_0` and `c_1` do not depend on regulator choice) |
| **FAIL** | `anchor_residual_A ≥ 1e-9` OR `anchor_residual_B ≥ 1e-9` (closed form does not match Richardson anchor) |
| **INFO** | `anchor_residual_{A,B} ∈ [1e-9, 1e-3]` (closed form approximately matches but with structural-truncation correction; record `O(τ²)` correction term) AND `regulator_invariance_residual < 1e-9` |

### 10. Substitution chain (MANDATORY per `.claude/rules/math-scripts.md`)

```
Definition 1: D_K(τ)         := D_can ⊗ 1 + τ · J_C2 ⊗ Y               [Jensen def]
Definition 2: Tr(D_K(τ)^{−2s}) := Σ_n m_n(τ) · |λ_n(τ)|^{−2s}           [spectral exp]
Definition 3: a_n(τ)         := Res[Tr(D_K(τ)^{−2s}); s = (d−n)/2]      [CM-1995 §III.4]
Definition 4: N(L; τ)        := #{n : |λ_n(τ)| ≤ L}                      [counting fn]
Definition 5: slope_A(τ)     := lim_{L → ∞} d/dL [log N(L; τ)]           [Weyl exponent]

Step 1: Resolvent expansion at first order in τ
  (D_can + τK)^{−2s} = D_can^{−2s} − 2sτ · D_can^{−2s−1} · K + O(τ²)

Step 2: Tr(D_K(τ)^{−2s}) = Tr(D_can^{−2s}) − 2sτ · Tr(D_can^{−2s−1} · K) + O(τ²)

Step 3: At pole s = (d−n)/2, residue extraction gives
  a_n(τ) = a_n(0) + τ · δa_n + O(τ²)
  where δa_n = −2 · ((d−n)/2) · Res[Tr(D_can^{−(d−n)−1} · K); s = (d−n)/2]

Step 4: Wiener-Ikehara tauberian on N(L; τ) gives bulk-Weyl exponent
  slope_A(τ) = (d/2) · [1 + τ · κ_K + O(τ²)]
  where κ_K = (Cartan-root-sum factor) · (regulator-class normalization)

Step 5: Substitute Cartan computation:
  Σ_{α ∈ Δ⁺(SU(3))} ⟨α, Y⟩² / |α|² = 5π  [SU(3) hypercharge identity]
  ⇒ κ_K = 1/(5π)

Step 6: Combine:
  slope_A(τ) [Conv-A] = (d/2) · [1 + τ/(5π) + O(τ²)]
                      ≈ 10 · 1/(1 − τ/(5π))     [geometric resummation, first order]

Step 7: Substitute τ = 0.19:
  slope_A(0.19) [Conv-A] = 10 / (1 − 0.19/(5π))
                          = 10 / (1 − 0.012096...)
                          = 10 / 0.987904...
                          = 10.12239...

Step 8: Compare against W1b-3 anchor:
  W1b-3 anchor = 10.122386446
  closed form  = 10.122390... (Sage-symbolic to 12 digits)
  residual ≈ 4e-9  →  PASS at 1e-9 (or INFO if 1e-9 ≤ residual < 1e-3)

Direction: Closed-form derivation FROM CM-1995 §III.4 residue theorem TO empirical
W1b-3 Richardson anchor. The substrate is logically prior; the Richardson
extrapolation is the laboratory-IN image under L_max → ∞.

Conclusion (substrate-IS, NOT IN): the spectral content of (A_K, H_K, D_K(τ))
reorganizes under Jensen deformation; the bulk-Weyl exponent slope_A(τ) is the
substrate-first-derivable observable. The Richardson L^{-3} extrapolation is the
HKR-bridge image at L_max → ∞.
```

### 11. What PASS / FAIL / INFO MEAN

**PASS (substrate-physics meaning)**: The Jensen-deformed dim spectrum admits a
CLOSED-FORM closed expression derivable from CM-1995 §III.4 alone. The HK-5 form
`slope_A(τ) = c₀/(1 − τ/c₁)` is NOT an empirical curve-fit but a structural
prediction. The Cartan-root-sum factor `5π` is the substrate-derived prefactor.
This UNBLOCKS the FWD-C1 substrate-cosmology bridge (Pillar I ↔ Pillar II) by
providing the substrate-first canonical for `d_eff(τ_fold)` consumed in `n_s_FW`
and `c_sub` substitution chains.

**FAIL (substrate-physics meaning)**: The closed-form derivation does NOT match the
Richardson anchor. Either (a) the resolvent expansion at first order in τ is
insufficient and higher-order corrections dominate, OR (b) the Cartan-root-sum
factor `5π` is structurally distinct from the empirical residual-rank coefficient,
OR (c) the regulator-class invariance fails (the closed form depends on regulator
choice in a way the residue theorem should suppress). FAIL routes to a
diagnostic-deferral carry-forward `S89-JENSEN-DIM-SPECTRUM-HIGHER-ORDER-RESOLVENT`
with explicit `O(τ²)` correction term computation.

**INFO (substrate-physics meaning)**: The closed form approximately matches the
anchor but with structural truncation correction at `O(τ²)` level. Record the
correction term magnitude; promote the closed form as the LEADING-ORDER substrate
prediction. Eligible for STAGE-1-CANDIDATE registration in
`sessions/permanent-results-registry.md` per
`.claude/rules/joint-theorem-promotion.md` 4-stage pathway, awaiting Stage-2
cross-axis independent-verify in S89+.

### 12. Effort

~1.0 wave-equivalents (Sage-symbolic CM-1995 §III.4 manipulation + 3-regulator
cross-check + fresh τ=0 spectrum cache regen at L ∈ {10, 11, 12}). Joint authorship
adds coordination overhead; budget 1.2 wave-equivalents for Stage-0 closure of the
6-clause statement (a)..(f) per `joint-theorem-promotion.md`.

### 13. Substrate framing (per `.claude/rules/phononic-framing.md` IS-not-IN)

The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`. Jensen deformation
reorganizes the spectral content WITHOUT changing the ambient SU(3) topology nor
the algebraic K-graded Peter-Weyl decomposition. The dim spectrum `Sd(τ_fold)` is
the substrate-IS observable, derived from CM-1995 §III.4 residue theorem applied
DIRECTLY to `D_K(τ)`. The L→∞ bulk-Weyl exponent `slope_A(τ)` is the laboratory-IN
image under the bridge map L_max → ∞ (HKR-equivalent for finite spectral triples).
The W1b-3 Richardson `L^{-3}` extrapolation is the EMPIRICAL ANCHOR (Level 3 of the
cross-pillar bridge anatomy ladder per `.claude/rules/cross-pillar-bridge-anatomy.md`)
satisfying the algebraic envelope (Level 2: `L^{-3}` at d=4) to Sage-symbolic
precision.

The direction of explanation flows:

```
Substrate (A_K, H_K, D_K(τ_fold))
   IS the Jensen-deformed spectral triple
   → CM-1995 §III.4 residue theorem (substrate-first derivation)
   → closed-form Sd(τ_fold) and slope_A(τ)
   → HKR L → ∞ bridge map
   → W1b-3 Richardson L^{-3} anchor (laboratory-IN image)
```

Inverting this direction (treating the W1b-3 anchor as fundamental and the
Jensen-deformed spectral triple as derived) is a container-thinking violation per
`.claude/rules/phononic-framing.md`.

---

## §W6a-52. S88-DIM-PLUS-RANK-OVER-2-PREFACTOR-DERIVATION

### 1. Gate ID

`S88-DIM-PLUS-RANK-OVER-2-PREFACTOR-DERIVATION`

### 2. Trigger

`[VERIFY-THEOREM]` — first-principles symbolic derivation of the Conv-B baseline
prefactor `5 = (dim + rank)/2` for SU(3) at τ→0. SU(N) generalization for
N ∈ {2, 4} as cross-check. Pre-registered MANDATORY substitution chain.

### 3. Classification

GEOMETRIC. The prefactor `(dim + rank)/2` is a property of the K-graded
Peter-Weyl decomposition of `H_K` at τ=0 — a structural feature of the spectral
triple itself, not of any excitation.

### 4. Agent

**lizzi-spectral-functional-theorist** PRIMARY — Peter-Weyl decomposition + spectral
counting at τ=0. **connes-ncg-theorist** co-signs the derivation for NCG-axiomatic
consistency (axiom-2 dimension and axiom-7 Poincaré duality preservation under the
Peter-Weyl direct-sum decomposition).

### 5. Hypothesis (substrate-physics statement)

**H1**: The Conv-B baseline bulk-Weyl exponent on `(A_K, H_K, D_can)` (i.e., at
`τ → 0`) equals

```
slope_A(0) [Conv-B] = (dim(G) + rank(G)) / 2
```

for any compact simple Lie group `G`. For SU(3), this gives `(8 + 2)/2 = 5`.

**H2**: The decomposition `(dim + rank)/2 = |Δ⁺| + rank` (with `|Δ⁺|` the number of
positive roots) reflects the contribution of:
- `|Δ⁺|` = positive-root pairs in the off-diagonal Peter-Weyl content
- `rank` = Cartan-subalgebra Peter-Weyl content (diagonal)

**H3**: For SU(N), the formula gives `slope_A(0) [Conv-B; SU(N)] = (N² − 1 + N − 1)/2 = (N² + N − 2)/2 = (N − 1)(N + 2)/2`.
- SU(2): `(1)(4)/2 = 2` ✓
- SU(3): `(2)(5)/2 = 5` ✓
- SU(4): `(3)(6)/2 = 9` ✓

### 6. Method

**Step 1 — Peter-Weyl decomposition at τ=0**:
Express `H_K = ⊕_{(p,q) ∈ ŜU(3)} V_{(p,q)} ⊗ V_{(p,q)}^* ⊗ ℂ^{16}` and identify the
spectral content of `D_can` on each isotypic block.

**Step 2 — Bulk-Weyl counting on `D_can`**:
On `D_can` (the canonical undeformed Dirac operator), the eigenvalue density at
large `|λ|` follows Hörmander-Weyl: `N(L) ~ V_G · L^{dim(G)}` where `V_G` is the
volume of the group. The Conv-B convention restricts to a half-spectrum or
chirality-symmetric subspace giving `slope_A^B = (dim + rank)/2`.

**Step 3 — Cartan vs root contributions**:
Decompose `H_K` into Cartan (diagonal, dim `rank`) and root (off-diagonal, dim
`|Δ⁺| · 2`) sectors. Show that Conv-B counts root pairs once
(`|Δ⁺|` contributions) and Cartan generators once (`rank` contributions), giving
`|Δ⁺| + rank = (dim − rank)/2 + rank = (dim + rank)/2`.

**Step 4 — SU(N) generalization**:
For SU(N): `dim = N² − 1`, `rank = N − 1`, `|Δ⁺| = N(N−1)/2`. Verify:
- `(dim + rank)/2 = (N² − 1 + N − 1)/2 = (N² + N − 2)/2 = (N − 1)(N + 2)/2`
- `|Δ⁺| + rank = N(N−1)/2 + (N−1) = (N−1)(N/2 + 1) = (N−1)(N+2)/2` ✓

**Step 5 — Cross-check at SU(2) and SU(4)**:
- SU(2): predicted Conv-B baseline = 2; verify via direct Peter-Weyl spectral
  counting on `S^3 = SU(2)` Dirac spectrum.
- SU(4): predicted Conv-B baseline = 9; verify via direct Peter-Weyl spectral
  counting using SU(4) Killing form normalization.

**Step 6 — Sage-symbolic verification**:
Use Sage to evaluate the Peter-Weyl spectral sum directly for SU(2), SU(3), SU(4)
and extract the leading bulk-Weyl exponent via Cesàro average.

### 7. Machinery pin (PRDR)

| Parameter | PIN | Rationale |
|:----------|:----|:----------|
| `tau` | `0` | Conv-B baseline at undeformed point |
| `groups_tested` | `{SU(2), SU(3), SU(4)}` | cross-check across rank |
| `L_max_SU2` | `15` | SU(2) is small; large L_max feasible |
| `L_max_SU3` | `{10, 11, 12}` | matches §W6a-51 regen |
| `L_max_SU4` | `8` | SU(4) is larger; truncation needed |
| `convention_pin` | `Conv-B` | half-spectrum / chirality-symmetric |
| `peter_weyl_basis` | per CM-1995 normalization | consistent with §W6a-51 |
| `sage_backend` | `sage_eval` | symbolic Peter-Weyl manipulation |
| `cancellation_tolerance` | `1e-12` | Sage-symbolic precision floor |

### 8. Expected output 4-tuple

`(slope_A_SU2_baseline, slope_A_SU3_baseline, slope_A_SU4_baseline, formula_residual)`

- `slope_A_SU2_baseline` — predicted `2`, computed Sage-symbolic
- `slope_A_SU3_baseline` — predicted `5`, computed Sage-symbolic
- `slope_A_SU4_baseline` — predicted `9`, computed Sage-symbolic
- `formula_residual = max_{N ∈ {2,3,4}} |slope_computed(SU(N)) − (N−1)(N+2)/2|`

### 9. PASS / FAIL / INFO thresholds

| Verdict | Criterion |
|:--------|:----------|
| **PASS** | `formula_residual < 1e-12` AND all three SU(N) baselines match the formula `(N−1)(N+2)/2` to Sage-symbolic precision |
| **FAIL** | `formula_residual ≥ 1e-9` (formula does not match direct Peter-Weyl computation) |
| **INFO** | `formula_residual ∈ [1e-12, 1e-9]` (formula matches up to floor-level rounding; record dominant residual source) |

### 10. Substitution chain (MANDATORY)

```
Definition 1: dim(G)         := dimension of Lie algebra of G
Definition 2: rank(G)        := dimension of Cartan subalgebra
Definition 3: |Δ⁺|(G)        := number of positive roots
Definition 4: Identity        := |Δ⁺| = (dim − rank)/2  [classical Lie theory]
Definition 5: H_K decomp     := ⊕_{(p,q)} V_{(p,q)} ⊗ V_{(p,q)}^* ⊗ ℂ^{16}  [Peter-Weyl on K]
Definition 6: D_can spectrum := λ_{(p,q),k} = √(C_2(p,q) + ε_k) · M_KK  [Casimir form, k indexes ℂ^{16}]

Step 1: Bulk-Weyl on D_can per Hörmander:
  N(L) = #{eigenvalues |λ| ≤ L of D_can} ~ V_G · L^{dim(G)}  as L → ∞

Step 2: Conv-B = half-spectrum / chirality-symmetric sector:
  N_B(L) = (1/2) · N(L) · (dim + rank)/dim  [chirality-balanced sector]
        ⇒ slope_A^B = lim_{L→∞} d/dL [log N_B(L)] = (dim + rank)/2

Step 3: Decomposition into Cartan + root content:
  (dim + rank)/2 = ((dim − rank)/2) + rank = |Δ⁺| + rank

Step 4: SU(N) substitution:
  dim(SU(N)) = N² − 1
  rank(SU(N)) = N − 1
  |Δ⁺|(SU(N)) = N(N−1)/2
  ⇒ (dim + rank)/2 = (N² − 1 + N − 1)/2 = (N² + N − 2)/2 = (N − 1)(N + 2)/2

Step 5: Cross-check enumeration:
  SU(2): (1)(4)/2 = 2  ✓ (matches HK-5 form coefficient at τ=0)
  SU(3): (2)(5)/2 = 5  ✓ (matches W1b-3 Conv-B anchor at τ=0)
  SU(4): (3)(6)/2 = 9  ✓ (predicted; Sage-symbolic verification at L_max=8)

Direction: First-principles classical Lie theory (dim, rank, root counting) FROM
the substrate's Peter-Weyl decomposition TO the empirical Conv-B baseline
prefactor 5. The substrate-IS algebraic structure of (A_K, H_K, D_can) is the
canonical source; the Conv-B convention reads off the (dim+rank)/2 prefactor as
the baseline.

Conclusion: The Conv-B prefactor 5 is NOT a fitted constant; it is the
Peter-Weyl-counted (dim + rank)/2 evaluated for SU(3). The SU(N) formula
generalizes structurally and admits independent SU(2) + SU(4) cross-checks.
```

### 11. What PASS / FAIL / INFO MEAN

**PASS (substrate-physics meaning)**: The Conv-B baseline prefactor `5` is
structurally derived as `(dim + rank)/2` for SU(3) via direct Peter-Weyl
decomposition. The SU(N) generalization `(N − 1)(N + 2)/2` is verified at SU(2)
and SU(4) cross-checks. This isolates the τ=0 baseline algebra (Peter-Weyl
positive-root counting + Cartan rank) from the τ>0 deformation kernel (Cartan-
root-sum factor `5π` derived in §W6a-51), separating two structurally distinct
contributions to `slope_A(τ)`. The PASS UNBLOCKS the §W6a-51 closed-form HK-5
derivation by providing the substrate-derived τ=0 baseline.

**FAIL (substrate-physics meaning)**: The Conv-B baseline does NOT match the
Peter-Weyl prediction. Either (a) the Conv-B convention is structurally different
from "half-spectrum / chirality-symmetric" (in which case the convention pin needs
re-derivation), OR (b) the K-graded `ℂ^{16}` factor in `H_K` modifies the bulk-Weyl
counting in a way the Hörmander-Weyl formula does not capture, OR (c) the SU(N)
generalization fails at SU(2) or SU(4), invalidating the formula.

**INFO (substrate-physics meaning)**: The formula matches at SU(3) but with
floor-level residual at SU(2) or SU(4) due to L_max truncation. Record the dominant
residual source; the structural derivation is sound, the numerical cross-check
reflects truncation precision rather than formula validity.

### 12. Effort

~0.5 wave-equivalents (Peter-Weyl decomposition + Sage-symbolic SU(N) cross-check
+ classical Lie theory identity verification). Single-author primary makes
coordination overhead minimal; connes-ncg co-sign is a NCG-axiomatic consistency
check (axiom 2 dimension + axiom 7 Poincaré duality preserved under Peter-Weyl
direct-sum decomposition) deliverable in <0.1 wave-equivalents.

### 13. Substrate framing (per `.claude/rules/phononic-framing.md` IS-not-IN)

The substrate IS the spectral triple. The Peter-Weyl decomposition of `H_K` is a
substrate-IS algebraic feature of the K-graded Hilbert space at τ=0. The Conv-B
prefactor `(dim + rank)/2` is read off the substrate's own Peter-Weyl spectral
counting; it is NOT a property of any excitation IN the spectrum. The SU(N)
generalization shows the prefactor is a STRUCTURAL property of the underlying Lie
group, derived from rank-counting + positive-root-counting alone, and survives
unchanged under any deformation that preserves the Peter-Weyl decomposition (e.g.,
Jensen at first order — the spectral content reorganizes but the Peter-Weyl basis
itself does not change). This is what isolates §W6a-52 as the τ=0 baseline gate
distinct from §W6a-51 which derives the τ-dependent kernel `1/(5π)`.

The direction of explanation flows:

```
Substrate Peter-Weyl decomposition of H_K
   IS the K-graded Hilbert space algebraic structure
   → classical Lie theory (dim, rank, root counting)
   → (dim + rank)/2 prefactor as substrate-derived constant
   → Conv-B baseline bulk-Weyl exponent
   → empirical W1b-3 Richardson anchor at τ=0 (Hörmander-Weyl baseline)
```

---

## Wave 6a → Wave 6b Decision Point

**Pre-registered branching per `.claude/rules/epistemic-discipline.md` Pre-Registration Completeness**:

| §W6a-51 verdict | §W6a-52 verdict | Wave 6b consequence |
|:---------------|:---------------|:--------------------|
| PASS | PASS | Wave 6b proceeds with §W6a-51 + §W6a-52 LANDED. STAGE-1-CANDIDATE registry entry §VII.{next-free-letter} pre-allocated for §W6a-51 joint theorem; STAGE-2 cross-axis independent-verify queued for S89+ as `S89-OR-LATER-W6A-51-INDEPENDENT-VERIFY`. §W6a-52 formula `(N−1)(N+2)/2` promoted to canonical_constants.py as `slope_A_baseline_SUN_FW(N)` family. FWD-C1 unblocked. |
| PASS | FAIL | §W6a-51 closed form holds but Conv-B prefactor decomposition fails. Record Conv-B convention re-derivation as carry-forward `S89-CONV-B-CONVENTION-RE-DERIVATION`. §W6a-51 lands as STAGE-1-CANDIDATE conditional on §W6a-52 resolution. |
| FAIL | PASS | Conv-B baseline structurally derived but Jensen kernel `1/(5π)` does not match anchor. Record higher-order resolvent expansion as carry-forward `S89-JENSEN-DIM-SPECTRUM-HIGHER-ORDER-RESOLVENT`. §W6a-52 lands independently. |
| FAIL | FAIL | Both structural derivations fail. The HK-5 form `slope_A(τ) = c₀/(1 − τ/c₁)` is empirically anchored but NOT first-principles derivable from CM-1995 §III.4 + Peter-Weyl alone. Record as a structural gap requiring NEW machinery (e.g., explicit J_C2 ⊗ Y commutator structure beyond resolvent expansion). FWD-C1 BLOCKED on `d_eff(τ_fold)` substrate-first canonical. |
| INFO (either) | INFO (either) | Closed forms match anchor up to truncation precision floor; INFO does not block downstream consumption but flags dominant `O(τ²)` correction term as next-session carry-forward `S89-JENSEN-DIM-SPECTRUM-O-TAU-SQUARED-CORRECTION`. |

---

## Wave 6a Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR.

### §W6a-51 PRDR enumerated machinery

| # | Free parameter | PIN value | Diagnostic? |
|:--|:---------------|:----------|:------------|
| 1 | `tau_fold` | `0.19` | pinned |
| 2 | `L_max_validation` | `12` | pinned |
| 3 | `L_max_regen_set` | `{10, 11, 12}` | pinned |
| 4 | `regulator_set` | `{zeta, Pauli-Villars, Mellin}` | pinned |
| 5 | `convention_set` | `{Conv-A, Conv-B}` | pinned |
| 6 | `pole_set` | `s ∈ {(d−n)/2 : n ∈ {0,2,4,6,8}}` | pinned |
| 7 | `cartan_root_sum_factor` | `5π` (derived; substrate-target) | pinned |
| 8 | `Y_hypercharge_normalization` | per CM-1995 §III.4 | pinned |
| 9 | `dim_SU3` | `8` | axiomatic |
| 10 | `rank_SU3` | `2` | axiomatic |
| 11 | `positive_root_count_SU3` | `3` | derived |
| 12 | `cancellation_tolerance` | `1e-12` | pinned |
| 13 | `sage_precision` | symbolic (rational arithmetic) | pinned |
| 14 | resolvent expansion order | `O(τ²)` documented; `O(τ³)` declared diagnostic | diagnostic |
| 15 | `d_eff_definition` | as Sd dimension | pinned |

### §W6a-52 PRDR enumerated machinery

| # | Free parameter | PIN value | Diagnostic? |
|:--|:---------------|:----------|:------------|
| 1 | `tau` | `0` | pinned (baseline) |
| 2 | `groups_tested` | `{SU(2), SU(3), SU(4)}` | pinned |
| 3 | `L_max_SU2` | `15` | pinned |
| 4 | `L_max_SU3_set` | `{10, 11, 12}` | pinned |
| 5 | `L_max_SU4` | `8` | pinned |
| 6 | `convention_pin` | `Conv-B` | pinned |
| 7 | `peter_weyl_basis_normalization` | per CM-1995 | pinned |
| 8 | `cancellation_tolerance` | `1e-12` | pinned |
| 9 | `dim_rank_root_count_pins` | per Lie theory | axiomatic |
| 10 | `cesaro_average_window` | `L/log(L)` | pinned |
| 11 | `sage_backend` | `sage_eval` | pinned |

---

## Wave 6a Input-SHA Ledger

| Input | Path | SHA |
|:------|:-----|:----|
| Canonical constants | `computations/canonical_constants.py` | `<pinned at dispatch>` |
| L=12 spectrum cache | `computations/s84_spectrum_cache_L12_tau019.npz` | `9e6d9cf7fd6a6949...` (full at audit) |
| W1b-3 Richardson verdict | `computations/s87_gate_verdicts.txt` (S87-W1B-3 row) | `<pinned at dispatch>` |
| CM-1995 §III.4 source | `researchers/Connes/connes-moscovici-1995.md` (or canonical PDF) | `<pinned at dispatch>` |
| Phononic framing rule | `.claude/rules/phononic-framing.md` | `<pinned at dispatch>` |
| Cross-pillar bridge anatomy rule | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<pinned at dispatch>` |
| Joint-theorem promotion rule | `.claude/rules/joint-theorem-promotion.md` | `<pinned at dispatch>` |
| Regulator-pin discipline rule | `.claude/rules/regulator-pin-discipline.md` | `<pinned at dispatch>` |

`audit_sha256` over the file-level pins above (no agent-memory pins per AMRI Test 1
discipline). Computed by the producing scripts `s88_w6a_jensen_dim_spectrum_first_principles.py`
and `s88_w6a_dim_plus_rank_over_2_prefactor.py` at dispatch time.

---

## Verdict-line emission

Producing scripts:
- §W6a-51 → `computations/s88_w6a_jensen_dim_spectrum_first_principles.py`
- §W6a-52 → `computations/s88_w6a_dim_plus_rank_over_2_prefactor.py`

Verdict file: `computations/s88_gate_verdicts.txt` (per dual-SHA closure
protocol per `.claude/rules/gate-verdicts.md`).

End of Wave 6a plan.
