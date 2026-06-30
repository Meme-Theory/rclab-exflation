# Session 115 W1-1 Synthesis: §VII.CK Stage-2 BLIND Independent Cross-Axis Verification — Axis-A (Spectral-Functional)

**Date**: 2026-06-24
**Agent**: lizzi-spectral-functional-theorist (Axis-A — spectral-functional / NCG-regularization)
**Gate**: S115-VIICK-STAGE2-VERIFY (Axis-A leg)
**Source Documents** (the ONLY documents read for this verify):
- `sessions/permanent-results-registry.md` — the registered §VII.CK entry (header `### §VII.CK — SHAPE-Branch Homogeneity Obstruction …`, ~line 22422) + master-index row 173; the §VII.BL multiplicity-scalar / Skolem–Noether leg-membership anchor (lines 21197–21241).
- `computations/session-114/s114_yuk_shape_wall_vii_landing.npz` + verdict line `CF-S114-YUK-SHAPE-WALL-VII-LANDING` in `computations/session-114/s114_gate_verdicts.txt` (the substrate-input-orthogonal D1 artifact I am permitted to read).
- Permanent anchors verified via the knowledge MCP (`{γ₉,D_K}=0` S34/S56; `[J,D_K]=0` S17a/BDI/KO-dim 6; multiplicity-leg generation id `t=(p−q) mod 3`).

**BLINDNESS ATTESTATION (load-bearing per `joint-theorem-promotion.md §"Stage 2"` + `epistemic-discipline.md §"What Counts as a Result"`):** I did NOT open the originating workshop transcript `sessions/session-113/workshops/ws-s113-7-yukshape/ws-s113-7-yukshape-verdict.md`, nor the Axis-B reviewer's synthesis, nor any other agent's reasoning. Each clause below is re-derived from the permanent anchors by my own argument and confirmed by my own Sage-QQ symbolic computation — going BEYOND the npz artifact (which checked only D1 at powers {1,3} on a 2×2 toy). My agreement with the registered claim is therefore structurally independent of the workshop's reasoning path.

---

## I. Session Outcome

All three closed-class clauses of §VII.CK — **D1** (γ₉-graded odd-power supertrace ≡ 0), **D2** (γ₉-graded even moment is C₂-only, not C₃), **D3** (every A_K-built form is multiplicity-scalar ⇒ generation-blind) — **independently re-derive and reproduce on the Axis-A (spectral-functional) leg: D1 PASS, D2 PASS, D3 PASS.** I confirm the registered structural theorem within the D1–D3 scope qualifier `class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}`; the D4 (right-regular SU(3)_R) door is OUT OF SCOPE for this gate and I make no claim on it (it is owed to the separate `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`).

**Axis-A structural contribution (the spectral-functional reading the registry did not make explicit):** all three obstructions are **FUNCTIONAL-INDEPENDENT** — they hold identically under cutoff `Tr f(D_K²/Λ²)`, zeta `S_ζ = ζ_{D_K}(0)`, anomaly-derived, and every other spectral functional. None of D1/D2/D3 invokes a spectral-moment weighting; each is a property of the triple's symmetry algebra `(γ₉, J, A_K)` alone. There is therefore no regularization-scheme escape from the SHAPE obstruction — changing the spectral functional cannot manufacture a per-generation handle the algebra forbids. This is the strongest possible status for an obstruction theorem: it is regulator-invariant by construction, and the held quantity (a sign-pattern) is SCHEME-INDEPENDENT (the magnitude of any surviving C₂-moment is scheme-dependent, but its generation-blindness is not).

---

## II. Key Results (per-clause first-principles re-derivation)

### D1 — `Tr[γ₉ D_K^{2k+1}] ≡ 0` by `{γ₉, D_K} = 0`

**Result**: GEOMETRIC. The γ₉-graded supertrace of any ODD power of D_K vanishes EXACTLY, at every τ and every L_max, per-block independently.

**First-principles re-derivation (my own substitution chain; anchor: `{γ₉,D_K}=0`, S34/S56, the Cl(8)/Lichnerowicz chirality anticommutator — confirmed via knowledge MCP, session-17b `{D_K,Γ_K}=0`, session-20b Prop 1.1 "D_K anticommutes with Γ_K (Lichnerowicz)").**

Let `p = 2k+1` be odd. Using `{γ₉, D_K} = γ₉ D_K + D_K γ₉ = 0`, i.e. `γ₉ D_K = −D_K γ₉`, push γ₉ through all p factors of D_K:
```
γ₉ D_K^p = (−1)^p D_K^p γ₉ = −D_K^p γ₉        (p odd ⇒ (−1)^p = −1).
```
Take the trace and use cyclicity `Tr[D_K^p γ₉] = Tr[γ₉ D_K^p]`:
```
Tr[γ₉ D_K^p] = Tr[(−1)^p D_K^p γ₉] = −Tr[D_K^p γ₉] = −Tr[γ₉ D_K^p]
⇒ 2·Tr[γ₉ D_K^p] = 0 ⇒ Tr[γ₉ D_K^p] = 0   EXACTLY.
```
This is an *exact algebraic zero* (the supertrace is its own additive inverse), not a small number — independent of dimension, L_max, τ, and the spectral functional. It requires ONLY a trace-class operator and the permanent anticommutator; no regularization choice enters.

**Independent symbolic confirmation (Sage-QQ, beyond the npz's 2×2/powers-{1,3} check).** I built a genuine 2n=6-dimensional chirality grading `γ₉ = diag(+1₃, −1₃)` and a generic anticommuting `D = [[0,B],[Bᵀ,0]]` with integer B, verified `{γ₉,D}=0` is EXACTLY zero, and confirmed `Tr[γ₉ D^p] = 0` over QQ for **all odd p ∈ {1,3,5,7,9}**. The anticommutator+cyclicity mechanism is manifestly power- and dimension-independent, so the per-block exact-zero generalizes to every Peter-Weyl sector `(p,q)` (consistent with the npz `max_{(p,q)} ‖{γ₉,D_π}‖ = 0`).

**On the npz operational-L downgrade (62/66 sectors).** The registry honestly discloses 4 pure-symmetric corners `(0,n)/(n,0)`, `p+q ≥ 9`, were unconstructed (recursive-Casimir `get_irrep` wall). This does NOT weaken D1: the identity is a PER-BLOCK exact-zero `Tr[(I⊗γ₉)D_π^{2k+1}]=0` for EACH `(p,q)` independently (by `{γ₉,D_π}=0` block-by-block), so there is no cross-sector cancellation to verify and the unconstructed corners contribute exactly 0 by the identical argument. The wall is an implementation artifact, not physics. I concur with this disclosure.

**connes R1 corollary (orientation slope).** `κ^{orient} = d/dτ(Tr[γ₉ D_K]) = d/dτ(0) ≡ 0` is an analytic consequence, not an open compute: the orientation supertrace is identically 0 at every τ, so its τ-derivative is identically 0. There is no τ-dependent orientation handle.

> **D1 verdict: PASS** — re-derived exactly from `{γ₉,D_K}=0` + cyclicity; reproduced over QQ at odd powers 1–9 on a 6-dim block; FUNCTIONAL-INDEPENDENT (no spectral-moment weighting enters).

### D2 — `Tr[γ₉ f(D_K²)]` is conjugation-even ⇒ carries C₂ only, not C₃, by `[J,D_K]=0`

**Result**: GEOMETRIC. The surviving (even-power) γ₉-graded moment is a function of the conjugation-EVEN quadratic Casimir C₂; the conjugation-ODD cubic Casimir C₃ — the only su(3) invariant that can resolve the triality/generation direction — cancels under BDI reality.

**First-principles re-derivation (anchors: `[J,D_K]=0` S17a, BDI reality, KO-dim 6, signs (ε,ε',ε'')=(+1,+1,−1); the η-invariant λ↔−λ pairing, S25 — confirmed via knowledge MCP).**

Two independent links, both verified symbolically:

**(i) The survivor is a function of `|λ|² ∼ D_K²`.** D1 kills odd powers, so the only non-vanishing γ₉-graded spectral data is `Tr[γ₉ f(D_K²)]` — a function of the conjugation-EVEN operator `D_K²`. On the Peter-Weyl block `(p,q)`, the eigenvalue floor is the quadratic Casimir: `λ²_min ∼ C₂(p,q)`. Hence `f(D_K²)` is a G-invariant scalar function of C₂ (and, a priori, C₃, the second independent su(3) invariant).

**(ii) BDI reality forces conjugation-evenness ⇒ C₂-only.** `[J,D_K]=0` (BDI, KO-dim 6) makes the spectrum λ↔−λ symmetric (η(D_K)=0, S25) and pairs each irrep `V_{(p,q)}` with its complex conjugate `V_{(q,p)}` at EQUAL weight. I verified the two Casimir parities exactly over QQ:
- `C₂(p,q) − C₂(q,p) = 0` ⇒ **C₂ is conjugation-EVEN** (symmetric under (p,q)↔(q,p)).
- `C₃(p,q) + C₃(q,p) = 0` ⇒ **C₃ is conjugation-ODD** (antisymmetric); moreover `(p−q) | C₃` exactly (the numerator factors as `(p−q)(p+2q+3)(2p+q+3)`), so C₃ is built on the SAME `(p−q)` that defines the triality/generation index `t = (p−q) mod 3`.

In a G-invariant trace summed over the J-paired conjugate doublet `{(p,q),(q,p)}` at equal weight w, the conjugation-ODD contribution cancels and the conjugation-EVEN contribution doubles. I confirmed this directly: the conjugate-pair sum of a linear-C₃ contribution `= 0` (C₃ CANCELS), while the conjugate-pair sum of a linear-C₂ contribution `= 2w·C₂` (C₂ SURVIVES). Therefore `Tr[γ₉ f(D_K²)]` can carry only C₂; it is structurally blind to C₃.

**Why this matters for SHAPE.** Among the polynomial su(3) Casimirs, **C₃ is the unique invariant odd in (p−q)** — the only one that could supply a sign-changing, generation-resolving texture (a per-generation handle distinguishing the up-type from down-type crossing). D2 proves the only γ₉-graded spectral moment that survives D1 is precisely the one that CANNOT see C₃. The even-grading is the obstruction; reality is its enforcer, and reality `[J,D_K]=0` is never sacrificed (it is satisfied by construction — consistent with the §VII.BL "reality is INNOCENT" relocation).

**Spectral-functional note (Axis-A).** The conjugation-parity argument is independent of `f`: it holds for `f(x)=e^{−x/Λ²}` (cutoff heat-kernel), for the zeta-moment `ζ_{D_K}(s)`, and for any even spectral functional, because the cancellation is driven by the J-pairing of the index set, not by the weighting `f`. No spectral functional can promote a C₃-sensitive moment past the BDI even-grading. FUNCTIONAL-INDEPENDENT.

> **D2 verdict: PASS** — re-derived: D1 leaves only `f(D_K²)`; `[J,D_K]=0` BDI pairing cancels the conjugation-odd C₃ and keeps the conjugation-even C₂. Confirmed over QQ (C₂ even, C₃ odd with (p−q)|C₃, conjugate-pair cancellation). FUNCTIONAL-INDEPENDENT.

### D3 — every A_K-built form is multiplicity-scalar (⊗1 on the generation leg) by Skolem–Noether leg-membership ⇒ generation-blind

**Result**: GEOMETRIC. Every operator built from the spectral-triple data with algebra elements in `A_K` — one-forms `[D_K,a]`, cyclic cocycles `a₀[D_K,a₁]⋯[D_K,a_k]`, their J-images and twisted-inner variants — acts as the identity `1_{m(p,q)}` on the multiplicity (generation) leg `ℂ^{m(p,q)}`, hence cannot distinguish the t-generations.

**First-principles re-derivation (anchor: Skolem–Noether leg-membership / the §VII.BL multiplicity-scalar identity, registry line 21205/21241; session-99 "left-invariance ⇒ multiplicity-scalar ⇒ Ω¹_{D_K}(A_K) = span{a₀[D_K,a₁]} valued in the multiplicity-scalar algebra"; multiplicity-leg generation id `t=(p−q) mod 3`).**

The Hilbert space decomposes as `H_K = ⊕_{(p,q)} V_{(p,q)} ⊗ ℂ^{m(p,q)}`, with the generation degeneracy carried entirely on the multiplicity factor `ℂ^{m(p,q)}`. The Peter-Weyl action is **block-scalar on the multiplicity leg**: `π(a) = ⊕_{(p,q)} π_{(p,q)}(a) ⊗ 1_{m(p,q)}` for all `a ∈ A_K`. This is the Skolem–Noether content: `A_K = ℂ⊕ℍ⊕M₃(ℂ)` has three non-isomorphic simple summands, so every represented element (and every block-inner automorphism σ ∈ Aut(A_K)) acts as `X ⊗ 1_m` — identity on the m-leg.

The set `S = { X ⊗ 1_m : X ∈ B(V) }` is a **subalgebra closed under `+`, `·`, and commutator**. Since `π(a) ∈ S` and (with D_K acting within a sector) `[D_K, a] ∈ S`, every word `a₀[D_K,a₁]⋯[D_K,a_k]` is again in `S` — i.e. `(·) ⊗ 1_m`. An operator of the form `(·) ⊗ 1_m` acts IDENTICALLY on each generation slot, so it distinguishes SECTORS `(p,q)` (LABELING-B, registry-foreclosed) but NEVER the t-generations within a sector (LABELING-A, the operative index). Generation-blind.

**Independent symbolic confirmation (Sage-QQ).** On a toy sector with `dim V = 3`, multiplicity `m = 2`, generic left-invariant `D_V` and generic block-scalar `a_i = A_i ⊗ 1_m`, I verified: `[D,a₁]`, `[D,a₂]`, and the 3-fold word `a₁[D,a₂][D,a₃]` are each block-scalar `(·)⊗1_m`, and the generation-0 slice equals the generation-1 slice EXACTLY ⇒ the A_K-built form cannot distinguish generations.

**Sharpness (my own escape-route test, beyond the registry sketch — this is the load-bearing Axis-A finding for D4 scope).** I sharpened the claim by asking what an operator must do to BREAK blindness. Two cases:
- A perturbation that COMMUTES with the block-scalar algebra (e.g. `1_V ⊗ σ_x`) drops out of `[D,a]` entirely (`[D_V⊗1_m + 1_V⊗σ_x, A⊗1_m] = [D_V,A]⊗1_m`), so it CANNOT create a handle. This shows the leg-blindness of `[D_K,a]` follows from the block-scalar structure of the **algebra alone** (Skolem–Noether) — even sharper than "D_K left-invariant."
- A perturbation that ENTANGLES the legs non-trivially (e.g. `M_V ⊗ σ_x` with `[M_V, A] ≠ 0`) yields a one-form that is NOT block-scalar; its generation-distinguishing content lives precisely in the off-diagonal generation block `[M_V,A]⊗σ_x`. I confirmed `[D_ext,a₂]` is NOT block-scalar over QQ, with the explicit non-zero `[M_V,A₂]` handle.

This is exactly the theorem's claim made operational: **the only way to a per-generation SHAPE handle is an operator OUTSIDE the A_K differential calculus that genuinely entangles the orbital leg V and the generation leg ℂ^m** — i.e. the external `ε_LX` channel (the §VII.BL non-LI fibre connection) and its right-regular avatar (the D4 channel). The A_K class is sealed.

**Spectral-functional note (Axis-A).** D3 is purely representation-theoretic; no spectral functional, regulator, or moment enters. The multiplicity-scalar lock is L_max-INVARIANT (it is a representation-class identity holding at every truncation — the §VII.BL `R_cross = 1` non-binding Level-2). There is no scheme in which an A_K-built cocycle acquires generation structure. FUNCTIONAL-INDEPENDENT.

> **D3 verdict: PASS** — re-derived from Skolem–Noether block-scalar `π(a)=⊕π_{(p,q)}(a)⊗1_{m(p,q)}` + subalgebra closure under product/commutator. Confirmed over QQ (block-scalar closure + generation-slice equality) and sharpened (the escape requires a genuinely leg-entangling NON-A_K operator). FUNCTIONAL-INDEPENDENT, L_max-INVARIANT.

---

## III. Gate Verdicts

| Gate / Clause | Verdict (Axis-A) | Decisive content |
|:--------------|:-----------------|:-----------------|
| D1 — `Tr[γ₉ D_K^{2k+1}] ≡ 0` | **PASS** | `{γ₉,D_K}=0` + cyclicity ⇒ exact 0; QQ-confirmed odd powers 1–9 on dim-6 block; per-block exact-zero (operational-L downgrade UNAFFECTED) |
| D2 — even moment ⇒ C₂ only | **PASS** | `[J,D_K]=0` BDI conjugate-pair (p,q)↔(q,p) cancels conjugation-ODD C₃ (`(p−q)\|C₃`), doubles conjugation-EVEN C₂; QQ-confirmed parities + cancellation |
| D3 — A_K-built ⇒ multiplicity-scalar | **PASS** | Skolem–Noether `π(a)=⊕π_{(p,q)}(a)⊗1_{m(p,q)}` + subalgebra closure; QQ-confirmed block-scalar + gen-slice equality; sharpness ⇒ escape is NON-A_K leg-entangling only |

**JOINT-clause posture (for the closeout's PASS-AND).** D1, D2, D3 are the closed-INTERNAL clauses of §VII.CK. On the Axis-A leg I PASS all three independently. On PASS-AND with the Axis-B blind verify, §VII.CK promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT with the **D4-open scope qualifier RETAINED** (`class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}`; D4 right-regular SU(3)_R is a separate gate `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`, on which I make NO claim here).

---

## IV. Structural Implications

1. **The SHAPE obstruction is regulator-invariant (Axis-A's signature contribution).** D1/D2/D3 are properties of `(γ₉, J, A_K)`, not of any spectral functional. The fermion-mass generation SHAPE texture is external to the A_K/Casimir/γ₉-trace class under EVERY regularization — cutoff, zeta `S_ζ=ζ_{D_K}(0)`, anomaly-derived, alike. There is no "switch the spectral functional" escape from the obstruction (contrast: the cosmological-constant problem, where the a₀ term's presence/absence IS scheme-dependent — here the obstruction is scheme-independent because it lives in the symmetry algebra, not in a moment).

2. **Three orthogonal axes, one mechanism.** §VII.CK (γ₉/orientation axis: D1 supertrace + D2 even-moment + D3 orientation-cocycle) is a STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV (crossing-slope SIGN axis) and §VII.BL (hierarchy MAGNITUDE axis), all riding the multiplicity-scalar lock. Cross-observable/cross-corner co-primary remains FORBIDDEN (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`); this entry is a companion, not a co-primary anchor. I concur with that classification.

3. **The escape is precisely located (sharpness finding).** My D3 sharpness test shows the ONLY route to a per-generation handle is a NON-A_K operator that entangles the orbital leg V with the generation leg ℂ^m. This is the `ε_LX` channel (§VII.BL) and its right-regular `R_{E_α}` avatar (the D4 door). The D1–D3 wall does not close D4 — and correctly does not claim to (the registry's scope qualifier is honest). This is the seam the D4-discharge gate must address.

4. **NON-PROMOTION-BY-HELD-NUMBER / sign-lock classification is correct.** The held quantity is a sign-PATTERN (uniform sign forced; no sign-changing per-generation scalar). It is NOT dimensionful-slot-collision, NOT undischarged-magnitude-bound. The Level-2 envelope is NON-BINDING / structurally-exact (the multiplicity-scalar lock holds identically at every L_max; no `c_continuum`). A plan-freeze auditor must read it as the NON-PROMOTION overlay, not as a convergence bridge. I concur (this is the §VII.BL/§VII.BV precedent).

---

## V. Carry-Forward Computations

This gate is a Stage-2 BLIND verify; its primary output is the per-clause verdict. The carry-forwards below are genuine future computations surfaced by the re-derivation (4-field specs per `feedback_fix-in-session-never-defer.md`).

V.1. **D4 right-regular SU(3)_R discharge (the open seam).**
   - **What**: complete `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` — verify the right-root operator `R_{E_α}` (`t(O)=±1`) is admissible only via the crossed product `A_K ⋊ SU(3)_R`, OUTSIDE `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0 (mod 3)` center-character selection rule; confirm the residual=1.0 EXACT numerical shadow. My D3 sharpness test already localizes the escape to a leg-entangling NON-A_K operator — `R_{E_α}` is the candidate; the gate must verify it is genuinely external (crossed-product) and not an A_K one-form in disguise.
   - **Inputs**: §VII.CK D4-disposition annotation (S114 W-2 `w-2-d4-rightreg-su3r-admissibility.md`); the center-character selection rule `t(p,q)=(p−q) mod 3`; `dirac_spectrum.py` right-regular SU(3)_R action; the W3-1 `CF-S114-YUK-RIGHTREG-CONNECTION` residual.
   - **Gate**: `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` — Axis-A (spectral-geometer/lizzi) × Axis-B (volovik), kk EXCLUDED by §VII.BL downstream-inheritance. PASS-AND on the crossed-product externality ⇒ §VII.CK upgrade to STAGE-3-PERMANENT-UNCONDITIONAL (D4 row CLOSED-EXTERNAL-AS-A-COUPLING tag-flip).
   - **Effort**: 2–3 hours, 1 agent session per axis + closeout.

V.2. **FUNCTIONAL-INDEPENDENCE registry annotation (Axis-A finding).**
   - **What**: register the Axis-A structural reading that D1/D2/D3 are FUNCTIONAL-INDEPENDENT (hold under cutoff/zeta/anomaly-derived alike) as an explicit clause on §VII.CK — the obstruction is regulator-invariant because it lives in `(γ₉,J,A_K)`, not in a spectral moment. Distinguishes §VII.CK's scheme-independence from scheme-DEPENDENT observables (e.g. the a₀/CC term).
   - **Inputs**: this synthesis §I + §IV.1; the §VII.BL non-binding Level-2 precedent; `regulator-pin-discipline.md` FI/RD/MIXED taxonomy.
   - **Gate**: methodology-class registry annotation (artifact-existence PASS); mack-cosmic-bridge sole writer if it touches the falsifier surface, else gen-physicist registry patch. Not a numerical gate.
   - **Effort**: 0.5–1 hour, in-session designated-writer patch.

V.3. **D2 C₃-externality cross-check via the explicit anomaly invariant (optional sharpening).**
   - **What**: confirm that the conjugation-odd C₃ is identifiable with the su(3) cubic d-symbol anomaly invariant, and that the BDI even-grading is exactly the statement "the γ₉-graded spectral action carries no gauge anomaly on the generation leg" — tightening the link between D2 and the anomaly-derived spectral action (my domain).
   - **Inputs**: the C₃ = `(p−q)(p+2q+3)(2p+q+3)/18` factorization (this synthesis); Andrianov-Lizzi anomaly-derivation of the bosonic action (`researchers/Lizzi/` 1001.2036); `[J,D_K]=0` BDI.
   - **Gate**: INFO — `D2-ANOMALY-IDENTIFICATION` (PASS iff the conjugation-odd C₃ coincides with the cubic anomaly invariant up to normalization; INFO otherwise). Strengthens but does not gate the §VII.CK promotion.
   - **Effort**: 1–2 hours, 1 agent session.

---

## VI. Summary Table

| # | Clause | Classification | Axis-A Verdict | Implication |
|:--|:-------|:---------------|:---------------|:------------|
| D1 | `Tr[γ₉ D_K^{2k+1}] ≡ 0` (`{γ₉,D_K}=0`) | GEOMETRIC | **PASS** | Odd γ₉-supertrace is exact 0 at every τ/L_max; no orientation-slope handle; FUNCTIONAL-INDEPENDENT |
| D2 | even moment ⇒ C₂ only (`[J,D_K]=0` BDI) | GEOMETRIC | **PASS** | The only surviving γ₉-moment is blind to the generation-resolving C₃; FUNCTIONAL-INDEPENDENT |
| D3 | A_K-built ⇒ multiplicity-scalar (Skolem–Noether) | GEOMETRIC | **PASS** | Every A_K one-form/cocycle is ⊗1 on the generation leg; escape requires NON-A_K leg-entangling operator (ε_LX/D4); FUNCTIONAL-INDEPENDENT, L_max-INVARIANT |
| — | §VII.CK D1–D3 closed-INTERNAL wall | GEOMETRIC (intra-pillar obstruction) | **PASS-AND eligible** | On PASS-AND with Axis-B ⇒ STAGE-3-PERMANENT, D4-open scope qualifier RETAINED |

**Bottom line (Axis-A):** §VII.CK clauses D1, D2, D3 independently re-derive and reproduce on the spectral-functional axis — **PASS / PASS / PASS** — with the additional structural finding that all three are FUNCTIONAL-INDEPENDENT (regulator-invariant; no spectral-functional escape). I make no claim on D4, which is correctly out of scope and owed to a separate gate.
