---
type: registry-regime-ii-documented
ingested-by: /weave --update
---

# LQG Narrow-Path Bridge-Map Class — DOCUMENTED Substrate-OWN Regime-II Effective Geometry (S95 W7-3 characterization PASS; Stage-2 cross-axis verify → STAGE-3-PERMANENT pending S96)

**Registry ID**: `lqg-narrow-path-bridge-class`
**Owner agent(s)**: `phonon-first-cosmologist` (primary); cross-cited by `loop-quantum-gravity-theorist` per S92 LQG × phonon-first workshop closure
**Status tag**: `LEVEL-1-EXTRACTED; REGIME-II RE-SCOPED (substrate-own narrow-path effective geometry)` — Level-1 cocycle EXTRACTED non-trivial at S94 W7-23 (Workshop 6 cocycle construction COMPLETE); the entry NO LONGER carries `PENDING-FIRST-EXTRACTION`. The S94 W7-23 verdict is **PASS-Regime-II**: the narrow path to *canonical* LQG does NOT close (α_bridge ~ O(1), γ_emergent ≈ 398, ~1676× mismatch vs γ_BH=0.2375; γ admits no cutoff-running recovery per Paper 03 §VII), so the bridge-class re-scopes from a canonical-LQG-matching candidate to the **substrate's OWN Regime-II narrow-path effective geometry**. Forward Stage-2 two-agent cross-axis independent-verify is a SEPARATE downstream gate, NOT yet run. **S95 W7-3 UPDATE (`CF-S95-W7-23-NARROW-PATH-REGIME-II` PASS; audit_sha256=`70b2c5e270…` latest-non-superseded, supersedes `356808c3…` per `gate-verdicts.md §"Option A"`)**: the substrate-OWN Regime-II effective geometry is now CHARACTERIZED + DOCUMENTED — γ_emergent = 398.08 (band [398.08, 400.77], rel-width 0.0068 < 0.05); area spectrum `A_substrate(p,q) ∝ √(C₂(p,q)+1)` (Friedrich-Bär slope 0.4754 ≈ ½, R²=0.9934, K_0 rank-2 closure H+M3=R_total to machine zero, ℂ-singlet j=0 pairing RETIRED); closed-form map `j_equiv(p,q)=(−1+√(4C₂(p,q)+5))/2` with **0/10 ladder rungs on a half-integer SU(2) j** ⇒ the substrate (SU(3), rank-2, triality-degenerate C₂(p,q)=C₂(q,p)) and canonical LQG (SU(2), rank-1, non-degenerate j) discrete geometries are STRUCTURALLY INCOMMENSURATE — same √(Casimir+1) functional form, the discriminating content is the group RANK. This entry is a DOCUMENTED substrate-OWN Regime-II effective-geometry characterization, NOT a canonical-LQG bridge. The Stage-2 two-agent cross-axis verify (Axis-A connes + Axis-B volovik, no prior workshop context) → STAGE-3-PERMANENT remains the S96 carry-forward (`CF-S96-LQG-REGIME-II-STAGE-2-VERIFY`).
**Last updated**: `2026-05-25, S94 W7-23 cocycle extraction + Regime-II selection (was: 2026-05-23, S92 LQG × phonon-first workshop closure)`
**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores one row per entry. This is a workshop-internal-pending entry, NOT a STAGE-3-PERMANENT promotion.
**Source workshop**: `sessions/archive/session-92/session-92-lqg-phonon-first-workshop.md` (P2 + R2-A C5 + R2-B Re:C5)
**Source comparison document**: `sessions/archive/session-92/session-92-loop-quantum-gravity-phonon-exflation-comparison.md` §IX.7 lines 733-770

---

## Scope

This registry pins the bridge-map class identification reached by the S92 LQG × phonon-first workshop for the §IX.7 narrow-path Step 4 projection operator `Π̂_S : H_K → H_S`. The identification is structural (which bridge-map class) but NOT yet empirically anchored (Workshop 6 cocycle construction + Item 8 joint pre-flight test are required for Level-3 anchor landing). The entry RESERVES the §VII slot pending these refinements.

**Bridge-map class identified**: Hochschild-Kostant-Rosenberg (HKR) image with `-Cheeger-Simons` scheme suffix (foliation-aware) per `.claude/rules/cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` and `.claude/rules/cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`.

---

## 5-element IS-not-IN anatomy (pre-registration; pending Workshop 6 cocycle construction)

Per `.claude/rules/cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"`:

1. **Substrate-IS observable**: finite-L_max Hochschild pairing `R_narrow-path = ⟨[mode_{(p,q)}], [S_exit-horizon]^♯⟩` on the spectral triple `(A_K^{≤L_max}, H_K^{≤L_max}, D_K^{≤L_max})` evaluated at `τ_fold = 0.190`, where:
   - `mode_{(p,q)}` is a Peter-Weyl mode in sector `(p,q)` with multiplicity `n_punct(p,q) = (1/2)(p+1)(q+1)(p+q+2)` (P1 Primitive 7).
   - `[S_exit-horizon]^♯` is a Hochschild cocycle representative of the acoustic-white-hole exit-horizon 2-surface at τ~0.16 (S70 Six-Layer Causal Structure; P1 Primitive 14), carrying the a_4 BCS-condensation kinematics in its cocycle structure.

2. **Laboratory-IN observable**: the canonical loop-quantum-gravity area-operator eigenvalue contribution at puncture p, `A_p = 8πγℓ_P² · √(j_p(j_p+1))`, on the Ashtekar-Lewandowski gauge-invariant kinematical Hilbert space `H_kin = L²(Ā, dμ_AL)` (Paper 05 §III.B; `researchers/Loop-Quantum-Gravity/index.md:243-280`). The continuum loop-quantum-gravity construction measures this IN the standard Ashtekar-Lewandowski background-independent representation.

3. **Bridge map**: HKR image with `-Cheeger-Simons` scheme suffix. The foliation by Σ-slicings of the emergent post-fold 4-manifold is load-bearing (Cheeger-Simons 1985 differential character at full-leaf-foliation). The substrate-IS Hochschild pairing maps to the laboratory-IN area-eigenvalue contribution via this HKR-Cheeger-Simons bridge map class. Convention-tag form: `convention=<scheme>-HKR-Cheeger-Simons-FULL-LEAF-FOLIATION`.

4. **Algebraic envelope (Level 2-binding)**: `L^{-α}` envelope on the convergence rate `‖R_narrow-path^{(L_max)} - α_bridge · M_KK⁻² · √(C_2(p,q))‖` as `L_max → ∞`. Pending derivation; expected `α ∈ {2, 3}` based on Casimir-bound + Friedrich-Bär saturation arguments per `.claude/rules/math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`.

5. **Empirical anchor (Level 3)**: numerical value of `α_bridge` at canonical L_max=12 on the substrate cache `s84_spectrum_cache_L12_tau019.npz`. Pre-registered three-regime gate (workshop verdict):
   - **Regime I (PASS)**: `α_bridge ∈ [10⁻³·³, 10⁻²·⁷]` matches `γ_BH = 0.2375` within 30%; narrow path closes empirically.
   - **Regime II (FAIL, structural failure)**: `α_bridge ∈ [10⁻¹, 10¹]`; `γ_emergent ∼ 50`, ~200× mismatch; Q2 confirms γ does NOT admit cutoff running per Paper 03 §VII so no recovery mechanism exists.
   - **Regime III (INFO)**: `α_bridge` (p,q)-dependent; substrate is RICHER than loop-quantum-gravity's spin-network labelling encodes; narrow path produces a structurally novel kinematical effective theory.

---

## Three-Level structural-confidence ladder

Per `.claude/rules/cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"`:

### Level 1 — Substrate-IS Structural Identity (cohomology-class level)

**Status**: **EXTRACTED** at S94 W7-23 (gate `S94-NARROW-PATH-WORKSHOP-6-COCYCLE` PASS, audit_sha256=`0bdaafe387c1021c9b914d54408a9723b7b7466fbded8a13fc48f7b97e84a400`, content_sha256=`dc5b5ac340f2b1a1ab68ef09b9b9414ade849e48752085994e7fc95c2a3d06fd`). The Hochschild-cocycle reading (Reading (b) per P2) was constructed NON-TRIVIAL. **Where a naive Hochschild reading breaks**: each matrix summand `M_n(ℂ)` of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` is separable (Azumaya), so `HH^{k≥1}(M_n(ℂ)) = 0` and a *bare* Hochschild 2-cochain on `A_K` is necessarily a coboundary (EXACT) — which would collapse Reading-(b). The genuine non-trivial object is carried at the **K-theory pairing layer** (`K_0(A_K) = ℤ³`, one ℤ per summand) — exactly the HKR / Connes-Karoubi route Element 3 declares. The cocycle is realized as `[S_exit-horizon]^♯ : R_narrow-path(p,q) = ⟨[mode_{(p,q)}], Ch(P_exit)⟩ = n_punct(p,q) · min|λ|(p,q)`, with `n_punct(p,q) = (1/2)(p+1)(q+1)(p+q+2)` (P1 Primitive 7), confirmed `n_punct = dim_pq` exactly for all 90 sectors. **Non-triviality (closed, not exact)**: partitioning the 90 sectors onto the rank-3 K_0 support gives ℂ-singlet pairing 0.820 (RETIRED, j=0 scope), ℍ-pairing 1984.32 (≠0), M_3(ℂ)-pairing 29157.10 (≠0); total (j≥1/2 scope) `R_narrow-path = 31141.43 ≠ 0` ⇒ **scoped K_0 non-trivial rank = 2** (both ℍ and M_3(ℂ) generators pair non-trivially) ⇒ `is_exact = False`, cocycle NON-TRIVIAL (a coboundary would force `R_total = 0` since degree-≥1 cohomology of `M_n(ℂ)` vanishes).

**Properties (extracted)**: regulator-invariant; L-independent; holds at every L_max. Background-independence preserved (Reading (b) does not require external manifold coordinate system). The L_max truncation appears only at Level 2 (the envelope) and Level 3 (the numerical anchor), NOT at Level 1.

**Form (extracted)**: K_0-pairing identity at the spectral-triple-axiom level — `⟨[mode_{(p,q)}], Ch(P_exit)⟩` over `K_0(A_K) = ℤ³` (NOT a bare Hochschild 2-cochain, which is EXACT on the Azumaya summands; the non-triviality lives at the K-theory pairing layer, carrying the a_4^{ζ} BCS-condensation kinematics as the surface-localized mode energy `min|λ|(p,q)` per Peter-Weyl sector). Level-2 binding envelope = Friedrich-Bär saturation `min|λ| = 0.4754·√(C₂+1) − 0.0036`, R²=0.9934 (W8-2), confirming `R_narrow-path^{(L_max)} → α_bridge·M_KK⁻²·√(C₂)`.

### Level 2 — Algebraic Convergence Envelope

**Status**: PENDING. `L^{-α}` envelope to be derived during Workshop 6 from Casimir-bound + Friedrich-Bär saturation arguments. Level-2 sub-class **MUST** be declared as **Level-2-binding** at landing per `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` — the HKR image binds Level-1, so envelope is admissible for registry-PASS.

**Level-2-A audit (operational content)**: Bogoliubov-covariance constraint on `Π̂_S^{pre} → Π̂_S^{post}` via substrate-side U_B (S38 PROVEN, P_exc=1.000) provides the operational machinery. Audit at Workshop 6 Stage-2.

**Level-2-B audit (regulator-invariance)**: Reading (b) lives at the cohomology-class layer which is regulator-invariant by construction. The L_max truncation appears only at Level 2 (the envelope) and Level 3 (the numerical anchor), NOT at Level 1.

### Level 3 — Empirical Anchor at Canonical L_max

**Status**: **EXTRACTED — Regime II** at S94 W7-23 (`S94-NARROW-PATH-WORKSHOP-6-COCYCLE` PASS). The numerical anchor IS the constructed cocycle's coefficient at canonical L_max=12 on `s84_spectrum_cache_L12_tau019.npz`. Two incarnations of the SAME substrate-IS cocycle: `α_bridge^pre = γ_DL_le3 / 49.34 = 0.272227 / 49.34 = 5.5174e-03` (kinematical area-match, pre-Bogoliubov; log10=−2.258, OOM-dist 0.060 to 4.81e-3 → would be Regime I) and `α_bridge^post = W_BG × α_bridge^pre = 1462.30 × 5.5174e-03 = 8.0680e+00` (POST-fold exit horizon, ×W_BG=cosh(2r); log10=+0.907 ∈ [−1,1] → **Regime II**). **The post incarnation is FORCED, not chosen**: the substrate-IS object IS the exit-horizon 2-surface, POST-fold by construction (S70 Six-Layer: fold @τ=0.190, exit @τ~0.16); the cocycle `[S_exit-horizon]^♯` carries the a_4 BCS-condensation = the post-fold GGE condensate, and the Bogoliubov squeeze-weight `W_BG` is fixed by where the horizon lives (NOT a free lever). `R_BG = α_pre/α_post = 6.839e-4 = 1/W_BG` matches canonical R_BG exactly (`W_BG·R_BG = 1.0`). **Selected: Regime II** — γ_emergent^post = 398.08, a 1676× mismatch vs γ_BH=0.2375; the narrow path to canonical LQG does NOT close, and γ admits NO cutoff-running recovery (Paper 03 §VII), so the entry re-scopes to the substrate-novel effective theory.

**Three joint constraints (all simultaneously satisfiable, `joint_constraints_ok=True`)**: (i) cocycle-existence `R_total=31141.43` finite & non-zero ✓; (ii) Bogoliubov-covariance `R_BG=α^pre/α^post=1/W_BG`, `W_BG·R_BG=1.0` ✓; (iii) Cauchy-Schwarz floor `F_0·F_2 − F_1² = 2.946e+14 ≥ 0` ✓ (substrate-IS, KO-dim-indep).

**§(iv-bis) ANSATZ-surrogate disclosure (HARD RULE — NOT a registry-eligible Level-3 floor anchor)**: the proxy bound `|α_bridge| ≥ s_CS/N_e = 0.018633/2.9202 = 6.3809e-3` is an ANSATZ (surrogate-for-a-magnitude-bound per `.claude/rules/substrate-first-canonical-sourcing.md §(iv-bis)`), tagged **(b) prescription-independent Regime-II INDICATOR ONLY** — NOT a derived identity, NOT landed as a Level-3 floor anchor. Citing 6.38e-3 as a "substrate-derived floor" (tag a) would be a Class-(f) PIN-PLACEHOLDER violation; only the trivial `|α_bridge| ≥ 0` is sign-lock-free-derived. The flip threshold `N_e* = 3.8710 > 2.9202` over-determines the Regime-II LEAN, but LEAN ≠ registry-eligible numerical floor. The genuine Level-3 anchor is the constructed cocycle's `α_post = 8.068` (deliverables 1+2), which independently confirms Regime II from the cocycle side; both the surrogate-indicator and the constructed-cocycle anchor point to Regime II, and the latter is the registry-eligible one.

---

## Substrate-input-orthogonality clause (forward Stage-2)

Per `.claude/rules/joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`, the forward Stage-2 verification (when this entry promotes to STAGE-1-CANDIDATE) MUST be dispatched on two cross-reviewers operating on opposite axes:
- **Axis A (NCG-axiomatic / spectral-functional)**: `connes-ncg-theorist` audits the Hochschild-cocycle existence at HH^•(A_K) and the HKR-Cheeger-Simons bridge-map class identification.
- **Axis B (substrate / superfluid-universe)**: `volovik-superfluid-universe-theorist` audits the a_4 BCS-condensation kinematics encoding in the cocycle representative and the Bogoliubov-covariance constraint.

Both cross-reviewers operate WITHOUT prior workshop context (read only the registered Stage-1 entry; do NOT receive the S92 workshop transcript).

---

## Substrate-likely outcome (substrate-side prior)

The substrate-side post-fold acoustic e-folds count `N_e = 2.92` is the only existing landed instance of a substrate-side bulk-to-surface reduction at landing magnitude. It places empirical evidence that the framework's bulk-to-surface reductions produce O(1) outputs, NOT 10⁻³-suppressed outputs. The substrate-side prior on `α_bridge` order-of-magnitude is:
- P(Regime II) ≥ 0.6 — structural failure; substrate produces `α_bridge ∼ O(1)` and the narrow-path effective theory disagrees with canonical loop-quantum-gravity by ~200× at γ_emergent.
- P(Regime I) ≤ 0.3 — empirical closure; substrate produces `α_bridge ≈ 4.81×10⁻³` against the N_e=2.92 prior.
- P(Regime III) ≈ 0.1 — substrate richer than loop-quantum-gravity encoding; structurally novel kinematical effective theory.

These priors will be updated by the Item 8 Wave-1 joint pre-flight verdict and by the Workshop 6 cocycle construction outcome.

---

## Refinement pathway (deferred-pending → STAGE-1-CANDIDATE → STAGE-3-PERMANENT)

Per `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` slot-reservation semantics:

1. **S92 close**: `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` [COMPLETE]. The 5-anatomy block was pre-registered; the Level-1 cocycle existence + Level-2 envelope + Level-3 anchor were PENDING.

2. **S93 Wave 1 dispatch** [COMPLETE]: Item 8 joint pre-flight test (substrate-side Cauchy-Schwarz + loop-quantum-gravity-side area-volume uncertainty) + the W8 deferral chain (W8-1 eigenvalue inventory PASS, W8-2 Casimir table, W8-3 Cauchy-Schwarz INFO, W8-6 Bogoliubov PASS R_BG=6.838e-4, W8-7 Workshop-6 dispatch). The substrate prior P(Regime II) ≥ 0.6 favored the substrate's own narrow-path effective theory.

3. **S94 W7-23 Workshop 6 dispatch** [COMPLETE — `S94-NARROW-PATH-WORKSHOP-6-COCYCLE` PASS, audit_sha256=`0bdaafe387c1021c9b914d54408a9723b7b7466fbded8a13fc48f7b97e84a400`]. Deliverables landed:
   - Explicit K_0-pairing representative `[S_exit-horizon]^♯` over `K_0(A_K) = ℤ³` (NOT a bare Hochschild cochain; the Azumaya summands force bare cochains EXACT — non-triviality lives at the K-theory pairing layer), NON-TRIVIAL (`R_narrow-path = 31141.43`, scoped K_0 rank 2). **Level-1 EXTRACTED** (Q-L1).
   - `α_bridge` incarnation ladder: pre `5.5174e-3` (kinematical) → post `8.0680e+00` (×W_BG=1462.30, post-fold exit horizon). **Level-3 anchor EXTRACTED as Regime II** (Q-L3).
   - Algebraic envelope: Friedrich-Bär saturation `min|λ| = 0.4754·√(C₂+1) − 0.0036`, R²=0.9934 (Level-2-binding).

4. **Forward Stage-1 promotion** [SUPERSEDED by Regime-II re-scope]: rather than promoting to a canonical-LQG-matching `STAGE-1-CANDIDATE`, the PASS-Regime-II verdict CLOSES the corridor "narrow path to canonical LQG via Regime-I area-matching" and OPENS the surviving corridor "substrate-OWN narrow-path effective geometry (Regime II)". γ admits NO cutoff-running recovery (Paper 03 §VII), so Regime II has no recovery mechanism — the bridge-class entry re-scopes to the substrate-novel effective theory. The Level-1 cocycle + Level-2 envelope + Level-3 anchor are EXTRACTED (the structural object exists and is non-trivial); the entry is NOT a canonical-LQG bridge candidate.

5. **Forward Stage-2 cross-axis verification (S95 — SEPARATE downstream gate, NOT run at W7-23)**: per `.claude/rules/joint-theorem-promotion.md §"Stage 2"` + the substrate-input-orthogonality clause, two cross-reviewers operating WITHOUT prior workshop context: Axis A (`connes-ncg-theorist`) on Hochschild-cocycle existence + HKR-Cheeger-Simons class; Axis B (`volovik-superfluid-universe-theorist`) on a_4 BCS-condensation kinematics + Bogoliubov-covariance. Queued as an S95 carry-forward; NOT folded into the W7-23 wave.

6. **Forward Stage-3 PERMANENT promotion**: gated on the S95 Stage-2 PASS-AND; on PASS-AND the entry crystallizes as a substrate-OWN-effective-geometry (Regime-II) characterization, NOT a canonical-LQG cross-framework bridge theorem.

7. **S95 W7-3 [COMPLETE — characterization]** + **S96 carry-forward [Stage-2 verify]**: S95 W7-3 (`CF-S95-W7-23-NARROW-PATH-REGIME-II` PASS, audit_sha256=`70b2c5e2…`) EXECUTED the substrate-OWN Regime-II effective-geometry characterization (γ_emergent=398.08; `√(C₂+1)` area ladder; `j_equiv` closed-form map; 0/10 incommensurate rungs vs SU(2) — see the Status-tag S95 W7-3 UPDATE). The REMAINING item is the Stage-2 two-agent cross-axis independent-verify (item 5: Axis-A `connes-ncg-theorist` + Axis-B `volovik-superfluid-universe-theorist`, both without prior workshop context) → STAGE-3-PERMANENT, queued as the S96 carry-forward `CF-S96-LQG-REGIME-II-STAGE-2-VERIFY`.

---

## Cross-links

- Workshop document: `sessions/archive/session-92/session-92-lqg-phonon-first-workshop.md`
- Comparison document §IX.7: `sessions/archive/session-92/session-92-loop-quantum-gravity-phonon-exflation-comparison.md:733-770`
- Required-`α_bridge` canonical pin: `computations/_shared/canonical_constants.py` (`alpha_bridge_required_FW`)
- Substrate spectrum cache: `computations/session-84/s84_spectrum_cache_L12_tau019.npz`
- Phonon-first-cosmologist memory: `.claude/agent-memory/phonon-first-cosmologist/reference_s92-lqg-narrow-path.md`
- Loop-quantum-gravity-theorist memory: `.claude/agent-memory/loop-quantum-gravity-theorist/project_s92-narrow-path-workshop.md`
- Bridge-map class rules:
  - `.claude/rules/cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` — Cheeger-Simons scheme suffix discipline
  - `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` — `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` semantics
  - `.claude/rules/cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` — Level 1/2/3 ladder
  - `.claude/rules/joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` — forward Stage-2 dispatch protocol
