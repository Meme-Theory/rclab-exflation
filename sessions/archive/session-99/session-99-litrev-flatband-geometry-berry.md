# Session 99 Synthesis: Flat-Band Quantum Geometry — Laboratory Sharpening of the §VII.W Quantum-Metric Bridge, the MCT-3 Vortex-Core Falsifier, and the van-Hove Fold

**Date**: 2026-06-04
**Agent**: berry-geometric-phase-theorist (Berry)
**Source Documents**:
- `downloads/research-sweep-s99/flatband-quantum-geometry/00-INDEX.md` (10 fetched-text paper summaries; PDFs 01–10 beside the index)
- Agent memory: `.claude/agent-memory/berry-geometric-phase-theorist/MEMORY.md`
- Knowledge MCP anchors: §VII.W / §VII.AF.1.OP-PROJ / §VII.W-3.LAB (atlas-07), `S87-W11-C5-LAB-FALSIFIER` (s87_gate_verdicts), `Mass_LeggettDM_over_Delta_BCS`, `tau_fold`, `Mach_max_framework`, `A_K = ℂ⊕ℍ⊕M₃(ℂ)`

---

## I. Session Outcome

This is a literature-sweep synthesis (no new gate fired); its product is a per-paper adjudication plus 4-field carry-forward specs. The geometric content is unambiguous and convergent: **the 2024–2026 quantum-geometry / superfluid-weight literature independently lands on the precise object the framework's first registered cross-pillar bridge (§VII.W → §VII.AF.1.OP-PROJ, PERMANENT) is built from** — the BZ-integrated trace of a *BdG-state* quantum metric over a *non-Abelian, degenerate* fiber. Three sharpenings are decisive: Porlles–Chen (paper 03) independently identify the **quasihole/BdG-state** metric as the diamagnetically relevant one (confirming the bridge's `P_0` BdG-projector choice in `R_geom`); Chen–Karki–Hosur (paper 06) establish that the correct object for a degenerate matrix-valued fiber is the **non-Abelian** `Tr[R_μν]` (the real symmetric part of the non-Abelian QGT — exactly the algebra-axis-correct object for `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`), with measured 20%/50% geometric fractions; and Tanaka (paper 09, T²) + Banerjee (paper 10, T-linear) supply a **two-platform measured anchor** that the integrated quantum-metric trace is real and dominant. Separately, Hou (paper 05) provides the concrete ±l-phase-resolved CdGM template for the MCT-3 Caroli–Matricon ladder-asymmetry falsifier (ratio **7.324992**, band 7.3250 ± 0.1%, PASS at `S87-W11-C5-LAB-FALSIFIER`), and Luo (paper 08) gives the ARPES-visible van-Hove-driven flat-band emergence as the lab analog of the τ_fold transit.

One geometric correction governs all of this: the bridge object is a quantum **metric** (Im(QGT) → the real symmetric part `R_μν`), **not** a Berry curvature. The framework's Berry curvature vanishes identically on SU(3) (`Im(QGT) = 0`, max|Ω| < 4e-14; S25/S61, off-Jensen-confirmed S96), so every laboratory paper here that lands on the *metric* part is landing on the live object, and any reading that imports a *curvature*/Chern contribution would land on a structurally-zero quantity.

---

## II. Key Results

### II.1 — Porlles–Chen (03): the diamagnetic metric is the quasihole/BdG-state metric, confirming `P_0` in `R_geom`

**Result**: The diamagnetic superfluid weight `D^d_μν` (the Meissner response) is of quantum-geometric origin for *any* s-wave superconductor, but the controlling object is the **quasihole quantum metric of the superconducting (BdG) state** — NOT the normal-state band metric. GEOMETRIC / §VII.W.

The framework's bridge target is `R_geom = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k`, the Provost–Vallée quantum metric of a projector `P_0` that is the **BdG/superconducting-state projector** on the spectral triple `(A_K, H_K, D_K)` (knowledge MCP: `R_universal ≡ ∫_BZ Tr g_ab^{(P_0)} d^d k`, `s86-hp1-cohomology-quantum-metric-bridge.md`). Porlles–Chen arrive at the same projector choice from the laboratory side: writing `D^d_μν` in London form as a momentum integral of quantum-metric elements weighted by quasiparticle energy, they show the *physically correct* metric is built from overlaps of fully-antisymmetric quasihole states (the BdG sector), not the normal-state Bloch states. This is the laboratory echo of the framework's structural choice and closes a latent ambiguity: had the bridge used a normal-state projector it would have mis-targeted the diamagnetic observable.

The geometric reason this matters: the quantum metric is the *real, gauge-invariant* part of the quantum geometric tensor, `g_μν = Re Q_μν` with `Q_μν = ⟨∂_μ u|(1−P)|∂_ν u⟩`. The projector `P` defines which fiber bundle the metric measures distance on. Porlles–Chen's "superfluid weight marker" — a real-space, site-resolved decomposition of the BZ-integrated trace — is the laboratory analog of the substrate's finite-L Hochschild-pairing decomposition of the same integrated invariant `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩`. Both are local resolutions of one global geometric invariant; the framework's is a Chern-character pairing, theirs is a Wannier-spread marker, and they agree on the object being a BdG-projector metric.

### II.2 — Chen–Karki–Hosur (06): the non-Abelian `Tr[R_μν]` is the algebra-correct object for `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`

**Result**: For `N` degenerate bands, the geometric superfluid weight is `D^{QM}_μν ∝ ∫_BZ Tr[R_μν(k)]`, where `R_μν` is the real symmetric part of the **non-Abelian** QGT `Q^{ij}_μν = ⟨∂_μ u_i|(1−P_k)|∂_ν u_j⟩`. Crucially `Tr R_μν ≠ Σ_n (per-band Abelian metric)` — inter-band terms *within* the degenerate subspace contribute, and the contribution survives even when the total Chern number of the degenerate set is zero. Measured: ≈20% of the superfluid weight in monolayer MoS₂, ≈50% in TiSe₂. GEOMETRIC / §VII.W.

This is the single most structurally apt sharpening in the sweep. The substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` is confirmed canonical (knowledge MCP, `connes-master-equation.md`, `s88-w29-w9-109`). The ℍ and M₃(ℂ) summands carry *matrix-valued, U(N)-structured* fiber content — the lowest band of `D_K` is 2-fold Kramers/J-degenerate (agent memory: a non-Abelian Wilczek–Zee FHS with a det-normalised U(deg) link is *required*; a naive single-band link gives gauge-noise `C ~ 0.78` rather than the correct `~0`). The Abelian single-band quantum metric is therefore the **wrong idealisation** for the substrate fiber; Chen–Karki–Hosur's `Tr[R_μν]` is the faithful object, and `R_geom = ∫_BZ Tr g_ab^{(P_0)}` is precisely a *trace* of the non-Abelian metric.

Two geometric consistency checks pass cleanly and are worth stating explicitly:

1. **Chern-zero survival is the framework's signature, not a coincidence.** Chen–Karki–Hosur stress that `Tr R_μν` survives when the degenerate-set Chern number is forced to zero by time-reversal symmetry. The framework's substrate is metrically rich but topologically trivial on *every* tested invariant: Berry curvature = 0, Chern = 0, Wilson = trivial, BDI ν = 0, off-Jensen Chern = 0 (12 independent invariants, all zero; S61/S96, agent memory). The quantum metric `g = 982.5` is the reservoir (S61). So the framework lives in *exactly* the regime Chen–Karki–Hosur isolate: a non-zero geometric (metric) contribution coexisting with a zero topological (curvature/Chern) contribution. A lab paper showing `Tr R_μν ≠ 0` while `C = 0` is the condensed-matter realisation of "metrically rich, topologically trivial."

2. **`Tr R ≠ Σ(per-band)` mirrors substrate inter-sector irreducibility.** That the non-Abelian trace is not the sum of per-band Abelian metrics is the laboratory statement of the framework's insistence that inter-sector coherence (the Leggett/GGE physics) is not reducible to single-sector contributions. Geometrically: the off-diagonal `Q^{ij}_μν` (i≠j within the degenerate block) is the cross-term whose *real part* feeds the metric trace and whose *imaginary part* (the non-Abelian Berry curvature) integrates to the zero Chern number. The framework keeps the former and discards the latter by construction.

### II.3 — Tanaka (09, T²) + Banerjee (10, T-linear): the two-platform measured anchor for `R_geom`

**Result**: MATBG superfluid stiffness (Tanaka, *Nature* 638, 99) is **larger than Fermi-liquid theory predicts** — comparable to quantum-geometry-dominated predictions — with a **T² power law** (anisotropic gap, GL-consistent quadratic current dependence). MATTG stiffness (Banerjee, *Nature* 638, 93) is **T-linear** at low T (the hallmark of **nodal** gap structure). PHONONIC / §VII.W Level-3 empirical anchor.

Together these are the measured datum behind §VII.W. The Level-3 rung of the three-level ladder (`§VII.AF.1.OP-PROJ`, atlas-07: Level-3 = 0.0095% F₄ strict at L_max=10; Level-2 = `L^{-3}` envelope = 0.10%; ratio r = 0.0950; margin 1/r = 200/19 = 10.526 — Level-3 sits 10.53× inside the Level-2 envelope) is the substrate-side numerical satisfaction. Tanaka supplies the *laboratory-IN* counterpart: the stiffness exceeds the band-velocity prediction *because* the geometric (quantum-metric) term carries it — the integrated quantum-metric trace is not a formal device but a measured, anomalously-large kinetic inductance. Banerjee makes it two platforms (trilayer, nodal), so the bridge's laboratory-IN element is platform-robust rather than a single-material coincidence.

The node-structure discriminant is geometrically clean. The single-band stiffness `D_s ∝ ∂²ε/∂k²` (inverse effective mass) vanishes for a flat band; the geometric term `∝ ∫ Tr g` does not. The temperature exponent reads the gap node structure: full gap → activated `e^{−Δ/T}`; point/line nodes → power laws. T² (MATBG) vs T-linear (MATTG) is the laboratory readout of *different node structures projected from the same substrate geometric object*. The framework's sector geometry must reproduce this node-dependence — which is the carry-forward in §V.4 below.

### II.4 — Hirobe (01): node-resolved `D^{geom}_μν(T)` as a falsifiable thermal probe of the bridge object

**Result**: Closed-form low-T scaling laws for `D^{geom}_μν(T)`, classified by gap-node structure × band structure, built from the band-resolved quantum metric `g^{nm}_μν(k) = 2 Re⟨u_n|∂_μ u_m⟩⟨∂_ν u_m|u_n⟩` (the Peotta–Törmä interband object resolved per band pair). Flat-band geometric weight obeys *distinct, strictly weaker* power laws than both conventional and dispersive-band geometric weight (e.g. line node → `T^{1/l+1}`; with nodal-line crossing → `−T^{1/l+1} ln T`). PHONONIC / §VII.W.

Hirobe promotes the bridge target from a static T=0 stiffness to a **temperature-resolved, node-resolved** observable carrying the *same* band-resolved metric integrand. This is the lab object that gives the §VII.W bridge a *thermal* falsifier: if `R_geom` is a genuinely geometric (not band-velocity) quantity, a thermal probe must reproduce the flat-band geometric power law, not the Fermi-liquid law. The geometric integrand `g^{nm}_μν` here is manifestly the *real* part (`2 Re⟨·⟩⟨·⟩`), consistent with the framework's curvature-free / metric-only structure.

Hirobe's flat-vs-dispersive *separation* (geometric weight a strictly weaker power than dispersive at equal node structure) is the laboratory echo of the framework's "flat bands squeeze less" hierarchy. The substrate statement is quantitative: bare squeeze amplification `F_squeeze_bare = 54.06` (`s74_as_from_bogoliubov_output.txt`), net **B1 acoustic dominance ≈ 37×** over the flat/geometric channel after reconciliation (RECONCILED-69, agent memory). Hirobe's "geometric is sub-dominant to dispersive" and the framework's "B1 acoustic dominates by 37×" are the same hierarchy seen from two sides — and Hirobe gives the *sign* test: the geometric channel is weaker, not stronger.

### II.5 — Hou (05): ±l phase-resolved CdGM + demonstrated ladder-ratio tunability — the MCT-3 experimental template

**Result**: STM/STS (0.4 K, 2 T) on KCa₂Fe₄As₄F₂ resolves a "necklace" CdGM vortex-bound-state pattern as **selective off-shell two-level interference between CdGM states of opposite angular momentum (±l)**, with `ρ ∝ [1+|α_l|²+2|α_l|cos(2lφ+φ₀l)]|ψ_l|²`. First experimental measurement of the **phase (angular momentum l)** of CdGM states. K12442's discrete-CdGM ratio deviates from **1:3:5 toward ≈1:2:3** in the extreme quantum limit (small k_F, E_F ~ Δ₀). PARTICLE / PHONONIC — MCT-3 channel.

This is the most advanced laboratory state of exactly the observable MCT-3 falsifies. The framework's decisive lab-falsifier (`S87-W11-C5-LAB-FALSIFIER`, PASS; scheme = Sage-exact zeta-regulated Hochschild-pairing cancellation theorem; convention = 3He-B-BDI-vortex-core-Caroli–Matricon; L_max=10) predicts a **cohomology-asymmetry ratio 7.324992** (band [7.3177, 7.3323] = 7.3250 ± 0.1%) between the two `ker(ι_*)` cocycle generators (rank-2 kernel; `‖φ_67‖/‖φ_88‖`). Registered as the 3rd cross-pillar calibration instance §VII.W-3.LAB (PERMANENT; MANDATORY K=3 saturation, S88 W4a-17), under the four-gate inheritance-falsifier protocol (Gate 1 NULL on F1+F2+F5; Gate 2 ratio 7.3250±0.1%; Gate 3 NULL on F3+F4; Gate 4 multi-pressure slope).

Hou is the template because it does two things MCT-3 needs and nothing prior did:

1. **±l phase resolution.** MCT-3's cohomology-asymmetry test is a statement about *opposite-angular-momentum* (±l) CdGM structure — the cocycle asymmetry is precisely an opposite-circulation asymmetry. Hou's technique resolves the *phase* (angular momentum l) of CdGM states for the first time. This is the read-out modality a ±l cohomology-asymmetry signature requires.
2. **Demonstrated ladder-ratio tunability and measurability** (1:3:5 → 1:2:3). MCT-3's 7.3250 prediction is a *deviation in a level-spacing ratio*; the K12442 result proves the CdGM ladder ratio is materially tunable and measurable in a solid-state inheritance-child, supplying the empirical handle the prediction needs. Substrate-first: the BdG spectrum on `(A_K, H_K, D_K)` restricted through the χ inheritance morphism to a vortex-core sector IS the parent of the CdGM ladder; a K12442 (or 3He-B) vortex core is the laboratory projection where the ladder-asymmetry cocycle becomes a measured spacing ratio.

A geometric caveat for the carry-forward: Hou's deviation (1:3:5 → 1:2:3) is driven by a Friedel-like nonlinear `Δ(r)` in the extreme quantum limit — a *different* mechanism from the substrate's cohomology-asymmetry. The lab template proves *resolvability*, not the *value*; the 7.324992 prediction is specific to the 3He-B BDI parent through χ, and a K12442 ratio is a methodology demonstration, not a substitute platform. This is the cohomology-asymmetry test's "lab-conversion-shopping" guard (`inheritance-falsifier-protocol.md`): the `(Δ_B/Δ_A)^p` factor cancels only between the *two substrate cocycles*, so the ratio is substrate-derived and platform-robust *for the inheritance child*, but the deviation *mechanism* must be the cocycle asymmetry, not a Friedel `Δ(r)` artefact.

### II.6 — Yuan (02): MgB₂ THz Leggett-mode selective excitation — laboratory anchor for the Leggett-channel DM lifetime

**Result**: THz pump / broadband THz probe disentangles the **Leggett mode** (relative interband phase oscillation between two condensates) from the **Higgs amplitude mode** in two-band MgB₂, using pump-pulse selectivity (multi-cycle vs single-cycle) and resonant ω/2ω enhancement. PHONONIC / DM Leggett-channel. [INCOMPLETE in index: extracted Leggett frequency / damping not captured from the math-heavy PDF.]

The framework's dark matter IS a Leggett-channel GGE quasiparticle — an inter-band coherence (relative-phase) mode, CPT-neutral and non-annihilating, with mass anchor `Mass_LeggettDM/Δ_BCS = 11.97` (knowledge MCP, LEGGETT-MOMENT-70; **CONDITIONAL on Γ_grav < H_0**). MgB₂'s Leggett mode is the canonical laboratory realisation of exactly that degree of freedom. Geometrically, the Leggett mode is the relative U(1) phase between two condensate sectors — in substrate language, the inter-sector coherence mode of the C² coset (the Leggett/Josephson *phase* channel, distinct from the Bogoliubov–Anderson *amplitude* channel on the same coset; `session-85-3b`). A THz-driven, selectively-excited Leggett mode *with measurable damping* gives a laboratory handle on the lifetime/spectral-function question for the substrate DM mode.

**Conflict flag (index vs canonical):** the index states "τ_DM = 4.93e82 s on the substrate side." The knowledge MCP returns **no `tau_DM` constant**, and the canonical DM-survival condition is the qualitative inequality **Γ_grav < H_0** (the CONDITIONAL tag on `Mass_LeggettDM_over_Delta_BCS`, and the open channel "Leggett mode gravitational decay lifetime Γ ~ m_L³/M_Pl²"). The specific `4.93e82 s` figure is **not canonical** — treat it as index-only and do not propagate it. The genuine carry-forward is to convert the MgB₂ Leggett *damping* into a universality-class bound on the inter-band-coherence decay channel the χ-inherited DM mode must satisfy (§V.5).

### II.7 — Penttilä (04): flat-band-ratio moderation of the geometric channel

**Result**: Within DMFT at finite T, the **flat-band ratio** and quantum metric remain good predictors of superconductivity *outside* the idealised isolated-flat-band + uniform-pairing limit; for non-isolated flat bands the zero-T superfluid weight together with the flat-band ratio is a good guideline for the BKT temperature. Recovers `D_s ∝` minimal quantum metric (bounded by Chern/winding) in the appropriate limit. GEOMETRIC / §VII.W + "flat bands squeeze less."

Penttilä supplies the lab observable that *quantifies* the flat-vs-dispersive partition — the flat-band ratio — and shows the superfluid response tracks it. Substrate-first: the Peter-Weyl sector structure of `D_K` determines an intrinsic flat-vs-dispersive partition (the (N₁,N₂,N₃,N₄) = (2,4,8,6) band split: acoustic singlet B1, flat optical B2 = the van Hove singularity, high sector B3; `baptista-operator-dk-tau.md`). The finding that the geometric channel remains predictive but is *moderated* by the flat-band ratio in non-isolated settings is the laboratory analog of the substrate's 37× acoustic dominance: the flat/geometric contribution is real but sub-dominant outside the idealised limit. Note the Chern/winding *bound* Penttilä recovers is a *lower* bound on the metric — consistent with the framework, where the topological invariants are zero and the metric floor is therefore the trivial bound, with the actual metric (`g = 982.5`) sitting far above it.

### II.8 — Luo (08): van-Hove-driven flat-band emergence — ARPES analog of the τ_fold transit

**Result**: High-resolution ARPES on AV₃Sb₅ (A = K, Rb, Cs) observes **four branches of flat bands spanning the entire BZ**, an emergence NOT anticipated by band-structure calculation and tied to the **evolution of van Hove singularities** (vHs at BZ boundary + Dirac cone at zone corner + intrinsic kagome flat band). GEOMETRIC / PHONONIC — van-Hove-fold transit.

The framework's cosmogenesis IS a supersonic transit (Mach 13.75; `c_fabric = 209.97 M_KK`) through a **van Hove fold** at `τ_fold = 0.190` — a first-order spectral-density reorganisation across a van Hove singularity, NOT a slow-roll inflation (`tau_fold = 0.190 PERMANENT van-Hove-cusp non-stationarity uniqueness theorem`). Luo is the laboratory demonstration that vHs *drive* flat-band emergence: as a control parameter crosses a saddle point, spectral weight reorganises into flat (high-DOS, geometric) structure. Substrate-first: the van Hove fold in the `D_K` spectrum is the parent event; AV₃Sb₅'s vHs-driven flat bands are an inheritance-child where the same DOS-reorganisation-at-a-saddle physics is ARPES-visible. Geometrically the saddle is a fold catastrophe (A₂, Thom-stable; `τ_min = 0.190158`, `d²λ/dτ² = 1.1757`; agent memory) — the same `A_2` singularity Berry's catastrophe-optics program classifies, here realised as a spectral-density divergence rather than a wave-intensity caustic. The material is doubly relevant: the emergent flat bands *also* carry the quantum-geometric superfluid weight of papers 01/04/07, linking the transit channel and the geometric channel in one family.

### II.9 — Peotta–Törmä review (07): the foundational definition of the bridge target

**Result**: The multiband superfluid weight `D_s` acquires a geometric contribution from the quantum metric, nonzero even for perfectly flat bands, with a **topological lower bound** (`D_s ≥` minimal quantum metric / Chern or winding). Flat-band `T_c` linear in interaction `U`; supercurrent interpreted via Wannier-function spread. GEOMETRIC / §VII.W — FOUNDATIONAL.

This is the load-bearing citation: the canonical definition + bound for the laboratory-IN element `R_geom = ∫_BZ Tr g_ab^{(P_0)}` that the HKR / `L_max → ∞` image of the finite-L Hochschild pairing `R_universal` lands on. It anchors the §VII.AF three-level ladder's laboratory-IN element as a *well-defined, bounded, geometry-controlled* observable. The central tension it states — a flat band's supercurrent comes *entirely* from geometry, not dispersion — is the substrate-side counterpart to "flat bands squeeze less": across the full spectrum the dispersive acoustic (B1) channel still dominates the geometric (B2/flat) one by ≈37×, but *within* the flat sector the supercurrent is purely geometric.

---

## III. Gate Verdicts

No gates fired in this sweep (literature index → synthesis). The canonical gates these papers bear on are already closed/PASS and are cited, not re-adjudicated:

| Gate (canonical, NOT re-run here) | Status | Decisive Number | Bears on paper(s) |
|:----------------------------------|:-------|:----------------|:------------------|
| §VII.AF.1.OP-PROJ (Pillar III↔IV bridge) | PERMANENT | Level-3/Level-2 r = 0.0950; margin 10.53× | 03, 06, 07, 09, 10 |
| `S87-W11-C5-LAB-FALSIFIER` (MCT-3 cohomology asymmetry) | PASS | 7.324992 (band 7.3250 ± 0.1%) | 05 |
| §VII.W-3.LAB (3rd cross-pillar calibration, rank-2 kernel) | PERMANENT (K=3) | 4-gate Class A NULL + Class B ratio | 05 |
| LEGGETT-MOMENT-70 (DM mass anchor) | PROVEN (CONDITIONAL Γ_grav<H₀) | Mass_LeggettDM/Δ_BCS = 11.97 | 02 |
| τ_fold van-Hove-cusp uniqueness | PERMANENT | τ_fold = 0.190; Mach = 13.75 | 08 |

---

## IV. Structural Implications

**The framework's strongest-evidenced bridge channel is now laboratory-saturated and structurally sharpened, not merely supported.** Three independent 2024–2026 results converge on the *exact* algebraic specification of `R_geom`:

1. **Projector choice confirmed (03).** The bridge's use of a BdG/superconducting-state projector `P_0` (rather than a normal-state band projector) is independently the physically-correct diamagnetic object. This *closes a latent ambiguity* in the §VII.W → §VII.AF anchor at the level of which metric the integrand uses — moving the choice from "framework convention" to "lab-confirmed."

2. **Non-Abelian trace is the algebra-correct object (06).** `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` is intrinsically non-Abelian and degenerate; the faithful integrand is the trace of the *non-Abelian* QGT `Tr[R_μν]`, not a sum of Abelian per-band metrics. This *strengthens* the bridge's structural footing: the framework was already using the trace form `Tr g_ab^{(P_0)}`, and paper 06 certifies that the trace-of-non-Abelian-metric is exactly the right object for a degenerate matrix fiber — with measured 20%/50% fractions proving it is substantial and extractable. It also *re-confirms* the metric-not-curvature reading: `Tr R_μν` (real symmetric part) is nonzero while the degenerate-set Chern number is zero — the condensed-matter realisation of the framework's "metrically rich, topologically trivial" (12 zero invariants, `g = 982.5` reservoir).

3. **Two-platform empirical anchor (09 + 10).** The integrated quantum-metric trace is measured to be real and dominant (Tanaka: stiffness > Fermi-liquid), on two platforms with two node structures (T² vs T-linear). The bridge's laboratory-IN element is platform-robust.

**No constraint-map state changes** (this is a sweep, not a compute session); the implication is that the §VII.W bridge's laboratory-IN element is on firmer ground than the registry currently annotates, and the carry-forwards below convert that into pre-registered cross-checks. The MCT-3 falsifier acquires a concrete experimental read-out template (05) and the τ_fold transit acquires an ARPES analog (08) — both *open new measurement adjacencies* without altering any verdict.

**One honest gap (sweep-acknowledged, not filled):** SW2 (FeSe NMR) and SW3 (¹⁷³Yb optical lattice, λ_8 / Γ_3B) returned only pre-window (2009–2022) seminal work; these channels are experimentally slower-moving and their load-bearing results predate the 2024–2026 window. Not filled from training knowledge (correct per sweep protocol). The DM-lifetime question (02) is similarly *not* canonically pinned to a number — the index's `τ_DM = 4.93e82 s` is uncanonical; the canonical condition is `Γ_grav < H_0`.

---

## V. Carry-Forward Computations

> Reviewer-author note: of these six, **V.1 and V.5 are the highest-EVOI** — V.1 because a one-script confirmation that the substrate `R_geom` integrand is built from the *BdG-state* (not normal-state) metric directly hardens the §VII.W → §VII.AF anchor a lab paper now independently demands; V.5 because the MgB₂ Leggett-damping bound is the first laboratory handle on the DM-mode lifetime question whose canonical status is currently only the qualitative `Γ_grav < H_0`. V.2/V.3/V.4 are bridge-robustness cross-checks; V.6 is a methodology guard.

### V.1 — Confirm the §VII.W integrand uses the BdG-state (quasihole) metric, not the normal-state metric

- **What**: Re-derive the `R_geom` integrand `Tr g_ab^{(P_0)}(k; τ_fold)` two ways — (a) with `P_0` = the BdG/superconducting-state projector (current convention), (b) with a normal-state band projector — on the `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` cache, and report `Δ = |R_geom^{BdG} − R_geom^{normal}| / R_geom^{BdG}`. Confirms Porlles–Chen (03): the diamagnetically-relevant metric is the BdG one.
- **Inputs**: `s86-hp1-cohomology-quantum-metric-bridge.md` (R_universal / R_geom definition); L_max=10 D_K spectrum cache (`s84_spectrum_cache_L12_tau019.npz`, filter to L_max=10); `tau_fold = 0.19`; canonical `A_K = ℂ⊕ℍ⊕M₃(ℂ)`; Provost–Vallée metric helper.
- **Gate**: feeds §VII.AF.1.OP-PROJ as a projector-choice confirmation sub-row. NEW gate `S100-VII-W-BDG-PROJECTOR-CONFIRM`: PASS if the BdG-projector integrand reproduces the canonical Level-3 = 0.0095% F₄ anchor AND the normal-state integrand does NOT (i.e. `Δ` exceeds the Level-2 envelope 0.10%, demonstrating the choice is load-bearing); INFO if `Δ < 0.10%` (choice is numerically immaterial at L_max=10); FAIL if the BdG integrand misses the canonical anchor.
- **Effort**: 3–4 hours, 1 agent session.

### V.2 — Non-Abelian vs Abelian metric-trace on the degenerate lowest band (paper 06 algebra check)

- **What**: On the 2-fold Kramers/J-degenerate lowest band of `D_K`, compute the geometric trace two ways: (a) non-Abelian `Tr[R_μν]` with `Q^{ij}_μν = ⟨∂_μ u_i|(1−P_k)|∂_ν u_j⟩` over the degenerate block (det-normalised U(deg) link), (b) the sum of per-band Abelian metrics. Report the fractional inter-band (i≠j) contribution `f_nonAb = (Tr R − Σ_n g_n)/Tr R`. Confirms Chen–Karki–Hosur (06) that `Tr R ≠ Σ` and quantifies the substrate's analog of their 20%/50% fractions.
- **Inputs**: L_max=10 D_K eigenvectors on the degenerate lowest band (non-Abelian Wilczek–Zee link machinery from BP-4 / S96 off-Jensen Chern script); `tau_fold = 0.19`; agent-memory note that single-band link gives gauge-noise `C ~ 0.78` (use as a negative control).
- **Gate**: NEW gate `S100-NONABELIAN-METRIC-FRACTION`: INFO-reporting `f_nonAb` with PASS if `f_nonAb > 0` (inter-band term is structurally present, confirming the non-Abelian object is the correct one) AND the imaginary part (non-Abelian curvature) integrates to Chern = 0 within `< 1e-12` (re-confirming metric-not-curvature); FAIL if `f_nonAb = 0` (degenerate fiber would reduce to Abelian, contradicting paper 06 and the matrix-algebra structure).
- **Effort**: 4–6 hours, 1 agent session (reuses the S96 non-Abelian FHS scaffold).

### V.3 — Thermal node-resolved `D^{geom}(T)` scaling cross-check against Hirobe (01)

- **What**: Give the substrate `R_geom` a thermal probe: compute `D^{geom}_μν(T)` from the band-resolved metric `g^{nm}_μν(k)` of `D_K` with a Fermi-factor weighting at the substrate gap scale, and classify the low-T power law (activated / `T^{1/l+1}` / `−T^{1/l+1} ln T`) against the substrate's flat-sector node structure. Tests whether the bridge object reproduces the *flat-band geometric* power law rather than the Fermi-liquid law.
- **Inputs**: band-resolved `g^{nm}_μν` on the L_max=10 cache; substrate gap scale `Δ_BCS`; node structure of the B2/flat sector (from `(2,4,8,6)` band split); Hirobe Eq. 8 form as the comparison template (methodological cross-check only, per substrate-first-canonical-sourcing).
- **Gate**: NEW gate `S100-RGEOM-THERMAL-SCALING`: PASS if the substrate `D^{geom}(T)` low-T exponent matches the flat-band geometric class (strictly weaker than the dispersive class) consistent with the 37× B1-acoustic dominance; INFO if the exponent is intermediate; FAIL if it matches the conventional Fermi-liquid law (which would contradict the bridge being a geometric object).
- **Effort**: 5–6 hours, 1 agent session.

### V.4 — Node-structure discriminant: substrate quantum metric vs MATBG-T² / MATTG-T-linear (papers 09/10)

- **What**: Determine which superconducting-gap node structure the substrate's projected quantum metric is consistent with (full gap / point node / line node), by reading the temperature exponent of `D^{geom}(T)` from V.3 and mapping it to the Tanaka(T²)/Banerjee(T-linear) discriminant. Report the substrate-predicted exponent and which of the two measured platforms it matches.
- **Inputs**: output of V.3; the Hirobe classification map (T² ↔ line-node or quadratic-point-node; T-linear ↔ flat-band-crosses-Dirac nodal); substrate sector geometry.
- **Gate**: feeds §VII.W laboratory-IN robustness. NEW gate `S100-NODE-DISCRIMINANT`: INFO-reporting the substrate-predicted node class + matched platform; PASS if the substrate exponent falls cleanly into one of the two measured classes (bridge object is platform-consistent); FAIL if it predicts a class (e.g. fully-activated `e^{−Δ/T}`) that neither measured platform shows AND that the substrate's own nodal structure forbids.
- **Effort**: 2–3 hours, 1 agent session (consumes V.3; mostly classification).

### V.5 — MgB₂ Leggett-damping → χ-inherited DM inter-band-coherence lifetime bound (paper 02)

- **What**: Extract the MgB₂ Leggett-mode frequency-to-gap ratio and damping rate from the on-disk PDF (`02_Yuan_*.pdf`; index marked these `[INCOMPLETE]`), then propagate the *universality-class* of laboratory Leggett damping through the χ inheritance morphism to bound the substrate DM inter-band-coherence decay channel. Compare against the canonical survival condition `Γ_grav < H_0`. **Do NOT use the index's uncanonical `τ_DM = 4.93e82 s`.**
- **Inputs**: `02_Yuan_*.pdf` (spot-verify via `read_arxiv_paper` arXiv 2412.13830 if the PDF refuses direct Read); canonical `Mass_LeggettDM_over_Delta_BCS = 11.97` (CONDITIONAL Γ_grav<H₀); open channel "Leggett mode gravitational decay lifetime Γ ~ m_L³/M_Pl²"; χ projection (M₃(ℂ)→0, the 3He-B inheritance morphism).
- **Gate**: feeds LEGGETT-GRAV-DECAY (the conditional under C11). NEW gate `S100-LEGGETT-DAMPING-INHERITANCE`: INFO-reporting the lab-derived damping universality class; PASS if the χ-inherited bound is consistent with `Γ_grav < H_0` (DM relic survives); FAIL if lab Leggett damping implies an inter-band-coherence decay faster than `H_0` under the inheritance map (would threaten the non-annihilation claim). First-extraction; carries `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` if only the universality class (not a number) lands.
- **Effort**: 4–5 hours, 1 agent session (PDF extraction + inheritance algebra).

### V.6 — MCT-3 ±l read-out template formalisation + Friedel-vs-cohomology guard (paper 05)

- **What**: Formalise Hou's `ρ ∝ [1+|α_l|²+2|α_l|cos(2lφ+φ₀l)]|ψ_l|²` ±l-interference form as the read-out modality for the MCT-3 Gate-2 cohomology-asymmetry test, and explicitly separate the substrate's predicted ±l asymmetry (ratio 7.324992 from `‖φ_67‖/‖φ_88‖`) from a Friedel-`Δ(r)`-driven 1:3:5→1:2:3 deviation. Output: a pre-registered signature distinguishing the two mechanisms in a ±l-resolved spectrum.
- **Inputs**: `inheritance-falsifier-protocol.md` (4-gate; `(Δ_B/Δ_A)^p` cancellation theorem); `lancaster-mct3-protocol-pre-registration.md`; Hou interference form (methodological template only); `S87-W11-C5-LAB-FALSIFIER` value 7.324992 + band [7.3177, 7.3323].
- **Gate**: feeds MCT-3 falsifier-row read-out spec (mack-cosmic-bridge sole writer of the §7 / falsifier-master-inventory surface — route the inventory annotation to mack-cosmic-bridge). NEW methodology-side gate `S100-MCT3-READOUT-TEMPLATE`: PASS if the ±l signature cleanly separates cohomology-asymmetry (ratio-specific, platform-robust under inheritance) from Friedel-`Δ(r)` (extreme-quantum-limit artefact); INFO if separable only with additional pressure-slope data (Gate-4 dependence).
- **Effort**: 3–4 hours, 1 agent session (methodology + inheritance-protocol formalisation; no heavy compute).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Porlles–Chen (03): diamagnetic metric = quasihole/BdG-state metric | GEOMETRIC / §VII.W | Lab-confirms `P_0` BdG-projector choice | Closes latent projector ambiguity in §VII.W→§VII.AF anchor |
| 2 | Chen–Karki–Hosur (06): non-Abelian `Tr[R_μν]` for degenerate fiber; 20%/50% fractions | GEOMETRIC / §VII.W | Algebra-correct object for `A_K=ℂ⊕ℍ⊕M₃(ℂ)` | Certifies trace-of-non-Abelian-metric; re-confirms metric-not-curvature (Chern=0) |
| 3 | Tanaka (09, T²) + Banerjee (10, T-linear): geometry-dominated stiffness, two platforms | PHONONIC / §VII.W Level-3 | Measured anchor real & dominant | Bridge laboratory-IN element platform-robust |
| 4 | Hirobe (01): node-resolved `D^{geom}(T)` scaling table | PHONONIC / §VII.W | Thermal falsifier of the bridge object | Flat-vs-dispersive separation echoes 37× B1 dominance + gives sign test |
| 5 | Hou (05): ±l phase-resolved CdGM + 1:3:5→1:2:3 tunability | PARTICLE / PHONONIC — MCT-3 | Experimental template for `S87-W11-C5` (7.324992) | ±l read-out + demonstrated ratio measurability; Friedel-vs-cohomology guard needed |
| 6 | Yuan (02): MgB₂ THz Leggett-mode selective excitation + damping | PHONONIC / DM Leggett-channel | Lab anchor for DM inter-band-coherence lifetime | Index `τ_DM=4.93e82 s` UNCANONICAL — canonical is `Γ_grav<H₀` |
| 7 | Penttilä (04): flat-band-ratio moderates geometric channel | GEOMETRIC / §VII.W | Lab quantifier of flat-vs-dispersive partition | Echoes 37× acoustic dominance outside idealised limit |
| 8 | Luo (08): vHs-driven flat-band emergence, AV₃Sb₅ ARPES | GEOMETRIC / PHONONIC — van-Hove fold | ARPES analog of τ_fold transit (A₂ fold) | Links transit channel + geometric channel in one material family |
| 9 | Peotta–Törmä (07): foundational `R_geom` definition + topological bound | GEOMETRIC / §VII.W FOUNDATIONAL | Load-bearing laboratory-IN definition | Anchors §VII.AF three-level ladder laboratory-IN element |
| 10 | SW2 (FeSe NMR) / SW3 (¹⁷³Yb) recency gap | — | Honest gap, NOT filled from training knowledge | Channels experimentally slower-moving than the 2024–2026 window |
