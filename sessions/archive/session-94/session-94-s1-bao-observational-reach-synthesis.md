# S94 Slot-1 (S-1) — BAO Peak-Position Observational-Reach Synthesis

**Agent**: `mack-cosmic-bridge` (solo `/rclab-review`; falsifier-inventory sole writer per `feedback_mack-bridge-role.md`)
**Date**: 2026-05-25
**Type**: Observational-reach audit of an EXISTING claim (`Investigating-Workshops.md §"How to identify"`: EXISTING claims that need adversarial testing). Q1b — single-axis observational translation; no two-camp tension.
**Inputs**: `sessions/archive/session-94/session-94-w5-workingpaper.md §W5-3` (gate `S94-BAO-PEAK-BRANCH`, INFO, verdict line 72 canonical / 67 superseded); `sessions/framework/registry/falsifier-master-inventory.md` Row #67; `computations/session-94/s94_gate_verdicts.txt:67-77`.
**Compute**: `computations/session-94/s94_s1_bao_observational_reach.py` (verdict-only; emits NO gate line — the W5-3 gate is already closed). Sage-QQ exact-rational cross-check confirmed all numbers.
**Scope**: VERDICT-ONLY review. No new gate. The W5-3 INFO stands unchanged; this synthesis quantifies the observational reach the WP (line 211) asserted but never converted to an observational unit, and recommends a Row #67 framing edit (effected in-session below).

---

## 1. The question

§W5-3 landed the per-gapped-branch Layer-1/Layer-2 fractional speed split **δ_b/c_b² = 0.19** (in-band on all 7 gapped branches; the satisfied disjunct of the pre-registered absolute-OR-fractional PASS band). The absolute deltas {B1:0.01516, B2:0.00038, B3:0.02654, Leggett:0.00485 M_KK} all fall below the absolute O(τ) band [0.05, 0.30] M_KK. The Goldstone branch is Killing-protected at δ = 0.000e+00 EXACT (N_peak = 1, GR-matching — the structural reason for ONE speed of light). The WP (line 211) claims a precision BAO acoustic-peak-position measurement against this per-branch prediction "is a real test (DESI / Simons / CMB-S4 data exist or are imminent)."

**But the 0.19 fractional split was NEVER converted into an observational unit** (Δθ_s, Δk in Mpc⁻¹, or Δℓ). The M_KK-unit branch speeds do not directly give a measurable BAO shift without the substrate-IS → emergent transport. This synthesis supplies that translation and tests the "real test" reach.

---

## 2. Substrate-first framing — the substrate IS the BAO acoustic signature

Per `phononic-framing.md §"IS Space, Not IN Space"`: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold=0.19))`. The BAO acoustic peak is the **interference pattern of post-transit GGE acoustic excitations propagating through the a₂ (Einstein-Hilbert) channel** — NOT a perturbation IN an expanding container. Direction of explanation flows FROM the substrate:

```
D_K eigenmodes
  → per-branch (Z_b, M_b) Layer-1 throughput speed c_b^(1)=√(Z_b/M_b)  +  Layer-2 BdG-cone speed c_b^(2)
  → per-branch dimensionless split  s_b = δ_b/c_b^(2) = 0.19  (substrate-IS, M_KK-internal)
  → [TRANSPORT T_{BZ→pivot}: effacement projection onto the emergent 4D acoustic channel]
  → fractional shift of the emergent BAO peak position  (laboratory-IN)
```

The split `s_b = 0.19` is a SUBSTRATE-INTERNAL fractional speed difference on a branch whose Layer-2 speed `c_b^(2)` is sub-luminal in M_KK units (`c_B1 = 0.0798`, all `≪ 1`). The OBSERVED BAO peak is set by the EMERGENT acoustic sound speed `c_s` (the Goldstone `c_Gold = 0.915` is the one true 4D light cone). **The internal split must be transported onto the emergent channel** — it does not directly displace the observed peak. This is precisely the `deg(T_{BZ→pivot})` transport-degree problem of `cross-pillar-bridge-anatomy.md §"Per-observable transport-degree scale-separation"` (corpus §23), the same machinery that gives n_T two scale-separated values (transit-scale +0.4676 vs CMB-pivot −3.024e-3) and α_s two (substrate-distance −0.0859 vs Goldstone-pivot ≈0).

---

## 3. The transport (substitution chain, per `math-scripts.md §"Double-Check Logic Before Compute"`)

**Claim**: the observed fractional BAO peak-position shift induced by the substrate split `s_b` is `s_b · A_eff,b`, where `A_eff,b = (c_b^(2)/c_Gold)²` is the effacement-projection weight of branch b onto the emergent 4D acoustic cone — NOT `s_b` itself.

### Step 1 — definitions
- `c_b^(1) = √(Z_b/M_b)` — Layer-1 substrate-throughput speed (`Z_b` = a₄^{ζ}-moment kinetic stiffness; `M_b` = a₂^{ζ}-moment inertia; Baptista eq 2.40). Substrate-IS, M_KK units, inside the BZ. [source: §W5-3 Step 1]
- `c_b^(2) = v_g(k)` — Layer-2 emergent-cone speed (BdG diagonalization of D_K²). Substrate-IS, M_KK units. [source: §W5-3; `canonical_constants.py` `c_B1=0.0798`, `c_B3=0.1397`, `c_Gold=0.915`]
- `s_b := δ_b/c_b^(2) = (c_b^(1) − c_b^(2))/c_b^(2)` — the DIMENSIONLESS substrate split. [W5-3: = 0.19 = τ_fold, all 7 gapped]
- Laboratory-IN observables: `θ_s = r_s/D_A(z_*)` (CMB acoustic angular scale); `k_peak = 2π/r_s` (comoving BAO wavenumber); `r_s = ∫ c_s(τ) dτ` (comoving sound horizon). [S43 KK-CMB-TF-43; `r_s_obs = 147.09 Mpc`]

### Step 2 — substitute (the peak position is linear in the sound speed)
`r_s ∝ c_s` at fixed conformal time (a faster sound travels a larger comoving horizon). Therefore:
- Step 2a: `d(ln r_s) = d(ln c_s)`
- Step 2b: `Δr_s/r_s = Δc_s/c_s` (a fractional sound-speed change gives an equal fractional horizon change — a degree-0 dimensionless relation; the M_KK→Mpc unit conversion cancels)
- Step 2c: `Δk_peak/k_peak = −Δr_s/r_s` (since `k = 2π/r`)
- Step 2d: `Δθ_s/θ_s = +Δr_s/r_s` (at fixed `D_A`)

### Step 3 — simplify (the transport degree: which `c_s`?)
The split is defined on the SUBSTRATE branch speed `c_b^(2)` (M_KK, sub-luminal), but `Δc_s/c_s` in Step 2 is the fractional change of the EMERGENT acoustic speed. The substrate split projects onto the emergent acoustic channel through the same effacement projection that suppresses internal modes onto 4D observables. The S43 KK-CMB-TF-43 result fixes the FORM: the first-sound (substrate) channel imprints on the observed matter BAO with amplitude `A_FS = c₂²/c₁² = 1/[3(1+R*)] = 100/489 = 0.2045` (Sage-exact) — a **(speed-ratio)²** projection weight. Applying the same projection FORM to branch b relative to the emergent acoustic cone (`c_Gold`):

```
A_eff,b = (c_b^(2)/c_Gold)²          [the effacement projection of branch b onto the 4D acoustic cone]
Δr_s/r_s |_observed = s_b · A_eff,b   [the substrate split TIMES the projection weight]
```

This is the §VII.BA five-formulation taxonomy verdict applied to T_{BZ→pivot}:

- **Reading-S (T2-VACUOUS scalar transport; substrate = pivot)**: `s_b = 0.19` transports UNCHANGED → 19% peak shift. **This is the WP/Row #67 IMPLICIT reading.** It is a CONTAINER-THINKING conflation: it identifies the M_KK-unit internal branch speed `c_b^(2)` WITH the emergent 4D acoustic speed. Substrate-first FORBIDS this — the internal branch is not the observed light cone.
- **Reading-NS (NON-SCALAR; substrate ≠ pivot)**: `s_b` projects with weight `A_eff,b ≪ 1` → observed shift `s_b · A_eff,b`. **This is the SUBSTRATE-FIRST reading** (it respects that the BAO peak is set by the emergent acoustic channel, reached only through the effacement projection — the S43 A_FS mechanism).

### Step 4 — convert to observational units
Anchor `r_s = 147.09 Mpc` → `k_BAO = 2π/r_s = 0.04272 Mpc⁻¹` — **confirming the W5-3 B1-dominant claim k ~ 0.043 Mpc⁻¹ IS the standard BAO ruler** (S43 `k_BAO = 0.0427`). The W5-3 number is consistent.

Planck 2018 acoustic angular scale (fetched: `researchers/Paasch/12_2015_Planck_Cosmological_parameters.md:41`, `researchers/Mack/29_2018_Planck_Cosmological_Parameters.md`): `100 θ_MC = 1.04077 ± 0.00032` → fractional precision **σ(θ_*)/θ_* = 3.075e-04 = 0.0307%**.

| Branch | `A_eff,b = (c_b^(2)/c_Gold)²` (Sage-exact) | Reading-NS shift `s_b·A_eff,b` | \|Δk\| (Mpc⁻¹) | Δ(100 θ_*) |
|:-------|:--------------------------------------------|:-------------------------------|:--------------|:-----------|
| **B1** (acoustic singlet, DOMINANT) | `17689/2325625 = 0.0076061` | **0.14452%** | 6.17e-05 | 1.50e-03 |
| **B3** (dispersive optical triplet) | `1951609/83722500 = 0.0233104` | **0.44290%** | 1.89e-04 | 4.61e-03 |
| Reading-S (any branch) | n/a (split unchanged) | 19.00% | 8.1e-03 | 0.198 |

### Step 5 — conclusion
The substrate-first (Reading-NS) observed BAO peak-position shift is **0.14% (B1-dominant)** to **0.44% (B3, largest gapped branch)** — NOT the naive 19%. The 19% is the substrate-INTERNAL fractional split; the observed shift is suppressed by the effacement projection `(c_b^(2)/c_Gold)² ~ 0.008–0.023`.

---

## 4. Verdict — within or outside forecast precision

Precision anchors (ALL from fetched local sources, not training knowledge):

| Channel | Precision | Source (fetched) |
|:--------|:----------|:-----------------|
| Planck 2018 CMB acoustic scale `100 θ_*` | **0.0307%** | `researchers/Paasch/12:41` (`1.04077±0.00032`); `researchers/Mack/29` |
| DESI DR2 combined BAO ruler `Δr_BAO/r_BAO` | **0.24%** (68% CL) | `researchers/Cosmic-Web/19_DESI_DR2_BAO_Dark_Energy.md:77,111` (2× DR1) |
| DESI per-tracer BAO `D_A`/`H` | **~1–3%** (best ELG ±2.6%) | `researchers/Mack/30_2024_DESI_BAO_Results.md:39-42,99` (systematics <0.5%) |
| DESI 5yr (full) `w(z)` → ruler floor | ~2% on `w`; ruler ~0.1–0.2% | `researchers/Mack/30:166` |
| CMB-S4 / Simons Observatory `θ_s` | **GAP — no fetched forecast** | bounding estimate ~0.01% (see §6) |

**Verdict matrix (σ-equivalents = shift / precision, assuming full imprint):**

| Shift reading | vs Planck θ_* (0.031%) | vs DESI DR2 ruler (0.24%) | vs DESI per-tracer (~2.6%) |
|:--------------|:----------------------:|:-------------------------:|:--------------------------:|
| **Reading-NS B1 (0.14%)** | 4.70× — WITHIN* | 0.60× — **OUTSIDE** | 0.056× — OUTSIDE |
| **Reading-NS B3 (0.44%)** | 14.4× — WITHIN* | 1.84× — WITHIN* | 0.17× — OUTSIDE |
| Reading-S (19%) | 618× | 79× | 7.3× — all WITHIN (but container-thinking) |

\* The "WITHIN" entries against the **Planck CMB θ_*** carry a load-bearing physical caveat (see §5): Planck measures the *recombination photon-baryon* acoustic scale, which the substrate Layer-1/Layer-2 split does NOT directly displace. The substrate channel is an *additional, amplitude-suppressed* feature (S43 A_FS ~ 0.2 imprint), not a wholesale shift of the dominant peak. The σ-equivalent measures peak-position *sensitivity IF the split fully imprinted* — it is an upper bound on reach, not a detection forecast.

**Bottom-line verdict**: The substrate-first BAO peak-position shift is **channel- and branch-dependent, and below DESI's galaxy-BAO peak-position reach for the B1-dominant claim**:
- **B1-dominant (the WP's headline channel) at 0.14% is OUTSIDE DESI DR2 (0.6×) and OUTSIDE DESI per-tracer** — a precision-BAO peak-position measurement does NOT reach it.
- B3 (0.44%) marginally exceeds the DESI DR2 *aggregate* ruler precision (1.8×), but no single tracer reaches it (best per-tracer ~2.6%), and the aggregate ruler is a *combined* statistic, not a per-feature peak-position resolution at the B3 scale.
- The CMB θ_* "WITHIN" results are not a clean detection channel (the amplitude caveat, §5).

The "real test (DESI / Simons / CMB-S4)" framing **overstates the observational reach of the B1-dominant distinguisher**. It is a faithful-but-below-current-precision result for the headline channel, not a presently-live falsifier.

---

## 5. The amplitude-vs-position caveat (why the CMB θ_* "WITHIN" is not a clean detection)

The σ-equivalent comparison in §4 measures how many 1σ the *peak-position* shift would be *if the substrate split fully imprinted on the detector's acoustic-scale observable*. Two physical facts qualify this:

1. **The substrate channel imprints at SUPPRESSED amplitude, not full weight.** Per S43 KK-CMB-TF-43, the internal (first-sound) acoustic channel projects onto the observed matter BAO with amplitude `A_FS = c₂²/c₁² = 0.2045` — and the Layer-1/Layer-2 split within a gapped branch is a *second-order* feature *on top of* that already-suppressed channel. The observed BAO peak is dominated by the standard photon-baryon acoustic oscillation (Feynman/Hawking, Giants-BAO: `c_s = c/√(3(1+R*))`, set by QED + recombination, unaffected by substrate dynamics at 10⁻⁴¹ s). The substrate Layer-1/Layer-2 split adds a low-amplitude shifted/doubled sub-feature, NOT a displacement of the dominant peak. So even the position shift that *would* be resolvable at Planck θ_* sensitivity is gated by whether the sub-feature's amplitude clears the detector noise — an amplitude question this position-only translation does not settle.

2. **Planck θ_* is the RECOMBINATION acoustic scale.** It is the photon-baryon sound horizon at z≈1090, robust to emergence at the (l_Pl/λ)ⁿ level (Einstein, Giants-BAO §"sound horizon robustness": corrections ~10⁻¹¹⁶). The substrate Layer-1/Layer-2 branch split does not shift *this* ruler; it lives in the additional substrate acoustic channel (the S43 first-sound ring at r₁ = 325.3 Mpc, a DISTINCT scale from the 147 Mpc standard ruler). Comparing the substrate peak-shift fraction against Planck's *θ_* precision* is therefore a sensitivity benchmark, not a same-observable test.

**Consequence**: the genuinely live observational channel for the substrate two-speed structure is the S43 **first-sound ring at r₁ = 325.3 Mpc** (k₁ = 0.0193 Mpc⁻¹) — a feature with NO LCDM counterpart — gated by the effacement amplitude (which S43 flagged as possibly ~10⁻⁶, undetectable, or up to 0.204·A_BAO if equipartition holds). The per-gapped-branch Layer-1/Layer-2 *peak-position* shift at the standard BAO scale (the W5-3 / Row #67 number) is a below-precision refinement of the proven S84 two-speed structure, not the live falsifier the "DESI/Simons/CMB-S4 real test" phrasing implies.

---

## 6. Literature gap — CMB-S4 / Simons Observatory θ_s forecast

No CMB-S4 or Simons Observatory acoustic-scale (θ_s) precision forecast is present in the fetched local corpus (`researchers/Mack/`, `researchers/Cosmic-Web/`, `researchers/Baptista/`). The paper-search MCP was non-responsive this session (returned empty for all queries; consistent with the documented intermittent-MCP failure mode). The `cmb_s4_floor_est = 0.0001` (~0.01%) used in the compute is a **conservative bounding estimate**, NOT a fetched value — it is roughly the optimistic next-generation acoustic-scale floor implied by the S43 Giants-BAO CMB-S4 reach (damping tail to ℓ~5000; r~0.001). Even at this optimistic floor, the verdict for the **B1-dominant** channel (0.14% shift) is "WITHIN" only with the §5 amplitude caveat — and the structural conclusion (B1 below DESI galaxy-BAO peak-position reach) is robust to it, because the DESI per-tracer and DR2-ruler comparisons use fetched values. The CMB-S4/SO θ_s forecast should be fetched and pinned if a future gate sharpens this channel (see CF below).

---

## 7. Row #67 recommendation — QUALIFY (effected in-session)

**Recommendation: QUALIFY** (not RETAIN, not full RE-TAG). The Row #67 table is substrate-physically correct and the per-branch numbers are sound; what overstates reach is the bare "precision BAO-peak measurement ... is a real test (DESI / Simons / CMB-S4)" Detector/horizon phrasing, which omits (a) the substrate→emergent transport (the 19% internal split → ~0.14% observed B1 shift) and (b) the amplitude-vs-position caveat.

The QUALIFY edit (effected below, in the inventory I solely write):
- Adds the **transported observational shift** (B1 0.14% / B3 0.44%, Reading-NS) alongside the M_KK split, with the `(c_b^(2)/c_Gold)²` effacement-projection FORM and the S43 A_FS cross-reference.
- Re-tags the Detector/horizon framing from "real test" to **"below-current-precision distinguisher (B1-dominant 0.14% < DESI DR2 ruler 0.24%); the live two-speed channel is the S43 first-sound ring at r₁=325.3 Mpc, amplitude-gated"**, with the Planck θ_* caveat.
- Preserves the PROVEN S84 anchor framing (`c_T/c_S = 2.062 > 1`) — the structure is proven; only the *observational reach of the per-branch BAO peak-position number* is qualified.

This keeps Row #67 a faithful catalog entry while removing the reach overstatement. The row is NOT demoted (the prediction is real and the structure proven); it is correctly scoped as a sub-precision refinement plus a pointer to the genuinely-distinctive S43 first-sound ring channel.

---

## 8. Follow-up compute — carry-forward (4-field, per `feedback_fix-in-session-never-defer.md`)

The position-only translation is verdict-complete. One genuine future compute would sharpen the channel from sensitivity-bound to detection-forecast: the **amplitude** of the per-branch Layer-1/Layer-2 sub-feature in the observed P(k) / C_ℓ (the effacement projection of the substrate split onto the emergent BAO, including whether it imprints at A_FS~0.2 or the ~10⁻⁶ effacement floor). This is NOT covered by the W5-3 position number.

### CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT

| Field | Spec |
|:------|:-----|
| **What** | Compute the OBSERVED amplitude (not just position) of the per-gapped-branch Layer-1/Layer-2 BAO sub-feature in the emergent matter power spectrum P(k) and CMB C_ℓ. Transport the substrate split `s_b·A_eff,b` (B1 0.14% position shift) through the full effacement projection (Γ_eff = 0.99970 leakage; S43 A_FS = 0.2045 first-sound imprint vs the ~10⁻⁶ effacement floor) to a detectable amplitude `δP/P` at k~0.043 Mpc⁻¹ AND the distinct S43 first-sound ring at k₁=0.0193 Mpc⁻¹ (r₁=325.3 Mpc). Resolves whether the two-speed channel is amplitude-detectable by DESI DR2 / Simons / CMB-S4, converting the §4 *sensitivity* bound into a *detection* forecast. |
| **Inputs** | `computations/session-94/s94_s1_bao_observational_reach.py` (the position-shift transport + A_eff,b weights); `canonical_constants.py` (`c_B1`, `c_B3`, `c_Gold`, `c_BLV`, `Gamma_eff=0.99970`); S43 KK-CMB-TF-43 transfer-function structure (`r_1=325.3 Mpc`, `A_FS=0.2045`, `f_b=0.156`); fetched DESI DR2 `Δr_BAO/r_BAO=0.24%` + Planck `100θ_*` precision; **a CMB-S4/Simons θ_s + P(k)-amplitude forecast to be FETCHED** (literature gap, §6). |
| **Gate** | Pre-registered: the transported sub-feature amplitude `δP/P` at k~0.043 (and the r₁ ring amplitude) is computed and compared against DESI DR2 / Simons / CMB-S4 amplitude sensitivity. PASS = above any current/forecast detection threshold (live falsifier); INFO = below current but above CMB-S4 forecast (next-gen target); FAIL = below the effacement floor at all forecast detectors (structurally undetectable, effacement-suppressed). |
| **Effort** | ~1.0 wave-equivalent (re-uses the S-1 transport machinery + S43 transfer-function structure; the new work is the effacement-amplitude projection + the fetched CMB-S4/SO forecast + the P(k)/C_ℓ amplitude compute). |

---

## 9. Planning input for S95 (this synthesis's deliverable)

- **BAO observational-reach verdict**: substrate-first (Reading-NS) B1-dominant peak-position shift = **0.14452%** (Sage-exact `0.19·17689/2325625`); B3 = **0.44290%**. **OUTSIDE DESI DR2 ruler (0.24%) for B1; OUTSIDE all per-tracer BAO.** The naive 19% is a container-thinking conflation of the M_KK-internal branch speed with the emergent 4D acoustic speed. `|Δk|_B1 = 6.17e-05 Mpc⁻¹`; `Δ(100θ_*)_B1 = 1.50e-03`.
- **Row #67 recommendation**: **QUALIFY** — effected in-session (transported shift + below-precision re-tag + first-sound-ring pointer + Planck-θ_* amplitude caveat). The PROVEN S84 `c_T/c_S=2.062` structure framing is preserved.
- **Genuinely-distinctive live channel**: the S43 first-sound ring at **r₁ = 325.3 Mpc (k₁ = 0.0193 Mpc⁻¹)** — NO LCDM counterpart — is the two-speed structure's real observational distinguisher, gated by the effacement *amplitude* (CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT).
- **Literature gap**: CMB-S4 / Simons Observatory θ_s + P(k)-amplitude forecast must be fetched (paper-search MCP down this session; bounding estimate used for the CMB-S4 floor only, structural conclusion robust without it).
- **Carry-forward**: `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT` (4-field above) — converts the position *sensitivity* bound into an amplitude *detection* forecast.

---

*End S-1 synthesis. Verdict-only review; no gate emission. Row #67 QUALIFY edit effected in-session below this synthesis's landing.*
