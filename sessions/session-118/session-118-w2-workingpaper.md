# Session 118 Wave 2 — Lepton-PMNS Joint Admissibility (Q18b) (Results Working Paper)

**Session**: 118 | **Wave**: 2 | **Plan**: session-118-plan-w2.md | **Theme**: Does the lepton mixing+spectrum under-determination survive the JOINT NuFIT 5.2 NO 3σ box (R + the three PMNS angles) over the free real-texture family (U_eL charged-lepton left-rotation, V_DR neutrino-Dirac orientation) at fixed input spectra. Single COMPUTE gate, neutrino-detection-specialist.

## Gate Sections

### §W2-1. CF-S118-PMNS-JOINT-ADMISSIBILITY (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `CF-S118-PMNS-JOINT-ADMISSIBILITY`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (joint R + 3-PMNS-angle set-membership over the free real-texture family)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: At fixed charged-lepton masses, Dirac singular values {0,Y₂,Y₃}, and B-branch Majorana M_R, the joint NuFIT 5.2 NO 3σ box {R∈[17,66] ∧ sin²θ₁₂,θ₂₃,θ₁₃ in 3σ} is non-empty with positive admissible-volume measure over the free (U_eL, V_DR) orbit — the lepton under-determination survives the joint observational constraint. **EXPECTED verdict PASS** (dual prior 0.70 PASS / 0.15 FAIL / 0.15 INFO; the FAIL=empty-box and INFO=narrow-sliver tracks are genuinely pre-registered, NOT foreclosed — runtime must adjudicate all three).
**Plan reference**: `sessions/session-plan/session-118-plan-w2.md` §W2-1 (machinery pin map, 3-track verdict rubric, dual-prior track-discriminator, analytic non-emptiness substitution-chain witness, input-SHA ledger).

**Output Artifacts** (closure-verification checklist; content-presence by regex, never line/byte counts — all VERIFIED on disk):

- **Script** `computations/session-118/s118_pmns_joint_admissibility.py` (42878 bytes) — `grep -E "from canonical_constants import|print_verdict_payload"`:
  - L99 `from canonical_constants import (` ✓
  - L591 `def print_verdict_payload(...)` + L632/L723 calls ✓
- **Data** `computations/session-118/s118_pmns_joint_admissibility.npz` — present (18041 bytes, 64 keys; `composite=PASS`, `f_adm_free=6.85e-05`, `f_adm_hits=137`, `witness_lands=True`, `f_adm_shared=0.0`, `R_shared=113.564`) ✓
- **Plot** `computations/session-118/s118_pmns_joint_admissibility.png` — present (277824 bytes; 3 panels: R-distribution + reachable-interval, angle-box scatter with joint hits, verdict checklist) ✓
- **Verdict line** `computations/session-118/s118_gate_verdicts.txt` — 1 canonical line matching `^CF-S118-PMNS-JOINT-ADMISSIBILITY:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=85520aa6f833d71b8ec1e398973b5f0444a9afe2e50ef52217046de44a413962`), dual-SHA companion row present, **0 three-tuple rows** (correct — [VERIFY] set-membership gate, `schema_v2_3tuple_required=false`); SHA unique across the file (sig_5) ✓. Emitted via the race-safe `mcp__knowledge__emit_verdict` tool (6 rows: canonical + dual-SHA companion + 4 extra annotation rows), NOT an open-coded append.
- **This WP §W2-1** — carries `**Status**: COMPLETED` / `**Verdict**: PASS` / `**Output Artifacts**` / `**MCP Pre-Compute Audit**` ✓

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):

- `search_knowledge("PMNS joint admissibility lepton under-determination R angle NuFIT")` → returns the upstream `S116-W2-LEPTON-PMNS-TEXTURE` (FAIL, `mix_grp=0/4`) and `S115-LEPTON-PMNS-FORCED-TEXTURE` (FAIL) gates, plus the s116/s115 data provenance. **NOT PRE-CLOSED**: `CF-S118-PMNS-JOINT-ADMISSIBILITY` is a new JOINT (R+3-angle) set-membership gate over the FREE texture family — distinct from the S116 single-point forced-texture FAIL and the S117 piecewise R-channel / U_eL-flat / M_R-search verdicts (none of which scanned the joint box). The open_channel `CURRENT` (S116 housekeeping) confirms lepton-PMNS was left "RESONANT-CONDITIONAL".
- `get_constant("dm2_21_NuFit")` → 7.49e-5 eV² (NuFit-6.0 NO BF, S100b; SHA-pinned source). Used for the central-R anchor cross-check only.
- `get_constant("dm2_31_NuFit")` → 2.513e-3 eV² (NuFit-6.0 NO BF, S100b). Central-R anchor R_central = dm2_31/dm2_21 − 1 = **32.5514** (R_bare=31.576 sits 3.0% from it — both deep interior of [17,66]).
- Imported `tau_fold=0.19`, `dm2_21_NuFit`, `dm2_31_NuFit` from `canonical_constants.py` (`from canonical_constants import` — MANDATORY S34+); the NuFIT 5.2 NO 3σ box edges + best-fit angles are `# local` class-(B) anchors per the plan machinery_pin_map (NOT canonical imports), cross-confirmed bit-for-bit against the S116 npz stored bands (`S2T12_LO/HI`, etc.).
- Input SHAs verified against the plan ledger: s116 npz `4252d2cc…` == frozen plan pin ✓; `canonical_constants.py` `d884a2b5…` == plan-freeze snapshot ✓ (no PRE-REG-INC drift).

**Verdict**: **PASS** — the joint NuFIT 5.2 NO 3σ box {R∈[17,66] ∧ sin²θ₁₂,θ₂₃,θ₁₃ in 3σ} is **NON-EMPTY** over the free (U_eL, V_DR) real-texture orbit. The analytic non-emptiness witness lands all 4 slots (R_bare=31.576 ∈ band; the 3 angles at NuFIT band centers via U_eL=U_obs†, all edge-clear >5%), AND the MC free-family measure f_adm_free = **6.85×10⁻⁵** (137 hits / 2×10⁶ Haar draws) ≥ floor N_min/N_eval = 5×10⁻⁶. Dual-prior posterior re-allocation: **0.90 → track_A** (witness lands ∧ f_adm_free ≥ floor). The lepton mixing+spectrum under-determination **SURVIVES** the joint observational constraint.

**Results**:

**Verdict 4-tuple**: `(value=joint-admissibility=PASS; WITNESS_lands_all4=True; f_adm_free=6.85e-05 (137 hits/2e6, CV 0.35, floor 5e-06); f_R=1; f_angle=6.85e-05; CONTRAST_shared-epsLX_R=113.564_OUT_f_adm_shared=0; J=0_real-textures, scheme=joint-admissibility-MC-Haar-O3-free-texture, convention=RATIO-R-m3sq-over-m2sq-minus-1-m1zero-NO/PMNS-U_eL-dag-U_nuL/real-texture-J-excluded/NuFIT-5.2-NO-3sigma-joint-box-R+3angles, L_max=N/A)`. Dual-SHA: `audit_sha256=85520aa6f833d71b8ec1e398973b5f0444a9afe2e50ef52217046de44a413962` (over [script, canonical, pinmap]), `content_sha256=32f0e352f6f1b9a2673a77158ca30be385b36eb9e47ad41b427a48ba6e6d911d` (over [script]).

**3-track verdict rubric resolved → PASS**: witness lands all 4 slots (edge-clear) AND f_adm_free = 6.85×10⁻⁵ ≥ floor 5×10⁻⁶ ⇒ PASS (not the INFO thin-sliver track — f_adm_free is 13.7× the floor; not the FAIL empty-box track — witness lands and the MC is positive-measure). Dual prior posterior: **0.90 → track_A (PASS, under-determination survives)**.

**(1) ANALYTIC NON-EMPTINESS WITNESS — the PASS anchor** (deterministic; bare V_DR=I, U_eL=U_obs†):

| Slot | Value | NuFIT 5.2 NO 3σ box | In band | Edge-frac (≥0.05 clear) |
|:-----|:------|:--------------------|:-------:|:------------------------|
| R = m₃²/m₂²−1 | **31.5764** | [17, 66] | ✓ | 0.297 |
| sin²θ₁₂ | **0.30300** | [0.270, 0.341] | ✓ | 0.465 |
| sin²θ₂₃ | **0.57200** | [0.434, 0.610] | ✓ | 0.216 |
| sin²θ₁₃ | **0.022030** | [0.02029, 0.02391] | ✓ | 0.481 |

All 4 slots land, all interior (min edge-frac 0.216 ≫ 0.05) ⇒ the joint region J is NON-EMPTY **by explicit construction**. The bare light spectrum is m_light = (0, 21.304, 121.596) in M_KK² units; m₁/m₃ = 0.00 EXACT (rank-2, Y₁=0). The angles land at the NuFIT band CENTERS to machine precision (U_PMNS = U_obs since U_nuL=I at V_DR=I). This re-derives S116 W2 STEP 3b `obs_pmns_reachable=True` (3/3 angle slots), now extended to the JOINT 4-slot box.

**(2) MC ADMISSIBLE-VOLUME MEASURE** (free U_eL/V_DR; N_eval = 2×10⁶ Haar-O(3) draws, 10 seed batches 118+b):
- **f_adm_free = 6.85×10⁻⁵** (137 joint-box hits) ± seed-CV **0.35** (Poisson noise from ~14 hits/batch). ≥ floor N_min/N_eval = 10/2e6 = 5×10⁻⁶ ✓ (13.7× the floor — a robust positive-measure confirmation, not a sliver).
- **f_R = 1.000** — R(V_DR) ∈ [17,66] for ALL Haar draws; the reachable R-interval is [27.25, 51.01], a sub-interval **entirely inside** [17,66]. **Structural finding**: the near-degenerate B-branch M_R (spread 16.5%) confines the light-mass ratio m₃/m₂ near Y₃²/Y₂² regardless of V_DR orientation ⇒ the whole free V_DR orbit is R-admissible (the S96 R<17 shortfall is avoided at the bowtie shape).
- **f_angle = 6.85×10⁻⁵** — fraction of Haar U_eL placing the 3 angles in 3σ (driven by the narrow sin²θ₁₃ slice, width 0.0036).
- **Factorization confirmed**: f_R·f_angle = 6.85×10⁻⁵ = f_adm_free EXACT. The joint event factorizes because R⊥angles (disjoint draws: R depends only on V_DR; U_PMNS = U_eL†U_nuL is Haar-distributed for Haar U_eL ⇒ the angle-box probability is V_DR-independent). The admissible orbit is small but strictly positive-measure.

**(3) SHARED-ε_LX CONTRAST — the tension witness** (M_ν locked to the S116 single-parameter texture; N_eval_shared = 2×10⁵):
- Shared-ε_LX reconstruction is **bit-exact**: max|M_ν,rebuilt − M_ν,S116| = 0.0 (w₂₃ = ε₂₃·Y₃ = 0.23546·11.928 = 2.80851).
- **R_shared = 113.564** ∉ [17,66] — the angle-fixing ε₂₃ drives R OUT of band (matches S117 2-2 R_eps23=113.564 exactly).
- **f_adm_shared = 0.0** (near-empty): even though U_eL still reaches the angles (f_angle_shared = 7.5×10⁻⁵), the locked R-overshoot makes the JOINT box empty. This is the tension witness: IF the framework forced the shared-ε_LX texture (removing the V_DR freedom by tying ε₂₃ to the charged sector), the joint box would be EMPTY. The free-texture V_DR orientation is precisely what relieves the R-overshoot.

**(4) Cross-checks** (all PASS):
- R closed-form (m₃²−m₂²)/(m₂²−m₁²) = 31.5764 vs m₃²/m₂²−1 = 31.5764, diff = 3.55×10⁻¹⁵ < 1×10⁻⁹ ✓
- m₁=0 rank-2: |m₁/m₃| = 0.00 < 1×10⁻⁹ ✓
- PMNS unitarity |UᵀU − I|_fro = 2.55×10⁻¹⁶ < 1×10⁻¹⁰ ✓
- NuFIT central-R anchor dm2_31/dm2_21 − 1 = 32.5514; R_bare = 31.5764 sits 3.0% from it — both deep interior of [17,66].
- Corroboration grid (19³ = 6859 structured U_eL Euler at the bare ν spectrum): f_angle_grid = 0, nearest approach 2.03 box-half-widths. **The coarse 19-pt grid under-resolves the 0.0036-wide sin²θ₁₃ box** — its null is a resolution artifact, NOT a reachability failure. The authoritative reachability mirror is the ANALYTIC WITNESS (§(1), lands True == S116 STEP 3b); the MC (§(2), 137 hits) confirms the positive measure.

**Substitution chain (substituted numbers)** — the factorization is the substrate content: an overall left-rotation M_ν → V M_ν Vᵀ preserves singular values ⇒ **R is U_eL-INVARIANT**, so R-band membership lives on V_DR while the 3 angles are reachable via the freely-absorbing U_eL. R≥17 ⇔ m₃/m₂ ≥ √18 = 4.2426; at the bare bowtie shape m₃/m₂ = 5.706 > 4.2426 ⇒ R_bare = 31.576 interior. (U_eL = U_obs† reproduces the charged-lepton masses for any O(3), S117 2-5 trace-cyclicity flat direction ⇒ U_PMNS = U_obs reachable.)

**HONEST CAVEAT (load-bearing; S100a-MD-NORMALIZATION INFO, PERMANENT)**: the D_K bottom-triple → Y_i map is NON-UNIQUE (MAP-A vs MAP-B), so the Dirac-Yukawa ratio Y₃/Y₂ — hence R_bare — is **oscillation-anchored**. R_bare ∈ band is a CONSISTENCY of the spectrum channel with NuFIT (vs central-R 32.551), **NOT a zero-free-parameter prediction**. The substrate-FIRST content is the seesaw STRUCTURE + the bowtie M_R shape + the factorization (R is U_eL-invariant) + the flatness of the U_eL/V_DR orbit (S117 2-5). The verdict is a statement about the SHAPE of the compatible solution region, not a derived value. **CP/Jarlskog J EXCLUDED**: real O(3) textures force δ_CP ∈ {0,π} ⇒ J=0 (the framework's standing prediction); the CP-sector under-determination is the separate §VII.BL / S117-W3-3 question, NOT this gate.

**Substrate-first assessment (PARTICLE)**: D_K eigenvalues → seesaw composite M_ν = M_D M_R⁻¹ M_Dᵀ (Dirac singular values {0,Y₂,Y₃} and the B-branch fold Majorana M_R, both internal to the spectrum per S100a) → light spectrum {0, m₂, m₃} → the oscillation ratio R and, via U_PMNS = U_eL†U_nuL, the three mixing angles → the joint NuFIT 5.2 NO 3σ box (the laboratory-IN measurement). The substrate **IS** the free-texture orbit; NuFIT is the container-IN observable box. This gate measures whether the intrinsic freedom (the spectral action is FLAT over U_eL and V_DR by trace cyclicity, S117 2-5) is observationally COMPATIBLE — and it is: the joint box is non-empty over a positive-measure free-texture orbit, so the framework's lepton mixing+spectrum freedom is COMPATIBLE with NuFIT but NOT predictive (the angles + R are reachable, not pinned to a unique value). This confirms atlas-08 Q18b "mixing under-determined both sectors" extends to the JOINT (R+angle) box; the seed-selection that WOULD pin a value is the separate non-pinnable §VII.BL standing direction, untouched here. The shared-ε_LX contrast (f_adm_shared=0) shows the V_DR freedom — not the Majorana scale — is what makes the joint box non-empty.

## Wave 2 Synthesis (team-lead)

**Single gate, PASS.** `CF-S118-PMNS-JOINT-ADMISSIBILITY` resolves the JOINT (R + 3-angle) admissibility question that the S117 piecewise results (2-2 R-channel / 2-3 M_R-search / 2-5 U_eL-flat) never reached: the joint NuFIT 5.2 NO 3σ box {R∈[17,66] ∧ sin²θ₁₂,θ₂₃,θ₁₃ in 3σ} is **NON-EMPTY** over the free (U_eL, V_DR) real-texture orbit. Analytic witness lands all 4 slots edge-clear (R_bare=31.576; angles at NuFIT centers via U_eL=U_obs†); MC f_adm_free=6.85e-5 (137/2e6, 13.7× the floor, CV 0.35); f_R=1.0 structural.

**Solution-space (structural vs numerical, per `output-standards.md`):**
- **(b) Structural** — the lepton mixing+spectrum under-determination is now confirmed observationally **COMPATIBLE** with NuFIT but **NOT predictive**: the angles + R are reachable over a positive-measure free-texture orbit, not pinned to a unique value. The structural driver is the factorization (R is U_eL-INVARIANT, so R-band lives on V_DR while the 3 angles are freely absorbed by U_eL) — `f_R·f_angle = f_adm_free` EXACT. The shared-ε_LX contrast is EMPTY (R=113.564 OUT) ⇒ the **V_DR freedom**, not the Majorana scale, is what makes the box non-empty. J=0 (real textures) is the standing prediction, untouched.
- **(a) Numerical** — f_R=1.0 confines R to the sub-interval [27.25, 51.01] ⊂ [17,66] for the whole V_DR orbit (near-degenerate B-branch M_R, 16.5% spread); NuFIT central-R anchor 32.551 vs R_bare 31.576 (3.0% interior).
- **Honest caveat (load-bearing)**: R_bare is **oscillation-anchored** (S100a MAP-A/MAP-B non-unique) — R∈band is a CONSISTENCY of the spectrum channel with NuFIT, NOT a zero-free-parameter prediction. The verdict is a statement about the SHAPE of the compatible solution region.

**Decision-point routing (plan Wave 2→3 table):** PASS → atlas-08 Q18b freshness fold (under-determination survives, STRENGTHENED, no status downgrade). The verdict + f_adm_free feed the §VII.BL seed-selection standing direction (which this gate FEEDS but does NOT resolve). No carry-forwards.

**Capstone-hygiene 5-Q gate:** Q1 (a(t)/Friedmann) NO · Q2 (§7 falsifier row) NO (no §7 anchor change — J=0 prediction unchanged) · Q3 (PROVEN/CONDITIONAL/BROKEN/INFO status change) NO (a PASS that STRENGTHENS the existing "under-determined" reading is not a status change) · Q4 (prose claim) NO · Q5 (citation) NO. → No capstone reconciliation owed (the plan routes capstone-hygiene only on a FAIL/INFO; this is a strengthening PASS).

**Effected In-Session (NON-MATH):**
- [x] **atlas-08 Q18b** — both occurrences folded to the W2 PASS (under-determination survives the joint box, f_adm_free=6.85e-5, f_R=1.0 structural; compatible-not-predictive; §VII.BL stays the standing direction): LIVE DASHBOARD row (`atlas-08-open-questions.md:18`) + detailed Q18b STATUS/NEXT entry (`:141-144`, the S115-era NEXT refreshed). Orchestrator-direct (atlas freshness in place).
- Self-audit: `grep -c '^- \[ \]'` over this block = 0.

## Carry-Forward Computations

No carry-forwards: all wave outcomes closed in-session. The W2 PASS confirms the under-determination survives the joint box; the seed-selection that WOULD pin a value is the non-pinnable §VII.BL spectral-action standing direction (a standing gap, leverage ≠ tractability — NOT a pre-registrable compute gate this session).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-29 | Lepton mixing+spectrum under-determination (Q18b) | piecewise S117 results (R-channel / M_R-search / U_eL-flat); JOINT (R+3-angle) box untested | under-determination CONFIRMED survives the joint NuFIT 3σ box (non-empty, f_adm_free=6.85e-5, f_R=1.0 structural); COMPATIBLE-not-predictive | `CF-S118-PMNS-JOINT-ADMISSIBILITY` PASS |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict (audit_sha256) |
|:-----|:-------|:------------|:------------|:-----------------------|
| CF-S118-PMNS-JOINT-ADMISSIBILITY | `computations/session-118/s118_pmns_joint_admissibility.py` | `s118_pmns_joint_admissibility.npz` | `s118_pmns_joint_admissibility.png` | `85520aa6…a413962` PASS ([VERIFY], no 3-tuple) |
