# Session 114 Wave 1 — Observational Frontier (CMB-orthogonal forward-EVOI axis) (Results Working Paper)

**Session**: 114 | **Wave**: 1 | **Plan**: session-114-plan-w1.md | **Theme**: the §EVOI.BF CMB-orthogonal forward-EVOI axis — the #1 non-CMB falsifier f·σ8 growth filled against the decisive Euclid 7-bin RSD instrument, plus the weight-free constructibility SCOPE of the #2 dense-matter (FRIB-L) axis on the anchored side of the §VII.BS NNU partition.

## Gate Sections

### §W1-1. CF-S113-FSIGMA8-EUCLID-7BIN (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `CF-S113-FSIGMA8-EUCLID-7BIN`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (f·σ8 growth = interference pattern of post-transit GGE acoustic excitations, gravitationally self-organized through the a_2 Seeley-DeWitt channel)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: the framework's zero-parameter f·σ8(z) curve sits within the joint Euclid 7-bin RSD 1σ envelope — the suppressed a_2-growth-channel prediction survives on a non-CMB dataset at a joint σ-distance below the 3σ decisive threshold.
**Plan reference**: `sessions/session-plan/session-114-plan-w1.md` §W1-1 (operator, 3.0σ decisive boundary, machinery pin, substitution chain, Input-SHA ledger).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script**: `computations/session-114/s114_w1_fsigma8_euclid_7bin.py` — present; `grep -E "from canonical_constants import|print_verdict_payload"` → both present (`from canonical_constants import *` + the explicit 4-name import on line 79–85; `def print_verdict_payload` + the call in `main()`).
- **Data**: `computations/session-114/s114_w1_fsigma8_euclid_7bin.npz` — present (joint/per-bin/cross-check/fence arrays + canonical pins + verdict fields).
- **Plot**: `computations/session-114/s114_w1_fsigma8_euclid_7bin.png` — present (left: fs8_FW vs fs8_LCDM on the 7-bin grid with Euclid 1σ; right: per-bin `|r|/σ` bars with the per-bin-max / joint-σ / 3σ-decisive horizontals).
- **Verdict line**: `computations/session-114/s114_gate_verdicts.txt` — `CF-S113-FSIGMA8-EUCLID-7BIN: PASS …` matches `^CF-S113-FSIGMA8-EUCLID-7BIN:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + the `[SIGN]` 3-tuple companion row (`sign=PASS magnitude=PASS regime=VALID`) + 2 extra annotation rows all landed via the race-safe `emit_verdict` MCP tool (5 rows; sig_5-unique, cross-process locked).
- **WP §W1-1**: this section, carrying Status / Verdict / Output Artifacts / MCP Pre-Compute Audit markers. Verification is by content-presence regex, never line/byte counts.

**MCP Pre-Compute Audit**:
- `search_knowledge("fsigma8 Euclid 7-bin joint chi-squared growth a_2 channel sigma distance")` → surfaced `INV13-W2-2-FSIGMA8-GROWTH-S8: PASS` (`bind_Euclid_max=1.516` per-bin; `product_supp_max=-4.058%@z0.51`), `S96-OBS-FSIGMA8-FORECAST: INFO` (`sigma_Euclid_max=1.534@z0.51` — flagged "max", i.e. **per-bin**), and `INV7-W1-6: INFO` (`joint_sigma_Euclid=2.963` — the **joint** value under an older covariance/threshold). This established that the joint number was already ~2.96σ and that the plan's "≈1.534σ" is the per-bin max, not the joint.
- `get_constant("f_FW")` → `0.5254916357116971` (S96; s70_bulk_flow.npz).
- `get_constant("sigma8_growth_a2")` → `0.79317` (S98; channel-distinct from O-Z `sigma8_OZ_50`≈0.799 — the anti-rescue fence value).
- `get_constant("f_LCDM")` → `0.5271303865722888` (S96).
- `get_constant("fsigma8_product_suppression_FW_max_pct")` → `-4.058` (S96; the PRODUCT-suppression peak @ z=0.51).
- **Not PRE-CLOSED**: the *joint 7-bin χ²* on the *current canonical S96 covariance* with the 3σ-decisive pre-registration is a new compute (prior gates emitted per-bin maxes or a joint value on an older covariance). The gate fills the joint σ-distance the plan flagged as the remaining W6-class CF.

**Verdict**: **PASS** (composite). `sign_verdict=PASS`, `magnitude_verdict=PASS`, `regime_verdict=VALID` (collapse rule → PASS). The 0-parameter suppressed f·σ8 curve is **not excluded** by the decisive Euclid 7-bin RSD forecast — joint σ-distance **2.9614σ**, just inside the 3σ decisive boundary (margin +0.0386σ).

**Results**:

*Headline.* Joint 7-bin σ-distance against the fetched DESI-Y5/Euclid RSD forecast covariance:

| Quantity | Value | Boundary | Verdict |
|:---------|:------|:---------|:--------|
| **σ_joint (Euclid, joint 7-bin, √χ²)** | **2.9614σ** (χ²=8.7700) | 3.0σ decisive (PASS iff ≤) | **PASS** (margin +0.0386σ) |
| σ_joint (DESI-Y5, joint 7-bin) | 1.9545σ (χ²=3.8202) | — (near-term anchor) | — |
| per-bin max \|r\|/σ_euclid (z=0.51) | 1.5345σ | — (this is the plan's "≈1.534") | per-bin cross-check |
| sign vector | **7/7 bins suppressed below LCDM** | every bin r<0 | sign **PASS** |

*Per-bin table (Euclid forecast; residual r = fs8_FW − fs8_LCDM against the LCDM fiducial):*

| z | fs8_FW | fs8_LCDM | r = FW−LCDM | σ_euclid | \|r\|/σ_euclid |
|:--|:-------|:---------|:------------|:---------|:--------------|
| 0.150 | 0.442816 | 0.458702 | −0.015885 | 0.052800 | 0.30086 |
| 0.380 | 0.456881 | 0.476090 | −0.019209 | 0.014850 | 1.29353 |
| 0.510 | 0.454956 | 0.474198 | −0.019242 | 0.012540 | **1.53447** |
| 0.700 | 0.444128 | 0.462065 | −0.017937 | 0.014190 | 1.26404 |
| 0.850 | 0.431442 | 0.447786 | −0.016343 | 0.011550 | 1.41502 |
| 1.050 | 0.411689 | 0.425707 | −0.014019 | 0.014850 | 0.94401 |
| 1.520 | 0.362921 | 0.372172 | −0.009251 | 0.023100 | 0.40049 |

*Cross-checks (all at machine zero or pin precision):*
- Matrix quadratic form `r^T C^{-1} r` vs scalar quadrature `Σ(r/σ)²`: residual **0.00e+00** (the forecast covariance is **diagonal** — no off-diagonal RSD correlations are stored in `s96_obs_fsigma8_forecast.npz`; confirmed no 2D array present — so `C^{-1}=diag(1/σ²)` exactly).
- Stored per-bin `nsig_FW_euclid` reproduction: residual **0.00e+00**.
- Product-suppression peak: **−4.0578% @ z=0.51** vs canonical `fsigma8_product_suppression_FW_max_pct=-4.058` (residual 1.52e-04 = rounding of the 4-sig-fig canonical).
- Curve fidelity sanity: `|f_FW_npz − canonical|/canonical = 0.00e+00`, `|f_LCDM_npz − canonical|/canonical = 0.00e+00` (≤ 1e-6 ✓).

*Anti-rescue fences (load-bearing, all enforced):*
- `sigma8_growth_a2 = 0.79317` USED — the a_2-growth channel readout, **NOT** the O-Z/spectral-action channel 0.799 (fence checked: `|0.79317 − 0.799| > 1e-3` ✓; matches npz `sigma8_FW`=0.79317 ✓).
- The **PRODUCT** fs8 = f·σ8 is the test quantity (peak suppression −4.058%), **NOT** bare-f (−0.311%).
- Zero branch/scheme freedom: the residual is against the LCDM fiducial (`r = fs8_FW − fs8_LCDM`), **not** tuned against the scattered mock `fsig8_obs` realization.

*4-tuple:* `(value=2.9614, scheme=FW-a2-growth-channel, convention=PRODUCT-SUPPRESSION, L_max=N/A)`.

*Substitution chain (plan Step 1–6, with substituted numbers — the suppression/sign claim):*
- **Step 3** (z=0 amplitude ratios): `σ8_FW(0)/σ8_LCDM(0) = 0.79317/0.811 = 0.97802 < 1`; `f_FW(0)/f_LCDM(0) = 0.5254916357/0.5271303866 = 0.99689 < 1`.
- **Step 4** (product ratio at z=0): `fs8_FW(0)/fs8_LCDM(0) = 0.99689 · 0.97802 = 0.97499` ⇒ −2.501% at z=0, deepening to the −4.058% peak @ z=0.51 because `D_FW(z)/D_LCDM(z)` diverges further below unity off z=0.
- **Step 5** (sign read-off): both factors < 1 ⇒ `fs8_FW(z) < fs8_LCDM(z)` at every z ⇒ residual negative in every Euclid bin ⇒ **sign_verdict = PASS** (computed: 7/7 negative).
- **Step 6** (magnitude): `σ_joint = √(r^T C^{-1} r) = 2.9614σ ≤ 3.0σ` ⇒ **magnitude_verdict = PASS**.

*Dual-SHA:* `audit_sha256=eeebc84c7685afff4a1ef6391432b58a649a8167f83f49d45306c729fe8bf6fe` (script ∥ canonical ∥ pinmap), `content_sha256=35bdbbde3e2ded0b67689211be269697772fbc0ffb12fe449726f2042bc2fece` (script only). Input SHAs matched the plan Input-SHA ledger exactly: `canonical_constants.py`=`9ee1a113…`, `s96_obs_fsigma8_forecast.npz`=`b84a49fb…`.

*Plan-vs-reality correction (no-technical-debt, fixed in-section).* The plan §W1-1 and the WP skeleton pre-registered the joint at "≈1.534σ" and named "≈1.516 (INV13-W2-2)" as the per-bin cross-check. The npz makes the layering unambiguous: **1.5345 is the PER-BIN MAX** (`max_nsig_euclid`, the single most-discriminating bin at z=0.51), and **1.516 is the INV13-W2-2 per-bin max under its own curve build** — neither is the joint. The genuine joint diagonal 7-bin value is **σ_joint = 2.9614σ**, which reproduces the older `INV7-W1-6 joint_sigma_Euclid=2.963` to rounding (the small 0.002 difference is the older covariance's rounding). The headline reports the *correct* joint 2.9614σ; the per-bin max is pinned as the cross-check. Both readings are below the 3σ decisive boundary, so the verdict is **PASS regardless** — but the honest joint number sits much closer to the boundary (+0.0386σ) than the plan's per-bin "1.534" implied. This is recorded in the verdict-line extra rows and routed to the wave-synthesis as a plan-pin correction.

*Solution-space (PASS_meaning).* The a_2 Seeley-DeWitt growth channel remains **viable**: the framework's #1 non-CMB falsifier survives on the decisive Euclid instrument with **zero free parameters** — a suppressed-growth prediction not excluded on a dataset not built for it (the §EVOI.BF UP-side LSS handle). The narrowness of the margin (2.96σ vs 3σ) makes this falsifier **live**: the actual Euclid DR1 RSD release is decisive — a measured f·σ8 at or above the LCDM value with the forecast precision would push the joint past 3σ and close the corridor.

*Mack-sole-writer hand-off (canonical write-order Step 3):* the Row #71 joint-χ² σ-distance sub-row is landed below in this same session (I am both the executor and the inventory sole writer). The constant `f_FW`/`sigma8_growth_a2` are already canonical (no `update_constant` owed — the gate consumes them, it does not mint a new prediction value; the joint σ-distance is a derived falsifier-surface number, recorded in the inventory, not a new `canonical_constants` pin).

---

### §W1-2. CF-S114-CO-SIGNDISC-FRIB-L-SCOPE (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S114-CO-SIGNDISC-FRIB-L-SCOPE`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (dense-matter CFL diquark-condensate density-dependence — representation-theoretic D_K content of the SU(3) that color-locks; the FRIB-L mapping leg is methodological)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: a weight-free dimensionless dense-matter discriminant built from the W2-1 SIGN-PASS (dΔ_CFL/dμ>0, M_KK-free) maps onto the FRIB-constrained symmetry-energy slope L (≈40–70 MeV, Sorensen+ 2024) with a detector-reachable σ — i.e. the #2 dense-matter axis is CONSTRUCTIBLE as an Ô-type (weight-free) falsifier rather than a structural no-go.
**Plan reference**: `sessions/session-plan/session-114-plan-w1.md` §W1-2 (set-membership operator, NON-COMPUTE PRDR (2)(3)(4) N/A, dual_prior, substitution chain, Input-SHA ledger).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | `must_contain` (verified by content-regex) |
|:---------|:-----|:-------------------------------------------|
| script | `computations/session-114/s114_w1_co_signdisc_frib_l_scope.py` | `from canonical_constants import` ✓; `print_verdict_payload` ✓ (def + call) |
| data | `computations/session-114/s114_w1_co_signdisc_frib_l_scope.npz` | present (12,727 bytes); round-trips verdict=FAIL / branch=STRUCTURAL-NO-GO ✓ |
| plot | `computations/session-114/s114_w1_co_signdisc_frib_l_scope.png` | present (79,904 bytes); 2-panel (dΔ/dμ scan + dimensionless L/J band vs substrate g) ✓ |
| verdict line | `computations/session-114/s114_gate_verdicts.txt` | `^CF-S114-CO-SIGNDISC-FRIB-L-SCOPE:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ (no [SIGN] 3-tuple — [VERIFY] constructibility gate, per plan `schema_v2_3tuple_required: false`) |
| WP section | this §W1-2 | Status/Verdict/Output Artifacts/MCP Pre-Compute Audit markers ✓ |

`audit_sha256 = faea15a71fddfe5bacee34f35a832cb8234eac4b92ed77c907320fd02d3ae8a2`
`content_sha256 = 84c4c1bb80c69a6730b4b1a6fb28f98ab7ebf02dc28e09ab2a6f239282a52563`
(audit over `script || canonical_constants.py || pinmap_json`; content over script bytes. Input-SHA ledger: all three plan-pinned input SHAs reproduced EXACTLY at runtime — `canonical_constants.py = 9ee1a113…`, `inv13_w2_1 = d14b8ad1…`, `s110_cf_co1 = 14550f36…`.)

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("CFL diquark gap dDelta dmu finite mu sign symmetry energy slope dense matter")` → returned **INV13-W2-1-FINITE-MU-CFL-EOS** (`dDelta/dmu>0=True`, `Delta_CFL_plateau=2.4107 M_KK`, `gap_ratio=4.8213` runaway, FAIL on the dimensionful M_max leg) + **S110-CF-CO1-EOS** (`Delta/mu=0.102` self-consistent, `C_max=2.26e-04 < floor 1e-03`, INFO) + the **CFL** PROVEN theorem (SU(3)_c × SU(3)_L+R → diagonal SU(3)). Confirms the two upstream inputs; the constructibility SCOPE itself is NOT yet evaluated.
- `search_knowledge("NNU partition M_KK Ohat rank-1 second_rel_sv dimensionful dimensionless VII.BS")` → returned **S103-NNU-BUNDLE-EXHAUSTIVENESS** (`rank=1`, `second_rel_sv=1.06581e-17`, PASS) confirming §VII.BS `O = M_KK · Ô` is STAGE-3-PERMANENT rank-1 — the structural basis for the dimensionless/dimensionful partition.
- `get_constant("M_KK")` → `7.428660036284456e+16` GeV (S42 CONST-FREEZE-42); imported ONLY to PROVE the discriminant is M_KK-invariant (never as a multiplier into the discriminant).
- `get_constant("Delta_BCS")` → `0.4642547` (R-protected, M_KK units = dimensionless ratio). A `get_constant`/`search_knowledge` probe for a symmetry-energy `S_0`/`L` constant → none exists (correctly: L is an external nuclear-physics observation, not a substrate prediction; per `substrate-first-canonical-sourcing.md §(i)` it is a methodological cross-check anchor, `# (local)` external literal).
- **NOT PRE-CLOSED**: no closure covers the constructibility SCOPE; this gate evaluates it.

**Verdict**: **FAIL — STRUCTURAL NO-GO** (set-membership: NO weight-free dimensionless discriminant maps to the FRIB L-band with resolvable σ).

**Results**:

**Set-membership verdict.** `PASS = ∃ weight-free dimensionless g(dΔ_CFL/dμ)` mapping into the FRIB L-band with `σ_reach > 0.5` AND M_KK-free; `FAIL = structural no-go`; `INFO = partial/regime-conditional`. The computed outcome is **FAIL**: `σ_reach = 0.0000 < 0.5` threshold, via BOTH the sign route AND the magnitude route (detailed below). The map IS provably M_KK-free (`map_M_KK_free = True`), but it does not reach the band — so the failure is genuinely structural, NOT a rescue-fence trip.

**(A) The dimensionless/dimensionful partition of the W2-1 npz** (anti-rescue `DIMENSIONLESS-OHAT-ONLY`):

| side | keys | enters discriminant? |
|:-----|:-----|:---------------------|
| **DIMENSIONLESS (Ô-type, admissible)** | `dDelta_dmu` (median 4.772, range [1.084, 7.237]; `[Δ]/[μ]` ⇒ M_KK-free), `sign_pass=True`, `frac_increasing=1.0`, `eos_gap_ratio_Delta_over_mu` (4.821 runaway → `ratio_plateau=0.1017` self-consistent), `ratio_plateau=0.1017` | **YES** |
| **DIMENSIONFUL (M_KK-inherited, FORBIDDEN)** | `eos_B_eff_MeV_fm3_dimensionful_MKK_inherited` (=1.75e+72, the tell of an M_KK-ridden quantity), `M_max_Msun`, `eps_c_grid`, `eos_eps_cond_MKK4` | **NEVER** (present-but-untouched; programmatically asserted) |

The fence is not a tautology: the M_KK-invariance test was shown to genuinely discriminate — `R_stiff` is invariant under `μ,Δ → λμ,λΔ` (base 46.90 = rescaled 46.90), whereas a dimensionful quantity like `Δ_plateau` scales by `λ ≈ 16 OOM` (0.443 → 3.29e+16) and FAILS the test. So `map_M_KK_free=True` is a real Ô-type certificate.

**(B) The candidate map g(R_stiff) = R_stiff = dln Δ/dln μ** and the dimensionless FRIB datum. The symmetry-energy slope `L = 3 n₀ (dS/dn)|_{n₀}` [MeV] is a density-derivative of the symmetry energy; its dimensionless recast is `L/J` (slope-to-value, `J = S₀ ≈ 32 MeV` external standard), so the MeV units cancel: **FRIB band `L/J ∈ [40/32, 70/32] = [1.250, 2.188]`**, central 1.719, half-width 0.469. The substrate analog of a density-derivative-of-the-condensate is the **logarithmic stiffening** `R_stiff = (dΔ/dμ)·(μ/Δ) = dln Δ/dln μ`, every factor M_KK-free. At the S110 self-consistent CFL onset (`μ_plateau=4.356`, `Δ_plateau=0.443`, `μ/Δ=9.829`): **`R_stiff = 4.772 × 9.829 = 46.90`** (`g_image = R_stiff`, identity-class dimensionless map — no MeV scale inserted, anti-rescue).

**(C) σ_reach — TWO independent failure modes, both fire:**

1. **Sign route (plan-anticipated, substitution-chain Step 5)**: `dΔ/dμ > 0` is a SIGN-PASS; `L > 0` holds for essentially every realistic nuclear EoS; so a sign-only discriminant cannot distinguish `L=40` from `L=70` MeV — it is **degenerate inside the band**, `σ_reach_sign ≡ 0`.

2. **Magnitude route (the script's substantive finding)**: `R_stiff = 46.90` does NOT land inside `L/J ∈ [1.25, 2.19]` — it overshoots the band by a factor of ~25 (`in_band = False`, `σ_reach_magnitude = 0`). **Robustness sweep**: across slope-statistics {min, median, mean, max} the smallest plausible `R_stiff = 10.66` (min slope) still exceeds the *loosest* band's (J=30 MeV) upper edge (2.33) by a factor of **4.57**; no choice lands it in-band. The only configuration that even approaches the band is the discarded inv13 *raw* runaway-onset (`R_stiff=1.004`, still below [1.25, 2.19]) — which the S110-CO1 self-consistent repair explicitly fixed and is not the physical CFL onset.

⇒ `σ_reach = max(σ_reach_sign, σ_reach_magnitude) = 0.0000 < 0.5`. The dense-matter axis is **Track-B intrinsic-dilute, M_KK-weighted all the way down**, corroborated by the S110 Track-B evidence `C_max = 2.26e-04 < C_MAX_FLOOR = 1e-03` (sub-floor compactness) and the prior S110-CF-CO2-FALSIFIER FAIL / WS-CO-1 STERILE precedent.

**Physical interpretation (nuclear-structure reading).** The substrate's CFL diquark condensate has `dln Δ/dln μ ≈ 47` — a near-step-function gap onset at the color-flavor-locking transition. The FRIB symmetry-energy slope describes `L/J ≈ 1.7`, the gentle nearly-linear density-stiffening of the *sub-saturation-to-saturation* nucleonic symmetry energy. These are different physical regimes (supra-saturation deconfined quark matter vs sub-saturation nucleonic matter) and different density-derivatives; the dimensionless substrate quantity is real and weight-free but simply does not project onto the FRIB observable's window. The only thing that *would* land in-band is a dimensionful `M_max` tuned to NICER — which the `DIMENSIONLESS-OHAT-ONLY` fence forbids (ansatz-forced PASS = PROHIBITED Class 4).

**4-tuple**: `(value="STRUCTURAL-NO-GO_σ_reach=0.0000_…", scheme=BdG-spectral-action-vanSuijlekom-Dmu, convention=DIMENSIONLESS-OHAT-ONLY, L_max=N/A)`.

**Substitution chain (plan Step 1–5, with substituted numbers):**
- Step 1 (NNU partition, §VII.BS STAGE-3-PERMANENT): `O = M_KK · Ô`, M_KK the single rank-1 unanchored weight (`second_rel_sv=1.066e-17`) ⇒ any mass/density-dimension headline rides M_KK.
- Step 2 (partition npz): dimensionful = {B_eff, M_max, eps_c, eos_eps_cond} FORBIDDEN; dimensionless = {dDelta_dmu, sign_pass, frac_increasing, gap_ratio, ratio_plateau=0.102} admissible.
- Step 3 (which side is the discriminant?): `g = R_stiff = dln Δ/dln μ`; `dΔ/dμ = [Δ]/[μ]` dimensionless; `μ/Δ` dimensionless ⇒ `g` on the DIMENSIONLESS side ⇒ Ô-type ⇒ does NOT ride M_KK (M_KK-invariance numerically PROVEN, base=rescaled=46.90).
- Step 4 (map to L): `L = 3n₀(dS/dn)` ⇒ dimensionless `L/J ∈ [1.25, 2.19]`; substrate analog `R_stiff = 46.90`.
- Step 5 (branch read-off): `R_stiff = 46.90 ∉ [1.25, 2.19]` (factor ~25 over) AND sign degenerate-in-band ⇒ **FAIL (STRUCTURAL NO-GO)**: no M_KK-free route maps to FRIB L with resolvable σ.

**dual_prior posterior re-allocation** (plan discriminator): the dual prior was Track A (CONSTRUCTIBLE) 0.50 / Track B (STRUCTURAL NO-GO) 0.50; the discriminator maps `FAIL → 0.9 to Track B`. ⇒ **posterior 0.10 Track A / 0.90 Track B**: the dense-matter axis is intrinsic-dilute and M_KK-weighted; the **growth axis (Gate 1, §W1-1) is the framework's sole non-CMB falsifier** on the anchored side of the §VII.BS NNU partition.

**Hand-off to mack-cosmic-bridge (canonical write-order Step 3; mack sole writer per `feedback_mack-bridge-role.md`)**: Row #88 (COMPACT-OBJECT-SECTOR GAP) annotation = "dense-matter axis STRUCTURAL NO-GO — weight-free FRIB-L discriminant does NOT exist (R_stiff=46.90 ∉ L/J∈[1.25,2.19] by factor ~25; sign degenerate-in-band; Track-B intrinsic-dilute, C_max=2.26e-04 sub-floor); §EVOI.BF axis confirmed SINGLE (growth alone)"; watchlist `S113-CO-SIGNDISC-FRIB-L-WATCH` → CLOSED (constructibility resolved NO-GO). Verdict audit_sha256 `faea15a71fddfe5bacee34f35a832cb8234eac4b92ed77c907320fd02d3ae8a2`; canonical_constants entry: none owed (FAIL — no new framework prediction value). I do NOT edit the inventory myself.

---

## Wave 1 Synthesis (team-lead)

Wave 1 resolved the §EVOI.BF non-CMB falsifier frontier to a SINGLE live axis. **W1-1 PASS** — the zero-parameter f·σ8 growth curve survives the decisive Euclid 7-bin RSD forecast at joint **σ_joint = 2.9614σ** (margin +0.0386σ to the 3σ decisive boundary), 7/7 bins suppressed below ΛCDM (sign PASS). The narrow margin makes it genuinely LIVE: Euclid DR1 RSD at the ΛCDM value with forecast precision would push it past 3σ. **W1-2 FAIL** — no weight-free dimensionless dense-matter discriminant maps onto the FRIB symmetry-energy slope (R_stiff = dlnΔ/dlnμ = 46.90 ∉ L/J ∈ [1.25, 2.19] by ~25×; sign degenerate-in-band; σ_reach = 0; the map IS provably M_KK-free, so the failure is structural, not a fence trip). Jointly the two verdicts collapse the §EVOI.BF dual-prior: **the growth axis (Row #71) is the framework's sole non-CMB falsifier** on the anchored side of the §VII.BS NNU partition; the dense-matter axis is Track-B intrinsic-dilute (a structural no-go on all three sub-axes — WS-CO-1 sterile ratio, M_max free-dial magnitude, degenerate-in-band sign).

### (a) Numerical revisions
- Euclid f·σ8 σ-distance: `1.534 (per-bin max @ z=0.51) → 2.96 (joint 7-bin, diagonal cov)`; DESI-Y5: `1.013 (per-bin) → 1.95 (joint)`. The plan/skeleton's "≈1.534σ joint" was a per-bin-max mislabel; the honest joint reproduces INV7-W1-6 (2.963) to rounding.

### (b) Structural changes
- §EVOI.BF non-CMB falsifier axis count: `2 candidate (growth + dense-matter) → 1 live (growth alone)`.
- Dense-matter axis: `constructibility-pending (S113 watchlist) → STRUCTURAL NO-GO (Track-B intrinsic-dilute)`.

## Carry-Forward Computations

No carry-forwards: both Wave-1 outcomes closed in-session (W1-1 PASS = growth channel viable; W1-2 FAIL = dense-matter corridor closed, a closed corridor is not a forward CF per `Investigating-Workshops.md`).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-23 | W1-1 `CF-S113-FSIGMA8-EUCLID-7BIN` | growth falsifier σ-dist per-bin ~1.5σ | **PASS** joint 2.96σ (LIVE, +0.0386σ to 3σ) | zero-parameter f·σ8 not excluded on decisive Euclid; #1 non-CMB falsifier survives |
| 2026-06-23 | W1-2 `CF-S114-CO-SIGNDISC-FRIB-L-SCOPE` | dense-matter axis constructibility-pending | **FAIL** STRUCTURAL NO-GO | no M_KK-free discriminant reaches FRIB L; §EVOI.BF axis confirmed single |
| 2026-06-23 | §EVOI.BF non-CMB surface | two candidate axes | growth axis ALONE | W1-1 PASS ∧ W1-2 FAIL |

Process observations: the diagonal-covariance forecast (`s96_obs_fsigma8_forecast.npz` stores no off-diagonal RSD correlations) makes `C⁻¹=diag(1/σ²)` exact — the joint χ² is scalar quadrature, residual 0.00e+00. The plan-pin "1.534=joint" correction is a per-bin-vs-joint layering fix (recorded in the W1-1 verdict extra rows + this synthesis), not a value error.

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict/registry | 
|:--|:--|:--|:--|:--|
| W1-1 | `s114_w1_fsigma8_euclid_7bin.py` | ✓ | ✓ | `s114_gate_verdicts.txt` (PASS) + inventory Row #71 joint sub-row |
| W1-2 | `s114_w1_co_signdisc_frib_l_scope.py` | ✓ | ✓ | `s114_gate_verdicts.txt` (FAIL) + inventory Row #88.compute-S114 |
