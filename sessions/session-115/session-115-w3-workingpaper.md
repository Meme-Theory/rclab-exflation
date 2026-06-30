# Session 115 Wave 3 — Confirmatory due-diligence + two OPTIONAL low-EVOI magnitude-refinement objects (Results Working Paper)

**Session**: 115 | **Wave**: 3 | **Plan**: session-115-plan-w3.md | **Theme**: EVOI-last wave — mechanical confirmatory due-diligence (W3-1) plus two OPTIONAL forward objects lifted from S114 closed corridors (W3-2 A_s selector, W3-3 two-sided island QES). Three independent COMPUTE gates, no internal dependencies.

## Gate Sections

### §W3-1. S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE**
**Agent**: `transit-dynamics-theorist` (gen-physicist acceptable fallback per context item 4)
**Hypothesis**: Routing candidate (iii) at the LOCATED van Hove crossing `q=0.191038` (instead of canonical `19/100`) with the bit-equality guard relaxed keeps the GRADED selector selecting (iii) and `dev[iii]^cross ≤ 0.01` (expected 0.00682), and `CF(0.191038/0.112)` carries a partial quotient ≥ 10 within 8 terms — so the `S0 = 95/56` exact identity has NO analog at the located value, confirming and structurally unable to flip the S114 W-1 (iii) verdict (CONFIRMS-CANNOT-FLIP; a non-PASS signals a script/convention bug, not a physics reversal).
**Plan reference**: `sessions/session-plan/session-115-plan-w3.md` §W3-1 (machinery pin, thresholds, substitution chain, CONFIRMS-CANNOT-FLIP framing).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

All five `output_artifacts:` entries verified present on disk by content (never line/byte count):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/session-115/s115_s0_knob_cross_substitution_confirm.py` | `from canonical_constants import` ✓ ; `print_verdict_payload` ✓ |
| data | `computations/session-115/s115_s0_knob_cross_substitution_confirm.npz` | present (18,964 B), float64 results dict |
| plot | `computations/session-115/s115_s0_knob_cross_substitution_confirm.png` | present (two-panel: dev-bar + 3-leg summary) |
| verdict_line | `computations/session-115/s115_gate_verdicts.txt` | `^S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM:.* audit_sha256=[a-f0-9]{64}` ✓ ; dual-SHA companion row ✓ ; NO 3-tuple ([VERIFY]) ✓ |
| wp_section | this section | `**Status**:.*COMPLETED` ✓ ; `**Verdict**:.*(PASS\|FAIL\|INFO)` ✓ ; `**Output Artifacts**` ✓ ; `**MCP Pre-Compute Audit**` ✓ |

Grep confirmations (line numbers as on disk):
```
$ grep -nE 'from canonical_constants import|print_verdict_payload' s115_s0_knob_cross_substitution_confirm.py
83:from canonical_constants import *  # noqa: F401,F403,E402
84:from canonical_constants import (  # noqa: E402  explicit (used below)
534:def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
623:    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)
$ grep -nE '^S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM:.* audit_sha256=[a-f0-9]{64}' s115_gate_verdicts.txt
16:S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM: PASS -- value='...' ... audit_sha256=c4943ae5...aef08a0 content_sha256=04fa37d2...56a9ffe schema_version=S84+
17:# audit_sha256_short=c4943ae5f8873c9f content_sha256_short=04fa37d299e6385f # S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM dual-SHA companion row
```
3-tuple count for this gate in the verdict file: **0** (correct — [VERIFY] trigger emits no SIGN/MAGNITUDE/REGIME row).

**MCP Pre-Compute Audit**:

Four `mcp__knowledge__*` queries executed before writing the script (NOT pre-closed — this is a confirmatory due-diligence re-run of an already-landed gate, so the result is intentionally a re-derivation, not a recompute of a closed mechanism):

| Query | Salient return |
|:------|:---------------|
| `get_constant('tau_cross_van_hove')` | `0.191038` (S114, source `S114-CF-S114-TAUFOLD-CUSP-CROSSING`; Superseded=False) — the LOCATED band-edge anticrossing |
| `get_constant('T_acoustic')` | `0.112` (= `14/125`, S42/S47 GGE acoustic temperature; canonical_constants.py L732; Superseded=False) |
| `get_constant('tau_fold')` | `0.19` (= `19/100`, S12/S42, gate `CONST-FREEZE-42`; Superseded=False) — the canonical flank |
| `trace_entity('S0-knob')` | gate `S101-W3-S0-KNOB`: `value='N_inside=1(selector);N_naive=2;knob=iii(...S0*T_ac=tau_fold);dev_iii=0.0013;legC=GRADED;...'` — confirms the S101 lineage (GRADED selector → (iii), the `95/56` identity). The equation hit flags the s101 bit-equality guard (line 240) — exactly the guard relaxed here to the substituted value. |

**Verdict**: **PASS** — CONFIRMS-CANNOT-FLIP. All three regulator-free legs hold; the S114 W-1 (iii) verdict is re-confirmed at the located crossing and shown structurally unable to flip. NO registry change (the gate confirms an already-landed verdict). `audit_sha256=c4943ae5f8873c9f5182c9460be8b4809d27d2848383e4b00e8407b84aef08a0`.

**Results**:

**Numbers (LEG A — dev-magnitude).** `S0_pred_iii^cross = q_cross / T_acoustic = 0.191038 / 0.112 = 95519/56000 = 1.70569643`. Against `S0_fit = 1.69415316` (cache-free core; W3-9 echo dev `0.00e+00`):
`dev[iii]^cross = |1.70569643 / 1.69415316 − 1| = 0.6814% ≤ 1.00% = PASS_BAND` → **LEG A PASS** (matches the plan's pre-registered `≈ 0.00682`). Candidate (i) (4/3 routed) gives `dev_i = 0.6539%` — STILL inside the naive 0.01 band (the 0.52% pin-proximity accident `(4/3)·0.9 ≈ 2π·τ_fold` persists, q-independent); candidate (ii) (δ/2) gives `dev_ii = 1.4430%` (outside). So the naive count is again degenerate (i + iii inside 0.01).

**GRADED selector (LEG B — class-invariance).** `legC_output_form = GRADED` (read from the W2-2 npz `s101_envelope_carrier_discriminate.npz`) → eligible class `graded-per-C2-quantum` → candidate (iii) is the SOLE member (eligibility: i=False, ii=False, iii=True). Robustness witnesses: graded residual max `6.66e-16` (clean < 1e-12), scalar residual max `0.892` (excluded > 1e-3). After the selector: `N_inside(selector) = 1`, selecting (iii). The selector reads a CLASS LABEL, INDEPENDENT of the numerical value of q, so re-routing q from `19/100` to `0.191038` does NOT change (iii)'s membership → **LEG B PASS**.

**Continued fraction (LEG C — exact-rational asymmetry).** Pure Euclidean CF on the EXACT rationals (in-script, cross-checked against Sage `continued_fraction`):
- LOCATED: `0.191038/0.112 = 191038/112000` reduces (gcd 2) to `95519/56000`; `CF(191038/112000) = [1, 1, 2, 2, 1, 1, 18, 44, 4]` — first partial quotient ≥ 10 is at **index 6, value 18** (within the first 8 terms) → **LEG C PASS**.
- CANONICAL contrast: `19/100 / 14/125 = 95/56`; `CF = [1, 1, 2, 3, 2, 2]`, max pq = 3 (all small) — the clean small-denominator identity `S0(canon)·T_acoustic = τ_fold` (exact: True).
- The large pq=18 means the located value has NO clean small-denominator convergent (it is "almost" `17/10` then jumps to denominator 56000); the `95/56` identity has **NO analog** at the located value.

**Sage cross-check** (authoritative arithmetic for LEG C, run before the script):
```
continued_fraction(191038/112000).quotients() = [1, 1, 2, 2, 1, 1, 18, 44, 4]   first pq≥10 @ idx 6 = 18
continued_fraction(95/56).quotients()         = [1, 1, 2, 3, 2, 2]               max pq = 3
located convergents (first 5)                 = 1, 2, 5/3, 12/7, 17/10
```

**Three-leg substitution chain (substituted numbers):**
- **Step 1-3**: `q_cross = tau_cross_van_hove = 0.191038`; `T_acoustic = 0.112 = 14/125`; `S0_fit = 1.694153`.
- **Step 4-6 (LEG A)**: `S0_pred_iii^cross = 0.191038/0.112 = 95519/56000 = 1.705696` ⇒ `dev = |1.705696/1.694153 − 1| = 0.006814 ≤ 0.01` ⇒ PASS.
- **Step 7 (LEG B)**: eligibility test `legC_output_form == 'GRADED'` → class `graded-per-C2-quantum` → (iii) sole member; reads a class label, NOT q ⇒ selector still selects (iii) ⇒ PASS.
- **Step 8 (LEG C)**: canonical `S0 = 19/100 / 14/125 = 95/56` (clean small-denom, identity `S0·T_ac = τ_fold`); located `CF(191038/112000) = [1,1,2,2,1,1,18,44,4]` carries a large pq (18) within 8 terms ⇒ no clean convergent ⇒ no analog ⇒ PASS.
- **Direction**: all three legs are regulator-free (set-membership + exact rational arithmetic); none depends on a dynamical / convention / regulator choice. **Conclusion**: the gate CONFIRMS the S114 W-1 (iii) verdict and is structurally unable to flip it — a non-PASS would have indicated a script/convention bug, not a physics reversal.

**4-tuple**: `(value=verdict_legs[A_dev=True,B_sel=True,C_cf=True];...;CONFIRMS-CANNOT-FLIP_W-1(iii), scheme=KNOB-DISCRIMINATION-3CAND-LEGC-ROUTED-CROSS-SUBSTITUTION, convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)`.

**Dual-SHA**: `audit_sha256 = c4943ae5f8873c9f5182c9460be8b4809d27d2848383e4b00e8407b84aef08a0` (over {script, canonical, pinmap}); `content_sha256 = 04fa37d299e6385ff8051b4e8971b0e150e405330d6ea43fd64d8f53756a9ffe` (over {script}). Input pins captured at runtime per the plan's `<computed-at-runtime>` declaration. Informational note: the s101-era literal W2-2 pin (`463f320…`) differs from the live W2-2 SHA — the static S101 artifact's bytes are unchanged; the s101 literal was an era-specific head-pin and is non-gating here (mirrors s101 line 369 "informational; mismatch flagged, not gating"). The gate's `audit_sha256` is correctly derived from the live runtime pin map.

**Substrate framing (PARTICLE).** The S0 scale knob fixes the absolute scale of the GRADED one-fiber freeze-frequency split `ω_g = q·C2(g)·M_KK` on the substrate's Peter-Weyl-decomposed D_K spectrum — q is the graded crossing offset read through the GGE acoustic temperature T_acoustic. The substrate IS the band-edge anticrossing where the monotone spectral-action flow S(τ) crosses the non-analytic van Hove threshold in ρ(λ;τ); the located crossing τ_cross=0.191038 is that threshold (the T3=(0,0)-MAX vs T5=(2,0)/(0,2)-MIN eigenvalue cross). Candidate (iii)'s selection is a statement about which substrate CLASS the knob inhabits — a structural fact, regulator-free, hence invariant under re-routing the offset from the canonical fold value to the located crossing. The gate confirms the substrate's own arithmetic (`S0 = τ_fold/T_acoustic = 95/56` exact) is a flank sub-choice within the substrate-pinned crossing window, not a tuned coincidence.

**Artifacts**: `computations/session-115/s115_s0_knob_cross_substitution_confirm.py` / `.npz` / `.png`.

---

### §W3-2. S115-AS-NEWAXIS-SELECTOR (transit-dynamics-theorist) — OPTIONAL (planner-discretion, EVOI-last)

**Status**: COMPLETED
**Gate ID**: `S115-AS-NEWAXIS-SELECTOR`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Disposition**: **OPTIONAL (planner-discretion, EVOI-last)** — NAMED forward object from a closed corridor (S114 W4-1); §EVOI.BF already prices the `A_s` magnitude as a permanent physical d.o.f. This gate WIDENS the no-selector evidence on a fresh axis-basis; it does NOT change the headline. User may elect to drop it at the Phase-3b checkpoint; RETAINED EVOI-ordered last rather than dropped.
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: A functional-determination principle outside `{impulse-quench, UNIFIED-AS-79, Parker-adiabatic}` — maximum-entropy/Jaynes selection on the post-transit occupation `n_k` (axis-1), OR Connes-distance-canonical normalization of the relic spectral functional (axis-2) — collapses the 1.2590-OOM cross-functional `A_s` spread to a single typed value (PASS, §EVOI.BF liability retired); OR no new-axis selector collapses it, widening FUNCTIONAL-PLURALISM-PERMANENT on the `{maxent, Connes}` axis-basis (FAIL). Verdict OPEN (prior 0.10 PASS / 0.90 FAIL); not pre-judged.
**Plan reference**: `sessions/session-plan/session-115-plan-w3.md` §W3-2 (maxent constrained-solve + Connes-distance spectral-triple machinery, 0.10-OOM collapse band, OPEN dual-prior).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **script** `computations/session-115/s115_as_newaxis_selector.py` (41,988 B) — `grep -nE "from canonical_constants import|print_verdict_payload"`:
  - L87 `from canonical_constants import *  # noqa: F401,F403  (A_s_FW, A_s_CMB, xi_KZ_FW)` ✓
  - L604 `def print_verdict_payload(verdict, value, audit_sha, content_sha,` ✓ (L796 call site)
- **data** `computations/session-115/s115_as_newaxis_selector.npz` (19,904 B) — present ✓
- **plot** `computations/session-115/s115_as_newaxis_selector.png` (113,751 B) — present ✓
- **verdict_line** `computations/session-115/s115_gate_verdicts.txt` — `grep -E "^S115-AS-NEWAXIS-SELECTOR:.* audit_sha256=[a-f0-9]{64}"`:
  - `S115-AS-NEWAXIS-SELECTOR: FAIL -- value='selection=COINCIDENCE-ONLY|...' ... audit_sha256=b07deb9ba49159b5…550059a content_sha256=ad4855b77e637012…34c5f9 schema_version=S84+` ✓
  - companion row: `# audit_sha256_short=b07deb9ba49159b5 content_sha256_short=ad4855b77e637012 # S115-AS-NEWAXIS-SELECTOR dual-SHA companion row` ✓
  - **3-tuple** ([SIGN]): `# sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID # S115-AS-NEWAXIS-SELECTOR 3-tuple annotation (schema-v2)` ✓
  - detail row: `# newaxis-detail: A_s_maxent=1.400596e-08 (OOM +0.8241); A_s_Connes=7.067612e-08 (OOM +1.5271); d_C_diam=0.217429; min_collapse_dist=0.6281 OOM vs band 0.1; maxent_2nd=none/connes_2nd=parker` ✓
- **wp_section** (this section) — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present ✓

**MCP Pre-Compute Audit**:

- `get_constant('A_s_FW')` → `1.5367059962762235e-08` (S111, `s111_cf_as3a_impulse_quench.npz`, gate S111-CF-AS3a, Superseded=False) — the impulse-quench FLOOR; consumed as the canonical comparison anchor.
- `trace_entity('A_s functional selection')` → **no trace** (the S114 prior is registered under the gate-ID, not this phrase).
- `search_knowledge('FUNCTIONAL-PLURALISM-PERMANENT A_s')` → returned A_s ledger equations across S68–S83 (no PRE-CLOSE of this gate); the new-axis question is genuinely un-evaluated.
- `search_knowledge('S114 W4-1 AS-FUNCTIONAL-SELECTION ...')` + `trace_entity('AS-FUNCTIONAL-SELECTION')` → the S114 prior gate `CF-S114-AS-FUNCTIONAL-SELECTION` (S114): `value='selection=PLURALISM|spread_OOM=1.259|struct_deriv=0|n_in_band=0|oom_impulse=0.86437/unified=0.196/parker=1.455'`, **FAIL**. This gate WIDENS that prior on the fresh `{maxent, Connes}` axis-basis. **NOT PRE-CLOSED** — the two new axes (maxent/Jaynes, Connes-distance) are outside the three functionals the S114 gate tested.

**Verdict**: **FAIL** (composite) — `sign=FAIL / magnitude=FAIL / regime=VALID`. SELECTION = **COINCIDENCE-ONLY**. Neither new axis collapses the 1.2590-OOM spread; **FUNCTIONAL-PLURALISM-PERMANENT is widened** on the `{maxent, Connes}` axis-basis. Dual-prior posterior → **0.95 Track B (PLURALISM-PERMANENT)** / 0.05 Track A. The §EVOI.BF "A_s magnitude = permanent physical d.o.f." headline STANDS, now on a broader axis-basis. The verdict was OPEN (prior 0.10 PASS / 0.90 FAIL) and not pre-judged; the maxent and Connes axes are FIXED physical principles, computed once, not tuned. **No `mack-cosmic-bridge` routing** (that is the PASS path; on FAIL the §EVOI.BF headline is unchanged, so no falsifier Row #12 / §EVOI.BF inventory-row update is owed).

**Results**:

**The existing spread (the 1.2590 OOM to collapse).** Three functional `A_s` literals vs Planck anchor `A_s^Planck = 2.1e-9` (`A_s_CMB`):

| Functional | `A_s` | OOM vs Planck |
|:--|:--|:--|
| impulse-quench (sudden) | `1.536706e-8` (= `A_s_FW`, S111-CF-AS3a) | **+0.86437** |
| UNIFIED-AS-79 (slow-roll) | `3.297762e-9` (S82) | **+0.19600** |
| Parker-adiabatic | `5.987138e-8` (inv-6 W2-2) | **+1.45500** |

`spread_existing = +1.45500 − 0.19600 = 1.25900 OOM` (Parker − UNIFIED). Matches the S114 W4-1 `spread_OOM=1.259` prior exactly.

**AXIS-1 — maximum-entropy / Jaynes occupation.** The GGE/Jaynes prediction: the maximum-entropy occupation `n_k^maxent = 1/(exp(λ_N + λ_E·ω_k) − 1)` (Bose form) with `(λ_N, λ_E)` the Lagrange multipliers enforcing the two substrate-fixed conserved moments read off the box-delta sudden spectrum `s100b_box_delta_bogoliubov.npz` (`ω_k = k`, massless out-dispersion, M_KK clock):
- `<N> = Σ|β_k|² = 2.081086e-5` (mean pair number)
- `<E> = Σ ω_k|β_k|² = 2.500575e-4` (total energy) ⇒ `<E>/<N> = 12.0157` (mean energy/pair, sets the maxent temperature)
- Lagrange solve (`scipy.optimize.fsolve`, `xtol=1e-10`): `λ_N = 14.885583`, `λ_E = 0.004312`; constraint residuals `(1.21e-18, 2.01e-16)` ⇒ **converged** (both constraints satisfied to machine ε).
- Pivot occupation `n_k^maxent(k_pivot=14.31) = 3.224592e-7`, ratio to raw `|β_k|²_pivot` = **1.0588** — the GGE redistributes only ~6% (the squeezed box-delta spectrum is near-flat: `|β|²` spans 3.04e-7→4.64e-7 over `k∈[1,50]`, so the maxent moment-matched occupation barely moves the pivot value).
- `A_s^maxent` (k̂=1/ξ_KZ-normalized, PRIMARY — matching the floor's own construction `A_s_FW = |β_k̂|²/(2π²)`) = **`1.400596e-8`**, **OOM +0.82409**. (pivot-norm cross-check `1.633597e-8`.)

**AXIS-2 — Connes-distance-canonical normalization.** The intrinsic NCG metric between the in-vacuum and out-vacuum states on the substrate spectral triple `(A_K, H_K, D_K)`. On the commutative diagonal sub-triple the Connes spectral distance `d_C(ω_p, ω_q) = sup_{‖[D,a]‖≤1} |ω_p(a)−ω_q(a)|` has the closed extremal value (DIAMETER) `d_C = 1/(λ_max − λ_min)` — the unique substrate-intrinsic dimensionless distance scale on the triple. From the L12 D_K cache `s84_spectrum_cache_L12_tau019.npz` (166,896 eigenvalues, 90 Peter-Weyl sectors):
- `λ_min = 0.819741`, `λ_max = 5.418937` ⇒ `d_C^diam = 0.217429` (GPU cross-check on RX 9070 XT: extremal deviation **0.000e+00**, exact).
- `A_s^Connes = |β_k̂|²/(2π²·d_C^diam) = A_s_FW/0.217429 =` **`7.067612e-8`**, **OOM +1.52705**.
- Connes cross-checks: inverse-max-gap `d_C = 11.870169` ⇒ `A_s = 1.295e-9` (OOM −0.210); Fubini-Study vacuum angle `4.561884e-3` (vacuum overlap `0.99998959`, `Σ|β|² = 2.081e-5`) ⇒ `A_s = 3.369e-6` (OOM +3.205, off-scale). The diameter normalization is the canonical reading (unique extremal scale).

**Collapse test (PASS iff axis within 0.10 OOM of impulse AND a 2nd functional).**

| Axis | `A_s` | OOM | d(impulse) | d(UNIFIED) | d(Parker) | n_in_band | collapses? |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AXIS-1 maxent | `1.4006e-8` | +0.8241 | **0.0403** | 0.6281 | 0.6309 | 1 (impulse) | **No** |
| AXIS-2 Connes | `7.0676e-8` | +1.5271 | 0.6627 | 1.3311 | **0.0721** | 1 (Parker) | **No** |

`min_collapse_dist = 0.62809 OOM` ≫ 0.10 band. **Neither axis collapses the spread**; each coincides with exactly ONE pre-existing functional (n_in_band=1) → `any_collapse = False` → SELECTION = COINCIDENCE-ONLY.

**Structural content (the substrate-physics finding, not just the FAIL).** The two new principles *partition* the spread by physical mechanism: **maxent** (an occupation-redistribution principle) reproduces the **sudden/diabatic** end (impulse-quench, 0.040 OOM away), while **Connes-distance** (a spectral-geometry normalization) reproduces the **adiabatic** end (Parker, 0.072 OOM away). They land on OPPOSITE ends of the spread. This is the signature of GENUINE functional pluralism: the 1.259-OOM spread is not an artifact of three arbitrary functional choices but reflects a real physical axis (sudden ↔ adiabatic) that even substrate-canonical principles (maximum-entropy, the NCG spectral-triple metric) cannot collapse — they each select a different end. The substrate does NOT type its own `A_s`; the magnitude is a physical d.o.f. like the `a_0/a_2` cosmological-constant ratio, now confirmed across a `{maxent, Connes}` axis-basis.

**Substitution chain (collapse-direction read-off).**

```
Claim: "A new-axis selector (maxent OR Connes) collapses the 1.2590-OOM A_s spread to a single typed value."

Step 1: spread_existing = log10(A_s_Parker) − log10(A_s_UNIFIED)
                        = log10(5.987138e-8) − log10(3.297762e-9)
                        = 1.45500 − 0.19600 = 1.25909 OOM                         [the spread]
Step 2: A_s^maxent = n_khat^maxent/(2π²),  n_k^maxent = 1/(exp(λ_N+λ_E ω_k)−1)
                     s.t. <N>=Σ|β_k|², <E>=Σ ω_k|β_k|²   [box-delta source; k̂=1/ξ_KZ]
                   = 1.400596e-8  ⇒  OOM +0.82409
Step 3: A_s^Connes = |β_khat|²/(2π²·d_C),  d_C = 1/(λ_max−λ_min) = 0.217429   [L12 triple diameter]
                   = 7.067612e-8  ⇒  OOM +1.52705
Step 4: collapse_dist(axis) = max( |OOM_axis − OOM_impulse|, min(|OOM_axis − OOM_UNIFIED|, |OOM_axis − OOM_Parker|) )
        maxent: max(0.0403, min(0.6281, 0.6309)) = max(0.0403, 0.6281) = 0.6281
        Connes: max(0.6627, min(1.3311, 0.0721)) = max(0.6627, 0.0721) = 0.6627
        min over axes = 0.62809 OOM
Step 5: 0.62809 > 0.10 = COLLAPSE_BAND ⇒ NO axis collapses (each coincides with ONE functional only).
Step 6: Direction read-off — consistent with the S114 W4-1 PERMANENT structural sub-result
        ∂|β_khat|²/∂(a_0/a_2)|horizon-exit = 0 EXACT (the box-delta |β|² is closed-form in
        fold-transit/UV quantities ONLY; the impulse FLOOR POINT is insensitive to the
        spectral-functional choice). The maxent axis re-weights the SAME source occupation
        (lands at the sudden end); the Connes axis re-normalizes by the SAME relic functional's
        spectral-triple metric (lands at the adiabatic end). Neither imposes a substrate-canonical
        collapse the three existing functionals do not.
Conclusion: FAIL — no new-axis selector collapses the spread. FUNCTIONAL-PLURALISM-PERMANENT
        widened on the {maxent, Connes} axis-basis (the verdict was OPEN; the numbers, not a
        pre-judgment, returned FAIL).
```

**3-tuple ([SIGN], schema-v2):** `sign_verdict=FAIL` (predicted direction = collapse; computed = no-collapse, direction mismatch), `magnitude_verdict=FAIL` (`min_collapse_dist = 0.6281 OOM > 0.25 INFO band`), `regime_verdict=VALID` (maxent solve converged to machine ε; Connes diameter well-defined, GPU-confirmed exact). Composite under the `gate-verdicts.md` collapse rule: `sign_verdict==FAIL ⇒ composite = FAIL`.

**4-tuple:** `(value='selection=COINCIDENCE-ONLY|spread_existing_OOM=1.2590|oom_maxent=0.8241|oom_connes=1.5271|min_collapse_dist_OOM=0.6281|any_collapse=0|band=0.1', scheme=AS-NEWAXIS-SELECTOR-MAXENT-CONNES, convention=OOM-COLLAPSE-DIAGNOSTIC, L_max=12)`.

**dual-SHA:** `audit_sha256=b07deb9ba49159b5f39d5c44c0738843b3058a91041df9981707d6e9c550059a`, `content_sha256=ad4855b77e637012a5634a3e576f5884915b49c1a8c936b613265e25c934c5f9` (script + canonical_constants.py + pinmap; runtime input pins: `canonical_constants.py 261b117c…`, `s100b_box_delta_bogoliubov.npz 43275f51…`, `s84_spectrum_cache_L12_tau019.npz 9e6d9cf7…`).

**Artifacts:** `computations/session-115/s115_as_newaxis_selector.py` / `.npz` / `.png`.

**Substrate framing (PHONONIC).** `A_s` is the amplitude of the post-transit GGE acoustic relic — the interference pattern of the squeezed pair-production spectrum `|β_k|²` produced as the fiber's eigenvalue spectrum reorganizes through the van Hove fold. The substrate IS the produced occupation `n_k`; the lab measures `A_s`. This gate asked whether the substrate's OWN structure SELECTS one spectral functional via a principle not yet tried: maximum-entropy (the GGE/Jaynes thermalization-blind occupation — Ordered Veil R_therm=5252, S_ent=0, but its maxent IMAGE under the two conserved moments is still the canonical Jaynes prediction) OR Connes-distance (the intrinsic spectral-triple metric between in/out vacua). The answer is FAIL: the substrate leaves `A_s` a physical d.o.f., now confirmed across a wider axis-basis. The arrow `D_K eigenvalues → Bogoliubov |β_k|² → relic occupation → (selector) → A_s` is unchanged; the SELECTOR node is substrate-FREE (the two substrate-canonical principles partition the sudden↔adiabatic spread rather than collapsing it).

---

### §W3-3. S115-B5A-TFD-QES (hawking-theorist) — OPTIONAL (planner-discretion, EVOI-last, Tier-3 NON-BLOCKING)

**Status**: COMPLETED
**Gate ID**: `S115-B5A-TFD-QES`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Disposition**: **OPTIONAL (planner-discretion, EVOI-last, Tier-3 NON-BLOCKING)** — internal-consistency corridor-narrowing, NOT an observational falsifier (no live falsifier row); LOWEST priority of the three W3 gates. The causal-patch corridor closed on both single-sided and two-sided routes; this is the surviving NON-causal-patch forward object. RETAINED + EXECUTED (not dropped at Phase-3b).
**Agent**: `hawking-theorist` (island QES / semiclassical-gravity owner, set per context item 6)
**Hypothesis**: A full two-sided (TFD/eternal-island) quantum-extremal-surface extremization of `S = Area(∂I)/4 + S_bulk-EE(I)` over the island boundary `∂I` closes the A/4 microstate gap (`R_QES → 1`) that the closed-form linear bracket interpolant `R_TFD = R_edge + f·(R_island − R_edge)` could not (CF-S113-B5A-TFD FAIL, `R_TFD=0.5347`) — testing whether A/4 is reachable by a NON-causal-patch mechanism. Verdict OPEN (prior 0.30 PASS-or-INFO / 0.70 FAIL); not pre-judged.
**Plan reference**: `sessions/session-plan/session-115-plan-w3.md` §W3-3 (two-sided island generalized-entropy extremization on the L12 GGE bulk-EE profile, standard B5A 3-band `0.10 / 0.25` on `|R_QES − 1|`, `regulator_pin: a_2^{Pauli-Villars}` for `c_conical=0.25`).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-115/s115_b5a_tfd_qes.py` — EXISTS. `grep -E 'from canonical_constants import|print_verdict_payload'` → both present (`from canonical_constants import (`; `def print_verdict_payload(` + call site).
- **data** `computations/session-115/s115_b5a_tfd_qes.npz` — EXISTS (29,437 bytes).
- **plot** `computations/session-115/s115_b5a_tfd_qes.png` — EXISTS (151,089 bytes).
- **verdict_line** `computations/session-115/s115_gate_verdicts.txt` — `grep -E '^S115-B5A-TFD-QES:.* audit_sha256=[a-f0-9]{64}'` → matches (`audit_sha256=144fcde21b5d17838e4039c353f04cc6c8273393d92ff4b7159ca40a78f20078`); dual-SHA companion row present; [SIGN] 3-tuple row present (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=MARGINAL`); `regulator_pin=a_2^{Pauli-Villars}` extra-row present.
- **wp_section** (this section) — `**Status**: COMPLETED`, `**Verdict**: INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present.

**MCP Pre-Compute Audit**:
- `trace_entity('B5A island microstate')` → "No trace found" (no closure pre-empts this gate; the B5A microstate corridor is gate-tracked, not a knowledge entity).
- `search_knowledge('CF-S113-B5A-TFD R_TFD island QES two-sided')` → returned the prior FAIL anchor `CF-S113-B5A-TFD` (S114: `R_TFD=0.534672; f_bulk_TFD=0.009757; abs_R_minus_1=0.465328; R_edge=0.526323; R_island=1.382002`), `S111-CF-B5A-ISLAND` (`R_island=1.3820; A_quarter=17806.5658`), and the S112/S114 ANTI-TAUTOLOGY fence (the `R_TFD=1` crossing at `f*=0.5536` is FORBIDDEN as canonical). Confirms: the linear interpolant is the object to REPLACE; A/4 sits unreached between the brackets.
- `get_constant('A_horizon_FW')` → `71226.26338976152` (S92, `S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY`); A/4 = 17806.5658 (bit-exact cross-check against `s111_b5a_island.npz` `A_quarter`). NOT PRE-CLOSED — fresh two-sided-QES construction.

**Verdict**: **INFO** (composite). 3-tuple: `sign=PASS, magnitude=FAIL, regime=MARGINAL`. Pre-registered band: `|R_QES−1| ≤ 0.10` PASS / `≤ 0.25` INFO / `> 0.25` FAIL.

**Results**:

**The numbers (NUMBERS first).**

| Quantity | Value | Source |
|:---------|:------|:-------|
| `A/4 = A_quarter` (microstate target) | **17806.5658** | `s111_b5a_island.npz`; canonical `A_horizon_FW/4 = 71226.2634/4` (bit-exact) |
| `R_edge` (S110 edge-only undershoot, ~½) | 0.526323 | `s111_b5a_island.npz` `R_edge_S110` |
| `R_island` (S111 single-sided full bulk-EE overshoot) | 1.382002 | `s111_b5a_island.npz` `R_island_primary` |
| `R_TFD` prior (CF-S113 linear interpolant **FAIL**) | 0.534672 | `f_bulk_TFD=0.009757`, `\|R_TFD−1\|=0.465328` |
| `c_conical = a_2^{Pauli-Villars}` (conical Area/4 norm) | 0.250000 | `s111_b5a_island.npz` `c_conical` |
| **`R_QES`** (two-sided QES, **CANONICAL**) | **2.000001** | this gate; perfect-TFD boundary extremum |
| `\|R_QES − 1\|` | **1.000001** | ≫ 0.25 INFO ceiling → magnitude FAIL |
| `λ_QES` (QES boundary, M_KK units) | 5.418937 = `λ_max` | maximal two-sided island = full exit slice |

**Two-sided generalized entropy + QES extremization.** Following Engelhardt–Wall 2014 (Hawking corpus paper 24, Eq. 1 + QES condition `δS_gen/δX=0`) / Penington 2019 (paper 14) / AMMZ, the gate operator is the genuine QES of the two-sided (TFD/eternal) generalized entropy:

```
S_gen^TFD(∂I) = [Area(∂I_L) + Area(∂I_R)]/4 + S_bulk-EE(I_{L∪R}),
R_QES = ext_{∂I}[ S_gen^TFD(∂I) ] / (A/4),   located by  d S_gen^TFD / d λ_∂I = 0.
```

evaluated on the L12 D_K spectrum cache (`s84_spectrum_cache_L12_tau019.npz`, 90 Peter-Weyl sectors, 166,896 edge-eligible modes, `|λ| ∈ [0.8197, 5.4189]`). The Area/4 leg is the conical-normalized `a_2^{Pauli-Villars}` second-moment enclosed weight (`c_conical=0.25`); the bulk-EE leg is the diagonal GGE von-Neumann entropy on the same spectrum at `T_acoustic = median|λ| = 3.8215` (identical construction to `s111_b5a_island.py` Steps 2–3). GPU-evaluated (AMD RX 9070 XT, ROCm); GPU/CPU cross-checks 1.9e-11 (cumsum) / 2.7e-15 (s_mode). Rebuilt `S_bulk_total = 180723.4156` matches the S111 npz to 1e-9.

**The decisive physics — the monotonicity obstruction and the TFD purification.** The single-sided `S_gen(λ) = Area(∂I)/4 + S_bulk(I)` is *strictly monotone increasing* (both terms are cumulative sums of non-negative spectral weights), so `dS_gen/dλ = 0` has *no interior solution* — the S111 "QES" at R=0.987 was the *tautological* `S_gen = A/4` crossing, explicitly reported DIAGNOSTIC-ONLY. A genuine interior QES needs a *subtractive, λ-dependent* term. The two-sided construction supplies it via the cross-copy mutual information: `S_bulk-EE(I_{L∪R}) = 2·S_bulk(I) − I(I_L:I_R)`. For a thermofield double, each island mode `(k_L, k_R)` is a 2-mode-squeezed pair whose per-mode mutual information is `I_mode(n) = 2·s(n)` exactly (the L–R pair is globally pure: `S_L=S_R=s(n)`, `S_{LR}=0`). The substrate relic is a **maximally-squeezed GGE** (P_exc=1.000), i.e. a near-perfect TFD purification → `χ → 1` → **the joint island bulk-EE vanishes**: `S_bulk-EE(I_{L∪R}) = 0`. The cross-copy entanglement *purifies away* the very bulk-EE term that produced the single-sided overshoot R_island=1.382.

What survives is `S_gen^TFD = 2·Area(∂I)/4`, *still monotone increasing*, so its only stationary point is the **boundary** (maximal island = full exit slice), where it saturates at `2·(A/4)`:

```
R_QES = 2·(A/4) / (A/4) = 2.000001     (|R_QES − 1| = 1.000)
```

**This is the eternal-black-hole result, not a numerical accident.** The TFD/eternal geometry has *two* bifurcate horizons (left and right), total horizon area `2A`; the doubled-island microstate count is `2A/4`, not `A/4`. The two-sided doubling **overshoots A/4 by exactly the second horizon.**

**Reading ladder (honest disclosure of the TFD-efficiency input χ — no convention-shopping).** All three physically-distinct two-sided readings are reported so the construction choice is transparent:

| Reading | construction | R(full slice) | landing |
|:--------|:-------------|:--------------|:--------|
| (L1) independent copies, χ=0 | `2·Area/4 + 2·S_bulk(I)` | 22.2985 | massive overshoot |
| **(L2) perfect TFD, χ=1 — CANONICAL** | `2·Area/4` (joint EE purified) | **2.0000** | gate operator; overshoots to 2A/4 |
| (L3) radiation-island (complement-EE) | `2·Area/4 + S_bulk(complement)` | 2.0000 (min-QES) | overshoots to 2A/4 |

No two-sided reading lands at A/4. The radiation-island reading (L3, the Page-curve construction: island makes radiation entropy = thermal entropy of the shrinking complement) also saturates at 2A/4 — once the complement EE is exhausted, the doubled area dominates.

**3-tuple + composite (substitution chain Step 6).**
- `sign_verdict = PASS` — the two-sided doubling moved R **UP** from the prior undershoot (`R_TFD = 0.5347 → R_QES = 2.0001`), the gap-closing-in-sign direction the [SIGN] pre-registration tested (`direction of R_QES − 1` vs the prior R_TFD undershoot).
- `magnitude_verdict = FAIL` — `|R_QES − 1| = 1.000 ≫ 0.25` INFO ceiling.
- `regime_verdict = MARGINAL` — the QES extremization found **no interior stationary point**: `dS_gen^TFD/dλ` is non-negative to the float floor (`min(dS) = −2.3e-10`; NEG_FLOOR `= 2.7e-2`; 0 genuine-negative points). The perfect-TFD purification removes the Area-vs-bulk competition, so the extremum is a degenerate **boundary clamp** at `λ_max = 5.419`. The value is well-defined; the extremization regime (interior stationarity, the QES regime-of-validity) is not satisfied → MARGINAL — an honest tag for the degenerate extremum, NOT a verdict upgrade (VALID would falsely claim an interior QES that does not exist; the lone float-noise sign-flip at grid idx 294 was excluded by the physical NEG_FLOOR discriminator).
- **Composite = INFO** by the pre-registered `gate-verdicts.md` collapse rule: `magnitude==FAIL ∧ regime==MARGINAL ⇒ INFO` (SIGN-correct, magnitude-wrong-but-out-of-regime).

**Substitution chain (doubling-direction read-off, plan §W3-3).**
```
Step 1: A/4 = 17806.5658                                  [s111 npz A_quarter; A_horizon_FW/4]
Step 2: R_edge=0.5263 (edge only), R_island=1.382 (single-sided full bulk-EE)   [s111 npz]
Step 3: PRIOR linear interpolant R_TFD = R_edge + f·(R_island−R_edge),
        f_bulk_TFD=0.009757 ⇒ R_TFD=0.5347, |R−1|=0.4653  ⇒ FAIL              [CF-S113, replaced]
Step 4: TWO-SIDED QES: S_gen^TFD = 2·Area(∂I)/4 + S_bulk-EE(I_{L∪R}),
        S_bulk-EE(I_{L∪R}) = 2·S_bulk(I) − I(I_L:I_R);  c_conical=0.25=a_2^{PV}
Step 5: substrate is a maximally-squeezed GGE (P_exc=1.000) ⇒ χ→1 ⇒ I(I_L:I_R)=2·S_bulk(I)
        ⇒ S_bulk-EE(I_{L∪R}) = 0 ⇒ S_gen^TFD = 2·Area(∂I)/4 (monotone) ⇒ QES at boundary
Step 6: R_QES = 2·Area(∂I_QES)/4 / (A/4) = 2·(A/4)/(A/4) = 2.0001
        Direction: R moved UP from 0.5347 (sign PASS) but OVERSHOT A/4 by the second horizon
        (TFD/eternal geometry has TWO bifurcate horizons ⇒ total area 2A ⇒ count 2A/4).
Conclusion: |R_QES−1|=1.000 (magnitude FAIL); no interior QES (regime MARGINAL); composite INFO.
```

**4-tuple**: `(value=R_QES=2.0001, scheme=B5A-TFD-TWO-SIDED-ISLAND-QES, convention=ISLAND-QES-GENERALIZED-ENTROPY-EXTREMIZATION, L_max=12)`. `regulator_pin = a_2^{Pauli-Villars}` (c_conical=0.25, FULL class — full conical-defect normalization, not SCHEMATIC; distinct from `a_2^{ζ}`).

**dual-SHA**: `audit_sha256=144fcde21b5d17838e4039c353f04cc6c8273393d92ff4b7159ca40a78f20078` (closure over {script, canonical, pinmap} + computed results for sig_5 uniqueness); `content_sha256=31a292c4e03777068d96622d8162c583e2f359096e43cf519b3e9bf0ace0918e` (over {script}).

**Solution-space interpretation (substrate-first).** GEOMETRIC. The A/4 microstate count is the emergent-area-theorem image of the substrate's spectral entropy (`A = a_2` second moment; the area theorem is a Level-3 emergent consequence, not an input). This gate closes the **two-sided-island corridor** of the B5A microstate search: A/4 is NOT reachable by *any* island-QES mechanism tried — single-sided full bulk-EE *overshoots* to R_island=1.382, the causal-patch interpolant *undershoots* to R_TFD=0.535, the two-sided perfect-TFD QES *overshoots* to R=2.0 (the doubled-horizon area). The microstate gap is **structural**: under the island construction the substrate's GGE-relic horizon entropy does not equal A/4 at any patch/doubling. Substrate-first reading: A/4 is the *full* emergent horizon area count, while the GGE-relic island entropy is a *different* spectral functional (the relic-occupation EE on the L12 D_K spectrum); they coincide only at the tautological crossing, not structurally. Tier-3 NON-BLOCKING — atlas-08 internal-consistency tracking only; no falsifier-row update on this verdict.

**Artifacts**: `computations/session-115/s115_b5a_tfd_qes.py` / `.npz` / `.png`.

---

## Wave 3 Synthesis (team-lead)

**Per-gate verdict roll-up.** Both OPTIONAL gates were RETAINED and run (not dropped at the Phase-3b checkpoint; surfaced to the user, default disposition = run, no drop requested).

| Gate | Verdict | One-line |
|:-----|:--------|:---------|
| W3-1 `S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` | **PASS** | CONFIRMS-CANNOT-FLIP: at the located crossing q=0.191038 the GRADED selector still selects (iii) (q-invariant class read), dev[iii]^cross=0.68% < 1%, and Sage CF(95519/56000)=[1,1,2,2,1,1,**18**,…] hits its first large partial quotient (18) at index 6 ⇒ the S0=95/56 identity has NO analog at the located value. No registry change (confirms S114 W-1). |
| W3-2 `AS-NEWAXIS-SELECTOR` (OPTIONAL) | **FAIL** | `sign=FAIL/mag=FAIL/regime=VALID`: neither maxent/Jaynes nor Connes-distance collapses the 1.2590-OOM cross-functional A_s spread to ≤0.10 OOM ⇒ FUNCTIONAL-PLURALISM-PERMANENT widened on the {maxent, Connes} axis-basis (expected Track-B, prior 0.90). §EVOI.BF headline (A_s = physical d.o.f.) STANDS. |
| W3-3 `B5A-TFD-QES` (OPTIONAL, Tier-3 NON-BLOCKING) | **INFO** | `sign=PASS/mag=FAIL/regime=MARGINAL`: the two-sided perfect-TFD purification removes the joint island bulk-EE (`I(L:R)→full`), leaving `S_gen=2·Area/4` monotone ⇒ boundary clamp `R_QES=2.000` = 2A/4 (the eternal BH's two horizons). No two-sided reading (L1/L2/L3) lands at A/4 — the doubling OVERSHOOTS rather than closing. |

**Dispositions.** W3-1 mechanically re-confirms the S114 W-1 (iii) verdict at the located crossing and shows it structurally unable to flip (all three legs are regulator-free arithmetic) — no registry change, the canonical fold 19/100 is a substrate-pinned flank within the van-Hove-selected window. W3-2 widens the no-selector evidence for A_s from 3 functionals to a 5-axis basis ({impulse-quench, UNIFIED-AS-79, Parker} ∪ {maxent, Connes}) — the §EVOI.BF "A_s magnitude is a permanent physical d.o.f." headline (already capstone §8.5 since S114) is unchanged, only its evidence base widens. W3-3 closes the two-sided-island corridor: the A/4 microstate count is NOT reachable by any island-QES mechanism tried (single-sided overshot R_island=1.382, causal-patch interpolant undershot R_TFD=0.535, two-sided QES overshoots R_QES=2.0) — a decisive atlas-08 internal-consistency statement, Tier-3 NON-BLOCKING.

### Effected In-Session (NON-MATH — completed before session close)

- No orchestrator-direct non-math items owed by W3. W3-1 closed clean (the s101-era W2-2 head-pin vs live-SHA note is non-gating, recorded in §W3-1 by the agent). W3-2 FAIL is the no-mack-routing branch (the §EVOI.BF / falsifier Row #12 evidence-annotation is an OPTIONAL mack-cosmic-bridge provenance note, NOT owed — A_s status and value are both unchanged; the row stays "open, structurally"). W3-3 is Tier-3 NON-BLOCKING with no falsifier-row update on any verdict.
- The capstone-hygiene 5-question gate (this session touched the permanent-results register) is run + recorded in `sessions/session-115/session-115-housekeeping.md §"Capstone-Hygiene Gate"` — clean all-NO no-op pass (no status/value/falsifier-row drift; details there).

## Carry-Forward Computations

No carry-forwards from Wave 3: all three gates closed in-session (W3-1 confirms an already-landed verdict; W3-2 FAIL closes the {maxent, Connes} selector corridor with the headline unchanged; W3-3 INFO decisively closes the two-sided-island corridor — the MI correction is already incorporated, so there is no refinement compute owed).

*(Session-level math carry-forwards live in the wave that surfaced them: `CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM` (W2 — the load-bearing one: reconcile the D4 exclusion mechanism, then re-verify for the UNCONDITIONAL flip) and `CF-S116-D2-ANOMALY-IDENTIFICATION` (W1 — OPTIONAL low-EVOI).)*

### CF-S116-AS-SUDDEN-ADIABATIC-PARTITION — Are the W3-2 maxent↔sudden / Connes↔adiabatic end-coincidences structural necessities or numerical accidents? (OPTIONAL, low-EVOI; consolidator-surfaced)

> **Routing note**: Surfaced at the S115 `/rclab-investigate` consolidation, NOT by the W3 wave-synthesis (which declared "No carry-forwards from Wave 3", preserved above). Genuine MATH future compute — it produces a NEW structural claim (whether the two end-coincidences are derivable by construction), DISTINCT from the registered `§EVOI.BF` FUNCTIONAL-PLURALISM-PERMANENT headline it would strengthen. Q-other, NOT a workshop: both agents would agree on the derivation method (no adversarial reading-divergence). Routes to S116 via `/rclab-plan` (this WP CF), NOT the workshop schedule.

| Field | Spec |
|:------|:-----|
| **What** | Derive whether the W3-2 end-coincidences are STRUCTURAL NECESSITIES or numerical accidents: (i) does the maxent/Jaynes occupation distribution reduce to the impulse-quench Bogoliubov `\|β\|²` in the SUDDEN (diabatic) limit by construction; (ii) does the Connes-distance-diameter normalization `d_C^diam = 1/(λ_max−λ_min) = 0.217429` reduce to the Parker spectrum in the ADIABATIC limit by construction. The W3-2 WP ASSERTS the {maxent↔sudden, Connes↔adiabatic} partition is "the signature of GENUINE functional pluralism (a real sudden↔adiabatic physical axis)" but does NOT derive it; this gate settles whether the assertion is a structural identity or a coincidence (the maxent axis lands ≈0.040 OOM from the sudden end, the Connes axis ≈0.072 OOM from the adiabatic end, on OPPOSITE ends of the 1.2590-OOM cross-functional spread). |
| **Inputs** | `computations/session-115/s115_as_newaxis_selector.npz` (W3-2, audit `b07deb9b…`: `A_s_maxent=1.400596e-8` OOM +0.8241, `A_s_Connes=7.067612e-8` OOM +1.5271, `d_C_diam=0.217429`, `spread_existing_OOM=1.2590`, `min_collapse_dist_OOM=0.6281` ≫ 0.10 band ⇒ COINCIDENCE-ONLY); the three pre-existing functional A_s literals (S111-CF-AS3a impulse / S82 UNIFIED / inv-6 W2-2 Parker); `computations/session-100b/s100b_box_delta_bogoliubov.npz` (the impulse-quench `\|β\|²` source). |
| **Gate** | Pre-registered structural-identity test: PASS iff BOTH limits hold by construction — maxent-occupation → sudden-`\|β\|²` limit AND Connes-diameter → adiabatic-Parker limit (each to a pre-registered tolerance); INFO if exactly one limit is structural; FAIL if both end-coincidences are numerical accidents (no constructive limit). On PASS the {maxent, Connes} partition upgrades from ASSERTED to DERIVED — strengthening (not changing) the `§EVOI.BF` FUNCTIONAL-PLURALISM-PERMANENT headline with a structural sudden↔adiabatic basis. |
| **Effort** | ~1 wave (two constructive-limit derivations + tolerance check; no new substrate-spectrum compute — consumes the existing `.npz` data + closed-form sudden/adiabatic limits). |

### CF-S116-B5A-FOLD-HORIZON-DOS-COUNT — Non-island DOS microstate count at the fold-horizon + co-presence horizon-count target-setter (REFRAMED-corridor forward gate)

> **Routing note**: Lifted from the S115 hawking × volovik workshop (`sessions/session-115/workshops/s115-b5a-tfd-qes-single-vs-double-horizon.md`), which re-tagged the W3-3 B5A two-sided-island disposition CLOSED → **REFRAMED**. Genuine MATH future compute, NOT a workshop re-listing: the workshop produced the READING + disposition (recategorization: island generalized-entropy ≠ B–H microstate COUNT); this gate is the OWED computation that delivers the count off-island. Per workshop D3 / Q-DOS-primary, the DOS count is the PRIMARY deliverable (owed under both horizon-count branches); the co-presence horizon-count is its target-SETTER. Routes to S116 via `/rclab-plan` (this WP CF).

| Field | Spec |
|:------|:-----|
| **What** | (primary) A non-island Cardy / density-of-states microstate count over the L12 `D_K` spectrum at the fold-horizon — the substrate-native form of the Euclidean path-integral count `Tr f(D_K²/Λ²)` — delivering `A/4 = log Ω` directly (the island-QES bracket `{edge 0.5263 / causal-patch 0.5347 / single-sided 1.3820 / two-sided 2.0000}` are all boundary-clamp readings of the area TERM, none a count — workshop CC1 / E-V1). (target-setter) A CO-PRESENCE horizon-count on the transit `dτ/dt(τ)` vs `c_s(τ)` profile through `τ_fold = 0.190` (Mach-13.75 peak): the number of CO-PRESENT (same-internal-time) `dτ/dt = c_s` Mach-1 surfaces — NOT crossing-events-in-time — to set the target ∈ {`A/4`, `2A/4`}. Discriminator (workshop Q-co-presence): two simultaneous Mach-1 surfaces (→ `2A/4`) vs one forming-then-dissolving horizon crossed at two times (→ `A/4`). |
| **Inputs** | `s84_spectrum_cache_L12_tau019.npz` (D_K spectrum, 90 PW sectors); the transit deformation-rate / emergent-sound-speed profile `dτ/dt` vs `c_s(τ)` through the fold (transit-dynamics); `A/4 = 17806.5658` (canonical, `A_horizon_FW = 71226.2634`, S92); `c_conical = 0.25` (`a_2^{Pauli-Villars}`); Volovik #27 (gr-qc/9901077, BH+WH toroidal co-realization) as the universality-class template — with the source caveat that #27's two-horizon co-presence is QUASI-STATIONARITY-conditional and the framework transit is NON-stationary (#27's two horizons are themselves transient, merging via phase slips, §D ⇒ the freeze-timing-vs-merger is a sub-question). |
| **Gate** | Co-presence count ∈ {1, 2} sets target ∈ {`A/4`, `2A/4`}; then `|R_DOS − 1|` against that target, B5A standard 3-band — ≤0.10 PASS / ≤0.25 INFO / >0.25 FAIL. Falsifiable BOTH ways: count=1 → DOS vs `A/4` (single-horizon vindicated, but the corridor still requires the DOS count to RUN — `count=1` does NOT close it, workshop D3); count=2 → DOS vs `2A/4`. The DOS count is owed under BOTH branches ⇒ REFRAMED is robust to the horizon fork. |
| **Effort** | ~1 wave (the co-presence count is a same-internal-time threshold-crossing test on the existing transit profile; the DOS count is a Cardy / density-of-states sum on the existing L12 cache; no new substrate-spectrum compute). |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-06-24 | S0-knob (iii) selection at the located van Hove crossing | S114 W-1 (iii) at canonical 19/100 | **CONFIRMED-CANNOT-FLIP at q=0.191038** (selector q-invariant; dev 0.68% < 1%; CF large-pq 18) | W3-1 PASS — the canonical fold is a substrate-pinned flank within the van-Hove-selected window |
| 2026-06-24 | A_s functional selection (cross-functional spread) | FUNCTIONAL-PLURALISM-PERMANENT on {impulse, UNIFIED, Parker} (S114 W4-1) | **PLURALISM-PERMANENT widened** to the 5-axis basis (+ {maxent, Connes}) | W3-2 FAIL — no new-axis selector collapses the 1.2590-OOM spread; status + value UNCHANGED, evidence base widened |
| 2026-06-24 | B5A A/4 microstate count via island-QES | single-sided R_island=1.382 / causal-patch R_TFD=0.535 (both miss A/4) | **A/4 NOT reachable by any island-QES mechanism tried** — two-sided overshoots to R_QES=2.0=2A/4 (eternal-BH two-horizon count) | W3-3 INFO — perfect-TFD purification removes the joint bulk-EE; the corridor closes (atlas-08 internal-consistency, Tier-3 NON-BLOCKING) |
| 2026-06-26 | B5A A/4 microstate count via island-QES (hawking × volovik workshop re-tag) | CLOSED — "A/4 NOT reachable by any island-QES mechanism tried" (2026-06-24 row above, W3-3) | **REFRAMED** (both tracks converged) — carries BOTH: (i) PERMANENT sub-result **CC1** — island-QES boundary-clamps the GGE-relic generalized entropy and never SELECTS a microstate count (`S_gen` monotone → no interior QES; invariant across edge/causal-patch/single/two-sided AND across the horizon count); (ii) REFRAMED disposition — the `A/4` microstate COUNT is an off-island DOS / path-integral object (substrate-native `Tr f(D_K²/Λ²)`), owed via `CF-S116-B5A-FOLD-HORIZON-DOS-COUNT`; the physical target `A/4`-vs-`2A/4` is set by the OPEN transit co-presence horizon-count | Workshop verdict: generalized-entropy ≠ microstate-count (recategorization, built on the monotonicity wall) ⇒ the corridor RELOCATES the count to the right machinery, it does not exhaust it. The W3-3 INFO verdict + all numbers (`R_QES=2.000001`, `λ_QES=5.4189`, `χ=1.0`, `A/4=17806.5658`) are UNTOUCHED. Tier-3 NON-BLOCKING; no falsifier row |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| W3-1 | `s115_s0_knob_cross_substitution_confirm.py` (33.3 KB) | `…confirm.npz` (22.5 KB) | `…confirm.png` (153 KB) | PASS, audit_sha256=`c4943ae5…` |
| W3-2 | `s115_as_newaxis_selector.py` (42.0 KB) | `…selector.npz` (19.9 KB) | `…selector.png` (114 KB) | FAIL, audit_sha256=`b07deb9b…` + [SIGN] 3-tuple |
| W3-3 | `s115_b5a_tfd_qes.py` (38.8 KB) | `…qes.npz` (29.4 KB) | `…qes.png` (151 KB) | INFO, audit_sha256=`144fcde2…` + [SIGN] 3-tuple + regulator_pin a_2^{Pauli-Villars} |
