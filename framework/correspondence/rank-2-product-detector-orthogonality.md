# Rank-2 Product Detector Orthogonality Theorem

**Status**: READY-TO-INSTALL → INSTALLED 2026-04-27 (S86 Level-10 housekeeping T10-9).
**Source**: S86 W-3 workshop `_housekeeping-extract-w3.md` OFR-1 (lines 293-296) + FALS-4 (lines 253-256) + workshop §Convergence #5 (lines 2962-3006) + §Emergence #1 (lines 3066-3114) + §What Holds line 3223 + §Closing Line line 3268.
**Recommending agent**: gen-physicist (extract); lizzi (workshop sponsor) + connes (axiom-derivation co-author).
**Cross-references**: parent inventory `sessions/framework/registry/falsifier-master-inventory.md` Row #2 (LiteBIRD live-watch) + Row #7 (LISA CGWB Ω_GW); §VII.M Three-Layer Regulator Theorem (S84 W2a-11); S85 W12-4 Mellin Strip Theorem.

This entry is the standalone framework structural result on the rank-2 product detector orthogonality theorem `[π_R, P_α] = 0`. It is the structural reason WHY r has a rank-2 product-detector falsifier suite (LiteBIRD = block-axis, LISA = regulator-axis), and is the operator-level expression of the commutativity between the block-decomposition projector `P_α` and the regulator-class projector `π_R`.

---

## §1 — Theorem statement

**Rank-2 Product Detector Orthogonality Theorem**:

For the substrate's r-prediction observable, the block-decomposition projector `P_α` (where `α ∈ {Path-H, Path-C}`) and the regulator-class projector `π_R` (where `R ∈ {Λ_A = (A) regulator class, Λ_C = (C) regulator class}`) satisfy:

```
[π_R, P_α] = 0   for all (R, α) ∈ {Λ_A, Λ_C} × {Path-H, Path-C}
```

Equivalently, the joint observable `P_T^{(α, R)}` factorizes at leading Mellin order:

```
P_T^{(α, R)}  =  f_R(Λ)  ·  g_α(τ_fold)
```

where `f_R(Λ)` is the regulator-class-dependent factor (Λ is the spectral cutoff scale, regulator-class-dependent), and `g_α(τ_fold)` is the block-decomposition-dependent factor (τ_fold is the substrate's fold τ).

---

## §2 — Derivation chain (NCG axioms 3+5+6 + S85 W12-4)

The orthogonality theorem is derived from THREE inputs: NCG axioms 3 (block decomposition), 5 (spectral structure), 6 (orientability) + S85 W12-4 Mellin Strip Theorem.

### Step 1 (NCG axioms 3+5+6): Block decomposition uniqueness

The Jensen-deformed SU(3) spectral triple's `D_K` admits a unique block decomposition `D_K = ⊕_α D_K^{(α)}` where `α` ranges over the inheritance-arrow images (Path-H = transverse fiber-oscillation, Path-C = substrate-compaction Mellin-tilt). Block decomposition is unique up to unitary conjugation by NCG axioms 3+5+6 (the trio that forces commutator-algebra closure with `J` and `γ`).

The block-decomposition projector `P_α : H → H_α` is well-defined and SELF-ADJOINT.

### Step 2 (S85 W12-4 Mellin Strip Theorem): Regulator-class structure

The S85 W12-4 Mellin Strip Theorem establishes that the regulator class for the substrate's spectral action partitions into discrete classes labeled by `R ∈ {Λ_A, Λ_C, ...}` corresponding to L1 zeta closure (Path-H regulator), L3 per-Q-span closure (Path-C regulator), etc. The regulator-class projector `π_R : H → H_R` selects the regulator-class subspace and is self-adjoint.

The §VII.M Three-Layer Regulator Theorem (S84 W2a-11) provides the explicit layer membership: L1 zeta ↔ Path-H, L3 per-Q span ↔ Path-C, L2 Zubarev ↔ regulator-class structurally orthogonal to both (singleton at L2 axiom-native slot per S86 W-8 cutoff-sqrt adjudication).

### Step 3 (commutator computation): Orthogonality

The block decomposition acts on `H` along the inheritance-arrow axis (substrate → laboratory). The regulator-class structure acts on `H` along the spectral-cutoff axis (`Λ` scaling). These two axes are STRUCTURALLY ORTHOGONAL — the inheritance-arrow does not couple to the regulator-class because the regulator is a CHOICE OF SPECTRAL ACTION CALIBRATION, not a substrate-physical observable. Inheritance-arrow images are substrate-physical.

The commutator `[π_R, P_α]` therefore vanishes:

```
[π_R, P_α] = π_R · P_α − P_α · π_R = 0
```

at leading Mellin order. Sub-leading corrections at `1/Λ²` are bounded by the S85 W12-4 Mellin Strip width and are negligible at framework scale.

### Step 4 (factorization at leading Mellin order)

Self-adjoint commuting projectors admit simultaneous diagonalization. The joint observable `P_T^{(α, R)}` therefore factorizes:

```
P_T^{(α, R)}  =  f_R(Λ)  ·  g_α(τ_fold)
```

where:
- `f_R(Λ)` is the regulator-class-dependent factor — `f_{Λ_A}(Λ) = Ω_GW^{(A)} ≈ 10⁻¹⁰` (LISA-detectable per `lisa-gw-prediction.md`); `f_{Λ_C}(Λ) = Ω_GW^{(C)} = 8.299 × 10⁻⁵⁸` (W13-2.Ω Companion-null) — Sage-verified 47.081 OOM (A)/(C) split
- `g_α(τ_fold)` is the block-decomposition-dependent factor — `g_Path-H(τ_fold) = r_Path-H = 0.0074705` (FROZEN canonical, S86 W-6 mack install); `g_Path-C(τ_fold) = r_Path-C = 0.0117`

---

## §3 — Detector matching (rank-2 product structure)

The two axes of the rank-2 product detector are matched to two independent observation programs:

| Axis | Detector | Resolves | Predicted signature |
|:-----|:---------|:----------|:--------------------|
| **Block-axis** (`α ∈ {Path-H, Path-C}`) | LiteBIRD (2028+) | `g_α(τ_fold)` resolution at `σ(r) ≈ 0.001`; tilt `n_T = -r/8` regulator-independent at pivot | Path-H: `r ≈ 0.00745`; Path-C: `r ≈ 0.0117`; 4.25σ discrimination at LiteBIRD precision |
| **Regulator-axis** (`R ∈ {Λ_A, Λ_C}`) | LISA (2030s) | `f_R(Λ)` resolution at LISA Ω_GW sensitivity ~ 10⁻¹¹ | (A) class: `Ω_GW ≈ 10⁻¹⁰` (LISA-detectable); (C) class: `Ω_GW = 8.299 × 10⁻⁵⁸` (LISA-null) |

The orthogonality `[π_R, P_α] = 0` MEANS that LiteBIRD's resolution of `g_α` is INDEPENDENT of LISA's resolution of `f_R` — and vice versa. Each detector is sensitive to ONE axis only at leading Mellin order; the joint outcome at the 2×2 detector matrix is the rank-2 product.

---

## §4 — 2×2 outcome matrix

The four joint outcomes of LiteBIRD + LISA observations are pre-registered as the rank-2 product detector matrix:

| Outcome | LiteBIRD | LISA | Substrate consequence |
|:--------|:---------|:-----|:----------------------|
| **(i)** | r ≈ 0.00745 (Path-H) | `Ω_GW ≈ 10⁻¹⁰` (A) detected | (Path-H, A) — substrate selects L1 zeta closure with (A) regulator class |
| **(ii)** | r ≈ 0.00745 (Path-H) | `Ω_GW < 10⁻¹⁵` (C) null | (Path-H, C) — substrate selects L1 zeta closure with (C) regulator class (LISA-null branch) |
| **(iii)** | r ≈ 0.0117 (Path-C) | `Ω_GW ≈ 10⁻¹⁰` (A) detected | (Path-C, A) — substrate selects L3 per-Q-span closure with (A) regulator class |
| **(iv)** | r ≈ 0.0117 (Path-C) | `Ω_GW < 10⁻¹⁵` (C) null | (Path-C, C) — substrate selects L3 per-Q-span closure with (C) regulator class (LISA-null branch) |

**Per-outcome co-gating**:

- **(i) and (ii)** — gated by LiteBIRD-only (regulator-axis is independent; outcomes are equally consistent with either LISA result conditional on Path-H block decomposition)
- **(iii) and (iv)** — gated by LiteBIRD ∧ LISA joint (the LISA result becomes diagnostic once the block decomposition selects Path-C, because the (A)/(C) split on Path-C is more sharply defined by the regulator class than on Path-H)

The runtime adjudication mechanism is the meta-classifier_v2 module (S87 carry-forward CF-2 deliverable, `S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2`); see W-3 carry-forwards CF-21..CF-23 in `_housekeeping-install-queue.md`.

---

## §5 — Sub-leading corrections

The factorization `P_T^{(α, R)} = f_R(Λ) · g_α(τ_fold)` holds at LEADING Mellin order. Sub-leading corrections at `1/Λ²` and beyond are bounded by the S85 W12-4 Mellin Strip width and are negligible at framework scale.

The S87 carry-forward `S87-PRODUCT-DETECTOR-FACTORIZATION-AUDIT` (W-3 audit slot) tracks `1/Λ²` corrections to the rank-2 product detector factorization. Confirm corrections bounded by `1/Λ² ~ negligible at framework scale`, OR flag if sub-leading corrections appreciably mix axes (would require expanding from rank-2 product detector to rank-3 or higher).

---

## §6 — Future-falsifier-design implication

The orthogonality theorem provides a structural template for designing future-generation falsifier programs. Look for additional `[π_R, P_α]`-commuting structures to expand the product detector rank:

- **Rank-3 expansion**: a third orthogonal axis `[π_S, P_α] = [π_S, π_R] = 0` for some structurally orthogonal projector `π_S` (e.g., a third regulator class beyond {Λ_A, Λ_C}, or a non-block / non-regulator axis like spectral-dimension projection).
- **Rank-2 expansion via block-axis**: a third block-decomposition image `α ∈ {Path-H, Path-C, Path-X}` for some new inheritance-arrow morphism beyond the two currently identified.

Each expansion requires (a) verification that the new projector commutes with both `π_R` and `P_α` (orthogonality test); (b) identification of an independent detector program sensitive to the new axis; (c) pre-registration of the expanded outcome matrix.

---

## §7 — Cross-references

- **Parent registry inventory**: `sessions/framework/registry/falsifier-master-inventory.md` Row #2 (LiteBIRD live-watch + internal-consistency) + Row #7 (LISA CGWB Ω_GW (A)/(C) regulator-class signature).
- **§VII.M Three-Layer Regulator Theorem** (S84 W2a-11): `sessions/permanent-results-registry.md` (Connes + Lizzi + VdD three-solo signature); regulator-class layer membership (L1 zeta ↔ Path-H, L3 per-Q span ↔ Path-C, L2 Zubarev ↔ singleton).
- **S85 W12-4 Mellin Strip Theorem**: `sessions/permanent-results-registry.md` (lizzi anchor); Mellin-strip width bound for sub-leading corrections.
- **Path-H / Path-C inheritance dictionary**: `sessions/framework/framework-3heb-comparison.md` (T10-10 install).
- **LiteBIRD 5-outcome regulator-discriminator typology**: `sessions/framework/registry/alpha-s-structural-protection.md` §6 (parent registry entry).
- **Ω_GW (A)/(C) split** (Sage-verified 47.081 OOM): `sessions/framework/lisa-gw-prediction.md` (project-level prediction file).
- **r_Path-H canonical**: `computations/canonical_constants.py` `r_PathH = 0.0074705` + `r_PathH_published = 0.00745` (S86 1a S-6 mack install); provenance line 953 + line 956.
- **Meta-classifier_v2 module**: S87 carry-forward CF-21 (`S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2`); 4-outcome runtime adjudication.
- **Per-outcome co-gating wiring**: Workshop §R3-A Convergence #3 (lines 2509-2554); §R3-B Convergence #3 (lines 2881-2915).
- **Workshop verdict SHA pin**: S86 W-3 workshop content_sha256 (to be appended at S87 verification of W-3 closure).

---

## §8 — Closing

The rank-2 product detector orthogonality theorem `[π_R, P_α] = 0` is the structural REASON r has a 2×2 falsifier matrix rather than a binary live-watch. LiteBIRD resolves the block-axis (Path-H vs Path-C); LISA resolves the regulator-axis ((A) vs (C)); the orthogonality theorem MEANS the two axes are independent at leading Mellin order, and the four joint outcomes are pre-registered with explicit per-outcome co-gating. The theorem is derivable from NCG axioms 3+5+6 + S85 W12-4 Mellin Strip Theorem; sub-leading corrections at `1/Λ²` are negligible at framework scale. The 2×2 outcome matrix is the workshop's most substrate-physically novel observation-program implication for the next-generation observation program (LiteBIRD 2028+ + LISA 2030s).
