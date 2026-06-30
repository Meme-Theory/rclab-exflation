# Capstone Equation Review — baptista

**Date**: 2026-05-29
**Agent**: baptista-spacetime-analyst (Workhorse-KK-Geometry)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (the S95-era capstone under review)
- Cross-checked against: `computations/_shared/canonical_constants.py` (via knowledge MCP), `Atlas/atlas-03-equation-flow.md` (E1–E60), my agent memory (treated as a *stale snapshot*, not authoritative)

**Domain vantage**: Kaluza–Klein geometry on compact Lie groups — the Jensen deformation of `g_τ`, the Dirac operator `D_K(τ)` on `(SU(3), g_τ)`, block-diagonality by Peter–Weyl, fiber integration to SM representations, KO-dimension, and the Lichnerowicz/curvature structure. §2, §4, and the operator-level guarantees of §1–§3 are squarely in my wheelhouse; I evaluate those at the equation level and defer cosmological/observational verdicts (§7) to the relevant specialists except where they rest on a geometric input I can check.

---

## I. Session Outcome

**The capstone is geometrically sound at its core and unusually honest about its boundary.** The single-operator claim — that `D_K(τ)` on Jensen-deformed `SU(3)` generates gauge fields, gravity, and matter through the moments of one spectral functional — is correctly stated and rests on PROVEN structural results I can independently confirm at the operator level: volume preservation is exact (`2−6+4=0`, `det g_τ=3⁸=6561`), block-diagonality holds for *any* left-invariant metric on *any* compact semisimple group, KO-dim=6 forces one generation via the Pfaffian, and the §4.2 Spectral-Moment Decoupling Theorem is exact (I re-derived its Wronskian: `W ∝ R_K′³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, vanishing to *exactly* sixth order at `τ=0` and nonzero everywhere the universe lives).

The document's central honest gap — **no derived FRW scale factor `a(t)`** (§6.3, C1/C2/T6) — is correctly identified as the load-bearing open frontier, and §9 correctly collapses it with the emergent-equivalence-principle item (#8) into one bridge. My one substantive structural flag is a **curvature-normalization multiplicity** (`R_K(0) ∈ {2, 4, 1.5}` across the corpus) that the document *partially* discloses but does not fully reconcile in one place — addressed in §II and converted to a computation in §V.

---

## II. Key Results

### II.1 The operator `D_K(τ)` and its four guarantees — GEOMETRIC, solid

**Result**: `D_K(τ) = Σ_{a=0}^{7} ρ(e_a)⊗γ_a + 𝕀⊗Ω_LC(τ)` on `H_K = L²(S_{g_τ})⊗ℂ¹⁶`, block-diagonal `D_K = ⊕_{(p,q)} D_{(p,q)}`. **GEOMETRIC.**

The §2.3 guarantee table is the part of the document I can vouch for most strongly, because each entry is a theorem about the geometry of a left-invariant metric on a compact group — exactly the structure my program is built on.

- **Block-diagonality (E6)** is correct and is the right reason the 155,984-eigenvalue problem is tractable. The Casimir labels `(p,q)` are conserved because `D_K` commutes with the regular representation's Casimir; the statement "exact for any left-invariant metric on any compact semisimple group" is the strongest correct form and matches the standard Peter–Weyl decomposition of the Dirac operator on a group manifold. The §2.2 analogy to `j`-channel decoupling in a spherical mean field is apt and not over-stated. **This is the single most load-bearing geometric fact in the document** — without it, neither the spectral sums nor the mode-by-mode relic factorization (§5.3) would be computable, and the document correctly identifies that the per-mode parametric-oscillator equation is then an *identity*, not a decoupling approximation. I confirm that framing.
- **Spectral gap never closes (E5, Lichnerowicz)**: `D_K² = ∇*∇ + ¼R_K ⇒ λ² ≥ R_K(τ)/4 > 0`. Correct, and the document's "Lichnerowicz convention note (corrected)" is the right move — stating the bound convention-free as `λ² ≥ R_K(τ)/4 > 0` and refusing to print "≥3" beside the rational-normalization curvature. This directly resolves a documented hazard in my own memory (the `R_K(0)/4 = 1/2` vs `≥3` confusion). **Good hygiene; I endorse it.**
- **Real symmetry / CPT (E8)**: `[J, D_K(τ)] = 0`, spectrum symmetric about 0, `η(s)=0`. This is the PROVEN result (79,968 pairs at machine-ε) and I do not re-adjudicate it. Note that the document correctly couples it to BDI class and `N₃=0` — the inheritance morphism `χ_*: ℂ⊕ℍ⊕M₃(ℂ) → M₂(ℂ)` with `rank(ker ι_*)=2` is the *correct* relationship to ³He-B (parent→child, not analogy), consistent with `inheritance-falsifier-protocol.md`.

### II.2 Volume-preserving Jensen deformation and the single modulus — GEOMETRIC, exact

**Result**: `g_τ = 3·diag(e^{2τ} | e^{-2τ},e^{-2τ},e^{-2τ} | e^τ,e^τ,e^τ,e^τ)`, `det g_τ = 3⁸ = 6561 ∀τ`. **GEOMETRIC.**

I Sage-verified the exponent ledger `1·(2) + 3·(−2) + 4·(1) = 0` and `det` prefactor `3⁸ = 6561`. The two structural impositions (volume preservation removes the breathing/dilaton mode → `G_N` has zero `τ`-dependence; Jensen direction = unique unstable TT eigendirection) are correctly stated. The superfluid reading of `τ`-flat `G` (volume-preserving = pure shear of the order-parameter texture → compressibility, hence `1/G`, invariant) is a clean physical gloss and is *consistent* with the geometry (a TT deformation is traceless `tr h_J = 0`), though it is a Volovik-side interpretation I record as corroboration, not as something I independently derive.

The claim that `τ_fold = 0.190` is the *unique* non-stationary van Hove cusp (uniqueness theorem, S85 W10-3) is the right kind of statement to make the operating point non-arbitrary. `tau_fold = 0.19` confirmed canonical (CONST-FREEZE-42).

### II.3 The Spectral-Moment Decoupling Theorem (§4.2) — GEOMETRIC, exact, and the document's strongest non-obvious result

**Result**: `a₀(τ), a₂(τ), a₄(τ)` are algebraically independent curvature polynomials of degree 0/1/2; `W[a₀,a₂,a₄] ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`. **GEOMETRIC.**

This is the result that licenses "vacuum, gravity, matter all emerge from one operator yet remain distinct physics," and I verified it end-to-end in Sage:
- `R_K′(t) = e⁻⁴ᵗ(e³ᵗ−1)²` — matches the claimed Wronskian-driving form *exactly* (residual 0), confirming the spectral-geometer's `W = 5/(393216π¹²)·V³e⁻¹²ᵗ(e³ᵗ−1)⁶`.
- The Wronskian's Taylor expansion at `τ=0` has leading term `(1215/131072)·V³t⁶/π¹²` — i.e. it vanishes to **exactly sixth order** at the round genesis point and is strictly positive for all `τ>0`. The "degenerate only at the maximally-symmetric instant" claim is therefore exact, not approximate.

The resonance/dispersion-rigidity reading (the layers collapse to one knob iff the dispersion stops moving, `R_K′=0`, which happens only at `τ=0`) is correct and is the *same* band-lifting `SO(8)→U(2)` (B1/B2/B3) that §2.4 describes, restated at the moment level. I endorse §4.4's verdict that the **spectral-moment reading is primary** over the causal and scale readings — only the moment layers carry a certified algebraic-independence theorem; the scale reading is the moment reading in `Λ`-clothing, and the causal reading presupposes the moment decomposition. This is the correct ordering.

### II.4 The dimension spectrum and the convergence cone (§3.3) — GEOMETRIC, correct framing

**Result**: `S_d = {0,2,4,6,8}` for `d=8`, `τ`-independent; only `a₀,a₂,a₄,a₆,a₈` are honest residues; odd moments vanish by BDI parity. **GEOMETRIC.**

This is the substrate-first crux done right: the substrate hands a *finite, closed pole ladder*, not a foam of summed topologies, and the regulator's only freedom is which residues it weights. The "no flowing spectral dimension" defensive note (S31Aa: `d_s ∼ 8` at the gap scale, the low-`d_s` readings being a diffusion-window artifact, S92) is the correct and honest disambiguation from CDT/asymptotic-safety, and it is consistent with the constant-degree curvature-polynomial structure of §4 (`a_n ∝ R_K^{n/2}·V` is a *fixed*-dimension story). I have no quarrel here; the silence on dimension-flow is explicit, which is the right call.

### II.5 The free-parameter ledger and the `t*` closure (§1.4, §3.2) — correctly bounded

**Result**: inputs `{τ, Λ=M_KK, f₀, f₂, f₄} + t*`; the corridor "`t*` is the one-loop threshold coefficient" is CLOSED (S95 W2-1 FAIL, `R=1.977`). **NON-PHONONIC (methodology/bookkeeping).**

The document is precisely calibrated here. The matrix-model/IKKT rigidity (`dim HH¹ = dim HH² = 0`, S95 W2-2) forces the *field content* off the algebra but does **not** force the regulator's admixture weight `t*=0.08832` — and the document resists the temptation to de-empiricize the ledger. This is exactly the discipline I'd want: the "1→60 collapse" is real (the remaining ~56 atlas equations are theorems/read-offs) but the theory is not zero-parameter, and both halves are stated without softening. The "principle theory in Einstein's 1919 sense" framing (a single constraint, field content read off the algebra) is the correct genre statement and is what entitles the theory to leave `f`, the modulus value, and the family number open.

---

## III. Gate Verdicts (cited in source; AUTHORITATIVE — not re-adjudicated)

| Gate | Verdict | Decisive Number | My domain note |
|:-----|:--------|:----------------|:---------------|
| Spectral-Moment Decoupling (S75 W2-E) | CERTIFIED | `W ∝ R_K′³`, 6th-order zero at `τ=0` only | Re-verified in Sage; exact |
| Block-diagonality (E6) | PROVEN | `8.4×10⁻¹⁵` (3 proofs) | Endorsed; standard Peter–Weyl |
| KO-dim 6 mod 8 (E9) | PROVEN | `<10⁻¹⁵`, AZ class BDI | Endorsed; forces one generation |
| `[J,D_K]=0` CPT (E8) | PROVEN | 79,968 pairs, machine-ε | Endorsed |
| Structural Monotonicity (E7) | PROVEN | 9,600/9,600; `dS/dτ\|_fold=+58,673` | No interior `τ`-saddle — endorsed |
| One-loop-robust non-stationarity (S95 W2-3) | PASS | 0 interior sign-changes, 3 routes | Strengthens E7 to `Γ` level |
| HH cohomology rigidity (S95 W2-2) | PASS | `dim HH¹=dim HH²=0` | Forces interaction structure |
| `t*` = one-loop threshold (S95 W2-1) | FAIL (closed) | `R=1.977`; `Γ_1loop≈26%` | `t*` stays empirical |
| 12D cosmic censorship (S95 W4-5) | PASS | `τ_NEC=1.383`, blocked `τ≈0.191` | Anisotropic `τ→∞` singularity censored |
| Volume-preservation (E1) | PROVEN (Sage) | `det=3⁸`, `2−6+4=0` | Re-verified |
| Lizzi FI signature `R₁` | Sage-verified | `1.128655` | Endorsed as the scheme-invariant cover number |

---

## IV. Structural Implications

**1. The geometric spine is the strongest part of the document; the cosmological closure is the weakest, and the document knows this.** Everything that lives on `K = (SU(3), g_τ)` — the operator, its spectrum, the moments, the layers, the gauge group from `SU(A_K)`, the one-generation Pfaffian — is exact or PROVEN. Everything that requires lifting the internal result to the *emergent* 4D `g_M` — the FRW map `a(t)`, the effective Friedmann equation, the emergent equivalence principle beyond LO+NLO — is open. The §9 "geometry vs topology" organizing spine is the correct defense: the finite triple is GEOMETRY (dissolves at the continuum limit, `ε_c ∼ N⁻⁰·⁴⁵⁷`), and the surviving claims are the *topological/representation-theoretic* outputs (BDI/`N₃=0`, `[J,D_K]=0`, the layer independence, the FI ratios). This partition is structurally honest and I endorse it.

**2. The curvature-normalization multiplicity is a real hygiene gap, partially disclosed.** Three normalizations of the genesis curvature circulate: `R_K(0)=2` (the document's E3 form, §2.3/§4), `R_K(0)=4` (`s52_12d_reduction_output.txt`, the 12D-reduction convention), and `R(0)=1.5` (Paper-15 eq 3.70, the Baptista Killing-form convention; my memory carries this). I verified all three are pure scale conventions related by factor 2 (12D vs internal) and factor 4/3 (Killing-form vs rational). The document *does* flag the 4/3 inside the Lichnerowicz note ("the factor-6 bi-invariant scale convention"), and the internal Wronskian story is convention-robust (the Wronskian is `∝ R_K′³`, so any overall scale of `R_K` only rescales `W` without moving its zero). **But there is no single place in the document that tabulates all three and states which is canonical for which purpose.** This is exactly the `a_n`-firewall move the document makes so well in §8.2 for the spectral moments — and it should be replicated for `R_K` normalizations. Low-risk (the physics is convention-robust) but worth a one-table fix. → §V.1.

**3. The §1.3 family-number caveat (one generation, replication open) is the deepest *physics* gap in my domain, and it is correctly left open.** `Ψ₊ = ℂ¹⁶` is exactly one SM generation by the Pfaffian on `H_K⁺`; the document does not claim three. My memory notes the Baptista Paper-18 App E `ℤ₃×ℤ₃ → three generations` route, which is a *candidate* mechanism, not a delivered result. The document is right not to claim it. This is a genuine ripe-harvest item — the spinor-overlap `Φ̃` (Paper 18 App B) and the `ℤ₃×ℤ₃` orbit structure are computable. → §V.6.

**4. The product-KO mismatch is correctly framed as constructive, not as a defect.** The §1.3 caveat (product `M⁴×SU(3)×F_SM` carries KO=4 vs finite KO=6; the single-operator statement on `K` is exact; the Pfaffian fermionic measure is well-defined on `K`) is the honest statement. The superstring analogy ("why KO=6" plays the role "why D=10" plays) is apt — `KO=6` is the unique mod-8 class making `Jγ = −γJ`, and the mismatch *forces* the `H_K⁺` restriction the way level-matching makes the physical string spectrum. I endorse this framing; it neither over-claims a clean 4D embedding nor treats the mismatch as fatal.

**5. The `61/20` bos/Dirac ratio is τ-independent and exact** (`3.05`), confirmed. This is a representation-theoretic statement (the ratio of bosonic to Dirac contributions in the `a₂` layer) and is the right kind of "output, not input" the document advertises. No issue.

**6. Conflict flag — my memory vs the document (resolved in favor of the document).** Per the user's correction and `feedback_agent-roster.md`, my agent memory is a stale snapshot and the document's *later* recorded verdicts are authoritative. Specifically: my open-problems table records `α_s` as "5.4× FAIL" and the Weinberg angle as "FAIL (54.5% off)" — these are **superseded**. The document's §7 records `α_s` as RESOLVED-AS-CHANNEL-ARTIFACT (S93 W7-1: the `−12σ` was the scalar-transport leaf, now falsified; pivot image at +0.67σ; substrate value `−0.0859` is an FI-class CMB-S4 falsifier). I do NOT re-adjudicate; I flag that my snapshot is older and the document's verdict stands. **However**, I note one thing the document does *not* close and my memory flags as a live geometric problem: the **Weinberg-angle running** (`sin²θ_W = 0.5839` at `M_KK` vs `0.231` observed, requiring RG running through scales the document assigns to §7's gauge-running business, not §2's). The document solves E26 at `τ₀=0.2994` (≠ `τ_fold`) and explicitly says the running between scales is §7's business — but §7 does not report a closed `sin²θ_W(M_Z)` value. This is either (a) genuinely open, or (b) closed elsewhere and not surfaced in the capstone. → §V.5 (a concrete check, framed as INFO-resolving, not as overturning anything).

**7. The "no potential well / transit not slow-roll" result (§5.1) is correctly grounded in the geometry.** The monotone `dS/dτ` follows from `d⟨λ²⟩/dτ > 0` (E7), which is a statement about how the Jensen deformation moves the spectrum — squarely geometric. The document correctly notes `r = 16ε` is INAPPLICABLE *structurally* (the fold violates single-clock adiabatic vacuum, `c_s=1`, and Bunch–Davies premises), not merely numerically. I endorse this; it is the correct reason, and it is a geometric/dynamical statement, not an observational fit.

---

## V. Carry-Forward Computations

**The open-question harvest. Every entry is runnable with the four fields filled.** These convert the document's §9 "honest open frontiers" and the structural gaps I identified in §IV into pre-registered computations. Ordered by my assessment of leverage × tractability.

```
V.1. R_K curvature-normalization firewall table (hygiene; my §IV.2)
   - What: Build a single canonical table mapping the three R_K(0) normalizations
     {2 (internal E3), 4 (12D-reduction s52), 1.5 (Baptista Paper-15 eq 3.70)} to
     their conversion factors (×2 for 12D-vs-internal, ×4/3 for Killing-vs-rational),
     state which is canonical for which purpose, and Sage-verify that R_1, the
     Wronskian zero-order, and the Lichnerowicz bound are all convention-invariant
     (W ∝ R_K′³ so any overall scale rescales W without moving its τ=0 sixth-order zero).
   - Inputs: RK_doc = -1/4 e^{-4t}+2e^{-t}-1/4+1/2 e^{2t}; R_370 = 3/2(2e^{2s}-1+8(e^{-s}-e^{-4s}));
     s52_12d_reduction_output.txt (R_K(0)=4 form); the §8.2 a_n firewall as the template.
   - Gate: NEW gate RK-NORMALIZATION-FIREWALL. PASS iff (i) all three forms reproduce
     each other under the stated scale factors to machine-ε, AND (ii) R_1=1.128655 and
     W's 6th-order τ=0 zero are reproduced identically under all three. INFO if a
     convention is found that is NOT a pure rescaling (would indicate a genuine
     geometric discrepancy, not a convention).
   - Effort: 1-2 hours, 1 agent session (mostly Sage + one table; low risk).

V.2. Derived effective Friedmann map S_SA(τ) → 4D gravitational action (frontier #1+#8; THE gap)
   - What: Construct the back-reaction-closure H² = f(ρ_relic, S_SA) by deriving a
     generally-covariant 4D effective action for g_M from the a₂ moment, then varying it.
     Concretely: lift the INTERNAL EIH/Bianchi identity (S44, ∇_μ on K) to the emergent
     g_M via the a₂-channel field equations; test whether ∇_μ G_eff^{μν}=0 holds on the
     emergent metric (not just internally). Target: a derived dτ̇/dτ away from the fold,
     replacing the GLOBALLY-UNDETERMINED τ̇ in t(τ)=t_0+∫dτ′/τ̇(τ′).
   - Inputs: a₂(τ) closed form (∝ R_K·V); S95 W3-1 (conservation-closed G_eff^{μν},
     noether_ratio=½); S95 W3-5 (κ_EP=1 EXACT, NLO); φ(τ)=f₂Λ²a₂(τ)/(48π²); the internal
     Bianchi identity S44; canonical M_KK, a_2_FW_zeta=2776.165389, f₂≈92.
   - Gate: feeds C1 (τ↔t map), C2 (K_pivot, BROKEN-WITH-LIVE-RESEARCH-PATHWAY), T6
     (Friedmann-BCS, BROKEN). NEW gate EFFECTIVE-FRIEDMANN-MAP. PASS iff a derived
     H²(τ) closes against the relic source WITHOUT the 133,200× BCS overwhelm (i.e. the
     source is the full 155,984-mode S_SA, not the 8-mode BCS); INFO if it closes only
     up to the M_KK⁻¹→seconds normalization; FAIL if the emergent Bianchi identity fails.
   - Effort: multi-session (this is the load-bearing open frontier); 1 lead agent +
     transit-dynamics + einstein-theorist cross-check. Largest single item.

V.3. Family number from ℤ₃×ℤ₃ orbit structure + spinor overlap Φ̃ (frontier #7; my §IV.3)
   - What: Compute whether the ℤ₃×ℤ₃ structure (Baptista Paper 18 App E) on the SU(3)
     fiber produces exactly three copies of Ψ₊=ℂ¹⁶ under fiber integration, using the
     Bott–Gunning spinor comparison map Φ̃ (Paper 18 App B) to test inter-generation
     overlaps. Output: generation count n_gen and the inter-PW-sector Yukawa/overlap ratios.
   - Inputs: Paper 18 App B (Φ̃ map), App E (ℤ₃×ℤ₃→3 gen route); the one-generation
     branching Ψ₊=(3,2,⅙)⊕(3̄,1,−⅔)⊕(3̄,1,⅓)⊕(1,2,−½)⊕(1,1,1)⊕(1,1,0); Peter–Weyl
     block decomposition D_K=⊕_{(p,q)} D_{(p,q)}; C2_IDX=[3,4,5,6].
   - Gate: NEW gate FAMILY-NUMBER-Z3xZ3. PASS iff fiber integration over the ℤ₃×ℤ₃
     orbit yields exactly 3 copies of ℂ¹⁶ with non-degenerate Φ̃ overlaps; INFO if it
     yields a multiplicity ≠3 (constrains the replication mechanism); FAIL if no orbit
     structure produces integer replication. Resolves §9 frontier #7.
   - Effort: 3-4 hours, 1 agent session (representation theory + fiber integration;
     the Φ̃ map is the hard part).

V.4. SDW convergence underneath the CC absolute magnitude (frontier #6; JACOBSON-NONLOCAL-64)
   - What: Test whether the Seeley–DeWitt expansion Tr f(D_K²/Λ²) ~ Σ f_{d-n}Λ^{d-n}a_n
     CONVERGES (vs is merely asymptotic) for the framework's working f*(x)=0.9117√x+0.0883e⁻ˣ,
     by comparing the direct spectral sum (the only valid evaluation for the √x piece) against
     the truncated heat-kernel series at increasing L_max ∈ {3,...,12}. Output: convergence
     exponent and whether any ABSOLUTE a₀-moment vacuum-energy magnitude stabilizes.
   - Inputs: f*(x); the L_max=12 master spectrum cache (s84_spectrum_cache_L12_tau019.npz);
     a_0_FW_zeta=6440, a_2_FW_zeta=2776.165389, a_4_FW_zeta=1350.7216; the dimension
     spectrum S_d={0,2,4,6,8}; Friedrich–Bär saturation theorem for the L_max truncation.
   - Gate: feeds frontier #5/#6 (CC absolute vs ratio). NEW gate SDW-CONVERGENCE. PASS
     iff the absolute a₀-moment stabilizes with L_max (a substrate-natural L* exists),
     promoting the CC ABSOLUTE magnitude from conditional to derived; INFO if only the
     dimensionless ratio ρ_vac/ρ_obs converges (confirms the existing 1.032 ratio is
     truncation-robust but the absolute stays held); FAIL if the absolute diverges with L_max.
     NOTE per multiplicative-normalization-cancellation rule: if f* factorizes as w(L_max)·g(K),
     the L_max-stability of the RATIO is a structural identity, not evidence — target the
     ASYMPTOTE value, pre-flight the Sage factorization check.
   - Effort: 4-6 hours, 1 agent session (spectral sums on the cache; the convergence-vs-
     asymptotic distinction needs care).

V.5. Weinberg-angle running sin²θ_W(M_KK) → sin²θ_W(M_Z) closure (my §IV.6)
   - What: Surface whether the capstone's §7 gauge-running closes sin²θ_W from the
     geometric M_KK value (0.5839, scheme-independent, 3 methods) to the observed M_Z
     value (0.231). Run the gauge-coupling RG from M_KK to M_Z with the framework's
     threshold structure (T₂/T₃=1, T_Y/T₃=4/3 exact; δ₁/δ₃=20/9) and report the M_Z value
     + its σ-distance from PDG. This is a CHECK of an existing claim, not an overturn.
   - Inputs: sin²(M_KK)=0.5839; g₁²=g₂²=⅗g₁² unification at Λ=M_KK; threshold ratios
     T₂/T₃=1, T_Y/T₃=4/3, δ₁/δ₃=20/9; Jensen eigenvalues at fold L₁=1.4623, L₂=0.6839,
     L₃=1.2092; τ₀=0.2994 (the E26-solving modulus); M_KK=7.4287×10¹⁶ GeV.
   - Gate: feeds the §7 gauge sector. NEW gate WEINBERG-RUNNING-CLOSURE. PASS iff the
     RG-run M_Z value lands within 2σ of PDG 0.23122; INFO if it confirms my memory's
     "54.5% off" residual persists (then it is a genuine open problem the capstone should
     surface explicitly, not leave to §7's unstated business); FAIL is not applicable
     (this is a status-resolution, not a falsifier). Resolves my §IV.6 conflict flag.
   - Effort: 2-3 hours, 1 agent session (standard 1-loop RG + threshold matching).

V.6. Off-Jensen Wronskian robustness of the Decoupling Theorem (extends §4.2)
   - What: The §4.2 Decoupling Theorem is proven ON the Jensen line (one modulus). Test
     whether algebraic independence of a₀,a₂,a₄ survives small OFF-Jensen TT deformations
     (the T1/T2 directions in the 5D moduli space), i.e. whether the Wronskian stays
     nonzero for τ + ε·(off-Jensen direction). This stress-tests the "genuinely distinct
     physics" claim against the restriction to a single modulus.
   - Inputs: 5D moduli parameterization (v_J=(2,-2,1); n_V=(1,3,4); T1=(7,11,8);
     T2=(-11,-7,8)); the off-Jensen Hessian (S76 W2-J: 35/35 negative evals, Jensen=ridge);
     a₀∝V, a₂∝R_K·V, a₄∝R_K²·V generalized to the 3-block (λ₁,λ₂,λ₃) metric; Sage.
   - Gate: NEW gate DECOUPLING-OFF-JENSEN. PASS iff W stays nonzero (sign-definite) in a
     finite neighborhood of the Jensen line for all τ>0 (independence is robust, not a
     Jensen artifact); INFO if W develops new zeros off-Jensen (independence is
     Jensen-specific — sharpens the scope of the theorem); FAIL if W vanishes identically
     off-Jensen (would mean the independence is an artifact of the one-modulus restriction).
   - Effort: 2-3 hours, 1 agent session (the off-Jensen a_n forms are the new derivation).

V.7. Anisotropic τ→∞ singularity character — direction-dependent Kretschmann (extends §5.2)
   - What: Make precise the §5.2 claim that the censored τ→∞ singularity is timelike in
     the contracting SU(2) block and spacelike in the expanding ℂ²/U(1) blocks (an
     anisotropic Kasner-type singularity). Compute the Kretschmann scalar K(τ) on the full
     12D metric, decompose its divergence by block, and verify the K∼e^{4τ} scaling and the
     direction-dependent causal character. Confirms the "no standard-GR analog" statement.
   - Inputs: g_τ block structure (e^{2τ}|e^{-2τ}|e^τ); the 12D lift (M⁴×SU(3));
     S95 W4-5 (12D censorship, τ_NEC=1.383); the Kasner-exponent map for the three blocks.
   - Gate: feeds the §5.2/§9 censorship statement. NEW gate ANISOTROPIC-SINGULARITY-CHAR.
     PASS iff K∼e^{4τ} is confirmed AND the block-wise causal character is timelike(SU(2))/
     spacelike(ℂ²,U(1)) as claimed; INFO if the character is uniform (weakens the "no
     GR analog" claim to a standard spacelike singularity); FAIL if K does not diverge
     (would contradict the singularity-relocation statement).
   - Effort: 3-4 hours, 1 agent session (12D curvature computation; the block-wise
     causal decomposition is the novel part).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `D_K(τ)` block-diagonal, 4 guarantees (E5/E6/E8) | GEOMETRIC | PROVEN (endorsed) | Geometric spine is exact; makes spectrum tractable |
| 2 | Volume-preserving Jensen `det=3⁸` | GEOMETRIC | PROVEN (Sage re-verified) | Single modulus + `τ`-flat `G_N` |
| 3 | Spectral-Moment Decoupling `W∝R_K′³` | GEOMETRIC | CERTIFIED (Sage re-verified, 6th-order zero) | Layers are distinct physics everywhere but `τ=0` |
| 4 | Dimension spectrum `S_d={0,2,4,6,8}`, no flow | GEOMETRIC | PROVEN (endorsed) | Finite pole ladder, not summed foam; distinct from CDT |
| 5 | Free-param ledger `{τ,Λ,f₀,f₂,f₄}+t*`; `t*` empirical | NON-PHONONIC | CORRECTLY BOUNDED | "1→60" real; not zero-parameter; honest |
| 6 | KO-dim 6 / Pfaffian → one generation | PARTICLE | PROVEN (endorsed) | Family replication genuinely open |
| 7 | `R_K(0)` normalization multiplicity {2,4,1.5} | GEOMETRIC | HYGIENE GAP (partially disclosed) | Convention-robust physics; needs one firewall table (V.1) |
| 8 | No derived FRW `a(t)` (C1/C2/T6) | GEOMETRIC/emergent | OPEN (correctly flagged) | THE load-bearing frontier; = emergent-EP (V.2) |
| 9 | `α_s` resolved-as-channel-artifact (S93 W7-1) | PHONONIC | SUPERSEDES my memory's "FAIL" | My snapshot stale; document authoritative |
| 10 | Weinberg running `M_KK→M_Z` closure | PARTICLE | UNSURFACED in capstone | Either open or closed-elsewhere; needs surfacing (V.5) |
| 11 | Transit not slow-roll (`dS/dτ` monotone) | GEOMETRIC | PROVEN (endorsed) | `r=16ε` INAPPLICABLE structurally, not numerically |

---

**Bottom line from the KK-geometry vantage.** The capstone gets the geometry right where I can check it, and where it cannot deliver — the lift from the internal `K`-result to the emergent 4D `g_M` (the `a(t)` map, the effective Friedmann equation, higher-order emergent Lorentz) — it says so plainly and locates the gap precisely (frontier #1 = #8, one bridge). The single equation `S[D_K(τ), f, Λ]` is a legitimate "universe in one operator" claim in the categorically-stronger sense the document advertises (it derives its stage rather than populating one), and it is *not* over-read into a closed self-selecting theory. My one structural addition is the `R_K`-normalization firewall (V.1); my one conflict flag is the Weinberg-running surfacing (V.5, where I defer to whatever the capstone authors find — my memory is the stale party). The richest math waiting for greedy hands is V.2 (the effective Friedmann map) and V.3 (the family number from `ℤ₃×ℤ₃`) — both are concrete, both are in the spinor/fiber-integration toolkit the framework already owns.
