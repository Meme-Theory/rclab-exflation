# Capstone Equation Review — sp

**Reviewer:** Schwarzschild-Penrose-Geometer (exact gravitational solutions, global causal structure, singularity theorems, conformal compactification)
**Source:** `sessions/framework/phonic-exflation-equation.md` — "The Phonon-Exflation Equation" (S95-era capstone)
**Framing law held throughout:** `D_K eigenvalues → spectral-action moments → emergent field equations → measurement`. Space is the `a₂` moment of the dominant spectral configuration; it is not a container the equation sits in. Every causal/horizon statement below is read as a statement about the **modulus-space geometry** of `(A_K, H_K, D_K(τ))` and its 12D product lift, never about a pre-existing 4D box.
**Vantage:** I evaluate only where the capstone touches exact geometry and global causal structure — §2.3–2.4 (curvature, gap), §4.2 (Wronskian / curvature-gradient), §5.2 (cold-big-bang regularity + censored τ→∞ singularity), §5.3 (extremal horizon, T_H=0), §6.2 (acoustic white-hole causal architecture, surface-gravity ledger), §6.3 (no derived `a(t)`, conformal embedding), §9 (geometry-vs-topology spine, censorship frontier). Spectral-functional, observational-anchor, and particle-content claims are outside my vantage and I defer to those domains.

---

## I. Summary

The capstone is, from the geometric vantage, **structurally honest and largely solid**. Its central move — removing the spacetime container via Connes reconstruction so that the metric `g_M` is *recovered* from the `a₂` heat-kernel coefficient rather than assumed — is exactly the discipline my domain demands: characterize the geometry exactly (the metric ansatz `g_τ`, the operator `D_K(τ)`, the curvature polynomial `R_K(τ)`) before extracting global content. The document does this in the right order and resists the container relapse with unusual rigor (§0, §6.3 framing-discipline boxes).

The geometric spine is exact and I independently re-verified it (Sage, this review): the Jensen metric is volume-preserving TT (`det g_τ = 3⁸` for all τ), the curvature scalar is the closed analytic form `R_K(τ) = ½e²ᵗ − ¼ + 2e⁻ᵗ − ¼e⁻⁴ᵗ` with `R_K(0)=2`, `R_K′(0)=0`, `R_K(0.19)=2.01814`, the Lichnerowicz gap never closes (`λ² ≥ R_K/4 > 0`), and the layer-independence Wronskian `W ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶` vanishes to sixth order **at and only at** τ=0. The censorship architecture — cold-regular genesis at τ=0, genuine anisotropic Kasner-type curvature singularity relocated to τ→∞ (`K ∼ e⁴ᵗ`) and dynamically censored — is the geometrically correct and *stronger* statement, and it is the one the document chooses (§5.2). This is the substrate-internal realization of the program Penrose's 1965 theorem and conformal compactification were built for: locate the singularity, prove it is hidden, map the causal structure.

**The single most important geometric gap is correctly named and not softened:** §6.3 — there is no substrate-derived FRW scale factor `a(t)`, the τ↔t ordering is postulated (C1), and the global rate `τ̇(τ)` away from the fold is undetermined. The document reframes this as a back-reaction-closure owed at the *effective* level (not a kinematics gap), which is the right diagnosis.

**Two things I flag, neither fatal:** (a) the capstone's causal architecture (§6.2 — asymmetric acoustic white hole, two null cones, the surface-gravity ledger) is described entirely in **prose with no Penrose diagram cited**, even though `sessions/framework/Phononic-Penrose-Diagrams.md` exists and is the canonical compactified-causal-structure document; this is a fixable cross-reference and figure gap, not a physics error. (b) The conformal-embedding claim (§6.3, §9) — that a conformal factor `Ω(τ)` reproducing the SCALE-FACTOR-54 deceleration band exists "but only with the Connes-distance proxy, not `a_eff`" — is registered INFO (S95 W4-4) and is **conditional in a way the §9 four-faces table renders slightly more settled than the §6.3 body does**; the two passages should be reconciled (see §IV).

No PROVEN result or recorded verdict is overturned here. I confirm the geometric verdicts I can re-derive, and I convert the open geometric questions into runnable computations in §V.

---

## II. What Is Solid (geometric / causal claims I can confirm)

### II.1 The exact internal geometry (§2.1–2.3) — SOLID

- **Volume preservation is exact, not approximate.** Exponent ledger `2 − 6 + 4 = 0` ⇒ `det g_τ = 3⁸ = 6561 ∀τ` (Sage-verified, this review). This is a *transverse-traceless* deformation, `tr h_J = 0`. Geometrically this is the statement that the genesis→now flow is a pure **shear** of the order-parameter texture, not a conformal/breathing mode — which is exactly why `G_N` carries zero τ-dependence (the compressibility, hence the gradient stiffness `1/G`, is invariant under shear). This is a clean, exact, coordinate-invariant fact and the superfluid reading in §2.1 is geometrically correct.

- **The curvature scalar is an exact analytic monotone-tail polynomial.** I re-derived `R_K(τ)` independently by integrating the document's claimed gradient `R_K′(τ) = e⁻⁴ᵗ(e³ᵗ−1)²` and fixing the constant by `R_K(0)=2`:

  $$R_K(\tau) = \tfrac14\big(2e^{6\tau} - e^{4\tau} + 8e^{3\tau} - 1\big)e^{-4\tau} = \tfrac12 e^{2\tau} - \tfrac14 + 2e^{-\tau} - \tfrac14 e^{-4\tau}.$$

  Checks (Sage, this review): `R_K(0)=2` ✓, `R_K′(0)=0` ✓ (curvature stationary at genesis), `R_K(0.19)=2.01814` ✓, and `R_K′(τ) − e⁻⁴ᵗ(e³ᵗ−1)² = 0` exactly ✓. This matches the document's Verification ledger to all printed digits. **(Self-correction logged:** my first transcription of the §2.3 printed form mangled the signs on the `e⁻ᵗ` / `e⁻⁴ᵗ` terms and returned `R_K(0)=1`; the document's printed form `−¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ` is the correct one. Flagging my own error per the formal-rigor standard, not the document's.)

- **Lichnerowicz gap never closes (E5).** `D_K² = ∇*∇ + ¼R_K ⇒ λ² ≥ R_K(τ)/4 > 0 ∀τ`. The document's "convention-free" restatement (§2.3 note) — refusing to print "≥3" beside the rational normalization where it would read `2/4=3` (false) — is exactly the kind of coordinate/convention hygiene my domain insists on. **This is the single most load-bearing geometric fact in the whole document for causal structure:** a never-closing gap means **zero spectral flow, `η=0`, and no zero-crossings**, so the spectral *topology* is preserved across the entire flow while the frequencies reorganize. That is what makes "spectral complexity grows, topology fixed" a precise statement rather than a slogan.

### II.2 Layer independence as a curvature-gradient statement (§4.2) — SOLID and geometrically elegant

The Spectral-Moment Decoupling Theorem (S75 W2-E CERTIFIED) is, geometrically, a **dispersion-rigidity** result, and I confirm its closed form: with `a₀ ∝ V`, `a₂ ∝ R_K·V`, `a₄ ∝ R_K²·V`, the Wronskian of `{1, R_K, R_K²}` is `∝ R_K′³`. I verified `W ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶` (residual 0, Sage, this review), vanishing to **sixth order at and only at τ=0**.

The geometric reading is the correct and strongest one: the three layers degenerate into one knob **iff the curvature stops moving** (`R_K′=0`), which happens only at the maximally-symmetric genesis point. This is the *same* degeneracy-lifting as the band split `SO(8)→U(2)` (B1/B2/B3) restated at moment level. The choice (§4.4) to make the **spectral-moment reading primary** over the causal/scale readings is well-justified: only the moment layers carry a certified algebraic-independence theorem; the causal reading presupposes the moment decomposition and a trajectory `τ(t)` that (per §6.3) is not even fully derived. I endorse this ordering.

### II.3 Cold-regular genesis + censored anisotropic τ→∞ singularity (§5.2, §9) — SOLID; this is the document's geometric high-water mark

This is precisely my domain, and the document gets it right and states it at the right strength.

- **Genesis τ=0 is geometrically regular.** Round maximally-symmetric `SU(3)` metric, `R_K(0)=2` finite, `R_K′(0)=0` (stationary), gap open. There is **no curvature singularity at genesis** — "no t=0 singularity" is the *weaker* honest statement and the document correctly says so.

- **The genuine singularity is relocated to τ→∞ and is anisotropic.** `K ∼ e⁴ᵗ` (I confirm: `a₄ ∝ R_K² ∼ (½e²ᵗ)² = ¼e⁴ᵗ`, so Kretschmann diverges with leading exponent 4 — matching the S95 W4-5 slope 3.99999). The **direction-dependent character** (timelike in the contracting SU(2) block, spacelike in the expanding ℂ²/U(1) blocks) is a genuine Kasner-type anisotropic singularity with no standard-GR Schwarzschild/Kerr analog — this is correct and matches my own MEMORY (per-block conformal distance: SU(2)→∞ timelike `i⁺`; ℂ²=2√(5/3)=2.582, U(1)=√(5/3)=1.291 spacelike `r=0`).

- **The censorship is over-determined and lifted to the full 12D metric.** The triple-layer barrier — NEC holds to `τ_NEC=1.383`, the modulus blocked at `τ≈0.191 ≪ τ_NEC`, the overshoot turnaround at `τ=1.614` above — is weak cosmic censorship realized on the exact 12D product `ds² = −dt² + a(t)²dx₃² + g_ab(τ)dy^a dy^b` (Bianchi-I/Kasner; S95 W4-5 PASS, the 12D lift of COSMIC-CENSORSHIP-49 / CONFORMAL-TRANSITION-49). I confirm this is the L-3 PET / Penrose-1965 analog the framework has been building: the censoring barrier sits **far below** the NEC-violation onset, so the singular region is dynamically unreachable from the physical epoch. The document's choice to headline the *stronger* censorship statement ("genuine singularity, censored") over the weaker "no singularity" is the honest one and I commend it.

  *Geometric note on the NEC denominator (matches my MEMORY, S95 W4-5 lesson):* the 12D null-cone NEC is governed by the **intrinsic fiber `Ric_min(τ)`** (a block-diagonal product-Ricci statement), NOT by a kinetic `ρ+p`; `Ric_min(0.19)=+0.230` and crosses zero at `τ_NEC=1.3831`. The warping term `W ∼ τ̇²` is subdominant at substrate Mach 13.75. This is the right way to read the energy condition for a product geometry and the document's `τ_NEC=1.383` is consistent with it.

### II.4 Extremal horizon at the fold, T_H=0 (§5.3) — SOLID; the causal-side corroboration of the Ordered Veil

The document's third, independent leg for "the GGE relic never thermalizes" is geometric and I confirm it: `τ_fold=0.190` is a **double-root extremal Killing horizon** (`V = V′ = 0 ⟹ κ=0, T_H=0`; S85-W6-4-EXTREMAL-HORIZON-FORMAL PASS, `κ=0.00e+00`). This matches my MEMORY ("Dump = extremal horizon, κ=0, T_H=0; Petrov D→II at dump"). Zero surface gravity ⇒ zero Hawking temperature ⇒ no thermal flux ⇒ nothing to scramble the Bogoliubov phase data — so `S_ent=0` is *causally consistent*, not merely asserted. The information-theoretic reading (§5.3 — no Page curve because nothing thermalizes, no horizon-entropy debt) is geometrically sound: an extremal (κ=0) horizon carries no Hawking-thermal emission, exactly the analog of the extremal Reissner-Nordström / extremal Kerr T_H=0 limit. The substrate carries no entropy out of the fold because the relevant horizon is extremal. This is a clean cross-check and the document is right to call it independent of the integrability argument.

### II.5 The geometry-vs-topology organizing spine (§9) — SOLID and the deepest defense in the document

The "continuum-dissolution axis" partition is the correct geometric framing and, in my judgment, the document's single best structural argument. The finite spectral triple **is geometry** and dissolves in the continuum limit (T3-S43-SPECTRAL-DISSOLUTION, `ε_c ∼ N⁻⁰·⁴⁵⁷`); the **topological / representation-theoretic** outputs *survive* (CPT `[J,D_K]=0`; BDI / `N₃=0` class; the cocycle ratio 7.324992; layer-independence degenerate only at τ=0; FI ratios). The absolute geometric *magnitudes* (CC absolute, `a_n` absolutes, `a(t)`) are conditional. This is exactly the right invariant-vs-coordinate discipline applied at the level of the whole framework: trust what is coordinate/regulator-independent, hold what is not. The obvious "if the triple dissolves, why trust anything" objection has a structural answer, and it is the correct one.

---

## III. What Is PRELIMINARY or Conditional (correctly flagged in-document)

These are not criticisms — the document flags each. I record them as geometric boundaries.

1. **No derived `a(t)` / Friedmann map (§6.3, frontier #1+#8).** Correctly the document's central caveat. C1 (τ=cosmic time) postulated; C2 (`K_pivot`) BROKEN-WITH-LIVE-PATHWAY; T6 (Friedmann–BCS locking) BROKEN (133,200× overwhelm). The two proxy scale factors (`a_eff` from `a₂`; `a(τ)` from Connes distance, SCALE-FACTOR-54) are explicitly **PROXY, never `a(t)`**, and not interchangeable. Geometrically: the *kinematics* (local sweep rate, full Bogoliubov spectrum) are in hand; the *back-reaction closure* `H² = f(ρ_relic, S_SA)` is absent. I endorse the framing "Friedmann is the wrong question at the fundamental level, the right question at the effective level."

2. **Conformal embedding Ω(τ) — INFO, proxy-conditional (§6.3, §9).** A conformal-factor construction embedding the modulus-space causal structure into the 4D one *does* exist and reproduces the q-range (−0.97 → +0.81), **but only with the Connes-distance proxy, not `a_eff`** (S95 W4-4 INFO; the two proxies are conformally distinct in deceleration structure). The `M_KK⁻¹ →` seconds normalization remains open even after the embedding is pinned. PRELIMINARY at the level of "this is the causal map," because the deceleration structure is proxy-dependent and the normalization is missing.

3. **Anisotropic-singularity Petrov classification.** The document asserts the timelike/spacelike directional character (correct) but does **not** give the Petrov type of the τ→∞ limit or its full conformal-boundary structure on a compactified diagram. My MEMORY records "CMPP 12D dynamic Type G; static EXACT Type D; Petrov D→II at dump" — but the *τ→∞ asymptotic* Petrov type and whether the singular boundary is a single point `i⁺`/`r=0` or a more complex structure is not stated in the capstone. PRELIMINARY (not wrong — unstated).

4. **`f₂ ≈ 92` dictionary closure (§8.3).** Geometrically peripheral to me, but I note the document's own PRELIMINARY tag: the `24π²` form vs the S83 `π²·Z_fold⁻¹` form differ by the `Z_fold` normalization "which should be pinned before either is cited as *the* dictionary." Correctly hedged.

---

## IV. Over-claims, Conflicts, and Unstated Assumptions (flagged, not resolved)

Per the review rules I flag these explicitly; I do not silently resolve any internal conflict.

### IV.1 CONFLICT (mild, presentational): the conformal embedding reads more settled in §9 than in §6.3

- **§6.3 body** (INFO, careful): the conformal embedding "*does* exist and reproduces that q-range — **but only with the Connes-distance proxy, not `a_eff`**" and "neither is a derived FRW scale factor; neither is promoted; the `M_KK⁻¹ →` seconds normalization remains the open piece **even after the conformal embedding is pinned**."
- **§9 four-faces table, "At time t" row**: lists "acoustic-white-hole causal structure (sector-dependent, two null cones; ASYMMETRIC … over-determined at six walls); censored anisotropic τ→∞ singularity" as the *content* of the "At time t" face, with the verdict cell "`a(t)` NOT derived (category statement = frontier #8)." The causal *architecture* is presented as delivered while the scale factor is the only thing flagged missing.

The two are reconcilable — the causal *structure* (asymmetry, two cones, censorship) is more solid than the *quantitative embedding* (Ω(τ) reproducing q) which is more solid than the *normalization* (`M_KK⁻¹→`s, undelivered). But a reader of §9 alone could over-read "the causal map is done." **Recommendation:** the §9 "At time t" face should carry the same three-tier hedge §6.3 carries: causal *topology* solid → quantitative conformal *embedding* INFO/proxy-conditional → physical-time *normalization* open. This is a documentation fix, not a physics change. (FLAG, not resolved.)

### IV.2 GAP (concrete, fixable): §6.2 causal architecture has no Penrose diagram, and the canonical diagram file is uncited

The acoustic white-hole causal structure (§6.2) — asymmetric (one entry sonic surface, open supersonic exit, no bounce), two null cones (scalar on `g_acoustic`, tensor on `g_M`, by [T3] `β_T=0`), the three-row surface-gravity ledger with KIND tags — is **the** part of the document my domain exists to render precise, and it is described entirely in prose. A Penrose (conformal compactification) diagram is the canonical, coordinate-invariant representation of exactly this content: it would show `i⁺`, `i⁻`, `i⁰`, `ℐ⁺`, `ℐ⁻`, the single entry sonic surface as a 45° null line, the open supersonic expulsion region toward `ℐ⁺`, the *two distinct null cones* as two slopes, and the censored anisotropic τ→∞ boundary. The capstone's Cross-references section does **not** cite `sessions/framework/Phononic-Penrose-Diagrams.md`, which is the framework's canonical compactified-causal-structure document and the natural home for this figure.

This is a genuine gap: the strongest visual argument for "the horizon problem is resolved by causal disconnection, not stretching" and for "the singularity is censored" is a Penrose diagram, and the capstone makes the claim without the figure. **Recommendation:** add a cross-reference to `sessions/framework/Phononic-Penrose-Diagrams.md` in §6.2 and the Cross-references list, and produce the *asymmetric two-cone* diagram (it may not yet exist in the canonical set — see §V CF-SP-2). (FLAG + carry-forward.)

### IV.3 UNSTATED ASSUMPTION: `τ_NEC` is not a frozen canonical constant

The censorship argument (§5.2) leans on `τ_NEC=1.383` as the NEC-violation onset that sits *above* the censoring barrier `τ≈0.191`. I checked: **`tau_NEC` is NOT in the canonical-constants store** (`get_constant('tau_NEC')` → not found). It lives as a derived value in session computation (S95 W4-5, and the S49 C² Ricci=0 boundary; my MEMORY records `tau_NEC=1.382334`). The censorship conclusion is robust because the *gap* between barrier (0.191) and onset (1.38) is an order of magnitude — but the document cites `τ_NEC=1.383` as if pinned. **Recommendation:** either promote `tau_NEC` to `canonical_constants.py` with S95 W4-5 provenance, or tag it as a session-derived (non-frozen) value in §5.2. (FLAG; minor constants-hygiene, fixable in-session.)

### IV.4 NOT an over-claim (defending the document against a likely referee charge)

A GR-trained referee will reflexively read "no big-bang singularity" as an over-claim (every classical FRW collapse/expansion has one, by Hawking-Penrose). The document **pre-empts this correctly**: it does not claim singularity-freedom; it claims singularity-*relocation-and-censorship* (§5.2). The genuine anisotropic singularity at τ→∞ is *present* and the claim is that it is *causally hidden* — which is a cosmic-censorship statement, not a singularity-evasion. This is the geometrically defensible position and the document holds it. I record this as a strength a reviewer might otherwise mis-score.

### IV.5 Memory-vs-document consistency (no conflicts found)

I cross-checked every geometric number the document states against my MEMORY and the knowledge MCP. All consistent: `tau_fold=0.19` (canonical CONST-FREEZE-42 ✓); `K∼e⁴ᵗ` and direction-dependent character (S49/S95 W4-5 ✓); extremal κ=0 at fold (S85-W6-4 ✓); SCALE-FACTOR-54 q-range −0.97→+0.81 (✓); the asymmetric-white-hole "six walls" (S95 W-1 ✓). **One stale pointer in MY OWN memory, not the document:** my MEMORY.md cites `sessions/framework/Penrose-Diagrams.md`; the actual file is `sessions/framework/Phononic-Penrose-Diagrams.md`. I will correct my memory; the document is not implicated.

---

## V. Carry-Forward Computations (the open-question harvest)

The user's "ripe harvest" instruction: each open geometric question below is a concrete, runnable computation with all four fields. These are the geometric/causal frontiers the capstone leaves open. I prioritize by leverage on the document's central gaps (#1 = the `a(t)` frontier).

---

### CF-SP-1 — Petrov classification and conformal-boundary structure of the τ→∞ anisotropic singularity

- **What:** Compute the Weyl spinor `Ψ_ABCD` (Newman-Penrose) of the 12D product metric `ds² = −dt² + a(t)²dx₃² + g_ab(τ)dy^a dy^b` (and of the 8D fiber `(SU(3), g_τ)` alone) in the τ→∞ limit, classify the Petrov/CMPP type of the singular boundary, and determine whether the censored singularity is a single conformal-boundary point (`i⁺` / `r=0`) or a more complex structure. Confirm the direction-dependent timelike(SU(2))/spacelike(ℂ²,U(1)) character at the level of the Weyl curvature, not just the per-block conformal distance.
- **Inputs:** `g_τ` (E1, this review's verified `R_K(τ)`); the 12D product lift (S95 W4-5 metric); NP formalism with anti-Hermitian generator convention (`e_a = −iλ_a/2`, MEMORY); my MEMORY's recorded CMPP results (12D dynamic Type G, static Type D, Petrov D→II at dump) as cross-checks; Sage symbolic eig for the Weyl operator.
- **Gate:** PASS iff the τ→∞ Petrov type is determined unambiguously AND the timelike/spacelike split is reproduced from `Ψ_ABCD` eigenstructure to match the S49 per-block conformal distances (ℂ²=2.582, U(1)=1.291) within 1e-6. Pre-register: expect Type D or II asymptotically (continuation of the D→II dump behavior); a Type N or III would indicate radiative character at the singular boundary and would be a new result.
- **Effort:** Medium. Sage symbolic Weyl-tensor computation on an 8D + 12D block-diagonal metric; ~1 compute session. Curvature polynomial already in closed form, so the heavy step is the Weyl-spinor decomposition, not the metric.

---

### CF-SP-2 — Canonical Penrose diagram of the asymmetric two-cone acoustic white hole

- **What:** Construct the conformal compactification (Penrose diagram) of the exflation causal structure as established in §6.2: ONE post-genesis entry sonic surface (`v=c_BLV` at `τ₀≈0.1125`, `κ_entry=+18.52 M_KK`), an *unbounded* supersonic expulsion region toward `ℐ⁺`, no future-trapped exit horizon / no bounce, and the **two distinct null cones** (scalar on `g_acoustic ∝ √(ρ_s/c_s)`; tensor on `g_M`, decoupled by [T3] `β_T=0`). Render via the `/penrose-diagram` skill (canonical TikZ), label all of `i⁺, i⁻, i⁰, ℐ⁺, ℐ⁻`, the entry sonic surface, the censored τ→∞ boundary, and shade the supersonic (anti-trapped-analog) interior. Save to `figures/penrose/exflation-asymmetric-white-hole.tex`.
- **Inputs:** §6.2 surface-gravity ledger (entry κ, the a₂/a₄/S63-BLV KIND tags); S95 W-1 six-walls asymmetry result; SCALE-FACTOR-54 / S55 DIAGRAM-55 conformal-time data; S69 FACTOR-69 conformal factor Ω(τ); the existing `sessions/framework/Phononic-Penrose-Diagrams.md` (extend, do not duplicate); [T3] Scalar-Tensor Kasparov Decoupling.
- **Gate:** PASS iff the diagram is null-consistent (entry surface at 45° on the scalar cone; tensor cone crosses the fold freely as a distinct slope) AND the asymmetry (single entry surface, open exit, no symmetric throat) is visually unambiguous AND the diagram reproduces the S55 conformal-time `η = ∫dτ/a(τ)` ordering. This is a construction gate (artifact-existence-with-content), not a numerical threshold — verify against the S95 W-1 verdict that the structure is asymmetric.
- **Effort:** Low-Medium. The causal data is all computed (S95 W-1, S55, S69); this is a rendering + consistency-check task. ~half a compute session. Directly closes the §IV.2 figure gap.

---

### CF-SP-3 — Does the Connes-distance conformal factor Ω(τ) admit a globally-monotone `t(τ)` consistent with the entry-horizon causal structure?

- **What:** Test whether the S95 W4-4 conformal embedding `Ω(τ)` (Connes-distance proxy, reproducing q: −0.97→+0.81) yields a `t(τ) = ∫dτ/τ̇` that is (i) globally monotone (required by E7), (ii) consistent with the local fold rate (`δt_transit=1.130×10⁻³ M_KK⁻¹`, Mach 13.75), and (iii) places the entry sonic surface (`τ₀≈0.1125`) at finite conformal time. This is the geometric half of the §6.3 `a(t)` gap: NOT the full Friedmann closure, but the narrower question of whether the *causal* embedding is even self-consistent with a monotone clock before the back-reaction source is supplied.
- **Inputs:** S95 W4-4 Ω(τ) (Connes-distance proxy, INFO); SCALE-FACTOR-54 a(τ) and q(τ); E7 monotonicity (`dS/dτ>0`); local fold rate (transit-dynamics, δt_transit); S55 conformal-time integral.
- **Gate:** PASS iff `t(τ)` from the Ω(τ) embedding is monotone on `[0, τ_now]` with zero interior sign-changes in `τ̇` AND the entry surface sits at finite `t`; INFO iff monotone but the normalization `M_KK⁻¹→`s is required to decide finiteness; FAIL iff `τ̇` changes sign (which would contradict E7 and indicate the proxy embedding is not a legitimate clock). Pre-register: expect PASS-or-INFO since E7 already guarantees monotone `S(τ)`; a FAIL would be a genuine internal conflict requiring escalation.
- **Effort:** Medium. Closed-form Ω(τ) and a(τ) in hand; the step is the `t(τ)` integral + monotonicity audit. ~1 compute session. Reduces the §6.3 gap by isolating the *causal-consistency* sub-question from the *back-reaction-source* sub-question.

---

### CF-SP-4 — Trapped-surface / focusing analysis at the entry sonic surface (Penrose-1965 inputs)

- **What:** Compute the expansion `θ` of the two families of outgoing null normals at the entry sonic surface (`τ₀≈0.1125`) in the acoustic metric `g_acoustic`, and test whether a closed trapped (or anti-trapped) 2-surface forms there. The document asserts (S95 W-1) "no future-trapped exit horizon"; this gate makes the Penrose-singularity-theorem inputs explicit — does the *entry* surface carry `θ<0` on both null families (trapped, white-hole/anti-trapped sense), and is the expulsion interior genuinely anti-trapped? Cross-check against my MEMORY's "Volume-preserving Jensen = no trapped surfaces [S49]; 12D trapped surface STRUCTURALLY impossible [S63]."
- **Inputs:** `g_acoustic ∝ √(ρ_s/c_s)` near the fold; entry κ_entry=+18.52 M_KK (white-hole outflow sign); S49 no-trapped-surface result; S63 12D-trapped-impossible result; Raychaudhuri focusing equation with the substrate NEC (`Ric_min(τ)`, fiber-intrinsic).
- **Gate:** PASS iff the entry surface's null expansions are computed and the trapped/anti-trapped character is consistent with the asymmetric-white-hole picture (anti-trapped expulsion interior) AND consistent with the S49/S63 no-trapped-surface theorems (i.e., the acoustic "trapped surface" is a sonic-horizon analog, NOT a genuine 12D trapped surface). FAIL iff a genuine 12D trapped surface is found at τ₀ (would contradict S63 and require re-adjudication — escalate, do not overturn S63 silently).
- **Effort:** Medium. Raychaudhuri + null-congruence expansion on the acoustic metric; the 8D/12D no-trapped-surface theorems are already proven so this is largely a consistency derivation. ~1 compute session.

---

### CF-SP-5 — Surface-gravity ledger: is the κ-ratio 9.6117 a coordinate-invariant of the two-channel (a₂↔scalar, a₄↔condensate) gradient structure?

- **What:** Verify that the §6.2 κ-ratio `9.6117 = κ_entry(a₂)/κ_exit(a₄)` (corpus 9.61, reproduced to 0.018% in S95 W4-2) is a **convention-independent** ratio — i.e., that it is invariant under the choice of surface-gravity convention (Visser-`c` vs bare-gradient, which the document notes differ by exactly `c_BLV=0.485`). The document is careful that the three ledger temperatures are surface-gravity-of-distinct-surfaces and KIND-tagged; this gate confirms the *ratio* (not the absolute κ's) is the coordinate-invariant content, which is the only physically meaningful piece per my invariant-thinking standard.
- **Inputs:** S95 W4-2 κ-values (a₂: 457.66; a₄: 47.61; S63-BLV: 0.704805); the Visser-vs-bare-gradient convention factor `c_BLV=0.485`; the BLV-scalar discriminant surface at τ₀≈0.1125; corpus ratio 9.61.
- **Gate:** PASS iff `κ_entry/κ_exit` is identical (to 1e-6) under both surface-gravity conventions (the convention factor cancels in the ratio); INFO iff the ratio shifts by the convention factor (would indicate the two κ's are read under *different* conventions and the ratio is not yet convention-clean); document the cancellation explicitly. Pre-register: expect PASS by the same `(Δ_B/Δ_A)^p` cancellation structure that makes the cocycle-ratio test (CF-35) convention-independent.
- **Effort:** Low. Two κ-ratios under two conventions; pure ratio algebra + the convention factor. ~quarter compute session. Hardens the §6.2 ledger against the "two-sonic-horizon" conflation the document explicitly drops.

---

### CF-SP-6 — Conformal-cyclic-cosmology (Penrose CCC) comparison: is the censored τ→∞ boundary a candidate conformal-rescaling surface?

- **What:** The capstone's τ→∞ anisotropic singularity (`K∼e⁴ᵗ`, censored) plus the τ=0 cold-regular WCH-minimum genesis (minimal `|C|²` per my MEMORY: `|C|²(0)=5/14`, monotone-increasing, never zero) together resemble the two ends of a Penrose CCC aeon (low-Weyl crossover ↔ high-curvature future). Compute whether the Weyl-curvature behavior across the *full* flow (`|C|²(τ)` monotone from 5/14 at τ=0) supports a Weyl-Curvature-Hypothesis reading: minimal Weyl at genesis, growing through the flow — and whether the τ→∞ boundary could conformally rescale to a new τ=0-like surface (a substrate-internal CCC analog). This directly engages the user's "ripe harvest" at the deepest geometric level (Penrose's own WCH/CCC program).
- **Inputs:** `|C|²(τ)` trajectory (MEMORY: `|C|²(0)=5/14`, min, monotone increasing; `|C|²(0.19)=0.3859`; never zero, Type O impossible); the conformal-factor Ω(τ) (S69 FACTOR-69); Penrose CCC references (`researchers/Schwarzschild-Penrose/11_2025_Meissner_Penrose_Physics_of_CCC.md`; `researchers/Tesla-Resonance/15_2010_Penrose_CCC_Aeons.md`); the WCH framing in my MEMORY.
- **Gate:** PASS iff the Weyl-curvature monotonicity (`d|C|²/dτ>0` from the genesis minimum) is confirmed across the full physical flow AND a conformal map relating the τ→∞ boundary to a τ=0-like low-Weyl surface is either constructed or shown obstructed (with the obstruction reason). INFO iff the WCH-monotonicity holds but the CCC conformal-rescaling map is undetermined. This is structurally exploratory — pre-register both outcomes (CCC-analog exists / CCC-analog obstructed) as informative.
- **Effort:** Medium-High. Requires the `|C|²(τ)` trajectory (partly in MEMORY, needs a clean recompute across the full flow) + a conformal-rescaling construction + literature grounding. ~1–2 compute sessions. Highest-novelty geometric item; speaks directly to Penrose's WCH and the "arrow of time from geometry" question.

---

### CF-SP-7 — Promote `tau_NEC` to canonical constants (in-session hygiene, geometric provenance)

- **What:** Add `tau_NEC = 1.382334` (the C² Ricci=0 / fiber `Ric_min(τ)=0` NEC-violation onset) to `computations/_shared/canonical_constants.py` with S95 W4-5 (and S49) provenance, OR tag every §5.2 citation of "τ_NEC=1.383" as a session-derived (non-frozen) value. Confirm the value to the precision the censorship argument needs (the barrier-to-onset gap is ~7×, so 4 sig figs suffice).
- **Inputs:** S95 W4-5 12D censorship gate (`Ric_min` crosses 0 at τ_NEC); S49 C²-block Ricci=0 boundary; my MEMORY `tau_NEC=1.382334`; the censoring barrier `τ≈0.19143`.
- **Gate:** PASS iff `tau_NEC` is either in `canonical_constants.py` with a PROVENANCE entry (value bit-stable against S95 W4-5) OR every document citation is tagged session-derived. This is a constants-hygiene gate (artifact-existence), not a physics threshold.
- **Effort:** Trivial. One `update_constant(...)` call + provenance, OR a §5.2 tag edit. Fix-in-session per the no-technical-debt rule. Closes §IV.3.

---

## VI. Verdict

From the geometric and global-causal vantage, the capstone is **a solid, honestly-calibrated synthesis** that does my domain's discipline in the right order: characterize the exact internal geometry first (Jensen metric, `D_K(τ)`, the closed-form `R_K(τ)`), then extract the global content (gap, censorship, horizons, causal structure), and refuse to approximate before the exact picture is in hand. The geometric spine — volume-preserving TT deformation, exact monotone-tail curvature polynomial, never-closing Lichnerowicz gap, sixth-order Wronskian degeneracy at and only at genesis — I independently re-verified (Sage, this review) and it holds to all printed digits.

The document's geometric high-water mark is its treatment of the singularity structure (§5.2, §9): it does **not** over-claim singularity-freedom; it claims the geometrically defensible and *stronger* statement — a genuine anisotropic Kasner-type singularity at τ→∞, dynamically censored by a barrier sitting an order of magnitude below the NEC-violation onset, lifted to the exact 12D metric. This is weak cosmic censorship realized substrate-internally, and it is the right way to put it. The extremal-horizon (κ=0, T_H=0) corroboration of the Ordered Veil (§5.3) is a clean, independent causal-side argument that I confirm.

**The central gap is correctly named and unsoftened** (§6.3): there is no derived FRW `a(t)`; the τ↔t ordering is postulated; the conformal embedding is proxy-conditional and INFO. The document reframes this as a back-reaction-closure owed at the effective level, which is the right diagnosis and reduces (rather than inflates) the open frontier by identifying frontiers #1 and #8 as one object.

**My flags are all fixable and none is a physics error:** (IV.1) reconcile the §9 four-faces "At time t" row to carry §6.3's three-tier hedge (causal topology solid / quantitative embedding INFO / normalization open); (IV.2) the §6.2 causal architecture has no Penrose diagram and does not cite the canonical `Phononic-Penrose-Diagrams.md` — the strongest visual argument for causal-disconnection-not-stretching is a conformal diagram, and the document makes the claim without it; (IV.3) `tau_NEC` is cited as pinned but is not a canonical constant.

The harvest (§V) is seven runnable geometric computations: the τ→∞ Petrov classification (CF-SP-1), the asymmetric two-cone Penrose diagram (CF-SP-2, closes the IV.2 figure gap), the causal-consistency of the conformal clock (CF-SP-3, narrows the §6.3 gap), the entry-surface trapped-surface/Raychaudhuri analysis (CF-SP-4), the convention-invariance of the κ-ratio (CF-SP-5), the CCC/Weyl-Curvature-Hypothesis comparison (CF-SP-6, highest-novelty, engages Penrose's own program), and the `tau_NEC` promotion (CF-SP-7, in-session hygiene). CF-SP-2 and CF-SP-6 are the two I would run first: the first discharges a documented gap, the second opens the deepest geometric question the capstone gestures at but does not pursue — whether the censored τ→∞ boundary and the low-Weyl genesis are the two ends of a substrate-internal conformal aeon.

**Bottom line:** the equation derives its own stage rather than populating a given one — and on the geometry of that stage, the document is honest about what is exact (the curvature polynomial, the gap, the censorship) and what is owed (the scale factor, the time normalization). That is the only posture under which a claim this large stays geometrically defensible, and the capstone holds it.

---

*Reviewer note (memory hygiene, not part of the review):* my own MEMORY.md cites the Penrose-diagram file at the stale path `sessions/framework/Penrose-Diagrams.md`; the canonical file is `sessions/framework/Phononic-Penrose-Diagrams.md`. I will correct this. The capstone is not implicated.
