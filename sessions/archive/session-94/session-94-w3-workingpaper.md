# Session 94 Wave 3 — Pati-Salam SU(4)_PS Level-3 + module-as-canonical K3 + §VII.AZ re-extraction (Results Working Paper)

**Session**: 94 | **Wave**: W3 | **Plan**: session-94-plan-w3.md | **Theme**: heavy SU(4)_PS-feasibility wave — discharge the three numerical/corpus carry-forwards downstream of the S93 W6 Pati-Salam structural work: the full SU(4)_PS Level-3 spectral-action anchor (Route-A sparse-Lanczos OR Route-B Friedrich-Bär saturation), the corpus §19 weighting-functional-family K-counter advancement (module-as-canonical K3), and the §VII.AZ band-admissible HH¹ exponent re-extraction. Every observable is GEOMETRIC — a spectral functional of the Jensen-deformed Dirac operator on the finite Pati-Salam (or SU(3)) spectral triple.

## Gate Sections

### §W3-9. S94-VII-PS-FULL-SPECTRUM-LEVEL-3 (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-PS-FULL-SPECTRUM-LEVEL-3`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (Level-3 < Level-2 directional claim; α(PS) precision-pin sub-adjudication)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The Level-3 spectral-action anchor `Res_{s=4} Tr(D_K_PS^{−2s})` on the full SU(4)_PS Peter-Weyl spectrum sits strictly inside the Level-2 algebraic envelope — satisfying the §VII.BE FWD-C4 numerical Level-3 pin AND completing the §VII.AQ.OP-PROJ full-spectrum Level-3 row — and Level-3 < Level-2 survives both the symbolic α(PS)=3 and the s=4 canonical α(PS)=4 readings.
**Plan reference**: `sessions/session-plan/session-94-plan-w3.md` §W3-9 (machinery pin, feasibility pre-check, thresholds, substitution chain, dual-slot 5-anatomy).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

All four artifacts verified on disk (content-presence; no line/byte targets):

- **script** `computations/session-94/s94_vii_ps_full_spectrum_level_3.py` (39407 B) — `grep -E 'from canonical_constants import|append_verdict|L_max_operational|eta_FB'` → matches present: `from canonical_constants import *`, `from canonical_constants import (`, `def append_verdict(...)`, `L_max_operational = 12`, `def friedrich_bar_su4(...)` / `eta_FB_SU4(a,b,c) = |lam_PS|_sector / sqrt(C2+1)`. ✓
- **data** `computations/session-94/s94_vii_ps_full_spectrum_level_3.npz` (16499 B; 55 keys) — required keys present: `L_max_plan=12`, `L_max_operational=12`, `spectrum_route=ROUTE-B-Friedrich-Bar-analytic-saturation-per-sector-no-operator-matrix`, `eta_FB_SU4_all_min=0.10181393`, `eta_FB_SU4_all_min_sector=[6 0 6]`, `eta_FB_SU4_lower_margin8pct=0.09366882`, `eta_FB_su3_floor_NOT_inherited=0.436488`, `verdict=FAIL`, `sign_verdict=PASS`, `magnitude_verdict=FAIL`, `regime_verdict=BREAKDOWN`, `s4_diverges=True`, `s_conv_threshold=4.5`, `residue_s6_Linf=9.3936e-4`, `alpha_s6_tail_envelope=2.8036`, `saturation_pass=False`, `vii_be_stage3_licensed=False`. ✓
- **plot** `computations/session-94/s94_vii_ps_full_spectrum_level_3.png` (202513 B; 4-panel: feasibility wall / residue-vs-L_max at s=4,5,6 / shell-scaling exponent 8−2s vs 3−2s / eta_FB re-derived). ✓
- **verdict line** `computations/session-94/s94_gate_verdicts.txt` — `grep -E '^S94-VII-PS-FULL-SPECTRUM-LEVEL-3:.* audit_sha256=[a-f0-9]{64}'` → matched (audit_sha256=`697fe5329797ee45583286620d621609d818013e8a2fbb5729a46ab91c6dcc81`, content_sha256=`1b00bd5eec34c9379a458837d98bd8b1800e96e2684ef6072db65d704402d64b`); dual-SHA companion row present; S87 schema-v2 3-tuple row present (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN`). audit_sha256 unique across the session verdict file (grep count = 1). ✓
- **WP section** (this section) — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. ✓

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("Pati-Salam SU(4) Level-3 spectral action residue FWD-C4")` → §VII.BE FWD-C4 STAGE-1-CANDIDATE landed S91/S92; structural Stage-2 PASS-AND on disk at S93 W6-4 (axis-A connes `146b5742…` / axis-B landau `9df77b09…`, J2 SYMBOLIC Level-3<Level-2=True). NOT pre-closed (this gate supplies the deferred NUMERICAL Level-3 anchor).
- `search_knowledge("Friedrich-Bar saturation eta_FB SU(4) Casimir bound L_max")` → S92 W9-3 unified Friedrich-Bär gate: SU(3) `eta_FB_all_min=0.436488`, `eta_FB_lower=0.40`, `NEW_sector13_bound=3.0022`, `botK_ceiling=0.8452` — the SU(3) floor I must NOT inherit (plan: re-derive on SU(4)_PS).
- `get_constant("alpha_HH1_per_pole_FW_s4")` → `4.0` (canonical s=4 envelope exponent, Wodzicki 2(s−2); S92-W7-CF-W9-10-B). Imported, not hardcoded.
- `trace_entity("S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3")` → STRUCTURAL Stage-2 PASS-AND; §VII.BE STAYS STAGE-1-CANDIDATE pending the numerical Level-3 pin (this gate).
- `list_constants("tau_fold|r_tau|M_KK|M_Pl|eta_FB")` → `M_KK=7.42866e16`, `M_Pl_reduced=2.435e18`, `tau_fold=0.19`; NO canonical `r_tau` (radial scale cancels in the dimensionless Level-3/Level-2 ratio; SU(3) `_cm_1995_residue_formula.py` uses r=1 identically).
- `search_knowledge("divergent channel Tier-2 dimensional re-anchorability pole regime breakdown Level-3")` → composite-collapse precedent S91 W4-W5-1 (`sign=PASS, mag=FAIL, regime=BREAKDOWN ⇒ composite=FAIL`); Tier-2 dimensional-re-anchorability is the registered forward route for a divergent channel.
- **Sage MCP** (exact-rational discipline): verified the SU(4) Casimir ladder `{C₂(4)=15/4, C₂(6)=5, C₂(15)=8, C₂(10)=9}` against the plan ladder (scale=1, conjugation-symmetric); proved the shell-scaling exponent `8−2s` analytically (convergence iff `s>9/2`).
- **PRE-CLOSED?** NO — the numerical Level-3 anchor was explicitly DEFERRED to this gate (S93 W6-4 route-4b). This gate computes it.

**Verdict**: **FAIL** — `value='L3_PS_s4_DIVERGES=True; …; saturation_pass=False; …; VII_BE_STAGE3_NOT_licensed_reanchor_to_s_ge_5; VII_AQ_OP_PROJ_row_completed_DIAGNOSTIC_order_one_CLOSED_route_NOT_reopened'` scheme=`FW-FRIEDRICH-BAR-SATURATION` convention=`ABSOLUTE-residue-anchor-a_n_Mellin-Element3-Bismut-Cheeger-adiabatic-limit-SU4_PS-full-spectrum-Peter-Weyl-direct-sum` L_max=`12_plan_12`. S87 schema-v2 3-tuple: **sign_verdict=PASS, magnitude_verdict=FAIL, regime_verdict=BREAKDOWN** → composite **FAIL** (regime BREAKDOWN ⇒ FAIL per the gate-verdicts.md composite-collapse rule; S91 W4-W5-1 precedent). The §VII.BE FWD-C4 numerical Level-3 pin at the inherited s=4 pole is **NOT satisfied** (the full-spectrum residue diverges); STAGE-3 promotion is **NOT licensed** (theorem stays STAGE-1-CANDIDATE with structural Stage-2 recorded). The forward route is Tier-2 dimensional re-anchorability to the convergent pole s≥5.

**Results**:

NUMBERS first, gate second, interpretation third.

**(1) 4-tuple.** `value=FAIL_s4_residue_DIVERGES`, `scheme=FW-FRIEDRICH-BAR-SATURATION` (Route-B), `convention=ABSOLUTE-residue-anchor-a_n_Mellin-Element3-Bismut-Cheeger-adiabatic-limit-SU4_PS-full-spectrum-Peter-Weyl-direct-sum`, `L_max=12_plan_12` (i.e. `L_max_operational=12`, `L_max_plan=12`; dense storage at L_max=12 = 1094.7 GB ≫ 17.1 GB VRAM = INFEASIBLE). Regulator pin: `a_n^{Mellin}` (CM-1995 §III.4 Mellin-transform residue class).

**(2) Decisive structural finding (the science).** The SU(4)_PS Mellin-cone Level-3 residue `Res_{s} Tr(D_K_PS^{−2s}) = Σ_{(a,b,c)≠0} dim_PS(a,b,c)·(C₂(a,b,c)+1)^{−s}` (the on-disk framework form, matching the S92 W9-3 `O_3` evaluator and the canonical per-pole exponent `alpha_HH1_per_pole_FW_s4`) has shell-sum scaling **`L^{8−2s}`** (Sage-exact): A₃=SU(4) has 6 positive roots ⇒ `dim_PS ~ L^6`, and there are `~L²` Peter-Weyl sectors per shell `a+b+c=L`. The total residue `Σ_L L^{8−2s}` **converges iff `8−2s < −1`, i.e. `s > 9/2 = 4.5`** (Sage `solve`).

| Pole s | shell exponent | regime | residue behavior |
|:-------|:---------------|:-------|:-----------------|
| **s=4 (literal, inherited)** | **8−2·4 = 0** | **DIVERGENT** | L=10→120: 0.05659 → 0.32630, ratio **5.77×**, successive deltas **GROWING** (4.90e-2 → 7.29e-2 → 9.68e-2) — a convergent sum would plateau |
| s=5 | 8−2·5 = −2 | convergent | 5.7222e-3 → 6.0175e-3 (plateaus) |
| s=6 | 8−2·6 = −4 | convergent | residue(L→∞) ≈ 9.393640e-4; truncation tail **L^{−2.80}** ≈ L^{−3} (§VII.AF.1 d=4 precedent) |

Contrast — the **SU(3) base** at s=4 has shell scaling `L^{3−2s} = L^{−5}` (A₂ = 3 positive roots ⇒ `dim ~ L²`, `~L` sectors/shell) and **CONVERGES**. This is *why* the SU(3) program correctly anchors its Level-3 at s=4. The rank-4 algebra's higher spectral dimension pushes the convergence threshold up by exactly one Mellin unit (`9/2` vs SU(3)'s `3/2`).

**PASS/FAIL criterion.** PASS iff `L3_PS / L2_envelope_PS < 1` (the Level-3 anchor sits strictly inside the L^{−α} envelope at canonical truncation). The pre-registered metric is the truncation residual `r(L) = |L3(L) − L3(∞)|/L3(∞)`. At the literal s=4 pole `L3(∞)` does not exist (the residue diverges); `r(L)` **GROWS** (proxy at L10→12 = 9.63e-2, and the absolute residue grows 5.77× to L=120). So `L3/L2` is unbounded, **not `< 1`** ⇒ **magnitude FAIL**. The s=4 pole is **OUT of the SU(4)_PS convergent regime** (`s > 4.5` required), breakdown fraction 100% (the sum diverges at all L_max) ⇒ **regime BREAKDOWN**. The directional claim `L^{−4} < L^{−3}` (4.823e-5 < 5.787e-4 at L=12) holds, so the SYMBOLIC `Level-3 < Level-2` inequality direction is sound *given a finite residue* ⇒ **sign PASS**. Composite-collapse (`gate-verdicts.md`): `regime == BREAKDOWN ⇒ composite = FAIL` regardless of other fields (S91 W4-W5-1 precedent). **Composite = FAIL.**

Solution-space reading: this CLOSES the corridor of pinning the §VII.BE FWD-C4 numerical Level-3 anchor at the inherited s=4 pole. The §VII.BE STAGE-3-PERMANENT promotion is **NOT licensed** (theorem stays STAGE-1-CANDIDATE; the structural Stage-2 PASS-AND on disk at S93 W6-4 — axis-A connes `146b5742…`, axis-B landau `9df77b09…`, J2 SYMBOLIC=True — is unaffected and remains recorded). The §VII.AQ.OP-PROJ full-spectrum Level-3 row is **completed with a DIAGNOSTIC finding** (the s=4 full-spectrum residue diverges); this does **NOT** reopen the §VII.AQ STAGE-3 route, which is independently CLOSED at the order-one axis (defect 4.000 ALGEBRA-INVARIANT, S93 W6-1). `mack-cosmic-bridge` lands all registry text at session-close; this gate emits only verdict + npz + WP section.

**(3) Feasibility pre-check (plan deliverable; centerpiece) + route disclosure.** Dense storage of `⊕_{(a,b,c)} D_{(a,b,c)}` at L_max=12 is 1094.7 GB ≫ 17.1 GB VRAM = INFEASIBLE. But the operative cost is **NOT diagonalization**: each Peter-Weyl sector's eigenvalue is **known analytically**, `|λ_PS(a,b,c,τ)| = √C₂(a,b,c)·exp(−τ·ρ)/r(τ)_PS` with `ρ=a+b+c` (the SU(4) analog of `_cm_1995_residue_formula.py` lines 15-17). The CM-1995 §III.4 residue at finite L_max reduces **algebraically to the direct sum over sectors** (entire in s at finite L_max), so **no operator matrix is ever formed**. Therefore **Route-A (sparse-Lanczos block-by-block) is NOT NEEDED** — the analytic per-sector form supersedes it; **Route-B (Friedrich-Bär analytic-saturation / direct per-sector summation)** is the operative route. The recursive Casimir-projection irrep *enumeration* is O(L³) trivial given the exact SU(4)=A₃ Weyl-dimension and quadratic-Casimir closed forms. `L_max_operational = 12` (the framework canonical cache ceiling for the bottom-K saturation test; analytic, no diagonalization); residue convergence characterized to L_max=120 (also analytic). `L_max_plan = 12` (dense INFEASIBLE). Honest disclosure: no `L_max_operational < L_max_plan` downgrade was needed because the analytic per-sector form removes the diagonalization wall entirely; the deviation from a literal "diagonalize at L_max=12" plan reading is in-session structural correction (Route-B), fully disclosed here and in the verdict scheme tag — NOT convention-shopping.

SU(4) Casimir ladder Sage-exact (QQ), conjugation-symmetric, matching the plan ladder with scale=1 (`C₂ = <λ,λ+2ρ>` in the long-root²=2 / index-1 normalization, fundamental **4** → 15/4): `C₂(**1**)=0, C₂(**4**)=C₂(**4̄**)=15/4, C₂(**6**)=5, C₂(**15**)=8, C₂(**10**)=C₂(**10̄**)=9`. Implemented via the same `A3_INV_CARTAN` inverse-Cartan form as the S93 W6-4 predecessor (lines 379-404), for bit-consistency.

`η_FB_SU4` **RE-DERIVED** on the SU(4)_PS spectrum (NOT inherited from the SU(3) floor 0.436488, S92 W9-3): `η_FB_SU4(a,b,c) = |λ_PS|_sector / √(C₂+1)`. Result `η_FB_SU4_all_min = 0.101814` at sector **(6,0,6)** (8% margin lower bound 0.093669) — **FAR below** both the framework pin `η_FB_lower = 0.40` and the SU(3) floor 0.436488. The Friedrich-Bär **saturation predicate FAILS**: NEW-sector(13) min |λ| = 0.9409 < bot-20 ceiling = 1.1064. Structural reason: under the Jensen `exp(−τρ)` deformation the bottom-K |λ_PS| **keep DECREASING** with L_max (8 smallest |λ| drop from 1.601 at L_max≤8 to 1.063 at L_max=12 to 0.361 at L_max=20) — `√C₂` growth (C₂ up to ~109 at ρ=12) cannot keep `|λ|=√C₂·exp(−τρ)` bounded below, since `exp(−0.19·12)=0.102`. The bottom-K is **not** Friedrich-Bär-saturated at the s=4 pole; this re-derivation is itself part of the FAIL diagnosis and confirms the plan's instruction (re-derive on SU(4)_PS, do not inherit). Substrate-first `r_tau_PS`: the radial scale is an overall multiplicative factor that **cancels** in the dimensionless Level-3/Level-2 ratio (set r=1 here, identical to the SU(3) `_cm_1995_residue_formula.py`; only the absolute dimensional value would carry it — the predecessor flagged this exact point).

**(4) Substitution chain (`[SIGN]`; per `math-scripts.md §"Double-Check Logic Before Compute"`).**
- Step 1: `L3_PS = Res_{s=4} Tr(D_K_PS^{−2s})` [this gate's anchor].
- Step 2: `L2_envelope_PS ~ L^{−α(PS)}`; candidate readings `α_sym = 3` (inherited substrate-distance-1 s=3, §VII.AF.1 d−1=3) and `α_s4 = 4` (canonical, `alpha_HH1_per_pole_FW_s4 = 4`, Wodzicki degree 2(s−2)=2(4−2)=4).
- Step 3: `L^{−α}` is monotone DECREASING in α for L>1 ⇒ `L^{−4} < L^{−3}` for all L>1. Substituted at L=12: 4.823e-5 < 5.787e-4 ⇒ the α=4 envelope is TIGHTER.
- Step 4 (direction): the SYMBOLIC `Level-3 < Level-2` (S93 W6-4 J2 SYMBOLIC=True) holds *given a finite positive residue*; the α(PS)=3-vs-4 choice is a PRECISION-PIN, not a sign question — pass-under-tighter (α=4) ⇒ pass-under-looser (α=3). **This is the sign-PASS leg.** BUT the residue at s=4 is NOT finite (Step 5).
- Step 5 (regime): the SU(4)_PS shell scaling `L^{8−2s}` (Sage-exact) ⇒ convergence iff `s > 9/2`. At s=4 the exponent is 0 ⇒ the residue **diverges** ⇒ the truncation residual `r(L)` GROWS, NOT `< 1` ⇒ **magnitude FAIL, regime BREAKDOWN**. Conclusion: `Level-3 < Level-2` is sign-robust to α(PS)∈{3,4}, but the literal s=4 numerical anchor does not exist for SU(4)_PS; the convergent, substrate-natural anchor lives at **s≥5** (at s=6 the finite residue 9.39e-4 sits inside an `L^{−3}` tail; residual at L=12 = 7.69e-4).

**(5) Cross-checks.** (a) SU(4) Casimir ladder vs plan ladder: 7/7 seeds match (scale=1), conjugation-symmetric (C₂(**4**)=C₂(**4̄**), C₂(**10**)=C₂(**10̄**)) — Sage `<λ,λ+2ρ>` and the `A3_INV_CARTAN` form agree. (b) Shell-scaling exponent `8−2s` and convergence threshold `s>9/2` proved analytically in Sage (`solve(8−2s==−1)`), matching the empirical divergence (s=4 ratio 5.77×) and convergence (s=6 tail L^{−2.80}≈L^{−3}). (c) mpmath 100-bit cross-check of the convergent-pole residue at L=12, s=6: 0.000938641882 (mpmath) vs 0.000938641882 (float64), |Δ| = 5.4e-19 (machine precision). (d) SU(3) base s=4 convergence sanity (L^{−5}, plateaus to 0.32817) confirms the SU(4)/SU(3) spectral-dimension distinction is real, not a numerical artifact.

**(6) Dual-SHA verdict line.** `audit_sha256 = 697fe5329797ee45583286620d621609d818013e8a2fbb5729a46ab91c6dcc81` (over [script, canonical, pinmap, per-gate identity keys]); `content_sha256 = 1b00bd5eec34c9379a458837d98bd8b1800e96e2684ef6072db65d704402d64b` (over [script]); unique across the session verdict file (grep count = 1); dual-SHA companion row + S87 schema-v2 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN`) emitted.

**Methodology (route + feasibility disclosure).** Route taken: **Route-B (Friedrich-Bär analytic-saturation; FW-FRIEDRICH-BAR-SATURATION scheme tag)**. Route-A (sparse-Lanczos block-by-block) was evaluated and found unnecessary: because each Peter-Weyl sector eigenvalue is the analytic `√C₂·exp(−τρ)`, the CM-1995 §III.4 residue is a direct sector sum requiring no operator matrix — the 1094.7 GB dense wall and the sparse-Lanczos prescription are both bypassed. This is an in-session structural correction (per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` plan-authorship discipline item 3: replace the diagonalization prescription with the analytic argument and tag the scheme accordingly), honestly disclosed here and in the verdict scheme tag — NOT convention-shopping. `dirac_spectrum.py` is SU(3)-only; the SU(4)_PS rep theory is built in the producing script (exact Weyl-dimension + Casimir closed forms), exactly as the plan specifies ("SU(3) base — SU(4)_PS extension in producing script").

**Forward route (carry-forward seed).** Tier-2 dimensional-re-anchorability (`cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`): re-pin the §VII.BE FWD-C4 Level-3 anchor to the **convergent pole s≥5** for SU(4)_PS (at s=6 the residue is finite with an `L^{−3}` tail = §VII.AF.1 d=4 precedent), OR re-anchor to a DIMENSIONLESS truncation-invariant (log-derivative / cohomology-class) per the Tier-2 route. The gate's own FAIL_meaning anticipated this ("misidentified Level-2 envelope; re-derive the SU(4)_PS Friedrich-Bär envelope before re-pinning"). Until then the §VII.BE numerical Level-3 row is HELD `NOT-SATISFIED-PENDING-substrate-physical-pole-re-anchor`; the joint theorem structure may independently hold via the structural Stage-2 PASS-AND on the non-Level-3 clauses (S93 W6-4).

---

### §W3-10. S94-MODULE-AS-CANONICAL-K3 (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-MODULE-AS-CANONICAL-K3`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC** (methodology / corpus K-counter advancement; HIT-distinctness pre-registration — not a substrate observable)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The Pati-Salam `M_4(ℂ)_PS` rank-4 module-as-canonical instance (per §VII.BE FWD-C4) is Hybrid-Independence-Test-distinct from the existing K=1 atlas-row/cache-moment instance, advancing the `cross-pillar-bridge-corpus.md §19` weighting-functional-family K-counter by exactly +1 (K=1 → K=2).
**Plan reference**: `sessions/session-plan/session-94-plan-w3.md` §W3-10 (HIT axes, topological STOPPING rule, corpus-row target, METHODOLOGY-class allowlist flag).

**Output Artifacts** (verified on disk):

| Artifact | Path | Verification |
|:---------|:-----|:-------------|
| script | `computations/session-94/s94_module_as_canonical_k3.py` (22382 B) | `from canonical_constants import` ✓ (1), `append_verdict` ✓ (2), `topological_stopping` ✓ (5) |
| data | `computations/session-94/s94_module_as_canonical_k3.npz` (10146 B) | present; emits `K_pre`, `K_target`, `hit_i/ii/iii/iv`, `HIT`, `rank_K0_A_K`/`rank_K0_A_K_PS`, `base_distinct`, `topological_stopping_rule` |
| plot | `computations/session-94/s94_module_as_canonical_k3.png` (44625 B) | present (optional; K_0 base-count bar chart annotated with the K-counter advance) |
| verdict line | `computations/session-94/s94_gate_verdicts.txt:48` | `^S94-MODULE-AS-CANONICAL-K3:.* audit_sha256=[a-f0-9]{64}` ✓ (1); companion row line 49 ✓; no 3-tuple (`schema_v2_3tuple_required=false`) |

- `audit_sha256 = a6f17ad37b14c4dbadc4f6c496e0f2d3cd1c31eff95e45de506d7d6103d70e02` (over `[script, canonical_constants.py, pinmap]`); **unique** in `s94_gate_verdicts.txt` (count=1; sig_5 preserved).
- `content_sha256 = c0dc138e8ef2e76c101e32d5e855e7ebf98940b5d2c9c0e61959f3c62be72149` (over `[script]`).

**MCP Pre-Compute Audit**:

- `search_knowledge("weighting-functional-family module-as-canonical K-counter Pati-Salam corpus 19")` → returns the corpus §19 theorem `Weighting-functional-family membership ... SUGGESTION at K=1` (PROVEN tag); the `detect_weighting_functional_family` audit detector; the S93 W2-4 gate `S93-W2-4-VII-AU-CF37-MODULE-AS-CANONICAL-CORPUS-ROW` (PASS, the K=1 row); and the §VII.AU.OP-PROJ parent anchor. Confirms the gate is NOT pre-closed: the K=1 row exists; a K=1→K=2 advancement is open and is exactly this gate's question.
- `get_constant` not required — this is a methodology K-counter assessment consuming integer/Boolean structural facts, not a numerical framework constant. (`canonical_constants` imported as the mandatory audit pin per `math-scripts.md`; `M_KK`, `M_Pl_reduced` imported as the `Φ_w` prefactor-convention documentation only.)
- **Sage-MCP cross-check** (`sage_eval`, QQ-exact): `rank K_0(A_K) = 3` (`ℂ⊕ℍ⊕M₃(ℂ) → ℤ³`), `rank K_0(A_K_PS) = 4` (`ℂ⊕M₂(ℂ)_L⊕M₂(ℂ)_R⊕M₄(ℂ)_PS → ℤ⁴`), integer `rank gap = 1`, `base_distinct = True`; `HIT = (T∨T∨T)∧T = True`; `K_post = 1+1 = 2 == K_target`.

**Verdict**: **PASS** — the Pati-Salam `M_4(ℂ)_PS` rank-4 module-as-canonical instance is Hybrid-Independence-Test-distinct AND topological-base-distinct; the `cross-pillar-bridge-corpus.md §19` weighting-functional-family K-counter advances **K=1 → K=2** by exactly +1. A corpus §19 K=2 row candidate is produced (mack-cosmic-bridge sole writer lands it at session-close; gate-ID flagged for the `methodology-wave-allowlist-ledger.md` append, orchestrator post-gate action). SUGGESTION status held; K=3 MANDATORY remains a forward gate.

**Results**:

**(1) 4-tuple**: `(value=K_post=2, scheme=FW, convention=K-counter-advancement-by-HIT-distinctness-base-count-not-fiber-count, L_max=N/A)`; `K_pre=1`, `K_target=2`, `advancement_step=+1`.

**(2) Verdict criterion** (pre-registered, exact Boolean — no float tolerance): PASS iff `HIT = (i ∨ ii ∨ iii) ∧ iv = True` AND `base_distinct(K_0(A_K_PS), K_0(A_K)) = True` ⇒ `K_post = K_pre + 1 = 2`. Both conjuncts hold ⇒ PASS. (FAIL would be NOT-HIT-distinct OR a fiber-re-weighting `base_distinct=False`; INFO would be K=1 baseline unconfirmed OR `canonical_id_incomplete=True`. Neither fired.)

**(3) K=1 baseline confirmed ON DISK** (the INFO-guard prerequisite): `computations/session-93/s93_gate_verdicts.txt:42` — `S93-W2-4-VII-AU-CF37-MODULE-AS-CANONICAL-CORPUS-ROW: PASS`, `K_counter=K=1 SUGGESTION`, `audit_sha256=ec16fa362fa4dd90…`. Without this the gate would close INFO; it is present, so the K-counter advancement is admissible.

**(4) Per-axis Hybrid Independence Test** (corpus §3; `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`; advancement iff `(i ∨ ii ∨ iii) ∧ iv`):

| Axis | Pati-Salam `M_4(ℂ)_PS` instance | vs SU(3) atlas-row/cache-moment K=1 instance | Verdict |
|:-----|:--------------------------------|:---------------------------------------------|:-------:|
| (i) distinct substrate-IS pillar | `A_K_PS = ℂ ⊕ M₂(ℂ)_L ⊕ M₂(ℂ)_R ⊕ M₄(ℂ)_PS` (rank-4 K_0 base) | `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` (rank-3 K_0 base) | **True** |
| (ii) distinct laboratory-IN pillar | Pati-Salam in-scope lab image (Pillar VI/VII/VIII host candidates) | SU(3)-triple lab image (3He-B BDI / Pillar IV) | **True** (sourced from S91 `hit_C2=PASS`) |
| (iii) distinct bridge map class | Wodzicki ∘ HKR composite at the `M_4(ℂ)_PS` rank-4 module (§VII.BE FWD-C4) | atlas-row / cache-moment SU(3) module-as-canonical | **True** |
| (iv) independent algebraic envelope | SU(4)_PS `L^{−α(PS)}` — independent algebraic derivation on the rank-4 triple | SU(3) atlas-row/cache-moment envelope | **True** (NOT a numerical refinement) |

`HIT = (True ∨ True ∨ True) ∧ True = True`. (Note: clauses (i), (ii), (iii) are each independently sufficient via the disjunction; (iv) is the load-bearing conjunct that the corpus §19.0 directive explicitly names — "an INDEPENDENT algebraic envelope, per the Hybrid Independence Test clause iv; candidate: the M_4(ℂ)_PS Pati-Salam block, seed / S91 W9 `hit_iv_pass` Wedderburn-rank distinction".)

**Topological STOPPING rule** (corpus §19.0 — the anti-inflation DERIVATION, not a heuristic): every admissible weighting `Φ_w : [φ] ↦ (M_KK/M_Pl)²·∫|λ|^{−s} w(λ) dμ` factors through the SAME finite K_0 class `[φ]`, so the K-counter is a **base-count** (count of structurally-distinct K_0 bases at structurally-distinct triples via HIT), **NOT a fiber-count** (count of weighting functionals). The Pati-Salam instance counts iff `K_0(A_K_PS)` is a structurally-distinct topological base, NOT merely a re-weighting of the SU(3) base. Verified: `rank K_0(A_K_PS) = 4 ≠ rank K_0(A_K) = 3` ⇒ `base_distinct = True`, `canonical_id_incomplete = False`. This is a genuinely-distinct BASE, not a fiber. (A fiber re-weighting — same `[φ]`, different `w` — would have `base_distinct=False` and would NOT advance the K-counter; this is the foreclosure the topological derivation enforces.)

**K_0-rank substantiation** (K_0 of a finite-dim C\*-algebra `= ℤ^(# simple summands)`; each `M_n(F)`, `F ∈ {ℝ,ℂ,ℍ}`, is Morita-equivalent to `F` and contributes one `ℤ`):
- SU(3) triple `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` → **3 simple summands** → `K_0 = ℤ³`. The `ℍ` summand is a FULL simple summand (quaternions are a division algebra), so the rank is 3, **not** 2.
- Pati-Salam `A_K_PS = ℂ ⊕ M₂(ℂ)_L ⊕ M₂(ℂ)_R ⊕ M₄(ℂ)_PS` → **4 simple summands** → `K_0 = ℤ⁴`.
- Sage-exact (QQ): `rank gap = 4 − 3 = 1 ≠ 0` ⇒ `base_distinct = True`.
- **Cross-check against S91 anchor**: `S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION` (PASS) records `A_K_PS_wedderburn_blocks=['chi_C','M_2_L','M_2_R','M_4_PS']`, `wedderburn_block_count_A_K_PS=4`. The independently-recorded block count (4) matches the K_0 rank (4): `ps_block_count_consistent=True`. The S91 gate also recorded the FULL HIT conjunction `hit_C1/C2/C3/iv=PASS` at the laboratory-pillar-ID level; this gate re-applies HIT at the module-as-canonical weighting-functional axis with the base-distinctness refinement, consistent with that prior PASS.

**(5) Substitution chain** (per `math-scripts.md §"Double-Check Logic Before Compute"`) — the `+1` advancement is a direction claim, so the chain is mandatory:

```
Claim: "The Pati-Salam M_4(ℂ)_PS instance advances the corpus §19 K-counter by exactly +1 (K=1 → K=2)."

  Def 1: K_pre = 1                                   [corpus §19 baseline, S93 W2-4 verdict line 42, K_counter=K=1 SUGGESTION]
  Def 2: HIT = (i ∨ ii ∨ iii) ∧ iv                   [Hybrid Independence Test, corpus §3 / bridge-anatomy parent]
  Def 3: base_distinct = (rank K_0(A_K_PS) ≠ rank K_0(A_K))   [topological STOPPING rule: base-count not fiber-count]
  Def 4: advancement_step = +1 IF (HIT ∧ base_distinct) ELSE 0

  Substitute:  rank K_0(A_K) = 3,  rank K_0(A_K_PS) = 4  ⇒  base_distinct = (4 ≠ 3) = True
               (i) = True (distinct algebra / K_0 base);  (iv) = True (independent envelope)
               ⇒ HIT = (True ∨ … ∨ …) ∧ True = True
  Simplify:    advancement_step = +1 IF (True ∧ True) = +1
  Direction:   K_post = K_pre + advancement_step = 1 + 1 = 2
               EXACTLY +1 because the topological STOPPING rule forbids fiber-counting:
               a single structurally-distinct K_0 base advances the K-counter once,
               regardless of how many weighting functionals Φ_w it supports.
  Conclusion:  K=1 → K=2 (SUGGESTION held; K=3 MANDATORY needs ONE MORE distinct base —
               NOT achievable from this Pati-Salam instance alone).
```

**(6) Corpus §19 K=2 row content for mack-cosmic-bridge** (sole writer per `feedback_mack-bridge-role.md`; lands at session-close):
- **Instance**: K=2 — Pati-Salam `M_4(ℂ)_PS` rank-4 module-as-canonical, structurally distinct from the K=1 §VII.AU CF-37 (c)∘(d) SU(3) instance (substrate-distance-2 pole s=4 atlas-row/cache-moment).
- **Substrate-IS**: the Fredholm module `(H_K_PS, D_K_PS(τ_fold), γ_9, J)` restricted to the Pati-Salam corridor image; topological shadow `[φ_PS] ∈ K_0(A_K_PS) ≅ ℤ⁴` (rank-4 base, vs the SU(3) K=1 instance's `ℤ³` rank-3 base).
- **HIT per-clause**: (i)=YES (distinct algebra `A_K_PS` ≠ `A_K`; distinct K_0 base ℤ⁴ vs ℤ³); (ii)=YES (Pati-Salam in-scope lab image, S91 candidate-ID); (iii)=YES (Wodzicki∘HKR at the M_4(ℂ)_PS rank-4 module); (iv)=YES (independent SU(4)_PS `L^{−α(PS)}` envelope, not a numerical refinement). Predicate `(YES∨YES∨YES)∧YES = YES`.
- **Topological STOPPING rule**: base-count not fiber-count — counts as +1 because the rank-4 K_0 base is structurally distinct, NOT a fiber re-weighting.
- **Provenance**: this gate `S94-MODULE-AS-CANONICAL-K3` PASS, `audit_sha256=a6f17ad37b14c4dbadc4f6c496e0f2d3cd1c31eff95e45de506d7d6103d70e02`; anchors S93 W2-4 (K=1), S91 PS candidate-ID (`e16af0ba…`), §VII.BE FWD-C4 Stage-2 (`146b5742…`/`9df77b09…`).
- **Status update**: SUGGESTION at K=2 (was K=1); K=3 MANDATORY pending a THIRD structurally-distinct K_0 base.
- **METHODOLOGY-class allowlist flag**: this gate-ID `S94-MODULE-AS-CANONICAL-K3` is flagged for the `methodology-wave-allowlist-ledger.md` append per the recursion-attack closure (`methodology-wave-allowlist.md` — orchestrator-only append; NOT performed by this gate).

**(7) Output artifacts**: `computations/session-94/s94_module_as_canonical_k3.py` (script) + `.npz` (data) + `.png` (plot); verdict line `computations/session-94/s94_gate_verdicts.txt:48` (+ companion row 49).

**Assessment — solution-space**: the §19 weighting-functional-family conjecture gains a SECOND structurally-distinct calibration instance, on the strongest possible distinctness axis — a distinct ALGEBRA producing a distinct K_0 BASE (`ℤ⁴` vs `ℤ³`), not merely a distinct weight on the same base. This is exactly the advancement the corpus §19.0 directive pre-named (the M_4(ℂ)_PS Pati-Salam block as the K=2/K=3 candidate via the `hit_iv` Wedderburn-rank distinction). The K-counter mechanics are clean: the topological STOPPING rule caps the advancement at +1 regardless of fiber multiplicity, so K=3 MANDATORY is NOT reachable from this instance alone — it requires a THIRD structurally-distinct K_0 base at a structurally-distinct triple (a future forward gate). The §VII.BE FWD-C4 STAGE-1-CANDIDATE structural Stage-2 PASS-AND (on disk, `146b5742…`/`9df77b09…`) corroborates the Pati-Salam triple's structural standing independent of this K-counter assessment; this gate consumes only the algebra-structure facts (fixed at plan-freeze), not FWD-C4's numerical Level-3 pin (deferred to §W3-9, route-4b S94).

**Phononic framing (NON-PHONONIC — methodology)**: this gate computes no substrate observable. The substrate-physics CONTENT it reasons about is the `K_0(A_K_PS) = ℤ⁴` topological base of the Pati-Salam spectral triple vs the `K_0(A_K) = ℤ³` base of the SU(3) triple — the topological shadow `[φ]` of the Fredholm module (`phononic-framing.md` Level 1). The K-counter counts distinct K_0 bases (the topological shadows), not the weighting functionals `Φ_w` fibered over them. Direction of explanation flows FROM the spectral triple (the canonical) DOWNWARD: the Fredholm module IS the canonical; the weighting functionals are contractions of its analytic shadow, and the K_0 class is the index of its topological shadow. No container-thinking: the SU(4)_PS Peter-Weyl block structure is the fabric's internal representation content, not a field on an embedded internal space.

---

### §W3-11. S94-VII-AZ-BAND-ADMISSIBLE-RE-EXTRACTION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-AZ-BAND-ADMISSIBLE-RE-EXTRACTION`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (band-residence verification; discharge predicate for the deferred-pending FIRST-EXTRACTION sub-class)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: A band-admissible re-extraction of `α_HH¹_emp(s=4)` (finer L_max envelope OR refined residue fit) lands the empirical HH¹ exponent inside `[1.5, 4.0]` — discharging the §VII.AZ.OP-PROJ Sub-claim-B Element-4 FIRST-EXTRACTION sub-class that S93 W6-2 found out-of-band at 0.194312 — OR it confirms the observable genuinely sits at ~0.194 and the deferred-pending window stays open.
**Plan reference**: `sessions/session-plan/session-94-plan-w3.md` §W3-11 (dual extraction route, band anchor, FIRST-EXTRACTION discharge predicate).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | `must_contain` verified |
|:---------|:-----|:------------------------|
| script | `computations/session-94/s94_vii_az_band_admissible_re_extraction.py` | `from canonical_constants import` ✓ · `append_verdict` ✓ (`append_verdict_line`) · `alpha_HH1` ✓ |
| data | `computations/session-94/s94_vii_az_band_admissible_re_extraction.npz` | present (35 keys; both exponents emitted) ✓ |
| plot | `computations/session-94/s94_vii_az_band_admissible_re_extraction.png` | present (2-panel: in-cache + asymptotic) ✓ |
| verdict line | `computations/session-94/s94_gate_verdicts.txt` | `^S94-VII-AZ-BAND-ADMISSIBLE-RE-EXTRACTION:.* audit_sha256=[a-f0-9]{64}` ✓ · dual-SHA companion ✓ |
| WP section | this section | `**Status**:.*COMPLETED` ✓ · `**Verdict**:.*(PASS\|FAIL\|INFO)` ✓ · `**Output Artifacts**` ✓ · `**MCP Pre-Compute Audit**` ✓ |

`audit_sha256=d889b01d1d3f4ceade577d61ababa94d7ee4ab5db1141f84e5af8c7e5d4afc70` (unique in file); `content_sha256=17e2f487210e85b76bef3f1a0b37ad115b7df43d6d3fdd06eba89d29def82ae6`. Content-presence verification only — no line/byte targets.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE writing the script):

- `get_constant("alpha_HH1_per_pole_FW_s4")` → `4.0` (S92, `S92-W7-CF-W9-10-B`); the band-ceiling anchor — imported into the script, NOT hardcoded. Confirms the canonical s=4 envelope target.
- `search_knowledge("HH1 cocycle Mellin exponent s=4 first-extraction 0.194312 VII.AZ band")` → returns `S93-W6-2-VII-AZ-OP-PROJ-ELEMENT-4-SUB-CLASS-TAG-REPLACEMENT` (FAIL; `tag STAYS REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION`, `alpha_HH1_emp_s4=0.194312`, `band_resident=False`) and `S92-W7-CF-…-A-HH-1-FIRST-EXTRACTION-S4` (INFO; `in_pass_band_1p5_to_4p0=False`, `C_HH1=34.24`, `norm_HH1_at_L10=155.6423`). Confirms NOT pre-closed: the prior extraction is on-disk out-of-band and the tag-flip discharge is open — exactly this gate's question.
- `get_constant("tau_fold")` → `0.19` (S12/S42, `CONST-FREEZE-42`); the single-τ-slice anchor. Imported from canonical.
- Cross-pole context (edge query): `alpha_HH1_per_pole_FW_s3 = 2` (substrate-distance-1 pole), `alpha_HH1_per_pole_FW_s4 = 4` (substrate-distance-2 pole) — the Wodzicki/Connes `α(s) = 2(s−2)` ladder. NOT PRE-CLOSED.

**Verdict**: **PASS** — the re-extracted **canonical** HH¹ exponent `α_HH¹_emp(s=4) = 3.453551 ∈ [1.5, 4.0]`. The discharge predicate `numerical(exists) ∧ admissible(in-band) = True ∧ True = True` fires → licenses the §VII.AZ.OP-PROJ Sub-claim-B Element-4 tag-flip `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE-FIRST-EXTRACTED` (mack-cosmic-bridge lands the flip at session-close). **Solution-space**: the prior 0.194312 was NOT the cocycle's genuine convergence rate — it was a **cache-ceiling / truncation artifact** of treating a coarse 3-point in-cache log-log slope as canonical; the deferred-pending FIRST-EXTRACTION window **closes**. The K=1 calibration instance for the deferred-pending FIRST-EXTRACTION sub-class (`cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`) is satisfied with a closing discharge.

**Results**:

**(1) 4-tuple**: `(value=α_HH¹_emp(s=4)_CANONICAL = 3.453551, scheme=FW, convention=ABSOLUTE-exponent-band-membership-FULL-aMellin, L_max=14)` at `pole_s=4`, `tau=0.19` (τ_fold, imported). LEVEL=FULL (substrate-natural CM-1995 §III.4 evaluator; NOT SCHEMATIC); MACHINERY-SCOPE=CACHE-PROJECTION; binding=substrate-natural-binding; regulator `a_2^{Mellin}` (regulator-pin-discipline.md MANDATORY — no bare `a_n`).

**(2) BOTH exponents** (KEY directive; `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"` — both emitted in the npz):

| Exponent | Range | Value | Role | In band [1.5, 4.0]? |
|:---------|:------|:------|:-----|:-------------------:|
| **Asymptotic** (Friedrich-Bär) | `L ∈ [10, 100]` | **3.453551** | **CANONICAL** (rule item 1: "asymptotic result IS the canonical envelope-exponent") | **YES** |
| In-cache (log-log fit) | `L_max ∈ {10,11,12,13,14}` | 0.193260 | DIAGNOSTIC (rule item 2) | no |

Fraction-arithmetic cross-check of the asymptotic slope: 3.453551 (`|float64 − Fraction| = 2.66e-15`). The asymptotic exponent is **anchor-robust**: `α ∈ {3.559, 3.480, 3.454, 3.420, 3.405}` across cutoffs `{50, 80, 100, 150, 200}` — ALL in-band; `|α_canonical − 4| = 0.546` vs the Wodzicki/Connes `α_HH1_per_pole_FW_s4 = 4` anchor.

**(3) Cache-ceiling effect** (rule item 3; `|asymptotic − in-cache| / asymptotic = 0.944 > 0.10` ⇒ MUST cite Friedrich-Bär saturation): the L_max=14 cache captures only **88.43%** of the asymptotic norm limit (`norm_HH1(L=14)=157.024` vs `norm_canonical_FB=177.568`); the **11.57%** beyond-cache tail dominates the gap, so the in-cache deltas barely move (12.348% → 11.570% of canonical across L=10→14) and the log-log slope over that flat window is artificially small (0.193). A genuine α≈3.45 envelope would give `delta(10)/delta(14)=(14/10)^3.45=3.19`; the observed ratio is only 1.067 — the in-cache window CANNOT resolve the true envelope because the gap is tail-dominated, not L-resolved. FB saturation licensed: `min η_FB(L=14)=0.4465 ≥ 0.40` floor.

**(4) Replication cross-check** (methodology validation): the coarse `L ∈ {10,12,14}` 3-point fit (the prior W7-5 / W6-2 protocol) reproduces **α = 0.194312 EXACTLY** (matches the prior on-disk value to < 1e-3). This confirms (a) the norm computation is bit-identical to the prior (`norm_HH1_at_L10 = 155.6423` matches the S92 INFO verdict) and (b) the prior 0.194312 IS the coarse-in-cache slope — re-confirming it was a cache-ceiling artifact, not the genuine envelope.

**(5) Route-B cross-check** (refined residue fit via `_cm_1995_residue_formula.py`, CLASS=FULL): the §VII.AZ HH¹ s=4 observable IS the cache-spectrum `Σ|λ|^{−8}` re-sum; the CM-1995 §III.4 residue at finite L_max reduces algebraically to that direct sum, so Route-B's envelope exponent **= Route-A canonical = 3.453551** (routes AGREE on band-residence ⇒ no INFO route-disagreement). FULL-class integrity check: the Reading A identity `GV_APS = GV_CS` holds to `max|Δ| = 0.00e+00` across `L ∈ {10..14}`.

**(6) Substitution chain** (band-residence is a NECESSARY conjunct; canonical exponent gates the predicate):
- Def: `α_canon = α_HH¹_emp(s=4)_CANONICAL = asymptotic FB exponent = 3.453551`; `band = [1.5, 4.0]`.
- `numerical(exists) = True` (finite real exponent from both routes).
- `admissible(in-band) = (3.453551 ∈ [1.5, 4.0]) = True`.
- `discharge = numerical(exists) ∧ admissible(in-band) = True ∧ True = True` ⇒ **PASS**, tag-flip licensed.
- Prior contrast (W6-2 NO-OP): with the coarse-in-cache slope treated as canonical, `discharge(prior) = True ∧ (0.194312 ∈ [1.5,4.0]) = True ∧ False = False` — the FAIL was a consequence of mis-designating the diagnostic (in-cache) exponent as canonical, NOT a property of the cocycle's genuine convergence.
- 3-tuple: `sign_verdict=PASS` (band-residence direction satisfied), `magnitude_verdict=PASS` (canonical in-band), `regime_verdict=VALID` (FB saturation anchor-robust across all cutoffs). Composite collapse ⇒ **PASS**.

**(7) Dual-SHA**: `audit_sha256 = d889b01d1d3f4cea…` over [script, canonical, pinmap]; `content_sha256 = 17e2f487210e85b7…` over [script]. Input pins: cache `fa2bfb83…`, canonical `cda984cc…`, CM-1995 residue `ee02f271…`.

**(8) Output artifacts**: `s94_vii_az_band_admissible_re_extraction.py` / `.npz` (both exponents + anchor-robustness scan + cache-ceiling diagnostics) / `.png` (panel (a) in-cache diagnostic, panel (b) asymptotic canonical with band).

**Substrate framing**: GEOMETRIC. The substrate IS the finite SU(3) spectral triple `(A_K, H_K, D_K, γ_9, J)` at τ_fold=0.190; `α_HH¹_emp(s=4)` IS the empirical Mellin convergence exponent of the Hochschild 1-cocycle norm on the `M_3(ℂ)` Wedderburn block (triality `(p−q) mod 3 ≠ 0`) at the substrate-distance-2 pole `s=4` (Mellin weight `|λ|^{−8}`). The genuine substrate convergence rate (revealed by Friedrich-Bär extrapolation, robust to cutoff) lands in-band; the cache-ceiling-truncated in-cache slope (0.193) is the methodology-floor F-image at the cache-projection evaluation convention, NOT the substrate's intrinsic rate. Flow: D_K eigenvalues (L_max=14 cache) → per-sector `M_3(ℂ)` HH¹ residue contributions → asymptotic Friedrich-Bär envelope → `α_HH¹_emp(s=4)=3.453551` → band-membership against [1.5, 4.0]. The Element-4 deferred-pending tag discharges because the exponent IS the substrate's genuine convergence rate AND that rate lands in-band.

---

## Wave 3 Synthesis (team-lead)

Wave 3 closed 3 gates: **1 FAIL** (§W3-9), **2 PASS** (§W3-10, §W3-11). The wave maps a Pati-Salam convergence-threshold boundary and advances two K-counter / first-extraction fronts:

- **§W3-9 FAIL** (sign=PASS, magnitude=FAIL, regime=BREAKDOWN) — the SU(4)_PS Mellin-cone Level-3 residue `Σ dim_PS·(C₂+1)^{−s}` has shell-sum scaling **L^(8−2s)** (A₃ has 6 positive roots ⇒ dim_PS~L⁶, ~L² sectors/shell), converging iff **s > 9/2 = 4.5**. At the inherited s=4 pole the exponent is 0 ⇒ the full-spectrum residue DIVERGES (5.77× over L=10→120); the §VII.BE FWD-C4 numerical Level-3 pin cannot be satisfied at s=4. The SU(3) base converges at s=4 (L⁻⁵) — the rank-4 algebra's higher spectral dimension shifts the convergence threshold up by one Mellin unit. η_FB_SU4 RE-DERIVED on the SU(4)_PS cache = 0.101814 ≪ 0.40 ⇒ Friedrich-Bär saturation also FAILS. §VII.BE STAYS STAGE-1-CANDIDATE (NOT promoted); its structural Stage-2 PASS-AND (S93 W6-4) is unaffected. Forward route: Tier-2 dimensional re-anchorability to the convergent pole s≥5. Route disclosure: Route-B (Friedrich-Bär) taken; Route-A (sparse-Lanczos) found UNNECESSARY — each Peter-Weyl sector eigenvalue is analytic (√C₂·exp(−τρ)), so the residue is a direct sector sum, no 1094.7 GB matrix ever formed (honest in-session structural correction per math-scripts.md D_K Block-Diagonality pre-check).
- **§W3-10 PASS** — the Pati-Salam M_4(ℂ)_PS rank-4 instance advances the corpus §19 weighting-functional-family K-counter **K=1 → K=2**: HIT-distinct ((i∨ii∨iii)∧iv) AND topological-base-distinct (rank K_0(A_K_PS)=4=ℤ⁴ vs rank K_0(A_K)=3=ℤ³, integer gap=1) → +1 under the base-count-not-fiber-count STOPPING rule. K=3 MANDATORY needs a THIRD structurally-distinct topological base.
- **§W3-11 PASS** — re-extracted canonical (asymptotic Friedrich-Bär L∈[10,100]) HH¹ exponent α_HH¹_emp(s=4) = **3.453551 ∈ [1.5, 4.0]**; the prior 0.194 was a cache-ceiling artifact (only 88.43% of the asymptotic norm captured at L=14; the in-cache window cannot resolve the L⁻³·⁴⁵ envelope). Discharges §VII.AZ.OP-PROJ Sub-claim-B Element-4 `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE-FIRST-EXTRACTED`; §VII.AZ STAGE-3-PERMANENT-eligible status preserved.

### Effected In-Session (non-math — completed before STOP)

- [x] §VII.BE FWD-C4 §W3-9 FAIL annotation (stays STAGE-1-CANDIDATE; Tier-2 re-anchor-at-s≥5 forward route; structural Stage-2 unaffected) + §VII.AQ.OP-PROJ DIAGNOSTIC row (does NOT reopen order-one-CLOSED STAGE-3) — mack — `sessions/permanent-results-registry.md:20554–20567,17902–17906` — `697fe532`
- [x] corpus §19.3 K=2 calibration instance row — mack — `sessions/framework/registry/cross-pillar-bridge-corpus.md:1314–1382` — `a6f17ad3`
- [x] §VII.AZ.OP-PROJ Element-4 tag-flip FIRST-EXTRACTION → FIRST-EXTRACTED (+ propagated to Level-2 row, Status parenthetical, Residue #3, forward-gates queue) — mack — `sessions/permanent-results-registry.md:19788,19799,19801,19853,19871` — `d889b01d`
- [x] methodology-wave-allowlist ledger row + instances rationale for `S94-MODULE-AS-CANONICAL-K3` (orchestrator-only per recursion-attack closure; `sha256_of_plan_block=f4e36ac3…`) — orchestrator-direct — `sessions/framework/registry/methodology-wave-allowlist-ledger.md` + `methodology-wave-instances.md`
- [x] corpus §19 K-counter status sync K=1 → K=2 (pointer-table row + sub-section header + directive prose) — orchestrator-direct (`.claude/rules/` subagent-denied) — `.claude/rules/substrate-first-canonical-sourcing.md:80,82,203`

### Process observations (closed in-session)

- **§W3-9 route correction**: the agent took Route-B (Friedrich-Bär analytic saturation) and found Route-A (sparse-Lanczos) unnecessary because the SU(4)_PS Peter-Weyl sector eigenvalues are analytic — disclosed in the WP §Methodology + verdict scheme tag (FW-FRIEDRICH-BAR-SATURATION). In-session structural correction, NOT convention-shopping. The dense-infeasibility wall (1094.7 GB) never required Lanczos.
- **K-counter status-file misattribution (caught)**: mack reported the corpus §19 K=1 status row as living in `cross-pillar-bridge-anatomy.md`; it actually lives in `substrate-first-canonical-sourcing.md` (line 203 pointer table + lines 80/82). Orchestrator located + synced it. Subagents are correctly edit-denied on `.claude/rules/`, so this is structurally an orchestrator-only fix regardless.
- **framework-reindex note**: PostToolUse reindex on the ledger/instances/corpus edits reported "registry meta-entry not found" — benign (the reindexer re-indexed the files but the per-file `Registry ID` meta-entry marker is not present on `methodology-wave-instances.md` / the corpus in the form the reindexer expects). No data loss; not a blocker. Noted for the curator.

## Carry-Forward Computations

### CF-S95-VII-BE-TIER2-REANCHOR — §VII.BE FWD-C4 Level-3 Tier-2 dimensional re-anchor at convergent pole s≥5

| Field | Spec |
|:------|:-----|
| **What** | Re-anchor the §VII.BE FWD-C4 Pati-Salam Level-3 at the convergent Mellin pole **s≥5** (since the inherited s=4 pole diverges: SU(4)_PS residue scales L^(8−2s), converges only s>4.5). Apply the Tier-2 dimensional-re-anchorability gate (`cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`): either find the substrate-singled-out convergent pole (Tier-1) or re-anchor to a dimensionless truncation-invariant functional (Tier-2). At s=6 a finite residue 9.39e-4 with L⁻²·⁸⁰ tail was observed in §W3-9 — confirm + pin. |
| **Inputs** | `computations/session-94/s94_vii_ps_full_spectrum_level_3.npz` (the §W3-9 SU(4)_PS Casimir ladder + per-pole residue scan + re-derived η_FB_SU4); the §VII.BE registry entry (STAGE-1-CANDIDATE); `canonical_constants.py`. |
| **Gate** | Convergent-pole residue at s≥5 satisfies Level-3 < Level-2 (truncation tail L⁻ᵅ with α>0), OR the Tier-2 dimensionless functional converges and is re-anchorable. PASS → §VII.BE FWD-C4 numerical Level-3 closes; the structural Stage-2 (already on disk) then licenses STAGE-3 review. |
| **Effort** | ~1.0 wave-equivalents (re-uses the §W3-9 SU(4)_PS analytic sector machinery; no fresh diagonalization). |

> The corpus §19 K=2 → K=3 MANDATORY advancement (needs a THIRD structurally-distinct topological base) is recorded in `cross-pillar-bridge-corpus.md §19.3` as a standing forward-gate; it is NOT a crisp 4-field CF here (no concrete third-base candidate is yet identified — adding one would be padding).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-25 | §VII.BE FWD-C4 SU(4)_PS Level-3 at s=4 | PENDING-FIRST-EXTRACTION | DONE-FAIL (s=4 diverges, L^(8−2s)); stays STAGE-1-CANDIDATE; re-anchor s≥5 | §W3-9 FAIL |
| 2026-05-25 | corpus §19 weighting-functional-family K-counter | SUGGESTION K=1 | SUGGESTION K=2 (M_4(ℂ)_PS base-distinct) | §W3-10 PASS |
| 2026-05-25 | §VII.AZ.OP-PROJ Sub-claim-B Element-4 | REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION | STAGE-1-CANDIDATE-FIRST-EXTRACTED (α=3.4536 in-band) | §W3-11 PASS |
| 2026-05-25 | `methodology-wave-allowlist-ledger.md` | (no S94-MODULE-AS-CANONICAL-K3 row) | S94-MODULE-AS-CANONICAL-K3 allowlisted (METHODOLOGY-class M4) | §W3-10 PASS + conditional append |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON |
|:-----|:-------|:------------|:------------|:-----|
| §W3-9 | computations/session-94/s94_vii_ps_full_spectrum_level_3.py (39.4 KB) | 16.5 KB | 202.5 KB | — |
| §W3-10 | computations/session-94/s94_module_as_canonical_k3.py (22.4 KB) | 10.1 KB | 44.6 KB | — |
| §W3-11 | computations/session-94/s94_vii_az_band_admissible_re_extraction.py (41.5 KB) | 10.9 KB | 129.4 KB | — |

All verdict lines + dual-SHA companions (+ 3-tuple rows for §W3-9/§W3-11) in `computations/session-94/s94_gate_verdicts.txt`.
