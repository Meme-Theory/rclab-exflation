# Session 99 Synthesis: Spectral Geometry / Heat Kernels / Zeta-Mellin Pole Structure (G5 Literature Sweep)

**Date**: 2026-06-04
**Agent**: baptista-spacetime-analyst (Workhorse-KK-Geometry)
**Source Documents**:
- `downloads/research-sweep-s99/spectral-geometry-math/00-INDEX.md` (primary; 10 paper summaries derived from fetched text)
- `downloads/research-sweep-s99/spectral-geometry-math/01..10_*.pdf` (spot-verification corpus)
- `.claude/agent-memory/baptista-spacetime-analyst/MEMORY.md`
- Canonical state verified via knowledge MCP (`search_knowledge`, `get_constant`, `query_entity`)

---

## I. Session Outcome

This is a **literature-adjudication** report, not a compute session — no new gate verdicts are produced. The ten G5 papers are mathematics/mathematical-physics references; their function is to (a) certify which framework spectral-geometry results sit in well-posed mathematical classes, and (b) seed pre-registered validation gates. The single most consequential structural finding: **papers 06 (Fucci-Stanfill) and 10 (Connes) supply the literal mechanism the CF28 pole-structure question turns on** — log branch points / non-simple dimension-spectrum poles are switched on by self-adjoint-extension/boundary data, NOT generic, and the clean Hurwitz/simple-pole form is the special (Friedrichs / closed-manifold) case. This certifies the framework's standing requirement (Connes-Moscovici 1995 §5: the local index formula and every Pillar-VII residue presuppose a **simple** dimension spectrum Sd ⊂ ℤ) is the correct precondition, and it sharpens CF28 into a per-pole simple-vs-log classification that MUST run before any new substrate-distance-pole registration at s ∈ {5,6,7}.

Three canonical-state corrections to the index are flagged in §IV (the index is an idea-generator, not a register): (1) the spectral-dimension/CDT comparison is **S92** (`d_s_fold_window_sigma = 1.4005`), not S80 as the index states, and the quoted "4.00 → 1.71" UV-flow values are **not canonically pinned** — only the fold-window σ_* is; (2) the integrability diagnostic CHAOS-1 is **"DIAGNOSTIC: ORDERED" with sub-Poisson ⟨r⟩ = 0.321** (single-particle), NOT clean Poisson — paper 08's symmetry-resolution caveat is therefore already a live, partially-realized concern, not a hypothetical; (3) the bosonic-fiber τ=0 mode tally is canonically **1 + 8 + 35 = 44** (S20b), distinct from the fold-point Lichnerowicz `n_tt = 31` (S61) — paper 05's validation angle must target the correct object.

---

## II. Key Results

### Result 1 — Papers 06 + 10: CF28 pole-structure mechanism is sourced to the literature

**Result**: Log branch points in the spectral ζ appear at nonpositive-integer s **iff** the self-adjoint extension departs from Friedrichs (Fucci-Stanfill Thm 1.1); the heat trace carries a `t^{−1/2} log(1/t)` term as the **time-domain image of a non-simple pole** (Connes Thm 1.1), and the SDW series **diverges factorially** (asymptotic, not convergent). Classification: **GEOMETRIC** (spectral-triple structure of ζ_{D_K}).

The framework's entire Pillar-VII residue program — every Seeley-DeWitt moment read as a residue of ζ_{D_K}(s) at a pole of the dimension spectrum — is conditional on the dimension spectrum Sd being **simple** (Connes-Moscovici 1995 §5, PROVEN-anchored: "the local index formula requires a regular spectral triple with simple dimension spectrum Sd ⊂ ℤ"; verified canonical). Fucci-Stanfill give the rigorous anatomy of *when that fails*: for a singular Sturm-Liouville operator the meromorphic structure collapses to a rescaled Hurwitz ζ with a **single simple pole at s=1/2** in the Friedrichs / Friedrichs-Neumann classes, but the general extension `T_{0,ν}^{(α,β)}` acquires log branch points at every s = −j, j ∈ ℕ₀, plus parameter-dependent branch points. The substrate lesson is sharp and reassuring: D_K on the **closed** SU(3) carries the canonical (Friedrichs-analog) self-adjoint extension, so its dimension spectrum is the clean simple-pole case — but any boundary-condition modification (an APS-type condition at a transit surface, a defect at the fold) would inject log terms.

Connes supplies the dual (time-domain) statement and two further canon-grade lessons. First, the explicit `t^{−1/2} log(1/t)` term is exactly the signature of a non-simple pole — a double pole, or a pole colliding with trivial-zero structure, produces `t^{−s} log t`. This is the literal origin of the framework's Class-8.7 degenerate-observable concern (`PRU Class 8.7`, S90, PASSED rule extension; witness S93-W3-3 with `n_degenerate_roots=1, max_root_mult=2, NOT_direct_sum`). Second, Connes' factorial divergence `a_n ∼ Γ(k)·(Bernoulli/Euler)/(2k)!` is the canonical form of the framework's S45-S46 heat-kernel-validity-tier lesson ("spectral a₂ ≠ SDW a₂"; the SDW series is asymptotic, bounding optimal truncation order). Third, Connes' intro **explicitly names compact Lie groups with bi-invariant metric** as the canonical closed-form heat-kernel class via representation theory — certifying the framework's Peter-Weyl heat trace `K(t) = Σ d_ρ e^{−t C_ρ}` (paper 01's setting) is the well-understood class.

### Result 2 — Paper 03 (Savale): rank-2 Weyl remainder 8/7 is the continuum floor for L^{−α} truncation envelopes

**Result**: For a compact Lie group with bi-invariant metric, the geodesic flow is the group action, the Ehrenfest time is infinite, and the Weyl-remainder exponent is rank-controlled: `N_h[0,1] = (2πh)^{−n} vol(S*X)[1 + O(h^{1+(p−1)/(3p+1)})]` with **p = rank(G)** (Savale Corollary 3). For bi-invariant SU(3) (n=8, rank p=2): `1 + (p−1)/(3p+1) = 1 + 1/7 = 8/7 ≈ 1.143`. Classification: **GEOMETRIC**.

This is the rigorous continuum statement underlying the framework's R-Protection truncation behavior. The infinite-Ehrenfest-time / integrable-flow regime — which the framework independently established (Berry-Tabor / Richardson-Gaudin fabric integrability, the Ordered Veil) — is *precisely why* the framework's spectral sums converge with rank-power remainders rather than exponential-chaotic ones. The leading `(2πh)^{−n} vol` term IS the a₀ volume coefficient in semiclassical disguise. Caveat (anchored): the framework already carries computed bulk-Weyl-exponent constants `BULK_WEYL_EXPONENT_CONV_A_FW = 10.1224` / `_L14 = 10.1224` (S87, two pole-conventions A/B per `regulator-pin-discipline.md §"Mellin Pole-Set Labeling"`). These are **bulk count coefficients, NOT the remainder exponent** — value 10.12 ≠ 8/7, so Savale's exponent does not reduce to an existing pin; the genuine validation angle is to compute the *remainder* exponent of the bi-invariant counting function and check it against 8/7 (a new gate, §V.2). A rank-4 Pati-Salam extension (`A_K^{PS} = ℂ ⊕ M₂(ℂ)_L ⊕ M₂(ℂ)_R ⊕ M₄(ℂ)`) would carry `1 + 3/13 = 16/13 ≈ 1.231`, a slower-converging remainder.

### Result 3 — Papers 01/02/09: the τ=0 anchor stack and the deformation-rigidity prototype

**Result**: Three independent τ=0 / deformation reference points. (a) Lai-Teh: at the cubic point t=1/3 the Dirac Laplacian collapses to `D²_{1/3} = 1 ⊗ Cas + 3`, eigenvalue **λ(p,q) = p² + q² + pq**, multiplicity **2p²q²(p+q)²** (Theorem 2.2). (b) Fang-Levitin-Vassiliev (d=3 S³): first-order eigenvalue shift `λ⁽¹⁾ = ∓(1/4π²) V⁽¹⁾` depends ONLY on the volume increment; spectral asymmetry (the η-invariant) onsets at **second order** (Thms 2.1, 2.2); charge-conjugation forces even multiplicity (no splitting). (c) Lauret (SU(2)): `λ₁(SU(2), g_{(a,b,c)}) = min{a²+b²+c², 4(b²+c²)}` with multiplicity jump **4 → 7 → 3** at the crossing `a²+b²+c² = 4(b²+c²)`, and the left-invariant SU(2) deformation manifold is **spectrally rigid**. Classification: **GEOMETRIC**.

These three lock onto canonical framework structure. Lai-Teh's `D²_{1/3} = 1 ⊗ Cas + 3` IS the block-diagonal Peter-Weyl reduction `D_K = ⊕_{(p,q)} D_{(p,q)}` the framework uses, at the bi-invariant point; λ(p,q) and its multiplicity are the τ=0 anchors against which every Jensen-deformed eigenvalue must reduce. Canonical confirms the bi-invariant limit is exercised (`D_F(τ=0) = 0` exactly, all 432 fiber modes zero, all Killing; the algebraic `λ² = n/36` form), but I find **no registered explicit reduction test** checking that the framework's deformed-spectrum code recovers Lai-Teh's `(λ, mult) = (p²+q²+pq, 2p²q²(p+q)²)` — a genuine carry-forward (§V.3).

Fang-Levitin-Vassiliev is the d=3 analytic template for the framework's two deepest spectral theorems. `λ⁽¹⁾ ∝ V⁽¹⁾` is exactly why the **volume-preserving** Jensen TT-deformation (PROVEN: `det(g_τ)/det(g_0) = 1.000000000` exact, S20c) kills first-order eigenvalue motion: TT ⇒ V⁽¹⁾ = 0 ⇒ λ⁽¹⁾ = 0, so the bottom eigenvalues are first-order-rigid and any leading τ-motion lives at second order. The "asymmetry-is-second-order" result is the d=3 incarnation of `[J, D_K] = 0` (CPT, PROVEN, S17a: verified at 79,968 pairs, max deviation **3.29e-13** — this is the canonical number; the agent-memory note "eta_pair_err 2.22e-14" is a distinct/looser-provenance value and should defer to 3.29e-13) and `η(D_K) = 0` / spectral-flow = 0: under a real-structure-commuting Dirac operator, spectral asymmetry is structurally a second-order effect, never first-order.

Lauret answers, on the Laplace side, the rigidity question paper 04 leaves open for non-abelian groups: the left-invariant SU(2) deformation manifold is spectrally rigid (spectrum determines metric up to isometry) — the encouraging rank-1 prototype for the framework's rank-2 reconstruction claim. The multiplicity jump 4→7→3 at the crossing IS the framework's eigenvalue-crossing / avoided-crossing / multiplicity-reorganization structure (the B1/B2/B3 trajectories, the τ-moduli anticrossing-swap at δ_τ_crit), in closed form.

### Result 4 — Paper 04 vs Paper 09: the spectrum-alone-vs-full-triple reconstruction boundary

**Result**: The first known triplet of mutually isospectral, non-isometric, irreducible flat **6-tori** (Mårdby-Rowlett-Rydell; choir number ♭₆ ≥ 3; supermultiplicative ♭_{m+n} ≥ ♭_m ♭_n) bounds spectral rigidity from below for abelian quotients; Lauret's SU(2) rigidity bounds it from above for rank-1 non-abelian groups. Classification: **GEOMETRIC**.

The structural lesson is canonical doctrine: the spectrum **alone** does not fix geometry for abelian-group quotients (♭_n > 1), and the framework's spectral characterization must invoke the **full spectral triple** (algebra `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` + real structure J + D_K), not the eigenvalue list — exactly the gap Connes' reconstruction theorem closes by adding the algebra (canonical: KO-dim=6, reconstruction-via-full-triple). The choir-number supermultiplicativity is the analytic warning that **product/direct-sum constructions proliferate isospectral ambiguity** — directly relevant to the M⁴ × SU(3) product, where the K-spectrum alone might not pin K. The open question (whether the *non-abelian* SU(3) representation-theoretic eigenvalue structure admits isospectral-non-isometric Jensen deformations, or is rigid like SU(2)) is a clean falsifier, §V.4.

### Result 5 — Paper 05 (Sauro): non-minimal â₂ for the TT-graviton/vector sectors

**Result**: The local trace of the second Seeley-DeWitt coefficient `tr â₂` for general **non-Laplace-type** second-order operators, with explicit parameter-dependent curvature coefficients (Eq. 82): `tr â₂ ⊃ −[b²/4(2+b)²] R_αβ R^αβ + [(b−8)b/24(2+b)²] R² + [b²/8(2+b)²] R_αβμν R^αβμν`; the transverse-mode degeneracy at the non-minimality parameter `bζ = −2` is where the principal-symbol kernel jumps and only transverse modes propagate. Classification: **GEOMETRIC** (heat-kernel scheme for the fiber operators).

This is the machinery the framework's NON-minimal fiber sectors need. The standard a₄ (d=8) SDW computation assumes Laplace-type operators (principal symbol ∝ identity); for the TT graviton and the Yang-Mills vector sector the operator is non-minimal, and Sauro's tr â₂ ⊃ (Ric², R², Riem²) with `b²/(2+b)²` coefficients is the correction template. The `bζ = −2` degeneracy (principal-symbol kernel jump → transverse-only propagation) is the analytic structure behind the framework's TT projection (the volume-preserving Jensen deformation imposes transverse-traceless; the gauge-fixing parameter isolating transverse modes is this non-minimality parameter). The Barvinsky-Vilkovisky `Tr log F̂ = Tr log D̂ + Tr log(1 + D̂⁻¹Ŷ)` split (principal-part curvature + endomorphism) maps onto the framework's separation of the a₂/a₄ curvature sector from the endomorphism-E (F², Higgs-potential) sector in the spectral action. **Correction to the index's validation angle**: it cites "31 singlet + 81-per-sector" as the TT mode tally to match; the canonical τ=0 bosonic-fiber decomposition is **1 (scalar) + 8 (vector) + 35 (TT) = 44** (S20b, PROVEN), and `n_tt = 31` is the *Lichnerowicz TT count at the fold* (S61), a distinct object. The non-minimal-scheme gate (§V.5) must verify against the correct sector tally.

### Result 6 — Paper 07 (Ambjørn-Loll CDT): spectral-dimension flow, same-functional-same-window only

**Result**: CDT measures `D_s(σ) = 4.02 − 119/(54+σ)` (Fig. 5, N₄ = 360,000) on the heat-kernel return probability — the SAME observable the framework defines, `d_s(σ) = −2 d ln P/d ln σ` with `P(σ) = Tr e^{−σ D_K²}`. CDT flows 4 (IR) → ≈1.82 (UV). Classification: **GEOMETRIC** (cross-framework benchmark, comparison-gated).

The comparison is admissible **only** under the same-functional-same-window discipline (`cross-pillar-bridge-corpus.md §24`, SUGGESTION K=2; `phononic-framing.md §"Same-functional-different-scale"`). `d_s` is a functional of P(σ) evaluated at a *chosen* σ-window; comparing the framework's σ→0 Weyl asymptotic to CDT's intermediate-window Monte-Carlo fit is a category error unless the (observable, diffusion-window) pair is fixed on both sides. The discriminator is the energy-axis DOS exponent γ_E, with any impedance constraint `Z = ρ_E v_g` a consistency check, not a lock. The framework is NOT a CDT-style sum over geometries (one fixed spectral triple, not a path integral over triangulations): the dimensional flow is **kinematic** (spectral-support reorganization), CDT's is **dynamical** (QG path-integral average). **Canonical correction (index error)**: this comparison is **S92** (`d_s_fold_window_sigma = 1.4005 M_KK^{−2}`, the fold-window diffusion time; source `s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md`), not "S80" as the index states; and the index's specific UV value "1.71" is **not a canonical pin** — only σ_* = 1.4005 is registered. The matched-window verdict and any d_s(σ_*) value must be read from the S92 workshop, not asserted from the index.

### Result 7 — Paper 08 (Shir-Martinez-Azcona-Chenu): corrected kNN surmise sharpens the Ordered-Veil falsifier

**Result**: A variance-corrected k-th-nearest-neighbor level-spacing surmise distinguishing integrable (Berry-Tabor / Poisson, no level repulsion) from chaotic (Bohigas-Giannoni-Schmit / RMT GOE/GUE/GSE, repulsion present) spectra beyond nearest-neighbor; the paper flags that **classically-integrable systems WITH symmetry can deviate from naive Poisson**. Classification: **PHONONIC** (Ordered-Veil non-thermalization / GGE permanence falsifier tool).

This is the refined falsifier for the framework's integrability claim (the GGE relic never thermalizes because the fabric is integrable — Berry-Tabor, Richardson-Gaudin — not chaotic; the Ordered Veil, PROVEN S38). The symmetry caveat is **already a live, partially-realized concern**, not hypothetical: canonical CHAOS-1 is **"DIAGNOSTIC: ORDERED"** with single-particle ⟨r⟩ = 0.321 (sub-Poisson) and pooled `r_pooled = 0.422` (Poisson ≈ 0.386, GUE ≈ 0.603 — both readings integrable-leaning). The sub-Poisson value is the expected signature of a maximally-symmetric spectrum (Weyl-group + Peter-Weyl degeneracies): the SU(3) spectrum must be **symmetry-unfolded within fixed (p,q) sectors** before the spacing distribution is read, exactly the deviation paper 08 warns of. The corrected kNN surmise is the tool to make the symmetry-resolved test quantitative: level repulsion at any k would falsify integrability / non-thermalization; Poisson (or super-Poisson, given the massive multiplicities) at all k confirms it. The three RMT universality classes keyed to symmetry map onto the framework's AZ classification (BDI, canonical).

---

## III. Gate Verdicts

No gates are produced by this literature sweep. The papers SEED gates (§V) and CERTIFY the well-posedness class of existing canonical results (§II). Canonical gate/theorem anchors cited (verified, not re-adjudicated):

| Anchor | Canonical Status | Source |
|:-------|:-----------------|:-------|
| `[J, D_K] = 0` (CPT) | PROVEN, max dev 3.29e-13 (79,968 pairs) | atlas-04 G8, S17a |
| `η(D_K) = 0` / spectral-flow = 0 | PROVEN (5 independent proofs) | S25, atlas-03 |
| Volume-preserving TT-deformation | PROVEN, det = 1.000000000 exact | atlas-07, S20c |
| Simple dimension spectrum Sd ⊂ ℤ (precondition) | PROVEN-anchored (Connes-Moscovici 1995 §5) | S82 WP |
| PRU Class 8.7 degenerate-observable | PASSED rule extension; witness S93-W3-3 | S90, S93 |
| CHAOS-1 integrability diagnostic | DIAGNOSTIC: ORDERED (⟨r⟩=0.321 sub-Poisson) | S8/S38/S46/S61 |
| CDT spectral-dimension comparison | S92 (`d_s_fold_window_sigma=1.4005`) | S92 workshop |
| Bosonic τ=0 fiber tally 1+8+35=44 | PROVEN | S20b |
| `BULK_WEYL_EXPONENT_CONV_A` ≈ 10.1224 | computed pin (no PROVENANCE entry) | S87 |

---

## IV. Structural Implications

**What these papers OPEN.** The CF28 pole-structure question now has a literal mathematical mechanism (papers 06 + 10): simple-vs-log is decided by self-adjoint-extension/boundary data, and the test is a per-pole heat-trace check for `t^{n/2} log t` terms. This converts CF28 from "is the residue clean?" into a concrete, runnable classification at each candidate pole. Paper 03 gives an independent continuum floor (8/7) for the truncation envelopes the framework reports empirically. Paper 09's SU(2) rigidity + crossing closed form gives a rank-1 prototype the rank-2 program can target directly.

**What these papers CLOSE / constrain.** Paper 04 hardens the doctrine that spectrum-alone is insufficient — the framework's reconstruction claim MUST be a full-triple claim (already canonical via Connes reconstruction, KO-dim=6), and product constructions must be checked for isospectral proliferation. Paper 05 constrains the a₄ hierarchy to be computed in the **non-minimal** scheme for TT/vector sectors — a scheme-correctness condition on a load-bearing (weight-4) moment.

**Canonical-state corrections (the index is an idea-generator, not a register).** Three index claims diverge from canonical and are flagged so downstream consumers do not propagate them:

1. **Spectral-dimension/CDT is S92, not S80.** The index attributes the d_s flow and the diffusion-window discipline to S80 and quotes "4.00 → 1.71." Canonical: the CDT comparison and fold-window pin (`d_s_fold_window_sigma = 1.4005`) are **S92** (`s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md`). The "1.71" UV value is not a registered constant. (S80 carries an unrelated `w0_15` branch-shortfall result per agent memory; the conflation is an index error.) The diffusion-window discipline itself lives at `cross-pillar-bridge-corpus.md §24` (K=2), independent of session number.

2. **CHAOS-1 is sub-Poisson "ORDERED," not clean Poisson.** The index's paper-08 angle frames the integrability test as "should show Poisson"; canonical CHAOS-1 already returns ⟨r⟩ = 0.321 (sub-Poisson, below Poisson ≈ 0.386). The symmetry-resolution caveat is therefore the *operative* subtlety, not a footnote — the unfolding-within-sectors step is mandatory before any Poisson-vs-RMT verdict.

3. **TT mode tally: τ=0 is 44 (1+8+35); fold Lichnerowicz is 31.** The index's paper-05 angle cites "31 singlet + 81-per-sector"; the canonical τ=0 bosonic-fiber decomposition is 1+8+35=44 (S20b) and `n_tt=31` is the fold-point Lichnerowicz count (S61). The non-minimal-scheme gate must name the correct object.

4. **Higher-pole registration is more advanced than the index implies.** The index requests s ∈ {5,6,7} registration "BEFORE any Pillar-VII registration." Canonical: §VII.BB already lands at **s=5** (α_s on M₃(ℂ), substrate-distance-3 pole), and §W12-148 already PASSes at **s=5 and s=6** with `|ρ_S+1| = 0.0` EXACT (machine precision). The pole↔a_n map (single-power, d=8) is `s = 8 − n`: s=8→a₀, s=6→a₂, s=4→a₄, s=2→a₆; so s ∈ {5,7} are **inter-curvature-grade** (odd-s) poles between the even-graded SDW poles. The CF28 carry-forward (§V.1) is therefore scoped to the *simple-vs-log classification of the s ∈ {5,6,7} poles* (a well-posedness pre-check), not to first-time registration of all of them.

**Substrate-first framing.** Every result above flows `D_K eigenvalues → spectral ζ_{D_K}(s) / heat trace Tr e^{−σ D_K²} → (simple-pole residues = SDW moments, OR log-coefficients if degenerate) → emergent observable`. The substrate IS the spectrum; the pole structure of its ζ-function is what decides which moments are clean observables versus log-carrying defects. No result here inverts that direction.

---

## V. Carry-Forward Computations

**These are validation-angle gates seeded by the G5 papers, each scoped against the canonical state verified above.**

```
V.1. CF28 simple-vs-log pole classification at s ∈ {5,6,7} (heat-trace log-term pre-check)
   - What: For each candidate substrate-distance pole s ∈ {5,6,7}, test whether the
     heat trace Tr(e^{−t D_K²}) acquires a t^{n/2} log(1/t) term at the matching order
     (Connes Thm 1.1 mechanism = non-simple pole; Fucci-Stanfill Thm 1.1 = boundary-data
     trigger). Output: per-pole boolean simple_pole(s) + residue-vs-log-coefficient tag.
     Reduce ζ_{D_K} pole order via the Peter-Weyl block heat trace K(t)=Σ d_ρ e^{−t C_ρ}
     and check for log structure against the clean Hurwitz/simple-pole reference.
   - Inputs: spectrum cache `computations/_shared/s84_spectrum_cache_L12_tau019.npz`
     (L_max=10, 65 (p,q) sectors); canonical simple-Sd anchor (Connes-Moscovici 1995 §5);
     PRU Class 8.7 degeneracy-witness machinery (S90/S93-W3-3, `max_root_mult`, `NOT_direct_sum`).
   - Gate: feeds CF28 (atlas-08 open channel "F_4-MB structural wall family pole-distinct
     corpus extension"). NEW sub-gate CF28-POLE-SIMPLICITY: PASS = all s∈{5,6,7} simple
     (residue = SDW moment, registry-eligible); FAIL = any log-carrying (residue ill-defined,
     registration blocked at that pole); INFO = degenerate-but-direct-sum (Class 8.7 witness path).
   - Effort: 1 agent session (2-4 hours); spectrum cache exists, heat-trace evaluator exists.

V.2. Bi-invariant SU(3) Weyl-remainder exponent vs Savale 8/7 (continuum-floor check)
   - What: Compute the remainder exponent of the bi-invariant SU(3) Laplace/Dirac counting
     function N(E) and compare to Savale Corollary 3 prediction 1+(p−1)/(3p+1)=8/7 for p=rank=2.
     Substitution: N(E) from the closed Lai-Teh/Casimir spectrum (λ(p,q)=p²+q²+pq, mult
     2p²q²(p+q)²); fit the O(E^{α}) remainder after subtracting the Weyl leading term.
     NOTE: this is the REMAINDER exponent, distinct from the existing bulk-count pin
     BULK_WEYL_EXPONENT_CONV_A (≈10.12, not a remainder exponent).
   - Inputs: Lai-Teh closed-form spectrum (paper 01); canonical `BULK_WEYL_EXPONENT_CONV_A/B`
     (S87) for cross-reference only; Sage MCP for exact 8/7 and exact remainder fit.
   - Gate: NEW gate WEYL-REMAINDER-RANK2: PASS = fitted exponent within tolerance of 8/7
     (sets the continuum floor for the L^{−α} truncation envelopes / R-Protection O(L^{−rank})
     drift); FAIL = inconsistent (truncation envelope floor is mis-assigned); INFO = rank-4
     PS extension exponent 16/13 logged for the Pati-Salam comparison branch.
   - Effort: 1 agent session (2-3 hours); closed-form spectrum, no diagonalization needed.

V.3. Lai-Teh τ=0 reduction test (mandatory bi-invariant anchor)
   - What: Verify the framework's Jensen-deformed SU(3) spectrum code recovers, at τ=0,
     Lai-Teh's λ(p,q)=p²+q²+pq with multiplicity 2p²q²(p+q)² (cubic-point D²_{1/3}=1⊗Cas+3,
     Theorem 2.2) AND the 4-term spectral-action polynomial (Λ⁸/Λ⁶/Λ⁴/Λ², Theorem 3.4) with
     the (3t−1)(3t−2) torsion-twist vanishing at t=1/3. Cross-check the off-diagonal ΔCas
     term as the analytic template for the τ-moduli deformation.
   - Inputs: `dirac_spectrum.py` (Peter-Weyl block constructor); spectrum cache at τ=0
     (or generate); canonical `D_F(τ=0)=0` exact (s30a) as a coarse sanity anchor.
   - Gate: NEW gate TAU0-LAITEH-REDUCTION: PASS = (λ, mult) match Lai-Teh bit-for-bit per
     sector AND 4-term polynomial coefficients reproduce; FAIL = mismatch (deformation code
     does not reduce correctly at the bi-invariant limit — upstream defect). No canonical
     registered reduction test currently exists — this closes that gap.
   - Effort: 1 agent session (3-4 hours); requires sector-by-sector multiplicity comparison.

V.4. SU(3) spectral-rigidity vs isospectral-non-isometric falsifier (paper 04 vs paper 09)
   - What: Test whether distinct Jensen-deformed SU(3) metrics are spectrally distinguishable
     (rank-2 analog of Lauret SU(2) rigidity, paper 09) OR admit isospectral-non-isometric
     deformations (the abelian-torus failure mode, paper 04). Use representation-number /
     theta-series matching (choir-number machinery) on the λ(p,q) eigenvalue structure across
     a τ-scan; check whether any two τ-values produce identical multiplicity-weighted spectra.
   - Inputs: spectrum cache across a τ-grid; canonical full-triple reconstruction anchor
     (KO-dim=6, A_K=ℂ⊕ℍ⊕M₃(ℂ)); paper-04 representation-number matching method.
   - Gate: NEW gate SU3-SPECTRAL-RIGIDITY: PASS = no two distinct-τ metrics isospectral
     (rigidity holds; spectrum reconstructs Jensen geometry, supporting the full-triple claim);
     FAIL = isospectral-non-isometric pair found (spectrum-alone insufficient; full-triple
     algebra+J strictly required — strengthens the paper-04 doctrine); INFO = rigidity holds
     on bottom-N but ambiguous in the tail.
   - Effort: 1-2 agent sessions (4-6 hours); τ-scan + theta-series comparison.

V.5. Non-minimal â₂ correction for TT-graviton / vector sectors (paper 05 scheme check)
   - What: Recompute the framework's a₄ (d=8) contribution from the TT-graviton and
     Yang-Mills vector sectors in the NON-Laplace-type scheme (Sauro Eq. 82 tr â₂ with
     b²/(2+b)² coefficients on Ric²/R²/Riem²) and compare to the existing Laplace-type
     a₄ result. Verify the transverse-mode count at the bζ=−2 degeneracy matches the
     CANONICAL fiber tally (τ=0: 1+8+35=44, S20b; fold Lichnerowicz n_tt=31, S61) — NOT the
     index's "31+81-per-sector" which is not canonical.
   - Inputs: Sauro Eq. 82 + the model-independent â₂ master (Eqs. 67/69, marked INCOMPLETE
     in the index — recover from paper 05 PDF if needed); canonical bosonic-fiber tally
     (S20b); canonical a₄ Yang-Mills + Higgs result.
   - Gate: NEW gate NONMINIMAL-A4-TT-VECTOR: PASS = non-minimal correction within tolerance
     of the Laplace-type a₄ (scheme is adequate as-computed) OR the corrected value is the
     registry value (scheme correction adopted); FAIL = O(1) discrepancy (the a₄ hierarchy
     was computed in the wrong scheme for the non-minimal sectors). INFO = transverse-mode
     count at degeneracy ≠ canonical tally (mode-counting inconsistency to resolve first).
   - Effort: 1-2 agent sessions (4-6 hours); requires the model-independent â₂ formula and
     careful sector identification.

V.6. Symmetry-unfolded kNN spacing surmise (sharpened Ordered-Veil integrability falsifier)
   - What: Compute symmetry-unfolded nearest-neighbor AND k-th-nearest-neighbor (k=2,3)
     level-spacing distributions of the bottom-N D_K eigenvalues WITHIN fixed (p,q)/symmetry
     sectors (the unfolding paper 08 mandates), and test against the corrected kNN surmise:
     Berry-Tabor Poisson (integrable, no repulsion) vs Wigner/RMT (chaotic, repulsion).
     Resolves the canonical CHAOS-1 sub-Poisson "ORDERED" diagnostic (⟨r⟩=0.321) into a
     symmetry-resolved kNN verdict.
   - Inputs: spectrum cache `s84_spectrum_cache_L12_tau019.npz`; canonical CHAOS-1 (⟨r⟩=0.321,
     r_pooled=0.422; S8/S38/S46/S61); paper-08 corrected-surmise variance correction (formula
     INCOMPLETE in index — recover from paper 08 PDF); AZ class BDI assignment (canonical).
   - Gate: feeds the Ordered-Veil / GGE-permanence falsifier family. NEW gate
     ORDERED-VEIL-KNN-SURMISE: PASS = Poisson (or super-Poisson) at all k after unfolding
     (confirms integrability / non-thermalization); FAIL = level repulsion at any k
     (falsifies the Ordered-Veil integrability claim); INFO = symmetry-resolution ambiguous
     (the maximally-symmetric spectrum deviates from naive Poisson per the paper-08 caveat).
   - Effort: 1 agent session (3-4 hours); spectrum cache exists, RMT tooling exists (s46/s61).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Papers 06+10: log-term/simple-pole mechanism for CF28 | GEOMETRIC | Mechanism sourced to literature; CF28 sharpened | Pillar-VII residues require simple Sd (Connes-Moscovici §5); per-pole log-check now runnable (§V.1) |
| 2 | Paper 03: rank-2 Weyl remainder 8/7 | GEOMETRIC | Continuum floor identified; not yet matched to a framework pin | 8/7 ≠ existing BULK_WEYL pin; remainder exponent is a new gate (§V.2); R-Protection O(L^{−rank}) floor |
| 3 | Papers 01/02/09: τ=0 anchor stack + rigidity prototype | GEOMETRIC | Anchors confirmed; explicit reduction test unregistered | TT⇒V⁽¹⁾=0⇒λ⁽¹⁾=0 (d=3 template for [J,D_K]=0); Lai-Teh reduction gate (§V.3); SU(2) crossing = B1/B2/B3 template |
| 4 | Paper 04 vs 09: spectrum-alone vs full-triple boundary | GEOMETRIC | Doctrine hardened | Full-triple reconstruction mandatory (canonical KO-dim=6); product constructions proliferate ambiguity; SU(3) rigidity falsifier (§V.4) |
| 5 | Paper 05: non-minimal â₂ for TT/vector | GEOMETRIC | Scheme-correctness condition on a₄ | a₄ (weight-4, load-bearing) must use non-minimal scheme for TT/vector (§V.5); index mode-tally corrected to 44 / 31 |
| 6 | Paper 07: CDT d_s flow benchmark | GEOMETRIC | Comparison admissible only window-matched | Kinematic (substrate) vs dynamical (CDT) flow; S92 (not S80); "1.71" not a canonical pin |
| 7 | Paper 08: corrected kNN surmise | PHONONIC | Falsifier sharpened; symmetry caveat already live | CHAOS-1 sub-Poisson "ORDERED" needs symmetry-unfolded kNN verdict (§V.6); repulsion at any k falsifies Ordered Veil |
