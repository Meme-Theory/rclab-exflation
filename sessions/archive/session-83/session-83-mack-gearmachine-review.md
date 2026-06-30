# Session 83 Synthesis: Mack Observational-Priority Review of Gear-Machine Thought Experiment

**Date**: 2026-04-18
**Agent**: mack-cosmic-bridge (Mack)
**Source Documents**:
- sessions/archive/session-83/workshops/s83-gear-machine-thought-experiment.md
- .claude/agent-memory/mack-cosmic-bridge/MEMORY.md (S66 tensor-transfer, S68 CMB-S4 forecasts, S71 alpha_s Bayesian shadow)
- sessions/permanent-results-registry.md (T15 alpha_s = n_s^2 - 1 entry)

---

## I. Session Outcome

The gear-machine workshop is a productive structural narrative that converges on one observationally-viable quantitative discriminator — **alpha_s = n_s^2 - 1 = -0.0690**, already at **9.62-sigma tension with Planck 2018** (Python-verified) — and four others of decreasing observational sharpness. The workshop's declared "34-sigma CMB-S4 decisive at ~2030" is Python-verified GIVEN sigma(alpha_s)=2e-3, which is consistent with the CMB-S4 Collaboration 2019 baseline forecast. Tesla's gear-wall framing is pedagogically productive for observational physicists BUT the workshop's second decisive discriminator (n_T blue at +0.468) conflates transit-scale and CMB-scale quantities — a pattern my S66 memory (TENSOR-TRANSFER-66 FAIL, n_T(k_CMB) = -3.02e-3) already flagged and the workshop does not acknowledge. This review identifies 2 of 5 discriminators as CMB-S4-imminent, 1 mis-scaled, 2 long-horizon.

---

## II. Key Results

### II.1 alpha_s = n_s^2 - 1 is the workshop's one genuine imminent-era discriminator

**Result**: alpha_s_framework = n_s^2 - 1 = **-0.068968** at n_s = 0.9649 (Python-verified); Planck 2018 tension **9.622-sigma** against measurement alpha_s = -0.0045 ± 0.0067; CMB-S4 projected separation vs. slow-roll landscape baseline **33.98-sigma** at sigma(alpha_s) = 2e-3. **Classification: GEOMETRIC** (structural identity from S50, derived via Mellin-moment relation on the spectral propagator; labeled T15 in permanent-results-registry).

Substitution chain for Planck tension:
- Definition: framework identity alpha_s = d n_s / d ln k, and S50 T15 theorem asserts alpha_s_id = n_s^2 - 1 for any K^2 propagator.
- Substitution: (n_s_Planck)^2 - 1 = 0.9649^2 - 1 = -0.068968.
- Simplification: |alpha_s_framework - alpha_s_Planck| / sigma_Planck = |-0.068968 - (-0.0045)| / 0.0067 = 9.622.
- Direction: the framework identity, evaluated at the measured n_s, predicts an alpha_s that is LARGER-MAGNITUDE-NEGATIVE than Planck's central value by 9.62 sigmas. Already-tension, not future-tension.

**Key observational reframing the workshop missed**: the 9.62-sigma tension is **present today**, not pending CMB-S4. If the framework's T15 identity is taken seriously, Planck 2018 already constrains it at >9-sigma significance. CMB-S4's role is to shrink the sigma(alpha_s) uncertainty to ~2e-3, at which point the 34-sigma discrimination becomes decisive AGAINST any slow-roll alternative (K1 IIB, K2 heterotic) that predicts |alpha_s| ~ 1e-3. The workshop's framing as "decisive at ~2030" understates the CURRENT status.

**Scheme-independence caveat (S82 comment in registry)**: my knowledge-base search found an S82 W3-9 script comment reading: "the identity alpha_s = n_s^2 - 1 is a SCHEME identity for certain slow-roll functionals, not a framework prediction." Workshop R3 frames T15 as unconditionally permanent; registry notes suggest the identity may be scheme-dependent. This needs to be closed at S84 before the discriminator is pre-registered as a CMB-S4 gate. (See CF-1 below.)

### II.2 n_T blue tilt is SCALE-MISMATCHED — workshop overclaims observational reach

**Result**: workshop asserts framework prediction n_T = +0.468 as CMB-S4-discriminating. Agent memory (S66 TENSOR-TRANSFER-66 FAIL) records: **n_T(k_CMB) = -3.02e-3**, blue tilt localized at transit scale across 54 decades from CMB, r(CMB) = 0.024 PASS at 24.2-sigma LiteBIRD (S68 LITEB-R-FORECAST-68). **Classification: GEOMETRIC** structural but observationally-mis-localized.

Substitution chain for the mismatch:
- Definition: n_T = d ln P_T / d ln k. CMB measures tensor tilt at k_CMB ~ 0.005 Mpc^-1. Transit occurs at the fold scale k_fold, separated from k_CMB by ~54 decades.
- Substitution: S65 scan n_T at transit scale ∈ [+0.289, +0.892] (the workshop's Γ5' substrate claim, verified in S65); S66 W-TRANSFER computes n_T(k_CMB) via transfer function across the intervening decades.
- Simplification: under the S66 transfer kernel, the blue tilt does not propagate to CMB scale — the CMB-scale n_T is dominated by standard single-field consistency n_T = -r/8, giving n_T(k_CMB) = -0.003 for r(CMB) = 0.024.
- Direction: the observationally-accessible n_T at k_CMB is NOT blue. The blue-tilt prediction is structurally correct AT the substrate-transit scale, but no CMB-era instrument can probe that scale.

**Observational verdict**: the workshop's n_T axis of its 5-test discrimination plane does not survive the scale-transfer. LiteBIRD + CMB-S4 will measure n_T at k_CMB, where the framework prediction is identical-to-slow-roll at -r/8. The n_T axis should be REMOVED from the 5-discriminator table as a CMB-S4 gate, and replaced with r(CMB) = 0.024 at 24-sigma LiteBIRD PASS.

### II.3 Alternative machine-state (tau ∈ {0.10, 0.30}) is genuine internal-consistency test, NOT observational

**Result**: Γ1' cubic-BC mesh jams at +102.2% (tau = 0.10) and -67.7% (tau = 0.30) — Python-verified against workshop's claims (both match to 0.1%). Γ5' blue-lock holds across [0.10, 0.30]. **Classification: GEOMETRIC structural, non-observational.**

Substitution chain for the alternative-tau analysis:
- Definition: sin^2(mu_BC) = 3 / (3 + exp(12 * tau)).
- Substitution: at tau = 0.190, target = 3 / (3 + exp(2.28)) = 0.234803; at tau = 0.10, val = 3 / (3 + exp(1.2)) = 0.474675; at tau = 0.30, val = 3 / (3 + exp(3.6)) = 0.075761.
- Simplification: deviation at tau=0.10 is (0.4747 - 0.2348)/0.2348 = +1.022 = +102.2%; at tau=0.30 is (0.0758 - 0.2348)/0.2348 = -0.677 = -67.7%.
- Direction: the mesh jams in opposite directions for tau moves in either direction from the fold; this is a RIGIDITY argument, not an observable prediction.

Current observational data **cannot** measure tau directly. tau_fold is a substrate-internal spectral-geometry parameter. The alternative-state analysis tests whether the framework has internal freedom at the fold — it does not — but it does not produce an observational falsifier beyond the already-closed sin^2(theta_W) and Γ5 blue-tilt at transit. The workshop correctly labels this as an "alternative machine-state analysis" rather than an observable prediction; I agree with that framing.

### II.4 EVOI ranking of the five-test discriminator plane

**Result**: of the 5 discriminators, **only 1 is CMB-S4-imminent (alpha_s)**; **1 is mis-scaled (n_T)**; **3 are long-horizon (ALP shape, M_KK, frequency comb)**. **Classification: NON-PHONONIC methodology.**

Reach-date ranking (nominal projections):
| # | Discriminator | Framework prediction | Projected instrument sensitivity | Reach date | SNR @ reach | EVOI class |
|:--|:--------------|:---------------------|:---------------------------------|:-----------|:------------|:-----------|
| 1 | alpha_s = n_s^2 - 1 | -0.0690 | sigma(alpha_s) ~ 2e-3 at CMB-S4 | ~2030 (CMB-S4) | 34.0 | **IMMINENT-DECISIVE** |
| 1a | same | -0.0690 | sigma(alpha_s) ~ 2.5e-3 at SO DR1 | ~2029 (Simons) | 27.2 | **IMMINENT-DECISIVE** |
| 2 | n_T (transit) = +0.468 | SCALE MISMATCH | n_T(k_CMB) = -r/8 = -0.003 | — | N/A | **WITHDRAW from CMB gate** |
| 3 | ALP discrete vs log-flat | 7-feature Γ6 comb | DM-ALP surveys incomplete | ~2035 | binary | LONG-HORIZON |
| 4 | Frequency comb in GW-BG | 7 features at specific ratios | LISA/SKA at 10^-10 sensitivity | ~2035 | binary | LONG-HORIZON |
| 5 | M_KK ~ 10^17 GeV | proton decay rate ~1/M_KK^4 | Hyper-K at 10^35 yr | ~2045 | ~1 | VERY-LONG |

EVOI ordering (priority for carrying forward):
1. **alpha_s** (reach 2029-2030, 27-34 sigma) — the single observationally-decisive test.
2. **ALP spectrum shape** (reach 2035, binary) — distinguishes framework from K1 explicitly.
3. **Frequency comb in GW-BG** (reach 2035, binary) — distinguishes framework from K1 and K2.
4. **M_KK scale via proton decay** (reach 2045, ~1-sigma in 20 yr of data) — weak, long-horizon.
5. **n_T at CMB** — WITHDRAW from gate list due to scale mismatch; r(CMB) = 0.024 stands as separate gate.

The workshop's "5-test joint discrimination plane" is observationally more like a **2-test plane** (alpha_s now, alpha_s at CMB-S4) plus three long-horizon binaries. That is still structurally valuable but the workshop's framing overstates imminence.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| alpha_s = n_s^2 - 1 vs Planck 2018 | **9.622-sigma tension NOW** | 9.622 |
| alpha_s vs CMB-S4 projected slow-roll baseline | **34.0-sigma separation at ~2030** | 33.984 |
| alpha_s vs SO DR1 (earlier reach) | **27.2-sigma separation at ~2029** | 27.2 |
| n_T at CMB-S4 (transit-scale claim) | **SCALE MISMATCH, withdraw** | n/a |
| Γ1' alternative-tau deviation tau=0.10 | **+102.2% (Python-verified)** | +1.022 |
| Γ1' alternative-tau deviation tau=0.30 | **-67.7% (Python-verified)** | -0.677 |
| S84-GEAR-MASTER-CANDIDATE | **PRE-REGISTERED per workshop R3** | pending S84 |
| S84-DYNAMICS-UNIQUENESS-GATE | **PRE-REGISTERED per workshop R2** | pending S84 |

Gate verdicts from the workshop R3 closure are authoritative; this review does not re-adjudicate them. The verdicts above are the subset I verified numerically in this review.

---

## IV. Structural Implications

### IV.1 The alpha_s = n_s^2 - 1 gate is the dominant observational priority regardless of gear-machine framing

Independent of the gear-machine narrative, alpha_s = n_s^2 - 1 is a pre-existing structural identity (S50 T15, permanent-registry status) with a 9.62-sigma present-tension against Planck 2018. The workshop's contribution is NOT the identity itself but its deployment as a CMB-S4 discriminator against both K1 (Type IIB flux) and K2 (heterotic E_8 × E_8 on CY3), which the workshop shows require slow-roll |alpha_s| ~ 1e-3. That deployment is observationally productive: at CMB-S4 precision, the identity forces a 34-sigma cross-test that cannot be accommodated by standard slow-roll inflation from any string-landscape construction the workshop considered.

**Framework-scoped caveat**: the 9.62-sigma tension cuts BOTH ways. If the framework commits to alpha_s = -0.069 NOW (at Planck's n_s = 0.9649), it is already in 9-sigma tension with Planck's direct alpha_s measurement. CMB-S4 will not merely improve the test — it will potentially CLOSE the identity in either direction (pass if central-alpha shifts toward -0.069, fail if it stays at -0.005 with tighter error bars). This means the workshop's framing of "34-sigma decisive at 2030" should be more precisely stated as: "CMB-S4 will decide whether the identity is a property of the universe or a property of the framework's slow-roll extrapolation."

### IV.2 Tesla's biographical gear-wall framing: productive but needs observational translation

Tesla's "walk up to the wall" visualization is a productive heuristic for **structural** audiences but requires deliberate translation when communicating to observational physicists. The gear-wall language effectively communicates "rank-6 machine driving 53 identities" in a way that numerical arguments do not. But the actual observational content — which is what Planck, DESI, CMB-S4, LiteBIRD, and LISA can test — lives in a smaller subset of the wall: the 4-5 predictions with measurable observables.

For observational physicists, I recommend the following translation:
- **Gear-mesh ↔ structural identity** (T15, CC-5, §VII.K-META registry entries — these ARE the machine's teeth).
- **Master gear ↔ rank-reducer** (the three-input composite MG-0, MG-1, MG-2 reduces 53 identities to a 3-parameter space).
- **Cubic-BC closure ↔ sin^2(theta_W) prediction** (already CLOSED at 0.064-sigma from Planck, S83 W3-G47 PASS).
- **Jensen-curvature ↔ transit-scale n_T blue** (structural but NOT CMB-observable per S66 scale-transfer).
- **alpha_s = n_s^2 - 1 ↔ the single imminent-era observational discriminator** (34-sigma at CMB-S4).

This translation de-emphasizes the gear metaphor and highlights the observational content. Both modes have value — Tesla's for internal consistency reasoning, mine for external observational engagement — but the workshop's synthesis mixes them and in places overclaims reach.

### IV.3 "Corner-with-extensions" meta-concept and EVOI implication for S84

The workshop converges on meta-concept type (b') — framework is a **corner of the landscape's rep-theory output cone, with extensions into directions the landscape does not cover**. Observationally, this implies:

- **Rep-theory extensions** (A_F singleton algebra layer) are structurally framework-specific but observationally indistinguishable from heterotic-CY3 at the output layer (SM gauge group, 3 generations, 16 fermion reps). These predictions are **validation gates**, not discrimination gates — they confirm the framework is consistent with the SM, but do not distinguish it from a string-landscape competitor that also reaches the SM output.
- **Dynamics extensions** (τ_fold, Jensen curvature, BCS-on-Jensen comb, 4-speed hierarchy) are framework-specific AT BOTH the structural and observational layer IF the discriminators have observationally-accessible signatures. The workshop's 5-discriminator plane claims 5 such signatures; my review reduces this to **1 imminent (alpha_s) + 2 long-horizon binaries (ALP shape, GW comb) + 1 very-long (M_KK via proton decay) + 1 mis-scaled (n_T)**.

EVOI implication for the S84 plan: the highest-priority carry-forwards are (a) formalizing alpha_s = n_s^2 - 1 as a pre-registered CMB-S4 gate with rigorous scheme-independence proof, (b) quantifying Simons Observatory DR1 sensitivity at projected 27-sigma, and (c) establishing the 5-discriminator plane's actual reach-date sequence. Everything else in the gear-machine workshop is structural synthesis, not new observational content.

---

## V. Carry-Forward Computations

### V.1 alpha_s scheme-independence proof and CMB-S4 pre-registration

- **What**: prove that the identity alpha_s = n_s^2 - 1 (T15, S50 permanent) is scheme-independent across {zeta, Zubarev, SDW, dim-reg, lattice-BR}, so that its deployment as a CMB-S4 discriminator does not inherit a scheme-dependent span. Resolve the S82 W3-9 "scheme identity for certain slow-roll functionals" comment by either proving scheme-independence or quantifying the scheme-dependent range of alpha_s predictions across the 5-regulator family (R-protection check from Γ2' MG-0).
- **Inputs**: S50 T15 derivation chain, S82 W3-9 scheme-identity comment (s82_w3_9_as_adjacent_obs.py), S71 ALPHA-S-BAYESIAN-SHADOW memory (Pantheon+ 17.7%, spectral zeta 10.2%), R-protection/NOT-R-protection taxonomy from §VII.K-META.
- **Gate**: PASS if span(alpha_s) across 5-regulator family is R-protected (< 1.5-ratio) and T15 is confirmed scheme-invariant; INFO if alpha_s varies by 10-50% across schemes (R-weak but bounded); FAIL if alpha_s varies > 2x across schemes (loses identity-status under scheme choice). If PASS, pre-register alpha_s = -0.0690 ± 0.0005 as the canonical CMB-S4 gate.
- **Effort**: 4-6 computations, one workshop, 1-2 session weeks.

### V.2 Simons Observatory DR1 pre-registration (alpha_s 27-sigma @ 2029)

- **What**: formalize a pre-registered gate for alpha_s measurement at Simons Observatory DR1 (expected ~2029) at projected sigma(alpha_s) ~ 2.5e-3 baseline. Quantify the framework's position relative to SO central-value projection and to slow-roll landscape baseline. Identify bibliographic sensitivity forecast (SO Collaboration paper, baseline vs. goals) as the authoritative source.
- **Inputs**: alpha_s_framework = -0.068968 (Python-verified for n_s = 0.9649), SO Collaboration sensitivity forecast (2019+), slow-roll baseline α_s ~ -0.001, current Planck 2018 α_s = -0.0045 ± 0.0067.
- **Gate**: PASS if framework predicts α_s with SO-DR1 compatibility region overlap > 95%; INFO if overlap 50-95%; FAIL if overlap < 50%. Decisive at ~2029 (earlier than CMB-S4).
- **Effort**: 1-2 computations (literature search + forecast tabulation), one workshop session.

### V.3 WITHDRAW n_T from 5-discriminator plane, replace with r(CMB)

- **What**: update the 5-discriminator table to remove the "n_T blue @ +0.468" axis, which is a transit-scale substrate prediction NOT accessible at CMB scale per S66 TENSOR-TRANSFER-66 FAIL. Replace with r(CMB) = 0.024 at 24.2-sigma LiteBIRD (S68 LITEB-R-FORECAST-68) as the tensor-sector discriminator. Document the scale-transfer explicitly in the gate so future observational-priority reviews do not re-import the transit-scale claim.
- **Inputs**: S66 TENSOR-TRANSFER-66 memory (n_T(k_CMB) = -3.02e-3), S68 LITEB-R-FORECAST-68 memory (r(CMB) = 0.024 at 24.2-sigma LiteBIRD), S65 NT-BLUE-65 memory (transit scale n_T = +0.468, NOT CMB-transferable).
- **Gate**: INFO gate documenting the scale-transfer, not a PASS/FAIL computation.
- **Effort**: 1 computation (documentation), 1 session-hour.

### V.4 Observational reach-date table for 5 discriminators

- **What**: construct a pre-registered reach-date table for all 5 workshop-named discriminators with: (a) nominal instrument, (b) projected sensitivity at reach date, (c) framework prediction, (d) slow-roll landscape baseline, (e) projected SNR at reach date. Include Simons Observatory, CMB-S4, LiteBIRD, LISA, SKA, Hyper-Kamiokande, CTA, DM-ALP-surveys. Tabulate sigma(alpha_s), sigma(f_NL), sigma(n_T|r), Omega_GW sensitivity, proton-decay exclusion, ALP mass-spectrum coverage.
- **Inputs**: SO-Collab forecast, CMB-S4 Science Book 2016+, LiteBIRD 2020+ forecast, LISA science case, SKA-science-case, Hyper-K science reach, ADMX/CAST/HAYSTAC ALP exclusions.
- **Gate**: INFO gate; outputs a living table for S84+ carry-forward.
- **Effort**: 3-5 computations (literature + forecast compilation), one workshop.

### V.5 Scheme-dependence check for Γ1' cubic-BC closure

- **What**: verify that the cubic-BC closure sin^2(mu_BC) = 3/(3 + exp(12*tau_fold)) = 0.234803 is scheme-independent across the 5-regulator family. Related to Tesla's CF-4 (M_H_framework independent-pinning) and to Γ2' MG-0 R-protection. The 0.134% residual must not be a scheme artefact — if it is, the claim "mesh closes to 0.134%" becomes a scheme-specific claim rather than a scheme-invariant one.
- **Inputs**: canonical_constants tau_fold, Γ1' cubic-BC identity, §VII.K-META R-protection/NOT-R-protection taxonomy, S83 W3-G47 PASS (sin^2 theta_W at 0.064-sigma).
- **Gate**: PASS if cubic-BC residual < 0.3% across all 5 schemes; INFO if residual 0.3-1% in some schemes; FAIL if residual > 1% in any scheme.
- **Effort**: 2-3 computations, 1 session-day.

### V.6 Cross-validation of alpha_s 9.62-sigma tension against systematic sources

- **What**: quantify the 9.62-sigma Planck-vs-framework tension on alpha_s against Planck's own systematic treatments (TT-only, TT,TE,EE combined, low-ell inclusion, lensing inclusion, systematic-marginalized alpha_s). Planck 2018 Inflation paper reports alpha_s = -0.0045 ± 0.0067 (TT,TE,EE+lowE+lensing); other combinations may differ. If the tension survives all Planck systematic variants, it is structural; if one variant reduces the tension below 3-sigma, the identity is vulnerable to systematic choice.
- **Inputs**: Planck 2018 Inflation paper (Akrami et al. 2020) alpha_s estimates across systematic choices, framework alpha_s = -0.068968.
- **Gate**: PASS-ROBUST if all Planck systematic variants show > 5-sigma framework-identity tension; PASS-CONDITIONAL if most variants show > 5-sigma but one shows < 3-sigma; FAIL if any systematic choice shows < 2-sigma.
- **Effort**: 2-3 computations (Planck paper systematic combination), 1 session-week.

### V.7 Observational-priority workshop on gear-machine translation

- **What**: two-round workshop (Mack + one senior-observer agent) to translate the workshop's 5-discriminator plane into an observational-language summary, retire the n_T-at-CMB claim, formalize the corner-with-extensions label for observational physicists. Focus: rewrite Tesla's biographical gear-wall prose into testable-prediction language WITHOUT losing the structural content.
- **Inputs**: full workshop doc (s83-gear-machine-thought-experiment.md), S66/S68 tensor-transfer memory, this synthesis.
- **Gate**: INFO gate; outputs a consolidated observational-priority table for S84.
- **Effort**: one 2-round workshop (4 turns), 1-2 session-days.

### V.8 Pre-register the `SO-ALPHA-S-29` early-reach gate for 2029

- **What**: separate from the CMB-S4-2030 gate, pre-register a Simons Observatory DR1 gate (**SO-ALPHA-S-29**) with: (a) expected reach date 2029, (b) sigma(alpha_s) baseline ~2.5e-3, (c) framework prediction alpha_s = -0.0690 (Python-verified for n_s = 0.9649), (d) decision rules for PASS/TENSION/FAIL. This gate fires BEFORE CMB-S4 and should be the first external test of the T15 identity.
- **Inputs**: alpha_s_framework = -0.068968 (Python-verified), SO-Collab 2019 baseline forecast, slow-roll baseline.
- **Gate**: PRE-REGISTERED; fires at SO DR1. Decision rule: PASS if measured alpha_s ∈ [-0.090, -0.050]; TENSION if measured alpha_s ∈ [-0.050, -0.010]; FAIL if measured alpha_s > -0.010.
- **Effort**: 1 computation (pre-registration document), 1 session-hour.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | alpha_s = n_s^2 - 1 = -0.0690 from T15 permanent identity | GEOMETRIC | **9.62-sigma Planck tension NOW; 34-sigma CMB-S4 at 2030; 27-sigma SO DR1 at 2029** (all Python-verified) | Single observationally-decisive test in the 5-discriminator plane; already-tension, not future-tension |
| 2 | n_T blue at +0.468 at transit | GEOMETRIC structural, NON-OBSERVATIONAL at CMB | **SCALE MISMATCH** — n_T(k_CMB) = -3.02e-3 per S66 TENSOR-TRANSFER-66 FAIL | Workshop's n_T axis should be WITHDRAWN from CMB-S4 gate; replace with r(CMB)=0.024 LiteBIRD at 24.2-sigma (S68 LITEB-R-FORECAST-68) |
| 3 | Alternative-state analysis tau ∈ {0.10, 0.30}: Γ1' jams +102.2%/-67.7% (Python-verified) | GEOMETRIC | **Internal-consistency test, not observational** | Confirms mesh-rigidity but produces no new observable falsifier |
| 4 | Tesla's gear-wall heuristic | Pedagogical | **Productive for structural audiences, mis-leading for observational ones** | Needs deliberate translation (gear = structural identity, master = rank-reducer) when engaging observational physicists |
| 5 | "Corner-with-extensions" meta-concept | Meta | **Observationally testable only in dynamics extensions (α_s, Γ6, Γ7), not rep-theory extensions** | EVOI priority: rep-theory gates are validation; dynamics gates are discrimination |
| 6 | 5-test joint discriminator plane | Observational | **1 imminent (alpha_s), 1 mis-scaled (n_T), 3 long-horizon (ALP shape, GW-comb, M_KK)** | Effectively reduces to 1 primary + 2 supporting binaries for near-term; workshop overstates imminence |
| 7 | S84-GEAR-MASTER-CANDIDATE pre-registration | Gate | **AUTHORITATIVE per workshop R3** | Feeds CF-1 (scheme-independence of alpha_s identity) |

---

**Review summary**: the workshop's decisive observational contribution is a single quantitative discriminator (alpha_s = n_s^2 - 1 = -0.069), already at 9.62-sigma tension with Planck and decisive at 27-34 sigma within 3-4 years. The other four named discriminators reduce to 1 scale-mismatched, 2 long-horizon binaries, and 1 very-long-horizon weak. Tesla's gear-wall framing is structurally productive but observationally noisy; the 5-discriminator-plane claim should be pared to 1 decisive + 2 binary + retire n_T.
