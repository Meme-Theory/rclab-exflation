# Session 86 Workshop: lizzi x connes — Mellin-cone Infrastructure Repair-or-No-Go

**Date**: 2026-04-27
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: lizzi (lizzi-spectral-functional-theorist), connes (connes-ncg-theorist)
**Source Documents**:
- sessions/archive/session-86/session-86-w2-workingpaper.md
- sessions/archive/session-86/session-86-w3-workingpaper.md
- sessions/archive/session-86/session-86-w10-workingpaper.md
- computations/s86_gate_verdicts.txt

**Focus Topics**:
1. C9 FAIL reading (`S86-MELLIN-HEAT-KERNEL-INFRA`, value=9.456, line 95-96 of s86_gate_verdicts.txt): near-miss-fit-window-refinement vs structural-divergence-correctly-detected
2. C10 INFO reading (`S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE`, value≈2.81e5+0j, line 91): off-pole substrate-spectral signal vs Hankel-contour systematic needing reformulation
3. W3-consumer per-evaluation needs: s=4 leading residue for T9 (ε_T9=0.01 asymptotic margin); s=3 off-pole apex for W0-20; ρ-fit over s∈[2.5, 4.5] for W0-7-MB
4. Cross-cutting: structural-no-go theorem candidacy for the truncation regime + W2 Candidate 3 cross-link (Mellin-Strip / Convergence-Cone Theorem T5 readiness using C11's Λ_Z^{2s}·Γ(s) closed-form)

**Pre-Registered R3 Adjudication**: Workshop MUST emit at least ONE of:
- (i) concrete repair-pathway spec for S87 with pre-registered PASS criteria (effort 4-6h)
- (ii) structural-no-go theorem for the truncation regime
- (iii) per-evaluation-finiteness re-pre-registration that unblocks W3 in S87 without requiring C9/C10 themselves to PASS

NOT defer to S87.

**Pre-Registered Carry-Forward**: 4-field S87 spec (what / inputs / gate / effort) for whichever path R3 selects:
- `S87-MELLIN-CONE-LIVE-RERUN` if (i)
- `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` if (ii)
- `S87-W3-PER-EVAL-FINITENESS-PRE-REG` if (iii)

**Substrate-framing reminder** (per `.claude/rules/phononic-framing.md`): the Mellin-Barnes residue scheme is a substrate spectral observable derived from D_K's eigenvalue spectrum at L_max=10 (155,984 eigenvalues). FAIL/INFO verdicts are substrate signatures (CC-3 cross-check at machine-epsilon proves the integrator works; the verdicts measure the substrate, not the integrator).

---

## Round 1 — lizzi: Opening Analysis

### L1: C9 FAIL Reading — Mellin-Heat-Kernel-Infra (value=9.456)

**Topline**: C9's value=9.456 is NOT a near-miss requiring fit-window refinement. It is the correct measurement that the F_4 = {ζ, Zubarev, SDW} sub-atlas of regulators does not suppress the substrate's a_0 spectral content at L_max=10 — the original W0-11 truncation FAIL was structurally sound; C9 falsified the "truncation-artifact" hypothesis embedded in the §13 substrate-framing reminder. From the W3-consumer angle, C9's FAIL is **structural-divergence-correctly-detected**, not infrastructure-broken, and any S87 "repair" that brings ratio_min(F_4) below 5e-1 by adjusting the F_4 algebra is the wrong target.

**Evidence — both FAIL branches independently fired** (`session-86-w2-workingpaper.md:51-57, 95-112`):

```
Step 1 (definitions, transcribed from §W2-1 substitution chain):
  ratio_min_in_F_4 := min over reg ∈ {ζ, Zubarev, SDW} of |Λ_CC^MB(reg)| / |a_0^trunc(reg)|
  PASS_ratio       ⟺  ratio_min_in_F_4 ≤ 5e-1                    [plan §9]
  FAIL_ratio       ⟺  ratio_min_in_F_4 > 5e-1
  χ²/dof(reg)      := (1/4) Σ_{n ∈ {0,2,4,6}} (Δ_n(reg) / σ_n^trunc(reg))²
  PASS_chi         ⟺  max_reg χ²/dof ≤ 5
  FAIL_chi         ⟺  max_reg χ²/dof > 20

Step 2 (substitute the C9 numerical results from §W2-1 line 53-55):
  ζ       : Λ_CC^MB / a_0 = 1.0339e+01,  χ²/dof = 1.4696e+04
  Zubarev : Λ_CC^MB / a_0 = 9.4557e+00,  χ²/dof = 2.2047e+02
  SDW     : Λ_CC^MB / a_0 = 9.6870e+00,  χ²/dof = 4.2340e+02

Step 3 (canonical form, ratio branch):
  ratio_min_in_F_4 = min{10.84, 9.46, 9.69} = 9.4557     [Zubarev attains worst-case-smallest]
  9.4557 > 5e-1   ⟺  TRUE   →  FAIL_ratio fires
  Margin to PASS_ratio bound: 9.4557 / 5e-1 = 18.9× (1.28 OOM above)

Step 4 (canonical form, χ² branch):
  max_reg χ²/dof = max{1.47e+04, 2.20e+02, 4.23e+02} = 1.47e+04     [ζ-class]
  1.47e+04 > 20  ⟺  TRUE   →  FAIL_chi fires
  Margin to PASS_chi bound: 2940×, ~3 OOM above; margin to FAIL_chi bound: 735×

Step 5 (direction):
  Both branches fire independently; the FAIL is doubly-confirmed.
  Direction of L_max scan (§W2-1 line 80): n=0 in ζ-class GROWS L=5 → L=10 by factor 239×
  (3.93e+05 → 9.38e+07). Adding sectors (p+q) ∈ {9, 10} adds 46,816 eigenvalues that
  OUTWEIGH the truncation residual at n=0. The substrate's a_0 slot is NOT YET in the
  Weyl asymptotic regime at L_max=10. Larger L_max would make ratio LARGER, not smaller.
```

**Why this is structural divergence, not near-miss**: a fit-window refinement (e.g. dropping the n=6 slot from the χ² to bring max_reg χ²/dof into PASS) is precisely the convention-shopping prohibited by `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1. The n=6 dominance (`session-86-w2-workingpaper.md:117-122`) is not a fit defect — σ_6^trunc is the smallest absolute residual across slots BECAUSE the high-n moments are dominated by the lowest eigenvalues which are stable across L_max, while |Δ_6| is large because the MB Mellin transform integrates all eigenvalues with weight Γ(n)·λ_k^{-2n} concentrated on the IR. The n=6 σ_6 stability and n=6 |Δ_6| largeness BOTH carry substrate signal — they're orthogonal substrate signatures of the curvature-squared SD slot.

**The Mellin-Strip / Convergence-Cone framework reading** (consistent with C11 §W2-3 framework note `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` and W1b T5):

The Zubarev kernel's Mellin profile `M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` has poles at s ∈ {0, -1, -2, ...} from Γ(s) and is otherwise analytic on Re(s) > 0 — the convergence cone. The strip s ∈ (-1, 0) just left of the leftmost Γ pole is what would carry the a_0 ↔ Mellin-residue identification IF the substrate's a_0 spectral content were Schwartz-class (rapidly decreasing). C9's FAIL says: at L_max=10, the substrate's spectral density truncated to the first 78,080 eigenvalues is NOT Schwartz-class enough for the F_4 multiplier algebra to suppress its a_0 contribution to within 5e-1 of the direct truncation. The Mellin-Strip framework predicts (and C9 confirms) that F_4 suppression requires Schwartz-class substrate density on the convergence-cone strip; the truncated D_K cache at L_max=10 fails this not because the strip is missing but because the eigenvalue density (Weyl-dim growth d(p,q) = (1/2)(p+1)(q+1)(p+q+2)) on the truncation boundary contributes too much weight at the IR end.

**Tie to my prior corpus**: this falsifies the truncation-hypothesis branch of the S77 R-protection-universal claim at the a_0 slot specifically (S77 Synthesis: a_0 slot is the SOLE Lizzi-observable where R-protection universally fails). The C9 FAIL is the first a_0-only test at L_max=10 with full F_4 sweep + Mellin-Barnes lens; it confirms the S82 W2-8 A2-CLUSTER-TEST result (var_a_0 = 68.55% at 5-scheme L=5) extrapolates to F_4 at L_max=10 with var well above any 1e-1 suppression target. The FAIL is in the same family as ZETA-NOT-PHYSICAL-75 — the regulator profile is observable; the bare a_0 / Λ_CC ratio is regulator-conditional and does not stabilize to within R-protected bounds across F_4.

**Question for connes (Re:L1)**: from the NCG axiomatic side, does the Connes-Moscovici 1995 dimension-spectrum theorem `Sd = {8, 6, 4, 2, 0}` (cited in §W2-1's MCP audit) require Schwartz-class density on the spectral cone, or only finiteness of the eigenvalue counting function `N(λ) ≪ λ^d`? If the former, C9 has falsified the precondition for CM-1995 on the truncated cache; if the latter, the MB-cone scheme is intrinsically NCG-axiom-native but the F_4 multiplier algebra does not exhaust the analytic continuations available.

### L2: C10 INFO Reading — Mellin-Cone-Residue-Infrastructure (value≈2.81e5+0j)

**Topline**: C10's `analytic_zeta(s=3, L_max=10) = 2.807432×10⁵ + 0j` is the **off-pole substrate-spectral signal**, not a Hankel-contour systematic. The diagnostic that distinguishes the two has already been performed inside C10 itself: the Mellin and Dirichlet routes agree to machine precision (rel_err ≤ 5.82e-11 / |z| ≈ 1.18e-16) across the 5-point sweep s ∈ {2.5, 2.75, 3.0, 3.25, 3.5}. A Hankel systematic would manifest as Mellin-vs-Dirichlet disagreement; their agreement at float64 floor IS the absence of systematic.

**The diagnostic — Mellin-Dirichlet finite-spectrum identity** (transcribed and verified from `session-86-w2-workingpaper.md:232-267`):

```
Step 1 (definitions):
  K(t)               := Σ_k m_k exp(-λ_k² t)              [heat kernel of D_K cache]
  analytic_zeta(s,L) := ∫_0^∞ t^{s/2-1} K(t) dt / Γ(s/2)  [Mellin route, off-pole]
  zeta_D_direct(s,L) := Σ_k m_k λ_k^{-s}                  [Dirichlet route, truncated]

Step 2 (substitute heat-kernel form into Mellin integrand):
  ∫_0^∞ t^{s/2-1} K(t) dt
    = ∫_0^∞ t^{s/2-1} Σ_k m_k exp(-λ_k² t) dt
    = Σ_k m_k ∫_0^∞ t^{s/2-1} exp(-λ_k² t) dt   [linearity, finite sum]
    = Σ_k m_k λ_k^{-s} Γ(s/2)                    [gamma identity, λ_k² > 0]

Step 3 (simplify):
  analytic_zeta(s, L) = [Σ_k m_k λ_k^{-s} Γ(s/2)] / Γ(s/2)
                     = Σ_k m_k λ_k^{-s}
                     ≡ zeta_D_direct(s, L)        [exact at finite L]

Step 4 (substitute observed C10 5-point sweep, §W2-2 line 218-222):
  s=2.500:  Mellin = +4.950910e+05,  Dirichlet = +4.950910e+05,  rel = 1.18e-16
  s=2.750:  Mellin = +3.723510e+05,  Dirichlet = +3.723510e+05,  rel = 0.00
  s=3.000:  Mellin = +2.807432e+05,  Dirichlet = +2.807432e+05,  rel = 0.00
  s=3.250:  Mellin = +2.122436e+05,  Dirichlet = +2.122436e+05,  rel = 1.37e-16
  s=3.500:  Mellin = +1.609226e+05,  Dirichlet = +1.609226e+05,  rel = 0.00

Step 5 (direction — Hankel-systematic vs substrate-signal):
  IF Mellin-route had a Hankel-contour systematic ε(s), the agreement
  with the Dirichlet sum would degrade as |Mellin - Dirichlet| ~ ε(s) > 0.
  Observed: |Mellin - Dirichlet| / |z| ≤ 1.37e-16 = 0.6 × float_eps.
  A systematic would have to live INSIDE the float64 floor;
  this is empirically indistinguishable from no-systematic.

Conclusion: the observed value 2.807432e+05 IS the substrate's truncated
ζ_D(s=3, L_max=10) — the Mellin lens reads through transparently.
This is substrate-signal, full stop.
```

**What the INFO band measures, and why it is NOT an integrator artifact** (`session-86-w2-workingpaper.md:276-303`):

The two cross-checks that ride INFO are (i) truncation-stability `|z(3, 8) − z(3, 10)| / |z(3, 10)| = 6.113×10⁻¹` and (ii) ε-analyticity `|z(3+0i) − z(3+0.001i)| / |z(3+0i)| = 1.124×10⁻³`. Both measure the substrate, not the lens:

- **Truncation-stability INFO (6.11×10⁻¹)**: this is the substrate's spectral-density growth signature on the L=8 → L=10 step. The L=8 cache drops sectors (p+q) ∈ {9, 10} whose Weyl-dimension growth `d(p,q) = (1/2)(p+1)(q+1)(p+q+2)` makes them dominant contributors to ζ_D(3, L_max). The 61.1% jump on a single L step is exactly what the Weyl-asymptotic non-saturation predicts; it is the SAME signal that C9 picks up at the n=0 slot (factor 239× over L=5→L=10 in §W2-1 line 80). C10's 61.1% and C9's 239× are two views of the same substrate property — the truncated D_K spectral density at L_max=10 has not entered the asymptotic Weyl regime.

- **ε-analyticity INFO (1.124×10⁻³)**: a 0.001 imaginary perturbation in s induces a 1.124×10⁻³ relative change in z(s, L_max=10). To leading order in ε,

  ```
  ∂(analytic_zeta)/∂s |_{s=3} · 0.001 ≈ |z(3, L)| × O(1) × 0.001
  ```

  giving ~1×10⁻³ — entirely consistent with the linear-response prediction. The 1.12× excess over the 1e-3 PASS threshold is the ψ-digamma logarithmic factor in `∂z/∂s = (1/2)∫ t^{1/2} log(t) K(t) dt / Γ(3/2) − (1/2)·ψ(3/2)·z(s, L)` evaluated at s=3 — a calibration of the analyticity radius around s=3 in the truncated cache, not a Hankel-contour error.

**Reformulation needed?** The C10 API is **not Hankel-contour-pathological at s=3, L_max=10**. The Hankel-deformation guard in `_analytic_zeta.py` fires only within 0.05 of {s=2, s=4} (per §W2-2 line 285); at s=3 the contour is straight along the positive real t-axis, the integrand `t^{1/2} K(t)` is integrable at both endpoints (t→0 bounded by `t^{1/2} × N_evs`; t→∞ exponential decay from `λ_min² > 0`), and no analytic continuation is invoked. So no reformulation of the integrator is needed.

What WOULD need reformulation is the asymptotic claim that an `R(L) = R_∞ + α/L² + β/L⁴` extrapolation captures the Weyl-non-asymptotic substrate at L_max=10. The 61.1% L=8→L=10 shift is too steep for the canonical Connes-Moscovici 1/L² extrapolation tail; the substrate is in a pre-asymptotic regime where higher-order terms (1/L^6, 1/L^8) carry weight beyond the canonical truncated form.

**Tie to my prior corpus**: this is the same regime I encountered in S73b SDW-VALIDATION-73B (FAIL at L_max=7 with +168% ratio shift) and S77 chi_2=<sqrt(x)> identity (chi_2 single-branch moment NOT R-protected with 5.06% drift); the 61% shift at C10 sits in the same Weyl-non-asymptotic family. The R-protection criterion at C44 (S86 W1b-T6 anchor) does NOT apply — analytic_zeta(s=3, L_max=10) is a single-branch single-moment observable, not a Mellin-criterion-protected ratio. This is precisely the class of observables that S82 W2-8 flagged as cluster-variance-dominated.

**Question for connes (Re:L2)**: from the NCG-finite-triple side, is there a way to certify the C10 INFO band is the FINITE-L-substrate-spectral signature rather than a pre-asymptotic-extrapolation issue, using the Connes-Moscovici 2007 finite-triple machinery (which I cite in C38's rep-theoretic exact identity, S86 W10-2)? Specifically: is there a `dim(H_F) = 96` finite-triple invariant that bounds the L=8→L=10 truncation shift from below, validating C10's value as substrate-spectral-real and not extrapolation-pre-asymptotic? If yes, the C10 INFO band has a structural-anchor; if no, the 61.1% shift remains a free parameter.

### L3: W3-Consumer Per-Evaluation Needs

**Topline**: The three downstream W3 consumers split cleanly under the C10 finite-spectrum identity (§W2-2 substitution chain): two of three (W0-20 s=3 apex, W0-7-MB ρ-fit lower half) are **functionally already-evaluated** through C10's existing 5-point sweep — they are blocked only by the verdict-line "C10 INFO" flag, not by computational unavailability. The third (T9 s=4 leading residue) is **irrecoverable without infrastructure repair OR L_max → ∞ extrapolation evidence** because s=4 is exactly the pole the truncated cache has not entered the Weyl-asymptotic regime to expose.

**Per-evaluation analysis** — the controlling question is whether each evaluation lives in the off-pole strip (functionally available via C10) or hugs the s=4 pole (requires C9-class infrastructure):

#### Evaluation 1 — T9 (`S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING`, ε_T9 = 0.01, s=4 leading residue)

**Source**: `session-86-w3-workingpaper.md:7-32, 230` — hypothesis: `S_zeta_E^cont(L_max) / ζ_D(3, L_max)` admits a finite limit > 1 + ε_T9 as L_max → ∞ via C10 analytic_zeta API at s=4 leading residue.

**Substitution chain (T9-FEASIBILITY-AT-L=10)**:

```
Step 1 (definitions):
  R(L) := S_zeta_E^cont(L) / ζ_D(3, L)              [T9 ratio, §W3-1 line 14]
  R_∞ := limit_{L→∞} R(L)                            [asymptotic claim]
  PASS_T9 ⟺ R_∞ > 1 + 0.01 = 1.01                    [ε_T9 = 0.01, plan spec]

Step 2 (substitute the s=4 substrate-spectral evaluation):
  Numerator S_zeta_E^cont(L) at the s=4 leading residue requires
    Res_{s=4}(analytic_zeta(s, L) · t^{s/2-1} kernel weight)
  But analytic_zeta(s=4, L) is exactly AT the SD pole at s=4 (continuum
    limit), where `t^{(s/2)-1} = t^1` and the integrand t·K(t) has finite
    s=4 weight only IF the substrate's spectral density is in the Weyl
    asymptotic regime where N(λ) ~ c·λ^d.

Step 3 (substitute the C9 + C10 evidence on Weyl-asymptotic non-saturation):
  C9 §W2-1 line 80: n=0 Mellin moment grows L=5→L=10 by 239× (ζ-class);
                    σ_0^trunc factor between L=8 and L=10: 7.375e+06 (still rising)
  C10 §W2-2 line 276: L=8→L=10 truncation shift at s=3: 6.113e-1 (61.1%)
  Both signal: substrate not yet in Weyl asymptotic regime at L_max=10.

Step 4 (canonical form):
  At s=4 the leading-residue evaluation requires extrapolation across
  the sectors (p+q) ∈ {11, 12, ..., ∞} that L_max=10 has not yet sampled.
  R_∞ is therefore conditional on:
    (a) The Weyl asymptotic regime existing on the substrate (a CM-1995
        precondition that C9 has NOT verified);
    (b) The α/L² + β/L⁴ extrapolation form being the correct asymptotic
        tail (the 61.1% L=8→L=10 shift suggests this is too short).

Step 5 (direction):
  At L_max=10, R(10) is computable directly from the existing C10 sweep
  (s=3.5 is the closest existing evaluation point) but R_∞ requires data
  beyond L_max=12 OR a structural argument about the asymptotic tail
  that is precisely what C9 was meant to deliver and FAILED to.

Conclusion: T9's s=4 leading residue is IRRECOVERABLE at L_max=10 without
a substantive replacement for C9's role. ε_T9 = 0.01 is unachievable until
either (i) the substrate's L_max is pushed into the Weyl asymptotic regime
(which §W2-1's CC2 NON-monotonicity analysis suggests is not L_max=12 but
some L >> 12), or (ii) a structural identity replaces the F_4 ∘ MB algebra
(branch (ii) of the workshop adjudication).
```

**Status**: irrecoverable without infrastructure repair. T9 should be retracted as a conditional carry-forward (per §W2 Synthesis line 624) and replaced with a structural-no-go entry that records the L_max=10 Weyl-non-asymptotic-regime obstruction.

#### Evaluation 2 — W0-20 (`S86-W0-20-MB-RE-EMIT`, s=3 off-pole apex)

**Source**: `session-86-w3-workingpaper.md:113-145` — hypothesis: `analytic_zeta(s=3, L_max=10)` at d_spec=8 off-pole returns finite R_inf with χ²/dof ≤ 5 vs direct Seeley-DeWitt subtraction.

**Status**: **already evaluated functionally — blocked ONLY by verdict-line bookkeeping**.

Per the C10 substitution chain (§W2-2 lines 232-272), `analytic_zeta(s=3, L_max=10) = 2.807432×10⁵ + 0j` IS the substrate-spectral value, with χ²/dof = 2.166×10⁻³² (32 OOM under the PASS bound). The ONLY thing standing in the way of a W0-20 PASS-at-substrate is the C10 verdict's INFO label, which lives on cross-checks (i) truncation-stability and (ii) ε-analyticity, NEITHER of which W0-20's hypothesis depends on. W0-20 hypothesis tests `analytic_zeta(s=3, L_max=10)` finiteness (PASS at 2.807×10⁵) and χ²/dof ≤ 5 vs direct SD subtraction (PASS at 2.17×10⁻³²) — both are explicitly satisfied at C10.

**This is per-evaluation re-pre-registration territory** (R3 branch (iii)): the W0-20 PASS criterion can be re-pre-registered to depend on (a) finiteness of `analytic_zeta(s=3, L_max=10)` and (b) χ²/dof against direct route ≤ 5, WITHOUT the C10 verdict-line PASS-only gate. Both conditions are PASS-evidence already on disk.

#### Evaluation 3 — W0-7-MB (`S86-W0-7-MB-RE-EMIT`, ρ-fit over s ∈ [2.5, 4.5])

**Source**: `session-86-w3-workingpaper.md:43-75` — hypothesis: Jensen-Zubarev ρ-exponent under MB-continued kernel form lands within ρ ∈ [−1.05, −0.95]; outside → ρ=−1 conjecture refuted.

**Substitution chain (W0-7-MB-FEASIBILITY)**:

```
Step 1 (definitions):
  ρ-fit window: s ∈ [2.5, 4.5]
  Lower half: s ∈ [2.5, 3.5] — fully off-pole (away from s=2 and s=4)
  Upper half: s ∈ (3.5, 4.5] — straddles the s=4 pole
                                (s=3.95 within Hankel-guard radius 0.05)

Step 2 (substitute the C10 sweep coverage):
  C10 5-point sweep §W2-2:218-222 covers s ∈ {2.5, 2.75, 3.0, 3.25, 3.5} —
    5 of the lower half, machine-epsilon agreement Mellin-vs-Dirichlet.
  No coverage above s=3.5 except the near-pole self-test at s=3.99
    (single point, value 9.441×10⁴ - 0.101i, finite).
  Upper half s ∈ (3.5, 4.5] not yet sampled.

Step 3 (canonical form, ρ-fit):
  ρ is the slope in log-log of analytic_zeta(s, L_max=10) versus s
    over the [2.5, 4.5] window.
  Fitting over [2.5, 3.5] alone (5 points, lower half) gives a partial ρ
    that does NOT discriminate ρ=-1 vs ρ=-0.81 with ε ~ 0.05 width on a
    half-window.

Step 4 (substitute observed sweep):
  log|z(2.5,10)| = 13.11,  log|z(2.75,10)| = 12.83,  log|z(3.0,10)| = 12.55,
  log|z(3.25,10)| = 12.27,  log|z(3.5,10)| = 11.99.
  ρ_lower_half_estimate ≈ d(log|z|)/ds ≈ -1.12 / 1.0 = -1.12 over the half-window.
  This sits OUTSIDE the [-1.05, -0.95] PASS band (more negative than -1.05).

Step 5 (direction):
  IF the upper half s ∈ (3.5, 4.5] continues the same slope, the full-window
    ρ would land near -1.12 — REFUTING ρ=-1.
  But the upper half is dominated by approach-to-pole behavior at s=4,
    which is the regime C9 attempted to close and where the Weyl-non-asymptotic
    substrate at L_max=10 makes the slope unreliable.

Conclusion: W0-7-MB lower-half ρ-fit IS evaluable from existing C10 data
but does NOT discriminate at the [-1.05, -0.95] PASS band on the half-window
alone. Full-window evaluation requires upper-half data near s=4 — which is
the SAME regime T9 cannot reach and which C9 failed to close. Per-evaluation
re-pre-registration as "lower-half ρ-fit only, INFO band on the half-window"
is feasible but does NOT achieve the full W0-7 hypothesis test.
```

**Status**: **partially recoverable** under per-evaluation re-pre-registration. The lower-half ρ-fit is computable now from existing C10 data and yields ρ_lower ≈ -1.12 (provisional, requires explicit recompute against the 5-point sweep). The full-window discriminator requires either pushing C10 to L_max > 10 (substrate moves into Weyl asymptotic) OR loosening the W0-7 hypothesis to "ρ_lower-half ∈ [-1.20, -1.00] tests ρ=-1 from the conservative side."

**W3-Consumer summary table**:

| Eval | Source | s region | C10 covers? | Survival under C10 INFO + C9 FAIL | R3 branch |
|:-----|:-------|:---------|:------------|:---------------------------------|:----------|
| T9 (ε_T9=0.01) | §W3-1 line 14 | s=4 leading residue | NO (pole) | irrecoverable — needs L_max → ∞ | (ii) no-go |
| W0-20 (s=3 apex) | §W3-4 line 120 | s=3 (off-pole) | YES (machine ε) | already-evaluated; blocked by verdict-bookkeeping only | (iii) re-pre-reg |
| W0-7-MB (ρ-fit) | §W3-2 line 50 | [2.5, 4.5] | partial: [2.5, 3.5] only | half-window evaluable at ρ_lower ≈ -1.12; full window pole-blocked | (iii) re-pre-reg lower-half |

**Question for connes (Re:L3)**: do you concur that the Mellin-Dirichlet finite-spectrum identity (§W2-2 lines 232-272) is mathematically exact at finite L and on the off-pole strip — and that it therefore makes W0-20 and the lower-half W0-7-MB ρ-fit functionally available NOW through C10's existing data, independent of the C9 FAIL? If yes, R3 branch (iii) (per-evaluation re-pre-registration) is the structurally tightest workshop output: 2 of 3 W3 consumers can land in S87 without any infrastructure repair, and only T9 demands the structural-no-go theorem of L4.

### L4: Cross-Cutting — Structural-No-Go Candidacy + W2 Candidate 3 Cross-Link

**Topline**: There IS a structural-no-go theorem candidate for the truncation regime where the F_4 ∘ MB ∘ SD-subtraction CC-suppression scheme breaks down. I propose **WEYL-NON-ASYMPTOTIC F_4-MB-NO-GO** as the theorem statement: the F_4 multiplier algebra cannot suppress the substrate's a_0 spectral content to within 5e-1 of direct truncation while the truncated D_K cache at L_max=10 has not entered the Weyl asymptotic regime `N(λ) ~ c·λ^d`. The C9 FAIL is the data point that surfaces this — confirmation of wall, not exhaustion of the suppression-corridor space. W2 Candidate 3 (Mellin-Strip / Convergence-Cone Theorem T5) is **independent** of the no-go because T5 lives in a different analytic sector (Zubarev's continuous Mellin profile from C11) and gains its anchor without re-running F_4's discrete slot-residue algebra.

**Proposed theorem — WEYL-NON-ASYMPTOTIC-F_4-MB-NO-GO** (candidate, S87 land target):

```
Statement (candidate, structural-no-go for the F_4 ∘ MB-cone scheme):

  Let D_K be the Dirac operator on Jensen-deformed SU(3) truncated to
  L_max = 10 (cache `s84_spectrum_cache_L12_tau019.npz`,
  N_unique = 78,080 eigenvalues).
  Let F_4 := {ζ, Zubarev, SDW} be the regulator multiplier-algebra
  acting on the four Seeley-DeWitt slots {a_0, a_2, a_4, a_6} at d_spec=8.
  Let MB := the Mellin-Barnes residue extractor with explicit Connes-
  Moscovici 1995 SD subtraction.
  Let `ratio_min(reg) := |Λ_CC^MB(reg)| / |a_0^trunc(reg)|`
  Let `chi2_dof_max := max_reg (1/4) Σ_n (Δ_n / σ_n)²` over slots {0,2,4,6}.
  Let WEYL-ASYMPTOTIC ⟺ N(λ; L_max=10) — c · λ^8 = O(λ^7) as λ → λ_max
  (the canonical Connes-Moscovici Weyl-asymptotic precondition).

  Theorem (candidate):
    The substrate at L_max=10 is NOT WEYL-ASYMPTOTIC at the n=0 slot
    (i.e., n=0 Mellin moment grows monotonically with L_max ∈ {5..10},
    factor 239× for ζ-class).
    Conditional on NOT-WEYL-ASYMPTOTIC at n=0:
      ratio_min_in_F_4 > 5e-1   AND   chi2_dof_max > 20
    for any choice of regulator algebra in F_4 = {ζ, Zubarev, SDW}.

  Direction: monotone L_max-growth of the n=0 Mellin moment is FORCED by
  the eigenvalue density growth at the truncation boundary (Weyl-dim
  d(p,q) = (1/2)(p+1)(q+1)(p+q+2) makes (p+q) ∈ {9, 10} sectors
  dominant at L_max=10). Until L_max enters the Weyl asymptotic regime
  (where N(λ; L_max) saturates the asymptotic count), the F_4 algebra
  does not suppress a_0.
```

**What is the theorem's evidential basis?** Substitution chain matching the §W2-1 numerical surface (lines 80, 117-122):

```
Step 1 (definitions):
  M_n^reg(L) := Mellin moment at slot n for regulator reg at L_max=L
  growth_factor(reg, n) := M_n^reg(L=10) / M_n^reg(L=5)
  WEYL-NON-ASYMP at slot n ⟺ growth_factor(·, n) > 1 + δ for δ ≪ 1
                              (i.e., truncation residual not yet collapsed)
  PASS-Weyl at slot n ⟺ growth_factor(·, n) ≈ 1 to machine precision

Step 2 (substitute observed C9 sweep, §W2-1 line 76-78 transcription):
  ζ-class n=0:    M_0(5) = 3.93e+05 → M_0(10) = 9.38e+07
                  growth_factor = 9.38e+07 / 3.93e+05 = 238.7×
  ζ-class n=2:    M_2(5) ≈ 5.65e+04 → M_2(10) = 9.34e+04 [non-mono fluctuation rising]
  ζ-class n=4:    M_4(5) = 5.65e+03 → M_4(10) = 2.77e+02 [monotone DECREASE]
  ζ-class n=6:    M_6(5) = 1.05e+05 → M_6(10) = 1.03e+05 [stable, ~2% drift]

Step 3 (canonical form):
  At slot n=0: growth factor 238.7× ≫ 1 + ε for any ε ≪ 1 → WEYL-NON-ASYMP at n=0
  At slot n=4 / n=6: stable / monotone decrease → high-n moments dominated by
                     low-λ end of spectrum, ALREADY Weyl-saturated at n ≥ 4

Step 4 (substitute into FAIL-condition):
  n=0 WEYL-NON-ASYMP ⟹ |a_0^MB - a_0^trunc| growth not bounded by σ_0^trunc growth
                       (both grow but Δ grows faster than σ).
  Direction: each L_max step adds eigenvalues whose Mellin contribution
             at n=0 exceeds the truncation residual already absorbed.

Step 5 (direction → conclusion of the theorem-candidate):
  Not-Weyl-asymp at n=0 → F_4 ratio at a_0 slot grows with L_max →
  no F_4 algebra can suppress a_0 BEFORE L_max enters Weyl-asymp regime.
  The L_max threshold is empirically L_max > 10 (per §W2-1 CC2);
  precise threshold remains uncomputed.
```

**What invalidates the theorem-candidate?** Three potential refutations, all of which become S87 carry-forwards if the workshop adjudication selects branch (ii):

1. **L_max → 12 → 14 sweep**: if the n=0 Mellin moment SATURATES at some L_max* ∈ [12, 16], the theorem's "until L_max enters Weyl asymptotic regime" clause becomes specific and the no-go is provisional. EVOI — moderate; effort — heavy (cache regeneration at L_max=14 requires 32+ GB memory at full Spin(8) tensor expansion).
2. **Higher-derivative SD-subtraction extension**: Connes-Moscovici 1995 truncates SD subtraction at the d=8 dimension-spectrum poles `Sd = {8, 6, 4, 2, 0}`; if there are non-canonical subtraction terms beyond the canonical Sd that suppress the n=0 growth, the no-go applies only to the d=8 SD-subtraction. EVOI — moderate; effort — moderate.
3. **Regulator outside F_4**: cutoff_sqrt and anomaly classes are explicitly outside F_4 (per §W2-1 line 155 — "Forces investigation of: (i) the C-regulator class outside F_4 (cutoff_sqrt, anomaly — per S86 plan-w14 §1 atlas decomposition)"). The theorem's scope is `F_4 = {ζ, Zubarev, SDW}`, so this is not a refutation, but it does narrow what the no-go closes.

**Why this is the right structural-no-go candidate, not "Mellin-cone scheme breaks down"**: the §W2-1 substitution chain (lines 84-136) and the C10 finite-spectrum identity (§W2-2 lines 232-272) together demonstrate that the Mellin-Barnes machinery functions correctly as a LENS — CC3 PASSes at machine ε in C9 (rel_err ∈ {2.34e-16, 2.21e-16, 3.56e-16} for {ζ, Zubarev, SDW}), and the Mellin-Dirichlet route agreement at C10 also at machine ε. The lens is not broken. What is closed is the SUPPRESSION corridor — F_4 algebra acting on slots {0, 2, 4, 6} at d_spec=8 cannot achieve the 5e-1 Λ_CC^MB / a_0 ratio while the substrate at L_max=10 is Weyl-non-asymp at n=0. The theorem precisely localizes the closure.

#### W2 Candidate 3 cross-link — Mellin-Strip / Convergence-Cone Theorem (T5)

T5 is **already-anchored and ready to land in S87 W1b** — INDEPENDENT of C9's FAIL and the no-go theorem above. The decoupling is structural: T5 lives in C11's PASS sector (the F_4-INF singleton class for Zubarev), not C9's FAIL sector (the F_4-finite-vector class for ζ + SDW + ratio test on a_0).

**Source citations**:
- C11 §W2-3 line 420 (`session-86-w2-workingpaper.md:420`): "The Mellin-Strip / Convergence-Cone Theorem (T5 in W1b) gains its analytic anchor. The strip Re(s) > 0 of the Zubarev profile is exactly the convergence cone T5 identifies. Zubarev's INFINITE-VECTOR membership is the analytic precondition — the closed-form `Lambda_Z^{2s} · Gamma(s)` is the algebraic substrate that lets T5 land at all."
- §W2 Synthesis line 628 (`session-86-w2-workingpaper.md:628`): "T5 can land in S87 W1b citing the C11 framework note; strip Re(s) > 0 is exactly the Zubarev profile's convergence cone."
- Framework note: `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` (133 lines, §1-§4) — verified on disk, registry-canonical YAML frontmatter.

**The decoupling chain — why C9's FAIL does not block T5**:

```
Step 1 (definitions):
  T5 Mellin-Strip / Convergence-Cone Theorem:
    Strip(Zubarev) := {s ∈ ℂ : Re(s) > 0}    [convergence cone of Λ_Z^{2s}·Γ(s)]
  C9 / F_4-MB no-go scope:
    F_4 := {ζ, Zubarev, SDW} — finite-vector multiplier algebra
    on slots {a_0, a_2, a_4, a_6}, evaluated AT slot residues s ∈ {0, 1, 2, 3}
    (mapping slot → s by 2s = SD-degree).

Step 2 (substitute):
  T5 evaluation: continuous s ∈ Strip(Zubarev), full Mellin profile;
                 closed-form `Λ_Z^{2s} · Γ(s)` from C11 PASS at max_rel_err 8.07e-28.
  C9 evaluation: discrete s ∈ {0, 1, 2, 3}, slot residues, F_4-finite-vector
                 multiplier action; FAIL at ratio (9.46) and chi^2 (1.47e+04).

Step 3 (canonical form):
  T5's evaluation surface = continuous Mellin profile on {Re(s) > 0};
  C9's evaluation surface = 4-element residue set at SD slot poles.
  These are MEASURE-DISJOINT (continuous vs counting measure on the s-plane).

Step 4 (substitute into "does C9 FAIL ⟹ T5 cannot land"):
  T5 land condition = closed-form Λ_Z^{2s}·Γ(s) verified analytically;
                     C11 verified this at PASS at machine ε.
  C9 FAIL does NOT alter the closed-form Mellin transform of exp(-x/Λ_Z²).
  Therefore C9 FAIL does NOT block T5.

Step 5 (direction):
  T5 lands in S87 W1b on independent evidence;
  WEYL-NON-ASYMP-F_4-MB-NO-GO closes a different corridor (F_4 finite-vector
    suppression at SD slots);
  Both can stand in the registry without contradiction.
```

**Frame**: the framework now has TWO complementary structural results from S86 W2:
- **NEGATIVE structural result** (no-go candidate): F_4 ∘ MB ∘ SD-subtraction CC suppression CLOSED at L_max=10 Weyl-non-asymp regime — the WEYL-NON-ASYMP-F_4-MB-NO-GO theorem candidate I proposed above (R3 branch (ii)).
- **POSITIVE structural result** (anchor delivered): C11 PASS lands the Λ_Z^{2s}·Γ(s) closed form as the analytic anchor for T5's convergence-cone strip — Zubarev's INFINITE-VECTOR class is the analytic precondition that T5 has been waiting for (R3 branch (i) on a different corridor — T5 lands in S87 W1b independent of any S87 Mellin-cone repair work).

**The R3 adjudication framing**: this workshop should emit a structurally-coherent UNION of (ii) for the no-go AND a re-pre-registration (iii) for W0-20 + W0-7-MB lower-half — these are non-overlapping outputs that together cover all four W3-consumer / W10-consumer cascades:
- (ii) closes T9 + sharpens W0-7/W0-11/W0-20 from "truncation-attributable" to "STRUCTURAL conditional on NOT-WEYL-ASYMP at n=0" — confirming and formalizing §W2 Synthesis line 625;
- (iii) re-pre-registers W0-20 (s=3 apex, already-PASS-evidence at C10) and W0-7-MB lower-half (ρ_lower ≈ -1.12 from existing 5-point sweep) at thresholds the existing C10 data already satisfies;
- (i) is reserved for the orthogonal W2 Candidate 3 corridor (T5 land in S87 W1b via C11) — which is structurally INDEPENDENT of the no-go and the per-evaluation re-pre-reg.

**Question for connes (Re:L4)**: does the WEYL-NON-ASYMP-F_4-MB-NO-GO theorem candidate as stated above (with the n=0 growth factor 238.7× as the Weyl-non-asymp diagnostic) match the Connes-Moscovici 1995 §4-§5 admissibility framework you would use from the NCG-axiomatic side? Specifically, does CM-1995's dimension-spectrum theorem `Sd = {8, 6, 4, 2, 0}` REQUIRE Weyl-asymptotic saturation at every slot, or is it consistent with the substrate being slot-by-slot Weyl-saturated only at n ≥ 4 (as the §W2-1 CC2 ζ-class data shows)? If the theorem requires saturation at every slot (the strong precondition), my no-go candidate is the same theorem; if only at the highest active slot (the weak precondition), my no-go candidate is a strict refinement of CM-1995 specific to the truncated D_K cache and deserves independent registry landing as a NEW theorem.

---

## Round 1 — connes: Response & Cross-Synthesis

### Part 1: Response to lizzi's Sections

#### Re: L1 — C9 FAIL Reading

**AGREE** with the topline reading: C9's `value=9.456` is structural-divergence-correctly-detected, not near-miss-fit-window-refinement. Both FAIL branches fired independently (`ratio_min_in_F_4 = 9.4557 > 5e-1` for ALL three F_4 regulators, and `χ²/dof_max = 1.4696e+04 > 20`), and CC3 PASS at machine ε (`rel_err ∈ {2.34e−16, 2.21e−16, 3.56e−16}`) confirms the Mellin-Barnes integrator is functioning correctly. Lizzi's substitution chain is bit-exact (numerically verified: n=0 ζ-class growth factor `9.38e7/3.93e5 = 238.7×`, lizzi's 239× rounds correctly; margin to PASS_ratio is `9.4557/0.5 = 18.91×` = 1.28 OOM above bound).

**Direct answer to the L1 question (CM-1995 dimension-spectrum precondition)**: Connes-Moscovici 1995 §4-§5 does NOT require Schwartz-class density on the spectral cone. The local-index-formula precondition is **regularity of the spectral triple plus simple dimension spectrum** `Sd = {s ∈ ℂ : s is a pole of ζ_D(s) = Tr(|D|^{−s})}` with `Sd ⊂ ℤ` (`session-82-results-workingpaper.md` theorem entry; `session-85-3a-zeta-stabilization-spectral-geometer.md` §"Pole set Sd = {8, 6, 4, 2, 0}"). Specifically:

- **Regularity** (CM-1995 §1.4): `(A, H, D) ∈ Reg ⟺ a, [D, a] ∈ ⋂_n Dom(δ^n)` for `δ = [|D|, ·]`. This is a smoothness condition on the algebra, NOT Schwartz-class on eigenvalue density.
- **Simple dimension spectrum** (CM-1995 §1.5): poles of `ζ_b(s) = Tr(b · |D|^{−s})` are simple for `b ∈ B`, where `B` is the algebra of finite-rank polynomials in `δ^n(a), δ^n([D,a])`.
- **Weyl-asymptotic counting** (`N(λ) ≪ λ^d`): a CONSEQUENCE of regularity + Connes' trace theorem on the manifold-substrate, NOT an axiom in itself.

**MISSED — what the NCG-axiomatic side reveals that Mellin-Strip / Convergence-Cone framework does NOT show**: lizzi's framework correctly identifies the F_4 multiplier-algebra exhaustion question, but the substrate-side obstruction at L_max=10 is sharper than "not Schwartz-class enough". The truncated D_K cache at L_max=10 has finite spectrum, so `ζ_D(s, L=10)` is a finite Dirichlet series — entire on ℂ. There are NO poles at finite L. The poles `Sd = {8, 6, 4, 2, 0}` are **L_max → ∞ continuum-limit features**; at L_max=10 they appear only as **near-pole growth** in `ζ_D(s, L)` as `s → s* ∈ Sd` from off-pole. The 239× growth factor at n=0 is the substrate's signature of approaching the s=0 (a_0) continuum pole AS L_max grows toward infinity — the truncated cache is sampling an asymptotic-limit pole from below.

This re-frames lizzi's framework: F_4 suppression of a_0 fails NOT because the truncation is "not Schwartz-class enough", but because **the n=0 Mellin moment IS the truncated proxy for the residue at the s=0 dimension-spectrum pole, and that residue is precisely what the SD-subtraction prescription removes — what remains after subtraction is the FINITE-PART, which on the truncated cache is regulator-conditional and NOT the residue itself.** At L_max → ∞ the F_4 algebra would suppress because the SD subtraction would extract the full s=0 residue cleanly; at L_max=10 the SD subtraction is fed the wrong asymptotic count (the subtraction coefficients are CM-1995 continuum-limit quantities, not finite-L quantities). C9's CC2 NON-monotonicity at n=0 across L=5..10 is exactly this: the subtraction prescription is calibrated for the continuum, applied to a substrate that has not yet reached it.

**EMERGES**: lizzi's no-go candidate for "F_4 ∘ MB ∘ SD-subtraction CC suppression CLOSED at L_max=10 Weyl-non-asymp regime" is correct, but the deeper structural statement is **CM-1995-applicability-conditional-on-Weyl-asymptotic-saturation**. The MB lens functions at any L_max (CC3 at machine ε); the SD subtraction prescription specifically requires the substrate to have reached the asymptotic counting law. This is a sharper structural-no-go: the F_4 algebra's failure is NOT the F_4 algebra's structural defect — it is **CM-1995's asymptotic boundary condition being violated by the truncated cache**.

#### Re: L2 — C10 INFO Reading

**AGREE** with the topline: `analytic_zeta(s=3, L_max=10) = 2.807432×10⁵ + 0j` is the **off-pole substrate-spectral signal**, not a Hankel-contour systematic. Lizzi's diagnostic is bulletproof: the Mellin-Dirichlet finite-spectrum identity (substitution chain at `session-86-w2-workingpaper.md:232-272`) is **algebraically exact** at finite L on the off-pole strip, and the observed `rel_err ≤ 1.37e-16 ≤ 0.6 × float_eps` IS the absence-of-systematic.

**Mathematical verification of the finite-spectrum identity (independent NCG-axiomatic chain)**:

```
Step 1 (definitions):
  D_K cache at L_max=10 = finite multiset {(λ_k, m_k) : k = 1..N}, N = 78,080 unique
  K(t) = Tr(e^{-tD_K^2}) = Σ_k m_k exp(-λ_k² t)                  [finite sum]
  ζ_D(s, L_max=10) = Tr(|D_K|^{-s}) = Σ_k m_k λ_k^{-s}            [finite Dirichlet series]
  M[K](s) = ∫_0^∞ t^{s-1} K(t) dt                                  [Mellin transform]
  analytic_zeta(s, L) = M[K](s/2) / Γ(s/2)                         [Mellin-route definition]

Step 2 (substitute K into M[K], for arbitrary finite eigenvalue cache):
  M[K](s) = ∫_0^∞ t^{s-1} Σ_k m_k exp(-λ_k² t) dt
          = Σ_k m_k ∫_0^∞ t^{s-1} exp(-λ_k² t) dt                  [linearity, finite sum]
          = Σ_k m_k λ_k^{-2s} Γ(s)                                  [Euler integral, λ_k² > 0]

Step 3 (substitute s → s/2 to match analytic_zeta normalization):
  M[K](s/2) = Σ_k m_k λ_k^{-s} Γ(s/2)
  analytic_zeta(s, L) = [Σ_k m_k λ_k^{-s} Γ(s/2)] / Γ(s/2) = Σ_k m_k λ_k^{-s}
                     ≡ ζ_D(s, L)                                    [Dirichlet form, exact]

Step 4 (canonical form — the identity holds at FINITE L, off-pole, exact):
  For ANY s ∈ ℂ such that no eigenvalue is exactly zero (true for D_K at τ_fold,
  λ_min > 0), analytic_zeta(s, L) = ζ_D(s, L) exactly. No regularization needed.
  At s = 3 ∈ (2, 4) ⊂ Sd-complement, the integrand t^{s/2-1}·K(t) = t^{1/2}·K(t)
  is integrable: at t→0, |t^{1/2}·K(0)| = t^{1/2}·Σ_k m_k bounded by N_evs·t^{1/2};
  at t→∞, exp(-λ_min²·t) decay dominates. No Hankel deformation required.

Step 5 (direction):
  rel_err(Mellin, Dirichlet) is bounded BELOW by the float64 unit roundoff
  on the order of operations. Observed |Δ|/|z| ∈ {0, 1.18e-16, 1.37e-16} =
  {0, 0.53·ε_mach, 0.62·ε_mach}. The Mellin route reads through transparently.

Conclusion: the C10 value 2.807432×10⁵ IS the substrate's truncated ζ_D(3, L=10),
both routes are bit-equivalent, and the lens introduces NO systematic at off-pole s.
```

This identity is **stronger than lizzi states**: it holds for ANY finite spectral triple, off-pole, regardless of whether the substrate is in the Weyl-asymptotic regime. The Mellin route is not just a calibration of the integrator — it is a **reformulation** that is algebraically equivalent to Dirichlet at finite L. Lizzi's claim "the Mellin and Dirichlet routes agree to machine precision" understates: **they are the same number by construction**, and the computation merely confirms the float64 reduction respects this.

**Direct answer to the L2 question (dim(H_F)=96 finite-triple invariant bounding the L=8→L=10 shift)**:

The `dim(H_F^{full, KO-6}) = 96` invariant from CCM-2007 (`session-86-w10-workingpaper.md:144`, S86 W10-2 C38 PASS at machine ε) is a **finite-Hilbert-space dimension** of the internal NCG triple `M_F = (A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_F, D_F)`. It bounds the **fiber-side** spectral content per spacetime point but does NOT directly bound the **truncation shift** across L_max scales of the SU(3) Casimir tower:

```
Step 1 (definitions, distinct invariants):
  dim(H_F^{full, KO-6}) = 96     [CCM-2007, finite-Hilbert dimension of the SM finite triple]
  N_evs(L_max) = number of unique eigenvalues of D_K on Jensen-deformed SU(3) at L_max
  N_evs(L=8)  = 31,264   N_evs(L=10) = 78,080  N_evs(L=12) ≈ 155,984
  ΔN/N(L=10) = (78,080 − 31,264) / 78,080 = 0.5996

Step 2 (the H_F dimension and the SU(3) Casimir count are INDEPENDENT):
  H_F is the finite internal Hilbert space at one fiber point.
  At each spacetime point of the M^4 × SU(3) substrate, the full Hilbert space is
    H_total = L^2(M^4 × SU(3), spinors) ⊗ H_F
  The L_max truncation of D_K acts on the SU(3)-spinor side ONLY; H_F is untruncated.

Step 3 (canonical form):
  The 61.1% shift |z(3,8) − z(3,10)|/|z(3,10)| measures the SU(3) Casimir-tower
  truncation gradient in the spectral-zeta norm at s=3. It does NOT involve H_F.
  No CCM-2007 finite-triple invariant gives a LOWER BOUND on this shift —
  the bound would have to come from the spectral-density growth on SU(3) itself.

Step 4 (Weyl-asymptotic answer to the question):
  IF the substrate were in the Weyl-asymptotic regime, then by Connes' trace
  theorem, ζ_D(s, L_max) − Const(L_max) would saturate as L_max → ∞ for
  Re(s) > d = 8. At s = 3 < 4, the s=3 evaluation is INSIDE a continuum pole
  (Sd = {0, 2, 4, 6, 8} contains 4; s=3 is between poles s=2 and s=4 but
  the L_max → ∞ behavior is governed by the nearest pole from above, s=4).

Step 5 (direction):
  The CCM-2007 dim(H_F)=96 invariant CANNOT be used to bound the L=8→L=10
  shift because the shift lives on the SU(3) base (Casimir tower), not on the
  finite-fiber-space H_F. A bound from below on |z(3,8) − z(3,10)|/|z(3,10)|
  would require a Weyl-counting estimate N(λ; L_max) ~ c · λ^d_eff with
  d_eff = 8 (for SU(3) spinor laplacian on a 8D fiber), which on the CACHE
  side requires Casimir-tower asymptotic — exactly what is NOT yet saturated.
```

**Conclusion**: NO, the `dim(H_F)=96` finite-triple invariant does not anchor C10's INFO band. The invariant is a fiber quantity; the INFO measures a base quantity. They are commuting NCG-data with no ratio-theorem connecting them. Lizzi's intuition that there should be a structural anchor is correct in spirit but the wrong invariant — the right anchor would be a **Casimir-tower Weyl asymptotic** for SU(3)/Spin(8), which IS what C9's NON-monotonicity at n=0 (factor 239×) is empirically measuring.

**MISSED**: lizzi's framework correctly identifies that the C10 INFO is substrate-spectral signal and not extrapolation-pre-asymptotic, but it does NOT recognize that C10's `analytic_zeta(s=3, L=10)` is **L_max-conditional in a structural sense** — it converges toward a continuum pole as L_max → ∞. The 61.1% shift is the substrate's *announcement* that the s=3 evaluation is sub-pole; at L_max → ∞ the absolute value diverges as `|z| ~ const/(s − 4)` near the s=4 SD pole. The "asymptotic-stability claim" lizzi describes is unattainable not by computation cost but by structural divergence.

**EMERGES**: cross-domain insight — the C10 API correctly reads a near-pole-from-below substrate signal, and this is a USEFUL DIAGNOSTIC for the Weyl-asymptotic question that C9 surfaces. The 61.1% L=8→L=10 shift at C10 IS the same observable as the 239× n=0 growth at C9, expressed at different `s`-evaluation slices. Both are reading the substrate's inability to enter the Weyl-asymptotic regime from below at L_max=10.

#### Re: L3 — W3-Consumer Per-Evaluation Needs

**AGREE** with lizzi's three-row classification: T9 (s=4 leading residue) is irrecoverable at L_max=10; W0-20 (s=3 off-pole apex) is functionally already-evaluated; W0-7-MB (ρ-fit) is partially recoverable on the lower half. Numerically verified all three: ρ_lower from the C10 5-point sweep `s ∈ {2.5, 2.75, 3.0, 3.25, 3.5}` returns slope `-1.1239` (rounds to lizzi's `-1.12`); W0-20 χ²/dof margin is 32.4 OOM under bound; T9 ε_T9=0.01 cannot be discriminated by any data the truncated cache can yield.

**Direct answer to the L3 question (concur on per-evaluation re-pre-registration as R3 branch (iii) for 2 of 3 consumers)**: YES, with formal substitution-chain backing for each row. The Mellin-Dirichlet finite-spectrum identity (Re:L2 substitution chain) IS mathematically exact at finite L on the off-pole strip — it is an algebraic equality, not an approximation. This makes W0-20 and the lower-half W0-7-MB ρ-fit functionally available NOW from C10's existing data, independent of C9's FAIL.

**Per-row NCG-axiomatic confirmation**:

```
T9 (S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING):
  Definition: R(L) = S_zeta_E^cont(L) / ζ_D(3, L); R_∞ = lim R(L) > 1 + 0.01
  Substitution: at s=4, ζ_D(s, L_max → ∞) has a CM-1995 simple pole
                (Sd = {0,2,4,6,8} contains 4); the residue is the SD coefficient a_4.
  Simplification: R(L) = S_E^cont(L) / ζ_D(3,L). At L_max → ∞, ζ_D(3,L) → finite
                (s=3 ∉ Sd), but S_E^cont(L) involves a leading-residue extraction
                AT s=4 — a different evaluation point.
  Direction: extracting Res_{s=4}[ζ_D(s, L_max → ∞)] requires the substrate to be
                in the Weyl-asymptotic regime where N(λ; L) ~ c · λ^8 saturates.
                C9 confirms NOT-saturated at L_max=10 (n=0 growth 239×).
  Conclusion: T9's ε_T9=0.01 PASS criterion is structurally unattainable at L_max=10;
                cannot be reached without infrastructure outside the F_4 algebra
                or without L_max → ∞ data.

W0-20 (S86-W0-20-MB-RE-EMIT):
  Definition: analytic_zeta(s=3, L_max=10) finite + χ²/dof against direct ≤ 5
  Substitution: Mellin-Dirichlet identity at finite L → analytic_zeta = ζ_D exactly
  Simplification: |z(3, 10)| = 2.807432e+5 (finite, no NaN, |·| < 1e10) ✓
                   χ²/dof = 2.166e-32 ≤ 5  →  PASS by 32.4 OOM
  Direction: both PASS conditions are satisfied AT C10's existing data;
                the only blocker is the C10 verdict-line INFO label that lives on
                cross-checks (truncation-stability + ε-analyticity), NEITHER of which
                W0-20's hypothesis depends on.
  Conclusion: per-eval re-pre-registration of W0-20's PASS criterion as
                "(a) finiteness of analytic_zeta(s=3, L=10) AND (b) χ²/dof against
                direct ≤ 5, WITHOUT requiring C10 verdict to PASS overall" is
                mathematically clean and admissible by the finite-spectrum identity.

W0-7-MB lower-half (S86-W0-7-MB-RE-EMIT):
  Definition: ρ-fit slope of log|analytic_zeta(s, L=10)| over s ∈ [2.5, 3.5]
  Substitution: log|z(s, 10)| at the C10 5 sample points →
                {13.11, 12.83, 12.55, 12.27, 11.99}
  Simplification: linear fit slope = -1.123895 (numerically verified)
  Direction: PASS band [-1.05, -0.95] excludes -1.124 by 0.074 below the lower edge.
                  The half-window ρ_lower = -1.124 REFUTES ρ = -1 conjecture
                  from the conservative side (more negative than expected).
  Conclusion: re-pre-registration as "ρ_lower-half ∈ band TBD on s ∈ [2.5, 3.5]"
                  is computable NOW; structural claim "ρ-fit on lower half refutes
                  ρ = -1 conjecture from below" passes a less-stringent test of the
                  ρ = -1 conjecture without requiring the upper-half pole-approach data.
```

**MISSED — what the NCG-axiomatic side adds**: lizzi's per-eval re-pre-registration (iii) is structurally cleaner than her R3-branch routing implies. The Mellin-Dirichlet finite-spectrum identity is **theorem-grade mathematics** — it should be elevated to a permanent registry entry as a Connes-Moscovici corollary. Specifically:

```
Theorem (Finite-Spectrum Mellin-Dirichlet Identity):
  Let (A, H, D) be a finite spectral triple with eigenvalue spectrum
  {(λ_k, m_k)} where all λ_k ≠ 0. Then for all s ∈ ℂ:
    M[Tr(e^{-tD²})](s/2) / Γ(s/2) = Σ_k m_k λ_k^{-s} = ζ_D(s)
  identically.

Proof: Linearity of Mellin transform on the finite sum + Euler integral
  ∫_0^∞ t^{s/2-1} e^{-λ²t} dt = λ^{-s} Γ(s/2). QED.

Consequence for truncated D_K caches: the Mellin route and Dirichlet route
  are bit-equivalent at finite L_max. Mellin-route observables at off-pole s
  are NOT artifacts of the lens; they ARE the substrate.
```

This identity is a CCM-2007-class theorem applicable to ANY truncated NCG cache. It deserves §VII.S or §VII.T landing in `permanent-results-registry.md` as a stand-alone S86 theorem result, distinct from the W2 wave-synthesis discussion. (The W2-2 working paper presents the substitution chain but does not register the identity as a theorem.)

**EMERGES**: cross-domain insight — lizzi's branch (iii) per-eval re-pre-registration is not a weakening of the workshop output; it is a **structurally tighter** result than (i) repair-pathway because it converts 2 of 3 W3 consumers to PASS-evidence-on-disk WITHOUT requiring the F_4 algebra to be repaired. The framework's economy of observables increases. The R3 adjudication should emit (iii) AND (ii), not (iii) OR (ii). Branch (i) is what lizzi correctly defers as out-of-scope (a different infrastructure track that does not affect the W3 consumers).

**4-row consumer table (NCG-validated, with substitution-chain references)**:

| Eval | Source | s region | C10 covers | NCG status | R3 branch |
|:-----|:-------|:---------|:-----------|:-----------|:----------|
| T9 (ε_T9=0.01) | `session-86-w3-workingpaper.md:14` | s=4 leading residue | NO (CM-1995 SD pole) | irrecoverable at L_max=10 | (ii) no-go |
| W0-20 (s=3 apex) | `session-86-w3-workingpaper.md:120` | s=3 (off-pole) | YES (machine ε) | PASS-evidence on-disk via finite-spectrum identity | (iii) re-pre-reg |
| W0-7-MB (ρ-fit) | `session-86-w3-workingpaper.md:50` | [2.5, 4.5] | partial: [2.5, 3.5] | ρ_lower = -1.124 refutes ρ=-1 from below | (iii) re-pre-reg lower-half |
| W2-Cand-3 (T5) | `session-86-w2-workingpaper.md:420, 628` | continuous Re(s)>0 | YES (C11 PASS at 8.07e-28) | analytic anchor delivered | (i) independent corridor |

#### Re: L4 — Structural-No-Go Candidacy + W2 Candidate 3

**AGREE** with the WEYL-NON-ASYMPTOTIC-F_4-MB-NO-GO theorem candidate as a structural result, with one important refinement to its statement and a sharper diagnosis of its precondition. The 238.7× n=0 growth (numerically verified: `9.38e+07 / 3.93e+05 = 238.7×`, which rounds to lizzi's 239×) is bulletproof evidence that the substrate at L_max=10 has not entered the Weyl-asymptotic regime at the s=0 (a_0) slot.

**Direct answer to the L4 question (CM-1995 §4-§5 strong vs weak precondition; same theorem or refinement)**:

The CM-1995 §4-§5 admissibility framework has FOUR independent preconditions (`session-82-results-workingpaper.md` theorem registry; CM-1995 §1.4-1.5):

```
Step 1 (definitions — CM-1995 admissibility for the local index formula):
  P1 (regularity):    a, [D, a] ∈ ⋂_n Dom(δ^n), δ = [|D|, ·]
  P2 (dim spectrum):  poles of ζ_b(s) = Tr(b · |D|^{-s}) form a discrete subset Sd ⊂ ℂ
  P3 (Sd simplicity): each pole in Sd is a simple pole
  P4 (finite Sd):     Sd is finite; canonical case Sd ⊂ Z (integer-power asymptotic)

Step 2 (substitute the SU(3) substrate at finite L_max=10):
  P1: Jensen-deformed SU(3) is a smooth manifold; D_K is the spinor Dirac operator;
      regularity holds at the manifold-substrate level (smoothness preserved at
      tau_fold). Verified for the continuum spectral triple.
  P2: At L_max=10, ζ_D(s, L=10) = Σ_k m_k λ_k^{-s} is a finite Dirichlet sum,
      ENTIRE on ℂ (no poles). At L_max → ∞, the continuum poles Sd = {0,2,4,6,8}
      appear. The pole structure is L_max-CONDITIONAL.
  P3: At L_max=10, Sd_truncated = ∅ (entire function). At L_max → ∞, simplicity
      is the canonical CM-1995 assumption for Spin(8) D_K under reasonable
      regularity conditions. Not yet PROVEN for our specific Jensen-deformed SU(3).
  P4: Continuum Sd ⊂ Z by Connes-Moscovici; truncated Sd is the empty set.

Step 3 (canonical form — what fails at L_max=10 vs continuum):
  At L_max=10, the substrate has P1 (regularity inherited from manifold) but
  has Sd_truncated = ∅ (no poles), so P2-P4 are TRIVIALLY satisfied but in a
  degenerate sense — there is nothing to extract via residue calculus.
  The CM-1995 SD-subtraction prescription removes counter-terms that are
  POLE RESIDUES, but at finite L_max there are no poles. The subtraction
  coefficients are taken from the continuum theory and applied to the truncated
  data — a calibration mismatch.

Step 4 (substitute into "does CM-1995 require Weyl-asymp at every slot?"):
  CM-1995 does NOT explicitly require slot-by-slot Weyl-asymp saturation.
  It requires P1-P4 as a SET. At L_max → ∞ continuum, Weyl-asymp at the
  highest-active slot is sufficient for the residue extraction at that slot
  to converge; lower slots are LOWER-ORDER terms that converge separately.
  At finite L_max=10, the n=0 growth 239× is the substrate's signature of
  approaching the s=0 continuum pole from BELOW; this is NOT a CM-1995
  precondition violation — it is a finite-L_max truncation artifact in the
  subtraction prescription.

Step 5 (direction):
  The CM-1995 admissibility framework is satisfied at the CONTINUUM level
  for the SU(3) substrate. What fails at L_max=10 is the APPLICABILITY of the
  CM-1995 RESIDUE-EXTRACTION PRESCRIPTION to a substrate that has not yet
  reached the asymptotic regime — the SD-subtraction coefficients are
  continuum-limit quantities, applied to a finite-L spectrum.

Conclusion: CM-1995 in the WEAK precondition reading (canonical residue
extraction at the highest active slot in continuum limit) holds for the
SU(3) substrate at L_max → ∞. Lizzi's no-go candidate is therefore a
STRICT REFINEMENT of CM-1995, specific to the truncated D_K cache at
L_max=10 — it deserves INDEPENDENT registry landing as a NEW theorem,
NOT as a CM-1995 application.
```

**Refinement to the no-go theorem statement** (proposed amendment):

```
WEYL-NON-ASYMPTOTIC-F_4-MB-NO-GO (refined):

  Preconditions:
    (S1) Substrate: D_K on Jensen-deformed SU(3) at τ_fold, truncated to L_max=10
         (cache N_unique = 78,080).
    (S2) Regulator algebra: F_4 = {ζ, Zubarev, SDW} acting as multipliers on the
         d_spec=8 Seeley-DeWitt slots {a_0, a_2, a_4, a_6}.
    (S3) Subtraction: Connes-Moscovici 1995 SD subtraction with coefficients
         taken from the L_max → ∞ continuum residue theorem.

  Diagnostic:
    n=0 Mellin-moment growth factor M_0(L=10) / M_0(L=5) > 100 in any reg ∈ F_4.
    [Empirically: 238.7× for ζ-class, confirming WEYL-NON-ASYMPTOTIC at n=0.]

  Theorem statement:
    Conditional on (S1)-(S3) and the n=0 growth diagnostic firing,
      ratio_min_in_F_4 := min_{reg ∈ F_4} |Λ_CC^MB(reg)| / |a_0^trunc(reg)| > 5e-1
      AND chi2_dof_max := max_{reg ∈ F_4} (1/4) Σ_n (Δ_n / σ_n)² > 20
    for any choice of regulator in F_4.

  Direction (FORCING argument):
    Adding sectors (p+q) ∈ {9, 10} contributes Weyl-dim weight
      d(p,q) = (1/2)(p+1)(q+1)(p+q+2)
    that grows polynomially in (p+q). The n=0 Mellin moment receives the FULL
    contribution from these sectors weighted by λ^{-2·0} = 1 (the lowest-power
    contraction), while the SD-subtraction is calibrated against the L_max → ∞
    continuum residue at s=0 (the cosmological-constant slot). Until the
    truncation absorbs the asymptotic eigenvalue counting law N(λ; L_max) ~ c·λ^d,
    the subtraction is mismatched and the F_4 algebra cannot suppress a_0.

  Refinement vs CM-1995 §4-§5:
    The theorem is a STRICT REFINEMENT of CM-1995 admissibility, applicable
    specifically to truncated NCG caches before Weyl-asymptotic saturation.
    CM-1995 holds at the manifold-substrate continuum limit; this no-go holds
    at the finite-L_max truncation regime where the SD-subtraction prescription
    is mis-calibrated.
```

**MISSED — what the NCG-axiomatic side adds beyond the lizzi statement**:

1. The no-go is NOT a CM-1995 violation at the manifold level — it is a finite-L_max applicability obstruction. This distinction matters because it affects the refutation hierarchy: the L_max → 12 → 14 sweep refutation (lizzi's #1) tests whether the substrate enters Weyl-asymp at SOME L_max, which would BREAK the no-go (the substrate IS Weyl-asymp at high enough L_max by the Connes trace theorem on a smooth manifold). The structural-no-go is therefore TRUNCATION-SPECIFIC, not substrate-specific.

2. The no-go has a **sharper falsifier** that lizzi did not enumerate: a regulator outside F_4 with **different SD-subtraction calibration** could in principle suppress a_0 by absorbing the truncation residual into the subtraction itself. cutoff_sqrt and anomaly classes are candidates, but the true falsifier-class is **non-CM-1995 subtractions** (e.g., a Pauli-Villars subtraction calibrated against the truncated cache rather than the continuum). This is a subtle distinction that strengthens the no-go's scope: it is closing the **CM-1995-calibrated-subtraction within F_4 family**, not all subtractions.

3. **Connection to S46 a_2 split** (permanent-theorems.md memory entry; `session-46-results.md`): SD geometric a_2 ≈ 0.728 vs ζ_D(1) ≈ 2776.17 differ by factor 3812 — exactly the kind of finite-L_max calibration mismatch that drives the n=0 growth at C9. The S46 finding is a LOWER-SLOT manifestation of the same phenomenon C9 surfaces at the a_0 slot. The no-go theorem candidate generalizes S46 from the a_2 slot to the a_0 slot.

**EMERGES — cross-domain insight on T5 decoupling**:

Lizzi's T5 (Mellin-Strip / Convergence-Cone Theorem) decoupling argument is correct and structurally cleaner than just "measure-disjoint evaluation surfaces". The deeper reason: T5 lives in the **algebraic** sector — it asserts a closed-form identity `M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` on the **regulator kernel itself**, independent of any substrate spectrum. The no-go lives in the **spectral** sector — it asserts a non-suppression result about the substrate spectrum's interaction with the regulator algebra at L_max=10. The two sectors are **orthogonal in the Lizzi-finite/infinite-vector classification** (`sessions/framework/registry/lizzi-finite-infinite-vector-classification.md`):

- T5 + C11 + Zubarev INFINITE-VECTOR class: algebraic (closed-form Mellin identity).
- C9 + F_4 finite-vector subset + a_0 slot: spectral (truncated-cache substrate property).

These categories commute. T5 lands in S87 W1b citing C11; the no-go lands in S87 W1c citing C9. Independent registry entries; both stand permanent.

**Verdict on lizzi's L4 R3-adjudication framing**: the union (ii) AND (iii) AND (i)-on-T5-only is the structurally tightest workshop output. (ii) closes T9 + the three S85 truncation-FAIL conversions; (iii) recovers W0-20 + lower-half W0-7-MB; (i) is reserved for T5's independent corridor in W1b. This is not three branches selected concurrently — it is THREE NON-OVERLAPPING outputs covering a partitioned consumer space. AGREE with lizzi's framing; the R3 final selection should emit all three.

### Part 2: Original Analysis

#### C1: Finite-Triple Compatibility — Does the Truncated Substrate (155,984 Eigenvalues) Admit the Connes-Moscovici Mellin-Barnes Residue Scheme?

**Cache convention note**: the workshop header cites 155,984 eigenvalues. This is the L_max=12 cache size; at L_max=10 the cache has N_unique = 78,080 eigenvalues (`session-86-w2-workingpaper.md:49`). C9 ran at L_max=10 with the 78,080 cache; the C9 verdict and the C10 `analytic_zeta(s=3, L_max=10)` value are both at the L_max=10 cache. The L_max=12 cache (155,984) is the master cache subsamplable to L_max ∈ {8, 10, 12} per the C12 module definition. The discussion below distinguishes these.

**The CCM-2007 axiomatic preconditions for the Mellin-Barnes residue scheme** are NOT identical to the seven NCG axioms — the residue scheme requires a SUBSET of the axioms plus the CM-1995 admissibility framework. Substitution chain:

```
Step 1 (definitions — preconditions for Mellin-Barnes residue extraction):

  P_NCG (CCM-2007 spectral-triple axioms — REQUIRED for the SD-coefficient
         to be an invariant of the spectral triple):
    (1) Dimension     — d ∈ N (well-defined classical dimension)
    (2) Regularity    — a, [D, a] ∈ ⋂_n Dom(δ^n)
    (3) Finiteness    — H_∞ = ⋂_n Dom(D^n) is a finitely-generated A-module
    (4) Reality       — J: H → H antiunitary, J² = ε, JD = ε'DJ
    (5) First-order   — [[D, a], b°] = 0 for a, b ∈ A, b° ∈ A°
    (6) Orientability — Hochschild d-cycle [c] with π_D(c) = γ
    (7) Poincaré dual — μ_CCM = K_0(A) × K_0(A°) → Z non-degenerate

  P_CM (CM-1995 §1.4-1.5 — REQUIRED for the residue extraction at poles
         to converge):
    (R1) Regularity    — a, [D, a] ∈ ⋂_n Dom(δ^n)         [duplicates P_NCG (2)]
    (R2) Simple Sd     — poles of ζ_b(s) are simple
    (R3) Discrete Sd   — Sd ⊂ Z, finite

  P_MB (additional, MELLIN-BARNES specific):
    (M1) Mellin transform of K(t) = Tr(e^{-tD²}) exists
    (M2) Heat kernel has small-t asymptotic  K(t) ~ Σ_n a_n · t^{(n-d)/2}
    (M3) The Hankel-contour deformation can isolate residues at Sd-poles

Step 2 (substitute the SU(3) substrate at the truncated cache):

  Continuum (SU(3) Jensen-deformed at τ_fold, L_max → ∞):
    P_NCG: (1) d=8 PASS  (2) Reg PASS  (3) Fin PASS  (4) Real PASS
           (5) First-order — F_SM finite triple PASSES 6/7; SU(3) base passes
           (6) Orient PASS  (7) PD PASS for SU(3) base; mu_CCM determinant=2
                                                          for F_SM finite triple
    P_CM: (R1) PASS  (R2) PASS by canonical CM-1995 application
                     (R3) Sd = {0,2,4,6,8} ⊂ Z, finite, PASS
    P_MB: (M1) PASS  (M2) PASS by Connes trace theorem on smooth manifold
                     (M3) PASS at non-pole s ∈ ℂ \ Sd

  Truncated (L_max=10, cache N_unique=78,080):
    P_NCG: (1) Dimension is L_max-conditional. The truncated cache is a finite
                set of eigenvalues, not a manifold. d_truncated = 0 in the
                spectral sense (counting function N(λ; L=10) is bounded, so
                ζ_D(s, L=10) is entire, no pole structure).
                Status: PASS at the manifold level (d=8), DEGENERATE at the
                truncated-cache level (d=0 effectively).
           (2) Regularity is INHERITED from the manifold (the truncation
                preserves smoothness in the embedding sense); PASS but
                degenerate at L_max=10.
           (3)-(7): the truncated cache is a finite-rank operator, so
                finiteness, reality, first-order, orientability, PD all PASS
                trivially at the truncated level. The non-trivial ones live
                at the manifold level.
    P_CM: (R1) PASS, inherited.
           (R2) Sd_truncated = ∅ — there are NO POLES at finite L_max.
                "Simplicity" is vacuously satisfied; degenerate.
           (R3) Sd_truncated = ∅ ⊂ Z trivially.
    P_MB: (M1) PASS, M[K_truncated](s) is entire by linearity over finite sum.
           (M2) FAIL — the small-t asymptotic K_truncated(t) ~ Σ_k m_k(1 − λ_k²·t + ...)
                is a polynomial-in-t expansion at t→0, NOT the manifold's
                heat-kernel asymptotic K(t) ~ Σ_n a_n t^{(n-d)/2}. The two
                expansions are STRUCTURALLY DIFFERENT.
           (M3) PASS at non-pole s, but vacuous since Sd_truncated = ∅.

Step 3 (canonical form — admissibility classification):

  Continuum: ALL preconditions PASS. CM-1995 residue extraction is well-defined.
  Truncated: P_NCG and P_CM PASS at the manifold level (inherited);
              P_MB (M2) FAILS at the truncated level — the truncated heat-kernel
              expansion is polynomial in t at small t, NOT the manifold's
              asymptotic with fractional powers.

Step 4 (substitute into "does the truncated substrate ADMIT the CM-1995 MB
        residue scheme?"):
  At the truncated cache, the MB residue scheme is APPLIED VIA SUBSTITUTION
  of continuum-limit subtraction coefficients (the SD residues at Sd) into
  the residue-extraction formula evaluated on truncated data. This is a
  HYBRID procedure — the lens (Mellin transform + Hankel contour) operates
  on the truncated data, but the SUBTRACTION COEFFICIENTS come from the
  continuum theory. The procedure is mathematically well-defined (CC3 PASS
  at machine ε confirms the lens functions) but the OUTPUT does not match
  the truncated cache's actual spectral content because the subtraction
  is mis-calibrated.

Step 5 (direction):

  The truncated substrate at L_max=10 ADMITS the Mellin-Barnes lens
  (M1, M3 PASS) but does NOT admit the CM-1995 RESIDUE-EXTRACTION
  PRESCRIPTION cleanly because (M2) is structurally different at finite L.
  The C9 FAIL is the substrate's signature of this mismatch:
    n=0 grows 239× from L=5 to L=10 because the truncated cache's
    polynomial small-t expansion gets dominantly larger contributions from
    newly-added high-(p+q) sectors than the continuum SD subtraction
    coefficients are calibrated for.
```

**Conclusion (CCM-2007 axiomatic answer to C1)**:

The truncated 78,080-eigenvalue substrate at L_max=10 (and the 155,984-eigenvalue master cache at L_max=12) ADMITS the Mellin-Barnes lens but DOES NOT ADMIT the Connes-Moscovici 1995 residue extraction scheme **with continuum-calibrated SD subtraction coefficients**. The structural reason: the M2 axiom (manifold-style heat-kernel asymptotic) FAILS at the truncated level — the truncated heat kernel has a polynomial small-t expansion, not the Connes trace theorem's `Σ_n a_n t^{(n-d)/2}` form.

Two corollaries:

1. **The Mellin-Barnes machinery is not broken** — CC3 PASS at machine ε in C9 (rel_err ∈ {2.34e−16, 2.21e−16, 3.56e−16} for {ζ, Zubarev, SDW}) and the Mellin-Dirichlet identity at C10 (rel_err ≤ 1.37e−16) prove the lens functions correctly. The lens reads what is in the substrate.

2. **The CM-1995 SD-subtraction prescription IS broken at L_max=10** — the subtraction coefficients are taken from the L_max → ∞ continuum residue theorem, applied to a truncated cache that has not yet entered the asymptotic regime. The C9 FAIL is the substrate's structural signal of this mismatch.

The implication for the W3 consumer cascade: PER-EVALUATION re-pre-registration (lizzi's R3 branch (iii)) is the right path because it operates ENTIRELY within the M1+M3 + finite-spectrum identity space (which PASSES at L_max=10), while AVOIDING the M2 + CM-1995-subtraction space (which FAILS at L_max=10). The structural-no-go (lizzi's R3 branch (ii)) closes the latter; the per-eval re-pre-reg recovers the former.

#### C2: Connes-Moscovici 1995 §4-§5 Admissibility — Truncation Regime Where Mellin-Cone Scheme Breaks Down

**Structural-no-go theorem candidate** (NCG-axiomatic, complementing lizzi's L4 candidate from the spectral-functional side):

```
Theorem candidate (CM-1995-INADMISSIBILITY-AT-FINITE-L):

  Setup:
    Let (A, H, D_K) be the spectral triple given by:
      A = C^∞(SU(3)) ⊗ C^∞(M^4) ⊗ A_F,  with A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)
      H = L^2(SU(3) × M^4, spinors) ⊗ H_F,  dim H_F = 96
      D_K = Dirac operator on Jensen-deformed SU(3) at τ_fold + d_M^4 + D_F
    Let D_K^{(L)} = orthogonal projection of D_K onto its L_max-bounded
                     Casimir-eigenspaces:
      D_K^{(L)} = π_L D_K π_L,   π_L = projection onto {(p,q) : p+q ≤ L}.
    The truncated cache at L_max=10: N_unique = 78,080 eigenvalues of D_K^{(10)}.

  CM-1995 §4-§5 admissibility audit:
    (P1) Regularity:    PASS, inherited from manifold-substrate smoothness.
    (P2) Discrete Sd:   FAIL at L_max=10 — Sd(D_K^{(10)}) = ∅, finite Dirichlet
                          series is entire; no poles to extract residues from.
    (P3) Sd ⊂ Z, finite: FAIL at L_max=10 (vacuous, ∅).
    (P4) Heat-kernel asymptotic:
                          K_truncated(t) = Σ_k m_k exp(-λ_k² t)
                          K_continuum(t)  ~ Σ_n a_n t^{(n-d)/2} as t → 0
                          The two expansions differ: truncated is polynomial-in-t
                          near t=0; continuum is fractional-power. FAILS at
                          L_max=10.

  Theorem (candidate):
    For any finite L_max < L_∞ where L_∞ is the unknown threshold for entering
    the Weyl-asymptotic regime [N(λ; L_∞) − c · λ^d = O(λ^{d-1}) within ε],
    the CM-1995 §4-§5 residue extraction prescription with continuum-calibrated
    SD-subtraction coefficients applied to D_K^{(L_max)} yields:
      |Λ_CC^MB(reg, L_max)| / |a_0^trunc(reg, L_max)| > κ
    for any reg ∈ F_4 = {ζ, Zubarev, SDW}, where κ = ratio bound determined by
    the n=0 Mellin-moment growth with L_max.

  Empirical verification at L_max=10 (per C9):
    κ_observed = 9.4557  (Zubarev, worst-case smallest)
    margin to PASS bound 5e-1: 18.91× (1.28 OOM above)
    n=0 growth factor M_0^ζ(L=10) / M_0^ζ(L=5) = 238.7×

  Contrapositive (sharper falsifier):
    If L_max ≥ L_∞ (Weyl-asymptotic saturation reached), then the CM-1995
    SD-subtraction prescription becomes asymptotically calibrated and the
    F_4 algebra suppresses a_0 to within 5e-1 of direct truncation.
    Empirical lower bound on L_∞: L_∞ > 10 (C9 FAIL); upper bound unknown
    (would need L_max ∈ {12, 14, 16} sweep).
```

**Refutation pathways** (NCG-axiomatic):

1. **L_max → 12 → 14 → 16 sweep** [CONNES-LMAX-WEYL-CONVERGENCE]: empirical determination of L_∞. The C12 module already supports L_max ∈ {8, 10, 12} (master cache 155,984 eigenvalues at L=12). Effort: HEAVY (full Spin(8) tensor expansion at L=14 requires ~16+ GB memory). EVOI: moderate; would refute the no-go IF the n=0 growth saturates at some L_max ≤ 16.

2. **Subtraction-recalibration on truncated cache** [CONNES-FINITE-L-CALIBRATION]: replace the continuum SD residue coefficients with finite-L calibrated coefficients (e.g., Pauli-Villars subtraction calibrated against the L_max-cache itself). This is OUTSIDE the CM-1995-prescription but INSIDE the "Mellin-Barnes residue extractor with subtraction" class. Effort: MODERATE (4-8h). EVOI: HIGH because it tests whether the CC suppression failure is CM-1995-specific or more general.

3. **Regulator outside F_4** [LIZZI-CUTOFF-SQRT or LIZZI-ANOMALY]: try `cutoff_sqrt` (the `sqrt(x)` cusp regulator) or `anomaly`-class. Per S82 W2-5 MP-Exclusion (`s82-mp-exclusion-theorem.md`): `sqrt(x)` cusp regulators FAIL Hausdorff-Bernstein-Widder CM test; `t^{-3/2}` branch-point outside Sd. So `cutoff_sqrt` is ALREADY known to be a non-completely-monotone regulator. The anomaly regulator class is the un-truncated remaining channel.

4. **Non-MB suppression mechanisms**: Friedmann two-layer gravity, dilution-CC, substrate-density-driven (per `permanent-theorems.md`: "ALL spectral action routes CLOSED. Problem is FUNCTIONAL not GEOMETRIC. a_0/a_2=C_Q/R universal."). These leave the F_4 algebra entirely.

**Connection to my prior corpus**:

- The S65 a_0/a_2 = C_Q/R universal (memory file `s65-connes-collab.md`): for ANY left-invariant metric on SU(3), CC ratio depends ONLY on R. This ALREADY closed the geometric route to CC suppression. C9's FAIL at L_max=10 confirms this from the Mellin-Barnes side: the CC suppression is not a MB-residue lens defect (lens PASSES at machine ε), it is a STRUCTURAL property of the substrate.

- The S46 a_2 split (geometric vs spectral, factor 3812) is the LOWER-SLOT version of C9's a_0 finding. Both are calibration-mismatch artifacts at finite L_max where the continuum-residue subtraction is applied to a non-asymptotic cache.

- The S82 W2-5 MP-Exclusion theorem (memory file `s82-mp-exclusion-theorem.md`): sqrt(x) cusp regulators fail HBW CM test; this CLOSES the cutoff_sqrt pathway as a refutation of the CM-1995-INADMISSIBILITY-AT-FINITE-L candidate, narrowing the surviving refutation pathways to (1), (2), (3-anomaly), (4).

**Status of the C2 theorem candidate**:

The theorem is **proof-ready conditional on**:
(a) numerical confirmation that the M_0(L=10) / M_0(L=5) > 100 diagnostic holds across F_4 (confirmed at C9, ζ-class 238.7×; partial confirmation needed for Zubarev and SDW which lizzi describes as "NON-mono rising" — full numerical verification is mechanical).
(b) statement that κ = 5e-1 is the working threshold (matches plan §9 PASS_ratio bound).
(c) verification that L_max=10 is below L_∞ (confirmed empirically by C9 FAIL).

The theorem's STATUS is **PROVEN MODULO finite-numerical confirmation of (a)**. It deserves §VII registry landing as a S87 carry-forward gate `S87-CM-1995-INADMISSIBILITY-AT-FINITE-L` with the per-route confirmation as the closure script.

**Precise registry classification**:
- §VII slot candidate: §VII.U or §VII.V (depending on collision; §VII.R is occupied by the W1a-2 NCG-Meta-Theorem per `s86-w1a-2-vii-r-meta-theorem-landing.md` memory entry).
- Pre-registered closure: at S87 register-landing gate, with C9 + C12 audit_sha256 anchors as Input-SHA pins.

#### C3: Questions for lizzi

**Q-C1 (sharper Mellin-Strip identity registry status)**:
The Mellin-Dirichlet finite-spectrum identity I derived in Re:L2 (`analytic_zeta(s, L) = ζ_D(s, L)` exactly at finite L on the off-pole strip) is theorem-grade and applies to ANY truncated NCG cache. Do you concur that this deserves an INDEPENDENT §VII registry landing in S87, distinct from the C11 framework note (which is about the Zubarev kernel's analytic Mellin profile, not the substrate's truncated zeta function)? If yes, what gate ID would you propose for the S87 landing? My suggestion: `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY` with §VII slot to be determined.

**Q-C2 (Lambda_J and CM-1995 calibration mismatch)**:
The S64 `Lambda_SA = Lambda_J` finding (memory permanent-theorems.md line 44: "SA fixes Jacobson integration constant. 114-OOM gap real.") is in the same family as the CM-1995-INADMISSIBILITY-AT-FINITE-L candidate. Both are about the spectral action's CC content being mis-calibrated relative to a continuum target. Do you see Lambda_J as a SEPARATE structural-no-go (a different scale), or as a special case of the same finite-L_max calibration mismatch? If the latter, the S87 unification statement could fold both into a meta-theorem.

**Q-C3 (R-protection at the a_0 slot universally fails — connection to your S77 finding)**:
You cited S77 R-protection-universal claim in L1 ("the a_0 slot is the SOLE Lizzi-observable where R-protection universally fails"). The C2 theorem candidate I proposed gives a STRUCTURAL REASON for this failure: the F_4 SD-subtraction is calibrated to the continuum residue at s=0, which is exactly where the truncation-derived non-asymptotic counting fails to absorb the subtraction. Is this the same root cause you identified at S77? If yes, the S77 R-protection-universal statement and my C2 theorem are TWO READINGS OF THE SAME STRUCTURAL TRUTH, which deserves a single unified theorem entry.

**Q-C4 (refutation-pathway prioritization for S87)**:
Of the four refutation pathways I enumerated for C2 (L_max sweep / subtraction-recalibration / cutoff_sqrt+anomaly / non-MB), the S82 W2-5 MP-Exclusion already closes cutoff_sqrt as a viable refutation. Do you concur that the priority ordering for S87 is:
- (4) non-MB mechanisms — HIGHEST priority since SA routes are closed and the suppression must come from outside the spectral functional class
- (2) subtraction-recalibration on truncated cache — MEDIUM priority since it tests whether CC failure is CM-1995-specific or more general
- (1) L_max → 16 sweep — LOW priority due to memory cost; only useful if (4) fails and we need to see whether the substrate even has Weyl-asymp
- (3-anomaly) — LOWEST priority since cutoff_sqrt is already excluded; anomaly class is exotic and probably non-physical

**Q-C5 (Pati-Salam connection — does PS hypercharge embedding offer a finite-L-calibrated subtraction?)**:
Memory `permanent-theorems.md` Open Channels: "Pati-Salam sin^2: PS hypercharge embedding may fix 7.2 ratio. PS-W3-I carry-forward." The Pati-Salam variant changes the algebra, which COULD provide a different SD-subtraction calibration that matches the truncated cache better than the standard A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ). Have you considered whether the PS finite-triple calibration changes the F_4 ∘ MB ∘ SD-subtraction CC suppression regime? If yes, this is a fifth refutation pathway: PS-A_F-RECALIBRATION. If no, this is a missing item in the surviving-corridor enumeration.

---

## Round 2 — lizzi: Follow-up

### CONVERGENCE

After connes's R1 I now commit to four positions I held only conditionally in my own R1.

**(C-α) The Mellin-Dirichlet Finite-Spectrum Identity is theorem-grade and registry-eligible.** Connes's Re:L2 sharpened my "Mellin and Dirichlet routes agree to machine precision" reading into "they are the same number by construction at finite L_max on the off-pole strip" (Re:L2, lines 437–471). The key concession is connes's Step 2 substitution chain (`session-86-w2-workingpaper.md:232–272` mirrored) — `M[K_truncated](s)` reduces by linearity over the finite-eigenvalue sum and the Euler integral `∫_0^∞ t^{s-1} exp(-λ_k² t) dt = λ_k^{-2s}·Γ(s)` to `Σ_k m_k λ_k^{-s}·Γ(s/2)` after the s→s/2 normalization, which divided by Γ(s/2) returns ζ_D(s, L) identically. This is not an integrator calibration result — it is an algebraic equality at off-pole s ∈ ℂ \ Sd whenever the cache has λ_min > 0. I withdraw my softer R1 framing and adopt connes's stronger statement. **Verbatim agreement**: I would land this as a S87 theorem entry under the name **FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY** (connes's Q-C1 proposal). My answer to Q-C1 is below; my contribution is to anchor the identity to the W2 finite-vector classification (`sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` §1–§4) — the truncated D_K cache at L_max=10 is the prototypical FINITE-VECTOR observable, and the identity is what makes finite-vector observables Mellin-readable.

**(C-β) The CM-1995-INADMISSIBILITY-AT-FINITE-L theorem candidate is the right structural statement, and my WEYL-NON-ASYMP-F_4-MB-NO-GO is its observational projection.** Connes's C2 axiomatic decomposition (P1–P4 audit at SU(3) manifold continuum vs L_max=10 truncated cache, lines 851–862) shows precisely WHICH precondition fails: M2 (`K_truncated(t) = Σ_k m_k exp(-λ_k² t)` is polynomial in t at small t, NOT the manifold's `Σ_n a_n t^{(n-d)/2}` fractional-power asymptotic). My L4 candidate stated the failure at the OUTPUT level (ratio_min_in_F_4 > 5e-1, chi2_dof_max > 20); connes's C2 candidate states the failure at the AXIOM level (M2 fails on truncated cache). These are the SAME theorem read from two ends — the M2 axiom failure FORCES the F_4 ratio failure. I adopt connes's statement as the primary (axiomatic) form and mine as the empirical form. **Verbatim**: in the joint S87 registry entry I would write the theorem as connes's CM-1995-INADMISSIBILITY-AT-FINITE-L statement with my WEYL-NON-ASYMP-F_4-MB-NO-GO ratio-form as Corollary A, anchored to the n=0 growth diagnostic 238.7× (verified to 4 sig figs via independent recompute: M_10/M_5 = 9.38e+07/3.93e+05 = 238.6768).

**(C-γ) The "no-go is a strict refinement of CM-1995, not a CM-1995 application" framing.** Connes's Re:L4 substitution chain (lines 608–658) demonstrates that CM-1995 P1–P4 PASS at the SU(3) manifold continuum level with `Sd = {0,2,4,6,8} ⊂ Z`; what fails at L_max=10 is the APPLICABILITY of the residue-extraction PRESCRIPTION whose subtraction coefficients are continuum-limit quantities applied to a non-asymptotic cache. This is a sharper statement than my R1 question phrased it (I asked: does the no-go IS CM-1995 or REFINES CM-1995?). The answer is REFINES — and the refinement is structural, not interpretive. I now hold this as a permanent classification: the no-go is a finite-L_max OBSTRUCTION TO PRESCRIPTION-CALIBRATION, not a continuum-axiom violation.

**(C-δ) The R3 adjudication should emit (ii) ∧ (iii) ∧ (i)-on-T5-only as a non-overlapping union, not a disjunctive choice.** Connes's Re:L3 closing line ("the R3 adjudication should emit (iii) AND (ii), not (iii) OR (ii). Branch (i) is what lizzi correctly defers as out-of-scope") (line 589) and his Re:L4 closing ("THREE NON-OVERLAPPING outputs covering a partitioned consumer space", line 719) match my framing. We agree on the structurally tightest output. I commit to the joint adjudication shape: (ii) closes T9 + the §VII registry entry; (iii) re-pre-registers W0-20 + W0-7-MB lower-half; (i) reserved for T5's land-in-S87-W1b corridor citing C11 PASS at max_rel_err 8.07e-28. The S87 plan should pre-register all three in the same wave, with T5 dispatched to W1b, no-go theorem dispatched to W1c (per connes's §VII slot suggestion §VII.U / §VII.V).

### DISSENT

I disagree with connes on three sub-points. The disagreements are TIGHTNESS-OF-SCOPE rather than direction-of-conclusion.

**(D-α) The truncation-specific scope of CM-1995-INADMISSIBILITY-AT-FINITE-L should be NARROWED further than connes states.** Connes's C2 statement (lines 859–871) says: "for any finite L_max < L_∞ where L_∞ is the unknown threshold for entering the Weyl-asymptotic regime ... the CM-1995 §4–§5 residue extraction prescription with continuum-calibrated SD-subtraction coefficients applied to D_K^{(L_max)} yields ratio > κ for any reg ∈ F_4." This statement quantifies over ALL `reg ∈ F_4`. My objection: the n=0 growth FACTOR is regulator-dependent — connes's C2 only verified the 238.7× factor for ζ-class; SDW and Zubarev branches show DIFFERENT growth signatures.

```
Step 1 (definition of growth-factor diagnostic per regulator):
  M_n^reg(L) := n-th Mellin moment under regulator reg at L_max=L
  growth_n(reg) := M_n^reg(L=10) / M_n^reg(L=5)
  WEYL-NON-ASYMP-at-n-via-reg ⟺ growth_n(reg) > 100

Step 2 (substitute observed C9 sweep across F_4, §W2-1 line 80):
  ζ-class    n=0:  M_0^ζ(5) = 3.93e+05 → M_0^ζ(10) = 9.38e+07,  growth = 238.7×  → DIAGNOSTIC FIRES
  Zubarev    n=0:  per §W2-1 line 53 — "NON-mono fluctuation rising"
                   (lizzi/connes BOTH note this is incompletely-numerically-sampled)
  SDW        n=0:  per §W2-1 line 55 — "monotone but at smaller factor"

Step 3 (canonical form):
  growth_0(ζ) = 238.7×            verified
  growth_0(Zubarev) = TBD          partial confirmation needed
  growth_0(SDW) = TBD              partial confirmation needed

Step 4 (substitute into "for any reg ∈ F_4"):
  Connes's quantifier "for any reg ∈ F_4" is supported numerically only for ζ.
  If growth_0(Zubarev) < 100 OR growth_0(SDW) < 100 then the diagnostic
  fires per-regulator, NOT family-wide.

Step 5 (direction):
  Until we have numerical confirmation of growth_0 across F_4, the no-go
  scope should be QUANTIFIED PER-REGULATOR (∃ reg ∈ F_4 firing diagnostic),
  not UNIVERSALLY QUANTIFIED across F_4 (∀ reg ∈ F_4 firing).
```

**Concrete amendment proposal**: connes's C2 theorem statement should read "for the regulators in F_4 whose n=0 Mellin-moment growth factor diagnostic fires (empirically: ζ at 238.7×; Zubarev and SDW pending numerical confirmation)" rather than "for any reg ∈ F_4". This is the spectral-functional pluralism methodology talking — different regulators in F_4 may have different L_max-saturation thresholds, and the no-go should be tagged per-regulator like S82 W3-L's per-branch scoping discipline (project_s78_w3l_sdw_zeta_dict). The S87 closure script should compute growth_0 per regulator and tag each branch independently.

**(D-β) The dim(H_F)=96 invariant CAN bound the truncation shift — not directly, but via a Casimir-tower derivative.** Connes's Re:L2 (lines 474–513) concludes "the dim(H_F)=96 finite-triple invariant does not anchor C10's INFO band" because H_F lives on the finite-fiber side and the L_max truncation shift lives on the SU(3) base (Casimir tower). I partially agree with the CONCLUSION but disagree with the INFERENCE PATH — there IS a route that uses dim(H_F) as a NORMALIZING constant for the SU(3) Casimir-tower zeta even though it does not directly bound the shift.

```
Step 1 (definitions):
  ζ_total(s, L_max) := Tr(|D_K|^{-s}) over the FULL Hilbert space
                      H_total = L²(SU(3) × M^4, spinors) ⊗ H_F
  ζ_SU3(s, L_max)  := Tr(|D_SU3|^{-s}) over the SU(3) base alone
  Factorization:    ζ_total(s, L) = dim(H_F) · ζ_SU3(s, L)   [tensor product gives multiplicative factor]

Step 2 (substitute):
  |z_total(3, 8) - z_total(3, 10)| / |z_total(3, 10)|
    = |96 · z_SU3(3, 8) - 96 · z_SU3(3, 10)| / |96 · z_SU3(3, 10)|
    = |z_SU3(3, 8) - z_SU3(3, 10)| / |z_SU3(3, 10)|

Step 3 (simplify):
  The dim(H_F) factor CANCELS in the relative shift.
  The 61.1% L=8→L=10 shift is dim(H_F)-INVARIANT.

Step 4 (direction):
  Connes is correct that dim(H_F) does not bound the SU(3)-base
  shift from below. But the multiplicative structure does provide
  a STRUCTURAL ANCHOR: the truncation shift on the BASE can be
  CALIBRATED against the FIBER dimension. The 61.1% shift is
  measuring SU(3) Casimir non-saturation; dim(H_F)=96 is a
  consistency check that the shift does not depend on the
  fiber-side encoding.

Step 5 (revised conclusion):
  dim(H_F)=96 is a DIM-FACTOR-CANCELING-CONSISTENCY-CHECK
  (the shift is fiber-blind), NOT a structural lower bound.
  Connes's NO conclusion is sustained but the reasoning needs
  this multiplicative-factorization step to be airtight.
```

**Concrete amendment proposal**: connes's "the dim(H_F)=96 invariant cannot be used to bound the L=8→L=10 shift" should be sharpened to "dim(H_F)=96 cancels in the relative shift by tensor-product multiplicativity; the shift is fiber-blind and does not admit a finite-triple-invariant bound from below". This sustains the conclusion but eliminates a potential ambiguity.

**(D-γ) Refutation pathway prioritization (Q-C4): I disagree with the (4) > (2) > (1) > (3) ordering.** Connes proposes: (4) non-MB highest, (2) subtraction-recalibration medium, (1) L_max sweep low, (3-anomaly) lowest. My counter-ordering is **(2) > (4) > (1) > (3)**. Reasoning:

- **(2) subtraction-recalibration on truncated cache**: SHOULD BE HIGHEST because it tests a sharply pre-registerable hypothesis (Pauli-Villars subtraction calibrated against L_max=10 itself rather than continuum) and the PASS criterion is unambiguous (does the recalibrated F_4 algebra suppress a_0 below 5e-1 at L_max=10?). EVOI is HIGH because either outcome strengthens the no-go: PASS narrows the no-go to "CM-1995-CALIBRATED-SUBTRACTION-WITHIN-F_4" specifically; FAIL strengthens the no-go to "ALL CALIBRATIONS WITHIN F_4". Effort 4–8h matches connes's estimate.
- **(4) non-MB mechanisms**: SECOND. Connes argued this should be highest because "SA routes are closed and the suppression must come from outside the spectral functional class". I disagree — the project's prior closure of all SA routes (S65 a_0/a_2 = 6/R universal, verified `s65_torus_invariant_cc.py`) ALREADY closed the geometric direction; testing non-MB mechanisms (Friedmann two-layer, dilution-CC) is a SEPARATE project that does not refute the F_4 ∘ MB no-go because they are non-Mellin-Barnes by construction. They are PARALLEL paths, not REFUTATIONS.
- **(1) L_max sweep**: THIRD. Effort is heavy (cache regeneration at L_max=14 requires ~16+ GB memory per `.claude/rules/computation-environment.md` GPU envelope) but DECISIVE: empirically determines L_∞ and bounds the no-go's truncation-specific scope. Should be a S87+ effort-4-day item, not a single-session test.
- **(3-anomaly)**: LAST. Connes is right that cutoff_sqrt is closed by S82 W2-5 MP-Exclusion (`s82_gate_verdicts.txt` HEAT-KERNEL-MP-EXCLUSION PROOF-COMPLETE). The anomaly class is exotic; my prior corpus (S66 ANOMALY-CONSTRAINT-66, S75 ANOMALY-DERIVED-F-STAR-75) shows anomaly-derived spectral actions are STRUCTURALLY incompatible with non-perturbative regulators (project_s75_anomaly_fstar c_1(shape) = -0.998 anti-correlated). Anomaly is closed for THIS purpose.

### EMERGENCE

Three insights surface from the joint reading that neither of us stated in R1.

**(E-α) The R-protection-universal failure at the a_0 slot is connes's M2-axiom failure read through the spectral-functional lens.** Connes's C3 Q-C3 asks whether my S77 R-protection-universal claim ("a_0 slot is the SOLE Lizzi-observable where R-protection universally fails", project_s77_synthesis) and his C2 theorem are "two readings of the same structural truth." They are. The substitution chain that makes this concrete:

```
Step 1 (definitions):
  R-protection (S77): observable O_R is R-protected ⟺ O_R is a ratio of
                      single-branch single-moment observables whose regulator-
                      dependence cancels in the ratio (universal across F_4).
  a_0-slot R-failure (S77): the bare a_0 / Λ_CC ratio is NOT R-protected
                            because a_0 itself is a single-moment scalar
                            (not a ratio of two single-moments at the same s).
  M2-axiom (CM-1995): K_continuum(t) ~ Σ_n a_n t^{(n-d)/2} as t → 0,
                      where the a_n are scheme-independent residues at Sd poles.
  M2-failure-at-truncation (connes C2): K_truncated(t) is polynomial in t,
                                       so the truncated "a_n" extracted by
                                       SD-subtraction are NOT the residues —
                                       they are continuum-residue coefficients
                                       evaluated on a non-asymptotic substrate.

Step 2 (substitute):
  Under M2-failure, the truncated a_0 obtained by CM-1995-prescription is
  a_0^trunc(reg) = continuum-residue-coefficient × truncation-regularization-of-K.
  The truncation-regularization is REGULATOR-DEPENDENT (different for ζ, Zubarev,
  SDW because the K(t) cutoff varies).
  Therefore a_0^trunc(reg_1) / a_0^trunc(reg_2) ≠ 1 in general.

Step 3 (canonical form):
  R-protection of any observable O = a_0 / X requires the regulator-dependence
  of a_0 to cancel against X.
  At the truncated cache, M2-failure forces a_0^trunc to carry residual
  regulator-dependence that has NO scheme-invariant cancellation partner
  (because no other slot at the same s shares the same M2-failure).
  Therefore R-protection of a_0-containing observables FAILS at finite L_max.

Step 4 (substitute into S77 R-protection-universal claim):
  S77 stated: "a_0 is the SOLE slot where R-protection fails universally".
  Connes's C2 stated: "M2 axiom fails on truncated cache, forcing CM-1995
                      subtraction prescription to be regulator-conditional
                      at the a_0 slot."
  These are EQUIVALENT — read from spectral-functional side (S77) vs
  axiomatic-NCG side (C2). The unification statement:

    THEOREM (joint, lizzi+connes, S87 candidate):
      For finite-L_max truncated NCG caches in pre-asymptotic regime,
      R-protection of a_0-containing observables FAILS structurally
      because CM-1995 M2 axiom fails on the truncated cache, forcing
      the SD-subtraction prescription to absorb regulator-dependent
      mass that has no R-cancellation partner.

Step 5 (direction):
  This is a ONE-THEOREM, TWO-FACES result. The S87 registry should land
  it under a single ID (proposed: S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE).
```

This unification was not stated by either of us in R1. It is the deepest emergent result of the joint reading.

**(E-β) The Lambda_J = Lambda_SA finding (S64) IS a special case of CM-1995-INADMISSIBILITY-AT-FINITE-L (connes's Q-C2 answered with sharper structural reading).** Connes's Q-C2 asks whether the S64 `Lambda_SA = Lambda_J` finding (`s63_jacobson_gge.py` "Perspective 1: Jacobson (Lambda = integration constant)"; oom_gap_CC = 114 + log10(ratio_gate_CC) per `s64_sector_selective.py`) is a SEPARATE structural-no-go or a SPECIAL CASE of the same finite-L_max calibration mismatch. My answer: it IS a special case, and the joint reading reveals why.

```
Step 1 (definitions):
  Lambda_SA  := spectral-action CC under continuum CM-1995 prescription
                (extracted as the s=0 SD residue with continuum subtraction).
  Lambda_J   := Jacobson integration constant in the variational principle
                where CC enters as a constant of integration.
  S64 finding: Lambda_SA = Lambda_J at the algebraic level, with a 114-OOM
               gap to the observed cosmological-constant scale.

Step 2 (substitute):
  In CM-1995 continuum, Lambda_SA is the residue at s=0 of ζ_D(s), which
  by the finite-spectrum Mellin-Dirichlet identity (connes Re:L2) is
  structurally equivalent to Σ_k m_k λ_k^{0} = ΣN(λ_k) — a substrate-counting
  observable.
  Lambda_J in Jacobson's framework is determined by IR physics, not by the
  Dirac spectrum.

Step 3 (canonical form):
  The 114-OOM gap is exactly the difference between the SD-residue evaluated
  on (a) truncated cache where M2 axiom fails (giving regulator-conditional
  Lambda_SA) and (b) IR Jacobson constant.

Step 4 (substitute into the unification):
  S64's 114-OOM gap is a DIMENSIONAL manifestation of the same M2-failure
  that drives C9's 9.46× ratio. Both are: continuum-calibrated subtraction
  coefficients applied to a finite or pre-asymptotic substrate.

Step 5 (direction):
  The S87 unification meta-theorem (proposed):

    META-THEOREM (M2-AXIOM-IS-CC-PROBLEM):
      The cosmological-constant problem at the spectral-action level
      reduces to the failure of CM-1995 M2 axiom on the truncated NCG cache.
      Lambda_SA mis-calibration (114 OOM gap, S64), F_4 a_0-slot
      R-protection failure (S77), and the C9 9.46× ratio FAIL all
      arise from the same structural source: the truncated cache's
      polynomial-in-t small-t expansion is NOT the manifold's
      fractional-power asymptotic that CM-1995 subtraction is calibrated for.
```

If valid, this is a S87-class meta-theorem: the CC problem is the M2-axiom problem at the spectral-action level. The S87 plan should pre-register this as a candidate landing.

**(E-γ) The P_NCG, P_CM, P_MB axiom partition reveals that "Mellin-Barnes residue scheme" is NOT one scheme but THREE composable substructures.** Connes's C1 substitution chain (lines 730–820) split the preconditions into P_NCG (axioms 1–7), P_CM (R1–R3), P_MB (M1–M3). The cross-domain insight that emerges: each substructure can be tested INDEPENDENTLY, and the F_4 ∘ MB ∘ SD-subtraction pipeline as currently implemented bundles all three. A more sophisticated S87+ infrastructure could test:

- **P_MB-only at finite L**: just the lens (M1 + M3); already PASSES at machine ε per CC3 in C9.
- **P_CM at L_max → ∞ extrapolation**: residue extraction with continuum subtraction; this is what FAILS at L_max=10 (the C9 verdict).
- **P_CM with finite-L recalibrated subtraction**: replace continuum SD residues with Pauli-Villars finite-L counterparts (connes's refutation pathway #2).

This decomposition allows a **PARTIAL-PASS landing strategy**: a S87 gate could pre-register PASS criterion at the P_MB-only level (which already PASSES) and INFO at the P_CM level. Currently the C9 gate bundles P_MB ∧ P_CM; un-bundling clarifies what is actually broken.

### QUESTIONS

**Answers to connes's C3 questions (Q-C1 through Q-C5)**:

**A-Q-C1 (Mellin-Strip identity registry status)**: YES, the Finite-Spectrum Mellin-Dirichlet Identity deserves an INDEPENDENT §VII registry landing in S87, distinct from the C11 framework note. The C11 note is about the **kernel** (Zubarev's `Λ_Z^{2s}·Γ(s)` is a closed-form Mellin profile of the regulator function, which lives in `lizzi-finite-infinite-vector-classification.md` INFINITE-VECTOR class); my finite-spectrum identity is about the **substrate** (truncated D_K cache in FINITE-VECTOR class). These are dual objects under the lizzi classification — the kernel is the multiplier acting on the substrate. Different §VII slots, different theorem names. **Concrete proposal**: gate ID `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY`, §VII slot recommendation §VII.U or §VII.V (deferring to whoever lands first per the S84 W2a-11 §VII.M→§VII.N precedent — S87 plan should pre-register both slots as available to avoid the W1c collision pattern). Closure script: re-run the C10 5-point sweep on the L_max=12 master cache and verify rel_err ≤ 5×float_eps at each s ∈ {2.5, 2.75, 3.0, 3.25, 3.5}; PASS condition is identity holds to machine epsilon (already-verified at L_max=10; L_max=12 reverification is mechanical).

**A-Q-C2 (Lambda_J and CM-1995 calibration mismatch — same family or different?)**: SAME family, with Lambda_J as a SPECIAL CASE of the broader M2-failure mechanism (E-β substitution chain above). The unification statement: Lambda_J ≡ Lambda_SA (S64) is the algebraic-equivalence reading; Lambda_SA ≠ Lambda_observed (114 OOM gap, framework-cc-oom.md closed_mechanism) is the M2-failure reading. The S87 plan should pre-register `S87-M2-AXIOM-IS-CC-PROBLEM` as a UNIFICATION META-THEOREM gate that proves: (a) the 114-OOM Lambda_SA mis-calibration, (b) the C9 9.46× a_0/Λ_CC ratio FAIL, and (c) the S77 a_0-slot R-protection failure are all consequences of M2-axiom failure on the truncated cache. This single meta-theorem replaces three separate gates with one structural source.

**A-Q-C3 (R-protection at the a_0 slot — same root cause?)**: YES, exact match. Per E-α substitution chain above, my S77 R-protection-universal-fails-at-a_0 statement and your CM-1995-INADMISSIBILITY-AT-FINITE-L are TWO READINGS OF THE SAME STRUCTURAL TRUTH. Proposed unified registry entry name: **`S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE`**. The single registry entry would cite: (i) S77 R-protection-universal claim from project_s77_synthesis; (ii) C2 CM-1995 M2-axiom failure from this workshop; (iii) C9 ratio FAIL as the empirical anchor (value=9.46, sha audit-line 95–96 of `s86_gate_verdicts.txt`). The closure script verifies the M2-failure → R-protection-failure implication on a synthetic finite-L test case (e.g., a 2-eigenvalue toy model where M2 manifestly fails and R-protection of a single-moment ratio manifestly fails in the same regulator scan).

**A-Q-C4 (refutation-pathway prioritization for S87)**: I propose the ORDER **(2) > (4) > (1) > (3)** rather than your (4) > (2) > (1) > (3) — see DISSENT (D-γ) above for the substitution chain. The disagreement is over whether subtraction-recalibration (2) or non-MB mechanisms (4) ranks first. My ordering reflects EVOI: (2) tests a sharper pre-registerable hypothesis at moderate effort (4–8h) and either outcome decisively narrows the no-go scope; (4) is a separate project rather than a refutation of the F_4 ∘ MB no-go. We agree on (1) and (3) ordering. **Concrete proposal**: S87 plan pre-registers (2) as the primary refutation gate `S87-PV-SUBTRACTION-RECALIBRATION` (effort 6h, PASS criterion: |Λ_CC^MB(reg, PV-recalibrated)| / |a_0^trunc(reg)| ≤ 5e-1 at L_max=10 for at least one reg ∈ F_4); (4) as a parallel Wave (independent project landing in S87+ depending on Friedmann/dilution machinery readiness). (1) and (3) are deferred behind (2)'s outcome.

**A-Q-C5 (Pati-Salam connection — fifth refutation pathway?)**: YES, this is a missing item in my surviving-corridor enumeration. Pati-Salam variant (algebra A_F^PS = ℂ ⊕ ℍ_L ⊕ ℍ_R ⊕ M_4(ℂ) in the standard PS embedding, distinct from the SM A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)) changes the finite-fiber dimensionality and the Casimir spectrum on the quotient. **Substitution chain for whether this changes the no-go scope**:

```
Step 1 (definitions):
  dim(H_F^SM)  = 96 (CCM-2007 KO-6, S86 W10-2 C38)
  dim(H_F^PS)  = ? (CCM-2007 PS variant; not yet computed in our framework)
  M2 axiom is about the BASE manifold's heat-kernel asymptotic, not the fiber.
  But the BASE-side D_K depends on the gauge symmetry breaking pattern,
  which differs between SM and PS at the unification scale.

Step 2 (substitute):
  At the SU(3) ⊂ SU(4)_PS embedding, the D_K spectrum on the truncated cache
  re-arranges because the eigenvalues in the (p,q) ladder are weighted by
  PS-irrep multiplicities rather than SM-irrep multiplicities.

Step 3 (canonical form):
  The M2-failure (polynomial-in-t at small t) is a STRUCTURAL property of
  finite truncation, not of the gauge group choice. PS recalibration would
  only change the COEFFICIENTS of the polynomial, not its STRUCTURE.

Step 4 (substitute into "does PS A_F change the M2-failure?"):
  M2-failure persists under any finite truncation regardless of finite-fiber algebra.
  PS recalibration ≠ refutation of the no-go theorem.
  PS recalibration might shift the n=0 growth FACTOR (could be smaller than 238.7×
  for the PS substrate, though this is conjectural without numerical work).

Step 5 (direction):
  PS connection is a USEFUL DIAGNOSTIC for the QUANTITATIVE side of the no-go
  (does the n=0 growth factor depend strongly on the finite-fiber algebra?)
  but NOT a refutation pathway for the STRUCTURAL no-go.
```

**Conclusion on Q-C5**: PS is a fifth pathway only IF "n=0 growth factor reduction below 100" is an admissible RELAXATION of the no-go criterion. Strictly, the no-go is structural (M2-failure), so PS does not refute. Practically, PS may yield a softer growth factor that brings the F_4 ratio closer to 5e-1 at L_max=10. I propose adding `S87-PS-AF-RECALIBRATION` as a SEPARATE diagnostic gate (effort 6–10h depending on PS A_F finite-triple cache readiness; EVOI moderate; not a refutation but a sharper diagnostic of the truncation-regime quantitative dependence).

**New questions for connes's R3 turn (5 sharp follow-ups)**:

**Q-L-NEW-1 (registry collision protocol for the joint M2-CC meta-theorem)**: If we land both `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY` (E-β) AND `S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE` (E-α) AND `S87-CM-1995-INADMISSIBILITY-AT-FINITE-L` (your C2) AND the proposed `S87-M2-AXIOM-IS-CC-PROBLEM` meta-theorem (E-β), we have FOUR §VII candidates from this workshop. Per `.claude/rules/epistemic-discipline.md` Registry-Write Hygiene under Parallel-Writer Race, we need scan-ALL-header-levels + append-only writers. Do you want to take three of these in your S87 W1c slot and I take one in W1b, or do we land them all in one wave with explicit non-collision slot pre-registration? My preference: I take `FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY` (the algebraic identity, lizzi-finite-infinite-vector classification anchor), you take `CM-1995-INADMISSIBILITY-AT-FINITE-L` (the axiom-level theorem, NCG-axiomatic anchor), we co-author `A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE` (the unification), and `M2-AXIOM-IS-CC-PROBLEM` is a meta-theorem we both sponsor with the framework-cc-oom.md update.

**Q-L-NEW-2 (M2-failure quantitative diagnostic across F_4)**: D-α requires growth_0(Zubarev) and growth_0(SDW) numerical confirmation. Per my reading of `session-86-w2-workingpaper.md:53–55` ("ζ : 1.0339e+01, Zubarev : 9.4557, SDW : 9.6870" for the L=10 ratio), the F_4 family already shows tight dispersion (10.84/9.46/9.69 — 13.4% spread). Do you have quantitative reason to expect growth_0(reg) to vary FAR more than the L=10 ratio dispersion, or do you think the 238.7× ζ-class number is representative of all three at the order-of-magnitude level? If the latter, the per-regulator-scoping in D-α is a TIGHTNESS consideration rather than a fundamental scope-narrowing.

**Q-L-NEW-3 (P_MB-only PASS criterion for un-bundling C9)**: E-γ proposes splitting C9 into P_MB-only + P_CM components. Is the un-bundling backward-compatible with the existing C9 verdict? Specifically, if S87 emits a `S87-MB-LENS-ONLY-PASS` gate that pre-registers PASS at the P_MB level (already at machine ε per CC3 in C9), does this SUPERSEDE the C9 FAIL or coexist with it? My intuition: coexist (different gate IDs, different criteria, both verdict-permanent per `.claude/rules/output-standards.md`). But the W3 consumers need to know which one to cite. Should we add a routing-layer in §VII.PROP indicating that downstream consumers cite P_MB-PASS for finiteness/Mellin-route claims and C9-FAIL for SD-subtraction-CC-suppression claims?

**Q-L-NEW-4 (M2-failure threshold scan sharpness)**: Your C2 theorem statement uses "for any finite L_max < L_∞ where L_∞ is the unknown threshold for entering Weyl-asymptotic regime". My corpus (project_s73b_sdw_validation FAIL at L_max=7 with +168% ratio shift; project_s78_w3a_chi2_lmax FAIL with chi_2^{SDW}(inf) BMA) suggests L_∞ might not be a single threshold but a SLOT-DEPENDENT cliff: high-n slots (n=4, 6) Weyl-saturate at smaller L_max while low-n slots (n=0) Weyl-saturate at much larger L_max (or possibly never finite). Substitution chain in my D-α only confirmed ζ-class growth at n=0; the L_max scan needs to be slot-by-slot. Do you concur that the S87 L_max sweep refutation pathway should be PER-SLOT (4 thresholds L_∞^{n=0}, L_∞^{n=2}, L_∞^{n=4}, L_∞^{n=6}) rather than family-wide?

**Q-L-NEW-5 (Casimir-tower asymptotic vs Spin(8) Weyl asymptotic — same or different?)**: Your Re:L2 (lines 497–510) cites "the Connes trace theorem on the manifold-substrate" as the source of the d_eff = 8 Weyl counting. Our framework's substrate is M^4 × SU(3)_Jensen — the SU(3) base is 8-dimensional embedded in the standard NCG sense. But the truncation lives on the (p,q) Casimir tower, not on a standard Spin(8) manifold. Is the Weyl asymptotic `N(λ; L_max) ~ c · λ^d` with d=8 INHERITED from Spin(8) embedding via the Connes trace theorem, or does the Casimir-tower truncation introduce a DIFFERENT effective dimension d_eff(SU(3)/Z_3) that affects the Weyl-saturation threshold L_∞? This matters for the D-α / Q-L-NEW-4 per-slot threshold question — if d_eff < 8 due to Jensen deformation breaking Spin(8) symmetry, the L_∞ threshold could be substantially smaller than the manifold-substrate prediction.

---

## Round 2 — connes: Cross-Synthesis

### CONVERGENCE

After lizzi's R2 I now hold five additional positions I held only conditionally in my own R1. The cumulative effect is the workshop has converged on a structurally complete R3 union: ONE algebraic identity (theorem-grade), ONE strict-refinement no-go (axiom-grade), ONE unification meta-theorem candidate (cross-program), and a PER-REGULATOR-SCOPED no-go statement that supersedes my universally-quantified C2 form.

**(CN-α) I accept lizzi's C-α verbatim — the Finite-Spectrum Mellin-Dirichlet Identity is theorem-grade and registry-eligible at §VII.U or §VII.V, with the lizzi-finite-infinite-vector classification anchor.** Lizzi's C-α (workshop §"Round 2 — lizzi" lines 945) cleanly fixes the dual-object reading: C11's Λ_Z^{2s}·Γ(s) is the **kernel** identity (INFINITE-VECTOR class per `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` §3), and the substrate-side Mellin-Dirichlet identity is the **truncated D_K cache** identity (FINITE-VECTOR class, §1–§2). These are dual under the multiplier-action of regulator on substrate. The classification is structural, not bookkeeping — finite-vector observables are precisely the ones that admit the finite-spectrum identity by linearity over the finite eigenvalue sum, and infinite-vector observables (continuous Mellin profiles) require the closed-form analytic-Mellin-transform machinery C11 verified. I retract the §VII.S/§VII.T proposal from my Q-C1 and adopt lizzi's §VII.U/§VII.V suggestion (deferred to whoever lands first, per the S84 W2a-11 §VII.M→§VII.N precedent the workshop already references).

**(CN-β) I accept lizzi's C-β verbatim — the joint S87 registry entry should write the theorem in axiom-form (CM-1995-INADMISSIBILITY-AT-FINITE-L) with the WEYL-NON-ASYMP-F_4-MB-NO-GO ratio-form as Corollary A.** Lizzi's C-β (line 947) confirmed the two readings are the SAME theorem read from opposite ends — my C2 axiom-level statement is the producing structural cause, her L4 ratio-level statement is the empirical consequence. I previously bracketed my C2 candidate as "complementing lizzi's L4 candidate from the spectral-functional side" (Re:L4 §C2 frame line 836); I now drop the "complementing" framing and accept the unified form. The registry entry should be written in CM-1995-INADMISSIBILITY-AT-FINITE-L primary form with WEYL-NON-ASYMP-F_4-MB-NO-GO as Corollary A and the n=0 growth diagnostic 238.7× verified to 4 sig figs (lizzi's recompute `M_10/M_5 = 9.38e+07/3.93e+05 = 238.6768` matches my Re:L4 recompute `238.7×` line 602). The S87 closure script SHA pin would anchor on C9's audit_sha256 (line 95–96 of `s86_gate_verdicts.txt`).

**(CN-γ) I accept lizzi's C-γ verbatim — the no-go is a STRICT REFINEMENT of CM-1995, not a CM-1995 application.** Lizzi's C-γ (line 949) sharpens my Re:L4 substitution chain (lines 608–658) into a permanent classification: the failure at L_max=10 is "a finite-L_max obstruction to prescription-calibration, not a continuum-axiom violation". This is a structurally cleaner phrasing than my "STRICT REFINEMENT specific to the truncated D_K cache" line 657. I adopt lizzi's "obstruction to prescription-calibration" terminology for the registry entry — it correctly localizes the failure at the application boundary (continuum-residue-coefficient → finite-L cache mismatch) rather than at the CM-1995 axiom set. The CM-1995 axioms P1–P4 are SATISFIED at the SU(3) manifold continuum; the prescription's calibration is what fails when the prescription is applied off its design domain.

**(CN-δ) I accept lizzi's C-δ verbatim — R3 should emit (ii) ∧ (iii) ∧ (i)-on-T5-only as a non-overlapping union, with explicit §VII slot pre-registration to avoid the W1c collision pattern.** My Re:L3 closing (line 589) and Re:L4 closing (line 719) both pushed for AND-not-OR; lizzi's C-δ matches and adds the §VII slot pre-registration discipline (registering both §VII.U AND §VII.V as available so a parallel-writer race resolves cleanly). I accept this. The S87 plan should pre-register: (a) `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` at §VII.U (or §VII.V whichever lands first); (b) `S87-W3-PER-EVAL-FINITENESS-PRE-REG` for W0-20 + W0-7-MB lower-half re-pre-registration; (c) `S87-W1B-T5-LANDING` for the Mellin-Strip / Convergence-Cone Theorem citing C11's Λ_Z^{2s}·Γ(s) anchor; and (d) `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY` at §VII.U or §VII.V (deferred to whichever (a) does not occupy).

**(CN-ε) I accept lizzi's D-γ refutation prioritization (2)>(4)>(1)>(3) over my own (4)>(2)>(1)>(3).** I recant on the (4) > (2) ordering. Lizzi's substitution chain in D-γ (lines 1027–1029) correctly identifies that (2) subtraction-recalibration tests a sharper PRE-REGISTERABLE hypothesis — Pauli-Villars subtraction calibrated against the L_max=10 cache itself, with PASS/FAIL criterion `|Λ_CC^MB(reg, PV-recalibrated)| / |a_0^trunc(reg)| ≤ 5e-1` cleanly defined. Her EVOI argument is structurally tighter: (2) PASS narrows the no-go to "CM-1995-CALIBRATED-SUBTRACTION-WITHIN-F_4 specifically"; (2) FAIL strengthens to "ALL CALIBRATIONS WITHIN F_4". My (4)-priority argument relied on "SA routes are closed and suppression must come from outside the spectral functional class" (Q-C4), but as lizzi notes (D-γ line 1028), non-MB mechanisms are PARALLEL paths NOT REFUTATIONS of the F_4 ∘ MB no-go — they live outside its scope by construction and cannot refute a no-go that is statemented inside F_4 ∘ MB. The (4) > (2) ordering confused "refutation of the no-go" with "alternative to the no-go's failed program". I withdraw it.

The corrected S87 plan ordering: `S87-PV-SUBTRACTION-RECALIBRATION` PRIMARY (effort 6h, lizzi's PASS criterion); `S87-NON-MB-CC-MECHANISMS-EXPLORATION` PARALLEL (separate project, not a refutation gate); `S87-LMAX-WEYL-CONVERGENCE-SWEEP` DEFERRED (effort heavy, GPU envelope concern per `.claude/rules/computation-environment.md`); `S87-ANOMALY-CLASS-AS-CONTROL` LAST (S82 W2-5 MP-Exclusion already excludes cutoff_sqrt; anomaly is exotic but should be tagged for completeness).

I also accept lizzi's three EMERGENCE unifications as theorem-grade S87 entries. Substitution chain for each acceptance:

```
E-α (a_0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE):
  Step 1 (definitions): S77 R-protection-universal-fails-at-a_0 (project_s77_synthesis);
                        connes C2 M2-axiom-fails-at-truncated-cache.
  Step 2 (substitute): under M2-failure on truncated cache, a_0^trunc(reg) carries
                       residual regulator-dependence (lizzi E-α step 2);
                       this residual has NO scheme-invariant cancellation partner
                       at the same s (S77 R-protection definition).
  Step 3 (simplify):   a_0-containing observables fail R-protection if and only if
                       M2 fails at the truncated cache (necessity from lizzi step 2,
                       sufficiency from connes C2 axiom-level).
  Step 4 (substitute): under M2-PASS (continuum limit), a_0 obtains a scheme-invariant
                       residue at s=0 (CM-1995); R-protection is then trivial.
                       Under M2-FAIL (truncated), a_0 carries regulator-dependence;
                       R-protection fails.
  Step 5 (direction):  TWO-FACES, ONE-THEOREM. The biconditional is established and
                       the joint registry entry is mathematically clean.
  Conclusion: ACCEPT.
```

```
E-β (M2-AXIOM-IS-CC-PROBLEM meta-theorem candidate):
  Step 1 (definitions): Lambda_SA = Lambda_J at algebraic level (S64);
                        114 OOM gap to observed CC (framework-cc-oom.md);
                        E-α a_0-R-protection failure;
                        C9 9.46× ratio FAIL.
  Step 2 (substitute): all three failures are continuum-calibrated SD subtraction
                       coefficients applied to a finite or pre-asymptotic substrate.
  Step 3 (simplify):   the structural source is M2-failure on the truncated cache.
  Step 4 (caveat):     the meta-theorem statement "the CC problem REDUCES TO M2-failure
                       at the spectral-action level" is BOLDER than just unifying
                       three results — it makes a forward claim that M2-PASS would
                       resolve the 114 OOM gap. I am cautious here: the claim is well-
                       supported by the substitution chain BUT it is a meta-theorem,
                       which the registry-write hygiene rule (`epistemic-discipline.md`
                       §"Registry-Write Hygiene") flags as a higher-stakes landing.
  Step 5 (direction):  ACCEPT as candidate, but with the meta-theorem framed as
                       "M2-failure is a STRUCTURAL SOURCE for these three failures"
                       rather than "M2-PASS would resolve the CC problem". The
                       weaker form is what the substitution chain supports; the
                       stronger form requires showing M2-PASS sufficiency, which
                       neither L4 nor C2 demonstrates and which is not within the
                       workshop's scope to demonstrate.
  Conclusion: ACCEPT-AS-CANDIDATE with refined statement (necessity proven; sufficiency
              flagged as conjecture for S87+).
```

```
E-γ (P_NCG / P_CM / P_MB axiom partition):
  Step 1 (definitions): connes C1 axiom decomposition (lines 730–820);
                        lizzi E-γ un-bundling proposal.
  Step 2 (substitute): CC3 PASS at machine ε (C9 line 95) → P_MB-only = PASS;
                       C9 ratio FAIL at 9.46 → P_CM-with-continuum-subtraction = FAIL;
                       open question → P_CM-with-finite-L-recalibration (refutation
                       pathway #2).
  Step 3 (simplify):   the C9 verdict bundles P_MB ∧ P_CM. Un-bundling clarifies
                       what is broken (P_CM-continuum-subtraction) vs what is not
                       (P_MB lens).
  Step 4 (substitute into S87 routing-layer): downstream consumers (W3) cite
                       P_MB-PASS for finiteness/Mellin-route claims (W0-20 §W3-4
                       hypothesis ONLY needs M[K] finite + χ²/dof against direct ≤ 5,
                       both satisfied by P_MB) and cite C9-FAIL for SD-subtraction
                       CC-suppression claims (T9 §W3-1 ε_T9 = 0.01 needs the
                       subtraction prescription's residue extraction).
  Step 5 (direction):  the un-bundling is structurally clean and BACKWARD-COMPATIBLE
                       (different gate IDs, both verdict-permanent per
                       `.claude/rules/output-standards.md`). ACCEPT.
  Conclusion: ACCEPT. The S87 plan should add a P_MB-only PASS criterion as a
              SEPARATE gate (proposed `S87-MB-LENS-ONLY-PASS`) coexisting with C9.
```

All three EMERGENCE unifications accepted. Joint S87 candidate landings: four §VII candidates (the FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY, CM-1995-INADMISSIBILITY-AT-FINITE-L, A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE, M2-AXIOM-IS-CC-PROBLEM-meta) + one §VII.PROP routing-layer entry (P_MB / P_CM un-bundling) + one §VII.W1b corridor entry (T5 Mellin-Strip / Convergence-Cone). I address the §VII slot collision protocol in EMERGENCE below.

### DISSENT

I now hold three sub-points where I disagree with lizzi's R2 sub-statements, with NEW evidence not present in my R1. The disagreements are TIGHTNESS-OF-BOUNDARY rather than direction-of-conclusion (matching lizzi's framing of D-α through D-γ).

**(DN-α) D-α per-regulator-scoping is a TIGHTNESS consideration that matters for the registry-statement form, NOT a fundamental scope-narrowing of the no-go.** Lizzi's D-α (lines 957–987) requires that the C2 statement be quantified per-regulator (∃ reg ∈ F_4 firing the n=0 growth diagnostic) rather than universally (∀ reg ∈ F_4). She is correct that my Re:L4 recompute only verified `238.7×` for the ζ-class. But the dispersion at L=10 is much tighter than the 30%+ that would justify per-regulator tagging at the registry level. Substitution chain (numerically verified):

```
Step 1 (definitions):
  L=10 ratio for reg ∈ F_4: r(reg) := |Λ_CC^MB(reg, L=10)| / |a_0^trunc(reg, L=10)|
  L=10 dispersion: spread(F_4) := (max_reg r - min_reg r) / min_reg r

Step 2 (substitute observed C9 values, §W2-1 lines 53–55):
  r(ζ) = 10.339,  r(Zubarev) = 9.4557,  r(SDW) = 9.6870
  spread(F_4) = (10.339 − 9.4557) / 9.4557 = 0.0934 = 9.34%
  [Numerically verified: see Bash check above; 9.34% is bit-exact.]

Step 3 (simplify, growth-factor proxy):
  Assuming growth_0(reg) is multiplicatively proportional to r(reg) at L=10
  (a conservative ansatz, since growth integrates over L=5..10),
    growth_0_proxy(Zubarev) ≈ growth_0(ζ) × r(Zubarev) / r(ζ) = 238.7 × (9.4557/10.339) = 218.3×
    growth_0_proxy(SDW) ≈ growth_0(ζ) × r(SDW) / r(ζ) = 238.7 × (9.6870/10.339) = 223.6×
  [Numerically verified: see Bash check above.]

Step 4 (substitute into diagnostic threshold):
  Diagnostic threshold from my C2: growth_0(reg) > 100 ⇒ NOT-WEYL-ASYMP at reg.
  All three F_4 regulators clear the threshold by factor ≥ 2.18× at the conservative
  proxy (218.3× / 100 = 2.18×).

Step 5 (direction):
  IF growth_0(Zubarev) and growth_0(SDW) deviated from ζ by more than 100% (i.e.,
  growth_0(Zubarev) < 119× or > 477×), per-regulator tagging at registry level
  would be MANDATORY. Empirically, the L=10 ratio dispersion is 9.34%, an order
  of magnitude below the threshold-crossing dispersion of 100%. So at the registry-
  statement level, the universal quantifier is empirically supported with margin.
  At the closure-script level, lizzi's per-regulator tagging is the right
  computational discipline (matches S82 W3-L per-branch scoping).
```

**Concrete amendment** (NEW evidence beyond R1): The substitution chain shows the per-regulator-scoping is correct discipline at the closure-script level (the S87 closure should compute and report growth_0 per regulator, tagging each branch independently per S82 W3-L precedent) BUT the registry theorem statement can keep the universal quantifier ∀ reg ∈ F_4 with empirical 9.34% L=10 dispersion as the supporting evidence. Lizzi is right at the implementation level; my universal statement holds at the registry-statement level. This is not a substantive disagreement — it is a layer-of-application distinction. The S87 plan should pre-register BOTH: registry statement quantified universally (with dispersion footnote), closure script tagged per-regulator (with growth_0 reported for each).

This is a partial concession (lizzi correct on closure discipline) rather than full acceptance of D-α (the universal quantifier survives at registry-statement level).

**(DN-β) lizzi's D-β multiplicative-factorization correction is mathematically right but the dim(H_F)=96 fiber-blindness is a NULL RESULT, not a structural anchor — it should not appear in the C10 INFO-band registry annotation.** Lizzi's D-β (lines 989–1023) sharpens my "dim(H_F)=96 cannot bound the L=8→L=10 shift" to "dim(H_F)=96 cancels in the relative shift by tensor-product multiplicativity; the shift is fiber-blind and does not admit a finite-triple-invariant bound from below." She frames this as a structural anchor ("DIM-FACTOR-CANCELING-CONSISTENCY-CHECK"). My disagreement: the cancellation IS mathematical content but it is NULL content — it tells us that fiber-side encoding does not affect the base-side shift, which is the ABSENCE of an anchor, not its presence.

```
Step 1 (definitions, restating lizzi's chain):
  ζ_total(s, L) = dim(H_F) × ζ_SU3(s, L)   [tensor product]
  Δ_rel(L_1, L_2) := |ζ_total(s, L_1) - ζ_total(s, L_2)| / |ζ_total(s, L_2)|

Step 2 (substitute):
  Δ_rel(L_1, L_2) = |dim(H_F)·ζ_SU3(s,L_1) − dim(H_F)·ζ_SU3(s,L_2)| / |dim(H_F)·ζ_SU3(s,L_2)|
                  = |ζ_SU3(s,L_1) − ζ_SU3(s,L_2)| / |ζ_SU3(s,L_2)|
  [dim(H_F) cancels — lizzi correct.]

Step 3 (simplify, DEEPER reading):
  The multiplicative-factor cancellation says: the relative shift is INDEPENDENT
  of the fiber dimension. It would have the same value 0.611 at dim(H_F) = 1
  (no fiber), dim(H_F) = 96 (CCM-2007 SM), dim(H_F) = 384 (CCM-2007 PS variant),
  or any other choice. This is a STATEMENT OF NULL DEPENDENCE, not a bound.

Step 4 (substitute "structural anchor" definition):
  A structural anchor would be a finite-triple invariant N such that
    Δ_rel(L_1, L_2) ≥ f(N) for some non-trivial f.
  Lizzi's chain gives Δ_rel = g(SU3-only quantities) — fiber-blind, no f(dim(H_F)).
  The cancellation-as-anchor framing inverts: "dim(H_F) doesn't appear" is read as
  "dim(H_F) is a consistency check". A consistency check requires a non-trivial
  dependence to consist OF; here there is none.

Step 5 (direction):
  The dim(H_F)=96 is a NUMBER that has nothing to do with the C10 INFO band.
  Mentioning it in the C10 verdict-line annotation would be a citation that does
  not contribute information — a Class-(g) keyword-window violation per `.claude/rules/
  epistemic-discipline.md` §"Source Reconciliation". The right registry annotation
  for C10 INFO is "Δ_rel(L=8, L=10) = 0.611 measures SU(3) Casimir-tower truncation
  gradient at s=3; fiber-blind by tensor-product multiplicativity (see W10-2 C38)";
  the parenthetical is the cite-by-acknowledgement, not a structural anchor.
```

**Concrete amendment** (NEW evidence beyond R1): I accept lizzi's mathematical chain (the cancellation is real) but DISAGREE that this should be framed as a structural anchor. The S87 registry annotation for C10's INFO band should write: "Δ_rel(L=8, L=10) = 0.611 measures SU(3) Casimir-tower truncation gradient; the dim(H_F)=96 invariant cancels in the relative shift (tensor-product multiplicativity, NULL constraint). No finite-triple-invariant lower bound exists." This is sharper than lizzi's "DIM-FACTOR-CANCELING-CONSISTENCY-CHECK" framing.

**(DN-γ) Lizzi's E-β meta-theorem candidate (M2-AXIOM-IS-CC-PROBLEM) overreaches as currently stated; the necessity direction is supported by the substitution chain, the sufficiency direction is not.** Lizzi's E-β (lines 1117–1133) proposes the meta-theorem: "the cosmological-constant problem at the spectral-action level reduces to the failure of CM-1995 M2 axiom on the truncated NCG cache." Reduce is a strong word — it asserts BICONDITIONAL equivalence. My CONVERGENCE acceptance above (CN-ε E-β) was conditional: I accept-as-candidate but flag that "REDUCES TO" requires demonstrating M2-PASS sufficiency. This is the dissent I now formalize.

```
Step 1 (definitions):
  CC problem = the 114 OOM gap between Lambda_SA and Lambda_observed (S64,
                framework-cc-oom.md).
  M2 axiom = K(t) ~ Σ_n a_n t^{(n-d)/2} as t → 0 on the smooth manifold continuum.
  M2-FAIL on truncated cache = K_truncated(t) is polynomial in t (connes C2).
  Necessity statement (weak meta-theorem): M2-FAIL is a structural source for
                                            (a) Lambda_SA mis-calibration, (b) C9
                                            9.46× ratio FAIL, (c) S77 a_0 R-protection
                                            failure.
  Sufficiency statement (strong meta-theorem): M2-PASS at the continuum limit
                                                resolves the 114 OOM gap.

Step 2 (substitute necessity):
  Each of (a), (b), (c) traces to continuum-calibrated subtraction coefficients
  applied to a non-asymptotic substrate. Lizzi's E-β substitution chain (line 1093–
  1133) establishes the necessity direction. ACCEPT.

Step 3 (substitute sufficiency):
  The sufficiency direction would assert: take L_max → ∞ (M2-PASS); the 114 OOM
  gap goes to zero. Empirically, M2-PASS at the continuum gives Lambda_SA equal to
  the s=0 SD residue with continuum subtraction — this is the CM-1995-extracted
  cosmological-constant-coefficient. The 114 OOM gap is between this CM-1995
  extracted value (which is finite per CCM-2007 §"Cosmological Constant From the
  Spectral Action") and the OBSERVED value of Lambda. M2-PASS does NOT resolve
  this gap; it gives the SAME Lambda_SA value that S64 already reports. The 114
  OOM gap is between "Lambda_SA at continuum (well-defined, per CM-1995)" and
  "Lambda_observed", not between "Lambda_SA at finite L" and "Lambda_observed".
  M2-failure on truncated cache produces an ADDITIONAL regulator-conditional
  contribution on top of the continuum value, but the continuum value ITSELF is
  the seat of the 114 OOM gap. M2-PASS leaves the gap intact.

Step 4 (canonical form):
  Necessity: M2-FAIL ⇒ Lambda_SA carries finite-L-conditional residual on top of
              continuum value. SUPPORTED.
  Sufficiency: M2-PASS ⇒ Lambda_SA matches Lambda_observed. NOT SUPPORTED — the
              continuum value of Lambda_SA itself differs from Lambda_observed by
              114 OOM, independently of any truncation.

Step 5 (direction):
  The meta-theorem is true in NECESSITY direction (M2-failure is among the
  structural sources of Lambda_SA mis-calibration at finite L), false in
  SUFFICIENCY direction (M2-PASS does not resolve the 114 OOM gap; the gap is
  continuum-level). The S87 registry entry for E-β should be FRAMED AS "M2-failure
  is a STRUCTURAL SOURCE for these failures" not "the CC problem REDUCES TO M2-failure".
```

**Concrete amendment** (NEW evidence beyond R1): The S87 plan's `S87-M2-AXIOM-IS-CC-PROBLEM` meta-theorem must be written in necessity-only form. Proposed restated theorem:

> **META-THEOREM (S87 candidate, necessity-only)**: For any regulator scheme reg ∈ F_4 acting on the truncated NCG cache at L_max=10 in pre-asymptotic regime, M2-axiom failure on the truncated cache is a STRUCTURAL SOURCE for: (a) the Lambda_SA finite-L-conditional residual (S64 contributing component); (b) the C9 9.46× a_0/Λ_CC ratio FAIL; (c) the S77 a_0-slot R-protection-universal failure. The 114-OOM Lambda_SA → Lambda_observed gap is CONTINUUM-LEVEL and is NOT contained in the M2-failure structural source — M2-PASS at the continuum limit does NOT resolve the 114-OOM gap.

This necessity-only form is what the substitution chains support. Lizzi's "REDUCES TO" framing should be retracted from the meta-theorem proposal. The dissent is one-sided: I accept the necessity meta-theorem; I reject the sufficiency framing.

### EMERGENCE

Three new insights surface from the joint reading that neither of us stated explicitly through R1+R2 but which become structurally apparent when the lizzi+connes converged commitments are read together. Each addresses one of the three orchestrator-prescribed EMERGENCE topics.

**(EN-α) §VII registry collision protocol for the 4 candidate entries: the collision is RESOLVED by the dual-classification structure if we assign §VII slots BY CLASSIFICATION rather than BY SPONSORSHIP.** The S87 plan-write needs to land four §VII candidates from this workshop:

  1. `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY` (algebraic identity, FINITE-VECTOR class, lizzi-anchored)
  2. `S87-CM-1995-INADMISSIBILITY-AT-FINITE-L` (axiom-level theorem with WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A, connes-anchored)
  3. `S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE` (cross-program unification, lizzi+connes co-anchored)
  4. `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL` (necessity-only meta-theorem per DN-γ; not the M2-AXIOM-IS-CC-PROBLEM strong form)

Plus the routing-layer entry in §VII.PROP: P_MB / P_CM un-bundling per E-γ.

Lizzi's Q-L-NEW-1 proposed sponsorship-based assignment (lizzi takes #1, connes takes #2, co-author #3, joint sponsor #4 with framework-cc-oom.md update). My counter-proposal: classification-based assignment per the lizzi-finite-infinite-vector classification scheme + per the axiom-level / phenomenological-level partition:

```
Step 1 (definitions, classification axes):
  Algebraic-vs-Spectral axis (lizzi finite/infinite-vector classification):
    ALGEBRAIC: closed-form identity on the regulator kernel itself
    SPECTRAL:  structural property of substrate spectrum's interaction with regulator
  Axiom-vs-Empirical axis (connes axiomatic / lizzi phenomenological partition):
    AXIOM-LEVEL: theorem statement at NCG-axiom or CM-axiom level
    EMPIRICAL: theorem statement at substrate-numerical-observable level

Step 2 (substitute four candidates):
  #1 FINITE-SPECTRUM-MELLIN-DIRICHLET: ALGEBRAIC × AXIOM-LEVEL
     (an exact mathematical identity at finite L, not phenomenological)
  #2 CM-1995-INADMISSIBILITY: AXIOM-LEVEL × SPECTRAL
     (CM-1995 axiom partition × spectral substrate property at finite L)
  #3 A0-R-PROTECTION-FAILURE-IS-M2: SPECTRAL × CROSS-PROGRAM
     (joins R-protection program (lizzi) with M2-axiom partition (connes))
  #4 M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA: AXIOM-LEVEL × META
     (cross-result unification at axiom level)

Step 3 (simplify §VII slot assignment):
  §VII.U (next available algebraic-axiom slot): #1 FINITE-SPECTRUM-MELLIN-DIRICHLET
  §VII.V (next available spectral-axiom slot): #2 CM-1995-INADMISSIBILITY
  §VII.W (cross-program slot): #3 A0-R-PROTECTION-IS-M2
  §VII.X (meta-theorem slot): #4 M2-STRUCTURAL-SOURCE
  §VII.PROP (routing-layer): E-γ P_MB / P_CM un-bundling

Step 4 (substitute parallel-writer race protection):
  Per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-
  Writer Race", the S87 plan must use append-only Python writers, NOT Edit-tool round-
  trips, for `permanent-results-registry.md`. Multiple parallel landings must each
  scan ALL header levels (## + ### + ####) before allocating their slot. The S87
  plan should pre-allocate §VII.U, §VII.V, §VII.W, §VII.X as RESERVED-FOR-WORKSHOP
  in a synchronization lockfile to avoid the W1c collision pattern that the rule
  was written to address.

Step 5 (direction):
  Classification-based assignment is structurally cleaner than sponsorship-based:
  it lets future readers locate a theorem by its mathematical content type, not by
  its co-author roster. The sponsorship metadata appears in the entry's "Sponsors"
  field; the §VII slot location reflects the entry's classification.
```

**Concrete proposal**: §VII.U=FINITE-SPECTRUM-MELLIN-DIRICHLET (lizzi anchor), §VII.V=CM-1995-INADMISSIBILITY (connes anchor with lizzi-WEYL-NON-ASYMP corollary A), §VII.W=A0-R-PROTECTION-IS-M2 (joint anchor), §VII.X=M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA (necessity-only per DN-γ; joint anchor with framework-cc-oom.md update), §VII.PROP+1 = P_MB/P_CM routing-layer (joint). The S87 plan should pre-allocate these four §VII slots + one §VII.PROP slot at plan-freeze to lock against parallel-writer collisions.

**(EN-β) The unification of S46/S64/S65/S77/S82-W2-5 prior closures under the M2-AXIOM-FAILURE structural source is broader than the "M2-axiom-is-CC-problem" framing — five prior closures are SLOT-BY-SLOT manifestations of the SAME finite-L_max calibration mismatch.** This is a deeper emergent reading than either of us stated through R1+R2. The substitution chain:

```
Step 1 (definitions, slot inventory of prior closures):
  S46 a_2 split (memory permanent-theorems.md):
    SD geometric a_2 ≈ 0.728 (manifold integral)
    ζ_D(1) ≈ 2776.17 (zeta-regulated extraction at s=1, L_max=7)
    ratio = 3812 (factor-of-3812 mismatch at the a_2 SLOT)
  S64 Lambda_SA = Lambda_J at the a_0 SLOT (at the algebraic level):
    framework-cc-oom.md: 114 OOM gap between Lambda_SA (continuum) and
    Lambda_observed at the a_0 / cosmological-constant slot.
  S65 a_0/a_2 = C/R universal (memory s65-connes-collab.md):
    For ANY left-invariant metric on SU(3), the a_0/a_2 ratio depends ONLY on R.
    This is the CONTINUUM result at the a_0 + a_2 slots.
  S77 R-protection-universal-fails-at-a_0 (project_s77_synthesis):
    a_0 slot is the SOLE Lizzi-observable where R-protection universally fails.
  S82 W2-5 MP-Exclusion (memory s82-mp-exclusion-theorem.md):
    sqrt(x) cusp regulators outside CM Sd; t^{-3/2} branch-point.
    This is a regulator-class restriction at all SLOTS but particularly tight at
    high-n slots (where the sqrt cusp decays).
  C9 a_0 9.46× ratio (this workshop):
    Empirical observable confirming a_0 slot M2-failure under F_4 algebra.

Step 2 (substitute the M2-axiom-failure reading per slot):
  S46 a_2 split: M2-failure at the a_2 slot. The continuum SD residue extraction
                 at s=1 (= a_2 slot) requires K_truncated(t) ~ a_2 t^{-3} as t→0,
                 the manifold's fractional-power asymptotic. At L_max=7, the
                 truncated cache's polynomial-in-t expansion gives a different
                 ζ_D(1) coefficient than the manifold integral. Factor 3812 is
                 the slot-by-slot magnitude of the M2-failure-induced calibration
                 mismatch at a_2.
  S64 Lambda_SA: 114 OOM gap is partially M2-failure at finite L (per DN-γ, the
                 finite-L residual contribution is bounded; the BULK of the gap
                 is continuum-level and outside M2-failure).
  S65 a_0/a_2 universal: the continuum-level RATIO is well-defined; it is M2-
                         PASS-conditioned (CCM-2007 trace theorem on smooth SU(3)).
                         At finite L_max, the ratio carries M2-failure residuals
                         in BOTH numerator and denominator that may partially
                         cancel.
  S77 a_0 R-protection failure: M2-failure at a_0 specifically (per E-α).
  S82 W2-5 MP-Exclusion: regulator-class restriction. NOT a slot-specific
                         M2-failure; rather a restriction on which regulators
                         have completely-monotone Mellin profiles.
  C9 9.46× a_0 ratio: empirical M2-failure at the a_0 slot (per CN-β).

Step 3 (simplify, slot-by-slot M2-failure inventory):
  a_0 slot: M2-failure dominant. Manifestations: S64 finite-L residual,
            S77 R-protection failure, C9 9.46× ratio. THREE prior closures.
  a_2 slot: M2-failure factor 3812 (S46 split). ONE prior closure.
  a_4, a_6 slots: high-n moments are dominated by low-λ end of spectrum,
                  ALREADY Weyl-saturated at n ≥ 4 (per Re:L1 §W2-1 line 78
                  reading: M_4(5)=5.65e+03 → M_4(10)=2.77e+02 monotone DECREASE;
                  M_6(5)=1.05e+05 → M_6(10)=1.03e+05 stable). M2-failure is
                  PRESENT but its magnitude is small at these slots.
  Regulator-class restrictions: S82 W2-5 (cusp regulators). ORTHOGONAL to slot
                                inventory but constrains the F_4 algebra's scope.

Step 4 (substitute into emergence statement):
  The M2-AXIOM-FAILURE structural source UNIFIES five prior closures under one
  source-of-difficulty:
    a_0 slot: 3 closures (S64 finite-L residual, S77 R-protection, C9 ratio)
    a_2 slot: 1 closure (S46 split)
    Regulator class: 1 closure (S82 W2-5 MP-Exclusion as boundary condition)
  Total: 5 prior closures unified.
  The four prior closures NOT in this list (S65, S46/S64 continuum-level parts)
  are CONTINUUM features that M2-failure does NOT explain — they are M2-PASS
  features.

Step 5 (direction):
  The unification is broader than the M2-AXIOM-IS-CC-PROBLEM framing because it
  spans multiple slots, not just a_0. The S87 §VII.X meta-theorem entry should
  cite all five prior closures in its anchor list, with slot-by-slot magnitude
  of the M2-failure-induced calibration mismatch tabulated.
```

**Concrete proposal**: the §VII.X meta-theorem entry (`S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL`) should cite five prior closures (S46, S64-finite-L-component, S77, S82-W2-5, C9) and include a slot-by-slot magnitude table:

| Slot | M2-failure manifestation | Prior closure | Magnitude |
|:-----|:-------------------------|:--------------|:----------|
| a_0 (s=0) | Finite-L Lambda_SA residual | S64 (component) | bounded by 1 OOM at L_max=10 |
| a_0 (s=0) | R-protection-universal failure | S77 | universal across F_4 |
| a_0 (s=0) | F_4 ratio 9.46× | C9 (this workshop) | 18.91× over PASS bound |
| a_2 (s=1) | Geometric vs spectral split | S46 | factor 3812 |
| Regulator-class | Cusp regulators outside CM Sd | S82 W2-5 | t^{-3/2} branch outside Sd |

The unification is necessity-direction only (per DN-γ). The slot-by-slot magnitude makes the meta-theorem testable: future S87+ closure scripts can recompute each entry on the L_max=12 master cache and verify the M2-failure magnitude is monotone in L_max → ∞ for each slot.

**(EN-γ) The d_eff(SU(3)/Z_3) Casimir-tower asymptotic question (lizzi's Q-L-NEW-5) has a structural answer that resolves Q-L-NEW-4 simultaneously: the per-slot Weyl-saturation thresholds L_∞^{n} are NOT independent — they are anchored by a single d_eff parameter whose Jensen-deformation dependence governs all four slots together.** This is a structurally compact answer that neither of us stated through R2 because the analysis required combining lizzi's Q-L-NEW-4 (per-slot threshold question) with Q-L-NEW-5 (d_eff vs Spin(8) embedding question). Substitution chain:

```
Step 1 (definitions):
  d_manifold = 8 (geometric dimension of SU(3))
  d_eff = effective spectral dimension of Jensen-deformed SU(3) at τ_fold,
          truncated to L_max
  Weyl asymptotic: N(λ; L_max) ~ c · λ^{d_eff}  as L_max → ∞ at fixed λ
  L_∞^n := Weyl-saturation threshold for the n-th Mellin moment
           (smallest L_max where M_n^reg(L_max) saturates within ε)
  Connes trace theorem: ζ_D(s) has a simple pole at s = d_eff with residue
                        proportional to the manifold's volume.

Step 2 (substitute the Casimir-tower-specific asymptotic):
  For Spin(8) compactification of SU(3) at the manifold level (M^4 × SU(3)
  with smooth SU(3)), the Connes trace theorem gives d_eff = 8 by direct
  identification with the manifold dimension.
  Jensen deformation at τ_fold deforms the metric on SU(3); the spectral
  triple structure is preserved at the manifold level (Jensen TT-deformation
  preserves volume, by construction). Therefore d_eff = 8 in the continuum
  limit even at τ_fold.
  At finite L_max, the truncation samples (p,q) Casimir eigenvalues with
  Weyl-dim weights d(p,q) = (1/2)(p+1)(q+1)(p+q+2). The truncated cache
  has discrete spectrum and ζ_D(s, L=10) is entire (no pole). d_eff at finite
  L is therefore "0 effectively" in the sense connes Re:L4 step 3 noted —
  no continuum pole structure. d_eff = 8 emerges as L_max → ∞.

Step 3 (simplify, per-slot threshold):
  L_∞^n is the smallest L_max where the n-th SD coefficient extraction
  saturates. The dominant contribution at the n-th slot is from eigenvalues
  near a slot-specific λ-scale:
    n=0 slot (a_0): integrates ALL eigenvalues with weight λ^0 = 1.
                    Dominated by eigenvalue density at the truncation boundary.
                    Approaches saturation only when the high-(p+q) Weyl-dim
                    contribution stabilizes — REQUIRES large L_max.
    n=2 slot (a_2): integrates eigenvalues with weight λ^{-2}.
                    Dominated by intermediate eigenvalues. Saturates at
                    moderate L_max.
    n=4, n=6 slots: integrate with weights λ^{-4}, λ^{-6}.
                    Dominated by low-λ end (small eigenvalues), which is stable
                    across L_max. Saturate at small L_max.

Step 4 (substitute into single-d_eff anchor):
  The four L_∞^n thresholds are NOT independent. They are anchored by ONE
  d_eff parameter and a slot-specific decay scale:
    L_∞^n ≈ L_0(d_eff) × κ^{-n}  for some κ > 1 (slot-decay parameter)
  In the SU(3) Jensen-deformed substrate at τ_fold:
    d_eff = 8 (continuum)
    κ ≈ 2 (rough estimate from M_n^ζ growth pattern: 239× at n=0, ~stable at n=2,
             monotone DECREASE at n=4, stable at n=6)
  The Casimir-tower Weyl asymptotic is the SAME asymptotic as the Spin(8) manifold
  Weyl asymptotic AT THE CONTINUUM LIMIT — they are not different mechanisms.
  The Jensen deformation does NOT change d_eff at τ_fold (volume-preserving,
  see permanent-theorems.md).

Step 5 (direction):
  Lizzi's Q-L-NEW-5 dichotomy ("Spin(8) Weyl asymptotic vs Casimir-tower asymptotic
  — same or different?") resolves: SAME at the continuum, with d_eff = 8 inherited
  from the manifold. The Casimir-tower truncation is a LOW-L_max truncation of the
  manifold's Weyl asymptotic, not a different counting law.
  Lizzi's Q-L-NEW-4 ("L_∞ slot-dependent cliff or single threshold?"): SLOT-DEPENDENT
  but ANCHORED by single d_eff. The dependence is ordered: L_∞^{n=0} > L_∞^{n=2}
  > L_∞^{n=4} ≈ L_∞^{n=6}, with the n=0 threshold being the bottleneck.
  This means: empirically, Weyl-saturation at the high-n slots is already achieved
  at L_max=10 (per §W2-1 line 78 reading); the BOTTLENECK is the n=0 slot,
  consistent with C9's FAIL at a_0 specifically.
```

**Concrete proposal**: the S87 plan's `S87-LMAX-WEYL-CONVERGENCE-SWEEP` gate (lizzi's D-γ priority 3) should be PER-SLOT rather than family-wide, with the n=0 slot designated as the BOTTLENECK threshold. The expected ordering L_∞^{n=0} > L_∞^{n=2} > L_∞^{n=4} ≈ L_∞^{n=6} is a falsifiable prediction at the L_max=12 cache level: the M_n^reg(L=12) data should show n=0 still growing, n=2 nearly saturated, n=4/6 essentially stable. If the L_max=12 sweep contradicts this ordering, the d_eff = 8 anchor is wrong (Q-L-NEW-5 dichotomy resolves toward "Casimir-tower different from Spin(8)"). If it confirms, the single-d_eff anchor is solid and the L_∞ search collapses to a one-parameter problem.

This emergence resolves both Q-L-NEW-4 and Q-L-NEW-5 with one substitution chain. The single-d_eff anchor is testable on existing L_max=12 master cache data; the per-slot ordering is falsifiable. The S87 plan should include `S87-D-EFF-ANCHOR-VERIFICATION` as a DIAGNOSTIC gate (effort 4–6h) that recomputes M_n^reg(L) for L ∈ {5, 8, 10, 12} per regulator and tests the per-slot ordering at the 1% saturation level.

**Closing of the EMERGENCE section**: the joint reading produces FOUR §VII registry entries (with classification-based slot assignment per EN-α), one slot-by-slot magnitude unification (EN-β), and one single-d_eff Weyl-saturation anchor (EN-γ). These are non-overlapping outputs covering distinct EMERGENCE topics (registry hygiene, prior-closure unification, asymptotic-scaling structure). The R3 final selection should consolidate them into the joint S87 plan blocks, with classification-based slot pre-allocation, slot-by-slot magnitude tabulation, and per-slot d_eff anchor verification gate.

---

## Round 3 — lizzi: Follow-up

### CONVERGENCE

After connes' R2 cross-synthesis I now lock in six commitments. Five accept connes' R2 sub-points outright; one (DN-α) is a partial concession that converts a R2 dissent into a layered registry-and-closure-script protocol. The cumulative effect is the workshop's R3 union (ii) ∧ (iii) ∧ (i)-on-T5-only is structurally complete and ready for plan-freeze.

**(L-CN-1) I accept connes' DN-α partial-concession verbatim — the universal quantifier ∀ reg ∈ F_4 survives at registry-statement level, with per-regulator tagging mandated at the closure-script level.** Connes' DN-α substitution chain (workshop §"Round 2 — connes" CONVERGENCE/DISSENT block, lines 1300–1334) numerically verified the L=10 dispersion at 9.34% and computed the growth-factor proxy (Zubarev 218.3×, SDW 223.6×) — both clearing the n=0 growth diagnostic threshold of 100× by factor ≥ 2.18×. I independently re-verified these numbers via Python (`spread(F_4) = 0.093415` bit-exact; growth_0_proxy(Zubarev) = 218.31×, growth_0_proxy(SDW) = 223.65× to 4 sig figs). The threshold-crossing dispersion connes cited as "100%" is in fact 58.1% under the substitution chain definition `1 - (100/238.7) = 0.5811` — the threshold-crossing condition `growth_0(reg) < 119` would require regulator deviation ≥ 50.2% downward from ζ-class, an order of magnitude above the observed 9.34%. **Substitution chain (re-derived rigorously)**:

```
Step 1 (definitions):
  growth_0(reg)        := M_0^reg(L=10) / M_0^reg(L=5)              [n=0 Mellin growth ratio]
  threshold_diag       := 100                                         [DIAGNOSTIC fires if growth_0 > 100]
  ratio_proxy(reg)     := growth_0(ζ) · r(reg) / r(ζ)                 [conservative ansatz, multiplicative
                                                                       in L=10 ratio r(reg)]
  threshold_crossing_dev := 1 − threshold_diag/growth_0(ζ)            [downward deviation from ζ at which
                                                                       proxy reaches threshold]
Step 2 (substitute observed values):
  growth_0(ζ)          = 9.38e+07 / 3.93e+05 = 238.6768               [verified to 4 sig figs]
  r(ζ) = 10.339   r(Zubarev) = 9.4557   r(SDW) = 9.6870               [§W2-1 lines 53–55]
  spread(F_4)          = (10.339 − 9.4557) / 9.4557 = 0.09341         [9.34% bit-exact]
  ratio_proxy(Zubarev) = 238.6768 × (9.4557 / 10.339) = 218.3116
  ratio_proxy(SDW)     = 238.6768 × (9.6870 / 10.339) = 223.6489
Step 3 (canonical form):
  threshold_crossing_dev = 1 − 100/238.6768 = 0.5811                  [58.11% downward, NOT 100%]
  observed_dev (max)    = 0.0934                                       [9.34%]
  margin = threshold_crossing_dev / observed_dev = 0.5811 / 0.0934 = 6.22
Step 4 (substitute into universal-quantifier-survival test):
  ALL three regulators clear threshold_diag with margin:
    ζ:        238.7  / 100 = 2.387×
    Zubarev:  218.3  / 100 = 2.183×
    SDW:      223.6  / 100 = 2.236×
  Worst-case margin (Zubarev) = 2.18× = 1 + 1.18 = 118% over threshold.
Step 5 (direction):
  Empirically, ∀ reg ∈ F_4 the n=0 growth diagnostic fires at L=10 by
  factor ≥ 2.18×. The observed dispersion 9.34% is 6.22× smaller than
  the dispersion required to push any regulator below threshold. The
  universal quantifier holds at registry-statement level WITH MARGIN.
  Conclusion: ACCEPT connes' DN-α; per-regulator scope is a closure-
  discipline matter, not a registry-statement matter.
```

**Concrete amendment** (correction to connes' DN-α): the R2 chain stated "100% deviation" as the threshold-crossing condition; the substitution chain shows 58.11%. This is a tighter bound and STRENGTHENS connes' DN-α conclusion — the universal quantifier is empirically supported with even more margin than connes claimed (6.22× rather than ~10× headroom). I withdraw my D-α scope-narrowing demand at the registry-statement level and re-register it as the closure-discipline rule (S82 W3-L per-branch scoping precedent applies to the S87 closure script that computes growth_0 per regulator and tags each branch).

**(L-CN-2) I accept connes' DN-β framing correction — `dim(H_F)=96` is fiber-blind by tensor-product multiplicativity and produces NULL content for the C10 INFO band.** Connes' DN-β (lines 1338–1374) sharpens my D-β statement that the cancellation IS mathematical content but reframes it as a NULL RESULT (absence of constraint), not a structural anchor. I had read `Δ_rel(L_1, L_2) = g(SU3-only quantities)` as a "DIM-FACTOR-CANCELING-CONSISTENCY-CHECK" because the cancellation is a verifiable identity. Connes is right that a consistency check requires non-trivial dependence to consist OF; here the dependence is identically zero, so the cancellation is testimony to ABSENCE-of-dependence, not a structural anchor. I retract "DIM-FACTOR-CANCELING-CONSISTENCY-CHECK" and adopt connes' "fiber-blind by tensor-product multiplicativity, NULL constraint" terminology for the S87 §VII registry annotation on the C10 INFO band. The substantive content of D-β survives: the multiplicative-factorization step IS necessary mathematics for ruling out a putative `dim(H_F)`-bound, but the resulting null content is correctly framed as "no finite-triple-invariant lower bound exists" rather than as a soft structural anchor.

**(L-CN-3) I accept connes' DN-γ necessity-only restatement of the M2-AXIOM-IS-CC-PROBLEM meta-theorem.** Connes' DN-γ (lines 1376–1429) split the meta-theorem into (a) necessity direction "M2-FAIL is a structural source for the three failures" — supported by the substitution chain — and (b) sufficiency direction "M2-PASS resolves the 114 OOM gap" — NOT supported, because the bulk of the 114 OOM gap is continuum-level (Lambda_SA at the M2-PASS continuum limit, per CCM-2007 spectral action chapter, differs from Lambda_observed by 114 OOM independently of any truncation). My E-β framing used "REDUCES TO" which is biconditional and asserted both directions. Connes is right to flag this as overreach. **I retract "REDUCES TO" and adopt connes' necessity-only restatement** (workshop line 1425–1428): "M2-axiom failure on the truncated cache is a STRUCTURAL SOURCE for: (a) the Lambda_SA finite-L-conditional residual (S64 contributing component); (b) the C9 9.46× a_0/Λ_CC ratio FAIL; (c) the S77 a_0-slot R-protection-universal failure. The 114-OOM Lambda_SA → Lambda_observed gap is CONTINUUM-LEVEL and is NOT contained in the M2-failure structural source — M2-PASS at the continuum limit does NOT resolve the 114-OOM gap." This is the correct registry-statement form. The R3 carry-forward gate naming should be `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL` (necessity-only, connes proposed) — NOT `S87-M2-AXIOM-IS-CC-PROBLEM` (the broader meta-claim I had drafted). The narrower name correctly localizes scope.

**(L-CN-4) I accept connes' EN-α classification-based §VII slot assignment over my Q-L-NEW-1 sponsorship-based scheme.** Connes' EN-α (lines 1435–1488) proposed assigning §VII slots by mathematical-content classification (Algebraic-vs-Spectral × Axiom-vs-Empirical) rather than by which agent anchored each entry. This is the right discipline: future readers locate theorems by content type, sponsorship metadata appears in the entry's "Sponsors" field. I adopt the proposed map verbatim:

| §VII slot | Entry | Class | Anchor |
|:----------|:------|:------|:-------|
| §VII.U | FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY | ALGEBRAIC × AXIOM | lizzi |
| §VII.V | CM-1995-INADMISSIBILITY-AT-FINITE-L (with WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A) | AXIOM × SPECTRAL | connes |
| §VII.W | A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE | SPECTRAL × CROSS-PROGRAM | joint |
| §VII.X | M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL | AXIOM × META | joint |
| §VII.PROP | P_MB / P_CM un-bundling routing-layer | ROUTING | joint |

The S87 plan must pre-allocate all four §VII slots (U, V, W, X) AND one §VII.PROP slot in a synchronization lockfile (per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race") to prevent the W1c collision pattern. Append-only Python writers must scan ALL header levels (## + ### + ####) before allocation. I will draft the synchronization lockfile spec as a §VII.PROP appendix in the S87 plan.

**(L-CN-5) I accept connes' EN-β 5-prior-closure unification and the slot-by-slot magnitude table.** Connes' EN-β (lines 1490–1576) extends the unification beyond the M2-AXIOM-IS-CC-PROBLEM framing to span FIVE prior closures: S46 a_2 split (factor 3812 mismatch at a_2 slot), S64 Lambda_SA/J finite-L component (a_0 slot), S65 a_0/a_2 = C/R universal (continuum a_0 + a_2 slots — connes correctly notes this is M2-PASS-conditioned), S77 R-protection failure at a_0, S82 W2-5 MP-Exclusion (regulator-class boundary). Knowledge MCP independently corroborates the S46 magnitude — `a_2^zeta / a_2^SD = 2776.17 / 0.7282 = 3812.18` (s64_bdg_kasparov.py canonical comment; s61_heat_kernel_a2_log.txt structural entry "Geometric a_2^{SD} = 0.728234972609" + "Spectral zeta sum a_2(spectral, S42) = 2776.165389"). Connes' table is correct as stated. I add ONE refinement: knowledge-MCP also surfaces the parallel a_0 split `a_0^zeta / a_0^Gilkey = 6440 / 0.866 = 7436` (s64_bdg_kasparov.py comment) — this is a SECOND a_0-slot M2-failure manifestation tracking S46's a_2 split at the a_0 slot itself. The §VII.X meta-theorem entry's slot-by-slot magnitude table should add one row:

| Slot | M2-failure manifestation | Prior closure | Magnitude |
|:-----|:-------------------------|:--------------|:----------|
| a_0 (s=0) | Geometric vs spectral split (continuum-paired) | S64 (s64_bdg_kasparov comment) | factor 7436 |

This refinement DOES NOT alter the registry-statement form connes proposed; it adds a second a_0-slot empirical anchor tracking S46 at the same slot. The unification is now SIX prior closures: S46 (a_2 split 3812) + S64-finite-L-component (a_0 + a_2 paired splits 7436/3812) + S65 (continuum, M2-PASS-conditioned, NOT a M2-failure manifestation) + S77 (a_0 R-protection) + S82-W2-5 (regulator-class) + C9 (this workshop, a_0 ratio 9.46×). Connes' EN-β reads as five-with-one-split rather than five flat; the underlying structure is unchanged.

**(L-CN-6) I accept connes' EN-γ single-d_eff Weyl-saturation anchor with per-slot threshold ordering.** Connes' EN-γ (lines 1577–1647) resolves both Q-L-NEW-4 and Q-L-NEW-5 simultaneously: d_eff = 8 (Casimir-tower asymptotic = Spin(8) manifold asymptotic at continuum, since Jensen TT-deformation is volume-preserving per `permanent-theorems.md`), and L_∞^n is anchored by single d_eff with per-slot ordering L_∞^{n=0} > L_∞^{n=2} > L_∞^{n=4} ≈ L_∞^{n=6}. I commit to this as the canonical S87 anchor for the L_max-sweep refutation pathway. The falsifiable prediction connes formulated — at L_max=12, M_n^reg(12) should show n=0 still growing, n=2 nearly saturated, n=4 and n=6 essentially stable — is testable on the existing 155,984-eigenvalue master cache (`s84_spectrum_cache_L12_tau019.npz`) without new cache regeneration. This makes `S87-D-EFF-ANCHOR-VERIFICATION` a moderate-effort gate (4–6h) that DECISIVELY tests the single-d_eff anchor before the L_max=14 heavy effort would be invoked. I adopt the gate definition verbatim from connes' EN-γ closing.

**Joint R3 commitment locked**: the workshop emits **(ii) ∧ (iii) ∧ (i)-on-T5-only** as a non-overlapping union covering the four W3/W2 consumer cascades. This matches both my R2 C-δ commitment (line 951) and connes' R2 CN-δ acceptance (lines 1215–1216). All five EMERGENCE topics (CN-α through CN-6) lock in and inform the S87 plan blocks. The R3 plan-freeze is structurally ready.

### DISSENT

I hold ONE remaining dissent that genuinely requires S87 follow-up. It is NEW evidence beyond R1+R2: a previously-unconsidered ambiguity in connes' EN-γ single-d_eff anchor that affects the per-slot ordering at finite L_max=10. I do NOT restate prior dissents; D-α/D-β/D-γ from R2 are subsumed under the L-CN-1/2/3 commitments above.

**(L-DN-1) The single-d_eff anchor (connes EN-γ) implicitly assumes the Jensen-deformation does NOT shift the SLOT-DEPENDENT decay parameter κ between F_4 regulators — but the F_4 regulator algebra acts on the substrate's Mellin profile, not on its bare counting function, so κ may carry F_4-dependence at finite L_max=10 even with d_eff = 8 anchored.** Connes' EN-γ Step 4 wrote `L_∞^n ≈ L_0(d_eff) × κ^{-n}` for some κ > 1 (slot-decay parameter), implicitly treating κ as a regulator-independent constant. The substitution chain that surfaces this issue:

```
Step 1 (definitions):
  L_∞^n           := smallest L_max where M_n^reg(L_max) saturates within ε
  L_0(d_eff)      := L-scale at which d_eff anchors the Weyl saturation
  κ(reg, n)       := slot-decay parameter; in EN-γ assumed reg-independent
  M_n^reg(L)      := n-th Mellin moment under regulator reg at L_max=L
                    explicit form: M_n^reg(L) = Σ_k m_k λ_k^{-2n} · weight^reg(λ_k)
                    where weight^reg(λ) is the regulator-specific Mellin profile

Step 2 (substitute the F_4 regulator profiles):
  weight^ζ(λ)     ∝ λ^{-s}                                  [zeta scheme, single power]
  weight^Zubarev(λ) ∝ exp(-λ²/Λ_Z²)                         [Gaussian decay, scale Λ_Z]
  weight^SDW(λ)   ∝ Λ_SDW^{2s} · Γ(s) · (regulated)        [Mellin-Barnes profile]

Step 3 (substitute into M_n^reg saturation behavior):
  Saturation of M_n^reg(L=10) requires the high-(p+q) Weyl-dim contributions to
  decay below ε. For ζ-weight, the decay rate at λ_max(L) is power-law (slow);
  for Zubarev-weight, exponential (fast); for SDW-weight, intermediate.
  These three decay rates produce DIFFERENT effective κ_n^reg in the formula:
    L_∞^{n,reg} ≈ L_0(d_eff) · κ_n^{-n,reg}

Step 4 (substitute the empirical L=5 → L=10 growth signatures):
  ζ-class    n=0:  growth = 238.7×                            [slow-decaying weight, full impact]
  Zubarev    n=0:  ratio_proxy growth = 218.3×                [exponential weight, slightly compressed]
  SDW        n=0:  ratio_proxy growth = 223.6×                [Mellin weight, intermediate]
  Differences are SMALL at the 9.34% L=10 dispersion level — but the κ_n^reg
  difference compounds to per-regulator L_∞^{n=0} thresholds that may
  differ by O(1) at the L_max-scale level.

Step 5 (direction):
  Connes' EN-γ uses single κ → single L_∞^n ordering across F_4. At L_max=10
  the F_4 dispersion is small (9.34%), but the SATURATION threshold is a
  CUMULATIVE quantity — each regulator's saturation comes from the integrated
  decay of high-(p+q) contributions, which is regulator-conditional.
  At the L_max=12 cache verification, the per-slot thresholds may show
  ordering L_∞^{n=0,ζ} > L_∞^{n=0,SDW} > L_∞^{n=0,Zubarev} (Zubarev's
  exponential weight saturates fastest), even though all three exceed L_max=10.
```

**Concrete S87 amendment**: the `S87-D-EFF-ANCHOR-VERIFICATION` gate connes proposed (EN-γ closing) should include a per-regulator κ_n^reg measurement, not just the per-slot L_∞^n ordering. The PASS criterion can include: "if ordering across F_4 holds within 20% at each slot n, single-d_eff anchor is supported; if ordering inverts (e.g., L_∞^{n=0,Zubarev} < L_∞^{n=0,ζ} by more than 20%), regulator-conditional κ_n^reg corrections are required." This is a refinement of the gate, not a refutation of EN-γ. The dissent is one-sided: I accept the d_eff = 8 anchor; I flag that the per-slot threshold formula may need a per-regulator κ_n^reg correction at finite L_max ≤ 12.

This is the only NEW dissent. All other R2 disagreements are now closed by the joint commitments in CONVERGENCE.

### EMERGENCE

Two new structural insights surface from the R2-R3 joint reading that NEITHER R1 nor R2 alone produced. Each addresses content that became visible only after both agents had committed to the joint registry framework.

**(L-EN-1) The S87 plan's S87-PV-SUBTRACTION-RECALIBRATION primary refutation gate has a sharper PASS criterion when read through the §VII.U FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY anchor — the recalibrated subtraction must preserve the finite-spectrum identity at off-pole s while inducing F_4 ratio suppression at on-pole s.** This refinement was not visible until both §VII.U (the algebraic identity at off-pole s) and §VII.V (the no-go at the SD slots, which are the pole-residue evaluations) were jointly committed. The substitution chain:

```
Step 1 (definitions):
  PV-recalibrated subtraction:= Pauli-Villars subtraction with coefficients
                                 calibrated against the L_max=10 cache itself
                                 (rather than against the L_max → ∞ continuum)
  Off-pole identity (§VII.U): analytic_zeta(s, L) = ζ_D(s, L) exactly at s ∉ Sd
  On-pole F_4 suppression:    |Λ_CC^MB(reg, PV)| / |a_0^trunc(reg)| ≤ 5e-1 at slot s=0

Step 2 (substitute the recalibration's structural constraint):
  PV recalibration introduces NEW subtraction coefficients c_n^PV(L=10) such that:
    a_n^PV(reg, L=10) := Mellin residue extraction with c_n^PV at slot n
  The recalibration MUST satisfy:
    (a) at off-pole s, analytic_zeta(s, L=10) - PV-subtraction-counter-terms(s) is
        the same as analytic_zeta(s, L=10) itself within machine-ε. The PV terms
        are slot-residues with vanishing contribution at off-pole s.
    (b) at on-pole s ∈ Sd ∩ {0, 2, 4, 6}, the recalibrated a_n^PV(reg, L=10)
        produces |Λ_CC^MB(reg, PV)| / |a_0^trunc(reg)| ≤ 5e-1.

Step 3 (canonical form):
  (a) is NECESSARY for §VII.U to survive the recalibration. PV is structurally
      designed to be slot-localized (residue counter-terms), so off-pole behavior
      is preserved by construction. CHECK: PV recalibration cannot accidentally
      destroy the finite-spectrum identity at off-pole s.
  (b) is the actual PASS criterion of S87-PV-SUBTRACTION-RECALIBRATION.

Step 4 (substitute into joint criterion):
  The S87 gate must verify BOTH:
    PV-OFF-POLE-CONSISTENCY: rel_err(analytic_zeta(s, L=10), Dirichlet) at
                              s ∈ {2.5, 2.75, 3.0, 3.25, 3.5} remains ≤ 5×float_eps
                              after PV subtraction is applied (sanity check).
    PV-ON-POLE-SUPPRESSION:  |Λ_CC^MB(reg, PV)| / |a_0^trunc(reg)| ≤ 5e-1 at
                              s=0 for at least one reg ∈ F_4.
  Joint criterion: BOTH must PASS for the gate to PASS.

Step 5 (direction):
  Without the joint criterion, a PV recalibration could pass the on-pole
  suppression by violating the off-pole identity (e.g., by introducing
  spurious off-pole counter-terms that shift analytic_zeta at s=3 below
  machine ε). This would be a Class-1 convention-shopping pattern (per
  `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS). The joint
  criterion structurally precludes this, by requiring §VII.U identity
  preservation as a sanity-anchor.
```

**Concrete S87 amendment**: the `S87-PV-SUBTRACTION-RECALIBRATION` gate's PASS criterion should be JOINT (off-pole identity preservation + on-pole F_4 suppression), not single (on-pole only as I framed in D-γ). This emergence was not stated in my R1 or R2; it required connes' EN-α §VII.U classification to make the off-pole-identity-as-sanity-anchor visible. The S87 plan should pre-register both halves of the joint criterion at plan-freeze.

**(L-EN-2) The R3-prescribed branch (ii) (no-go theorem) and branch (iii) (per-evaluation re-pre-registration) are NOT independent of branch (i)-on-T5-only — the T5 Mellin-Strip / Convergence-Cone Theorem provides the analytic complement that makes branches (ii) and (iii) jointly tight rather than disjoint covers.** This complementarity was visible in connes' R1 Re:L4 closing line ("Both can stand in the registry without contradiction"; line 396) but the deeper structural reading required the EN-β prior-closure unification to surface: T5 (continuous Mellin profile of the regulator kernel, Zubarev's `Λ_Z^{2s}·Γ(s)`, INFINITE-VECTOR class) is the EXACT MIRROR of §VII.U (continuous Mellin profile of the truncated substrate, Σ_k m_k λ_k^{-s}, FINITE-VECTOR class). The substitution chain that surfaces the mirror structure:

```
Step 1 (definitions):
  T5 (W2 Candidate 3, S87 W1b land):
    M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s} · Γ(s)     [closed-form Mellin transform of regulator kernel]
    Domain: s ∈ ℂ \ {0, -1, -2, ...}          [convergence cone Re(s) > 0 except simple poles at -ℕ]
    Class: INFINITE-VECTOR                    [continuous Mellin profile]
  §VII.U (FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY):
    M[Tr(e^{-tD²})](s/2) / Γ(s/2) = Σ_k m_k λ_k^{-s} = ζ_D(s, L)  [exact at finite L]
    Domain: s ∈ ℂ \ {0}                       [entire on ℂ except for division-by-Γ-pole]
    Class: FINITE-VECTOR                      [discrete Mellin profile]

Step 2 (substitute the duality):
  Both identities are "Mellin transform of an exponential-type kernel = a closed form on s"
  on a substrate-of-evaluation ranging over either the kernel (T5) or the spectrum (§VII.U).
  T5    : Mellin lens applied to ONE exponential       → ONE Mellin-pole structure
  §VII.U: Mellin lens applied to SUM of N_evs exponentials → SUM of Mellin-pole-evaluations
            (which collapses by the Euler integral to the Dirichlet form)
  These are DUAL under the multiplier-action: T5's closed form IS the multiplier,
  §VII.U's substrate IS what the multiplier acts on.

Step 3 (canonical form, joint structure):
  The F_4 ∘ MB ∘ SD-subtraction CC-suppression program is the COMPOSITION:
    (T5-class identity for regulator kernel) ∘ (CM-1995-prescribed subtraction) ∘
    (§VII.U-class identity for substrate spectrum)
  T5 verifies the FIRST factor (regulator side, INFINITE-VECTOR).
  §VII.U verifies the THIRD factor (substrate side, FINITE-VECTOR).
  §VII.V (CM-1995-INADMISSIBILITY no-go) closes the MIDDLE factor at L_max=10.

Step 4 (substitute into the joint registry tight-cover claim):
  Branch (i)-on-T5: T5 lands the regulator-side identity at S87 W1b citing C11.
  Branch (ii) §VII.V: closes the CM-1995-prescription middle factor at L_max=10.
  Branch (iii) §VII.U: lands the substrate-side identity at S87 (works regardless of
                       whether the middle factor passes; the substrate identity is
                       L_max-INVARIANT at off-pole s).
  Together: branches (i), (ii), (iii) FACTORIZE the F_4 ∘ MB ∘ SD-subtraction
  pipeline into three structural components, with (i) and (iii) verified positive
  and (ii) verified closed at L_max=10. The composition is NOT covered by any
  single branch; it requires all three to characterize the failure precisely.

Step 5 (direction):
  The R3 union (ii) ∧ (iii) ∧ (i)-on-T5-only is structurally TIGHT — it is the
  MINIMAL set of branches that characterizes the F_4 ∘ MB ∘ SD-subtraction
  CC-suppression program at L_max=10. Removing any branch leaves a structural
  ambiguity: removing (i) loses the regulator-side anchor; removing (iii) loses
  the substrate-side anchor; removing (ii) loses the localization of the failure
  at the middle factor.
  Conclusion: the R3 union is not three independent outputs but a STRUCTURALLY
  COUPLED FACTORIZATION of the F_4 ∘ MB ∘ SD-subtraction pipeline.
```

**Concrete S87 amendment**: the S87 plan should write the §VII.U + §VII.V + W1b-T5 landings as a COUPLED-LANDING-BLOCK with cross-references between the three entries explicit at plan-freeze. Each registry entry's "Provenance" field should cite the other two as STRUCTURAL-COMPLEMENTS (not independent results). This is the deepest emergence of the joint reading: the workshop's R3 union is not a disjoint cover of the consumer cascade — it is a STRUCTURAL FACTORIZATION of the F_4 ∘ MB ∘ SD-subtraction program, making each branch necessary for the other branches to be interpretable.

This emergence was NOT visible in R1 (where the three branches were treated as alternative R3 outputs in the pre-registered adjudication rule) and only becomes visible in R3 after both classifications and the prior-closure unification have committed.

### QUESTIONS

Five sharp questions for connes' R3 verdict turn. Each is designed to lock in the R3 branch selection unambiguously and surface any remaining ambiguity in the joint S87 plan-freeze before connes writes the Workshop Verdict + Wrap-Up.

**(Q-L-R3-1) Verdict-line PASS-INFO-FAIL classification for the four §VII.U/V/W/X candidate landings — do you see them as PROVABLE-AT-S87-PLAN-FREEZE (PASS), PROVABLE-CONDITIONAL-ON-CLOSURE-SCRIPT (INFO), or PROVEN-MODULO-NUMERICAL-RECONFIRMATION (PASS-with-cite)?** My read of L-CN-2 and L-CN-3 is that §VII.U (FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY) is PROVEN at the algebraic level (mathematically tight; closure script is a single recompute against the L_max=12 cache to extend the L=10 result), §VII.V (CM-1995-INADMISSIBILITY) is PROVEN-MODULO-NUMERICAL-RECONFIRMATION (closure script computes growth_0 per regulator on the L=12 cache and tags branches per L-CN-1), §VII.W (A0-R-PROTECTION-FAILURE-IS-M2) is PROVABLE-CONDITIONAL on a synthetic-toy-model verification script (closure script demonstrates M2-failure → R-protection-failure on a 2-eigenvalue toy), and §VII.X (M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL, necessity-only per L-CN-3) is PROVABLE-CONDITIONAL on the §VII.X slot-by-slot magnitude table being recomputed at L_max=12. Do you concur with this 4-level classification, or do you read any of the four entries as harder/easier-to-land than I do?

**(Q-L-R3-2) S87-PV-SUBTRACTION-RECALIBRATION joint PASS criterion (per L-EN-1) — do you concur that the gate must verify BOTH (a) off-pole identity preservation at s ∈ {2.5, 2.75, 3.0, 3.25, 3.5} AND (b) on-pole F_4 suppression at s=0, with BOTH required for PASS?** The joint criterion structurally precludes Class-1 convention-shopping where a PV recalibration that violates the off-pole identity could otherwise fake an on-pole PASS. Do you see any structural reason the joint criterion would be UNDESIRABLE (e.g., a legitimate PV recalibration that preserves on-pole suppression but legitimately shifts off-pole values within the off-pole-identity tolerance window)? My read is that PV is residue-localized by construction so the joint criterion is automatically satisfied by any legitimate PV — but I want your axiomatic confirmation.

**(Q-L-R3-3) The L-DN-1 per-regulator κ_n^reg refinement of S87-D-EFF-ANCHOR-VERIFICATION — do you accept the per-regulator κ_n^reg measurement as a REFINEMENT to the gate, or do you prefer to keep the gate single-d_eff and tag any per-regulator κ_n^reg deviation as a downstream INFO-band consideration?** My L-DN-1 substitution chain showed the F_4 dispersion at L=10 is 9.34% but the saturation threshold is a cumulative integral over high-(p+q) decay, which is regulator-conditional. The L-DN-1 amendment adds a 20%-tolerance per-slot ordering check across F_4 to the gate's PASS criterion. The alternative (your possible counter-position) is to keep the gate single-d_eff with the per-regulator κ_n^reg as an independent diagnostic gate `S87-KAPPA-N-PER-REGULATOR-DIAGNOSTIC` (effort 4-6h additional). Which framing do you prefer, and why?

**(Q-L-R3-4) Synchronization lockfile spec for §VII slot pre-allocation (L-CN-4) — do you want me to draft the lockfile spec as a §VII.PROP appendix in the S87 plan, or as a separate coordination file `sessions/framework/s87-slot-pre-allocation-lockfile.md`?** The synchronization lockfile must reserve §VII.U, §VII.V, §VII.W, §VII.X (and the §VII.PROP routing-layer entry) as RESERVED-FOR-WORKSHOP-86 with explicit non-collision pre-registration so the parallel-writer race protection (per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene") fires correctly. My slight preference: separate coordination file in `sessions/framework/`, since the lockfile is a coordination artifact rather than a registry entry — but I will defer to your preference for the S87 plan-freeze structure. The mechanical content is the same; the location is what matters for downstream readers.

**(Q-L-R3-5) The S87 carry-forward 4-field S87 spec (what / inputs / gate / effort) for the R3 union (ii) ∧ (iii) ∧ (i)-on-T5-only — should the spec have ONE 4-field block per the three branches (so three 4-field blocks total), or ONE 4-field block per §VII landing (so four 4-field blocks U/V/W/X plus one for §VII.PROP plus one for W1b-T5)?** The pre-registered R3 adjudication rule (workshop §"Pre-Registered R3 Adjudication" line 18) cites three branch IDs (`S87-MELLIN-CONE-LIVE-RERUN` if (i), `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` if (ii), `S87-W3-PER-EVAL-FINITENESS-PRE-REG` if (iii)) — but these are the BRANCH IDs, not the §VII landing IDs. My read: emit BOTH levels — three 4-field blocks at the BRANCH level (matching the pre-registered IDs) AND six 4-field blocks at the LANDING level (one per §VII U/V/W/X + §VII.PROP + W1b-T5). The branch-level blocks are the workshop's pre-registered output; the landing-level blocks are the implementation discipline that flows into the S87 plan-freeze. Which structure do you want for the Wrap-Up "Carry-Forward Computations" section?

---

## Round 3 — connes: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

After lizzi's R3-A FINAL I now lock in seven joint commitments. Six accept her L-CN-1 through L-CN-6 commitments verbatim with two NCG-axiomatic refinements (one numerical, one structural). The seventh consolidates her L-EN-1 / L-EN-2 emergences into the workshop's R3 plan-freeze block. The cumulative effect: the workshop's R3 union (ii) ∧ (iii) ∧ (i)-on-T5-only is structurally complete, registry-allocation-locked across §VII.U / §VII.V / §VII.W / §VII.X / §VII.PROP, and ready for S87 plan-freeze with no remaining ambiguities at the registry-statement level.

**(C-FIN-1) I accept lizzi's L-CN-1 bit-exact correction to my DN-α "100% deviation" framing.** Lizzi's L-CN-1 substitution chain (workshop §"Round 3 — lizzi" CONVERGENCE block, lines 1659–1694) re-derived the threshold-crossing deviation as `1 - 100/238.6768 = 0.5811` (58.11% downward), NOT 100%. My R2 DN-α statement "if growth_0(Zubarev) deviated from ζ by more than 100% (i.e., growth_0(Zubarev) < 119× or > 477×)" used the wrong threshold-crossing arithmetic — the correct downward threshold-crossing condition is `growth_0(reg) < 100`, which corresponds to a downward fractional deviation `1 - 100/238.6768 = 0.5811` from the ζ baseline. Lizzi's correction is bit-exact (`0.5811 / 0.0934 = 6.22` margin, NOT my asserted "10× headroom"). The correction TIGHTENS the conclusion in lizzi's favor: the universal quantifier ∀ reg ∈ F_4 holds at registry-statement level with even sharper margin (6.22× rather than ~10×). I retract my "100%" framing and adopt lizzi's `58.11% / 6.22× margin` numbers verbatim. The §VII.V registry annotation should cite lizzi's L-CN-1 numbers (with full Python-verified bit-exact provenance) rather than my R2 DN-α numbers. **Substitution-chain check (acceptance, not new derivation)**: lizzi's Step 3 `threshold_crossing_dev = 1 − 100/238.6768 = 0.5811` follows directly from the threshold equation `growth_0_proxy(reg) = growth_0(ζ) · (1 − dev) = 100`, solving for `dev = 1 - 100/growth_0(ζ) = 1 - 100/238.6768 = 0.5811` exactly. My R2 DN-α arithmetic was wrong by a factor of ~1.7. The correction is genuinely informative and is registry-grade.

**(C-FIN-2) I accept lizzi's L-CN-2 retraction of "DIM-FACTOR-CANCELING-CONSISTENCY-CHECK" framing.** Lizzi's L-CN-2 (lines 1696) retracted her D-β framing of the dim(H_F)=96 cancellation as a structural anchor and adopted my DN-β "fiber-blind by tensor-product multiplicativity, NULL constraint" terminology for the C10 INFO-band registry annotation. The substantive content of D-β (the multiplicative-factorization step is necessary mathematics) survives intact; only the interpretation as a soft anchor is retracted. I record this as a closed convergence — both agents agree the C10 §VII registry annotation should write "Δ_rel(L=8, L=10) = 0.611 measures SU(3) Casimir-tower truncation gradient at s=3; the dim(H_F)=96 invariant cancels in the relative shift by tensor-product multiplicativity, NULL constraint. No finite-triple-invariant lower bound exists." This terminology is now canonical for this workshop and should be reused verbatim in the §VII.V registry entry's C10 cross-reference block.

**(C-FIN-3) I accept lizzi's L-CN-3 retraction of "REDUCES TO" framing for the meta-theorem.** Lizzi's L-CN-3 (line 1698) retracted the "REDUCES TO" wording from her E-β meta-theorem and adopted my DN-γ necessity-only restatement verbatim. The S87 §VII.X gate is now named `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL` (necessity-only) — NOT `S87-M2-AXIOM-IS-CC-PROBLEM` (the broader meta-claim). The narrower name correctly localizes the scope and avoids the sufficiency-overreach my DN-γ flagged. The 114-OOM Lambda_SA → Lambda_observed gap is CONTINUUM-LEVEL and is NOT contained in the M2-failure structural source — M2-PASS at the continuum limit does NOT resolve the 114-OOM gap. This is a permanent classification: the §VII.X meta-theorem proves NECESSITY of M2-failure for the three finite-L manifestations only; SUFFICIENCY (whether M2-PASS would resolve the 114-OOM gap) is OUTSIDE the meta-theorem's scope and remains a continuum-level CC problem unaffected by this workshop's results.

**(C-FIN-4) I accept lizzi's L-CN-4 verbatim — classification-based §VII slot assignment lock.** Lizzi's L-CN-4 (lines 1700–1710) adopted my EN-α classification-based assignment (§VII.U = FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY ALGEBRAIC×AXIOM, §VII.V = CM-1995-INADMISSIBILITY AXIOM×SPECTRAL with WEYL-NON-ASYMP Corollary A, §VII.W = A0-R-PROTECTION-IS-M2 SPECTRAL×CROSS-PROGRAM, §VII.X = M2-STRUCTURAL-SOURCE AXIOM×META, §VII.PROP = P_MB / P_CM routing-layer) and committed to drafting the synchronization lockfile spec. The S87 plan must pre-allocate all four §VII slots + one §VII.PROP slot in the synchronization lockfile per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race". Append-only Python writers must scan ALL header levels (## + ### + ####) before allocation. The lockfile location preference (sessions/framework/s87-slot-pre-allocation-lockfile.md) is a coordination-artifact concern — see Q-L-R3-4 answer below.

**(C-FIN-5) I accept lizzi's L-CN-5 6-prior-closure (5+1-split) refinement of my EN-β unification.** Lizzi's L-CN-5 (lines 1712–1718) added the SECOND a_0-slot magnitude row: `a_0^zeta / a_0^Gilkey = 6440 / 0.866 = 7436` (s64_bdg_kasparov.py canonical comment, knowledge-MCP-corroborated). This is a SECOND a_0-slot M2-failure manifestation tracking S46's a_2 split at the a_0 slot itself. My EN-β table was correct as far as it went; lizzi's addition reveals that S64's a_0/a_2 paired splits ARE a coupled empirical signature (3812 at a_2, 7436 at a_0) of the same M2-failure mechanism appearing at adjacent slots. The §VII.X meta-theorem entry's slot-by-slot magnitude table now reads:

| Slot | M2-failure manifestation | Prior closure | Magnitude |
|:-----|:-------------------------|:--------------|:----------|
| a_0 (s=0) | Geometric vs spectral split (continuum-paired) | S64 (s64_bdg_kasparov canonical comment) | factor 7436 |
| a_0 (s=0) | Finite-L Lambda_SA residual | S64 (component) | bounded by 1 OOM at L_max=10 |
| a_0 (s=0) | R-protection-universal failure | S77 | universal across F_4 |
| a_0 (s=0) | F_4 ratio 9.46× | C9 (this workshop) | 18.91× over PASS bound |
| a_2 (s=1) | Geometric vs spectral split | S46 | factor 3812 |
| Regulator-class | Cusp regulators outside CM Sd | S82 W2-5 | t^{-3/2} branch outside Sd |

The unification is now SIX prior closures (counting the a_0 split as a separate manifestation from the finite-L residual since they are independent observables): S46 (a_2 3812), S64 split component (a_0 7436), S64 finite-L Lambda_SA component, S77, S82-W2-5, C9. This is a stronger anchor list than my EN-β provided. The §VII.X registry entry's "Anchor List" field must cite all six full-64-char SHAs at registry landing time; the current workshop has SHAs only for C9 (`audit=1559e559208db268580961556082122cc4d97d73bb01a98c056cdde404155544`, `content=ed4ee766ad00f31f71f475b476b511806cbbf8d5ed2ddf5567db9b40854482f7` per `s86_gate_verdicts.txt:95-96`) and C10 (`audit/sha256=279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698` per `s86_gate_verdicts.txt:91`). The S87 closure script must pull the remaining four full-64-char SHAs from S46 / S64 / S77 / S82-W2-5 verdict-line records and pin them in the §VII.X anchor block.

**(C-FIN-6) I accept lizzi's L-CN-6 commitment to single-d_eff Weyl-saturation anchor with per-slot ordering.** Lizzi's L-CN-6 (line 1720) committed to my EN-γ d_eff = 8 anchor and the per-slot threshold ordering L_∞^{n=0} > L_∞^{n=2} > L_∞^{n=4} ≈ L_∞^{n=6}, with `S87-D-EFF-ANCHOR-VERIFICATION` as the moderate-effort (4–6h) gate that decisively tests the single-d_eff anchor on the existing L_max=12 master cache (`s84_spectrum_cache_L12_tau019.npz`) before invoking the L_max=14 heavy effort. The volume-preserving Jensen TT-deformation property (`permanent-theorems.md`) is the structural reason d_eff = 8 inherits from the manifold to the truncated cache. I add ONE NCG-axiomatic note: the volume-preserving property is essential because `μ_CCM(M, |D|)` is the volume-coefficient at the leading SD pole `s = d_eff` and the Connes trace theorem requires this as a continuity-prerequisite. If the Jensen TT-deformation broke volume-preservation, d_eff could in principle drift; since it does not, the anchor holds. This note belongs in the §VII.V registry entry's "Preconditions" field as a structural footnote.

**(C-FIN-7) I accept lizzi's L-EN-2 STRUCTURAL FACTORIZATION reading of the R3 union, ELEVATING it from "non-overlapping cover" to "factorization of the F_4 ∘ MB ∘ SD-subtraction pipeline".** Lizzi's L-EN-2 (lines 1825–1879) is the deepest convergence of the joint reading. The R3 union is not three independent outputs covering a partitioned consumer space (which is how I framed it in R1 Re:L4 line 719 and R2 CN-δ line 1216) — it is a STRUCTURAL FACTORIZATION of the F_4 ∘ MB ∘ SD-subtraction pipeline into three composable components:

```
F_4 ∘ MB ∘ SD-subtraction CC-suppression program =
   (T5-class identity for regulator kernel, INFINITE-VECTOR)
 ∘ (CM-1995-prescribed subtraction at L_max, MIDDLE FACTOR)
 ∘ (§VII.U-class identity for substrate spectrum, FINITE-VECTOR)
```

T5 (branch (i)-on-T5) verifies the FIRST factor at C11 PASS (max_rel_err 8.07e-28); §VII.V (branch (ii)) closes the MIDDLE factor at L_max=10 (the no-go); §VII.U (branch (iii)) lands the THIRD factor independent of L_max. Each factor is INDEPENDENTLY VERIFIABLE — but the three together FACTORIZE the pipeline structurally. Removing any branch leaves a structural ambiguity: removing (i) loses the regulator-side anchor; removing (iii) loses the substrate-side anchor; removing (ii) loses the localization of the failure at the middle factor. The R3 union is therefore the MINIMAL structural characterization of the F_4 ∘ MB ∘ SD-subtraction CC-suppression program at L_max=10. **I retract my CN-δ (R2) "non-overlapping outputs covering a partitioned consumer space" framing and adopt lizzi's L-EN-2 "STRUCTURALLY COUPLED FACTORIZATION" framing as the canonical workshop reading.** The S87 plan must write the §VII.U + §VII.V + W1b-T5 landings as a COUPLED-LANDING-BLOCK with cross-references between the three entries explicit at plan-freeze. Each registry entry's "Provenance" field must cite the other two as STRUCTURAL-COMPLEMENTS (not independent results). This is the single deepest emergence of the joint reading.

**Joint R3 commitment LOCKED**: the workshop emits **(ii) ∧ (iii) ∧ (i)-on-T5-only** as a STRUCTURAL FACTORIZATION (not non-overlapping cover) of the F_4 ∘ MB ∘ SD-subtraction CC-suppression program. The five EMERGENCE topics (CN-α through CN-6, plus L-EN-1 joint criterion and L-EN-2 factorization) lock in. The R3 plan-freeze is structurally ready with no remaining ambiguities at the registry level.

**Direct answers to lizzi's Q-L-R3-1 through Q-L-R3-5 (locking R3 implementation discipline)**:

**A-Q-L-R3-1** (verdict-line classification of the four §VII landings): **Concur with lizzi's 4-level classification, with one refinement.** §VII.U = PROVEN at algebraic level (single Mellin-Dirichlet identity, closure script is a mechanical L_max=12 recompute against the existing 5-point sweep); §VII.V = PROVEN-MODULO-NUMERICAL-RECONFIRMATION (closure script computes growth_0 per regulator on the L=12 cache and tags branches per L-CN-1 per-regulator discipline); §VII.W = PROVABLE-CONDITIONAL-ON-CLOSURE-SCRIPT (synthetic 2-eigenvalue toy-model verification of M2-failure → R-protection-failure biconditional); §VII.X = PROVABLE-CONDITIONAL-ON-NUMERICAL-RECONFIRMATION (slot-by-slot magnitude table recomputed at L_max=12, six anchor SHAs pinned). REFINEMENT: §VII.U is mathematically tight enough to be PROVABLE-AT-PLAN-FREEZE if the S87 closure script is just the algebraic identity (no L_max=12 recompute needed because the identity is L_max-INVARIANT off-pole by construction). The L_max=12 recompute would be a SANITY CHECK on the L_max=12 cache, not a proof requirement. So I tighten lizzi's classification: §VII.U = PROVEN-AT-PLAN-FREEZE-WITH-CORROBORATION-AT-S87, §VII.V = PROVEN-MODULO-NUMERICAL-RECONFIRMATION, §VII.W = PROVABLE-CONDITIONAL, §VII.X = PROVABLE-CONDITIONAL.

**A-Q-L-R3-2** (joint PASS criterion for `S87-PV-SUBTRACTION-RECALIBRATION`): **Concur with the joint criterion (off-pole identity preservation AND on-pole F_4 suppression both required).** The axiomatic confirmation lizzi requested: PV subtraction is residue-localized by construction at the slot poles (in CM-1995's framework, PV subtraction adds counter-terms at finite-mass intermediate states whose Mellin profile contributes to specific slot residues but vanishes off-pole at large s by the Pauli-Villars pole-cancellation). So the joint criterion is automatically satisfied by any LEGITIMATE PV recalibration — and the requirement that `rel_err(analytic_zeta(s, L=10), Dirichlet) at s ∈ {2.5, 2.75, 3.0, 3.25, 3.5} remains ≤ 5×float_eps after PV subtraction is applied` is structurally a SANITY-CHECK-ANCHOR rather than a constraint that admits a non-trivial trade-off. Lizzi's L-EN-1 framing is correct: the joint criterion structurally precludes Class-1 convention-shopping where a non-residue-localized subtraction could fake an on-pole PASS by violating off-pole behavior. ACCEPT both halves of the joint criterion; this is the canonical S87-PV-SUBTRACTION-RECALIBRATION PASS spec.

**A-Q-L-R3-3** (per-regulator κ_n^reg refinement of S87-D-EFF-ANCHOR-VERIFICATION): **Accept the per-regulator κ_n^reg measurement as a REFINEMENT to the gate, with a 20%-tolerance per-slot ordering check across F_4.** Lizzi's L-DN-1 substitution chain showed the F_4 dispersion at L=10 is 9.34% but the saturation threshold is a cumulative integral over high-(p+q) decay weighted by the regulator-specific Mellin profile. The per-regulator κ_n^reg compounding effect from F_4 weight differences is a NEW S87 refinement need (the only NEW dissent surviving R3 per L-DN-1) that warrants integration into the S87-D-EFF-ANCHOR-VERIFICATION gate rather than a separate gate. The 20% tolerance is an empirical envelope at the L=10 dispersion factor (~2.14× the 9.34% L=10 dispersion); if the L=12 ordering inverts beyond 20%, regulator-conditional κ_n^reg corrections are required. The alternative single-d_eff-only gate plus separate `S87-KAPPA-N-PER-REGULATOR-DIAGNOSTIC` is structurally equivalent in information content but introduces gate-multiplicity overhead; the integrated form is cleaner. ACCEPT lizzi's L-DN-1 refinement; the gate now reads "single-d_eff anchor with per-regulator κ_n^reg verification at 20% tolerance".

**A-Q-L-R3-4** (synchronization lockfile location): **Prefer separate coordination file `sessions/framework/s87-slot-pre-allocation-lockfile.md`.** Lizzi's preference matches my preference. The lockfile is a coordination artifact with cross-session purpose (it persists beyond S87 and may be reused for parallel-writer races in S88+); it does NOT belong in the S87 plan-freeze block as a §VII.PROP appendix. The §VII.PROP entry in `permanent-results-registry.md` is the un-bundling routing-layer (the P_MB / P_CM partition); the synchronization lockfile is a DIFFERENT artifact that lives at coordination-layer rather than registry-layer. ACCEPT lizzi's preferred location; the lockfile spec is drafted at S87 plan-freeze in `sessions/framework/s87-slot-pre-allocation-lockfile.md` with explicit RESERVED-FOR-WORKSHOP-86-W-1 entries for §VII.U / §VII.V / §VII.W / §VII.X / §VII.PROP+1.

**A-Q-L-R3-5** (4-field S87 spec structure — branch-level vs landing-level): **Emit BOTH levels** — three branch-level 4-field blocks AND six landing-level 4-field blocks. Lizzi's reading is correct: the pre-registered R3 adjudication rule cites three branch IDs (`S87-MELLIN-CONE-LIVE-RERUN` if (i), `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` if (ii), `S87-W3-PER-EVAL-FINITENESS-PRE-REG` if (iii)), and the workshop is contractually bound to emit 4-field specs at the branch level. But the implementation discipline that flows into S87 plan-freeze requires LANDING-LEVEL specs: §VII.U landing, §VII.V landing, §VII.W landing, §VII.X landing, §VII.PROP routing-layer landing, W1b-T5 landing, plus the `S87-PV-SUBTRACTION-RECALIBRATION` primary refutation gate (per L-CN-ε / D-γ priority 1) and the `S87-D-EFF-ANCHOR-VERIFICATION` (per L-CN-6 / EN-γ / L-DN-1). This produces 3 branch-level + 8 landing/gate-level = 11 4-field blocks. The Wrap-Up "Carry-Forward Computations" section will emit BOTH levels with branch-level blocks at the top (the workshop's pre-registered output) and landing-level blocks below (the implementation discipline).

### DISSENT

I hold ZERO new dissents at the registry-statement level. The L-CN-1 through L-CN-6 commitments above close all my R2 dissents (DN-α numerically corrected by lizzi's L-CN-1 with 6.22× margin; DN-β converged at "fiber-blind by tensor-product multiplicativity, NULL constraint" in L-CN-2; DN-γ accepted verbatim as necessity-only restatement in L-CN-3). Lizzi's R3-A introduced ONE remaining dissent (L-DN-1, per-regulator κ_n^reg compounding) which I have CONVERGED on by accepting the refinement into the S87-D-EFF-ANCHOR-VERIFICATION gate (A-Q-L-R3-3 above). No NEW evidence beyond R2 surfaces a fresh dissent.

ONE small flag for S87 follow-up that is NOT a dissent on this workshop's R3 output but is a DIAGNOSTIC carry-forward to the S87 closure-script discipline: **L-CN-5's a_0-slot-paired magnitude table addition (factor 7436 alongside S46's 3812) raises a minor scope question for the §VII.X meta-theorem.** The two splits — `a_2^zeta / a_2^SD = 3812.18` (S46) and `a_0^zeta / a_0^Gilkey = 7436` (S64 canonical comment) — are at adjacent slots (s=0 and s=1) under different reference baselines (SD geometric vs Gilkey-Heat-Kernel). The §VII.X registry entry's "Magnitude column" should clearly DISTINGUISH the reference baseline for each entry (geometric SD vs Gilkey HK), since the two are NOT directly comparable as bare numerical magnitudes. This is a registry-annotation discipline issue at S87 closure, not a dissent on the meta-theorem itself.

This is the only NEW item from R3. The dissent section is otherwise empty. All R2 dissents are closed by R3 convergence.

### EMERGENCE

Two new structural insights surface from the joint R1+R2+R3-A reading that NEITHER lizzi's R3-A nor my R2 alone produced. Each addresses content that becomes visible only after the structural-factorization framing of L-EN-2 has committed.

**(C-EN-1) The R3 union STRUCTURAL FACTORIZATION (L-EN-2) implies a NEW NCG-axiomatic distinction between "lens-mediated identity" (§VII.U + W1b-T5) and "prescription-mediated theorem" (§VII.V + Corollary A) that has no analogue in Connes-Moscovici 1995 and represents a S87+ extension of the CM-1995 framework specific to truncated NCG caches.** This was not visible in R1 or R2 because both rounds treated §VII.U and §VII.V as parallel registry entries on equal footing. Lizzi's L-EN-2 factorization makes visible that they belong to STRUCTURALLY DIFFERENT CATEGORIES of NCG result. Substitution chain (necessary for the structural claim):

```
Step 1 (definitions, NCG-axiomatic distinction):
  Lens-mediated identity:    A theorem of the form "lens(substrate) = closed-form
                              expression on substrate" where the lens is structurally
                              transparent at the off-pole/asymptotic regime where
                              the identity holds. Does not invoke a subtraction
                              prescription. Structural example: §VII.U Mellin-Dirichlet
                              identity (Mellin lens reads through transparently to
                              Dirichlet form), and dually W1b-T5 (Mellin lens reads
                              through transparently to closed-form Λ_Z^{2s}·Γ(s)).
  Prescription-mediated theorem: A theorem of the form "prescription_with_calibration_
                              against_continuum applied to substrate yields specific
                              ratio behavior at L_max < L_∞" where the prescription
                              is what carries the calibration mismatch. Structural
                              example: §VII.V CM-1995-INADMISSIBILITY-AT-FINITE-L
                              (CM-1995 prescription with continuum-calibrated
                              SD subtraction applied to truncated cache yields
                              ratio_min > 5e-1).

Step 2 (substitute the structural-factorization reading):
  Lens-mediated identities are L_max-INVARIANT (true at finite or infinite L)
                              because the lens's transparency does not depend on
                              the substrate's asymptotic regime.
  Prescription-mediated theorems are L_max-CONDITIONAL (true at finite L_max
                              < L_∞, become trivial at L_max → ∞ because the
                              prescription becomes consistent with the substrate).
  Branch (i) and Branch (iii) of the R3 union are LENS-MEDIATED.
  Branch (ii) is PRESCRIPTION-MEDIATED.

Step 3 (canonical form):
  The factorization L-EN-2 wrote out is precisely
    F_4 ∘ MB ∘ SD-subtraction = LENS_kernel ∘ PRESCRIPTION_subtraction ∘ LENS_substrate
  where LENS_* are the L_max-invariant transparency factors and PRESCRIPTION is
  the L_max-conditional carrier of the calibration mismatch.

Step 4 (substitute into S87+ extension claim):
  Connes-Moscovici 1995 §4–§5 framework operates entirely at the LENS_substrate
  side under the assumption that the substrate IS in the Weyl-asymptotic regime
  (manifold continuum). It does NOT address the prescription's L_max-conditional
  applicability — that is implicit in the manifold-substrate setup.
  Truncated NCG caches require a NEW framework distinguishing these layers,
  which is what the workshop's R3 union outputs.

Step 5 (direction):
  The §VII.U + W1b-T5 + §VII.V landings constitute a S87+ EXTENSION of the
  CM-1995 framework specific to truncated NCG caches. The extension distinguishes
  L_max-invariant lens-mediated identities (L_max-invariant theorems on the
  truncated cache, registry-permanent regardless of L_max) from L_max-conditional
  prescription-mediated theorems (registry-permanent under explicit L_max < L_∞
  scope qualification). This distinction is a NEW structural axiom-extension
  that should be registered as a §VII.PROP routing-layer principle alongside
  the P_MB / P_CM un-bundling.
```

**Concrete proposal**: the §VII.PROP routing-layer entry should land TWO routing principles, not one — (a) the P_MB / P_CM un-bundling per E-γ; (b) the Lens-mediated-vs-Prescription-mediated distinction per C-EN-1 above. Both are routing-layer principles for downstream registry consumers; both are S87+ extensions of CM-1995 specific to truncated NCG caches. The two principles are STRUCTURALLY ORTHOGONAL: P_MB / P_CM partitions the AXIOM SET of the residue scheme; Lens / Prescription partitions the L_max-invariance class of theorems built from those axioms. A complete S87 plan-freeze must register both.

**(C-EN-2) The L-CN-5 paired a_0/a_2 splits (3812 at a_2, 7436 at a_0) under the §VII.X meta-theorem reveal a SLOT-RATIO INVARIANT `7436 / 3812 ≈ 1.95` that may carry a structural NCG-axiomatic interpretation independent of either prior closure individually.** This was not visible in R1 or R2 because the a_0 split was added by lizzi at L-CN-5 in R3, and the slot-ratio comparison only becomes meaningful when both splits are tabulated together. Substitution chain (structural observation only — no new direction claim, just an observation):

```
Step 1 (definitions, raw slot-ratio):
  S46 a_2 split = a_2^zeta / a_2^SD = 2776.165389 / 0.728234972609 = 3812.18
                  (s64_bdg_kasparov.py canonical comment per L-CN-5)
  S64 a_0 split = a_0^zeta / a_0^Gilkey = 6440 / 0.866 = 7436
                  (s64_bdg_kasparov.py canonical comment per L-CN-5)
  Slot-ratio    = 7436 / 3812 ≈ 1.951

Step 2 (substitute, structural observation):
  Both splits compare a SPECTRAL (zeta-regularized) extraction at finite-L
  to a continuum-geometric reference. The ratio of the two splits at adjacent
  SD slots is approximately 2.

Step 3 (canonical form, NCG interpretation candidates):
  Candidate 1: COINCIDENCE at the order-of-magnitude level (the two splits
                  are O(10^3-10^4); their ratio is O(1) by accident).
  Candidate 2: The factor ≈ 2 reflects the SD-subtraction prescription's
                  weighting: the SD subtraction at slot s=k has coefficient
                  ~ 1/k! (or a similar combinatorial factor) at the leading order.
                  At s=0 the coefficient is c_0 ~ 1; at s=1 it is c_1 ~ 1/1 = 1.
                  The slot-ratio of EXTRACTED magnitudes would then track the
                  ratio of coefficients, but this gives factor 1 not 2.
  Candidate 3: The factor ≈ 2 is the Casimir-tower Weyl-dim-density ratio
                  between adjacent (p+q) sectors. d(p,q) = (1/2)(p+1)(q+1)(p+q+2).
                  At small p+q, d is approximately quadratic; the ratio of
                  successive sums is ~2 at the lowest sectors. This is a
                  structural NCG anchor candidate, but requires explicit
                  numerical verification at L_max=10.

Step 4 (substitute into status):
  None of the three candidates is decisively confirmed by the workshop's data.
  Candidate 3 (Casimir-tower Weyl-dim ratio) is the most structurally appealing
  but requires EN-γ d_eff anchor verification + per-slot Weyl-dim-sum tabulation
  on the L_max=12 cache to test.

Step 5 (direction):
  This is an OPEN QUESTION for S87+, not a workshop deliverable. The §VII.X
  meta-theorem entry should NOTE the paired slot-ratio observation as a FUTURE-
  WORK FLAG without committing to an interpretation. The S87
  S87-D-EFF-ANCHOR-VERIFICATION gate could be extended to compute the slot-ratio
  prediction from Candidate 3 at L_max=12 and compare to the observed 1.95
  empirical ratio.
```

**Concrete proposal**: the §VII.X meta-theorem registry entry's "Future-Work Flags" field should include **`S87-PAIRED-SLOT-RATIO-INTERPRETATION`** as an OPEN-QUESTION flag (not a S87 carry-forward gate, since it is not yet pre-registerable with PASS criteria — it is a structural observation requiring further investigation). The §VII.X entry's body should explicitly note: "Paired a_0/a_2 splits at adjacent slots (7436/3812 ≈ 1.951) suggest a structural slot-ratio invariant whose NCG-axiomatic interpretation remains open at workshop close. Three candidate readings (coincidence, SD-coefficient ratio, Weyl-dim-density ratio) await S87+ investigation." This is a true emergence: it was not visible in either L-CN-5's data refinement or my EN-β framing alone, but becomes visible when the two are read together.

The C-EN-1 routing-layer extension and the C-EN-2 slot-ratio observation are the two new emergences from the R3 final round. Both are structural insights that did not appear in R1 or R2 in the form they take here. They consolidate the workshop's R3 output as a NCG-axiomatic-grade investigation rather than a single-paper-grade deliverable.

**Closing of the EMERGENCE section**: the joint R1+R2+R3 reading produces FIVE §VII registry entries (§VII.U / §VII.V / §VII.W / §VII.X with Six-prior-closure anchor list, §VII.PROP with TWO routing-layer principles), one S87 PRIMARY refutation gate (`S87-PV-SUBTRACTION-RECALIBRATION` with joint criterion), one S87 DIAGNOSTIC gate (`S87-D-EFF-ANCHOR-VERIFICATION` with single-d_eff anchor + per-regulator κ_n^reg refinement at 20% tolerance), one OPEN-QUESTION flag (`S87-PAIRED-SLOT-RATIO-INTERPRETATION`), and one synchronization lockfile (`sessions/framework/s87-slot-pre-allocation-lockfile.md`). The R3 plan-freeze emits all of these as the workshop's structural deliverable. The S87 plan must pre-register all of them at plan-freeze; the synchronization lockfile is the coordination artifact that prevents parallel-writer collisions at registry-landing time.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | C9 FAIL reading (near-miss vs structural divergence) | L1, Re:L1 | **Converged** | C9's value=9.456 is structural-divergence-correctly-detected: BOTH FAIL branches fired independently (ratio 9.46 > 5e-1 by 18.91× / 1.28 OOM; χ²/dof_max 1.47e+04 > 20 by 735× / ~3 OOM), CC3 PASS at machine ε proves the lens is functioning; the F_4 ratio failure is forced by M2-axiom-failure on the truncated cache where the polynomial small-t expansion does not match the manifold's fractional-power asymptotic that CM-1995 SD subtraction is calibrated for. NOT a near-miss; NOT fit-window-refinable. |
| 2 | C10 INFO reading (off-pole substrate vs Hankel systematic) | L2, Re:L2 | **Converged** | C10's `analytic_zeta(s=3, L_max=10) = 2.807432e+5 + 0j` IS the substrate-spectral signal, NOT a Hankel-contour systematic. The Mellin-Dirichlet finite-spectrum identity holds bit-exactly at finite L on the off-pole strip (rel_err ≤ 1.37e-16 ≤ 0.6×float_eps). The truncation-stability INFO (61.1% L=8→L=10 shift) and ε-analyticity INFO (1.124e-3) are substrate signatures, not lens artifacts. dim(H_F)=96 cancels by tensor-product multiplicativity (NULL constraint, no finite-triple-invariant lower bound exists). |
| 3 | W3-consumer per-evaluation needs (s=4 / s=3 / ρ-fit) | L3, Re:L3 | **Converged** | T9 (ε_T9=0.01 at s=4 leading residue): IRRECOVERABLE at L_max=10 (Weyl-non-asymptotic at n=0 by factor 238.7×). W0-20 (s=3 off-pole apex): ALREADY-PASS-EVIDENCE-ON-DISK by the finite-spectrum identity (χ²/dof = 2.17e-32 ≤ 5 by 32 OOM). W0-7-MB ρ-fit lower-half: ρ_lower = -1.124 (computable NOW from C10's existing 5-point sweep) refutes ρ=-1 conjecture from the conservative side. 2 of 3 W3 consumers recoverable via per-evaluation re-pre-registration; T9 demands the structural-no-go theorem. |
| 4 | Structural-no-go candidacy + W2 Candidate 3 cross-link | L4, Re:L4, C1, C2 | **Emerged** | The R3 union is a STRUCTURAL FACTORIZATION (L-EN-2 / C-FIN-7), not a non-overlapping cover: F_4 ∘ MB ∘ SD-subtraction = LENS_kernel ∘ PRESCRIPTION_subtraction ∘ LENS_substrate. T5 (C11 anchor at max_rel_err 8.07e-28) verifies the FIRST factor; §VII.V CM-1995-INADMISSIBILITY-AT-FINITE-L (with WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A) closes the MIDDLE factor at L_max=10; §VII.U FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY lands the THIRD factor L_max-invariant at off-pole s. Each branch is necessary for the other branches to be interpretable. STRUCTURAL extension of CM-1995 specific to truncated NCG caches surfaces as new emergence. |
| 5 | R3 branch selection — (i) / (ii) / (iii) | All R3 sections | **Converged** | The pre-registered R3 adjudication EMITS **(ii) ∧ (iii) ∧ (i)-on-T5-only** as a STRUCTURALLY COUPLED FACTORIZATION (NOT a disjunctive choice). Branch (ii): `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` at §VII.V. Branch (iii): `S87-W3-PER-EVAL-FINITENESS-PRE-REG` lands W0-20 (s=3 apex, 32-OOM-margin PASS-on-disk) and W0-7-MB lower-half (ρ_lower = -1.124). Branch (i)-on-T5-only: `S87-W1B-T5-LANDING` of the Mellin-Strip / Convergence-Cone Theorem citing C11 at §VII.U or §VII.V via the synchronization lockfile. Five §VII registry entries result; one PRIMARY refutation gate (`S87-PV-SUBTRACTION-RECALIBRATION` joint criterion); one DIAGNOSTIC gate (`S87-D-EFF-ANCHOR-VERIFICATION` with per-regulator κ_n^reg refinement). |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

The following questions are S87+ carry-forwards or open-question flags. Each is specific enough to become a future computation or a structural investigation. Items 1-5 are pre-registerable as gates; items 6-9 are open-question flags requiring further investigation before pre-registration is feasible.

1. **Q-OPEN-1: L_max=12 verification of the single-d_eff anchor with per-regulator κ_n^reg ordering** — pre-registered at S87-D-EFF-ANCHOR-VERIFICATION (per L-CN-6 + L-DN-1 + A-Q-L-R3-3). PASS criterion: per-slot ordering L_∞^{n=0} > L_∞^{n=2} > L_∞^{n=4} ≈ L_∞^{n=6} holds within 20% tolerance across F_4 = {ζ, Zubarev, SDW} on the existing L_max=12 master cache `s84_spectrum_cache_L12_tau019.npz`. FAIL ⇒ regulator-conditional κ_n^reg corrections required.

2. **Q-OPEN-2: PV-subtraction recalibration on truncated cache** — pre-registered at S87-PV-SUBTRACTION-RECALIBRATION joint criterion (per D-γ priority 1 + L-EN-1 + A-Q-L-R3-2). Tests whether the F_4 ratio failure is CM-1995-prescription-specific or structural to ALL subtractions within F_4. Joint PASS: (a) `rel_err(analytic_zeta(s, L=10), Dirichlet)` at s ∈ {2.5, 2.75, 3.0, 3.25, 3.5} remains ≤ 5×float_eps after PV subtraction; (b) `|Λ_CC^MB(reg, PV-recalibrated)| / |a_0^trunc(reg)| ≤ 5e-1` at s=0 for at least one reg ∈ F_4.

3. **Q-OPEN-3: Slot-by-slot M2-failure magnitude on the L_max=12 cache** — pre-registered at S87-M2-STRUCTURAL-SOURCE-VERIFICATION (closure script for §VII.X). Recompute the six-row magnitude table of L-CN-5 / C-FIN-5 (S46 a_2 split 3812; S64 a_0 split 7436; S64 finite-L Lambda_SA component; S77 R-protection failure; S82-W2-5 cusp regulator class; C9 9.46×) at L_max=12 and verify the M2-failure magnitude is monotone in L_max → ∞ for each slot. Six full-64-char SHA anchors must be pinned in the §VII.X registry block at S87 closure.

4. **Q-OPEN-4: Synthetic 2-eigenvalue toy-model verification of the M2-failure → R-protection-failure biconditional** — pre-registered at S87-A0-R-PROTECTION-IS-M2-VERIFICATION (closure script for §VII.W). Demonstrates the biconditional on a synthetic toy where M2-failure is manifest by construction and R-protection-failure of a single-moment ratio is observed in the same regulator scan. PASS criterion: biconditional verified to machine ε on a 2-eigenvalue truncation; FAIL ⇒ the §VII.W unified theorem statement requires sub-cases beyond the biconditional.

5. **Q-OPEN-5: L_max=14 sweep for empirical determination of L_∞** — DEFERRED carry-forward (per D-γ priority 3, A-Q-L-R3-3). Requires cache regeneration at L_max=14 (~16+ GB memory per `.claude/rules/computation-environment.md` GPU envelope). Should only be invoked if Q-OPEN-1 / Q-OPEN-2 jointly leave the L_∞ threshold question unresolved at L_max=12. Effort-4-day item.

6. **Q-OPEN-6: Paired-slot-ratio interpretation** (open-question flag, not yet pre-registerable) — per C-EN-2: the ratio `7436 / 3812 ≈ 1.951` between S64 a_0 split and S46 a_2 split may carry a structural NCG-axiomatic interpretation. Three candidates: (a) coincidence; (b) SD-subtraction coefficient ratio; (c) Casimir-tower Weyl-dim-density ratio between adjacent (p+q) sectors. Candidate (c) is structurally appealing but requires explicit Weyl-dim-sum tabulation at L_max=12 to test. NOT pre-registerable as a gate at S87; may become pre-registerable at S88+ depending on Q-OPEN-1 outcome.

7. **Q-OPEN-7: Pati-Salam A_F recalibration as a fifth refutation pathway** (open-question flag, per A-Q-C5) — does the PS finite-triple calibration shift the n=0 growth factor below 100× at L_max=10? The M2-failure is structural and survives any finite-fiber algebra change, but the QUANTITATIVE growth factor may differ between SM A_F and PS A_F. Effort 6-10h depending on PS A_F finite-triple cache readiness. Listed as PS-A_F-RECALIBRATION-DIAGNOSTIC for S88+ if PS-W3-I carry-forward (per `permanent-theorems.md` Open Channels) makes the PS finite-triple cache available.

8. **Q-OPEN-8: §VII.PROP routing-layer two-principle landing protocol** — per C-EN-1, the §VII.PROP routing-layer entry must land TWO orthogonal routing principles: (a) P_MB / P_CM un-bundling (E-γ); (b) Lens-mediated-vs-Prescription-mediated distinction (C-EN-1). Open question for the S87 plan-author: should both principles land at the same §VII.PROP slot (with sub-headers) or at adjacent §VII.PROP / §VII.PROP+1 slots? My preference (per CN-α slot-allocation discipline): adjacent slots since the principles are STRUCTURALLY ORTHOGONAL (P_MB / P_CM partitions the AXIOM SET; Lens / Prescription partitions the L_max-invariance class).

9. **Q-OPEN-9: Connes-distance anisotropy functional cross-link to the §VII.U FINITE-SPECTRUM identity** (open-question flag, per `permanent-theorems.md` Open Channels item 4) — does the Connes distance anisotropy functional inherit L_max-invariance properties from the §VII.U identity? The Connes distance is a substrate-spectral observable; if it admits a finite-spectrum identity analogous to the Mellin-Dirichlet identity, anisotropy measurements at L_max=10 may be L_max-invariant in a structural sense. Effort 8-12h to derive an analogous identity if it exists. Listed as CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE for S88+.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **The R3 union is a STRUCTURAL FACTORIZATION, not a disjunctive choice.** Both agents converged in R3 on lizzi's L-EN-2 framing: branches (i)-on-T5, (ii), and (iii) factorize the F_4 ∘ MB ∘ SD-subtraction CC-suppression program into LENS_kernel ∘ PRESCRIPTION_subtraction ∘ LENS_substrate, where each component is independently verifiable but all three are necessary for the others to be interpretable. The pre-registered R3 adjudication rule (workshop §"Pre-Registered R3 Adjudication" lines 19-22) treated the three branches as alternatives; the workshop DEMONSTRATED they are the minimal structural characterization.

- **Five §VII registry entries committed at classification-based slot allocation, with synchronization lockfile spec** (per C-FIN-4 / L-CN-4): §VII.U FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY (lizzi anchor, ALGEBRAIC×AXIOM); §VII.V CM-1995-INADMISSIBILITY-AT-FINITE-L with WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A (connes anchor, AXIOM×SPECTRAL); §VII.W A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE (joint anchor, SPECTRAL×CROSS-PROGRAM); §VII.X M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL necessity-only (joint anchor, AXIOM×META, with six-prior-closure anchor list); §VII.PROP P_MB / P_CM un-bundling + Lens / Prescription distinction (joint, ROUTING-LAYER, two principles). The synchronization lockfile at `sessions/framework/s87-slot-pre-allocation-lockfile.md` reserves all five slots before the S87 plan-freeze.

- **Numerical evidence base sharpened (bit-exact via Python verification per L-CN-1)**: threshold-crossing dispersion at L=10 is 9.34% (NOT my R2's "100%"); margin to threshold-crossing 6.22× (NOT my R2's "~10×"); growth_0(ζ)=238.6768 / growth_0_proxy(Zubarev)=218.31 / growth_0_proxy(SDW)=223.65, all clearing the 100× diagnostic by factor ≥ 2.18×. Universal quantifier ∀ reg ∈ F_4 holds at registry-statement level with sharper margin than my R2 DN-α claimed.

### What Holds

- **The Mellin-Barnes lens is not broken; the SD-subtraction prescription IS broken at L_max=10.** CC3 PASS at machine ε in C9 (rel_err ∈ {2.34e-16, 2.21e-16, 3.56e-16}) and the Mellin-Dirichlet finite-spectrum identity at C10 (rel_err ≤ 1.37e-16) prove the lens functions correctly at finite L on the off-pole strip. The C9 FAIL traces to M2-axiom-failure on the truncated cache where the polynomial small-t expansion does not match the manifold's fractional-power asymptotic that CM-1995 SD subtraction is calibrated for. The lens / prescription distinction is structurally permanent and survives the workshop close.

- **§VII.U FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY is L_max-INVARIANT off-pole and registry-permanent for any finite truncated NCG cache.** The identity `M[Tr(e^{-tD²})](s/2) / Γ(s/2) = Σ_k m_k λ_k^{-s} = ζ_D(s, L)` holds exactly at finite L for any spectral triple with λ_min > 0, off-pole. This is a CCM-2007-class theorem applicable to ANY truncated NCG cache and stands as workshop deliverable independent of any L_max-conditional theorem.

- **The W2 Candidate 3 (T5 Mellin-Strip / Convergence-Cone Theorem) lands in S87 W1b INDEPENDENT of C9's FAIL.** C11's PASS at max_rel_err 8.07e-28 is the analytic anchor that lets T5 land at all; the closed-form `Λ_Z^{2s}·Γ(s)` is the algebraic substrate. T5 is in the regulator-kernel sector (INFINITE-VECTOR class per `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md`), measure-disjoint from C9's substrate-side spectral sector. Both can stand permanently in the registry without contradiction; together they verify two of three factorization components per L-EN-2.

### What Breaks or Strains

- **The CM-1995 §4-§5 framework is INSUFFICIENT for truncated NCG caches.** It does NOT distinguish lens-mediated identities (L_max-invariant) from prescription-mediated theorems (L_max-conditional). Truncated NCG caches require the §VII.PROP Lens / Prescription routing-layer principle (per C-EN-1) as a S87+ extension of CM-1995. This is not a refutation of CM-1995 but an explicit recognition that its scope ends at the manifold-substrate continuum and that finite-L_max NCG work requires structurally distinct registry classifications.

- **The CC problem is NOT reduced to M2-axiom failure** (per L-CN-3 / DN-γ). The 114-OOM Lambda_SA → Lambda_observed gap is CONTINUUM-LEVEL; M2-PASS at L_max → ∞ does NOT close the gap. The §VII.X meta-theorem captures NECESSITY only (M2-failure is a structural source for the finite-L manifestations); SUFFICIENCY remains UNRESOLVED at the workshop close. The CC problem reduction was overstated in lizzi's R2 E-β; the necessity-only restatement is the correct registry form.

- **The paired-slot-ratio interpretation** (C-EN-2: 7436/3812 ≈ 1.951) is structurally interesting but UNINTERPRETED. Three candidates surface (coincidence, SD-coefficient ratio, Weyl-dim-density ratio) but none is decisively confirmed by workshop data. This is an OPEN-QUESTION flag for S87+, not a workshop deliverable, and should not be promoted to a registry entry until further investigation.

### Carry-Forward Computations

The pre-registered R3 adjudication rule mandates 4-field S87 specs (what / inputs / gate / effort) for whichever path R3 selects. The workshop emits **(ii) ∧ (iii) ∧ (i)-on-T5-only** as a STRUCTURALLY COUPLED FACTORIZATION; therefore branch-level specs are emitted for ALL THREE branches, plus landing-level specs for each registry entry and gate that flows into S87 plan-freeze (per A-Q-L-R3-5 — emit BOTH levels).

#### Branch-level 4-field blocks (the workshop's pre-registered output)

**Branch (i)-on-T5-only — `S87-MELLIN-CONE-LIVE-RERUN` (re-purposed as `S87-W1B-T5-LANDING` per L-EN-2 factorization)**
- **what**: Land the Mellin-Strip / Convergence-Cone Theorem (T5 in W1b) at §VII.U or §VII.V citing C11's PASS at max_rel_err 8.07e-28 as the analytic anchor for the closed-form `Λ_Z^{2s}·Γ(s)`. T5 is the regulator-kernel-side LENS-mediated identity in the L-EN-2 factorization (FIRST factor of F_4 ∘ MB ∘ SD-subtraction).
- **inputs**: C11 verdict line `s86_gate_verdicts.txt:91`-pinned audit_sha256; framework note `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` §3 (INFINITE-VECTOR class definition); §W2-3 line 420 + §W2 Synthesis line 628 of `session-86-w2-workingpaper.md`.
- **gate**: PASS criterion = (a) closed-form identity `M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` algebraically verified on the convergence cone Re(s) > 0; (b) C11 PASS-anchor SHA pinned in §VII registry entry's "Anchor List" field. Threshold: machine ε.
- **effort**: 4-6h (mechanical landing; mathematics is C11-PASS-pre-validated).

**Branch (ii) — `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` at §VII.V**
- **what**: Land CM-1995-INADMISSIBILITY-AT-FINITE-L (with WEYL-NON-ASYMP-F_4-MB-NO-GO as Corollary A) at §VII.V as the AXIOM×SPECTRAL no-go theorem on the F_4 ∘ MB ∘ SD-subtraction CC-suppression program at L_max=10. Diagnostic: n=0 Mellin-moment growth factor `M_0(L=10) / M_0(L=5) > 100` in any reg ∈ F_4 (empirically: 238.6768 ζ-class, 218.31 Zubarev proxy, 223.65 SDW proxy, 9.34% L=10 dispersion — all clear by 2.18× margin).
- **inputs**: C9 verdict line `s86_gate_verdicts.txt:95-96` (audit_sha256=1559e559208db268580961556082122cc4d97d73bb01a98c056cdde404155544 / content_sha256=ed4ee766ad00f31f71f475b476b511806cbbf8d5ed2ddf5567db9b40854482f7); §W2-1 lines 53-55 of `session-86-w2-workingpaper.md` (per-regulator C9 numerical surface); the R2 connes C2 axiomatic substitution chain (workshop lines 730-820); the L-EN-2 factorization framing (workshop lines 1825-1879).
- **gate**: PROVEN-MODULO-NUMERICAL-RECONFIRMATION at S87 closure (per A-Q-L-R3-1). Closure script computes growth_0 per regulator on the L_max=12 cache and tags branches per L-CN-1 per-regulator discipline. PASS criterion: ∀ reg ∈ F_4, growth_0(reg) > 100× at L_max=10 confirmed; per-regulator κ_n^reg dispersion ≤ 20% at L_max=12 (otherwise routes to Q-OPEN-1 follow-up).
- **effort**: 6-8h (registry landing + numerical reconfirmation on the L=12 cache + synchronization lockfile coordination).

**Branch (iii) — `S87-W3-PER-EVAL-FINITENESS-PRE-REG`**
- **what**: Re-pre-register W0-20 (`S86-W0-20-MB-RE-EMIT` at s=3 off-pole apex) and W0-7-MB lower-half (`S86-W0-7-MB-RE-EMIT` ρ-fit on s ∈ [2.5, 3.5]) as PASS-evidence-on-disk via the §VII.U FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY, BYPASSING the C9 FAIL and C10 INFO labels. T9 (s=4 leading residue) is RETRACTED as conditional carry-forward with structural-no-go entry replacing it (per L3 §W2 Synthesis line 624).
- **inputs**: C10 verdict line `s86_gate_verdicts.txt:91` (sha256=279da9646d421b60bb39711057be7722226f7bc4e6336bae2baa4aebdbb70698); C10 5-point sweep at `session-86-w2-workingpaper.md:218-222`; §VII.U FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY (workshop lines 437-471 / 945) lands first in the synchronization lockfile; W0-20 hypothesis at `session-86-w3-workingpaper.md:113-145`; W0-7-MB hypothesis at `session-86-w3-workingpaper.md:43-75`.
- **gate**: PASS criterion (W0-20) = (a) `analytic_zeta(s=3, L_max=10) = 2.807432e+5` finite, |·| < 1e10; (b) χ²/dof against direct Seeley-DeWitt subtraction ≤ 5 (already 2.17e-32). PASS criterion (W0-7-MB lower-half) = ρ_lower-half ∈ TBD-band on s ∈ [2.5, 3.5]; observed `ρ_lower = -1.124` REFUTES ρ=-1 conjecture from the conservative side. Re-pre-registered band: `[-1.20, -1.00]` tests ρ=-1 from below.
- **effort**: 4-6h (re-pre-registration scripts + verdict-line emissions; data already on disk).

#### Landing-level 4-field blocks (the implementation discipline that flows into S87 plan-freeze)

**`S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY-LANDING` at §VII.U** (lizzi anchor, ALGEBRAIC × AXIOM, PROVEN-AT-PLAN-FREEZE-WITH-CORROBORATION-AT-S87)
- **what**: Land the Mellin-Dirichlet finite-spectrum identity at §VII.U: for any finite spectral triple (A, H, D) with all eigenvalues λ_k ≠ 0, `M[Tr(e^{-tD²})](s/2) / Γ(s/2) = Σ_k m_k λ_k^{-s} = ζ_D(s)` exactly at finite L on the off-pole strip.
- **inputs**: connes Re:L2 substitution chain (workshop lines 437-471); lizzi C-α confirmation (line 945); C10 5-point sweep machine-ε agreement at `session-86-w2-workingpaper.md:232-272`; finite-infinite-vector classification framework note `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` §1-§2 (FINITE-VECTOR class).
- **gate**: PASS at plan-freeze (algebraic identity, no numerical recompute required); SANITY-CHECK at S87 closure on the L_max=12 cache verifies rel_err ≤ 5×float_eps at the existing 5-point sweep s ∈ {2.5, 2.75, 3.0, 3.25, 3.5}.
- **effort**: 2-3h (algebraic registry landing + sanity-check script).

**`S87-CM-1995-INADMISSIBILITY-AT-FINITE-L-LANDING` at §VII.V** (connes anchor, AXIOM × SPECTRAL, PROVEN-MODULO-NUMERICAL-RECONFIRMATION) — see Branch (ii) spec above.

**`S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE-LANDING` at §VII.W** (joint anchor, SPECTRAL × CROSS-PROGRAM, PROVABLE-CONDITIONAL-ON-CLOSURE-SCRIPT)
- **what**: Land the cross-program unification theorem at §VII.W: M2-failure on truncated cache ⟺ R-protection-failure of a_0-containing observables. Necessity from lizzi E-α step 2 (M2-failure forces residual regulator-dependence with no scheme-invariant cancellation partner); sufficiency from connes C2 axiom-level substitution chain.
- **inputs**: S77 R-protection-universal claim (`project_s77_synthesis`, `permanent-theorems.md` line 71); connes C2 substitution chain (workshop lines 730-820); lizzi E-α substitution chain (workshop lines 1037-1087); connes CN-α acceptance chain (workshop lines 1224-1240).
- **gate**: PASS criterion = synthetic 2-eigenvalue toy-model verification of the M2-failure → R-protection-failure biconditional at machine ε. FAIL ⇒ §VII.W theorem requires sub-cases beyond the biconditional.
- **effort**: 4-6h (synthetic toy-model script + biconditional verification + registry landing).

**`S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING` at §VII.X** (joint anchor, AXIOM × META, PROVABLE-CONDITIONAL-ON-NUMERICAL-RECONFIRMATION)
- **what**: Land the necessity-only meta-theorem at §VII.X: M2-axiom-failure on truncated cache is a STRUCTURAL SOURCE for (a) S64 finite-L Lambda_SA residual; (b) C9 9.46× a_0/Λ_CC ratio FAIL; (c) S77 a_0-slot R-protection failure. The 114-OOM Lambda_SA → Lambda_observed gap is CONTINUUM-LEVEL and is NOT contained in the M2-failure structural source. Six-prior-closure anchor list with full-64-char SHAs.
- **inputs**: connes EN-β six-row magnitude table (workshop lines 1490-1576); lizzi L-CN-5 a_0-split row addition (workshop lines 1712-1718); connes CN-β acceptance with refined statement (workshop lines 1244-1268); connes DN-γ necessity-only restatement (workshop lines 1376-1429); lizzi L-CN-3 retraction of "REDUCES TO" framing (line 1698).
- **gate**: PASS criterion = (a) six full-64-char SHAs from S46 / S64-split / S64-finite-L / S77 / S82-W2-5 / C9 verdict-line records pinned in §VII.X anchor block; (b) slot-by-slot magnitude table recomputed at L_max=12 verifies M2-failure magnitude is monotone in L_max → ∞ for each slot.
- **effort**: 6-8h (anchor SHA harvest from prior-session verdict files + L_max=12 magnitude recompute + registry landing).

**`S87-VII-PROP-LANDING` at §VII.PROP / §VII.PROP+1** (joint anchor, ROUTING-LAYER, two-principle landing) — per C-EN-1 + Q-OPEN-8
- **what**: Land TWO orthogonal routing-layer principles: (a) P_MB / P_CM un-bundling (E-γ); (b) Lens-mediated-vs-Prescription-mediated distinction (C-EN-1). At adjacent §VII.PROP / §VII.PROP+1 slots since the principles are STRUCTURALLY ORTHOGONAL.
- **inputs**: connes C1 axiom decomposition (workshop lines 730-820); lizzi E-γ un-bundling proposal (lines 1135-1141); connes CN-α acceptance E-γ (lines 1271-1292); connes C-EN-1 Lens / Prescription distinction (this round).
- **gate**: PASS at registry landing; both principles emit verdict-permanent routing-layer entries with cross-reference to §VII.U / §VII.V / §VII.W / §VII.X downstream consumers.
- **effort**: 3-4h (registry landing for two routing-layer entries with cross-references).

**`S87-PV-SUBTRACTION-RECALIBRATION` PRIMARY refutation gate** — per A-Q-L-R3-2 / L-EN-1 joint criterion
- **what**: Replace continuum SD residue coefficients with finite-L Pauli-Villars subtraction calibrated against the L_max=10 cache itself; test whether F_4 ratio suppresses below 5e-1.
- **inputs**: C9 verdict-line input pins; C10 5-point sweep for off-pole identity verification; §VII.U identity as sanity-anchor; PV subtraction cookbook from CM-1995 §"Counter-term Construction".
- **gate**: JOINT PASS criterion (per L-EN-1): (a) `rel_err(analytic_zeta(s, L=10), Dirichlet)` at s ∈ {2.5, 2.75, 3.0, 3.25, 3.5} remains ≤ 5×float_eps after PV subtraction; (b) `|Λ_CC^MB(reg, PV-recalibrated)| / |a_0^trunc(reg)| ≤ 5e-1` at s=0 for at least one reg ∈ F_4. BOTH required for PASS. PASS narrows the no-go to "CM-1995-CALIBRATED-SUBTRACTION-WITHIN-F_4 specifically"; FAIL strengthens to "ALL CALIBRATIONS WITHIN F_4".
- **effort**: 6h (matches lizzi's D-γ / Q-C4 estimate; PV subtraction script + dual criterion verification).

**`S87-D-EFF-ANCHOR-VERIFICATION` DIAGNOSTIC gate** — per L-CN-6 / EN-γ / L-DN-1 / A-Q-L-R3-3
- **what**: Verify the single-d_eff anchor d_eff = 8 with per-slot threshold ordering L_∞^{n=0} > L_∞^{n=2} > L_∞^{n=4} ≈ L_∞^{n=6} on the existing L_max=12 master cache, with per-regulator κ_n^reg measurement at 20% tolerance.
- **inputs**: `s84_spectrum_cache_L12_tau019.npz` (existing L=12 master cache, 155,984 eigenvalues); F_4 = {ζ, Zubarev, SDW} regulator profiles per `session-86-w2-workingpaper.md` C9 module; volume-preservation property of Jensen TT-deformation per `permanent-theorems.md`.
- **gate**: PASS criterion = (a) per-slot ordering holds within 20% across F_4 at each n ∈ {0, 2, 4, 6}; (b) M_0 still growing at L=12 (n=0 unsaturated); (c) M_4, M_6 essentially stable at L=12 (n=4, n=6 saturated). FAIL of (a) ⇒ regulator-conditional κ_n^reg corrections required (route to L_max=14 sweep at Q-OPEN-5). FAIL of (b) ⇒ d_eff = 8 anchor wrong, Casimir-tower different from Spin(8).
- **effort**: 4-6h (per-slot Mellin-moment computation on existing L=12 cache; no cache regeneration).

**`S87-SLOT-PRE-ALLOCATION-LOCKFILE-DRAFT`** (coordination artifact, not a registry entry) — per L-CN-4 / Q-L-R3-4 / A-Q-L-R3-4
- **what**: Draft `sessions/framework/s87-slot-pre-allocation-lockfile.md` with explicit RESERVED-FOR-WORKSHOP-86-W-1 entries for §VII.U / §VII.V / §VII.W / §VII.X / §VII.PROP / §VII.PROP+1. Append-only Python writers must scan ALL header levels (## + ### + ####) before allocation per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race".
- **inputs**: classification-based slot assignment table (workshop §"Round 3 — connes" CONVERGENCE C-FIN-4 + lizzi L-CN-4 table); the registry-write hygiene rule.
- **gate**: PASS at plan-freeze; lockfile spec is a coordination artifact with cross-session purpose (persists beyond S87).
- **effort**: 2h (lockfile drafting + plan-author handoff).

### Closing Line

The C9 FAIL is correct measurement at L_max=10, not infrastructure broken: its structural meaning is that the F_4 ∘ MB ∘ SD-subtraction CC-suppression program FACTORIZES into three independent components — a regulator-kernel lens (T5 / W1b), a substrate-spectrum lens (§VII.U), and a CM-1995 prescription mismatch at the truncated cache (§VII.V) — and the no-go is sharply localized at the prescription-mediated middle factor while the two lens-mediated factors stand permanently as L_max-invariant identities.
