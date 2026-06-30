# Session 115 W1-1 Synthesis: §VII.CK Stage-2 BLIND Axis-B Independent Verify (D1/D2/D3)

**Date**: 2026-06-24
**Agent**: kitaev-quantum-chaos-theorist (Axis-B reviewer — quantum-chaos / spectral-statistics / operator-algebra axis)
**Gate**: S115-VIICK-STAGE2-VERIFY (Axis-B leg)
**Source Documents** (read; blind protocol):
- `sessions/permanent-results-registry.md` — registered §VII.CK entry (master-index row 173 + section body §22422–22461), read up to end-of-file boundary
- Permanent anchors verified via knowledge MCP: `{γ₉,D_K}=0` (S34/S56), `[J,D_K]=0` (S17a, KO-dim 6), `t=(p−q) mod 3` (`proven_384`)
- `.claude/templates/synthesis.md`

**Blindness attestation** (load-bearing per `joint-theorem-promotion.md` §"Stage 2" + `epistemic-discipline.md` §"What Counts as a Result"): I did NOT open the originating workshop transcript `ws-s113-7-yukshape/ws-s113-7-yukshape-verdict.md`, did NOT open the Axis-A reviewer synthesis, did NOT read the D1 W3-3 npz artifact, and did NOT coordinate with any agent. Every clause below is re-derived from the registered claim text plus the three permanent anchors, using my own exact symbolic computation (Sage QQ). Substrate-input-orthogonality holds: my D1/D2/D3 derivations consume the registered entry text + the operator-algebra structure of `A_K`, NOT the numerical artifact Axis-A consumes.

---

## I. Session Outcome

**All three CLOSED-INTERNAL clauses verify: D1 = PASS, D2 = PASS, D3 = PASS.** The §VII.CK obstruction theorem holds on the homogeneous Jensen-deformed spectral triple `(A_K, H_K, D_K, γ₉, J)` over the registered scope `class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}`: no G-invariant functional in that class can supply a non-monotone sign-changing per-generation (multiplicity-leg `t`) scalar. Each clause reduces to an exact algebraic identity I reproduced independently with Sage QQ (machine-exact rationals, no float round-off). The D4 right-regular SU(3)_R door is explicitly OUT OF SCOPE for this Stage-2 verdict (the registered scope qualifier excludes it; D4's disposition is owed to the separate gate `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` per task W2-1) and I do NOT verdict it here.

On Axis-B PASS-AND with the Axis-A reviewer (if Axis-A also PASSes all three), §VII.CK promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT with the D4-open scope qualifier RETAINED.

---

## II. Key Results

### D1 — Tr[γ₉ D_K^odd] ≡ 0 (γ₉-graded odd-power supertrace vanishes)

**Result**: STRUCTURAL IDENTITY, machine-exact. Classification: **GEOMETRIC** (a property of the substrate spectral triple's chirality grading γ₉ acting on D_K — the fabric itself, not its excitations).

The claim is that the γ₉-graded supertrace of any ODD power of D_K is identically zero, per-block and L_max-invariant. I re-derive it from the single permanent anchor `{γ₉, D_K} = 0` (S34/S56 — γ₉ is the Cl(8) imaginary-only chirality generator; I confirmed via knowledge MCP that the anticommutator block structure `{D_K, γ₉}` appears in S35 with the KO-dim-6 condition set `J²=+1, JD=+DJ, Jγ=−γJ`).

The substitution chain (my own, not lifted):
- Step 1: `{γ₉, D_K} = γ₉ D_K + D_K γ₉ = 0` ⇒ `γ₉ D_K = −D_K γ₉`.
- Step 2: `Tr[γ₉ D_K^{2k+1}] = Tr[(γ₉ D_K) D_K^{2k}] = Tr[(−D_K γ₉) D_K^{2k}] = −Tr[D_K γ₉ D_K^{2k}]`.
- Step 3: cyclicity of the trace ⇒ `−Tr[D_K γ₉ D_K^{2k}] = −Tr[γ₉ D_K^{2k} D_K] = −Tr[γ₉ D_K^{2k+1}]`.
- Step 4: therefore `2·Tr[γ₉ D_K^{2k+1}] = 0` ⇒ `Tr[γ₉ D_K^{2k+1}] = 0` EXACTLY (the trace is its own additive inverse). The argument uses only the anticommutator and cyclicity, so it is INDEPENDENT of L_max and of τ.

**Independent exact check (Sage QQ).** I built a generic chirality-paired block: γ₉ = diag(+1,…,−1,…), and the most general D with `{γ₉,D}=0` (= purely chirality-off-diagonal, `[[0,X],[Y,0]]`) with symbolic entries over QQ. Confirmed `{γ₉,D}=0` by construction, then:
- `Tr[γ₉ D¹] = Tr[γ₉ D³] = Tr[γ₉ D⁵] = 0` EXACTLY for fully generic symbolic entries (both balanced 2+2 and unbalanced 2+1 chirality splits).

I deliberately stress-tested against a vacuity failure mode — "is this just `γ₉`-trace is always 0?" — by examining EVEN powers. For a purely chirality-off-diagonal D, `Tr[γ₉ D^{2k}] = Tr[(XY)^k] − Tr[(YX)^k] = 0` by cyclicity even when `dim₊ ≠ dim₋`, and the only nonzero graded trace is the McKean–Singer index at `k=0`: `Tr[γ₉ D⁰] = dim₊ − dim₋ = 1` for the 2+1 block. This is the correct and important structural distinction: a supersymmetrically-paired (chirality-off-diagonal) D has ALL graded power-traces collapse except the index. The odd-power vanishing is therefore not vacuous — it is forced by the anticommutator + cyclicity precisely as the registry states, and it correctly leaves the index (a topological, generation-blind integer) as the sole γ₉-graded survivor of the off-diagonal part.

A quantum-chaos reading reinforces this: the γ₉-graded odd-power supertrace is the leading odd "spectral-form-factor"-type chirality moment. `{γ₉,D_K}=0` is a hard chiral (sublattice/BDI) symmetry; it pins the spectrum into ±λ pairs, and in any ±λ-symmetric spectrum every odd moment of the chirality-weighted spectral density cancels pairwise by construction. There is no dynamical content for an odd γ₉-moment to encode — it is a symmetry-forced zero, the same mechanism that kills odd Lyapunov-spectrum sums in chiral random-matrix ensembles. **D1 confirms the structural identity. VERDICT: PASS.**

### D2 — Tr[γ₉ f(D_K²)] is conjugation-even ⇒ carries C₂ only (NOT C₃)

**Result**: STRUCTURAL IDENTITY, machine-exact. Classification: **GEOMETRIC / PARTICLE** (the representation-theoretic content of D_K — which Casimir invariants its even spectral moments can resolve).

The claim: `Tr[γ₉ f(D_K²)]` survives D1 (because `D_K²` is γ₉-EVEN, `{γ₉,D_K}=0 ⇒ [γ₉,D_K²]=0`, so the γ₉-graded trace of an even function need not vanish), BUT because `f(D_K²)` is a function of the conjugation-EVEN quantity `|λ|²`, the BDI reality `[J,D_K]=0` forces it to carry the quadratic Casimir `C₂` and NOT the cubic `C₃`. I verified `[J,D_K]=0` / KO-dim-6 independently via knowledge MCP (the `[J, D_K(τ)] = 0` inline entry, S17a, with the full BDI condition set).

The decisive step is identifying the conjugation operation on the spectral data with the irrep ↔ conjugate-irrep map `C: (p,q) → (q,p)` (complex conjugation / charge conjugation, which J implements on the representation content; `J` is antilinear and `D_K²` is built from `|λ|²` which is J-invariant). On the multiplicity/sector labels, J-conjugation-evenness of `f(D_K²)` means the functional must be SYMMETRIC under `(p,q) ↔ (q,p)`.

**Independent exact check (Sage).** I wrote the standard SU(3) Casimirs symbolically and tested their parity under `(p,q) → (q,p)`:
- `C₂(p,q) = ⅓(p² + q² + pq + 3p + 3q)`: `C₂ − C₂∘C = 0` EXACTLY ⇒ **C₂ is conjugation-EVEN**.
- `C₃(p,q) = (1/18)(p−q)(p+2q+3)(2p+q+3)`: `C₃ + C₃∘C = 0` EXACTLY ⇒ **C₃ is conjugation-ODD** (`C₃∘C = −C₃`).

Numerical spot-checks confirm: the conjugate pair `(1,0)/(0,1)` gives `C₂ = 4/3` (equal — even) but `C₃ = +10/9 / −10/9` (opposite — odd); the self-conjugate `(1,1)` gives `C₂ = 3`, `C₃ = 0`. Crucially, `C₃ ∝ (p−q)` — i.e. the cubic Casimir is the UNIQUE low-order invariant that carries the factor `(p−q)`, which mod 3 IS the generation index `t`. So `C₃` is precisely the invariant that could in principle carry per-generation sign-changing (non-monotone) structure, and it is exactly the one a conjugation-EVEN even-moment functional CANNOT build.

This closes the door cleanly: `Tr[γ₉ f(D_K²)]`, being even under J-conjugation, lands in the even-invariant span (`C₂` and its powers / even polynomials), which is monotone in `(p+q)`-type magnitude and carries NO `(p−q)` sign handle. The one Casimir that does carry the generation-sign handle (`C₃ ∝ (p−q)`) is forbidden by the reality structure. The substrate's own BDI reality is what kills the SHAPE handle at the even-moment door. **D2 confirms the even-grading ⇒ C₂-only argument, and confirms it lands on the operative observable (`C₃` is the `(p−q)`-carrier). VERDICT: PASS.**

### D3 — A_K-built one-forms are multiplicity-SCALAR on the generation leg (Skolem–Noether leg-membership)

**Result**: STRUCTURAL IDENTITY, machine-exact. Classification: **GEOMETRIC** (operator-algebra structure of the spectral triple — how `A_K = ℂ⊕ℍ⊕M₃(ℂ)` and its differential calculus act on the multiplicity leg).

The claim: every `A_K`-built cyclic-cocycle / one-form `Tr[γ₉ a₀[D,a₁][D,a₂][D,a₃]]` (`aᵢ ∈ A_K`) is multiplicity-SCALAR on the generation leg `ℂ^{m(p,q)}` by Skolem–Noether leg-membership — each `[D_K, a]` maps into `⊕ B(V_(p,q)) ⊗ 1_{m(p,q)}`, acting as identity on the `ℂ^{m(p,q)}` multiplicity factor — hence generation-blind on the `t`-leg. I re-derive this from TWO independent angles, both confirmed exactly.

**Angle 1 — Wedderburn / Skolem–Noether double-commutant (operator algebra).** `H_K` decomposes as `⊕_(p,q) V_(p,q) ⊗ ℂ^{m(p,q)}`. A simple summand `B = M_n(ℂ)` of `A_K` (and the G-equivariant `D_K` built over it) acts only on the REPRESENTATION factor `V_(p,q)`; by Skolem–Noether every automorphism / element of a simple algebra acting on `V ⊗ ℂ^m` that is `B`-linear is `B ⊗ (something on the commutant)`, and an algebra element itself is `b ⊗ 1`. The commutant of `{b ⊗ 1_m : b ∈ M_n}` is exactly `{1_n ⊗ c : c ∈ M_m}` (the multiplicity algebra), and the double commutant returns `M_n ⊗ 1_m`. I verified the commutation core in Sage over QQ with fully symbolic `a ∈ M₃` and `b ∈ M₃` (3 generations): `[a⊗1_m, 1_n⊗b] = 0` for GENERIC `a, b`. Therefore any `A_K`-built operator (rep-leg algebra element, or any polynomial in `[D_K, aᵢ]` which all live in the rep-leg algebra) commutes with the full multiplicity algebra ⇒ lies in `M_n ⊗ 1_m` ⇒ acts as `⊗1` (scalar) on the generation leg. A product of multiplicity-scalars is multiplicity-scalar, so the full degree-3 cocycle is `⊗1` on the `t`-leg.

**Angle 2 — Z₃ center-character selection rule (representation theory).** The generation index `t = (p−q) mod 3` is the SU(3) center `Z₃` character (verified PROVEN via knowledge MCP: `proven_384`, with the center-character selection rule `t(a) = t(b) + t(O) mod 3`). An operator `O` connects sector `(a)` to sector `(b)` iff the trivial rep occurs in `ā ⊗ O ⊗ b`, i.e. `t(a) = t(b) + t(O) mod 3`. I verified the underlying fact — that triality is ADDITIVE and uniform across SU(3) tensor products — exactly in Sage via `WeylCharacterRing("A2")`: for `3⊗3`, `3⊗3̄`, `8⊗3`, `6⊗3̄`, `8⊗8`, `10⊗8`, EVERY irrep component of the product carries triality `t(A) + t(B) mod 3` (uniform; the Z₃ grading is a ring homomorphism). An `A_K`-built one-form `[D_K, a]` is built from the G-equivariant `D_K` (center-character 0) and `a ∈ A_K` acting color-singlet (center-character 0), so `t(O) = 0`. The selection rule then forces `t(a) = t(b)`: the operator is triality-DIAGONAL, it can distinguish SECTORS (`(p,q)` blocks) but it CANNOT move between the three generations (which differ by `t`), so it acts as `⊗1` on the multiplicity leg = multiplicity-scalar.

The two angles agree and are mutually reinforcing: leg-membership (the algebra acts on the rep leg, identity on multiplicity) IS the operator-algebra shadow of `t(O)=0` (center-character-preserving). Either way, no `A_K`-built / Casimir-graded / γ₉-traced functional reaches the generation leg non-scalarly. The crossing-SHAPE handle the SM fermion mass texture needs (a sign-changing function OF the generation label) is therefore not internal to this class — it must come from outside (the registry names the external `ε_LX` channel; that externality claim is about D4 and is out of scope for my verdict, but the INTERNAL obstruction — that NO `A_K`-built form supplies it — is what D3 asserts and what I confirm). **D3 confirms leg-membership ⇒ multiplicity-scalar via two independent exact derivations. VERDICT: PASS.**

---

## III. Gate Verdicts

| Gate (clause) | Verdict | Decisive Number / Identity |
|:--------------|:--------|:---------------------------|
| D1 — `Tr[γ₉ D_K^odd] ≡ 0` | **PASS** | `2·Tr[γ₉ D_K^{2k+1}] = 0` from `{γ₉,D_K}=0` + cyclicity; Sage QQ: `Tr[γ₉ D^{1,3,5}] = 0` EXACT, generic symbolic D; even-power survivor = McKean–Singer index `dim₊−dim₋` only |
| D2 — even-grading ⇒ C₂ only | **PASS** | Sage exact: `C₂ − C₂∘C = 0` (EVEN); `C₃ + C₃∘C = 0` (ODD); `C₃ ∝ (p−q) = t`-carrier ⇒ forbidden to a conjugation-even functional |
| D3 — leg-membership ⇒ multiplicity-scalar | **PASS** | Sage exact: `[a⊗1, 1⊗b]=0` generic (Skolem–Noether double commutant); triality additive & uniform across `3⊗3 … 10⊗8` ⇒ `t(O)=0` ⇒ triality-diagonal ⇒ `⊗1` on generation leg |
| D4 — right-regular SU(3)_R | **OUT OF SCOPE** | NOT verdicted here (registered scope excludes D4; owed to `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` / task W2-1) |

**Per-clause PASS-AND eligibility**: all three in-scope clauses (D1, D2, D3) PASS on Axis-B. On Axis-A PASS-AND, §VII.CK is eligible for STAGE-3-PERMANENT with the D4-open scope qualifier RETAINED.

---

## IV. Structural Implications

**The obstruction is a symmetry-forced zero, not a dynamical bound.** As a quantum-chaos diagnostician I note what this theorem is and is NOT. It is NOT a chaos/scrambling statement — there is no Lyapunov exponent, no OTOC growth rate, no level-spacing classification at issue. It is a SELECTION-RULE / symmetry obstruction: three hard symmetries of the homogeneous substrate (`{γ₉,D_K}=0` chiral/BDI; `[J,D_K]=0` reality; `t=(p−q) mod 3` Z₃ center) each independently forbid a different functional sub-class from carrying a sign-changing per-generation handle. This is the correct epistemic type for the registry's NON-PROMOTION-BY-HELD-NUMBER / sign-lock tag (the held quantity is a sign-PATTERN forced uniform, exactly as `cross-pillar-bridge-anatomy.md §"Non-Promotion-by-Held-Number Meta-Taxonomy"` requires).

**L_max-invariance is structurally correct, not an empirical plateau.** All three clauses are exact at every truncation: D1 is per-block exact-zero (no cross-sector cancellation to converge), D2 is a parity statement on the Casimir polynomials (truncation-independent), D3 is an operator-algebra/center-character identity (holds for every `(p,q)` block). The registry's NON-BINDING / structurally-exact Level-2 classification (no `c_continuum` the substrate converges TO) is the right reading — and consistent with my framework-wide finding that this internal geometry is fabric-scale integrable (no scrambling, lambda_L=0; the obstruction lives on the same homogeneous, symmetry-protected substrate). A plan-freeze auditor reading this as a convergence bridge would mis-HARD-HALT on the non-binding Level-2; it must be read as the NON-PROMOTION overlay (the §VII.BL / §VII.BV precedent), which is what the entry states.

**Companion structure is respected.** §VII.CK is a STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV (crossing-slope SIGN axis) and §VII.BL (hierarchy MAGNITUDE axis) on the third γ₉/orientation axis. My verdict does not treat it as a co-primary anchor of either (cross-observable co-primary correctly FORBIDDEN per the algebra-axis orthogonality K=3 clause). The shared mechanism (multiplicity-scalar lock) acting on three orthogonal observables (SIGN / MAGNITUDE / γ₉-orientation) is internally consistent: the SHAPE branch (D1 supertrace + D2 even-moment + D3 orientation-cocycle) is the γ₉-axis instance of the same homogeneity obstruction.

**What this opens/closes.** CLOSES the internal SHAPE-handle question over `{A_K-built ∪ Casimir-graded ∪ γ₉-traced}` (no internal functional in that class delivers fermion-mass generation SHAPE). LEAVES OPEN (by registered scope, not by my verdict) the D4 right-regular SU(3)_R connection — the one candidate with non-scalar leg content, which escapes the `t(O)=0` wall because the right-regular root operators carry `t(O)=±1`. The D4 disposition (CLOSED-EXTERNAL-AS-A-COUPLING per S114 W-2) is a SEPARATE Stage-2 gate; I make no claim on it.

---

## V. Carry-Forward Computations

V.1. Axis-A / Axis-B PASS-AND closeout for §VII.CK promotion
   - **What**: Logical AND of the two blind Stage-2 verdicts on D1, D2, D3; on PASS-AND across both axes, flip §VII.CK STAGE-1-CANDIDATE → STAGE-3-PERMANENT (D4-open scope qualifier RETAINED), emit the canonical dual-SHA verdict line for `S115-VIICK-STAGE2-VERIFY`.
   - **Inputs**: this synthesis (`session-115-w1-viick-verify-axis-b.md`, Axis-B = PASS/PASS/PASS); the Axis-A reviewer synthesis; registered §VII.CK block (registry §22422–22461); `joint-theorem-promotion.md` §"Stage 2/3".
   - **Gate**: `S115-VIICK-STAGE2-VERIFY` — PASS iff (Axis-A PASS-AND Axis-B) on EACH of D1, D2, D3; any clause FAIL/INFO on either axis blocks promotion (stays STAGE-1-CANDIDATE; route failing clause to remediation).
   - **Effort**: <1 hour, 1 closeout agent session (this is task #6, the designated gen-physicist closeout; I do NOT emit the verdict line — the closeout owns it).

V.2. D4 right-regular SU(3)_R unconditional discharge (separate Stage-2 gate)
   - **What**: Independent two-axis verify of the D4 CLOSED-EXTERNAL-AS-A-COUPLING disposition — that the right-regular root operator `R_{E_α}` (`t(O)=±1`) is admissible only via the crossed product `A_K ⋊ SU(3)_R`, OUTSIDE `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` center-character selection rule; verify the commutant theorem (`‖[L_g, Y_R]‖_F → 0`) and the forced Z₃-circulant texture independently.
   - **Inputs**: registered §VII.CK D4-disposition annotation (registry §22458–22460); S114 W3-1 residual=1.000000 (`t(O)=0` Cartan); the `t(O)=±1` root-operator selection rule (verified additive/uniform in this synthesis, Sage `WeylCharacterRing`); `inheritance-falsifier-protocol.md` if rank(ker) ≥ 2.
   - **Gate**: `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` — PASS iff both blind axes confirm D4 external-as-a-coupling; on PASS, §VII.CK scope qualifier upgrades to STAGE-3-PERMANENT-UNCONDITIONAL (genus complete over `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}`). Reviewers MUST EXCLUDE §VII.BL co-authors/downstream-inheritance (kk excluded) per the Axis-B selection protocol.
   - **Effort**: 2–3 hours, 2 blind reviewer agent-sessions + 1 closeout (this is task #9 / W2-1, spectral-geometer × volovik).

V.3. Cross-check D2 against the full McKean–Singer index density at finite τ (optional firming)
   - **What**: Confirm that `Tr[γ₉ f(D_K²)]` for the framework's actual block-diagonal `D_K(τ_fold)` evaluates to a function of `C₂(p,q)` only (no `C₃` content) by direct numerical projection onto the Casimir basis, sector-by-sector — closing the gap between the symbolic parity argument (verified here) and the concrete spectrum.
   - **Inputs**: `dirac_spectrum.py` block builder at `τ_fold=0.190`; `γ₉ = I_{dim(p,q)} ⊗ γ₉` lift per block; the symbolic `C₂/C₃` parities established in this synthesis; `canonical_constants.py` (`tau_fold`).
   - **Gate**: new INFO gate `S116-D2-CASIMIR-PROJECTION` — INFO: report the C₃-content coefficient (expected machine-zero); PASS-band `|C₃-coefficient| < 1e-10` would firm D2 numerically (it is already structurally PASS — this is corroboration, not a gate the promotion depends on).
   - **Effort**: 2–3 hours, 1 agent session (OPTIONAL — D2 is structurally closed without it).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | D1 `Tr[γ₉ D_K^odd] ≡ 0` (from `{γ₉,D_K}=0` + cyclicity; Sage QQ exact, generic D) | GEOMETRIC | **PASS** | Odd γ₉-supertrace symmetry-forced zero; only index survives off-diagonal part — no odd SHAPE handle |
| 2 | D2 even-grading ⇒ C₂ only (`C₂` even, `C₃` odd under `(p,q)↔(q,p)`; `C₃ ∝ (p−q)=t`) | GEOMETRIC / PARTICLE | **PASS** | BDI reality forbids the `(p−q)`-carrying cubic Casimir at the even-moment door — the one invariant that could sign-change per generation |
| 3 | D3 leg-membership ⇒ multiplicity-scalar (Skolem–Noether double commutant `[a⊗1,1⊗b]=0`; `t(O)=0` ⇒ triality-diagonal) | GEOMETRIC | **PASS** | Every `A_K`-built one-form is `⊗1` on the generation leg; cannot move between generations — generation-blind by two independent routes |
| 4 | §VII.CK D1∧D2∧D3 closed-internal class (Axis-B leg) | GEOMETRIC | **PASS-AND-eligible** | On Axis-A PASS-AND ⇒ STAGE-3-PERMANENT (D4-open scope qualifier retained); promotion verdict owned by closeout (task #6) |
| 5 | D4 right-regular SU(3)_R | GEOMETRIC | **OUT OF SCOPE** | Not verdicted on Axis-B; separate Stage-2 gate `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (task #9 / W2-1) |
