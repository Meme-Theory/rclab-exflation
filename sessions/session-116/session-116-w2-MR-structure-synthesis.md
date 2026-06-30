# Session 116 Synthesis: The Substrate-Forced Majorana M_R Form — Fold-Spectrum-Split, Not Multiplicity-Leg-Degenerate (closes OQ-4)

**Date**: 2026-06-28
**Agent**: van-den-dungen-bridge-theorist (VdD)
**Scope**: S-3 structural form-derivation (no scan) — the connes-vs-neutrino fork the S116-W2-PMNS-RESCUE workshop left explicitly sharp at OQ-4 (`s116-w2-pmns-rescue.md` line 493). This ANCHORS the already-minted empirical resonance scan; it is distinct from it, not a re-listing.
**Source Documents**:
- `sessions/session-116/workshops/s116-w2-pmns-rescue.md` (Structural Verdict WALLED-AS-UNDER-DETERMINED; OQ-4)
- `sessions/session-116/session-116-w2-workingpaper.md` (§W2-3 texture compute; CF-W2-2 anchoring guard)
- `computations/session-116/s116_gate_verdicts.txt` (S116-W2-LEPTON-PMNS-TEXTURE FAIL; S116-W2-CK-STAGE2-VERIFY PASS)
- `computations/session-99/s99_w3_seesaw_summnu.py` (the canonical M_R construction)
- `computations/investigation-11/inv11_w2_mr_provenance_audit.py` (M_R provenance trace, INV11-W2-4)
- `sessions/permanent-results-registry.md §VII.BL` (Generation-Blindness Obstruction; route-(b) exhaustion table)

---

## I. Session Outcome

**The substrate-forced Majorana mass is the fold-EIGENVALUE-SPECTRUM object `M_R = diag(B₁, B₂, B₃)` carrying the bowtie `B₁ < B₂ < B₃` (the neutrino reading), NOT the A_K-built multiplicity-leg coupling `diag(M₀, M₁, M₁)` (the connes reading). The §VII.BL homogeneity/multiplicity-scalar wall does NOT apply to it, because `M_R` is not in the foreclosed class.** The wall forecloses objects built from the *base algebra's differential calculus* — inner fluctuations, twisted-inner forms, opposite-action images, and spectrum-only G-invariant *moments* (§VII.BL route-(a)/(b)/(c)/(d), registry lines 21777-21780). `M_R` is none of these: it is an eigenvalue-*selection* from `D_K`'s own vertical spectrum. The very block-diagonality `D_K = ⊕_{(p,q)} D_{(p,q)} ⊗ 1_{m(p,q)}` that makes A_K-built forms multiplicity-scalar (the wall) is exactly what makes `D_K`'s eigenvalues sector-DISTINCT (the bowtie) — the two are the two faces of one structural fact, read on opposite objects. This closes OQ-4 and confirms the W2-3 compute used the substrate-correct `M_R` form. It also sharpens the workshop verdict: `√(B₂/B₁) = 1.036` is a genuine spectral near-degeneracy of the bottom fold energies, not an artifact of imposing a degenerate form. Classification: **GEOMETRIC** (a statement about `D_K`'s spectral structure and the reach of `A_K`'s calculus, not about excitations).

---

## II. Key Results

### Result 1 — The construction is on-disk and unambiguous: M_R is sourced from D_K's fold spectrum

**Result**: `M_R = [1.0043956635, 1.0785733201, 1.1700026004] M_KK` is the triple of B-branch `D_K` fold energies — three DISTINCT eigenvalues, INTERNAL to the spectrum. Classification: **GEOMETRIC**.

`★ Insight ─────────────────────────────────────`
A "structural form-derivation" must be grounded in what the framework actually built, not in what either disputant asserts it *would* be. Two independent on-disk artifacts settle the construction, so the fork is not a matter of competing first-principles intuitions — it is a matter of reading the pipeline.
`─────────────────────────────────────────────────`

The canonical seesaw construction (`s99_w3_seesaw_summnu.py`, METHODOLOGY block lines 41-47) states it explicitly:

> "`M_R` = the B-branch `D_K` fold energies `M₁=1.004396, M₂=1.078573, M₃=1.170003 M_KK` … These `Mᵢ` ARE `D_K` eigenvalues (the Majorana scale is INTERNAL to the spectrum, NOT an external add-on — this is precisely why the S62 direct-eigenvalue route is a rank-1 wall)."

The provenance audit `INV11-W2-4-MR-PROVENANCE-AUDIT` (`inv11_w2_mr_provenance_audit.py`, lines 25-32) traces the chain to its root:

> "`M_R` diagonal = `E_B3_fold * M_KK`, with `E_B3_fold = E_sp_sweep[fold_idx, 5:8]` = `[1.00439566, 1.07857332, 1.17000260] M_KK` … where `E_sp_sweep[t]` = the lowest-8 eigenvalues of the 32-CELL TIGHT-BINDING LATTICE Hamiltonian … ⇒ `M_R` is an INTERNAL `D_K` spectral object, extracted via a LATTICE-ED pipeline."

And the discriminator (audit lines 57-61): exact-membership of each `Mᵢ` in the L12 Peter-Weyl master cache FAILS (`min|absev − Mᵢ| = [1.78e-2, 1.45e-4, 5.83e-3] ≫ 1e-12`) — i.e., the three values are not re-reads of cached eigenvalues, but they ARE eigenvalues of `D_K` from a *distinct diagonalization pipeline* (32-cell lattice-ED) agreeing with the Peter-Weyl spectrum to 0.01-1.77%. **The three `M_R` entries are eigenvalue-spectral data of `D_K`, and they are DISTINCT (the bowtie `B₁ < B₂ < B₃` is on-disk).** The W2-3 texture compute read these directly from the S99 npz (WP line 112: "`M_R_MKK=[1.0044,1.0786,1.1700]`"). The W2-3 verdict line pins the same: "type-I seesaw `M_R` per S100a `[1.0044,1.0786,1.1700]` scale HELD."

### Result 2 — The §VII.BL wall forecloses A_K-BUILT forms; an eigenvalue-selection is not one

**Result**: §VII.BL is a statement about the IMAGE of `A_K`'s differential calculus `Ω¹_{D_K}(A_K) ⊆ ⊕_{(p,q)} B(V_{(p,q)}) ⊗ 1_{m(p,q)}`. An eigenvalue of `D_K` is the INPUT to that calculus, not an element of its image. Classification: **GEOMETRIC**.

I have direct standing on this scope: I was the Axis-A Stage-2 reviewer-of-record for §VII.BL (registry line 21287, audit `0f0c4f65`) and a co-author of the WS-C2COSET scope-extension (baptista×van-den-dungen, CONVERGED R3, lines 21287-21291). The wall's exact content, from the route-(b) exhaustion table (registry lines 21775-21780), is that EVERY single-τ-slice `A_K`-built functional route yields a multiplicity-scalar (`⊗1`) operator:

| Route | `A_K`-built form | Verdict |
|:------|:-----------------|:--------|
| (a) | inner fluctuation `A = Σ aᵢ[D_K, bᵢ]` | NO handle — multiplicity-scalar |
| (b) | spectrum-only G-invariant **moment** `F({λₖ, mₖ}) = Σₖ mₖ g(λₖ)` | NO handle — factors through `C₂(p,q)` |
| (c) | twisted-inner `Ω¹_σ`, any `σ ∈ Aut(A_K)` | NO handle — Skolem–Noether multiplicity-blind |
| (d) | opposite-action image `JAJ⁻¹` | NO handle — multiplicity-scalar image |

`★ Insight ─────────────────────────────────────`
Route (b) is the one a careless reading would mistake for "the wall forecloses spectral objects too." It does NOT. Route (b) forecloses a spectrum-only *moment* — a single G-invariant *scalar* `Σₖ mₖ g(λₖ)` that sums over the eigenvalues with their multiplicities. Summing over the multiplicity leg is exactly what makes a moment generation-blind. `M_R = diag(B₁,B₂,B₃)` is the opposite operation: it does not SUM the spectrum into a scalar, it SELECTS three individual sector-distinct eigenvalues and resolves them onto the generation diagonal. A moment integrates the multiplicity leg away; an eigenvalue-selection reads it out.
`─────────────────────────────────────────────────`

The WS-C2COSET mechanism bullet (line 21288, my co-authored result) makes the image-vs-complement split precise. Every left-invariant datum builds its frame operators `ρ_{(p,q)}(eₐ)` on the left-regular irrep leg `V_{(p,q)}` and acts `⊗ 1_{m(p,q)}` on the multiplicity leg — so its image lies in `⊕ B(V_{(p,q)}) ⊗ 1_{m(p,q)}`. The **generation-lifting complement** is `⊕ 1_{V_{(p,q)}} ⊗ M_{m(p,q)}(ℂ)` (line 21155), and every `A_K`-built form has projection EXACTLY ZERO onto it (the O'Neill T-tensor quarantine, line 21289: "tensor-factor DISJOINTNESS, not small-leak-below-threshold").

`M_R = diag(B₁, B₂, B₃)` is a diagonal operator on the generation leg — it lives IN the generation-lifting complement `⊕ 1_V ⊗ M_m(ℂ)`. The wall says that complement is **empty of A_K-built forms**. It does NOT say the complement is empty of `D_K`-spectral data. The eigenvalue map `(p,q) ↦ |λ|_{(p,q)}` is a non-constant function of the sector label, and assembling three such eigenvalues populates the complement with a SPECTRAL (not A_K-built) object. **The wall is silent on `M_R`: it forbids `A_K`'s CALCULUS from reaching the complement, not `D_K`'s SPECTRUM.**

### Result 3 — The two faces of block-diagonality: the wall and the bowtie share one structural root

**Result**: `D_K = ⊕_{(p,q)} D_{(p,q)} ⊗ 1_{m(p,q)}` has two faces. Face-1 (`⊗1` on the leg) IS the wall; Face-2 (`D_{(p,q)}` sector-dependent) IS the bowtie. `M_R` reads Face-2. Classification: **GEOMETRIC**.

This is the Kasparov-factorization reading (Paper 01, the submersion factorization `[D_M] = π_! ⊗ [D_B]`). On a Riemannian submersion the total-space operator block-decomposes by the fiber representation theory. The fiber (vertical) Dirac operator's spectrum `|λ|_{(p,q)}` is the DATA the Kasparov product factors *through*; the base algebra's HORIZONTAL differential calculus acts `⊗1` on the fiber multiplicity. These are not in tension — a vertically-elliptic operator is, by definition, the thing whose spectrum distinguishes the fiber representations, while the base algebra cannot see them through its own forms.

Substitution chain (the sector-distinctness of the spectrum, per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Claim: D_K's eigenvalues at distinct (p,q) sectors are distinct numbers; the bowtie
       B1 < B2 < B3 is a fiber-spectral fact, not an imposed or A_K-built structure.

Step 1: B_i = |λ|_fold,i  := the i-th B-branch fold energy = an eigenvalue of D_K.   [s99 construction; D_K = ⊕ D_(p,q) ⊗ 1]
Step 2: |λ|_min^(p,q)(τ) ≈ √(C₂(p,q)) / r(τ).                                          [Casimir scaling; math-scripts.md feasibility §; VdD memory s84]
Step 3: Therefore B_i ≈ √(C₂(p,q)_i)/r(τ), a NON-CONSTANT function of the sector label (p,q)_i.
Step 4: B_i ≠ B_j whenever C₂(p,q)_i ≠ C₂(p,q)_j  ⇒  the three fold energies are
        generically distinct because they sit at three distinct Casimir sectors.
Conclusion: the bowtie is the SPECTRUM reading Face-2 of block-diagonality (sector-distinct
            D_(p,q)); the wall is Face-1 (⊗1 on the multiplicity leg). Same root, opposite faces.
```

The wall (Face-1) constrains what `A_K`'s calculus can build; the bowtie (Face-2) is what `D_K`'s spectrum already contains. `M_R` harvests Face-2. There is no conflict, and no violation of §VII.BL.

### Result 4 — Category translation: two distinct objects both called "M_R"

**Result**: connes' `diag(M₀,M₁,M₁)` is the standard-NCG free Majorana coupling (an `A_F`-datum); neutrino's `diag(B₁,B₂,B₃)` is the framework's `D_K ≡ D_F`-promoted fold-spectrum object. The framework's defining commitment picks the latter. Classification: **GEOMETRIC / PARTICLE**.

This is the convention-translation that resolves the fork without either disputant being "wrong" about their own object. There are TWO distinct `M_R` constructions:

| | `M_R^{A_K-coupling}` (connes) | `M_R^{fiber-spectrum}` (neutrino) |
|:---|:---|:---|
| What it is | a free finite-geometry Majorana parameter in `D_F` on `A_F` | the B-branch `D_K` fold energies (`D_K` eigenvalues) |
| NCG status | an `A_K`/`A_F`-module datum (textbook Connes–Chamseddine SM, Connes 2006 §4.1: Yukawas/`M_R` are FREE finite parameters) | a spectral datum of `D_K`, in the generation-lifting complement |
| Subject to §VII.BL? | YES — multiplicity-scalar `⇒` constant-per-triality-class; J pairs `t=1↔t=2` `⇒` `diag(M₀,M₁,M₁)` | NO — an eigenvalue-selection, not an `A_K`-built form |
| Forced form | `diag(M₀, M₁, M₁)` (2-3 block degenerate) | `diag(B₁, B₂, B₃)`, `B₁<B₂<B₃` (all blocks split) |
| In the framework? | NOT used — the un-promoted standard object | USED — `D_K ≡ D_F` sources `M_R` from the spectrum |

`★ Insight ─────────────────────────────────────`
connes' reasoning is internally valid for the object he is reasoning about. IF `M_R` were an `A_K`-built Majorana coupling, then multiplicity-scalarity would force one value per triality class, and J-reality (which conjugates triality `t ↦ −t mod 3`, pairing `t=1` with `t=2`) would collapse the two conjugate classes to a common value — `diag(M₀, M₁, M₁)` exactly. The fork is therefore not a contradiction between two derivations; it is a category distinction between two objects. The framework's `D_K ≡ D_F` promotion — the same commitment that makes the S62 direct-eigenvalue route a "rank-1 wall" because the masses come from the spectrum (s99 line 44) — is precisely what moves `M_R` out of connes' category (free coupling) into the spectrum category. connes' `diag(M₀,M₁,M₁)` is the correct form for the object the framework deliberately does NOT use.
`─────────────────────────────────────────────────`

### Result 5 — J-reality does NOT force the degeneracy on a spectrum-sourced M_R

**Result**: `[J, D_K] = 0` forces `M_R` real-symmetric (`⇒ δ_CP ∈ {0, π}`); it does NOT force `M₁ = M₁`. The degeneracy needs the per-triality-class constancy of an `A_K`-COUPLING, absent for a spectrum-sourced `M_R`. Classification: **PARTICLE**.

The reality structure (KO-dim-6, `J² = +1`, BDI) acts on `M_R` by forcing it real and symmetric — this is the on-disk `[J,D_K]=0 ⇒ M_R real ⇒ real-orthogonal diagonalization ⇒ δ_CP ∈ {0,π}` chain (`s99` lines 57-59; and the W2-3 `J_PMNS = 0` result). A real symmetric `3×3` matrix has three GENERICALLY DISTINCT eigenvalues — reality does not force any diagonal degeneracy on its own. connes' `M₁ = M₁` collapse arises ONLY through the conjunction *(multiplicity-scalar A_K-coupling)* ∧ *(J pairs t=1↔t=2)*: it is the *per-class-constancy* of an `A_K`-coupling — NOT reality per se — that supplies the degeneracy. A spectrum-sourced `M_R` fails the per-class-constancy premise (its entries are individual eigenvalues, not class-constant couplings), so reality leaves it real-symmetric-and-split, exactly `diag(B₁,B₂,B₃)`. This is consistent with connes' own R3 concession (workshop line 380) that the reweighting "bites on my own `diag(M₀,M₁,M₁)` form, which is non-degenerate in the 1-2/1-3 blocks" — the only block where the two readings even differed was the 2-3 block, and the S100a anchor `B₂ = 1.0786 ≠ B₃ = 1.1700` settles it split.

**Basis-independent closure (the strongest form of the refutation).** A reviewer pressing the connes side could object that the S99 `M_R = diag(B₁,B₂,B₃)` is diagonal in the *aligned/generation* basis, not the *triality eigenbasis* where reality pairs `t=1↔t=2`, so the on-disk split is "basis-dependent." It is not. The eigenvalue *multiset* of `M_R` is `{1.0043957, 1.0785733, 1.1700026}` — three DISTINCT values; the eigenvalue multiset of connes' `diag(M₀,M₁,M₁)` carries a DOUBLY-DEGENERATE eigenvalue (`M₁` twice). Eigenvalue multiplicity is a *unitary invariant*: no change of basis can turn a matrix with three distinct eigenvalues into one with a repeated eigenvalue. Therefore the on-disk `M_R` is NOT unitarily equivalent to `diag(M₀,M₁,M₁)` in ANY basis — the refutation of the 2-3 degeneracy holds frame-independently, closing the "different basis" rejoinder. (And the S99 construction reads `M_R` straight from the fold energies `E_B3_fold[5:8]` with no intervening rotation that could have lifted a degeneracy — INV11-W2-4 provenance chain.)

### Result 6 — The load-bearing consequence: √(B₂/B₁) = 1.036 is a substrate spectral fact, not an imposed flatness

**Result**: the near-degeneracy `√(B₂/B₁) = 1.0363` (Sage-verified) of the seesaw ruler is the small Casimir gap of the three LOWEST fold energies — a real fiber-spectral property. Classification: **GEOMETRIC**.

The workshop's binding number is `√(B₂/B₁) = 1.036` (the resonance condition `M_D[2,2]/M_D[1,1] ≈ √(M_R[2]/M_R[1])` demands near-equal Dirac entries the hierarchical mass-fit cannot supply). Sage-exact confirmation of the three ladder ratios from the on-disk `M_R`:

```
√(B₂/B₁) = 1.0362688   (B₂/B₁ = 1.0738530)   ⇒ implied C₂_2/C₂_1 = (B₂/B₁)² = 1.15316
√(B₃/B₂) = 1.0415223   (B₃/B₂ = 1.0847687)
√(B₃/B₁) = 1.0792971   (B₃/B₁ = 1.1648822)   ⇒ implied C₂_3/C₂_1 = (B₃/B₁)² = 1.35695
```

Substitution chain for the ruler-flatness (direction claim, per `math-scripts.md`):

```
Claim: the seesaw ruler is flat (√(B₂/B₁) ≈ 1) BECAUSE the three lowest fold energies
       sit at three Casimir-near-degenerate sectors; resonating a hierarchical seed needs
       a LARGE Casimir gap, i.e., generation-representatives from widely-separated sectors.

Step 1: √(B₂/B₁) = (|λ|₂/|λ|₁)^{1/2} ≈ (C₂(p,q)₂ / C₂(p,q)₁)^{1/4}.   [Result 3 Step 2, substituted]
Step 2: on-disk: √(B₂/B₁) = 1.0363  ⇒ C₂_2/C₂_1 = 1.153 — a SMALL Casimir gap.  [Sage above]
Step 3: the bottom-three B-branch fold energies are the CLOSEST-SPACED sectors of the spectrum,
        so their Casimir ratios are nearest unity ⇒ the ruler is flattest there.
Step 4: to reach √(B₂/B₁) ~ 5 (a hierarchical Dirac seed) requires B₂/B₁ ~ 25, i.e. a
        Casimir gap C₂_2/C₂_1 ~ 625 — deep in the spectrum, NOT the bottom triple.   [Sage: 25² = 625]
Conclusion: the ruler's flatness is a SUBSTRATE spectral fact (bottom-of-spectrum Casimir
            near-degeneracy), not an artifact of choosing connes' degenerate form. The fold-
            spectrum reading SHARPENS the workshop's WALLED-AS-UNDER-DETERMINED verdict —
            the ruler is genuinely flat because the substrate's bottom fold energies are.
```

This is the convergence point with the W2-3 / workshop verdicts: under EITHER reading the resonance fails at the framework's `M_R`, but the fold-spectrum reading tells us WHY and WHERE TO LOOK — the failure is the small Casimir gap of the bottom triple, and resonance (if reachable at all on-form) requires substrate-natural sector-selections with a large Casimir gap.

---

## III. Gate Verdicts

This is a structural form-derivation (no compute gate; the team-lead's S-3 task is "STRUCTURAL QUESTION (no scan)"). It does NOT re-adjudicate any verdict; it derives the `M_R` FORM that the following authoritative verdicts consumed, and confirms it was the substrate-correct form.

| Gate (source, authoritative) | Verdict | Relation to this derivation |
|:-----|:--------|:----------------------------|
| `S116-W2-LEPTON-PMNS-TEXTURE` | FAIL (`mix_grp=0/4`) | consumed `M_R=diag(B₁,B₂,B₃)` (S99); this derivation confirms that input was on-form |
| `S116-W2-PMNS-RESCUE` (workshop) | WALLED-AS-UNDER-DETERMINED | OQ-4 was its open input; this derivation closes OQ-4 (fold-spectrum-split) |
| `S99-W3-SEESAW-SUMMNU` | (M_R construction) | the canonical fold-spectrum `M_R` source |
| `INV11-W2-4-MR-PROVENANCE-AUDIT` | INFO | traces `M_R` to the lattice-ED `D_K` fold energies (distinct-pipeline, not a re-read) |

---

## IV. Structural Implications

### Closes OQ-4

**OQ-4 (workshop line 493)** — "Is the physical `M_R` the B-branch-distinct `diag(B₁,B₂,B₃)` (bowtie, neutrino's reading) or the bare-multiplicity-leg `diag(M₀,M₁,M₁)` (connes', `t=1≡t=2`-degenerate in the 2-3 block)?" — **RESOLVED: `diag(B₁,B₂,B₃)`, fold-spectrum-split.** The §VII.BL multiplicity-scalar wall does not reach an eigenvalue-spectrum object; the framework's `D_K ≡ D_F` promotion sources `M_R` from the fold spectrum (Result 1, on-disk); connes' `diag(M₀,M₁,M₁)` is the standard-NCG `A_F`-coupling form the framework does not use (Result 4); the 2-3 block is split on-disk (`B₂=1.0786 ≠ B₃=1.1700`).

### What this opens / closes / shifts

- **Confirms (not shifts) the W2-3 input**: the texture compute used the substrate-correct `M_R` form. The `mix_grp=0/4` FAIL is not attributable to a wrong `M_R` form.
- **Sharpens the workshop verdict**: `WALLED-AS-UNDER-DETERMINED` is correct, and the `√(B₂/B₁)=1.036` ruler-flatness is now understood as the bottom-of-spectrum Casimir near-degeneracy — a real fiber-spectral property, not an imposed degeneracy (Result 6). The flatness will NOT be relieved by re-reading `M_R` as connes' form (which would make the 2-3 block EXACTLY degenerate, `√(M₁/M₁)=1`, even flatter in that block).
- **§VII.BL scope unchanged**: this derivation does not weaken §VII.BL. The wall stands verbatim on `A_K`-built forms (routes a/b/c/d). It simply does not extend to eigenvalue-selections — which it never claimed to. The generation-INDEX channel remains walled (both disputants conceded `D_K` is generation-blind); `M_R` lives on the orthogonal fiber-SPECTRUM channel.

### Anchor-pin for `CF-S117-SEESAW-RESONANCE-MR-SEARCH` (the S-3 deliverable; satisfies CF-W2-2)

The resonance search MUST be anchored to the fold-spectrum form, NOT convention-shopped across both readings. Per CF-W2-2 (WP lines 216-221) the scan is pinned to the S-3-derived form. The anchor:

1. **Scan ONLY fiber-spectrum `M_R` candidates** — triples of DISTINCT `D_K` fold eigenvalues, each carrying genuine bowtie splitting, parametrized by (i) `τ`-scan of the B-branch fold energies (including the `τ=0.107` crossing) and (ii) substrate-natural SECTOR-SELECTION (which `(p,q)` sectors supply the three generation-representatives). The entries are eigenvalue-selections, not A_K-couplings.
2. **FORBID A_K-built `diag(M₀,M₁,M₁)` degenerate forms** — these are the un-promoted standard-NCG `A_F`-coupling object the framework does not use (Result 4). A resonance that fires ONLY on a degenerate-coupling form is OFF-FORM → INFO, NOT PASS (consistent with the CF-W2-2 anchoring guard and `PROHIBITED_ACTIONS Class-1`). The resonance must fire on a genuine sector-distinct fold-spectrum `M_R` to count as substrate-natural.
3. **The resonance condition maps to a Casimir-gap condition** — `M_D[2,2]/M_D[1,1] ≈ √(M_R[2]/M_R[1]) ≈ (C₂(p,q)₂/C₂(p,q)₁)^{1/4}` (Result 6). The hierarchical Dirac seed requires a LARGE Casimir gap. The bottom-three B-branch triple has a SMALL gap (`C₂_2/C₂_1 = 1.15`), hence the `1.036` flatness. The search direction is therefore: **does any substrate-natural sector-selection with a larger Casimir gap (e.g., the lowest fold energy WITHIN each of the three triality classes `t ∈ {0,1,2}`, rather than the three globally-lowest) reach `√(B₂/B₁)` large enough to resonate the hierarchical seed?**
4. **Coupled to the R-channel** (`CF-S117-LEPTON-SEESAW-R-CHANNEL`): changing `Bᵢ` changes the light masses `m_ν,i = m_D,i²/Bᵢ`, hence `Δm²` and `R = Δm²₃₂/Δm²₂₁`. A sector-selection that resonates the mixing angles must SIMULTANEOUSLY reproduce the oscillation `Δm²` ladder; the two channels cannot be optimized independently. Any resonance PASS must report the joint (angle, `R`) outcome at the same fold-spectrum `M_R`.

### Honest scope boundaries (source-fidelity)

- **Sector-label of the fold energies not independently certified here.** INV11-W2-4 established the three `M_R` values are NOT L12-cache re-reads (a distinct lattice-ED pipeline), so the `(p,q)`/triality label of each is not directly readable from the on-disk artifacts. The CATEGORY verdict (spectrum vs coupling) does NOT depend on the labels — it depends only on `M_R` being sourced from `D_K`'s spectrum (settled, Result 1). The labels DO matter for the resonance search's sector-selection direction (anchor item 3), which is why I route that to the forward compute, not assert it.
- **The Dirac side is oscillation-anchored, not zero-parameter.** Per `s99` honest-scope (lines 52-56), the `Yᵢ` normalization is oscillation-anchored. So the `M_R` FORM is substrate-derived (the fold spectrum), but the seesaw mixing OUTCOME also depends on the externally-anchored `m_D` — which IS the under-determination the workshop found. This derivation settles the `M_R` form; it does not by itself close the under-determination of `U_eL`.
- **No verdict re-adjudication.** The W2-3 FAIL and the workshop WALLED verdict stand as emitted.

---

## V. Carry-Forward Computations

`★ Insight ─────────────────────────────────────`
The forward queue stays lean: `CF-S117-SEESAW-RESONANCE-MR-SEARCH` and `CF-S117-LEPTON-SEESAW-R-CHANNEL` are already minted (W2-3 WP). This synthesis supplies the ANCHOR (§IV, satisfying the already-minted CF-W2-2, ~0 compute) plus ONE genuinely-new compute below — the sector-resolved, on-form realization of the resonance search that the anchor demands but that was never computed (INV11 left the `(p,q)` labels open).
`─────────────────────────────────────────────────`

**V.1. Sector-resolved on-form seesaw resonance scan (anchored realization of `CF-S117-SEESAW-RESONANCE-MR-SEARCH`)**
   - **What**: (i) Resolve the `(p,q)`/triality label and `C₂(p,q)` of each B-branch fold energy by matching the lattice-ED fold triple against the L12 Peter-Weyl block-diagonal cache `sector_evals` (nearest-`|λ|` + sector tag), producing the Casimir-gap ladder `(C₂(p,q)ᵢ/C₂(p,q)ⱼ)^{1/4}`. (ii) Scan substrate-natural fold-spectrum `M_R` candidates — `τ`-scan of the B-branch fold energies (incl. `τ=0.107`) AND sector-selection (three globally-lowest vs lowest-per-triality-class `t∈{0,1,2}`) — testing the resonance condition `M_D[2,2]/M_D[1,1] ≈ √(M_R[2]/M_R[1])` at the mass-fit Dirac seed. Report `mix_grp` AND `R = Δm²₃₂/Δm²₂₁` jointly at each candidate.
   - **Inputs**: `s116_lepton_pmns_texture.npz` (mass-fit `M_D`); `s99_w3_seesaw_summnu.npz` (`M_R` fold triple, `m_D`, `M_ν`); `s84_spectrum_cache_L12_tau019.npz` (`sector_evals` for `(p,q)` resolution); `dirac_spectrum.py` B-branch fold energies across `τ`; the Casimir scaling `|λ|_min^(p,q)≈√C₂/r`; NuFIT 5.2 NO 3σ bands + `R`-floor `[17,66]`.
   - **Gate**: PASS iff a substrate-natural (fiber-spectrum, sector-distinct) `M_R` fires `mix_grp ≥ 3` at the mass-fit seed AND reproduces `R ∈ [17,66]` jointly; FAIL if no fiber-spectrum sector-selection across the moduli reaches `√(B₂/B₁)` large enough (the bowtie is structurally too flat); **INFO (OFF-FORM) if resonance fires only on an A_K-built degenerate `diag(M₀,M₁,M₁)` form** (which is NOT the substrate `M_R` per this synthesis — anchor item 2), or only on a `τ`-rescaled non-fold `M_R`.
   - **Effort**: ~1 agent, MEDIUM (sector-tag match against the L12 cache + `τ`-scan of fold energies + per-candidate seesaw recompute; re-uses the mass-fit `M_D`; coupled-channel report).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `M_R = [1.0044,1.0786,1.1700] M_KK` = B-branch `D_K` fold energies (3 DISTINCT eigenvalues) | GEOMETRIC | on-disk (s99 + INV11) | the construction is a fiber-spectrum selection, not an `A_F`-coupling |
| 2 | §VII.BL forecloses `A_K`-BUILT forms (routes a/b/c/d); an eigenvalue-selection is not one | GEOMETRIC | registry lines 21775-21780 + VdD Stage-2 standing | the wall does not reach `M_R` |
| 3 | Two faces of `D_K=⊕D_{(p,q)}⊗1`: Face-1 (`⊗1`)=wall, Face-2 (sector-distinct)=bowtie; `M_R` reads Face-2 | GEOMETRIC | substitution chain (Kasparov factorization, Paper 01) | wall and bowtie share one root, no conflict |
| 4 | `diag(M₀,M₁,M₁)` = standard-NCG free coupling; `diag(B₁,B₂,B₃)` = `D_K≡D_F` fold-spectrum; framework uses the latter | GEOMETRIC/PARTICLE | category translation | the fork is a category distinction; connes' form is the un-used object |
| 5 | `[J,D_K]=0 ⇒ M_R` real-symmetric (`δ_CP∈{0,π}`), NOT degenerate | PARTICLE | reality ≠ per-class-constancy | the `M₁=M₁` collapse needs an `A_K`-coupling, absent here |
| 6 | `√(B₂/B₁)=1.0363` ruler-flatness = bottom-spectrum Casimir near-degeneracy (`C₂_2/C₂_1=1.15`) | GEOMETRIC | Sage-verified | substrate fact; sharpens WALLED-AS-UNDER-DETERMINED; resonance needs large Casimir gap |
| — | **OQ-4 CLOSED: `M_R` is fold-spectrum-split `diag(B₁,B₂,B₃)`** | GEOMETRIC | **verdict** | anchors `CF-S117-SEESAW-RESONANCE-MR-SEARCH` (fiber-spectrum forms only; A_K-degenerate forms OFF-FORM→INFO) |
