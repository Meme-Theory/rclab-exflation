# Session 100a Synthesis: H₀ Spinor-Chain Adjudication — Which H₀ Does √16 Ground?

**Date**: 2026-06-07
**Agent**: kaluza-klein-theorist (KK)
**Source Documents**:
- `sessions/session-100a/session-100a-w4-workingpaper.md` (§W4-15 + Wave-4 synthesis)
- `computations/session-60/s60_bayesian_h0.py` (BAYESIAN-H0-60 producing script)
- `computations/session-100a/s100a_gate_verdicts.txt` (line 49 canonical + companion rows 50–53)

**Supporting artifacts consulted** (read-only; pinned values cited, no gate scripts executed):
`computations/session-58/s58_friedmann_derivation.{py,npz}`, `computations/session-59/s59_spinor_norm.npz`, `computations/session-60/s60_bayesian_h0.npz`, `sessions/archive/session-58/session-58-results-workingpaper.md` (W3-16), `sessions/archive/session-58/session-58-volovik-baptista-workshop.md` (:528, :712), `sessions/archive/session-58/session-58-{mack-collab,synthesis,wayforward}.md`, `sessions/framework/registry/falsifier-master-inventory.md` (Row #81, :1885–1897), `sessions/framework/registry/falsifier-watchlist.md` (H₀ row), `sessions/framework/Atlas/atlas-08-open-questions.md` (Q27, :262), `sessions/session-100a/session-100a-housekeeping.md` (A10/A11), `computations/_shared/canonical_constants.py` (:72, :95, :674), knowledge MCP (`search_knowledge`, provenance edges).

---

## I. Session Outcome

`S100a-H0-SPINOR-FACTOR` PASS (audit `39abff2d275ce8b509b1312513560ffa6e1299995b3c3398e09b936713d51788`) is authoritative and untouched: the spinor-normalization factor is **√16 = 4 EXACT** on the integer mesh, and the chain's normalization step is first-principles — that verdict is not re-adjudicated here. What this synthesis adjudicates is the **magnitude** the factor grounds, and the finding is sharp: **the published H₀ = 65.4 km/s/Mpc does not reproduce from any pinned chain artifact under legitimate Friedmann power-counting.** The only H₀ readout the S58→S59 chain ever *computed* is 68.77 km/s/Mpc (`s59_spinor_norm.npz`, RETRACTED-S60), whose deficit-closed limit is 67.4 — *above* the CMB anchor converging *down onto it*, the opposite displacement direction from the published 65.4. Neither competing reading survives as stated: R1's "matched deficits divide out of 65.4" fails because 65.4 is a prose projection with nothing in it for deficits to cancel, and R2's "shift 65.4 by (4/3.92)^p" fails because its baseline is the same non-derived number. The magnitude is **undecidable from existing artifacts**; the pre-registered recompute gate `S101-H0-PROPER-A2` (§V.1) is therefore mandatory, and the Row #81 value cell should be HELD (recommendation only — mack sole-writer surface, §II.D).

---

## II. Key Results

### II.A. Deliverable (a) — The explicit power-counting substitution chain N_factor → M_Pl,eff → H₀

**Result**: H₀^FW = H₀^obs × √16 / N_meas, i.e. the canonical spinor factor enters the Friedmann readout at power **p = +1** (numerator) and the truncation-dressed measured factor at power **p = −1** (denominator); closing the a₂ truncation deficit moves H₀ **downward**, 68.77 → 67.40. Classification: **GEOMETRIC** (the chain reads the fabric's a₂ spectral moment — the gravitational channel — into an emergent expansion-rate readout; nothing here is an excitation).

Per `math-scripts.md §"Double-Check Logic Before Compute"`, every definition, substitution, and sign read-off, with the pinned numbers substituted. No "obviously from structure" steps.

```
Claim: "Where the spinor factor enters the Friedmann normalization, with sign and power."

Substitution chain (S58 W3-16 chain as actually computed by s58/s59; all pins cited):

Step 1  (spectral coupling):
        alpha(tau_fold) = (f_2/2pi^2) * a_2(tau_fold),  f_2 = 1 pinned
                        = 162984.41511373137 / (2pi^2) = 8256.886927   [dimensionless, M_KK units]
        [a2_fold_wdw, s58_friedmann_derivation.npz; S52 WDW 5-point; alpha_fold key matches]

Step 2  (spectral Planck mass; s58 script line 493):
        M_SA = sqrt(16*pi*alpha) * M_KK = 4.785789363550277e19 GeV
        => M_SA ∝ a_2^{1/2},  M_SA ∝ M_KK^{1}
        [npz keys M_Pl_eff_GeV (s58) = M_Pl_unreduced_SA (s59); GeV from M_KK in GeV — dimensions consistent]

Step 3  (measured spinor factor — the truncation-dressed empirical anchor):
        N_meas ≡ M_SA / M_Pl_unred,obs = 4.785789e19 / 1.2209e19 = 3.920438854652296
        [s59_spinor_norm.npz key N_factor_MPl; the "3.92" of atlas-08 Q27, 3 sig figs;
         a_2-level square: N_factor_a2 = 15.369840813067405 = N_meas^2 to <0.01%]

Step 4  (spinor normalization — the W4-15 object, structural):
        M_phys = M_SA / N_struct,   N_struct = sqrt(dim Delta_12 / dim Delta_4) = sqrt(64/4)
               = sqrt(16) = 4 EXACT                      [S100a-H0-SPINOR-FACTOR PASS, eq (3) WP §W4-15]
        Equivalently a_2^{grav} = a_2^{total}/16 (s59: a2_corrected = 10186.5259 = 162984.4151/16 exact).

Step 5  (gravitational identification, corrected):
        M_red,FW = M_phys / sqrt(8*pi) = (M_SA/4)/sqrt(8*pi) = 2.386567152769585e18 GeV
        [s59 key M_Pl_reduced_corrected — matches to all printed digits]

Step 6  (Friedmann readout at fixed OBSERVED energy content; regime: z = 0, rho = rho_crit,obs):
        H^2 = rho / (3 M_red^2)        [H ∝ M_red^{-1} at fixed rho; rho_crit,obs ≡ 3 H_obs^2 M_red,obs^2]
        => H_FW / H_obs = M_red,obs / M_red,FW = 2.435e18 / 2.386567e18 = 1.020293938586312
        [s59 key H_0_ratio_corrected — EXACT match to the npz, all digits]

Step 7  (collapse to factor form):
        H_FW = H_obs * (M_unred,obs * 4 / M_SA) = H_obs * N_struct / N_meas
             = 67.4 * 4 / 3.920438854652296 = 68.76781146071743 km/s/Mpc
        [s59 key H_0_corrected — EXACT match; this is the S59 "68.8", RETRACTED-S60]

Step 8  (direction of the truncation correction):
        S59-measured a_2 deficit: frac_deficit = 0.04099972 (4.1% of a_2 missing from p+q >= 4)
        a_2 -> a_2*(1+0.041)  =>  M_SA -> M_SA*sqrt(1.041) = M_SA*1.0203  =>  N_meas -> 4.0003
        =>  H_FW -> 67.4 * 4/4.0003 = 67.39 km/s/Mpc
        Direction: closing the deficit RAISES M_SA (all omega_n > 0), RAISES N_meas toward 4,
        and LOWERS H_FW from 68.77 toward 67.4 — DOWNWARD, terminating at the anchor.

Conclusion: H_FW ∝ N_struct^{+1} * N_meas^{-1} ∝ N_struct^{+1} * a_2^{-1/2} * M_KK^{-1}.
        The truncated chain sits ABOVE the CMB anchor (68.77 > 67.4) and converges DOWN to it.
        Every ratio is dimensionless; km/s/Mpc enters only through the observational anchor.
```

**Anchor-degeneracy disclosure (load-bearing).** In Step 6 the energy content is the *observed* critical density, which is itself defined from the observed H₀ and observed M_red. The chain therefore predicts the **ratio of Planck masses** (equivalently G_N^FW/G_N^obs — the fabric's a₂ second-spectral-moment gravitational coupling against the laboratory's), and the "H₀ readout" is the observed anchor rescaled by that ratio's deviation from 1. At exact deficit closure (N_meas → 4) the readout degenerates to H_obs identically. The falsifiable content of this chain lives in the **G_N/M_Pl comparison channel**, not in an independently-normalized H₀ magnitude. Any Row #81 value must carry this disclosure.

**Where 65.4 came from — and why it does not reproduce.** The 65.4 first appears in S58 W3-16 prose (`session-58-results-workingpaper.md:1798`: "If this factor is corrected (dividing a₂ by 16) … H₀_SA → 65.4 km/s/Mpc (within 3% of observed)"), echoed in the S58 wayforward table (:34, "PASS (if derived)"), mack-collab (:67), and synthesis (§D, :89). It was a **hand projection, never a compute artifact**: no script or npz in S58–S100a produces it (grep + knowledge-MCP provenance trace; the only S59 file containing "65.4" is a coincidental V_eff array element in `s59_inspect_output.txt:111`; the S100a gate script *inherits* it as `H_0_FW_contingent=65.4  # S59/S60 chain` at `s100a_h0_spinor_factor.py:533`). Exhaustive propagation of the √16 correction through the pinned s58 npz values under every legitimate convention pairing gives:

| Route (all H ∝ √G at fixed ρ) | Value [km/s/Mpc] | Status |
|:---|:---|:---|
| In-chain ×4 rescale (reduced identification kept, ρ-pin 4.08e-47) | 14.45 | legitimate but uses the identification the correction itself repairs |
| Unreduced identification, ρ-pin 4.08e-47 (anchor 71.0) | 72.44 | legitimate variant |
| **Obs-anchored at 67.4: H_obs × (M_unred/M_corr) = 67.4 × 1.020294** | **68.77** | **THE computed value — `s59` npz, exact match; RETRACTED-S60** |
| Deficit-closed limit (Step 8) | 67.40 | anchor-degenerate |
| 67.4 × (M_corr/M_unred) — inverted ratio | 66.05 | sign slip, not 65.4 |
| 67.4 × (M_corr/M_unred)² — H ∝ G | 64.73 | power slip, not 65.4 |
| 67.4 × (3.92/4)^{3/2} ≡ 67.4 × (G_corr/G_obs)^{−3/4} | **65.39** | **the only reconstruction landing on 65.4 — a non-Friedmann power (±3/4, ±3/2 correspond to no identification)** |

The published 65.4 is reconstructible **only** via half-odd powers that correspond to no Friedmann identification. It is 3.0% *below* 67.4 where the legitimate chain sits 2.0% *above* — both "within ~3% of observed," which is how the slip survived every narrative check while the **displacement sign inverted**. Row #81's framing "the framework predicts the CMB anchor itself reads HIGH" and its falsifier direction ("convergence toward the mid-60s corroborates") inherit this inverted sign.

### II.B. The S60 divergence result and what it actually says

**Result**: `BAYESIAN-H0-60` = **FAIL** (realized verdict, `s60_bayesian_h0.npz` key `gate_verdict`): "ALL ratios diverge. a4/a2 last frac change 0.0967 > 0.5%. Incremental a4/a2 frac change 0.1080. N_factor diverges as L^6.2. No convergent observable from truncated PW spectral action." Classification: **GEOMETRIC** (truncation behavior of the fabric's spectral moments).

Three precision points the Focus framing needs corrected/sharpened:

1. **The divergence caveat is not merely an in-script comment at line 640.** Line 640 sits in the PASS-branch detail string of `s60_bayesian_h0.py` ("N_factor DIVERGES (L^α): no H₀ prediction without proper a₂"); the branch that actually fired is the FAIL branch (lines 649–653), whose realized detail is *stronger* ("No convergent observable from truncated PW spectral action"). Both branches carry the divergence statement; the realized one is a pre-registered FAIL verdict, not a caveat.
2. **The divergent object is the bare cumulative-PW reconstruction**, N(L) = a₂_cumul/(a₀_cumul/16) (script line 91): N_cumul = {0.037, 0.303, 1.43, **4.86 (L=3)**, 13.4, 31.9, 67.9, **121.0 (L=7)**}, with growth exponents α_a₀ = 8.44, α_a₂ = 9.14, α_a₄ = 9.82 and 99.7% of the a₄/a₂ variance attributable to truncation level. Line 555: "S59 prescription N = √16 = 4.0 was ACCIDENTAL at L=3." The S59 H₀ = 68.8 was retracted on exactly this ground (s60 docstring lines 6–9).
3. **The same docstring states the repair**: "The correct H₀ requires the true Seeley-DeWitt a₂(D_K²), which is a FINITE local geometric integral (independent of PW truncation)." The divergence is an artifact of reconstructing a₂ from unregulated truncated eigenvalue sums; the SD coefficient proper (heat-kernel small-t asymptotics / zeta residue) is finite. As of S88 the framework carries canonical zeta-regulated coefficients (`a_2_FW_zeta = 2776.165389`, `a_0_FW_zeta = 6440.0`, S88-A-N-FW-CANONICALIZATION; the W4-12 gate this same wave certifies the zeta leg as FULL-physical) — the "proper a₂" route the S60 FAIL called for now has canonical inputs, pending the convention-reconciliation map to the WDW-route chain (a₀: 101984 WDW vs 6440 zeta — different normalization objects; this reconciliation is the S101 gate's first task, not something to eyeball here).

**Explicit source conflict (flagged per rules).** WP §W4-15 cross-check 2 narrates "all ω_n > 0, so higher sectors push N monotonically UP **toward 4**." The s60 npz shows the cumulative-PW N passing *through* 4 (4.86 already at L=3) and growing without bound. Reconciliation: the W4-15 statement is **route-conditional** — it holds on the S59 WDW-route deficit estimate (a fixed finite a₂ with a bounded ~4.1% missing piece) and is contradicted on the bare cumulative-PW route (BAYESIAN-H0-60 FAIL). The W4-15 PASS itself is untouched by this conflict: its pre-registered criterion is the integer-mesh rel = 1/49 ≤ 1/40 against the empirical anchor, independent of either a₂ route; cross-check 2 is supporting narration, and its deficit-match content (implied 99/2500 = 3.96% vs S59-measured 4.1%, scale AND sign) is genuine *for the WDW route*.

### II.C. Deliverable (b) — Adjudication: R1 vs R2

**Result**: **Neither reading survives as stated; R2 wins on its core requirement (a continuum re-pin IS required) with its numerical prescription rejected; the magnitude is UNDECIDABLE from existing artifacts** — which fires the conditional S101 gate spec (§V.1). Classification: **GEOMETRIC** (adjudication of which spectral-moment chain output is real).

**R1 (truncation-self-consistent pair) — REJECTED for the magnitude, with its kernel preserved for the factor.** R1 claims the 3.92 measurement and the truncated a₂ carry the same ~4% deficit, the deficits divide out of the H₀ ratio, and the published 65.4 already IS the continuum answer. Three independent failures:

1. *Nothing to cancel in*: 65.4 is not the output of any chain (§II.A table); a cancellation argument cannot rescue a number that was never computed.
2. *The deficit enters once, not twice*: in the only computed chain (Step 7), the truncated a₂ appears solely through M_SA in the denominator (N_meas = M_SA/M_unred,obs; the numerator is the observed Planck mass and the exact integer 4). There is no second truncated a₂ for a pairwise division. The W4-15 deficit match (3.96% vs 4.1%) is **two estimates of the same single deficit agreeing** — a consistency closure for the *factor* (N_meas vs N_struct), not two deficits on opposite sides of a ratio. Quantitatively, the un-cancelled single deficit is exactly the +2.03% by which 68.77 exceeds the 67.40 deficit-closed limit (Step 8).
3. *No continuum exists on the route R1 implicitly uses*: if "the truncated a₂ it was paired with" means the cumulative-PW object, BAYESIAN-H0-60 FAIL says that object diverges — there is no continuum answer reachable from it at any truncation, matched deficits or not.

What survives of R1: the truncation-consistency closure for the **factor** is real and valuable (the empirical 3.92 is the truncation-dressed shadow of the structural 4 on the WDW route; the W4-15 PASS stands on it). R1's error is transferring that closure from the factor to the H₀ magnitude.

**R2 (continuum re-pin) — ACCEPTED in requirement, REJECTED in prescription.** R2 is right that the canonical `spinor_norm_factor_FW = 4.0` plus a deficit-corrected a₂ must be propagated through the chain before any magnitude is citable. But its prescription — shift the published 65.4 by (4/3.92)^{±1} to ~66.7 or ~64.1 — inherits the non-derived 65.4 baseline and mislocates where the factor enters. Per the substitution chain: the structural 4 is *already* in the numerator of the only computed value (68.77 = 67.4 × 4/3.9204); the continuum re-pin closes the 3.92 → 4.0003 deficit in the **denominator** (the measured M_SA), giving 67.39 — not 64.1, not 66.7, not 65.4, and not 68.8. And that 67.4-limit is anchor-degenerate (§II.A disclosure): the surviving falsifiable content is the M_Pl/G_N ratio channel, pending the proper-a₂ recompute.

**Adjudicated reading**: the exact spinor factor grounds the **normalization step** of the Friedmann chain (the statement M_Pl,phys = M_SA/√16 with no free parameter — exactly what the gate's value string and the WP §W4-15 PASS_meaning assert). It grounds **no currently-citable H₀ magnitude**: 65.4 is non-reproducible and sign-inverted; 68.77 is RETRACTED-S60; 67.4 is the anchor-degenerate limit of a chain whose a₂ input still lacks a convergent-route evaluation. The dual-prior Track A 0.95 posterior (STRUCTURAL √16) applies to the factor, where it belongs.

### II.D. Deliverable (c) — Recommended FLAGSHIP Row #81 value + confidence annotation (RECOMMENDATION ONLY — mack-cosmic-bridge sole-writer surface per `feedback_mack-bridge-role.md`)

**Result**: recommend **FLAGSHIP-class retained, value cell HELD** under the `cross-pillar-bridge-anatomy.md §"Non-Promotion-by-Held-Number"` taxonomy (P1: structure proven ∧ P2: NUMBER held ∧ P3: no sideways re-pin; differentia: **undischarged-magnitude-bound**). Classification: **GEOMETRIC** (registry-state recommendation on a substrate observable).

Row #81 as landed (inventory :1885–1897) already contains the honest seed — "Structural leg (factor = √16 EXACT, rel 1/49) is PROVEN-class; the 65.4 magnitude inherits the S59/S60 chain's own assumptions (NOT re-audited this gate)" — but four cells need reconciliation against what those inherited assumptions actually are:

| Cell | Current | Recommended |
|:---|:---|:---|
| Prediction value | "**H₀ = 65.4 km/s/Mpc** (S58 W3-16 / S59 NORM-59 / S60 Bayesian chain; contingency DISCHARGED S100a)" | "H₀ magnitude **HELD** pending `S101-H0-PROPER-A2` (NON-PROMOTION-BY-HELD-NUMBER; undischarged-magnitude-bound). Structural leg: M_Pl,eff/M_Pl,unred = √16 = 4 EXACT (S100a PASS, audit `39abff2d…`). Chain-computed historical candidates: 68.77 (S59 NORM-59 npz `H_0_corrected`; **RETRACTED-S60**, BAYESIAN-H0-60 FAIL) and the deficit-closed anchor-degenerate limit 67.4. The 65.4 figure is the S58 W3-16 prose projection — reconstructible only via non-Friedmann powers, displacement sign inverted vs the computed chain — retired from the value cell." |
| σ-distances | "3.59σ below Planck-anchored ΛCDM 67.34 ± 0.54; 1.88σ below TDCOSMO-2025 lower bar …" | **SUSPENDED** pending S101 (all three σ-distances are computed on the retired 65.4). |
| Falsifier function | "convergence well above ~67 … falsifies; convergence toward the mid-60s corroborates" | **Direction suspended.** Under the computed chain the truncated value sits ABOVE 67.4 and converges DOWN onto it — mid-60s convergence would NOT corroborate. Until S101 lands, the row's falsifiable content is the convention-clean ratio channel: G_N^FW/G_N^obs (equivalently M_Pl,FW/M_Pl,obs) with the anchor-degeneracy disclosure of §II.A. |
| Notes / caveat | "inherits the S59/S60 chain's own assumptions (NOT re-audited this gate)" | **Yes — the s60 divergence caveat survives into Row #81, and verbatim-stronger**: cite the realized FAIL ("No convergent observable from truncated PW spectral action", `s60_bayesian_h0.npz`) + the s60-docstring retraction of S59's 68.8 + the proper-a₂ repair path (finite local SD integral; canonical `a_2_FW_zeta` exists since S88) + the S101 gate pointer. |

**Why keep FLAGSHIP**: the watchlist's pre-registered contract was "CONTINGENT → FLAGSHIP on spinor-factor resolution"; the contingency named the **factor**, and the factor resolved (Q27 was the factor question — its RESOLVED status at atlas-08 :262 and housekeeping A10 stands). Demoting the row would retroactively rewrite the promotion trigger. The held-number tag scopes the confidence without inverting the promotion. (Alternative mack may prefer: `LIVE-PENDING-RECOMPUTE` class; secondary.) The same edits echo on the four surfaces of housekeeping A11: inventory Row #81, `falsifier-watchlist.md` H₀ row (:27, :64, :165–166 — note :166 already carries the not-re-audited scoping), capstone §7.2 row #10, and atlas-05 Window-19. Capstone-hygiene routing: this is a Q2/Q3 status-scoping on a §7 falsifier-anchor row → mack sole-writer, per `.claude/rules/capstone-hygiene-gate.md`.

**What is NOT recommended**: any change to the `S100a-H0-SPINOR-FACTOR` verdict line (permanent, authoritative), to Q27's RESOLVED status (the factor question), to `spinor_norm_factor_FW = 4.0` (canonical, correct), or to the FLAGSHIP promotion event itself.

### II.E. Deliverable (d) — Status-scoping of the Route-D 4-of-64 surviving-count anchor

**Result**: the 4-of-64 surviving-block **premise** is anchored at Stage-0 (workshop lines), inside a PASSed [VERIFY] gate whose *arithmetic* is gate-anchored — the registry/capstone echoes of √16 need an explicit anchor-status tag, and the premise deserves its own Stage-1 registry landing (§V.2). Classification: **GEOMETRIC**.

The decomposition of what is anchored where:

| Component of √16 = 4 | Anchor | Status class |
|:---|:---|:---|
| dim Δ₈ = 2⁴ = 16, dim Δ₄ = 4, dim Δ₁₂ = 64 = 4×16 (Clifford multiplicativity) | `s100a_h0_spinor_factor.npz` exact-integer flags; Sage-exact mirror | Gate-anchored (PASS), regulator-free |
| Res_{s=8} ζ_D = (Vol(SU(3))/(2π)⁸)·16 — the zeta-side 16 | `s87-d-eff-derivation-connes.md:176` (S87 derivation note) | Derivation-note anchor |
| EH term = a₂^M·a₀^K cross-term; a₀^K ∝ Tr_{Δ₈}(1)·Vol(K) = 16·Vol(K) | Paper 33 / S53 heat-kernel product factorization | Literature + session anchor |
| **Physical graviton retains exactly the Δ₄ block — 4 of 64** | `session-58-volovik-baptista-workshop.md:528` (Route D, Baptista-voice B4 paragraph: "a defined derivation within the CCM formalism") + `:712` (Q3, Volovik-voice Sakharov cross-reading: G⁻¹ ∝ Tr(1_spinor), 64→4 ⇒ √16, "without assuming which cross-term dominates" posed as a *question*) | **Stage-0 workshop-line anchor — NOT a registered theorem** |

Per `joint-theorem-promotion.md`, a workshop-internal candidate is Stage-0: citable, but not permanent-registry material until Stage-1 registration + Stage-2 cross-axis verify. The W4-15 gate verified the **integer-mesh consequence** of the premise (and its agreement with the empirical 3.92), which is exactly what a [VERIFY] trigger does — it did not, and was not pre-registered to, derive the on-shell projection statement itself ("√g R₄ carries NO internal spinor index; the on-shell-projected gravitational trace retains exactly one 4D Dirac block"). That statement is a one-lemma KK-reduction claim squarely in this agent's domain: on P = M⁴ × K the graviton zero mode h_μν is an internal scalar (it carries no Δ₈ index), so the normalization of its kinetic term retains dim Δ₄ = 4 of the 64 Δ₁₂ components, the remaining Tr_{Δ₈}1 = 16 being the internal multiplicity the spectral side over-counts — *provided* the EH identification runs through the a₂^M·a₀^K cross-term alone (the no-cross-term-dominance question Volovik's Q3 explicitly left open). That proviso is the clause Stage-2 must audit.

**Recommended tag** for every registry/capstone echo of √16 until the landing: "factor √16 = 4 (S100a-H0-SPINOR-FACTOR PASS, audit `39abff2d…`); surviving-block premise 4-of-64 per Route D (S58 workshop :528, **Stage-0 anchor**; registry landing CF §V.2 pending)". This parallels the WP's own addendum discipline for CF-S101-HK-1 (scope the protected operator-form class explicitly so a later revision cannot orphan the registered claim).

---

## III. Gate Verdicts

Verdicts below are quoted from their canonical sources and are authoritative; none is re-adjudicated here.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S100a-H0-SPINOR-FACTOR` (S100a W4-15; verdict file line 49) | **PASS** | factor_derived = 4 = √16 EXACT; rel = 1/49 = 2.041% ≤ 1/40 = 2.5%; margin 9/1960; Q27 RESOLVED |
| `FRIEDMANN-DERIVATION-58` (S58 W3-16) | INFO | M_Pl_eff/M_Pl_unred = 3.92; H₀_SA = 3.61 km/s/Mpc uncorrected; "if corrected: 65.4" (prose projection — see §II.A) |
| `NORM-59` / SPINOR-NORM-59 (S59, `s59_spinor_norm.npz`) | PASS | N_factor = 3.9204 ∈ [3.8, 4.2]; H_0_corrected = 68.7678 (subsequently RETRACTED-S60) |
| `PW-H0-CONV-60` (S60 W2-1) | FAIL | N(L=4) = 13.4; a₂ grows as L^6.2 — basis of the S59-H₀ retraction |
| `BAYESIAN-H0-60` (S60 W5, `s60_bayesian_h0.npz`) | **FAIL** | "ALL ratios diverge … N_factor diverges as L^6.2. No convergent observable from truncated PW spectral action"; N_cumul(L=7) = 121.0; truncation = 99.7% of variance |

(For completeness of the wave context: W4-12 INFO-by-design, W4-13 INFO, W4-14 PASS — not load-bearing for this adjudication except W4-12's certification of the zeta a_n leg as FULL-physical, which feeds §V.1's inputs.)

---

## IV. Structural Implications

1. **The constraint surface sharpened, not weakened.** The exact √16 is a real wall: the spinor-normalization step of the gravitational channel is now parameter-free, the same 1/16 = 1/dim(spinor) root as Trap 3 (e/(ac) = 1/16 trace factorization — one more appearance of the spinor-trace tensor-product structure across the framework). What fell away is a *number that was never computed*: the framework does not currently own an H₀ magnitude, and pretending otherwise via 65.4 would have mis-scored every incoming precision-H₀ release through an inverted falsifier direction.

2. **The chain's true observable migrates.** With the anchor-degeneracy disclosure (§II.A), the S58/S59-form chain is a **G_N prediction** (the fabric's a₂ moment vs the laboratory's Newton constant — currently 4% high at the truncated WDW a₂, exact at deficit closure) re-expressed through observed energy content. An H₀ readout independent of the anchor requires the framework's own energy-content leg (the Volovik-partition Level-2 of S58's two-level architecture) joined to the convergent-a₂ Level-1 — that joint is what S101 should pre-register, not a rescale of 65.4.

3. **The divergence FAIL is load-bearing and survives.** BAYESIAN-H0-60's realized FAIL ("no convergent observable from truncated PW spectral action") plus the s60-docstring retraction of 68.8 must travel with any H₀ row. The repair path it named — the finite local SD a₂ — now has canonical inputs (`a_2_FW_zeta`, S88), making the recompute cheap. The 65.4-vs-68.8-vs-67.4 spread (≈5%) is exactly the size of the convention/truncation freedom the recompute closes.

4. **Sign discipline vindicated.** The published value's displacement direction (below the CMB anchor) and the computed chain's (above, converging down) differ — a pure substitution-chain failure surviving 42 sessions because both lie "within ~3%." This is the precise failure mode `math-scripts.md §"Double-Check Logic Before Compute"` exists to kill; the S58 projection predates the rule.

5. **Anchor-status hygiene for premises inside PASSed gates.** A [VERIFY] PASS on an integer-mesh consequence does not promote its physical premise past Stage-0 (§II.E). The 4-of-64 lemma is one Stage-1 landing away from closing this — and the lemma's proviso (EH from the a₂^M·a₀^K cross-term alone) is the right Stage-2 clause for a cross-axis reviewer to audit.

---

## V. Carry-Forward Computations

V.1. **S101-H0-PROPER-A2 — convergent-route H₀ chain recompute** (REQUIRED: adjudication outcome is "re-pin required / magnitude undecidable from existing artifacts")
   - **What**: Recompute the full chain of §II.A Steps 1–8 with (i) `spinor_norm_factor_FW = 4.0` (canonical, exact), (ii) a CONVERGENT a₂ route — primary: the canonical zeta-regulated `a_2_FW_zeta` with an explicit WDW↔zeta convention-reconciliation map (a₀ objects 101984 vs 6440 are different normalizations; reconcile spinor-trace, fiber-volume, and τ_fold pins BEFORE substitution; the map is the gate's first deliverable, Class-8.4 representation-convention pin); fallback: direct closed-form local SD a₂(D_K²) on the Jensen fiber at τ_fold. Output: M_Pl^FW, the ratio G_N^FW/G_N^obs, N ≡ M_SA/(4·M_Pl_unred,obs), and the H₀ readout H_obs × (M_red,obs/M_red,FW) emitted WITH the anchor-degeneracy disclosure; mandatory substitution chain with the Step-8 sign verification (deficit closure lowers H).
   - **Inputs**: `canonical_constants.py`: `spinor_norm_factor_FW`, `a_2_FW_zeta`, `a_0_FW_zeta`, `M_KK`, `M_Pl_reduced`, `M_Pl_unreduced`, `H_0_km_s_Mpc`, `rho_crit_GeV4`; `computations/session-58/s58_friedmann_derivation.npz` (WDW pins: `a2_fold_wdw` = 162984.41511373137, `M_Pl_eff_GeV` = 4.785789363550277e19, `alpha_fold` = 8256.886927); `computations/session-59/s59_spinor_norm.npz` (`N_factor_MPl` = 3.920438854652296, `frac_deficit` = 0.04099972, `H_0_corrected` = 68.76781146 — retracted baseline for regression contrast); `computations/session-60/s60_bayesian_h0.npz` (FAIL verdict + α_a₂ = 9.1355 divergence exponent, the negative control the convergent route must beat).
   - **Gate**: `S101-H0-PROPER-A2` — PASS iff the convergent-route N lands in a pre-registered band about 1 (band frozen at S101 plan-freeze with Class-8.3 precision pins; suggested |N − 1| ≤ 0.05) AND the emitted readout carries the anchor-degeneracy disclosure; FAIL if the route reproduces divergence or lands outside band; INFO for partial convention reconciliation (map established, magnitude deferred). On ANY landing, Row #81's value cell re-pins to the gate output (mack sole-writer, Step-3 write-order).
   - **Effort**: ~1 gate (1 agent session) — canonical a_n and irrep caches exist; the work is convention reconciliation + chain assembly.

V.2. **S101-ROUTE-D-SURVIVING-BLOCK-LANDING — Stage-1 registration of the 4-of-64 KK-reduction lemma** (from §II.E)
   - **What**: Land the surviving-block premise as a STAGE-1-CANDIDATE registry entry with its own derivation artifact replacing the workshop-line cite: on P = M⁴ × K, Δ₁₂ = Δ₄ ⊗ Δ₈ (64 = 4×16); the EH term arises in the a₂^M·a₀^K cross-term carrying Tr_{Δ₈}(1) = 16; the on-shell graviton h_μν carries no internal spinor index, so its normalization retains exactly dim Δ₄ = 4 components ⇒ M_phys/M_spec = √(4/64) = 1/4. Clause-tag the proviso "EH identified from the a₂^M·a₀^K cross-term alone" (the S58 Q3 open question) explicitly for the Stage-2 reviewers; include the Sakharov G⁻¹ ∝ Tr(1) cross-reading as a separate clause.
   - **Inputs**: `sessions/archive/session-58/session-58-volovik-baptista-workshop.md:528` + `:712` (Stage-0 text); `computations/session-100a/s100a_h0_spinor_factor.npz` (integer-mesh structural flags); Paper 33/S53 heat-kernel product factorization; `s87-d-eff-derivation-connes.md:176`; `computations/_bridge_landing_script_template.py` (single-shot AFTER pattern).
   - **Gate**: `S101-ROUTE-D-SURVIVING-BLOCK-LANDING` — PASS iff the registry section matches the built promotion text post-fsync re-read AND the lemma text carries the cross-term proviso as an explicit clause; Stage-2 cross-axis verify then queued per `joint-theorem-promotion.md` (axis-A spectral, axis-B substrate; exclude this agent's S100a-W4-15 authorship lineage per the Stage-0-authorship exclusion).
   - **Effort**: ~0.5 gate (landing script + lemma write-up; arithmetic already gate-verified).

V.3. **Row #81 four-surface reconciliation batch** (mack-cosmic-bridge sole-writer execution of §II.D — routed recommendation, not physics compute)
   - **What**: Apply the §II.D cell edits (value HELD with NON-PROMOTION-BY-HELD-NUMBER tag; σ-distances suspended; falsifier direction suspended pending S101 with the ratio-channel interim; notes cell carries the BAYESIAN-H0-60 FAIL verbatim + the 68.8 retraction + S101 pointer) across the four A11 surfaces: inventory Row #81, watchlist H₀ row, capstone §7.2 row #10, atlas-05 Window-19. Q27 stays RESOLVED; FLAGSHIP class stays; `spinor_norm_factor_FW` untouched.
   - **Inputs**: this synthesis (§II.A table, §II.D cells); `s60_bayesian_h0.npz` verdict strings; `s59_spinor_norm.npz` (`H_0_corrected`, retraction provenance); Row #81 current text (:1885–1897).
   - **Gate**: verification condition (not a physics gate): post-edit grep confirms all four surfaces carry the HELD tag + the S101 pointer + no remaining bare "65.4 km/s/Mpc" prediction cell without the held-number qualifier; capstone-hygiene Q2/Q3 block records the routing.
   - **Effort**: single mack dispatch, no compute.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Substitution chain: H_FW = H_obs × √16/N_meas; factor at p = +1, measured N at p = −1; H ∝ a₂^{−1/2}; deficit closure moves H DOWN (68.77 → 67.40) | GEOMETRIC | Verified against `s59` npz to all digits (`H_0_ratio_corrected` = 1.020294 exact) | The published 65.4's below-anchor displacement has the wrong sign vs the computed chain |
| 2 | 65.4 km/s/Mpc non-reproducible: S58 W3-16 prose projection; only non-Friedmann powers (±3/2, ±3/4) land on it; no compute artifact S58–S100a produces it | GEOMETRIC | Established (exhaustive convention table §II.A + knowledge-MCP provenance) | Row #81 value cell cannot carry 65.4 as a chain output |
| 3 | Only computed corrected H₀ = 68.7678 (`s59` npz) — RETRACTED-S60; deficit-closed limit 67.4 anchor-degenerate | GEOMETRIC | Pinned (verdicts authoritative) | The chain's falsifiable content is the G_N/M_Pl ratio channel until S101 |
| 4 | R1 REJECTED for magnitude (single deficit, enters once; kernel survives for the factor); R2 ACCEPTED in requirement, prescription rejected (baseline inherits 65.4) | GEOMETRIC | Adjudicated (§II.C) | Magnitude UNDECIDABLE from existing artifacts → S101-H0-PROPER-A2 required |
| 5 | BAYESIAN-H0-60 realized FAIL ("no convergent observable…") + 68.8 retraction survive into Row #81 verbatim; proper-a₂ inputs now canonical (`a_2_FW_zeta`, S88) | GEOMETRIC | Pinned (s60 npz) | Recompute is cheap; the divergence caveat is a verdict, not a comment |
| 6 | Row #81 recommendation: FLAGSHIP retained, value HELD (NON-PROMOTION-BY-HELD-NUMBER, undischarged-magnitude-bound); σ-distances + falsifier direction suspended | GEOMETRIC | RECOMMENDED (mack sole-writer) | Four-surface batch §V.3; Q27 RESOLVED and the factor PASS untouched |
| 7 | Route-D 4-of-64 premise = Stage-0 workshop-line anchor inside a PASSed [VERIFY] gate; registry/capstone echoes of √16 need the anchor-status tag | GEOMETRIC | Scoped (§II.E) | Stage-1 landing §V.2 with the cross-term proviso as the Stage-2 clause |
| 8 | W4-15 cross-check-2 "N converges toward 4" vs s60 N_cumul through-4 divergence: route-conditional (WDW deficit estimate vs bare cumulative-PW) — source conflict flagged and reconciled | GEOMETRIC | Flagged | Narration scoped; the W4-15 PASS criterion is independent of either route |
