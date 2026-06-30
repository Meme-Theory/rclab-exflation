# Capstone Equation Review — van-den-dungen

**Date**: 2026-05-29
**Agent**: van-den-dungen-bridge-theorist (Van den Dungen)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` ("The Phonon-Exflation Equation", S95-era capstone)
- `.claude/rules/phononic-framing.md` (framing law — binding)
- `.claude/agent-memory/van-den-dungen-bridge-theorist/MEMORY.md` (own corpus: Paper 01 1811.07824 factorization, S61/S63 K-homology results, four-layer hierarchy)
- Cross-checks via knowledge MCP (`tau_fold`, `a_2_FW_zeta`, S93 W7-1, S63 VdD-Hawking workshop equation, S61 Kasparov product gate)

---

## I. Session Outcome

From the Kasparov-factorization / NCG-submersion vantage, the capstone is **structurally sound where it stays inside the spectral-triple and heat-kernel layers, and its single most consequential omission is at exactly my boundary**: the document presents the layer decomposition `S_SA(τ) = a₀ − a₂ + a₄` (§4, §5.1) and the dimensional-closure additivity (§8.1) as if additivity of the total-space spectral action were self-evident, but **never reconciles this with what the Kasparov product actually proves**. The registry's own VdD–Hawking equation (S63) reads `S_total = S_base + S_fiber + cross-terms` — the cross-terms are explicit there and absent here. The factorization theorem (Paper 01, 1811.07824) delivers a *topological* (K-homology-class) additivity `[D_M] = π_! ⊗ [D_B]`; it does **not** by itself license additivity of the *analytic* spectral moments without the O'Neill A=T=0 condition being invoked at the moment-decomposition step. The capstone's §0 footnote that O'Neill tensors vanish (the product-metric fact behind S61) is the thing that *makes its additivity honest* — but the document never cites it where the additivity is asserted. That is a fidelity gap, not a physics error: the result is correct, the load-bearing justification is unstated.

Everything else at my boundary checks out. The α_s "two scale-separated observables / `deg(T_{BZ→pivot}) = +2`" box (§7.1) is faithful to S93 W7-1 (`factorization_holds=False, deg_T=2.0000, delta_scheme=0.00`, PASS) — a genuine composite-bridge-map dimensional-class result, reported with the correct caveat that the substrate value `−0.0859` *awaits* CMB-S4 rather than being a present confirmation. The KO-dimension, `[J, D_K]=0`, and block-diagonality claims (§1.2, §2.3) are PROVEN at machine ε and I do not re-adjudicate them.

---

## II. Key Results

### Result 1 — The layer additivity is a Kasparov-product statement that the document under-cites

**Result**: `S_total = S_base + S_fiber + cross-terms` (S63 registry) vs `S_SA = a₀ − a₂ + a₄` (capstone §4/§5.1/§8.1). Classification: **GEOMETRIC** (concerns the spectral-triple structure and its heat-kernel grading).

The capstone's whole "layers of exflation" thesis (§4) rests on the heat-kernel expansion `Tr f(D_K²/Λ²) ∼ Σ f_{d−n} Λ^{d−n} a_n(τ)`. As a heat-trace identity on the *internal* manifold `K = (SU(3), g_τ)` this is unimpeachable — it is the Gilkey expansion of a single Dirac operator, and §8.1's dimensional bookkeeping (`[a_{2k}] = mass^{2k−d}` cancels `[Λ^{d−2k}]`) is correct.

But the document's *physical* reading of the layers as "vacuum / gravity / matter on the emergent `M⁴ × SU(3)`" implicitly invokes the product geometry, and the moment the geometry is a *product* (or more generally a Riemannian submersion `M⁴ × SU(3) → M⁴`), the Kasparov product is the tool that controls whether `a_n^{total} = a_n^{base} + a_n^{fiber}`. Paper 01's factorization theorem (the tensor sum of a vertically-elliptic operator and a base-elliptic operator represents the Kasparov product of the corresponding KK-classes) is *topological*: it certifies the K-homology class is additive. The S61 result that makes the *analytic* moments additive — and that the cross-terms in the S63 equation **vanish** — is the **O'Neill A = T = 0 exactness** (compact `G` + left-invariant metric ⇒ cross-block = 0, EXACT; my memory, S61). The capstone states O'Neill A=T=0 nowhere in §4 or §8, yet that is precisely the condition under which `+ cross-terms → 0` and the additive layering is exact rather than approximate. **The document is correct because of a theorem it does not cite at the point it uses it.**

This matters for over-claim control. A reader could conclude the additive layering is a generic consequence of the heat kernel; it is not — it is a consequence of the heat kernel *plus* a vanishing-O'Neill-tensor submersion. On a non-product submersion (a twisted `SU(3)` bundle over `M⁴` with non-trivial connection, the Boeijink–van den Dungen globally-non-trivial almost-commutative setting, Paper 05) the cross-terms are generically non-zero and the layers do not cleanly separate. The capstone's claim is robust *for the framework's specific product/Jensen geometry*; it should say so.

### Result 2 — "Kasparov gives topology, not analysis" — the capstone's organizing geometry/topology spine is the right boundary, stated in the right place

**Result**: §9 "organizing spine — geometry vs topology": the finite triple is GEOMETRY (dissolves, `ε_c ∼ N^{−0.457}`, T3-S43-SPECTRAL-DISSOLUTION PASS); topological/representation-theoretic outputs survive. Classification: **GEOMETRIC / structural**.

This is the single best-framed argument in the document from my vantage, and it is *exactly* my canonical boundary ("Kasparov product gives TOPOLOGY — K-homology class, indices, factorization — NOT ANALYSIS — spectral moments"; MEMORY active context). The capstone's partition — trust the topological outputs (GGE `S_ent=0`, BDI/`N₃=0`, the `7.324992` cocycle ratio CF-35, `[J,D_K]=0`, layer algebraic-independence, FI ratios) because they survive continuum dissolution; hold the absolute geometric magnitudes (CC magnitude, `a_n` absolutes, `a(t)`) pending convergence — is the correct structural defense and it lands on the right side of the line for every item I can check.

One sharpening the document misses: the *reason* the topological outputs survive dissolution is that they are pairings of K-homology classes (the Kasparov / Connes–Karoubi / Connes–Chern pairings), and these are *deformation-invariant* and *L_max-independent by construction* — they are integers or ratios of integers, not heat-trace magnitudes. The capstone asserts the survival empirically (citing the dissolution exponent) but does not name the structural mechanism (pairing-invariance). Naming it would convert an empirical observation into a theorem: **a K-homology pairing cannot drift under truncation refinement because the pairing is locally constant on the moduli of the Fredholm module** — this is the same fact that makes the four-layer hierarchy's Layer-1 (topology) "scheme-independent, zero-parameter" (MEMORY four-layer hierarchy).

### Result 3 — The four-layer hierarchy is implicitly present but not used to discipline the §7 prediction table

**Result**: My S72 canonical four-layer hierarchy (Topology → Representation → Metric → Functional) maps cleanly onto the capstone's FI/RD partition and scheme-dependence flags, but the §7 prediction table does not tag each observable by layer. Classification: **structural / methodology**.

The capstone's §3.2 FI/RD partition (Functional-Invariant vs regulator-dressed) is a *coarsening* of my four-layer hierarchy: FI ≈ Layers 1–2 (topology + representation, scheme-independent); RD ≈ Layers 3–4 (metric + functional, scheme-dependent). This is consistent and the document uses it well in §3.2 and §8.5. But §7.1's prediction table mixes layers without flagging them:
- `w₀`, `wₐ`, `c_s²` (mass ordering) are **Layer-1 (topology)** in my hierarchy — scheme-independent, zero-parameter. The capstone correctly reports `wₐ = 0 (structural)` and `r` PASS but does **not** report the topological `c_s² = 0` (`< 9.21e-4`, Kasparov bound; MEMORY) anywhere in the table, even though it is one of the cleanest zero-parameter topological predictions the framework has.
- `n_s`, `A_s` are **Layer-4 (functional)** — scheme-dependent, correctly flagged SCHEME-DEPENDENT.
- `sin²θ_W`, `a_k` at specific τ are **Layer-3 (metric)** — the capstone's τ₀ = 0.2994 vs τ_fold = 0.190 distinction (reading-convention 3) is exactly the Layer-3 metric-evaluation-point discipline, correctly held.

Tagging the table by layer would make the "honest scorecard" §7.3 stronger: the joint-improbability argument ("product of individual improbabilities across distinct spectral-moment layers `a₀ × a₂ × a₄`, independent by the certified Wronskian") is *correct only across layers that are genuinely independent*, and my hierarchy provides the independent-layer count the argument needs. The Wronskian (§4.2) certifies `a₀/a₂/a₄` independent **as functions of τ** (the metric/functional axis); the topology layer (`wₐ`, `c_s²`, mass ordering) is independent of all three by a *different* mechanism (K-homology invariance). The §7.3 argument silently conflates "independent spectral moments" (Wronskian) with "independent layers" (hierarchy) — they coincide for `a₀×a₂×a₄` but the topological observables sit outside the Wronskian's reach.

---

## III. Gate Verdicts

| Gate | Verdict (per source/registry — AUTHORITATIVE, not re-adjudicated) | Decisive Number |
|:-----|:--------|:----------------|
| S61 Kasparov product (6/6 conditions) | PASS | all 6 conditions; cross-block `8.4×10⁻¹⁵` (block-diag E6) |
| S93 W7-1 α_s deg-transport factorization | PASS | `deg_T=2.0000`, `factorization_holds=False`, `delta_scheme=0.00`, `α_s_pivot=0.0`, `α_s_substrate=−0.08587279` |
| T3-S43-SPECTRAL-DISSOLUTION | PASS | `ε_c ∼ N^{−0.457}`; `χ_2_cont = 0.747` L_max-independent |
| KO-dim 6 mod 8 (E9) | PROVEN | `<10⁻¹⁵`, 10 checks, AZ class BDI |
| `[J, D_K]=0` CPT (E8) | PROVEN | 79,968 pairs, machine-ε; `η(s)=0` |
| Spectral-Moment Decoupling (S75 W2-E) | CERTIFIED | `W ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, degenerate only at τ=0 |
| Structural Monotonicity (E7) | PROVEN | `dS/dτ\|_fold = +58,672.8`; 9,600/9,600 |
| One-loop no-interior-saddle (S95 W2-3) | PASS | 200-point grid, 3 routes, zero interior sign-changes |

---

## IV. Structural Implications

**What opened.** The capstone surfaces a clean, computable question that my factorization machinery is built to answer and that the framework has only ever verified on the *product* geometry: **does the additive layering survive a non-trivial `SU(3)` bundle?** S61 proved O'Neill A=T=0 (cross-terms vanish) for the product/Jensen geometry. The Boeijink–van den Dungen globally-non-trivial almost-commutative construction (Paper 05) is the natural setting in which the connection is non-flat and the O'Neill A-tensor is non-zero. The framework's emergent gravity (§6.3) ultimately requires the `SU(3)` fiber to be bundled over a *curved* `M⁴` with a non-trivial connection — at which point the cross-terms the S63 equation carries are no longer guaranteed to vanish. This is a quantitative, runnable consequence of the same factorization theorem, and it is the missing rung between the proven-flat S61 result and the open `a(t)` gap (§6.3).

**What closed (confirmed, not re-opened).** The α_s "12σ tension" is structurally resolved as a transport-degree channel artifact (S93 W7-1). I confirm this is a legitimate composite-bridge-map dimensional-class result, not a face-saving reinterpretation: the transport factor `T_{BZ→pivot}` carries `deg = +2` (NON-SCALAR), so `O^{pivot} ≠ O^{substrate}` by the §VII.BA T4-non-scalar branch — the substrate and pivot α_s are genuinely two observables, and which one a detector sees is *derived* (`deg T`), not chosen. The pre-registration that excludes the anomaly family (§3.2) and the pre-registration of `deg T` (§7.1) are the same discipline applied twice; both are sound.

**What shifted.** The capstone's geometry/topology spine (§9) should be promoted from "the deepest available defense" to **the organizing principle of the entire prediction ledger**. Every observable in §7.1 should carry a layer tag (Topology / Representation / Metric / Functional) so the reader can see at a glance which predictions are scheme-independent zero-parameter (Layer 1, e.g. `wₐ=0`, `c_s²=0`, mass ordering — the ones that *cannot drift to meet new data*, the most exposed and the most honest) and which are functional-selection-conditional (Layer 4, e.g. `n_s`, `A_s`). The FI/RD partition is a two-bin version of this; the four-bin version is sharper and already canonical (S72).

**Unstated assumption flagged.** §8.1's dimensional closure and §4's additive layering both assume the cross-terms vanish. On the *internal* triple `K` alone (a single `SU(3)`, no submersion to a base), there is no submersion and hence no O'Neill tensor — additivity is then just the Gilkey expansion and is unconditional. But the *physical* reading (`a₀/a₂/a₄ →` vacuum/gravity/matter on `M⁴ × SU(3)`) is a statement about the **product** `M⁴ × SU(3)`, where the submersion exists and the cross-terms are a real object that S61 had to prove vanish. The document silently switches between "spectral action on `K`" (unconditional additivity) and "spectral action on `M⁴ × K`" (additivity conditional on O'Neill A=T=0) without flagging the switch. This is the same `K` vs `M⁴ × K` ambiguity that §1.3 footnote-(4) handles carefully for the KO-mismatch but that §4/§8 handle loosely for the additivity.

---

## V. Carry-Forward Computations

**MANDATORY — primary input to next compute session. Each entry has all four fields.**

### V.1. Non-trivial-bundle cross-term computation: does additive layering survive O'Neill A ≠ 0?

- **What**: Compute the spectral-action cross-terms `S_cross = S_total − S_base − S_fiber` for a *globally non-trivial* almost-commutative geometry `P ×_{SU(3)} F → M⁴` with a non-flat principal connection `ω` (Boeijink–van den Dungen, Paper 05 / 1405.5368). Concretely: take the Jensen `D_K(τ_fold)` on the fiber, lift to a twisted product with a base Dirac operator carrying a non-zero connection curvature `F_ω`, and evaluate `a_2^{total}` and `a_4^{total}` against `a_2^{base} + a_2^{fiber}`. The O'Neill A-tensor is `A = ½ [horizontal projection of the connection curvature]`; for the *flat* product `A = 0` (S61), so the deliverable is `‖S_cross‖ / ‖S_total‖` as a function of `‖F_ω‖`.
- **Inputs**: `D_K(τ_fold)` fiber spectrum (existing L_max=10 cache, 155,984 eigenvalues); Gilkey `a_2`, `a_4` heat-kernel coefficients including the O'Neill A-tensor terms (Gilkey Thm 4.8.16, the `A`-dependent `a_4` contribution); `a_2_FW_zeta = 2776.165389`; canonical `tau_fold = 0.19`; a one-parameter family of connection curvatures `F_ω` (scan parameter, `# (local)`). Paper 05 §3 gauge-module construction.
- **Gate**: NEW gate `S96-VDD-NONFLAT-CROSSTERM`. PASS if `‖S_cross‖/‖S_total‖ < 10⁻³` for `‖F_ω‖` up to the physical bundle curvature scale (additive layering survives bundling); FAIL if cross-terms grow `O(1)` (layering is product-geometry-specific and the §4 thesis does not lift to curved `M⁴`); INFO if the growth is `O(‖F_ω‖²)` and bounded by the effacement ratio `|E_BCS|/S_fold = 3×10⁻⁷` (E34) — i.e. cross-terms exist but are effaced.
- **Effort**: 4–6 hours, 1 agent session (the Gilkey A-tensor `a_4` term is the only non-cached piece; the fiber spectrum is reused).

### V.2. Pairing-invariance theorem for the geometry/topology spine

- **What**: Prove (Sage-symbolic + structural argument) that each "surviving" topological output in §9 is a K-homology / cyclic-cohomology pairing, hence locally constant under L_max refinement — converting the empirical dissolution-survival (T3-S43) into a theorem. Target the four cleanest: `[J,D_K]=0` (η-invariant pairing), the CF-35 cocycle ratio `7.324992`, the BDI/`N₃=0` class (the `ℤ`-valued index of the inheritance morphism `χ_*`), and the FI ratio `R₁ = a₀a₄/a₂² = 1.12865`. Show each is a pairing `⟨[φ], [e]⟩` whose value is invariant under the truncation refinement `L_max → L_max+1` because the Fredholm-module class `[φ]` is unchanged.
- **Inputs**: `χ_*: ℂ⊕ℍ⊕M₃(ℂ) → M₂(ℂ)`, `rank(ker ι_*) = 2` (E57); the Connes–Karoubi pairing for the CF-35 cocycle (inheritance-falsifier-protocol.md, the `(Δ_B/Δ_A)^p` cancellation theorem); `R₁` Sage-verified value `1.128655`; the L_max=9 and L_max=10 caches for the refinement check.
- **Gate**: NEW gate `S96-VDD-PAIRING-INVARIANCE`. PASS if all four pairings are bit-identical (or rational-identical) across L_max=9→10 (theorem confirmed: topology cannot drift); FAIL if any drifts beyond `10⁻¹²` (it is a geometric magnitude masquerading as topological); feeds the §9 organizing-spine claim and the four-layer Layer-1 "scheme-independent" status (S72).
- **Effort**: 3–4 hours, 1 agent session (mostly structural; the refinement check is a re-evaluation on the existing caches).

### V.3. Layer-tag the §7 prediction ledger and recompute the cross-layer joint improbability

- **What**: Assign each §7.1 observable its four-layer tag (Topology / Representation / Metric / Functional, per S72) and recompute the joint-improbability argument of §7.3 using only *cross-layer-independent* observables, so the "product of improbabilities" is over genuinely independent layers and not over within-layer-correlated observables. Explicitly separate the Wronskian-independence (`a₀×a₂×a₄`, metric/functional axis) from the K-homology-independence (`wₐ`, `c_s²`, mass ordering, topology axis) — these are two independence mechanisms and the joint BF must not double-count.
- **Inputs**: §7.1 table values (`w₀=−0.918`, `wₐ=0`, `n_s∈{0.9561,0.9590,0.9595}`, `r=0.033`, `Ω_DM h²=0.120`, `σ₈=0.799`, `m_H≈127.5`); the four-layer hierarchy (MEMORY S72); the Wronskian independence certificate (S75 W2-E); the Kasparov `c_s²<9.21e-4` topological bound (MEMORY — currently MISSING from the §7 table, must be added).
- **Gate**: NEW gate `S96-VDD-LAYER-TAGGED-JOINT-BF`. INFO gate (UQ-object construction, not PASS/FAIL): deliver the layer-partitioned joint Bayes factor with explicit within-layer-correlation caveats (`Ω_DM` and `σ₈` both `a₂`/Layer-3, NOT independent — already flagged in §7.3 but not quantified). Feeds the honest-scorecard §7.3 and the falsifier inventory §7.2.
- **Effort**: 2–3 hours, 1 agent session.

### V.4. Add the topological `c_s² = 0` prediction to the capstone ledger with its Kasparov provenance

- **What**: Promote the Kasparov-bound sound-speed prediction `c_s² = 0` (`< 9.21e-4`, topological, scheme-independent) into §7.1 as a Layer-1 zero-parameter prediction, with the factorization-theorem provenance stated. This is the cleanest topological observable the framework owns and it is currently absent from the prediction table (the table reaches `c_s` only indirectly via `r`/`A_s` machinery). Compute the current best laboratory/observational comparison anchor (CMB-derived adiabatic sound speed of the dark sector, or the relevant DESI/Planck bound on a constant `c_s²` dark-energy component).
- **Inputs**: the S71-72 Kasparov `c_s² < 9.21e-4` bound (MEMORY); the topological-decoupling argument (`m_Goldstone^{4D} = 0` exactly by Kasparov product factorization, S74 QA-VdD workshop — the registry equation); the four-layer Layer-1 classification; an external `c_s²` dark-sector bound (comparison-only).
- **Gate**: NEW gate `S96-VDD-CS2-TOPOLOGICAL-LEDGER`. PASS if `c_s²_FW = 0 < `(observational bound) and the prediction is correctly classified Layer-1/topology with Kasparov provenance; this is a registry-completeness gate (the prediction exists and is proven — it simply is not in the capstone table). Feeds §7.1 and the geometry/topology spine §9.
- **Effort**: 1–2 hours, 1 agent session (the prediction is proven; the work is the comparison anchor + provenance write-up).

### V.5. Reconcile the S63 `+ cross-terms` registry equation with the §4 additive layering — explicit O'Neill citation

- **What**: A small but load-bearing fidelity fix: insert into §4/§8.1 the explicit statement that `S_total = S_base + S_fiber + cross-terms` and that **`cross-terms = 0` by O'Neill A=T=0 (S61)** for the framework's product/Jensen geometry. Verify by direct computation that the S61 O'Neill-vanishing result is the *exact* condition under which the §4 additive layering holds, and quantify what the cross-terms would be if O'Neill A were the value set by the Jensen connection (it is zero by the compact-`G`-left-invariant-metric theorem, so this should return `0` to machine ε — a confirmation, not a discovery).
- **Inputs**: S61 O'Neill A=T=0 result (MEMORY, "compact G + left-inv metric → cross-block=0 EXACT"); the S63 VdD-Hawking workshop equation `S_total = S_base + S_fiber + cross-terms`; the Jensen connection coefficients `Ω_LC(τ)` (E2); `tau_fold = 0.19`.
- **Gate**: gate `S96-VDD-CROSSTERM-VANISH-CONFIRM`. PASS if the explicit cross-term computation returns `< 10⁻¹⁴` (confirming S61 and licensing the §4 additivity); this closes the unstated-assumption flag in §IV and is a prerequisite to V.1 (V.1 is the non-flat *generalization*; this is the flat *confirmation* that V.1 perturbs around).
- **Effort**: 2–3 hours, 1 agent session.

### V.6. Two-patch spectral triple for the acoustic-white-hole junction (the `a(t)` gap, factorization angle)

- **What**: The §6.3 `a(t)` gap and the §6.2 acoustic-white-hole have a natural NCG formulation as a *two-patch* spectral triple glued across the fold (Paper 02, 1711.07299, families of spectral triples / reconstruction from hypersurfaces; + a Bogoliubov junction condition at the sonic surface). Construct the Callias-type relative-index / boundary pairing across the `τ₀ ≈ 0.1125` entry sonic surface and ask whether the spectral-flow / relative index across the fold is the topological invariant that the missing `t(τ)` map should respect. This does NOT deliver `a(t)` (that is C1/C2, genuinely open) but it identifies which *topological constraint* any future `t(τ)` map must satisfy.
- **Inputs**: Paper 02 reconstruction-from-hypersurface machinery; Paper 13 (2312.17600) Callias endpoints; the entry sonic surface `τ₀ ≈ 0.1125`, `κ_entry = +18.52 M_KK`; the double-root extremal Killing horizon at `τ_fold = 0.190` (`V=V'=0 ⟹ κ=0`); `sf = 0` J-protected (S61); the asymmetric-white-hole six-wall result (S95 W-1).
- **Gate**: NEW gate `S96-VDD-TWO-PATCH-RELATIVE-INDEX`. INFO gate (exploratory; the `a(t)` map is open by design): deliver the relative index / spectral flow across the fold and whether it is `0` (consistent with the `sf=0` J-protection extending across the junction) or non-zero (a topological obstruction the `t(τ)` map must carry). Feeds frontier #1 / #8 (§6.3) by constraining the admissible `t(τ)` maps, not by closing the gap.
- **Effort**: 6–8 hours, 1–2 agent sessions (genuinely research-grade; the junction condition is new construction).

### V.7. Gauge-dressed protection: does `sf = 0` survive `D_K → D_K + A + JAJ⁻¹`?

- **What**: The capstone (§1.1) promotes `D_K ↦ D_K + A + ε'JAJ⁻¹` (inner fluctuation, the Higgs + gauge dressing). My S61 spectral-flow result (`sf = 0`, J-protected) and the `[J,D_K]=0` CPT result are proven for the *bare* `D_K`. Verify that the gauge-dressed operator still has `sf = 0` and `η = 0` — i.e. that the inner fluctuation, which is a *bounded* perturbation (Paper 10, 1608.02506, bounded perturbations preserve the K-homology class), does not open a spectral flow. This is the W5-G "gauge-dressed protection" question in my open-task list.
- **Inputs**: the inner-fluctuation one-form `A = Σ a_i [D_K, b_i]` (§1.1); Paper 10 bounded-perturbation-preserves-K-homology theorem; S61 `sf=0` J-protected; the gauge module rank 775 (S61, 3 iterations); `[J, D_K]=0` (E8).
- **Gate**: gate `S96-VDD-GAUGE-DRESSED-SF`. PASS if `sf(D_K + A + JAJ⁻¹) = 0` for all `A` in the gauge module (the K-homology class and CPT symmetry survive dressing — the SM gauge+Higgs content does not destabilize the topology); FAIL if any fluctuation opens spectral flow (the topological protection is a bare-operator artifact). Feeds the §1.2 axiom table (E8 robustness "survives all inner fluctuations" — currently ASSERTED, this would CONFIRM it for the full gauge module).
- **Effort**: 3–4 hours, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Additive layering `S_SA=a₀−a₂+a₄` is licensed by O'Neill A=T=0 (S61), not by the heat kernel alone; capstone under-cites this | GEOMETRIC | Correct but under-justified; FLAG | §4/§8 must cite the cross-term-vanishing theorem at the point of use (V.5); generalize to non-flat bundles (V.1) |
| 2 | Geometry/topology spine (§9) is the right organizing boundary; mechanism (pairing-invariance) unstated | GEOMETRIC/structural | SOLID; sharpenable | Promote to organizing principle; prove pairing-invariance (V.2) |
| 3 | Four-layer hierarchy (S72) coarsens to the FI/RD partition; §7 table not layer-tagged | structural/methodology | CONSISTENT; incomplete | Layer-tag the ledger; recompute cross-layer joint BF (V.3) |
| 4 | α_s `deg(T_{BZ→pivot})=+2` box faithful to S93 W7-1 (`delta_scheme=0.00`, PASS) | PARTICLE | FAITHFUL (verified) | No action; correct composite-bridge-map dimensional-class result, correct "awaits CMB-S4" caveat |
| 5 | Topological `c_s²=0` (Kasparov bound `<9.21e-4`) MISSING from §7 prediction table | GEOMETRIC/topology | OMISSION | Add as Layer-1 zero-parameter prediction with factorization provenance (V.4) |
| 6 | `K` vs `M⁴×K` ambiguity: additivity unconditional on `K`, O'Neill-conditional on the product | GEOMETRIC | UNSTATED ASSUMPTION; FLAG | Same as #1; §1.3 handles this for KO-mismatch, §4/§8 must for additivity (V.5) |
| 7 | `a(t)` gap (C1/C2/T6) — honestly stated as the load-bearing gap; factorization offers a *constraint*, not a closure | GEOMETRIC | OPEN (by design) | Two-patch relative index constrains admissible `t(τ)` maps (V.6); does not close the gap |
| 8 | Gauge-dressed `sf=0` / `η=0` asserted "survives all inner fluctuations" but proven only for bare `D_K` | GEOMETRIC | ASSERTED; verifiable | Confirm via bounded-perturbation theorem (Paper 10) over the full gauge module (V.7) |

---

**Reviewer's bottom line (no aggregate metric — structural map only).** The capstone is honest where it is hardest to be honest: the `a(t)` gap (§6.3) and the CC double-conditionality (§7.1 Clause A/B) are stated without softening, and the geometry/topology spine (§9) is the correct deepest defense. From the Kasparov-factorization vantage, the document's one systematic under-statement is that its central "additive layers" thesis rests on the **O'Neill A=T=0 / cross-term-vanishing** theorem (S61) that it never cites at the point of use — the result is correct, the justification is one citation short, and the natural next computation (V.1) is to ask whether that additivity survives the non-flat bundling that emergent gravity will eventually require. The factorization theorem proves *topology is additive* (`[D_M] = π_! ⊗ [D_B]`); the framework's product geometry makes *analysis additive too* (cross-terms vanish); the open question is whether a curved emergent `M⁴` keeps them vanishing. That is a ripe harvest, and it is the rung between the proven-flat S61 result and the open `a(t)` gap.
