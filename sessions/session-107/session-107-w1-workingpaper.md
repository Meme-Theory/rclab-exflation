# Session 107 Wave 1 — §VII.CB Level-3 Magnitude-Convergence Discharge (Results Working Paper)

**Session**: 107 | **Wave**: 1 | **Plan**: session-107-plan-w1.md | **Theme**: Discharge the single HELD Level-3 row of the EXISTING §VII.CB cross-pillar bridge (Pillar I↔VI↔IV) by computing the MAGNITUDE channel directly and testing it against the binding L⁻³ Level-2 envelope.

## Gate Sections

### §W1-1. S107-VIICB-MAGNITUDE-CONVERGENCE-ANCHOR (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S107-VIICB-MAGNITUDE-CONVERGENCE-ANCHOR`
**Trigger**: `[VERIFY]` (NOT `[SIGN]` — the C_1 sign is a REPORTED DIAGNOSTIC, never a pre-registered direction; no schema-v2 3-tuple emitted)
**Classification**: **GEOMETRIC** (the M₂(ℂ) trace `Tr_{M₂(ℂ)}(P_a₂·T^{(IV)})|_L` is a spectral-triple-structural observable — the a₂ Seeley-DeWitt curvature-degree-2 K-homology class, not a phononic excitation)
**Agent**: `transit-dynamics-theorist` (NOT a Stage-2 verify ⇒ no author-exclusion; the agent owns the type-IV EMT + Γ_sub acoustic lift)
**Hypothesis**: The §VII.CB magnitude channel `M(L) = Tr_{M₂(ℂ)}(P_a₂·T^{(IV)})|_L` converges to the continuum HKR image `g_M = a_2_FW_zeta = 2776.165389` fast enough that `res(L=10) < 1e-3` and flows as `L⁻³` — confirming `M` is the FLOWING observable the envelope bounds, channel-orthogonal to the analytically-FLAT sign channel.
**Plan reference**: `sessions/session-plan/session-107-plan-w1.md` §W1-1 (machinery pin, thresholds, substitution chain Claims A+B, DST-T-3 lift sub-pin, Input-SHA Ledger).

**Verdict**: **FAIL** (robust — direction-neutral on the C_1 diagnostic; genuinely closes the magnitude-binding question, NOT a lift-dependent INFO)

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML; verified on disk by content-presence, NOT line count):

| Artifact | Path | must_contain → grep result |
|:---------|:-----|:---------------------------|
| script | `computations/session-107/s107_viicb_magnitude_convergence_anchor.py` | `from canonical_constants import` ✓ (line 79); `print_verdict_payload` ✓ (def + call) |
| data | `computations/session-107/s107_viicb_magnitude_convergence_anchor.npz` | keys present: `M_of_L`, `res_of_L`, `res_L10`, `alpha_fit`, `C1_sign`, `g_M`, `Level2_L10`, `lift_convention` ✓ (all 8) |
| plot | `computations/session-107/s107_viicb_magnitude_convergence_anchor.png` | log res(L) vs log L over {8,10,12} + L⁻³ reference + 1e-3 binding marker + fitted-slope line ✓ (140 dpi) |
| verdict_line | `computations/session-107/s107_gate_verdicts.txt` | `^S107-VIICB-MAGNITUDE-CONVERGENCE-ANCHOR:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row + `# regulator_pin=a_2^{zeta}` row |

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `get_constant('a_2_FW_zeta')` → **2776.165389**, S88, gate `S88-A-N-FW-CANONICALIZATION`, **Superseded=False** (the g_M continuum target, regulator a₂^{ζ}). Confirmed.
- `get_constant('L_envelope_d4_Lmax10')` → **0.001**, S86, gate `S86-W5-CANON-EXTRACT`, Superseded=False (the binding L⁻³ envelope at L_max=10; cross-checked against the LOADED `level2_at_lmax10=1e-3` from the S106 W3-2 envelope npz — match).
- `get_constant('tau_fold')` → **0.19** (cross-checked vs S105 npz `tau_fold` echo and the s84 cache τ-anchor — match).
- `search_knowledge('VIICB magnitude convergence anchor Level-3 ...')` → no S107 discharge present; the held Level-3 row is OPEN (confirmed not already discharged). `session-106-phonon-first-synthesis.md` confirms the magnitude channel `M(L) = Tr_{M₂(ℂ)}(P_a₂·T^{(IV)})|_L` with HKR `L→∞` image `g_M = a_2_FW_zeta` IS the observable the L⁻³ envelope bounds.
- `search_knowledge('relay Compton radius D_K spectrum dictionary lift ...')` → **`S104-W4-2-TYPEIV-EMT-BRIDGE-SPEC` INFO**, `n_unpinned=1; unpinned=localized-relay_acoustic-flow_profile_v(r)`, carry-forward `CF-S105-RELAY-VR-CONSTRUCTION`. **DECISIVE**: confirms the `r ↔ D_K-spectrum` correspondence is the explicitly-UNPINNED item and **no canonical lift exists** — so the `alternative_if_canonical_lift_found` clause does NOT fire; the gate executes under the plan's PINNED CHOICE (`LIFT=SPECTRAL-RADIUS-DICTIONARY`).
- All four Input-SHA pins re-verified at runtime: `canonical_constants e6829db0…` OK, `s105_typeiv e2860d57…` OK, `s106_w3_2_envelope a8efd183…` OK, `s84_L12_cache 9e6d9cf7…` OK. No drift → INFO/PRE-REG-INC (input-drift branch) NOT triggered.

**Results**

**Output 4-tuple**: `(value=res(L=10)=2.941453e-01, scheme=FW, convention=ABSOLUTE-LIFT=SPECTRAL-RADIUS-DICTIONARY, L_max=10)`. Dual-SHA: `audit_sha256=2ce93202f248e290e978e6c08211124be9cb3ad53c97f4da54ff1d1f7828e290` (over [script, canonical, pinmap = the 4 input SHAs]), `content_sha256=959aee120997879eef36cb21fe5c4c33bb795cff6c8f5b83bb44624b9ef4c680` (over [script]). Full 64-char, computed from the input-pin map. Companion row `# regulator_pin=a_2^{zeta}` + lift-convention disclosure row emitted.

**NUMBERS (first).** The magnitude channel `M(L) = Tr_{M₂(ℂ)}(P_a₂·T^{(IV)})|_L = nambu_factor · norm · Σ_{k≤L} |λ_k|^{−2s} · [Γ_sub(|λ_k|/|λ|_min)/g_ext]`, s = pole_in_s = 3, nambu_factor = `Tr_{ℂ²}(P_a₂)` = 1.0 (rank-1 minimal central projection; GPU-verified on a 128×128 dense block AND numpy), `g_M = 2776.165389`:

| L | n_sectors (p+q≤L) | bare a₂ moment Z(L) = Σ\|λ\|⁻⁶ | M(L) | res(L) = \|M(L)−g_M\|/\|g_M\| |
|:--|:------------------|:------------------------------|:-----|:------------------------------|
| 8  | 44 | 382.9836 | 1774.0457 | 3.609726e-01 |
| 10 | 65 | 410.4103 | 1959.5694 | **2.941453e-01** ← binding anchor |
| 12 | 90 | 430.5653 | 2095.9052 | 2.450359e-01 |

- **res(L=10) = 2.941453e-01** (the binding-inequality anchor).
- **alpha_fit = −0.954042** (slope of log res(L) vs log L over {8,10,12}; least-squares).
- **C_1 sign = −1** (DIAGNOSTIC; `delta_L10 = M(L=10) − g_M = −816.595954 < 0`): the **§VII.AF.1-negative fork** — M approaches g_M from below. REPORTED, not chained; the 50/50 dual_prior is NOT re-allocated by this FAIL.
- Spectral-radius dictionary domain: `|λ|/|λ|_min ∈ [1.000, 6.611]` at L=12 (`|λ|_min = 0.81974111`).

**GATE (second).** Direction-neutral on C_1. Both pre-registered sub-criteria FAIL, INDEPENDENTLY:
- **PRIMARY (binding inequality, Claim A):** `res(L=10) = 0.2941 < 1e-3` → **FALSE** (res is ~294× ABOVE the binding Level-2 envelope, not below).
- **SECONDARY (FLOWING signature, Claim B):** `alpha_fit = −0.954`; the gate requires `alpha_fit < 0 AND |alpha_fit| ∈ [2.0, 4.0]` → **FALSE** (|−0.954| = 0.954 < 2.0; M flows toward g_M but at ~L⁻¹, far slower than the L⁻³ envelope rate).

Composite: **FAIL** (PRIMARY FALSE ∧ SECONDARY FALSE).

**Substitution chains (as executed; per `math-scripts.md §"Double-Check Logic Before Compute"`).**

*Claim A (binding-inequality direction):* res is a magnitude `|·| ≥ 0`; PASS_A ⇔ `res(L=10) < Level2(L=10)` ⇔ `|M(L=10) − 2776.165389|/2776.165389 < 0.001` ⇔ `M(L=10) ∈ (2773.389, 2778.941)`. Substituting the computed `M(L=10) = 1959.569`: `1959.569 ∉ (2773.389, 2778.941)` (it is 816.6 below the lower edge). PASS_A **FALSE**. The inequality direction is fixed by res being a distance (NOT by any predicted sign of M − g_M) — consistent with the plan's Claim A.

*Claim B (FLOWING-signature direction):* PASS_B ⇔ `alpha_fit < 0 AND |alpha_fit| ∈ [2.0,4.0]` ⇔ `alpha_fit ∈ [−4.0, −2.0]`. Substituting `alpha_fit = −0.954`: `−0.954 ∉ [−4.0, −2.0]` (DECREASING — the sign IS correct, alpha < 0 — but `|alpha| = 0.954` is below the band floor 2.0). PASS_B **FALSE**. Note: M is NOT multiplicative-normalization-FLAT (alpha ≠ 0, so it is not the same defect the sign channel carries); it flows, but at the WRONG rate.

*C_1 sign (NON-CHAINED — diagnostic only):* `C1_sign = sign(M(L=10) − g_M) = sign(−816.596) = −1`. REPORTED, never pre-registered as a direction. Per `epistemic-discipline.md §"Dual-prior pre-registration"`, the §VII.AF.1-negative / §VII.AU-positive opposite-sign siblings on the identical (d=4,s=3) structure prove the C_1 sign is observable-specific; writing a chain that asserts it would be a Class-8.2 PRU smuggle. No posterior re-narrativization.

**DST-T-3 lift convention (as executed).** `LIFT=SPECTRAL-RADIUS-DICTIONARY` (the plan-freeze PINNED CHOICE; NO canonical lift found — `S104-W4-2` confirms the `r ↔ D_K-spectrum` dictionary is the unpinned item, so the `alternative_if_canonical_lift_found` clause does NOT fire). `r ↔ |λ|/|λ|_min`; `Γ̂_sub = diag_k[Γ_sub(|λ_k|/|λ|_min)] ⊗ 1_{ℂ²}` on `H^{≤L} ⊗ ℂ²`; `P_a₂` = rank-1 minimal central projection on the Nambu ℂ² block. The L=8/10/12 truncations are obtained by FILTERING the L=12 master cache (`s84_spectrum_cache_L12_tau019.npz`) at `p+q ≤ L` (Peter-Weyl block-diagonal superset truncation; `math-scripts.md §"D_K Block-Diagonality"`) — deterministic, mutually consistent by construction, no `get_irrep` reconstruction needed.

**Lift-robustness / declare-diagnostic check (the FAIL is NOT lift-dependent — this is why it is FAIL, not INFO/PRE-REG-INC).** A structural feature of the pinned dictionary: `r = |λ|/|λ|_min ≥ 1` for ALL modes (every eigenvalue magnitude ≥ the minimum), so `Γ_sub(|λ_k|/|λ|_min)` samples ONLY the exterior branch `r ≥ 1` — the type-IV core (`r < 1`, `g_core < 0`, the ANEC-violating acoustic-white-hole interior) is structurally NEVER reached by D1. I tested two alternative dictionaries that DO reach the core (D2: `r = |λ|_min/|λ| ∈ [0.151, 1]`, core-only; D3: `r = |λ|/median ∈ [0.21, 1.42]`, band-centered). **All three FAIL both sub-criteria:** res(L=10) = 0.294 (D1), 1.885 (D2), 2.207 (D3) — all ≫ 1e-3; |alpha_fit| = 0.954 (D1), 0.241 (D2), 0.016 (D3) — all far below the [2,4] band (D2/D3 even DIVERGE, alpha > 0). The verdict does not flip with the lift ⇒ the FAIL is robust ⇒ the gate genuinely closes the magnitude-binding question; the INFO_meaning (lift-dependent / structurally-untestable) branch does NOT apply.

**Substrate-IS assessment (the structural reason for the FAIL).** The continuum target `g_M = a_2_FW_zeta = 2776.165389` is the **ζ-regularized** a₂ value — the analytic continuation / full zeta sum of `D_K²` at the curvature-degree-2 grade — NOT the limit of the truncated partial sum `Σ_{k≤L} |λ_k|^{−2s}`. The finite-L partial moment Z(L) at L=8–12 is ~383–431 (Richardson limit ~632 with its OWN exponent p≈0.52), roughly **4–7× below g_M**. The a₂ zeta value lives in the analytic-continuation / high-mode tail that the L≤12 partial sum structurally cannot reach at the L⁻³ envelope rate. This is robust to (i) the lift dictionary choice, (ii) the normalization reading, and (iii) holds even for the bare lift-trivial moment.

Per `phononic-framing.md §"IS Space, Not IN Space"`, the direction is preserved: the substrate IS the finite-L type-IV core EMT `(A_K, H_K, D_K(τ_fold))`; its a₂ moment `M(L)` is the substrate-IS observable; `g_M` is the continuum HKR image (the laboratory-IN container quantity). The explanation flows `D_K eigenvalues → Γ_sub lifted to the spectral triple → M(L) → HKR L→∞ map → g_M`. This gate measured how fast the substrate-IS `M(L)` reaches its OWN HKR image and found it does NOT do so within the binding L⁻³ envelope at L_max=10. The FAIL is a **constraint-map update**, not an agent failure: it confirms that **§VII.AU's finite-L under-performance is a GENERIC (d=4,s=3) phenomenon that reaches §VII.CB** — the topology→analysis over-reach boundary (Level-1 cohomology-class identity holds and is regulator-invariant; the Level-2/3 finite-L *numerical* binding is the rung that fails). The Level-1 identity `[T^{(IV)}]_{a₂,HKR} = [g_M]_{a₂,HKR}` and the §VII.CB theorem-STRUCTURE (STAGE-3-PERMANENT at S106) are UNAFFECTED — what FAILs is the finite-L numerical anchor against the binding envelope on the magnitude channel.

**Solution-space consequence.** The §VII.CB Level-3 row STAYS HELD `NOT-SATISFIED-PENDING-MAGNITUDE-CONVERGENCE-ANCHOR`; §VII.CB does NOT earn full REGISTRY-PASS this session. Routed to `CF-S108-VIICB-MAGNITUDE-REMEDIATION` (the magnitude channel re-tests under a different lift convention OR a higher-L mesh {12,14,16} to determine whether convergence is merely slow-but-eventual — though the substrate-IS finding above suggests the partial-sum vs zeta-sum gap is structural, not a slow-convergence artifact, which the S108 remediation should test directly). No `mack-cosmic-bridge` HELD → SATISFIED promotion (that fires only on PASS). The C_1 sign diagnostic (§VII.AF.1-negative fork) is recorded here.

## Wave 1 Synthesis (team-lead)

**Verdict: FAIL (robust, direction-neutral).** `S107-VIICB-MAGNITUDE-CONVERGENCE-ANCHOR` measured the §VII.CB magnitude channel `M(L)=Tr_{M₂(ℂ)}(P_a₂·T^{(IV)})|_L` against the binding L⁻³ Level-2 envelope and found it does NOT bind: `res(L=10)=0.2941` (~294× above the 1e-3 envelope; PRIMARY FALSE) and `alpha_fit=−0.954` (flows toward g_M but at ~L⁻¹, far below the [2,4] FLOWING band; SECONDARY FALSE). The FAIL is lift-robust — all three dictionaries tested (exterior-only D1, core-only D2, band-centered D3) FAIL both sub-criteria — so this is a genuine gate closure, NOT a lift-dependent INFO. C_1 sign = −1 (§VII.AF.1-negative fork; diagnostic, not chained; dual-prior left at 50/50).

**Structural reason (substrate-IS).** `g_M = a_2_FW_zeta = 2776.165389` is the **ζ-regularized** a₂ (analytic-continuation / full-zeta value), not the limit of the truncated partial sum (Z(L)≈383–431 at L≤12, Richardson limit ~632 — 4–7× below g_M). The a₂ zeta value lives in the analytic-continuation tail the L≤12 partial sum cannot reach at the L⁻³ rate. This is the topology→analysis over-reach boundary: the Level-1 cohomology-class identity `[T^{(IV)}]_{a₂,HKR}=[g_M]_{a₂,HKR}` is regulator-invariant and UNAFFECTED; only the finite-L *numerical* anchor on the magnitude channel fails. **§VII.AU's finite-L under-performance is confirmed a GENERIC (d=4,s=3) phenomenon reaching §VII.CB.**

## Carry-Forward Computations (MATH ONLY — propagate to S108)

### CF-S108-VIICB-MAGNITUDE-REMEDIATION
1. **What**: re-test the §VII.CB magnitude channel binding — does `res(L=10)<1e-3` hold under (a) a different DST-T-3 lift convention that reaches the type-IV core, OR (b) a higher-L mesh {12,14,16}; AND decide whether the partial-sum↔ζ-sum gap is structural (a Richardson/Abel-sum reconstruction of the ζ-regularized a₂ from the truncated moment) rather than a slow-convergence artifact.
2. **Inputs**: this gate's `res_of_L`/`alpha_fit` series (`s107_viicb_magnitude_convergence_anchor.npz`); the S105 type-IV npz `e2860d57…`; the S106 W3-2 binding-envelope npz `a8efd183…`; `a_2_FW_zeta`; an alternative-lift convention OR the {14,16} spectra (recursive Casimir `get_irrep`, feasibility-pre-checked per `math-scripts.md §"D_K Block-Diagonality"`).
3. **Gate**: `res(L=10)<1e-3` under the alternative lift, OR a demonstrated L-trend converging below 1e-3, OR a Richardson/Abel reconstruction of g_M from the partial moments to <1e-3 (PASS → §VII.CB Level-3 HELD→SATISFIED, full REGISTRY-PASS); else the structural-gap reading is confirmed (the partial-sum channel cannot reach the ζ-value — §VII.CB Level-3 permanently held on this channel, route to a ζ-native Level-3 observable).
4. **Effort**: ~1.0 wave.

## Constraint-Map Updates

- **§VII.CB Level-3 row STAYS HELD** `NOT-SATISFIED-PENDING-MAGNITUDE-CONVERGENCE-ANCHOR`; §VII.CB does NOT earn full REGISTRY-PASS at S107. The §VII.CB theorem-STRUCTURE (STAGE-3-PERMANENT, S106) + the Level-1 identity are untouched.
- The **(d=4,s=3) finite-L topology→analysis over-reach boundary is sharpened**: §VII.AU's under-performance is not a one-off — the type-IV a₂ magnitude channel (§VII.CB) lands on the same side (§VII.AF.1-negative C_1 fork, but slow-flow that still misses the envelope). Partial-sum vs ζ-sum is the diagnosed mechanism.
- No `mack-cosmic-bridge` HELD→SATISFIED promotion (fires only on PASS).

## Effected In-Session (NON-MATH)

- [x] §VII.CB master-index held-tag pointer (Level-3 HELD + the S107-FAIL keeps-it-held note) — routed to `mack-cosmic-bridge` sole-writer session-close pass (S106 standing-hygiene item c; `s107-close-mack`). Verified at close.
- [x] C_1 diagnostic (§VII.AF.1-negative fork) recorded in §W1-1 Results — no dual-prior re-allocation (FAIL does not select a track).

## Files Produced

- `computations/session-107/s107_viicb_magnitude_convergence_anchor.py`
- `computations/session-107/s107_viicb_magnitude_convergence_anchor.npz`
- `computations/session-107/s107_viicb_magnitude_convergence_anchor.png`
- `computations/session-107/s107_gate_verdicts.txt` (line 15 — canonical + dual-SHA companion + `# regulator_pin=a_2^{zeta}` + lift-convention rows)
- `sessions/session-107/session-107-w1-workingpaper.md` (§W1-1)
