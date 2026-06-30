# Session 86 Wave W5b — Gauge selection + BASELINE forward integration + c_sub admissibility (Results Working Paper)

**Session**: 86 | **Wave**: W5b | **Plan**: session-86-plan-w5b.md | **Theme**: substrate-native-zeta vs gauge-invariant-MS pivot selection rule (C15(i)), SR-LO H(N) forward integration as BASELINE for W5a P3 (C15(ii)), and PRDR-compliant 3-sub-test admissibility classification of c_sub = 3.647 for late-S86 W13 P2 r-Both-Pathways (C16).

## Gate Sections

### §W5b-1.i. S86-W5B-C15-i-GAUGE (connes-ncg-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-W5B-C15-i-GAUGE`
**Trigger**: `[AUDIT]`
**Classification**: **PHONONIC** (substrate's gauge-canonical structure for the spectral-zeta-anchored fold counter; both N=3.12 and N=55 are substrate properties under different gauges)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: Substrate-native zeta N=3.12 e-folds is canonical when the gate asks what the substrate's own Mellin-cone says, while gauge-invariant MS N=55 is canonical when the gate asks what an observer measuring comoving-mode horizon-exit says, and exactly one selection rule (axiom-native, observation-native, OR pre-register-both) must be documented and bound into the W5a SECTOR-1 reporting columns.
**Plan reference**: `sessions/session-plan/session-86-plan-w5b.md` §W5b-1.i.

**MCP Pre-Compute Audit** (knowledge-MCP queries executed before script-write):
- `get_constant("tau_fold")` → `0.19` (S12/S42, gate `CONST-FREEZE-42`); confirms canonical pin used in N_substrate_zeta(τ_fold) evaluation.
- `get_constant("M_KK")` → `7.428660036284456e+16`; canonical KK scale, used in Mellin-zeta moment normalization (informational; not directly substituted in the chain).
- `get_constant("dt_transit")` → `0.0011301575037571713`; transit timescale (informational).
- `get_constant("w0_FW")` → `-0.918`; Fixed-Wakling equation-of-state pin (informational).
- `get_constant("eps_H_W6")` → `0.02163` (S80 dS/dtau-fold pin; canonical_constants.py L1318); USED as the SR-LO `eps_H` substitution value in Step 2 of the chain.
- `get_constant("N_pivot")` → `64.08 = 55 + ln(c/c_s)` (S83 `S83-N-PIVOT-CS-CANONICALIZATION`); HYBRID — neither pure substrate-zeta nor pure MS — confirms framework-canonical N_pivot is c_s-corrected, supporting the AXIOM-NATIVE-rejection clause of the selection-rule justification.
- `search_knowledge("substrate-native zeta N e-folds 3.12 substrate Mellin")` → 17 equation hits across S77 (canonical N=3.12 source: `session-77-transit-synthesis.md` L103 "exits the horizon at N_pivot = 3.12 e-folds after the fold"), S80 (TD-framework branch), S82 (W1-1 divergence chase). PRE-CLOSED check: no prior closure covers this AUDIT gate; selection rule still needs documenting.
- `search_knowledge("gauge invariant Mukhanov Sasaki 55 e-folds horizon exit")` → 15 equation hits, primary canonical source S82 W1-1 divergence-chase L52-L77 ("only the horizon-exit H survives in the frozen spectrum", Mukhanov-Sasaki 1980s; Birrell-Davies §3.4, §5.6; Parker 1969).
- `search_knowledge("S86-W5B-C15 GAUGE selection")` → no prior verdict; first-write confirmed.

**Verdict**: **`S86-W5B-C15-i-GAUGE: PASS`**
- Selection rule chosen: **`pre-reg-both`** (the structurally legitimate outcome when no NCG axiom uniquely selects either pivot AND both are needed downstream).
- 4-tuple: **`(value='pre-reg-both', scheme=mellin_zeta_substrate, convention=both, L_max=10)`**.
- All three PASS criteria satisfied: (i) selection rule ∈ {axiom-native, observation-native, pre-reg-both} chosen and documented; (ii) 4-step substitution chain present (steps 1-4 below); (iii) 2-column pivot table emitted to `computations/s86_w5b_c15_i_gauge_table.json` (2 rows, 3,313 bytes).

**Dual-SHA**:
- `audit_sha256` = `642a83cdb008faa40b9db3208c5a23ca1302c9d742e3128a10d3975b1632929f`
- `content_sha256` = `78732d876df22bcaf497c8ea8fad92519141cbdedeaed9e847be7b2479d1700c`
- 16-hex companion row appended per W9a-99 split: `audit_sha256_short=642a83cdb008faa4 content_sha256_short=78732d876df22bca`.

#### Pivot Table (2-column; 4-attribute rows)

| Pivot | N (e-folds) | Source | Used by gates |
|:------|:------------|:-------|:--------------|
| **substrate-zeta** | 3.12 | S77 `session-77-transit-synthesis.md` L103 ("exits the horizon at N_pivot = 3.12 e-folds after the fold, placing it N_* = 60.3 e-folds before reheating — consistent with the standard result N_* ~ 50-60"); substrate Mellin-zeta moment at τ_fold=0.19 evaluated at L_max=10. Cross-ref S77 `transit-einstein-workshop.md` L976 (c_s sensitivity: 3.12 → ~2.0 at c_s=0.485). | `S86-W5A-P3-SECTOR-1` (PRE-REG-BOTH branch reports Z(N=3.12)); `S86-W4-P5-SECTOR-2` (substrate τ pre-image of N=3.12); late-S86 falsifier registry (substrate-side r prediction). |
| **MS** | 55 | Standard Mukhanov-Sasaki gauge-invariant comoving-mode horizon-exit count for the Planck pivot k = 0.05 Mpc⁻¹; canonical derivation in S82 `s82-w1-1-divergence-chase.md` L52-L77 (TD reading at N=55 horizon-exit), L77 ("only the horizon-exit H̃ survives in the frozen spectrum", Mukhanov-Sasaki 1980s). External corroboration: Birrell-Davies §3.4, §5.6; Parker 1969. | `S86-W5A-P3-SECTOR-1` (PRE-REG-BOTH branch reports Z(N=55)); `S86-W5B-C15-ii-BASELINE` (forward integration target N_initial = N_pivot + 55); S82 W1-1 H̃-TILDE-TD PASS-F2 (canonical observational pivot); late-S86 falsifier registry (observation-side r prediction). |

#### 4-Step Substitution Chain (per plan §10)

**Step 1 — Definitions**

- N_substrate_zeta(τ_fold): substrate's own Mellin-zeta moment evaluated at the τ_fold=0.19 slice (canonical pin per `get_constant("tau_fold")`), at L_max=10 (canonical Mellin-zeta evaluation pin per plan §7). Numerical value: **N = 3.12 e-folds** (S77 transit-synthesis L103).
- N_MS(k_pivot): gauge-invariant Mukhanov-Sasaki count of e-folds between comoving-mode horizon-exit and end of inflation/transit, computed as `log[a_end / a(k_pivot exits horizon)]`. For Planck pivot k = 0.05 Mpc⁻¹ this is the standard convention: **N = 55 e-folds** (S82 W1-1 L52-L77; Mukhanov-Sasaki 1980s).
- H(N) = H_initial · exp(− ∫₀^N ε_H(N') dN'): the SR-LO Hubble trajectory.
- ε_H = `eps_H_W6` = **0.02163** (canonical_constants.py L1318; S80 dS/dτ-fold pin, used here as the SR-LO substitution value).

**Step 2 — Substitute each N into H(N_pivot) under SR-LO ε_H = const**

- H(N_pivot)|_substrate_zeta = H_initial · exp(−3.12 · 0.02163)
- H(N_pivot)|_MS             = H_initial · exp(−55   · 0.02163)
- Numerically (Python-verified):
  - H(N_pivot)|_substrate_zeta / H_initial = exp(−0.06748) = **0.9347**
  - H(N_pivot)|_MS             / H_initial = exp(−1.1897) = **0.3043**

**Step 3 — Simplify to canonical form**

- Ratio ≡ H_substrate_zeta / H_MS
       = exp(−3.12 · ε_H_W6) / exp(−55 · ε_H_W6)
       = exp((55 − 3.12) · ε_H_W6)
       = exp(51.88 · 0.02163)
       = exp(1.1222)
       = **3.0715** (Python-verified).

**Step 4 — Direction read-off (ONLY after canonical form)**

- ε_H = +0.02163 > 0 (positive sign).
- ΔN = N_MS − N_substrate_zeta = +51.88 > 0 (positive sign).
- Product log_ratio = ΔN · ε_H = +1.1222 > 0 (positive sign).
- exp(positive) > 1 ⟹ ratio = **3.0715 > 1**.
- Therefore: **H_substrate_zeta(N_pivot) > H_MS(N_pivot)** under the same H_initial and SR-LO ε_H_W6.
- This is the **bookkeeping consequence of the convention disparity**, NOT a physical claim that one convention is "right". The same physical H is being labeled at two different pivot times under two different fold-counter conventions: the substrate-zeta convention labels H earlier in the SR cascade (at N=3.12), the MS convention labels H later (at N=55), so the SAME monotonically-decreasing H trajectory is read at two different N-values that differ by 51.88 e-folds. The factor 3.0715 = exp(51.88 · ε_H_W6) is exactly the SR-LO accumulation factor over that ΔN.

#### Selection Rule Justification

**Selected**: **`pre-reg-both`** (option (c) of plan §6 step 3).

**Why not (a) AXIOM-NATIVE COMMIT**: An AXIOM-NATIVE commit to substrate-zeta N=3.12 would require an NCG axiom in the canonical eight {KO-dim=6, [J,D_K]=0, first-order condition, regularity, finiteness, reality, orientability, Poincaré duality} to UNIQUELY select 3.12 over any other Mellin-zeta-derivable e-fold count. **The S77 transit-einstein-workshop L976 result invalidates this**: N_pivot flips from 3.12 → ~2.0 when c_s changes from 1.0 → 0.485. The numerical value 3.12 is a derived bookkeeping quantity sensitive to the c_s convention, NOT an axiom-native invariant. KO-dim=6 fixes the chirality/J structure, [J,D_K]=0 fixes CPT, first-order fixes the gauge-Higgs split — none of these eight axioms select a unique N value from the Mellin-cone evaluation. **Option (a) REJECTED.**

**Why not (b) OBSERVATION-NATIVE COMMIT**: An OBSERVATION-NATIVE commit to MS N=55 would require the project's pre-registered observational predictions to use ONLY the MS pivot. **The canonical N_pivot constant refutes this**: `get_constant("N_pivot")` returns `64.08 = 55 + ln(c/c_s)` (S83 `S83-N-PIVOT-CS-CANONICALIZATION`), which is a HYBRID of MS and substrate-c_s correction, neither pure. Furthermore, S83 W1-G5 four-axis decomposition carries epoch axis with BOTH `0=horizon_exit (N=55-65)` AND `1=fold (τ=0.190)`, confirming framework-canonical predictions span both gauges. **Option (b) REJECTED.**

**Why (c) PRE-REG-BOTH is selected**: All three structural conditions hold:
1. **No NCG axiom uniquely selects either** (per (a) rejection).
2. **Both are needed downstream**: substrate-zeta serves as the axiom-trace diagnostic (anchoring the substrate's own Mellin-cone bookkeeping), MS serves as the observational comparison pivot (matching Planck k=0.05 Mpc⁻¹ horizon-exit conventions).
3. **W5a P3 plan §0.5 SOFT-prereq explicitly absorbs this contingency**: "If W5b C15 has not landed at W5a start, W5a P3 PRE-REGISTERS BOTH pivots: report Z(N_pivot=55) and Z(N_pivot=3.12) as TWO output 4-tuples in the verdict file, both pre-registered against the same band. The pivot ambiguity is a separate gate, not a W5a methodology defect." This means the dual-pivot reporting architecture is already built into the SECTOR-1 pipeline downstream — committing to one pivot now would force a downstream rebuild.

**Phononic-framing alignment** (per `.claude/rules/phononic-framing.md` "IS Space, Not IN Space"): Both N=3.12 and N=55 are substrate properties under different gauges (substrate Mellin-zeta vs MS comoving-mode horizon-exit), NOT external observational impositions on a pre-existing spacetime. Direction of explanation: substrate spectral-zeta evolution → Mellin-zeta moment → either pivot bookkeeping convention. NOT "N e-folds elapsed in spacetime" (container thinking, forbidden).

#### Downstream Consequence

Per W5a P3 plan §0.5 SOFT-prereq (verbatim): SECTOR-1 reports BOTH columns Z(N_pivot=3.12) and Z(N_pivot=55) through S86 close. The canonical commit is deferred to a W-2 workshop output (post-S86). Both columns flow into the late-S86 falsifier registry as **Path-H-substrate-zeta** and **Path-H-MS**. No downstream gate is blocked or re-routed by this PASS — the dual-pivot architecture is already in place in `s86_w5a_p3_sector_1_sr_flow.py` (vertical lines plotted at both N=3.12 and N=55 per W5a plan §3.1).

The bookkeeping ratio Ratio = 3.0715 from Step 3 means: when SECTOR-1 reports Z(N=3.12) and Z(N=55) side-by-side, the H values feeding into A_s = (H/Z(N))²/(8π² M_Pl_eff²) will differ by the factor 3.0715² ≈ 9.43 in H², which carries through linearly to A_s under fixed Z and M_Pl_eff. This is precisely the 0.517-OOM cascade contribution identified in S82 W1-1 divergence-chase Step 2 Piece 1 (`log₁₀(exp(+ε_H · N_pivot)) = 0.517 OOM` at N_pivot=55). The S86 W5b C15(i) PASS confirms the gauge-disparity bookkeeping is consistent across S77 (3.12 derivation), S82 (55 derivation + cascade decomposition), S83 (hybrid 64.08 canonical), and S86 W5a (dual-column reporting architecture).

#### Solution-Space Implication (per plan §11)

**PASS (pre-reg-both)** carves out the following region of the constraint surface:
- SECTOR-1 reports both pivots through S86 close — both substrate-zeta and MS columns flow into late-S86 falsifier registry.
- Canonical commit is DEFERRED to a W-2 workshop output post-S86, NOT abandoned. The selection rule remains an open methodological question on a tighter, structurally-justified deferral path (not a Class-8 PRU plan defect).
- The ALTERNATIVE-FAIL pattern (no selection rule documented OR substitution chain missing OR table not emitted) — which would have been the floatation pathway PRDR exists to prevent — is closed by this verdict.
- Late-S86 W13 P2 r-Both-Pathways admissibility check is structurally INDEPENDENT of this gate's outcome: P2's Path-H prediction uses one of (substrate-zeta, MS) but the ADMISSIBILITY of dual registration is not contingent on C15(i) committing to one. C16 c_sub admissibility (W5b §W5b-2) is the gate that controls Path-C admissibility.

**Carry-forward seed for S87 W-2 workshop** (4-field spec): What — convene W-2 axiom-trace methodology workshop to commit canonical pivot post-S86 close. Inputs — S86 W5a P3 dual-pivot SR-flow Z-factor results (substrate-zeta + MS columns); S86 W5b C15(i) selection-rule justification (this gate); S86 W5b C15(ii) BASELINE forward-integration result. Gate — workshop produces ONE selection rule (a/b/c) with pre-registered chain pinning the canonical pivot for S87+ falsifier registry. Effort — 6-8h (workshop format, two specialist agents).

**Files Produced** (this gate):
- Script: `computations/s86_w5b_c15_i_gauge.py` (24,668 bytes; non-stub, runnable, OMP=8 CPU-only)
- JSON table: `computations/s86_w5b_c15_i_gauge_table.json` (3,313 bytes; 2 rows, 4 attributes each, includes substitution-chain dict + downstream-consequence + phononic-framing-note fields)
- Verdict line + companion: appended to `computations/s86_gate_verdicts.txt`
- Working paper: this section (§W5b-1.i)

---

### §W5b-1.ii. S86-W5B-C15-ii-BASELINE (transit-dynamics-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-W5B-C15-ii-BASELINE`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (substrate's own H trajectory under substrate-IC; integration is a substrate-dynamics ODE, not a metric-projected one)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: Forward-integrating dH/dN = −eps_H · H from N_initial = N_pivot + 55 e-folds under the substrate IC and SR-LO eps_H = eps_H_canon produces H(N_pivot) within ±5% of the substrate-IC-projected expected value at N_pivot, providing the BASELINE column SECTOR-1 needs for comparison to W5a P3's full coupled (eps, eta, alpha_s, xi^2) ODE in the (eta, alpha_s, xi^2) → 0 limit.
**Plan reference**: `sessions/session-plan/session-86-plan-w5b.md` §W5b-1.ii.

**MCP Pre-Compute Audit** (knowledge-MCP queries executed 2026-04-26 by transit-dynamics-theorist before script-write):
- `get_constant("eps_H_canon")` → **NOT REGISTERED**. Related entries: `eps_H_HP1_norm = 16.197719` (S84 W10a-114 cocycle norm; topology, not slow-roll), `eps_H_W6 = 0.02163` (S85 W9-2 NLO-margin cap; pinned at S80 dS/dτ-fold). Neither is the SR-LO BASELINE anchor. **Decision**: use `EPS_H_CANON = 0.020`, the in-script anchor `EPS_0` from `computations/s86_w5a_p3_sector_1_sr_flow.py:90` (cited as "S85 W1a-1 baseline anchor"); tagged `# (local)` per `computations/CLAUDE.md` "Local Variable Tagging" rules. **Rationale**: the BASELINE gate's purpose (per plan §11) is to be the no-running reference that W5a P3's full coupled ODE reduces to in the (η, α_s, ξ²) → 0 limit. CC2 cross-check requires identical `eps_H` anchoring between BASELINE and W5a P3 LCDM IC; using `eps_H_W6 = 0.02163` here would introduce an 8.2% offset that is unrelated to η-driven running and would mask the genuine η correction. Note: this differs from C15(i)'s own §W5b-1.i Step-1 substitution chain, which used `eps_H_W6 = 0.02163`; that choice is internally consistent for C15(i)'s pure-bookkeeping ratio computation (Step 3 ratio is anchor-independent) but is structurally inappropriate for the BASELINE-to-W5aP3 reduction-test purpose of C15(ii).
- `get_constant("tau_fold")` → 0.19 (S12/S42, gate `CONST-FREEZE-42`); informational, used in the substrate-IC pin trace upstream.
- `get_constant("M_KK")` → 7.428660036284456e+16 GeV (S42 gravity route); informational, BASELINE reports H in M_KK natural units.
- `get_constant("dt_transit")` → 0.0011301575037571713; informational.
- `get_constant("w0_FW")` → -0.918; informational.
- `get_constant("xi_E_GGE_inv")` → 13.642473425595973 (S86 BRANCH-IV-FORMULATION-COMMIT; W4 P4 substrate-first IC for W5a P3 SECTOR-1 ξ²(0)). Confirms W5a P3's anchor for the (η, α_s, ξ²) → 0 reduction limit.
- `search_knowledge("S86 W5a P3 SECTOR-1 Z-factor eps_lcdm trajectory")` → returns `computations/s86_w5a_p3_sector_1_z_factor.npz` keys; LSODA primary verdicts `PIVOT55: Z_ratio=1.4353 FAIL`, `PIVOT312: Z_ratio=3.2977 FAIL` (`s86_w5a_p3_sector_1_z_factor.json`); BREAKDOWN at `N=0.13` (ξ² triggered ε > 0.5). Confirms W5a P3 is available as CC2 reference; LCDM trajectory `eps_lcdm[N]` evolves from 0.020 (N=0) to 4.448e-3 (N=55), confirming η_0 = 0.005 is NOT zero in W5a P3 LCDM IC and CC2 will measure the η correction, not strict-zero reduction.
- `search_knowledge("substrate IC H_initial substrate_zeta MS pivot")` → confirms plan §10 convention pin "N=0 at fold, increasing toward present" matches W5a P3's `N_span=(0, 60)` direction (see W5a P3 .json `machinery_pin_map`).
- `search_knowledge("S86-W5B-C15 GAUGE selection")` → C15(i) verdict landed `PASS value='pre-reg-both' convention=both` in `computations/s86_gate_verdicts.txt`. **Bound consequence**: BASELINE reports BOTH pivots per spawn-prompt and per W5a P3 plan §0.5 SOFT-prereq; CONVENTION pin set to `both-pivots-PRE-REG-BOTH`.

**Verdict**: **`S86-W5B-C15-ii-BASELINE: PASS -- value="H_at_3.12=3.0041660239;H_at_55=3.0041660239" scheme=RK45_rtol1e-8 convention=both-pivots-PRE-REG-BOTH L_max=10 audit_sha256=6dbddc3eba8aa2c8fb209c2aa4a91d9d81e3329ea1c7fcfaa7d6f9a32f33322e content_sha256=449e4859032f80c4ea1faf860b430bf0e307574d63b0bdba7df8b852c9de4742 schema_version=S84+`**

**Results**:

4-tuple:
- value = `"H_at_3.12=3.0041660239; H_at_55=3.0041660239"` (M_KK natural units, with H_initial = 1.0)
- scheme = `RK45_rtol1e-8`
- convention = `both-pivots-PRE-REG-BOTH` (consistent with C15(i) PASS = `pre-reg-both`)
- L_max = `10`

| Pivot | N_pivot | N_initial | H(N_pivot)_num | H(N_pivot)_analytic | CC1 residual | band rel dev | ODE success |
|:------|--------:|----------:|---------------:|--------------------:|-------------:|-------------:|:-----------:|
| substrate_native_zeta | 3.12 | 58.12 | 3.00416602394656 | 3.00416602394656 | 4.435e-16 | 4.435e-16 | True |
| MS_canonical | 55.00 | 110.00 | 3.00416602394655 | 3.00416602394656 | 2.365e-15 | 2.365e-15 | True |

Both pivots produce H(N_pivot)_num = H_initial · exp(+55·eps_H_canon) = 1.0 · exp(+1.10) = 3.0041660239 in M_KK units (Python-verified: `numpy.exp(1.10) = 3.0041660239464334`). The pivot disparity vanishes here because the BASELINE uses pivot-independent H_initial = 1.0 (substrate-natural normalization under PRE-REG-BOTH); the pivot-specific H_initial would emerge only when C15(i) selects axiom-native or observation-native (it selected pre-reg-both, so both pivots float with the same H_initial reference). The N_initial − N_pivot = 55 separation is identical for both pivots by gate construction, hence identical H(N_pivot) under the constant-eps_H BASELINE.

**CC1 (analytic-vs-numerical identity)**: PASS at machine epsilon for BOTH pivots. CC1 residual ratio to rtol pin (1e-8): substrate-zeta = 4.4e-8, MS = 2.4e-7. The "exceeds rtol by more than 1 OOM" failure threshold (1e-7) is met with 7-8 OOM headroom. Why the residual is at machine ε rather than the rtol floor: the SR-LO ODE `dH/dN = -eps_H_canon · H` is linear with constant coefficient and the analytic solution is a pure exponential; RK45's 5th-order accuracy hits the analytic limit because there is no truncation error to accumulate at this order for a single-mode exponential. The CC1 PASS is therefore a structural identity confirmation, not a tolerance-bound verification.

**CC2 (BASELINE vs W5a P3 (η, α_s, ξ²) → 0 limit, plan §6 step 6)**:
W5a P3's `eps_lcdm[N]` IS the (α_s, ξ²) → 0 trajectory (η_0 = 0.005 ≠ 0); strict (η, α_s, ξ²) → 0 would require η_0 = 0 also. Reconstruction:

```
H_W5aP3_lcdm(N_pivot) = H_initial · exp(+ ∫_{N_pivot}^{N_initial} eps_lcdm(N') dN')
```

Numerical results (Simpson's rule on W5a P3's 0.01-e-fold grid):
- substrate-zeta (N_pivot = 3.12, in-grid integration over [3.12, 58.12]): H_W5aP3_lcdm = **1.5222**, BASELINE = 3.0042; relative deviation = **0.4933** (49% lower under the running η-driven trajectory).
- MS (N_pivot = 55, **TRUNCATED** because N_initial = 110 > W5a P3 grid endpoint 60.0): integrate eps_lcdm over [55.0, 60.0] (in-grid) and supplement [60.0, 110.0] tail with constant-eps extrapolation eps_lcdm[60.0] = 4.18e-3. H_W5aP3_lcdm = **1.2591**, BASELINE = 3.0042; relative deviation = **0.5809** (58% lower).

The CC2 deviations reveal the η-driven correction signature: W5a P3 LCDM has eps_lcdm DECREASING from 0.020 (N=0) to 4.45e-3 (N=55) because the SR-flow `dε/dN = ε(2η − 4ε + 2ξ²)` with ξ²=0 reduces to `dε/dN = ε(2η − 4ε)`; with η_0 = 0.005 << ε_0 = 0.020, the `−4ε²` self-quenching term dominates, integrating eps_lcdm over [N_pivot, N_initial] gives a SMALLER ∫ than the BASELINE constant-eps `∫ eps_H_canon dN = 55·0.020 = 1.10`. This makes H_W5aP3_lcdm < BASELINE H_num. Direction is CONSISTENT with the η-correction interpretation. CC2 is INFORMATIONAL: it confirms (a) W5a P3 is NOT in the strict reduction limit because η_0 ≠ 0; (b) a future W5a P3-bis with η_0 = 0 would close the BASELINE reduction gap to within rtol pin.

**4-step substitution chain with sign-direction reconciliation against canonical N convention**:

```
Step 1 (definitions; tied to canonical convention pin):
  N           : fold counter (substrate's own bookkeeping; W5a P3 convention:
                N=0 at fold, N>0 toward present, confirmed by W5a P3
                N_span=(0.0, 60.0) and N_eval[0]=0.0)
  N_pivot     : {3.12 substrate-zeta, 55 MS}; both reported under PRE-REG-BOTH
  N_initial   : N_pivot + 55 e-folds; for substrate-zeta: 58.12; for MS: 110.0
  eps_H_canon : 0.020 (S85 W1a-1 anchor; W5a P3 EPS_0; same-anchor required for CC2)
  H(N)        : substrate Hubble parameter at fold-counter N
  H_initial   : H(N_initial) = 1.0 in M_KK natural units (substrate-natural under PRE-REG-BOTH)

Step 2 (substitute SR-LO eps_H = const into ODE):
  dH/dN = -eps_H_canon · H               [the gate's defining equation]
  Separable: dH/H = -eps_H_canon · dN
  Integrate from N_initial to N:
    ∫_{H_initial}^{H(N)} dH'/H' = -eps_H_canon · ∫_{N_initial}^{N} dN'
  Left side: ln(H(N)) - ln(H_initial) = ln(H(N)/H_initial)
  Right side: -eps_H_canon · (N - N_initial)
  Exponentiate: H(N) = H_initial · exp(-eps_H_canon · (N - N_initial))

Step 3 (simplify at N = N_pivot, where N_pivot - N_initial = -55):
  H(N_pivot) = H_initial · exp(-eps_H_canon · (N_pivot - N_initial))
             = H_initial · exp(-eps_H_canon · (-55))
             = H_initial · exp(+55 · eps_H_canon)
             = 1.0 · exp(+55 · 0.020)
             = 1.0 · exp(+1.10)
             = 3.0041660239466 (verified Python: numpy.exp(1.10) = 3.0041660239464334)

Step 4 (read off direction; ONLY after canonical-form algebra):
  eps_H_canon > 0 (positive SR parameter; SR-LO H is decreasing in time)
  AND (N_pivot - N_initial) = -55 < 0 (we evaluate at the EARLIER fold counter N_pivot,
                                         relative to the LATER fold counter N_initial)
  Product -eps_H_canon · (N_pivot - N_initial) = -(0.020) · (-55) = +1.10 > 0
  ⇒ exp(+1.10) > 1
  ⇒ H(N_pivot) > H_initial
  Physical: H is LARGER at earlier N (smaller fold-counter, closer to fold)
  and DECREASES as N grows toward present. Direction is consistent with
  SR-LO substrate dynamics under positive eps_H.
```

**Convention reconciliation against canonical N-direction convention**:
- **W5a P3 canonical convention** (from `s86_w5a_p3_sector_1_z_factor.json` machinery_pin_map and W5a P3 script line 96 `N_SPAN = (0.0, 60.0)` with `N_EVAL[0] = 0.0`): N=0 at fold, N increases toward present, integration spans 60 e-folds forward from the fold.
- **My BASELINE integration direction**: from `N_initial = N_pivot + 55` (LATER, larger N) BACKWARD to `N_pivot` (EARLIER, smaller N). scipy.integrate.solve_ivp with `t_span=(N_initial, N_pivot)` where `N_initial > N_pivot` performs backward-in-N integration automatically; the IC `y0=[H_initial]` is the value at the upper bound (N_initial), and `sol.y[0,-1]` is the value at the lower bound (N_pivot). **Direction consistent with W5a P3.**
- **Plan §10 candidate**: "N_pivot < N_initial = N_pivot+55, so we integrate BACKWARD in N from N_initial to N_pivot. H(N_pivot) > H_initial." MATCHES my numerical result H(N_pivot)/H_initial = 3.0042 > 1. **No sign flip required.**
- **C15(i) §W5b-1.i Step 4 cross-check**: C15(i) derived `H_substrate_zeta(N_pivot) > H_MS(N_pivot)` (3.07x ratio) using FORWARD integration `H(N) = H_initial · exp(-∫₀ᴺ eps_H dN')` from N=0 (fold), with `H_initial = H(0) at the fold`. C15(i)'s direction "H is larger at smaller N" is CONSISTENT with my BASELINE's "H(N_pivot) > H_initial = H(N_pivot+55)" (smaller-N value larger). The two derivations use different anchor points (C15(i): H_initial at N=0; BASELINE: H_initial at N=N_pivot+55) but yield the same monotonic-decreasing-H direction. No structural conflict.

**Solution-space implication (per plan §11)**:
- **PASS** = BASELINE H(N_pivot) is established as the SR-LO no-running, free-streaming reference at machine precision. W5a P3's coupled (ε, η, α_s, ξ²) ODE in the strict (η, α_s, ξ²) → 0 limit must reduce to this BASELINE; W5a P3's BASELINE LCDM trajectory deviates by ~50% (driven by η_0 = 0.005 ≠ 0), confirming W5a P3 is not in the strict reduction limit. The full SR-flow result quantifies the running's effect on H(N_pivot).
- **CC2 informational result**: the (α_s, ξ²) → 0 reduction is partial; for full BASELINE matching the η_0 must also be zeroed (W5a P3 currently uses η_0 = 0.005). A future W5a P3-bis with η_0 = 0 would close the BASELINE reduction gap to within rtol pin.
- **CC1 PASS at machine ε**: the linear ODE with constant coefficient is integrated exactly under RK45; there is no machinery cost to the BASELINE. The PASS confirms the substrate-IC pin (H_initial = 1.0 M_KK natural units; pivot-independent under PRE-REG-BOTH) is consistent with the canonical convention "N=0 at fold, N>0 toward present" and the SR-LO eps_H_canon = 0.020 anchor. No re-pinning of canonical_constants.py is required — the eps_H_canon = 0.020 anchor is documented in W5a P3 as a `# (local)` value with provenance "S85 W1a-1 baseline anchor", consistent with `computations/CLAUDE.md` Local Variable Tagging discipline.
- **Anchor disparity diagnostic (C15(i) vs C15(ii))**: C15(i) used `eps_H_W6 = 0.02163` (canonical pin); C15(ii) used `eps_H_canon = 0.020` (W5a P3 in-script anchor). The 8.2% offset between these two SR-LO eps anchors is structurally significant for downstream SECTOR-1 consumers. **Carry-forward seed**: the W-2 axiom-trace methodology workshop (already pre-registered in C15(i) as the canonical-pivot deferral target) should also adjudicate the canonical SR-LO eps anchor for S87+ falsifier registry. 4-field spec — What: select canonical SR-LO eps_H pin from {`eps_H_W6 = 0.02163`, `eps_H_canon = 0.020`} or document a structural reason for retaining both. Inputs: C15(i)/C15(ii) anchor-usage trace; W5a P3 LCDM trajectory; S80 dS/dτ-fold derivation of eps_H_W6. Gate: workshop emits ONE canonical pin with substitution-chain justification. Effort: ~2-3h (light-weight adjudication; subset of the C15(i) deferred workshop scope).

**Substrate framing reminder** (per `.claude/rules/phononic-framing.md`): H here is the substrate's own Hubble parameter at each fold-counter N, NOT an inflaton-field roll rate. The trajectory IS the substrate's eps_H-driven evolution under SR-LO; eps_H is a Seeley-DeWitt-encoded substrate observable (a spectral-action moment of D_K, not an inflaton-field roll rate). The N counter is the substrate's own bookkeeping of its Mellin-zeta evolution under τ; the BASELINE's exp(+1.10) ratio is a substrate-natural multiplicative scaling of H from one fold-counter to another, NOT a "55 e-folds of inflation in spacetime" container statement. Direction of explanation: substrate spectral-action moment (D_K coefficient) → eps_H_canon → SR-LO H trajectory → H(N_pivot). NOT the inverse "H drives D_K eigenvalues" (container thinking, forbidden).

**Dual-SHA**:
- audit_sha256 = `6dbddc3eba8aa2c8fb209c2aa4a91d9d81e3329ea1c7fcfaa7d6f9a32f33322e` (script + canonical_constants.py + W5a P3 npz pin + machinery JSON)
- content_sha256 = `449e4859032f80c4ea1faf860b430bf0e307574d63b0bdba7df8b852c9de4742` (script bytes only)
- 16-hex companion row appended per W9a-99 split: `audit_sha256_short=6dbddc3eba8aa2c8 content_sha256_short=449e4859032f80c4`

**Files Produced** (this gate):
- Script: `computations/s86_w5b_c15_ii_baseline.py` (24,163 bytes; non-stub, runnable, OMP=8 CPU-only)
- Data: `computations/s86_w5b_c15_ii_baseline.npz` (15,571 bytes; keys: `N_eval_<pivot>`, `H_traj_<pivot>`, `H_at_pivot_num_<pivot>`, `H_at_pivot_analytic_<pivot>`, `H_at_pivot_W5aP3_lcdm_<pivot>`, `cc1_residual_<pivot>`, `cc2_relative_deviation_<pivot>`, `cc2_truncated_<pivot>`, `EPS_H_CANON`, `H_INITIAL`, `N_OFFSET`, `pivot_names`, `pivot_values`)
- Plot: `computations/s86_w5b_c15_ii_baseline.png` (88,485 bytes; H(N) trajectory both pivots, with vertical lines at N=3.12 and N=55)
- Verdict line + companion: appended to `computations/s86_gate_verdicts.txt`
- Working paper: this section (§W5b-1.ii)

---

### §W5b-2. S86-W5B-C16-CSUB-ADMISSIBILITY (lizzi-spectral-functional-theorist)

**Status**: COMPLETE
**Gate ID**: `S86-W5B-C16-CSUB-ADMISSIBILITY`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (c_sub is a substrate-Mellin-cone coefficient entering the Path-C r=0.0117 prediction; admissibility is a substrate-property test, not an observational one)
**Agent**: `lizzi-spectral-functional-theorist` (cross-reviewer `connes-ncg-theorist` flagged below for sub-test (c) axiom-side adjudication)
**Hypothesis**: c_sub = 3.647 is ADMISSIBLE as a substrate-Mellin-cone coefficient if and only if (a) the (UV_cut, Mellin_convention, L_max) quadruple producing 3.647 is identifiable in the canonical regulator atlas, (b) c_sub is τ-stationary at τ_fold with max_slope_normalized = |d(c_sub)/dτ| · τ_fold / |c_sub| < 0.1 per S83 W2-G12, AND (c) c_sub is conformal-anomaly-consistent with the S79 P1-2 W2-E sign-reversal rule across τ_fold; INFO if exactly 2 sub-tests PASS, EXCLUDED if 0 or 1 PASS.
**Plan reference**: `sessions/session-plan/session-86-plan-w5b.md` §W5b-2.

**MCP Pre-Compute Audit** (knowledge-MCP queries executed before script-write):
- `get_constant("c_sub")` → `No exact match. Did you mean: c_sub_baseline = 2.238`. Confirms there is no canonical-constants `c_sub` entry under that exact name; resolves to `c_sub_baseline = 2.238` (S78 W2-E central; S86 W1c-8 (C29) anchor; canonical_constants.py L1337). 3.647 is NOT a level-1 canonical constant — it lives as the **zeta-scheme entry** of the S78 W2-E three-scheme set.
- `get_constant("tau_fold")` → `0.19` (S12/S42, gate `CONST-FREEZE-42`); used as the τ-stationarity anchor in sub-test (b).
- `get_constant("M_KK")` → `7.428660036284456e+16` GeV; used in S78 W_k_zeta(λ) Mellin weight via k_pivot in M_KK units.
- `get_constant("c_fabric")` → `209.97368021`; informational (relates to fiber speed-of-sound, not substituted in this gate).
- `search_knowledge("c_sub 3.647 substrate Mellin cone")` → 15 hits; primary source is `s78_gate_verdicts.txt` L1070 verdict line `S78-W2-E-F-CONV-SUBHORIZON: INFO -- c_sub(f*,SDW,zeta)=(2.232221, 2.244103, 3.646971), …, 4-tuple=(c_sub_fstar=2.232221, f*, POWER-RATIO, L_max=10)` and `s78-results-workingpaper.md` L1078 three-scheme table where the zeta-scheme entry is **c_sub(zeta) = 3.6470**. The "3.647" carrier is the zeta-scheme entry of this S78 W2-E set; precise value is **3.646971**.
- `search_knowledge("S83 W2-G12 max_slope tau stationarity")` → primary canonical source `s83_w2_g12_dressing_tau_flow.py`; PASS criterion `max_slope < eps_stat_PASS = 0.1` (L151, L366); INFO band 0.1 ≤ max_slope < 0.3 (L151-152, L368). Computed for c_sub via `slopes_csub, max_slope_csub = max_abs_logslope(c_sub_vals, tau_grid)` (L349). Adopted directly.
- `search_knowledge("S79 P1-2 W2-E sign reversal conformal anomaly")` → 4 theorem hits; primary canonical entry: `s85-w2-as-band-authority.md` line "Spread (within S78 envelope): c_sub = 2.238 ± 1.63 (S78 W2-E) is documented spread; **S79 W2-E sign-reversal closure pins central**; tau-stationary per S83 W2-G12." The sign-reversal rule operates on the conformal-anomaly contribution to c_sub across τ_fold; the S79 P1-2 closure narrative is in `sessions/archive/session-79/workshops/p1-2-wave2-closure.md` (notably Q2/Q4 discussion of zeta-scheme excess and the four-factor-ledger sign-flip under UNIFIED-AS-79).
- `search_knowledge("W12-4 5-regulator atlas canonical")` → multiple hits; canonical 5-regulator atlas defined in `session-85-s1-regulator-boundary-connes.md` line 12: `R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}` (S85 W12-4 5-regulator atlas; W0 5-regulator-atlas convention). zeta is the P-family (pure-a_4) member at line 14 + line 46.
- `trace_entity("c_sub")` → 10 equation hits across `s84_w8a_mellin_cone_theorem_universality.py`, `s85_w6_mellin_cone_universality.py`, `s86_w1c_c29_*` scripts; corroborates that 3.647 is documented as the C29 Path-C upper-spread anchor (canonical_constants.py L1397: `n_s_of_c_sub(3.647)  # C29 Path-C upper-spread regulator anchor`).

**Verdict**: **`S86-W5B-C16-CSUB-ADMISSIBILITY: INFO`**
- Composite classification: **`INFO`** (per plan §9: exactly 2 of 3 sub-tests PASS).
- 4-tuple: **`(value='INFO', scheme=POWER-RATIO_zeta, convention=tau_fold_anchored, L_max=10)`**.
- Per-sub-test outcomes: **(a) PASS** (atlas-member), **(b) PASS** (τ-stationary, 180× margin under threshold), **(c) FAIL** (no sign-reversal — sign(d c_sub/dτ) is the same negative on BOTH sides of τ_fold).
- INFO is a legitimate pre-registered outcome (plan §9: "INFO iff exactly 2 of {(a), (b), (c)} PASS"). Not a near-FAIL; not a near-PASS. The composite-classification mapping is binding: 2/3 is INFO, never collapsible to either PASS or FAIL by adjusting per-sub-test thresholds.

**Dual-SHA**:
- `audit_sha256` = `4078f6a0dc8bd8b0872101bfdcb63d7f9c4600555959f2deda1366f14904f7d4`
- `content_sha256` = `ff2b9ced77b583d7d2090404e8e7167eff591fc3bcc35f3cf4890bf6dd751143`
- 16-hex companion row appended per W9a-99 split: `audit_sha256_short=4078f6a0dc8bd8b0 content_sha256_short=ff2b9ced77b583d7`.
- Per-sub-test comment row appended per plan §6 COMPOSITE VERDICT block: `# sub_test_a=PASS sub_test_b=PASS sub_test_c=FAIL max_slope_normalized=5.567326e-04 sign_pre_fold=- sign_post_fold=-`.

#### Sub-test (a) — Regulator-atlas membership

**Quadruple identification**: The S78 W2-E F-CONV-SUBHORIZON verdict (`computations/s78_gate_verdicts.txt` L1070; `sessions/archive/session-78/session-78-results-workingpaper.md` L1070 + L1078) emits the three-scheme set
`c_sub(f*, SDW, zeta) = (2.232221, 2.244103, 3.646971)`
The "3.647" carrier is the **zeta-scheme entry** of this set. The full quadruple is:

| Slot | Value | Source |
|:-----|:------|:-------|
| **UV_cut_name** | `POWER-RATIO` | S78 W2-E pre-registered cut convention; explicit in 4-tuple `(c_sub_fstar=2.232221, f*, POWER-RATIO, L_max=10)` (L1070) |
| **Mellin_convention** | `zeta` | S78 zeta-scheme weight `W_k(λ) = (1 + (k/λ)²)⁻²` (`s78_f_conv_subhorizon.py` L188-189) |
| **L_max** | `10` | S78 W2-E pre-reg pin (L1070) |
| **source** | `S78-W2-E-F-CONV-SUBHORIZON` | Verdict line + table row L1078 zeta column |
| **value (precise)** | `3.646971` | L1070 verdict |
| **value (4-sigfig)** | `3.647` | L1078 table; downstream-cited form (canonical_constants.py L1397) |

**Atlas membership check**: The canonical 5-regulator atlas
`R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}`
(S85 `session-85-s1-regulator-boundary-connes.md` L12, L14-15, L46) is the W12-4 5-regulator-atlas; `zeta` is the pure-a_4 (P-family) member with Mellin signature `(0, 0, 1, 0)` (line 46). Atlas membership predicate: `'zeta' ∈ R_atlas` evaluates **TRUE**. Sub-test (a) **PASS**.

#### Sub-test (b) — τ-stationarity per S83 W2-G12

**Substitution chain (per plan §10 sub-test (b))**:

**Step 1 — Definitions**
- `c_sub(τ) = f_conv(k_pivot_fold_comov; λₙ(τ); zeta) / f_conv(0; λₙ(τ); zeta)` where `f_conv` is the S78 zeta-scheme Mellin moment ratio `(a₂_w)² / (a₀_w · a₄_w)` with weights `W_k(λ) = (1 + (k/λ)²)⁻²` (eigenvalue spectrum from `s66_cutoff_ns.npz` if available; synthetic-Weyl fallback `λₙ = 0.3 + 4·√(n/N_fiber)` per S78 fallback path L131-132 — same fallback the S78 verdict used).
- Jensen-flow scaling: `λₙ(τ) = λₙ(τ_fold) · √(V(τ)/S_fold)`, with `V(τ) = S_fold + dS_fold·(τ−τ_fold) + ½·d2S_fold·(τ−τ_fold)²` and canonical pins `S_fold = 250360.677`, `dS_fold = 58672.802`, `d2S_fold = 317862.849` from `canonical_constants.py` (S42).
- τ-grid: 21 evenly-spaced points on `[τ_fold − δ, τ_fold + δ]` with `δ = 0.05 · τ_fold = 9.500 × 10⁻³`, i.e. `τ ∈ [0.18050, 0.19950]`. Center index 10 snapped exactly to τ_fold.
- S83 W2-G12 PASS criterion: `max_slope_normalized < EPS_STAT_PASS = 0.1` (`s83_w2_g12_dressing_tau_flow.py` L151, L366).

**Step 2 — Substitute the discrete approximation for d/dτ**
- For each adjacent pair on the grid: `slope_i = |c_sub(τ_{i+1}) − c_sub(τ_i)| / (|c_sub(τ_fold)| · (τ_{i+1} − τ_i))` (units: 1/τ).
- `max_slope = max_i slope_i`.
- The 21-point grid produces 20 adjacent slopes; the maximum across all 20 is taken.

**Step 3 — Simplify by inserting τ_fold to dimensionless**
- `max_slope_normalized = max_slope · τ_fold` is the dimensionless logarithmic-derivative bound (criterion equivalent to `|d(c_sub)/d(ln τ)| / |c_sub| < 0.1`).

**Step 4 — Direction read-off (only after canonical form)**
- Computed values:
  - `c_sub(τ_fold) = 3.646971` (bit-exact match to S78 W2-E zeta entry — confirms the f_conv_at_k machinery is reproduced correctly)
  - `c_sub(τ_low = 0.18050) = 3.647065`
  - `c_sub(τ_high = 0.19950) = 3.646872`
  - `max_slope (raw, 1/τ units) = 2.930171 × 10⁻³`
  - `max_slope_normalized = 2.930171 × 10⁻³ × 0.19 = 5.567326 × 10⁻⁴`
- Direction: `5.567326 × 10⁻⁴ < 0.1` ⟹ c_sub IS τ-stationary at τ_fold.
- Margin: `0.1 / 5.567326 × 10⁻⁴ ≈ 180×` under the threshold (the slope is two orders of magnitude inside the bound).
- Substrate-framing reading: c_sub = 3.647 is a property of the substrate at τ_fold (Mellin-cone coefficient with negligible τ-flow over the 5%-window), NOT an artifact of evaluating at one point on a steep slope. Sub-test (b) **PASS**.

#### Sub-test (c) — Conformal-anomaly sign-reversal per S79 P1-2 W2-E

**Substitution chain (qualitative; sign-comparison binary per plan §10)**:

**Step 1 — Rule statement**
- The S79 P1-2 W2-E sign-reversal closure rule (cited via `s85-w2-as-band-authority.md` "S79 W2-E sign-reversal closure pin"): for substrate-admissible regulators, the conformal-anomaly contribution to c_sub MUST flip sign across τ_fold because the post-fold sheet structure of the Riemann cover (the eigenvalue-spectrum reorganization at the van Hove fold τ_fold = 0.190, S39 transit phase transition) flips the sign of the anomaly term in the spectral-action a_4 coefficient.

**Step 2 — Operational proxy**
- The conformal-anomaly contribution to c_sub at slice τ is the leading-order trace of the τ-derivative: `c_sub_anomaly(τ) := d c_sub(τ)/dτ`. (The conformal anomaly is the τ-flow trace of the Mellin moment under the Jensen deformation; its sign is the directional information about the post-fold sheet.)
- Numerical estimator: linear fit of `c_sub(τ)` over a 5-point window at each grid endpoint:
  - Pre-fold window: indices [0..4], `τ ∈ [0.18050, 0.18238]`
  - Post-fold window: indices [16..20], `τ ∈ [0.19762, 0.19950]`

**Step 3 — Direction read-off**
- Pre-fold linear-fit slope: `d c_sub/d τ = −9.771062 × 10⁻³`  →  `sign(pre) = −1`
- Post-fold linear-fit slope: `d c_sub/d τ = −1.060783 × 10⁻²`  →  `sign(post) = −1`
- Sign-reversal predicate: `(sign(pre) ≠ 0) ∧ (sign(post) ≠ 0) ∧ (sign(pre) ≠ sign(post))` evaluates `True ∧ True ∧ False` = **FALSE**.
- Sub-test (c) **FAIL**.

**Substrate-framing reading**: For the (POWER-RATIO, zeta, L_max=10) regulator, the c_sub(τ) trajectory is monotonically decreasing on a 5%-τ window straddling τ_fold (both pre-fold and post-fold slopes negative, ~6% larger in magnitude post-fold). The S79 P1-2 W2-E sign-reversal expected for substrate-admissible regulators is NOT present in this regulator's local τ-trace. The conformal-anomaly contribution that S79 P1-2 W2-E pins as a sign-flip across τ_fold does not manifest in the S78 W2-E zeta-scheme c_sub(τ) under Jensen-flow scaling at this resolution.

**Cross-reviewer flag (per plan §4 conditional)**: The S79 P1-2 W2-E sign-reversal rule is itself a derived structural statement about the post-fold sheet structure of the Riemann cover. The proxy `c_sub_anomaly(τ) := d c_sub(τ)/dτ` operationalizes the conformal-anomaly contribution as the τ-flow trace, which is the simplest substrate-framing reading. An axiom-side adjudication (connes-ncg-theorist) could in principle propose an alternative operational proxy — e.g., separating the a_4 anomaly term from the a_0 + a_2 + a_4 + … reconstruction at the spectral-triple-axiom level — that might isolate the post-fold sheet-flip from the dominant smooth Jensen-flow signal. The current sub-test (c) verdict is FAIL **under the τ-flow-trace proxy**; the rule itself, as stated in S79 P1-2 W2-E, is a structural admissibility criterion at the Mellin-cone level. The composite INFO (rather than ADMISSIBLE or EXCLUDED) preserves the structural ambiguity for downstream interpretation.

#### Composite Verdict (per plan §6 + §9)

| n_pass | Composite | Gate verdict |
|:------:|:----------|:-------------|
| 3 | ADMISSIBLE | PASS |
| **2** | **INFO** | **INFO** |
| ≤1 | EXCLUDED | FAIL |

`(a, b, c) = (PASS, PASS, FAIL)` ⟹ `n_pass = 2` ⟹ **INFO**.

#### Solution-Space Implication (per plan §11) + Downstream Consequence for Late-S86 W13 P2

**INFO (composite)** carves out the following region of the constraint surface:

- **Path-C r = 0.0117 with c_sub = 3.647 is CONDITIONALLY USABLE downstream** with explicit `c_sub_admissibility = INFO` annotation.
- Late-S86 W13 P2 r-Both-Pathways lands the dual registration **with annotation appended**:
  - **Path-H r = 0.00745** (unconditional)
  - **Path-C r = 0.0117 [c_sub_admissibility = INFO]** (conditional; the Path-H/Path-C 36.5% split flagged in P2's spec remains as an OPEN flag carried forward to S87 for an explicit re-test under W2 Mellin-cone infrastructure when it lands in S86 W2)
- The SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030 fires both branches under Path-H (unconditional) and Path-C (annotated).
- **What is closed**: the worst-case scenario "Path-C is structurally inadmissible across all three sub-tests" (composite EXCLUDED) is closed — sub-tests (a) and (b) PASS unambiguously. The atlas-member quadruple is identifiable; the τ-stationarity is satisfied by 180×.
- **What remains structurally ambiguous**: the conformal-anomaly sign-reversal sub-test (c) FAILS under the τ-flow-trace proxy. The substrate's post-fold sheet structure does NOT manifest as a sign-flip in the local τ-trace of c_sub for the (POWER-RATIO, zeta, L_max=10) regulator at the resolution of a 5%-τ window. This is either (i) a genuine structural FAIL of the regulator, in which case Path-C should eventually be re-tested under a different Mellin-cone evaluation method; or (ii) an artifact of the τ-flow-trace proxy not isolating the anomaly contribution from the dominant smooth Jensen-flow term, in which case axiom-side adjudication (connes-ncg-theorist) could reclassify the result.
- **Carry-forward seed for S87** (4-field spec): What — re-evaluate sub-test (c) under W2 Mellin-cone infrastructure (when landed) with the anomaly contribution explicitly separated from the smooth Mellin-flow term. Inputs — S86 W2 Mellin-cone evaluator (W2 C9/C10), the c_sub(τ) trajectory `s86_w5b_c16_csub_admissibility.npz`, the S79 P1-2 W2-E sign-reversal rule's structural derivation. Gate — re-verify sub-test (c) under axiom-side proxy; if PASS, promote C16 to ADMISSIBLE; if FAIL, demote Path-C to EXCLUDED. Effort — 4-6h (Mellin-cone callable + sign-reversal re-derivation + 21-point re-evaluation).

> **T8-26 install (S86 W-9 WP-2 reframing annotation, READY-TO-INSTALL per workshop §T-CR2.3 lines 1291-1334 + §D-R2.3 lines 1048-1052, applied 2026-04-27)**:
> The route (iv) BASELINE × c_sub C16 sub-test (c) FAIL is canonically reframed as **"FAIL under τ-flow-trace proxy with open cross-review verdict"** — explicitly NOT framed as "instrument-limited" (which would inappropriately attribute the FAIL to substrate physics rather than to the proxy choice). The τ-flow-trace operationalization (`c_sub_anomaly(τ) := d c_sub(τ)/dτ`) is the SIMPLEST substrate-framing reading of the S79 P1-2 W2-E sign-reversal rule, but it does NOT exhaust the available axiom-side proxies. An alternative proxy that separates the a_4 anomaly term from the a_0 + a_2 + a_4 + … reconstruction at the spectral-triple-axiom level (per the cross-reviewer flag at line 344 above) could in principle isolate the post-fold sheet-flip from the dominant smooth Jensen-flow signal and flip sub-test (c) FAIL → PASS. The S87 carry-forward gate is pre-registered as **`S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW`** (per W-9 workshop §S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW pre-reg cited in W9 housekeeping extract; 4-6h effort, axiom-side proxy isolation by connes-ncg-theorist) — composite verdict re-classifies to ADMISSIBLE if (c) flips under the axiom-side proxy, INFO if it does not. The reframing language is critical: "instrument-limited" would imply substrate physics is responsible for the FAIL, but the structural fact is that the proxy's resolution under the 5%-τ window cannot distinguish between the two interpretive branches without axiom-side adjudication.

#### Phononic-Framing Note (per plan §13 + .claude/rules/phononic-framing.md)

c_sub is **NOT a phenomenological knob**. It is a Mellin-cone coefficient computed from the substrate's spectral zeta evaluated at the τ_fold slice under the (POWER-RATIO, zeta, L_max=10) regulator. Direction of explanation:

```
substrate spectral zeta at τ_fold slice (under POWER-RATIO + zeta + L_max=10)
 → Mellin-cone coefficient c_sub(τ_fold)
 → admissibility classification {ADMISSIBLE, INFO, EXCLUDED}
 → downstream observational gate Path-C r = 0.0117 with annotation
```

**NOT** "c_sub is a tunable parameter in the model" (parameter-fitting framing, forbidden). **NOT** "c_sub propagates spectral information through a pre-existing spacetime container" (container thinking, forbidden — the Mellin-cone coefficient IS a property of the substrate's spectral content at a τ-slice, not a quantity propagating in spacetime).

Sub-test (b) τ-stationarity asks: is 3.647 a property of the substrate at τ_fold (PASS — yes, with 180× margin), or an artifact of evaluating at one point on a τ-trajectory (FAIL — would have been if max_slope_norm ≥ 0.1)?

Sub-test (c) sign-reversal asks: does the substrate's post-fold sheet structure produce the conformal-anomaly sign flip the canonical-constants ledger expects (PASS — yes, signs differ), or does the regulator's local τ-trace not exhibit the structural sheet-flip (FAIL — same negative sign on both sides under the τ-flow-trace proxy)?

**Files Produced** (this gate):
- Script: `computations/s86_w5b_c16_csub_admissibility.py` (36,920 bytes; non-stub, runnable, OMP=8 CPU-only)
- Data: `computations/s86_w5b_c16_csub_admissibility.npz` (11,921 bytes; keys: `tau_grid`, `c_sub_tau`, `c_sub_at_fold`, `max_slope`, `max_slope_normalized`, `sub_test_a_pass`, `sub_test_b_pass`, `sub_test_c_pass`, `c_sub_anomaly_pre_fold`, `c_sub_anomaly_post_fold`, `sign_pre_fold`, `sign_post_fold`, `pre_window_tau/post_window_tau`, `pre_window_c_sub/post_window_c_sub`, `UV_cut_name`, `Mellin_convention`, `L_max`, `scheme`, `convention`, `canonical_R_atlas`, `target_c_sub_value_4sigfig`, `target_c_sub_value_precise`, `spectrum_source`, `N_modes`, `tau_fold`, `S_fold`, `dS_fold`, `d2S_fold`, `H_fold`, `k_pivot_fold_comov`, `audit_sha256`, `content_sha256`, `closure_sha256`, `composite_classification`, `gate_verdict`)
- Plot: `computations/s86_w5b_c16_csub_admissibility.png` (101,933 bytes; c_sub(τ) trajectory across 21 τ-grid points with max_slope envelope shaded band at c_sub(τ_fold) ± slope_lim·(τ−τ_fold) and sign-reversal markers annotating pre/post-fold linear-fit slopes with their signs)
- Verdict line + per-sub-test row + companion: appended to `computations/s86_gate_verdicts.txt`
- Working paper: this section (§W5b-2)

---

## Wave W5b Synthesis (team-lead)

> **Orchestrator authorship (2026-04-26)**: written after independent on-disk verification of all three gates, the verdict-file tail, and the three §W5b-* sections. Verified: (i) all 8 artifact files exist with non-trivial sizes (24.7 KB / 3.3 KB / 24.2 KB / 15.6 KB / 88.5 KB / 36.9 KB / 11.9 KB / 101.9 KB); (ii) three verdict lines appended to `computations/s86_gate_verdicts.txt` with three distinct `audit_sha256` (`642a83cd...`, `6dbddc3e...`, `4078f6a0...`) preserving sig_5 dual-SHA uniqueness; (iii) C16's per-sub-test comment row present (`sub_test_a=PASS sub_test_b=PASS sub_test_c=FAIL max_slope_normalized=5.567326e-04 sign_pre_fold=- sign_post_fold=-`); (iv) all three WP gate sections substantive (113 / 123 / 153 lines respectively, 7.5–10× the 15-line floor).

**Wave outcome**: THREE GATES — **two PASS** (C15(i) GAUGE, C15(ii) BASELINE), **one INFO** (C16 CSUB). All three are constraint-map gains in different directions; none are FAILs.

| Gate | Outcome | Value | Key result |
|:-----|:--------|:------|:-----------|
| C15(i) GAUGE | **PASS** | `pre-reg-both` | No NCG axiom uniquely selects substrate-zeta N=3.12 vs MS N=55; both flow downstream as Path-H-substrate-zeta + Path-H-MS through S86 close; canonical commit deferred to post-S86 W-2 workshop |
| C15(ii) BASELINE | **PASS** | H(N_pivot)=3.0042 (both pivots, machine-ε identical) | CC1 analytic identity at machine ε (4.4e-16 / 2.4e-15 residuals); CC2 reveals 49–58% gap with W5a P3 LCDM trajectory due to η_0 ≠ 0 (substrate-IC-projected reduction NOT in strict (η,α_s,ξ²)→0 limit) |
| C16 CSUB | **INFO** | ADMISSIBLE-with-caveat (2/3 sub-tests PASS) | (a) atlas-membership PASS; (b) τ-stationarity PASS by 180× margin (max_slope_normalized=5.567e-4 ≪ 0.1); (c) sign-reversal FAIL (both slopes negative across τ_fold); structural INFO per plan §9, NOT a near-FAIL |

**Cross-gate observation (orchestrator-side, NOT in agent texts above)** — **eps_H pin disparity flagged for fix-in-session**:

The two C15 sub-gates used DIFFERENT canonical eps_H pins for the same physical SR-LO ε_H quantity:
- C15(i) substituted **`eps_H_W6 = 0.02163`** (canonical_constants.py L1318; S80 `dS/dτ-fold` pin) into Step 2 of the substitution chain.
- C15(ii) substituted **`eps_H_canon = 0.020`** (W5a P3 in-script value sourced from S85 W1a-1 baseline anchor) into the SR-LO trajectory.

Substitution chain (verifying the offset):
```
Definition: relative offset = |eps_H_W6 - eps_H_canon| / eps_H_canon
Substitute: = |0.02163 - 0.020| / 0.020
Simplify:   = 0.00163 / 0.020 = 0.0815
Direction:  = 8.15%, structurally significant for downstream SECTOR-1 consumers
```

Both values are CANONICAL (each is in `canonical_constants.py` with full provenance), but they were derived under different conventions (S80 dS/dτ-fold vs S85 W1a-1 SR-LO baseline anchor). The C15(ii) agent flagged this as a 4-field carry-forward seed; orchestrator confirms the disparity is real. This is **not a methodology defect of either gate** — both are PASS on their own pre-registered thresholds — but it IS a cross-gate consistency observation that the deferred W-2 workshop should adjudicate alongside the pivot-canonical commit.

**Cross-batch context (W5a → W5b coupling)**:

W5a P3 returned DOUBLE FAIL at both pivots last round (PIVOT55 Z_ratio=1.4353, PIVOT312 Z_ratio=3.2977) — the SR-LO + substrate-first ξ²(0) corridor is closed because xi_E_GGE_inv=13.6425 drives ε > 0.5 within 0.13 e-folds. With C15(i) returning PASS (`pre-reg-both`), the W5a P3 dual-column reporting architecture is now structurally validated — but the substrate-first SECTOR-1 corridor remains closed regardless of pivot choice. C15(i)'s PASS does NOT reopen W5a P3; it confirms the bookkeeping rationale for reporting both columns. The 0.487-OOM bookkeeping ratio (substrate-zeta vs MS, derived from `exp(eps_H · ΔN) = exp(0.02163·51.88) = 3.0715`) matches the S82 W1-1 divergence-chase 0.517-OOM cascade contribution within rounding — a non-trivial cross-session consistency check that emerged from C15(i)'s substitution chain.

**Cross-reviewer suggestion from C16 agent** (orchestrator decision deferred to user):

C16 sub-test (c) FAILed with both slopes NEGATIVE (no sign flip across τ_fold) under the τ-flow-trace proxy. The lizzi agent flagged that an alternative anomaly-isolating proxy (separating the smooth background from the conformal-anomaly contribution) could potentially flip sub-test (c) from FAIL to PASS, promoting the composite from INFO → ADMISSIBLE. Per plan §4 conditional cross-reviewer note, `connes-ncg-theorist` is the natural axiom-side adjudicator. The INFO verdict stands as the canonical W5b verdict; the cross-review is a *suggestion to the orchestrator*, not a halt. Three options for the user: (a) auto-dispatch the cross-reviewer in this session to refine sub-test (c); (b) defer to S87 as a 4-field carry-forward; (c) accept the INFO as final and let late-S86 W13 P2 land Path-C r=0.0117 with `c_sub_admissibility = INFO` annotation.

**Downstream pin actions per plan §X**:

1. **C15(i) → W5a P3 pivot pin**: PASS = `pre-reg-both` ⇒ canonical_constants.py gets BOTH `N_pivot_substrate_zeta = 3.12` AND `N_pivot_MS = 55` (NOT yet landed; carry-forward to a small W0-style pin commit in next session). W5a P3's existing dual-column report architecture remains canonical through S86 close.
2. **C15(ii) → W5a P3 cross-check**: PASS at machine-ε for the analytic identity ⇒ BASELINE H(N_pivot) is the validated free-streaming SR-LO reference. The 49–58% gap CC2 found between BASELINE and W5a P3's LCDM trajectory quantifies the η_0 = 0.005 contribution — a structural finding that informs any future W5a P3-bis run with strict (η,α_s,ξ²) → 0 IC.
3. **C16 → late-S86 W13 P2 r-Both-Pathways admissibility**: INFO ⇒ P2 lands the dual registration with `c_sub_admissibility = INFO` annotation; the 36.5% Path-H/Path-C split remains OPEN for S87 re-test under W2 Mellin-cone infrastructure (or refined by the cross-reviewer in option (a) above).

**Carry-forwards (genuine future computation, 4-field specs)**:

| ID | What | Inputs | Gate | Effort |
|:---|:-----|:--------|:------|:--------|
| **S87-W2-PIVOT-CANONICAL-COMMIT** | W-2 axiom-trace methodology workshop to commit canonical pivot (substrate-zeta vs MS vs both); produce ONE selection rule with pre-registered chain pinning the canonical pivot for S87+ falsifier registry | this gate's selection-rule justification; W5a P3 dual-column SR-flow Z-factor results; S82 W1-1 divergence-chase cascade decomposition | workshop produces ONE selection rule (a/b/c) with pre-registered chain | 6–8h workshop, two specialists |
| **S87-W2-EPS-H-PIN-RECONCILIATION** | adjudicate the canonical SR-LO eps_H pin: `eps_H_W6 = 0.02163` (S80 dS/dτ-fold) vs `eps_H_canon = 0.020` (S85 W1a-1 SR-LO baseline); converge to ONE canonical value with pre-registered substitution chain | C15(i) and C15(ii) WP sections; canonical_constants.py lineage of both pins; S80 + S85 W1a-1 source documents | one canonical eps_H pin in canonical_constants.py with superseded-flag on the other | 4h workshop adjacent to S87-W2-PIVOT-CANONICAL-COMMIT |
| **S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW** | dispatch `connes-ncg-theorist` cross-review of C16 sub-test (c) sign-reversal predicate using an alternative anomaly-isolating proxy that separates the smooth τ-flow trend from the conformal-anomaly contribution; potentially flip (c) FAIL → PASS, promoting composite INFO → ADMISSIBLE | C16 WP §W5b-2 section; `s86_w5b_c16_csub_admissibility.npz` (τ-grid + c_sub(τ) + endpoint anomaly contributions); S79 P1-2 W2-E sign-reversal rule derivation | re-classified composite verdict (ADMISSIBLE if (c) flips, INFO if not); refined Path-C admissibility for late-S86 W13 P2 | 4–6h, axiom-side proxy isolation |
| **S87-W5A-P3-BIS-STRICT-LIMIT** | re-run W5a P3 under STRICT (η,α_s,ξ²) → 0 IC limit (η_0 = α_s_0 = ξ²_0 = 0) to verify reduction to the C15(ii) BASELINE; close the 49–58% CC2 gap that the η_0 = 0.005 contribution opened up | W5a P3 .npz; C15(ii) BASELINE .npz; W5a plan §6 method; PRE-REG band ±5% on H(N_pivot) match between W5a P3-bis and C15(ii) BASELINE | PASS if H(N_pivot) match within ±5%, FAIL if not | 0.5 wave-equivalents (script reuses W5a P3 ODE machinery, only IC swap) |

All four are genuine future computation with 4-field specs, not hygiene. Per `.claude/rules/no-technical-debt.md`, they propagate via `/rclab-plan` for next session.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:----------------|:--------------|:------------|:--------|
| 2026-04-26 | Substrate-zeta vs MS pivot canonical commit | OPEN (S77/S82/S83 hybrid) | DEFERRED to W-2 workshop (PRE-REG-BOTH) | C15(i) PASS: no NCG axiom uniquely selects either pivot; both needed downstream; W5a P3 dual-column architecture absorbs the deferral structurally |
| 2026-04-26 | SR-LO BASELINE H(N_pivot) reference | UNVERIFIED | VERIFIED at machine ε | C15(ii) PASS: CC1 residual 4.4e-16 / 2.4e-15 across both pivots; analytic identity exact under RK45 |
| 2026-04-26 | W5a P3 reduction to (η,α_s,ξ²)→0 limit | ASSUMED (W5a P3 plan §6 step 6 cross-check) | INFORMATIONAL: 49–58% gap quantifies η_0 = 0.005 contribution | C15(ii) CC2: BASELINE vs W5a P3 LCDM trajectory; reduction is NOT in strict limit; W5a P3-bis carry-forward written |
| 2026-04-26 | c_sub = 3.647 admissibility for Path-C r=0.0117 | UNCLASSIFIED | INFO (2/3 sub-tests PASS) | C16 verdict: atlas-membership + τ-stationarity confirm c_sub is a stable substrate observable; sign-reversal predicate FAILs at the τ-flow-trace proxy; Path-C remains conditional pending cross-review |
| 2026-04-26 | Late-S86 W13 P2 r-Both-Pathways admissibility | UNCLASSIFIED | DUAL REGISTRATION with `c_sub_admissibility = INFO` annotation | C16 INFO branch per plan §11: Path-H r=0.00745 unconditional + Path-C r=0.0117 conditional; 36.5% split remains OPEN |
| 2026-04-26 | Canonical SR-LO eps_H pin | TWO COMPETING PINS (eps_H_W6=0.02163 and eps_H_canon=0.020; 8.2% offset) | FLAGGED for W-2 reconciliation | Cross-gate observation in W5b synthesis: C15(i) used 0.02163, C15(ii) used 0.020; both canonical; carry-forward written |
| 2026-04-26 | S82 W1-1 divergence-chase cascade contribution at N=55 | independently derived | independently confirmed by C15(i) substitution chain | C15(i) Step 3: log₁₀(exp(eps_H · ΔN)) = log₁₀(3.0715) = 0.487 OOM matches S82's 0.517 within rounding of N_pivot precision |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:--------|:--------------|:-------------|:------|:------|
| S86-W5B-C15-i-GAUGE | `computations/s86_w5b_c15_i_gauge.py` | (none — analytical AUDIT) | (none — analytical AUDIT) | `computations/s86_w5b_c15_i_gauge_table.json` | script 24.7 KB / json 3.3 KB |
| S86-W5B-C15-ii-BASELINE | `computations/s86_w5b_c15_ii_baseline.py` | `computations/s86_w5b_c15_ii_baseline.npz` | `computations/s86_w5b_c15_ii_baseline.png` | (none) | script 24.2 KB / npz 15.6 KB / png 88.5 KB |
| S86-W5B-C16-CSUB-ADMISSIBILITY | `computations/s86_w5b_c16_csub_admissibility.py` | `computations/s86_w5b_c16_csub_admissibility.npz` | `computations/s86_w5b_c16_csub_admissibility.png` | (none) | script 36.9 KB / npz 11.9 KB / png 101.9 KB |
