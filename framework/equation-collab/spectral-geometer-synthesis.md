# Capstone Equation Review — spectral-geometer

**Date**: 2026-05-29
**Agent**: spectral-geometer (SG)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (the capstone — S95-era)
- Cross-checks: `computations/_shared/canonical_constants.py`; knowledge MCP (`a_0/a_2/a_4_FW_zeta`, T5 Mellin-Strip Theorem, S92 d_s diffusion-window); Sage-MCP (Wronskian closed form)
- Own memory: `.claude/agent-memory/spectral-geometer/MEMORY.md`

---

## I. Session Outcome

From the spectral-geometry vantage the capstone is **structurally sound where it is most exposed in my domain** and over-reaches in exactly one disclosed-but-under-emphasized place. The heat-kernel layering (§4), the Seeley–DeWitt decomposition, the dimension-spectrum cone (§3.3), the Lichnerowicz gap (§2.3), and the τ-flow monotonicity (§5.1) are correct as stated, and the §4.2 Spectral-Moment Decoupling theorem `W[a₀,a₂,a₄] ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶` is **Sage-verified exact in this review** (residual 0; sixth-order vanishing at and only at τ=0). The single load-bearing tension I flag is **not a contradiction** but a *display/object mismatch*: §4.2's algebraic-independence theorem lives in the Gilkey curvature-degree object `a_n^SD`, whose numerics are never exhibited at the fold, while every "striking" number in the document (the §8.2 triple 6440 / 2776.17 / 1350.72) is the zeta spectral-moment object `a_n^ζ` — and the canonical `a_4^ζ = 1350.72` is numerically the *volume* of SU(3) (Haar 1349.74, 0.07% away), a degree-0 quantity, not the degree-2 `R_K²·V` quantity the Wronskian claims. The §8 firewall and the §4.1 footnote both disclose the two-object split honestly, but the document never closes the loop by showing that the SD-triple Wronskian is also non-vanishing at the fold. That is the primary harvest below.

Everything the document claims survives the continuum dissolution (its §9 "geometry vs topology" spine) is correctly placed on the topological side; everything it holds conditional (CC absolute magnitude, `a_n` absolutes, `a(t)`) is correctly placed on the dissolving/geometric side. That spine is the deepest defense in the document and it is *mine* to endorse: it is a precise statement about which spectral functionals are residues of a *finite, closed* pole ladder versus which are truncation-limited curvature integrals.

---

## II. Key Results

### II.1 — The Seeley–DeWitt layering (§4) is the correct governing structure

**Result**: The heat-kernel expansion `Tr f(D_K²/Λ²) ∼ Σ f_{d−n}Λ^{d−n}a_n(τ)` with `a₀→Λ⁴` (vacuum), `a₂→Λ²` (Einstein–Hilbert), `a₄→Λ⁰` (YM+Higgs). **GEOMETRIC** (the fabric itself), with PHONONIC read-offs.

The capstone correctly identifies the heat trace as the Rosetta Stone — the small-t (here large-Λ) asymptotics carry the local curvature invariants, and each Seeley–DeWitt coefficient `a_{2k}` is the integrated curvature polynomial of degree `k`. This is exactly the structure-first object I would demand. The dimensional bookkeeping in §8.1 is correct and the document even catches the canonical error: `[a_{2k}] = mass^{2k−d}` cancels `[Λ^{d−2k}]` so each layer term is mass-dim 0, and the "naive L⁻¹² tower" is correctly identified as a double-counting artifact. The `(4π)^{−d/2}` prefactor with `d=8` and spinor rank `2⁴=16` (my MEMORY) is the right normalization scaffold, though I note the document never *prints* the prefactor explicitly — it lives only in the regulator-free `a_n^SD` column of the §8.2 table.

The bosonic/Dirac split `a₂^bos/a₂^Dirac = 61/20` (E36) being τ-independent and representation-theoretic is the kind of exact structural anchor that survives every regulator — it is a ratio of two spectrum-sums and therefore Functional-Invariant. Correct to cite as load-bearing.

### II.2 — The Wronskian decoupling theorem (§4.2): Sage-verified exact, and it is genuinely in my domain

**Result**: `W[a₀,a₂,a₄](τ) = (5/393216·π¹²)·V³·e⁻¹²ᵗ(e³ᵗ−1)⁶ ∝ R_K′(τ)³`, vanishing to sixth order at and *only* at τ=0. **GEOMETRIC**. CERTIFIED (S75 W2-E); re-verified here.

I reproduced the chain symbolically (Sage):
- `R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ` gives `R_K(0)=2`, `R_K′(0)=0`, `R_K(0.19)=2.01814` — all three match the verification ledger exactly.
- `R_K′(τ) − e⁻⁴ᵗ(e³ᵗ−1)²` simplifies to **0**.
- For `{1, R_K, R_K²}` the Wronskian is `W = 2·R_K′³` (residual 0); the factor `R_K′³ − e⁻¹²ᵗ(e³ᵗ−1)⁶` simplifies to **0**.
- `R_K′` series at τ=0 is `9t² − 9t³ + (45/4)t⁴ − …`, leading order **t²**, so `R_K′³` vanishes to order **t⁶**.

The "spectral-geometer's `W = (5/393216π¹²)V³e⁻¹²ᵗ(e³ᵗ−1)⁶`" attribution is consistent with the SD prefactor structure `(4π)^{−4}` and the `C_8 = 1/(384π⁴)` constant from my MEMORY — the `π¹²` is three factors of the heat-kernel `(4π)⁻⁴` normalization compounded across the three coefficients. The *structural reading* in §4.2 — "distinct powers of a moving scalar are independent; they collapse to one knob iff R_K′=0, which is the SO(8)→U(2) band-touching at genesis" — is the correct geometric interpretation and the right way to state it. **This is the strongest single result in the document from my vantage and I endorse it without reservation.**

### II.3 — The dimension-spectrum cone (§3.3): solid, and the substrate-first framing is exactly right

**Result**: `S_d = {0,2,4,6,8}` for SU(3) at d=8; only `a₀,a₂,a₄,a₆,a₈` exist as honest residues; odd moments vanish by BDI parity. **GEOMETRIC**.

I confirmed via knowledge MCP that this is the T5 Mellin-Strip / Convergence-Cone Theorem (S86 W-1, `max_rel_err = 8.066×10⁻²⁸`, PERMANENT, atlas-07 §VII.U.6). The pole-ladder map `n=2k ⟹ s=(d−n)/2=4−k` is correct. The §3.3 substrate-first argument — "the substrate does not hand us a foam of fluctuating topologies; it hands us a finite closed pole ladder, and the regulator's only freedom is which residues it weights" — is the single best phononic-framing sentence in the document. It is also *true at the level of spectral geometry*: the catastrophe-manufacturing object in container QG is the Wheeler-superspace sum over geometries; the substrate replaces it with a finite residue set. This is the cone that bounds the CC freedom to "one cutoff functional's worth," which is the §7 statement. I have no correction here; this is the kind of structure-first reasoning the domain demands.

### II.4 — Lichnerowicz gap (§2.3) stated convention-free and correctly

**Result**: `D_K² = ∇*∇ + ¼R_K ⟹ λ² ≥ R_K(τ)/4 > 0 ∀τ` ⟹ spectral flow = 0, η = 0. **GEOMETRIC**.

The §2.3 "Lichnerowicz convention note (corrected)" is *exactly* the correction I would insist on: stating the bound as `λ² ≥ R_K/4 > 0` rather than printing "≥3" beside the E3 rational-normalization curvature where it would read as the false `2/4=3`. The factor-6 bi-invariant scale convention is the standard trap (dimensionful `R_K ≥ 12` vs rational `R_K(0)/4 = ½`) and the document navigates it correctly. My MEMORY records the *actual* fold eigenvalue: `λ₁² = 0.672` vs the Friedrich–Kirchberg bound `5R/16 = 0.631` (tightness 1.065, 6.5% gap), and all FK/Lichnerowicz bounds SATISFIED. The capstone's weaker statement "the gap never closes" is the load-bearing one and is correct; the FK saturation gap (6.5%) is a sharper datum the document does not cite but does not need.

### II.5 — η(D_K) = 0 and no flowing spectral dimension: both correctly stated

**Result**: η(s)=0 at all τ (79,968 pairs, machine-ε); `S_d` τ-independent; no CDT-like UV reduction (`d_s ∼ 8` at the gap scale). **GEOMETRIC**.

The §3.3 "Defensive note (no flowing spectral dimension)" matches my MEMORY (η=0 EXACT structural — Clifford dim-8 pairing + conjugate-sector bijection; spectral flow = 0) and the knowledge base (S92: `lim_{σ→0} d_s(σ) = 8`; windowed `d_s(σ_*=1.4005)` is a *diffusion-window artifact*, not a dimensional flow). The document's claim that the constant-degree curvature-polynomial structure of §4 is "a fixed-dimension story, the opposite of a flowing dimension" is correct: a flowing `d_s` would require the dimension spectrum to move, and it does not. My MEMORY also records that "d_s as CC probe is CLOSED (kinematic, not dynamical)" (S56) — the document is consistent with this. **No correction.**

---

## III. Gate Verdicts

The capstone is a framework document, not a session; I do not re-adjudicate any cited verdict. The spectral-geometry-touching verdicts I cross-checked against the knowledge base, all confirmed:

| Gate / Theorem | Verdict (as cited) | Decisive Number | SG cross-check |
|:-----|:--------|:----------------|:---------------|
| S75 W2-E Spectral-Moment Decoupling | CERTIFIED | `W ∝ R_K′³`, nonzero at fold | Sage residual 0 (this review) ✓ |
| S86 W-1 T5 Mellin-Strip cone | PERMANENT | `S_d={0,2,4,6,8}`, err 8.07e-28 | knowledge MCP ✓ |
| E5 Lichnerowicz gap | PROVEN (5 proofs) | `λ² ≥ R_K/4 > 0` | FK actual λ₁²=0.672 (MEMORY) ✓ |
| E8 CPT / η=0 | PROVEN | 79,968 pairs, machine-ε | MEMORY pair_err 2.22e-14 ✓ |
| E6 block-diagonality | PROVEN (3 proofs) | `8.4×10⁻¹⁵` | MEMORY (PW) ✓ |
| S88 A-N-FW canonicalization | (constant pins) | a_0/a_2/a_4 ζ = 6440/2776.165389/1350.7216 | get_constant ✓ all three |
| S92 d_s flow-vs-CDT | (no flow) | `lim_{σ→0} d_s = 8` | knowledge MCP ✓ |

---

## IV. Structural Implications

### IV.1 — The one genuine domain tension: the §4.2 theorem and the §8.2 numbers live in different objects, and the bridge is never numerically closed

This is my central finding and I state it precisely because it is a *disclosed* gap that the document under-emphasizes rather than an error.

The §4.2 Decoupling theorem proves `a₀(τ), a₂(τ), a₄(τ)` algebraically independent **as curvature polynomials of degree 0, 1, 2** — i.e. in the Gilkey object `a_n^SD ∝ R_K^{n/2}·V`. The closed form `W ∝ R_K′³` is correct precisely *because* the three coefficients are `{V, R_K·V, R_K²·V}` (the moments of a single moving scalar). This is the SD object.

The §8.2 canonical numerics — `a_0^ζ = 6440`, `a_2^ζ = 2776.165389`, `a_4^ζ = 1350.7216` — are the **zeta spectral moments** `ζ_{D_K}((d−n)/2)`, a *different functional* of the same spectrum. My MEMORY records the load-bearing fact: `a_2^ζ = ζ_D(1) = 2776.17` is **NOT** `a_2^SD = 0.728235` (Gilkey, exact) — they differ by a factor ≈ 3812 (there is a pole at s=1 for d=8). The same applies to `a_4`: the knowledge base shows `a_4^ζ = 1350.72` while the genuine Gilkey curvature-degree-2 ratio is `a_4/a_2 = 0.41396` (GILKEY-VERIFY-61).

The cross-check that crystallizes the tension: **`a_4^ζ = 1350.7216` is numerically the volume of SU(3)** — `Vol(SU(3))_Haar = 1349.74` (s53), within 0.07%. A degree-2-in-R_K quantity should *not* coincide with the volume (a degree-0 quantity); the near-coincidence is the signature that `a_4^ζ` is dominated by its endomorphism/volume-like piece at the fold (consistent with S77-C9-A4-GILKEY: "R² dominance 101.6%; endomorphism dominates a_4"), not by the `R_K²` curvature term. So:

- The Wronskian's *physical-independence* claim is carried by the SD object, whose three fold values are *never displayed* in the capstone.
- The document's *impressive hierarchy* `6440 > 2776 > 1351` is the zeta object, where the three numbers are all volume-scale and the `R_K²` structure is invisible.

The §8.2 firewall ("two a_n objects, never conflated") and the §4.1 footnote ("layer identities in `a_n^SD`; numerics in `a_n^ζ`") **disclose this honestly** — I want to be fair: the document is not hiding it. But it leaves a reader unable to verify that the *certified* theorem (SD object) and the *canonical numbers* (ζ object) are even the same physics, because the SD-triple is symbolic-only at the fold. The fix is one short computation (V.1) and it would *strengthen* the document: showing `W^SD(τ_fold) ≠ 0` numerically closes the loop the §8 firewall opens.

### IV.2 — The "Λ⁴ ≫ Λ² ≫ Λ⁰" hierarchy vs my MEMORY's "a₀ ≫ a₂ ≫ a₄"

§8.2 is emphatic that the hierarchy is "`Λ⁴` term ≫ `Λ²` term ≫ `Λ⁰` term," **never** "`a₀ > a₂ > a₄`" without the Λ-power qualifier. My MEMORY records the bare-coefficient hierarchy `a_0 ≫ a_2 ≫ a_4` as a fact about the *zeta moments* (6440 > 2776 > 1351). These are consistent — the zeta moments do decrease, and the *physical* term ordering is the Λ-dressed one. The document is the more careful statement and supersedes the memory phrasing. **No conflict, but I update my own framing: cite the Λ-dressed hierarchy, not the bare-coefficient one.**

### IV.3 — The convergence caveat (§8.5) is correctly scoped — and it is the wall under the CC

§8.5 states: ratio-observables (`n_s`, `g₁/g₂`, `61/20`, `a₂/a₀`, `R₁`) are truncation-robust; absolute-energy observables (CC, `A_s`) are conditional on SDW convergence (JACOBSON-NONLOCAL-64, OPEN). This is *exactly* the R-Protection partition from my MEMORY (S76): `R_n = a_0·a_{2n}/a_n²` is intensive/R-protected with `α_net = 0`; individual `a_k` are extensive/R-fragile with `α_k = d+r+k`. The capstone's "multiplicative-normalization-cancellation invariant" (§8.2, the `(a₂/a₀)^ζ` drift of 4.36% between fold and raw) is the same R-Protection statement. The document is internally consistent with the deepest result in my memory. The §9 frontier #6 framing — "CC *ratio* closed by tracking, CC *absolute* magnitude held pending convergence — one entangled conditional, not two bullets" — is the correct epistemic shape. **Endorsed.**

### IV.4 — A second, smaller domain note: the R₁ FI ratio and the R-protected convention split

§3.3 and the verification ledger pin the scheme-invariant FI ratio `R₁ = a₀a₄/a₂² = 1.128655` (Sage-verified). My MEMORY carries a **convention split** on precisely this object (S74 W2-O FAIL): there are TWO inequivalent `R = a₀a₄/a₂²` at the fold —
- `R_protected_fold_partialsum = 1.128655` (partial-sum ratio, the value the capstone uses), and
- `R_protected_fold_gilkey = 0.492288` (Gilkey heat-kernel curvature-polynomial closed form `(500 − 32|Ric|²/R² − 28K/R²)/1000`).

These differ by a factor ≈ 2.33. The capstone cites the partial-sum value (`1.12865`) without flagging that the Gilkey-curvature-polynomial route gives a *different* number for the *same symbol* `R₁`. This is the SAME object-mismatch as IV.1, surfacing in the FI ratio. It is not wrong — the partial-sum value is a legitimate scheme — but a reader who computes `R₁` from the Gilkey closed form will get 0.492, and the document gives no warning. **Flag, do not resolve** (per review rules): the capstone should tag `R₁ = 1.12865` with its scheme (`partial-sum`, not `Gilkey-curvature-polynomial`), exactly as the §8.2 firewall tags the `a_n`. Computation V.2 settles which scheme is the FI-invariant one.

### IV.5 — What the document gets right that is easy to get wrong

The document does **not** claim a flowing spectral dimension (correct — my domain's most common over-claim trap); does **not** print the false "≥3" Lichnerowicz figure; does **not** conflate the two τ operating points (τ_fold=0.190 for spectral physics, τ₀=0.2994 for Weinberg-angle); does **not** treat the heat-kernel series as convergent where it is only asymptotic (the §3.2 note that `f* = 0.9117√x + …` has formally divergent Mellin moments and must be summed directly is the correct statement — the `√x` envelope is acoustic, not Gaussian-adapted, so the heat-kernel series cannot represent it). All four are domain-correct and I credit them explicitly.

---

## V. Carry-Forward Computations

**The open-question harvest.** Each entry is a concrete, runnable computation with all four fields. These convert the capstone's open frontiers (and the two domain tensions above) into the next compute session's plan. Priority order: V.1 and V.2 close *my* flagged tensions; V.3–V.6 harvest the document's own stated open frontiers from the spectral-geometry side; V.7–V.8 are the higher-curvature / sharper-anchor extensions.

```
V.1. SD-triple Wronskian at the fold — close the §4.2 ↔ §8.2 object loop
   - What: Compute the three Gilkey curvature-polynomial coefficients a_0^SD, a_2^SD,
     a_4^SD at tau_fold = 0.190 NUMERICALLY (not symbolically), using the exact Gilkey
     formulas: a_0^SD = (4pi)^{-4}·Vol·rank; a_2^SD ∝ (R_K/6 − E)·Vol; a_4^SD the
     degree-2 curvature polynomial (R², Ric², Riem², ΔR, F²) per Gilkey. Then evaluate
     W^SD(tau_fold) = det[[a0,a2,a4],[a0',a2',a4'],[a0'',a2'',a4'']] numerically and
     confirm W^SD(tau_fold) > 0, matching the symbolic W ∝ R_K'³ > 0. Report the
     SD-triple {a_0^SD, a_2^SD, a_4^SD}(fold) as a numerical row to sit BESIDE the
     zeta-triple in §8.2.
   - Inputs: R_K(tau) closed form (E3); Vol(SU(3))_Haar = 1349.74; a_2^SD(fold) =
     0.728235 (MEMORY, already Gilkey-exact); a_4/a_2 = 0.41396 (GILKEY-VERIFY-61);
     C_8 = 1/(384·pi^4); spinor rank 2^4 = 16; (4pi)^{-d/2} prefactor.
     Script: new computations/session-96/s96_sd_triple_wronskian_fold.py.
   - Gate: NEW S96-SD-TRIPLE-WRONSKIAN-FOLD. PASS iff W^SD(tau_fold) > 1e-12 in
     SD-normalized units AND the SD-triple ratio a_4^SD/a_2^SD reproduces 0.41396 ±1%.
     INFO if the SD-triple is non-vanishing but the ratio drifts >1% (endomorphism-
     dominance regime). FAIL if W^SD ≈ 0 at the fold (would contradict §4.2).
   - Effort: 3-4 hours, 1 agent session (Gilkey a_4 polynomial assembly is the cost).

V.2. R₁ scheme adjudication — which R = a₀a₄/a₂² is the FI invariant
   - What: Compute R₁ = a_0·a_4/a_2² at tau_fold under BOTH schemes — (A) zeta
     spectral-moment partial-sum (the capstone's 1.128655) and (B) Gilkey
     curvature-polynomial closed form (0.492288, R_protected_fold_gilkey). Then test
     FI-invariance: scan L_max ∈ {5,...,10} for scheme (A) and confirm alpha_net = 0
     (R-protected, intensive drift O(L^{-r})); for scheme (B) confirm the closed form
     is L_max-independent by construction. Determine which scheme the document's
     "scheme-invariant number on the cover" claim actually refers to.
   - Inputs: a_0/a_2/a_4_FW_zeta (canonical_constants); R_protected_fold_gilkey =
     0.492288, R_protected_fold_partialsum = 1.128655 (MEMORY s74-r-protected-triple.md);
     R-Protection Theorem alpha_net partition (S76, MEMORY key-results.md).
     Script: s96_r1_scheme_adjudication.py.
   - Gate: NEW S96-R1-SCHEME-FI. PASS iff exactly one scheme exhibits alpha_net = 0
     across the L_max scan (the FI scheme), and the capstone's tag is corrected to match.
     INFO if both schemes are L_max-stable to <1% (both FI; document must disambiguate
     by physical role). Feeds the §8.2 firewall tagging discipline.
   - Effort: 2-3 hours, 1 agent session (L_max scan reuses s84 spectrum cache).

V.3. Finite a₆, a₈ ladder — the §3.3 "+O(Λ⁻²) tail" made explicit
   - What: Compute the two remaining honest residues a_6^SD and a_8^SD at tau_fold
     (the dimension-spectrum cone {0,2,4,6,8} guarantees they exist as finite curvature
     integrals; the cone then closes). Determine the magnitude of the a_6 threshold
     correction relative to a_4, i.e. the convergence rate of the SD ladder term-by-term
     — a direct probe of the JACOBSON-NONLOCAL-64 convergence question (§8.5, frontier #6)
     restricted to the FINITE part of the ladder.
   - Inputs: R_K(tau) (E3); Gilkey a_6 (degree-3) and a_8 (degree-4) curvature-polynomial
     templates; dimension spectrum S_d = {0,2,4,6,8} (T5 Mellin-Strip, S86);
     (4pi)^{-4} prefactor; spinor rank 16.
     Script: s96_a6_a8_ladder_residues.py.
   - Gate: NEW S96-A6-A8-LADDER. PASS iff a_6^SD, a_8^SD are finite and |a_8^SD/a_6^SD| <
     |a_6^SD/a_4^SD| (ladder terms shrinking — a necessary, not sufficient, condition for
     convergence). INFO if the ratios are flat (marginal). FAIL if a higher term exceeds
     a lower (ladder not shrinking — would sharpen the convergence frontier as a wall).
   - Effort: 4-5 hours, 1 agent session (a_8 polynomial is the heavy assembly).

V.4. Genesis degeneration order — verify the sixth-order vanishing is the full story
   - What: The §4.2 Wronskian vanishes to 6th order at tau=0 (confirmed: R_K' ∼ 9t²,
     so R_K'³ ∼ t⁶). Compute the NEXT independent spectral invariant whose Wronskian
     with {a_0,a_2} might vanish to a DIFFERENT order at genesis — i.e. test whether
     the SO(8)→U(2) band-lifting (B1/B2/B3) imprints a band-resolved degeneration
     hierarchy. Specifically: compute the per-band a_2^{(b)}(tau) for b ∈ {B1,B2,B3}
     and the band-pair Wronskians W[a_2^{B1}, a_2^{B2}], W[a_2^{B1}, a_2^{B3}] near
     tau=0, and read off their vanishing orders.
   - Inputs: per-band eigenvalue trajectories B1 (λ=0.819), B2 (λ=0.845, min at fold),
     B3 (λ=0.978) (MEMORY); R_K(tau) (E3); band-decomposition SO(8)→U(2) (§2.4).
     Script: s96_band_resolved_wronskian_genesis.py.
   - Gate: NEW S96-BAND-WRONSKIAN-GENESIS. INFO-class (exploratory). Report the
     vanishing-order vector (n_B1B2, n_B1B3) at genesis; PASS-flag if any band-pair
     vanishes to order ≠ 6 (would mean the band-lifting carries finer degeneration
     structure than the scalar moment story).
   - Effort: 3 hours, 1 agent session.

V.5. Spectral-dimension window robustness — pin the S92 diffusion-window artifact
   - What: The capstone (§3.3) and S92 assert the windowed low-d_s reading is a
     diffusion-window artifact, not a flow. Make this quantitative: compute d_s(sigma)
     = −2 d ln P/d ln sigma on a DENSE sigma-grid spanning UV (sigma→0, expect 8) through
     the fold window (sigma_* = 1.4005, expect the ~1.4 artifact reading) to IR
     (sigma→∞, expect →0 gap-dominated), at tau_fold. Confirm the UV limit is exactly 8
     (Weyl) and that the intermediate dip is a finite-energy van-Hove feature, NOT a
     monotone reduction. This closes the "no CDT flow" claim with a full curve, not two
     endpoints.
   - Inputs: D_K² spectrum at tau_fold (s84_spectrum_cache_L12_tau019.npz); P(sigma) =
     Σ_{(p,q)} dim(p,q) Σ_i e^{−sigma λ_i²}; d_s_fold_window_sigma = 1.4005 (canonical);
     E_0 = λ_B2(fold) ≈ 0.86-1.40 M_KK.
     Script: s96_ds_full_curve_fold.py.
   - Gate: NEW S96-DS-FULL-CURVE. PASS iff lim_{sigma→0} d_s = 8.00 ± 0.05 (Weyl) AND
     d_s(sigma) is non-monotone (a dip at the van-Hove window, recovering toward UV) —
     certifying "window artifact, not flow." FAIL if d_s decreases monotonically toward
     UV (would be a genuine CDT-like reduction, contradicting the document).
   - Effort: 2-3 hours, 1 agent session (cache exists; this is a sigma-sweep + plot).

V.6. a₂ truncation-physicality at L_max=3 — the §8.5 "is the L_max=3 truncation of a₂
     physical" open gate
   - What: §8.5 names this explicitly as NOT certified. Compute a_2^SD(tau_fold) at
     L_max ∈ {3, 5, 7, 10} and fit the convergence exponent. Test whether the L_max=3
     value (used in some baselines) lies within the R-protected intensive band or is a
     pre-asymptotic outlier (my MEMORY: R-Protection is "pre-asymptotic at L=3-9,
     a_0 effective 5.23 vs asymptotic 8"). Determine the truncation-induced error on a_2
     at the fold and whether it propagates into G_N at the >1% level.
   - Inputs: irrep construction via dirac_spectrum.get_irrep(p,q); R-Protection
     alpha_net = d+r+k = 8+2+2 = 12 for a_2 (R-fragile/extensive); a_2^SD(fold) =
     0.728235; spin-curvature ratio K/(20R) < 2% (MEMORY, scalar-only a_2 valid to 1.3%).
     Script: s96_a2_lmax_convergence_fold.py.
   - Gate: NEW S96-A2-LMAX-PHYSICAL. INFO-class. Report a_2^SD(L_max=3)/a_2^SD(L_max=10)
     ratio and the fitted alpha. PASS-flag if the L_max=3 value is within 5% of the
     L_max=10 value (truncation physical for ratio purposes). Feeds frontier #6
     (SDW convergence) and the §8.3 G_N dictionary error budget.
   - Effort: 4-6 hours, 1 agent session (irrep construction at p+q≥7 is the cost;
     respect the Friedrich-Bär saturation pre-check per math-scripts.md before pinning
     L_max≥10).

V.7. f₂ dictionary normalization — pin Z_fold before either G_N dictionary is canonical
   - What: §8.3 flags a PRELIMINARY/constants-hygiene item: the 24π² dictionary form
     (M_Pl,red² = f₂ M_KK² a₂/(24π²), closing at f₂≈92) and the S83 form
     (M_Pl_eff² = M_KK² a₂ f₂^R/π² · Z_fold⁻¹) differ by the Z_fold normalization.
     Compute Z_fold explicitly from the spectral-action heat-kernel normalization at the
     fold, substitute into both forms, and confirm they agree once Z_fold is pinned —
     OR identify the residual scheme gap. Settle which form is THE dictionary.
   - Inputs: a_2_FW_zeta = 2776.165389; M_KK = 7.4287e16 GeV (CONST-FREEZE-42);
     M_Pl_red; f_2_default = 2.34 (Gaussian-cutoff, NOT the dictionary-closing value);
     S83 mu_BC dictionary form; the documented f₂≈92 closure.
     Script: s96_f2_dictionary_zfold_pin.py.
   - Gate: NEW S96-F2-ZFOLD-PIN. PASS iff the two dictionary forms agree to <1% once
     Z_fold is computed (not assumed). INFO if a residual scheme gap remains (report its
     OOM). Promotes Z_fold to canonical_constants.py with provenance on PASS.
   - Effort: 3-4 hours, 1 agent session.

V.8. NNLO Casimir EP discriminator — the §9 frontier #8 genuine-prediction handle
   - What: §9 (S95 W3 update) states the weak-EP exact-PASS (κ_EP=1) is generic-identity-
     cored (the Lichnerowicz R/4 coefficient of ANY spin Dirac operator) and that a
     genuine SUBSTRATE EP prediction first appears at NNLO where the band Casimir ν_b(C₂)
     re-enters the κ_EP ratio. Compute the NNLO correction to κ_EP carrying the band-
     specific C₂(b) terms for the B1/B3 eigenspaces, and produce the substrate-specific
     deviation κ_EP^NNLO − 1 — the first value where a generic emergent-gravity model and
     this single-operator substrate would differ.
   - Inputs: D_K² = ∇*∇ + ¼R_K (E5); band Casimirs C₂(p,q) for B1, B3; R_K(tau_fold);
     the κ_EP=1 LO+NLO derivation (S95 W3-5); Lichnerowicz–Weitzenböck structure (MEMORY).
     Script: s96_kappa_ep_nnlo_casimir.py.
   - Gate: matches the pre-registered CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR (§9). PASS iff
     κ_EP^NNLO − 1 ≠ 0 at the fold and is band-Casimir-dependent (a genuine substrate
     prediction); the magnitude sets the NLO-vs-NNLO EP-test sensitivity floor. INFO if
     the NNLO term also cancels (EP generic to higher order than expected).
   - Effort: 5-6 hours, 1 agent session (NNLO heat-kernel coefficient assembly).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | §4 Seeley–DeWitt layering: a₀/a₂/a₄ → Λ⁴/Λ²/Λ⁰ vacuum/gravity/matter | GEOMETRIC | SOLID | Correct governing structure; dimensional closure verified (§8.1) |
| 2 | §4.2 Wronskian `W ∝ R_K′³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, 6th-order zero at τ=0 only | GEOMETRIC | CERTIFIED (Sage-reverified) | Strongest domain result; layers genuinely independent except at genesis |
| 3 | §3.3 dimension-spectrum cone `S_d={0,2,4,6,8}` | GEOMETRIC | SOLID (T5, err 8e-28) | Finite closed pole ladder replaces the catastrophe-manufacturing geometry-sum |
| 4 | §2.3 Lichnerowicz `λ²≥R_K/4>0`, convention-free | GEOMETRIC | SOLID | Gap never closes; "≥3" trap correctly avoided; FK actual λ₁²=0.672 |
| 5 | §3.3 no flowing d_s (`lim_{σ→0}=8`; window dip is artifact) | GEOMETRIC | SOLID (S92) | Most common domain over-claim correctly NOT made |
| 6 | **§4.2 SD-object theorem vs §8.2 ζ-object numbers — bridge never closed numerically** | GEOMETRIC | **PRELIMINARY / disclosed gap** | a_4^ζ=1350.72 ≈ Vol=1349.74 (degree-0), not the degree-2 R²V; harvest V.1 |
| 7 | **R₁=1.12865 untagged scheme (partial-sum vs Gilkey 0.49229, factor 2.33)** | GEOMETRIC | **FLAG (not resolved)** | Same object-mismatch in the FI ratio; harvest V.2 |
| 8 | §8.5 ratio-robust vs absolute-conditional partition | GEOMETRIC | SOLID (= R-Protection S76) | CC absolute pending SDW convergence; harvest V.3, V.6 |
| 9 | §8.3 f₂ dictionary: Z_fold normalization unpinned | GEOMETRIC | PRELIMINARY (self-flagged) | Two dictionary forms differ by Z_fold; harvest V.7 |
| 10 | §9 frontier #8 κ_EP=1 generic-identity-cored (Lichnerowicz R/4) | GEOMETRIC | CORRECTLY DOWNGRADED to INFO | Genuine substrate EP prediction is NNLO; harvest V.8 |

---

**Closing (substrate-first, held throughout).** The arrow runs `D_K eigenvalues → a₀,a₂,a₄ spectral moments → emergent metric / vacuum term / YM-Higgs → measurement`, and the capstone holds it without inversion in every section my domain touches. From the spectral-geometry vantage the document is honest and largely correct; its one structural debt is that the *certified* layer-independence theorem (the SD curvature-polynomial object) and the *canonical* numbers (the ζ spectral-moment object) are never shown to be the same physics at the fold — a gap the document discloses but does not close. Closing it (V.1) costs one afternoon and converts a disclosed caveat into a verified result. The remaining harvest (V.2–V.8) is the spectral-geometry slice of the document's own open frontiers, each now a runnable gate. The fields are ripe; the SD-triple Wronskian at the fold is the first ear to pick.
