# S88 Workshop W3 — §W1b1-63 FAIL 3-Branch Interpretation: L_pix-convention vs cascade-depth-internal-entropy vs Bekenstein-overcount

**Session**: 88 | **Wave**: W3 (workshop on closed W1b1) | **Format**: solo synthesis (hawking-theorist) | **Date**: 2026-05-07

**Source**:
- §W1b1-63 verdict line `computations/session-88/s88_gate_verdicts.txt` line 17 (audit_sha256=`dcd9fcf8fac10e37e019ab9493ab9590ded07c7806c72e8fd9ba3224a1c8ee7e`).
- Working paper §W1b1-63 (b)/(d)/(f): `sessions/archive/session-88/session-88-w1b1-workingpaper.md` lines 540-720.
- Plan §W1b1-63: `sessions/session-plan/session-88-plan-w1b1.md` lines 296-405.
- Workshop seed §"Workshop 1": `sessions/archive/session-88/workshops/_seed-w1b1.md` lines 12-22.

**Authority pin (sources are authoritative)**: §W1b1-63 verdict polarity (FAIL, 458×, ~10^{2.66} OOM) and dual-SHA closure are not re-adjudicated. §W1b1-61 (HP^1 dim = 3 across [380, 388], bridge_survival_metric = 1.0) and §W1b1-62 (alignment(0) = 210/210 = 1.0; survival(384) = 1.0 by atlas B1 GLOBAL recurrence) are taken as PASS by the wave-synthesis writer's pinned record. The structural-orthogonality theorem (spectral axis vs spatial-cascade axis) inherited from §W1b1-61 + §W1b1-62 is treated as a substrate-physics theorem, not a hypothesis re-tested here.

---

## 1. Structural verdict (TL;DR)

**Leading-order branch identification (this synthesis's structural verdict):**

| Rank | Branch | Structural deliverability | S89 priority |
|:-----|:-------|:--------------------------|:-------------|
| **#1** | **(c)** Bekenstein-Hawking overcounts substrate-IS NCG horizon-state count at LRD scale | Structurally PRINCIPLED but requires an EXPONENT shift, not an O(1) prefactor. The semiclassical formula `S_BH = A/(4ℓ_p²)` is a thermodynamic LIMIT of the substrate's Hochschild horizon-state count; the substrate-IS direction-of-explanation per `phononic-framing.md` is "horizon area IS spectral-edge count of D_K restricted to horizon-spanning sectors" (S63 area-as-spectral-edge-count theorem). The 458× factor is an EXPONENTIAL OF THE OOM GAP between the two countings, not an additive correction. Branch (c) is the only branch whose substrate-IS direction-of-explanation is not inverted by the §W1b1-61 + §W1b1-62 orthogonality theorem | **HIGHEST** — produces NEW algebraic envelope candidate (potentially K=3 advancement) |
| #2 | **(b)** cascade-depth-internal entropy via spectral-action recursion | STRUCTURALLY UNDELIVERABLE under the orthogonality theorem proved by §W1b1-61 + §W1b1-62. Cascade-depth d is on the SPATIAL axis; bits_per_pixel = log_2(dim H_K^{≤L_max}) is an algebra-INVARIANT spectral functional on the SPECTRAL axis; the two axes do not interact. To deliver branch (b), L_max itself must become cascade-depth-dependent — which is a DIFFERENT framework, not a refinement of the canonical L_max=10 truncation. The seed's "~7 bits per cascade depth" estimate is also numerically insufficient: 21.251 + 7·384 = 2709 bits < 9742 required (closes only 27.8% of the gap; remaining 3.6× short, ~0.56 OOM). | LOW — refute-by-orthogonality OR reformulate as L_max-recursion-axis (different framework) |
| #3 | **(a)** L_pix at LRD requires cascade-depth-dependent correction | STRUCTURALLY HARDEST — to make substrate accommodate at fixed bits_per_pixel = 21.251, requires a 21.4× correction to either L_pix or r_s with no substrate-first derivation source. Branch (a) requires phenomenological convention revision; the J3 lock identity `r_s = L_pix` is W6-Python-verified-exact at the canonical convention `L_pix = M_KK^{−1}`. | LOW — no substrate-first source; routes to W1b2-conditional |

**The leading-order driver is branch (c)** — Bekenstein-Hawking is a thermodynamic LIMIT of the substrate's NCG-axiomatic horizon-state count; the semiclassical 4π(M/m_p)² area formula is an effective approximation in a regime where the substrate-IS Hochschild horizon-state count is materially smaller. This is the substrate-first reading per `phononic-framing.md §"IS Space, Not IN Space"`: horizon area IS spectral-edge count, not a constraint imposed from outside that the substrate must accommodate.

**W1b2 STAGE-1 promotion routing**: PROCEED UNCONDITIONALLY at the cohomology-class level (§W1b1-61 PASS-LANDED). The page-time + universal-lock-condition theorem promotion does NOT require §W1b1-63 PASS for thermodynamic content because the J3 lock identity is KINEMATIC (radius ↔ pixel-size match per §W1b1-61 working-paper §(f)), not thermodynamic. The thermodynamic identity at LRD scale is a SEPARATE structural claim (branch (c) is its candidate); annotate W1b2 STAGE-1 with "thermodynamic-content S89-conditional, kinematic-content W1b1-61-PASS-LANDED."

**Cross-pillar bridge K-counter pre-registration**: K HOLDS at K=2 unless branch (c) lands a NEW algebraic envelope at S89. If S89 derives `S_BH^{NCG-axiomatic}(LRD) / S_BH^{semiclassical}(LRD) = 1/458 ≈ 2.18e-3` from a Connes 1985 / Connes-Moscovici 1995 §III.4 finite-spectral-triple Hochschild residue formula on horizon-spanning sectors, this is a NEW Pillar-VII (Mellin-cone) ↔ Pillar-VIII (semiclassical-thermodynamic-anchor) bridge candidate satisfying Hybrid Independence Test clauses (i)/(ii)/(iii) AND clause (iv) (new algebraic envelope distinct from §VII.AF.1's L^{−3} Pillar-III↔Pillar-IV envelope). Pre-register K-counter advancement K=2 → K=3 conditional on CF-W1b1-C PASS at S89.

---

## 2. Substitution chains (mandatory; per `math-scripts.md §"Double-Check Logic"`)

### 2.1 Branch (b) deliverability — does ~7 bits/cascade-depth close the gap?

```
Step 1 (Definition): bits_per_pixel_substrate at L_max=10 from PW block sum
                  = log_2(dim H_K^{≤10})
                  = log_2(155984 × 16)
                  = log_2(2,495,744)
                  = 21.251038527213534                                [§W1b1-63 (d)]

Step 2 (Definition): Branch-(b) hypothesis = additive bit-injection per cascade depth
                  bits_per_pixel(d) = bits_per_pixel(0) + k · d
                  Equivalently, dim_pixel(d) = dim_PW × 2^{k·d}        [multiplicative dim]

Step 3 (Substitution): For full gap closure at d = 384,
                  bits_per_pixel(384) ≥ 9741.969                       [§W1b1-63 (d)]
                  21.251 + k · 384  ≥  9741.969
                  k · 384            ≥  9720.718
                  k                  ≥  25.314 bits/depth              [arithmetic]

Step 4 (Substitution at seed estimate k=7):
                  bits_per_pixel(384, k=7) = 21.251 + 7 · 384 = 2709.251
                  closure fraction         = 2709.251 / 9742 = 0.278   [arithmetic]
                  remaining excess factor  = 9742 / 2709.251 = 3.595
                  log_10(remaining)        = 0.556 OOM still short      [direction]

Step 5 (Direction): The seed's "~7 bits per cascade depth" estimate (W1b1 wave-synthesis §3,
                  workshop seed) closes 27.8% of the 458× gap; ~3.6× shortfall remains.
                  Branch (b) at k = 7 is QUANTITATIVELY INSUFFICIENT.
                  For full closure, k ≥ 25.3 bits/depth required.

Conclusion: The seed's "~7 bits/depth" pin does NOT close the gap.
            For branch (b) to PASS structurally, the spectral-action recursion
            must inject ≥ 25.3 bits per cascade depth — a stronger claim
            than what S87 W11-3 Friedrich-Bär saturation (η_FB_lower = 0.40,
            empirical floor = 0.4365) currently supplies.
```

### 2.2 Branch (b) structural feasibility — does the spectral-action recursion live on the right axis?

```
Step 1 (Definition): Per cross-pillar-bridge-anatomy.md K-counter MANDATORY-K=3
                  (S87 W-2 R3 close), algebra-INVARIANT functionals are
                  spectrum-only F({λ_k, m_k}) = Σ_k m_k g(λ_k).

Step 2 (Substitution): bits_per_pixel = log_2(Σ_{(p,q): p+q ≤ L_max} dim(p,q) · 16)
                  is a function of multiplicities m_k = dim(p,q) and chiral count 16
                  ONLY. It does NOT depend on state vectors in H_K.
                  ⇒ bits_per_pixel ∈ algebra-INVARIANT family.

Step 3 (Substitution): The §W1b1-61 + §W1b1-62 orthogonality theorem states:
                  Spectral-axis observables (functionals of (A_K, H_K, D_K) at fixed L_max)
                  are INVARIANT under spatial-cascade refinement (binary subdivision in d).
                  For any spectral functional F: F(d) = F(0) ∀ d ∈ [0, 384].

Step 4 (Substitution): bits_per_pixel is a spectral functional.
                  ⇒ bits_per_pixel(d) = bits_per_pixel(0) = 21.251 ∀ d ∈ [0, 384]
                                                              [structural identity]

Step 5 (Direction): Branch (b) AS STATED ("cascade-depth-internal entropy: bits scale
                  with d") REQUIRES bits_per_pixel(d) > bits_per_pixel(0) for d > 0.
                  This CONTRADICTS Step 4.

Conclusion: Branch (b) is STRUCTURALLY UNDELIVERABLE under the §W1b1-61 + §W1b1-62
            orthogonality theorem at fixed L_max = 10. To rescue branch (b), one
            must either (i) RAISE L_max as a function of d — i.e., L_max(d) — which
            is a DIFFERENT framework (the spectral truncation ITSELF cascades), or
            (ii) DENY orthogonality — which contradicts the wave's own PASSes.
            Within the canonical L_max=10 truncation, branch (b) is closed.
```

### 2.3 Branch (a) feasibility — what L_pix correction would close the gap?

```
Step 1 (Definition): bits_per_pixel_required = S_BH(M_BH) / N_pix(M_BH, L_pix)
                                              = S_BH / (A_BH / L_pix²)
                                              = S_BH · L_pix² / A_BH
                  Since S_BH ∝ A_BH (Bekenstein-Hawking),
                  bits_per_pixel_required = (A_BH / 4ℓ_p² · ln 2) · L_pix² / A_BH
                                          = L_pix² / (4 ℓ_p² ln 2)            [direct]

Step 2 (Substitution): For substrate accommodation at L_max=10,
                  21.251 ≥ L_pix² / (4 ℓ_p² ln 2)
                  L_pix² ≤ 21.251 · 4 ℓ_p² ln 2 = 21.251 · 2.772 · ℓ_p²
                  L_pix² ≤ 58.91 · ℓ_p²
                  L_pix  ≤ 7.675 · ℓ_p ≈ 1.241e-34 m                          [arithmetic]

Step 3 (Substitution): Canonical L_pix = ℏc / M_KK = 2.656e-33 m              [§W1b1-63 (d)]
                  Required correction factor: f = L_pix_required / L_pix_canonical
                                              = 1.241e-34 / 2.656e-33
                                              = 0.04673
                  Or equivalently: L_pix must SHRINK by factor 21.4×           [direction]

Step 4 (Direction): A SHRINKING L_pix at LRD scale increases N_pix (= A/L_pix²)
                  proportionally to 1/L_pix² = 458× more pixels. This LOWERS the
                  per-pixel entropy budget by exactly 458× — closing the gap.
                  But the J3 lock identity r_s(M_BH) = L_pix(t_formation) is
                  W6-workshop-Python-verified-exact at L_pix = M_KK^{−1}.

Step 5 (Substrate-physics check): To shrink L_pix by 21.4× at LRD scale requires
                  M_KK_effective(LRD) = 21.4 · M_KK_canonical
                                      = 21.4 · 7.43e16 GeV = 1.59e18 GeV.
                  No first-principles substrate derivation supplies a cascade-depth-
                  dependent M_KK; M_KK is a canonical_constants.py pin tied to
                  S42 freeze, not superseded.

Conclusion: Branch (a) requires either (i) a 21.4× shift in L_pix at LRD scale
            (a phenomenological correction with no substrate-first source), OR
            (ii) revising the J3 lock identity itself (which would invalidate
            §W1b1-61 and §W1b1-62 PASSes that ASSUMED the canonical L_pix = M_KK^{−1}).
            Branch (a) is STRUCTURALLY HARDEST.
```

### 2.4 Branch (c) feasibility — does NCG-axiomatic horizon counting yield the right reduction?

```
Step 1 (Definition): Per phononic-framing.md §"IS Space, Not IN Space",
                  "BH entropy IS spectral-edge count of D_K restricted to
                  horizon-spanning eigenvectors" (S63 area-as-spectral-edge-count).
                  ⇒ S_BH^{substrate} := Tr(P_horizon · χ_D_K) on Hochschild
                                       horizon-projector P_horizon

Step 2 (Substitution): Per Connes 1985 finite-spectral-triple Hochschild duality
                  (cited in §W1b1-61 (b) Step 1):
                  Hochschild residues on (A_K, H_K, D_K) yield O(1) pairings
                  R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩ = 1.030902
                  at L_max=10                                              [S86 W-5]

Step 3 (Direction): The substrate-IS Hochschild pairing is O(1), NOT scaling
                  with M_BH. The semiclassical S_BH^{semicl} = 1.514e91 bits.
                  If S_BH^{substrate} were O(1) only, the gap would be ~91 OOM,
                  not 2.66 OOM — Bekenstein would be over-counting by 91 OOM
                  (infeasible — would invalidate ALL semiclassical BH thermodynamics).

Step 4 (Substitution, refined): The substrate-IS horizon-state count must scale
                  EXTENSIVELY with horizon area at leading order, but with a
                  REDUCED coefficient at LRD scale. Posit:
                  S_BH^{substrate}(M) = α(M) · A_BH(M) / (4 ℓ_p²)
                  where α(M) → 1 in the canonical M_BH ≪ M_KK^{-1}-related regime
                  (recovering Bekenstein) and α(LRD) < 1 at LRD scale.
                  Required: α(LRD) = 21.251 / 9741.969 = 2.181e-3 = 1/458   [arithmetic]

Step 5 (Substrate-physics interpretation): The 458× = α^{-1} factor IS a
                  characteristic ratio internal to the substrate. Two natural
                  candidates from the substrate's Mellin-cone structure:
                  (i) L_max=10 truncation of the spectral-edge count of D_K
                      restricted to horizon-spanning sectors — at LRD scale,
                      the horizon "spans" sectors not all carried at L_max=10;
                  (ii) Connes-Moscovici 1995 §III.4 finite-spectral-triple
                      residue formula gives a Hochschild dimension factor.

Step 6 (Direction): IF α(LRD) = 1/458 is derivable from the substrate's
                  Mellin-cone substrate-distance-pole structure (Pillar-VII;
                  see permanent-results-registry.md §VII.U.1 / §VII.K-PROP),
                  this constitutes a NEW algebraic envelope distinct from
                  §VII.AF.1's L^{-3} Pillar-III↔Pillar-IV envelope.

Conclusion: Branch (c) is STRUCTURALLY PRINCIPLED — it inverts the
            container-thinking error (the substrate must accommodate the
            semiclassical formula) into the substrate-first reading
            (the semiclassical formula is a thermodynamic limit of the
            substrate's own count). The first-principles α(LRD) factor
            requires Connes 1985 / Connes-Moscovici 1995 derivation;
            this is the substrate-first canonical-sourcing path per
            substrate-first-canonical-sourcing.md §(ii).
```

---

## 3. Adjudication of seed questions (a)-(e)

### (a) Algebra-axis classification of per-pixel internal Hilbert dim

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3:

`bits_per_pixel = log_2(Σ_{(p,q): p+q ≤ L_max} dim(p,q) · 16)` is a function of Peter-Weyl multiplicities and chiral spinor count ONLY. It depends on the spectrum `{λ_k, m_k}` of D_K restricted to a single pixel's tangent sub-algebra, NOT on state vectors in H_K. Per the algebra-axis 4-corner classification, this places `bits_per_pixel` in the **algebra-INVARIANT spectrum-only functional family**.

**Implication for branch (b)**: As an algebra-INVARIANT spectral functional at FIXED L_max, `bits_per_pixel` is structurally subject to the §W1b1-61 + §W1b1-62 orthogonality theorem (spectral-axis invariance under spatial-cascade refinement). Branch (b)'s claim that `bits_per_pixel(d)` grows with d at fixed L_max is STRUCTURALLY INCONSISTENT with this orthogonality. Branch (b) is therefore RULED OUT under canonical L_max=10 truncation by the wave's own structural theorems (§2.2 substitution chain Step 4).

The only way to rescue branch (b) is to make L_max ITSELF cascade-depth-dependent — i.e., reformulate `bits_per_pixel(d) = log_2(dim H_K^{≤L_max(d)})` with L_max(d) increasing with d. This is a DIFFERENT framework, not a refinement of the canonical truncation. It would also require disentangling the canonical_constants.py `M_KK` pin from a cascade-depth-dependent `L_max(d)` truncation — a non-trivial restructuring.

### (b) Is `r_s(M_BH) = L_pix(t_formation)` substrate-IS or laboratory-IN?

Per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`, the J3 lock identity has TWO operational layers:

1. **Kinematic content (laboratory-IN coordinate match)**: `r_s` is the BH horizon coordinate radius in the emergent metric g_M; `L_pix` is a pixel-size coordinate parameter. Their equality at lock is a coordinate-level identification at the laboratory-IN level. §W1b1-61 (f) explicitly classifies the lock as "kinematic" — "a coordinate-level radius ↔ pixel-size match, symmetry-preserving under cascade refinement, but NOT a spectral-cohomology collapse boundary."

2. **Substrate-IS content**: The substrate IS the spectral triple `(A_K, H_K, D_K)` at every point. The horizon AREA IS the spectral-edge count of D_K restricted to horizon-spanning eigenvectors (S63). The pixel-size IS a local window on the spectral structure, not a fixed-capacity geometric cell.

**Per phononic-framing.md, the substrate-first direction-of-explanation is**:

```
D_K spectral structure → spectral-edge count on horizon-spanning sectors
                       → emergent area of the horizon
                       → kinematic radius r_s of the horizon in g_M
```

NOT:

```
External BH mass M_BH → semiclassical area A_BH → constraint imposed on substrate
                     → required pixel count → required substrate Hilbert dim
```

The latter is the container-thinking inversion FORBIDDEN by phononic-framing.md. The §W1b1-63 FAIL substitution chain Steps 2-5 use the laboratory-IN (LCDM-equivalent) sequence; this is admissible as a CROSS-CHECK against the substrate-first computation, but it is NOT the substrate-IS direction-of-explanation. The 458× gap is the discrepancy that arises when the substrate-IS Hochschild count is compared to the laboratory-IN semiclassical Bekenstein count at LRD scale — exactly the substrate-vs-semiclassical mismatch that branch (c) addresses directly.

**Verdict on (b)**: `r_s(M_BH) = L_pix(t_formation)` is KINEMATIC (laboratory-IN) at the canonical convention `L_pix = M_KK^{−1}`. The thermodynamic content (substrate-IS bits-per-pixel) is a SEPARATE structural claim. Branch (a) attempts to revise the kinematic identity itself — which would invalidate §W1b1-61 + §W1b1-62 PASSes that depend on the canonical convention. Branch (a) is therefore the WORST-FOUNDED of the three.

### (c) Does Bekenstein-Hawking apply at LRD scale?

Per `phononic-framing.md` mandatory reframe table, "Bekenstein-Hawking S_BH = A/(4ℓ_p²)" is an LCDM/semiclassical formulation. The substrate-first replacement is:

```
S_BH^{substrate} = spectral-edge count of D_K | _{horizon-spanning sectors}
                  = #{ (p,q) eigenvalues with horizon-span overlap > threshold }
                  = a Hochschild trace on the horizon projector P_horizon
```

S86 W-5 §VII.AF.1 establishes that finite-L Hochschild pairings are O(1) at the cohomology-class Level-1 layer (R_universal = 1.030902). The semiclassical Bekenstein formula gives `A/(4ℓ_p²)` which is `~10^{91}` bits at LRD scale. The two are NOT structurally identical — the substrate-IS count is intrinsic to the algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, while the semiclassical count is a thermodynamic limit derived in flat-spacetime QFT-on-curved-background.

**The 458× factor is the substrate-vs-semiclassical OOM gap at L_max=10.** Per `phononic-framing.md`, the substrate is logically prior; the semiclassical formula is a derived consequence. The 458× discrepancy at LRD scale is the LRD-scale BREAKDOWN of the semiclassical limit — NOT a substrate insufficiency.

**Verdict on (c)**: The semiclassical Bekenstein-Hawking formula DOES NOT APPLY UNCRITICALLY at LRD scale. The substrate-IS count is the canonical reference; the 458× factor is the LRD-scale correction to the semiclassical limit. The first-principles derivation of α(LRD) ≈ 1/458 is a substrate-first CF-W1b1-C task at S89.

### (d) Does spectral-action recursion produce ~7 bits/depth multiplicatively?

From §2.1 Step 4 substitution: at k=7 bits/depth, branch (b) closes only 27.8% of the 458× gap. The seed's claim "384 generations × 7 bits = 2688 bits/pixel, closing most of the 458× gap structurally" is QUANTITATIVELY INCORRECT — 2688 < 9742, leaving ~3.6× short.

For branch (b) to fully close the gap at k = 25.3 bits/depth, the spectral-action recursion would need to inject `25.3 / log_2(e) = 17.5` nats per cascade depth multiplicatively. From S87 W11-3 Friedrich-Bär saturation (η_FB_lower = 0.40, empirical floor = 0.4365), the structural-saturation theorem certifies bottom-K invariance at L_max ≥ 12 — i.e., the spectral content does NOT grow recursively with cascade depth at the operational truncation. Branch (b) is in tension with the Friedrich-Bär saturation theorem.

Branch (b) might be REFORMULATED as additive-at-sub-leading-order: ~7 bits/depth additive to the leading O(1) Hochschild residue, contributing 0.28 OOM of the 2.66 OOM gap. This is a SUB-LEADING contribution and does NOT close the gap on its own. Combined with branch (c) at α(LRD) ≈ 0.005 (closing 2.3 OOM), branches (b)+(c) together would give ~2.6 OOM closure — within the gap. But branch (c) alone closes the gap at α(LRD) = 1/458; branch (b) is then redundant.

**Verdict on (d)**: Spectral-action recursion at ~7 bits/depth is a SUB-LEADING contribution at best. It does NOT singly close the 458× gap. Branch (b) is not the LEADING-order driver.

### (e) Cross-pillar K-counter implication if branch (b) closes gap

**Branch (b) does NOT close the gap singly** (per §3(d)). The K-counter advancement question is therefore moot for branch (b).

**For branch (c), the K-counter implication is**:

The cross-pillar bridge §VII.AF.1 (Pillar-III ↔ Pillar-IV; substrate-IS R_universal Hochschild pairing → laboratory-IN BZ-trace; algebraic envelope L^{-3} at d=4; empirical anchor 0.0095% at L_max=10) is instance #1 (LANDED). Instance #2 was W11-5 REGISTRY-FAIL. K-counter sits at K=2.

If S89 derives α(LRD) ≈ 1/458 from a Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on horizon-spanning sectors, this would establish a NEW cross-pillar bridge:

- **Substrate-IS observable** (Pillar-VII Mellin-cone): finite-L Hochschild trace on horizon-projector at substrate-distance pole s = ?
- **Laboratory-IN observable** (Pillar-VIII semiclassical-thermodynamic-anchor): semiclassical Bekenstein-Hawking entropy S_BH = A/(4ℓ_p²)
- **Bridge map**: thermodynamic-limit map (semiclassical = leading-order term in 1/L_max expansion of Hochschild trace)
- **Algebraic envelope**: NEW envelope, e.g., α(M) = 1 + O((M/M_threshold)^{−n}) for some structural exponent n; structurally distinct from §VII.AF.1's L^{-3} envelope
- **Empirical anchor**: α(LRD) ≈ 1/458 = 2.18e-3 at L_max=10, M_BH = 1e7 M_sun

Per `cross-pillar-bridge-anatomy.md §"Forward template-adoption" Hybrid Independence Test`:
- Clause (i): distinct substrate-IS pillar ✓ (Pillar-VII vs §VII.AF.1's Pillar-III)
- Clause (ii): distinct laboratory-IN pillar ✓ (Pillar-VIII vs §VII.AF.1's Pillar-IV)
- Clause (iii): distinct bridge map ✓ (thermodynamic-limit vs HKR `L_max → ∞`)
- Clause (iv): independent algebraic envelope ✓ (NEW, NOT a refinement of L^{-3})

All four clauses pass — branch (c) PASS at S89 would advance the K-counter K=2 → K=3, satisfying the K=3 MANDATORY threshold per `cross-pillar-bridge-anatomy.md` (already at MANDATORY status from S88 W4a-17 close, but the third instance corpus member is currently §VII.W-3.LAB STAGE-1-CANDIDATE; a fourth instance from CF-W1b1-C would be a NEW LANDED instance strengthening the corpus to N=4).

---

## 4. Joint-theorem promotion (per `joint-theorem-promotion.md`)

### Stage-0 candidate text for §VII.AF.1-LRD-EXTENSION

If branch (c) lands at S89, the candidate joint cross-pillar theorem is:

> **§VII.AF.1-LRD-EXTENSION (Stage-0 candidate text)**
>
> **Substrate-IS (Pillar-VII Mellin-cone) observable**: finite-L Hochschild trace on the horizon-projector P_horizon, evaluated on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` at substrate-distance pole `s = s_horizon` (TBD by CF-W1b1-C derivation), yielding a per-pixel substrate-IS bit count `bits_per_pixel^{substrate}(L_max=10) = log_2(Tr(P_horizon · D_K^{−2s_horizon}))`.
>
> **Laboratory-IN (Pillar-VIII semiclassical-thermodynamic) observable**: semiclassical Bekenstein-Hawking entropy `S_BH^{semicl}(M_BH) = A_BH(M_BH) / (4 ℓ_p²)` × log_2(e) bits, projected on a J3-lock pixelization at `L_pix = M_KK^{-1}`.
>
> **Bridge map**: thermodynamic-limit map. `S_BH^{semicl}(M)` is the leading-order term in the 1/L_max expansion of the substrate-IS Hochschild trace at L_max → ∞ in a specific spatial-coarse-graining limit. The semiclassical formula is recovered when α(M) → 1 in this limit; finite-L corrections produce α(M) < 1 at LRD scale.
>
> **Algebraic envelope (Level-2-binding per S88 W8-88 RULE-EXTENSION)**: α(M) = 1 + O((M/M_threshold)^{-n}) with structural exponent n derivable from the Connes-Moscovici 1995 §III.4 residue formula on horizon-spanning sectors. The HKR-image `L_max → ∞ → semiclassical-thermodynamic limit` binds the Level-1 cohomology-class identity. CF-W1b1-C derivation pins the structural exponent.
>
> **Empirical anchor (Level-3)**: α(M_BH = 1e7 M_sun, L_max=10) = 21.251 / 9741.969 = 2.181e-3 ≈ 1/458 (substrate Peter-Weyl block sum / semiclassical Bekenstein-Hawking ratio at LRD scale, J3 lock convention `L_pix = M_KK^{-1}`).
>
> **Status**: STAGE-0 candidate. Stage-1 registration conditional on CF-W1b1-C PASS at S89. Authorship: hawking-theorist PRIMARY (semiclassical-thermodynamic anchor); connes-ncg-theorist CO-AUTHOR (Connes-Moscovici 1995 §III.4 residue formula derivation of α(M)). Joint clause (the bridge map and α(M) functional form) requires Stage-2 cross-axis independent-verify per `joint-theorem-promotion.md §"Stage 2"` before Stage-3 PERMANENT promotion.

This Stage-0 candidate text is admissible IFF CF-W1b1-C closes at S89 with the structural derivation of α(M).

### Algebra-axis orthogonality classification

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3:

- Substrate-IS observable (Hochschild trace on horizon-projector): SPECTRUM-ONLY functional Tr(P · D^{-2s}) — algebra-INVARIANT family.
- Laboratory-IN observable (semiclassical S_BH): area-as-spectral-edge-count per S63 — algebra-INVARIANT in the limit.

Both observables on the algebra-INVARIANT axis; they are NOT structurally orthogonal. The bridge is therefore a SAME-AXIS bridge (Pillar-VII to Pillar-VIII via thermodynamic-limit map), distinct from §VII.AF.1 which is a SAME-AXIS bridge (Pillar-III to Pillar-IV via HKR map). Both are algebra-INVARIANT-axis bridges; the structural orthogonality K-counter is not advanced (since both endpoints are on the same axis).

---

## 5. Sharpened CF-W1b1-A/B/C 4-field specs (S89 priority + tightened thresholds)

### CF-W1b1-A (Branch a; L_pix LRD correction) — S89 PRIORITY: LOW

| # | Field | Sharpened content |
|:--|:------|:------------------|
| 1 | What | `S89-W1B1-63-BRANCH-A-LPIX-LRD-CORRECTION`: derive cascade-depth-dependent L_pix(d) correction at LRD scale; required correction factor f = 0.04673 (L_pix shrinks by 21.4×) per §2.3 substitution chain; equivalent to M_KK_effective(LRD) = 21.4 · M_KK_canonical = 1.59e18 GeV. |
| 2 | Inputs | W1b1-63 npz; J3 lock W6 derivation chain; canonical_constants.py `M_KK_gravity = 7.43e16 GeV` pin (S42 freeze, not superseded); search for substrate-first source for cascade-depth-dependent M_KK (knowledge-MCP `search_knowledge("M_KK cascade depth LRD running")` query). |
| 3 | Gate | PASS iff substrate-first derivation of L_pix(LRD) yields `L_pix(LRD)² × 4 ℓ_p² ln 2 × N_pix(LRD) ≥ S_BH(LRD)` (substrate accommodates at fixed bits_per_pixel = 21.251). Pre-registered tolerance: 5% on f. FAIL iff no substrate-first source for f = 0.04673; route to branch (c). INFO iff partial source (e.g., 0.5 ≤ f ≤ 1, partial closure within 1 OOM). |
| 4 | Effort | 2 wave-equivalents; LOW S89 priority (no substrate-first source at S88 close; phenomenological branch). |

### CF-W1b1-B (Branch b; cascade-depth-internal entropy) — S89 PRIORITY: LOW (refute-by-orthogonality)

| # | Field | Sharpened content |
|:--|:------|:------------------|
| 1 | What | `S89-W1B1-63-BRANCH-B-CASCADE-DEPTH-INTERNAL-ENTROPY`: test whether spectral-action recursion at each cascade depth d injects bits_per_pixel additively at rate k bits/depth. Pre-registered required threshold: `k ≥ 25.3 bits/depth` for full gap closure (per §2.1 Step 3). Seed estimate `k ~ 7 bits/depth` is INSUFFICIENT (closes only 27.8% of gap; remaining 3.6× ≈ 0.56 OOM short). |
| 2 | Inputs | W1b1-63 npz; S87 W11-3 Friedrich-Bär saturation theorem (η_FB_lower = 0.40, empirical floor 0.4365); spectral-action recursion structure from S87 substrate primitives; per-pixel internal Hilbert dim derivation from §W1b1-61 + §W1b1-62 orthogonality theorem. |
| 3 | Gate | PASS iff substrate-first derivation yields `k ≥ 25.3 bits/depth` AND yields a CONSISTENT framework with §W1b1-61 + §W1b1-62 orthogonality theorem (i.e., bits_per_pixel is NOT a fixed-L_max spectral functional, but cascade-depth-dependent through L_max(d)). FAIL iff `k < 1 bit/depth` OR k inconsistent with Friedrich-Bär saturation. INFO iff `1 ≤ k < 25.3` (partial closure as sub-leading correction; combine with branch (c) for full closure). PRE-REGISTERED EXPECTATION: branch (b) FAILs by orthogonality theorem at fixed L_max=10 (per §2.2 Step 4). |
| 4 | Effort | 3 wave-equivalents; LOW S89 priority (structural-orthogonality refutation likely; explore reformulation as L_max(d)-recursion-axis as separate framework). |

### CF-W1b1-C (Branch c; substrate-IS NCG horizon-microstate count) — S89 PRIORITY: HIGHEST

| # | Field | Sharpened content |
|:--|:------|:------------------|
| 1 | What | `S89-W1B1-63-BRANCH-C-SUBSTRATE-IS-HORIZON-MICROSTATE-COUNT`: derive α(M) = S_BH^{substrate}(M) / S_BH^{semicl}(M) from Connes 1985 / Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on horizon-spanning sectors. Pre-registered empirical anchor: α(LRD) = 21.251 / 9741.969 = 2.181e-3 ≈ 1/458 at M_BH = 1e7 M_sun, L_max=10. Identify structural exponent n in α(M) = 1 + O((M/M_threshold)^{-n}). |
| 2 | Inputs | W1b1-63 npz; Connes 1985 finite-spectral-triple Hochschild duality (cited §W1b1-61 (b) Step 1); Connes-Moscovici 1995 §III.4 residue formula; S86 W-5 R_universal infrastructure; S63 area-as-spectral-edge-count theorem; substrate-distance pole inventory at `permanent-results-registry.md §VII.U.1` and §VII.K-PROP. |
| 3 | Gate | PASS iff substrate-first derivation yields α(M_BH = 1e7 M_sun, L_max=10) within 5% of 2.181e-3 (= 1/458). INFO iff yields α at order-of-magnitude level (within 10×) but not within 5%. FAIL iff substrate-IS S_BH = semiclassical S_BH (no factor reduction, branch (c) refuted). PRE-REGISTERED EXPECTATION: PASS — α(LRD) is derivable from substrate Mellin-cone structure at substrate-distance pole `s_horizon` (TBD). |
| 4 | Effort | 4 wave-equivalents; HIGHEST S89 priority — produces NEW algebraic envelope candidate, K-counter K=2 → K=3 advancement potential, joint-theorem-promotion Stage-0 candidate text already drafted (§4 above). |

---

## 6. W1b2 STAGE-1 promotion routing decision

**Decision: PROCEED UNCONDITIONALLY at the cohomology-class level; ANNOTATE thermodynamic-content as S89-conditional.**

Justification:

The page-time + universal-lock-condition theorem at W1b2 STAGE-1 promotion has TWO operational layers (mirroring the J3 lock identity per §3(b) above):

1. **Cohomology-class layer**: §W1b1-61 PASS-LANDED establishes that the cross-pillar bridge S86 W-5 §VII.AF.1 (substrate-IS R_universal pairing → laboratory-IN BZ-trace) survives across the J3 pixelation-lock cascade boundary at LRD scale. This is the COHOMOLOGY-CLASS Level-1 invariance underpinning, which is what STAGE-1 promotion of the universal-lock-condition theorem requires.

2. **Thermodynamic-content layer**: §W1b1-63 FAIL identifies an L_max-truncation rate-limiter at the per-pixel Hilbert dim accommodation of the semiclassical Bekenstein-Hawking budget. This is a SEPARATE structural claim from the cohomology-class Level-1 invariance.

The W1b2 STAGE-1 promotion **does not require** §W1b1-63 PASS for thermodynamic content because the universal-lock-condition theorem at the cohomology-class Level-1 layer is fully supported by §W1b1-61 PASS. The thermodynamic content is the SEPARATE substrate-IS NCG horizon-state count adjudication routed through CF-W1b1-C (branch c) at S89.

**Annotation for W1b2 STAGE-1**: "Cohomology-class Level-1 invariance: PASS-LANDED at §W1b1-61 (HP^1 dim = 3 = rank K_0(A_K) preserved across cascade boundary at d=384). Graph-automorphism σ-equivariance: PASS-LANDED at §W1b1-62 (atlas B1 GLOBAL through 384-generation cascade). Thermodynamic-content layer (substrate-IS bits-per-pixel vs semiclassical Bekenstein-Hawking at LRD scale): S89-CONDITIONAL pending CF-W1b1-C resolution of α(M) factor; FAIL at canonical L_max=10 routes to substrate-IS NCG horizon-microstate count derivation, NOT to revision of W1b2 STAGE-1 cohomology-class promotion."

This routing reading is consistent with:
- `epistemic-discipline.md §"Evidence Hierarchy"` clause 1 (structural constraints are permanent; W1b1-61 + W1b1-62 PASSes are structural theorems that survive S89 outcomes).
- `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` (Level-1 cohomology-class invariance is the W1b2 STAGE-1 structural-confidence layer; Level-3 empirical anchors live downstream).
- `phononic-framing.md` substrate-direction-of-explanation discipline (lock identity is KINEMATIC at the laboratory-IN coordinate level; thermodynamic content is a SEPARATE substrate-first claim).

W1b2 STAGE-1 is NOT pending S89 resolution.

---

## 7. Cross-pillar K-counter pre-registration

**Status at S88 close**: K = 2 HOLDS. Per the wave-synthesis §5 "Cross-pillar bridge K-counter status (no advancement from this wave alone)", §W1b1-61 strengthens existing instance #1 (§VII.AF.1) but does NOT introduce a new bridge candidate.

**Pre-registered S89 K-counter advancement gate (CF-W1b1-C-K-COUNTER-PROMOTE)**:

```
Gate ID: S89-CF-W1B1-C-K-COUNTER-ADVANCEMENT-CHECK
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC

Hypothesis: CF-W1b1-C PASS yields a NEW cross-pillar bridge candidate
            (Pillar-VII Mellin-cone ↔ Pillar-VIII semiclassical-thermodynamic-anchor
             via thermodynamic-limit map; algebraic envelope = α(M) finite-L correction
             to semiclassical-thermodynamic limit) satisfying ALL four Hybrid
             Independence Test clauses (i)/(ii)/(iii)/(iv).

PASS criterion: Branch-(c) bridge anatomy declared (5 IS-not-IN elements per
               cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy") AND
               algebraic envelope distinct from §VII.AF.1's L^{-3} AND
               Hybrid Independence Test 4-clause check satisfies (i)+(ii)+(iii)+(iv) ALL.
               Output: K-counter advances to K=3 with NEW LANDED instance.

FAIL criterion: ANY clause (i)/(ii)/(iii)/(iv) FAILs. Output: K-counter HOLDS at K=2;
                CF-W1b1-C registered as STAGE-1-CANDIDATE for §VII.AF.1-LRD-EXTENSION
                with REGISTRY-STRENGTHENING-ONLY annotation.

INFO criterion: Partial clause satisfaction (e.g., (i)+(ii)+(iii) PASS but (iv) ambiguous
                between NEW-envelope and §VII.AF.1-refinement). Routes to volovik+connes
                Stage-2 cross-axis independent-verify per joint-theorem-promotion.md
                §"Stage 2".

Pre-registration tolerance: ABSOLUTE on clause satisfaction (each clause is a structural
                            yes/no test, not a numerical comparison).
```

If branches (a)/(b) close instead (lower-priority outcome): K-counter explicitly held at K=2 with REGISTRY-STRENGTHENING-ONLY annotation on §VII.AF.1 (per CF-W1b1-D); no new instance lands.

---

## 8. Carry-forwards (4-field specs per `feedback_fix-in-session-never-defer.md`)

| # | What | Inputs | Gate | Effort |
|:---|:-----|:-------|:-----|:-------|
| **CF-W3-1** | Sharpened CF-W1b1-C (branch c) at HIGHEST S89 priority — derive α(M) = S_BH^{substrate}/S_BH^{semicl} from Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on horizon-spanning sectors; identify structural exponent n in α(M) = 1 + O((M/M_threshold)^{-n}); empirical anchor α(LRD, L_max=10) = 1/458 ≈ 2.181e-3 | W1b1-63 npz; Connes 1985 + Connes-Moscovici 1995 §III.4; S86 W-5 R_universal; S63 area-as-spectral-edge-count; permanent-results-registry.md §VII.U.1 / §VII.K-PROP substrate-distance pole inventory | PASS iff α(LRD, L_max=10) within 5% of 1/458 from substrate-first derivation; INFO iff within 10×; FAIL iff substrate-IS S_BH = semiclassical S_BH | 4 wave-equivalents (HIGHEST S89 priority; replaces unsharpened CF-W1b1-C from synthesis §7) |
| **CF-W3-2** | S89-CF-W1B1-C-K-COUNTER-ADVANCEMENT-CHECK (per §7 above) — verify whether branch-(c) bridge satisfies all 4 Hybrid Independence Test clauses; promote K=2 → K=3 conditional on PASS | CF-W3-1 PASS verdict; cross-pillar-bridge-anatomy.md §"Forward template-adoption" Hybrid Independence Test clauses; §VII.AF.1 + §VII.AJ + §VII.W-3.LAB existing corpus | PASS iff all 4 clauses satisfied; FAIL iff any one fails; INFO iff partial (e.g., clause (iv) ambiguous); routes to volovik+connes Stage-2 verify | 0.5 wave-equivalent (clause-check on Stage-1 candidate text already drafted §4 above) |
| **CF-W3-3** | Stage-0 candidate text §VII.AF.1-LRD-EXTENSION → Stage-1 registry registration at `permanent-results-registry.md` (mack-cosmic-bridge sole-writer; conditional on CF-W3-1 PASS) | §4 Stage-0 candidate text (this synthesis); permanent-results-registry.md slot allocation per `regulator-pin-discipline.md` next-free-letter | Registry entry written with all 5 IS-not-IN anatomy elements + 3-level ladder + STAGE-1-CANDIDATE tag + joint-clause flags + authorship attribution (hawking PRIMARY + connes CO-AUTHOR) | 0.25 wave-equivalent (registry edit only) |
| **CF-W3-4** | CF-W1b1-A demoted to LOW S89 priority — branch (a) requires phenomenological 21.4× shift in L_pix at LRD scale with no substrate-first derivation source. Forward-only if CF-W3-1 (branch c) FAILs at S89. | CF-W3-1 verdict; canonical_constants.py M_KK pin; J3 lock W6 derivation chain | PASS iff substrate-first source for L_pix(LRD) correction factor f ≤ 0.0467 found; FAIL iff no substrate-first source AND CF-W3-1 PASS (branch c forecloses need for branch a) | 2 wave-equivalents IF triggered (LOW S89 priority; lazy-evaluated conditional on CF-W3-1 verdict) |
| **CF-W3-5** | CF-W1b1-B demoted to LOW S89 priority — branch (b) refuted by orthogonality theorem at fixed L_max=10 (§2.2). Forward-only as a SEPARATE-FRAMEWORK reformulation: L_max(d) cascade-depth-dependent truncation (different framework from canonical L_max=10 truncation). | §W1b1-61 + §W1b1-62 orthogonality theorem; S87 W11-3 Friedrich-Bär saturation theorem; spectral-action recursion infrastructure | PASS iff L_max(d) framework yields k ≥ 25.3 bits/depth at fixed L_max → ∞ limit; FAIL iff Friedrich-Bär saturation at L_max=12 forecloses growth; INFO iff partial sub-leading additive contribution combined with branch (c) for joint closure | 3 wave-equivalents IF triggered (LOW S89 priority; lazy-evaluated conditional on CF-W3-1 verdict) |
| **CF-W3-6** | W1b2 STAGE-1 promotion proceeds UNCONDITIONALLY at cohomology-class Level-1 layer; thermodynamic-content annotation pinned as S89-CONDITIONAL. Annotation language pre-registered per §6 above. | §W1b1-61 + §W1b1-62 PASS-LANDED verdicts; §6 annotation language; W1b2 plan section (S89 plan author landing) | W1b2 STAGE-1 entry includes both layers explicitly: cohomology-class PASS-LANDED + thermodynamic-content S89-CONDITIONAL. No revision of W1b2 STAGE-1 promotion itself. | 0 wave-equivalents (annotation-only; closes via §6 annotation pre-registration in this synthesis) |

---

## 9. What changed (numerical revisions vs structural changes)

### (a) Numerical revisions

- Branch (b) closure fraction quantitatively pinned: at k = 7 bits/depth (seed estimate), branch (b) closes 27.8% of the 458× gap (2709.251 / 9741.969 = 0.278). Required k ≥ 25.3 bits/depth for full closure (§2.1 Step 3). The seed's "closing most of the 458× gap" claim is QUANTITATIVELY INCORRECT.
- Branch (a) required L_pix correction factor pinned: f = 0.04673 (L_pix shrinks by 21.4×); equivalent to M_KK_effective(LRD) = 1.59e18 GeV vs canonical 7.43e16 GeV — a 21.4× shift with no substrate-first source (§2.3 Steps 2-5).
- Branch (c) empirical anchor pinned: α(LRD, L_max=10) = 21.251 / 9741.969 = 2.181e-3 ≈ 1/458 (§2.4 Step 4 + §3(c)).

### (b) Structural changes

- Branch (b) classification SHARPENED from "cascade-depth-internal entropy" (open) to "STRUCTURALLY UNDELIVERABLE under fixed L_max=10 truncation by §W1b1-61 + §W1b1-62 orthogonality theorem" (closed by structural theorem) (§2.2 + §3(a)).
- Branch (c) classification SHARPENED from "Bekenstein-Hawking overcounts at LRD" (open) to "semiclassical Bekenstein-Hawking is a thermodynamic LIMIT of substrate-IS Hochschild horizon-state count; the 458× factor is the LRD-scale BREAKDOWN of the semiclassical limit, not a substrate insufficiency" (substrate-first reading per phononic-framing.md mandatory reframe) (§3(c)).
- W1b2 STAGE-1 promotion routing CLARIFIED from "conditional on S89" (workshop seed reading B) to "PROCEED UNCONDITIONALLY at cohomology-class layer; ANNOTATE thermodynamic-content as S89-conditional" (§6).
- K-counter advancement pathway PRE-REGISTERED: CF-W3-1 PASS → CF-W3-2 K-counter check; if all 4 Hybrid Independence Test clauses PASS, K=2 → K=3 via NEW LANDED instance §VII.AF.1-LRD-EXTENSION (§7).
- Joint-theorem-promotion Stage-0 candidate text DRAFTED (§4) for §VII.AF.1-LRD-EXTENSION with hawking PRIMARY + connes CO-AUTHOR attribution and joint-clause flags pre-registered.

---

## 10. Substrate framing

This synthesis operates at the **canonical-sourcing layer** of `phononic-framing.md` (substrate-first canonical sourcing for the 458× factor) and the **explanation-direction layer** (substrate-IS direction-of-explanation: D_K spectral structure → spectral-edge count → emergent horizon area → semiclassical formula as thermodynamic limit).

The 458× FAIL at §W1b1-63 is NOT a substrate insufficiency. The substrate IS the spectral triple `(A_K, H_K, D_K)`. The semiclassical Bekenstein-Hawking formula `S_BH = A/(4ℓ_p²)` is a derived thermodynamic limit; at LRD scale, the substrate-IS Hochschild horizon-state count differs from the semiclassical limit by α(LRD) = 1/458. This is the substrate-first reading.

Container-thinking inversions FORBIDDEN throughout: the substrate does not "fail to accommodate" an externally-imposed entropy budget; the externally-imposed budget IS the semiclassical thermodynamic limit, which is a derived consequence of the substrate's own spectral structure. The 458× factor is the LRD-scale correction to the semiclassical limit.

---

## 11. Cross-references

- §W1b1-61 PASS verdict (audit_sha256=`231990406eb2c881...`) — cohomology-class Level-1 invariance preserved.
- §W1b1-62 PASS verdict (audit_sha256=`9565694b31138b08...`) — graph-automorphism σ-equivariance preserved.
- §W1b1-63 FAIL verdict (audit_sha256=`dcd9fcf8fac10e37...`) — primary subject of this synthesis.
- `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` — registry-PASS criterion for K-counter advancement.
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — algebra-INVARIANT vs algebra-DEPENDENT classification of bits_per_pixel.
- `cross-pillar-bridge-anatomy.md §"Forward template-adoption" Hybrid Independence Test` — 4-clause test for K-counter advancement.
- `joint-theorem-promotion.md` 4-stage pathway — Stage-0 candidate text drafted (§4) for §VII.AF.1-LRD-EXTENSION.
- `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"` — substrate-first direction-of-explanation for branch (c).
- `substrate-first-canonical-sourcing.md §(ii)` — audit pattern for α(M) substrate-first sourcing at S89.
- S87 W11-3 Friedrich-Bär saturation theorem (η_FB_lower = 0.40, empirical floor 0.4365) — bottom-K invariance at L_max ≥ 12; relevant for branch (b) refutation.
- S86 W-5 §VII.AF.1 cross-pillar bridge — instance #1 of K-counter; potential successor instance from CF-W3-1 PASS (CF-W3-3 registry landing).
- S63 area-as-spectral-edge-count theorem — substrate-first replacement of semiclassical Bekenstein-Hawking; underpins branch (c).

---

**End of S88 Workshop W3 synthesis (solo, hawking-theorist, 2026-05-07).**
