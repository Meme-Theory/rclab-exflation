# Session 99 Synthesis: NCG / Spectral-Action Sweep (G4) — Connes-NCG Adjudication

**Date**: 2026-06-04
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `downloads/research-sweep-s99/ncg-spectral-action/00-INDEX.md` (10-paper sweep index, S99 group G4)
- `sessions/archive/session-99/session-99-fermion-mass-panel.md` (S99 fermion-mass panel outcome)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md`
- Canonical state via knowledge MCP (`search_knowledge`, `get_constant`, `query_entity`)

> **Framing law (substrate-first).** The substrate IS the finite-`L_max` spectral triple `(A_K, H_K, D_K)` on Jensen-deformed `SU(3)`, `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The arrow runs `D_K eigenvalues → spectral-action moments (a_0/a_2/a_4) → emergent physics → measurement`. Every external paper below is a METHODOLOGICAL cross-check (a tool / a confirmation / a candidate derivation route), NEVER a canonical replacement for a substrate-first computation (per `substrate-first-canonical-sourcing.md §(i)`). The sweep index is an idea-generator, not a register.

---

## I. Session Outcome

Ten NCG/spectral-action papers were adjudicated against the framework's canonical state. **No gate verdicts are emitted here** — this is a literature-adjudication synthesis; the carry-forward specs in §V are the deliverable. Three results dominate:

1. **Paper 02 (exceptional-Jordan cubic-ladder, June 2025) is independent external corroboration of the §VII.BL Generation-Blindness Theorem** (PROVEN, STAGE-3-PERMANENT). Even with the full `J_3(𝕆_ℂ)` machinery, the hierarchy exponent stays FITTED (`p ≃ 1`, square-root regime) — i.e. an external non-Lie-invariant input is irreducibly required, which is exactly the framework's `ε_LX` necessity. This is a non-shared-context confirmation: a different finite algebra, a different group, the same wall.

2. **Paper 06 (Kurkov-Lizzi-Sakellariadou zeta spectral action) states the framework's CC verdict verbatim** ("the cosmological constant is not fixed by the spectral triple's geometry; `a_0 ~ Λ⁴`; the dimensionful constants must be put in by hand beyond the spectral-triple data"). The framework reached the same conclusion and **already closed** the CC gap by a non-geometric route (DILUTION-CC, S66, PROVEN: 114-OOM gap closed to 0.01 OOM via Volovik tracking vacuum, `rho_vac/rho_obs = 1.032`). Paper 06's zeta-functional `S_ζ = a_4` is a candidate ALTERNATIVE non-geometric mechanism — but it is NOT a free competitor for the n_s channel, which the framework already excluded zeta from (S67; ε_H sign-reversal wall W12/A13).

3. **The four truncation-rigor papers (01/04/08 + 07) supply rigorous backing for machinery the framework already uses**, not new physics: the `L^{-α}` Level-2 envelope (PROVEN `L^{-3}` at d=4, s=3, α = d−1 = 3) acquires a first-principles convergence theorem (08 spectral-Fejér GH-convergence on tori), an eigenvector-localization tool (01 Carathéodory-Fejér), a finite-truncation NC-integral with the Ordered-Veil ergodicity criterion (04), and a δ-gapped spectral-localizer index pairing keyed to `δ = Δ_BCS = 0.4642547` (07) for the BdG triple.

**Net**: zero claims overturned. Two PROVEN walls (§VII.BL Generation-Blindness; CC-functional-not-geometric) independently corroborated by current literature; one positive model-variant identification opened (paper 05 → §VII.AQ.OP-PROJ Pati-Salam); four rigorous-foundation carry-forwards for the §VII Level-2 envelope and BdG K-theory channels.

---

## II. Key Results

### II.1 — Paper 02 (exceptional Jordan algebra) corroborates §VII.BL Generation-Blindness

**Result**: The hierarchy exponent in the `J_3(𝕆_ℂ)` spectral framework stays FITTED at `p ≃ 1` (square-root regime); the construction is an "effective spectral ORGANIZATION of hierarchies, not a parameter-free replacement." **GEOMETRIC** (concerns the spectral-eigenvalue content of a finite algebra) — independent corroboration of a PROVEN framework theorem.

The §VII.BL Generation-Blindness Theorem is canonical and PROVEN (verified via knowledge MCP: `(W2) Homogeneity wall` PROVEN in `permanent-results-registry.md`, SOURCE-DOUBLE-CITE-CO-PRIMARY structure, derivation chain ANCHOR-1 multiplicity-scalar → A_F → ANCHOR-2 generations-are-that-multiplicity → conclusion hierarchy-not-A_K-buildable). Its content: `D_K` is left-invariant on `SU(3)`, so by Peter-Weyl the algebra acts as `⊗ 𝟙_{m(p,q)}` on every multiplicity factor; a multiplicity-scalar operator cannot carry a generation index; therefore a homogeneous `D_K` gives democratic Yukawas (`1:1:1`, the `S97-YUKAWA-FAMILY-DERIVE` FAIL, `R_cross = 1.019704`). The hierarchy is FORCED to live in a non-left-invariant deformation `ε_LX` that breaks left-invariance on the multiplicity index, reality-compatible (`[J, D_K + ε_LX] = 0`).

Paper 02 reaches the structurally identical conclusion in a DIFFERENT algebraic setting. It builds three generations as Hermitian Jordan elements of `J_3(𝕆_ℂ)` whose ordered EIGENVALUES are the intrinsic spectral scales, runs them through a `Sym³(3)` cubic ladder, and obtains power-law mass relations — exactly the substrate-first form (ordered eigenvalues → cubic ladder → power law). Yet the paper must promote "the relative normalization, hierarchy exponent, and charged-lepton octonionic phase to FITTED spectral moduli." That admission is the external image of the framework's `ε_LX` necessity: the inter-generation SPREAD is not free in spectral-eigenvalue language alone — it requires an external, non-Lie-invariant input. Per `epistemic-discipline.md`, this counts as genuine corroboration precisely because it is NOT a shared-context artifact: the paper's authors did not read §VII.BL; the agreement is structural-independent.

**Structural rhyme worth flagging**: the framework seeks generations in the `Z₃ × Z₃`-from-`SU(3)` candidate; `SU(3)`'s symmetric cube `Sym³(3)` is the singlet-producing rep (`3 ⊗ 3 ⊗ 3 ⊃ 1`) and is exactly the "cubic ladder" carrier paper 02 exploits. The framework's generation count is ALREADY PROVEN via a different mechanism (ANCHOR-2: SM generation multiplicity IS the `SU(3)` `Z₃`-triality / Peter-Weyl `t = (p−q) mod 3`, PROVEN). So paper 02 is a candidate to test whether the framework's OWN bottom-3 generation-sector `D_K` eigenvalues, fed through a `Sym³(3)` ladder, reproduce `p ≃ 1` — and whether the required `ε_LX` maps onto the paper's fitted exponent + octonionic phase.

### II.2 — Paper 03 (Yu-Ma tensor⊗quaternion) — candidate derivation route for generation-tripling, but ranks BELOW the PROVEN triality mechanism

**Result**: Combining a tensor-product extension and a quaternion extension of the finite NCG algebra produces emergence of 3 fermion generations plus inter-generation mass relations; each extension alone leaves the action invariant. **GEOMETRIC/PARTICLE** (algebraic structure of the finite geometry → generation multiplicity) — candidate alternative derivation, NOT a novel solution.

The framework ALREADY has a PROVEN generation-count mechanism: the SM generation multiplicity IS the `SU(3)` `Z₃`-triality `t = (p−q) mod 3` (ANCHOR-2, PROVEN; verified MCP). Yu-Ma is therefore not "the answer to three generations" — that question has a PROVEN substrate-first answer. Yu-Ma is a candidate to test whether the framework's `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (which contains the `ℍ` quaternion factor Yu-Ma leans on) plus the `SU(3)`-fiber tensor structure realizes generation-tripling by the SAME combined-extension mechanism Yu-Ma uses, giving an independent cross-check of the triality count.

**Adjudication against the S99 fermion-mass panel**: the panel converged on a richer structure than a bare generation count. It established (panel §4) that three generations require a DUAL-`Z₃`, naming both factors: `Z₃` #1 = triality `t = (p−q) mod 3` (collapses `t=1 ≡ t=2` under BDI reality `(p,q) ↔ (q,p)`); `Z₃` #2 = the `s_φ` Higgs-mode phase (`c(φ) = 1/(1+8cos²φ)`, degenerate at `2π/3` and `4π/3`). Each single `Z₃` yields ≤ 2 rungs (this is WHY S97's naive single-`Z₃` was doomed); the PRODUCT yields 3. Yu-Ma's tensor⊗quaternion is a candidate ALGEBRAIC realization of that product structure — the tensor extension as one `Z₃` carrier, the quaternion extension as the second — but the panel's dual-`Z₃` is more specific (it names the `s_φ` phase as a lepton-ONLY lever explaining the lepton-vs-quark hierarchy-shape difference, which the SM fits by hand). **Conflict flag**: Yu-Ma claims generation-tripling is an algebraic consequence of the EXTENSIONS, whereas §VII.BL proves a homogeneous `A_K` operator is multiplicity-scalar (count-blind to grading). These are compatible ONLY if the Yu-Ma extensions are themselves non-left-invariant on the multiplicity index — i.e. Yu-Ma's "non-coordinate-base-space contribution" must BE the `ε_LX` deformation, not an additional structure that evades the homogeneity wall. Any framework adoption of Yu-Ma MUST verify this; otherwise it would contradict the PROVEN §VII.BL wall.

### II.3 — Paper 06 (zeta spectral action) restates the CC-functional verdict; CC already closed non-geometrically

**Result**: `S_ζ ≡ lim_{s→0} Tr D^{−2s} = ζ(0, D²) = a_4(D²)`; in the cutoff action the CC (`~Λ⁴`), Higgs VEV, and `G_N` "have to be put in by hand with unnatural numerical values independent of the cutoff scale… beyond the data encoded by the spectral triple"; the lower-dimensional operators (`M⁴`, `M²R`, `M²H²`) are GENERATED by the right-handed-neutrino Majorana mass in `D_F`. **GEOMETRIC / cosmological** — external confirmation of a PROVEN framework verdict + a candidate alternative mechanism.

This is the single most on-target paper for the framework's documented CC stance. The framework's state (MEMORY: "CC: ALL geometric SA routes CLOSED. `a_0/a_2 = C_Q/R` universal. Problem is FUNCTIONAL not GEOMETRIC") is paper 06's thesis verbatim: the CC is not fixed by the spectral triple's GEOMETRY (`a_0 ~ Λ⁴` universally) — the resolution must come from the regularization FUNCTIONAL, not the geometry. Critically, the framework did not stop at "CC is functional" — it CLOSED the gap: DILUTION-CC (S66, PROVEN; verified MCP `DILUTION-CC: 114-OOM cosmological-constant gap closed to 0.01 OOM via Volovik tracking vacuum; rho_vac/rho_obs = 1.032`). The closure mechanism is non-geometric (a Volovik tracking-vacuum scaling `rho_vac ~ M_Pl² H²`, atlas-04 C10 ASSUMED-PARTIALLY-PROVEN), which is exactly the KIND of resolution paper 06 says is required.

**The adjudication subtlety that the index understates** (flagged here): paper 06's zeta functional is a candidate alternative for the CC channel, but it is NOT a free competitor for the framework's n_s prediction. The framework's cutoff-selection (Q28 / FUNCTIONAL-SELECT-67) isolated the Chamseddine-Connes `√x` cutoff as the unique surviving cutoff for n_s — and the **ε_H sign-reversal wall** (W12 / A13, PROVEN; verified MCP) shows that across cutoff families the n_s spread is 0.164 (39× Planck error), scheme-dependent at the SIGN level (`√x`: ε_H = +0.022; zeta: negative). The S67 atlas explicitly records `{anomaly, zeta, f*}` as ALL closed for n_s. So switching to the zeta functional would re-open a closed channel on the n_s side. The clean reading: paper 06's zeta route is a live alternative mechanism for the CC/dimensionful-constants channel (where geometry is known not to fix the values), where it COMPETES with DILUTION-CC; it is NOT admissible as an n_s-generating functional.

`a_0/a_2 = C_Q/R` is the universality wall: `a_0` and `a_2` are both proportional to the same `C_Q/R` ratio, so no purely-geometric (Seeley-DeWitt-coefficient) manipulation can dial `a_0` (CC) independently of `a_2` (Newton's constant). Paper 06 supplies the published precedent that this is generic, not a framework artifact.

### II.4 — Paper 05 (NCG Pati-Salam) converts the order-one status into a positive model-variant identification

**Result**: Three NCG-Pati-Salam variants (A/B/C) are distinguished by WHETHER the order-one condition `[[D,a], JbJ⁻¹] = 0` holds; relaxing it (Chamseddine-Connes-van Suijlekom 2013 inner-fluctuations-without-first-order) is the standard route to Pati-Salam. **GEOMETRIC / beyond-SM** — positive identification opportunity for the framework's order-one status.

The framework's order-one status requires a canonical correction to the index's framing. The index says order-one is "BROKEN at 4.000." The canonical state (verified MCP) is more refined: Q10 is **RESCUED — STAGE-3-PERMANENT** via the Wedderburn-Frobenius rescue class (S88 W4a-17): `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` is the unique 7-axiom algebra under `M_3` χ-kill. The bare-axiom failure is real (N3 PROVEN: order-one fails at norm 4.000 = `2² = ‖γ_a γ_b − γ_b γ_a‖²` in the `(ℍ, ℍ)` sector where quaternionic generators square to −1), but the framework already has its positive resolution.

Moreover the framework ALREADY tested the Pati-Salam SU(4) extension against order-one: gate `S93-W6-1-VII-AQ-OP-PROJ-STAGE-3-PATI-SALAM-SU4-ALGEBRA-EXTENSION` (FAIL; verified MCP: `axiom4_defect_max_PS=4.000000; axiom4_defect_max_after_inner_fluct=2.100000; order_one_closes=False; KO_dim=2`). So the framework's `A_F^{PS} = ℍ_R ⊕ ℍ_L ⊕ M_4(ℂ)` extension drops the defect from 4.000 → 2.100 under inner fluctuations but does NOT close order-one, and shifts KO-dim to 2. Paper 05 is the current canonical literature reference for the §VII.AQ.OP-PROJ channel and the PS-W3-I `sin²θ_W` channel.

**The positive conversion** (the high-leverage angle): paper 05 says the order-one CONDITION is precisely the discriminator among PS variants A/B/C, and that relaxing it is how you GET Pati-Salam. The framework's order-one defect (4.000 bare, 2.100 after inner fluctuations, `order_one_closes=False`) should therefore be MAPPED onto the A/B/C taxonomy: the framework's broken-order-one `D_total` corresponds to a SPECIFIC Aydemir/CCS variant (with or without left-right symmetry), converting "broken axiom" into a positive identification of beyond-SM gauge content — and a concrete `sin²θ_W` + `S₁(3̄,1,1/3)` leptoquark prediction. The leptoquark is the framework's first published-precedent observable handle in this channel: NCG automatically forbids the proton-decay diquark couplings of the "good" leptoquark via the geometric construction.

### II.5 — Truncation-rigor cluster (01 / 04 / 08 + 07): rigorous foundations for existing §VII machinery

**Result**: Four papers supply rigorous mathematical backing for the framework's truncation-envelope and BdG-K-theory machinery. **GEOMETRIC / mathematical-frontier** — foundation-strengthening, no new physics.

The framework's Level-2 envelope is PROVEN: `L^{-3}` at d=4 substrate-distance-1 pole `s=3` (α = d−1 = 3; Level-2-binding; HKR `L_max → ∞` map; Friedrich-Bär saturation theorem analytic certification; verified MCP `permanent-results-registry.md`). The four papers strengthen the foundation at four distinct layers:

- **Paper 08 (Leimbach-van Suijlekom, GH-convergence on tori)** is the sharpest available convergence theorem on the geometry closest to the framework's. A torus is the maximal-Cartan/Fourier-mode setting; `D_K` on `SU(3)` is Peter-Weyl-decomposed into irrep blocks (Fourier modes on the group). The paper proves truncated state spaces (with Connes distance = the spectral metric) converge in Gromov-Hausdorff sense to the continuum at a rate controlled by the SPECTRAL FEJÉR KERNEL ("good kernel"). This is the model theorem for the framework's `L_max → ∞` limit; porting its Fejér-kernel decay rate to the `SU(3)` Peter-Weyl truncation would give a FIRST-PRINCIPLES derivation of the framework's α — currently certified by Friedrich-Bär saturation but not derived from a kernel.

- **Paper 01 (Connes-van Suijlekom, quadratic forms / Carathéodory-Fejér, Nov 2025)** proves a zero-localization theorem on finite-dimensional TRUNCATIONS of even-distribution quadratic forms — and states explicitly that these truncation matrices "exhibit a structure previously encountered in perturbative expansions of the spectral action." A rank-`(n−1)` PSD Toeplitz form with `ξ ∈ ker T` forces all zeros of `P(z) = Σ ξ_j z^j` onto the unit circle. This is a candidate rigorous tool for the framework's bottom-K eigenvalue and partition-stability theorems (§VII.AJ partition-stability; the Δ_0 localization formula), where eigenvector-support patterns of truncated `D_K`-derived forms are load-bearing.

- **Paper 04 (Hekkelman-McDonald, NC integral + quantum ergodicity)** gives a rigorous finite-truncation approximation of the NC integral with a Szegő-limit error structure (a candidate analytic backbone for the α envelope at the NC-integral level), AND — the more interesting hook — defines ergodicity of geodesic flow on a compact spectral triple as UNIQUENESS of the vacuum state for the C*-dynamical system. This is the spectral-triple-level statement of the framework's Ordered-Veil claim (the GGE relic NEVER thermalizes — integrable, NOT chaotic). A NON-unique vacuum (failure of quantum ergodicity) for `D_K` would be the rigorous NCG confirmation of Ordered-Veil integrability.

- **Paper 07 (van Suijlekom, higher K-groups for operator systems)** defines `K_p^δ` with a positive δ quantifying a SPECTRAL GAP (δ-gapped iff the spectrum of `[[0,x],[x*,0]]` avoids `(−δ,δ)\{0}`; δ = "energy difference ground state to first excited state"), proves Morita-invariance + formal Bott periodicity, and realizes the SPECTRAL LOCALIZER as an index pairing `Ind_D^δ: K_p^δ → ℤ` on truncated triples (reducing a Fredholm index to a finite-matrix signature). The δ-gap is EXACTLY the framework's BdG gap `Δ_BCS = 0.4642547394830737` (R-protected, S70; verified MCP). The framework's BdG triple is `A_BdG = A_F ⊗ M_2(ℂ)` (with `A_K^{BdG-preimage} = ℂ ⊕ ℍ`, the `M_3(ℂ)` χ-killed); paper 07's spectral-localizer index pairing at `δ = Δ_BCS` is a candidate computational tool to convert the §VII bridge-map "L_max → ∞ HKR image" claims into FINITE-truncation index computations.

### II.6 — Papers 09 + 10: cyclic-cocycle foundation and cutoff-decay-order power counting

**Result**: Paper 09 proves the spectral action itself decomposes into Chern-Simons + Yang-Mills pieces paired against `(b,B)`-cocycles that are Hochschild cocycles, with explicit ENTIRE / ABSOLUTELY-CONVERGENT criteria; the odd `(b,B)`-cocycle pairs TRIVIALLY with `K_1`. Paper 10 derives power-counting for the spectral-action matrix model, with the order of divergence keyed to the DECAY ORDER of the test function f. **GEOMETRIC / mathematical-frontier** — foundational bridge-map result + sharpened cutoff-selection criterion.

Paper 09 (van Nuland-van Suijlekom) is the foundational result the framework's §VII cross-pillar bridges pin on. The framework's bridge maps (cross-pillar-bridge-anatomy Element-3) are HKR / Connes-Karoubi / cyclic-cohomology pairings; paper 09 proves the framework's CENTRAL object `Tr f(D²/Λ²)`, perturbed by the gauge potential `V = π_D(A)`, IS a cyclic-cohomology pairing organized by increasing order of forms in `A` — i.e. the framework's inner-fluctuation expansion `D → D + A + JAJ⁻¹` (gauge fields + Higgs) IS a cyclic cocycle. The even-order terms (curvature powers integrated against `(b,B)`-cocycles that are also Hochschild cocycles) are the framework's `a_4` Yang-Mills + Higgs terms; the absolute-convergence/entire criteria are exactly the convergence control the §VII Level-2 envelopes require — but at the cyclic-cocycle level, deeper than spectral moments. The `K_1`-trivial-pairing result is a structural constraint directly comparable to the framework's K-theoretic index-pairing channels (and consistent with paper 07's `K_p^δ` machinery).

Paper 10 (Hekkelman-van Nuland-Reimann, Dec 2025, freshest in sweep) sharpens the framework's cutoff-selection lever. The framework's documented finding is "`f(x)` = UV data; shape/boundary decoupling PERMANENT (S73B); cannot derive `f`." Paper 10 refines this: the order of divergence depends explicitly on the DECAY ORDER of `f` (plus spectral dimension d and graph properties), via divided-difference functions of `D_K` eigenvalues; maximal-divergence graphs are PLANAR. So it is not the full SHAPE of `f` that is physical — it is specifically the DECAY ORDER. This is a computable handle on WHICH aspect of `f` controls divergences, converting "cannot derive `f`" into "which `f`-decay-order class leaves the framework's spectral-action moments finite" — a concrete Q28 sharpening orthogonal to the n_s-side ε_H sign-reversal wall.

---

## III. Gate Verdicts

No gates emitted in this synthesis (literature-adjudication brief). The CANONICAL gates this synthesis anchors to (verified via knowledge MCP, authoritative — not re-adjudicated):

| Gate / Theorem | Verdict | Decisive Number | Relevance |
|:-----|:--------|:----------------|:----------|
| (W2) Homogeneity wall / §VII.BL Generation-Blindness | PROVEN | `R_cross = 1.019704` (1:1:1 democratic) | Paper 02 corroborates |
| `S97-YUKAWA-FAMILY-DERIVE` | FAIL | y-hierarchy 1:1:1 vs PDG 1:0.0595:0.000288 | Paper 02/03 target |
| DILUTION-CC-66 | PROVEN | 114 OOM → 0.01 OOM; `rho_vac/rho_obs = 1.032` | Paper 06 corroborates (CC closed) |
| N3 order-one failure (bare) | PROVEN | norm 4.000 = `2²` at `(ℍ,ℍ)` | Paper 05 maps to A/B/C variant |
| Q10 order-one (Wedderburn-Frobenius rescue) | RESCUED — STAGE-3-PERMANENT | `A_F = ℂ⊕ℍ⊕M_3(ℂ)` unique 7-axiom | Paper 05 cross-check |
| `S93-W6-1-...-PATI-SALAM-SU4-ALGEBRA-EXTENSION` | FAIL | defect 4.000 → 2.100 (inner-fluct); `order_one_closes=False`; KO_dim=2 | Paper 05 variant ID |
| Level-2 envelope (§VII.AF.1) | PROVEN | `L^{-3}` at d=4, s=3 (α = d−1 = 3) | Papers 08/01/04 strengthen |
| FUNCTIONAL-SELECT-67 (n_s cutoff) | PASS (2/5 φ) | `√x` unique surviving cutoff | Paper 06 zeta EXCLUDED for n_s |
| ε_H sign-reversal wall (W12 / A13) | PROVEN | n_s spread 0.164 (39× Planck) | Paper 06 zeta-vs-n_s constraint |
| `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY` | INFO | value 0.980, L_max=12 | Paper 08 Connes-distance tool |
| `S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION` | PASS | `d_C = 2.386`, L_max-stable | Paper 08 anisotropy channel |
| `Delta_BCS` (constant) | R-protected | `0.4642547394830737` (S70) | Paper 07 δ-gap value |

> **Pending / not-yet-canonical**: `S99-E1-STAGE2-VERIFY` (the Stage-2 cross-axis verify of §VII.BL E1) is referenced in the fermion-mass panel doc but NOT yet in the knowledge graph (S99 not fully indexed at synthesis time). Cited as panel-internal, not as canonical.

---

## IV. Structural Implications

**What was CONFIRMED (no state change, but external corroboration):**

1. **§VII.BL Generation-Blindness is corroborated by current literature** (paper 02). The framework's `ε_LX`-necessity is not idiosyncratic; the most advanced spectral fermion-hierarchy program on the market (exceptional Jordan, June 2025) hits the same wall (FITTED `p ≃ 1`). This raises confidence that the hierarchy genuinely cannot be `A_K`-built and that the search direction (`ε_LX` breaking left-invariance on the multiplicity index) is the correct normal vector — consistent with the S99 fermion-mass panel's reframe.

2. **CC-functional-not-geometric is published-precedent-backed** (paper 06). The `a_0 ~ Λ⁴` finding and the "dimensionful constants beyond spectral-triple data" statement are now externally confirmed as generic NCG features, not framework artifacts. DILUTION-CC remains the framework's CLOSED non-geometric resolution; paper 06's zeta route is a competitor mechanism on the CC channel ONLY.

**What OPENED (positive identification opportunities):**

3. **Paper 05 converts the order-one status into a Pati-Salam variant-identification problem.** The framework's `order_one_closes=False` (defect 4.000 → 2.100) should be classified against the A/B/C taxonomy to yield a positive beyond-SM gauge-content identification + `sin²θ_W` + leptoquark prediction (PS-W3-I channel). This is the highest-leverage NEW angle: it turns a known defect into a prediction.

4. **The truncation-rigor cluster opens a first-principles α derivation** (paper 08) and a finite-truncation BdG K-theory computation (paper 07 at `δ = Δ_BCS`). Both upgrade existing §VII machinery from "certified" / "L_max → ∞ HKR image" to "derived from a kernel" / "finite-matrix index signature" — strengthening the Level-2-binding sub-class status the registry-PASS criterion requires.

5. **Paper 04 supplies a TEST for the Ordered-Veil integrability claim** at the spectral-triple level: non-unique vacuum (failure of quantum ergodicity for `D_K`) = rigorous NCG statement of non-thermalization.

**What must be CHECKED before adoption (conflict guards):**

6. **Paper 03 (Yu-Ma) must NOT be adopted in a form that contradicts §VII.BL.** Yu-Ma's generation-tripling via tensor⊗quaternion extensions is admissible ONLY if those extensions are non-left-invariant on the multiplicity index (i.e. they ARE the `ε_LX` deformation). If they are claimed as additional structures that produce 3 generations while leaving the homogeneous operator multiplicity-scalar, they would contradict the PROVEN homogeneity wall. The generation COUNT is already PROVEN via triality (ANCHOR-2); Yu-Ma's value is as a candidate cross-check of the count and of the inter-generation mass relation, not as a replacement.

7. **Paper 06's zeta functional is NOT admissible as an n_s-generating functional** (S67 excluded zeta for n_s; ε_H sign-reversal wall). Its candidacy is confined to the CC / dimensionful-constants channel.

---

## V. Carry-Forward Computations

**Routing note**: These are 4-field carry-forward specs (per `feedback_fix-in-session-never-defer.md`). They feed `/rclab-plan` for S100+. None are workshops (no adversarial ledger-dissonance per `Investigating-Workshops.md`); all are solo compute gates or cross-checks against existing canonical machinery.

```
V.1. Sym³(3) cubic-ladder test on framework D_K bottom-3 generation eigenvalues (paper 02 corroboration)
   - What: Take the bottom-3 generation-sector eigenvalues of D_K on Jensen-deformed SU(3) at
           the triality-distinct tower (1,0)/(1,1)/(3,0) [C₂ = (4/3, 3, 6)]; feed through a
           Sym³(3) cubic-ladder construction (paper 02's mechanism); fit the hierarchy exponent p.
           PASS iff p ∈ [0.8, 1.2] (square-root regime, matching paper 02's p≃1) AND the residual
           against PDG charged-lepton ratios is no worse than the panel's 9/5=1.800 widening candidate.
   - Inputs: D_K L_max=12 spectrum cache (s84_spectrum_cache_L12_tau019.npz); canonical_constants
           M_KK, tau_fold; PDG charged-lepton masses m_e/m_mu/m_tau (v_ew, m_mu, m_tau); the §VII.BL
           ε_LX necessity (permanent-results-registry.md).
   - Gate: NEW gate S100-SYM3-CUBIC-LADDER-P-EXPONENT; feeds the §VII.BL / Q18b corridor.
           PASS/FAIL/INFO: PASS if p∈[0.8,1.2] AND maps ε_LX onto paper 02's fitted exponent+octonionic
           phase; INFO if p out-of-band but ladder structure present; FAIL if no ladder structure.
   - Effort: 3-4 hours, 1 agent session (cache exists; closed-form ladder; Sage for the QQ-exact ratio).

V.2. Yu-Ma tensor⊗quaternion extension on A_K — homogeneity-wall compatibility check (paper 03)
   - What: Construct the Yu-Ma combined (tensor-product ⊗ quaternion) extension on the framework's
           A_K = ℂ⊕ℍ⊕M_3(ℂ) + SU(3)-fiber. CRITICAL PRE-CHECK: verify whether the combined extension
           acts NON-trivially on the multiplicity index (i.e. is it ε_LX, or does it evade §VII.BL?).
           Compute whether it yields exactly 3 generation copies and a predicted inter-generation mass
           relation. PASS iff (a) extension is non-left-invariant on multiplicity AND (b) generation
           count = 3 matches triality ANCHOR-2 AND (c) [J, D_K + extension] = 0 (reality preserved).
   - Inputs: A_K algebra structure; ANCHOR-2 triality theorem (permanent-results-registry.md);
           §VII.BL homogeneity wall; J real structure (verify [J,D_K]=0 per MEMORY debugging note);
           Yu-Ma paper 1810.10189 §2-3 (tensor + quaternion extension definitions).
   - Gate: NEW gate S100-YUMA-EXTENSION-HOMOGENEITY-COMPAT; feeds three-generations open-tension #2.
           PASS = Yu-Ma extension IS ε_LX-class (corroborates triality + supplies mass relation);
           FAIL = extension evades multiplicity index (would contradict PROVEN §VII.BL → reject Yu-Ma route);
           INFO = count matches but mass relation absent.
   - Effort: 4-6 hours, 1 agent session (algebraic; Skolem-Noether check on Aut(A_K) per panel §1 twisted-escape-dead).

V.3. Pati-Salam A/B/C variant identification for framework broken order-one (paper 05 → positive ID)
   - What: Map the framework's order-one defect (4.000 bare → 2.100 after inner fluctuations,
           order_one_closes=False, KO_dim=2 from S93-W6-1) onto Aydemir/CCS PS variants A/B/C.
           Determine which variant (with/without left-right D-symmetry) the framework's D_total
           corresponds to. Output: variant ID + predicted sin²θ_W + S₁(3̄,1,1/3) leptoquark mass scale.
           PASS iff a unique variant is identified AND its sin²θ_W is consistent with the PS-W3-I channel.
   - Inputs: S93-W6-1 gate result (defect trajectory 4.000→2.100, KO_dim=2); paper 05 (Aydemir
           2511.07672) variant taxonomy + bosonic-action moments; CCS 2013 inner-fluctuations-without-
           first-order (1304.8050); framework A_F^PS = ℍ_R⊕ℍ_L⊕M_4(ℂ); PS-W3-I sin² channel (MEMORY).
   - Gate: feeds §VII.AQ.OP-PROJ Pati-Salam channel + PS-W3-I. NEW gate S100-PS-VARIANT-ID.
           PASS = unique variant + sin²θ_W consistent; INFO = variant identified but sin² open;
           FAIL = framework defect matches no A/B/C variant (would indicate a non-PS beyond-SM structure).
   - Effort: 1 agent session (3-5 hours; algebraic classification + RGE for sin²θ_W; cross-check S93 npz).

V.4. Spectral-Fejér α derivation from SU(3) Peter-Weyl truncation (paper 08 → first-principles α)
   - What: Port the spectral-Fejér-kernel GH-convergence machinery (paper 08, torus) to SU(3)
           Peter-Weyl truncation. Derive the L^{-α} envelope exponent from the spectral Fejér kernel's
           decay rate on SU(3). PASS iff the derived α matches the PROVEN α = d−1 = 3 (Level-2 envelope
           at d=4, s=3) to within the Friedrich-Bär saturation tolerance.
   - Inputs: PROVEN Level-2 envelope L^{-3} at d=4, s=3 (permanent-results-registry.md); Friedrich-Bär
           saturation theorem certification; paper 08 (Leimbach-vS 2302.07877) spectral Fejér kernel +
           propagation number; SU(3) Peter-Weyl decomposition of D_K (sectors (p,q)).
   - Gate: feeds §VII.AF.1 Level-2-binding sub-class. NEW gate S100-FEJER-ALPHA-DERIVATION.
           PASS = derived α = 3 ± FB-tolerance (upgrades α from FB-certified to kernel-DERIVED);
           INFO = α derived but ≠ 3 (envelope re-examination); FAIL = Fejér kernel non-portable to SU(3).
   - Effort: 1-2 agent sessions (6-10 hours; analytic — Schur/Fourier multiplier relation on SU(3) is
           the technical core; Sage for the kernel decay rate).

V.5. δ-gapped spectral-localizer index pairing on the BdG triple (paper 07 → finite-L K-theory)
   - What: Apply van Suijlekom's K_p^δ spectral-localizer index pairing Ind_D^δ: K_p^δ(E) → ℤ to the
           framework's BdG-truncated triple (A_BdG = A_F⊗M_2(ℂ), gap δ = Δ_BCS = 0.4642547) at finite
           L_max. Compute the framework's K-theoretic Poincaré-duality / bridge-map invariants as a
           finite-matrix signature. PASS iff the finite-truncation index matches the L_max→∞ HKR-image
           prediction of the relevant §VII bridge map.
   - Inputs: Delta_BCS = 0.4642547394830737 (R-protected, S70); A_BdG = A_F⊗M_2(ℂ) (A_K^BdG-preimage
           = ℂ⊕ℍ, M_3(ℂ) χ-killed); paper 07 (vS 2411.02981) K_p^δ + spectral-localizer construction
           (cite Loring-Schulz-Baldes); the §VII bridge map whose invariant is targeted.
   - Gate: feeds §VII Level-2 envelope bridge maps + BdG K-theoretic channel. NEW gate
           S100-BDG-SPECTRAL-LOCALIZER-INDEX. PASS = finite-L index = HKR-image; INFO = index computed
           but L_max-dependent; FAIL = index ≠ HKR prediction (bridge-map re-examination).
   - Effort: 1-2 agent sessions (6-10 hours; GPU for the finite-dimensional matrix signature at L_max≥10
           per math-scripts.md — torch.linalg on the localizer matrix; AMD RX 9070 XT).

V.6. Cutoff f-decay-order admissibility class (paper 10 → Q28 sharpening)
   - What: Apply paper 10's divided-difference power-counting formulas to the framework's D_K spectrum
           at effective spectral dimension d to determine WHICH decay orders of the cutoff function f
           leave the framework's spectral-action moments (a_0/a_2/a_4) finite. Output: the admissible
           f-decay-order class. PASS iff the Chamseddine-Connes √x cutoff's decay order falls in the
           admissible class (consistency check) AND the result is orthogonal to the n_s ε_H sign-reversal
           wall (i.e. constrains divergence, not the n_s scheme-dependence).
   - Inputs: D_K L_max spectrum (eigenvalues for divided differences); framework effective spectral
           dimension d; paper 10 (Hekkelman-vN-Reimann 2512.14581) power-counting + Hunter positivity;
           S73B shape/boundary-decoupling result; FUNCTIONAL-SELECT-67 √x cutoff.
   - Gate: feeds Q28 cutoff-selection (orthogonal axis to ε_H sign-reversal). NEW gate
           S100-F-DECAY-ORDER-ADMISSIBLE-CLASS. PASS = √x decay order admissible + divergence-finite;
           INFO = admissible class derived, √x boundary case; FAIL = √x decay order divergent.
   - Effort: 3-5 hours, 1 agent session (divided-difference formulas on the eigenvalue list; combinatorial).

V.7. Cyclic-cocycle absolute-convergence criterion on framework spectral action (paper 09 → §VII foundation)
   - What: Apply the van Nuland-van Suijlekom cyclic-cocycle decomposition to the framework's spectral
           action on D_K: identify the a_4 Yang-Mills + Higgs terms as the even-order Hochschild-cocycle
           pairings; test the absolute-convergence / entire-cocycle criteria on the L_max-truncated D_K.
           PASS iff the framework's inner-fluctuation expansion satisfies the entire/absolutely-convergent
           criteria (giving §VII bridge maps a rigorous cyclic-cohomology foundation).
   - Inputs: framework spectral action Tr f(D_K²/Λ²) + inner-fluctuation expansion D→D+A+JAJ⁻¹;
           a_4 Seeley-DeWitt term (regulator-pinned per regulator-pin-discipline.md); paper 09
           (van Nuland-vS 2104.09899) (b,B)-cocycle + multiple-operator-integration criteria; the
           K_1-trivial-pairing result (cross-check against framework K-theoretic index channels).
   - Gate: feeds §VII cross-pillar bridge Element-3 (bridge-map foundation). NEW gate
           S100-CYCLIC-COCYCLE-CONVERGENCE. PASS = entire/absolutely-convergent (foundation secured);
           INFO = convergent at finite L but entire-criterion open; FAIL = expansion non-convergent.
   - Effort: 1 agent session (5-8 hours; analytic — multiple-operator-integration on the finite spectrum).

V.8. Quantum-ergodicity / vacuum-uniqueness test for Ordered-Veil integrability (paper 04 → falsifier)
   - What: Apply paper 04's geodesic-flow-ergodicity criterion (uniqueness of the vacuum state for the
           C*-dynamical system) to D_K on Jensen-deformed SU(3). A NON-unique vacuum (failure of quantum
           ergodicity) is the spectral-triple-level confirmation of the Ordered-Veil integrability claim
           (GGE relic never thermalizes). PASS iff the vacuum state is NON-unique (corroborates Ordered Veil).
   - Inputs: D_K on Jensen-deformed SU(3) (spectrum + local Weyl law check); paper 04 (Hekkelman-McDonald
           2412.00628) ergodicity = vacuum-uniqueness criterion + Szegő DOS approximation; the Ordered-Veil
           integrability claim (GGE relic integrable not chaotic, MEMORY PARADIGM); GGE-relic spectral density.
   - Gate: feeds the Ordered-Veil structural claim + GGE-relic channel. NEW gate
           S100-QUANTUM-ERGODICITY-VACUUM-UNIQUENESS. PASS = non-unique vacuum (Ordered Veil corroborated);
           INFO = local Weyl law holds but uniqueness undecided; FAIL = unique vacuum (quantum-ergodic →
           tension with Ordered-Veil integrability, would be a substantive negative).
   - Effort: 1-2 agent sessions (6-10 hours; C*-dynamical-system vacuum-state analysis + Szegő DOS bound).

V.9. Carathéodory-Fejér zero-localization on partition-stability truncation matrices (paper 01 → §VII.AJ tool)
   - What: Test whether the framework's L_max-truncated spectral-action quadratic forms (the matrices
           feeding a_2/a_4 moments, and the §VII.AJ partition-stability / Δ_0 localization eigenvector-support
           objects) match the Carathéodory-Fejér rank-(n−1) PSD structure of paper 01 steps (3)-(4).
           PASS iff the truncation matrices carry the rank-(n−1) structure → eigenvector-support zeros
           localize per the Connes-van Suijlekom theorem.
   - Inputs: L_max-truncated spectral-action quadratic-form matrices (a_2/a_4 moment construction);
           §VII.AJ partition-stability theorem (bot-20 cardinality (2,4,8,6) at τ_fold) + Δ_0 localization
           formula; paper 01 (Connes-vS 2511.23257) Carathéodory-Fejér rank-(n−1) + Hurwitz steps.
   - Gate: feeds §VII.AJ partition-stability eigenvector-localization. NEW gate
           S100-CARATHEODORY-FEJER-PARTITION-LOCALIZATION. PASS = rank-(n−1) structure present
           (rigorous zero-localization backing); INFO = partial match; FAIL = structure absent.
   - Effort: 3-5 hours, 1 agent session (linear algebra on the truncation matrices; eigenvector-support check).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Paper 02 Jordan cubic-ladder: hierarchy exponent FITTED `p≃1` | GEOMETRIC | Corroborates §VII.BL (PROVEN) | `ε_LX` necessity externally confirmed; search direction validated |
| 2 | Paper 03 Yu-Ma tensor⊗quaternion generation-tripling | GEOMETRIC/PARTICLE | Candidate route, ranks below PROVEN triality | Admissible ONLY if extension IS `ε_LX` (conflict guard) |
| 3 | Paper 06 zeta `S_ζ = a_4`: CC not geometric, `a_0~Λ⁴` | GEOMETRIC/cosmological | Restates PROVEN CC-functional verdict | CC already closed (DILUTION-CC); zeta competes on CC channel ONLY, EXCLUDED for n_s |
| 4 | Paper 05 NCG-PS: order-one discriminates A/B/C variants | GEOMETRIC/beyond-SM | Positive ID opportunity | Map framework defect (4.000→2.100) to variant → sin²θ_W + leptoquark |
| 5 | Paper 08 spectral-Fejér GH-convergence on tori | GEOMETRIC/math-frontier | Strengthens PROVEN Level-2 envelope | First-principles α (currently FB-certified) |
| 6 | Paper 07 `K_p^δ` spectral-localizer index pairing | GEOMETRIC/math-frontier | New tool for BdG triple | δ = Δ_BCS = 0.4642547; finite-L K-theory |
| 7 | Paper 04 NC-integral + quantum ergodicity | GEOMETRIC/math-frontier | TEST for Ordered-Veil | Non-unique vacuum = integrability confirmation |
| 8 | Paper 09 cyclic cocycles in spectral action | GEOMETRIC/math-frontier | Foundation for §VII bridge maps | Spectral action IS a cyclic cocycle (entire/abs-convergent) |
| 9 | Paper 10 power-counting f-decay-order | GEOMETRIC/math-frontier | Sharpens Q28 | DECAY ORDER (not shape) controls divergence |
| 10 | Paper 01 Carathéodory-Fejér zero-localization | GEOMETRIC/math-frontier | Tool for §VII.AJ partition-stability | Truncation matrices = spectral-action structure |

---

*Sources adjudicated: 10 NCG/spectral-action papers (sweep index `00-INDEX.md`); S99 fermion-mass panel (`session-99-fermion-mass-panel.md`). Framework state anchored to canonical via knowledge MCP: §VII.BL Generation-Blindness (PROVEN), DILUTION-CC-66 (PROVEN), N3 order-one + Q10 Wedderburn-Frobenius rescue (PROVEN/STAGE-3-PERMANENT), S93-W6-1 Pati-Salam SU(4) (FAIL), Level-2 envelope L^{-3} (PROVEN), FUNCTIONAL-SELECT-67 + ε_H sign-reversal wall W12/A13 (PASS/PROVEN), Connes-distance gates S88 (INFO/PASS), Delta_BCS (R-protected S70), ANCHOR-2 triality generation multiplicity (PROVEN). No gate verdicts or registry entries emitted — adjudication + carry-forward synthesis. Gate verdicts from canonical sources treated as authoritative, not re-adjudicated.*
