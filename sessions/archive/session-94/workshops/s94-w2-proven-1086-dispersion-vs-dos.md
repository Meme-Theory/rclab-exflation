# W-2 — JOINT STRUCTURAL VERDICT: `proven_1086` "B2 flat band — Infinite-order Van Hove" disposition

**Workshop**: W-2 — disposition of registry claim `proven_1086` ("B2 flat band — Infinite-order Van Hove", S22c, `Classification-of-phonon-exflation.md:59`, Paper 27, status PROVEN).
**Turn**: T4 (Round 2 FINAL, balanced joint verdict + canonical output doc). Author = `landau-condensed-matter-theorist` (DOS-degeneracy reading; wrote T2).
**Opponent**: `kaluza-klein-theorist` (dispersion-refuted reading; wrote T1 + T3).
**Status of this document**: this is the schedule's `--output` deliverable. It carries the JOINT verdict (NOT a one-sided DOS-reading win), the routed edit-text blocks for the doc-owner and the Slot-3 closeout, and the one-line closeout summary. I OWN the registry entry and the refuted reading; I write the converger's verdict, not the winner's.

---

## Transcript pointer

The full adversarial exchange is in three turn files, read in order: **T1** `s94-w2-T1-kk-R1.md` (kk steelman — `proven_1086` is a band-dispersion claim, REFUTED on-functional by W7-22, with a heavy four-part burden placed on the DOS reading); **T2** `s94-w2-T2-landau-R1.md` (my steelman — S22c proved the DOS-degeneracy sense, a δ-pile-up `8·δ(E−E_0)` on a structurally distinct functional `Φ_DOS` that W7-22 does not touch, discharging the four-part burden + rebutting T1 argument-by-argument); **T3** `s94-w2-T3-kk-R2.md` (kk's FINAL rebuttal — concedes the velocity-slaving mis-aim, then introduces the DECISIVE new fact that the framework's canonical B2 DOS is the FINITE, framework-named `rho_smooth = 14.02 = 1/(π·v_g)`, not a δ-function, and argues multiplicity ≠ order; offers ≈90% convergence). This T4 verdict weighs both sides and disposes the claim.

---

## JOINT STRUCTURAL VERDICT

### Verdict in one sentence

`proven_1086` is **RE-WORDED onto the DOS functional `Φ_DOS` and RETAINED for its proven, load-bearing content — a finite, large, BCS-driving band-edge density of states (`rho_smooth = 14.02 M_KK⁻¹`, the `N(0)` feeding `g·N(0)=3.24`) — while the qualifiers "infinite-order van Hove" and "flat band" are DEMOTED/scope-clarified as REFUTED on-functional by W7-22 and contradicted by the framework's own canonical `rho_smooth` value.** The residual terminological question — whether the fixed mult-8 δ-WEIGHT earns the noun "van Hove singularity" at all — is reported as an HONEST NON-CONVERGENCE and routed to a compute gate, because it does not change the proven physics under either resolution.

### The two fixed points both sides agreed on from the start

1. **The dispersion reading is REFUTED (mutual, robust, fit-window-independent).** On `Φ_dispersion = v_g^{B2}(τ)/n_dispersion(τ)`, W7-22 (`S94-DS-GAMMA-E-RESOLUTION`; INFO; `audit_sha256=1b71fb67…`) found `|v_g(τ_fold)| = 0.0227` (ρ-pinned) / `0.0541` (band-ladder), BOTH ≥ 2.3× the `1e-2` floor at every τ-slice in `[0.15, 0.23]`; `n_dispersion = 1` (order-ratio 18.93 ≫ 0.1); `first_gap = 0.00497` monotone-decreasing through the fold with no cusp/local-min/collapse; the `√`-edge (`n=2`) model fits worse than linear in every window. I OWN this reading and CONCURRED in the W7-22 WP that it is genuinely refuted — no manufactured dissent. There is no `v_g → 0` flat band. **kk's T1 §1 stands; I do not relitigate it.**

2. **The PROVEN, load-bearing BCS-driving physics is real and untouched by W7-22.** The B2 band edge supplies a large density of states `N(0)` that drives BCS condensation: `g·N(0) = 3.24` (S22c, alongside Pomeranchuk `f_0 = −4.687`); the S28c PROVEN theorem "Van Hove divergent DOS triggers BCS through the 1D theorem, not through a Fermi surface" (43–51× enhancement); the atlas-07 permanent-results "Van Hove DOS" WALL (`ρ = 14.02, Z = 1.016`, PASS). **kk conceded this in T3 §4.1; I insisted on it in T2; both sides agree it must be preserved.** This is the substantive content `proven_1086` exists to summarize, and it does NOT die with the dispersion refutation.

### What I conceded that kk won — weighing kk's strongest points honestly (the converger's duty)

I am the converger, not the winner. kk conceded my velocity-slaving rebuttal in T3 §0 (Claim B's `Z = ρ·v_g = 1/π` is a continuum-branch identity that does not, by itself, refute a hypothetical `ρ_singular = m·δ` branch — the domain of the identity is the dispersing continuum, where `v_g` is finite; the brief is correct that the δ-branch survives Claim B). In return I must weigh kk's two strongest points honestly. **Both land, and both are decisive against the "infinite-order van Hove" NAMING. I record them in full.**

#### Crux 1 — The finite canonical `rho_smooth = 14.02` (kk T3 §1). VERIFIED; load-bearing; it defeats the "divergent DOS / infinite-order" wording.

kk's T3 §1 is the strongest argument in the entire exchange, and I verified its load-bearing arithmetic against the knowledge base and via Sage rather than taking it on assertion:

```
Substitution chain (the framework's canonical DOS IS the continuum branch, NOT the δ-branch):

  Step 1:  rho_smooth      = rho_B2_per_mode = 14.023250234055  M_KK⁻¹
                             [canonical, get_constant(S37, s37_instanton_action.npz);
                              framework's OWN name: "rho_smooth = 14.02 (van Hove)" — session-34-scratchpad VERBATIM;
                              "the SMOOTH-wall DOS rho_vH = 14.02" — session-62-hawking-qa VERBATIM;
                              atlas-07 WALL "Van Hove DOS": rho = 14.02, Z = 1.016, PASS]
  Step 2:  ρ_continuum     = 1/(π|v_g|)               [canonical continuum-branch DOS; eq_8045:
                                                        "Z_wall = ρ·v = [1/(π·v)]·v = 1/π ~ 0.318",
                                                        "DOS divergence (ρ~1/(π·v)) and velocity vanishing cancel"]
  Step 3:  set ρ_continuum = rho_smooth, solve for v_g
                  |v_g|    = 1/(π · 14.023250234055)
                           = 0.0226987239671          M_KK   [Sage-exact, this T4]
  Step 4:  W7-22 ρ-pinned  v_g^ρ(fold) = 1/(π·rho_B2_per_mode) = 0.022699  M_KK  [T1 §1 line 68; T3 §1 Step 4]
  Step 5:  Step 3 ≡ Step 4 to the published 5 sig figs (residual 4.77e-7 = publication rounding of 0.022699).
  Cross-check: Z = rho_smooth · (1/(π·rho_smooth)) = 1/π = 0.318309886184 EXACT [Sage-exact, this T4; matches eq_8045].
  Conclusion: the framework's canonical "Van Hove DOS" (14.02) is ρ_continuum = 1/(π|v_g|) at the W7-22
              velocity, to the digit — the VELOCITY-SLAVED CONTINUUM branch, NOT ρ_singular = 8·δ.
```

**This is the crux, and I weigh it for kk.** My T2 rested the DOS-degeneracy reading on the proposition that the load-bearing, BCS-driving object is `ρ_singular = 8·δ` and that the continuum branch is a side term. The framework's own canonical constant says the reverse: the DOS the substrate actually computed, NAMED `rho_smooth` ("smooth" — the antonym of "singular"), pinned to `canonical_constants` at S37, and fed downstream into `g·N(0)`, is the FINITE `14.02 M_KK⁻¹` — exactly `1/(π·v_g)` at the W7-22 velocity. The `8·δ` singular branch I introduced in T2 appears in **no** canonical constant, **no** wall value, and **nowhere** in the `N(0)`-feeding chain. It is an object I constructed to carry the "infinite-order" label after the dispersion reading died, and the substrate-first record does not contain it.

I also weighed my own anticipated rescue (kk T3 §1.1: "`14.02` is the regulated δ-peak height at finite L_max") and I find kk's three counter-points correct: (1) the framework explicitly named it `rho_smooth` / "SMOOTH-wall DOS" — a smooth-band continuum DOS, not a regulated δ-peak (which the framework would not call "smooth"); the framework separately maintains a DISTINCT singular-wall object — the S85 `S85-VAN-HOVE-CUSP-THEOREM` gate (`value=0.221`, `scheme=DOS-cusp`, FAIL) — confirming the framework itself distinguishes the smooth-wall DOS from a cusp/singular DOS; (2) a regulated δ-peak height would SCALE with the regulator (peak ~ 1/ΔE, grows with L_max resolution), but `rho_B2_per_mode` is pinned as a fixed `per_mode`-normalized canonical constant equal to `1/(π·v_g)` at the *measured* `v_g` — a velocity-slaved continuum DOS is L_max-stable in exactly this way; (3) even if granted, the "regulated-δ" defense re-imports the very `v_g → 0` requirement the dispersion refutation killed (you cannot reach a true δ from `1/(π·v_g)` without `v_g → 0`; W7-22 found `v_g` bounded ≥ 2.3× above the floor across a 7-point τ-grid), collapsing the "orthogonal functional" back onto `Φ_dispersion`. **The "infinite-order" / "divergent DOS" wording has no canonical referent; the proven DOS is finite, smooth-named, and velocity-slaved. This point goes to kk.**

#### Crux 2 — Multiplicity ≠ order (kk T3 §2). CONCEDED; the "infinite-order" qualifier cannot be discharged by the mult-8.

My T2 §2.4 promoted the multiplicity (8, maximal among the low-lying manifold) to the van Hove ORDER: "on `Φ_DOS` the multiplicity IS the order." kk's T3 §2 shows this is a category error, and I concede it. The argument is structurally clean and uses my OWN hierarchy (T2 eqs. 1.3–1.5) against the identification:

- The **ORDER** of a van Hove singularity is the exponent of the energy-axis non-analyticity `|E−E_0|^{−γ_E}`, `γ_E ∈ [0,1)`, with the δ as the `γ_E → 1` boundary. It is a dimensionless *local-in-energy scaling exponent*, read from the dispersion `E(k)` near `k_0` via `γ_E = 1 − 1/n`.
- The **MULTIPLICITY** is the *integrated weight* of the δ — `∫ρ_singular dE = m`, the COEFFICIENT of the δ, not its order.
- By my own definition (T2 eq. 1.5: a δ of any nonzero coefficient is the infinite-order limit), `1·δ` (B1), `3·δ` (B3), and `8·δ` (B2) ALL have the SAME van Hove order (all are δ-functions, all stronger than every power-law). They differ in WEIGHT, not ORDER.

So promoting multiplicity to order does not rescue "infinite-order": it would make the B1 ground tone and B3 sector ALSO "infinite-order van Hove singularities" — precisely the vacuous-label outcome I conceded in T2 §2.4 must be avoided. The maximal-multiplicity level is the maximal-WEIGHT δ, not the maximal-ORDER van Hove. **kk is right: "infinite-order" asserts an ORDER property; the mult-8 is a WEIGHT property; the two do not coincide. This point goes to kk, and it is the second independent reason the "infinite-order" qualifier falls.** The only functional on which an ORDER is defined for this band reads `n=1` (refuted as a singularity); the multiplicity-8, however large, is not an order.

#### Where kk's §4.6-reversal lands, and where it does not

kk's T3 §3.1 argues that by dropping the §V.D condensate near-crossing and resting on the NORMAL-state band bottom (my T2 §4.6), I moved the DOS claim ONTO the functional W7-22 directly measured. I grant this **for the continuum part**: the NORMAL-state band-bottom continuum DOS IS `ρ_continuum = 1/(π|v_g|) = 14.02`, which W7-22 governs and which carries no infinite-order singularity. Where I do NOT fully concede: the fixed mult-8 δ-WEIGHT is still a genuinely distinct additive term in the decomposition `ρ = 8·δ + 1/(π|v_g|)` (my T2 eq. 2.2, which kk accepted as the correct *form* in T3 §0), and W7-22 confirms its presence (`bot_deg=4` per sector, FIXED at every τ) rather than refuting it. The honest reading is: **W7-22 touches and refutes the singularity-ORDER (it is `n=1`, finite `v_g`, and the canonical DOS is the finite continuum branch); the mult-8 δ-WEIGHT exists but, per Crux 2, carries no ORDER and so cannot bear the "infinite-order" or "van Hove singularity" label by itself.** This is exactly the §4.3 residual, addressed below.

### The disposition

Assembling the two fixed points + the two crux concessions, the converged disposition is the INTERSECTION of kk's T1 position and my T2 position — neither kk's flat DEMOTE (which would lose the proven physics) nor my RETAIN-"infinite-order" (which the canonical `rho_smooth` and the multiplicity≠order argument both refute):

**RETAIN the DOS-edge physics on `Φ_DOS`, re-worded; DEMOTE the "infinite-order" order-claim AND the "flat band" dispersion-noun.** The surviving content is a finite, large, velocity-slaved DOS edge (`rho_smooth = 14.02 M_KK⁻¹`) that supplies the `N(0)` driving BCS — a strong BCS driver, proven, load-bearing, untouched by W7-22 — NOT an infinite-order singularity and NOT a dispersionless flat band. W7-22 is scoped as refuting the band-flattening / infinite-order reading on-functional.

### Honest non-convergence (the §4.3 residual) — reported, not papered over

One substantive disagreement genuinely remains, and per `Investigating-Workshops.md` honest-count discipline and the brief's instruction, I report it rather than force a resolution:

**Does the fixed mult-8 δ-WEIGHT earn the NOUN "van Hove singularity" (even shorn of "infinite-order") on a finite spectral triple?**

- **kk's position** (T3 §3.2): NO. A van Hove singularity is irreducibly an emergent feature of a CONTINUUM band — a non-analyticity of `ρ(E)` from a stationary point of a dispersing `E(k)`, whose defining content is the ORDER. On a finite triple two objects must not be conflated: (1) the fixed representation-theoretic degeneracy (mult-8, the ℂ¹⁶ Clifford structure, present at all τ, k-independent, no dynamics, no order — a group-theoretic multiplicity); (2) the emergent band-structure non-analyticity (the van Hove proper, requiring dispersion + a stationary point + an order — which on B2 is `n=1`, no singularity). "van Hove" is the noun for object (2), which does not exist here; the mult-8 is object (1), a weight. The canonical `rho_smooth` (finite, "smooth"-named) tilts strongly toward "maximal-multiplicity DOS edge," not "van Hove singularity."

- **my position** (T2 §4.7): on a FINITE spectral triple there is no continuum Brillouin zone to integrate, so the closest well-defined analog of a continuum DOS divergence — the object that plays the role of "the energy at which the most spectral weight concentrates" — IS the maximal-multiplicity δ-pile-up. Under that finite-triple analogy, "DOS van Hove" remains a defensible name for the mult-8 level (the framework's own `session-38` labels ONLY the mult-8 level "the van Hove singularity," not B1 or B3). The terminology is a finite-triple-analog call on which a reasonable reading can differ.

**This residue is genuine and I do not resolve it by fiat.** I judge that the canonical `rho_smooth` evidence (finite, framework-named "smooth") and the multiplicity≠order argument together make kk's reading the stronger one on the present evidence — but the question of what NOUN a finite-triple maximal-multiplicity δ deserves is a structural-terminological call that the present compute (W7-22, which proved `v_g ≠ 0` and `n=1`) does not settle, because W7-22 measured the ORDER (`Φ_dispersion`), not the noun-licensing question (whether a discrete maximal-multiplicity δ on a finite triple is categorically a "van Hove singularity"). **The proven physics — finite, large DOS edge → `N(0)` → BCS — is invariant under BOTH resolutions, which is the one thing both sides agreed on from the start.** The disposition above (RETAIN-physics, DEMOTE-"infinite-order"/"flat-band") holds under EITHER resolution of the residue; the residue only affects whether the re-worded row keeps the word "van Hove" as a label or replaces it with "maximal-multiplicity DOS edge." I route it to a compute gate (CF below) rather than forcing the noun, and the routed edit-text (Block 1) is written to be correct under either resolution (it uses "DOS-edge / maximal-multiplicity (mult-8) optical level" and scopes "van Hove" as the demoted/contested term).

### Same-functional discipline — the structural lesson

The entire dispute is a same-functional-fair-comparison instance. The refutation lives on `Φ_dispersion` (W7-22); the proven physics lives on `Φ_DOS`; the two are NOT transportable to each other (`cross-pillar-bridge-anatomy.md §"Diffusion-window-observable specialization"`, K=2, the `Φ_graph-Laplacian ≠ Φ_heat-trace` precedent). BUT — and this is the refinement both turns converged on — within `Φ_DOS` the decomposition `ρ = ρ_singular + ρ_continuum = 8·δ + 1/(π|v_g|)` shows the continuum branch is velocity-slaved (Claim B: `ρ_continuum · v_g = 1/π` EXACT, and the canonical `rho_smooth = 14.02` IS this branch at the measured `v_g`), while the singular branch is a fixed δ-WEIGHT carrying no ORDER. The "infinite-order van Hove" wording conflated (a) the order-language of a continuum singularity (object that does not exist; `n=1`), (b) the WEIGHT of a fixed degeneracy (the mult-8, which has no order), and (c) the finite velocity-slaved continuum DOS (`rho_smooth`, which is not a singularity). The disposition disentangles all three: retain (c) as the proven BCS driver, demote (a) and the "flat band" noun, and report (b)'s noun-licensing as the open residue.

---

## ROUTED EDIT (for doc-owner to land — `Classification-of-phonon-exflation.md:59`)

> **DO NOT land by me** — `Classification-of-phonon-exflation.md` editing is `mack-cosmic-bridge`'s sole-writer domain per housekeeping A33 / `feedback_mack-bridge-role.md`, and the registry-row disposition is outside the per-workshop-author landing scope. This block PRODUCES the exact disposition text; the orchestrator / doc-owner lands it.

The current row 59 reads:

```
| B2 flat band | Infinite-order Van Hove | S22c | 27 | PROVEN |
```

Replace with (5-column schema preserved: `Observable | Mechanism/reading | Session | Paper | Status`):

```
| B2 mult-8 optical band edge | Finite large BCS-driving DOS edge (rho_smooth = 14.02 M_KK⁻¹; the N(0) feeding g·N(0)=3.24, S22c; 43–51× enhancement, S28c). NOT a dispersionless "flat band" and NOT an "infinite-order van Hove": the band disperses LINEARLY (n=1, v_g(fold)=0.0227≠0) above a FIXED mult-8 Clifford/ℂ¹⁶ degeneracy; the canonical DOS is the finite velocity-slaved continuum branch (14.02 = 1/(π·v_g)), not a δ-divergence. The infinite-order / flat-band reading is REFUTED (W7-22). [Open: whether the mult-8 δ-WEIGHT licenses the noun "van Hove singularity" on a finite triple — see CF-S95-W2-VAN-HOVE-NOUN.] | S22c (DOS-edge g·N(0)); S28c (1D BCS theorem); W7-22 (dispersion + order scope, REFUTED) | 27, 16 | PROVEN (finite DOS-edge BCS driver); "infinite-order van Hove" + "flat band" DEMOTED (W7-22) |
```

Rationale for the doc-owner: this preserves every PROVEN, load-bearing thing (the DOS edge, `N(0)`, BCS — which the framework uses everywhere) and removes ONLY the two qualifiers that are (i) refuted on-functional by W7-22 and (ii) contradicted by the framework's own canonical `rho_smooth = 14.02 = 1/(π·v_g)`. The row text is written to be correct under either resolution of the open noun question: it leads with "DOS edge / mult-8 optical level," scopes "van Hove singularity" as the contested/open term, and cross-references the CF. The `Van Hove singularities | Phase transition classification | S34–44 | 27 | PROVEN` row (`:51`) and the `12 Van Hove trajectories` row (`:66`) are NOT touched by this disposition — they concern the phase-transition classification and band-topology counting, distinct from `proven_1086`'s band-edge DOS/dispersion claim; the doc-owner should leave them as-is.

---

## ROUTED CORPUS ROW (for the Slot-3 closeout to land in `cross-pillar-bridge-corpus.md §24`-sequence)

> **DO NOT write the corpus now.** Per the schedule's CRITICAL SEQUENCING note: §24 was ALREADY advanced this session by W4-2 (`S94-LQG-CDT-STAGE-2`, 5 LQG-CDT rows STAGE-2-VERIFIED, housekeeping A18/A26); §24 is currently K=2 after W6-19's ENRICH-no-advance companion at §24.2. The Slot-3 closeout lands this AFTER confirming W4-2's existing §24 STAGE-2 advancement, to avoid a K-counter collision. This block produces the row text + its classification only; it goes in the corpus file (NOT the rule file, per memory rule #14).

**Classification: ENRICH (no K-advance, observable-identity axis).** Per kk's T3 §5 flag and my T2 §3, the dispersion-vs-DOS pair this workshop surfaced is the SAME failure-mode genus as W7-3 / W6-19 — a criterion/value calibrated on one functional mis-carried to a structurally distinct functional — NOT a new failure-mode axis. It is an observable-identity-axis enrichment, identical in genus to the `Φ_graph-Laplacian ≠ Φ_heat-trace` precedent. It does NOT advance the §24 K-counter; it enriches the existing §24.2/§24.3 sequence as a companion instance. This keeps it from colliding with W4-2's §24 STAGE-2 advancement.

Candidate §24-sequence companion row (ENRICH; observable-identity axis):

```
### §24.x (ENRICH — observable-identity axis; no K-advance; companion to W7-3/W6-19) — dispersion-vs-DOS functional-identity pair (W-2, S94)

Genus: same-functional-fair-comparison failure at the OBSERVABLE-IDENTITY layer (Φ_A ≠ Φ_B; a criterion/value on Φ_A mis-carried to Φ_B). Same genus as the Φ_graph-Laplacian ≠ Φ_heat-trace precedent (§24 parent) and W7-3 / W6-19.

Instance: the B2 band-edge "infinite-order van Hove" claim (proven_1086, S22c) admits THREE distinct functionals that MUST NOT be conflated:
  Φ_dispersion       := v_g^{B2}(τ) / n_dispersion(τ)        — the van Hove ORDER (energy-axis scaling exponent γ_E = 1−1/n)
  Φ_DOS-continuum    := ρ_continuum = 1/(π|v_g|)             — the finite velocity-slaved DOS branch (canonical rho_smooth = 14.02 = 1/(π·v_g), EXACT, this T4 Sage-verified)
  Φ_DOS-singular     := ρ_singular = m·δ(E−E_0)              — the fixed multiplicity δ-WEIGHT (m=8; integrated weight ∫=8, NOT an order)
Mis-carriage mode A (kk T1): reading proven_1086 as a Φ_dispersion claim — fair against a dispersion claim, category error against a DOS claim.
Mis-carriage mode B (landau T2): promoting Φ_DOS-singular's multiplicity (WEIGHT) to a van Hove ORDER — a δ of any coefficient is equi-order (infinite); multiplicity ≠ order (kk T3 §2, conceded T4).
Resolution: ORDER lives on Φ_dispersion (= n=1, refuted as a singularity); the canonical proven DOS is Φ_DOS-continuum (finite, velocity-slaved, = 14.02 = 1/(π·v_g) at the W7-22 velocity to the digit); Φ_DOS-singular is a fixed δ-WEIGHT carrying no order. The "infinite-order van Hove" wording conflated all three.
Anchor: rho_B2_per_mode = 14.023250234055 (S37, canonical); 1/(π·rho) = 0.0226987239671 ≡ W7-22 ρ-pinned v_g(fold)=0.022699 (Sage-exact, residual 4.77e-7 = publication rounding); Z = ρ·v = 1/π = 0.318309886184 EXACT (eq_8045).
Disposition: proven_1086 RE-WORDED onto Φ_DOS-continuum + RETAINED (finite DOS-edge BCS driver); "infinite-order van Hove" + "flat band" DEMOTED (W7-22, on-functional for the order/dispersion claim).
K-status: ENRICH (no K-advance). Sibling of W7-3/W6-19 on the observable-identity axis; does NOT advance the §24 failure-mode-axis K-counter (currently K=2 post W4-2 / W6-19). Lands AFTER W4-2's S94-LQG-CDT-STAGE-2 §24 advancement to avoid collision.
```

---

## Carry-Forward (4-field spec)

The γ_E crystallization (`n=1` linear `γ_E=0` vs `n=2` √-edge `γ_E=1/2`) is ALREADY a W7 WP carry-forward (`CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION`) — NOT duplicated here. The S2-1 adjudication ran on the existing W7-22 evidence (`v_g ≠ 0` already proven); the crystallization is a separate compute, not a prerequisite, and the verdict above is verdict-only with respect to it.

ONE genuinely-new compute surfaced — the honest-non-convergence residue (the "van Hove" noun-licensing question) is not settled by W7-22's existing evidence and warrants its own gate rather than a forced terminological resolution:

```
CF-S95-W2-VAN-HOVE-NOUN — Noun-licensing for the B2 mult-8 δ-WEIGHT on a finite spectral triple
1. What:    Derive whether a fixed maximal-multiplicity δ-WEIGHT (m·δ(E−E_0), m=8, k-independent, τ-independent)
            on a FINITE spectral triple categorically licenses the noun "van Hove singularity," OR whether
            "van Hove" is reserved for an emergent continuum-band non-analyticity (a stationary point of a
            dispersing E(k) with a well-defined ORDER γ_E ∈ [0,1)). Test the finite-triple-analog claim:
            does the L_max→∞ continuum limit of the mult-8 level converge to a genuine continuum-DOS
            non-analyticity (licensing "van Hove"), or to a fixed representation-theoretic degeneracy
            (a group-theoretic multiplicity, NOT a band-structure singularity)? The discriminator is whether
            the bottom-multiplicity δ-WEIGHT and its energy spacing to the dispersing continuum admit a
            continuum-limit scaling that produces an energy-axis non-analyticity, vs remaining a discrete
            ℂ¹⁶ Clifford degeneracy at fixed E_0.
2. Inputs:  rho_B2_per_mode = 14.023250234055 (S37, canonical); W7-22 npz (S94-DS-GAMMA-E-RESOLUTION:
            v_g^B2(τ)-trajectory, bot_deg=4/sector at all τ, first_gap(τ), n_dispersion=1); the L_max=12
            master D_K cache (s84_spectrum_cache_L12_tau019.npz) for an L_max-scan of the (0,1)/(1,0)
            bottom multiplicity and its gap to the dispersing continuum; S85 cusp-gate provenance
            (S85-VAN-HOVE-CUSP-THEOREM, the framework's DISTINCT singular-wall object, for contrast).
3. Gate:    PASS = the L_max-scan shows the mult-8 δ-WEIGHT's gap to the continuum scales toward an
            energy-axis non-analyticity (continuum-DOS divergence; licenses "van Hove" as a finite-triple
            analog); FAIL = the mult-8 remains a fixed ℂ¹⁶ Clifford degeneracy at fixed E_0 with no
            continuum-limit non-analyticity (the noun "van Hove" is over-claimed; the honest label is
            "maximal-multiplicity DOS edge"); INFO = the L_max-scan is structurally saturated / inconclusive
            on the noun question (the terminological call is undecidable from the substrate spectrum alone).
            Pre-register the order/weight discriminator threshold at plan-freeze (γ_E-continuum-limit existence
            vs δ-WEIGHT fixity). NOTE: the disposition (RETAIN-physics + DEMOTE-"infinite-order"/"flat-band")
            is INVARIANT under all three outcomes; this gate ONLY decides the residual noun in the re-worded
            row, NOT the proven physics.
4. Effort:  Small–medium. L_max-scan of one Peter-Weyl sector pair on the existing master cache + a
            continuum-limit scaling fit; single-agent (landau or kk); ~1 wave. No new high-L_max irrep
            construction needed (the (0,1)/(1,0) bottom is in the L_max=12 cache; Friedrich-Bär/Casimir
            saturation check per math-scripts.md before any L_max≥13 pin).
```

---

## For the closeout (1-line summary)

**W-2 VERDICT**: `proven_1086` RE-WORDED onto `Φ_DOS-continuum` + RETAINED (finite DOS-edge BCS driver `rho_smooth=14.02=1/(π·v_g)`, `N(0)`→`g·N(0)=3.24`/S28c 43–51×); "infinite-order van Hove" + "flat band" DEMOTED (W7-22 on-functional: `v_g≠0`, `n=1`; + contradicted by the canonical finite `rho_smooth`, Sage-verified `= 1/(π·v_g)` to the digit + multiplicity≠order); routed edit-text for `Classification:59` (mack-cosmic-bridge to land) + ENRICH-not-advance §24 companion row (Slot-3 to land AFTER W4-2's §24 STAGE-2, no K-collision) + `CF-S95-W2-VAN-HOVE-NOUN` (the one honest-non-convergence residue: does the mult-8 δ-WEIGHT license the noun "van Hove" on a finite triple — invariant to the proven physics).

---

*End W-2 Turn 4 (landau-condensed-matter, balanced joint verdict + canonical output doc). Workshop W-2 CLOSED.*
