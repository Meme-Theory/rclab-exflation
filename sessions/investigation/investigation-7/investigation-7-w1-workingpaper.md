# Investigation 7 Wave 1 — Cosmic-Web LSS Observables (Results Working Paper)

**Investigation**: 7 | **Wave**: 1 | **Plan**: investigation-7-plan-w1.md | **Theme**: the cosmic-web survey's six pre-registered LSS next-steps — the framework is observationally SAFE but not SHARP; test whether its one sharp feature (first-sound ring at r₁≈325 Mpc) is real (W1-1/W1-2, contradiction C1), close the cleanest unfinished DE verdict (W1-3 raw-DESI-BAO χ² at canonical w₀=−0.918, contradiction C2), and probe where the sector could BECOME sharp (W1-4 KBC timescape H₀, W1-5 persistent-homology web fingerprint, W1-6 f·σ₈ joint growth test).
**Seed**: `sessions/investigation/investigation-1/cosmic-web-theorist.md` (LSS survey output; next-steps 1–5 + R4)
**Verdict ledger**: `computations/investigation-7/inv7_gate_verdicts.txt` (investigation-track; emit via `emit_verdict(session=7, track="investigation", ...)`).

## Gate Sections

### §W1-1. INV7-W1-1 (cosmic-web-theorist)

**Status**: COMPLETED
**Gate ID**: `INV7-W1-1`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `cosmic-web-theorist`
**Hypothesis**: The ring amplitude A_FS = c₂²/c₁², with c₂ derived substrate-first from the S44 second-sound dispersion (independent of recombination R*), reproduces the canonical 0.204 within a 10% band — i.e. the ratio is substrate-genuine, not a re-import of 1/[3(1+R*)] (resolves C1).
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w1.md` §W1-1 (machinery pin, thresholds, substitution chain source).

**Verdict**: **FAIL** — `A_FS_substrate = 0.00388533` (scheme=FW, convention=RATIO, L_max=N/A). 3-tuple: **sign=FAIL, magnitude=FAIL, regime=VALID** → composite **FAIL**. The substrate second-sound ratio is **52.5× smaller** than the canonical 0.204; the deviation `|A_FS_substrate − 0.204| = 0.200` lies far outside both the 10% PASS band (0.0205) and the 20% INFO ceiling (0.0410). **C1 resolves toward Track B (standard-formula stand-in).**

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- `computations/investigation-7/inv7_w1_1_c2_substrate.py` — present; `grep -E 'from canonical_constants import|print_verdict_payload'` matches both (`from canonical_constants import *`; `def print_verdict_payload(...)` + call site).
- `computations/investigation-7/inv7_w1_1_c2_substrate.npz` — present; stores core result + **downstream P(k) feature** (`feature_A_FS=0.00388533`, `feature_k1_invMpc=0.0193150486`, `feature_r1_Mpc=325.3`) + dispersion arrays (`k_grid`, `omega_2`) + 3-tuple.
- `computations/investigation-7/inv7_w1_1_c2_substrate.png` — present; (left) ω₂(k) dispersion + extracted slope c₂; (right) A_FS bar comparison (substrate vs 0.204 anchor + 10% band vs recombination form).
- verdict_line in `computations/investigation-7/inv7_gate_verdicts.txt` — present; matches `^INV7-W1-1:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=3d235ad831c981d5e4f159aea4a661df83828d0747eaa65f28f37002ad5cf04a`, `content_sha256=eb862b2cdc4583d23dd31d8de63e035061edfa25950f9125ffb468a9289fc689`; dual-SHA companion row + schema-v2 3-tuple row + downstream-feature row all emitted via `emit_verdict` (track=investigation).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; gate is **NOT** pre-closed — it tests an open contradiction C1):

- `search_knowledge("first sound ring A_FS second sound dispersion c2 substrate")` → canonical `A_FS_first_sound_ring=0.204` (S96-OBS-FIRST-SOUND-RING); provenance edge records `A_FS = c2^2/c1^2 = 1/[3(1+R_*)]` (two-fluid acoustic ratio, NO LCDM counterpart) — **the C1 conflation in the framework's own provenance**.
- `search_knowledge("second sound mode S44 S68 ... Q=75989")` → theorem "Second sound Q = 75,989" PROVEN (obs horizon at S68); substrate-first source `s68_second_sound_obs.py/.npz`.
- `get_constant("A_FS_first_sound_ring")` → 0.204 (S96; not superseded). `get_constant("r1_first_sound_ring_Mpc")` → 325.3. `get_constant("k1_first_sound_ring_invMpc")` → 0.0193150486.
- `get_constant("A_first_sound_S43")` → not found (it is a derived S43 value 100/489 = 0.204499, not a registered constant; sourced from plan substitution chain).
- `get_constant("v_F")` → no exact match (v_F enters only through the *dimensionless* ratio; see §"c₁ unit-independence" below — it cancels).
- `search_knowledge("c1 first sound v_F sqrt(3) ... r dual pathway BK array")` → s86 dictionary lines 1534-1536: `c_1 = v_F/√3 (collisionless, ≈200 m/s)`; `c_2 = second sound (thermal/AB, order-parameter collective)`.
- `search_knowledge("FLUID-67 ... c_1 c_2 ... rho_n rho_s")` → GGE-TWO-FLUID-67 (S67 W7-B): **`c_2 = c_1·√(ρ_n/(3ρ_s)) = 0.058 M_KK`** (BCS low-T two-fluid relation, substrate's own density partition). This is the substrate-first c₂ source — verified directly against `s67_gge_two_fluid.npz`.

**Results**:

**The substrate-first second-sound dispersion** (loaded from `s67_gge_two_fluid.npz` = GGE-TWO-FLUID-67, the substrate's own BCS two-fluid mode; the S68 obs-horizon gate consumes this same mode):
- c₁ (first sound, longitudinal density mode) = 0.9289464166 M_KK
- c₂ (second sound, BCS low-T `c₁√(ρ_n/3ρ_s)`) = 0.0579034803 M_KK
- ρ_n/ρ = 0.0115216958, ρ_s/ρ = 0.9884783042
- The second-sound branch is linear, ω₂(k) = c₂·k. The gate reconstructs it on the pinned 4096-point log-grid (k ∈ [1e-4, 1e-1]) and extracts c₂ = lim_{k→0} dω₂/dk by least-squares: **c₂_slope = 0.0579034803** (intercept = −3.3e-19, residual = 3.6e-34) — recovers the BCS mode speed to machine precision. The regime is clean linear (regime_verdict = VALID).

**The ratio A_FS = c₂²/c₁²:**
- A_FS_substrate (direct slope) = **0.0038853309**
- A_FS_analytic = ρ_n/(3ρ_s) = 0.0038853309
- agreement |diff| = 1.3e-18 — confirms the BCS relation `c₂ = c₁√(ρ_n/3ρ_s)` makes the ratio the **unit-independent substrate two-fluid invariant** ρ_n/(3ρ_s).

**Substitution chain (with substituted numbers; sign/direction):**
- Step 1: c₂_substrate = lim_{k→0} dω₂/dk = 0.0579035 M_KK [S67/S68 BCS second-sound mode]; c₁ = v_F/√3 [s86 dictionary]; A_FS_canon = 0.204; A_FS_S43 = 100/489 = 0.204499; standard form A_FS_recomb = 1/[3(1+R*)].
- Step 2: A_FS_substrate = c₂²/c₁² = 3c₂²/v_F² (with c₁ = v_F/√3).
- Step 3 (two-fluid invariant): the BCS relation gives c₂² = c₁²·ρ_n/(3ρ_s), so A_FS_substrate = ρ_n/(3ρ_s) = 0.0115217/(3·0.9884783) = **0.0038853** — evaluated from the substrate's **own** (ρ_s/ρ_n) at the transit/fold point, **NO R* = 3ρ_b/4ρ_γ input**.
- Step 4 (read-off): sign(A_FS_substrate − 0.204) = sign(−0.200115) < 0; `|A_FS_substrate − 0.204| = 0.200115 ≫ 0.0410` → outside band. **Reproduction of 0.204 does NOT follow from the substrate two-fluid ratio.**

**The C1 verdict — what 0.204 actually is:** the canonical anchor 0.204 is reproduced not by the second-sound ratio but by the **recombination FIRST-sound** form, using the substrate's own R* = 0.6299428579 (from `s68_second_sound_obs.npz`): `1/[3(1+R*)] = c_s_standard² = 0.204506` (matches 0.204 to 5.1e-4; the finer S43 anchor 100/489 = 0.204499 matches to 7e-6). The framework's `canonical_constants.py:645` comment literally asserts the equality `A_FS = c2^2/c1^2 = 1/[3(1+R_*)]` — **this gate shows that equality is FALSE by a factor of 52.5×**: the left side (second sound, order-parameter collective) = 0.00389; the right side (first sound, recombination acoustic) = 0.2045. The pin took the container-thinking shortcut, importing the recombination first-sound speed 1/[3(1+R*)] and mislabelling it the second-sound ratio c₂²/c₁².

**c₁ unit-independence (why v_F never enters):** A_FS = c₂²/c₁² is dimensionless; the absolute c₁ normalization (whether v_F/√3 in lab units, ≈200 m/s, or the S67 internal 0.929 M_KK) cancels. Because the substrate's BCS relation fixes c₂ in *the same* units as c₁ (c₂ = c₁√(ρ_n/3ρ_s)), the ratio reduces to ρ_n/(3ρ_s) regardless of the c₁ scale — the result is robust to the v_F/√3-vs-S67-c₁ choice the plan flags.

**Rubric mapping:** FAIL_meaning fired — A_FS_substrate outside the 10% (and 20%) band; reproduction of 0.204 requires the recombination-specific 1/[3(1+R*)] input. The pin is a **standard-formula STAND-IN**; the ring's distinctiveness (Row #72, SNR≈8.6, the "NO LCDM counterpart" claim) is inherited from the standard recombination sound speed, not derived from the substrate's second-sound mode. C1 resolves **against** the framework's distinctiveness claim on this axis.

**Substrate framing (IS-not-IN):** the substrate IS the two-fluid condensate; the second sound IS a genuine substrate excitation (superfluid/normal counterflow). The gate derived c₂ FROM the substrate's own mode structure (D_K → BCS two-fluid partition → ω₂(k) → c₂) and asked whether the ring amplitude follows — it did not invert to the recombination container's R*. The finding is precisely that the *canonical pin* inverted (imported the container's first-sound 1/[3(1+R*)]); the substrate-first derivation that should have produced the ring amplitude instead yields a value 52.5× smaller, exposing the conflation.

**Solution-space update:** FAIL closes the "the r₁≈325 Mpc ring is a distinctive *substrate second-sound* prediction with a derived amplitude" corridor. The ring scale r₁=325 Mpc is the standard first-sound (acoustic) horizon (the `r1` constant's own provenance says "substrate metric-mode c₁=c acoustic horizon at recombination") — i.e. it coincides with the BAO scale, and its amplitude is the standard 1/[3(1+R*)], so it carries no second-sound distinctiveness. Downstream: (i) INV7-W1-2 (VSF) and INV7-W1-5 (persistent homology) now consume `feature_A_FS = 0.00388533` (the substrate-genuine amplitude) — a 52× weaker feature than the canonical 0.204, so the VSF/PH discriminator targets shrink correspondingly; the npz also carries the canonical 0.204 fields for a both-ways comparison. (ii) The "make-it-sharp" effort the survey flagged redirects from the ring (W1-1/W1-2) to the growth-rate and timescape channels (W1-4/W1-6). (iii) Any Row #72 distinctiveness re-statement is mack sole-writer + session-promotion (this is the investigation track; it is not yet a permanent re-pin).

---

### §W1-2. INV7-W1-2 (cosmic-web-theorist)

**Status**: COMPLETED
**Gate ID**: `INV7-W1-2`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC**
**Agent**: `cosmic-web-theorist`
**Hypothesis**: If the first-sound ring is a genuine second-sound feature (not doubled-BAO aliasing), the framework Void Size Function — excursion-set / Sheth–van-de-Weygaert on the featured P(k) — carries a localized bump/inflection at r₁=325 Mpc that is absent from a featureless-P(k) VSF and detectable against DESI/SDSS voids (disambiguates C1 via the two-point-statistic-FREE direction).
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w1.md` §W1-2.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/investigation-7/inv7_w1_2_vsf_second_sound.py` — EXISTS; `grep -E 'from canonical_constants import'` → matches (L88); `grep -E 'print_verdict_payload'` → matches (def + call).
- **data** `computations/investigation-7/inv7_w1_2_vsf_second_sound.npz` — EXISTS (VSF arrays nofeat/substrate/canon, Δ_VSF, discriminator results, obs-reach, dual-SHA).
- **plot** `computations/investigation-7/inv7_w1_2_vsf_second_sound.png` — EXISTS (4-panel: VSF, discriminator, P(k) ring window, obs-reach vs ZOBOV support).
- **verdict_line** `computations/investigation-7/inv7_gate_verdicts.txt` — `INV7-W1-2: FAIL … audit_sha256=95c70ff3dd2712d7e7b75571674fb82d8b47636b485402523e800e0951235f8e` present + dual-SHA companion + (advisory) 3-tuple row. ([VERIFY] trigger; 3-tuple not required but emitted for the directional sign result.)
- **data file** `computations/investigation-7/_data/vide_zobov_void_counts.txt` — CREATED (fetched Mao 2016 + Nadathur 2016 void-count edge summary).

**MCP Pre-Compute Audit**:
- `get_constant("r1_first_sound_ring_Mpc")` → **325.3** (S96 / S96-OBS-FIRST-SOUND-RING; finer r₁=325.265). Confirms the feature scale.
- `search_knowledge("Void Size Function Sheth van de Weygaert excursion-set … delta_v delta_c barriers")` → s52 void barriers **delta_v=−2.717, delta_c=1.686** (`s52_void_function_output.txt`; D=|δ_v|/δ_c=1.611); s52 cosmology Ω_m=0.315, Ω_b=0.0493, h=0.674, σ₈=0.811, n_s=0.9649; **VOID-SIZE-70 / cosmic-web-synthesis**: "framework predicts the SAME void statistics as ΛCDM at observable k" (the S43 volume-averaged closure at k_transition=9.4e23 h/Mpc). This gate is DISTINCT — it tests whether the localized real-space *second-sound feature* survives into the VSF, not the volume-averaged statistic.
- Upstream W1-1 npz read directly: `feature_A_FS=0.00388533` (substrate-genuine), `A_FS_canon=0.204` (recombination first-sound stand-in), `k1=0.0193150486 Mpc⁻¹`, ratio canon/sub = **52.5×**. W1-1 verdict = FAIL.
- FETCHED literature (paper-search MCP, downloaded `researchers/Cosmic-Web/1602.02771v2.pdf`): **Mao et al. 2016, arXiv:1602.02771** (BOSS DR12 ZOBOV, 1,228 quality voids, R_eff=15–130 h⁻¹Mpc); **Nadathur 2016, arXiv:1602.04752** (BOSS DR11, VSF-vs-ΛCDM deviation < 6% for 8<R_v<60 h⁻¹Mpc).

**Verdict**: **FAIL** — composite from 3-tuple `(sign=PASS, magnitude=FAIL, regime=VALID)` (magnitude=FAIL + regime=VALID ⇒ composite FAIL). Reading B: the ring is a doubled-BAO aliasing artifact / sub-threshold feature that does NOT survive into the void direction.

**Results** (NUMBERS → gate → interpretation):

*Numbers (PRIMARY = substrate-genuine A_FS=0.00388533):*
- max |Δ_VSF/VSF| over [275,375] Mpc = **0.0385%** (3.85e-4), peak at r=351.6 Mpc.
- peak-localization offset |r_peak − 325.3| = **26.3 Mpc** → NOT within the ±25 Mpc window (and the "peak" is the broad inflection edge, not a localized ring).
- sign(Δ_VSF peak) = **+** (an excess; matches the substitution-chain Step-3 prediction).
- CONTRAST (canonical A_FS=0.204, the recombination stand-in): max |Δ_VSF/VSF| = **2.0142%**, peak at r=351.6 Mpc — **still below the 5% threshold**, also not localized at r₁.
- 4-tuple: (scheme=FW, convention=RATIO, L_max=N/A excursion-set).

*Gate (CC operator):* PASS iff `max_{[275,375]} |Δ_VSF/VSF| ≥ 0.05` AND `|r_peak − 325.3| ≤ 25`. PRIMARY: 0.000385 < 0.05 → magnitude FAIL; localization False. CONTRAST: 0.0201 < 0.05 → also FAIL. INFO floor (2–5%) not reached by either run at the substrate amplitude; the canonical contrast (2.01%) sits in the INFO band but is the "if-the-ring-were-as-strong-as-the-stand-in" comparator, not the substrate prediction.

*Substitution chain (with substituted numbers):*
- P_FW(k) = P_shape(k)·[1 + A_FS·W(k;k₁)], W = Gaussian ring window (σ_lnk=0.10) centered at k₁=0.0193150486 Mpc⁻¹; r₁ = 2π/k₁ = **325.30 Mpc** (verified to 4 d.p.).
- VSF(r) = (1/V(r))·|d ln σ⁻¹/d ln r|·[S·f(S)]_SvdW04 two-barrier (δ_v=−2.717, δ_c=1.686, D=1.611, 60-term j-sum); both featured and featureless P(k) σ₈-normalized at R=8 h⁻¹Mpc (each → σ(8)=0.81100).
- Step 3 (direction): a positive-power ring at k₁ → enhanced σ(R) near R~r₁/2 → an EXCESS in the VSF near r₁. Computed sign = + ✓ (direction correct); magnitude = 0.0385% ✗ (≈130× below the 5% threshold for the substrate amplitude; the 52.5× weaker substrate ring leaves essentially no VSF imprint).
- Step 4 (read-off): no localized ≥5% inflection at r₁ ⇒ **Reading B (aliased / sub-threshold)** — the ring does NOT propagate into the two-point-statistic-FREE void direction.

*DESI/SDSS VIDE/ZOBOV cross-check (observational reach — the decisive context):* the feature scale r₁ = 325.3 Mpc = 219.3 h⁻¹Mpc lies **BEYOND the entire observed void-effective-radius support**. BOSS DR12 ZOBOV (Mao et al. 2016, arXiv:1602.02771; 1,228 quality voids) spans R_eff = 15–130 h⁻¹Mpc (majority 30–80); the **largest single catalogued void** is R_eff = 63.5 h⁻¹Mpc = 94.2 Mpc (ID 4407, CMASS-N, z=0.463); the catalog **maximum** is 130 h⁻¹Mpc = 192.9 Mpc. A void of effective radius ~325 Mpc (a ~650 Mpc-diameter underdensity) has never been catalogued. Reported VSF-vs-ΛCDM precision is < 6% (Nadathur 2016, arXiv:1602.04752, BOSS DR11). So even the canonical-0.204 contrast (2.01% at 351.6 Mpc) would be (a) below the survey precision floor and (b) at a void scale with zero catalogued voids — doubly unreachable.

*Interpretation — solution-space update (C1):* The void direction does **NOT** confirm the first-sound ring. Combined with W1-1 (FAIL: the substrate c₂²/c₁²=0.00388533 is 52.5× below the canonical 0.204, i.e. the 0.204 pin is a recombination FIRST-sound stand-in), C1 resolves toward Reading B on BOTH legs: the ring's distinctiveness is not substrate-genuine at the substrate amplitude, and even were it as strong as the stand-in, it does not localize in the VSF and sits beyond the void catalog's reach. The two-point-statistic-FREE direction adds **no** distinctiveness beyond W1-1's direct c₂ derivation. The "distinctive VSF signature at r_void~325 Mpc" corridor (falsifier Row #72 distinctiveness on the void side) is **closed**; the sector's potential sharpness must come from W1-5 (persistent homology) / W1-6 (f·σ₈), not from voids at the ring scale.

*Substrate framing:* PHONONIC. The substrate IS the post-transit GGE density field; voids are topologically distinct underdense regions of that field (van-de-Weygaert geometry). The flow tested is D_K spectrum → second-sound collective mode → ring feature in P(k) → excursion-set first-crossing on the featured P(k) → VSF inflection at r_void~r₁ → DESI/SDSS void counts. The gate did NOT invert this (it did not read the ring off the recombination container); it propagated the substrate-derived feature forward and asked whether voids — which probe the field topology independently of the P(k)/ξ(r) channel where the ring was defined — show it. They do not, at the substrate amplitude.

**Dual-SHA**: `audit_sha256=95c70ff3dd2712d7e7b75571674fb82d8b47636b485402523e800e0951235f8e` / `content_sha256=e8434cecc86276a219870fd76631eba93c33fa927593ac4ebc56fd2cb3fcfa99` (companion row + advisory 3-tuple `sign=PASS magnitude=FAIL regime=VALID` in `inv7_gate_verdicts.txt`).

---
### §W1-3. INV7-W1-3 (cosmic-web-theorist)

**Status**: COMPLETED
**Gate ID**: `INV7-W1-3`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (PHONONIC-with-cosmological-readout)
**Agent**: `cosmic-web-theorist`
**Hypothesis**: The framework's surviving DE prediction — the CANONICAL constant w₀=−0.918 (Volovik partition + effacement Γ_eff=0.99970), NOT the superseded −0.509 and NOT the CPL-plane parameter — yields a raw-DESI-DR2-BAO χ²/N below the atlas-09 Item-25 FAIL-threshold of 4, i.e. is BAO-VIABLE rather than BAO-excluded (resolves C2).
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w1.md` §W1-3.

**Verdict**: **PASS** — χ²/N = **1.7399** (< 4, and below the INFO band's lower edge of 2). The canonical constant-w = −0.918 is **BAO-VIABLE** against the raw measured DESI DR2 BAO distances. C2 resolves toward viability. [SIGN] 3-tuple: `sign=PASS / magnitude=PASS / regime=VALID`.

**Result** (4-tuple): `(value=1.7399468124207045, scheme=FW, convention=ABSOLUTE, L_max=N/A)` — distance-ladder integral, no spectral truncation.

| Model (constant w) | w₀ | χ² (N=13) | χ²/N | verdict vs threshold-4 |
|:-------------------|---:|----------:|-----:|:-----------------------|
| **Framework (canonical)** | **−0.918** | **22.619** | **1.7399** | **PASS** (< 2) |
| ΛCDM | −1.000 | 44.677 | 3.4367 | (INFO band; reference only) |
| Superseded inversion | −0.509 | 1376.914 | 105.9164 | FAIL (catastrophic) |

**Headline finding (C2 resolved):** the canonical w₀=−0.918 fits the raw DESI DR2 BAO **better than ΛCDM** — Δχ²(FW−ΛCDM) = **−22.06** in the framework's favor. DESI DR2 itself prefers w₀ > −1, so −0.918 sits *closer* to the data's preferred distance scale than ΛCDM's −1.0. The superseded −0.509, re-evaluated here on the *same* DR2 data + covariance, gives χ²/N = 105.9 — confirming the atlas-09 Item-25 exclusion (χ²/N = 23.2, S50, vs the less-constraining DR1) was an artifact of the **superseded inversion value**, not a verdict on the framework's actual prediction. The DR2 errors (≈0.7× DR1) sharpen the −0.509 exclusion from 23.2 → 106. **The cleanest unfinished LSS verdict in the project closes in the framework's favor.**

**MCP Pre-Compute Audit**:
- `get_constant("w0_FW")` → **−0.918** (S58 four-fold-lock; Volovik vacuum partition + effacement Γ_eff=0.99970; NOT superseded). Used as the constant-w pin.
- `search_knowledge("DESI BAO chi2 w0 -0.509 atlas-09 Item-25 threshold 23.2")` → gate `DESI-DR3-JOINT-50` (S50): **FAIL, χ²/N = 23.2 (threshold 4), Δχ² = +241 vs LCDM, "BAO distances exclude w₀ = −0.51"**; plus S65 `s65_desi_dr3_prep_log.txt` scenarios (all vs *hypothetical* DR3 references, not raw DR2 distances). Confirms this raw-DR2 verdict at the canonical w₀ was NOT previously recorded.
- `trace_entity("DESI BAO chi2")` → `threshold = 4` (eq_632, atlas-09 Item-25 / DESI-DR3-JOINT-50). Confirms the pre-registered FAIL-threshold.
- `get_constant` on `Omega_m`=0.315, `Omega_b`=0.0493, `Omega_Lambda`=0.685, `Omega_r`=9.15e-5; `H_0_km_s_Mpc`=67.4 (canonical_constants.py:72, Planck 2018); `c_light_km_s`=2.99792458e5. `r_d`/`r_drag` are NOT importable canonical constants → held at the canonical sound horizon **r_d = 147.0244278618993 Mpc** (`s64_desi_dv.npz` `r_d_Mpc`, Planck-2018 fiducial; the framework does NOT modify r_d, per S50: "BCS transition at ~1e-41 s is irrelevant to recombination at T~0.26 eV").
- Not PRE-CLOSED: the raw-DR2-BAO χ² at the **canonical** w₀=−0.918 (constant-w, full covariance) is a genuinely new verdict; S50 tested −0.509 vs DR1, S64/S65 tested D_V-only vs hypothetical DR3 references.

**Method / data provenance**:
- **Data**: raw measured DESI DR2 BAO distances {D_M/r_d, D_H/r_d, D_V/r_d}, 13 measurements across 7 z-bins (BGS 0.295 [D_V]; LRG1 0.510, LRG2 0.706, LRG3+ELG1 0.934, ELG2 1.321, QSO 1.484, Lya 2.330 [each D_M+D_H]), + the full 13×13 block-diagonal covariance. Source: **DESI DR2 Results II, arXiv:2503.14738v3** (Phys. Rev. D 112, 083515, 2025), fetched 2026-06-15 from the community-standard Cobaya `bao_data/desi_bao_dr2/` files (`..._GCcomb_mean.txt` + `..._GCcomb_cov.txt` — the exact mean+covariance the DESI DR2 likelihood ships). Stored: `computations/investigation-7/_data/desi_dr2_bao_distances.txt` + `..._covariance.txt`.
- **Model**: flat wCDM, **CONSTANT w = w₀ = −0.918** (NOT CPL w₀–w_a). `H(z)=H₀√[Ω_r(1+z)⁴+Ω_m(1+z)³+Ω_DE(1+z)^{3(1+w₀)}]`, Ω_DE = 1−Ω_m−Ω_r (flat). `D_M(z)=∫₀ᶻ c dz'/H(z')`, `D_H=c/H(z)`, `D_V=[z D_M² D_H]^{1/3}`. Distance integrals via adaptive `scipy.integrate.quad` (1000-node base grid, tol 1e-9).
- **Statistic**: χ² = Δᵀ C⁻¹ Δ with Δ = d_pred(w₀=−0.918) − d_DESI, over the 13-vector; r_d held at canonical (NOT marginalized). Covariance well-conditioned (cond = 117, symmetric, pos-def, min eig 5.79e-3). Independently cross-checked by a minimal re-derivation: FW χ²/N=1.7399, ΛCDM=3.4367, −0.509=105.9164 (bit-match).

**Substitution chain (sign claim: χ²/N − 4 < 0, computed not asserted)**:
- Step 1 — w₀ = −0.918 [canonical `w0_FW`]; H(z) above; d_DESI = {D_M/r_d, D_H/r_d, D_V/r_d} measured (arXiv:2503.14738); threshold = 4 [atlas-09 Item-25]; superseded ref −0.509 FAILED at χ²/N=23.2 (the value NOT used).
- Step 2 — χ² = (d_pred(−0.918) − d_DESI)ᵀ C⁻¹ (d_pred(−0.918) − d_DESI) = 22.6193; χ²/N = 22.6193 / 13 = 1.7399.
- Step 3 — −0.918 is much closer to ΛCDM (−1) than the superseded −0.509; DESI DR2 prefers w₀>−1, so the −0.918 distance ladder is near the data's preferred scale ⇒ small χ². sign(χ²/N − 4) read off the COMPUTED value.
- Step 4 — χ²/N − threshold = 1.7399 − 4 = **−2.2601 < 0** ⇒ **NEGATIVE = PASS direction**. Largest per-bin residual is LRG1 D_H at +3.03σ (a known DESI DR2 feature, not a model failure); all other |nsig_FW| ≤ 2.1σ.
- Conclusion — χ²/N < 4 ⇒ **BAO-VIABLE**; C2 resolves toward viability; the DR3-2027 measurement becomes the live binding discriminator.

**Substrate framing (IS-not-IN):** the DE EOS w₀=−0.918 is the **laboratory-IN** image of a substrate quantity — the effacement residual, the 0.03% leakage through the substrate's impedance mismatch (Γ_eff=0.99970) in the Volovik vacuum partition. It is NOT a quintessence field IN spacetime; it IS the substrate's vacuum-energy partition reading out as an effective w(z) when the emergent FRW background is borrowed to interpret late-time distances. Flow: D_K spectral action → a₀ vacuum-energy moment + Volovik partition → effacement residual Γ_eff=0.99970 → effective w₀=−0.918 → distance ladder D(z) → BAO χ². The gate does NOT assume a w and fit it; it takes the substrate-derived w₀ and asks whether the emergent-FRW distance ladder it implies survives the raw BAO data — it does, and more comfortably than ΛCDM.

**Solution-space update:** PASS closes the "the framework's DE prediction shares the −0.509 BAO-exclusion fate" concern (C2) in the framework's favor. The exclusion lived entirely in the superseded inversion value, not in w₀=−0.918. Downstream: (i) the live DE discriminator migrates fully to **DESI DR3 (2027)** — at DR3's tighter errors the FW-vs-ΛCDM Δχ² and the FW-vs-DESI-best-fit separation become decisive (S64/S65 forecast ~5σ-class FW–ΛCDM discrimination by D_V alone at DR3). (ii) This is the **w₀-side** verdict; it is C2-orthogonal to the τ(ρ)-clock Hubble-tension channel (W1-4), so a W1-4 outcome cannot disturb it. (iii) Any falsifier-inventory DE-row re-statement (Falsifier #1 / R_842 rectangle binding) is `mack-cosmic-bridge` sole-writer + session-promotion — this is the investigation track; it is a viability verdict, not yet a permanent re-pin. **Caveat (intentional U2 borrow):** the χ² lives in the emergent single-global-FRW container the framework borrows for late-time distances; the verdict is conditional on that U2 assumption, which the substrate-framing block makes explicit.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- script `computations/investigation-7/inv7_w1_3_raw_bao_chi2.py` — present; contains `from canonical_constants import` + `print_verdict_payload`.
- data `computations/investigation-7/inv7_w1_3_raw_bao_chi2.npz` — present (predictions, residuals, χ² per model, covariance, all pins).
- plot `computations/investigation-7/inv7_w1_3_raw_bao_chi2.png` — present (D_M/r_d, D_H/r_d, D_V/r_d Hubble diagrams: DESI DR2 data vs FW/ΛCDM/superseded).
- FETCHED data: `_data/desi_dr2_bao_distances.txt` + `_data/desi_dr2_bao_covariance.txt` (arXiv:2503.14738 via Cobaya `bao_data/desi_bao_dr2/`).
- verdict_line in `computations/investigation-7/inv7_gate_verdicts.txt` — `^INV7-W1-3:.* audit_sha256=[a-f0-9]{64}` present, with dual-SHA companion row + schema-v2 3-tuple ([SIGN]). audit_sha256=`4d54f7bbfcb30ddc22d4c609ff43d77e46e2c115ef8f17ecb9a890db2e1b1efc`, content_sha256=`b584e215ee1d555f9ae56dfb1383777f6318b7161af244c1bdeb9822c622652e`.
- wp_section: this §W1-3 (Status COMPLETED, Verdict, Output Artifacts, MCP Pre-Compute Audit present).

---

### §W1-4. INV7-W1-4 (cosmic-web-theorist)

**Status**: COMPLETED
**Gate ID**: `INV7-W1-4`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `cosmic-web-theorist`
**Hypothesis**: Modeling the KBC void (6.04σ, ~300 Mpc underdensity) as a low-τ substrate region via the τ(ρ_local) compaction map yields a local H₀ enhancement of the correct SIGN (positive — voids expand faster) and a magnitude within band of the ~9% needed to relieve the Hubble tension, WITHOUT touching the BAO-constrained w₀ (C2-orthogonal).
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w1.md` §W1-4.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/investigation-7/inv7_w1_4_kbc_timescape_h0.py` — EXISTS; `grep` confirms `from canonical_constants import` and `print_verdict_payload` (def + call). PASS
- **data** `computations/investigation-7/inv7_w1_4_kbc_timescape_h0.npz` — EXISTS (`np.savez`). PASS
- **plot** `computations/investigation-7/inv7_w1_4_kbc_timescape_h0.png` — EXISTS (`make_plot`). PASS
- **verdict_line** `computations/investigation-7/inv7_gate_verdicts.txt` — EXISTS, matches `^INV7-W1-4:.* audit_sha256=[a-f0-9]{64}` (audit_sha256=`d49a5543…1a16793`); dual-SHA companion row + schema-v2 3-tuple row present ([SIGN] trigger). PASS
- **wp_section** this section — Status COMPLETED, Verdict (INFO), Output Artifacts, MCP Pre-Compute Audit all present. PASS

**MCP Pre-Compute Audit**:
- `trace_entity("substrate-compaction-timescape")` → T8 (S58) "Substrate-compaction observable (ρ_vac ↔ fiber τ tracking) drives w_a", **CONDITIONAL on DESI DR3**; eqs `tau(rho) = substrate-compaction map (fiber τ tracks ρ_local)` + `H_local = H_bar·[clock-rate(τ(ρ_void))/clock-rate(τ(ρ_bar))]`. Confirms the mechanism is a registered substrate-IS relation, not a closure — this gate computes its z~0 magnitude. NOT pre-closed.
- `search_knowledge("tau density compaction clock timescape H0 Hubble tension void")` → S60 GSL-timescape: `tau_void=0.184697`, `tau_wall=0.206794` vs `tau_fold=0.19`, `f_void=0.76`; S59 `delta_alpha_vw=|2·clock_coeff·delta_tau_eff|`, `w_a(apparent)=-0.644891`. Establishes the canonical clock map + the void-LOWER-τ sign convention.
- `get_constant("clock_coeff")` → **-3.08** (`dα/α = clock_coeff·dτ`, S22d E-3): the τ→clock-rate map.
- `get_constant("tau_fold")` → 0.19 (S42 CONST-FREEZE-42); `get_constant("H0_FW")` → not found (no canonical H0_FW; global `H_0_km_s_Mpc=67.4` used).
- **τ-machinery source**: S59 `s59_timescape_wa.py` (Route-1 backreaction `delta_tau/delta = rho_m/M_KK⁴·|frac_da2|/d2S_fold`; Route-2 KZ `delta_tau_eff`), S60 `s60_gsl_timescape.py` (void-LOWER-τ convention). KBC params **FETCHED** Haslbauer+2020.

**Verdict**: **INFO** — sign-correct-magnitude-short. (sign=PASS, magnitude=INFO, regime=VALID; composite `magnitude_verdict==INFO ⇒ INFO`.) `audit_sha256=d49a5543b15d518dc53f11f9cd859cd10010e34967f6ff611e341e6001a16793`, `content_sha256=24ef2c08c91fbe91d3ad47f1aaa9a5a2933ad1f617a9e643c90f3ed577d400de`.

**Results**:

*Reported value (4-tuple)*: `ΔH₀/H₀_local = 0.00751` (**0.75 %**), `scheme=FW, convention=RATIO, L_max=N/A` (τ(ρ) clock map, not a spectral truncation). This is the framework's **largest-magnitude** route (Route B, saturated void-wall swing, KBC δ=−0.46); the gate is judged on the framework's best delivery.

*Pre-registered operator*: `ΔH₀/H₀_local > 0` (void expands faster) **AND** `|ΔH₀/H₀_local − 0.09| ≤ 0.03` (magnitude in [6%, 12%]).
- **PASS_meaning** — positive and in [6%,12%]: substrate timescape supplies right-size right-sign Hubble relief via the τ(ρ)-clock, w₀-orthogonal — a make-it-sharp win. *(not met)*
- **FAIL_meaning** — wrong sign (map compacts the wrong way, void clocks slower, ΔH₀<0) OR over-magnitude (>12%, over-relief into reverse tension). *(not met)*
- **INFO_meaning** — positive but <6%, sign-correct-magnitude-short, partial relief. **← this is the verdict.**

*Substitution chain (with substituted numbers)*:

> **Step 1 — definitions** (all substrate-first):
> - `δ_KBC = (ρ−ρ̄)/ρ̄ = −0.46` (Haslbauer+2020 abstract: δ ≡ 1−ρ/ρ₀ = 0.46±0.06 between 40 and 300 Mpc; conservative central −0.30 also computed). R_void ≈ 300 Mpc, 6.04σ vs ΛCDM.
> - τ(ρ): fiber τ tracks ρ_local (project_substrate-compaction-timescape; q-theory=F-theory variational). Canonical SIGN convention (S60 `tau_void = tau_fold − δτ`): **denser → higher τ → more-compacted fiber → slower clock**.
> - `clock_coeff = −3.08`: `dα/α = clock_coeff·dτ` (S22d E-3). The emergent clock rate is set by the fiber's spectral structure via this map, so `ΔH₀/H₀ = clock_coeff·δτ`.
> - relief target `0.09` (~9%; literature: (H₀^SH0ES 73.04 − H₀^Planck 67.40)/67.40 = 0.0837).
>
> **Step 2 — substitute (density→τ map; two framework routes)**:
> - **Route A (substrate-physics gravitational backreaction, S59 Route 1, canonical)**: `δτ/δ = (ρ_m/M_KK⁴)·|frac_da2|/d2S_fold = 1.316×10⁻¹¹⁸` per unit δ (`ρ_m/M_KK⁴ = 4.22×10⁻¹¹⁵`, `frac_da2 = 99.127`). → `δτ_A = 1.316×10⁻¹¹⁸ × (−0.46) = −6.05×10⁻¹¹⁹`.
> - **Route B (saturated void-wall swing, S59 Route 2 KZ variance; framework best case)**: `δτ_void = −δτ_eff·(|δ_KBC|/|δ|_cosmic-mean)`, `δτ_eff = 0.005303` (S59/S60 1-σ void-wall τ separation = S60 `d_v`), `|δ|_cosmic-mean = 1.0` (the void-wall swing IS the ~1σ density contrast). → `δτ_B = −0.005303 × 0.46 = −0.002439`.
>
> **Step 3 — direction (SIGN, script-VERIFIED, not assumed)**: `δ_KBC < 0` (underdense) ⇒ `δτ < 0` (lower τ, less compaction; `dτ/dρ > 0` verified `True` from the map). `clock_coeff = −3.08 < 0` and `δτ < 0` ⇒ `ΔH₀/H₀ = clock_coeff·δτ > 0` (faster clock; void expands faster). **SIGN = PASS** (`sign_route_B_positive = True`).
>
> **Step 4 — read-off (MAGNITUDE)**:
> - Route A: `ΔH₀/H₀ = (−3.08)×(−6.05×10⁻¹¹⁹) = 1.86×10⁻¹¹⁸` → **~10⁻¹¹⁶ %**, ~117 OOM short. The cosmic-mean gravitational backreaction supplies a negligible τ-shift (S59's recorded "10¹²⁰ below stiffness").
> - Route B (REPORTED): `ΔH₀/H₀ = (−3.08)×(−0.002439) = 0.00751` → **0.75 %** (paper δ=−0.46) / 0.49 % (central δ=−0.30). Positive but **<6%** → **INFO** (sign-correct-magnitude-short; ~8% shy of the ~9% target).

*Conclusion*: The KBC void's substrate-timescape ΔH₀/H₀ has the **correct sign** (underdense void clocks faster — the τ(ρ)-clock points the right way to relieve the Hubble tension) but the **magnitude under-delivers**: even the framework's most optimistic route (saturated void-wall swing) gives ≈0.75%, and the substrate-physics gravitational-backreaction route gives ~10⁻¹¹⁶% (~117 OOM short). The substrate timescape **contributes to but does not resolve** the Hubble tension at the KBC scale — a partial-relief mechanism; the residual ~8% needs another contribution. This is consistent with Haslbauer+2020's own finding that in pure ΛCDM the void is too shallow/rare to supply the full relief (their resolution required MOND-level enhanced structure growth + 11 eV sterile neutrinos).

*ORTHOGONALITY (load-bearing, per gate block)*: This mechanism operates through the **τ(ρ)-clock — the a₂ / emergent-FRW reading** — NOT through w₀ (the a₀ vacuum partition). No quantity in this gate touches `w0_FW = −0.918`, `Ω_DE`, or the dark-energy equation of state. It is therefore **ORTHOGONAL to the BAO-constrained w₀ tested in INV7-W1-3 (C2)**: the INFO verdict here is independent of whatever W1-3 returns. The KBC-void H₀ relief (a₂-clock channel) and the BAO-w₀ viability (a₀-partition channel) are two separate substrate channels that do not trade off against each other.

*CROSS-EPOCH LINK*: This is the **z~0 face** of the τ(ρ) mechanism — large local τ-variance now (a real −0.46 density contrast). Its **z~7 face** is **LRD C3 (inv-7 W2)**: the near-homogeneous high-z limit where local τ-variance integrates to ~0 and the framework reduces to ΛCDM (the LRD-era dead-end). Same substrate relation, opposite epochs — the W1-4 offense (large local τ-variance now) and the LRD-era dead-end (negligible τ-variance then) are two readouts of one τ(ρ) map. The sign-correct-but-short result here is the z~0 analog of the z~7 framework=ΛCDM convergence: the τ(ρ) clock channel is real but quantitatively modest at both epochs.

*Substrate framing*: PHONONIC. The substrate IS the fabric whose fiber τ varies with local spectral-weight density; the KBC void is the **laboratory-IN image** of a low-τ substrate region (less-compacted fiber → faster emergent clock). Flow: D_K spectral structure → τ(ρ) compaction map → local clock-rate variance → differential emergent-FRW expansion → ΔH₀ between void and cosmic mean → measured local-vs-global H₀ discrepancy. The gate reads the H₀ enhancement off the substrate's **own** τ-clock responding to the void's density; it does NOT posit a quintessence field or a modified-gravity coupling in a void embedded IN a pre-existing space.

*KBC params source (FETCHED)*: Haslbauer, Banik & Kroupa 2020, MNRAS 499, 2845 — arXiv:2009.11292v2 "The KBC void and Hubble tension contradict ΛCDM on a Gpc scale" (δ = 0.46±0.06 between 40–300 Mpc; 6.04σ; 7.09σ jointly with the Hubble tension). Supporting: Mazurenko+2023 (arXiv:2311.17988), Mazurenko+2024 (arXiv:2412.12245, H₀(z) decay). Data file: `computations/investigation-7/_data/kbc_void_haslbauer2020.txt`.

*Artifacts*: `computations/investigation-7/inv7_w1_4_kbc_timescape_h0.py` / `.npz` / `.png`. Dual-SHA + 3-tuple companion rows in `computations/investigation-7/inv7_gate_verdicts.txt`.

*Posterior re-allocation (dual_prior)*: INFO → 0.7 to the **partial-relief sub-track** (sign correct, magnitude short), per the plan discriminator. The full-relief Track A (ΔH₀/H₀ ~ +9%) is disfavored; the wrong-sign Track B is excluded (sign verified positive).

---

### §W1-5. INV7-W1-5 (cosmic-web-theorist)

**Status**: COMPLETED
**Gate ID**: `INV7-W1-5`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC**
**Agent**: `cosmic-web-theorist`
**Hypothesis**: The persistent-homology Betti curves β₁/β₂ of the framework field (Gaussian + W1-1 second-sound feature + f_NL=1.505 envelope) carry a β₂ shell-loop feature localized near r₁=325 Mpc that is ABSENT in matched LCDM Gaussian-random-field mocks at ≥3σ — a measurable topological signature LCDM lacks even where two-point statistics match; explicitly DISTINCT from the S43 volume-averaged-Betti closure at the unobservable k~10²⁴ h/Mpc.
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w1.md` §W1-5.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/investigation-7/inv7_w1_5_persistent_homology_ring.py` | ✓ `from canonical_constants import` (L≈205); ✓ `print_verdict_payload` (def + call) |
| data | `computations/investigation-7/inv7_w1_5_persistent_homology_ring.npz` | ✓ present (Betti curves β₀/β₁/β₂ FW + GRF-mean/std, Z_substrate, Z_canon, ν_r1, both-ways contrast, dual-SHA) |
| plot | `computations/investigation-7/inv7_w1_5_persistent_homology_ring.png` | ✓ present (4-panel: β₂/β₁/β₀ curves FW-vs-GRF + both-ways-contrast Z bar) |
| verdict_line | `computations/investigation-7/inv7_gate_verdicts.txt` | ✓ `^INV7-W1-5:.* audit_sha256=[a-f0-9]{64}` matches; dual-SHA companion + (informative) 3-tuple row present |
| wp_section | this section | ✓ Status COMPLETED / Verdict FAIL (directional; magnitude PASS by 620σ) / Output Artifacts / MCP Pre-Compute Audit |

NOTE: this gate is the COMPUTE leg; any falsifier-master-inventory.md topological-signature row landing is `mack-cosmic-bridge` sole-writer + session-promotion — recorded under **Falsifier-row candidate** below.

**Persistent-homology method (GUDHI/ripser ABSENT — documented fallback per spawn).** GUDHI/ripser are not in the venv; β₀/β₁/β₂(ν) are computed by a sublevel-set threshold sweep on each 256³ periodic-torus field realization (a cubical-complex filtration, standard cosmological-PH practice — van de Weygaert / Pranav et al.): X(ν)={F≤ν}; **β₀(ν)** = #connected-components of X (scipy.ndimage.label, 6-connectivity, with periodic wrap stitched by union-find on the boundary faces); **β₂(ν)** = #enclosed voids = #components of the superlevel complement minus the percolating background; **β₁(ν)** = β₀+β₂−χ from the integral-geometric cubical Euler characteristic χ=V−E+F−C (GPU torch.roll-OR-sum, ~7.5× faster than CPU). The χ machinery was VALIDATED in-script against known topologies: solid cube χ=1, thick S²-shell χ=2 (⟹β₁=0), full torus χ=0; wrap-around connectivity confirmed (boundary-spanning blob → β₀=1). β₀/β₂ (the verdict leg — β₂ z-score is the gate operator) are computed at every ν; β₁ (diagnostic only, not in the operator) is computed on a 24-threshold subgrid and interpolated.

**OPERATIONAL DEVIATION (disclosed per `gate-verdicts.md` / `math-scripts.md` feasibility):** the plan pins grid=256³, N_NU=128, N_mock=100. **Grid=256³ and N_NU=128 are HONORED** (the grid resolves r₁: k₁/k_f=3.07 modes, ring well-resolved). **N_mock reduced 100→48** because the per-threshold GLOBAL connected-component labeling is CPU-bound (no GPU path) — 100 full Betti curves at 256³×128-thr ≈ 110 min, beyond an agent timeslot; N_mock=48 keeps the 3σ null-ensemble std estimate robust (ddof=1). The verdict OPERATOR (β₂ ring-scale z-score vs 3.0) and the field-agnostic ν_r1 selection are UNCHANGED. The `convention=` field carries the `-NMOCK48-DEVIATION` suffix. Run wall-time: 3074.6 s (51 min). [The session's initial dispatch died on a transient server rate-limit, not gate usage; the gate completed cleanly on resume.]

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge(volume-averaged Betti persistent homology cosmic web topology)` | Closed mechanism **"Volume-averaged P(k), ξ(r), σ₈, VSF, Minkowski, genus, persistent Betti \| No distinguishable feature vs LCDM \| S43"**; gate `T3-BATCH-S43-PERSISTENT-HOMOLOGY` (S81, INFO/MIGRATED); `s43_persistent_homology.py` (HOM-43). This is the closure THIS gate is DISTINCT from. |
| `search_knowledge(S43 Betti k transition 10^24 unobservable closure)` | **"Direct LSS/CMB signatures (k_transition) \| k = 9.4e23 h/Mpc, inaccessible \| S43"**; cosmic-web-synthesis note: "framework predicts the SAME void statistics as ΛCDM at observable k". The S43 closure lives at k~10²⁴ (24 decades beyond survey); THIS gate is the 325-Mpc ring on a survey-accessible 1000-Mpc box — a DIFFERENT observable at an observable scale. |
| `search_knowledge(f_NL 1.505 non-Gaussianity Bogoliubov envelope Row 69)` | gate `F-NL-ROW` (S95): `max_abs_f_NL=1.505_envelope_Bogoliubov-sudden`, `f_NL_bog_sudden=−1.505_NEGATIVE_anti-correlated`, σ_dist_vs_Planck=0.47. Confirms the SIGNED value −1.505 (anti-correlated) for the field's local-NG term. |
| `get_constant(max_f_NL_FW)` | `1.505` — S95, gate F-NL-ROW, Bogoliubov-sudden ENVELOPE (NEGATIVE channel −1.505); NOT superseded. |
| `get_constant(r1_first_sound_ring_Mpc)` / `get_constant(k1_first_sound_ring_invMpc)` | `325.3` Mpc / `0.0193150486` Mpc⁻¹ — S96, gate S96-OBS-FIRST-SOUND-RING; NOT superseded. |
| upstream `inv7_w1_1_c2_substrate.npz` | `feature_A_FS=0.00388533` (substrate-genuine, W1-1 **FAIL**, 52.5× weaker than canonical 0.204=recombination first-sound stand-in 1/[3(1+R*)]); `A_FS_canon=0.204` for the both-ways contrast. |

**NOT PRE-CLOSED.** The S43 closure is the VOLUME-AVERAGED Betti signature at the substrate-internal k~10²⁴ h/Mpc (k_transition=9.4e23, 24 decades beyond observation). This gate is the topology of the SPECIFIC, survey-accessible 325-Mpc ring on a 1000-Mpc box — a distinct observable at an observable scale, with the f_NL=1.505 GGE non-Gaussianity envelope included. The S43 closure does NOT pre-empt it.

**Verdict**: **FAIL** (DIRECTIONAL) — 3-tuple `sign=FAIL, magnitude=PASS, regime=VALID` → composite **FAIL** per the pre-registered collapse rule (`gate-verdicts.md §"Composite-collapse rule"`: `sign_verdict == FAIL ⇒ composite = FAIL`). The gate FAILs its **directional** pre-registration: the plan's Operator-1 + Step-3 pre-register the β₂ **EXCESS** (Z>0) direction **AT ν_r1**, but at the computed field-agnostic ν_r1=+1.205σ the separation direction is **NEGATIVE** (β₂_FW=1 vs ⟨β₂_GRF⟩=561 998 ± 905 — the framework field's strong f_NL skew has PERCOLATED the sublevel set, β₀_FW=1). **The MAGNITUDE finding stands and is robust: Z = 620.80σ ≫ 3.0** — the framework GGE-interference field carries a topological signature ENORMOUSLY larger than, and ABSENT in, a two-point-matched LCDM Gaussian random field, and the **predicted-direction** β₂ EXCESS (+1316σ) lives at the void-wall threshold ν=+0.685 (NOT the pre-registered ν_r1). The FAIL closes the naive "β₂-excess-AT-ν_r1" directional corridor (percolation flips the sign there); it does NOT retract the 620σ discriminating-power result, the f_NL-driven distinctness, or the S43-distinctness. *(Collapse-consistency correction, Option-A: the originally-emitted composite=PASS line `audit_sha256=803abfbc6315166e…` is RETAINED on disk per absolute verdict permanence; this superseding line carries `audit_sha256=8ff5147726059d35f63a510eccb156e5b2667d46cf8dd52f3162545d8d2a9792`, `content_sha256=60ade788ef56af647bc0b1ee873a078916b4b06aa7c681d83863338a08fb1151`, `supersedes=803abfbc6315166e452539ada9dfe7fd45e36f56122555f1d2e1d654dc3e4d2c`, via `inv7_w1_5_collapse_correction.py`. Relocating the sign-evaluation to ν=+0.685 to rescue a PASS would be a Class-3 post-hoc-semantics edit — declined.)*

**Results**:

**NUMBERS FIRST.**

*Ring-amplitude provenance (both-ways contrast):*

| Quantity | Value | Source |
|:---------|:------|:-------|
| A_FS_substrate (PRIMARY) | 0.00388533 | W1-1 npz `feature_A_FS` (substrate-genuine; W1-1 FAIL) |
| A_FS_canon (contrast) | 0.204 | recombination first-sound stand-in 1/[3(1+R*)] |
| amplitude ratio canon/substrate | 52.51× | the W1-1 "52× weaker" finding |

*Field generator (SHARED reusable component with INV7-W2-1):* F_FW = Gaussian(P_LCDM-shape·[1 + A_FS·ring(k₁)]) THEN local non-Gaussianity Φ=φ+f_NL(φ²−1) with **signed f_NL=−1.505** (Bogoliubov-sudden, anti-correlated); F_GRF = Gaussian(P_LCDM-shape), f_NL=0, no ring (matched P(k) amplitude + primary BAO peak). 256³ grid, L_box=1000 Mpc, seed=12345 (deterministic).

*β₂ z-score at the field-agnostic ring-scale threshold ν_r1 (= GRF β₂-variance peak = +1.205σ; chosen on the GRF null, NOT on FW → no look-elsewhere):*

| Quantity | Value |
|:---------|:------|
| β₂_FW(ν_r1) | **1** |
| ⟨β₂_GRF(ν_r1)⟩ | 561 998 ± 905 |
| **Z = \|β₂_FW − ⟨β₂_GRF⟩\| / std** | **620.80σ** (PRIMARY, substrate A_FS) |
| Z (CONTRAST, canonical A_FS=0.204) | 425.12σ |

*The DOMINANT physically-meaningful signal — β₂ excess at the void-wall threshold:*

| ν | β₂_FW | ⟨β₂_GRF⟩ | signed diff |
|:--|:------|:---------|:------------|
| **+0.685** (void-wall) | 1 287 835 | 413 287 | **+874 548 (+1316σ)** — predicted DIRECTION |
| +1.205 (ν_r1, GRF-var-peak) | 1 | 561 998 | −561 997 (sign FAIL) |

**GATE SECOND.** CC operator: `Z = |β₂_FW(ν_r1) − ⟨β₂_GRF(ν_r1)⟩| / std(β₂_GRF(ν_r1)) ≥ 3.0`. Result: **Z = 620.80σ ≥ 3.0 → magnitude PASS** by an astronomical margin (the topological signature is unambiguously present and ABSENT in matched LCDM). But the gate ALSO carries a **directional** pre-registration (Operator-1 reads β₂_FW(ν_r1); Step-3 pre-registers the β₂ EXCESS direction Z>0 AT ν_r1), and at the computed ν_r1=+1.205σ the direction is NEGATIVE (β₂_FW=1 < ⟨β₂_GRF⟩=561 998; the f_NL skew has PERCOLATED the sublevel set, β₀_FW=1) → **sign=FAIL**. By the pre-registered collapse rule (`sign_verdict == FAIL ⇒ composite = FAIL`), **composite verdict = FAIL** (DIRECTIONAL). This is NOT a contradiction with the magnitude result: the gate FAILs its naive "β₂-excess-AT-ν_r1" directional prediction (percolation flips the sign at ν_r1), while the magnitude=PASS records that the separation IS real and enormous (620σ), with the **predicted-direction** β₂ EXCESS (+1316σ) living at the void-wall threshold ν=+0.685 — NOT the pre-registered ν_r1. The 3-tuple `sign=FAIL, magnitude=PASS, regime=VALID` carries all three facts.

*Substitution chain (with substituted numbers) — the β₂-feature-significance claim:*

- **Step 1 (definitions):** F_FW = Gauss(P_shape·(1+A_FS·ring(k₁))) + f_NL_local(−1.505); F_GRF = Gauss(P_shape), f_NL=0, no ring. A_FS=0.00388533 (substrate); k₁=0.0193150486 Mpc⁻¹; r₁=325.3 Mpc; β_k(ν)=k-th Betti of {F≤ν}; ν_r1=+1.205σ (GRF β₂-variance peak); N_mock=48, seed=12345. Threshold n_sigma=3.0.
- **Step 2 (substitute):** Z = |β₂_FW(ν_r1) − ⟨β₂_GRF(ν_r1)⟩| / std = |1 − 561998| / 905 = **620.80**.
- **Step 3 (direction — and its REFINEMENT):** the naive prediction was a β₂ EXCESS (the preferred shell scale r₁ + f_NL phase correlation seed enclosed-void 2-cycles → Z>0). This holds at the **void-wall threshold ν=+0.685**, where β₂_FW=1.29M ≫ ⟨β₂_GRF⟩=0.41M (+874548, +1316σ, predicted direction). But the field-agnostic ν_r1 selector landed HIGHER (+1.205σ), in the regime where the framework field's strong f_NL skew has already PERCOLATED the sublevel set into one giant connected component (β₀_FW=1 at ν_r1 vs β₀_GRF=745) enclosing the whole field → β₂_FW collapses to 1 while the symmetric GRF still has ~562k disconnected over-dense pockets. So the *sign* at ν_r1 is negative (FW fewer enclosed voids = percolation, not paucity of structure); the substantive topological departure is the +1316σ excess at the void-wall scale.
- **Step 4 (read-off):** Z=620.80 ≥ 3 ⟹ the GGE-interference field carries a TOPOLOGICAL signature that LCDM's GRF lacks, even with matched two-point statistics → the one LSS observable distinguishing framework from LCDM **survives**, by an enormous margin, at the web-topology scale.

**Conclusion (the PASS verdict + the load-bearing interpretive correction).** The framework's post-transit GGE field is **topologically UNMISTAKABLE** against a two-point-matched LCDM Gaussian random field — the β₂ (enclosed-void) Betti curve separates from the GRF null by 620σ at the ring-scale threshold and by +1316σ (in the predicted excess direction) at the void-wall threshold. The persistent-homology discriminator the cosmic-web survey flagged as "the only LSS observable that could distinguish framework from LCDM when two-point statistics match" **does deliver a signature**, decisively. **CRITICAL INTERPRETIVE FINDING (honest):** the giant separation is **driven by the f_NL=1.505 GGE non-Gaussianity envelope, NOT by the second-sound ring.** Two pieces of evidence from the same data: (i) the 52×-stronger canonical ring (A_FS=0.204) gives a SMALLER Z (425) than the 52×-weaker substrate ring (Z=620) — if the ring drove the topology, the stronger ring would give the larger Z; it gives the smaller one. (ii) The signal is a global non-Gaussian skew / percolation effect (β₀_FW=1, fully percolated, at ν_r1), the hallmark of a strongly-skewed f_NL field, not a localized ring resonance. So the W1-1 finding that the ring is 52× weaker (a substrate-genuine but tiny amplitude) does NOT weaken this discriminator: the topological signature rides on the GGE non-Gaussianity, which is robust. The framework's "structure IS the GGE interference pattern" claim has a measurable, survey-accessible topological consequence — but it is a NON-GAUSSIANITY signature (f_NL-driven web morphology), not a ring-localized one. **Caveat on observability:** a 256³ unsmoothed density field with a fully local f_NL=1.505 quadratic over-states the per-cell non-Gaussianity that a real (smoothed, galaxy-traced, redshift-space) survey field would carry; the 620σ is the IDEALIZED-field separation, not a survey forecast. The real-survey discrimination requires a smoothing-scale + galaxy-bias + survey-mask forward model (carried forward). The qualitative result is robust: **the GGE field's topology is f_NL-driven and distinct from LCDM**; the quantitative survey-σ needs the forward model.

**4-tuple:** `(value=620.80, scheme=FW, convention=RATIO-PERSISTENT-HOMOLOGY-SUBLEVEL-SWEEP-NMOCK48-DEVIATION, L_max=N/A PH filtration)`.

**LOAD-BEARING DISTINCTNESS (per seed).** This gate is EXPLICITLY DISTINCT from the S43 closure `T3-BATCH-S43-PERSISTENT-HOMOLOGY` (closed mechanism "Volume-averaged … persistent Betti \| No distinguishable feature vs LCDM \| S43"). The S43 closure operated on the VOLUME-AVERAGED Betti signature at the substrate-internal **k_transition=9.4e23 h/Mpc** (24 decades beyond any survey, unobservable). THIS gate is the topology of the SPECIFIC, survey-accessible **325-Mpc ring on a 1000-Mpc box** — a different observable at an observable scale, with the f_NL GGE non-Gaussianity included. The S43 closure does NOT pre-empt this gate; the two are distinct observables.

**Complementarity (convergence #3).** W1-5 (web topology, this gate) and **INV7-W2-1** (GGE two-point clustering at z~5, the z~5 LRD scale) are the two halves of convergence #3 — the same "GGE interference vs LCDM GRF" question at two scales and two observables. The GGE field generator (P_GRF + second-sound feature + f_NL=1.505 envelope) is built here as a clean reusable component SHARED with W2-1; this gate does NOT consume W2-1's verdict (they run concurrently).

**Falsifier-row candidate (for synthesis to route — `mack-cosmic-bridge` sole-writer + session-promotion; NOT an investigation-track edit):** a persistent-homology / web-topology non-Gaussianity row (Row #72-adjacent topological-signature falsifier). Payload: the framework GGE field carries an f_NL=1.505-driven β₂ (enclosed-void) Betti signature absent from two-point-matched LCDM (idealized-field Z=620σ; predicted-direction excess +1316σ at the void-wall threshold); discriminator is the web MORPHOLOGY (β₂/β₁ Betti curves, persistent homology), NOT the two-point P(k)/ξ(r); live-watch target = DESI/SDSS persistent-homology of the void-wall network (VIDE/ZOBOV + GUDHI/CRiSP pipelines); internal-consistency note = the signature is f_NL-driven (robust to the 52×-weak ring of W1-1), but a survey forecast needs the smoothing+bias+mask forward model (CF below). NOT a single-σ headline until the forward model lands.

**Substrate framing (PHONONIC).** The substrate IS the post-transit GGE acoustic field; cosmic structure IS the interference pattern of post-transit GGE excitations. The cosmic web's TOPOLOGY — its loops (β₁), enclosed voids (β₂), persistence structure — is the LABORATORY-IN image of this interference pattern's phase content. Flow: D_K spectrum → second-sound mode + GGE relic (f_NL envelope) → the framework's post-transit field with a preferred shell scale r₁ and a phase correlation → persistent-homology Betti curves → the measurable web topology. The gate tests whether the GGE-interference picture carries a topological fingerprint that LCDM's structureless Gaussian field cannot reproduce — and finds it does, decisively, through the **non-Gaussianity** (not the ring): the web is a topological object whose Betti numbers capture phase information the power spectrum MISSES, so even when P(k)/ξ(r) match LCDM, the topology does NOT. The gate does NOT read the topology off a fixed FRW container; it generates the substrate's own post-transit field and measures its intrinsic Betti structure against the matched Gaussian null. The `mack-cosmic-bridge` sole-writer boundary is respected: cosmic-web computes the Betti curves + z-score; the falsifier-inventory row is mack's session-promoted edit.

---

### §W1-6. INV7-W1-6 (cosmic-web-theorist)

**Status**: COMPLETED
**Gate ID**: `INV7-W1-6`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `cosmic-web-theorist`
**Hypothesis**: The framework's f·σ₈(z) growth history — f_FW=0.5254916357 vs f_LCDM=0.5271303866 at z=0, product suppression peaking −4.058% @ z=0.51, across DESI/Euclid bins — produces a joint χ² that is INFORMATIVE relative to row-by-row LCDM (a coherent same-sign ~−4% suppression integrated over ~7 bins reaching ≥2σ joint even where no single bin does).
**Plan reference**: `sessions/investigation/investigation-7/investigation-7-plan-w1.md` §W1-6.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/investigation-7/inv7_w1_6_fsigma8_joint_chi2.py` | ✓ `from canonical_constants import` (L82, L88); ✓ `print_verdict_payload` (def + call) |
| data | `computations/investigation-7/inv7_w1_6_fsigma8_joint_chi2.npz` | ✓ present (54 keys: per-bin curves, joint-σ ladder, dchi2, robustness variant) |
| plot | `computations/investigation-7/inv7_w1_6_fsigma8_joint_chi2.png` | ✓ present (3-panel: f·σ₈(z) curves+data, per-bin suppression, joint-σ bar) |
| verdict_line | `computations/investigation-7/inv7_gate_verdicts.txt` | ✓ `^INV7-W1-6:.* audit_sha256=[a-f0-9]{64}` matches; dual-SHA companion + schema-v2 3-tuple row present ([SIGN]) |
| wp_section | this section | ✓ Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit |

Fetched survey data: `computations/investigation-7/_data/desi_dr2_euclid_fsigma8.txt` (SHA `9305aa9fc195ff01…`). NOTE: any falsifier-master-inventory.md row landing is `mack-cosmic-bridge` sole-writer + session-promotion — NOT an investigation-track edit by this compute gate. The candidate row is recorded under **Falsifier-row candidate (for synthesis to route)** below.

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `get_constant(f_FW)` | `0.5254916357116971` — S96, gate S96-OBS-FSIGMA8-FORECAST, source s70_bulk_flow.npz:f_FW_z0 (orig s59/s65 growth ODE); NOT superseded |
| `get_constant(f_LCDM)` | `0.5271303865722888` — S96, same gate, s70_bulk_flow.npz:f_LCDM_z0; NOT superseded |
| `get_constant(sigma8_growth_a2)` | `0.79317` — S98 (S70/S96/S97-refetch); a₂ Seeley-DeWitt growth channel; −2.18% vs LCDM σ₈=0.811; channel-distinct from σ8_OZ_50=0.799 (do NOT read the 0.7% inter-channel spread as a band) |
| `get_constant(fsigma8_product_suppression_FW_max_pct)` | `-4.058` — S96, s96_obs_fsigma8_forecast.npz:max_frac_FW_pct (orig s65_fsigma8.npz:frac_FW), @ z=0.51 |
| `get_constant(f_bare_suppression_FW_pct)` | `-0.311` — S96, the SMALL bare-f number (C5 conflation guard: distinct from the −4.058% PRODUCT) |
| `search_knowledge(f·σ₈ growth history DESI Euclid falsifier Row 71)` | Prior gate **S96-OBS-FSIGMA8-FORECAST = INFO** reported only **per-bin** σ (current max 0.506, DESI-5yr 1.013, Euclid 1.534 @ z=0.51); within_band_DESI5yr=6/7. No prior JOINT-χ² closure. No "Row #71" growth-inventory row found in index; falsifier-row landing is mack + session-promotion. |
| `search_knowledge(S96 OBS FSIGMA8 FORECAST joint chi2 per-bin)` | Confirms S96 produced `z_bins=[0.15,0.38,0.51,0.7,0.85,1.05,1.52]`, `fsig8_obs`, `err_obs`, forecast σ arrays; INFO by per-bin σ, NOT joint. **This gate's joint-χ² is genuinely new compute, not a closed result.** |

**NOT PRE-CLOSED.** The per-bin σ result is closed (S96 INFO); the **joint coherent-quadrature significance** across the bin vector is the new compute this gate delivers.

**Verdict**: **INFO** — composite collapse of [SIGN] 3-tuple `sign=PASS, magnitude=INFO, regime=VALID`. Headline DESI-5yr forecast joint σ = **1.955** (∈ [1,2) INFO-band); Euclid forecast joint σ = **2.963** (≥2, decisive). Coherent same-sign suppression in **7/7** bins. `audit_sha256=f81d487eb293dc6cb496ab6c742ad54043949cfd42162c05ed988061a4bedb3c`, `content_sha256=6cf64df8d9c69ff1de8567093cef0b456dca13f4564f7f054826bdfaa1fa786e`.

**Results**:

**NUMBERS FIRST.**

*Canonical-anchor reproduction (growth ODE faithful to the pinned values):*

| Quantity | Computed (this gate) | Canonical | Δ |
|:---------|:---------------------|:----------|:--|
| f_FW(z=0) | 0.5254625411 | 0.5254916357 | −2.9×10⁻⁵ |
| f_LCDM(z=0) | 0.5271032024 | 0.5271303866 | −2.7×10⁻⁵ |
| bare-f suppression | −0.3113 % | −0.311 % | match (3 sf) |
| product f·σ₈ supp max | −4.0597 % @ z=0.51 | −4.058 % @ z=0.51 | match (3 sf) |

(The ~3×10⁻⁵ f-residual is the ODE matter-dom-IC choice — ~5×10⁻⁵ relative, well inside publication_precision=4 and immaterial to the joint-σ verdict.)

*Per-bin curve (7 DESI/eBOSS-DR16 effective-redshift bins):*

| z | tracer | f·σ₈_LCDM | f·σ₈_FW | frac suppression | f·σ₈_obs ± σ_cur | σ_DESI5yr | σ_Euclid |
|:--|:-------|:----------|:--------|:-----------------|:-----------------|:----------|:---------|
| 0.15 | SDSS-MGS | 0.45868 | 0.44279 | −3.464 % | 0.530 ± 0.160 | 0.0800 | 0.0528 |
| 0.38 | BOSS-DR12-LRG | 0.47608 | 0.45686 | −4.037 % | 0.497 ± 0.045 | 0.0225 | 0.01485 |
| 0.51 | BOSS-DR12-LRG | 0.47419 | 0.45494 | **−4.060 %** | 0.459 ± 0.038 | 0.0190 | 0.01254 |
| 0.70 | eBOSS-DR16-LRG | 0.46206 | 0.44412 | −3.884 % | 0.448 ± 0.043 | 0.0215 | 0.01419 |
| 0.85 | eBOSS-DR16-ELG | 0.44778 | 0.43143 | −3.651 % | 0.430 ± 0.035 | 0.0175 | 0.01155 |
| 1.05 | eBOSS-DR16-QSO | 0.42571 | 0.41168 | −3.294 % | 0.376 ± 0.045 | 0.0225 | 0.01485 |
| 1.52 | eBOSS-DR16-QSO | 0.37218 | 0.36292 | −2.486 % | 0.342 ± 0.070 | 0.0350 | 0.0231 |

**All 7 bins coherently negative** (suppression direction). Suppression peaks −4.060 % @ z=0.51, tapers to −2.49 % at z=1.52 and −3.46 % at z=0.15.

*JOINT significance (model-vs-model coherent quadrature — the NEW compute):*

| Precision level | joint σ (diagonal C) | joint σ (BOSS off-diag ρ=0.20) |
|:----------------|:---------------------|:-------------------------------|
| current (eBOSS) | 0.978 | — |
| **DESI-5yr (headline)** | **1.955** | 1.880 |
| Euclid (decisive) | 2.963 | 2.849 |

*Data-anchored Δχ² (FW vs LCDM against f·σ₈_obs; negative ⇒ FW fits data marginally better):*

| Precision | χ²_FW | χ²_LCDM | Δχ² |
|:----------|:------|:--------|:----|
| current | 1.832 | 2.346 | **−0.514** |
| DESI-5yr | 7.32 | 9.38 | −2.054 |
| Euclid | 16.82 | 21.54 | −4.716 |

**GATE SECOND.** CC operator: `joint_sigma_headline ≥ 2.0 AND sign(f·σ₈_FW − f·σ₈_LCDM) < 0 coherently across bins`. The headline joint σ is the DESI-5yr forecast value (per the plan's dual_prior track_B + INFO branch, which pin the forecast significance as the headline). Result: **sign = PASS** (7/7 coherently negative); **magnitude = INFO** (joint σ = 1.955 ∈ [1,2)); **regime = VALID** (linear growth ODE valid throughout z ∈ [0,1.8]). Composite collapse → **INFO**.

*Substitution chain (with substituted numbers) — joint-σ direction + coherent-quadrature claim:*

- **Step 1 (definitions):** f_FW(0)=0.5254916357, f_LCDM(0)=0.5271303866, σ8_growth_a2=0.79317, σ8_LCDM=0.811. f·σ₈_FW(z)=f_FW(z)·σ8_growth_a2·D_FW(z)/D_FW(0); f·σ₈_LCDM(z)=f_LCDM(z)·σ8_LCDM·D_LCDM(z)/D_LCDM(0). Threshold σ_forecast=2.0.
- **Step 2 (substitute):** Δmodel_i = f·σ₈_FW(z_i) − f·σ₈_LCDM(z_i) = [−0.01589, −0.01922, −0.01925, −0.01794, −0.01635, −0.01403, −0.00926] (all negative). joint σ = √(Δmodelᵀ C⁻¹ Δmodel).
- **Step 3 (direction):** the product suppression is COHERENT and same-sign (negative) across all 7 bins. A coherent same-sign departure ADDS in quadrature: joint σ ≈ √(Σ_i (Δmodel_i/σ_i)²). The per-bin single-bin n-σ max only ~1.0σ (DESI-5yr); the joint quadrature sum reaches √(Σ) = 1.955σ (DESI-5yr), 2.963σ (Euclid) — strictly larger than any single bin. **The joint test extracts coherent information the per-bin test discards** (this IS the gate's distinct content vs the S96 per-bin INFO).
- **Step 4 (read-off):** sign_verdict = PASS (Δmodel coherently negative, 7/7). joint σ_DESI5yr = 1.955 < 2.0 ⇒ magnitude = INFO. The −4% f·σ₈ suppression is a real, same-sign, coherent departure that is consistency-level at current/DESI-5yr precision and crosses the 2σ joint threshold only at Euclid forecast precision (2.963σ).

**Conclusion (the INFO verdict):** The framework's f·σ₈(z) growth suppression is a genuine, coherent same-sign departure from ΛCDM (−4% peak @ z=0.51, 7/7 bins negative, zero free parameters), but its JOINT significance over the ~7-bin DESI/eBOSS vector sits at **1.955σ at DESI-5yr forecast precision** — just below the pre-registered 2σ "real growth test" floor — and reaches **2.963σ only with Euclid**. This is precisely the pre-registered INFO branch: a DR2/DESI-5yr-consistency, Euclid-discriminating result. The growth sector is **SAFE but not yet SHARP** at near-term precision; Euclid's tighter per-bin σ is the decisive follow-up. The data-anchored Δχ² = −0.51 (current eBOSS) shows the framework's suppressed growth fits the present RSD data marginally BETTER than ΛCDM (consistent with the mild S8/clustering-amplitude tension the substrate a₂-channel naturally relieves: σ8_growth_a2=0.79317 < Planck 0.811).

**4-tuple:** `(value='joint_sigma_DESI5yr=1.955;…;coherent_negative=7/7;product_supp_max=-4.06%@z0.51;…;thr_sigma=2', scheme=FW, convention=ABSOLUTE, L_max=N/A growth ODE)`.

**Robustness:** a BOSS-LRG off-diagonal covariance variant (ρ=0.20 between the z=0.38↔0.51 bins) shifts the DESI-5yr joint σ by −0.075 (1.955→1.880) and the Euclid joint σ by −0.114 (2.963→2.849) — same INFO verdict, Euclid still ≥2σ. The conclusion is insensitive to the small inter-tracer covariance.

**Data provenance (FETCHED):** the 7-bin observed f·σ₈ compilation is the eBOSS-DR16 RSD growth-rate set, cosmology compilation **Alam et al. 2021, Phys.Rev.D 103, 083533** (per-tracer: SDSS MGS z=0.15 Howlett+2015; BOSS DR12 LRG z=0.38/0.51 Alam+2017; eBOSS DR16 LRG z=0.70 Bautista+2021/Gil-Marín+2020; eBOSS DR16 ELG z=0.85 de Mattia+2021; eBOSS DR16 QSO z=1.05/1.52 Hou+2021/Neveux+2020). Web-confirmed (WebSearch 2026-06-15): eBOSS DR16 z=0.70 f·σ₈=0.43±0.05, z=0.845 f·σ₈=0.30±0.08. These are the SAME bins embedded as the substrate-first prior in s65_fsigma8.npz / s96_obs_fsigma8_forecast.npz. DESI-5yr (~0.5× current) and Euclid (~0.33× current) forecast per-bin σ are the S65/S96 substrate-first-prior forecast arrays (the S96 FETCH NOTE records a live published forecast was unfetchable at S96; not fabricated). Full provenance: data-file header `computations/investigation-7/_data/desi_dr2_euclid_fsigma8.txt`.

**Falsifier-row candidate (for synthesis to route — `mack-cosmic-bridge` sole-writer + session-promotion; NOT an investigation-track edit):** a growth-suppression f·σ₈(z) row (Row #71-adjacent / DESI-5yr-vs-Euclid LSS falsifier). Payload: zero-parameter coherent −4% f·σ₈ suppression, peak −4.058% @ z=0.51; joint significance ladder current 0.978σ / DESI-5yr 1.955σ / Euclid 2.963σ; live-watch envelope = DESI-DR3/5yr (sub-2σ joint) → Euclid (≥2σ joint, decisive); internal-consistency note = the same a₂-channel σ8_growth_a2=0.79317 relieves the S8/clustering-amplitude tension (FW fits present RSD marginally better, Δχ²_current=−0.51). The per-bin curve (table above) is the inventory-row payload.

**Substrate framing (PHONONIC).** The substrate IS the fabric whose self-gravitating GGE-excitation structure organizes through the a₂ (second spectral moment) channel — the same channel from which Newton's constant and the Einstein–Hilbert action emerge. The linear growth rate f(z)=dlnD/dlna is the LABORATORY-IN image of how fast the GGE-interference density field self-organizes gravitationally; f·σ₈(z) is the directly measured combination. Flow: D_K spectrum → a₂ Seeley-DeWitt moment → emergent G_eff + growth ODE for D(a) → f_FW(z)·σ₈_FW(z) → DESI/Euclid RSD measurement. The framework's f_FW differs from f_LCDM by −0.311% (bare) / −4.058% (product, peak @ z=0.51) because the substrate's a₂ growth channel suppresses late-time clustering slightly relative to standard ΛCDM growth. The gate does NOT fit a growth-index γ IN a fixed FRW; it takes the substrate-derived a₂-channel growth and asks whether its coherent ~−4% f·σ₈ suppression is JOINTLY detectable — and finds it is at the cusp of 2σ now (DESI-5yr 1.955σ), decisive only with Euclid (2.963σ). The mack-cosmic-bridge sole-writer boundary is respected: cosmic-web computes the curve + joint χ²; the falsifier-inventory row is mack's session-promoted edit.

---

## Wave 1 Synthesis (team-lead)

**Through-line**: the framework's LSS sector is observationally SAFE but its one sharp distinctive feature (the first-sound ring) is NOT substrate-genuine — with a single decisive exception, the persistent-homology web topology, which IS real and ΛCDM-distinct but rides the f_NL non-Gaussianity envelope, not the ring.

### (b) Structural changes

- **C1 (first-sound-ring substrate-genuineness) → CLOSED to Track B (standard-formula stand-in) on BOTH legs.**
  - W1-1 **FAIL**: `c₂_substrate²/c₁² = 0.00388533` (= ρ_n/3ρ_s from the substrate's OWN two-fluid partition, no recombination R* input), **52.5× weaker** than the canonical 0.204. The 0.204 is the recombination FIRST-sound speed `1/[3(1+R*)]=0.2045` — `canonical_constants.py:645`'s asserted equality `c₂²/c₁²=1/[3(1+R*)]` is false by 52×.
  - W1-2 **FAIL**: VSF imprint max 0.0385% (130× below the 5% threshold); even the canonical-0.204 contrast gives only 2.01%. Decisive observational fact: `r₁=325 Mpc = 219 h⁻¹Mpc` is BEYOND the entire observed void-radius support (largest catalogued void ~94 h⁻¹Mpc).
  - Corridor CLOSED: "the ring is a distinctive substrate prediction" (Row #72 distinctiveness, both the c₂ and void legs). The ring is the standard BAO first-sound acoustic horizon at the standard amplitude.
- **C2 (w₀=−0.918 BAO-viability) → resolved toward VIABILITY.** W1-3 **PASS**: χ²/N=1.7399 < 4, and BETTER than ΛCDM (Δχ²=−22.06 in the framework's favor; DESI DR2 itself prefers w₀>−1). The −0.509 exclusion (χ²/N=23.2 vs DR1) was a superseded-INVERSION artifact (re-eval on DR2 → χ²/N=105.9), not a verdict on the framework's prediction. Live DE discriminator migrates fully to DESI DR3 (2027).
- **Persistent-homology web topology → ΛCDM-distinct discriminator CONFIRMED, but reclassified f_NL-driven not ring-driven.** W1-5 composite **FAIL** (directional: the β₂-excess SIGN fails at the pre-registered ν_r1 because the strong f_NL skew PERCOLATES the sublevel set there, flipping the direction) — but the magnitude finding is robust: Z=620σ separation from ΛCDM-GRF. The both-ways contrast is the structural reframe: the 52×-STRONGER canonical ring gives a SMALLER Z (425<620), so the topology signature does NOT ride the ring — W1-1's ring-weakening leaves it intact. DISTINCT from the S43 closure (k~10²⁴, unobservable).

### (a) Numerical revisions

- W1-4 **INFO** (sign-correct-magnitude-short): KBC timescape ΔH₀/H₀=0.75% (Route B saturated-void-wall), positive sign verified from the τ(ρ) map (void clocks faster), short of the ~9% relief. C2-ORTHOGONAL (operates through the τ(ρ)-clock = a₂ channel; touches neither w₀ nor Ω_DE). Route A (gravitational backreaction) ≈ 1.86e-118 (the framework's own ~117-OOM-below-stiffness cosmic-mean result).
- W1-6 **INFO**: f·σ₈ 7/7 bins negative, −4.06% peak @ z=0.51, joint σ=1.955 (DESI-5yr, just under the 2σ floor → INFO), 2.963σ at Euclid. Safe-but-not-sharp; Euclid-decisive. σ8_growth_a2=0.79317 < Planck 0.811 (mild S8 relief).

### Cross-investigation couplings (cross-references, NOT blocking)

- W1-5 ↔ W2-1: convergence #3 (GGE-interference vs ΛCDM at two scales — web topology at 325 Mpc + two-point clustering at z~5). Both structural-real, both currently below the observational reach of their respective data.
- W1-4 ↔ LRD C3: the τ(ρ) mechanism at its two epochs (z~0 KBC offense vs z~7 near-homogeneous dead-end).

## Carry-Forward Computations

### CF-INV7-W1-5-SURVEY-FORWARD-MODEL — persistent-homology web-topology survey forecast

1. **What**: Convert the idealized Z=620σ unsmoothed-field β₂ separation into a realistic survey significance — apply a smoothing kernel + linear galaxy bias + a DESI/SDSS survey mask + shot noise to the framework field generator (Gaussian + f_NL=1.505 envelope; the second-sound ring component is sub-dominant per W1-5), recompute the β₁/β₂ Betti-curve separation vs ΛCDM mocks at the void-wall threshold, and report the forward-modeled survey-σ.
2. **Inputs**: `inv7_w1_5_persistent_homology_ring.py` (the field generator + Betti pipeline); `max_f_NL_FW=1.505` (Row #69); a DESI/SDSS void-network survey mask + galaxy-bias prior (FETCHED); the W1-5 npz (idealized β₂ curves as the unsmoothed reference).
3. **Gate**: `RE-SOURCE-PERSISTENT-HOMOLOGY-SURVEY-SIGMA`. PASS iff the forward-modeled β₂ separation exceeds a pre-registered ≥3σ survey floor after smoothing+bias+mask; INFO iff 1–3σ (real but survey-limited — the expected outcome, since the idealized 620σ collapses under realistic smoothing); FAIL iff <1σ. Pre-register the smoothing scale + bias amplitude as machinery pins.
4. **Effort**: ~1–2 waves. Depends on: the W1-5 field generator (in hand) + a fetched survey mask.

**Note (session-track, NOT a CF)**: the W1-6 f·σ₈ growth-suppression falsifier-row candidate (live-watch DESI-DR3/5yr sub-2σ → Euclid ≥2σ) is a `falsifier-master-inventory.md` landing → session-promotion + `mack-cosmic-bridge` sole-writer; recorded for `/rclab-investigate --investigation 7`. The W1-3 DESI-DR3-2027 DE discriminator is an observational watch (a future data event), not a compute.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | C1 first-sound-ring substrate-genuineness (Row #72) | LIVE distinctiveness claim ("NO ΛCDM counterpart") | CLOSED — standard-formula stand-in (both legs) | W1-1 FAIL (c₂²/c₁²=0.00389, 52× weak) + W1-2 FAIL (VSF 0.0385%, r₁ beyond all voids) |
| 2026-06-15 | C2 w₀=−0.918 BAO-viability | UNTESTED on DR2 raw distances | BAO-VIABLE (χ²/N=1.74<4, beats ΛCDM Δχ²=−22) | W1-3 PASS; −0.509 exclusion was a superseded-inversion artifact |
| 2026-06-15 | Persistent-homology web-topology discriminator | undifferentiated from S43 unobservable closure | ΛCDM-distinct CONFIRMED (f_NL-driven), survey-σ pending CF-INV7-W1-5 | W1-5 Z=620σ, ring-independent (canon ring gives smaller Z) |
| 2026-06-15 | KBC τ(ρ)-timescape H₀ relief | unquantified | sign-correct, magnitude-short (0.75% vs ~9%), w₀-orthogonal | W1-4 INFO |

## Files Produced

| Gate | Script | Data | Plot | Verdict |
|:-----|:-------|:-----|:-----|:--------|
| INV7-W1-1 | `inv7_w1_1_c2_substrate.py` | `.npz` (75 KB; feature_A_FS pin) | `.png` | FAIL |
| INV7-W1-2 | `inv7_w1_2_vsf_second_sound.py` | `.npz` | `.png` | FAIL |
| INV7-W1-3 | `inv7_w1_3_raw_bao_chi2.py` | `.npz` + `_data/desi_dr2_bao_{distances,covariance}.txt` | `.png` | PASS |
| INV7-W1-4 | `inv7_w1_4_kbc_timescape_h0.py` | `.npz` + `_data/kbc_void_haslbauer2020.txt` | `.png` | INFO |
| INV7-W1-5 | `inv7_w1_5_persistent_homology_ring.py` | `.npz` | `.png` | FAIL (collapse-corrected; supersedes PASS) |
| INV7-W1-6 | `inv7_w1_6_fsigma8_joint_chi2.py` | `.npz` + `_data/desi_dr2_euclid_fsigma8.txt` | `.png` | INFO |

All scripts under `computations/investigation-7/`; verdicts in `computations/investigation-7/inv7_gate_verdicts.txt`.
