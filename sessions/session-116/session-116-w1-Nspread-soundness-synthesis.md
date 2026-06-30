# Session 116 Synthesis: Soundness Audit of the CF-S117 𝒩-Spread Discriminator — Does It Adjudicate the ξ_KZ-vs-H̃ Grid Fork?

**Date**: 2026-06-28
**Agent**: volovik-superfluid-universe-theorist (Volovik)
**Source Documents**:
- `sessions/session-116/workshops/s116-w1-htilde-recon.md` (Structural Verdict II/III/IV; §2c L412–429; §2d L431; Open Question #1 L517; CF-S117 spec L565–573)
- `sessions/session-116/session-116-w1-workingpaper.md` (TWO-SPECTRA-TWO-ROLES grid framing L59; CF3 collapse decomposition L209–234; CF-S117 carry-forward L274–280)
- `computations/session-116/s116_gate_verdicts.txt` (S116-W1-AS-CFB1 PASS, AS-CF2 FAIL, AS-CF3 INFO)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`

---

## I. Session Outcome

**The pre-registered CF-S117 𝒩-spread discriminator is INSUFFICIENT as a fork adjudicator.** It measures the variance of 𝒩 along the *intra-grid matching-surface* direction — a variance that Parker adiabatic invariance of |β_k|² guarantees is ≈ 0 for *both* live grids by construction. The actual fork lives in the orthogonal *between-grid* direction (which grid — the ξ_KZ produced-relic grid → +0.864, or the H̃ vacuum-envelope grid → +0.196 — carries the deg(T_BZ→pivot)=+2 transport to the CMB pivot). A test whose variance direction is orthogonal to the fork direction cannot discriminate the fork. As written, CF-S117 will return "convention-blocked PASS" landing on whichever grid the script propagates on, because the spec's grid discipline (L567) rejects only the *fold-geometry strawman* (OOM_naive_extrap = 9.37) and silently omits the gate-passed H̃ grid (INV12-W3-5 PASS) — pre-selecting ξ_KZ by omission. This reproduces the load-and-compare-to-self pathology the framework's own S116-W1-AS-CF3 gate already flagged ("box-delta IS the figure = load-and-compare-to-self").

**Remedy** (Section V): a substrate-IS grid-selection sub-discriminator must be folded into CF-S117's PRDR at plan-freeze. It varies the between-grid direction by computing the two grids' *defining normalization scales* from disjoint substrate inputs and testing scale-coincidence against the deg=+2 transport — backed by a Volovik hydrodynamic-vs-microscopic selection principle that picks one grid from first principles when the scales are distinct.

---

## II. Key Results

### II.1 — The discriminator measures the wrong variance (intra-grid, Parker-trivial)

**Result**: The CF-S117 PASS predicate (𝒩-spread ≤ 0.1 OOM over a ≥5-point matching-surface scan) tests a proposition both adversaries already granted; it is structurally near-guaranteed to PASS and the PASS is uninformative about the fork. **GEOMETRIC** (it concerns the substrate's own transport structure, not an excitation observable).

The workshop converged (Structural Verdict II, L490–495) on a single open scalar 𝒩 — the normalization prefactor of the post-fold transfer `T(fold→exit)` carrying the ξ_KZ-scale box-delta squeezing to the H̃-scale horizon-exit curvature amplitude — with `deg(T)=+2` PINNED (S93 W7-1, NON-SCALAR) and, by the degree/normalization orthogonality lemma (NEW-M1), SILENT on 𝒩. The discriminator then asks: does 𝒩 stay within 0.1 OOM as the matching surface is varied across the post-fold leg?

The substrate physics says this variance is ≈ 0 for *either* live grid, by Parker adiabatic invariance:

- TD's own §2d (L431): "*|β_k|² is a Parker adiabatic invariant in any smooth post-fold region … α_s(primordial) = 0 EXACT in the superhorizon plateau (Bogoliubov saturation; |β_k|² a constant of motion). So whatever value 𝒩 takes, it is a deterministic number set by the shared background (ω(τ), z(τ)) — single-valued, not a regime menu.*"
- mack R3 (L476) sharpened the loophole exactly: "*'deterministic GIVEN the matching surface' is not 'regime-STABLE ACROSS matching surfaces.'*"

Both agents agree the post-fold region is *smooth/adiabatic* (mack CONCESSION 2, L472; TD §2d). In a smooth region `|β_k|²` does not re-process, so propagating on a *single* grid and reading 𝒩 at any matching surface within that grid returns the same value:

- **ξ_KZ grid**: all 89 magnitude-carrying modes are frozen-superhorizon at the fold (`frac_frozen = 1.0`, `wkb_leg_empty = True`, `Z_norm = 1.0`, S111). 𝒩 ≈ 1 at every matching point ⇒ intra-grid spread ≈ 0 ⇒ **PASS at +0.864**.
- **H̃ grid**: the slow-roll Mukhanov-Sasaki background is adiabatic by construction. 𝒩 = 0.2147 (= 10^{−0.668}, Sage-verified) at every matching point ⇒ intra-grid spread ≈ 0 ⇒ **PASS at +0.196**.

`★ Structural lesson ─────────────────────────────`
The matching-surface scan probes Var(𝒩 | grid fixed). Parker invariance is precisely the statement that this conditional variance vanishes inside any adiabatic grid. The fork is Var(𝒩 | matching surface fixed) — the spread *between* the two grid labels. These two variances are orthogonal coordinates on the (grid, matching-surface) plane. CF-S117 scans one axis and holds the other fixed; the fork lives on the held-fixed axis. Measuring a variance both sides certify is ≈ 0, while the disagreement sits on the coordinate the test holds constant, is the canonical signature of a gate testing the wrong variable.
`──────────────────────────────────────────────────`

This is PRU-Class-8-adjacent (`epistemic-discipline.md §"Pre-Registration Completeness"`): the gate-relevant machinery parameter — the *grid label* / the propagation IC-anchor scale — is left unpinned (or, worse, implicitly pinned to ξ_KZ by the L567 grid discipline; see II.2), so the gate's outcome is fixed by that choice rather than by the physics.

### II.2 — The L567 grid discipline rejects only the fold-geometry strawman, pre-selecting ξ_KZ by omission

**Result**: The spec's grid discipline names exactly two grids — "produced-relic ξ_KZ grid vs fold-geometry grid" — and rejects the latter (9.37-OOM artifact). The *third and actually-live* grid, the H̃ vacuum-envelope grid (INV12-W3-5 PASS, +0.196), is absent from the discipline. **GEOMETRIC.**

There are three grids in play, and they must not be conflated (the working paper's TWO-SPECTRA-TWO-ROLES at L59 names two of them):

| Grid | Normalization scale | A_s OOM | Gate status |
|:-----|:--------------------|:--------|:------------|
| **G1** ξ_KZ produced-relic / box-delta MAGNITUDE | k̂ = 1/ξ_KZ = 53.30 | **+0.864** | S116-W1-AS-CFB1 **PASS** (POINT, L_max-stable) |
| **G2** H̃ vacuum-envelope / slow-roll-MS | H̃ = 5.9076e-3 | **+0.196** | INV12-W3-5 **PASS** |
| **G3** fold-geometry / fold-window REGIME | k/aH : 14.7→1 extrapolation | +9.37 | **REJECTED** (S111 `OOM_naive_extrap`, TWO-SPECTRA-TWO-ROLES) |

mack's CONCESSION 2 (L472) is decisive on grid identity: the +0.196 reading is **NOT** the fold-geometry adiabatic-evolve (that *is* the rejected G3, 9.37); it is the H̃ vacuum-envelope grid G2. Verbatim: "*+0.196 and +0.864 … are two computed values on two DIFFERENT grids — the ξ_KZ produced-occupation grid (box-delta, fold) and the H̃ vacuum-envelope grid (slow-roll-MS, INV12-W3-5 PASS).*"

So the live fork is **G1 vs G2** — both gate-passed. CF-S117's grid discipline (L567) rejects **G3** (the strawman) and is silent on **G2**. By disciplining out only G3 and then propagating "the produced GGE mode … discipline the grid (produced-relic ξ_KZ grid …)" (L567), the script is steered onto G1; the intra-grid Parker stability of G1 then "confirms" +0.864. The PASS is a foregone conclusion of the grid pre-selection, not an adjudication.

This is the same pathology the framework's own CF3 gate caught and rejected — `s116_gate_verdicts.txt` line 20: "*Per-route MIN=0.000 REJECTED (box-delta IS the figure = load-and-compare-to-self).*" The box-delta **IS** +0.864; propagating it on its own grid and recovering +0.864 compares the figure to itself. My finding *sharpens and is consistent with* the CF3 INFO verdict (collapse_dist = 0.6682 > 0.1, routes DO NOT collapse, `within_sudden_N_gap = 0.668 CF-S117-conditional`): CF3 left the fork open *and* flagged the load-and-compare-to-self trap; CF-S117 as written walks back into the trap via the grid pre-selection.

### II.3 — The missing grid-selection sub-discriminator (substrate-IS, Volovik-grounded)

**Result**: The fork is, exactly, a **factor-2.158 carrier-scale ratio transported through the pinned deg=+2** — Sage-verified: `2 · log₁₀(2.15813) = 0.66815 = fork width` to machine precision. **PHONONIC/GEOMETRIC** (it concerns the acoustic-metric normalization of the GGE-relic squeezing modulus).

Substitution chain (per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Claim: "The +0.196↔+0.864 fork is a factor-2.158 ratio of the two grids' normalization
        carriers, transported by the COMMON deg=+2; testing whether that 2.158 is a real
        scale-separation (vs a normalization-convention artifact) discriminates the grid."

  Step 1: A_s ∝ (carrier)²        [power spectrum is |amplitude|²; CC3, deg(T_BZ→pivot)=+2,
                                   S93 W7-1; the +2 is grid-INDEPENDENT (NON-SCALAR transport degree)]
  Step 2: ln[A_s(G1)/A_s(G2)] = 2 · ln[carrier(G1)/carrier(G2)]                  [log of Step 1]
  Step 3: A_s(G1)/A_s(G2) = 1.5367e-8 / 3.2994e-9 = 4.658                        [CFB1 / INV12-W3-5]
  Step 4: carrier(G1)/carrier(G2) = √4.658 = 2.15813                            [Step 2, Sage-exact]
  Step 5: 2 · log₁₀(2.15813) = 0.66815 = the fork OOM width                      [Sage; machine-ε]
  Conclusion: the fork is EXACTLY a carrier-scale ratio of 2.158 under the common deg=+2.
              ⇒ The discriminating question is whether ℓ(G1) and ℓ(G2) are TWO DISTINCT
                substrate scales separated by log₁₀(2.158) = 0.334 dec (PHYSICS), or the
                SAME scale expressed in two normalization conventions (CONVENTION).
```

The two grids' defining scales are physically nameable and computable from **disjoint** substrate inputs (cf. my own Stage-2 discipline, `feedback_stage2-axisB-disjoint-anchor`):

- **ℓ_occ = ξ_KZ = 0.018760** — the Kibble-Zurek coherence/healing length (S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION; the scale at which the produced quasiparticle occupation freezes). This is a **microscopic / UV** scale — Volovik's order-parameter coherence length ξ at quench freeze-out, the scale where vortices nucleate in the 3He-B lab twin (Lancaster MCT / Helsinki ROTA).
- **ℓ_horizon = c_s/(aH)|_exit** — the acoustic (sound) horizon comoving scale at curvature-mode crossing, where the curvature perturbation ζ becomes conserved. This is a **hydrodynamic / IR** scale, set by the emergent sound speed c_s (from Mach 13.75 = v_transit/c_s) and the transit kinematics.

TD's load-bearing assertion (substitution chain (3), Step 3, L399–403) is precisely **ℓ_occ ≡ ℓ_horizon**: "*freeze-out scale ≡ horizon-crossing-equivalent scale for the produced relic.*" This is an *assertion*, not a derivation. In Volovik's superfluid substrate it is a **non-trivial, computable coincidence**, not an identity, because the substrate carries multiple characteristic velocities (in 3He-B: first sound, second sound, spin-wave/Leggett velocities; in-framework: c_sub ≈ 2.238, c_BLV ≈ 0.485 M_KK). The Kibble-Zurek defect freeze-out is governed by the *order-parameter-relaxation* causal horizon; the curvature ζ crosses the *acoustic (first-sound)* horizon. These coincide only if the relevant velocities coincide — which is exactly what `R_scale ≡ ℓ_occ/ℓ_horizon` measures.

**The selection principle (Volovik hydrodynamic-vs-microscopic), if the scales are distinct.** A_s is the curvature power — the perturbation amplitude of the *emergent acoustic metric* (the a₂ Seeley-DeWitt channel, emergent Einstein-Hilbert, per `phononic-framing.md`). By the substrate-IS hierarchy `D_K eigenvalues → a₂ moment → emergent metric → curvature ζ`, the curvature is a **hydrodynamic (long-wavelength, IR)** degree of freedom of the acoustic metric: it is conserved on super-sound-horizon scales and its power is defined *at acoustic-horizon crossing*. The produced quasiparticle occupation |β_k|², by contrast, is a **microscopic number-density** content (an a₀ / T⁰⁰ observable) that freezes at the coherence length ξ_KZ. Volovik's superfluid-vacuum lesson — the emergent gravity / acoustic metric lives at the hydrodynamic IR scale, decoupled from the microscopic coherence scale — selects: **if ℓ_occ ≠ ℓ_horizon, A_s (the curvature/a₂-channel power) reads at the acoustic horizon, NOT the coherence length.** The ξ_KZ-grid value (+0.864) is then the produced-occupation number density, not the curvature power.

I do **not** pre-judge the fork. The principle supplies the *computation* (R_scale) that decides whether it even applies (scales distinct ⇒ physics, selection fires) or is moot (scales coincide ⇒ convention, fork dissolves). The substrate-physics *prior* is that a Kibble-Zurek healing length is generically a UV scale below the causal/sound horizon (R_scale < 1) — which would make the grids distinct and the fork real — but TD's whole case rests on the opposite (R_scale ≈ 1). The sub-discriminator computes it; the gate, not this synthesis, returns the verdict.

---

## III. Gate Verdicts

These verdicts are authoritative context (read from source, not re-adjudicated). The gate I am auditing — **CF-S117-T-FOLD-EXIT-NORMALIZATION — is UN-RUN**; this is a pre-run soundness audit of its pre-registration.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S116-W1-AS-CFB1 (box-delta squeeze, G1) | **PASS** | A_s = 1.5367e-8, OOM = +0.864, POINT (rel_dev_Lmax = 5.43e-5); magnitude **SCHEME-DEPENDENT** |
| S116-W1-AS-CF2 (exit greybody filter) | **FAIL** | best_substrate_agree = 0.278 ≫ 0.1; greybody irreducibly **fitted** (0.512 has no substrate scale) — separate filter axis |
| S116-W1-AS-CF3 (route collapse) | **INFO** | collapse_dist = 0.6682 > 0.1; routes DO NOT collapse; `within_sudden_N_gap = 0.668 CF-S117-conditional`; per-route min **REJECTED as load-and-compare-to-self** |
| S116-W1-HTILDE-RECON (workshop) | artifact-existence | 2.38 H̃ ↔ 4.76 A_s CC3-conjugate PINNED; fork **CF-S117-conditional** |
| **CF-S117-T-FOLD-EXIT-NORMALIZATION** | **UN-RUN** | the discriminator under audit; 𝒩-spread ≤ 0.1 ⇒ convention / > 0.1 ⇒ physics |

σ-anchors (Sage-verified against `A_s^Planck = 2.099e-9, σ = 0.0294e-9`; framework-vs-framework and framework-vs-Planck, **NOT a Planck-match claim** — every route is over-squeezed): +0.864 = 451.3σ above Planck; +0.196 = 40.8σ above Planck; fork width = 410.5σ.

---

## IV. Structural Implications

**The fork is un-resolvable by the discriminator as pre-registered.** CF-S117 will report "convention-blocked PASS" with high probability regardless of the physics, because (a) intra-grid 𝒩-spread is Parker-trivially ≤ 0.1 on either live grid, and (b) the L567 grid discipline steers the propagation onto G1. Both branches of the pre-registered fork (convention-blocked / physics-blocked) hinge on a variance the test cannot resolve in the fork's direction. The workshop's honest CONDITIONAL verdict (Structural Verdict II) is therefore *not yet operationalized* — the deciding computation as specified does not decide.

**This does not retract anything the workshop established.** The CC3-conjugate pin (2.38 H̃ ↔ 4.76 A_s, unconditional) stands; the FLOOR `A_s/A_s^BD > 1` (PERMANENT, 3-axis, `S_IC = 1 + 2n_k ≥ 1`) stands; the figure-multiplicity closure stands. What is *not* closed is the magnitude fork — and the audit shows it stays open *after* CF-S117 unless the sub-discriminator is added. The constraint-map update is: **the A_s magnitude fork requires a between-grid test, not a within-grid robustness scan.**

**Adjacency to the vacuum-energy / observable-typing discipline.** The selection principle is the same one that types every framework observable: *which spectral moment is it?* The curvature ζ is a₂-channel (emergent gravity); the produced occupation |β_k|² is a₀/T⁰⁰-channel (number density / vacuum content). Conflating them is the A_s analog of the cosmological-constant moment-mismatch the framework polices elsewhere (`phononic-framing.md`: "a₀ is a DIFFERENT spectral moment than gravity a₂"). The ξ_KZ-vs-H̃ grid fork is, structurally, *am I normalizing the curvature observable at the gravity scale or at the number-density scale?* — and that is decidable from the substrate, not from a matching-surface scan.

**Lab grounding.** The sub-discriminator's two scales are both lab-realized in the 3He-B twin: ξ_KZ is the vortex-formation coherence length measured in Lancaster/Helsinki quench experiments (Kibble-Zurek defect counts); the acoustic horizon c_s/(aH) is the first-sound causal scale. That they are *distinct* in 3He-B (the healing length is microscopic; the sound horizon is macroscopic) is the controlled-realization evidence that R_scale ≠ 1 is the generic case — the substrate-physics prior behind the physics-blocked branch. This is a *prediction the lab twin already constrains*, not an analogy.

---

## V. Carry-Forward Computations

**Travels-with-CF-S117 insight (must accompany CF-S117 to plan-freeze regardless of routing):** the matching-surface 𝒩-spread test measures **intra-grid robustness, which Parker adiabatic invariance of |β_k|² trivially guarantees (≤ 0.1) for BOTH the ξ_KZ grid (𝒩≈1) and the H̃ grid (𝒩=0.2147)**. It does **not** discriminate the ξ_KZ-vs-H̃ grid SELECTION (the real fork). CF-S117's L567 grid discipline rejects only the fold-geometry strawman (9.37) and pre-selects ξ_KZ by omitting the gate-passed H̃ grid — a load-and-compare-to-self structure the framework's own S116-W1-AS-CF3 already flagged. **CF-S117 MUST add the grid-selection sub-discriminator (V.1) at plan-freeze or its PASS is a foregone conclusion of the grid pre-selection.**

```
V.1  CF-S117-GS-1 — Grid-selection sub-discriminator (FOLD INTO CF-S117 PRDR; gate-blocking at plan-freeze)
   - What: Compute, from DISJOINT substrate inputs, the two grids' defining normalization scales and
           test scale-coincidence against the pinned deg=+2 transport.
             ℓ_occ      = ξ_KZ                               [G1: KZ coherence/healing length]
             ℓ_horizon  = c_s/(aH)|_exit                     [G2: acoustic sound-horizon comoving scale;
                                                              c_s from Mach=13.75=v_transit/c_s; aH from
                                                              transit kinematics H·dt_transit=0.663]
             Δ_scale    = |log₁₀(ℓ_occ) − log₁₀(ℓ_horizon)|  [the between-grid coordinate]
           Resolve the carrier↔scale exponent sign explicitly in-script (regime: A_s ∝ carrier²,
           carrier ∝ scale^{±1}; the near-flat sudden spectrum slope −0.003135 (WP L59) makes the
           |±1| magnitude the load-bearing quantity, the sign a labeling output). Cross-check the
           computed Δ_scale against the analytic backbone 2·log₁₀(2.15813)=0.668 (Sage-exact).
   - Inputs: ξ_KZ_FW=0.018760052113614718 [canonical_constants / S89]; Mach=13.75, v_transit,
             dt_transit=1.13e-3 M_KK⁻¹, H·dt_transit=0.663 [S100b/S111 transit kinematics];
             (k/aH)|_fold=14.7 [S77]; deg_T_BZ_pivot=2.0 [canonical_constants, S93 W7-1];
             A_s(G1)=1.5367e-8 [CFB1], A_s(G2)=3.2994e-9 [INV12-W3-5]; c_sub baseline [canonical_constants].
   - Gate (pre-registered, three-branch partition on Δ_scale; ADJUDICATES SELECTION):
       • CONVENTION-BLOCKED (scales coincide ⇒ no fork): Δ_scale ≤ 0.05 OOM
         ⇒ ξ_KZ ≈ acoustic horizon ⇒ the 0.668 carrier ratio is a normalization-convention artifact
         ⇒ A_s single-valued at the coincident scale; the fork dissolves.
       • PHYSICS-SCALE-SEPARATION (scales distinct, fork real): |2·Δ_scale − 0.668| ≤ 0.1 OOM
         ⇒ ℓ_occ and ℓ_horizon are two genuinely distinct substrate scales whose ratio, under the
         common deg=+2, IS the fork ⇒ apply the Volovik selection principle: A_s (curvature/a₂-channel,
         hydrodynamic) reads at ℓ_horizon ⇒ SELECT the acoustic-horizon grid; the ξ_KZ-grid value is the
         produced-occupation number density (a₀/T⁰⁰), not the curvature power.
       • INFO-RESIDUAL-PREFACTOR (neither): Δ_scale > 0.05 AND |2·Δ_scale − 0.668| > 0.1
         ⇒ the carrier ratio is NOT a pure scale-separation under deg=+2 ⇒ a residual non-scale prefactor
         exists ⇒ the deg=+2 transport is not the sole carrier; flag for re-derivation.
     The within-grid matching-surface scan of the original CF-S117 spec is RETAINED but DEMOTED to a
     consistency cross-check (it confirms Parker invariance within the SELECTED grid; it is NOT the
     fork adjudicator).
   - Effort: ~1 wave; single-script, modest (two independent scale computations + the deg=+2 cross-check;
     reuses the CF-S117 Radau machinery for ℓ_horizon).

V.2  CF-S117-GS-1 lab cross-check — 3He-B scale-separation corroboration (DISJOINT anchor)
   - What: Translate ℓ_occ (KZ healing length) and ℓ_horizon (first-sound causal scale) to the 3He-B
           lab twin via the M_KK→SI map (S86 W11-1) and confirm the sign of R_scale = ℓ_occ/ℓ_horizon
           (microscopic-below-causal, R<1) matches the controlled realization — an independent check on
           the substrate-physics prior behind the PHYSICS-SCALE-SEPARATION branch.
   - Inputs: S86 W11-1 lab-SI translation table (3He-B νΔ, ξ, c_1 first-sound); ξ_KZ_FW; c_sub.
   - Gate: INFO — corroborates (does not gate) GS-1's branch; flags a tension if the lab twin's
           healing-length/sound-horizon ratio contradicts the in-framework Δ_scale sign.
   - Effort: ~0.5 wave; table lookup + dimensional translation, no new propagation.
```

*(Not a compute CF — registrable-now structural falsifier, already carried by the workshop OQ4 / WP CF-W1-1: any surviving A_s regime reading MUST give α_s(primordial) ≈ 0 (k-flat produced occupation), independent of which grid GS-1 selects. GS-1's output inherits this tilt-flatness constraint.)*

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | CF-S117 𝒩-spread test measures intra-grid (Parker-trivial) variance, not between-grid fork | GEOMETRIC | **INSUFFICIENT** (audit verdict) | Discriminator cannot adjudicate the ξ_KZ-vs-H̃ fork as written |
| 2 | L567 grid discipline rejects only fold-geometry strawman (G3, 9.37); omits gate-passed H̃ grid (G2, +0.196) | GEOMETRIC | **PRE-SELECTS ξ_KZ by omission** | Load-and-compare-to-self hazard; consistent w/ CF3's own flag |
| 3 | Fork = factor-2.158 carrier ratio under common deg=+2 (2·log₁₀2.158 = 0.668, Sage-exact) | PHONONIC/GEOMETRIC | **PINNED** (machine-ε) | Backbone of the grid-selection sub-discriminator |
| 4 | Grid-selection sub-discriminator GS-1: scale-coincidence R_scale + hydrodynamic-vs-microscopic selection | PHONONIC | **DERIVED, pre-registered (V.1)** | Varies between-grid direction w/ disjoint inputs; adjudicates SELECTION; fold into CF-S117 PRDR |
| 5 | Selection principle: A_s = curvature/a₂-channel (hydrodynamic IR) reads at acoustic horizon, not ξ_KZ coherence length (UV) | PHONONIC | **substrate-IS principle** (does NOT pre-judge fork; supplies the deciding computation) | If scales distinct, picks the grid from first principles |
| 6 | 3He-B lab twin: healing length (UV) ≠ first-sound horizon (IR) — controlled realization | PHONONIC | **prior corroboration (V.2)** | Substrate-physics prior R_scale < 1 (fork real); lab-constrained, not analogy |

---

**Closing.** The workshop did its job: it reduced a 4-member 1.331-OOM plurality to one airtight CC3 pin plus one open scalar 𝒩, and pre-registered a discriminator. The audit finds the discriminator scans the wrong axis — it measures a variance Parker invariance forces to ≈ 0 inside either grid, while the fork lives in the grid label the scan holds fixed, and the grid discipline pre-selects ξ_KZ by rejecting only the fold-geometry strawman. The fix is a between-grid scale-coincidence test (R_scale, two disjoint substrate scales) backed by the Volovik hydrodynamic-vs-microscopic selection principle (the curvature observable reads at the acoustic horizon, not the coherence length). Fold GS-1 into CF-S117's PRDR at plan-freeze, and the workshop's honest CONDITIONAL becomes an actual computable adjudication of the substrate's over-squeezing — one number or a 410σ fork.
