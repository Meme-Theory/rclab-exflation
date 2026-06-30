# Session 109 — Plan Wave 1 (single-gate close-out)

**Session**: 109 | **Wave**: 1 | **Mode**: SINGLE-GATE CLOSE-OUT (deliberately not a full session)
**Verdict file**: `computations/session-109/s109_gate_verdicts.txt` (canonical; emit via the `emit_verdict` knowledge-MCP tool per `.claude/rules/gate-verdicts.md` — all other paths FORBIDDEN)
**Working paper**: `sessions/session-109/session-109-w1-workingpaper.md`

## Honest scope note (why this session is one gate)

The `/rclab-plan` Phase-1 gather + Phase-1c-REGISTERS.CONSUME on S108 returns **exactly one tractable, dispatch-ready, pre-registrable compute carry-forward**: `CF-S109-VIICB-ZETA-NATIVE-LEVEL-3` (S108 w1 WP; S108 w2 WP carries NONE). The forward-register CONSUME (EVOI §1–§6, atlas-08, open-channel-ledger, atlas-04) confirms — re-affirming the S108 §6 CONSUME certification verbatim — that **every** remaining high-leverage register item is a STANDING GAP with **no** pre-registrable gate (M_KK-DERIVATION [the keystone bottleneck of #1/#2-scale/#7b′/#9b-SCALE], K_pivot/C2, residual-3% CC, τ_fold-RELAXATION, A_s floor, TD/LI H̃-divergence A3), a BLOCKED item (anchor-independent H₀), a DATA-HORIZON-gated item (branch-iv/DESI ~2027), the lone PENDING-VERIFICATION cohort holdout (K8 §VII.AF.1.STATE-PROJ — no dispatch-ready Stage-2 gate), or a conceptual Tier-4 item (arrow-of-time, Born rule, higher-moments). Leverage ≠ tractability. The framework is at a **completion plateau**; S110 is therefore framed as a structural-support INVESTIGATION (most naturally the M_KK-DERIVATION keystone), not a compute wave. This single gate is run now per the user directive ("if there is only the one carry-forward, just do it now").

---

## Gate S109-VIICB-ZETA-NATIVE-LEVEL-3

```yaml
gate_id: S109-VIICB-ZETA-NATIVE-LEVEL-3
schema_version: R3
trigger: "[VERIFY]"
classification: GEOMETRIC   # zeta-regularized spectral moment / Mellin-cone residue on (A_K, H_K, D_K) — the fabric, not its excitations
agent_type: lizzi-spectral-functional-theorist   # owns _analytic_zeta.py + the a_2 zeta-split provenance; zeta-regularized spectral action is their substrate
provenance: CF-S109-VIICB-ZETA-NATIVE-LEVEL-3  (sessions/session-108/session-108-w1-workingpaper.md §"Carry-Forward Computations")
```

### Hypothesis (one sentence)

The §VII.CB Level-3 magnitude anchor, re-evaluated on the **ζ-native functional** (the FULL-physical `analytic_zeta` Mellin↔Dirichlet route at the a₂ pole, `poleconv-A-double, pole_in_s=3, curvature_grade_n=2`) at canonical `L_max=10`, reproduces the canonical `g_M = a_2_FW_zeta = 2776.165389` to within the binding `L⁻³` Level-2 envelope (`rel < 1e-3`) — placing the Level-3 anchor and its Level-2 envelope on the SAME functional. **GENUINE — CAN FAIL** (S108 W1 proved the convergent partial sum cannot reach g_M; if the ζ-native route also misses g_M, or if g_M itself has no convergent ζ-native L→∞ limit, the magnitude channel is structurally un-anchorable even ζ-natively).

### PASS / FAIL / INFO

- **PASS** — `rel = |zeta_native_L3(L_max=10) − a_2_FW_zeta| / a_2_FW_zeta < 1e-3` **AND** the anti-tautology guard holds (the anchor is computed from the spectrum cache via `analytic_zeta`, NOT a re-read of `a_2_FW_zeta`; see audit_discriminators). ⇒ §VII.CB Level-3 magnitude row **HELD→SATISFIED**, full REGISTRY-PASS. The §7/falsifier-surface flip is `mack-cosmic-bridge` sole-writer (route at run-time per `feedback_mack-bridge-role.md`).
- **FAIL** — `rel ≥ 1e-3` with the ζ-native functional correctly constructed (it genuinely evaluates a₂ on the ζ side but still misses, OR the ζ-native a₂ at the (s=3,n=2) pole is Weyl-DIVERGENT in L_max so no convergent target exists). ⇒ magnitude channel **structurally un-anchorable even ζ-natively** (Non-Promotion-by-Held-Number, differentia `undischarged-magnitude-bound`, deeper hold). §VII.CB theorem-STRUCTURE + Level-1 + binding L⁻³ Level-2 stay STAGE-3-PERMANENT regardless.
- **INFO** — the constructed anchor is bit-identical to `a_2_FW_zeta` (load-and-compare-to-self ⇒ vacuous; the gate must be re-specified) OR a Tier-1 dimensionless re-anchor is required to make the comparison well-posed (per the §VII.BT S103 `peel_heldout` precedent, `cross-pillar-bridge-anatomy.md §25`). Composite-collapse: report the 3-tuple; INFO if magnitude=INFO.

Tolerance rule: **RATIO** (`rel`, relative to `a_2_FW_zeta`). Publication precision: `a_2_FW_zeta` is canonical at 7 sig figs ⇒ `rel_tol` floor `1e-7` ≪ the `1e-3` gate band (Class-8.3 clear).

### machinery_pin_map (PRDR — pinned at plan-freeze; executor runs the dry-run to confirm no free parameter remains)

```yaml
L_max: 10                        # canonical truncation (filter the L12 cache to p+q <= 10)
spectrum_cache: computations/session-84/s84_spectrum_cache_L12_tau019.npz   # tau_fold = 0.190
evaluator_module: computations/_shared/_analytic_zeta.py   # FULL-physical Mellin<->Dirichlet (NOT SCHEMATIC)
class_pin: FULL                  # level-pin per substrate-first-canonical-sourcing.md §(iv); convention carries NO -SCHEMATIC suffix
pole: s = 3                      # substrate-distance-1
poleconv: A-double               # zeta_{D_K}(s) = Sum m_k lambda_k^{-2s}; poles at s=(d-n)/2
curvature_grade_n: 2             # a_2 channel; (pole_in_s=3, curvature_grade_n=2), d_spec=8 -> n = 8 - 2*3 = 2
regulator_pin: a_2^{Mellin}      # poleconv-A-double (pole_in_s=3, curvature_grade_n=2); per regulator-pin-discipline.md §"Mellin Pole-Set Labeling"
target: a_2_FW_zeta              # 2776.165389 (canonical_constants.py; get_constant Superseded=False)
envelope_ref: computations/session-106/s106_w3_2_pillar_i_vi_iv_envelope.npz   # binding L^-3 Level-2 envelope (Level-2(L=10) = 1e-3)
baseline_ref: computations/session-108/s108_viicb_magnitude_remediation.npz    # partial-sum Z(inf) ~ 650.70, gap_factor 4.266 (the S108 FAIL the ζ-native route is contrasted against)
pass_band: 1e-3                  # = Level-2(L_max=10) envelope value
random_seed: N/A                 # deterministic (mpmath off-pole integration; mp.dps >= 50 per _analytic_zeta docstring)
gpu_path: CPU (mpmath arbitrary-precision off-pole integral; small); cap OMP_NUM_THREADS=8 before numpy import
```

### audit_discriminators (PRU / v3-closure-recovery guards)

1. **Anti-tautology (load-and-compare-to-self, v3 Class-6)** — the ζ-native L3 anchor MUST be computed from the spectrum cache via `analytic_zeta` (Dirichlet/Mellin residue at s=3). The script MUST assert `zeta_native_L3 != a_2_FW_zeta` bit-exact; equality ⇒ emit **INFO** (vacuous), never PASS.
2. **Convergent-vs-Weyl-divergent sub-determination** — evaluate `zeta_native(s=3, n=2)` across `L_max ∈ {6,8,10}` and report whether the a₂ pole value CONVERGES or DIVERGES with L_max. A divergent series has no L→∞ target ⇒ the magnitude channel cannot be anchored ζ-natively either (FAIL with structural finding), distinct from a convergent-but-slow miss.
3. **Level-pin disclosure** — `_analytic_zeta.py` is FULL-physical; the verdict `convention=` carries the FULL class (NO `-SCHEMATIC` suffix). If the executor finds any SCHEMATIC fallback path inside the module, disclose per `substrate-first-canonical-sourcing.md §(iv)`.
4. **Regulator-pin** — verdict carries `a_2^{Mellin}` + `poleconv-A-double (pole_in_s=3, curvature_grade_n=2)` companion row; consistent with the S108 ACFAMILY sibling-family re-pin (`8ca8f479`).
5. **Dual-SHA + sig_5** — `audit_sha256` = closure over the input-pin map; unique vs all prior s109 lines (only line in the file at emission).

### substitution_chain (executor completes per math-scripts.md §"Double-Check Logic" BEFORE compute; skeleton)

```
Claim: "the ζ-native a_2 at (s=3,n=2,A-double) reproduces g_M within the L^-3 envelope at L_max=10 (PASS), OR is Weyl-divergent in L_max (FAIL-structural)."
  Step 1: zeta_D(s) := Sum_k m_k lambda_k^{-2s}        [truncated Dirichlet, finite L_max; _analytic_zeta identity]
  Step 2: a_2-channel anchor := Res / off-pole analytic continuation at s=3 (A-double), grade n=2   [_analytic_zeta API]
  Step 3: g_M := a_2_FW_zeta = 2776.165389             [canonical; provenance "S42 spectral zeta sum + S46 a_2 split"]
  Step 4: rel := |anchor(L_max=10) - g_M| / g_M        [RATIO]
  Step 5: trend := sign(anchor(L=10) - anchor(L=8))    [convergent if -> 0; Weyl-divergent if monotone-growing]
  Conclusion: PASS iff (rel < 1e-3 AND anchor != g_M bit-exact); FAIL iff (rel >= 1e-3 AND functional correct); INFO iff tautology/ill-posed.
```

### dual_prior (track-discriminator per epistemic-discipline.md §"Dual-prior pre-registration")

- **Track A** (ζ-native SATISFIES — the S108 partial-sum FAIL was a functional-mismatch artifact; the same functional as g_M reproduces it): prior **0.55**.
- **Track B** (structurally un-anchorable even ζ-natively — g_M is itself a low-L / Weyl-divergent ζ-sum with no convergent L→∞ target): prior **0.45**.
- Discriminator: PASS → Track A 0.90; FAIL → Track B 0.90; INFO → priors unchanged (re-spec).

### input_files (script computes runtime SHA over each for the closure hash)

- `computations/session-84/s84_spectrum_cache_L12_tau019.npz`  `<runtime-sha>`
- `computations/session-106/s106_w3_2_pillar_i_vi_iv_envelope.npz`  `<runtime-sha>`
- `computations/session-108/s108_viicb_magnitude_remediation.npz`  `<runtime-sha>`
- `computations/_shared/_analytic_zeta.py`  `<runtime-sha>`
- `canonical_constants.py` (a_2_FW_zeta, d_spec, tau_fold)  `<runtime-sha>`

### output_artifacts

- script  `computations/session-109/s109_viicb_zeta_native_level3.py`  (`from canonical_constants import *`; `print_verdict_payload(...)`)
- data    `computations/session-109/s109_viicb_zeta_native_level3.npz`  (anchor(L∈{6,8,10}), rel, trend, dual-prior posterior, both SHAs)
- plot    `computations/session-109/s109_viicb_zeta_native_level3.png`  (ζ-native a₂(L) vs L_max, with g_M line + L⁻³ envelope band + the S108 partial-sum Z(∞) baseline for contrast)
- verdict `computations/session-109/s109_gate_verdicts.txt`  (canonical line + dual-SHA companion + regulator_pin companion; via `emit_verdict`)
- wp_section  `sessions/session-109/session-109-w1-workingpaper.md` §W1-1  (Status / Verdict / Output Artifacts / MCP Pre-Compute Audit / substrate framing)

### substrate framing (phononic-framing.md — substrate-IS)

The substrate IS the ζ-regularized spectral moment a₂ of D_K — `a₂ = Σ_k m_k λ_k^{-2s}|_{s=3, A-double}` analytically continued off the cone apex. g_M (the emergent 4-metric's a₂ Seeley-DeWitt coefficient) is this substrate-IS spectral moment; the laboratory never measures it directly. The gate asks whether the substrate's own ζ-native functional, truncated at the canonical L_max=10, lands on its L→∞ value within the algebraic envelope — a purely intrinsic substrate-convergence question. Direction: `D_K eigenvalues → ζ-native a₂ moment → emergent g_M → (would-be) measurement`. No container-thinking inversion.

---

## Decision point (S109 → close)

- **PASS** → §VII.CB Level-3 magnitude HELD→SATISFIED (mack flips the §7/falsifier-inventory row + registry §VII.CB Level-3 cell, sole-writer); §VII.CB reaches full REGISTRY-PASS. EVOI: move §VII.CB magnitude to §5 (closed). S110 = structural-support investigation (M_KK-DERIVATION keystone).
- **FAIL** → §VII.CB Level-3 magnitude **permanently un-anchorable** (structural, both partial-sum AND ζ-native); record the Non-Promotion-by-Held-Number boundary; theorem-STRUCTURE STAGE-3-PERMANENT stands. EVOI: §VII.CB magnitude closes as a permanent structural-position wall. S110 = structural-support investigation.
- **INFO** → re-spec (Tier-1 dimensionless re-anchor per §VII.BT precedent) as a carry-forward; S110 picks it up alongside the structural-support investigation.

In ALL cases the S109 close runs the capstone-hygiene 5-question gate (S109 touches §VII.CB, a capstone-governing register) and re-stamps the EVOI currency tag to S109.
