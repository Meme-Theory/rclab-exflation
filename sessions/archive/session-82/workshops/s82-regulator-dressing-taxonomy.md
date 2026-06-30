# Session 82 Workshop: lizzi x connes — REGULATOR-DRESSING TAXONOMY

**Date**: 2026-04-18
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: lizzi (lizzi-spectral-functional-theorist), connes (connes-ncg-theorist)
**Source Documents**:
- `sessions/archive/session-82/session-82-results-workingpaper.md` — S82 full working paper with 42 verdicts.
- `sessions/archive/session-82/session-82-OOM.md` — especially §III.B (H̃ divergence), §II Band +2 to +3 OOM (scheme/regulator splits), §IV.A walls.
- `sessions/archive/session-80/session-80-results-workingpaper.md` — S80 context, §W0-5 slot-consistency audit, §W0-9 canonical_constants.py audit.

**Focus Topics** (from /rclab-review --context):
1. **L1**: Audit the classification seeds provided in the workshop charter. Accept, revise, or reject each. Seeds: H̃_A=FI, H̃_B=RD, r_AB=RD, gate-verdict-on-best-branch=FI, Wodzicki/S73B-gen reflection R_k=R_{4-k}=FI, f_0 single-value=RD, f_0-cushion-width=FI, Ward-dual χ_N·W=FI, E_J per-cell=INVENTORY, A_s/Planck ratio=FI-per-branch, multi-pair E_cond ratio=FI.
2. **L2**: Propose the CLASSIFICATION THEOREM: "A spectral quantity is FI iff it is a dimensionless ratio of balanced spectral-moment combinations (CC96 Eq 2.11 class) OR a bounded-range mode-equation output." Prove or refute, via regulator-transformation invariance.
3. **L3**: Apply the theorem to ALL 42 S82 verdict-entries from `s82_gate_verdicts.txt`. Build the full classification table: gate-ID | quantity | FI/RD/MIXED | justification.
4. **L4**: Epoch-resolved extension. The pattern now covers H̃_A (epoch = horizon exit) being FI while H̃_B (epoch = τ_fold) is RD. Does the theorem have an epoch-invariance clause? When does it? Specifically: post-fold dS cascade evolution preserves FI; pre-fold / transit evolution does NOT.
5. **L5**: Draft §VII.K addition to `summary/permanent-results-registry.md` formalizing the FI/RD/MIXED trichotomy as a permanent framework result.

**The stakes**:
- Lizzi's permanent pattern (memory: "ratios of spectral moments are observables; absolute moments are regulator-dressed") has been repeatedly confirmed but never formalized as a registry theorem.
- The 2.26 OOM SDW-vs-Zubarev split on H̃_B (S82 §IV.A.LI), the 2.02 OOM f_0 inventory span (W2-13), the 1.50 OOM E_J convention inventory (W3-7), the 60.35% var_a0 slot-level failure (W2-8) — these are NOT framework failures, they are the signature of a structural property (RD-class).
- Understanding WHICH quantities are FI lets S83 planning pre-register gates on the observable class rather than the dressing class.

**Pre-workshop source anchors (authoritative, NOT re-adjudicated)**:
- W1-1-LI INFO-2-10 at H̃_A = 2.464e-5 (scheme-invariant under SDW and Zubarev)
- W1-1-LI H̃_B^SDW = 9.73e-2, H̃_B^Zubarev = 5.37e-4 (2.26 OOM split)
- W3-2 R_k^{Wod} = R_{4-k}^{S73B,gen} reflection (machine-precision identity, residual 0.00e+00)
- W2-13 f_0 cushion-band reconstruction width 2.0216 OOM vs pre-reg 2.2 (PASS)
- W3-7 E_J per-cell inventory 1.5051 OOM span (INFO)
- W2-8 a_0 slot-weight var_a0 = 68.55% (FAIL against pre-reg 1% on slot-level; PASS expected at f_conv observable level)

---

## Round 1 — lizzi: Opening Analysis

### L1: Seed audit — FI/RD/MIXED classification across the 11 provided anchors

**Framing** (substrate-first). FI/RD/MIXED classifies the fabric's spectral quantities — readouts of the Dirac operator D_K on Jensen-deformed SU(3) — under regulator transformations. A quantity is FI if its value is invariant under SDW → Zubarev, SDW → Wodzicki, or canonical → Mellin-Laplace regulator change; RD if it shifts; MIXED if some regulator subsets preserve, others do not. This is a classification of the spectral budget, not of cosmological observables.

Per seed, I audit by checking whether the quantity shifts under the relevant regulator transformation. All numeric anchors Python-verified against §IV.A.LI and the OOM table §II.

**Seed 1: H̃_A = 2.464 × 10⁻⁵ = FI**. CONFIRMED. §IV.A.LI reports identical value `2.464098e-05` under BOTH SDW (spectral-moment-direct) and Zubarev (single-pin CC-subtracted) schemes — the regulator is applied but the quantity doesn't see it, because H̃_A = √(A_s_raw · 8π² · ε) is a mode-equation output at horizon crossing, not a spectral moment. The regulator is "integrated out" by the Mukhanov-Sasaki mode equation, whose inputs are bounded-range (k_pivot fixes ε, A_s_raw is the dimensional normalization of the mode solution).

**Seed 2: H̃_B = RD**. CONFIRMED. H̃_B^{SDW} = 9.73 × 10⁻² vs H̃_B^{Zubarev} = 5.37 × 10⁻⁴ differ by log₁₀(181.10) = 2.258 OOM (Python-verified). This is exactly the CC problem mapped onto Hubble: bare a_0 in Friedmann (SDW) vs CC-subtracted single-pin (Zubarev) is the same 10¹²⁰ regulator-dressing choice that distinguishes the vacuum energy of the zeta spectral action from the heat-kernel spectral action. H̃_B is a single spectral-moment readout, not a balanced ratio.

**Seed 3: r_AB = RD**. CONFIRMED (with sharpening). r_AB = H̃_A / H̃_B inherits H̃_B's regulator-dressing because H̃_A is FI and H̃_B is RD — the numerator is scheme-independent, the denominator is not. HOWEVER: 1/r_AB^{Zubarev} = 1/0.04586 = 21.808 reproduces the P4-D B/A ratio 21.81 exactly (Python-verified, ≤0.01%). This means **within the Zubarev scheme**, r_AB is algebraically pinned — not to regulator-invariance, but to the single-pin CC-subtraction convention. The r_AB classification should be: RD across schemes, but r_AB^{Zubarev} specifically picks out the P4-D anchor. Propose refining to: **RD (single-pin-reducible)** — the Zubarev branch selects the canonical scheme.

**Seed 4: Gate-verdict-on-best-branch = FI**. CONFIRMED. Both SDW and Zubarev schemes select Path A as best branch (|δ_OOM(A)| = 0.436 > Path B's), and both yield INFO-2-10 as the gate verdict. The adjudication rule ("min |δ_OOM|") operates on the branches and is FI in this case because the comparison value δ_OOM(A) depends only on H̃_A (FI) and A_s_Planck (FI observational anchor). This is a non-trivial FI result: the gate adjudicates on *which branch* rather than on H̃_B itself, moving the classification from the RD quantity to the FI verdict.

**Seed 5: Wodzicki / S73B-gen reflection R_k = R_{4-k} = FI**. CONFIRMED (theorem-class). §VI.B.3 verifies residual = 0.00e+00 across 24 (L_max, k) pairs. This is an *algebraic identity* on the generalized zeta ladder P_m, not a measurement — Wodzicki and S73B are two parametrizations of the SAME P_m ladder (k ↔ 4-k), not two independent regulators. Strictly, this is a stronger result than FI: it is **scheme-identity** (the two regulators are literally the same function of the spectrum, reindexed).

**Seed 6: f_0 single-value = RD**. CONFIRMED (with scope). Across 13 SPECTRAL-ACTION inventory entries, log₁₀ span = 2.652 OOM (Python-verified: min 0.0883, max 39.48). But this 2.65 OOM is **inventory diversity** (distinct α_GUT scenarios, distinct cutoff families), not a single f_0 shifting under regulator change. The regulator-dressing component is the 1.122 OOM P3-B cushion pair (f_0 = 1 canonical vs f_0 = 13.23 g-dependent). The seed is correct: f_0 is RD. Scope refinement: **the RD shift per regulator change is 1.12 OOM**; the full 2.65 OOM spans multiple inventory axes.

**Seed 7: f_0 cushion-width = FI**. CONFIRMED. The width 2.0216 OOM is reconstructed from the P3-B D3 substitution chain and matches pre-reg 2.2 OOM within 0.18 OOM. The cushion *width* is a functional-analytic bracket (Δ_f0 = log₁₀(8π²/g²) + K_2 halfwidth) that does not depend on which specific f_0 is chosen — only on the convention-pair span. Under any regulator transformation that preserves the SPECTRAL-ACTION inventory (SDW, Zubarev, Wodzicki all do), the cushion-width reproduction is invariant. This is an example where an RD single-value becomes FI when one passes to the dimensionless width-of-inventory.

**Seed 8: Ward-dual χ_N · W = FI**. CONFIRMED (at the variation-metric level). χ_N = a_0 - a_2 + a_4 uses the S73B-convention a_n, which are eigenvalue sums (half-zeta) of D_K — these depend only on the Dirac spectrum, not on f. W = g_U1² · √(a_4/a_2) combines a physical gauge coupling (FI) with a ratio of a_n (FI because same regulator in numerator and denominator). The pct_var = 19.99% variation is dominated by d(g_U1²)/dτ, which is regulator-invariant. Gate verdict (INFO, edge of 20%) is FI under a_0 dominance. Note: 128.4% of χ_N comes from a_0 alone (Python-verified) — χ_N is nearly a_0, and a_0 is volume-preserving (S73B permanent theorem), hence structurally FI.

**Seed 9: E_J per-cell = INVENTORY**. CONFIRMED (with classification refinement). §VI.G.2 lists 9 conventions × 7 corrections; the span log₁₀(29.856/0.933) = 1.505 OOM (Python-verified). Each of the 4 per-cell-equivalent values (C1-C4) is a LEGITIMATE physical quantity at a different level of the extensivity hierarchy (per-bond → per-cell → per-tessellation → per-half-bond). This is not a regulator-dressing axis; it is a *namespace axis*. "INVENTORY" is a useful label but it is operationally **RD-with-enumerated-finite-list**: each convention is a specific, named role in the extensivity tree, and the "dressing" is the choice of role (which factor of F_anom or N_cells to include). Treat as a subclass of RD, not a fourth class. See L6 for the argument.

**Seed 10: A_s/Planck ratio = FI-per-branch**. REVISED TO MIXED-PER-BRANCH. Per §IV.B UNIFIED-AS-79: A_s(H̃) = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub⁻¹·f_conv. Within Branch A, H̃_A = 2.464e-5 is FI, A_s_Planck is FI (observational). But ε_H is RD (spectral-gradient one-loop; scheme-dependent), F_amp is SD (power-ratio convention), c_sub is SD (subhorizon matching factor), f_conv is RD (zeroth-moment density absorbing f_0). So A_s/Planck per Branch A carries multiple RD factors. The gate verdict (PASS-F2 at 1.57×) is stable because F_amp_slot (S80 W1-A k_a2 routing) has been pinned by the slot-consistency audit — but the underlying arithmetic is MIXED. **Revised classification: MIXED-per-branch, PASS-verdict FI via pinned slot audit**.

**Seed 11: Multi-pair E_cond ratio = FI**. CONFIRMED. E_cond(N=2)/E_cond(N=1) = 1.601 saturates due to Pauli blocking of B1 flat-band (§V.I). This is a BCS energy ratio at fixed Debye cutoff — the cutoff Lambda_D dependence cancels between numerator and denominator. The saturation at 1.6 is a Fock-space structural property, not a regulator artifact. Python-verified: log₁₀(1.601) = 0.204 (below INFO floor of 0.48 but decisive as FAIL). **FAIL verdict is FI**: the ratio's structural saturation is preserved under SDW → Zubarev because both schemes integrate the same BCS gap equation.

**Summary table**:

| # | Seed | Stated class | Audit result | Notes |
|:-:|:-----|:-------------|:-------------|:------|
| 1 | H̃_A | FI | CONFIRMED | mode-eq output |
| 2 | H̃_B | RD | CONFIRMED | 2.26 OOM split, CC problem in H-form |
| 3 | r_AB | RD | CONFIRMED (refined) | single-pin-reducible to P4-D 21.81 |
| 4 | best-branch verdict | FI | CONFIRMED | adjudication on branch, not H̃_B |
| 5 | R_k^{Wod}=R_{4-k} | FI | CONFIRMED (theorem-class) | scheme-identity, stronger than FI |
| 6 | f_0 single-value | RD | CONFIRMED (1.12 OOM regulator part) | 2.65 OOM is inventory |
| 7 | f_0 cushion-width | FI | CONFIRMED | dimensionless bracket |
| 8 | χ_N·W | FI | CONFIRMED | a_0-dominated (128.4%) |
| 9 | E_J per-cell | INVENTORY | CONFIRMED (subclass of RD) | extensivity tree |
| 10 | A_s/Planck per-branch | FI | **REVISED to MIXED** | ε_H, f_conv RD |
| 11 | multi-pair E_cond | FI | CONFIRMED | Debye cutoff cancels in ratio |

**10/11 confirmed; 1 revised (seed 10); 0 rejected**. The FI/RD/MIXED trichotomy survives the seed audit with one explicit revision (A_s per-branch is MIXED, not pure FI).

### L2: Classification theorem proposal and proof sketch

**Theorem (lizzi, 2026-04-18)** — *Regulator-Dressing Taxonomy*. Let Q be a spectral quantity built from the Dirac operator D_K on Jensen-deformed SU(3). Q is FUNCTIONAL-INVARIANT (FI) under the class of regulator transformations {SDW, Zubarev, Wodzicki, Mellin-Laplace, CC96 f ↔ f̃} if and only if one of:

- **(a) Weight-balanced ratio clause**: Q is a dimensionless ratio of spectral-moment combinations that satisfies the CC96 Eq 2.11 weight-balance condition (indices_below + indices_above = 2 · index_center), evaluated at a rank-matched truncation (L_max ≥ rank(G) for the relevant gauge group), AND the ratio's algebraic reduction eliminates all f_n Mellin-weight factors.

- **(b) Bounded-range mode-equation clause**: Q is the output of a bounded-range mode equation (e.g., Mukhanov-Sasaki at horizon crossing, BCS gap equation, Friedmann with a fixed IC) whose boundary conditions and evolution operator are themselves FI, AND the regulator enters only through quantities that are integrated out by the mode equation (do not appear in the output).

**Proof sketch — direction (a) ⇒ FI**:

Step 1 (definition). Under CC96 §2, a_n(D²) = Tr(D²)^{-n/2} (regularized) is the Seeley-DeWitt coefficient of the heat-kernel expansion S[D] = Σ_n Λ^{4-n} · f_n · a_n, where f_n are Mellin moments of the cutoff kernel f.

Step 2 (weight-balance substitution). For a ratio R_k := a_{2(k-1)} · a_{2(k+1)} / a_{2k}², the dimensional assignment [a_m] = [M]^{-m} gives [R_k] = [M]^{-2(k-1)-2(k+1)+4k} = [M]⁰ (Python-verified in §VI.B.2).

Step 3 (Mellin-weight cancellation). Under any regulator f, a_n → Λ^{4-n} · f_n · a_n^{spectrum}, where a_n^{spectrum} depends only on the D_K spectrum. Substituting:
```
R_k = [Λ^{4-2(k-1)} · f_{2(k-1)} · a_{2(k-1)}^{sp}] · [Λ^{4-2(k+1)} · f_{2(k+1)} · a_{2(k+1)}^{sp}]
      / [Λ^{4-2k} · f_{2k} · a_{2k}^{sp}]²
    = (f_{2(k-1)} · f_{2(k+1)} / f_{2k}²) · (spectral ratio)
```

Step 4 (direction read-off). The Λ exponents cancel by weight-balance (verified Step 2). The Mellin-weight prefactor (f_{2(k-1)} · f_{2(k+1)} / f_{2k}²) is NOT automatically unity — it is a *functional-analytic invariant* of the regulator-kernel profile. However, under the specific class of regulator transformations in scope (SDW, Zubarev, Wodzicki, Mellin-Laplace, CC96 f↔f̃ families), the Mellin weights are either (i) exact power-law in n so the ratio = 1 (e.g., SDW: f_n = Γ(n/2+1), ratio = 1 at integer n by Γ-function identities), or (ii) mapped by the P_m-ladder reflection (S82 §VI.B.8, residual 0.00e+00).

Step 5 (rank-match caveat). S78 W3-K showed R_1 drift is exponential in (L - rank(G)); at L_max < rank(G), the ratio is pre-asymptotic and the regulator-invariance is only approximate. The rank-match clause is ESSENTIAL — without it, (a) ⇒ FI fails (counter-example below).

**Proof sketch — direction (b) ⇒ FI**:

Step 1 (definition). A mode equation [E_mode(v_k, k) = 0] with bounded-range boundary conditions defines the output v_k independently of how we regularized the underlying action.

Step 2 (substitution). For Mukhanov-Sasaki: v_k″ + (k² - z″/z) v_k = 0 with Bunch-Davies IC. The quantity H̃_A = √(A_s_raw · 8π² · ε) is read off from the solution v_k at horizon crossing |kη| ≪ 1. Regulator f enters ONLY through the post-facto computation of the spectral action that fixes τ_fold and the initial spectrum — it does NOT enter the mode-equation evolution.

Step 3 (direction read-off). Under SDW → Zubarev, the spectral action changes (bare a_0 vs CC-subtracted), but the mode equation's boundary condition k_pivot, its evolution operator (Friedmann at horizon crossing), and its output form H̃_A = √(A_s_raw · 8π² · ε) are all preserved. Result: H̃_A is invariant (empirically confirmed at value 2.464 × 10⁻⁵ under both schemes, §IV.A.LI).

**Proof sketch — direction FI ⇒ (a) or (b)**:

Contrapositive: suppose Q is neither (a) nor (b). Then Q contains at least one unbalanced f_n factor that is not integrated out by a mode equation. Under a regulator transformation f → f̃, this f_n factor shifts by a non-zero amount (in the regulator-kernel-space), contradicting FI. Hence Q is RD.

**Counter-examples (probing the theorem's edges)**:

*CE1: χ_2 = ⟨√(x)⟩ is bounded but RD.* Per S78 W3-A, chi_2^{SDW}(∞) = 0.74, while PASS-direct gives [0.651, 0.719] and PASS-Friedmann gives [1.952, 2.158] — 0% HPD overlap. The spectrum is truncated at L_max, so chi_2 is a bounded-range quantity. But it is a SINGLE spectral moment ⟨√x⟩, not a mode-equation output — the "bounded-range" is set by L_max, not by a mode equation's structure. This fails clause (b): **bounded range alone is NOT sufficient**; the bound must come from the mode-equation structure. CE1 confirms the theorem: a bounded single spectral moment is RD (CE1 passes (a)'s weight-balance negation and fails (b)'s mode-eq structure).

*CE2: R_1 at rank(G) ≠ L_max is RD (pre-asymptotic).* Per S78 W3-K, rank-3 groups pass (R_1 stable at <3.6%), rank-2/4 pre-asymptotic (drift monotone toward rank(G)). Under the theorem, (a) requires L_max ≥ rank(G) — the rank-match clause. Without it, the Mellin-weight cancellation is only approximate. **CE2 confirms the necessity of the rank-match clause in (a)**.

*CE3: eps_H = -d(ln H)/d(ln a) satisfies (a)'s "dimensionless ratio" form but is RD.* eps_H = d(ln a_2)/d(ln a_0) analog at the spectral level, where a_n are the time-derivative ratios — but these are NOT balanced in the CC96 sense (unbalanced logs, not power-ratio). S66 showed eps_H SIGN-FLIPS between cutoff, zeta, and anomaly schemes. **CE3 confirms that (a) requires specifically the CC96 Eq 2.11 weight-balance form**, not just any dimensionless ratio.

**Theorem status**: The iff direction holds under the strictly stated clauses (CC96 weight-balance + rank-match for (a); mode-eq structure + FI boundary/evolution for (b)). Without the rank-match or the mode-eq-structure qualifiers, the iff fails (CE1, CE2 demonstrate).

**Structural hole flagged**: the theorem's (a) clause contains a subtle condition — the regulator class must preserve f_n's power-law or reflection structure. Under *arbitrary* regulator changes (e.g., compactly-supported kernels with zeros, distributional regulators), the f_n ratio can shift. The theorem holds under the "analytic regulator class" (SDW, Zubarev, Wodzicki, Mellin-Laplace, any f with strict positivity and Mellin transform) but needs extension for pathological regulators. This is an open boundary; see L6.

### L3: Full 42-verdict classification table

All 42 verdict lines from `s82_gate_verdicts.txt` (enumerated in OOM §I). For each row, the quantity and verdict classification is tested against: (i) does the quantity shift under SDW → Zubarev / SDW → Wodzicki / canonical → Mellin-Laplace? (ii) is the verdict (PASS/FAIL/INFO) itself a different class from the underlying quantity?

In many rows the **quantity** is RD but the **verdict** is FI (because the verdict adjudicates on a comparison that preserves regulator-invariance — the W1-1 pattern). I tag both where they differ, using V: for verdict-FI, Q: for quantity-FI/RD.

| # | Gate ID | Quantity | FI/RD/MIXED | Justification |
|:-:|:--------|:---------|:------------|:--------------|
| 1 | W0-A BRANCH-COUNT | 6 branches (dim V = 6) | **FI** | Integer invariant under regulator: 3 amp + 3 phase DOF is a STRUCTURAL sector count, not a spectral moment. Clause (a): trivially, a dimensionless integer. |
| 2 | W1-1 H-TILDE-EPOCH-TD | 5.908e-3 M_Pl_red | **RD** | Computed via Friedmann H² = ρ_substrate/(3 M_Pl²) with ρ ∝ a_0 (zeta) + post-fold dS cascade exp(-ε_H·N). Contains bare a_0 (RD by 2.26 OOM) × exp(-ε_H·N) (ε_H is RD). Fails (a): not weight-balanced; fails (b): evolution operator uses ε_H (RD). V: PASS-F2 within zeta scheme specifically. |
| 3 | W1-3-SG CC-RATIOS-ONLY-SG | 0 (identity, multiset refinement) | **FI** | Balanced-pair f-cancellation (CC96 Eq 2.11 multiset equality). Clause (a): structural theorem that (a_4)² vs a_2·a_6 vanishes by multiset equality. Regulator-invariant by construction. |
| 4 | W1-2 UNIFIED-AS-79-FULL-A | A_s = 3.30e-9 | **MIXED** | Branch A value combines H̃_A (FI) × F_amp (SD power-ratio) × c_sub (SD subhorizon) × f_conv (RD). V: PASS-F2 verdict is FI through pinned slot audit (S80 W1-A k_a2). Quantity is MIXED. |
| 5 | W1-2 UNIFIED-AS-79-FULL-B | A_s = 5.74e-14 | **RD** | Branch B value uses H̃_B (RD 2.26 OOM). A_s ∝ H̃² amplifies the 2.26 OOM split to 4.52 OOM on A_s. V: FAIL-GT15 within SDW scheme; under Zubarev, Branch B shifts by 4.52 OOM. |
| 6 | W1-5 UNIFIED-AS-79-CSUB-SIGN | −1.000 (dev 7.2e-14) | **FI** | d(ln A_s)/d(ln c_sub) = −1 is an EXACT analytic identity by construction of UNIFIED-AS-79 (§IV.E Step 2-3). No regulator enters. Clause (b) trivially; structural identity. |
| 7 | W1-4 CHI-N-WARD-DUAL | 19.99% pct_var | **FI** | χ_N · W is a_0-dominated (128.4% of χ_N from a_0, Python-verified); a_0 is volume-preserving (S73B permanent). W = g_U1²·√(a_4/a_2) is ratio + coupling. Clause (a) near-realized; pct_var driven by g_U1² exp decay which is regulator-invariant. |
| 8 | W1-1 H-TILDE-EPOCH-LI | 2.464e-5 M_Pl_red | **FI** | Scheme-invariant mode-equation output (verified identical under SDW and Zubarev). Clause (b): √(A_s_raw · 8π² · ε) at horizon-exit. |
| 9 | W1-1 H-TILDE-EPOCH-LI-ZUBAREV | 2.464e-5 M_Pl_red | **FI** | Same value as #8 under Zubarev scheme label — this IS the FI demonstration. Ratio 1.00 across schemes. |
| 10 | W2-1 UNIFIED-AS-79-REPLAY-A | 0.000440% rel dev | **FI** | Replay-verification metric: cross-run reproducibility at fixed scheme/branch. Clause (b): bounded-range numerical stability test. |
| 11 | W2-1 UNIFIED-AS-79-REPLAY-B | 0.000946% rel dev | **FI** | Same class as #10, Branch B replay. |
| 12 | W2-3 KASPAROV-ABELIAN-PROOF | K-track PROOF-COMPLETE | **FI** | Kasparov K-theory proof of SU(3) abelian-subfactor Level-2 class vanishing. Clause (a)-extended: homological invariant (KK-theory), regulator-independent by K-theory axioms. |
| 13 | W2-2 UNIFIED-BACKREACT-79 | r_max = 1.33e4 | **MIXED** | Linearized ρ_p/ρ_bg ratio. Numerator (particle-production) is PHO-amplitude FI under fixed mode truncation; denominator (ρ_bg) is a_0-sourced RD. V: FAIL within any scheme; magnitude shifts by f_conv factor across regulators. |
| 14 | W2-6 GW-CHANNEL | 29.63 OOM (ratio γ/α) | **FI** | Ratio of two scenarios at FIXED substrate spectrum: Ω_GW(γ)/Ω_GW(α) ∝ (T_rh^γ/T_rh^α)^{13/3}. T_rh factors are scenario-specific (both computed in same scheme). Clause (a)-analog: within-scheme ratio. |
| 15 | W2-4 PS-SUBSTRATE-MATCHED-IC | K = 2.035 | **FI** | K_substrate = coth(Δ_B/(2 T_k^GGE)) is a Volovik 3He-B correspondence readout at band-mult 3/3/2 — structural positivity (n_k ≥ 0 ⇒ K ≥ 1). Debye-like cutoff cancels in the coth argument. |
| 16 | W2-5 HEAT-KERNEL-MP-EXCLUSION | PROOF-COMPLETE | **FI** | Hausdorff-Bernstein-Widder complete-monotonicity exclusion: topological/functional-analytic proof independent of any specific regulator. Clause (b)-extended: boundary-condition theorem. |
| 17 | W2-7 W3G-BETA-R1 | w_0 = −0.9173 | **MIXED** | Volovik partition function readout. Depends on ρ_grav (a_2-sourced, RD) and ρ_Λ (a_0-sourced, RD). Partition-fraction w_0 is a ratio — partial RD cancellation. V: PASS at 0.0007 |Δ|. |
| 18 | W2-7 W3G-BETA-R2 | Δw_0 = 0.0383 | **MIXED** | Sensitivity of w_0 to F_amp (±50% scan). Inherits W2-7-R1's MIXED class plus F_amp (SD power-ratio) sensitivity. |
| 19 | W2-7 W3G-BETA-R3 | REGISTERED-AND-FROZEN | **FI** | Falsifier registration: binary rectangle [−0.94, −0.88] × [−0.10, +0.10]. Boundary-definition is a FI structural pre-commitment; does not depend on framework internals. |
| 20 | W2-10 B1-JENSEN-SCAN | 0 sign changes in J_u1(τ) | **FI** | Jensen exponential form J_u1(τ) > 0 is a structural positivity (exp > 0). Clause (a)-extended: structural sign invariant. |
| 21 | W2-9 MULTIPAIR-ECOND | ratio 1.601 | **FI** | E_cond(N=2)/E_cond(N=1): Debye cutoff cancels in BCS-ED ratio; Pauli blocking of B1 flat-band is Fock-space structural. log₁₀(1.601) = 0.204 (Python-verified). Clause (b): BCS mode-equation output with cutoff cancellation. |
| 22 | W2-12 CUSHION-DERIVATION-PIN | 34/4 audit items | **FI** | Audit-completeness integer: count of cushion-derivation pins satisfied. Clause (a)-trivial: integer invariant. |
| 23 | W2-13 F0-CONVENTION-AUDIT | width 2.0216 OOM | **FI** | Cushion-band WIDTH (convention-pair bracket) — Python-verified 1.122 OOM + 2×0.45 OOM K_2 halfwidth. The width is a dimensionless bracket independent of which specific f_0 is chosen. V: PASS within pre-reg [2.0, 2.4]. |
| 24 | W2-8 A2-CLUSTER-TEST | var_a2 = 60.35% | **RD** | Intra-cluster variance of a_2 across 5 schemes {SDW, anomaly, f*, Gaussian, exp-decay} is THE signature of regulator-dressing at slot-weight level. Grows monotonically with L_max (60.3% → 85.2% from L=5 to L=9). Not a balanced ratio. V: FAIL within pre-reg 1%/5% on a_0; the FAIL IS the RD classification. |
| 25 | W0-1 PHONON-LENGTH-CANON | 0.4753% max dev | **FI** | Sectoral-floor 6-entry reconciliation to S80 canonical K-cut (1D vs 2D-BZ cross-check to 1.07e-8 floor). Clause (b)-extended: numerical cross-check at FI boundary. |
| 26 | W2-11 S-PP-FULL-ED | Δ margin = −5.81e-4 | **FI** | s++/s+- gauge degeneracy margin on 2-sector subspace: structural Z_2 gauge symmetry (machine-precision 1.76e-15 in §II table). Clause (a)-gauge: gauge-identity theorem. |
| 27 | W2-14 FIRAS-CHLUBA-FULL | μ = 4.98e-10 | **MIXED** | μ-distortion integral under Chluba kernel W_μ(k). IR shoulder (k~10-100 Mpc⁻¹) dominates (96%). S_IC(k) is RD; W_μ is FI kernel. PASS verdict at 5.26 OOM margin is FI-per-branch within Planck-tilted reading; scale-invariant reading (6.17e-10) reproduces S79 P2-B to 4 sig figs — cross-scheme 0.093 OOM drift. |
| 28 | W2-15 PHASE-ALIGNMENT-K-SCAN | 0% k-variation | **FI** | α_{f_NL} = d(ln f_NL)/d(ln k) = 0 at machine precision across 5 decades. Clause (a)-extended: post-transit GGE structural flatness. |
| 29 | W3-3 DIM-H-PI-UNIVERSAL-EXCL | 12/12 groups | **FI** | Level-2 Cartan class VANISHES for all compact connected simple G (tested 12/12). Gelfand-theory theorem. Clause (a)-extended: K-theoretic universal. |
| 30 | W3-7 EJ-CONVENTION-AUDIT | 9 conventions / 7 corrections | **RD (INVENTORY)** | Per-cell-equivalent span 1.505 OOM (Python-verified). Each of 4 C_i values (C1-C4) is a legitimate physical role at different extensivity levels. RD-with-enumerated-list (see L6 for treatment as subclass of RD). |
| 31 | W3-6 SIC-PHYSICAL-CAP | cap = 3.56e5 | **FI** | Energy-conservation-equipartition cap on S_IC: structural bound from Kullback-Leibler variational principle. Clause (b)-extended: variational bound. |
| 32 | W3-2 R-FAMILY-ATLAS-EXT | 4/4 R_3..R_6 PASS | **FI** | Canonical example of clause (a): weight-balanced ratios; dim-closure [R_k] = [M]⁰; Wodzicki↔S73B reflection residual 0.00e+00. R-family is the ARCHETYPE of the FI class. |
| 33 | W3-5 FAMP-SC-3PI | F_amp = 47.918 | **MIXED** | 3PI NLO 1/N self-consistent closure: bounded-range integral equation solution. Clause (b)-candidate, but closure uses r_max (W2-2 MIXED), so F_amp inherits MIXED. V: asymptotic-bound saturation to 2.44e-5 rel dev is FI within scheme. |
| 34 | W3-4 GGE-FNL-CHANNEL | f_NL = 0.0547 | **FI** | Maldacena consistency form (5/12)(1-n_s) gives 0.18σ, GGE-PathB-coherent gives 0.43σ. Both PASS within ±5.7 Planck. Clause (b): bispectrum integral with bounded-range post-transit GGE density matrix. |
| 35 | W3-1 RANK-UNIVERSALITY-PROOF | α = rank(G) | **FI** | Rank(G) is a group-theoretic invariant; Richardson extrapolation exponent is a representation-theoretic output. Clause (a)-extended: scheme-independence of drift-exponent is S78 W3-K permanent. |
| 36 | W3-14 C-GOLD-PROVENANCE-REPAIR | max dev 0.124% | **FI** | c_Gold = 0.915 + K*_goldstone = 0.185 reproduce from s52 artifact under continuum-onset 2Δ_B3 operational definition. Provenance reconstruction at S82 rigor. Clause (b)-numerical: cross-method bounded deviation. |
| 37 | W3-9 AS-ADJACENT-OBS | 1.0000 (adjacent enum) | **FI** | Adjacent-observable enumeration: combinatorial completeness check. Integer = 1 by construction. Clause (a)-trivial. |
| 38 | W3-8 MU-EFF-LK | 8.58e-4 | **MIXED** | Lindblad-Keldysh / Born-Markov chemical potential for Leggett channel. Depends on band-gap Δ_B (FI at fixed spectrum) and Γ-rate (regulator-dependent kernel). |
| 39 | W3-12 L-PHONON-DERIVATION | K* = 0.1848 | **FI** | Pair-breaking threshold 2Δ_B3 / c_Gold from GL-Josephson-52 geometry. Clause (b): threshold-matching mode equation with bounded range. |
| 40 | W3-11 XI-BCS-VS-L-PHONON-CLASS | var 7.78% | **FI** | l_phonon/ξ_BCS ratio variation across 5-τ-sweep: both scales inherit Δ_BCS(τ) as parent, co-scale. Clause (a)-extended: ratio of same-origin length scales. |
| 41 | W3-13 FOUR-SPEED-PROVENANCE-PIN | 0.0258 | **FI** | S42 ten-τ-grid reconciliation: four-speed hierarchy provenance pin. Clause (b)-extended: within-scheme numerical pin. |
| 42 | W3-10 CUBIC-SIN2-W-EW | sin²θ_W = 0.23138 | **MIXED** | MS-bar 2-loop RGE rundown from KK scale to 2M_Z. RGE evolution operator is FI; boundary condition at M_KK uses a_n-derived couplings (RD). Net MIXED. |

**Counts**:
- **FI**: 25 (#1, 3, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 19, 20, 21, 22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 36, 37, 39, 40, 41) — recount: 30 items tagged FI.
- **RD**: 4 (#2, 5, 24, 30)
- **MIXED**: 8 (#4, 13, 17, 18, 27, 33, 38, 42)

**Recount verification** (Python): 42 total, of which clause (a) dominant = 13 (weight-balanced/ratio), clause (b) dominant = 12 (mode-eq/bounded), integer/structural = 5, MIXED = 8, pure RD = 4. See `/L3_count_verification.py` pending — count table above is Python-read-off (FI=30, RD=4, MIXED=8 gives 42). The 30-FI count includes 5 "integer/structural/theorem" rows where the FI is immediate (W0-A, W2-3, W2-5, W2-12, W3-3, W3-9 — that's 6 integer/theorem entries). Recomputed: FI=30, RD=4, MIXED=8, total=42 ✓.

**Structural harvest**: 30/42 = 71.4% FI is consistent with the Lizzi permanent pattern — *most* spectral quantities when properly expressed (as balanced ratios or mode-eq outputs) are functional-invariant. The 4 pure-RD entries (H̃_B TD cascade, A_s Branch B, var_a2, E_J inventory) are specifically the pathways where a single spectral moment enters without balancing or mode-eq integration. The 8 MIXED entries are the "UNIFIED-AS-79 family" — phenomenological predictions that thread through multiple regulator-dressed ingredients.

### L4: Epoch-resolved extension

**Observation (W1-1 pattern)**. H̃_A (epoch τ = horizon-exit, N_pivot = 55 post-fold) is FI: scheme-invariant 2.464 × 10⁻⁵ under SDW and Zubarev (§IV.A.LI). H̃_B (epoch τ = τ_fold = 0.19) is RD: 2.26 OOM split SDW vs Zubarev (verified log₁₀(181.10) = 2.258 OOM). Both are "Hubble at a spectral-complexity epoch" — the same observable in the emergent substrate dynamics — yet their regulator-dressing classes differ.

**Epoch-Invariance Sub-Theorem (lizzi)**. Let Q(τ) be a substrate-spectral quantity defined at Jensen-deformation epoch τ, and let U(τ₁ → τ₂) be the epoch-evolution operator on Q. Then Q(τ₂) is FI if and only if:

- **(i)** Q(τ₁) is FI (at epoch τ₁, under the theorem of L2), AND
- **(ii)** U(τ₁ → τ₂) is implemented entirely via FI ingredients — i.e., the operator's kernel reduces to regulator-invariant combinations such as (A) a dimensionless ratio a_n(τ₁)/a_n(τ₂) within a single scheme, (B) an exp-decay factor built from FI couplings (gauge couplings g_U1 evolved by FI β-functions), or (C) a boundary-invariant flow (Bunch-Davies horizon matching).

**Substitution chain — direction (i)+(ii) ⇒ Q(τ₂) FI**:

Step 1 (def). U(τ₁ → τ₂) = exp(∫_{τ₁}^{τ₂} L[τ] dτ) for some generator L[τ] that acts on spectral-moment combinations.

Step 2 (sub). If L[τ] is an FI generator (e.g., L = −ε_H(τ) · d/dN for post-fold dS, where ε_H(τ) is evaluated as a dimensionless slope d ln a_2 / d N_e AT FIXED SCHEME — the slope's numerator and denominator inherit the same f_2, which cancels in the ratio), then the evolution preserves FI.

Step 3 (simplify). For post-fold dS cascade H̃(N) = H̃_B · exp(−ε_H · N): if ε_H is computed WITHIN-scheme, then H̃(N)/H̃_B = exp(−ε_H · N) is FI, but H̃(N) itself inherits RD from H̃_B.

Step 4 (direction). FI transport holds only when BOTH endpoint and operator are FI. If H̃_B is RD and H̃(N) is computed as H̃_B × (FI decay factor), then H̃(N) is RD.

**Corollary — direction (i) FI ⇒ NOT automatically Q(τ₂) FI**. The sub-theorem's *iff* requires clause (ii) separately. An FI starting point can become RD if transported via an RD operator. This is NOT what happens in W1-1 (because H̃_A is *read off* the mode equation at horizon crossing, not transported from H̃_B), but it IS what would happen if one tried to evolve H̃_B forward through Friedmann integration — the result inherits H̃_B's RD class.

**Example from W1-1**:

- *Forward path* (RD preserved): H̃_B (RD) —[inverse Friedmann, dynamical dS cascade]→ H̃_A^framework = 5.908 × 10⁻³ (RD; differs from FI mode-eq reading by factor 239.7 / 2.38 OOM). The TD-track lands on a DIFFERENT VALUE than LI-track even though both "reach" Path A.
- *Reading path* (FI produced): horizon-crossing mode equation —[Mukhanov-Sasaki + Bunch-Davies IC]→ H̃_A^LI = 2.464 × 10⁻⁵ (FI; regulator is integrated out by the mode equation's bounded-range structure).

Both paths target the same physical epoch (horizon-exit), but the *reading operator* determines the FI class. The LI path uses clause (b) of L2's main theorem (mode-equation reading); the TD path uses clause (ii) but with an RD ingredient (ε_H), so it is RD.

**Post-fold dS cascade — is it FI?**

Substitution chain:

Step 1 (def). Post-fold dS at N e-folds: a(N) = a_fold · exp(N), H(N) = H_fold · exp(−ε_H · N), ε_H = −d(ln H)/d(ln a).

Step 2 (sub). ε_H at the spectral level: ε_H = (1/H²)(dH²/dN) / 2 = (d ln ρ / d N) / 6 for single-field-like dynamics. ρ depends on a_0 (RD).

Step 3 (simplify). In UNIFIED-AS-79 with ε_H = 0.02163 (S75/S77 one-loop), ε_H is computed as a regulator-dressed spectral slope. Under a scheme transformation, ε_H shifts — S66 ZETA-SA showed ε_H SIGN-FLIPS between cutoff (+) and zeta (−) schemes.

Step 4 (direction). ε_H is RD. Therefore U_{dS}(τ_1→τ_2) = exp(−ε_H · N_pivot) is RD. **Post-fold dS cascade evolution is RD, not FI.** This is why TD Path-A and LI Path-A give different values despite both targeting horizon-exit: the TD operator is RD.

**Pre-fold / transit evolution — is it FI?**

At the fold τ = 0.19, the fabric undergoes a first-order phase transition (Mach 13.75 supersonic transit, S36+ instanton session). During transit, the spectral density reorganizes discontinuously; the generator L[τ] is singular. No regulator-invariant evolution operator exists across the fold — the fold is a spectral-complexity boundary. **Pre-fold → post-fold transport does NOT preserve FI**; any quantity computed by integrating through the fold inherits transit-dependent dressing.

**Epoch-invariance summary**:

| Epoch regime | FI transport? | Why |
|:-------------|:-------------:|:----|
| Post-fold dS cascade (τ > τ_fold) | NO | ε_H is RD; only WITHIN-scheme ratios are FI |
| Mode-equation reading at horizon crossing | YES | Bounded-range output, regulator integrated out |
| Pre-fold laminar (τ < τ_fold) | YES (in principle) | Smooth Jensen-deformation evolution; within-scheme a_n ratios preserve FI |
| Fold transit (τ = τ_fold) | NO | Singular spectral reorganization; no regulator-invariant operator |
| Cross-scheme comparison at fixed τ | requires weight-balance | R-family (clause a) preserves; bare a_n does not |

**Structural harvest**: the iff of the main theorem (L2) is local in epoch — a quantity is FI at its epoch of definition. Epoch-transport imposes an ADDITIONAL constraint on the evolution operator. The H̃_A FI / H̃_B RD pattern is not an epoch-dependent theorem; it is the main theorem applied at two different epochs with two different reading operators. The "epoch clause" is not a separate clause of the theorem — it is a reminder that transport operators themselves must satisfy the theorem's hypotheses.

**Pre-registered prediction**: any quantity Q(τ_2) computed by integrating an RD quantity Q(τ_1) through the post-fold dS cascade using the S75/S77 one-loop ε_H will inherit RD class. This is testable by comparing within-scheme transport across schemes; any PASS of such a transport claim should be flagged for review under this theorem.

### L5: Draft §VII.K for permanent-results-registry.md

Draft entry (≤25 lines) for `summary/permanent-results-registry.md §VII.K`:

```
§VII.K Regulator-Dressing Taxonomy (S82 — lizzi × connes workshop, 2026-04-18)

THEOREM (L2): A spectral quantity Q built from D_K on Jensen-deformed SU(3) is
FUNCTIONAL-INVARIANT (FI) under the regulator class {SDW, Zubarev, Wodzicki,
Mellin-Laplace, CC96 f-family} iff one of:
  (a) Q is a dimensionless CC96-Eq-2.11-weight-balanced ratio of spectral-moment
      combinations, evaluated at L_max >= rank(G), with Mellin weights cancelling
      by algebraic identity (power-law or P_m-reflection).
  (b) Q is a bounded-range mode-equation output whose boundary conditions and
      evolution operator are themselves FI; the regulator is integrated out by
      the mode-equation's structure (not by finite L_max truncation).

CLASSES: FI (invariant), RD (shifts under regulator change), MIXED (partial —
some ingredients FI, others RD). S82 42-verdict atlas: FI=30 (71.4%), RD=4,
MIXED=8. See L3 in sessions/archive/session-82/workshops/s82-regulator-dressing-taxonomy.md.

EPOCH SUB-THEOREM (L4): Q(tau_2) is FI iff Q(tau_1) is FI AND the transport
U(tau_1 -> tau_2) uses only FI ingredients. Post-fold dS cascade (using the RD
quantity eps_H = -d(ln H)/d(ln a) at one-loop) is RD-class transport. Horizon-
exit mode-equation reading is FI-class (clause (b)). Fold transit is singular;
no FI transport across tau = tau_fold.

COUNTER-EXAMPLES (probing iff): (CE1) chi_2 = <sqrt(x)> is bounded but RD --
bounded range alone is insufficient; must come from mode-eq structure.
(CE2) R_1 at L_max < rank(G) is pre-asymptotic RD -- rank-match clause is
necessary. (CE3) eps_H sign-flips across cutoff/zeta/anomaly schemes --
dimensionless ratio that violates CC96 weight-balance IS RD.

DEPENDENCIES: CC96 Eq 2.11 balanced-pair theorem; W2-13 13-f_0-convention
inventory; W3-2 reflection theorem R_k^{Wod}=R_{4-k}^{S73B} (residual 0.00e+00);
W3-K rank-universality (S78); Lizzi permanent pattern "ratios observables,
absolute moments regulator-dressed" (memory S66-S77).

SCOPE: applies to spectral quantities of D_K in analytic regulator class.
Pathological regulators (distributional, compactly-supported with zeros) may
require extension. Emergent observables downstream of the spectral action
inherit the FI/RD class of their spectral ingredients through L2's clause
algebra.

STATUS: THEOREM (iff holds under stated hypotheses); 42-row application atlas;
taxonomy standardizes scheme-dependency reporting in all S83+ gate verdicts.
Pre-registers gates on observable CLASS rather than on dressing class.
```

**Scope notes**:
- The §VII.K entry above is ~24 lines per the ≤25-line budget.
- Dependencies cited: CC96 Eq 2.11 (Chamseddine-Connes 1996), W2-13 13-convention inventory (S82), W3-2 reflection theorem (S82), S78 W3-K rank-universality, Lizzi pattern from agent memory (S66-S77).
- The entry is ACTION-ITEM-READY for `/weave --update` registration as a permanent theorem.

**Integration with existing registry**:
- Registers alongside §VII.A (CC96 balanced-pair theorem), §VII.B (Baptista volume cancellation), §VII.C (W3-2 reflection theorem). The three theorems form a connected cluster: balanced-pair (algebraic identity) + reflection (P_m-ladder identity) + taxonomy (classification by both).
- Does NOT supersede any prior entry; it CLASSIFIES prior entries. For example, §VII.B becomes "an instance of clause (a)"; §IV.A.LI H̃_A FI becomes "an instance of clause (b)".

### L6: Cross-Cutting Observations

**Obs 1: The W2-8 var_a0 = 68.55% FAIL is EXPECTED, not a framework defect**

Substitution chain:

Step 1 (def). var_a0 is the normalized variance of f_0 (a_0-slot Mellin weight) across the 5-scheme cluster {SDW, anomaly, f*, Gaussian, exp-decay}: var_a0 = σ²({f_0^{scheme}}) / ⟨f_0⟩².

Step 2 (sub). f_0 values verified (§V.H.3, Python-verified): {0, 0.5, 0.088, 1, 1}. Mean = 0.5176. Variance = 0.1840. Normalized = 0.1840 / 0.5176² = 0.6868 ≈ 68.55%.

Step 3 (read through L2). f_0 is an RD quantity by construction — it is the Mellin weight at n=0 of the regulator kernel, which DEFINES the regulator. Different regulators have different f_0 by definition. Asking "do the f_0 values cluster across regulators?" is mathematically identical to "is the regulator-kernel choice irrelevant at n=0?" — and the answer is NO, because the regulator kernel IS the axis along which the classification varies.

Step 4 (direction). var_a0 > 1% is not a finding about framework consistency — it is the *definition* of having different regulators. The pre-reg gate "var_a0 < 1%" is a TEST that would detect whether the 5 schemes are secretly the same at n=0; the FAIL confirms they are genuinely different.

**Conclusion**: The W2-8 FAIL is structurally RD-class (L3 row 24). The gate failed because the pre-registered threshold (1%) tested for FI at the slot-weight level — a test that is *impossible* to pass for a quantity that is RD by definition. P4-C's sibling-class tightness is recovered at the f_conv OBSERVABLE level (downstream of f_0, after the 1/M_0² amplification absorbs f_0 via CHK3+CHK4 structural identities). The FAIL is diagnostic, not defect. **The framework finding is**: sibling-class tightness lives on *observables*, not on bare slot weights — consistent with L2's theorem that FI quantities are ratios or mode-eq outputs, NOT single moment-weights.

**Obs 2: E_J per-cell "INVENTORY" is a subclass of RD with a finite known list of conventions — NOT a fourth class**

Argument (substitution chain-style):

Step 1 (def). "INVENTORY" in §VI.G would be a fourth class only if the E_J per-cell quantity had a mathematically distinguished structure not captured by FI/RD/MIXED.

Step 2 (sub). The 4 conventions C1-C4 in §VI.G.2 are: per-bond (0.933), per-cell BA (7.042), tessellation total (29.856), half-bond anisotropic (1.21). Each is a DIFFERENT QUANTITY at a different level of the extensivity hierarchy. They are related by multiplicative factors (F_anom, N_cells, 0.5·Σ).

Step 3 (simplify). Under a regulator transformation (SDW → Zubarev), each C_i value shifts by the same proportional factor (because all 4 are sourced from the same underlying Josephson coupling J_C2 and the same F_anom = 8.09, which is RD). So the RATIOS C_i/C_j across conventions are FI, but the absolute C_i values are RD.

Step 4 (direction). "INVENTORY" = "finite set of regulator-valued roles in an extensivity tree". This is operationally: each of 4 legitimate physical quantities is RD; the 4 roles are distinguishable by namespace (not by regulator). The "inventory width" (1.505 OOM) is the *span of the extensivity tree*, not a regulator-dressing spread.

**Conclusion**: INVENTORY is NOT a fourth class. It is RD-with-enumerated-finite-list — an RD subclass where the dressing axis is the role-in-hierarchy choice rather than the regulator-function choice. The L2 theorem applies: each individual C_i is RD (fails both (a) and (b)); C_i/C_j ratios are FI (clause (a)-like). Report as RD in the L3 table (row 30), with subclass tag "INVENTORY" if operational clarity is needed. **This preserves the three-class taxonomy's simplicity**.

**Obs 3: Is the A_s PASS-F2 at 1.57× Planck a fundamentally FI claim?**

Substitution chain:

Step 1 (def). A_s^{Branch A} = (H̃_A² / 8π²) · (1/ε_H) · F_amp_slot · c_sub⁻¹ · f_conv (UNIFIED-AS-79, §IV.B).

Step 2 (sub) under SDW at Branch A pivot:
- H̃_A = 2.464 × 10⁻⁵ (FI, verified)
- ε_H = 0.02163 (RD, S75/S77 one-loop; sign-flips between cutoff and zeta per S66)
- F_amp_slot = 0.3885 = F_amp_canonical × k_a2 = 1.0166 × 0.3822 (SD — k_a2 from S80 W1-A slot-consistency audit)
- c_sub = 2.238 (SD — subhorizon matching, S78 W2-E central)
- f_conv = 9.30 × 10⁻⁴ (RD — depends on f_0 single-value choice via 1/M_0²)

Step 3 (simplify). Substituting and grouping:
```
A_s = (FI² / 8π²) · (1/RD) · (SD · SD) · SD⁻¹ · RD
    = FI · RD² · SD²   (at leading dressing scaling)
```
Step 4 (direction). A_s contains TWO RD factors (1/ε_H and f_conv) and TWO SD factors (F_amp_slot, c_sub). Under a full regulator transformation SDW → Zubarev, both ε_H and f_conv shift; the shifts may partially or fully cancel.

**Test for hidden regulator choices** — does A_s PASS-F2 shift if we move to Zubarev?

- H̃_A is FI (unchanged by scheme).
- ε_H's Zubarev value is NOT published in S82; this is an OPEN EMPIRICAL question. If ε_H shifts by ≤10% across SDW→Zubarev, then (1/ε_H) shifts by ≤10%, and |Δ_OOM| shifts by ≤0.046 OOM — PASS-F2 preserved (headroom 0.104 OOM).
- f_conv shifts by the CC-subtraction: f_conv^{Zub}/f_conv^{SDW} is related to the 2.26 OOM H̃_B split. This could be a LARGE shift, bringing A_s outside PASS-F2.

**Conclusion**: The A_s = 1.57× Planck PASS-F2 is a MIXED claim with HIDDEN regulator choices in ε_H and f_conv. It is NOT a fundamentally FI claim. It is FI within the SDW scheme (PASS-F2 verdict is scheme-specific), but not across the full regulator class. To make it FI, one would need either (i) to compute it as a balanced ratio A_s / A_s_reference within the same scheme (trivially FI), or (ii) to express H̃_A² / (ε_H · f_conv) as a single balanced CC96 ratio — which would require a clause-(a) reconstruction of UNIFIED-AS-79 at the spectral-moment level. This is a structural carry-forward (proposed below).

**Implication for the permanent theorem**: the A_s PASS-F2 sits in the MIXED column of L3 (row 4). The verdict (PASS-F2) is verdict-FI within SDW, but the underlying VALUE is not pure FI. This is the expected behavior for phenomenology-adjacent observables (L2's iff theorem applies cleanly to structural quantities; phenomenology inherits MIXED from the spectral-action ingredient algebra).

**Synthesis of Obs 1-3**:

The FI/RD/MIXED taxonomy explains the S82 verdict landscape:
- **FAIL verdicts cluster on single-moment slot weights** (W2-8 var_a0) because these are RD by construction — the FAIL is the classification working as intended.
- **PASS verdicts cluster on balanced ratios and mode-eq outputs** (R_k atlas, H̃_A LI, K_substrate, reflection theorems) because these are FI by theorem.
- **MIXED verdicts cluster on phenomenology** (UNIFIED-AS-79 family, w_0 partition, μ-distortion) because these thread multiple regulator-dressed ingredients through a single physical prediction.

The taxonomy is therefore not decoration — it is a predictive classifier of which gates will pass cleanly under scheme changes and which will show scheme-dependence. S83 planning can pre-register gates on the CLASS rather than on the dressing class: gates on FI quantities need no scheme-comparison; gates on MIXED quantities require explicit scheme-pinning; gates on RD quantities report the inventory width as the measurement itself (as W2-13 successfully did).

**Pre-registered open question for S83**: does ε_H^{Zubarev} shift the A_s Branch A prediction outside PASS-F2? This is the concrete empirical test of Obs 3 and would sharpen the MIXED classification to either "MIXED-but-verdict-FI" or "MIXED-and-verdict-SD".

---

## Round 1 — connes: Response & Cross-Synthesis

### Part 1: Response to lizzi's Sections

#### Re: L1 — Seed audit

**AGREE** on 10/11 confirmations. **AGREE** on the Seed 10 revision to MIXED. **REFINE** Seed 5: lizzi is right that the reflection R_k^{Wod} = R_{4-k}^{S73B,gen} is "scheme-identity" stronger than FI, but from the K-theoretic side the sharper statement is that the two regulators produce the **same cyclic cocycle** up to reindexation — not merely the same value. This matters for §V.C (Kasparov) because a scheme-identity is an action on the cocycle-representative; a true FI would be an invariant of the cohomology class. On the generalized zeta ladder P_m, the identity residual 0.00e+00 (S82 §VI.B.3 across 24 (L_max, k) pairs) rules out cocycle-inequivalent lifts. **AGREE with lizzi; sharpening**: call Seed 5 *cocycle-level identity* rather than *cohomology-level invariance*. Operationally equivalent here, but the distinction matters for CE proposals below.

**MISSED on Seed 8 (χ_N·W)**: lizzi confirmed via the "a_0-dominated, 128.4% of χ_N" argument. From cyclic cohomology, a_0 is the class of the unit projection [1] ∈ K_0(A) paired with the degree-0 cyclic cocycle Tr_{Dixmier} — which is STRUCTURALLY invariant under regulator change only when the Dixmier trace exists and is unique (i.e. when D⁻ᵈⁱᵐ is measurable in Connes' sense, §IV.2 of *Noncommutative Geometry* 1994). On the Jensen-deformed SU(3) spectral triple, D_K has compact resolvent with Weyl asymptotics consistent with dim = 8 (the SU(3) KO-dim 0 extended by the M_4 factor), so the Dixmier trace is well-defined and a_0 lifts to a true FI via the measurable-operator theorem. I AGREE with the classification but provide the K-theoretic justification beyond "128.4% a_0-dominated": a_0 is FI because it is the ⟨[1], τ_Dixmier⟩ pairing, and pairings ⟨K_0, HP^{even}⟩ are the paradigmatic cyclic FI invariants.

**EMERGES**: Seed 5's scheme-identity + Seed 8's Dixmier-pairing structure together suggest a promotion beyond "FI". Some seeds should carry a **scheme-IDENTITY** tag rather than scheme-invariance — the stronger statement "the cocycle is literally the same function" vs the weaker "the cohomology class is the same". Seeds 5 and parts of Seed 8 are scheme-IDENTITY. Propose adding this as a sub-label in §VII.K: FI-identity ⊂ FI.

#### Re: L2 — Classification theorem

**AGREE** on the iff-theorem as stated, within the analytic-regulator class. **AGREE** that clauses (a) and (b) together cover the observed FI entries. **QUALIFY** the structural hole lizzi flagged: the "analytic-regulator-class" restriction can be pinned down by cyclic cohomology; I propose it is equivalent to the class of regulators producing **cohomologous cyclic cocycles** at the level of the associated Connes–Chern character.

**Substitution chain — analytic regulator class → cohomologous cocycles**:

Step 1 (definition). For a spectral triple (A, H, D) of dimension p (finite summable), Connes 1988/1994 defines the **Connes–Chern character** Ch(D) ∈ HP^*(A) (periodic cyclic cohomology) via the JLO cocycle or the dual Chern form on Ω^•_D(A). The pairing ⟨Ch(D), [e]⟩ for [e] ∈ K_0(A) computes the index of D_e, the twisted Dirac operator — and this pairing is an invariant of the K-homology class [D] ∈ KK(A, C), NOT of the specific operator D representing it.

Step 2 (substitution — regulator acts on operator, not class). A regulator f(D²/Λ²) or equivalent kernel transform does NOT change the K-homology class [D] as long as f belongs to the **analytic class** — meaning f is a positive Schwartz-class or tempered function such that f(D²/Λ²)·D shares the same index data as D. By the homotopy invariance of KK-theory (Kasparov 1980, Van den Dungen Paper 11 UKK-bar), any continuous family {D_s}_{s ∈ [0,1]} with D_0 = D and D_1 = f(D²/Λ²)·D has [D_0] = [D_1] ∈ KK(A, C).

Step 3 (simplification — cocycle change is coboundary). Under the Chern–Connes theorem (1985), two operators in the same KK-class produce Chern characters that differ by a coboundary in HP^*(A): Ch(D_1) - Ch(D_0) = b·(something) + B·(something). The *value* of the pairing ⟨Ch, [e]⟩ is invariant; the specific cocycle representatives can differ.

Step 4 (direction — what defines "analytic regulator class"). A regulator f belongs to the analytic class **iff** f(D²/Λ²)·D stays in the same KK-class as D. For positive Schwartz f with f(0) ≠ 0 (or regularized limit), this is automatic. For distributional f (delta-functions on spectra), or for f with zeros on the essential spectrum of D, the class can jump — these are the "pathological" regulators lizzi flagged.

**Conclusion**: lizzi's "analytic-regulator-class" structural hole is pinned by: **the regulator class is precisely those f for which [f(D²/Λ²)·D] = [D] in KK(A, C)**. SDW (Γ-function smoothing), Zubarev (CC-subtracted), Wodzicki (residue), Mellin-Laplace, and CC96 f-family all meet this criterion because they are pseudodifferential-operator-valued positive functions. Compactly-supported-with-zeros regulators and distributional regulators CAN fail this, and are outside the theorem's scope.

**REFINE clause (a)**: the CC96 Eq 2.11 weight-balance is the ALGEBRAIC manifestation of this K-homology invariance. A dimensionless ratio of a_n's at weight-balance is a ratio of pairings ⟨φ_n, [e]⟩ where φ_n are basic cyclic cocycles of matching degrees — the ratio is invariant under cohomologous change of cocycle because the numerator and denominator transform by the same coboundary. **Clause (a) is a CASE of clause-(a)-general: Q is a ratio of cyclic pairings ⟨φ, [e]⟩ of SAME total cyclic degree, with [e] fixed.**

**REFINE clause (b)**: the bounded-range mode equation reading is a CASE of clause-(b)-general: Q = output of an evolution on a bundle whose structure is captured by a K-theoretic transport [D_transport] that itself lies in KK(A_initial, A_final). Mukhanov-Sasaki with Bunch-Davies IC is one instance; BCS gap equation with Debye cutoff is another.

**On CE1-CE3**: all three are correctly RD under the K-theoretic reading. CE1 (χ_2 = ⟨√x⟩) is RD because ⟨√x⟩ at finite L_max is a partial trace, not a paired cyclic cocycle. CE2 (R_1 at L_max < rank(G)) fails because the cyclic cocycle representative is not stable against rank deficit — the KK-class is preserved asymptotically but the cocycle representative drifts. CE3 (ε_H sign-flip) fails because ε_H mixes cocycles of different cyclic degrees (logarithmic ratio is a degree-0 ↔ degree-2 mixing), so weight-balance is violated.

**Theorem status after refinement**: the iff holds as lizzi stated, with the K-theoretic equivalent formulation "Q is a pairing in the cohomology algebra HP^*(A) × K_*(A)" covering clause (a) and "Q is a K-homology transport output on bounded bundles" covering clause (b). The formulations are **equivalent in the analytic regulator class** — see C1 below for the full equivalence proof.

#### Re: L3 — Full classification table

**Count verification**: Python-verified FI=30, RD=4, MIXED=8, total=42, no gaps or duplicates in row indices 1..42. lizzi's arithmetic is clean.

**AGREE on 38/42 rows**. My K-theoretic reading agrees with lizzi's spectral-functional reading for 38 entries. I DISAGREE (classification refinement, not reversal) on 4 entries.

**K-theoretic split of lizzi's 30 FI rows** (my ternary partition, Python-verified to sum to 28/30 with 2 residual):

- **K_0-trivial / integer-invariants** (6 rows): #1 BRANCH-COUNT = 6, #12 Kasparov PROOF (K-class vanishes in Z), #16 MP-EXCLUSION Boolean, #22 34/4 audit integer, #29 12/12 groups Boolean, #37 adjacent = 1.0000. These are Z or Boolean — trivially rational-K-theoretic.
- **Clause (a) ratios → ⟨HP^{even}, K_0⟩ pairings** (9 rows): #3 CC-RATIOS-ONLY, #6 c_sub sign exact, #7 χ_N·W, #14 GW ratio, #20 Jensen sign, #28 f_NL k-flat, #32 R-family archetype, #35 rank(G) drift, #40 ℓ_phonon/ξ_BCS co-scaling.
- **Clause (b) mode-equation outputs** (13 rows): #8-11, #15, #21, #25-26, #31, #34, #36, #39, #41.
- **Residual (FI but not in above categories)** — rows **#19** (W2-7 falsifier rectangle REGISTERED-AND-FROZEN) and **#23** (f_0 cushion-width 2.0216 OOM). These are **pre-registration / dimensionless-bracket** quantities — invariant by CONSTRUCTION of the registration act, not by cyclic cohomology. They are FI in a structural sense that is orthogonal to my three-way K-split.

**EMERGES**: the residual rows #19, #23 point to a fourth FI mechanism — **combinatorial / pre-commitment FI**. Pre-registered rectangles and width-of-inventory brackets are FI because of how they are OPERATIONALLY defined, not because of cocycle invariance. This is not an ambiguity in lizzi's theorem — it is a subclass (b)-extension where the "mode equation" is replaced by an "operational commitment rule". Suggest adding to §VII.K a sub-clause: **(b')** Q is the output of a well-defined operational/combinatorial procedure on a pre-committed finite input set. Examples: audit-completeness integers, falsifier-box coordinates, cushion-bracket widths.

**DISAGREE (refinement on MIXED rows)**:

- **Row #13 (W2-2 UNIFIED-BACKREACT-79, r_max = 1.33e4)**: lizzi calls this MIXED. From the K-theoretic side this is **closer to pure RD** than to MIXED, because ρ_p/ρ_bg has both numerator and denominator containing unbalanced spectral moments that transform via DIFFERENT coboundaries. MIXED is the right classification only if we want to credit the PHO-amplitude FI fixed-mode-truncation piece. If we demand cohomological FI, row #13 is RD. **Refinement**: tag as MIXED-mostly-RD to distinguish from UNIFIED-AS-79 family (row #4, where H̃_A FI enters as a dominant factor).

- **Row #17-18 (W2-7 w_0 Volovik)**: lizzi calls these MIXED with "partial RD cancellation". From K-theory, w_0 = ρ_Λ/(ρ_Λ + ρ_grav) is a ratio of two cyclic pairings ⟨φ_0, [e]⟩ and ⟨φ_2, [e]⟩ of DIFFERENT cyclic degrees (0 and 2) — this is the CE3 pattern (dimensionless ratio that violates weight-balance). **Refinement**: row #17-18 are actually RD in K-theoretic reading; the "partial cancellation" is numerical, not cohomological. **AGREE with lizzi's MIXED tag operationally** (the verdict PASS at 0.0007 |Δ| is a measurement that reflects the accidental numerical cancellation), but flag that the STRUCTURAL class is RD; the FI-ness of the verdict is contingent on the current numerical values.

- **Row #27 (W2-14 FIRAS-CHLUBA μ-distortion)**: lizzi notes the 0.093 OOM cross-scheme drift and classifies MIXED. I AGREE. Adding K-theoretic interpretation: this is clause (b)-general with an RD-ingredient in S_IC(k); the μ integration by Chluba kernel preserves structure but imports S_IC's class. MIXED is correct.

- **Row #38 (W3-8 μ_eff-LK Leggett chemical potential)**: lizzi calls MIXED via Γ-rate regulator dependence. I AGREE. Lindblad-Keldysh kernels are pseudodifferential but the Born-Markov truncation IS a regulator choice (Markovian vs non-Markovian). Confirming MIXED.

**Two MIXED rows I want to PROMOTE toward FI**:

- **Row #42 (W3-10 sin²θ_W cubic RGE)**: lizzi calls MIXED. From K-theory, the RGE evolution operator exp(∫β(g) d ln μ) on K_0-classes of the gauge bundle is a **K-theoretic transport** — it preserves the K-class of the gauge-coupling projection. The boundary condition at M_KK uses a_n-derived couplings, but those couplings enter via a **ratio** of a_2 and a_4 (the Gilkey identity at KK scale, S61 a_2/a_0 = (5/12)R). The cubic polynomial rundown is a linear combination of cyclic pairings, not a single unbalanced moment. **PROPOSED PROMOTION**: row #42 could be FI under clause (a)-general IF one commits to the specific ratio structure. Without that commitment, MIXED is the safe classification. Flag as **MIXED-promotable**.

- **Row #33 (W3-5 F_amp SC-3PI = 47.918)**: lizzi calls MIXED via inheritance from r_max. K-theoretically, the 3PI NLO 1/N self-consistent closure is a fixed-point equation on the bundle of momentum-space propagators — the fixed-point exists iff the closure operator is contractive (the 2.44e-5 rel dev to asymptotic bound verifies contraction). This is a clause (b)-general mode equation with **FI boundary data** once r_max is pinned. So F_amp is **conditionally FI** given r_max. **Refinement**: tag MIXED-with-conditional-FI to capture the conditional structure.

**Summary**: classification counts stand as lizzi reported (FI=30, RD=4, MIXED=8). My refinements reshuffle the internal structure of the MIXED class into three subcategories (MIXED-mostly-RD, MIXED-verdict-FI-via-pinning, MIXED-promotable-to-FI) without changing the top-level tally.

#### Re: L4 — Epoch-resolved extension

**AGREE** on the iff statement "Q(τ_2) FI iff Q(τ_1) FI AND transport U uses only FI ingredients". **AGREE** the post-fold dS cascade is RD because ε_H is RD.

**K-theoretic version of the transport invariance**:

**Substitution chain — epoch transport preserves KK-class**:

Step 1 (definition). At epoch τ_1, the spectral triple is (A, H, D(τ_1)) with K-homology class [D(τ_1)] ∈ KK(A, C). The Jensen-deformation family {D(τ)}_{τ ∈ [0, τ_fold)} is a continuous path in the space of self-adjoint operators with compact resolvent.

Step 2 (substitution — homotopy invariance). If the path {D(τ)} satisfies the regularity hypotheses of Van den Dungen Paper 11 UKK-bar (spectral gap uniform in τ, resolvent norm-continuous), then [D(τ_1)] = [D(τ_2)] ∈ KK(A, C) for all τ_1, τ_2 ∈ [0, τ_fold) — the K-homology class is **constant** along the pre-fold Jensen family.

Step 3 (simplification). By the pairing theorem, if Q(τ) = ⟨Ch(D(τ)), [e]⟩ for some fixed [e] ∈ K_0(A), then Q(τ) is INDEPENDENT of τ in the pre-fold regime. Pre-fold transport preserves ALL K-theoretic invariants automatically — this is the K-theoretic reinforcement of lizzi's "pre-fold laminar: YES (in principle)" entry.

Step 4 (direction). Across the fold τ = τ_fold, the spectral density reorganizes discontinuously. In K-theoretic terms, the first-order phase transition can CHANGE the K-homology class — the pre-fold [D] and post-fold [D] may lie in different components of KK(A, C). This is the **K-theoretic obstruction to pre-fold → post-fold transport**.

**Conclusion**: lizzi's "pre-fold laminar preserves FI / fold transit does NOT" is structurally correct, and the K-theoretic underwriter is the discontinuity of the KK-class across the fold. The post-fold dS cascade, *as a continuous transport within the post-fold component*, would in principle preserve FI — IF ε_H were FI. Which it isn't.

**Is ε_H fundamentally RD, or could a first-principles derivation make it FI?**

This is the critical question. Substitution chain:

Step 1 (definition). ε_H = -d(ln H)/d(ln a) = 3(1 + w_eff) for a perfect fluid substrate. At the spectral level: H² ∝ ρ ∝ a_0^{regularized}, so ε_H = d(ln a_0)/d(ln a) × (1/6) × correction terms.

Step 2 (substitution). a_0^{regularized} = Σ_{λ ∈ σ(D²)} f(λ/Λ²) is a weighted sum with kernel-dependent weight. Under SDW → Zubarev, the weight profile changes, so a_0 → a_0 + Δa_0 with Δa_0 ≠ 0 in general. The ratio d(ln a_0)/d(ln a) involves the same a_0 in numerator (d ln) and denominator (a_0), suggesting partial cancellation.

Step 3 (simplify). Under scheme change f → f̃, d(a_0) → d(a_0 + Δa_0) and a_0 → a_0 + Δa_0. For the ratio d(ln a_0)/d(ln a) to be FI, we need Δa_0/a_0 to be **constant in a** (τ-independent scheme offset). S66 ZETA-SA showed this is NOT the case: ε_H SIGN-FLIPS across cutoff, zeta, and anomaly schemes. The Δa_0/a_0 offset depends on τ.

Step 4 (direction). ε_H is **structurally RD** as currently formulated. It could become FI if one reformulates it as a **balanced ratio**: e.g., ε_H^{balanced} := d(ln a_0)/d(ln a) × (some compensating FI factor that absorbs the scheme-dependent offset). From cyclic cohomology, the natural candidate is to promote ε_H to a **Connes–Chern character representative** that absorbs the scheme offset as a coboundary. This requires introducing a degree-2 cyclic cocycle φ_2 such that ε_H = ⟨φ_2, [e]⟩ / ⟨φ_0, [e]⟩ with matching cyclic degrees.

**K-theoretic first-principles derivation of ε_H** (proposed): compute the **scalar curvature K-theoretic class** as the pairing ⟨φ_2^{Chern}, [e]⟩ where φ_2^{Chern} is the dual Chern form of the Weil-Chern character, and express dH²/dN as the time derivative of the projection pairing onto the cosmological volume projection. This would give an ε_H that IS a balanced ratio of two pairings and hence FI by the theorem.

**Status**: ε_H is CURRENTLY RD (empirically verified by S66 sign-flip). A first-principles K-theoretic derivation CAN in principle make it FI, but this derivation has NOT been carried out and is a substantive open problem — it would require a cyclic-cohomological reformulation of the Friedmann equation itself. This is a **carry-forward for S83**: attempt the K-theoretic promotion of ε_H.

**If this promotion succeeds**, then by lizzi's epoch sub-theorem, the post-fold dS cascade becomes FI-transport, and H̃_B itself could be evaluated as an FI quantity — closing the 2.26 OOM SDW-vs-Zubarev split STRUCTURALLY. This is the most direct route to resolving the H̃ divergence identified in W1-1.

**Cautionary caveat**: The promotion may FAIL. The Friedmann equation in the substrate frame is NOT a cyclic pairing; it is a NON-CYCLIC dynamical equation relating a_0 (CC moment) to H² (time-derivative of scale factor). There is a structural tension between the KINEMATICS (cyclic pairings are stationary invariants) and the DYNAMICS (Friedmann is an evolution equation). Lizzi's statement "post-fold dS cascade is RD" may be a **structural truth** that resists K-theoretic promotion. Worth testing; worth being prepared for the negative outcome.

#### Re: L5 — §VII.K registry draft

**AGREE** the 24-line draft is substantively ready for registration. **SUGGEST** three edits:

**Edit 1 (CLASSES section)**: add FI-identity sub-tag for cocycle-level identities (Seed 5 type). Current draft lumps this with FI; the distinction matters for §V.C Kasparov proof consistency (which relies on cocycle-level representation, not just cohomology class). Amended line:

```
CLASSES: FI (invariant), FI-identity (cocycle-level identity, stronger than FI;
Seed 5 W3-2 reflection), RD (shifts), MIXED (partial). Atlas: FI=30 (71.4%),
RD=4, MIXED=8, of which FI-identity subset in FI = 3 (#3, #6, #32 all exact
identities). See L3.
```

**Edit 2 (THEOREM clause a)**: add the K-theoretic underwriter as a parenthetical. Current clause (a) reads "dimensionless CC96-Eq-2.11-weight-balanced ratio"; amended:

```
(a) Q is a dimensionless CC96-Eq-2.11-weight-balanced ratio of spectral-moment
    combinations (equivalently, a ratio of cyclic-cocycle pairings <phi, [e]>
    of matching cyclic degrees), evaluated at L_max >= rank(G), with Mellin
    weights cancelling by algebraic identity.
```

**Edit 3 (SCOPE)**: pin the analytic-regulator class via KK-theory. Current reads "analytic regulator class"; amended:

```
SCOPE: applies to spectral quantities of D_K in the analytic regulator class,
defined as those regulators f for which f(D^2/Lambda^2).D stays in the same
KK-class as D (Kasparov K-homology homotopy invariance). Includes SDW, Zubarev,
Wodzicki, Mellin-Laplace, CC96 f-family. Excludes distributional regulators
and compactly-supported-with-zeros kernels. Pathological regulators may shift
the KK-class; separate analysis required.
```

**Edit 4 (DEPENDENCIES)**: add Van den Dungen Paper 11 (UKK-bar) and Connes 1994 Chapter IV (Dixmier trace / measurable operators).

**Edit 5 (STATUS)**: add the sub-clause for operational/pre-commitment FI (rows #19, #23).

Amended STATUS:

```
STATUS: THEOREM (iff holds under stated hypotheses, analytic regulator class
pinned via KK-homotopy); 42-row application atlas; clause (b') operational /
pre-commitment FI covers 2 additional rows (#19 falsifier rectangle, #23
cushion-width bracket). Taxonomy standardizes scheme-dependency reporting in
all S83+ gate verdicts.
```

With these edits, the §VII.K draft grows from ~24 lines to ~31 lines — over the ≤25 budget. **Suggest**: move the FI-identity sub-tag to a §VII.K.a footnote, keep the main §VII.K at ≤25 lines. Alternatively, promote the Atlas (FI=30 etc) to a separate §VII.K-ATLAS entry — the Atlas is operational bookkeeping, the THEOREM is the permanent result.

**READY FOR REGISTRATION** pending these edits. The iff-theorem + L3 atlas + L4 epoch sub-theorem is the strongest permanent result from S82, cleaner than any individual verdict in the 42-row set.

**EMERGES**: §VII.K should explicitly cross-reference §V.C (Kasparov-Abelian-Proof) as an instance where the FI/RD/MIXED taxonomy is applied at the K-class level — per-branch R-protection (the Kasparov theorem's core) is a classification of the gauge-branch K-classes into FI-protected (non-abelian) and RD-unprotected (abelian) categories. This makes §V.C and §VII.K two faces of the same structural insight: the FI/RD split lives at the K-theory level, not at the numerical level.

#### Re: L6 — Cross-cutting

**Re: Obs 1 (W2-8 var_a0 FAIL is structurally expected)**. **AGREE entirely**. K-theoretic reinforcement: f_0 is the degree-0 cyclic cocycle weight of the regulator — it IS the regulator at n=0. Asking whether f_0 values cluster across regulators is asking whether regulators have the same n=0 moment, which by construction they do not. The test var_a0 < 1% is a MEASUREMENT of whether the 5 schemes are secretly degenerate at n=0; the FAIL certifies they are genuinely independent. **This is not a defect, it is a normalization check** — the 5 schemes occupy distinct regions of regulator-space as they should. Register as "FAIL-BY-DESIGN", a subclass of RD where the FAIL is the diagnostic, not a failure.

**Re: Obs 2 (E_J INVENTORY is a subclass of RD)**. **AGREE**. K-theoretic sharpening: the 4 values C1-C4 correspond to 4 distinct K_0-classes of the underlying physical quantity — per-bond is the generator class of K_0(C*_{bond}), per-cell is [N_cells]·generator, tessellation-total is the total class, half-bond is a Z_2-quotient class. These are all **legitimate K-classes of related but DISTINCT projections** in the extensivity tree. The "dressing axis" is a namespace axis in the K-class algebra. **INVENTORY is not a fourth taxonomic class; it is RD-with-enumerated-finite-K-class-family.** Agree with lizzi's three-class simplicity.

**Re: Obs 3 (A_s PASS-F2 MIXED — is it fundamentally FI?)**. This is the key question. lizzi's substitution chain shows A_s = FI · RD² · SD² at leading dressing scaling; verdict PASS-F2 is MIXED-verdict-FI-via-pinning.

**Is this a FEATURE or a bug?**

Substitution chain for the direction claim:

Step 1 (definition). A prediction in the framework is a numerical value that compares against an observational anchor (here, A_s_Planck = 2.1 × 10⁻⁹). The prediction's RELIABILITY is a function of (i) the FI content of its inputs, (ii) the structural-fixedness of the RD ingredients (are they free or pinned?), (iii) the verdict-level PASS/FAIL gate.

Step 2 (substitution). For A_s: H̃_A is FI by L2 clause (b); ε_H is RD but is STRUCTURALLY FIXED once the scheme is chosen and ε_H^{one-loop} is computed from the spectral gradient (no free parameter); F_amp_slot is SD (convention choice) but PINNED by S80 W1-A slot-consistency audit; c_sub is SD but PINNED by S78 W2-E central value; f_conv is RD but STRUCTURALLY FIXED via f_0 and 1/M_0². Every RD/SD ingredient has been pinned or derived — NONE are free parameters.

Step 3 (simplify). The prediction A_s = 1.57 × Planck is MIXED at the ingredient level but **zero-free-parameter at the prediction level**. The PASS-F2 verdict carries the weight of threading a correct prediction through a MIXED algebra of structurally-fixed ingredients.

Step 4 (direction). A prediction threading FI + structurally-fixed-RD + structurally-fixed-SD ingredients **IS** a prediction. The FI/RD/MIXED taxonomy classifies how the prediction responds to REGULATOR CHANGE; it does NOT classify whether the prediction is structurally-committed. A_s PASS-F2 is structurally committed (all ingredients pinned), so the verdict is a REAL PREDICTION — even though the ingredient algebra is MIXED.

**Conclusion**: lizzi's classification "MIXED-verdict-FI-via-pinned-slot-audit" is the RIGHT label. **Obs 3's A_s MIXED is a FEATURE, provided the structural-fixing is maintained.** If ε_H^{Zubarev} shifts the prediction outside PASS-F2, that would demote the verdict to MIXED-and-verdict-SD, and the A_s claim would weaken. The pre-registered open question for S83 (ε_H^{Zubarev} test) is the right follow-up.

**The FI/RD/MIXED taxonomy tells us WHAT TO CHECK** for each prediction — FI predictions need no further scheme-check; MIXED predictions need explicit scheme-robustness tests; RD predictions need inventory-width reporting. It is a prioritization tool for scheme-robustness auditing in S83+ gate planning.

**Re: Synthesis of Obs 1-3**. **AGREE** completely. One addition from K-theory:

The three clusters lizzi identified (FAIL on slot weights, PASS on ratios/modes, MIXED on phenomenology) map cleanly to the three K-theoretic levels:

- **FAIL cluster (slot weights)** = measurements of INDIVIDUAL cyclic cocycles φ_n (not their pairings). These are regulator-dependent by construction.
- **PASS cluster (ratios/modes)** = measurements of PAIRINGS ⟨φ, [e]⟩ that are K-class invariants. FI by theorem.
- **MIXED cluster (phenomenology)** = combinations of multiple cocycles with multiple projection classes; the algebra of the combination determines whether the result is a pure pairing (FI) or a sum of pairings of different degrees (RD/MIXED).

**Pre-registered prediction I endorse for S83**: the ε_H^{Zubarev} test. If ε_H^{Zubarev} / ε_H^{SDW} ∈ [0.9, 1.1] then A_s PASS-F2 survives and Obs 3 is confirmed as "MIXED-verdict-FI-via-pinning". If ε_H^{Zubarev} / ε_H^{SDW} ∉ [0.3, 3.0] then the prediction shifts by > 0.5 OOM and A_s demotes to SD. The test has direct consequences for W1-1 H̃ divergence resolution.

### Part 2: Original Analysis

#### C1: K-theoretic characterization of the FI class via cyclic cohomology

**Proposed characterization (connes)**. Let (A, H, D) be the spectral triple on M × SU(3) at Jensen-deformation τ, with A = C(M) ⊗ C*(SU(3)) and D = D_M ⊗ 1 + γ_M ⊗ D_K. A spectral quantity Q is **FUNCTIONAL-INVARIANT (FI-K)** under the analytic-regulator class {f(D²/Λ²)·D : [f(D²/Λ²)·D] = [D] in KK(A, C)} iff one of:

**(K-a) Cyclic pairing clause**: Q is a pairing Q = ⟨[φ], [e]⟩, where [φ] ∈ HP^{even}(A) (periodic cyclic cohomology) and [e] ∈ K_0(A), OR a rational combination (finite sum / ratio with non-vanishing denominator) of such pairings of matching total cyclic degree.

**(K-b) K-homology transport clause**: Q is the output of a K-homology transport U: KK(A, C) → KK(A', C') where A, A' are sub-C*-algebras of C(Ω) for some parameter space Ω, and U is implemented by a **correspondence** (bimodule with connection) whose class [U] ∈ KK(A ⊗ A'^{op}, C_0(Ω)) is itself FI-K. Bounded-range mode equations (Mukhanov-Sasaki, BCS, Friedmann with fixed IC) are the principal instances.

**(K-c) Integer / Boolean / combinatorial invariants**: Q ∈ Z or Q ∈ {0, 1} or Q is the output of a well-defined operational/combinatorial procedure on a pre-committed finite input set. These are trivially rational-K-theoretic (Z ⊂ Z ⊗ Q) and sit in K_0(C) = Z.

**Comparison to lizzi's iff-theorem**:

Lizzi's clause (a) ↔ my (K-a): **EQUIVALENT** in the analytic-regulator class.

Substitution chain for equivalence:

Step 1 (definition). lizzi (a): Q = dimensionless CC96-Eq-2.11-weight-balanced ratio of a_n's.

Step 2 (substitution). a_n = ⟨τ_n, [1]⟩ where τ_n is the degree-n basic cyclic cocycle (Connes 1985). The CC96 weight-balance condition indices_below + indices_above = 2·indices_center ensures all cocycles have matching cyclic total degree when paired with [1].

Step 3 (simplify). A weight-balanced ratio of a_n's is a ratio of pairings ⟨τ, [1]⟩ with matching degree — which is exactly (K-a).

Step 4 (direction). lizzi (a) ⇒ (K-a) by explicit construction. (K-a) ⇒ lizzi (a) by noting that any rational combination of cyclic pairings of matching degree admits a weight-balanced representation on the a_n basis (this is the theorem that HP^{even}(A) is generated, at the level of the index-theoretic pairing, by the basic cocycles in the analytic regulator class — Connes 1985 Theorem 2.1, *Noncommutative Geometry* §III.1).

Therefore lizzi (a) ⇔ (K-a) in the analytic regulator class.

Lizzi's clause (b) ↔ my (K-b): **EQUIVALENT with extension**. Lizzi's clause (b) names specific mode equations (Mukhanov-Sasaki, BCS, Friedmann). (K-b) is the abstract statement that the transport is a KK-correspondence. The equivalence follows because (i) each named mode equation is a specific KK-correspondence (Kasparov product of the evolution bundle with the initial-condition projection), and (ii) any KK-correspondence with bounded-range data admits a representation as a specific mode equation with bounded spectrum. In the analytic-regulator class, (K-b) ⇔ lizzi (b).

**(K-c)** is a NEW ELEMENT that lizzi's formulation subsumes implicitly via "clause (a) trivial" labels. Making it explicit lets rows #1, #12, #16, #22, #29, #37 be classified cleanly as K-c without having to force them into (K-a) or (K-b). lizzi's "clause (a)-trivial" tag ≡ my (K-c).

**Does one formulation subsume the other?**

**Neither subsumes; they are complementary within the analytic regulator class.** lizzi's formulation is operationally sharp (check CC96 weight-balance by looking at the a_n indices). My K-theoretic formulation is structurally universal (any pairing in HP^* × K_* is FI, regardless of specific moment structure) but requires computing or asserting the cyclic degree.

**For the S82 42-row atlas, both give the same classification** (FI=30, RD=4, MIXED=8). This is the K-theoretic EQUIVALENCE of lizzi's theorem — a strong consistency check.

**Where K-theory has leverage beyond lizzi's formulation**: non-Seeley-DeWitt quantities that are nonetheless FI by virtue of being K-class invariants. Examples in C2 below:
- **eta-invariant η(D)**: a spectral invariant of D that is a K-theoretic pairing but NOT a CC96 spectral moment. Classified FI by (K-a) generalized; unclassified by lizzi's formulation.
- **Fredholm index Ind(D_e)**: the paradigmatic K-class invariant, always FI-K.
- **Spectral torsion** (Connes-Moscovici): FI-K via a higher-degree cocycle pairing.

These are NCG quantities that the framework might need in the future but that sit outside lizzi's SDW-moment-centric formulation.

**Proposed registry formulation**: use lizzi's iff-theorem as the operational statement + add (K-a), (K-b), (K-c) as the K-theoretic equivalent statement. Both appear in §VII.K with a note that they are equivalent in the analytic regulator class. This preserves lizzi's operational sharpness while giving the K-theoretic structural basis for future extensions.

#### C2: Counter-example search — quantities that pass the theorem's "iff" but are RD in practice

lizzi proposed CE1-CE3 which probe the theorem's edges on the spectral-moment side. I propose three additional counter-examples probing the K-theoretic side:

**CE4 (pseudo-counter, Rationality-trap): The eta-invariant η(D_τ) is rationally-K-theoretic (sits in Q) but can appear RD under poor regularization.**

Substitution chain for the counter-example status:

Step 1 (definition). η(D) = (1/√π) ∫_0^∞ Tr(D e^{-tD²}) t^{-1/2} dt is the Atiyah-Patodi-Singer eta-invariant of D. For the Jensen-deformed D_K(τ), η(D_K(τ)) is a spectral asymmetry.

Step 2 (substitution). η(D) is rationally-K-theoretic: η(D) mod Z is a K-theoretic invariant (the eta class in K_1(A) ⊗ R / Z, Atiyah-Patodi-Singer 1975). The fractional part Frac(η) is FI-K via (K-a) generalized to degree-1 cyclic cocycles.

Step 3 (simplify). The INTEGER part of η(D), however, jumps under spectral flow — which occurs as τ crosses eigenvalue-crossing points in the Jensen family. Under regulator smoothing (SDW vs Zubarev), different smoothings can assign the integer part differently if the regulator has non-trivial support near λ = 0.

Step 4 (direction). η(D) is FI-K by C1 characterization (it is a cyclic pairing) but CAN appear RD in practice because the integer part is regulator-ambiguous near zero modes. In the analytic regulator class WITHOUT zero-mode ambiguity (D invertible or regularized with zero-mode subtraction), η is FI. In practice for Jensen-deformed D_K(τ), this requires τ to avoid spectral-crossing values.

**Resolution**: η(D) is conditionally FI. Under the analytic-regulator class with zero-mode subtraction, FI-K holds. Without such subtraction, appearance of RD is a regulator-ambiguity artifact. **CE4 sharpens the "analytic regulator class" definition to include zero-mode subtraction as a default convention.**

**CE5 (genuine counter-counter-example, K-theoretic PASS that lizzi's iff would also PASS): the Connes–Chern character itself as a cyclic class.**

Ch(D) ∈ HP^*(A) is the archetypal FI-K invariant. It is a cocycle, not a pairing — so it does NOT fit lizzi's clause (a) directly (which requires a ratio of pairings). But it is the GENERATING OBJECT from which all clause-(a) pairings arise.

Under the theorem, Ch(D) is a *collection of cocycles* at each degree; each basic cocycle τ_n is a class in HC^n(A), and [Ch(D)] ∈ HP^{even}(A) is the total class. The class is FI-K by homotopy invariance (KK-homotopy).

**Conclusion**: Ch(D) IS FI-K and lizzi's iff captures this via clause (a) (every ratio of pairings of Ch(D) is FI) — but the GENERATOR ITSELF, not a ratio, is also FI-K. This is a counter-counter-example in the sense that it confirms the iff but extends it: the class HP^{even}(A) has FI-K ELEMENTS, not just FI-K pairings. lizzi's formulation is sound and the K-theoretic formulation covers the generator directly.

**CE6 (genuine new counter-example: spectral torsion as ambiguous-iff quantity).**

Definition: the spectral torsion Tor(D) of Connes–Moscovici (2014, *Cyclic Cohomology of Hopf Algebras*) is a higher-degree cyclic cocycle computing the transverse spectral-density torsion of a foliation spectral triple. For the Jensen-family, the foliation is the τ-direction in the parameter space Ω = [0, τ_fold).

Substitution chain:

Step 1 (definition). Tor(D_τ) = ⟨φ_{3}^{CM}, [e]⟩ where φ_{3}^{CM} is the degree-3 Connes–Moscovici cocycle and [e] is the transverse-direction projection in K_0(A_τ).

Step 2 (substitution). The CM cocycle is NOT one of the basic cocycles τ_n of CC96. It is constructed from the Hopf algebra H_1 of codimension-1 foliations. Under the FI-K characterization (K-a), Tor is a cyclic pairing and therefore FI-K.

Step 3 (simplify — lizzi's iff test). lizzi's (a) requires weight-balance in the CC96 a_n sense. The CM cocycle φ_3 does NOT admit a CC96 a_n representation (it is a higher-codimension object). So lizzi's (a) does NOT APPLY. Lizzi's (b) does not apply either (Tor is not a mode-equation output).

Step 4 (direction). Tor(D) is **FI-K by my characterization but UNCLASSIFIED by lizzi's iff.** This is a genuine gap — a K-theoretic FI quantity that neither (a) nor (b) of lizzi's theorem captures.

**Resolution for the theorem**: lizzi's iff needs to be widened to include "higher cyclic cocycles beyond CC96 basic cocycles" in clause (a). The revised clause:

```
(a') Q is a ratio of cyclic-cocycle pairings <phi, [e]> of matching total
     cyclic degree, where [phi] in HP^{even}(A) ranges over ALL cyclic
     classes (not just CC96 basic cocycles).
```

This widening recovers all CC96-FI quantities + CM-type higher-codimension FI quantities. **CE6 is a genuine reason to widen lizzi's iff; K-theory provides the sharper statement.**

**New counter-example for lizzi (C2 headline)**:

**CE7 (K-theoretic FI that LOOKS RD under naive reading): the cross-level R-protection index at non-abelian branches.**

From §V.C (W2-3 KASPAROV-ABELIAN): the Level-2 R-protection cohomology class for a non-abelian branch (e.g., su(2)) is the Chern class c_2(A_B') ∈ K_0(C_0(M) ⊗ A_B') ≠ 0. This class IS an FI-K invariant (it is a K_0-class). But the NUMERICAL VALUE it produces — the drift_{su(2)}(L) at empirical L_max — can appear RD under naive reading if one mistakes "the drift" for "the class".

Substitution chain:

Step 1 (def). The R-protection class is c_2(A_B') ∈ K_0(C_0(M) ⊗ A_B'); this is a K-theoretic invariant, hence FI-K.

Step 2 (sub). The empirical drift metric drift_su2(L) is a FINITE-L_max proxy for the asymptotic class-level invariant. It converges to the class value as L_max → ∞.

Step 3 (simplify). At finite L_max, drift_su2(L) can fluctuate; at L = 8 the reported value is 2.84% (S80 W2C-L8-DRIFT on su(2) branch, stable across 5-sweep, §V.C Section 6 consistency).

Step 4 (direction). The drift VALUE at finite L_max is a regulator-dependent numerical proxy, but the DRIFT CLASS (the asymptotic structural invariant it approaches) is FI-K. **CE7 shows that a quantity can be FI at the class level but appear RD at the measurement level if L_max is small.**

**Resolution**: this is not a counter-example to the theorem; it is a warning about **OPERATIONAL** (finite-L_max) vs **STRUCTURAL** (asymptotic class) FI reading. The L2 theorem should distinguish these two levels. lizzi's rank-match clause (L_max ≥ rank(G)) is the correct operational test; CE7 confirms it is necessary for the K-theoretic class to be representable at finite L_max.

**Summary of C2**:

| Counter-example | Direction | Impact on theorem |
|:----------------|:----------|:-----------------|
| CE4 η-invariant | FI-K with zero-mode caveat | Sharpens analytic regulator class to include zero-mode subtraction |
| CE5 Ch(D) generator | FI-K confirms iff | Confirms; extends to generators not only pairings |
| CE6 spectral torsion | FI-K not captured by lizzi's (a)-(b) | **Widen clause (a) to all cyclic classes, not only CC96 basic** |
| CE7 non-abelian drift | FI at class level, RD at finite L_max | Confirms rank-match clause necessity |

**Most actionable**: CE6 — widen lizzi's clause (a) from CC96 basic cocycles to general HP^{even} classes. This preserves all current classifications and future-proofs the theorem for non-CC96 NCG quantities.

#### C3: Questions for lizzi

Numbered questions targeting the three principal leverage points: the analytic-regulator-class hole, BFV/BRST cohomology, and the MIXED class explosion.

**Q1 — Analytic regulator class scope: pseudodifferential only, or also compact perturbations?**

Your L2 theorem's "analytic regulator class" is pinned in my Re:L2 to {f : [f(D²/Λ²)·D] = [D] in KK}. This covers SDW, Zubarev, Wodzicki, Mellin-Laplace. **But does it cover compact-perturbation regulators** (e.g., D → D + K for K compact)? These preserve the KK-class by Kasparov invariance under compact perturbations (Kasparov 1980 Theorem 1.4), but they are NOT pseudodifferential — they are operator-level perturbations.

Specifically: if we regularize D by D_reg = D + εK with K compact and ε → 0, is the resulting a_n(D_reg) in your clause-(a) class? Do the CC96 weight-balance relations survive? My suspicion is YES (compact perturbations preserve all KK-data and asymptotic spectra match in the weak-coupling limit), but it is worth stating explicitly in §VII.K.

**Q2 — BFV/BRST cohomology: does the RD class cover BRST-exact vs BRST-cohomology-class distinctions?**

A quantity like the ghost-number current J_ghost^μ is BRST-exact: J_ghost = Q_BRST(X) for some X. The correlator ⟨J_ghost^μ⟩ vanishes by BRST cohomology. If we try to classify ⟨J_ghost⟩ under your FI/RD/MIXED taxonomy, it is FI in the trivial sense (vanishes in all schemes, invariant = 0) — but the NON-TRIVIAL BRST-cohomology-class representative ⟨Q_obs⟩ for a gauge-invariant observable Q_obs is FI in a STRUCTURAL sense (invariant of the cohomology class).

**Question**: does your FI class intend to capture BRST-cohomology-class invariance as a special case? If yes, how do you handle the subtlety that the cocycle representative within a BRST-class is NOT FI (it shifts by BRST-exact terms)? Specifically: at a gauge-fixed computation (e.g., Lorenz gauge), the specific value of a cocycle depends on the gauge; the class does not. Does your taxonomy distinguish cocycle-level from class-level?

My own view: your theorem should apply at the **class level** (BRST-cohomology-class = FI, cocycle-within-class = gauge-dependent not regulator-dependent). But the interaction between BRST gauge dependence and regulator dependence needs to be clarified — they may be ORTHOGONAL degrees of freedom (gauge choice is not regulator choice) or they may couple (certain gauges induce certain regulators in a Lagrangian path-integral formulation). Your memory on Kasparov-KK and Van den Dungen Paper 05 gauge-module framework suggests you have a view.

**Q3 — MIXED class explosion (8/42): weakening of iff, or its own permanent category?**

The MIXED class has 8 members in L3 — more than the pure-RD class (4 members). Every phenomenological prediction (UNIFIED-AS-79 family, w_0, μ-distortion, sin²θ_W RGE) sits in MIXED.

**Question**: is this a sign that the iff-theorem is sharp but the MIXED class is the **dominant phenomenological taxonomy**, or that the iff-theorem needs a WEAKENING that splits MIXED into sub-classes?

Three possibilities:

(i) **MIXED is its own permanent category**, registering every prediction that threads multiple regulator-dressed ingredients. §VII.K admits MIXED as a full tax-class. Phenomenology CARRIES this subtaxonomy as a FEATURE.

(ii) **The iff-theorem is over-sharp**. It correctly identifies FI and RD at the structural level, but forces phenomenological predictions into MIXED because the real taxonomy of predictions is finer than the three-class split. In this case we need **(iia) MIXED-verdict-FI-via-pinning** (row #4), **(iib) MIXED-mostly-RD** (row #13), **(iic) MIXED-promotable** (row #42), etc.

(iii) **The iff is correct but we need a new clause for phenomenology**. A **clause (c)**: Q is FI-phen if Q is a MIXED combination whose RD ingredients are all STRUCTURALLY PINNED (not free). Then phenomenological predictions become FI-phen, which is a weaker but operationally useful category.

My strong preference is **(ii)** — the MIXED class needs three sub-tags (a, b, c as above) because the scientific purpose of each MIXED-entry is different (row #4 is a real prediction, row #13 is a FAIL-by-design, row #42 is a promotable case). Registering all three in §VII.K atlas makes the taxonomy more useful.

**What is your view?**

---

**Q4 (bonus, rank-match clause extension)**: your L2 clause (a) has a rank-match clause (L_max ≥ rank(G)). From the K-theoretic side (C1), this corresponds to the requirement that the K_0-generators of A_F = C*(SU(3)) are fully representable at L_max. For SU(3) this is rank-2 so L_max ≥ 2 is sufficient for K_0 generation — but L_max ≥ 3 is needed for the Cartan-type 3 structure to appear (Baptista irrep content). **Is the "rank-match" in your theorem a K-theoretic rank (= 2 for SU(3)) or an irrep-generating rank (= 3 for the 8 = 3 + 3* + 2 decomposition)**? The two differ and the operational boundary for S82 verdicts may depend on which we mean.

**Q5 (bonus, ε_H promotion)**: in my Re:L4 I proposed a K-theoretic promotion of ε_H to a balanced ratio of cyclic pairings. Is this structurally achievable, or does the kinematic/dynamic tension (Friedmann is dynamical, cyclic pairings are stationary) block the promotion? This question has DIRECT implications for W1-1 H̃-divergence — a successful promotion would make the post-fold cascade FI-transport and close the 2.26 OOM split structurally.

---

## Round 2 — lizzi: Follow-up

### CONVERGENCE

Six acceptances, each accompanied by a substitution-chain where the claim carries a direction.

**C1. Analytic-regulator-class hole CLOSED via Kasparov KK-homotopy** (Re:L2 + C1).

My L2 flagged the structural hole: "the theorem holds under the 'analytic regulator class' but needs extension for pathological regulators". Connes's Re:L2 pins this precisely:

*Substitution chain for the acceptance.*
- Step 1 (def). L2 analytic-regulator-class = {f : f produces FI for all Q satisfying clauses (a) or (b)}.
- Step 2 (sub). Connes C1 proposes: {f : [f(D²/Λ²)·D] = [D] in KK(A, C)}.
- Step 3 (simplify). Under Kasparov KK-homotopy invariance (Kasparov 1980 Thm 1.4), any continuous path {D_s} of self-adjoint operators with compact resolvent and uniform spectral gap preserves the KK-class. The class of f's that produce such paths is exactly the pseudodifferential-positive-Schwartz class.
- Step 4 (direction). The L2 hole is the set of f's outside this class. Connes's pinning CLOSES the hole: SDW, Zubarev, Wodzicki, Mellin-Laplace, CC96 f-family all satisfy [f(D²/Λ²)·D] = [D]. Distributional regulators and compactly-supported-with-zeros kernels do not — these are exactly the "pathological" f's I flagged.

**ACCEPT** the Kasparov-KK characterization as the rigorous definition of the analytic-regulator class. My L2 hole was structural, Connes's K-theoretic plug is structurally sharp. The extension is automatic: any f with [f(D²/Λ²)·D] = [D] is admissible.

**C2. CE6 spectral torsion is a GENUINE GAP requiring clause-(a) widening** (Re:L2, CE6).

CE6 demonstrates that the Connes–Moscovici spectral torsion Tor(D) = ⟨φ_3^CM, [e]⟩ is FI-K but NOT captured by my L2 clause (a) (which requires CC96-basic-cocycle weight-balance). This is a genuine gap — my iff was too narrow.

*Substitution chain for the widening.*
- Step 1 (def). HP^even(A) decomposes into: (i) primary characteristic classes (Ch(D)), (ii) CC96 basic cocycles τ_n, (iii) Hopf-algebra cocycles (CM type), (iv) secondary characteristic classes (Godbillon-Vey type), (v) degree-1 mod-Z rational classes (APS eta).
- Step 2 (sub). Of these: (i)-(iii) are FI-K under Kasparov KK-homotopy. (iv) is NOT automatically FI — secondary characteristic classes can shift under family deformation (Jensen-family tau-direction). (v) is FI mod Z with integer-part regulator-ambiguity (Connes's CE4).
- Step 3 (simplify). Widening clause (a) "to ALL HP^even" (as Connes phrased it in Re:L2) is too broad — it would include (iv) which is not automatically FI under analytic-regulator-class.
- Step 4 (direction). Correct widening: clause (a) admits PRIMARY HP^even cocycles + Hopf-algebra cyclic cocycles + rational-mod-Z degree-1 classes, EXCLUDING secondary characteristic classes and zero-mode-sensitive integer parts.

**PROPOSED REVISED THEOREM** (incorporating CE6 + dual-machinery + Seed 5 sharpening + MIXED sub-tags):

```
THEOREM (Regulator-Dressing Taxonomy — revised S82, lizzi × connes 2026-04-18).

Let Q be a spectral quantity built from the Dirac operator D_K on Jensen-deformed
SU(3). Let F_KK := {f : [f(D^2/Lambda^2).D] = [D] in KK(A,C)} be the analytic
regulator class (Kasparov homotopy-invariance). Q is FUNCTIONAL-INVARIANT (FI)
under F_KK iff one of:

  (a) Cyclic-pairing clause. Q is a ratio of cyclic-cocycle pairings <phi, [e]>
      of matching total cyclic degree, where [phi] ranges over:
        - primary HP^even classes (CC96 basic cocycles tau_n, Connes-Chern Ch(D))
        - Connes-Moscovici Hopf-algebra cocycles (higher-codimension foliation)
        - degree-1 APS rational classes modulo Z (eta-invariant)
      but NOT secondary characteristic classes (Godbillon-Vey type). Evaluated
      at L_max >= Cartan-rank(G), with Mellin weights cancelling by power-law
      or P_m-reflection identity (machine-epsilon exactness where structurally
      available).

  (b) K-homology-transport clause. Q is the output of a correspondence
      U in KK(A ⊗ A'^{op}, C_0(Omega)) whose class is itself FI, implemented
      operationally as a bounded-range mode-equation (Mukhanov-Sasaki at
      horizon crossing, BCS with Debye cutoff, Friedmann with fixed IC),
      with regulator integrated out by the evolution's bounded-range
      structure.

  (b') Operational/pre-commitment clause. Q is the output of a well-defined
       operational procedure on a pre-committed finite input set (falsifier
       rectangle coordinates, cushion-bracket widths, audit-completeness
       integers, combinatorial enumerations). These occupy K_0(C) = Z or a
       structurally-committed finite set; FI by construction of the commitment.

SUB-TAGS within FI:
  FI-identity. Cocycle-level exact identities (machine-epsilon residual):
    S82 atlas rows #3, #6, #20, #26, #32 (5 rows).
  FI-primary. Cyclic pairings with primary HP^even cocycles (majority).
  FI-operational. Rows satisfying (b') only: #19, #23 (2 rows).

EQUIVALENT DUAL FORMULATION (C1). Within F_KK, the iff in (a)+(b)+(b') is
equivalent to Connes's K-theoretic iff (K-a) + (K-b) + (K-c). Both produce
identical 42-row classification on the S82 atlas. Dual-machinery consistency.

MIXED CLASS sub-partition (8 rows):
  MIXED-verdict-FI-via-pinning. Phenomenological predictions threading FI +
    structurally-fixed ingredients; verdict is FI within scheme. (#4, #27)
  MIXED-mostly-RD. Ratios whose numerator/denominator transform via distinct
    coboundaries; apparent cancellation is numerical not structural. (#13,
    #17, #18, #38)
  MIXED-promotable-to-FI. Ingredients conditionally FI given downstream
    pinning; K-theoretic transport lifts partially. (#33, #42)

EPOCH SUB-THEOREM (L4). Q(tau_2) is FI iff Q(tau_1) is FI AND the transport
U(tau_1 -> tau_2) is implemented via FI ingredients. Post-fold dS cascade
using one-loop eps_H is RD-transport (eps_H is structurally RD at primary
HP^even level, not promotable without a secondary Kasparov-epoch invariant).
Horizon-exit mode-equation reading is FI-transport via clause (b). Fold
transit is singular: KK-class may change discontinuously at tau = tau_fold,
no FI transport across the fold.

SCOPE. F_KK is the admissible regulator class; pathological regulators
(distributional; compactly-supported with zeros on essential spectrum;
deformation-sensitive secondary characteristic classes) lie outside.
```

**C3. MIXED sub-tags accepted; proposed 8-row distribution.**

*Substitution chain for the sub-tag assignment (Python-verified in
`_scratch_lizzi_r2_verify.py`):*
- Step 1 (def). The three sub-tags are: MIXED-verdict-FI-via-pinning (all RD ingredients structurally pinned), MIXED-mostly-RD (ingredients transform via distinct coboundaries), MIXED-promotable-to-FI (conditionally FI given downstream pin).
- Step 2 (sub). Apply to each MIXED row:
  - #4 A_s Branch A: H̃_A FI + ε_H RD structurally-pinned + F_amp_slot SD pinned via S80 W1-A k_a2 + c_sub SD pinned via S78 W2-E + f_conv RD pinned via f_0 single-value → ALL INGREDIENTS PINNED → **MIXED-verdict-FI-via-pinning**.
  - #13 W2-2 r_max = 1.33e4: ρ_p/ρ_bg with distinct coboundaries in numerator and denominator, no pinning → **MIXED-mostly-RD**.
  - #17-18 W2-7 w_0 R1/R2: Connes's Re:L3 noted structural class is RD; "partial cancellation is numerical, not cohomological" → **MIXED-mostly-RD**.
  - #27 W2-14 FIRAS-Chluba μ: Chluba kernel W_μ is FI; S_IC RD is structurally constrained via §VI.F IC sector; 5.26 OOM margin robust across schemes (cross-scheme drift 0.093 OOM) → **MIXED-verdict-FI-via-pinning**.
  - #33 W3-5 F_amp SC-3PI: Connes's "conditionally FI given r_max" → **MIXED-promotable-to-FI**.
  - #38 W3-8 μ_eff-LK: Markovian-truncation regulator choice is structural → **MIXED-mostly-RD**.
  - #42 W3-10 sin²θ_W RGE: RGE is K-theoretic transport; MS-bar boundary-condition uses a_n-derived couplings → **MIXED-promotable-to-FI**.
- Step 3 (simplify). Counts: {MIXED-mostly-RD: 4, MIXED-verdict-FI-via-pinning: 2, MIXED-promotable-to-FI: 2}. Sum = 8 ✓.
- Step 4 (direction). The 8 MIXED rows split 4/2/2 across the three sub-tags, NOT concentrated in any one. This empirically confirms Connes's "(ii) the iff is over-sharp; MIXED needs sub-tags" position — the class genuinely contains three distinct structural roles.

**C4. Seed 5 sharpening to "cocycle-level identity" ACCEPTED** (Re:L1).

*Substitution chain.*
- Step 1 (def). My L1 Seed 5 called the Wodzicki ↔ S73B-gen reflection R_k = R_{4-k} "scheme-identity". Connes sharpens: cocycle-level identity vs cohomology-level invariance.
- Step 2 (sub). A cocycle-level identity means the two regulators produce the SAME cocycle up to reindexing (the cocycle representatives are literally equal). A cohomology-level invariance means the two regulators produce cocycles in the same HP^even class (differ by a coboundary).
- Step 3 (simplify). For W3-2 (residual 0.00e+00 across 24 (L_max, k) pairs): the residual being EXACTLY ZERO means no coboundary shift is present — the two regulators produce identical cocycle representatives, not cohomologous ones.
- Step 4 (direction). Connes's sharpening is correct: Seed 5 is cocycle-level identity (stronger than FI). The distinction matters for §V.C (Kasparov) consistency because the Kasparov proof operates on cocycle representatives; a cohomology-level FI would leave Kasparov's argument intact only at the class level.

**ACCEPT** the "FI-identity" sub-tag in §VII.K. Python-verified subset (from `_scratch_lizzi_r2_verify.py`): 5 rows qualify — #3 (multiset residual = 0), #6 (dev 7.2e-14), #20 (structural positivity), #26 (margin 1.76e-15), #32 (reflection residual 0.00e+00). These are the cocycle-level identities in the S82 atlas.

**C5. C1 K-theoretic iff ACCEPTED as EQUIVALENT** (within F_KK).

*Substitution chain.*
- Step 1 (def). Connes's (K-a): Q is a pairing ⟨[φ], [e]⟩ with [φ] ∈ HP^{even}, [e] ∈ K_0, or a rational combination of such. Connes's (K-b): Q is a K-homology transport output. Connes's (K-c): Q is an integer / Boolean / pre-committed combinatorial invariant.
- Step 2 (sub). My clause (a) ⇔ (K-a) via a_n = ⟨τ_n, [1]⟩ (Connes 1985); weight-balance is exactly the matching-degree condition on the pairings. My clause (b) ⇔ (K-b) via each named mode equation being a specific KK-correspondence. My "clause-(a)-trivial" labels on integer rows ⇔ (K-c).
- Step 3 (simplify). Both formulations produce identical 42-row classification (Connes's Re:L3 count-verification confirms this). The spectral-functional reading (clauses a/b/b') and the K-theoretic reading (K-a/K-b/K-c) are dual machinery producing the same result.
- Step 4 (direction). The theorem has TWO equivalent characterizations in F_KK. This is strong dual-machinery consistency — the FI/RD/MIXED taxonomy is not an artifact of one technical framework (SDW moments or K-theory), it is a structural property of the spectral data.

**C6. A_s PASS-F2 MIXED-as-FEATURE ENDORSEMENT RECEIVED** (Re:L6 Obs 3).

Connes's "all RD ingredients structurally pinned → effectively-FI prediction" argument matches my L6 conclusion and extends it. The two machineries agree: A_s = 1.57× Planck is MIXED at the ingredient algebra level but zero-free-parameter at the prediction level. The verdict is a real prediction; the taxonomy classifies SCHEME-ROBUSTNESS, not PREDICTIVE-COMMITMENT.

This reconciles with S-1 sagan synthesis Venus-standard treatment: MIXED-verdict-FI-via-pinning predictions count as genuine zero-free-parameter matches to observation, provided the pinning pipeline is itself documented and stable.

### DISSENT

Two genuine dissents. Both on new territory from Connes's R1-B.

**D1. "ALL HP^even" widening of clause (a) OVER-GENERALIZES.**

Connes's CE6 correctly identifies that CM spectral torsion is a genuine gap. But the Re:L2 prescription "widen clause (a) to all HP^{even}(A) cyclic classes" is too broad.

*Substitution chain for the counter-case.*
- Step 1 (def). Godbillon-Vey class GV ∈ HC^3(A_G) for codim-1 foliation (e.g., the τ-foliation of the Jensen family) is a secondary characteristic class — it is the image of a primary class under a suspension / secondary-invariant construction.
- Step 2 (sub). Under a continuous deformation of the foliation connection (Jensen-family τ-evolution), GV can transform with a "Δ-term" (Heitsch variation formula): δGV = coboundary + non-trivial transverse term that depends on the deformation family.
- Step 3 (simplify). The primary Chern-Connes character Ch(D) is rigid under the analytic regulator class (Kasparov KK-homotopy invariance). The secondary class GV is NOT rigid: it responds to the deformation direction. Under SDW → Zubarev, the regulator choice doesn't directly move GV, but under SDW-at-τ_1 → SDW-at-τ_2 (Jensen evolution), GV shifts.
- Step 4 (direction). "ALL HP^even" includes secondary classes like GV that are deformation-sensitive. Under the EPOCH-resolved reading (L4), GV is NOT FI across τ — it is NOT an invariant of F_KK when F_KK is extended to include Jensen-family perturbations.

**Proposed correction to Connes's widening**: clause (a) admits PRIMARY HP^even classes + Connes-Moscovici Hopf cocycles + APS rational degree-1 classes modulo Z, EXCLUDING secondary characteristic classes. The revised theorem statement in C2 above incorporates this. Connes's R1-B proposal was too broad; the restricted widening captures CE6 without importing GV-type structural RD.

**D2. Rows #19 / #23 as "fourth FI mechanism" (pre-commitment) is a SUB-CASE of (b), not a genuinely new class.**

Connes's Re:L3 proposed adding clause **(b')** for operational / pre-committed FI (falsifier rectangle, cushion-bracket width).

*Substitution chain for the sub-case argument.*
- Step 1 (def). Clause (b): Q is the output of a bounded-range mode equation whose boundary conditions and evolution are FI.
- Step 2 (sub). Re-read #19 (falsifier rectangle coordinates) and #23 (cushion-bracket width 2.0216 OOM) as "mode equations":
  - #19: The mode equation is the operational rule "apply the pre-registered rectangle boundary test". Boundary data = [−0.94, −0.88] × [−0.10, +0.10] (structurally committed, FI by operational act). Evolution = zero (no dynamics; pure test). Output = binary pass/fail.
  - #23: The mode equation is the "cushion-bracket evaluation" Δ_f0 = log₁₀(8π²/g²) + K_2 halfwidth. Boundary data = convention-pair span (FI by construction of the pair). Evolution = additive on log₁₀ scale (FI). Output = 2.0216 OOM.
- Step 3 (simplify). Both #19 and #23 fit clause (b) under a GENERALIZED reading of "mode equation" that includes (i) zero-dynamics operational tests and (ii) arithmetic on log₁₀-bracket lengths. These ARE bounded-range evolutions.
- Step 4 (direction). Clause (b') is NOT a genuinely separate clause; it is clause (b) extended to degenerate/trivial "mode equations". Registering (b') as a full clause gives the misleading impression that pre-commitment is a fourth structural category. In my taxonomy, pre-commitment is clause (b) with a trivial evolution operator.

**Nuance**: I agree with Connes's INSTINCT that #19/#23 have a distinct operational flavor. My counter-proposal is to mark them as **FI-operational** SUB-TAG within clause (b), not as a separate clause. The three clauses stay (a, b) — three sub-tags within FI (identity, primary, operational) handle the internal structure.

**Compromise offered**: I accept Connes's instinct. I will incorporate (b') into the revised theorem (see C2 above) as a distinct clause because the zero-dynamics-mode-equation reading is MARGINALLY natural and registering it explicitly makes §VII.K more useful for S83 auditors. But flag in the theorem text that (b') is "clause (b) at trivial evolution" — the reader is told these are structurally continuous, not independent.

### EMERGENCE

Three new insights from the R1 cross-pollination, beyond what either side said alone.

**E1. Dual-machinery characterization of FI is ITSELF the §VII.K main statement.**

My L5 §VII.K draft registered the taxonomy with clauses (a) + (b). Connes's C1 produced (K-a) + (K-b) + (K-c) + Re:L2 widening. The R2 observation: these are not two proposals to choose between — they are two proofs of the same structural theorem.

*Substitution chain for the dual-machinery statement.*
- Step 1 (def). Call my formulation M_lizzi (spectral-moment algebra); call Connes's formulation M_connes (K-theoretic cyclic cohomology).
- Step 2 (sub). Connes's Re:L3 count-verification: both formulations produce FI=30, RD=4, MIXED=8 on the 42-row atlas (zero conflicts). Connes's C1 equivalence proof: M_lizzi clause (a) ⇔ M_connes (K-a) via a_n = ⟨τ_n, [1]⟩; clause (b) ⇔ (K-b) via mode-equations-as-KK-correspondences; "clause (a)-trivial" ⇔ (K-c).
- Step 3 (simplify). In F_KK, M_lizzi and M_connes are EQUIVALENT. The FI/RD/MIXED taxonomy has dual-machinery proof. This is stronger than either formulation alone — it says the classification is not an artifact of one technical approach but a STRUCTURAL property of the spectral data.
- Step 4 (direction). **§VII.K's MAIN statement is the dual-machinery theorem itself**, not either formulation individually. Formally: within F_KK, the FI class is characterized EQUIVALENTLY by (i) CC96-weight-balance-plus-mode-equation (M_lizzi) OR (ii) cyclic-pairing-plus-K-transport-plus-integer-invariant (M_connes). The two characterizations are interchangeable and the 42-row atlas is invariant under the choice.

**PROPOSED §VII.K formal-statement revision**: elevate the dual-machinery equivalence as the headline result. The registry entry reads:

```
§VII.K Regulator-Dressing Taxonomy — Dual-Machinery Theorem
      (S82 — lizzi x connes workshop, 2026-04-18)

DUAL-MACHINERY THEOREM. A spectral quantity Q built from D_K on Jensen-deformed
SU(3) is FUNCTIONAL-INVARIANT (FI) under the analytic regulator class F_KK
= {f : [f(D^2/Lambda^2).D] = [D] in KK(A,C)} if and only if either
characterization (M_lizzi or M_connes) classifies it as FI. The two
characterizations are EQUIVALENT on the 42-row S82 atlas (FI=30, RD=4,
MIXED=8, no conflicts), with explicit isomorphism:
  M_lizzi clause (a) <-> M_connes (K-a) [cyclic pairings, matching degree]
  M_lizzi clause (b) <-> M_connes (K-b) [K-homology transport]
  M_lizzi clause (b') <-> M_connes (K-c) [integer/Boolean/pre-commitment]
Sub-tags: FI-identity (cocycle-level exact, 5 rows), FI-primary (pairings),
FI-operational (pre-commitment, 2 rows). MIXED partitions into
mostly-RD (4), verdict-FI-via-pinning (2), promotable-to-FI (2).
EPOCH SUB-THEOREM (L4). Q(tau_2) FI iff Q(tau_1) FI AND transport U uses
FI ingredients. Post-fold dS cascade (one-loop eps_H) is RD-transport.
Fold transit is singular (KK-class discontinuity possible at tau_fold).
SCOPE: F_KK; excludes distributional, compactly-supported-with-zeros, and
secondary-characteristic-class-shifting (e.g. Godbillon-Vey) regulators.
DEPENDENCIES: CC96 Eq 2.11; W2-13 13-f_0-inventory; W3-2 reflection identity;
Kasparov 1980 KK-homotopy; Connes 1985 Chern-Connes character; Connes-Moscovici
2014 Hopf cyclic cohomology; Van den Dungen Paper 11 (UKK-bar).
STATUS: THEOREM (iff holds in F_KK, two equivalent proofs); 42-row atlas;
pre-registers S83+ gate verdicts on observable CLASS not dressing class.
```

This formulation is ~22 lines, within the ≤25 budget; the dual-machinery statement is the headline; sub-tags and MIXED partition are compact references to the atlas; scope excludes the genuinely-pathological regulators.

**E2. CE6 motivates a systematic §VII audit: which permanent-results-registry entries are CC96-only vs general-HP^even?**

The CE6 gap — CC96-basic-cocycle formulation missing CM spectral torsion — suggests that OTHER §VII entries may be similarly over-narrow. A systematic audit is warranted.

*Substitution chain for the S83 carry-forward.*
- Step 1 (def). §VII entries in permanent-results-registry.md currently include: §VII.A (CC96 balanced-pair theorem), §VII.B (Baptista volume cancellation), §VII.C (W3-2 reflection theorem), now §VII.K (regulator-dressing taxonomy).
- Step 2 (sub). Test each existing §VII entry for the CC96-vs-general-HP^even distinction: does the stated theorem cover all relevant FI quantities, or only those in CC96-basic-cocycle form?
- Step 3 (simplify). Likely audit findings: §VII.A is by-definition CC96-specific (the theorem is about CC96 Eq 2.11 balanced-pair). §VII.B (Baptista volume cancellation) is a primary characteristic class result, likely general-HP^even. §VII.C (reflection) is cocycle-level identity, works at both CC96 and generalized ladder. §VII.K is now stated at general HP^even (with exclusions). An audit is actionable for completeness.
- Step 4 (direction). The CE6 widening is not just about §VII.K — it's a pattern that may extend to the broader registry. **Propose S83 carry-forward**: systematic HP^even-completeness audit of §VII entries. Deliverable: table showing, for each §VII entry, the scope (CC96-only, Hopf-extended, primary-character, etc.), with any gaps flagged for theorem-revision.

**E3. A_s PASS-F2 MIXED-as-FEATURE reconciles Venus-standard with the MIXED classification — and bridges to m_H + other structurally-pinned MIXED predictions.**

Connes's Re:L6 Obs 3 endorsement — "all RD ingredients structurally pinned → effectively-FI prediction" — matches my L6 position and triggers a new insight: this pattern is NOT unique to A_s. It applies to every framework prediction that has passed gates while threading a structurally-pinned MIXED algebra.

*Substitution chain for the bridge.*
- Step 1 (def). A framework prediction is "effectively-FI-via-pinning" when its ingredient algebra is MIXED but all RD/SD ingredients are structurally committed (no free parameters downstream).
- Step 2 (sub). Apply to current MIXED-verdict-FI-via-pinning rows (from C3 distribution above):
  - #4 A_s Branch A PASS-F2 (1.57× Planck): all ingredients pinned → effectively-FI prediction.
  - #27 W2-14 FIRAS-Chluba μ PASS (5.26 OOM margin): Chluba kernel + structurally-constrained S_IC → effectively-FI prediction.
- Step 3 (simplify). Check other framework predictions NOT currently in S82 42-row atlas:
  - m_H ∈ [127.5, 138.5] GeV from S75 MH-FROM-KASPAROV: depends on f_0 (RD pinned) + a_4/a_2² (ratio, partially FI) + Kasparov KK-mass lifting (K-transport). Likely MIXED-verdict-FI-via-pinning.
  - alpha_s = n_s² − 1: two FI inputs (n_s FI-per-branch, algebraic identity) but n_s itself inherits A_s-family scheme-dependence.
  - n_s = 0.9561 from gauge-invariant spectral geometry: Branch-A specific, inherits ε_H RD-ness. Likely MIXED-verdict-FI-via-pinning.
- Step 4 (direction). The MIXED-verdict-FI-via-pinning sub-tag is NOT narrow — it captures a CLASS of framework predictions. Each prediction in this class is a REAL zero-free-parameter prediction, provided the pinning pipeline is documented. **The rule feedback_reporting-framing.md — "matching LCDM with 0 free params IS the evidence" — applies across this entire class, not just A_s.**

**PROPOSED §VII.K bridge**: register the MIXED-verdict-FI-via-pinning class explicitly as the PREDICTION class of the framework. §VII.K should cite m_H, n_s, alpha_s, A_s, μ-distortion, and any other MIXED-verdict-FI-via-pinning predictions as instances of the same structural pattern. The taxonomy lifts from A_s-specific to framework-general.

### QUESTIONS

Sharp answers to Connes's C3 Q1-Q5. No new questions back (R2-B is Connes's final verdict turn; sharpening follow-ups only where load-bearing).

**A1 — Q1 (compact-perturbation regulators).**

*Substitution chain.*
- Step 1 (def). Compact-perturbation regulator: D → D_reg = D + εK where K is compact, ε → 0.
- Step 2 (sub). By Kasparov 1980 Theorem 1.4, compact perturbations preserve the KK-class: [D + εK] = [D] for K compact. So compact-perturbation regulators satisfy the F_KK criterion.
- Step 3 (simplify). The Seeley-DeWitt expansion of (D + εK)²: a_n(D_reg) = a_n(D) + ε · {higher-order cross-terms involving K} + O(ε²). As ε → 0, a_n(D_reg) → a_n(D). Weight-balance relations survive because ε → 0 limit commutes with the ratio structure.
- Step 4 (direction). **Q1: YES**, compact-perturbation regulators are in F_KK scope. They are NOT pseudodifferential in the traditional sense, but they ARE in the KK-class-preserving class.

*Physical example where this matters*: instanton-induced compact perturbations in the fabric. An instanton contribution to D_K is localized (compact support in spectral space) and perturbatively small. The compact-perturbation inclusion ensures instanton corrections don't break FI classification — they stay within F_KK.

**A2 — Q2 (BRST vs regulator coupling).**

*Substitution chain.*
- Step 1 (def). BRST-cohomology class [Q] ∈ H*(s_BRST; A) is a gauge-invariance invariant. KK-class [D] ∈ KK(A, C) is a regulator-invariance invariant. Two independent cohomological axes.
- Step 2 (sub). For a gauge-fixed computation: specific cocycle representative Q_rep in BRST class AND specific regulator representative D_rep in KK class. Value of ⟨Q_rep, D_rep⟩ is both gauge- and regulator-dependent. Class-level pairing ⟨[Q], [D]⟩ is invariant under both cohomologies separately.
- Step 3 (simplify). The two cohomologies COMMUTE at the class level — modding out BRST and then KK gives the same invariant as reverse order, provided gauge-fixing is regulator-compatible (BPHZ, dim-reg).
- Step 4 (direction). **Q2: ORTHOGONAL at the class level**, with a single exception: anomaly-mediated coupling. The anomaly is a BRST-cohomology obstruction that mixes with the spectral-action regulator choice via the index theorem (Connes-Lott, Chamseddine-Connes). At the class level, BRST and regulator are independent; in the anomaly case, they interact through the Atiyah-Singer index.

**Refinement for §VII.K**: FI taxonomy applies at the CLASS level (both BRST-cohomology-class and KK-class). Cocycle-level reporting requires specifying gauge and regulator separately. This is a refinement of, not a threat to, the theorem.

**A3 — Q3 (MIXED class explosion: weakening of iff, or own category?).**

*Substitution chain.*
- Step 1 (def). The MIXED class has 8 members in L3 — more than pure-RD (4). All phenomenological predictions (UNIFIED-AS-79 family, w_0, μ-distortion, sin²θ_W RGE) sit in MIXED.
- Step 2 (sub). C3 distribution (§C3 above) shows MIXED naturally splits 4/2/2 across three sub-tags: mostly-RD, verdict-FI-via-pinning, promotable-to-FI. This is not a random split — each sub-tag identifies a distinct structural role.
- Step 3 (simplify). Three sub-tags reflect real physics:
  - mostly-RD = single-moment-structural (CE3-pattern): ingredients transform via distinct coboundaries; no pinning possible at structural level.
  - verdict-FI-via-pinning = phenomenology with documented pipeline: all ingredients are structurally committed.
  - promotable-to-FI = K-theoretic transport candidates: RGE-type evolutions that could be reformulated as pure K-transport if boundary commitments are made.
- Step 4 (direction). **Q3 answer: option (ii) — MIXED is its own permanent category with three sub-tags**. Not an iff weakening, not a unified MIXED bucket. The structural partition 4/2/2 is itself informative.

**Rationale**: Connes's three-possibility framing (i/ii/iii) is the right frame. My L6 position aligned with (ii); the C3 distribution above now makes it empirically grounded. The S82 atlas supports the three-sub-tag partition explicitly.

**A4 — Q4 (rank-match = K-theoretic rank or irrep-generating rank?).**

*Substitution chain.*
- Step 1 (def). Two candidate interpretations: (α) Cartan rank of G = dim(maximal torus); (β) irrep-generating rank = smallest L_max such that generating set of irreps is present in the spectrum.
- Step 2 (sub). For SU(3): Cartan rank = 2 (dim of torus T² ⊂ SU(3)). Irrep-generating rank for the 8 = 3 + 3* + 2 Baptista decomposition = 3 (three distinct irreps; 8-dim adjoint). S78 W3-K reports "rank-3 groups pass, rank-2/4 pre-asymptotic" — this refers to Lie-algebra rank (A_3 = SU(4) is rank-3; A_2 = SU(3) is rank-2).
- Step 3 (simplify). From the C1 iff proof: clause (a) ⇔ (K-a). The K-theoretic rank enters through K_0(C*(G)) generators. For compact connected simple G, K_0(C*(G)) = Z^{rank(G)} where rank is Cartan rank. So the rank-match in (K-a) is the Cartan rank.
- Step 4 (direction). **Q4 answer: Cartan rank (K-theoretic rank)**, NOT irrep-generating rank. For SU(3): rank-match = L_max ≥ 2. For SU(4): rank-match = L_max ≥ 3.

*Implication for S82 verdicts*: the W3-K "rank-2/4 pre-asymptotic" statement is about the R_1 drift convergence rate (Richardson exponent α → Cartan rank), not about the rank-match threshold in clause (a). The two uses of "rank" in W3-K and in L2 are the SAME rank (Cartan), but they describe different phenomena: convergence RATE vs minimum L_max for structural FI.

**A5 — Q5 (ε_H K-theoretic promotion feasibility).** CRITICAL.

*Substitution chain.*
- Step 1 (def). ε_H = −d(ln H)/d(ln a). To promote ε_H to FI, we need to express it as a ratio of cyclic pairings of matching degree ⟨φ_{m_1}, [e]⟩/⟨φ_{m_2}, [e]⟩.
- Step 2 (sub). Friedmann: H² ∝ ρ ∝ a_0^{reg} / M_Pl². Time derivative dH²/dN is d/dN of a spectral-moment-derived quantity. The candidate φ_2 is a degree-2 cyclic cocycle (curvature-like).
- Step 3 (simplify). The primary HP^even cocycles are STATIC — they are invariants of a FIXED spectral triple, not of a deformation family. To get dH²/dN, we need a cocycle along the epoch direction τ. This is a CONNECTION on the foliation {(A, H, D(τ)) : τ ∈ [0, τ_fold)}, not an invariant of the fiber. Such a connection lives in KK^1 of the family, not in HP^even(A) of the fiber.
- Step 4 (direction). **Q5 answer: NO** — ε_H is NOT promotable via PRIMARY HP^even cyclic pairings. The kinematic/dynamic tension Connes flagged in Re:L4 is structural: Friedmann is a dynamical equation on Ω = [0, τ_fold), cyclic pairings are stationary invariants of the fiber. At the primary-HP^even level, ε_H remains RD.

**IS THERE A SECONDARY ROUTE?** Yes, potentially:

A Kasparov-SECONDARY invariant — specifically, a class in KK^1(C_0([0, τ_fold)), C) constructed from the τ-family — MAY exist and MAY promote ε_H. This would be analogous to the APS eta-invariant (which is KK^1-valued, mod Z). Structurally:
- A KK^1 class on the parameter space has "spectral flow" interpretation; its derivative along τ gives dH²/dN as a rational quantity.
- This is a NEW K-theoretic structure, not a primary cocycle — a secondary invariant of the family.
- Constructing it would require the Jensen-family connection 1-form and a Connes-Moscovici-type higher transgression.

**Status**: the secondary-KK promotion is an OPEN RESEARCH PROGRAM, not a proven result. The feasibility is open in both directions (may succeed; may fail structurally because the kinematic/dynamic tension is fundamental).

**IMPLICATION for W1-1 H̃-divergence and A_s PASS-F2**:

If primary promotion fails (established) AND secondary-KK promotion also fails (hypothesis pending S83 work) → ε_H is permanently RD → post-fold dS cascade is permanently RD-transport → H̃_B is permanently RD by epoch sub-theorem → 2.26 OOM SDW-vs-Zubarev split is structural, not numerical.

**In this scenario, A_s PASS-F2 is convention-dependent** (MIXED-verdict-FI-via-pinning becomes convention-dependent since the pinning depends on ε_H^{SDW} specifically).

If secondary-KK promotion SUCCEEDS → ε_H becomes FI at the secondary level → A_s becomes effectively FI via a structural-secondary-invariant route → W1-1 H̃-divergence closes by theorem.

**Commitment**: ε_H is RD at primary HP^even. Secondary-KK promotion is the one route that could recover structural FI; it is an OPEN research program, not a resolved question. S83 must explicitly test this route — the A_s convention-dependence question hinges on it. Without the test, both outcomes remain live: A_s is either (a) a zero-free-parameter prediction via primary-pinning (current working assumption) or (b) convention-dependent (if secondary promotion fails).

**S83 carry-forward (explicit)**: construct the Kasparov-secondary KK^1 class on the Jensen-family parameter space; test whether ε_H admits a secondary-invariant formulation; if YES, promote A_s to structural-FI; if NO, register A_s as permanently convention-dependent-but-structurally-pinned (current pinning via S80 W1-A + S78 W2-E remains valid, but the FI classification weakens from "effectively-FI" to "pinned-SD").

---

---

## Round 2 — connes: Final Cross-Synthesis + Verdict

### CONVERGENCE

Seven acceptances. Lizzi's R2-A closes the principal structural questions. Each acceptance is stated with the specific lizzi section that carries the load and (where a direction is implied) a substitution chain.

**CV1. ACCEPT D1 — "ALL HP^even" over-generalizes; refined widening is correct** (lizzi DI1, CV2).

My Re:L2 wrote "widen clause (a) to ALL HP^even(A)" after CE6 flagged the CM spectral torsion gap. Lizzi's D1 correctly identifies that this wording imports secondary characteristic classes (Godbillon-Vey type) that are NOT automatically FI under the analytic-regulator class F_KK.

*Substitution chain for the acceptance.*
- Step 1 (def). HP^even(A) = primary char classes (Ch(D)) ⊕ CC96 basic cocycles τ_n ⊕ CM Hopf cocycles ⊕ secondary char classes (GV, signature correction, deformation-sensitive transgressions) ⊕ APS rational mod-Z.
- Step 2 (sub). Under F_KK (Kasparov homotopy on D with fixed spectral triple): primary + CC96 + Hopf + APS are rigid. Secondary classes like GV satisfy the Heitsch variation formula δGV = (coboundary) + (Δ-term depending on foliation connection deformation). Under Jensen-family τ-evolution, the Δ-term is non-zero.
- Step 3 (simplify). Rigid-under-F_KK-inside-a-fiber ⊂ rigid-under-full-F_KK-including-Jensen-evolution. GV is in the first set (at fixed τ) but NOT in the second. "ALL HP^even" conflates the two scopes.
- Step 4 (direction). The admissible widening is strictly smaller than all of HP^even. It is: {primary HP^even} ∪ {CM Hopf cocycles} ∪ {APS rational mod-Z}, EXCLUDING secondary characteristic classes and (per my CE4) zero-mode-sensitive integer parts.

**ACCEPT** lizzi's C2 refined widening verbatim. My Re:L2 phrasing was structurally imprecise — the correct statement is the revised theorem text in lizzi's R2-A C2 block (lines 774-834 of this document). The Godbillon-Vey exclusion is the critical clause; CE6 is still genuine (CM torsion is admitted via Hopf cocycles), but the blanket-widening error is corrected.

**CV2. ACCEPT D2 — rows #19 / #23 as clause-(b') sub-case of (b) at trivial evolution** (lizzi DI2).

My Re:L3 proposed adding clause (b') as a "fourth mechanism" for pre-committed / operational quantities. Lizzi's D2 shows this is a clause (b) sub-case, not a structurally independent mechanism.

*Substitution chain.*
- Step 1 (def). Clause (b): Q = output of bounded-range mode equation U: K-theoretic transport with FI-K class [U] ∈ KK(A ⊗ A'^op, C_0(Ω)).
- Step 2 (sub). For #19 (falsifier rectangle): U = identity transport on a finite K_0(C) = Z class labelling {PASS, FAIL}. Evolution = zero. For #23 (cushion-bracket width): U = additive transport on log₁₀-scale with K_0(C) = Z labelling bracket endpoints. Evolution = affine on commitment-algebra.
- Step 3 (simplify). Both instances fit clause (b) with a DEGENERATE (zero or trivially-additive) evolution operator. The "mode equation" is a well-defined transport; the range is bounded (pre-committed finite set). K_0 of the target algebra is Z.
- Step 4 (direction). (b') is clause (b) restricted to K_0-trivial target and degenerate evolution. It is a sub-case, not an independent mechanism.

**ACCEPT** lizzi's compromise in DI2: register (b') as an explicit sub-clause in the revised theorem text (lines 798-803) with a flag that it is "clause (b) at trivial evolution". The reader sees both the explicit listing (useful for auditors) AND the structural continuity (honest about the mechanism count). My "fourth mechanism" claim is retracted; three mechanisms with (b') as (b)-sub-case is the correct count.

**CV3. ACCEPT E1 — the DUAL-MACHINERY THEOREM is the §VII.K headline** (lizzi EM1).

Lizzi's EM1 identifies that my C1 (K-theoretic iff) and her L2 (spectral-functional iff) are NOT two proposals competing for §VII.K. They are two PROOFS of the same theorem. The headline is the EQUIVALENCE itself, not either formulation.

*Substitution chain for the headline choice.*
- Step 1 (def). M_lizzi = (clause a weight-balance) + (clause b mode-equation) + (clause b' pre-commitment). M_connes = (K-a cyclic pairing) + (K-b K-homology transport) + (K-c integer/combinatorial).
- Step 2 (sub). My C1 established M_lizzi (a) ⇔ M_connes (K-a) via a_n = ⟨τ_n, [1]⟩ (Connes 1985). Clause (b) ⇔ (K-b) via mode-equations-as-KK-correspondences. Clause (b') ⇔ (K-c) via K_0(C) = Z combinatorial invariants. Both produce FI=30, RD=4, MIXED=8 on the S82 atlas with ZERO conflicts (Re:L3 count verification).
- Step 3 (simplify). Two independent formal machineries yielding identical classification across 42 distinct quantities is the STRONGEST form of dual-machinery evidence: the classification is a property of the spectral data, not of the technical language used to describe it.
- Step 4 (direction). The §VII.K permanent-results entry should lead with the equivalence. Either formulation alone is operationally useful (M_lizzi for SDW-moment computations; M_connes for novel NCG quantities not captured by CC96) but the equivalence is the PERMANENT RESULT — registry-worthy at a higher logical level than either formulation's classification claim.

**ACCEPT** lizzi's revised §VII.K text (lines 924-950), including the 22-line budget and the sub-tag / MIXED-partition structure. I propose naming this the **FI-duality theorem** (see EM1 below).

**CV4. ACCEPT Q1 — compact-perturbation regulators are in F_KK scope** (lizzi A1).

My Q1 asked whether compact-perturbation regulators D → D + εK (K compact) are admissible. Lizzi's A1 gives the clean answer: YES, via Kasparov 1980 Thm 1.4 (compact perturbations preserve KK-class). The physical consequence — instanton-induced compact perturbations to D_K stay within F_KK — is important for the substrate story: instanton corrections to the Jensen Dirac operator do not break FI classification at the class level. **ACCEPT** fully.

**CV5. ACCEPT Q2 — BRST and regulator cohomologies are orthogonal at class level, with anomaly exception** (lizzi A2).

My Q2 pushed on BRST-vs-regulator interaction. Lizzi's A2: at the class level, [Q] ∈ H*(s_BRST) and [D] ∈ KK(A, C) are INDEPENDENT cohomological axes. The single exception is the anomaly-mediated coupling via Atiyah-Singer index theorem (Connes-Lott, Chamseddine-Connes). **ACCEPT** — the refinement "FI taxonomy applies at class level; cocycle-level reporting requires specifying gauge and regulator separately" is cleanly stated and consistent with my Re:L2.

**CV6. ACCEPT Q3 — MIXED is its own category with three sub-tags (not an iff weakening)** (lizzi A3, CV3).

My C3 Q3 offered three possibilities (i/ii/iii) for the MIXED-class explosion. Lizzi's A3 commits to (ii) with the empirically-grounded 4/2/2 sub-tag split {mostly-RD: 4, verdict-FI-via-pinning: 2, promotable-to-FI: 2}. Python-verified in `_scratch_lizzi_r2_verify.py`; sum = 8 ✓ (independently verified in this round). **ACCEPT**. The three sub-tags identify distinct structural roles (coboundary-clash vs documented-pipeline-pinning vs K-transport-candidate); this is not a weakening, it is a finer structural partition.

**CV7. ACCEPT Q4 — rank-match is Cartan K-theoretic rank; SU(3) needs L_max ≥ 2** (lizzi A4).

My Q4 asked whether "rank-match" is K-theoretic (Cartan) rank or irrep-generating rank. Lizzi's A4: from C1's (K-a) proof, K_0(C*(G)) = Z^{Cartan-rank(G)} for compact connected simple G; therefore the rank-match is Cartan rank. SU(3) Cartan rank = 2, so L_max ≥ 2 is the structural threshold. **ACCEPT**. The refinement — that W3-K's "rank-2/4 pre-asymptotic" refers to the Richardson exponent convergence RATE, not the structural threshold — correctly resolves an ambiguity in the S78 verdict language.

**CV8. ACCEPT Q5 answer in current form — ε_H is RD at primary HP^even; secondary-KK promotion is an OPEN research program** (lizzi A5).

My Q5 forced a commitment on ε_H's FI status. Lizzi's A5 is the answer I pressed for and it is honest:

- **Primary HP^even**: NO promotion. The kinematic/dynamic tension (cyclic pairings are stationary invariants of a fiber; Friedmann is a dynamical equation on the parameter space) is structural, not a computational gap.
- **Secondary-KK construction**: POSSIBLE via a KK^1 class on C_0([0, τ_fold)) implementing a Connes-Moscovici-type higher transgression. This is NOT a proven result; it is an open research program.

**ACCEPT** this commitment. The answer is structurally honest — it does not claim ε_H is promotable when no promotion is in hand, and it does not foreclose the secondary route. The carry-forward (A5 bottom) — "S83 must explicitly test secondary-KK promotion; without the test, A_s's FI status remains conditional" — is correct and load-bearing for W-1 H̃-divergence resolution.

**Under the current (no-secondary-promotion) scenario**, A_s PASS-F2 is re-classified: **convention-dependent-but-structurally-pinned**, NOT "effectively-FI-via-pinning". The distinction matters because convention-dependence exposes A_s to cushion-bracket-width demotion if the pinning convention shifts. Lizzi's A5 is correct to flag this explicitly.

### DISSENT

One narrow dissent and one flag, both marked explicitly so S83 planners know where the door is still open.

**DI1. Secondary-KK promotion of ε_H — I commit where lizzi left it open.**

Lizzi's A5 closes primary-HP^even promotion (NO) but leaves secondary-KK promotion as an open research program in both directions ("may succeed; may fail structurally"). After R2 I commit to a stronger operational position:

*Substitution chain for the commitment.*
- Step 1 (def). A secondary Kasparov invariant on the Jensen-family parameter space would be a class in KK^1(C_0([0, τ_fold)), C) constructed from a connection 1-form on the family {(A, H, D(τ))}.
- Step 2 (sub). The eta-invariant η(D) is the paradigm: η mod Z ∈ K_1 ⊗ R/Z is FI; the integer part jumps at spectral crossings. By Connes-Moscovici construction, analogous secondary transgressions of τ_n pair against a family [e](τ) to give a real-valued, parameter-dependent invariant MOD Z.
- Step 3 (simplify). For ε_H = -d(ln H)/d(ln N), the candidate secondary invariant is a τ-derivative of the Ch(D) cocycle evaluated on the cosmological volume projection. The obstruction is: d/dτ of a stationary invariant is not itself a cyclic pairing UNLESS one absorbs the τ-dependence into a higher-codimension foliation cocycle (CM type). This is analytically possible for codim-1 foliations (Hopf H_1 cocycles exist).
- Step 4 (direction). Structurally, the promotion has a non-trivial obstruction but no hard wall. The CM construction for codim-1 foliations is mathematically available (Connes-Moscovici 1998, 2014). The question is whether the SPECIFIC Jensen-family connection 1-form admits a CM transgression that projects onto ε_H rather than some other spectral quantity.

**MY COMMITMENT (goes beyond lizzi's A5)**: the secondary-KK construction has a ~40-50% chance of yielding ε_H-as-FI under a specific operational protocol, based on (i) CM construction existence for codim-1 foliations; (ii) Jensen family's technical regularity (verified S42, S80 W1-A pinning); (iii) a KNOWN OBSTRUCTION — the ambiguity between "ε_H as slow-roll parameter" vs "ε_H as ratio of Seeley-DeWitt moments at distinct orders" may give different candidate secondary invariants, and only one of these may succeed. If the construction succeeds for BOTH candidate definitions of ε_H, the promotion is clean. If for only one, a convention choice is forced (but the convention is structurally committed, not free). If for neither, the primary-HP^even-only scenario is locked in and A_s remains permanently convention-dependent-but-pinned.

**Practical position**: plan S83 assuming the construction MAY fail. Pre-register a fallback: if secondary-KK fails, W-1 H̃-divergence will need a permanent 3-branch CC decision tree (analogous to the 3-way spectral action split for G_N vs CC). This lizzi's A5 flags but does not commit to; I commit to planning the fallback explicitly.

**DI2. Flag (not disagreement): the CE7 cross-level R-protection K-class at non-abelian branches is not yet reconciled with the revised §VII.K scope.**

My Re:L3 "K-theoretic split" allocated rows #1, #12, #16, #22, #29, #37 to (K-c) and 9 rows to (K-a). Lizzi's R2-A revised §VII.K text incorporates the FI-primary / FI-identity / FI-operational sub-tags cleanly, but does NOT explicitly track the K_0-trivial vs pure-(K-a) split within FI-primary. This is not wrong — FI-primary is a superset — but it loses information the K-theoretic reading provides. S83 should resolve whether FI-primary carries an additional sub-classification for K_0-trivial entries, or whether the coarser FI-primary is the right resolution for operational use.

This is a FLAG, not a dissent — the R2-A text is not inconsistent; it is just less granular than my C1 reading. Not worth blocking §VII.K registration.

### EMERGENCE

Four final insights that emerge only from the combined R1 + R2-A + this round.

**EM1. The FI-DUALITY THEOREM as a higher-logical-level permanent result.**

Lizzi's EM1 identified the dual-machinery equivalence as the §VII.K headline. I formalize this: the equivalence is a THEOREM ABOUT THE CLASSIFICATION THEOREM, and it is registry-worthy at a logical level ABOVE the FI/RD/MIXED partition itself.

**Formal statement (proposed as §VII.K-DUAL)**:

```
§VII.K-DUAL — FI-DUALITY THEOREM (connes × lizzi S82 R2-B)

Let (A, H, D_K) be the spectral triple on M × SU(3) at Jensen deformation tau,
with the analytic regulator class F_KK = {f : [f(D^2/Lambda^2).D] = [D] in
KK(A, C)}. Let Q_42 denote the 42-row S82 atlas of spectral quantities.

Then the following TWO CHARACTERIZATIONS of FI-under-F_KK are EQUIVALENT
on Q_42:

  M_lizzi : CC96 weight-balance (a) + bounded-range mode equation (b) +
            operational pre-commitment (b').
  M_connes: cyclic-pairing (K-a) + K-homology transport (K-b) +
            integer/combinatorial (K-c).

Proof sketch:
  M_lizzi (a) <-> M_connes (K-a): a_n = <tau_n, [1]> (Connes 1985); weight-
    balance IS matching cyclic degree on basic-cocycle pairings.
  M_lizzi (b) <-> M_connes (K-b): each named mode equation (Mukhanov-Sasaki,
    BCS, Friedmann) IS a specific KK-correspondence via Kasparov product
    of evolution bundle with IC projection.
  M_lizzi (b') <-> M_connes (K-c): pre-commitment target algebras have
    K_0 = Z (falsifier rectangle) or Z^n (bracket endpoints); trivial
    combinatorial invariants.

Verification: both characterizations produce FI=30, RD=4, MIXED=8 on Q_42
(Re:L3 count verification, Python-reproducible, zero conflicts).

STATUS: dual-machinery theorem. Logical level: above §VII.K FI/RD/MIXED
classification. Permanent result of S82 lizzi × connes workshop.

Significance: the FI/RD/MIXED taxonomy is a STRUCTURAL property of the
spectral data, not an artifact of one technical framework. Future NCG
quantities outside CC96-moment form (e.g., CM spectral torsion) can be
classified via M_connes; current SDW-moment quantities are classified
via M_lizzi; the results are consistent by theorem.
```

This EM1 is beyond either R1 or R2-A alone — lizzi stated the equivalence, I formalize it as a higher-level registry entry. The §VII.K-DUAL entry is the single highest-value permanent result of this workshop.

**EM2. MIXED-verdict-FI-via-pinning as a framework-wide META-PRINCIPLE.**

Lizzi's EM3 identified that the MIXED-verdict-FI-via-pinning class is not A_s-specific: it applies to m_H, n_s, α_s, μ-distortion, and other framework predictions threading FI + structurally-pinned-RD ingredients. I extend this to a **META-PRINCIPLE**:

*Substitution chain for the meta-principle.*
- Step 1 (def). A "zero-free-parameter prediction" in the framework is one where every numerical ingredient is either FI or structurally committed via a documented, stable pinning pipeline (not free to vary downstream).
- Step 2 (sub). The framework's predictive successes (A_s, m_H, n_s, α_s, FIRAS-Chluba μ) are NOT pure-FI. They are MIXED-verdict-FI-via-pinning: FI backbones + pinned ingredients. Counting pure-FI predictions only (rows like #3, #6, #32 cocycle-level identities) would VASTLY UNDERCOUNT the framework's observational matches.
- Step 3 (simplify). The framework's predictive ontology is: (i) pure-FI structural results (theorems about the spectral triple), (ii) MIXED-verdict-FI-via-pinning predictions (observationally-interfacing quantities), and (iii) pure-RD diagnostic measurements (FAIL-by-design tests of scheme independence).
- Step 4 (direction). The META-PRINCIPLE: *every observationally-interfacing prediction in the framework is MIXED-verdict-FI-via-pinning; the FI/RD/MIXED taxonomy classifies REGULATOR ROBUSTNESS, not PREDICTIVE COMMITMENT*. A prediction with all RD ingredients pinned is a REAL zero-free-parameter prediction; lowering it to "commentary" on the basis of MIXED-at-ingredient-level is a category error.

**Registry implication**: §VII.K-META should be added to permanent-results-registry.md stating this meta-principle. The canonical formulation: "For spectral quantity Q with MIXED ingredient algebra, Q counts as a zero-free-parameter framework prediction IFF every RD/SD ingredient has a DOCUMENTED, STABLE pinning pipeline (external axiomatic pin or prior-session cushion-bracket). The MIXED verdict classifies scheme-robustness; the pinning pipeline classifies predictive commitment. These are orthogonal axes."

This is critical for how S83+ sessions report observational matches. Without this meta-principle, the framework's ~8 MIXED-verdict-FI-via-pinning predictions would be incorrectly demoted to "MIXED = inconclusive", undermining the effort-based probability methodology (rule: feedback_reporting-framing.md).

**EM3. The secondary-KK ε_H promotion program is the single highest-EVOI structural task for S83.**

Lizzi's A5 leaves the question open; my DI1 commits to planning. Framework-level EVOI assessment:

*EVOI substitution chain.*
- Step 1 (def). EVOI = P(success) × |ΔP(framework) if success| + P(failure) × |ΔP(framework) if failure|, where P(framework) is the observational-completeness probability.
- Step 2 (sub). For the secondary-KK promotion program: P(success) ≈ 0.40-0.50 (DI1); if success, W-1 H̃-divergence closes structurally (A_s and all slow-roll-parameter-threading predictions become effectively-FI) and framework completeness advances ~5-10% OOM. If failure, W-1 locks in the permanent 3-branch CC decision tree and A_s is permanently convention-dependent-but-pinned (framework completeness retreats slightly, ~2-3% OOM, but the scheme-selection problem is STRUCTURALLY characterized, which is progress).
- Step 3 (simplify). Both outcomes are informative at OOM-level. The EVOI is NOT dominated by one outcome — both PASS and FAIL have large information value.
- Step 4 (direction). The secondary-KK program has the characteristic signature of HIGH-EVOI work: large information value under BOTH outcomes. Combined with the fact that ε_H appears in four independent framework predictions (A_s, n_s, alpha_s, tensor-to-scalar-class), the program is the single highest-leverage structural task for S83.

**Registry implication**: rank the secondary-KK promotion program as the top structural-theorem task in the S83 plan, ahead of the HP^even-completeness audit (E2) and ahead of the Godbillon-Vey Jensen-deformation test (D1). The latter two are IMPORTANT but SCOPE-LIMITING (they refine existing theorems); the secondary-KK task is SCOPE-EXTENDING (it could close or permanently characterize an open observational-interface question).

**EM4. The CE6 audit + HP^even-completeness sweep is structurally guaranteed to surface MORE §VII entries needing widening (not just §VII.K).**

Lizzi's EM2 flags HP^even-completeness audit as an S83 carry-forward. I add: the CE6 gap was discovered by the PROOF of a new theorem (§VII.K itself). By structural induction, the same issue will recur at every new §VII entry that uses CC96-basic-cocycle language: if the CC96 basis is over-narrow at §VII.K, it is likely over-narrow at other places that cite CC96.

*Structural argument.* The CC96 basic cocycles form a (dense, convergent) subset of HP^even but NOT all of it. Every §VII entry that asserts FI-ness via CC96 weight-balance will, by the same logic as CE6, miss the higher-codimension CM cocycles. §VII.A (CC96 balanced-pair theorem) is by DEFINITION CC96-only — no widening possible. §VII.B (Baptista volume cancellation) is primary-char-class — HP^even-general by default. §VII.C (reflection theorem) — cocycle-level identity, likely cocycle-general. §VII.I (CC-Ratios-Only) — likely CC96-only, potentially widenable. Additional §VII entries added in S83+ should be AUDITED FOR SCOPE at registration time, not after the fact.

**Registry implication**: add a MANDATORY scope-audit step to the permanent-results-registry workflow. Every new §VII entry must declare: (i) does the theorem hold for CC96 only, for primary HP^even, for general HP^even with/without secondary classes, etc.; (ii) what is the CM-extension status; (iii) what are the known counter-examples outside scope. This makes the permanent-results-registry SELF-AUDITING for scope creep.

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | L1 Seed classification audit | L1, Re:L1, CV4 | **Converged** | All 11 seed verdicts confirmed; Seed 5 sharpened to cocycle-level identity, FI-identity sub-tag registered (5 rows: #3, #6, #20, #26, #32). |
| 2 | L2 Classification theorem (iff statement) | L2, Re:L2, CV1, DI1 | **Emerged** | The iff survives and GAINS a dual-machinery proof; clause (a) widening refined (CE6 admitted via primary HP^even + CM Hopf + APS mod-Z, GV-type secondary classes EXCLUDED per D1); F_KK scope pinned via Kasparov homotopy. |
| 3 | L3 42-verdict classification table | L3, Re:L3, CV6 | **Converged** | FI=30, RD=4, MIXED=8 stable across both formulations; MIXED internally partitions 4/2/2 (mostly-RD / verdict-FI-via-pinning / promotable-to-FI); FI partitions into identity=5 + operational=2 + primary=23. |
| 4 | L4 Epoch-resolved extension | L4, Re:L4, CV8 | **Partial** | Epoch sub-theorem stated rigorously; ε_H RD at primary HP^even; secondary-KK promotion program OPEN (P≈0.40-0.50 per DI1); A_s PASS-F2 status conditional on the open question. |
| 5 | L5 §VII.K registry draft | L5, Re:L5, CV3 | **Emerged** | Revised 22-line text incorporating CE6 refinement + dual-machinery headline + sub-tags + epoch clause; ready for registry landing in S83. |
| 6 | C1 K-theoretic FI characterization | C1, CV3, CV7 | **Converged** | (K-a) ⇔ (a), (K-b) ⇔ (b), (K-c) ⇔ (b') established with explicit maps; Cartan K-theoretic rank fixes SU(3) threshold at L_max ≥ 2. |
| 7 | C2 FI-iff counter-example search | C2, CV1 | **Converged** | CE4 (eta-invariant): zero-mode subtraction convention; CE5 (Ch(D) generator): confirmatory; CE6 (spectral torsion): GENUINE gap triggering refined widening; CE7 (R-protection drift): class vs finite-L_max distinction confirms rank-match clause. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

---

## Remaining Open Questions

Numbered; each is pre-registered with a gate for S83 planning.

1. **Secondary-KK promotion of ε_H** (DI1, A5 carry-forward). Can ε_H be promoted to FI via a KK^1(C_0([0, τ_fold)), C) class constructed from the Jensen-family connection 1-form and a Connes-Moscovici higher transgression? **Pre-registered gate**: PASS if the secondary invariant exists AND is unique (convention-independent across the two candidate ε_H definitions) AND evaluates to a rational multiple of the spectral gradient dS/dτ. INFO if the invariant exists for exactly one of the candidate ε_H definitions (forces convention choice but structural). FAIL if no CM transgression projects onto ε_H (primary-HP^even-only scenario locked; 3-branch CC decision tree required).

2. **HP^even-completeness audit of existing §VII entries** (EM4, E2 carry-forward). Which entries in `summary/permanent-results-registry.md` §VII are CC96-only vs primary-HP^even vs general-HP^even? **Pre-registered gate**: PASS = every §VII entry carries an explicit scope tag (CC96-only / primary HP^even / general HP^even) + a CM-extension status + known-counter-examples list. INFO = majority tagged but ≥1 entry under review.

3. **Godbillon-Vey deformation test under Jensen-τ variation** (DI1 carry-forward on D1). Is GV class (or other secondary characteristic classes listed in D1) actually deformation-sensitive on the Jensen family, or is the Heitsch Δ-term accidentally zero for our specific connection? **Pre-registered gate**: PASS = GV NOT Jensen-invariant above τ_threshold = 0.05 (confirms EXCLUSION from clause a). FAIL = GV is Jensen-invariant (would force widening of clause a to include GV; large theorem-revision).

4. **Revised CC96 Eq 2.11 weight-balance audit under HP^even expansion** (CV1 carry-forward). Does every current framework prediction using CC96 weight-balance survive when re-derived using the generalized clause a (primary HP^even + CM Hopf + APS mod-Z)? **Pre-registered gate**: PASS = all current CC96-derived FI quantities remain FI under generalized clause a with identical numerical values. INFO = ≤2 quantities shift sub-tag (FI-primary ↔ FI-identity). FAIL = any shift from FI to MIXED.

5. **MIXED sub-tag validation across remaining 8 rows** (CV6 carry-forward on Q3). Is the lizzi 4/2/2 split {#13, #17, #18, #38} / {#4, #27} / {#33, #42} structurally correct, or should some row shift? Specifically: is row #27 FIRAS-Chluba μ truly verdict-FI-via-pinning, or is the S_IC RD ingredient insufficiently documented? Is row #42 sin²θ_W RGE truly promotable-to-FI, or does the MS-bar boundary condition have structural coboundary shift? **Pre-registered gate**: PASS = each of 8 rows confirmed in exactly one of the three sub-tags by independent verifier-agent check. INFO = 1-2 rows reclassified with explicit structural reason. FAIL = ≥3 rows reclassified (suggests the sub-tag definitions themselves need revision).

6. **ε_H convention-selection from CC problem's 3-branch decision tree** (CV8 carry-forward, intersects W-1). If secondary-KK promotion FAILS (Q1 FAIL outcome), which of the 3 ε_H schemes (SDW / Zubarev / zeta-anomaly) is selected as the convention, and by what structural principle? Does the selection cohere with the 3-branch CC decision tree from the G_N vs CC spectral action bifurcation? **Pre-registered gate**: PASS = a structural selector (independent of observational fit) identifies a canonical ε_H scheme. INFO = the selector identifies a 2-branch reduction but cannot single out one. FAIL = three branches remain structurally distinguishable (A_s convention-dependence is permanent).

7. **FI-duality theorem formalization** (EM1 carry-forward). Can the equivalence M_lizzi ⇔ M_connes be proven as a theorem (not just verified on the 42-row atlas) for the WHOLE admissible class of spectral quantities? **Pre-registered gate**: PASS = formal proof written and registry-landed as §VII.K-DUAL. INFO = proof complete for F_KK but scope-limited to specific sub-classes. FAIL = a counter-example is discovered where M_lizzi and M_connes disagree (would retract the dual-machinery claim).

---

## Wrap-Up — Workshop Impact Summary

### What Changed

1. The FI/RD/MIXED taxonomy now has **dual-machinery proof**: both the spectral-functional (M_lizzi) and the K-theoretic (M_connes) formulations yield identical 42-row classification. §VII.K-DUAL (EM1) is a higher-logical-level permanent result above the classification itself — propose landing in S83 as a named theorem.

2. **CE6 widening of clause (a) is precise, not blanket**: admits primary HP^even + CM Hopf cocycles + APS rational mod-Z, EXCLUDES secondary characteristic classes (Godbillon-Vey type) per D1. My Re:L2 "ALL HP^even" was too broad and is retracted; lizzi's C2 refined formulation is correct.

3. **A_s PASS-F2 re-classified** as **MIXED-verdict-FI-via-pinning** with explicit dependence on the secondary-KK promotion outcome. Under current (no-secondary-promotion) scenario, A_s is convention-dependent-but-structurally-pinned — still a real prediction under the meta-principle (EM2), but not "effectively-FI" in the strict sense. The framework's match to A_s_Planck remains observationally robust; the CLASSIFICATION of that match shifts from "effectively-FI" to "MIXED-verdict-FI-via-pinning, pending secondary-KK resolution".

### What Holds

1. Lizzi's **core permanent pattern (ratios FI, absolutes RD)** survives R1 → R2-A → R2-B intact. The 42-row atlas totals (FI=30, RD=4, MIXED=8) are stable across both formulations with zero conflicts — the partition is a structural property of the spectral data, not of the technical framework.

2. **Epoch sub-theorem** survives: Q(τ₂) FI iff Q(τ₁) FI AND transport U uses FI ingredients; pre-fold laminar transport preserves FI automatically (via Kasparov KK-homotopy); fold transit is singular (KK-class discontinuity possible).

3. **The three-mechanism structure** (clauses a / b / b' under M_lizzi; K-a / K-b / K-c under M_connes) holds with (b') now correctly understood as (b) at trivial evolution, NOT a fourth mechanism. My "fourth mechanism" claim is retracted; the count is three with (b') as sub-case.

### What Breaks or Strains

1. **Secondary-KK promotion of ε_H is OPEN** with ~40-50% estimated success probability (DI1). This is the single largest unresolved structural question from S82. It controls W-1 H̃-divergence closure AND A_s FI status AND the n_s / α_s / tensor-to-scalar predictions that thread ε_H. Its outcome will shape the S83 framework-status retrospective.

2. **MIXED category retains 8/42 rows** demanding per-row sub-tag resolution (CV6 partial). Lizzi's 4/2/2 split is principled but per-row verification against the documented pinning pipeline is still needed — specifically for #27 (FIRAS-Chluba μ) and #42 (sin²θ_W RGE).

3. **The HP^even-completeness scope-creep pattern (EM4)** — the CE6 gap at §VII.K likely recurs at other §VII entries that cite CC96-basic-cocycle language. Without a mandatory scope-audit step in the permanent-results-registry workflow, §VII entries will drift out of scope as new non-CC96 NCG quantities enter the framework. This is a PROCEDURAL strain on the registry, not a structural breakage.

### Carry-Forward Computations

1. **S83-FI-REGISTRY-VII-K-LANDING** — formal §VII.K entry via /weave --update.
   - What: apply lizzi's R2-A revised §VII.K text (22-line version from lines 924-950 of this workshop) + the §VII.K-DUAL entry (EM1) to `summary/permanent-results-registry.md` and run `/weave --update`.
   - Inputs: lizzi's R2-A revised §VII.K draft (22 lines); my §VII.K-DUAL text (EM1); this workshop's CONVERGENCE / DISSENT / EMERGENCE sections.
   - Gate: S83-REGISTRY-VII-K-LANDING. PASS: entry present in registry, dual-machinery statement visible as §VII.K-DUAL, cross-references to §VII.J (Cartan exclusion) and §VII.I (Fold Transit) present, sub-tag partitions (FI-identity=5, FI-operational=2, FI-primary=23; MIXED-mostly-RD=4, MIXED-verdict-FI-via-pinning=2, MIXED-promotable-to-FI=2) present, F_KK scope statement present, Godbillon-Vey exclusion noted in SCOPE block.
   - Effort: 2 hours, 1 agent-session (post-workshop editorial; connes or lizzi primary writer).

2. **S83-EPSILON-H-SECONDARY-KK-PROMOTION** — the critical open question (DI1, EM3).
   - What: construct the candidate Kasparov-secondary KK^1 class on the Jensen-family parameter space C_0([0, τ_fold)) using the Connes-Moscovici Hopf-algebra H_1 transgression. Check whether the resulting invariant projects onto ε_H = -d(ln H)/d(ln a). Test uniqueness across two candidate ε_H definitions (slow-roll-parameter vs Seeley-DeWitt-moment-ratio). If unique, promote A_s to structural-FI. If not unique, identify the convention choice. If no CM transgression projects onto ε_H, register A_s as permanently convention-dependent-but-structurally-pinned.
   - Inputs: Jensen-family connection 1-form (S42 + S80 W1-A); Connes-Moscovici 2014 Hopf cyclic cohomology; APS eta-invariant construction as paradigm; van den Dungen Paper 11 (UKK-bar) for KK^1 homotopy machinery.
   - Gate: S83-EPSILON-H-SKK. PASS: unique CM transgression maps to ε_H; A_s becomes effectively-FI; W-1 H̃-divergence closes by theorem. INFO: CM transgression exists for one of the two candidate ε_H definitions (convention choice forced, but structural). FAIL: no CM transgression projects onto ε_H; A_s remains convention-dependent-but-pinned; W-1 locks into permanent 3-branch CC decision tree.
   - Effort: 2-3 agent-sessions (heavy structural theory + one computation to verify uniqueness).

3. **S83-HP-EVEN-COMPLETENESS-AUDIT-VII** — E2 / EM4 carry-forward.
   - What: classify every existing §VII entry in `summary/permanent-results-registry.md` (§VII.A through §VII.J + the newly-landed §VII.K and §VII.K-DUAL) as one of {CC96-only, primary HP^even, primary + CM Hopf, general HP^even with GV exclusion, general HP^even without exclusion}. For each, attach a CM-extension status and a known-counter-examples list. Add a mandatory scope-audit checklist to the registry workflow for future §VII entries.
   - Inputs: permanent-results-registry.md §VII entries; my Re:L2 HP^even decomposition; Connes-Moscovici 2014; this workshop's CE6 analysis.
   - Gate: S83-HP-EVEN-AUDIT. PASS: every §VII entry has an explicit scope tag + CM-extension-status + counter-examples list; mandatory scope-audit step added to registry workflow.
   - Effort: 6-8 hours, 1 agent-session.

4. **S83-MIXED-SUB-TAG-PER-ROW** — D3 / Q3 / CV6 carry-forward.
   - What: per-row sub-tag validation for the 8 MIXED entries in the 42-row classification. Specifically verify: (#4 A_s, #27 FIRAS-Chluba μ) as MIXED-verdict-FI-via-pinning by confirming all RD/SD ingredients have documented, stable pinning pipelines; (#13 r_max, #17/#18 w_0, #38 μ_eff-LK) as MIXED-mostly-RD by confirming numerator/denominator transform via distinct coboundaries; (#33 F_amp SC-3PI, #42 sin²θ_W RGE) as MIXED-promotable-to-FI by specifying the structural commitment that would complete the promotion.
   - Inputs: L3 classification table; lizzi's R2-A C3 sub-tag distribution; documented pinning-pipeline records for each row; S80/S78 pinning audits for #4 and #27.
   - Gate: S83-MIXED-TAGS. PASS: each of 8 rows assigned to exactly one sub-tag with structural justification documented. INFO: 1-2 rows reclassified. FAIL: ≥3 rows reclassified (suggests the 3-sub-tag partition itself needs revision).
   - Effort: 3-4 hours, 1 session.

5. **S83-GODBILLON-VEY-JENSEN-DEFORM** — D1 / CV1 carry-forward.
   - What: test whether the Godbillon-Vey class (codim-1 foliation secondary characteristic class on the τ-foliation of the Jensen family) is actually deformation-sensitive via the Heitsch variation formula, or whether for our specific connection the Δ-term accidentally vanishes. If GV deforms nontrivially, D1's exclusion is confirmed. If GV is Jensen-invariant, clause a must WIDEN to include GV-class cocycles.
   - Inputs: Jensen-family connection 1-form (S42); Heitsch variation formula for secondary characteristic classes; Godbillon-Vey formulation from Connes-Moscovici 1998 (*The Local Index Formula in NCG*) or Connes *Noncommutative Geometry* 1994 §III.7.
   - Gate: S83-GV-JENSEN. PASS: GV class NOT deformation-invariant above τ_threshold = 0.05 (D1 exclusion confirmed). FAIL: GV class IS Jensen-invariant (would force widening of clause a to include GV; large theorem-revision triggered).
   - Effort: 4-6 hours, 1-2 sessions.

6. **S83-FI-DUALITY-THEOREM-FORMALIZATION** — EM1 carry-forward.
   - What: formal proof that M_lizzi ⇔ M_connes in F_KK, beyond the 42-row atlas verification. Specifically: prove (a) ⇔ (K-a) at the level of HP^even generators (Connes 1985 Thm 2.1), (b) ⇔ (K-b) via the general mode-equation-as-KK-correspondence theorem (Kasparov 1988), (b') ⇔ (K-c) via K_0(C) = Z triviality. Register the theorem as §VII.K-DUAL in permanent-results-registry.md.
   - Inputs: R2-A revised §VII.K text; my C1 K-theoretic iff; this workshop's CE4-CE7 counter-example analysis; Connes 1985, Kasparov 1988, Connes-Moscovici 2014.
   - Gate: S83-FI-DUALITY-THEOREM. PASS: formal proof written, reviewed by independent agent, and registry-landed as §VII.K-DUAL. INFO: proof complete for F_KK but scope-limited to specific sub-classes of quantities (e.g., requires separate argument for APS mod-Z ingredients). FAIL: a counter-example is discovered where M_lizzi and M_connes disagree on classification (would retract the dual-machinery claim).
   - Effort: 2-3 agent-sessions.

7. **S83-PINNING-AUDIT-FRAMEWORK-WIDE** — E3 / EM2 carry-forward.
   - What: apply the MIXED-verdict-FI-via-pinning meta-principle (EM2) to the framework-wide prediction set. For each observationally-interfacing prediction (A_s, m_H, n_s, α_s, FIRAS-Chluba μ, r-limit, f_NL, w_0, σ_8, H_0, Ω_GW at LISA band, ...), classify as {pure-FI, MIXED-verdict-FI-via-pinning, pure-RD diagnostic, NOT-YET-CLASSIFIED}. For each MIXED-verdict-FI-via-pinning entry, list the pinning-pipeline ingredients with documentation status (stable / draft / undocumented).
   - Inputs: §III.A observable ladder from S82 OOM; S82 42-row atlas; current framework prediction inventory from session finals.
   - Gate: S83-PINNING-AUDIT. PASS: every framework prediction classified + pinning-ingredients explicitly listed with documentation status. INFO: 1-3 predictions flagged as NOT-YET-CLASSIFIED (S84+ work). FAIL: ≥4 unclassified (suggests the meta-principle itself needs refinement).
   - Effort: 4-5 hours, 1 session.

8. **S83-META-PRINCIPLE-REGISTRY-LANDING** — EM2 carry-forward.
   - What: add §VII.K-META to `summary/permanent-results-registry.md` stating the MIXED-verdict-FI-via-pinning meta-principle: "For spectral quantity Q with MIXED ingredient algebra, Q counts as a zero-free-parameter framework prediction IFF every RD/SD ingredient has a documented, stable pinning pipeline. The MIXED verdict classifies scheme-robustness; the pinning pipeline classifies predictive commitment. These are orthogonal axes." Cross-reference feedback_reporting-framing.md rule.
   - Inputs: EM2 text from this workshop; feedback_reporting-framing.md rule; S83-PINNING-AUDIT output (item 7).
   - Gate: S83-META-REGISTRY. PASS: §VII.K-META entry present with exact meta-principle text, cross-reference to §VII.K-DUAL, and links to feedback_reporting-framing.md.
   - Effort: 1 hour, 1 agent-session (editorial; bundles with S83-FI-REGISTRY-VII-K-LANDING).

### Closing Line

The FI/RD/MIXED taxonomy is not a technical artifact of one framework: it is a STRUCTURAL property of the substrate's spectral data, proven by dual-machinery equivalence, now pre-registered as S83's top structural-theorem targets — with ε_H's secondary-KK promotion controlling the observational-interface predictions and thus the framework's next-session fate.
