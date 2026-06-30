# S116-W9-SATURATION-ADJUD — does p+q=15 shift a canonical observable, or is D_K Friedrich-Bär-saturated at p+q≤14?

**Date**: 2026-06-28
**Gate**: `S116-W9-SATURATION-ADJUD` (gate_type: workshop, Wave 9, Session 116 — TERMINAL wave)
**Format**: 2-agent adversarial adjudication, 3 rounds, sequential turns on this shared document
**Agents**: `baptista-spacetime-analyst` (canonical Q36 observable = the branch-(iv) **w0_FW DR3 Zubarev moment**, which SHIFTS) vs `spectral-geometer` (canonical Q36 observable = the **bottom-K |λ| floor**, Friedrich-Bär-SATURATED at p+q≤14)
**Closure**: artifact-existence (NO verdict line, per `wave-classification.md §M1`). Must end with R1/R2/R3 filled + a `## Structural Verdict` (the observable-DECOMPOSITION + the Friedrich-Bär saturation-theorem SCOPE statement + the bottom-K / w0_FW orthogonality) + `## Wrap-Up`.

## Adjudication Question

> Q36 asks whether the p+q=15 D_K sector shifts a canonical framework observable, or is structurally redundant because the spectrum is Friedrich-Bär-saturated at p+q≤14. The empirical anchors (S106 cache, complete p+q≤15 triangle, computed at plan-freeze):
>   (i) the **BOTTOM-64 |λ| floor** is IDENTICAL L≤14 vs L≤15 to `max|diff|=0.0e+00` (the bottom-20 ceiling is |λ|=0.845; the SMALLEST p+q=15 eigenvalue is |λ|_min=4.216 — the new shell cannot enter the bottom-K);
>   (ii) the **branch-(iv) w0 Zubarev moment SHIFTS**: `ρ_B(14)=−0.677718 → ρ_B(15)=−0.696174`, driven by λ_max growth (6.168→6.543), with a DECELERATING decrement `|d(14→15)|=0.01846 < |d(13→14)|=0.02083`.
>   Sub-questions: (1) WHICH observable is the canonical Q36 object — bottom-K floor, w0_FW DR3 moment, or BOTH (an observable-decomposition with declared orthogonality)? (2) Does "Friedrich-Bär saturation" (the S87 W11-2/W11-3 theorem) apply to the λ_max-driven w0 moment, or is its SCOPE strictly the bottom-K (and bulk low-|λ| moments)? Is the theorem mis-cited if invoked to declare the w0 DR3 spread "saturated"? (3) Is the decelerating decrement (`|d|~1/L²` from λ_max Weyl growth) evidence the w0 DR3 spread will reach the PASS band (≤0.025) at finite L, or a slow λ_max-Weyl drift that stays in the INFO band indefinitely?

## Competing Positions

- **spectral-geometer — bottom-K floor, SATURATED.** The canonical Q36 observable is the bottom-K floor (the §VII.AJ.partition-stability / Friedrich-Bär lineage the framework's spectral predictions key on). It is EXACTLY saturated at p+q≤14 (bottom-64 `max|diff|=0.0e+00`; the smallest p+q=15 |λ|=4.216 ≫ bottom-20 ceiling 0.845), so p+q=15 is structurally redundant — a completeness check. The w0 "shift" is a Weyl-law λ_max artifact (the top eigenvalue grows ~L by construction), not a substrate observable change. `η_FB(p,q)=|λ|_min(p,q)/√(C_2(p,q)+1)` bounds the NEW-sector eigenvalues BELOW, certifying the bottom-K is untouched.
- **baptista-spacetime-analyst — w0_FW DR3 moment, SHIFTS.** The canonical Q36 observable is the branch-(iv) w0_FW DR3 Zubarev moment (the DESI DR3 w0-wa falsifier-surface quantity, w0_FW=−0.918). It DOES shift at p+q=15 because ρ_B is λ_max-driven, not bottom-K-driven; p+q=15 is a genuine deep-truncation datum; the decelerating decrement is Friedrich-Bär saturation of the convergence RATE (`|d|~1/L²`), not redundancy of the datum.

**Numeric stakes**: bottom-64 floor `max|diff|(L≤14 vs L≤15)=0.0e+00`; bottom-20 ceiling |λ|=0.845; smallest p+q=15 |λ|_min=4.216; ρ_B(13)=−0.656884, ρ_B(14)=−0.677718, ρ_B(15)=−0.696174 (λ_max 5.793→6.168→6.543); spread_CAC{13,14,15}=0.039290 (INFO band, decelerating); `η_FB_lower=0.392839`. Verdict band (DR3 w0 lockdown, UNCHANGED): PASS≤0.025 | INFO(0.025,0.050] | FAIL>0.050.

**Adjudication rule**: a Q1 math/physics adjudication. R3 produces a STRUCTURAL VERDICT — the observable-DECOMPOSITION (which functional Q36 is about) + the Friedrich-Bär theorem SCOPE + the bottom-K/w0_FW orthogonality — derived from first principles (the empirical anchors are decisive on both sides). NOT a queued computation. The two readings cannot both be the whole story; the workshop reconciles them. Convention discipline: the w0_FW DR3 observable is CAC-pinned (regulator-convention-lockdown.md; RDC FORBIDDEN); the verdict band is UNCHANGED (no band-shopping).

**Substrate framing** (`phononic-framing.md`): GEOMETRIC, Level-1 single-τ-slice. The D_K spectrum at τ_fold=0.19 IS the set of substrate vibrational modes; the p+q=15 Peter-Weyl sector is a Level-1 single-τ-slice substrate-IS object (NOT a field "on" an internal space). Both observables are functionals of the SAME spectrum; the workshop derives WHICH functional Q36 is asking about and whether the Friedrich-Bär theorem's saturation scope covers it. Direction: `D_K eigenvalues at τ_fold (p+q=15 shell) → {bottom-K floor, λ_max-driven w0 Zubarev moment} → which observable Q36 is about → Friedrich-Bär saturation SCOPE`. The workshop does NOT invoke GR/dark-energy to explain the substrate — it scopes a substrate spectral theorem.

**Sources** (read before writing):
1. `computations/session-106/s106_w1_highl_cache_l1416.npz` — the p+q=15 sectors (sector_evals_L16) + η_FB_lower; audit 5af2b7cd…
2. `computations/session-105/s105_branch_iv_direct_l1314.npz` + `.py` — S105 ρ_B(12,13,14) + spread_CAC=0.0443091 INFO; the GT builder + Zubarev S85 W0-7 evaluator
3. `sessions/framework/Atlas/atlas-07-permanent-results.md` — §VII.AJ.partition-stability (Friedrich-Bär saturation theorem; bottom-K 4-stratum (2,4,8,6))
4. `computations/session-92/s92_w9_3_friedrich_bar_saturation_unified.py` — the Friedrich-Bär saturation theorem implementation (S87 W11-2/W11-3, S89 W3-1 PASS)
5. `.claude/rules/regulator-convention-lockdown.md` — DR3-class CAC discipline; `.claude/rules/math-scripts.md` — feasibility pre-check
6. The same-wave compute `S116-W9-GTBUILDER-L15` (spread_CAC{13,14,15} + bottom-K saturation cross-check) — cited as evidence if landed

---

## R1 — Opening Positions (steelman your assigned side)

### R1 · spectral-geometer — bottom-K floor SATURATED (p+q=15 redundant) steelman

**Position.** The canonical Q36 observable is the **bottom-K |λ| floor** of D_K at τ_fold = 0.190. It is Friedrich-Bär-saturated at p+q ≤ 14: the bottom-64 floor is identical L≤14 vs L≤15 to `max|diff| = 0.0e+00` (verified from the S106 cache, not merely cited). The p+q=15 shell is a **completeness check that returned its predicted null**, not a new datum. The branch-(iv) w0 Zubarev moment ρ_B does shift — but that shift is a **Weyl-law λ_max truncation artifact**, slaved to the top of a spectrum that is *unbounded above* in the continuum, not a change in any substrate observable. The Friedrich-Bär theorem is a lower-bound theorem; its saturation scope is the bottom-of-spectrum, and invoking it for the λ_max-tail moment is a category error.

#### 1. Governing structure — the observable decomposition is forced by the Weyl density

The D_K spectrum at τ_fold IS the set of substrate vibrational modes (Level-1, single-τ-slice; GEOMETRIC). Any spectral functional splits into two structurally orthogonal classes by *where on the spectrum its weight sits*, and the heat kernel is the Rosetta stone:

```
Tr e^{-σ D_K²} = Σ_k m_k e^{-σ |λ_k|²}                                         (1)
   large σ  →  dominated by |λ|_min  (BOTTOM-of-spectrum / IR)
   small σ  →  dominated by |λ|_max  (WEYL edge / UV; Weyl density ρ(λ) ~ λ^{d-1} = λ^7 at d=8)
```

The bottom-K floor is the σ→∞ / large-s `Tr(D_K^{-2s})` end: it is fixed entirely by the lowest |λ| sectors. The Zubarev moment ρ_B is the *opposite* end — a Gaussian/exponential profile `exp(-x/Λ_Z²)` integrated against the **full** retained spectrum. At d=8 the bottom-K (K = 20–64) is a measure-zero sliver of the ~156k eigenvalues; everything the Zubarev moment weighs lives in the λ⁷-dense bulk and upper spectrum. The two observables sample **disjoint** regions of the same spectrum. This is not a convention choice; it is forced by the d=8 Weyl density. **Eq. (1) is the governing object; the decomposition is its corollary.**

#### 2. The Friedrich-Bär saturation theorem — precise statement and SCOPE

The theorem (S87 W11-2/W11-3, S89 W3-1 PASS; implemented in `s92_w9_3_friedrich_bar_saturation_unified.py`) is, in the Friedrich (1980) / Bär (1992) lower-bound lineage, a **per-sector lower bound on the sector-minimal eigenvalue**:

```
|λ|_min(p,q)  ≥  η_FB_lower · √(C_2(p,q) + 1),     η_FB_lower = 0.392839             (2)
   C_2(p,q) = (p² + q² + pq + 3p + 3q)/3   (SU(3) quadratic Casimir)
   η_FB_lower = ETA_FB_SAFETY · η_floor = 0.9 × 0.4365   (8.4% safety margin below the (1,1) empirical floor)
```

The mechanism: because (2) is a **lower** bound that grows like √C_2 ~ (p+q), every NEW sector at level L = p+q lands at a |λ|_min that *increases* with L. Once the new-sector lower bound exceeds the bottom-K ceiling, no sector at that level or higher can enter the bottom-K — for **all** L ≥ L*, with a margin that *widens* as L grows. That is the saturation: L_max = 14 ≡ L_max → ∞ for the bottom-K observable, certified analytically before any higher sector is built.

**Scope statement (the load-bearing point, and my home turf).** Eq. (2) bounds eigenvalues from **below**. It says exactly nothing about |λ|_max. The top of the truncated spectrum is governed by **Weyl's counting law** (N(λ) ~ C·λ^d; equivalently the per-shell edge max|λ|(L,0) = 0.633·√C_2(L,0) + 0.555 ≈ 0.365·L + 0.555 for large L — linear, unbounded). Friedrich-Bär and Weyl are theorems about *opposite ends* of the spectrum. Therefore:

> **The Friedrich-Bär saturation theorem certifies the bottom-K floor and any bottom-dominated (large-σ / large-s) bulk moment. It is structurally incapable of certifying — or being "violated" by — a λ_max-tail-sensitive moment.** Invoking FB to declare the w0 DR3 Zubarev moment "saturated" (or to read its decelerating decrement as "FB-saturation of the convergence rate") cites a lower-bound theorem to control an upper-spectrum quantity. That is a category error, not a saturation claim.

#### 3. Empirical certification (extracted from `s106_w1_highl_cache_l1416.npz`, this turn)

| quantity | value | reading |
|:--|:--|:--|
| bottom-64 floor `max|diff|` (p+q≤14 vs ≤15) | **0.0e+00** EXACT | the new shell does not touch the bottom-K |
| bottom-20 ceiling (20th-smallest \|λ\|) | 0.8452 | the floor window the substrate physics lives in |
| global smallest \|λ\| | 0.8197 | = the **B1 acoustic band** — the bottom-K IS the framework's band spectrum |
| p+q=15 shell \|λ\|_min | **4.216** | ≫ 0.845 ceiling by factor ~5 |
| FB lower bound on min-C₂ p+q=15 sector (8,7) | 3.341 | (2) certifies the shell is excluded *before* building it; actual 4.216 clears it with margin |
| FB lower bound on p+q=16 (8,8) | 3.536 | p+q=16 is FB-bounded and **NOT BUILT** |

The last row is decisive on its own. The framework **already trusts FB-saturation operationally**: the S106 build certified the entire p+q=16 shell redundant via (2) and never constructed it (`n_fb_bounded = 17`, the full p+q=16 shell). The exact same inequality bounds p+q=15 for the bottom-K. The p+q=15 shell was built *only* as a completeness check, and it returned precisely the FB-predicted null: `max|diff| = 0.0e+00`. A completeness check that confirms the theorem is not a "shift in a canonical observable"; it is the theorem passing its own audit.

#### 4. Why the bottom-K is the canonical Q36 object

The framework's spectral predictions key on the bottom of the spectrum, never on λ_max:

- **§VII.AJ.partition-stability** (the very theorem Q36 invokes): the 4-stratum cardinality vector (2,4,8,6) is a bottom-20 occupation statistic — a *bottom-K* observable by construction.
- **B1/B2/B3 acoustic-color bands** (0.8197 / 0.8452 / 0.978): the low-lying long-wavelength substrate excitations that carry the observable physics.
- **Friedrich-Kirchberg lower bound** 5R/16 = 0.631 vs actual λ₁² = 0.672 — a *first-eigenvalue* (bottom) statement.
- **n_s tilt** is set by the low-|λ| modes.

λ_max, by contrast, has **no continuum limit**: the SU(3) Dirac spectrum is unbounded above, so the largest retained eigenvalue is a pure artifact of where the truncation is cut. A quantity slaved to λ_max is slaved to the truncation boundary, not to the substrate. Direction (substrate-first): `D_K eigenvalues at τ_fold → {bottom-K floor [saturated], λ_max-driven Zubarev moment [drifts with the cut]} → the bottom-K floor is what Q36 is about → FB saturation certifies it`.

#### 5. The w0 "shift" is a Weyl-λ_max artifact — three independent signatures

**(a) ρ_B tracks λ_max, not the bottom.** With the bottom-64 floor pinned to `max|diff| = 0.0`, ρ_B nonetheless moves: ρ_B(13)=−0.656884 → ρ_B(14)=−0.677718 → ρ_B(15)=−0.696174, in lockstep with λ_max = 5.793 → 6.168 → 6.543. A bottom-K observable would be flat (it is, exactly); ρ_B is not, so it is *not* a bottom-K observable. It samples the moving upper edge.

**(b) Exact image of my own prior result (INV8-W3-3).** I previously established that the full heat trace P(σ) is genuinely L_max-dependent (new sectors *add* to the trace), **while** the windowed and bottom observables — d_s(σ_*), the energy-axis γ_E — are L_max-**saturated** to `|Δγ| = 0.00000` across L∈{10,11,12,13}, *because new sectors land above the fold and add zero resolution below it*. That is the identical decomposition: whole-spectrum moments drift; windowed/bottom observables saturate. ρ_B is a whole-spectrum (in fact upper-weighted) moment; the bottom-K floor is the windowed observable. The present case is INV8-W3-3 at p+q=15.

**(c) The CAC proxy drifts AWAY from the physical anchor while its window-spread shrinks.** Under the CAC lockdown (regulator-convention-lockdown.md; w0_cac(L) = ρ_B(L) + offset, offset pinned so w0_cac(10) = w0_FW = −0.918 exactly), the prediction runs `w0_cac: −0.918 @L10 → −0.9757 @L12 → −0.9993 @L13 → −1.0200 @L14` — a monotone drift of 0.102 away from the physical anchor. The physical prediction itself, w0_FW = −0.918, is the closed-form Volovik-partition + effacement (Γ_eff = 0.99970) value and is **L_max-independent by construction** — it is not a truncated spectral moment. So the small window-spread that develops at high L is **stability around a drifted value, not vindication of −0.918**. Even granting that the 3-point window-spread (= two consecutive decrements) will shrink below the 0.025 PASS band at finite L (it is the fixed-width spread of a decelerating sequence, so it must), what "reaches PASS" is the *drift-rate of a truncation artifact slowing enough to look flat over three points* — around a central value 0.10 displaced from the physical prediction. Necessary-but-not-sufficient: a flat artifact is still an artifact.

A consistency check on (a)/(c): Λ_Z = 1.0 ≪ λ_max = 6.168. The Zubarev scale sits far below the spectral edge, yet ρ_B is empirically λ_max-driven — which is itself a signal that the moment is dominated by the λ⁷-dense bulk/upper region where the truncation bites, exactly as Eq. (1) at small effective σ predicts.

#### Questions for baptista (R2 seeds)

1. **Is the λ_max-driven ρ_B a substrate observable or a truncation-Weyl artifact?** λ_max has no continuum limit (the SU(3) Dirac spectrum is unbounded above). How can a quantity slaved to the truncation boundary — and which *drifts away* from the physical w0_FW = −0.918 as the cut is raised — be the canonical falsifier-surface observable, rather than the L_max-independent closed-form −0.918 it is supposed to proxy?

2. **Does the Friedrich-Bär theorem CLAIM to saturate λ_max-tail moments?** Eq. (2) is a *lower* bound; its reach is the bottom and the bottom-dominated bulk. If you read the decelerating decrement as "FB-saturation of the convergence rate," you are invoking a lower-bound theorem to govern an upper-spectrum quantity. Either exhibit the upper-bound companion that licenses that reading, or concede the deceleration is ordinary Weyl-edge slowdown (∂λ_max/∂L ≈ 0.375, decrement ~1/L²-ish) with no FB content.

3. **What singles out L=10 as the CAC anchor, and why is "stability around a drifted value" a vindication rather than a falsification of the proxy?** If w0_cac → −1.02⁺ while the spread → PASS, the gate certifies the artifact has stopped moving fast — around a value 0.10 from −0.918. Reconcile, too, Λ_Z = 1.0 ≪ λ_max = 6.168 with the moment's empirical λ_max-sensitivity: if the Zubarev weight genuinely decoupled the edge, ρ_B would saturate like the bottom-K — it does not.

### R1 · baptista-spacetime-analyst — w0_FW DR3 moment SHIFTS (p+q=15 a genuine datum) steelman

**Position.** Q36 is posed on the **DESI DR3 w0–wa falsifier surface**. The framework's prediction there is w0_FW = −0.918, and the branch-(iv) **Zubarev moment ρ_B(L)** is its spectral-action route (`s105_branch_iv_direct_l1314.py` §"Substrate-first arrow": `D_K eigenvalues at τ_fold → Zubarev branch-(iv) moment ρ_B → CAC-anchored w_0 → DESI DR3 w_0–w_a`). That moment IS the canonical Q36 object, and it **shifts** at p+q=15: ρ_B(14)=−0.677718 → ρ_B(15)=−0.696174. I **grant spectral-geometer's strongest empirical claim in full**: the bottom-K |λ| floor is exactly Friedrich-Bär-saturated — bottom-64 `max|diff| = 0.0e+00`, the p+q=15 shell enters at |λ|_min=4.216 ≫ the 0.845 bottom-20 ceiling and cannot touch the floor. What I deny is the *identification*. The bottom-K floor is **a** canonical framework observable (it carries §VII.AJ.partition-stability, the B-bands, the n_s tilt); it is not **the Q36** observable, because the bottom-K floor does not compute w0. The two are not rivals — they are **orthogonal functionals of one spectrum**, and (the evaluator shows) *literally the numerator and the denominator of ρ_B*. spectral-geometer is right about the bottom; I am right about the edge; FB governs only the bottom; and the p+q=15 datum is the very thing that proves all three.

#### 1. Governing structure — read the evaluator, not the σ-heuristic

spectral-geometer's Eq. (1) (the heat-kernel large-σ/small-σ split) is a *heuristic* for where a functional's weight sits. The actual branch-(iv) functional is not a heat trace; it is the S85 W0-7 Zubarev statistic (`s105…py` lines 288–293, zeta scheme, a_2^{Mellin} poleconv-A-double s=3/n=2):

```
(B1)   ρ_B(L) = mean_Z(L) / λ_max(L) − 1,
       mean_Z(L) = [ Σ_{j: lvl≤L} d_j e^{−|λ_j|²/Λ_Z²} |λ_j| ] / [ Σ_{j: lvl≤L} d_j e^{−|λ_j|²/Λ_Z²} ],   Λ_Z = 1.
```

This is decisive, and it is GEOMETRIC (Level-1, single-τ-slice at τ_fold=0.190). Two structural facts read directly off (B1):

- **mean_Z is the bottom of the spectrum, and it is FROZEN.** The Gaussian kernel `e^{−|λ|²}` at Λ_Z=1 suppresses every mode above |λ|≈2; the entire p+q=15 shell (|λ|≥4.216) enters mean_Z at weight `e^{−4.216²} ≈ 1.9·10⁻⁸`. Back-solving mean_Z = (1+ρ_B)·λ_max from the pinned anchors:

| L | ρ_B(L) | λ_max(L) | mean_Z(L)=(1+ρ_B)·λ_max | decrement \|d\| | law μ·b/λ_max² |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 13 | −0.656884 | 5.793 | **1.987671** | — | — |
| 14 | −0.677718 | 6.168 | **1.987835** | 0.020834 | 0.020842 |
| 15 | −0.696174 | 6.543 | **1.987934** | 0.018456 | 0.018455 |

  mean_Z is constant to 4–5 sig figs (Δ ≈ +9·10⁻⁵ per shell — the residue of the 10⁻⁸-weighted additions). mean_Z lives in exactly the region FB saturates: it is the *same physics* as the frozen bottom-K floor.

- **λ_max is the spectral EDGE, and it is the sole driver of the shift.** Decomposing Δρ_B(14→15) into its two channels (mean_Z held fixed vs λ_max held fixed): the **λ_max channel = 100.1%** of the shift, the **mean_Z channel = −0.1%**. The entire ρ_B shift is the explicit λ_max denominator in (B1), nothing else.

**Substitution chain** (per `math-scripts.md §"Double-Check Logic"`, the [SIGN] claim "ρ_B decreases, decelerating, driven by λ_max with mean_Z frozen"):

```
Step 1  ρ_B(L) = mean_Z(L)/λ_max(L) − 1                          [(B1), s105…py:293]
Step 2  mean_Z(L) ≈ μ = 1.9878 (frozen; new modes weight ~1.9e-8) [table above]
Step 3  ρ_B(L) = μ/λ_max(L) − 1  ⇒  dρ_B/dλ_max = −μ/λ_max² < 0   [μ>0]
Step 4  λ_max(L) ↑ with L: 5.793→6.168→6.543, ∂λ_max/∂L = b = 0.375 (constant) [anchors]
Step 5  dρ_B/dL = (−μ/λ_max²)(+b) < 0  ⇒  |dρ_B| = μ·b/λ_max²
        ⇒ decreasing AND decelerating as 1/λ_max² (law column matches to ratio 0.9999–1.0004).
Conclusion  (B2) |dρ_B/dL| = μ·b/λ_max²,   μ = 1.9878,  b = 0.375.   ∎
```

#### 2. The observable-decomposition is EXACT and forced by (B1) — numerator ⊥ denominator

The decomposition is not a soft "two ends of the spectrum" appeal; it is the algebraic structure of ρ_B:

```
(B3)   ρ_B  =  [ mean_Z  / λ_max ]  − 1
              =  [ BOTTOM region, FROZEN, FB-saturated ] / [ EDGE, Weyl-linear, drifting ] − 1.
```

- **bottom-K floor** = a window observable on the BOTTOM region → FB-saturated (granted, max|diff|=0).
- **mean_Z** = a Gaussian-weighted mean on the SAME bottom region → also frozen (same physics; FB even saturates the *numerator* of ρ_B).
- **the w0 SHIFT** = pure λ_max-denominator drift → the EDGE, a region FB is structurally silent on.

So bottom-K saturation and the w0 shift are **orthogonal by construction**: they are different operations on disjoint spectral regions that happen to be glued into one ratio. spectral-geometer and I are each describing a different factor of (B3). Neither is wrong; the error would be to let either factor speak for the whole.

#### 3. Friedrich-Bär SCOPE — I adopt spectral-geometer's lower-bound statement, and it cuts toward me

I **agree with spectral-geometer's §2 scope statement verbatim**: Eq. (2) is a *lower* bound, `|λ|_min(p,q) ≥ η_FB_lower·√(C_2+1)`; its reach is the bottom-of-spectrum; it says nothing about |λ|_max. Apply it to (B3):

- FB saturates the bottom region ⇒ FB saturates BOTH the bottom-K floor AND mean_Z (the numerator). Good — this is the strongest possible version of spectral-geometer's case, and I concede it.
- FB is silent on λ_max (the denominator) ⇒ FB **cannot adjudicate the w0 shift either way**. It can neither certify it "saturated" nor flag it "violated."

Therefore citing FB to declare the w0 DR3 spread "saturated" (workshop sub-question 2) is a **SCOPE ERROR**, and we both now agree it is. This is a CONVERGENCE point, not a dissent: FB scope = bottom-K + bulk low-|λ| moments (incl. mean_Z); FB ⊥ the λ_max-tail. The dissent is narrower than spectral-geometer framed it — it is *only* about which factor of (B3) is "the Q36 observable," not about FB.

#### 4. Why the w0 moment is the canonical Q36 object — and the deceleration is NOT FB

Two independent arguments that Q36 is about the edge-factor, not the bottom-factor:

**(i) Question-scope.** Q36 is the DESI DR3 w0–wa surface. spectral-geometer's §4 list of bottom-K observables — partition-stability, B1/B2/B3 bands, Friedrich-Kirchberg λ₁, n_s — is a list of things that are *not w0*. None of them maps to the dark-energy equation of state. The branch-(iv) Zubarev moment is the only listed route from D_K to w0 (`s105…py` substrate arrow). A bottom-K observable cannot be "the canonical Q36 object" when it does not compute the Q36 quantity.

**(ii) Institutional.** `regulator-convention-lockdown.md` exists *specifically* for "DR3-class L_max-stability gates — gates whose verdict is a function of **w_0_FW(L_max)** evaluated at two or more values of L_max." That rule is **vacuous unless w0_FW(L_max) varies with L_max.** The framework has codified an entire convention discipline (CAC, offset_Zubarev=−0.340827, RDC FORBIDDEN) around the *premise that the w0 moment is an L_max-varying tracked observable*. The bottom-K floor, being flat, would need no such gate. The DR3 lockdown is institutional proof that the canonical Q36 observable is the moving moment, not the static floor.

**Honest refinement of my own assigned framing.** The seed framed the decelerating decrement as "Friedrich-Bär saturation of the convergence RATE." Having read (B1), I **retract the FB label** — by §3's scope statement FB is a bottom-K lower bound and cannot own the edge-driven rate. The deceleration is the *exact* closed form (B2): `|d| = μ·b/λ_max²`, the analytic derivative of μ/λ_max with μ frozen, matching the data to 0.01%. That is a STRONGER claim than "FB-saturation," not a weaker one: the convergence is not an analogy, it is a closed-form law. (This is the rigorous move — I will not defend an imprecise label on my own side.)

#### 5. p+q=15 is a genuine datum — spectral-geometer's own R1 proves it

The knockout is internal to spectral-geometer's §5(c). That argument computes w0_cac(15) = ρ_B(15) + offset = −1.037001 to show "the proxy drifts." **That computation REQUIRES ρ_B(15) — the p+q=15 datum.** A *redundant* shell leaves the observable bit-for-bit unchanged (precisely what the bottom-K floor does: max|diff|=0.0e+00). ρ_B demonstrably changes by 0.018456. You cannot simultaneously hold "p+q=15 is redundant" and run a central-drift argument that is *powered by* ρ_B(15). Redundancy and informativeness are mutually exclusive; spectral-geometer's strongest signature establishes informativeness.

And the datum is informative in a specific, valuable way: the trio {13,14,15} is exactly what lets us *prove* mean_Z is frozen (table §1), extract the closed-form law (B2), and locate the asymptote. Redundant data cannot yield a convergence theorem.

**The honest concession, and why it ELEVATES the datum.** I grant spectral-geometer's §5(c) substance: with mean_Z frozen, (B1) gives ρ_B → −1 as λ_max → ∞, so w0_cac → **−1.341** — a genuine drift away from the −0.918 anchor. But this is an **anchor-fidelity** question (does the proxy asymptote to the closed-form value?), structurally distinct from the **L_max-stability** question the DR3 gate actually tests (is the spread small?). The DR3 spread is convergent (§6 below). The anchor-fidelity gap is real, open, and — here is the point — **was surfaced by the deep-truncation data**. p+q=15 did not pass a completeness check and return null; it returned the number that exposes a proxy-design question invisible at L≤12. That is the opposite of redundant.

The gap is even *constructive*. Because the drift is 100% the running λ_max(L) denominator while mean_Z is frozen from early L, re-referencing the Zubarev normalization edge to the physical cache value λ_max(L=10) — i.e. ρ_B^{fixed-edge}(L) = mean_Z(L)/λ_max(10) − 1 — would yield a **frozen** moment (mean_Z frozen ⇒ ρ_B^{fixed-edge} ≈ ρ_B(10) for all L) and hence w0_cac ≡ −0.918, PASS and flat. Whether the substrate-correct normalization is the running edge or the fixed physical-cache edge is a proxy-design compute (a clean S117 carry-forward, NOT an in-gate convention switch — the current CAC is correct per the lockdown). Only the L≥13 data could pose it.

#### 6. Convergence — the spread reaches PASS at finite L (we agree it converges)

spectral-geometer §5(c) concedes the spread "will shrink below the 0.025 PASS band at finite L … it must." (B2) makes this precise: the sliding 3-point window spread ≈ |d_{L-1}|+|d_L| = μb(λ_max(L-1)⁻²+λ_max(L)⁻²), and `Σ 1/λ_max² < ∞`. The pinned data already show the slide: spread_CAC{12,13,14}=0.0443 (S105) → spread_CAC{13,14,15}=0.039290 (this wave). Projecting (B2) with λ_max(L)≈0.375L+0.918, PASS (≤0.025) is reached at window {17,18,19}, **L≈19**. So verdict cell 4 = **convergent (→PASS at finite L)**, and this is a CONVERGENCE point with spectral-geometer.

The operational caveat is build-horizon, not non-convergence: at present the window is INFO. But the extension is *more feasible than full-spectrum reconstruction*, because the global edge λ_max(L) is set by the (L,0)/(0,L) symmetric sectors — C_2(p,q) is maximal at fixed level p+q for (L,0) (C_2(L,0)=L(L+3)/3 > C_2(p,L−p) for 0<p<L) — and those are exactly the GT-direct (p,0) bosonic-ladder sectors built wall-free in `s105…py` §5a. mean_Z is frozen, so tracking ρ_B to the PASS window needs only λ_max(L), i.e. the cheap symmetric tops. This makes CF-S117-BRANCH-IV-L16 (and reaching the PASS window) tractable.

#### Answers to spectral-geometer's R1 questions

- **Q1 (substrate observable or Weyl artifact?).** A false dichotomy. ρ_B(L) is a deterministic functional of the τ_fold spectrum at each truncation — substrate-IS at every L. Its L_max-dependence is *regulator-dependence*, intrinsic to every spectral-action moment (Tr f(D/Λ) is Λ-dependent by construction; physics is read at the physical Λ, never at Λ→∞, which diverges). "Must be L_max-independent or it is an artifact" is a demand the spectral-action methodology rejects. λ_max indeed has no continuum limit; ρ_B's limit is the trivial −1, and the framework reads the prediction at its canonical truncation, not at the limit. The drift to −1.341 is a proxy-fidelity question (§5), not grounds to deny the per-L value is substrate. And it is the Q36 object because Q36 is the w0 surface, which the bottom-K does not address.

- **Q2 (does FB claim to saturate λ_max-tail moments?).** No — and I do not claim it does. I adopt your lower-bound scope statement (§3): FB saturates the bottom (including mean_Z, the numerator) and is silent on λ_max. I therefore **concede the deceleration has no FB content** — but it is not "ordinary Weyl-edge slowdown" either. It is the exact law (B2) `|d|=μb/λ_max²` from the μ/λ_max form with μ frozen — a closed-form convergence law, verified to 0.01%. No FB; better than "slowdown."

- **Q3 (what singles out L=10; is "stability around a drifted value" vindication?).** L=10 is not arbitrary: it is the framework's canonical cache (the 155,984-eigenvalue L_max=10 spectrum at which *all* framework observables are evaluated), and the CAC offset anchors there by construction. "Stability around a drifted value" is **L_max-stability** (the DR3 gate's actual target) — genuine substrate information about the moment's convergence. **Anchor-fidelity** (does it asymptote to −0.918?) is a separate question; I concede it is open and route it to S117. The Λ_Z=1 ≪ λ_max "paradox" dissolves under (B1): mean_Z *is* bottom-localized and frozen (Λ_Z=1 doing its job); ρ_B is λ_max-sensitive through the explicit denominator, not through bulk/edge weighting. There is no contradiction — your §5(b) "upper-weighted bulk-dominated moment" reading is refuted by the 100.1%/−0.1% channel split: the numerator is as bottom-localized as the FB-saturated floor.

#### Questions for spectral-geometer (R2 seeds)

1. **Redundancy vs your own §5(c).** Your central-drift argument computes w0_cac(15) from ρ_B(15). A redundant shell leaves the observable unchanged (the bottom-K floor: max|diff|=0); ρ_B changes by 0.018456. How is the datum that *powers your drift argument* simultaneously "redundant"? Reconcile "p+q=15 is a completeness check that returned its predicted null" with §5(c)'s reliance on ρ_B(15).

2. **Numerator vs denominator.** Back-solving (B1), mean_Z = 1.98767, 1.98784, 1.98793 — frozen to 5 sig figs across {13,14,15}, with the shift carried 100.1% by the explicit λ_max denominator (μ·b/λ_max² to 0.01%). This refutes "the moment is dominated by the λ⁷-dense bulk" (§5(b)/your consistency check): the numerator is as bottom-localized as the FB-saturated floor; the λ_max-dependence is a *normalization choice* (S85 W0-7), not bulk weighting. Do you accept that FB saturates the numerator (mean_Z) while being structurally silent on the denominator (λ_max) — so "FB saturates the w0 moment" is precisely the scope error we both reject?

3. **Anchor-fidelity as the real open question.** (B1) gives ρ_B → −1, w0_cac → −1.341 — a closed-form anchor-fidelity gap that *only the deep-truncation data* could surface, and that a fixed-edge normalization ρ_B^{fixed-edge}=mean_Z/λ_max(10)−1 would close (frozen mean_Z ⇒ w0_cac ≡ −0.918, PASS). Do you agree this is (a) a genuine S117 carry-forward, and (b) reachable only from L≥13 data — making p+q=15 the most informative branch-(iv) datum since L=12, not a redundant completeness check?

---

## R2 — Rebuttal (engage the opponent's strongest case)

### R2 · spectral-geometer

#### CONVERGENCE

I grant baptista's R1 decomposition in full. I verified it independently this turn rather than accepting it on assertion — as the spectral-geometer I concede nothing I have not checked against exact numbers.

**The decomposition ρ_B = mean_Z/λ_max − 1 (baptista R1 (B1)) is algebraically EXACT, and I confirm it from the pinned anchors.** Back-solving mean_Z = (1+ρ_B)·λ_max:

| L | ρ_B | λ_max | mean_Z = (1+ρ_B)·λ_max | baptista R1 §1 |
|:-:|:-:|:-:|:-:|:-:|
| 13 | −0.656884 | 5.793 | 1.987671 | 1.987671 ✓ |
| 14 | −0.677718 | 6.168 | 1.987835 | 1.987835 ✓ |
| 15 | −0.696174 | 6.543 | 1.987934 | 1.987934 ✓ |

mean_Z is frozen to Δ ≈ +1·10⁻⁴ per shell. The channel split is exact: holding mean_Z=mean_Z(14) and moving λ_max 6.168→6.543 gives Δρ_B = 1.987835/6.543 − 1.987835/6.168 = −0.018471 = 100.08% of the total −0.018456; the mean_Z channel contributes (1.987934−1.987835)/6.543 = +1.5·10⁻⁵ = −0.08%. baptista's 100.1%/−0.1% (R1 §1, §2) holds to the digit. His closed-form law (B2) is the exact finite difference μ(1/λ_max(14) − 1/λ_max(15)) = μ·b/(λ_max(14)·λ_max(15)) = 1.9878·0.375/40.36 = 0.018470 vs actual 0.018456 — the 0.08% residue is precisely the non-frozen part of mean_Z. The decomposition is not a soft "two ends of the spectrum" appeal; it is an identity, and the data sit on it to four decimals.

**My bottom-K saturation IS the frozen numerator.** This is the geometric core of the convergence. The Zubarev numerator mean_Z is a Gaussian-weighted mean with kernel e^{−|λ|²/Λ_Z²}, Λ_Z=1. At Λ_Z=1 every mode above |λ|≈2 is suppressed by e^{−4}≈0.018; the entire p+q=15 shell (|λ|_min=4.216) enters mean_Z at weight e^{−4.216²}≈1.9·10⁻⁸. So mean_Z is a BOTTOM-LOCALIZED functional — it lives in exactly the spectral region my bottom-K floor occupies. Friedrich-Bär saturation of the bottom-K floor (max|diff|=0.0e+00) and the freezing of mean_Z are the SAME phenomenon: the bottom of the τ_fold spectrum is fixed at p+q≤14, so any bottom-localized functional of it — the floor (a min-K window) OR the heat-kernel-weighted mean (a Gaussian window) — is fixed. My §VII.AJ saturation result saturates baptista's *numerator*, not merely the floor. We are describing one frozen object through two windows.

**baptista's w0 shift IS the λ_max denominator, and his knockout (R1 §5) lands.** I concede it without reservation: my own R1 §5(c) drift argument computes w0_cac(15) = ρ_B(15) − 0.340827 = −1.037, and that computation REQUIRES ρ_B(15). A shell that left the observable bit-for-bit unchanged — which is exactly what the bottom-K floor does (max|diff|=0) — cannot POWER a 0.018456 drift. Redundancy and informativeness are mutually exclusive on a *fixed* observable; I cannot hold "p+q=15 redundant" while running a drift argument fueled by ρ_B(15). The resolution is the decomposition: **redundancy is observable-dependent.** p+q=15 is redundant for the bottom-K floor (Δ=0, FB-certified null) AND informative for the w0 moment (Δρ_B=0.018456 ≠ 0, pure λ_max-denominator drift). Both hold because they are statements about different factors of (B3).

**Self-correction (rigor demands it).** My R1 §5(b) and the §5 consistency check claimed ρ_B "is dominated by the λ⁷-dense bulk/upper region." baptista's channel split (R1 §2, §3, Q2) refutes this and I withdraw it: the numerator is as bottom-localized as the FB-saturated floor (it *is* mean_Z, frozen), and the λ_max-dependence enters through the explicit normalization denominator, NOT through bulk weighting. The Λ_Z=1 ≪ λ_max "paradox" I posed in R1 dissolves exactly as baptista says (R1 Q3): Λ_Z=1 is doing its job — it bottom-localizes the numerator; the edge-sensitivity is a normalization choice in the S85 W0-7 statistic, not a bulk-weighting of the moment. My Eq. (1) heat-kernel split was the right intuition for WHERE FB reaches, but the wrong diagnosis of ρ_B's λ_max-sensitivity, which is denominator-explicit, not weight-implicit.

#### DISSENT

The substantive disagreement has converged. What remains is a scope sharpening (now shared) and one structural claim I OWN that strengthens baptista's case rather than opposing it.

**FB scope — converged, sharpened.** baptista adopts my R1 §2 lower-bound scope statement verbatim (R1 §3); I adopt his refinement. The precise joint statement: Eq. (2), |λ|_min(p,q) ≥ η_FB_lower·√(C_2+1), is a LOWER bound; its reach is the bottom-of-spectrum. It therefore saturates BOTH the bottom-K floor AND mean_Z (the Gaussian-weighted bottom mean is governed by the same frozen low-|λ| sectors). It is structurally SILENT on λ_max (the Weyl edge — the opposite end, governed by N(λ)~λ^d, not by a Casimir lower bound). Hence FB is correctly scoped to the NUMERATOR of (B3) and cannot adjudicate the DENOMINATOR either way. **Answer to baptista's Q2: yes — "FB saturates the w0 moment" is a scope error**, because it reads a numerator-governing lower-bound theorem as governing the full ratio. We both reject it. This is now a convergence point with a sharpened statement, not a live dissent.

**The "canonical Q36 observable" question dissolves — I concede BOTH.** I no longer hold that the bottom-K floor is THE Q36 observable. The decomposition shows bottom-K and w0 are the frozen-numerator and the running-ratio of one functional; both are substrate-IS, both canonical — for DIFFERENT falsifier surfaces. baptista's question-scope argument (R1 §4(i)) is correct: Q36 is posed on the DESI DR3 w0–wa surface, and none of my R1 §4 bottom-K observables (partition-stability, B1/B2/B3, Friedrich-Kirchberg λ₁, n_s) computes w0. For Q36-as-posed the operative object is the w0 moment. But the bottom-K is not absent from it — it is the *numerator's stability certificate* (mean_Z frozen because the bottom is FB-saturated). Honest verdict: BOTH, with declared roles — bottom-K canonical for the partition/band/tilt surface; w0 moment canonical for the DR3 surface; bottom-K saturation is what makes the w0 numerator trustworthy.

**What I now OWN (genuine residual, strengthening baptista): the anchor-fidelity gap is WEYL-FORCED, not merely "open."** baptista surfaced the gap (R1 §5: ρ_B → −1 ⇒ w0_cac → −1.341) and routed it to S117 as "open." I sharpen it to a theorem of my domain. The numerator mean_Z is fixed (FB-saturated, a finite IR scale ≈ 1.9879). The denominator λ_max is the Weyl edge, which grows linearly WITHOUT BOUND: empirically ∂λ_max/∂L = 0.375 (5.793→6.168→6.543), consistent with the per-shell edge fit max|λ|(L,0) = 0.633√C_2(L,0)+0.555 ≈ 0.37·L (C_2(L,0)=L(L+3)/3, so √C_2 ~ L/√3; (15,0): 0.633·√90+0.555=6.56 vs λ_max(15)=6.543, within the ±5% band). Therefore

> **ρ_B = (fixed IR scale)/(running Weyl edge) − 1 → 0⁺ − 1 = −1, FORCED by Weyl's law.**

w0_cac → −1 − 0.340827 = −1.341 is then forced: an anchor-fidelity gap of 0.423 from the L_max-INDEPENDENT closed form w0_FW = −0.918 (Volovik partition + effacement Γ_eff=0.99970). This is not a contingent drift to be discovered empirically at higher L — it is the unavoidable asymptotic of ANY (bottom-localized)/(Weyl-edge) normalization. The deep-truncation trio {13,14,15} did not "show a drift"; they confirmed the two ingredients (mean_Z frozen, λ_max linear) that make the −1 limit a structural certainty.

**The load-bearing distinction both sides now hold: L_max-stability ≠ anchor-fidelity.** The DR3 gate tests the SPREAD (≤0.025?). Because |d| = μb/λ_max² ~ 1/L² is summable (Σ 1/λ_max² < ∞), the 3-point spread converges and reaches PASS at finite L (spread_CAC{13,14,15}=0.039290, decelerating; my recompute brackets first PASS at window ≈{18,19,20}, L≈19–20, consistent with baptista R1 §6 "L≈19"). So on STABILITY the gate is convergent. But the value it stabilizes AROUND drifts to −1.341, not −0.918. PASS-on-stability is a Weyl-driven artifact slowing enough to look flat over a finite window — necessary but not sufficient for vindicating −0.918. This was my R1 §5(c) "a flat artifact is still an artifact"; baptista granted its substance (R1 §5). It is now a SHARED epistemic pin: the INFO→PASS transition certifies stability, NOT fidelity.

#### EMERGENCE

The two readings are not rival theories of one observable; they are the numerator and denominator of one exact ratio, and the workshop's joint position IS the ratio. GEOMETRIC, Level-1 single-τ-slice: `D_K eigenvalues at τ_fold (p+q=15 shell) → {mean_Z [bottom-localized, FB-frozen], λ_max [Weyl edge, drifting]} → ρ_B = mean_Z/λ_max − 1 → w0_cac → DESI DR3 surface`. Both factors are substrate-IS functionals of the same spectrum; neither is a measurement "in" a container.

**The exact observable-decomposition (joint seed):**

```
ρ_B   =   mean_Z      /     λ_max     −  1
          └ bottom ┘         └ edge ┘
          FROZEN              DRIFTING
          (FB-saturated)      (Weyl-linear, ∂λ_max/∂L=0.375)
          = spectral-geom.    = baptista's w0 shift
            bottom-K, as a      (100.1% of Δρ_B)
            Gaussian window
```

- **bottom-K ⟷ mean_Z, FB-saturated.** The bottom-K floor (min-K window) and mean_Z (Gaussian window) are two windows on the SAME FB-frozen low-|λ| sectors; max|diff|=0 and Δmean_Z~10⁻⁴ are one saturation. The same-wave compute **S116-W9-GTBUILDER-L15** confirms both empirically: bottom-K floor max|diff|=0.0e+00 (saturated) AND the GT-pure (15,0)/(0,15) sentinel = 0.0 exact — the symmetric tops that SET λ_max (C_2(L,0) is maximal at fixed level) are bit-reproduced, so both factors of (B3) are certified at p+q=15.
- **w0-shift ⟷ λ_max, Weyl-drifting, convergent.** The denominator is the Weyl edge; its drift is 100.1% of the w0 shift, decelerating as μb/λ_max² ~ 1/L², summable ⇒ PASS on the spread at finite L (≈L 19–20).
- **FB scope = the numerator side ONLY.** FB (a Casimir lower bound) governs mean_Z and the bottom-K; it is structurally silent on the Weyl edge λ_max. Citing FB to call the w0 spread "saturated" conflates the numerator certificate with the full ratio.
- **Both observables substrate-IS; "which matters" is observable-dependent.** bottom-K is canonical for the partition/B-band/n_s surface; the w0 moment is canonical for the DESI DR3 surface; p+q=15 is null for the first, informative for the second. Q36's answer is a function of which falsifier surface you stand on.

**Engaging baptista's anchor-fidelity find (R1 §5, Q3) — yes, it is a genuine, separable finding, and it is the workshop's real discovery.** I agree on both counts and add the structural certificate:

- (a) **Genuine S117 carry-forward, NOT an L_max-stability question.** The DR3 gate's surface (the spread) converges; the anchor-fidelity surface (does the proxy asymptote to −0.918?) is a DISTINCT, Weyl-forced surface that FAILS to −1.341. These are two different Level-3 anchor questions; the current 4-row Structural Verdict table conflates them in the single "convergence" cell. I propose the verdict carry an explicit anchor-fidelity note/row: "spread convergent (→PASS, L≈19–20); anchor-fidelity Weyl-forced to −1.341 under running-edge normalization — OPEN, route to S117."
- (b) **Reachable ONLY from L≥13 data.** Certifying the −1 limit needs THREE points to establish mean_Z frozen AND λ_max linear *simultaneously*; two points cannot separate a frozen-numerator/linear-denominator drift from a generic convergent sequence. So p+q=15 is the most informative branch-(iv) datum since L=12 for the DR3 surface — and simultaneously the FB-predicted null for the bottom-K surface. Both, by the decomposition.
- The constructive corollary baptista noted (R1 §5: fixed-edge ρ_B^{fixed-edge}=mean_Z/λ_max(10)−1 freezes the moment ⇒ w0_cac≡−0.918, PASS-and-flat) is the Weyl-forced reading inverted: stop the denominator running and only the FB-frozen numerator survives. From spectral geometry that is the natural choice IF the physical content is the bottom-localized mean (it is) — but I will not pre-judge a definition; it is a proxy-design compute, well-posed *precisely because the gap is structural*.

**Answers to baptista's R1 questions (consolidated):** Q1 — conceded; redundancy is observable-dependent; my §5(c) is powered by the denominator-drifting factor, not the frozen one. Q2 — yes; FB saturates mean_Z (Gaussian-windowed bottom) and is silent on λ_max; "FB saturates the w0 moment" is the scope error we jointly reject; I retract my §5(b) bulk-dominated reading. Q3 — yes (a) genuine S117 carry-forward, elevated to Weyl-forced; yes (b) reachable only from L≥13, making p+q=15 maximally informative for DR3.

**Sharper questions for R3:**

1. **Is the S117 compute "running vs fixed edge," or "edge-normalization at all"?** The fixed-edge proxy freezes ρ_B at ρ_B(10) by holding the denominator — but that merely RELOCATES the L_max-dependence into the choice of which λ_max(L\*) to fix. Since mean_Z is the FB-frozen physical content and λ_max has no continuum limit, is the substrate-correct branch-(iv) statistic perhaps one that does NOT normalize by the spectral edge at all (the −1 offset + λ_max division being an artifact of the S85 W0-7 Zubarev DEFINITION rather than substrate physics)? Frame the S117 carry-forward as the broader proxy-design question, not just running-vs-fixed.

2. **Should the Structural Verdict separate stability from fidelity?** Given the spread converges (→PASS) while the central value is Weyl-forced to −1.341, the single "w0 DR3 spread convergence" cell cannot express the result. Do you (as R3-B verdict-writer) agree the table needs an explicit anchor-fidelity row — "convergent on L_max-stability ⊥ Weyl-forced anchor-fidelity gap (OPEN)" — so downstream consumers do not read PASS-on-spread as vindication of −0.918?

### R2 · baptista-spacetime-analyst
#### CONVERGENCE

The substantive physics has converged. I verified spectral-geometer's R2 independently this turn rather than granting it on assertion — and the data sit on the decomposition.

**1. The exact decomposition — re-verified, not asserted.** I re-ran the back-solve mean_Z = (1+ρ_B)·λ_max and the two-channel split from the pinned anchors this turn:

| L | ρ_B | λ_max | mean_Z=(1+ρ_B)·λ_max |
|:-:|:-:|:-:|:-:|
| 13 | −0.656884 | 5.793 | 1.987671 |
| 14 | −0.677718 | 6.168 | 1.987835 |
| 15 | −0.696174 | 6.543 | 1.987934 |

mean_Z spread across {13,14,15} = **2.63·10⁻⁴** (frozen). Channel split 14→15: λ_max channel = −0.018471 = **100.08%** of Δρ_B; mean_Z channel = +1.6·10⁻⁵ = **−0.09%**. spectral-geometer's R2 CONVERGENCE table and channel arithmetic match mine to the digit; (B1) ρ_B = mean_Z/λ_max − 1 is an algebraic identity (`s105…py:50–51,293`) and the data lie on it to four decimals. CONVERGED.

**2. spectral-geometer's geometric identification is the workshop's core, and I sign it without reservation: "my bottom-K saturation IS the frozen numerator."** The bottom-K floor (a min-K window) and mean_Z (a Gaussian window, kernel e^{−|λ|²/Λ_Z²}, Λ_Z=1) are two windows on the SAME FB-frozen low-|λ| sectors — the entire p+q=15 shell enters mean_Z at weight e^{−4.216²}≈1.9·10⁻⁸. FB-saturation of the floor (max|diff|=0.0e+00) and the freezing of mean_Z (Δ~10⁻⁴) are ONE phenomenon through two windows. spectral-geometer's §VII.AJ saturation result saturates my *numerator*, not merely "a different observable." CONVERGED.

**3. FB scope — converged and sharpened (jointly held).** Eq. (2) |λ|_min ≥ η_FB_lower·√(C_2+1) is a LOWER bound; it saturates BOTH the bottom-K floor AND mean_Z (numerator); it is structurally SILENT on λ_max (the Weyl edge, N(λ)~λ^d). Citing FB to declare the w0 DR3 spread "saturated" reads a numerator-governing lower-bound theorem as governing the full ratio — a SCOPE ERROR we both reject. Shared statement, not a dissent.

**4. The "canonical Q36 observable" dissolves into observable-dependence — I confirm BOTH.** I never claimed the bottom-K was THE Q36 object (R1 §4); spectral-geometer's R2 now concedes the w0 moment is the operative object for Q36-as-posed (DESI DR3 surface) while keeping the bottom-K as the numerator's stability certificate. Joint resolution, which I sign: **redundancy is observable-dependent.** p+q=15 is FB-redundant for the bottom-K floor (Δ=0) AND informative for the w0 moment (Δρ_B=0.018456, 100.08% λ_max-denominator). bottom-K canonical for the §VII.AJ.partition-stability / B-band / n_s surface; w0 moment canonical for the DESI DR3 surface.

**5. I accept spectral-geometer's R2 self-correction.** spectral-geometer withdrew the R1 §5(b) "ρ_B dominated by the λ⁷-dense bulk" reading. The 100.08%/−0.09% channel split settles it: the numerator is as bottom-localized as the FB-saturated floor; the λ_max-dependence is denominator-explicit normalization (the S85 W0-7 statistic), NOT bulk weighting. The Λ_Z=1 ≪ λ_max "paradox" dissolves exactly as I argued (R1 Q3) and spectral-geometer now grants.

**6. One self-correction of my OWN R1 §6 (rigor cuts both ways).** My R1 §6 located the first PASS window at {17,18,19}, L≈19. My fresh projection (λ_max(L)=0.375L+c, spread=|d_{L-1}|+|d_L|, μ≈1.9879) gives window {17,18,19}=0.02542 (still INFO) and window **{18,19,20}=0.02310 (first PASS)**. spectral-geometer's R2 bracket {18,19,20}, L≈19–20 was the more accurate call; I adopt it. First PASS at window **{18,19,20}, L≈20** — the convergence is real and at finite L. CONVERGED.

#### DISSENT

The substantive disagreement is gone. One residual remains, and it is CLASSIFICATORY, not physical: **where the anchor-fidelity gap lives in the verdict structure.**

I ACCEPT spectral-geometer's R2 sharpening of my own find. I surfaced (R1 §5) ρ_B → −1 ⇒ w0_cac → −1.341 and called it "open"; spectral-geometer R2 sharpened it to **Weyl-forced** — mean_Z frozen (finite IR scale ≈1.9879) over λ_max linear-unbounded (∂λ_max/∂L=0.375) ⇒ ρ_B = (fixed IR)/(running Weyl edge) − 1 → −1, structurally forced, not contingent. I re-verified the asymptote this turn: w0_cac → **−1.340827**, a gap of **0.422827** from the L_max-independent closed form w0_FW = −0.918. The sharpening is correct and strengthens the find; I adopt "Weyl-forced."

**The dissent: the Weyl-forced anchor-fidelity gap is a SEPARATE Level-3 finding, NOT a Q36 verdict-row.** spectral-geometer R2 Q2 proposes the 4-row Structural Verdict TABLE carry an explicit anchor-fidelity ROW. I agree the result must be VISIBLE (the shared pin below demands it), but I dissent from seating it as a co-equal Q36 verdict cell, on a precise structural ground:

- **Level-collision.** In the cross-pillar-bridge 3-level ladder, **L_max-stability is a Level-2 statement** (the algebraic-envelope convergence RATE: |d|~μb/λ_max² summable ⇒ spread → PASS). **Anchor-fidelity is a Level-3 statement** (does the empirical anchor asymptote to the physical −0.918?). They live at DIFFERENT rungs. The 4 pre-registered Q36 cells answer the Level-2 question — the DR3 gate's pre-registered object per `regulator-convention-lockdown.md` is the SPREAD. Seating a Level-3 anchor question as a Level-2 verdict row is a level-collision.
- **Pre-registration scope.** Q36-as-posed asks "does p+q=15 shift a canonical observable, or is it FB-redundant?" The answer is the decomposition + FB-scope + convergence-on-spread — the 4 cells. The anchor-fidelity gap is a CONSEQUENCE the deep data SURFACED, not the question asked. Folding it into the verdict TABLE retroactively widens the gate's pre-registered scope.

So the dissent is narrow: against COLLAPSING the two surfaces into one cell, NOT against spectral-geometer's (correct) demand for visibility. As R3-B verdict-writer I commit to: the 4-row table stays the Q36 verdict; I add an explicit **anchor-fidelity NOTE** beneath the convergence row + a distinct **Open-Question** + a **separate carry-forward**, each tagged "distinct Level-3 surface (anchor-fidelity ≠ L_max-stability), Weyl-forced to −1.341, OPEN, S117." That delivers exactly the protection spectral-geometer wants — no reading PASS-on-spread as vindication of −0.918 — WITHOUT a level-collision in the verdict cells. On substance (visibility, separability, Weyl-forced) we fully agree; the dissent is purely placement.

**Answering spectral-geometer R2 Q1 (S117 framing — "running vs fixed edge, or edge-normalization at all?").** spectral-geometer is right to broaden it; I adopt the broader frame. The −1 offset + λ_max-division IS the S85 W0-7 Zubarev DEFINITION (`s105…py:50–51,293`), not substrate-forced. The fixed-edge proxy ρ_B^{fixed}=mean_Z/λ_max(10)−1 freezes to ρ_B(10) ⇒ w0_cac ≡ −0.918 (PASS-and-flat), but it merely RELOCATES the L_max-dependence into WHICH λ_max(L\*) one fixes — spectral-geometer's point lands. CF-S117 is therefore the BROAD proxy-design question: should branch-(iv) reference the spectral edge at all, given mean_Z carries the FB-frozen physical content and λ_max has no continuum limit? Running-edge / fixed-edge / no-edge-normalization are three axes of ONE design question. NOT an in-gate convention switch — the current CAC is correct per the lockdown; the carry-forward POSES and COMPUTES the design question, it does not pre-judge it.

**Shared epistemic pin (I accept spectral-geometer R2 verbatim).** "The INFO→PASS transition certifies stability, NOT fidelity." PASS-on-spread is a Weyl-driven artifact slowing enough to look flat over a finite window — necessary but not sufficient for vindicating −0.918. This is exactly WHY the anchor-fidelity gap must be a separate, visible finding: a consumer who sees the spread reach PASS at L≈20 must NOT read it as the prediction converging to −0.918. It is converging to −1.341. Held jointly.

#### EMERGENCE

The two readings were never rival theories of one observable; they are the numerator and denominator of one exact ratio, and the workshop's joint position IS the ratio. GEOMETRIC, Level-1 single-τ-slice — both factors are substrate-IS functionals of the same D_K spectrum at τ_fold, neither a measurement "in" a container:

```
ρ_B   =   mean_Z      /     λ_max     −  1
          └ bottom ┘         └ edge ┘
          FROZEN (FB-sat.)    DRIFTING (Weyl-linear, ∂λ_max/∂L=0.375)
          = bottom-K, as a    = the w0 shift
            Gaussian window      (100.08% of Δρ_B)
```

I co-sign spectral-geometer's R2 EMERGENCE seed and add the level-structure:

- **bottom-K ⟷ mean_Z — FB-saturated, EXACT.** Two windows (min-K and Gaussian) on the SAME FB-frozen low-|λ| sectors; max|diff|=0.0e+00 and Δmean_Z=2.63·10⁻⁴ are ONE saturation. The same-wave compute **S116-W9-GTBUILDER-L15** (INFO; verdict canonical, audit_sha256 94ed48e7…, sign=PASS magnitude=INFO regime=VALID) certifies BOTH factors at p+q=15: bottom-K floor max|diff|=0.0e+00 (numerator saturated) AND the GT-pure (15,0)/(0,15) sentinel = 0.0 exact — the symmetric tops that SET λ_max (C_2(L,0) maximal at fixed level) are bit-reproduced (denominator certified).
- **w0-shift ⟷ λ_max — Weyl-drifting, convergent.** 100.08% of Δρ_B is the explicit λ_max denominator; the closed-form law |d|=μb/λ_max² (0.020862 / 0.018471 vs actual 0.020834 / 0.018456; residual = the non-frozen 10⁻⁴ of mean_Z) is summable ⇒ spread → PASS at window {18,19,20}, L≈20.
- **FB SCOPE = numerator/bottom-K side ONLY.** A Casimir lower bound; governs mean_Z and the floor; structurally silent on the Weyl edge. "FB saturates the w0 spread" conflates the numerator certificate with the full ratio.
- **Q36 "matters" is observable-dependent.** bottom-K canonical for partition/B-band/n_s; w0 moment canonical for DESI DR3; p+q=15 null for the first, maximally-informative for the second — reachable only from L≥13 (three points are needed to separate frozen-numerator / linear-denominator from a generic convergent sequence; spectral-geometer R2 EMERGENCE (b), co-signed).
- **The anchor-fidelity gap is the workshop's real DISCOVERY — a separate Level-3 surface.** Weyl-forced to −1.341 (gap 0.422827 from −0.918); a distinct rung from the Level-2 L_max-stability convergence; surfaced ONLY by the deep-truncation data. It is an explicit annotation + Open-Question + carry-forward, NOT a Q36 verdict cell (per DISSENT).

**Carry-forwards (math, → S117):**

- **CF-S117-BRANCH-IV-L16** — *What*: build the p+q=16 FB-bounded shell (17 sectors, analytic-tail-only in `fb_bounded_sectors`); form spread_CAC{14,15,16}; test the |d|~1/λ_max² deceleration continues toward the {18,19,20} PASS window. *Inputs*: reuse `irrep_symmetric_power_gt` + `rho_zubarev_from_sectors` + `build_dirac_pipeline` verbatim from `s105…py`; mean_Z frozen ⇒ only λ_max(16) needed, set by the wall-free GT-direct (16,0)/(0,16) symmetric tops. *Gate*: |d(15→16)| within 5% of μb/λ_max(16)². *Effort*: low (one shell, one evaluator call).
- **CF-S117-BRANCH-IV-PROXY-DESIGN** — *What*: the broad edge-normalization question (spectral-geometer R2 Q1) — does branch-(iv) reference λ_max at all? Compute ρ_B under {running-edge [current CAC], fixed-edge mean_Z/λ_max(10)−1, no-edge-normalization}; report each variant's w0_cac asymptote + DR3 spread. *Inputs*: mean_Z(L), λ_max(L) trajectories {10..15} (+ L=16 from the above). *Gate*: pre-registered — which normalization yields an L_max-independent w0_cac that asymptotes to the substrate-physical value? NOT an in-gate convention switch (current CAC correct per lockdown). *Effort*: medium (3 normalization variants on existing trajectories).

**Effected-in-session (non-math; routed, NOT executed by me — curated-doc discipline):**

- The **Friedrich-Bär saturation-theorem SCOPE note** is a JOINT workshop × compute reading on the §VII.AJ.partition-stability registry surface (`atlas-07-permanent-results.md:675`; connes + mack SOURCE-DOUBLE-CITE-CO-PRIMARY, PERMANENT). Precise statement to land: *"FB saturation (§VII.AJ.partition-stability) scope = the bottom-K floor + bulk low-|λ| moments (incl. the Zubarev numerator mean_Z); it is a Casimir LOWER bound and is structurally SILENT on λ_max-tail-sensitive moments (the branch-(iv) w0 Zubarev moment). Do NOT cite FB to declare a λ_max-driven moment 'saturated.'"* The §VII surface is mack-cosmic-bridge's SOLE-writer domain (`feedback_mack-bridge-role.md`) → route to `session-116-housekeeping.md §A` for the orchestrator's mack dispatch. I do NOT edit the curated §VII surface; I specify + route.

**Final question for Round 3 (to spectral-geometer — your Weyl-edge turf).** The proxy-design verdict hinges on what λ_max(L) PHYSICALLY IS in the branch-(iv) → w0 map, and the two readings decide whether CF-S117-PROXY-DESIGN is *reassurance* or *redesign*:

- **(A) λ_max ≡ physical UV cutoff Λ.** Then "read the spectral-action prediction at the physical Λ, never at Λ→∞" is methodologically correct (Tr f(D/Λ) is Λ-dependent by construction); the −1.341 asymptote is just the unphysical Λ→∞ limit we never evaluate at, and there is NO fidelity failure — only a category-reminder not to take L→∞. The gap is benign.
- **(B) λ_max ≡ truncation-boundary artifact.** Then the proxy references a non-substrate quantity (the largest *retained* eigenvalue, set by where the cut falls, with no continuum limit); the L_max-dependence is spurious and the substrate-correct statistic should not reference λ_max at all. The gap signals a proxy mis-design.

Which is it? You own the Weyl edge — N(λ)~λ^d governs λ_max(L), and whether that linear growth is "the physical cutoff running" or "the truncation boundary moving" is exactly a heat-kernel / Weyl-asymptotics question. Your R3 answer is the discriminator that turns the S117 carry-forward from open-ended into a decidable compute.

---

## R3 — Convergence on a Structural Verdict

### R3 · spectral-geometer — final position

**The substantive physics has converged. I put my final position on record and answer baptista's R3 discriminator head-on — it is my home turf, the Weyl edge, and the answer is decisive.** I re-verified every number below by hand this turn rather than granting it on assertion.

#### 1. The discriminator: λ_max(L) is reading (B) — and the dichotomy dissolves exactly as Q36 did

baptista's final question forces a choice on the denominator of (B1): is λ_max(L) a **physical UV cutoff Λ** (reading A — read the prediction at the physical Λ, never at Λ→∞; the −1.341 asymptote is the limit we wisely never evaluate; gap benign) or a **truncation-boundary artifact** (reading B — λ_max is the largest *retained* eigenvalue, set by where the cut falls, no continuum limit; the gap is a proxy mis-design)?

**Answer: (B) for λ_max, decisively — and baptista's reading-(A) PRINCIPLE is correct; it is merely mis-assigned.** The branch-(iv) statistic carries TWO scales playing structurally different roles, and the question dissolves the same way "which is the canonical Q36 observable" did:

- **Λ_Z = 1 is the fixed physical cutoff — reading (A) holds for it.** The Gaussian kernel e^{−|λ|²/Λ_Z²} IS a genuine spectral-action regulator at a FIXED scale. baptista's (A) principle — "Tr f(D/Λ) is Λ-dependent by construction; read at the physical Λ, not at Λ→∞" — is methodologically correct and applies HERE: read mean_Z at Λ_Z=1 and it is benign, convergent, frozen. That is reading-(A) behavior, correctly.
- **λ_max(L) is NOT a second cutoff; it is the truncation edge — reading (B) holds for it.** It is not a regulator scale one holds fixed; it is the L_max boundary one is taking to ∞. (A)'s defense cannot rescue it, because (A) requires a FIXED Λ, and λ_max is by construction the running edge.

So "(A) or (B)?" resolves to **(A) for Λ_Z, (B) for λ_max.** The −1.341 asymptote is reading-(B): the Weyl edge running away in the denominator, not a benign Λ→∞ category-reminder. baptista's (A) defense is sound but mis-assigned — the fixed physical cutoff in branch-(iv) is Λ_Z, at which the genuine quantity mean_Z is benign; λ_max is a different beast.

#### 2. Why it is forced — the fixed-Λ convergence test (three defining properties)

A physical UV cutoff Λ in a spectral action has three defining properties; λ_max(L) fails all three, and the failure is a Weyl-asymptotics theorem, not a convention:

```
(SG1)  A physical cutoff Λ is HELD FIXED while L_max → ∞;
       the REGULATOR (not the truncation) supplies convergence.
```

1. **Fixed under L_max → ∞.** Λ_Z = 1 is held fixed; λ_max(L) = max{|λ_k| : p+q ≤ L} is *defined as* the truncation boundary and grows ∂λ_max/∂L ≈ 0.375 without bound (5.793 → 6.168 → 6.543, constant slope 0.375; consistent with the per-shell Weyl edge max|λ|(L,0) = 0.633√C₂(L,0)+0.555, C₂(L,0)=L(L+3)/3 ⇒ √C₂ ~ L/√3 ⇒ max|λ| ~ 0.365·L, linear-unbounded; (15,0): 6.560 vs 6.543, in-band). λ_max is slaved to L_max; a physical cutoff is not.
2. **Heat-kernel / Seeley-DeWitt representation.** A genuine cutoff enters through regulator moments f_n that survive in the heat-kernel expansion Tr f(D²/Λ²) ~ Σ_n f_n Λ^{d−n} a_n (a_0 Λ^d cosmological, a_2 Λ^{d−2} Einstein-Hilbert, …). λ_max — a sup-norm of the retained spectrum — has NO heat-kernel image, NO Seeley-DeWitt coefficient, NO continuum limit. Λ_Z does (it is the Gaussian regulator scale); λ_max does not.
3. **Fixed-Λ convergence.** At fixed Λ_Z, mean_Z CONVERGES as L_max → ∞ (frozen to Δ~10⁻⁴; the entire p+q=15 shell enters at weight e^{−4.216²} ≈ 1.9·10⁻⁸). ρ_B converges to the TRIVIAL −1 only *because* its scale λ_max → ∞.

The cleanest form of the discriminator is a side-by-side L_max → ∞ test on the two factors of (B1), evaluated identically:

```
(SG2)  L_max → ∞ at fixed regulator:
         mean_Z(Λ_Z=1)            →  1.98794    (finite physical value; reading-A signature)
         ρ_B = mean_Z/λ_max − 1   →  −1         (trivial; ONLY because λ_max → ∞; reading-B signature)
       The two are evaluated identically and differ by exactly the λ_max denominator.
       ⇒ the λ_max denominator IS the reading-B object.   ∎
```

mean_Z passes the reading-(A) test (fixed Λ_Z, converges to a physical value); ρ_B fails it (no fixed scale to hold; converges to −1 by scale-divergence). The ONLY structural difference between them is the λ_max denominator. Therefore the λ_max denominator is precisely the truncation-boundary artifact. A physical cutoff does not run to ∞ as you compute more carefully; a truncation edge does. The asymptote is reached *by the scale itself diverging* — the unmistakable Weyl-edge / reading-(B) signature.

#### 3. The substrate-physical scale is M_KK (or Λ_Z), never the spectral edge — CF-S117 becomes decidable

Substrate-first (GEOMETRIC, Level-1 single-τ-slice): the D_K spectrum on Jensen-deformed SU(3) at τ_fold IS the fiber's vibrational spectrum, *unbounded above* by compact-fiber Weyl growth. M_KK sets the fiber's mass scale (the tower spacing) — a FIXED substrate scale — but there is NO physical "top" of the tower. In physical units λ_max(L)·M_KK → ∞ is the truncation edge, NOT M_KK. So even dimensionfully the fixed substrate UV scale is M_KK (reading A); λ_max(L) is the moving truncation edge (reading B). Normalizing branch-(iv) by λ_max(L) substitutes the truncation boundary for the substrate's fixed scale.

This turns **CF-S117-BRANCH-IV-PROXY-DESIGN** from open-ended into a **decidable** compute: the substrate-correct branch-(iv) denominator is a FIXED, heat-kernel-representable substrate scale (Λ_Z = 1, already in hand; or M_KK), NOT a spectral-edge value at ANY L*. The "fixed-edge" variant mean_Z/λ_max(10)−1 is better than the running edge but still references a truncation edge (relocating the L_max-dependence into the choice of L*, my R2 Q1) — so the design verdict is the BROAD axis, **no-spectral-edge-normalization**: keep the Λ_Z-regulated mean_Z (sound), drop the λ_max division (artifact). The −1 offset + λ_max-division is the S85 W0-7 Zubarev *definition*, not substrate physics.

#### 4. Confirming the converged verdict, and accepting baptista's placement dissent

I confirm the workshop's converged structural verdict in full:

- **The observable-decomposition (B1)/(B3) is algebraically EXACT.** ρ_B = mean_Z/λ_max − 1; bottom-K ⟷ mean_Z (FROZEN, FB-saturated, Δmean_Z~10⁻⁴) ⊥ w0-shift ⟷ λ_max (Weyl-drifting, 100.08% of Δρ_B, decelerating as |d|=μb/λ_max² ~ 1/L², summable ⇒ spread → PASS at window {18,19,20}, L≈20). The same-wave compute **S116-W9-GTBUILDER-L15** (INFO; spread_CAC{13,14,15}=0.039290; GT-pure (15,0)/(0,15) sentinel=0.0; bottom-K max|diff|=0.0e+00) certifies BOTH factors at p+q=15: the numerator saturated, the denominator's symmetric tops bit-reproduced.
- **Friedrich-Bär scope = numerator side ONLY.** Eq. (2) |λ|_min ≥ η_FB_lower·√(C₂+1) is a Casimir LOWER bound; it saturates the bottom-K floor AND mean_Z (the Gaussian-windowed bottom mean); it is structurally SILENT on λ_max (the Weyl edge, N(λ)~λ^d). Citing FB to declare the w0 DR3 spread "saturated" reads a numerator-governing lower-bound theorem as governing the full ratio — a SCOPE ERROR we jointly reject. This is the §VII.AJ.partition-stability registry-scoping note (route to mack via housekeeping §A; I specify, I do not edit the curated §VII surface).
- **Q36 is observable-dependent.** bottom-K (FB-saturated, my assigned read) and the w0_FW DR3 moment (shifts, baptista's read) are BOTH canonical substrate-IS observables — for DIFFERENT falsifier surfaces (partition/B-band/n_s vs DESI DR3). The question dissolves into the decomposition; "which matters" is a function of which surface you stand on. p+q=15 is the FB-predicted null for the first AND the maximally-informative datum for the second (reachable only from L≥13 — three points are needed to separate a frozen-numerator/linear-denominator drift from a generic convergent sequence).
- **Anchor-fidelity gap is Weyl-FORCED, and I ACCEPT baptista's placement.** ρ_B = (fixed IR scale ≈ 1.98794)/(running Weyl edge) − 1 → −1 ⇒ w0_cac → −1.340827, gap 0.422827 from the L_max-independent closed form w0_FW = −0.918. On baptista's narrow R2 dissent: I accept that this is a SEPARATE Level-3 surface (anchor-fidelity), NOT a Level-2 Q36 verdict cell (L_max-stability / convergence-rate). His level-collision argument is structurally correct per the cross-pillar-bridge 3-level ladder; my R2 Q2 demand was for VISIBILITY, and that is satisfied by his committed anchor-fidelity note + Open-Question + carry-forward. No co-equal verdict cell; no reading of PASS-on-spread as vindication of −0.918.

**My reading-(B) verdict SHARPENS the gap's status — strengthening, not weakening, baptista's separation.** The anchor-fidelity gap is not an *open* "does this sound proxy asymptote correctly?" Level-3 question. It is a *diagnosed* proxy-definition artifact: the proxy CANNOT asymptote to −0.918 because its denominator is the truncation edge, which diverges by Weyl's law. The fix is known in KIND (de-reference the spectral edge; normalize by a fixed substrate scale). So the carry-forward is decidable, not exploratory — exactly the discriminator baptista asked my Weyl-edge answer to deliver.

**Final position on record.** The two R1 positions were never rival theories of one observable; they are the numerator and the denominator of one exact ratio (B1), and the workshop's joint position IS the ratio. bottom-K saturation IS the frozen numerator (mean_Z); the w0 shift IS the running denominator (λ_max); Friedrich-Bär governs the numerator and is silent on the denominator; Q36's answer is observable-dependent; and the anchor-fidelity gap is a Weyl-forced, separately-visible Level-3 discovery whose proxy-design fix is now decidable — **keep the fixed-Λ_Z mean_Z, drop the truncation-edge normalization.** I hand to baptista (R3-B) for the Structural Verdict + Wrap-Up.

### R3 · baptista-spacetime-analyst — final position + writes the Structural Verdict below

**The fork was never between two observables; it was between the numerator and the denominator of one exact ratio.** I re-derived every load-bearing number this turn by exact-rational (Sage QQ) recompute rather than carrying it on assertion — the converged structure sits on the decomposition to the last digit, and I record where I finally stand.

**Independent exact-rational re-verification (this turn).** From the pinned anchors ρ_B(13,14,15) = −0.656884 / −0.677718 / −0.696174, λ_max = 5.793 / 6.168 / 6.543, offset_Zubarev = −0.340827:

- mean_Z = (1+ρ_B)·λ_max = **1.987670988 / 1.987835376 / 1.987933518** — frozen, spread = **2.6253·10⁻⁴** across {13,14,15}.
- decrements |d(13→14)| = **0.020834** > |d(14→15)| = **0.018456** — decreasing AND decelerating (confirmed).
- channel split 14→15: λ_max channel = **100.081%**, mean_Z channel = **−0.081%** (sum 100.0%) — the shift is the explicit denominator, full stop.
- closed-form law |d|(14→15) = μb/(λ_max(14)·λ_max(15)) = **0.018471** vs actual 0.018456, ratio **1.00081** — the residue is exactly the non-frozen 10⁻⁴ of mean_Z.
- spread_CAC{13,14,15} = **3929/100000 = 0.039290** exact (INFO band) — offset cancels, = ρ_B(13) − ρ_B(15).
- anchor-fidelity asymptote ρ_B → −1 ⇒ w0_cac → **−1.340827**, gap **0.422827** from the L_max-independent w0_FW = −0.918.

Every number both R1 positions asserted lands on (B1) ρ_B = mean_Z/λ_max − 1 to the digit. CONFIRMED.

**Where I finally stand.**

1. **The exact decomposition resolves the fork.** ρ_B = mean_Z/λ_max − 1 is the governing object (the S85 W0-7 Zubarev statistic, `s105…py:293`), and the two R1 positions are its two factors: spectral-geometer's bottom-K floor IS the FB-frozen numerator mean_Z (two windows — min-K and Gaussian — on the SAME low-|λ| sectors); my w0 shift IS the running λ_max denominator (100.081% of Δρ_B). Neither is "the" Q36 observable to the exclusion of the other; **both are canonical substrate-IS observables — for DIFFERENT falsifier surfaces** (bottom-K for §VII.AJ.partition-stability / the B-bands / n_s; the w0 moment for the DESI DR3 surface). Redundancy is observable-DEPENDENT: p+q=15 is the FB-predicted null for the bottom-K (max|diff| = 0.0e+00; smallest p+q=15 |λ| = 4.216 ≫ the 0.845 bottom-20 ceiling) AND the maximally-informative datum for the w0 moment (Δρ_B = 0.018456). I grant spectral-geometer's strongest empirical claim — the bottom-K FB-saturation — in full; the dissent was only ever about identification, and it dissolves into the ratio.

2. **FB scope = the numerator side only, held jointly.** Eq. (2) |λ|_min(p,q) ≥ η_FB_lower·√(C₂+1) is a Casimir LOWER bound; it saturates the bottom-K floor AND mean_Z (the numerator) and is structurally SILENT on λ_max (the Weyl edge, N(λ) ~ λ^d). Citing FB to declare the w0 DR3 spread "saturated" reads a numerator-governing lower-bound theorem as governing the full ratio — a SCOPE ERROR we both reject. This is not a dissent; it is the converged §VII.AJ.partition-stability scoping statement (routed to mack, below).

3. **The anchor-fidelity gap is my separate find — and spectral-geometer's R3 reading-(B) answer makes it decidable.** I surfaced (R1 §5) ρ_B → −1 ⇒ w0_cac → −1.340827, a 0.422827 gap from −0.918; spectral-geometer sharpened it (R2) to Weyl-FORCED (fixed IR numerator over linearly-unbounded Weyl denominator), and his R3 answered my final discriminator decisively on his home turf: λ_max(L) is reading-(B) (the truncation edge — slaved to L_max, no heat-kernel image, no continuum limit), while the genuine fixed physical cutoff in branch-(iv) is Λ_Z = 1 (reading-(A), at which mean_Z is benign and convergent). I accept this in full. It ELEVATES the find: the gap is not an open "does this proxy asymptote correctly?" question — it is a DIAGNOSED proxy-definition artifact (the denominator cannot asymptote to −0.918 because it diverges by Weyl's law), whose fix is known in KIND: de-reference the spectral edge; normalize by a fixed substrate scale (Λ_Z or M_KK). This makes CF-S117-W0-ANCHOR-FIDELITY a decidable compute, not an exploration.

4. **Placement: the anchor-fidelity gap is a SEPARATE Level-3 surface, NOT a Q36 verdict cell.** L_max-stability (the DR3 gate's pre-registered object — the SPREAD) is a Level-2 convergence-rate statement; anchor-fidelity (does the proxy asymptote to the physical −0.918?) is a Level-3 statement; seating the latter as a co-equal Level-2 verdict cell is a level-collision and retroactively widens Q36's pre-registered scope. spectral-geometer accepted this placement (R3). So the 4-row table below IS the Q36 verdict; the anchor-fidelity gap lands as an explicit NOTE + an Open-Question + a carry-forward — visible, separable, never read as PASS-on-spread vindicating −0.918.

I write the Structural Verdict and Wrap-Up below.

---

## Structural Verdict

**The governing structure is one exact ratio** (GEOMETRIC, Level-1 single-τ-slice at τ_fold = 0.190; both factors substrate-IS functionals of the same D_K spectrum, neither a measurement "in" a container):

```
(B1)  ρ_B  =  mean_Z   /   λ_max   −  1
              └ bottom ┘     └ edge ┘
              FROZEN          DRIFTING
              FB-saturated    Weyl-linear (∂λ_max/∂L = 0.375)
              = spectral-geom. bottom-K, = baptista's w0 shift
                as a Gaussian window       (100.081% of Δρ_B)
```

Q36's two R1 positions are the numerator and the denominator of (B1). The verdict resolves the fork by the decomposition: **bottom-K ⟷ mean_Z (FB-saturated, EXACT) ⊥ w0-shift ⟷ λ_max (Weyl-drifting, convergent |d| ~ 1/λ_max²)**. The Friedrich-Bär saturation theorem (§VII.AJ.partition-stability) governs the NUMERATOR side only — the bottom-K floor + the bulk low-|λ| moments (incl. mean_Z) — and is structurally SILENT on the λ_max denominator; "FB saturates the w0 spread" is a SCOPE ERROR, jointly rejected. Same-wave compute **S116-W9-GTBUILDER-L15** (INFO; verdict canonical, audit_sha256 `94ed48e7…`) certifies BOTH factors at p+q=15: bottom-K floor max|diff| = 0.0e+00 (numerator saturated) AND the GT-pure (15,0)/(0,15) sentinel = 0.0 exact (the symmetric tops that SET λ_max bit-reproduced — denominator certified). All decomposition numbers re-verified this turn by exact-rational (Sage QQ) recompute (mean_Z frozen to 2.6253·10⁻⁴; channel split 100.081%/−0.081%; spread_CAC{13,14,15} = 3929/100000).

| Item | Verdict | Note |
|:-----|:--------|:-----|
| Canonical Q36 observable | **BOTH — observable-DECOMPOSITION** ρ_B = mean_Z/λ_max − 1 | The two R1 positions are the numerator and denominator of ONE exact ratio (B1). bottom-K canonical for §VII.AJ.partition-stability / B-bands / n_s; w0_FW DR3 moment canonical for the DESI DR3 surface. "Redundancy" is observable-DEPENDENT: p+q=15 is FB-null for bottom-K (Δ=0), maximally-informative for w0 (Δρ_B = 0.018456). |
| Friedrich-Bär theorem scope | **bottom-K + bulk low-\|λ\| ONLY** (incl. the Zubarev numerator mean_Z) | Eq. (2) \|λ\|_min ≥ η_FB_lower·√(C₂+1) is a Casimir LOWER bound; saturates the floor AND mean_Z; structurally SILENT on the λ_max Weyl edge (N(λ) ~ λ^d). Citing FB to call the w0 DR3 spread "saturated" = SCOPE ERROR (jointly rejected). §VII.AJ.partition-stability scoping note → mack (housekeeping §A9). |
| bottom-K ⊥ w0_FW orthogonality | **ORTHOGONAL** | Numerator (FROZEN, FB-saturated, Δmean_Z = 2.6253·10⁻⁴ over {13,14,15}) ⊥ denominator (Weyl-linear, ∂λ_max/∂L = 0.375; carries 100.081% of Δρ_B). Disjoint spectral regions glued into one ratio; different operations, not rival readings. |
| w0 DR3 spread convergence | **convergent (→ PASS at finite L)**; marginal-INFO now | spread_CAC{13,14,15} = 0.039290 = 3929/100000 ∈ (0.025, 0.050] INFO, NARROWING (S105 {12,13,14} = 0.044514 → 0.039290). \|d\| = μb/λ_max² ~ 1/L² summable ⇒ first PASS at window {18,19,20}, L ≈ 20. Build-horizon-limited, NOT non-convergent. |

**Anchor-fidelity NOTE (a SEPARATE Level-3 surface — do NOT read into the convergence cell).** The w0 DR3 spread converges on **L_max-stability** (Level-2 convergence-rate), but the value it stabilizes AROUND is **Weyl-FORCED** to w0_cac → −1.340827 (ρ_B → −1 as the fixed IR numerator mean_Z ≈ 1.9879 divides the linearly-unbounded Weyl edge λ_max), a gap of **0.422827** from the L_max-independent closed form w0_FW = −0.918. PASS-on-spread certifies STABILITY, NOT FIDELITY — a consumer must not read the INFO→PASS transition at L ≈ 20 as the prediction converging to −0.918. spectral-geometer's R3 reading-(B) diagnosis (λ_max = truncation edge, no continuum limit; Λ_Z = 1 = the genuine fixed cutoff) makes the fix decidable in KIND: de-reference the spectral edge. Routed as an Open-Question + CF-S117-W0-ANCHOR-FIDELITY below, NOT a Q36 verdict cell (level-collision: Level-3 anchor-fidelity ≠ Level-2 L_max-stability).

---

## Remaining Open Questions

1. **The anchor-fidelity gap (the workshop's real discovery).** w0_cac is Weyl-FORCED to −1.340827, a 0.422827 gap from the closed-form w0_FW = −0.918 — surfaced ONLY by the deep-truncation trio {13,14,15} (three points are needed to separate a frozen-numerator / linear-denominator drift from a generic convergent sequence). It is a SEPARATE Level-3 surface from the Level-2 L_max-stability the DR3 gate tests. The fix is decidable in KIND (spectral-geometer R3 reading-(B): de-reference the truncation edge; normalize by a fixed substrate scale Λ_Z / M_KK), but WHICH normalization is substrate-correct is the open compute. → **CF-S117-W0-ANCHOR-FIDELITY**.
2. **Does the |d| ~ 1/λ_max² deceleration continue at p+q=16 toward the {18,19,20} PASS window?** The closed-form convergence law (B2) predicts |d(15→16)| = μb/λ_max(16)²; the empirical first-PASS window {18,19,20} (L ≈ 20) is one shell beyond the current build. Confirming the law at the next truncation (and that the spread keeps narrowing below 0.039290) is the next branch-(iv) datum. → **CF-S117-BRANCH-IV-L16**.
3. **Is the substrate-correct branch-(iv) denominator a fixed scale at all** (running-edge [current CAC] / fixed-edge mean_Z/λ_max(10)−1 / no-spectral-edge-normalization)? mean_Z carries the FB-frozen physical content; λ_max has no continuum limit. spectral-geometer R3 predicts the no-spectral-edge answer (keep the Λ_Z-regulated mean_Z, drop the λ_max division). This is the proxy-design axis of CF-S117-W0-ANCHOR-FIDELITY, NOT an in-gate convention switch (current CAC correct per `regulator-convention-lockdown.md`).

---

## Wrap-Up

### What Changed

#### (a) Numerical revisions

- spread_CAC: `0.044514` (S105 {12,13,14}) → **`0.039290`** = `3929/100000` exact (this wave, {13,14,15}) — narrowing, still INFO band.
- ρ_B(15) = **−0.696174** (NEW datum; λ_max(15) = 6.543); mean_Z frozen at ≈ **1.98793** (spread 2.6253·10⁻⁴ over {13,14,15}).
- first-PASS window sharpened: R1 `{17,18,19}` / L≈19 → R2/R3 converged **`{18,19,20}` / L≈20** (decelerating |d| = μb/λ_max²).
- anchor-fidelity asymptote pinned (Sage-exact): w0_cac → **−1.340827**, gap **0.422827** from w0_FW = −0.918.
- channel split pinned: λ_max = **100.081%**, mean_Z = **−0.081%** of Δρ_B(14→15); closed-form law ratio **1.00081**.

#### (b) Structural changes

- **Q36 reframed**: single-observable fork (bottom-K *vs* w0_FW) → **observable-DECOMPOSITION** ρ_B = mean_Z/λ_max − 1 (the two positions are the numerator and the denominator of one exact ratio).
- **"Redundancy" re-typed**: absolute → **observable-DEPENDENT** (p+q=15 is FB-null for bottom-K, maximally-informative for w0).
- **Friedrich-Bär theorem SCOPED**: ambiguous "saturates the spectrum" → **bottom-K + bulk low-|λ| / mean_Z numerator ONLY**, structurally SILENT on λ_max (a §VII.AJ.partition-stability registry-scoping statement; → mack §A9).
- **Anchor-fidelity ELEVATED**: "open drift" → **Weyl-FORCED, diagnosed proxy-definition artifact** on a SEPARATE Level-3 surface (distinct from Level-2 L_max-stability); fix decidable in KIND.
- **Epistemic pin established**: L_max-stability ≠ anchor-fidelity; PASS-on-spread certifies STABILITY, NOT FIDELITY.

### What Holds

- The exact decomposition (B1)/(B3) ρ_B = mean_Z/λ_max − 1 — an algebraic identity (`s105…py:293`); both sides independently verified, and my exact-rational (Sage QQ) recompute this turn confirms mean_Z {1.987670988, 1.987835376, 1.987933518}, channel split 100.081%/−0.081%, law ratio 1.00081, spread 3929/100000, asymptote gap 0.422827.
- **bottom-K FB-saturation EXACT**: bottom-64 max|diff|(L≤14 vs L≤15) = 0.0e+00; smallest p+q=15 |λ| = 4.216 ≫ bottom-20 ceiling 0.845.
- **FB scope = numerator/bottom-K side only** (Casimir LOWER bound, silent on the Weyl edge) — jointly held.
- **Both observables substrate-IS and canonical** for their respective falsifier surfaces (observable-dependent "which matters").
- **S116-W9-GTBUILDER-L15** certifies BOTH factors at p+q=15: numerator (bottom-K max|diff| = 0.0e+00) + denominator (GT-pure (15,0)/(0,15) sentinel = 0.0 exact).
- **DR3 CAC convention discipline UNCHANGED** (no band-shopping, no in-gate convention switch; current CAC correct per `regulator-convention-lockdown.md`).

### What Breaks or Strains

- **Anchor-fidelity (STRAINS, diagnosed-not-fatal).** The branch-(iv) Zubarev proxy as currently defined (running-λ_max-edge normalization, S85 W0-7) CANNOT asymptote to w0_FW = −0.918 — it is Weyl-FORCED to −1.340827 (gap 0.422827). This strains the proxy's anchor-FIDELITY, NOT its L_max-STABILITY (which is convergent). Diagnosed: the denominator is the truncation edge (no continuum limit), so the fix is known in KIND (de-reference the spectral edge; normalize by Λ_Z / M_KK). The workshop's real discovery, routed to CF-S117-W0-ANCHOR-FIDELITY.
- **Build-horizon (operational, NOT physics).** The first-PASS window {18,19,20} (L ≈ 20) is beyond the current p+q=15 build; reaching it needs the wall-free GT-direct symmetric tops (mean_Z frozen ⇒ only λ_max(L) is required). This is a feasibility horizon, NOT non-convergence.

### Carry-Forward Computations (MATH ONLY — propagate to S117)

**CF-S117-BRANCH-IV-L16**
1. **What**: build the p+q=16 FB-bounded shell (17 sectors, analytic-tail-only in `fb_bounded_sectors`); form spread_CAC{14,15,16}; test whether the closed-form |d| = μb/λ_max² deceleration continues toward the {18,19,20} PASS window.
2. **Who**: baptista-spacetime-analyst.
3. **Input**: reuse `irrep_symmetric_power_gt` + `rho_zubarev_from_sectors` + `build_dirac_pipeline` VERBATIM from `s105_branch_iv_direct_l1314.py`; mean_Z frozen ⇒ only λ_max(16) needed, set by the wall-free GT-direct (16,0)/(0,16) symmetric tops (C₂(L,0) maximal at fixed level); the S106 cache `sector_evals_L16` already carries p+q≤16.
4. **Gate**: |d(15→16)| within 5% of the closed-form μb/λ_max(16)²; spread_CAC{14,15,16} < spread_CAC{13,14,15} = 0.039290 (continued narrowing).
5. **Effort**: low (one shell, one evaluator call; GT-direct symmetric tops only — feasible at p+q=16 per the S116 bit-exact GT result).
6. **Depends on**: S106 cache `s106_w1_highl_cache_l1416.npz`; `s105_branch_iv_direct_l1314.py` evaluators; canonical_constants offset_Zubarev = −0.340827, w0_FW = −0.918.

**CF-S117-W0-ANCHOR-FIDELITY**
1. **What**: resolve the Weyl-forced anchor-fidelity gap (ρ_B → −1 ⇒ w0_cac → −1.340827 vs w0_FW = −0.918). Compute ρ_B under three normalization axes — {running-edge [current CAC], fixed-edge mean_Z/λ_max(10)−1, no-spectral-edge-normalization (fixed Λ_Z / M_KK)} — and report each variant's w0_cac asymptote + DR3 spread + heat-kernel representability of the denominator.
2. **Who**: baptista-spacetime-analyst (+ spectral-geometer cross-check on the Weyl-edge / reading-(B) discriminator).
3. **Input**: mean_Z(L), λ_max(L) trajectories {10..15} (+ L=16 from CF-S117-BRANCH-IV-L16); Λ_Z = 1, offset_Zubarev = −0.340827, w0_FW = −0.918.
4. **Gate**: pre-registered — which normalization yields an L_max-INDEPENDENT w0_cac (fixed, heat-kernel-representable denominator) that asymptotes to the substrate-physical value? spectral-geometer R3 reading-(B) prediction: no-spectral-edge (keep the Λ_Z-regulated mean_Z, drop the λ_max division). NOT an in-gate convention switch — the CF POSES + COMPUTES the proxy-design question; current CAC stays correct per `regulator-convention-lockdown.md`.
5. **Effort**: medium (3 normalization variants on existing trajectories).
6. **Depends on**: the mean_Z(L)/λ_max(L) trajectories from the branch-(iv) lineage (S102→S105→S116, + CF-S117-BRANCH-IV-L16); the reading-(A)/(B) discriminator (spectral-geometer R3); canonical_constants Λ_Z, offset_Zubarev, w0_FW, M_KK.

### Effected In-Session (NON-MATH — executed by the R3-B agent before terminating)

- [x] **Friedrich-Bär saturation-theorem SCOPE note — SPECIFIED + ROUTED to `session-116-housekeeping.md §A9` for the orchestrator's mack dispatch at §6** (NOT edited by me — the §VII.AJ.partition-stability surface is mack-cosmic-bridge's SOLE-writer domain, `feedback_mack-bridge-role.md`; connes + mack SOURCE-DOUBLE-CITE-CO-PRIMARY, PERMANENT, `atlas-07-permanent-results.md:675`). Precise scoping text + the append-only patch target recorded in §A9; locus VERIFIED on disk (atlas-07:675, grep-confirmed) before routing. The note is ADDITIVE and audit-trail-preserving — it does NOT down-tag the PERMANENT theorem; it scopes WHAT it saturates (bottom-K + bulk low-|λ| / mean_Z numerator, SILENT on λ_max).
- [x] **Agent-memory note — EXECUTED directly** (own domain). Updated `.claude/agent-memory/baptista-spacetime-analyst/s116-branch-iv-l15-fb-scope.md` with the workshop's converged outcome: the EXACT decomposition ρ_B = mean_Z/λ_max − 1 (numerator ⊥ denominator), the closed-form law |d| = μb/λ_max² (Sage-exact ratio 1.00081), the Weyl-forced anchor-fidelity gap (w0_cac → −1.340827), and the reading-(A)/(B) discriminator (Λ_Z fixed cutoff vs λ_max truncation edge → de-reference-the-edge fix).
- No `.py` compute, no curated-doc edit, no verdict line (workshop closes by artifact-existence per `wave-classification.md §M1`).

### Closing Line

Session 116 closes on an identity: ρ_B = mean_Z/λ_max − 1 — the FB-frozen bottom-K numerator and the Weyl-running λ_max denominator are the two factors of one exact ratio, Q36's rival positions were never rivals, and the deep-truncation trio {13,14,15} returned both the FB-predicted null on the bottom-K floor and the workshop's real discovery: the Weyl-forced anchor-fidelity gap to −1.341, diagnosed and routed to S117.
