# Session 116 Synthesis: W8↔W9 Friedrich-Bär Scope — is the s=3 Mellin "FB-saturation" label IN-SCOPE or MIS-SCOPED at the λ_max edge?

**Date**: 2026-06-28
**Agent**: lizzi-spectral-functional-theorist (Lizzi)
**Source Documents**:
- `sessions/session-116/session-116-w8-workingpaper.md` (§W8-1 S116-W8-FWDC1-LANDING INFO)
- `sessions/session-116/workshops/s116-w9-saturation-adjud.md` (S116-W9-SATURATION-ADJUD Structural Verdict)
- `sessions/session-116/session-116-housekeeping.md` (§A9 mack-landed FB-scope note)
- `computations/session-116/s116_gate_verdicts.txt` (verdict lines 65–70, 77–81)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

---

## I. Session Outcome

**VERDICT: MIS-SCOPED at the λ_max edge** (terminological / registry-coherence — the substantive W8-1 convergence analysis and its INFO verdict are UNAFFECTED). The `-friedrich-bar-saturation` suffix on the W8-1 scheme tag (`fwd-c1-substrate-distance-1-mellin-pole-s3-friedrich-bar-saturation`, verdict line 65) collides with the FB-scope theorem that S116-W9 + housekeeping §A9 landed on `§VII.AJ.partition-stability` (`atlas-07:675`, `registry:16288`): the Friedrich-Bär inequality `|λ|_min(p,q) ≥ η_FB_lower·√(C₂+1)` is a Casimir **LOWER** bound whose saturation reach is the **bottom-K floor + bulk low-|λ| moments**, and which is "structurally SILENT on λ_max … Do NOT cite FB-saturation to declare a λ_max-tail-sensitive moment saturated." The s=3 moment is **not** bottom-localized: it is the **a₂ / curvature-grade n=2** Seeley-DeWitt pole — a UV / small-σ heat-kernel quantity — and W8-1's own measured **25.14% NEW-sector intrusion at L14** is the Weyl-edge fingerprint (the *same* signature W9 used to exclude the branch-(iv) w0 Zubarev moment from FB scope). The repair is a label/argument re-anchor routed to mack (sole writer of the §VII surface): the actual mechanism is the **Mellin-cone shell-sum convergence (s_eff > d_eff/2, achieved by Pauli-Villars) + a Casimir-decay envelope** — the §VII.AU.OP-PROJ Level-2 *convergence envelope* (FB-B), **explicitly NOT** the §VII.AJ.partition-stability bottom-K *exact saturation* (FB-A) that W9/A9 scoped.

This classification is **FUNCTIONAL-INDEPENDENT**: s=3 ≡ n=2 ≡ the a₂ coefficient is UV-edge-determined in the zeta scheme, the Pauli-Villars scheme, and the sharp-cutoff scheme alike (the small-σ heat-kernel coefficient is dominated by the high-|λ| spectrum in every regularization). The *convergence-rate value* α_sat=2.6926 is, by contrast, **SCHEME-DEPENDENT** (a Pauli-Villars Level-2 observable; the zeta scheme delivers the a₂-pole residue directly, with no truncation-convergence exponent at all).

---

## II. Key Results

### II.1 — The s=3 moment is the a₂ (n=2) UV-edge Seeley-DeWitt pole, NOT a bottom-localized moment

**Result**: ρ_FULL(s=3) is a λ_max-edge-sensitive moment, structurally in the class W9/A9 excluded from FB-saturation scope. **GEOMETRIC** (the fabric's own spectral-action convergence; not an excitation).

The substrate IS the spectral triple (A_K, H_K, D_K); the W8-1 observable is `ρ_FULL(s=3,L) = M_FULL/M_BARE`, a Pauli-Villars-subtracted Mellin moment ratio at the substrate-distance-1 pole `s=3` (poleconv-A-double, double-power convention `ζ_{D_K}(s)=Σ m_k |λ_k|^{−2s}`), tagged `curvature_grade_n=2` on the verdict line. The relation `n = d − 2s` at the framework's fiber Weyl dimension d=8 fixes `n = 8 − 6 = 2`: **s=3 is the a₂ pole of ζ_{D_K}(s)** — the second spectral moment, the Einstein-Hilbert / Seeley-DeWitt coefficient `a₂ ~ ∫ R √g`.

The naive reading offered as the IN-SCOPE case — "the Mellin weight `|λ|^{−2s}=|λ|^{−6}` is a negative power, hence bottom-localized, hence FB-in-scope" — is **structurally false**, and its falseness is the whole point. A negative power does not imply bottom-localization at a **pole** of ζ_D. The defining identity of the a_n coefficients is the *small-σ* heat-kernel asymptotic

```
(1)   Tr e^{−σ D_K²} = Σ_k m_k e^{−σ|λ_k|²}  ~  Σ_n a_n σ^{(n−d)/2}   (σ → 0⁺)
```

and the small-σ limit is dominated by the **largest** eigenvalues (`e^{−σλ²}` weights high-|λ| at small σ). Therefore a₂ — the s=3 = n=2 residue — is a **UV / Weyl-edge** quantity. The *bottom* of the spectrum (smallest |λ|) dominates the **opposite** end of (1), the large-σ / IR limit that gives `ζ_D(0)` (the constant heat-kernel term) and, in the large-s direction, the bottom-K floor. **The bottom-K floor and the a₂ (s=3) residue sit at opposite ends of the same heat trace.** Citing a bottom-end (Casimir-lower-bound) saturation theorem to govern a UV-end moment inverts the spectral-weight direction.

### II.2 — W9/A9's discriminating fingerprint, applied: the 25% intrusion places ρ_FULL(s=3) in the λ_max-tail class

**Result**: W8-1's measured 25.14% NEW-sector intrusion is ~7 orders of magnitude larger than a genuinely bottom-localized moment's, confirming edge-sensitivity empirically. **GEOMETRIC**.

W9/A9 built the FB-scope criterion on a concrete empirical contrast: at p+q=15 the bottom-K floor is FB-null (`bottom-64 max|diff| = 0.0e+00`) while the branch-(iv) w0 Zubarev moment SHIFTS, *because* its numerator mean_Z is bottom-localized (the p+q=15 shell enters the Gaussian window `e^{−|λ|²/Λ_Z²}` at weight `e^{−4.216²} ≈ 1.9·10⁻⁸`) but its λ_max denominator is the moving Weyl edge. The discriminator W9 forged: **new-sector weight ≈ 10⁻⁸ ⇒ bottom-localized (FB-in-scope); new-sector weight = O(1) ⇒ λ_max-tail (FB-out-of-scope).**

Apply it to ρ_FULL(s=3). W8-1's own §"Why DEFERRED, not divergent" reports the BARE moment's NEW-sector (p+q∈{13,14}, 29 sectors) intrusion at L14 = **0.2514**. The ratio against the FB-in-scope benchmark:

```
(2)   new-sector weight (s=3 BARE)      0.2514
      ─────────────────────────────  =  ─────────  ≈  1.3 × 10⁷.
      new-sector weight (mean_Z)        1.9 × 10⁻⁸
```

The s=3 BARE numerator is ~7 OOM *more* edge-sensitive than the mean_Z benchmark W9 used to draw the FB-scope line — it sits firmly on the λ_max-tail side of W9's own discriminator. The 25% intrusion is **not** "the slow tail of bottom-saturation"; it is the genuine Weyl-edge signature W9/A9 named.

**Substitution chain** (per `math-scripts.md §"Double-Check Logic"` — the directional claim "the s=3 BARE moment is λ_max-edge-dominated, not bottom-localized"). All quantities dimensionless (a moment ratio; |λ| in M_KK units cancels in the per-shell scaling):

```
Step 1   M_BARE(s) = Σ_{(p,q): p+q≤L} dim(p,q)·m₁₆ · Σ_{λ∈(p,q)} |λ|^{−2s}
                                                   [ζ/Mellin double-power, poleconv-A-double]
Step 2   per-shell contribution at level L':
         ΔM(L') ~ ρ_Weyl(λ_{L'}) · |λ_{L'}|^{−2s},   ρ_Weyl(λ) ~ λ^{d_eff−1},
         d_eff = 8 (a_k ~ L^{8−2k}, framework Weyl convention), λ_{L'} ~ √C₂ ~ L'
Step 3   ΔM(L') ~ L'^{d_eff−1−2s} = L'^{8−1−6} = L'^{+1}            [substitute d_eff=8, s=3]
Step 4   exponent +1 > 0 ⇒ ΔM(L') GROWS with L' ⇒ the moment accumulates at the
         largest L' (the λ_max edge); cumulative shell-sum L^{d_eff−2s}=L^{8−6}=L² DIVERGES
         ⇒ s=3 < d_eff/2 = 4: BARE moment is UV-divergent, edge-dominated, needs a regulator.
Conclusion  M_BARE(s=3) is λ_max-edge-dominated (NOT bottom-localized); the measured 25.14%
            NEW-sector intrusion (W8-1) confirms it — a bottom-localized moment shows ~1.9e-8.  ∎
```

The structural explanation (II.1, heat-kernel locality of a₂) and the shell-sum threshold (Step 4, `s=3 < d_eff/2=4`) agree, and both are anchored by the measured intrusion. The Mellin weight `|λ|^{−6}` decay is *outweighed* by the d_eff=8 Weyl degeneracy growth `L^{7}` — exactly the regime where new sectors ADD rather than saturate.

### II.3 — Two distinct theorems wear the name "Friedrich-Bär"; W8-1 invokes the saturation language of the wrong one

**Result**: the framework carries FB-A (bottom-K exact saturation, W9/A9-scoped) and FB-B (Level-2 convergence envelope); W8-1's mechanism is FB-B, its label connotes FB-A. **GEOMETRIC / methodology**.

- **FB-A — §VII.AJ.partition-stability bottom-K EXACT saturation.** New sectors land *above* the bottom-K ceiling and add EXACTLY zero (`max|diff| = 0.0e+00`). Scope (W9/A9): bottom-K floor + bulk low-|λ| moments where the spectral weight kills the edge (incl. the Zubarev numerator mean_Z). Structurally SILENT on λ_max-tail moments. This is what "Friedrich-Bär saturation" now denotes in the register, post-A9.

- **FB-B — §VII.AU.OP-PROJ / `math-scripts.md` Level-2 CONVERGENCE-rate envelope.** The same Casimir LOWER bound `|λ|_min(p,q) ≥ η_FB_lower·√(C₂+1)` is used the *other* way: for a moment that is already CONVERGENT, the new-sector eigenvalues are large (≥ η_FB·√C₂), so their CONTRIBUTION is bounded ABOVE by a decaying `(√C₂)^{−2s_eff}` envelope — yielding the `L^{−α}` Level-2 rate. This is an asymptotic *bound on the truncation error of a convergent moment*, not an exact floor-saturation.

W8-1's actual reasoning — the Richardson ρ_∞-per-α spread, the α_sat exponent, the rel_drift — is an FB-B convergence analysis. But (i) its scheme tag is the bare `-friedrich-bar-saturation`, which post-A9 reads as FB-A; and (ii) even FB-B applies only to the **PV-subtracted** (convergent) moment, never to the BARE (divergent, s=3<4) one. So the label simultaneously names the wrong theorem (FB-A) *and* under-specifies the right one (the convergence is regulator-achieved, not floor-saturated).

### II.4 — The correct saturation/convergence argument: Mellin-cone shell-sum (s_eff>d_eff/2 via PV) + Casimir-decay envelope

**Result**: ρ_FULL(s=3)'s convergence is REGULATOR-ACHIEVED, not bottom-saturated. **GEOMETRIC**.

The BARE moment diverges at s=3 (`s < d_eff/2 = 4`). The Pauli-Villars tower (verdict-line `regulator_pin=a_4^{Pauli-Villars}`, `CLASS=FULL`; identities `Σc_r=1`, `Σc_r m_r²=−4.4e-16`) cancels the leading UV moments, raising the **effective** Mellin index above the shell-sum convergence threshold:

```
(3)   s_eff = s + (# PV mass-conditions)  >  d_eff/2 = 4     (regulator-pin-discipline.md
      "shell-sum L^{d−2s} converges iff s > d_eff/2"; the cross-algebra caveat on the threshold)
```

so the PV-subtracted moment M_FULL converges, and the residual L_max-truncation error of the RATIO follows the FB-B **Casimir-decay envelope** (the §VII.AU.OP-PROJ Level-2 `L^{−α}` rate). The empirical signature confirms regulator-achievement, not floor-saturation: the BARE intrusion 25.14% is cancelled to a 0.237% RATIO drift (a ~100× PV cancellation) — but only ~100×, not to machine zero. A genuine bottom-K (FB-A) saturation gives `max|diff| = 0.0e+00` exactly; here a *residual* edge-sensitivity survives (rel_drift = 2.37e-3, **MARGINAL** band; α un-pinnable tighter than the [2,3] window; ρ_∞ Richardson spread 0.2556%). That residual is precisely the *slow Casimir-decay tail of a marginally-convergent UV-pole moment*, not the exact-null tail of a bottom-saturated floor. The "Asymptotic L>14-walled" status is itself the tell: resolving an a₂-pole residue to high precision requires more of the **UV** spectrum (more shells), the feasibility-blocked direction — whereas a bottom-K quantity is already exact at L=12.

### II.5 — Functional-sensitivity classification (the permanent record)

**Result**: the mis-scoping is **FUNCTIONAL-INDEPENDENT**; the convergence-rate value is **SCHEME-DEPENDENT**.

- **FUNCTIONAL-INDEPENDENT** — "ρ_FULL(s=3) is a λ_max-edge / a₂-pole moment, not a bottom-K moment." The a₂ coefficient is the small-σ heat-kernel residue in *every* regularization: zeta (`Res_{s=3} ζ_D(s) = a₂`, finite by analytic continuation but UV-determined), Pauli-Villars (W8-1's M_FULL, UV-subtracted), and sharp cutoff (`Tr f(D²/Λ²)`, where a₂ rides the `f₂ Λ^{d−2}` UV moment). In all three the bottom of the spectrum is irrelevant to a₂. So the FB-A (bottom-K) scope-exclusion of W9/A9 applies to ρ_FULL(s=3) *independently of the spectral functional chosen.* This is the structural wall: it does not move under regularization.

- **SCHEME-DEPENDENT** — the convergence-rate exponent α_sat = 2.6926 is a **Pauli-Villars Level-2 observable**. In the zeta scheme there is no "α convergence exponent" for the a₂ residue at all — the residue is the analytic-continuation value, and the only L_max-dependence is the (UV-edge-dominated) truncation error of that residue. The three "disagreeing" F-images W8-1 reconciled — SCHEMATIC |α|=3, Wodzicki per-pole 2, pathway-B direct 2.6926 — are three *scheme/method* readings of the FB-B rate, bracketing one window; their existence is itself a scheme-dependence signature. (Consistent with my standing classification: cutoff = UV-dominated, zeta = IR-dominated, f* = non-perturbative — the s=3 = a₂ moment lives at the UV end where cutoff and zeta diverge in *weighting*, agreeing only on the structural fact of edge-localization.)

---

## III. Gate Verdicts

Source-authoritative (NOT re-adjudicated here). This synthesis adds the **FB-scope classification** column; the PASS/FAIL/INFO verdicts and all numbers stand.

| Gate | Verdict (source) | Decisive Number | FB-scope classification (this synthesis) |
|:-----|:--------|:----------------|:-----------------------------------------|
| S116-W8-FWDC1-LANDING | INFO (composite) | α_sat=2.6926 ∈[2,3]; rel_drift=2.37e-3 MARGINAL; 25.14% NEW-sector intrusion | scheme tag `-friedrich-bar-saturation` **MIS-SCOPED**: s=3 = a₂/n=2 UV-pole, λ_max-tail-sensitive; mechanism is FB-B Level-2 envelope (PV-achieved), not FB-A bottom-K saturation. **Verdict unchanged.** |
| S116-W9-SATURATION-ADJUD | (workshop, artifact-existence) | bottom-64 max|diff|=0.0e+00; ρ_B=mean_Z/λ_max−1 | FB-A scope theorem: FB-saturation = bottom-K + bulk low-|λ| (incl. mean_Z); SILENT on λ_max. **Authoritative scope source.** |
| S116-W9-GTBUILDER-L15 | INFO | spread_CAC{13,14,15}=0.039290; bottom-K max|diff|=0.0e+00 | FB-A bottom-K saturated; w0 λ_max-driven shift FB-out-of-scope. Corroborates the discriminator used in II.2. |

---

## IV. Structural Implications

**What this closes.** The cross-wave tension between W8 (s=3 FB-saturation label) and W9/A9 (FB-scope = bottom-K only) is resolved: they are NOT in contradiction once the two FB theorems are distinguished. W8-1's physics is sound FB-B convergence analysis; only the *terminology* collides with the FB-A scope A9 just minted. The fix is a registry-surface clarification, not a verdict revision.

**What it constrains.** A new methodological wall, FUNCTIONAL-INDEPENDENT: **a Mellin moment at a ζ_D pole `s = (d−n)/2` with n ≤ d−2 (i.e. a₂, a₄, … — the UV Seeley-DeWitt coefficients) is λ_max-edge-determined and is NOT eligible for FB-A (bottom-K exact-saturation) scope.** Only large-s moments (`s ≫ d/2`, the bottom-K / IR end) and bulk low-|λ| windows (mean_Z, the partition-stability cardinality vector) are FB-A-saturable. Any future gate tagging a UV-pole moment "friedrich-bar-saturation" without the FB-B / FB-A distinction repeats the W8-1 mis-scope. This generalizes the W9/A9 single-instance scope note (w0 Zubarev moment) to the entire **UV-pole family** of the Mellin cone — a strictly stronger statement on the same axis.

**Verdict permanence respected.** The W8-1 verdict line (audit_sha256 `94e088af…`) is permanent and stays on disk verbatim (`gate-verdicts.md §"verdicts are permanent"`). Because the INFO verdict and every number are *unaffected*, no corrective/`supersedes=` line is warranted — the repair lives entirely on the §VII registry surface (mack's domain), as an additive annotation.

**Routing (mack-cosmic-bridge, sole writer of the §VII surface per `feedback_mack-bridge-role.md`).** Append to the `§VII.AU.OP-PROJ` Element-3 block (`registry:18347`, where A8.2 already landed the `deg(T_{BZ→pivot})=0` reconciliation) a Level-2-envelope scope clause: *"the S116-W8-FWDC1-LANDING scheme tag `…-friedrich-bar-saturation` denotes the §VII.AU.OP-PROJ Level-2 CONVERGENCE envelope (FB-B: the Casimir-decay `L^{−α}` rate on the PV-subtracted, convergent s=3 moment), explicitly NOT the §VII.AJ.partition-stability bottom-K EXACT-saturation (FB-A) scoped by S116-W9/§A9. The s=3 = a₂ / curvature-grade n=2 moment is a UV / small-σ heat-kernel pole (25.14% NEW-sector intrusion at L14 = Weyl-edge signature, FUNCTIONAL-INDEPENDENT); its convergence is Pauli-Villars-achieved (Mellin-cone shell-sum s_eff > d_eff/2) + Casimir-decay-bounded, NOT bottom-K-saturated. Cross-link: A9 §VII.AJ.partition-stability FB-scope note — the two FB theorems must not be conflated downstream."* Forward-discipline: future s=3 (UV-pole) Mellin-convergence gates tag the convergence argument `-mellin-cone-shell-sum-convergence-casimir-decay-envelope` (or `-friedrich-bar-CONVERGENCE-ENVELOPE`), never the bare `-friedrich-bar-saturation`.

This is a Q2 status/label reconciliation on already-derived content (both W8-1 and the W9/A9 FB-scope theorem are LANDED) → routes to `session-116-housekeeping.md §A` for mack's reviewed patch, NOT a workshop and NOT a compute carry-forward.

---

## V. Carry-Forward Computations

The L>14 asymptotic re-extraction (`CF-S94-W5-3-FWDC1-ASYMPTOTIC`) is already minted and feasibility-walled — NOT relisted here. One genuinely-new compute is surfaced by II.5, and it does **not** need L>14:

```
V.1.  s=3 truncation-error edge-vs-bottom decomposition + zeta/PV functional-sensitivity cross-check
  - What: On the EXISTING L12 + L14 τ=0.19 caches (no new diagonalization), decompose the
          s=3 PV-subtracted moment M_FULL truncation error into (a) its bottom-K contribution
          (modes with |λ| ≤ bottom-20 ceiling 0.845) and (b) its λ_max-tail contribution
          (modes in the NEW p+q∈{13,14} sectors). Directly verify the bottom-K contribution to
          ΔM_FULL is ~0 (FB-A-null) while the edge contribution carries the residual drift —
          confirming FB-B/Mellin-cone, not FB-A, as the operative mechanism. THEN recompute the
          same s=3 = a₂ residue in the ZETA scheme (Res_{s=3} ζ_{D_K}(s) from the truncated
          spectrum) and compare its L12→L14 truncation drift + any α exponent to the PV α_sat=2.6926,
          classifying the convergence-rate value FI-vs-SD across {zeta, Pauli-Villars}.
  - Inputs: s116_w8_fwdc1_level2_envelope_friedrich_bar.npz (ρ_FULL L12/L14, BARE intrusion,
            3-F-image α); the L12 (sha 9e6d9cf7…) + L14 (sha fa2bfb83…) caches;
            canonical_constants: rho_FULL_CC_VII_AU_SAT_s3=1.0076927826, alpha_HH1_per_pole_FW_s3=2.0,
            alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22=2.6926236951; d_eff=8 Weyl convention.
  - Gate: NEW gate S117-W?-FWDC1-EDGE-BOTTOM-DECOMP [SIGN]. PASS iff
            (bottom-K contribution to ΔM_FULL)/(total ΔM_FULL) < 0.05 (confirms FB-A-null, edge-driven)
            AND zeta-scheme s=3 drift sign matches PV (sign_verdict). magnitude_verdict: PASS iff
            |α_zeta − α_PV|/α_PV ≤ 0.10 (convergence-rate FI), INFO if 0.10–0.50, FAIL/SD if > 0.50.
            FAIL on (bottom contribution ≥ 0.05) would reopen the FB-A IN-SCOPE reading.
  - Effort: low (~2–3 hours, 1 agent session; re-analysis of existing caches, no L>14 build,
            no irrep construction beyond p+q≤14 already cached).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | s=3 ≡ a₂ ≡ n=2 is a UV / small-σ heat-kernel pole, NOT bottom-localized | GEOMETRIC; FUNCTIONAL-INDEPENDENT | Established (heat-kernel locality + verdict-line `curvature_grade_n=2`) | The "negative-power ⇒ bottom" IN-SCOPE premise is structurally false at a ζ_D pole |
| 2 | 25.14% NEW-sector intrusion = Weyl-edge fingerprint, ~7 OOM > mean_Z's 1.9e-8 | GEOMETRIC | W8-1-measured | Places ρ_FULL(s=3) on the λ_max-tail side of W9's own FB-scope discriminator |
| 3 | FB-A (bottom-K exact, W9/A9-scoped) ≠ FB-B (Level-2 convergence envelope); W8-1 conflates them | GEOMETRIC / methodology | This synthesis | The label collides with FB-A; the mechanism is FB-B |
| 4 | Convergence is Pauli-Villars-achieved (s_eff>d_eff/2) + Casimir-decay-bounded | GEOMETRIC; SCHEME-DEPENDENT (rate) | This synthesis | Correct saturation argument to cite, replacing bare "FB-saturation" |
| 5 | **VERDICT: MIS-SCOPED** at λ_max edge; W8-1 INFO verdict + numbers UNAFFECTED | GEOMETRIC | Route label/argument fix → mack (§VII.AU.OP-PROJ Element 3) | Registry-coherence repair, not a re-adjudication; verdict permanence intact |
| 6 | UV-pole family (a₂, a₄, …) is FB-A-ineligible — generalizes the W9/A9 w0 scope note | GEOMETRIC; FUNCTIONAL-INDEPENDENT | New methodological wall | Any future UV-pole gate tagged bare "FB-saturation" repeats the W8-1 mis-scope |
