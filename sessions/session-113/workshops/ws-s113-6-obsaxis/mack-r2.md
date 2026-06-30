# WS-S112-6 OBSAXIS — Round 2 (rebuttal)

**Workshop**: WS-S112-6 OBSAXIS — the CMB-orthogonal observational steer (NICER dense-matter EoS vs DESI/Euclid f·σ₈ growth)
**Author**: mack-cosmic-bridge — Round 2, rebuttal (Reading B: DESI/Euclid f·σ₈ growth axis)
**Date**: 2026-06-22
**One-line**: nazarewicz's R1 is the strongest version of Reading A and forces me to concede a real error in my R1 — the interior EoS pipeline DOES exist and DOES run. But the concession does not flip the EVOI ranking, because nazarewicz's headline observable (M_max) rides the framework's one permanently-unanchored weight (M_KK, §VII.BS NNU), so the "tractable surface compute" cannot pin it FROM THE SUBSTRATE — it can only move a free dial. The growth-axis σ-distance, by contrast, is built on dimensionless observables the NNU theorem leaves anchored, with a real FETCHED forecast covariance. The ranking holds: growth is the higher-EVOI *pre-registrable-today, substrate-anchored* falsifier.

---

## 1. What I concede to nazarewicz (cleanly, because it is correct)

My R1 leaned too hard on Row #88's bare "the framework has NO compact-object sector." nazarewicz correctly sharpens this: Row #88's "no compact-object sector" means **no formation channel and no self-bound exterior M–R from a hydrostatic surface** — it does NOT mean "no interior EoS." The interior pipeline `D_K → Δ(μ) → P(ρ) → TOV → M(R)` is instantiated three times on disk (INV13-W2-1, S110-CF-CO1-EOS, INV11-W5-2), and CFL is the substrate's *native* dense phase (the SU(3) the framework is built on is the same SU(3) that color-locks). I was wrong to imply the dense-matter axis is unconstructed. It is half-constructed, and nazarewicz's accounting of which half (interior present, surface absent) is accurate.

I also concede nazarewicz's §2(ii) point in its own terms: a predictive band `[0.16, 4.78] M_⊙` against an observed window `[2.0, 2.6] M_⊙` is, *if the band were collapsible from the substrate*, a maximally-informative measurement. The EVOI formula does reward maximal prior width with a fixed scoring function. That is a genuine and well-posed argument, and I will not dismiss it.

So the disagreement is not "does the substrate have a dense-matter sector" (it does) versus "does it have a growth sector" (it does). Both exist. The disagreement is narrower and sharper: **can each axis's headline falsifier be pinned FROM THE SUBSTRATE today, or does it ride a free parameter?** That is where Reading A breaks and Reading B holds.

---

## 2. The rebuttal's core: M_max rides the M_KK keystone — the band is NOT a collapsible epistemic uncertainty

nazarewicz's EVOI case rests entirely on §2(ii) + §6: the `[0.16, 4.78] M_⊙` band is "epistemic (surface-condition) uncertainty, not statistical," and a substrate-derived `Δ→0` surface "collapses the surface-condition degree of freedom from free dial to substrate-derived." This is the load-bearing claim, and it is **false in the specific way that matters**, because of a structural theorem nazarewicz himself cites and then under-weights.

**The §VII.BS NNU theorem (STAGE-3-PERMANENT, `second_rel_sv = 1.066e-17`, `S103-NNU-BUNDLE-EXHAUSTIVENESS` PASS):** every dimensionful substrate observable factors as `O = w · Ô` with a *single* un-fixed weight `w = M_KK = 7.428660×10¹⁶ GeV` (`get_constant("M_KK")`, CONST-FREEZE-42, non-superseded). The dimensionless skeleton `Ô` is substrate-fixed; the weight `w` is the framework's one permanently-unanchored import (the same wall that blocks A_s magnitude, the CC absolute scale, and incumbent-discrimination — §EVOI.BF's "absolute CMB scales it cannot fix without an external M_KK").

Now apply it to M_max. **M_max is a mass — it carries the weight.** Write `M_max = M_KK · M̂_max` where `M̂_max` is the dimensionless TOV-sequence maximum on the substrate's own (M_KK-natural) EoS. The factor-30 band `[0.16, 4.78] M_⊙` is what you get when you read M_max off the EoS at a *physical* density scale — and the physical density scale (where the relay-condensate's pressure is set in g/cm³) is itself an M_KK-weighted quantity. The surface-condition `Δ(μ_surface) = 0` that nazarewicz proposes is a calculation in **M_KK-natural units**: it pins the dimensionless edge `μ̂_surface`, NOT the dimensionful surface density in g/cm³. To turn `μ̂_surface` into a g/cm³ at which TOV terminates, you must multiply by powers of M_KK — the un-fixed weight.

So the substitution chain for nazarewicz's "collapse the band" claim is:

```
Step 1: M_max = M_KK · M̂_max                      [§VII.BS NNU, O = w·Ô, w = M_KK]
Step 2: M̂_max = f(μ̂_surface, Δ̂(μ̂), TOV)          [dimensionless TOV sequence, substrate-fixed]
Step 3: A substrate Δ→0 edge solve pins μ̂_surface  [dimensionless — this is the tractable compute nazarewicz proposes]
Step 4: BUT M_max = M_KK · M̂_max still carries M_KK [the weight is UN-FIXED, §VII.BS]
Conclusion: the Δ→0 surface compute pins the DIMENSIONLESS M̂_max; it does NOT
            pin the DIMENSIONFUL M_max in M_⊙ unless M_KK is independently fixed —
            and M_KK is the framework's ONE permanently-unanchored weight.
```

This is the precise sense in which nazarewicz's "epistemic uncertainty collapsible by a ~2-3 wave compute" is mis-diagnosed. Part of the `[0.16, 4.78]` band IS a genuine surface-condition (dimensionless) uncertainty that the proposed compute could narrow. But the *headline comparison to NICER's M = 2.08 M_⊙ in solar masses* requires the dimensionful M_max, and that rides M_KK. The band does not collapse to a falsifiable point against NICER's mass; it collapses (at best) to `M_KK · [a narrower dimensionless interval]`, which is still a free dial in M_⊙ until M_KK is pinned. **A surface compute cannot fix what the NNU theorem proves is structurally un-fixed.**

nazarewicz half-saw this in §4b ("M_max itself is a mass, so it carries the weight") and §4c ("a free dial is the opposite of a falsifier; tuning to [2.0, 2.6] would be ansatz-forced PASS — PROHIBITED"). I am pressing exactly that admission to its conclusion: the dimensionful M_max gate is, by §VII.BS, a free dial in the one direction NICER measures, and no surface compute removes the dial — it only narrows the dimensionless multiplier on it.

---

## 3. The empirical tell: the "repaired" EoS is STILL sub-floor compact (the dilution is structural)

nazarewicz argues the compactness gap (`C_substrate ~ 2.4e-4` vs `C_NICER ~ 0.25`) might be a fixable missing-surface artifact. The on-disk verdict string of the very gate nazarewicz cites as the repair refutes this:

**`S110-CF-CO1-EOS` (INFO):** `M_max=4.783_Msun ... Delta/mu=0.102_band[0.03,0.3] ... C_max=2.26e-04_floor1e-03 ... inv13_runaway_ratio=4.821->selfcons=0.102`.

Read the compactness leg carefully. The self-consistent μ_eff(ρ) repair fixed the gap *ratio* (4.821 → 0.102, now in the physical CFL window) — a real success on the gap-runaway. But the resulting compactness is `C_max = 2.26e-4` against the gate's own **floor of 1e-3**. The repaired object is **4.4× below its own minimum-compactness floor**, and ~1100× below NICER. The gap-ratio fix did NOT move the compactness toward NICER at all — it stayed at `~2e-4`.

This is the empirical signature of nazarewicz's own §4a dual-prior **Track B** (the substrate compact object is *intrinsically* a `C ~ 10⁻⁴` dilute gravastar, `w_core = −0.92` dark-energy-like, not a nuclear fluid). The repair that fixed the gap ratio left the compactness three OOM low — strong evidence the dilution is a structural property of the relay-condensate, not a missing-surface artifact. Per nazarewicz's own framing, if Track B holds, "Reading A degrades from 'predict M–R' to 'no-go: no neutron-star branch' — still a falsifier, but a weaker kind." The on-disk number points at Track B.

And note what "no-go" means for EVOI on this axis: a no-go is a *one-directional* falsifier (the substrate-has-no-neutron-star-branch reading). It cannot be confirmed-into-a-prediction, only refuted-or-not. Row #88 already says this: "the rich ECO observational program **cannot refute it; it can only expose the gap**." The pass-leg of EVOI is near-empty; only the fail-leg (and a weak, NON-discriminating one — equally Kerr-and-framework) carries weight.

---

## 4. The WS-CO-1 STERILE precedent re-enters through M_max (nazarewicz's scope-survival is partial)

nazarewicz's §4b carefully scopes Reading A to the *dimensionful M–R / compactness* axis and argues the WS-CO-1 STERILE verdict (mack × schwarzschild-penrose) only killed the *dimensionless-ratio echo/QNM* axis, leaving the dimensionful M–R "a distinct, still-open corridor." I credit the care — and I agree the STERILE verdict was scoped to the dimensionless-ratio axis. But two on-disk facts show the dimensionful axis does not cleanly survive:

**(a) The framework's own dimensionful-CO falsifier gate was BLOCKED.** `S110-CF-CO2-FALSIFIER` is on disk as **FAIL**, `value='PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE'`, `convention=WS-CO-1-Reading-STERILE-upstream-block-NOT-FIRED`. The framework *tried* to land a compact-object falsifier post-WS-CO-1 and it mechanically closed as upstream-blocked. nazarewicz's "distinct, still-open corridor" is, on the verdict ledger, a blocked corridor — the CO-falsifier gate did not fire.

**(b) The STERILE structural reason re-enters M_max.** WS-CO-1 found the compact-object sector's framework-specific content "rides ω_GR (M_KK-set)" and its transport-safe dimensionless ratios are Kerr-degenerate. M_max is not a dimensionless ratio, so it is not *Kerr*-degenerate — but it IS M_KK-set (§2 above, §VII.BS). The same structural fact that made the ratios sterile (framework content rides M_KK) makes M_max a free dial. The dimensionful axis "survives" WS-CO-1 only in the sense that M_max is not Kerr-degenerate; it does NOT survive as a *substrate-pinned* falsifier, because its scale is the un-fixed weight. This is exactly the crux nazarewicz named in §(ii) and left for me to answer: **yes, the dimensionful M–R re-entangles M_KK the way the ratios did** — not via Kerr-degeneracy, but via the NNU weight. That collapses the gate to "free dial, not falsifier" in the dimensionful direction NICER measures.

---

## 5. Re-affirming Reading B: the f·σ₈ gate IS pre-registrable NOW with a SUBSTRATE σ-distance

The prompt asks me to verify, not just assert, that my growth gate is pre-registrable today with a substrate σ-distance. I verified it on disk. The σ-distance is real, substrate-built, and dimensionless-anchored:

**`INV13-W2-2-FSIGMA8-GROWTH-S8` (PASS), dual-SHA + companion rows:**
- `bindable_DESI5yr=1bins Euclid=7bins`, `max 1.001σ @ z0.5`, explicitly **reproducing the upstream Row #71 forecast σ-dist 1.013 DESI-Y5 / 1.534 Euclid**.
- The σ-distance is computed by applying the **FETCHED DESI-Y5 / Euclid RSD forecast covariance** (Row #71 provenance, `s96_obs_fsigma8_forecast.npz`, DESI-5y forecast) to the **substrate's own** suppressed f·σ₈ curve (product suppression −4.058% @ z=0.51, `f_FW=0.5254916`).
- The discriminating observables are **dimensionless**: `S8_FW = 0.8128` (a ratio), the −4.058% **product suppression** (a fractional deviation), the f·σ₈(z) **shape**. None of these carries the M_KK weight. The companion row even records the anti-rescue discipline: `growth sigma8=0.79317 USED, NOT OZ 0.79900` (no channel-shopping), and the C5 guard (PRODUCT −4.058%, NOT bare-f −0.311%).

This is the decisive contrast with Reading A. The growth gate's headline falsifier is a set of dimensionless observables (S₈ ratio, fractional f·σ₈ suppression, spectral shape) that the §VII.BS NNU theorem leaves **anchored** (they are `Ô`-type, weight-free). The σ-distance against DESI/Euclid is therefore a genuine substrate prediction, not `M_KK · (free dial)`. The gate I pre-registered in R1 §6 (`CF-S113-FSIGMA8-EUCLID-7BIN`) is fully specified today: prediction pinned, σ-budget pinned (1.534σ Euclid joint over 7 bins), instrument pinned, anti-rescue fence pinned. No analogous NICER gate can be pre-registered today without leaving M_max as `M_KK · M̂_max` with M_KK un-fixed.

I will also strengthen, not just defend: the growth axis is the UP-side LSS handle in the §EVOI.BF re-anchor (Row #71.aug: "the f·σ₈ / S₈ LSS axis is the UP-side handle, NOT part of the observational-DOWN cohort"). A PASS there is independent-confirmation gold on a dataset the framework was not built to fit. The NICER axis, by the §2-§4 argument, can at best deliver a weak one-directional no-go on a free-dial observable.

---

## 6. The honest residual — where Reading A retains genuine value

To keep this an open-verdict adjudication and not a demolition, I record what survives for Reading A even after §2-§4:

- **The W2-1 SIGN-PASS is durable and real.** `dΔ_CFL/dμ > 0` at every scan point is a genuine, dimensionless, substrate-fixed prediction about diquark density-dependence — and it is NOT M_KK-weighted (it is a sign of a derivative). nazarewicz's strongest seed (flagged in my R1 §4) is whether a *sign-based* or *dimensionless-ratio-based* dense-matter observable could be pre-registrable. I concede this is the one place Reading A has a weight-free handle. My answer remains: a sign-of-stiffening prediction does not discriminate against NICER's M/R **magnitude** contours (NICER measures M in M_⊙ and R in km, not dΔ/dμ). But if Reading A could tie the SIGN-PASS to a dimensionless *terrestrial* discriminant (e.g. the FRIB symmetry-energy slope L, nazarewicz §2(iv)) — a weight-free ratio — that would be a genuinely pre-registrable dense-matter gate. That is a real R3 question, and it is narrower and more honest than "predict M_max against NICER."

- **The dataset-fixity point is correct.** NICER M–R + Sorensen+ 2024 band is fixed and improving; that is a real EVOI asset I do not dispute. It just cannot rescue a free-dial headline observable.

So the steelman of Reading A that survives is NOT "M_max vs NICER" (free dial) but "a weight-free dense-matter dimensionless discriminant (sign-of-stiffening, or L from FRIB) tied to a fixed terrestrial+astrophysical band." That is a legitimate competitor to the growth gate — but it is a *different, narrower* gate than the one nazarewicz pre-registered (S113-CO-MR-NICER targets `M_max ∈ [2.0,2.6] M_⊙` and `C_max ∈ [0.20,0.30]`, both dimensionful/M_KK-weighted), and it is not yet constructed.

---

## (i) Updated lean (honest)

**I retain my lean toward Reading B (growth) as the higher-EVOI *pre-registrable-today, substrate-anchored* falsifier — but I have UPDATED it from "by a clear margin / wide gap" (R1) to "by a structural margin that is narrower than I claimed in R1, and conditional on the dimensionful/dimensionless distinction."**

The update has two parts. First, a concession: nazarewicz showed the dense-matter pipeline exists and runs, so my R1's "Reading A must first invent a sector that doesn't exist" was too strong — the sector is half-built, and the EVOI-of-maximal-band argument is well-posed. Second, the reason the lean nonetheless holds: nazarewicz's headline observable (M_max in M_⊙, C_max) rides the §VII.BS M_KK keystone — the framework's one permanently-unanchored weight — so the "tractable surface compute" pins only the dimensionless multiplier, not the dimensionful comparison to NICER; and the on-disk `S110-CF-CO1-EOS` (`C_max=2.26e-4 < 1e-3 floor` even after repair) plus `S110-CF-CO2-FALSIFIER` FAIL (blocked) point at nazarewicz's own Track-B (intrinsic dilute gravastar → weak one-directional no-go). The growth gate's σ-distance is built on weight-free dimensionless observables (S₈ ratio, fractional f·σ₈ suppression) with a real FETCHED forecast covariance, and is fully pre-registrable today.

I do NOT concede the ranking, but I sharpen it: **growth wins on the *dimensionful* M–R comparison decisively (M_max is a free dial via NNU); the contest is genuinely live ONLY if Reading A retreats to a weight-free dimensionless dense-matter discriminant (the W2-1 SIGN-PASS, or FRIB L)** — which is a different, narrower, not-yet-constructed gate than nazarewicz's S113-CO-MR-NICER.

## (ii) The single crux the R3 verdict must resolve

**Does the substrate's headline dense-matter falsifier reduce to a DIMENSIONLESS, M_KK-weight-free observable, or does it ride the M_KK keystone?**

- If the decisive dense-matter falsifier is the **dimensionful M_max / C_max against NICER** (nazarewicz's S113-CO-MR-NICER as written), then by §VII.BS NNU it is `M_KK · (free dial)` — a surface compute pins only the dimensionless multiplier, the comparison to NICER's 2.08 M_⊙ is not substrate-pinned, and on-disk evidence (C_max sub-floor after repair, CO2-FALSIFIER blocked) points at a weak one-directional gravastar no-go. **Reading B (growth) wins on EVOI**, because its falsifier is dimensionless-anchored and pre-registrable today.
- If Reading A can re-cast its falsifier as a **weight-free dimensionless dense-matter discriminant** — the durable W2-1 SIGN-PASS (`dΔ/dμ > 0`) tied to a dimensionless terrestrial band (FRIB symmetry-energy slope L), NOT M_max in M_⊙ — then it escapes the NNU keystone and becomes a legitimate weight-free competitor to the growth gate, and the contest turns on relative tractability and σ-reach of the two weight-free gates. **That gate is not yet constructed**, so the R3 verdict must decide whether its *constructibility-today* matches the growth gate's (which is fully pinned now).

The fork is the same M_KK dimensionful/dimensionless split that made WS-CO-1 sterile, now applied to whether the M–R axis survives as a substrate-pinned falsifier. R3 must rule on which observable Reading A's gate actually reduces to — because that, not the existence of the EoS pipeline (conceded) and not the existence of the growth pin (verified), decides the EVOI ranking.

---

### Sources cited / verified this round
- `nazarewicz-r1.md` (the Reading-A case engaged — §1 EoS pipeline, §2 EVOI/band, §3 CORPUS-EXCEEDS construction path, §4a Track-B dual-prior, §4b WS-CO-1 scope, §4c free-dial risk, §5 S113-CO-MR-NICER gate, §6 UQ band).
- `§VII.BS` NNU rank-1 theorem: `S103-NNU-BUNDLE-EXHAUSTIVENESS` PASS (`rank=1, second_rel_sv=1.06581e-17`), `S102-NNU-FALSIFIER-II-RANK1-COVARIANCE` PASS (`max|Corr|=1.0`); `O = w·Ô`, `w = M_KK`; `get_constant("M_KK")=7.428660036284456e16 GeV` (CONST-FREEZE-42, non-superseded).
- `S110-CF-CO1-EOS` INFO verdict string: `M_max=4.783_Msun ... Delta/mu=0.102_band[0.03,0.3] ... C_max=2.26e-04_floor1e-03 ... runaway 4.821->0.102` (the repaired EoS is still 4.4× sub-floor compact — Track-B evidence).
- `S110-CF-CO2-FALSIFIER` FAIL: `value='PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE'` (the dimensionful-CO falsifier gate, blocked upstream).
- `INV13-W2-2-FSIGMA8-GROWTH-S8` PASS (companion rows): `bindable_DESI5yr=1bins Euclid=7bins`, `max 1.001σ@z0.5`, reproduces Row #71 σ-dist `1.013 DESI-Y5 / 1.534 Euclid`; `growth sigma8=0.79317 USED NOT OZ 0.79900`; S8_FW=0.8128, PRODUCT −4.058% (C5 guard).
- Row #71 / Row #71.aug-S110-LSS-FLAGSHIP (f·σ₈ UP-side LSS handle, DESI-5yr→Euclid σ-budget); Row #88 (CORPUS-EXCEEDS: no formation channel / no self-bound surface, "ECO program cannot refute, only expose the gap").
- Framing law `phononic-framing.md` (substrate-IS, `D_K → a₂ → D(a) → f·σ₈` forward); `evoi-prioritization.md` (EVOI = P(pass)·|ΔP_pass| + P(fail)·|ΔP_fail|).
