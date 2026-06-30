# W-2 Turn 1 — kaluza-klein (dispersion-refuted steelman)

**Workshop**: W-2 — disposition of registry claim `proven_1086` ("B2 flat band — Infinite-order Van Hove", S22c, `Classification-of-phonon-exflation.md:59`, Paper 27, status PROVEN).
**Turn**: T1 (Round 1, steelman). Agent A = `kaluza-klein-theorist` (owner of the band-dispersion refutation).
**Opponent**: `landau-condensed-matter-theorist` (DOS-degeneracy reading), responds T2.
**Mandate**: make the strongest case that S22c's "infinite-order van Hove" claim, read as the natural band-flattening/dispersion claim, is now REFUTED on-functional by W7-22 (`S94-DS-GAMMA-E-RESOLUTION`); place the burden on the DOS-reading to show S22c's proof actually lived on the DOS functional. **This is a steelman — I do NOT converge.**

---

## 0. Structure-first framing (the governing geometry)

Before any number: what is the geometric object, and on which functional does the van Hove ORDER live?

The B2 band is the substrate's fiber-excitation spectrum at the substrate-distance-2 region of the spectral triple `(A_K, H_K, D_K)`. Concretely (W7-22 Step 1; MCP-confirmed `E_B2_mean = 0.845269087679269`, S38), it is the modulus of the Dirac eigenvalue of `D_K` restricted to the Peter-Weyl `(0,1)/(1,0)` optical sectors, multiplicity 8 (= 2 sectors × 4-fold per sector), as a function of a band-level index `k`, at deformation parameter `τ`, in the NORMAL state `Δ=0`:

```
E_B2(k; τ) = |λ_{(0,1)/(1,0)}(k; τ)|.                                   (0.1)
```

This is a substrate-IS spectral observable. It is NOT a measurement IN a crystal container — the band IS the spectral content of the fiber, and `v_g`, the DOS, and any van Hove structure are all functionals OF `E_B2(k; τ)`. The direction of explanation flows substrate → emergent, never the reverse (`phononic-framing.md §"IS Space, Not IN Space"`).

A van Hove singularity is, by definition, a non-analyticity of the **density of states** `ρ(E)`. In one dimension (the operative case here — the B2 band disperses along a single discrete level-index direction, W7-22 Step 4),

```
ρ(E) = (1/π) · 1/|v_g(E)|,        v_g(E) := dE/dk.                       (0.2)
```

The ORDER of the van Hove singularity is fixed entirely by the leading-order behavior of the dispersion `E(k)` near its extremum `k_0`. Write the local Taylor expansion

```
E(k) = E_0 + c_n · (k − k_0)^n + O((k−k_0)^{n+1}),   c_n = first non-vanishing coeff.   (0.3)
```

Then `v_g ∝ (k−k_0)^{n−1}`, and the DOS power-law exponent is

```
γ_E = 1 − 1/n.                                                          (0.4)
```

- `n = 1` (finite velocity at the bottom, `c_1 ≠ 0`): `ρ` is a finite step. `γ_E = 0`. **No van Hove singularity at all** — the DOS is bounded.
- `n = 2` (quadratic extremum, `c_1 = 0, c_2 ≠ 0`): the canonical 1D van Hove. `v_g → 0`, `ρ ∼ |E−E_0|^{−1/2}` integrable inverse-square-root divergence. `γ_E = 1/2`.
- `n → ∞` (a genuinely FLAT band): `v_g ≡ 0` over a finite `k`-range, `ρ → δ(E−E_0)`. `γ_E → 1`. This is the **infinite-order van Hove**.

**The single load-bearing observation of this entire steelman:** in equation (0.4) the van Hove ORDER `n` — including the infinite-order limit — is a property of the DISPERSION FUNCTIONAL `E(k)`. The DOS divergence is a CONSEQUENCE of `v_g → 0`; it is not an independent input. Equation (0.2) is one-directional: the DOS is computed FROM the velocity. There is no DOS singularity without a corresponding flattening of `E(k)`. An "infinite-order van Hove" therefore makes a definite, falsifiable claim about the dispersion: `v_g → 0` at the relevant point.

This is the functional on which the vH order lives. The same-functional discipline (`cross-pillar-bridge-anatomy.md §"Diffusion-window-observable specialization"`, K=2; the `Φ_graph-Laplacian ≠ Φ_heat-trace` precedent) is satisfied by construction here: the discriminator
```
Φ_dispersion(τ) = v_g^{B2}(τ) / n_dispersion(τ)
```
is read ONLY where the van Hove order is defined — through `v_g` and the leading-order index `n` of `E(k;τ)`. I do NOT mis-carry the W7-3 heat-trace-window `v_g = 0.00751` (a DIFFERENT functional — a diffusion-window heat-trace estimate, not the band-dispersion `v_g`; W7-22 §"Same-functional fair-comparison compliance" makes this explicit).

---

## 1. What W7-22 measured, and what it found

W7-22 (`S94-DS-GAMMA-E-RESOLUTION`; INFO; verdict line 84, companion 85; `audit_sha256=1b71fb67a44eb9984fe3730fa8d150e356101a210cb1e268914957ca1cb6ddc4`, unique count 1) is the cleanest possible direct probe of `Φ_dispersion`. It computed `v_g^{B2}(τ)` at the band bottom `k_0`, NORMAL state `Δ=0`, across a ≥7-point `τ`-grid spanning `τ_fold=0.190`, by per-`τ` re-evaluation of the L_max=12 master `D_K` cache (verified `τ==s` to 3.775e-15 — the S84 cache `(0,1)` abs-eigenvalues reproduced bit-for-bit). The per-`τ` trajectory:

| τ | v_g (band-ladder c₁) | order-ratio \|c₁\|/\|c₂\|·Δk | n_disp | bot_deg | first_gap |
|:--|:--|:--|:--|:--|:--|
| 0.1500 | +0.06298 | 688.21 | 1 | 4 | 0.00533 |
| 0.1633 | +0.05935 | 46.87 | 1 | 4 | 0.00527 |
| 0.1767 | +0.05571 | 22.71 | 1 | 4 | 0.00515 |
| **0.1900 (fold)** | **+0.05410** | **18.93** | **1** | 4 | 0.00497 |
| 0.2033 | +0.05435 | 21.33 | 1 | 4 | 0.00474 |
| 0.2167 | +0.05453 | 24.13 | 1 | 4 | 0.00448 |
| 0.2300 | +0.05464 | 27.41 | 1 | 4 | 0.00417 |

ρ-pinned (substrate-natural, Claim-B): `v_g^ρ(fold) = 1/(π·ρ_B2_per_mode) = 1/(π·14.023250) = 0.022699` (M_KK).

The read-off against the two pre-registered thresholds is unambiguous:

1. **`v_g_floor = 1e-2`**: `|v_g(τ_fold)| = 0.0227` (ρ-pinned) AND `0.0541` (band-ladder). BOTH ≥ 2.3× the floor, at the fold AND at every `τ`-slice in `[0.15, 0.23]`. **`v_g` does NOT → 0.**
2. **`order-ratio < 0.1 ⇒ n=2`**: order-ratio at fold = `18.93 ≫ 0.1` (range 18.9–688 across the grid). **`n_dispersion = 1` (linear), NOT `n=2` √-edge.**

Two further structural facts from the same compute, both decisive against the infinite-order-vH dispersion reading:

3. **`first_gap` is monotone and never collapses.** `first_gap = |λ₂|−|λ₁| = 0.00497` at the fold, smooth, finite, monotonically *decreasing* in `τ` with NO cusp, NO local minimum, and NO approach to zero AT `τ_fold=0.190`. A flat-band bottleneck — even a soft one — would force `first_gap → 0` at the fold (degenerate levels merging into a dispersionless manifold). The data does the opposite: the gap is largest below the fold and shrinks *monotonically through it* with no feature at `τ_fold` whatsoever.

4. **The "mult-8 bottom" is a FIXED Clifford/ℂ¹⁶ degeneracy, not a dispersionless band.** `bot_deg = 4` per sector (8 combined) at ALL `τ`. This is the fixed spinor multiplicity of the ℂ¹⁶ representation space — it is the SAME 8 at `τ=0.15` and `τ=0.23`, with no `τ`-dependence and no band-flattening dynamics. The band DISPERSES linearly *above* this fixed-degeneracy bottom.

**Conclusion of §1:** every diagnostic that an infinite-order van Hove in the dispersion sense REQUIRES — `v_g → 0`, `n → ∞` (or at minimum `n ≥ 2`), `first_gap → 0` at the fold — is FALSIFIED. The B2 bottom is a finite-velocity LINEAR band edge with a fixed (not dynamical) bottom multiplicity. On `Φ_dispersion`, `proven_1086`'s "infinite-order van Hove" is not merely failing to reach the infinite-order limit — it is failing to reach even the *first* order (`n=1` is a bounded DOS step, NOT a singularity at all).

---

## 2. The opponent's own owner concurred on-functional — this is not a contested measurement

The DOS-reading owner, `landau-condensed-matter-theorist`, OWNS the refuted reading (the registry entry `proven_1086` is landau's; `Classification-of-phonon-exflation.md` is landau's document). In the W7-22 working paper, landau independently re-fit the npz and CONCURRED that the dispersion reading is refuted (WP §"Review by landau-condensed-matter-theorist", lines 91–93). I quote the concurrence verbatim because it removes any suggestion that the refutation is a one-sided artifact of my own (Reading-KK) bias:

> "I OWN the refuted reading; I CONCUR that Reading-van-Hove is genuinely refuted, no manufactured dissent. (a) Sensitivity is adequate on the discriminating axis. A genuine infinite-order vH flattening requires |v_g|→0 AT τ_fold; the npz shows |v_g| has only a shallow 16% *minimum* at the fold ... both ≥2.3× the floor ... no collapse. The decisive structural check is `first_gap`: it is 0.00497 at the fold, monotone-decreasing in τ with NO cusp/local-min/collapse AT τ_fold, never approaching 0. A flat-band bottom merging would force first_gap→0 there; it does the opposite. bot_deg=4/sector (mult-8) is FIXED at all τ — `proven_1086`'s 'flat band' conflated a fixed Clifford/ℂ¹⁶ bottom multiplicity with a dispersionless band; the band disperses *above* its degenerate bottom. The v_g→0 refutation is robust to the fit window."

And critically, landau also pre-empted the obvious escape (the `n=1` vs `n=2` fit fragility):

> "BUT the sqrt-edge model E=E₀+A√k (the n=2 vH signature) fits *worse* (0.077), and every window gives v_g=O(10⁻²)>0; the fragility is the 0-vs-½ KK sub-question, NOT van-Hove (which needs v_g→0 and loses regardless of polynomial order)."

This is the decisive structural point. The residual fit fragility (`|c₁|/|c₂|` swinging 0.91 → 1.50 → 18.93 across fit-window choice `n_fit ∈ {3,4,5}`) does NOT rescue the infinite-order-vH reading, because that reading needs `v_g → 0`, and `v_g` is bounded away from 0 in EVERY fit window. The fragility lives entirely on the orthogonal KK-internal sub-question of whether the dispersion is `n=1` (`γ_E=0`) or `n=2` (`γ_E=1/2`) — and even there the `√`-edge model (the `n=2` signature) fits WORSE than the linear model in every window. The infinite-order limit (`n → ∞`, `γ_E → 1`) is not even in contention: it is the furthest possible reading from a finite-`v_g` linear bottom.

**On the functional where the van Hove order lives, the refutation is mutual, robust, and fit-window-independent. There is no live dispute about the dispersion measurement itself.** The only question left open is the disposition of `proven_1086` given that measurement — which is the workshop's job.

---

## 3. The natural reading of "flat band → infinite-order van Hove" IS the dispersion sense

The DOS-reading defense (which landau will press in T2, per the brief) is that S22c proved the DOS-DEGENERACY sense — that the fixed mult-8 level is a `δ`-function pile-up in `ρ(E)`, an infinite-order singularity on a STRUCTURALLY DISTINCT functional `Φ_DOS-degeneracy` that W7-22's NORMAL-state `v_g` trajectory does not touch. I now argue why the burden of proof for that reading is heavy, and why the natural reading of the registry phrase is the dispersion sense.

### 3.1 The term "flat band" is, definitionally, a statement about dispersion

The registry entry is "**B2 flat band** → Infinite-order Van Hove" (`:59`). The subject of the claim — the thing of which "infinite-order van Hove" is predicated — is "the B2 **flat band**." A "flat band" is, in every standard usage in condensed-matter physics, a band whose energy `E(k)` is *independent of `k`* over a finite region of the Brillouin zone: `dE/dk = v_g ≡ 0`. That is precisely the `n → ∞` limit of (0.3). The phrase "flat band → infinite-order van Hove" is the textbook implication chain

```
flat band (v_g ≡ 0)  ⇒  ρ(E) = δ(E − E_0)  ⇒  infinite-order van Hove (γ_E → 1).   (3.1)
```

The arrow in (3.1) is the standard derivation: flatness (a dispersion property) IMPLIES the `δ`-function DOS (the singularity). The DOS singularity is the *consequence* of the flatness; it is not a separate fact. To read "B2 flat band" as a claim about a `δ`-pile-up DOS that holds EVEN WHEN the band is NOT flat (i.e. when `v_g ≠ 0`) is to sever the noun from the implication it heads. The registry author wrote "flat band," and "flat band" means `v_g = 0`. W7-22 shows `v_g ≠ 0`. On the plain reading, the antecedent of (3.1) is false, and the claim falls.

### 3.2 The framework's OWN pre-W7 treatment of the B2 van Hove was a DISPERSION treatment

This is the heaviest stone in the steelman. The DOS-reading must assert that S22c's proof established a DOS functional `Φ_DOS-degeneracy` distinct from the dispersion. But the framework's own record of how the B2 van Hove was treated — in the sessions surrounding and following S22c — is uniformly a DISPERSION treatment. I cite the knowledge base directly:

**(a) S34 (`session-34-baptista-collab.md`, §1.4)** defines the B2 van Hove velocity as
```
v_{B2} = dE_{B2}/dτ,
```
in the section titled "1.4 The van Hove singularity lives exactly at the fold center." The van Hove is characterized by a VELOCITY — a derivative of the dispersion. This is `Φ_dispersion`, not a DOS pile-up.

**(b) S53 (`session-53-baptista-volovik-workshop.md`)** states verbatim: "The Van Hove singularity at the B2 flat band. This is a property of the **Dirac eigenvalue flow λ(τ)**, independent of condensate physics." The van Hove IS a property of the eigenvalue FLOW — i.e. of how `λ` disperses in `τ`. W7-22's classification line is identical ("GEOMETRIC — property of the D_K eigenvalue flow λ(τ)"). Same functional.

**(c) S61 (`computations/session-61/s61_vanhove_dispersion_output.txt`, gate `VANHOVE-DISP-61`)** is the decisive provenance. The gate is *named* "Van Hove **Dispersion**." It computes the full B2 band structure `omega(k, τ)` (1600 Hamiltonians, 50 τ × 32 k), the group velocity `v_g = E_J(τ)`, the effective mass `m*_keff`, and the bandwidth — and it derives the DOS FROM the dispersion via `ρ_wall = 1/(π|v|)`. Its "FLAT BAND PROTECTION THEOREM" is stated as a property of the band Hamiltonian in `k`-space:
```
H_B2(k, τ) = H_B2(0, τ) + E_J(τ) · λ_k · I_4   ⇒  all 4 bands EXACTLY parallel at every τ;
                                                 ⇒  v_g = E_J(τ) for all bands (EXACT).
```
This is a statement about how the bands DISPERSE in `k` (they are parallel; their group velocity is `E_J(τ)`). It is a DISPERSION-functional theorem. The DOS in §6 of that output is computed downstream of the dispersion (`E_VH`, "DOS peak height," `dE_VH/dτ`) — exactly the one-directional dependence of (0.2): DOS is read OFF the dispersion.

**(d) S32 (`session-32-baptista-collab.md`)** confirms the LDOS framing is `ρ_wall = 1/(π|v|)`, "the correct 1D density of states for **a quadratic band extremum (or flat-band bottleneck)**." Note the parenthetical: the LDOS enhancement is the DOS of a quadratic extremum (`n=2`) OR a flat-band bottleneck (`n → ∞`) — both DISPERSION conditions. The DOS enhancement is *defined through* the velocity vanishing. There is no DOS singularity in the framework's own treatment that is not sourced by `v → 0`.

**The pattern is unbroken:** every framework treatment of the B2 van Hove from S32 through S61 reads it on the dispersion functional — velocity (`v_{B2} = dE/dτ`, `v_g = E_J`), eigenvalue flow `λ(τ)`, band structure `omega(k,τ)`, effective mass — with the DOS derived downstream. The DOS-reading must therefore claim that the *original S22c proof* established a DOS functional that the framework's own subsequent treatments uniformly DID NOT use, and which is independent of the velocity that all of those treatments computed. That is a strong claim, and the burden is on the DOS-reading to exhibit S22c's proof and show it lived somewhere other than `Φ_dispersion`.

### 3.3 The Claim-B cancellation REMOVES the DOS from the discriminating content

There is a deeper structural reason the DOS cannot be an independent functional carrying the van Hove order. W7-22 Claim B established, to residual `0.0e+00`:
```
Z(τ) = ρ_B2 · v_g = [1/(π|v_g|)] · |v_g| = 1/π,   INDEPENDENT of n_dispersion and τ.    (3.2)
```
This is the impedance-product identity (`session-32-w4-r2-qa-landau.md`: "DOS divergence (ρ~1/(π·v)) and velocity vanishing (v→0) cancel exactly"). The substantive content of (3.2): the DOS `ρ_B2 = 1/(π|v_g|)` and the velocity `v_g` are NOT independent functionals — they are reciprocal, and their product is a `τ`- and `n`-independent constant `1/π`. The DOS carries NO discriminating content about the van Hove order beyond what `v_g` already carries; it is the *reciprocal image* of the velocity. The order `n` is read from `v_g` (the un-cancelled probe), and the DOS is `v_g`'s reciprocal — they encode the SAME information.

This is fatal to a "structurally distinct DOS functional" defense at the level where the van Hove ORDER lives: if the DOS pile-up were an *independent* functional, its product with `v_g` would not be a constant — it would carry residual `τ`-structure. The fact that `ρ_B2 · v_g = 1/π` exactly means the DOS is *slaved* to the velocity. An infinite-order DOS singularity (`ρ → δ`) is, via (3.2), the statement `v_g → 0` — which W7-22 refutes. The DOS-reading cannot have it both ways: either the DOS is slaved to `v_g` (in which case `ρ → δ` requires `v_g → 0`, refuted), or the DOS-reading must point to a genuinely DIFFERENT functional that is NOT `1/(π|v_g|)` — and then it owes us the definition of that functional and a demonstration that S22c's proof established IT.

### 3.4 A fixed degeneracy is a multiplicity, not a singularity-of-order

The DOS-reading's physical content is: "the fixed mult-8 level IS a δ-function pile-up in `ρ(E)`." I grant that a degenerate level contributes a `δ`-function to the DOS at the level energy — every discrete eigenvalue does, on a finite spectral triple. But this is a category confusion with the van Hove ORDER. On a finite (L_max=12) spectral triple, the spectrum is discrete and EVERY level is a `δ`-function in `ρ(E)`; the B1 ground tone (mult 1), the B3 sector (mult 3), and the (0,0) singlet are ALL `δ`-functions in the finite-rank DOS. A `δ`-function from a fixed multiplicity is a property of the *finite cardinality of the spectrum*, not a van Hove singularity. The van Hove ORDER `γ_E` (0, 1/2, or → 1) is defined by the *continuum* DOS exponent that emerges as the band is resolved in `k` — i.e. by the dispersion (0.4). The mult-8 degeneracy is `τ`-independent and `k`-independent; it has no order `n` because it does not disperse. Calling a fixed multiplicity an "infinite-order van Hove" conflates the trivial `δ`-content of any discrete level with the non-trivial flat-band limit `n → ∞` — which is exactly the conflation W7-22 (and landau's own concurrence, §2) diagnosed: "`proven_1086`'s 'flat band' conflated a fixed Clifford/ℂ¹⁶ bottom multiplicity with a dispersionless band."

For the DOS-reading to survive, landau must show that S22c proved something about the DOS that is NOT (i) the trivial `δ`-content of a discrete level (which any finite spectrum has and which carries no van Hove order), and NOT (ii) the reciprocal image `1/(π|v_g|)` of the velocity (which (3.2) shows is slaved to `v_g` and hence refuted by `v_g ≠ 0`). The DOS-reading needs a THIRD object — an infinite-order DOS singularity that is neither finite-spectrum-trivial nor velocity-slaved. The burden is on landau to exhibit it in the S22c proof.

---

## 4. The disposition this steelman supports

On the dispersion functional `Φ_dispersion = v_g^{B2}(τ)/n_dispersion(τ)` — the functional on which the van Hove ORDER lives by definition (0.4), and on which the framework's own S22c-era treatment uniformly read the B2 van Hove (§3.2) — `proven_1086`'s "infinite-order van Hove" claim is REFUTED:

- `v_g(τ_fold) = 0.0227` (ρ-pinned) / `0.0541` (band-ladder), BOTH ≥ 2.3× the `1e-2` floor at every `τ`-slice; `v_g` does NOT → 0 (the infinite-order requirement);
- `n_dispersion = 1` (order-ratio 18.93 ≫ 0.1) — a finite-velocity LINEAR bottom, `γ_E = 0` (NOT a singularity at all, let alone infinite-order);
- `first_gap` monotone, never → 0 at the fold (no flat-band merging);
- the mult-8 bottom is a FIXED Clifford/ℂ¹⁶ degeneracy (a multiplicity, not a dispersionless band);
- the refutation is robust to fit-window choice and was independently CONCURRED by the registry entry's own owner;
- the `√`-edge (`n=2`) model fits WORSE than linear — the infinite-order limit (`n → ∞`) is the furthest possible reading from the data.

**Therefore `proven_1086` should be DEMOTED, or its scope clarified to the dispersion layer where the claim is now falsified.** If the registry intends "B2 flat band → infinite-order van Hove" as a band-flattening/dispersion claim — which is the natural reading of "flat band" (§3.1) and the reading every framework treatment from S32–S61 used (§3.2) — then it is REFUTED on-functional, and the PROVEN status is no longer defensible at the dispersion layer.

**The burden for the alternative is heavy and specific.** For the DOS-degeneracy reading to RETAIN `proven_1086` (re-worded onto a DOS functional that W7-22 leaves untouched), landau must in T2 discharge ALL of the following:

1. **Exhibit the S22c proof** and show what it actually established — not what the phrase "infinite-order van Hove" could in principle mean, but what S22c's computation proved.
2. **Show that proof lived on a functional `Φ_DOS-degeneracy` that is NOT `Φ_dispersion`** — i.e. NOT the velocity / eigenvalue-flow / band-structure functional that S34, S53, S61, S32 all used (§3.2).
3. **Show that `Φ_DOS-degeneracy` is NOT the velocity-slaved reciprocal `1/(π|v_g|)`** — because (3.2) proves that object carries no information beyond `v_g`, and an infinite-order singularity in it requires `v_g → 0`, which is refuted (§3.3).
4. **Show that `Φ_DOS-degeneracy` is NOT the trivial finite-spectrum `δ`-content** that every discrete level on the L_max=12 triple carries — because that content has no van Hove ORDER and would make "infinite-order van Hove" a label for a property the (0,0) singlet and B1/B3 sectors share (§3.4).

Absent a positive demonstration of all four, the natural reading stands, and `proven_1086` is a dispersion claim now refuted on-functional. The disposition this steelman supports is **(i) DEMOTED / scope-clarified to the dispersion layer; W7-22's on-functional refutation stands.**

---

## 5. Pre-emption note (sharpening the question, NOT conceding it)

I anticipate landau's strongest T2 move: that the registry CONTEXT — specifically `Classification-of-phonon-exflation.md §IV.D` ("Flat band → α=1, C~T from flat DOS") and §V.D (the van Hove near-crossing concentrating the DOS to spike BCS pairing) — frames the B2 flat band thermodynamically, through the DOS, suggesting S22c's proven content was the DOS pile-up driving the specific-heat exponent / BCS enhancement.

I do not concede this, and I flag two reasons it does not rescue the infinite-order claim on the dispersion functional, leaving them for T3:

- **(α)** §IV.D's "flat band → α=1, C~T from flat DOS" is itself the implication chain (3.1): the "flat DOS" is the CONSEQUENCE of flatness (`v_g = 0`). The thermodynamic content `C ~ T` is *derived from* the flat dispersion. If `v_g ≠ 0` (W7-22), the antecedent fails and the `α=1` flat-band thermodynamics does not follow — indeed §IV.D itself notes the flat-band `α=1` OVER-predicts the observed DM/DE ratio by 2.75× and is "too small / none match," i.e. the framework does not actually use the flat-band DOS as a confirmed thermodynamic anchor. The DOS-reading cannot lean on §IV.D as established physics that W7-22 leaves intact; §IV.D is itself dispersion-sourced and is not a confirmed result.

- **(β)** §V.D's van Hove near-crossing (T3/T4/T5 trajectories within `δ=0.0008`) "concentrates the DOS, spiking the BCS pairing" — but this is the BCS-gap mechanism, a CONDENSATE-state quantity (`Δ(τ)`), whereas the van Hove ORDER is a NORMAL-state (`Δ=0`) property of `E(k)`. The DOS concentration that spikes pairing is real, but it is (again) `1/(π|v|)` near a near-crossing — velocity-slaved, refuted by `v_g ≠ 0`. More importantly, conflating the *BCS-pairing DOS enhancement at a near-crossing* with the *infinite-order van Hove ORDER of the B2 band bottom* is a same-functional violation in its own right: the near-crossing DOS spike (a condensate-physics functional) is not the band-bottom dispersion order (a NORMAL-state geometric functional, W7-22's classification). These are different functionals, and the van Hove ORDER lives only on the latter.

These pre-emptions are not the burden-discharge of §4 items 1–4; they only sharpen WHY the natural reading is the dispersion sense and WHY the DOS-context citations are themselves dispersion-sourced. The full rebuttal awaits landau's T2 positive case for `Φ_DOS-degeneracy`.

**I do not converge in this turn.** The strongest case is on the table: S22c's "infinite-order van Hove" is, on its natural reading and on the framework's own S22c-era treatment, a DISPERSION claim; W7-22 refutes it on-functional (`v_g ≠ 0`, `n=1`, `first_gap` never collapses, mult-8 fixed); the disposition is DEMOTION / dispersion-layer scope-clarification unless landau discharges the heavy and specific four-part burden of §4.

---

*End W-2 Turn 1 (kaluza-klein, dispersion-refuted steelman). Next: T2 — landau steelmans DOS-stands + rebuts.*
