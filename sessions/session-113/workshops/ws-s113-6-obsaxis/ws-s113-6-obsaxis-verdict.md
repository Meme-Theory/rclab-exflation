# WS-S112-6 OBSAXIS — R3 Structural Verdict (open)

**Workshop**: WS-S112-6 OBSAXIS — the CMB-orthogonal observational steer (NICER dense-matter EoS vs DESI/Euclid f·σ8 growth)
**Date**: 2026-06-22
**Participants**: nazarewicz-nuclear-structure-theorist (Reading A — NICER dense-matter EoS / pulsar M–R) · mack-cosmic-bridge (Reading B — DESI/Euclid f·σ8 growth-suppression)
**Format**: 3-round open-verdict adversarial workshop (R1 steelman / R2 rebuttal / R3 converge)
**Verdict author**: nazarewicz-nuclear-structure-theorist (writing the NEUTRAL converged verdict; the assigned Reading-A pole holds the conservative standard and concedes where the on-disk ledger forces it)
**Adjudication question**: Which non-CMB axis (NICER dense-matter EoS vs DESI/Euclid f·σ8 growth) is the higher-EVOI, more-tractable next falsifiable substrate prediction, and what is its pre-registrable gate?

All load-bearing numbers below were independently re-verified against the on-disk verdict ledger and canonical constants this round (not taken from either participant's summary).

---

## 1. Each agent's FINAL lean (from their R2)

**nazarewicz (Reading A) — R2 final lean:** Moved substantially toward Reading B. "Growth is the higher-EVOI *next pre-registrable* prediction" — conceded the tractability term: the recorded head-to-head pair (`INV13-W2-2 PASS` / `INV13-W2-1 FAIL`) is real, the f·σ8 −4.058% suppression is a pinned zero-parameter already-once-passed flagship, and R1 conflated *leverage* (factor-30 M_max band) with *tractability* (a band wide because the surface is a free dial is under-determined, not high-information). Surviving residual: `S110-CF-CO1-EOS` (which predated mack's R1) fixed the *named cause* of the W2-1 FAIL (runaway Δ/μ 4.821→0.102 via a substrate-honest self-consistent μ_eff, not ansatz-forced), so dense-matter is FAIL→INFO with one pathology (the surface/compactness) remaining, not "12× off and dead." Crux left for R3: is EVOI scored on *pre-registrable-today* (growth wins) or *information-per-fixed-wave* (contestable)?

**mack (Reading B) — R2 final lean:** Retained Reading B, but **narrowed** from R1's "by a clear margin / wide gap" to "by a structural margin, conditional on the dimensionful/dimensionless distinction." Conceded cleanly that the interior EoS pipeline exists and runs (his R1 over-read Row #88). Core rebuttal: M_max is a mass, so by §VII.BS NNU (STAGE-3-PERMANENT) `M_max = M_KK · M̂_max` — a surface compute pins only the dimensionless multiplier M̂_max, never the dimensionful M_max NICER measures, because M_KK is the framework's one permanently-unanchored weight. Supported by two on-disk facts: `S110-CF-CO1-EOS` compactness `C_max = 2.26e-4 < `its own `1e-3` floor (Track-B structural-dilution evidence), and `S110-CF-CO2-FALSIFIER: FAIL` (the dimensionful CO-falsifier gate mechanically blocked by WS-CO-1 STERILE). Crux left for R3: does the dense-matter headline falsifier reduce to a dimensionless, M_KK-weight-free observable, or does it ride the M_KK keystone?

**Convergence**: both participants independently arrived at the *same fork* — the M_KK dimensionful/dimensionless split. This is genuine convergence, not a stalemate. The two cruxes (i) and (ii) are the same structural question stated from two sides.

---

## 2. The crux (TRACTABILITY)

The neutral crux, sharpened by both R2 rounds to its load-bearing core:

> **A NICER dense-matter prediction is constructible from the substrate at the DIMENSIONLESS level, but its headline observable as written (M_max in M_⊙, compactness C against NICER) is M_KK-weighted — and M_KK is the framework's one permanently-unanchored import (§VII.BS NNU, STAGE-3-PERMANENT). The f·σ8 growth prediction, by contrast, is built entirely on weight-free dimensionless observables (S8 ratio, fractional f·σ8 suppression) that the NNU theorem leaves anchored, and is pinned + once-passed today.**

The tractability question is therefore NOT "does the substrate have a compact-object sector" (the workshop settled this: it has a *half*-sector — interior EoS present via INV13/S110-CO1/INV11, exterior self-bound surface absent — and CFL is its native dense phase, the same SU(3) that color-locks). It is the finer:

**Can the dense-matter axis's *falsifier* be pinned FROM THE SUBSTRATE today, or does it ride the M_KK free dial in exactly the direction NICER measures?**

The substitution chain that decides it (mack R2 §2, conceded by nazarewicz as the unanswered crux of his own R2):

```
Step 1: M_max = M_KK · M̂_max                       [§VII.BS NNU: O = w·Ô, w = M_KK]
Step 2: M̂_max = f(μ̂_surface, Δ̂(μ̂), TOV)            [dimensionless TOV sequence, substrate-fixed]
Step 3: a substrate Δ(μ)→0 edge solve pins μ̂_surface [dimensionless — the tractable compute proposed]
Step 4: M_max = M_KK · M̂_max STILL carries M_KK     [the weight is un-fixed by §VII.BS]
Conclusion: the surface compute pins the DIMENSIONLESS M̂_max; it does NOT pin the
            dimensionful M_max in M_⊙ against NICER's 2.08 M_⊙ unless M_KK is
            independently fixed — and M_KK is permanently unanchored.
```

On-disk evidence the dilution is *structural* (not a missing-surface artifact, i.e. nazarewicz's own dual-prior Track B): the self-consistent repair `S110-CF-CO1-EOS` fixed the gap ratio (4.821→0.102, into the physical CFL window) but left `C_max = 2.26e-4` — **4.4× below its own 1e-3 floor and ~1100× below NICER's C ≈ 0.25**. The repair that fixed the gap moved the compactness *not at all*. And the framework's own attempt to mint a dimensionful compact-object falsifier, `S110-CF-CO2-FALSIFIER`, is on disk as **FAIL / `PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE`**.

The growth side of the crux is settled by verification, not argument: `INV13-W2-2-FSIGMA8-GROWTH-S8: PASS` (`sign+magnitude+regime` all PASS), `S8_FW=0.8128` in-band, 16/16 z-bins sign-negative, `bind_DESI5yr_max=1.001σ@z0.5`, `bind_Euclid_max=1.516 (7 bins)`, reproducing the upstream Row #71 forecast σ-distance (1.013σ DESI-Y5 / 1.534σ Euclid) by applying the **fetched** DESI-Y5/Euclid RSD forecast covariance to the substrate's own suppressed curve. The discriminating observables (S8 ratio, −4.058% product suppression, f·σ8 shape) are `Ô`-type — weight-free.

---

## 3. STRUCTURAL VERDICT

**RANK (synthesis, "both, in this order"):**

**#1 — DESI/Euclid f·σ8 growth-suppression (Reading B) is the higher-EVOI, more-tractable next falsifiable substrate prediction.**

**#2 — NICER dense-matter EoS (Reading A) is the higher-*leverage* axis, but its pre-registrable falsifier survives ONLY in a weight-free dimensionless form (the W2-1 SIGN-PASS `dΔ/dμ>0`, or a FRIB symmetry-energy-slope L discriminant) — NOT as the M_max-in-M_⊙ / compactness gate as originally written, which is structurally a free dial.**

**First-principles reason (the structural core):** The framework's §VII.BS NNU theorem (rank-1, `second_rel_sv=1.066e-17`, STAGE-3-PERMANENT) factors every dimensionful substrate observable as `O = M_KK · Ô` with M_KK the single permanently-unanchored weight. This theorem partitions BOTH candidate axes by whether their headline falsifier is `Ô`-type (weight-free, substrate-pinned) or `O`-type (weight-riding, free-dial):

- **f·σ8 growth is `Ô`-type.** Its falsifier observables (S8 ratio, fractional f·σ8 suppression, spectral shape) carry no M_KK weight; the −4.058% product suppression is a fractional deviation, dimensionless by construction. The NNU theorem leaves it anchored. ⇒ pre-registrable today with a real substrate σ-distance against a fetched forecast covariance.
- **NICER M_max / compactness as written is `O`-type.** M_max is a mass, C is set at an M_KK-weighted physical density. The NNU theorem proves a surface compute pins only M̂_max (dimensionless), leaving the comparison to NICER's 2.08 M_⊙ a free dial. ⇒ NOT pre-registrable-survivable today; the proposed ~2–3-wave surface compute narrows the dimensionless multiplier but cannot anchor the dimensionful comparison.

This is the *same* M_KK dimensionful/dimensionless split that rendered the compact-object sector STERILE in WS-CO-1 (S110) — there it made the dimensionless ratios Kerr-degenerate; here it makes the dimensionful M_max a free dial. The compact-object sector's framework-specific content "rides M_KK" on both the ratio axis (WS-CO-1) and the magnitude axis (this workshop). The growth axis is the framework's only non-CMB falsifier surface whose headline observable sits on the *anchored* side of the NNU partition.

**Tractability reason (the EVOI metric):** EVOI = P(pass)·|ΔP_pass| + P(fail)·|ΔP_fail| rewards an axis where BOTH legs are pre-registrable and move the posterior:
- **Growth**: P(pass) HIGH (already PASS once, DESI ~1.0σ → Euclid ~1.5σ/7-bins sharpening); |ΔP_pass| LARGE (zero-parameter confirmation on a not-built-for dataset = independent-confirmation gold, the §EVOI.BF UP-side LSS handle); |ΔP_fail| LARGE (a measured f·σ8 above the suppressed value at decisive σ cleanly refutes the a₂-growth channel). Both legs large, work-to-falsifiability ≈ 0.
- **NICER as written**: P(pass) for a survivable M–R discrimination is near-zero today (C sub-floor after repair; the dimensionful M_max is a free dial); |ΔP_fail| is weak and *one-directional* (Row #88: "the ECO program cannot refute it; it can only expose the gap" — a dilute-gravastar no-go, equally Kerr-and-framework, Occam favors Kerr). The high-EVOI version requires first deriving the surface AND independently fixing M_KK — neither is a "next falsifiable prediction."

**Why this is a synthesis, not an elimination:** Reading A is ranked #2, not closed. Two assets survive every rebuttal: (a) the **W2-1 SIGN-PASS** (`dΔ_CFL/dμ > 0` at every scan point) is a genuine, dimensionless, weight-free substrate prediction about diquark density-dependence — it sits on the ANCHORED side of the NNU partition; (b) the dense-matter axis carries a **terrestrial FRIB cross-check** (Paper 25, Sorensen+ 2024: symmetry-energy slope L ≈ 40–70 MeV at the same density NICER probes) that the growth axis structurally lacks. Both R2 rounds independently identified that the surviving, pre-registrable dense-matter gate is a *weight-free dimensionless discriminant* (sign-of-stiffening, or L), NOT M_max-in-M_⊙. That gate is legitimate and more honest than S113-CO-MR-NICER — but it is narrower and **not yet constructed**, so it ranks below the fully-pinned growth gate on tractability-today while remaining the higher-leverage construction to fund next.

---

## 4. Forward artifact — RANKED pre-registrable forward gate

### Gate #1 (the chosen axis — pre-registrable TODAY): `CF-S113-FSIGMA8-EUCLID-7BIN`

4-field spec:

1. **What (observable / substrate-derived prediction + σ-distance):** the framework's zero-parameter f·σ8(z) curve — `f_FW(0) = 0.5254916357`, `σ8_growth_a2 = 0.79317`, product suppression **−4.058% @ z=0.51** (the −4.058% PRODUCT, never the −0.311% bare-f; C5 conflation guard) — tested as a joint χ² against the RSD f·σ8 template, substrate-first chain `D_K → a₂ Seeley-DeWitt → D(a) → f(z) → f·σ8(z)`. Pre-registered σ-budget (already pinned, Row #71, fetched forecast covariance): per-bin Euclid ~1.5σ, **joint 7-bin ≈ 1.534σ (approaching decisive)**; DESI-5yr ~1.013σ @ z≈0.5 is the near-term marginal anchor. PASS = suppressed FW curve within the joint Euclid 1σ envelope (zero-parameter prediction survives on a non-CMB dataset); FAIL = joint σ-distance ≥ pre-registered decisive threshold (a₂-growth channel excluded). **Anti-rescue fence: σ8_growth=0.79317 USED, NOT the O-Z headline 0.79900; the −4.058% PRODUCT is the test quantity, NOT bare-f −0.311%; zero branch/scheme freedom.**
2. **Dataset:** DESI-DR2 RSD f·σ8 (near-term marginal anchor) → **Euclid DR1 RSD across the 7 spectroscopic z-bins (z ≈ 0.9–1.8)** (decisive instrument).
3. **σ-distance:** joint ≈ 1.534σ over 7 Euclid bins (pinned via the fetched DESI-Y5/Euclid forecast covariance, `s96_obs_fsigma8_forecast.npz`).
4. **Effort:** ~1 wave (every input — prediction value, σ-budget, instrument, observable, anti-rescue fence — is already pinned; this is the Euclid build-out Row #71 already flags as the remaining W6-class compute CF).

### Gate #2 (the higher-leverage axis — RANKED below #1; weight-free re-cast, NOT yet constructed): `CF-S113-CO-SIGNDISC-FRIB-L` (proposed)

4-field spec:

1. **What:** the **weight-free** dense-matter discriminant that escapes the NNU keystone — tie the durable W2-1 SIGN-PASS (`dΔ_CFL/dμ > 0`, a dimensionless sign, M_KK-free) to a dimensionless terrestrial observable: the substrate-derived symmetry-energy slope L (or the dimensionless EoS-stiffening-sign at supra-saturation), tested against the FRIB-constrained `L ≈ 40–70 MeV` band (Paper 25). This REPLACES the free-dial S113-CO-MR-NICER (M_max-in-M_⊙ / C, both M_KK-weighted — structurally un-pinnable per §3); it tests only `Ô`-type content. **Explicit discipline: no M_max-in-M_⊙ comparison; tuning the surface to hit a dimensionful target is ansatz-forced PASS (PROHIBITED Class 4).**
2. **Dataset:** FRIB heavy-ion symmetry-energy data (terrestrial) + the Sorensen+ 2024 combined band (χEFT + HIC + neutron-star); secondary consistency cross-check against NICER R_{1.4} ≈ 12–13 km *as a dimensionless-ratio consistency test only*, not a primary mass discriminator.
3. **σ-distance:** TBD — requires the construction in (4); the gate's first job is to determine whether a weight-free dense-matter discriminant has any detector-reachable σ at all.
4. **Effort:** ~2–3 waves (genuinely not-yet-constructed: derive the dimensionless discriminant from the substrate, map it to FRIB L, establish whether it has σ-reach). This is the higher-*leverage* construction (it would open a terrestrial-anchored, FRIB-cross-checked falsifier the growth axis lacks) — funded AFTER Gate #1, conditional on the weight-free re-cast being shown constructible.

### Routing (falsifier-surface writes — mack-cosmic-bridge sole writer)

Per `feedback_mack-bridge-role.md` and the canonical write-order, the falsifier-inventory edits are **routed to mack-cosmic-bridge** (NOT written here):

- **ROUTE-mack #1:** `sessions/framework/registry/falsifier-master-inventory.md` Row #71 — append an additive σ-distance sub-row for `CF-S113-FSIGMA8-EUCLID-7BIN` (Euclid 7-bin joint ≈ 1.534σ; DESI-DR2 anchor ~1.013σ). The f·σ8 growth axis is re-confirmed by this workshop as the **#1 non-CMB pre-registrable falsifier** (the §EVOI.BF UP-side LSS handle).
- **ROUTE-mack #2:** `sessions/framework/registry/falsifier-master-inventory.md` Row #88 (the COMPACT-OBJECT-SECTOR GAP record) — annotate with the WS-S112-6 OBSAXIS verdict: the dimensionful M_max/compactness falsifier is **structurally a free dial** (M_max = M_KK·M̂_max, §VII.BS NNU), confirmed by `S110-CF-CO1-EOS` (C_max=2.26e-4 sub-floor after gap-repair → Track-B intrinsic dilution) and `S110-CF-CO2-FALSIFIER` FAIL (blocked). The surviving dense-matter falsifier is the **weight-free SIGN-PASS / FRIB-L discriminant** (Gate #2, not-yet-constructed); cross-link to the WS-CO-1 STERILE precedent (same M_KK split). NO canonical_constants pin (the verdict mints no value).
- **ROUTE-mack #3 (watchlist):** add `CF-S113-CO-SIGNDISC-FRIB-L` to the falsifier-watchlist as a *constructibility-pending* candidate (higher-leverage, weight-free, FRIB-anchored; ranked #2; fund after Gate #1).

---

## 5. Residual dissent + the decisive next step

**Residual dissent (narrow, honest):** The verdict ranks growth #1 and dense-matter #2, and both participants converged on that ordering. The *residual* disagreement is over the SIZE of the EVOI gap, and it reduces to one un-adjudicated sub-question both R2 rounds flagged: **if EVOI is scored on "information-per-fixed-compute-wave" rather than "pre-registrable-today,"** the growth Gate #1 PASS branch *confirms an already-passing* zero-parameter prediction (diminishing |ΔP_pass| — it survived once already), whereas a successful weight-free dense-matter Gate #2 would resolve a *never-answered* binary (does the substrate have a weight-free dense-matter discriminant with detector reach?) with undiluted |ΔP|, against a dataset (FRIB + NICER) already in hand. nazarewicz holds this keeps the gap narrower than mack's "structural margin" implies; mack holds that constructibility-today is the binding EVOI criterion and Gate #2 is not yet constructed. **This dissent does not change the RANK** (Gate #1 is pre-registrable now and weight-free; Gate #2 is neither) — it only bears on how much earlier Gate #2 should be funded relative to a third growth refinement.

**The decisive next step:** Run **Gate #1 (`CF-S113-FSIGMA8-EUCLID-7BIN`) now** — it is fully pinned, weight-free, and sharpens the framework's #1 non-CMB falsifier on the decisive instrument. **In parallel, scope (do not yet fully run) Gate #2's constructibility question:** can a weight-free dimensionless dense-matter discriminant (W2-1 SIGN-PASS tied to FRIB L) be derived from the substrate with any detector-reachable σ? That single constructibility check resolves the residual dissent: if YES, dense-matter becomes a legitimate weight-free competitor and the FRIB cross-check makes it the higher-leverage second falsifier; if NO, the dense-matter axis is confirmed as a structural no-go (Track B — intrinsic dilute gravastar, M_KK-weighted all the way down) and the framework's non-CMB falsifier surface is the growth axis alone. Either outcome is decisive constraint-map information.

**Bottom line:** Growth (f·σ8) is the higher-EVOI, more-tractable next falsifiable prediction — #1, pre-registrable today, weight-free. Dense-matter (NICER) is the higher-leverage axis but its M_max/compactness falsifier rides the M_KK keystone and is structurally a free dial; it survives at #2 only re-cast as a weight-free SIGN-PASS / FRIB-L discriminant that is not yet constructed. The campaign should run the growth gate now and fund the dense-matter weight-free re-cast as the ranked-second construction.
