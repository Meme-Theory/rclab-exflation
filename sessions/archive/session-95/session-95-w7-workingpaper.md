# Session 95 Wave 7 — Spectral-Dimension γ_E, proven_1086 Noun-Licensing, LQG Narrow-Path Regime-II (Results Working Paper)

**Session**: 95 | **Wave**: W7 | **Plan**: session-95-plan-w7.md | **Theme**: Spectral-dimension γ_E crystallization (B2 band-bottom dispersion order), proven_1086 van-Hove noun-licensing adjudication, and the substrate's OWN Regime-II effective geometry where the canonical-LQG bridge does NOT close.

## Gate Sections

### §W7-1. CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION (phonon-first-cosmologist)

**Status**: COMPLETED
**Gate ID**: `CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (property of the D_K eigenvalue flow λ(τ) near k_0 — the fabric itself, not its excitations)
**Agent**: `phonon-first-cosmologist`
**Hypothesis**: The B2 (0,1)⊕(1,0) band-bottom dispersion order at τ_fold is decisively n=1 (linear, γ_E=0), not n=2 (√-edge, γ_E=½): a window-stable nonzero leading velocity c_1 dominates the local dispersion at k_0, so γ_E crystallizes to 0.
**Plan reference**: `sessions/session-plan/session-95-plan-w7.md` §W7-1 (machinery pin, thresholds, substitution chain source, Casimir/Friedrich-Bär feasibility pre-check).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

| Artifact | Path | Exists | must_contain — grep verification |
|:---------|:-----|:-------|:---------------------------------|
| script | `computations/session-95/s95_w7_1_gamma_e_crystallization.py` | ✅ (40137 B) | `from canonical_constants import` ✅ ; `append_verdict` ✅ |
| data | `computations/session-95/s95_w7_1_gamma_e_crystallization.npz` | ✅ (21030 B) | (no must_contain; present) |
| plot | `computations/session-95/s95_w7_1_gamma_e_crystallization.png` | ✅ (198513 B) | (no must_contain; present) |
| verdict_line | `computations/session-95/s95_gate_verdicts.txt` | ✅ | `^CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION:.* audit_sha256=[a-f0-9]{64}` ✅ ; dual-SHA companion ✅ ; schema-v2 3-tuple companion ✅ |
| wp_section | this section | ✅ | `Status: COMPLETED` ✅ ; `Verdict: …(INFO)` ✅ ; `Output Artifacts` ✅ ; `MCP Pre-Compute Audit` ✅ |

Grep transcript (verbatim):
```
$ grep -E "^CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION:.* audit_sha256=[a-f0-9]{64}" → MATCH (canonical line)
$ grep -E "^# audit_sha256_short=.* # CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION dual-SHA" → MATCH
$ grep -E "^# sign_verdict=.* # CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION 3-tuple"      → MATCH
$ grep -c b0a0e174ad79818eabc705dfeb19950e4e142d5032910c81deeb873dc4468bb8 (audit_sha256) → 1  (sig_5 unique)
$ grep -c "from canonical_constants import" s95_w7_1_gamma_e_crystallization.py → ≥1 ; grep -c "append_verdict" → ≥1
```

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("gamma_E spectral dimension B2 band van Hove dispersion order energy axis DOS")` → returned the S94 W7 plan reading-map (`n_disp=1 ⇒ Reading-KK γ_E≈½`; `n_disp=2 ⇒ Reading-van-Hove γ_E→1`), the canonical `rho_smooth=14.023 = rho_B2_per_mode`, the s92 d_s ENERGY-axis DOS equation `d_s(σ_*)=2σ_*⟨λ²⟩`, the "B2 mult-8 optical band edge" theorem, and the s93 W7-3 γ_E DOS-exponent estimator. **Not PRE-CLOSED**: the *crystallization* (window-stable order vs fit-window-fragility resolution) is the new compute; the dispersion ORDER reading itself was OPEN as the S94 W7-22 carry-forward. (NB: this gate uses the S95-plan convention γ_E = 1 − 1/n ⇒ n=1→γ_E=0; the S94 plan's reading-map labelled n=1 "γ_E≈½" — the S95 gate's pre-registered definition governs.)
- `trace_entity("proven_1086")` → `proven_1086` = **Pomeranchuk instability f=−4.687** (NOT the B2 band); the S94 W-2 workshop produced `proven_2073` (Mis-carriage mode A) on framing `proven_1086` as a dispersion claim. Salient: the B2-band noun-licensing residual lives in W7-2's `proven_1086` re-word, not this gate; W7-1 closes only the dispersion ORDER (γ_E).
- `get_constant("rho_B2_per_mode")` → `14.023250234055` (S37, `s37_instanton_action.npz`); confirms the canonical pin feeding `v_g = 1/(π·rho_B2) = 0.0226987`.
- Sage MCP (`sage_eval`) → exact `γ_E(n=1)=0`, `γ_E(n=2)=1/2`; `v_g_canonical=0.0226987239671`; min(v_g/floor)=2.26987 > 1 ⇒ c_1≠0 ⇒ n=1 ⇒ γ_E=0 (substitution-chain Steps 1,4,5 exact-verified).

**Verdict**: **INFO** — composite (3-tuple: sign=PASS, magnitude=INFO, regime=VALID). γ_E **crystallizes to 0** (n=1 linear) on the **window-stable invariants** (n=1 at 100% of windows in BOTH corridors; leading coefficient c_1 → v_g at CV=1.10e-12), but the **literal pre-registered metric** CV(order_ratio)<0.10 is NOT met (CV≈1.03–1.09) because **order_ratio = |c_1|/(|c_2|·Δk) is a 1/W-divergent NON-invariant** — structurally unsatisfiable for a genuine analytic n=1 band. This maps verbatim to the plan's **INFO_meaning** ("single-sign reading persists … without crisp CV convergence → γ_E LEANS/crystallizes to 0 but is not crystallized to the CV<0.10 bar"). INFO is a result, not a failure (`math-scripts.md §"All Results Are Good"`).

4-tuple: `(value=INFO / γ_E=0.0 / n=1, scheme=SU3-SIGMA-MODEL-CONTINUOUS-K, convention=ENERGY-AXIS-DISPERSION-ORDER, L_max=12)`. `audit_sha256=b0a0e174ad79818eabc705dfeb19950e4e142d5032910c81deeb873dc4468bb8`, `content_sha256=98b29b9879c0a164eeecf8ef0a91ca2a89d93d67b0ebd2b5de4b4b67bdbfad3d`.

**Results**:

**Crystallized value**: **γ_E = 0** (n=1 linear), from γ_E = 1 − 1/n with n_crystallized = 1.

**Substitution chain (substituted numbers)** — [SIGN] dispersion-ORDER n=1 vs n=2:
- Step 1: γ_E := 1 − 1/n (energy-axis DOS scaling exponent; s92 d_s).
- Step 2: E(k)−E_0 = c_1|k−k_0|¹ + c_2|k−k_0|² + …; n = min{p : c_p ≠ 0}.
- Step 3: v_g(τ_fold) = |dE/dk|_{k_0+} = |c_1|. **Verified at machine zero**: S94 npz `vg_traj ≡ c1_arr` (max|diff| = 0.00e+00).
- Step 4: canonical v_g = 1/(π·rho_B2) = 1/(π·14.023250234055) = **0.022698724** (= S94 npz `vg_fold_rho`, reldiff 0); band-ladder v_g(fold) = **0.054099152**. canon = 2.2699× floor; ladder = 5.4099× floor (V_G_FLOOR = 1e-2).
- Step 5: c_1 = v_g ≥ 2.27× V_G_FLOOR > 0 ⇒ min{p : c_p ≠ 0} = 1 ⇒ n = 1 ⇒ γ_E = 1 − 1/1 = **0**.
- Step 6: c_1 bounded away from 0 (BOTH incarnations ≥ 2.27× floor) ⇒ n=1, γ_E=0, **EXCLUDING the n=2 √-edge** (requires c_1→0, contradicting Step 4).

**n_dispersion(τ_fold) = 1**, window-stable: 100% of the 9 discrete-ladder windows (N=3..11) AND 100% of the 8 σ-model continuous-k windows read n=1. (S94 baseline already read n=1 at every τ-slice; this gate adds window-stability.)

**Cross-fit-window order-ratio CV** (literal pre-registered metric, threshold CV<0.10):
- σ-model corridor (canonical): CV(order_ratio) = **1.0336** ≥ 0.10. Per-window order_ratio = |c_1|/(|c_2|·W) sweeps 158.9 → 5675.6 as W shrinks 0.05→0.0014 — **diverges as 1/W by construction** (c_1, c_2 both window-stable), so the order_ratio CV cannot meet <0.10 for a TRUE n=1 band. The order_ratio is the wrong quantity to CV-stabilize.
- discrete-ladder corridor (a-faithful): CV(order_ratio) = **1.0901** ≥ 0.10 (order_ratio swings 0.91→86 across N; fit-window-fragile in level-index units). N=5 reproduces S94 bit-for-bit: c_1=0.054099, c_2=0.002857, order_ratio=18.9333 (S94 npz 18.9332).

**The CORRECT window-stable invariants** (the actual crystallization):
- Leading coefficient **c_1 → v_g** at every σ-model window; CV(c_1) = **1.10e-12** (≪ 0.10); c_1 ≡ v_g_canonical = 0.0226987 (bit-stable).
- Dimensionless sub/leading ratio **|c_2|·W/|c_1| → 0** as W→0 (last = 1.76e-04) — confirms n=1 (the quadratic term vanishes relative to the linear term near k_0).
- n window-stable = 1 (both corridors).

**Corridor used**: **(b) SU(3) σ-model continuous-k** is canonical (regulator-free; no L_max truncation); **(a) band-curvature re-fit** also computed for cross-check. Both agree n=1.

**Casimir / Friedrich-Bär feasibility pre-check** (corridor (a) L_max≥14 redundancy): empirical η_FB floor (excl (0,0)) = 0.43649 (argmin C_2 ≈ (1,1)); η_FB_lower (10% margin) = 0.39284. B2 band-bottom E_0 = 0.835894 (mult 4), first_gap = 0.004970, band-bottom ceiling = E_0 + first_gap = 0.840864. A new p+q=14 sector (smallest-C_2 (7,7), C_2=63.0) has min|λ| lower bound = η_FB_lower·√(C_2+1) = **3.14271 ≫ 0.840864** ⇒ **SATURATION = True**: the B2 bottom is L_max-saturated at L_max=12 (it lives at Peter-Weyl level p+q=1, present in any L_max≥1). **L_max_plan=14, L_max_operational=12, truncation_consistent=True**; corridor (a) higher-L_max is REDUNDANT; irrep construction at p+q≥13 NOT attempted (honest operational deviation from the conditional L_max=14 plan pin, disclosed here + in the verdict-line scheme per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class-1 boundary).

**Both v_g incarnations vs V_G_FLOOR=1e-2**: canonical 0.022699 (2.2699×) AND band-ladder 0.054099 (5.4099×) — both above the floor ⇒ c_1≠0 ⇒ n=1.

**Substrate-physics assessment** (substrate-first per `phononic-framing.md`): GEOMETRIC. γ_E is a property of the D_K eigenvalue flow λ(τ) of the B2 (0,1)⊕(1,0) optical sector near k_0 — the fabric's own internal structure, NOT a diffusion observable in a container. The chain runs D_K eigenvalues → local dispersion → order n = min{p : c_p≠0} → energy-axis scaling exponent γ_E = 1 − 1/n; the group velocity v_g IS the n=1 coefficient c_1, and the substrate's canonical pin v_g = 1/(π·rho_B2) bounds c_1 ≥ 2.27× above the floor, so the dispersion is **linear (n=1, γ_E=0)** at the eigenvalue-flow layer, not a √-edge. **The crystallization's real content**: the fit-window fragility of the L_max=12 proxy was NOT an order ambiguity — n=1 is the window-stable invariant; the order_ratio magnitude is a fit-window-fragile non-invariant (1/W-divergent). γ_E is pinned at 0 for the spectral-dimension d_s flow (the directly-fitted ENERGY-axis DOS exponent). The diffusion-window discipline (`cross-pillar-bridge-anatomy.md §"Diffusion-window-observable specialization"`, K=2) is honored: γ_E lives on the ENERGY axis, NOT a σ→0-manifold-dimension-vs-CDT comparison; **min d_s<3 is RETIRED**, the van-Hove discriminator is γ_E. INVARIANT to this gate: the proven Φ_DOS-continuum value rho_smooth = 14.02 = 1/(π·v_g) (the BCS driver g·N(0)=3.24) stands — W7-1 resolves only Φ_dispersion (the ORDER), not Φ_DOS-continuum.

**Methodology note (for synthesis / W7-2 coupling)**: the literal pre-registered PASS metric `CV(order_ratio)<0.10` is structurally unsatisfiable for a genuine n=1 band (order_ratio ∝ 1/W diverges under window-shrinking with stable c_1,c_2). The physical content — n=1, γ_E=0 — is decisively crystallized on the window-stable invariants (c_1→v_g, n-flatness, |c_2|W/|c_1|→0). This is a Class-8.2-adjacent observation: a future gate testing dispersion order should CV-stabilize the **leading coefficient c_1** (or the dimensionless |c_2|W/|c_1| → 0) rather than order_ratio. Carried forward as a methodology candidate, not a re-run (the physics is settled: γ_E=0).

**Artifacts**: `s95_w7_1_gamma_e_crystallization.py` (40137 B) / `.npz` (21030 B) / `.png` (198513 B). The .png is a 2×2 panel: (top-left) σ-model continuous-k dispersion E(k) near k_0 (linear-leading); (top-right) window-stable c_1 → v_g; (bottom-left) order_ratio as the 1/W-divergent non-invariant (both corridors); (bottom-right) n=1 at 100% of windows + |c_2|W/|c_1| → 0.

---

### §W7-2. CF-S95-W2-VAN-HOVE-NOUN (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S95-W2-VAN-HOVE-NOUN`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (the (0,1)⊕(1,0) bottom multiplicity is a property of the spectral triple's Peter-Weyl structure)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The fixed mult-8 δ-WEIGHT on the FINITE spectral triple is either (kk) a representation-theoretic ℂ¹⁶ Clifford degeneracy — a multiplicity, NOT a band-structure singularity — or (landau) a defensible finite-triple analog of a van Hove singularity; a pre-registered structural discriminator (continuum-limit multiplicity-and-gap scaling crossing a band-structure-singularity criterion) decides the noun WITHOUT pre-favoring either reading.
**Plan reference**: `sessions/session-plan/session-95-plan-w7.md` §W7-2 (two-branch discriminator, machinery pin, thresholds, neutral substitution chain).

**Verdict**: **FAIL** — the noun "van Hove singularity" is **NOT LICENSED** for `proven_1086`. The B2 mult-8 δ-WEIGHT lands the **OVER-CLAIM branch**: `m(L_max)` is FD-flat (multiplicity fixed, `|d ln m / d ln L| = 0` exactly under both conventions) AND `first_gap(L_max)` is bounded away from 0 (zero relative variation, `β_gap = 0`). It is a representation-theoretic ℂ¹⁶ Clifford degeneracy at fixed E₀, not a band-structure singularity. The honest label is **"maximal-multiplicity DOS edge"** (kk reading supported). FAIL here is the constraint-map result, not an agent shortfall: it closes the noun-licensing corridor.

> **Disposition note (own concession, T4)**: I (landau) am the converger/registry-owner of `proven_1086`. At the S94 W-2 workshop T4 joint verdict I already conceded `multiplicity ≠ order` ("a δ of any nonzero coefficient is equi-order/infinite" — the `γ_E → 1` boundary). This gate is the pre-registered structural test of whether the *continuum limit* rescues the noun via either accretion or a gap-collapse non-analyticity. It does not. The concession stands and is now quantified: the multiplicity does not grow and the gap does not close under L_max-refinement, because the (0,1)/(1,0) Peter-Weyl blocks are FIXED finite-dimensional irrep diagonalizations (D_K block-diagonal, PROVEN wall). The verdict does NOT pre-favor a reading — both branches were live; the substrate spectrum lands in OVER-CLAIM by exact, regulator-free structure.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | `must_contain` grep |
|:---------|:-----|:-------|:--------------------|
| script | `computations/session-95/s95_w7_2_van_hove_noun.py` | ✅ | `from canonical_constants import` ✅, `append_verdict` ✅ |
| data | `computations/session-95/s95_w7_2_van_hove_noun.npz` | ✅ | (binary, present) |
| plot | `computations/session-95/s95_w7_2_van_hove_noun.png` | ✅ | (binary, present) |
| verdict_line | `computations/session-95/s95_gate_verdicts.txt` | ✅ | `^CF-S95-W2-VAN-HOVE-NOUN:.* audit_sha256=[a-f0-9]{64}` ✅ + dual-SHA companion ✅ |
| wp_section | this section | ✅ | Status:COMPLETED ✅, Verdict ✅, Output Artifacts ✅, MCP Pre-Compute Audit ✅ |

- **audit_sha256** = `a1f54312fc025b1b65b48e9612bcbfff63d7ced5c0c63f775ebd2b52df7fabfe` (unique; first emission, no supersession)
- **content_sha256** = `ba5df54486b8c12994f4bcfc9b31e21880036bf16441836a89b1e18ab3eb14df`
- `schema_v2_3tuple_required: false` per the plan ([VERIFY] noun-adjudication, no directional pre-registration) — discriminator-provenance + Φ_DOS-continuum-invariance companion rows emitted instead.

**MCP Pre-Compute Audit** (queries run before writing the script; `mcp__knowledge__*`):

- `trace_entity("proven_1086")` → Pomeranchuk instability f=−4.687 (the row identifier); plus `proven_2073`/`Mis-carriage mode A` (kk T1) — the S94 W-2 disposition pre-context. Confirms this gate operates on the residual NOUN, not new physics.
- `search_knowledge("van Hove singularity band structure")` → the canonical proven_1086 row in `Classification-of-phonon-exflation.md` is ALREADY partially re-worded: "**B2 mult-8 optical band edge** — Finite large BCS-driving DOS edge (rho_smooth = 14.02 M_KK⁻¹ … 43–51× enhancement, S28c). NOT a dispersionless 'flat band' and NOT an [over-claimed singularity]". The full "van Hove" noun is the open residual.
- `search_knowledge("proven_1086 Φ_DOS-singular maximal multiplicity Clifford degeneracy van Hove noun")` → `Mis-carriage mode B (landau T2)` PROVEN in `cross-pillar-bridge-corpus.md`: "promoting Φ_DOS-singular's multiplicity (a WEIGHT) to a van Hove ORDER … multiplicity ≠ order (kk T3 §2, conceded T4). Promoting the mult-8 to 'infinite-order' would make the B1 (1·δ) and B3 (3·δ) levels ALSO 'infinite-order van Hove' — the vacuous-label outcome." This is the standing structural fact the gate's Step-4 Fact A imports — NOT PRE-CLOSED (the continuum-limit scaling test is new).
- `get_constant("rho_B2_per_mode")` → 14.023250234055 (S37); `get_constant("v_g_B2_fold")` → 0.022699323 (S94). The Φ_DOS-continuum invariant. `rho_smooth` not under that name in MCP — it IS `rho_B2_per_mode` (the 1/(π·v_g) value).
- **Not pre-closed**: the noun-licensing adjudication via continuum-limit multiplicity-and-gap scaling had not been computed. This gate is the first such test.

**Results**:

The three S94 W-2 functionals MUST NOT be conflated (per `phononic-framing.md §"Same-functional-different-scale"`). This gate operates strictly on **Φ_DOS-singular** (the δ-weight), NOT Φ_dispersion (the order) or Φ_DOS-continuum (the proven BCS driver):

```
Φ_dispersion     := γ_E = 1 − 1/n          (the ORDER; n=1 linear, γ_E=0; refuted as a singularity, S94)
Φ_DOS-continuum  := ρ = 1/(π|v_g|) = 14.02  (the proven velocity-slaved DOS, EXACT; INVARIANT to this gate)
Φ_DOS-singular   := m·δ(E−E_0), m=8         (the fixed multiplicity δ-WEIGHT; THIS gate's sole object)
```

*(1) B2 bottom-multiplicity + first_gap L_max-scan* (combined (0,1)⊕(1,0), master-cache sub-truncations):

| L_max | m (combined-distinct) | m (per-sector ×2) | first_gap (M_KK) | E₀ (M_KK) |
|:-----:|:---------------------:|:-----------------:|:----------------:|:---------:|
| 6 | 4 | 4 | 0.0049703200 | 0.8358935100 |
| 8 | 4 | 4 | 0.0049703200 | 0.8358935100 |
| 10 | 4 | 4 | 0.0049703200 | 0.8358935100 |
| 12 | 4 | 4 | 0.0049703200 | 0.8358935100 |

The bottom multiplicity, first_gap, and E₀ are **machine-identical** across all sub-truncations. (The S94 frozen `bot_deg ≡ 4` at every τ matches the combined-distinct count; the plan's "mult-8 = 4 per sector × 2" framing maps to the same scaling-flat object — both conventions tested, both FD-flat.)

*(2) Discriminator scaling fits*:
- `|d ln m / d ln L_max|` = **0.000e+00** (combined-distinct) and **0.000e+00** (per-sector ×2) — exactly FD-flat under both conventions (< 1e-6 floor).
- `β_gap = d ln(first_gap)/d ln L_max` = **+0.000e+00**; gap relative-variation = **0.000e+00** (< 0.20 bound). No power-law approach to 0.

*(3) Casimir-floor sanity (Sage-exact, regulator-free)*: B2 bottom E₀ = 0.83589351; global higher-(p,q) min|λ| = **0.87297503** (adjoint (1,1)). **No higher sector dips below E₀** (gap +0.037082). Friedrich-Bär slope min|λ| vs √(C₂+1) = **+0.4868 > 0** ⇒ higher sectors move UP with Casimir. Sage QQ: C₂((0,1)) = **4/3**; min C₂ among p+q≥2 = **3** (adjoint), strictly > 4/3 ⇒ no continuum accretion into E₀, exactly and representation-theoretically.

*(4) Branch verdict*: `m_fd_flat = True` ∧ `gap_bounded = True` ⇒ **branch_OVER-CLAIM = True**; `mult_grows = False` ∧ `gap_powerlaw_to_zero = False` ⇒ **branch_LICENSE = False**. Verdict **FAIL** (noun OVER-CLAIMED).

*(5) Proven-physics INVARIANCE cross-check*: 1/(π·v_g_B2_fold) = **14.022880** vs `rho_B2_per_mode` = **14.023250**, rel_resid = **2.64e-05**. The Φ_DOS-continuum value `rho_smooth = 14.02 = 1/(π·v_g)` — the N(0) feeding the BCS driver g·N(0)=3.24 — is **UNCHANGED** under this gate's FAIL. Only the residual NOUN moves.

*(Neutral discriminator substitution chain, with substituted numbers)*: Step 1 (van Hove = DOS non-analyticity ρ ~ |E−E_c|^{−(1−γ_E)} at ∇_kE=0 of a dispersing band, γ_E∈[0,1)). Step 2 (finite-triple object m·δ(E−E₀), m=8 = 4×2). Step 3 (LICENSE iff L_max→∞ gives a continuum-DOS non-analyticity: m→∞ OR first_gap→0 power-law). Step 4 (Fact A: mult≠order, S94 T4; Fact B: rho_smooth=14.02 INVARIANT — both standing, no pre-judgment). Step 5 (read off: m FD-flat=0 AND β_gap=0, gap_rel_var=0 ⇒ OVER-CLAIM branch; the C₂=4/3 < 3 Casimir gap forbids accretion). **Conclusion: noun OVER-CLAIMED — "maximal-multiplicity DOS edge."**

*4-tuple*: (value=`noun_OVER-CLAIMED_mFDflat=True_dlnm=0.00e+00/0.00e+00_betagap=+0.00e+00_gaprelvar=0.00e+00_noaccretion=True_rhoINVARIANT=2.6e-05`, scheme=`PETER-WEYL-MULTIPLICITY-L-SCAN`, convention=`FINITE-TRIPLE-NOUN-LICENSING`, L_max=12).

**Plan-text-drift note** (`substrate-first-canonical-sourcing.md §(ii.B)`): the plan pinned `canonical_constants.py` SHA `cc3878…`; the live file is `7a66ea…` (drift from APPENDED S95 constants — 4 lines tagged S95 at lines 628–630, e.g. `residue_s6_PS_Linf`, `n_PBH_FW_saturated_tail`). My four consumed constants (`rho_B2_per_mode`, `v_g_B2_fold`, `PI`, `tau_fold`) are **byte-identical to the committed plan-freeze state** (`git diff HEAD` empty on those lines), so the drift is NON-LOAD-BEARING. Both physics inputs — the L12 master cache (`9e6d9cf7…`) and the S94 γ_E trajectory (`71e573e0…`) — match their plan-freeze SHAs EXACTLY. `audit_sha256` computed over live bytes (honest).

**Routing consequence (doc-integration; I do NOT edit the curated doc)**: this FAIL routes the `Classification-of-phonon-exflation.md:59` `proven_1086` re-word. The row's "van Hove" noun is **NOT LICENSED**; the wording should be the neutral **"maximal-multiplicity DOS edge"** (4 modes/sector × 2 sectors at E₀=0.8359 M_KK; rho_smooth=14.02=1/(π·v_g) feeding BCS g·N(0)=3.24 stands UNCHANGED). Flagged for the closeout's `Classification-of-phonon-exflation.md` integration pass + the §24 ENRICH-companion row (coupled with W7-1's γ_E=0/n=1 verdict). I (landau, registry-owner of proven_1086) endorse the OVER-CLAIM disposition.

**Output Artifacts**: `s95_w7_2_van_hove_noun.py` / `.npz` / `.png` at `computations/session-95/`.

**Substrate-physics assessment** (PHONONIC/GEOMETRIC framing): GEOMETRIC. The B2 mult-8 is the fabric's representation-theoretic content at the band bottom — the ℂ¹⁶ Clifford degeneracy of FIXED Peter-Weyl (0,1)/(1,0) blocks, NOT a continuum-band feature measured IN a container. Because D_K is block-diagonal (PROVEN wall) and each sector is a complete irrep diagonalization, the L_max "sub-truncation" only filters sector PRESENCE — it cannot make a fixed block's bottom accrete states or close its internal gap. There is no continuum limit in which the noun "van Hove singularity" is earned. The honest substrate label is a *maximal-multiplicity DOS edge*: a real, large, finite degeneracy that drives BCS via Φ_DOS-continuum (rho_smooth=14.02), distinct from the over-claimed *singularity* noun. The direction of explanation holds: D_K eigenvalues → Peter-Weyl multiplicity → finite DOS edge → BCS driver; never "a singularity in a band measured in space."

---

### §W7-3. CF-S95-W7-23-NARROW-PATH-REGIME-II (phonon-first-cosmologist)

**Status**: COMPLETED
**Gate ID**: `CF-S95-W7-23-NARROW-PATH-REGIME-II`
**Trigger**: `[VERIFY]` (closed-form-map existence; no single directional claim)
**Classification**: **GEOMETRIC** (the exit-horizon cocycle area-spectrum is a property of the spectral-triple geometry)
**Agent**: `phonon-first-cosmologist`
**Hypothesis**: In Regime II (γ_emergent ≈ 398, mismatch ~1676× vs canonical SU(2) γ_BH=0.2375, so the path to canonical LQG does NOT close), the substrate's exit-horizon cocycle [S_exit-horizon]^♯ generates a well-defined effective area-spectrum with a closed-form Barbero-Immirzi-analog γ_emergent, distinct in form from canonical A_p = 8πγℓ_P²√(j(j+1)).
**Plan reference**: `sessions/session-plan/session-95-plan-w7.md` §W7-3 (closed-form-map existence check, machinery pin, thresholds, characterization substitution chain).

**Verdict**: **PASS** — the substrate's OWN Regime-II effective geometry is closed-form-pinned: γ_emergent characterized with a <5% band, A_substrate(p,q) ∝ √(C₂(p,q)+1) derived from the K_0 pairings + Friedrich-Bär slope, and the explicit closed-form map to the canonical SU(2) √(j(j+1)) ladder written. Reading-(b) (substrate has a consistent effective geometry distinct from canonical LQG) is SUPPORTED. The 1676× mismatch is the CHARACTERIZATION, NOT a path to canonical LQG.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | must_contain → grep result |
|:---------|:-----|:-------|:---------------------------|
| script | `computations/session-95/s95_w7_3_narrow_path_regime_ii.py` | ✓ | `from canonical_constants import` → matches (L71/72); `append_verdict` → matches (def + call) |
| data | `computations/session-95/s95_w7_3_narrow_path_regime_ii.npz` | ✓ (21,016 B) | — (optional:false; present) |
| plot | `computations/session-95/s95_w7_3_narrow_path_regime_ii.png` | ✓ (142,133 B) | — (optional:false; present) |
| verdict_line | `computations/session-95/s95_gate_verdicts.txt` | ✓ | `^CF-S95-W7-23-NARROW-PATH-REGIME-II:.* audit_sha256=[a-f0-9]{64}` → matches (original L113 + corrective L118, latest-non-superseded); dual-SHA companion rows present |

- **Canonical verdict line** (latest-non-superseded): `audit_sha256=70b2c5e2b7f117f83ac8c200fb522ba01967334bd993145b2e3ac54addec4f4b content_sha256=0358d2fe24eb49c46ea4f510142faa1e82fbfc6df0bf8001480fb6571918dd59`. Carries `supersedes=356808c3…` per `gate-verdicts.md §"Option A"`: the original PASS line (`audit_sha256=356808c3…`) is RETAINED on disk (verdict permanence); the corrective re-emission (cosmetic Step-4 OOM print-narrative consistency fix — physics + all four verdict components IDENTICAL) appends with the supersedes tag. Both audit SHAs unique across the file (sig_5 clean); content_sha256 on disk == verdict-line (script bytes match).
- `schema_v2_3tuple_required: false` per plan §W7-3 — [VERIFY] characterization; the path-non-closure is pre-registered (not a directional gate), so NO SIGN/MAGNITUDE/REGIME companion row.

**MCP Pre-Compute Audit**:
- `search_knowledge("narrow-path Regime-II cocycle gamma_emergent LQG bridge area spectrum")` → `S94-NARROW-PATH-WORKSHOP-6-COCYCLE` **PASS-Regime-II** (gamma_emergent=398.08, mismatch=1676×, K0rank=2, cocycle_nontrivial=True); `lqg-narrow-path-bridge-class` registry **LEVEL-1-EXTRACTED; REGIME-II RE-SCOPED** (workshop-internal-pending). **Not pre-closed** — this gate IS the S95 carry-forward characterizing the substrate-OWN Regime-II geometry (item 5/7 of the bridge-class refinement pathway).
- `search_knowledge("VII VIII cross-pillar bridge Barbero-Immirzi area Friedrich-Bar Casimir ladder")` → cross-pillar bridge anatomy (5-anatomy + 3-level, MANDATORY K=3); confirms this is a substrate-IS characterization, NOT a registry-PASS bridge entry (no laboratory-IN match → the 5-anatomy/3-level discipline does not apply, plan §W7-3 cross-pillar note).
- `get_constant("GAMMA_BH_SU2_CONVENTION_LQG")` → 0.2375 (S92; Paper 03 §VII; SU(2)-convention; U(1) CS value γ_0≈0.127 is a DIFFERENT convention — mixing is Class-(c) PIN-DRIFT risk; convention tag carried in the verdict).
- `get_constant("ALPHA_BRIDGE_REQUIRED_FW")` → 0.00481 (S92; α_bridge = γ_BH/49.34 for Regime-I closure; Q2 confirms γ does NOT admit cutoff running → Regime II has no recovery).
- `get_constant("A_horizon_FW")` → 71226.26338976152 (S92; emergent total exit-horizon area; W7-3 OOM cross-check only).

**Results**:

NUMBERS (all consume the FROZEN S94 W7-23 cocycle npz, SHA `60e06590…` = plan pin, verified):

- **Deliverable 1 — γ_emergent + band**: γ_emergent = **398.077** (the npz cocycle-norm-to-area ratio, post-fold incarnation). Band via the npz-internal scaling γ/α = γ_emergent_post/α_post = **49.34** EXACTLY of the post-α band [8.0680, 8.1226] → γ band **[398.08, 400.77]**, rel-width **0.0068 < 0.05** ✓. (The plan-pin γ_BH/α_bridge_required = 0.2375/0.00481 = 49.376 differs by 7.36e-4 — a Class-(d) PIN-DERIVATIVE difference = the 3-sig-fig rounding of α_bridge_required, NOT substrate physics; γ_emergent is anchored to the npz value.)
- **Deliverable 2 — A_substrate(p,q) ∝ √(C₂(p,q)+1)**: Friedrich-Bär slope **fb_slope = 0.4754 ≈ ½** (|slope−0.5|<0.1 ✓ — the √-of-Casimir signature), ladder **R² = 0.9934 ≥ 0.95** ✓ (standing anchor). K_0 closure (j≥1/2 rank-2 scope): **H + M3 = 31141.4262 = R_total** to machine zero (0.0e+00, Sage-verified); the ℂ-singlet (j=0, 0.8197) is RETIRED and correctly excluded — C+H+M3 = 31142.2459 would re-add it and is NOT the closure identity. cocycle_nontrivial=True, is_exact=False, rank=2 ⇒ k0_closes=True ✓. Ladder values (kappa=1): (0,0)→1.0000, (1,0)/(0,1)→1.5275, (1,1)→2.0000, (2,0)/(0,2)→2.0817, (2,1)/(1,2)→2.5166, (3,0)/(0,3)→2.6458.
- **Deliverable 3 — closed-form effective-geometry MAP**: solving √(j(j+1)) = √(C₂(p,q)+1) ⇒ **j_equiv(p,q) = (−1 + √(4·C₂(p,q)+5))/2** (Sage-exact radical: e.g. (0,0)→√5/2−½=0.6180, (1,1)→√17/2−½=1.5616 — both IRRATIONAL). **0 of 10** ladder rungs land on a half-integer SU(2) j ⇒ the two ladders are **structurally incommensurate** (not a rescaling). Triality degeneracy C₂(p,q)=C₂(q,p) holds on all 4 conjugate pairs (the SU(2) j-ladder has no such degeneracy). map_well_defined=True ✓.

SUBSTITUTION CHAIN (Step-4 structural mismatch, substituted numbers):
- γ_emergent/γ_BH = 398.077/0.2375 = **1676.11392** (reproduces npz gamma_mismatch_post to rel_err **0.0e+00**; Sage-exact, γ_BH = 19/80).
- α_post/α_bridge_required = 8.0680/0.00481 = 1677.35 ≫ 1; log10(α_post) = +0.907; npz oom_post = **3.2246** above the Regime-I window ⇒ **Regime II selected**.
- Per Paper 03 §VII, γ does NOT admit cutoff running ⇒ NO recovery mechanism ⇒ the path to canonical LQG does NOT close. This is the substrate-likely structural outcome (pre-registered per the S92 workshop), NOT a FAIL.

CROSS-CHECKS:
- A_horizon_FW = 71226.26 (ℓ_P²) cross-check (OOM only): smallest nontrivial area rung (γ-units) = 398.077·√(7/3) = 608.07; effective puncture count A_horizon/rung_min ~ **1.17×10²** — the macroscopic exit-horizon area is populated by ~10² area quanta (order-of-magnitude consistent; the area ladder is the microscopic quantum-of-area spectrum).
- In-script Friedrich-Bär refit on the 10 (p,q) labels: slope=0.4754, intc=−0.0036, R²=1.000000 (exact by construction — linear data; the binding R² anchor is the npz fb_r2=0.9934 over the full 90-sector fit).
- **Verdict 4-tuple**: (value=`REGIME-II-EFF-GEOM…path_to_canonical_LQG=DOES-NOT-CLOSE(pre-registered)`, scheme=`REGIME-II-EFFECTIVE-GEOMETRY`, convention=`SU(2)-CONVENTION-LQG-COMPARISON`, L_max=`N/A`).

**Substrate-physics assessment** (substrate-first per `phononic-framing.md` — IS, not IN):

The substrate IS the exit-horizon cocycle [S_exit-horizon]^♯ on the spectral triple (A_K, H_K, D_K(τ_fold)); it is NOT embedded in an LQG container. The direction of explanation flows **D_K eigenvalues → SU(3)-Casimir ladder √(C₂(p,q)+1) → emergent area geometry → (HKR/-Cheeger-Simons bridge) → canonical LQG A_p image**, never the reverse. What this gate establishes: the fabric's OWN quantum-of-area spectrum is the **SU(3)-Casimir ladder** √(C₂(p,q)+1) — a rank-2, 2D (p,q)-indexed, triality-degenerate discrete geometry — carrying an effective Barbero-Immirzi-analog γ_emergent ≈ 398. Canonical LQG's A_p = 8πγℓ_P²√(j(j+1)) is the laboratory-IN SU(2) image: a rank-1, 1D half-integer-j-indexed, non-degenerate ladder with γ_BH = 0.2375. The closed-form map j_equiv(p,q) = (−1+√(4C₂+5))/2 exists and is exact, but lands **0/10** substrate rungs on a half-integer SU(2) rung — the two discrete geometries are **structurally incommensurate**, not related by a rescaling. This is the heart of the characterization: the 1676× Immirzi mismatch is not a tolerance failure to be closed; it is the quantitative statement that the substrate's discrete geometry is a genuinely distinct (richer, rank-2/triality) effective theory from the SU(2) spin-network. Because γ admits no cutoff-running recovery (Paper 03 §VII), Regime II has no escape to canonical LQG — pre-registered, not a surprise.

**Cross-pillar (VII↔VIII) framing**: this is a substrate-IS characterization (Pillar VII spectral-action geometry of the cocycle ↔ Pillar VIII KK-geometry-on-Lie-groups via the SU(3) Casimir), NOT a registry-PASS cross-pillar bridge entry — no laboratory-IN observable is being matched (the canonical A_p is cited only for direction-of-explanation), so the 5-anatomy/3-level discipline of `cross-pillar-bridge-anatomy.md` does not apply (plan §W7-3 cross-pillar note). The structural pattern is the same eigenvalue-ladder isomorphism question that recurs across pillars: a √(quadratic-Casimir+1) area spectrum is the universal form (SU(3) here, SU(2) in LQG); the discriminating content is the RANK of the group (2 vs 1) and the consequent commensurability of the discrete meshes. PASS routes `lqg-narrow-path-bridge-class.md` from workshop-internal-pending to a documented Regime-II effective-geometry entry (substrate-OWN; still NOT a canonical-LQG closure), per the Wave-7 closeout decision point.

**Methodology note (plan-text-drift, `substrate-first-canonical-sourcing.md §ii.B`)**: the plan-pinned `canonical_constants.py` SHA (`cc387821…`) drifted to the runtime SHA (`7a66eaf1…`) because later S95 waves appended constants via `update_constant`. The THREE constants this gate consumes — GAMMA_BH_SU2_CONVENTION_LQG=0.2375, ALPHA_BRIDGE_REQUIRED_FW=0.00481, A_horizon_FW=71226.26 — are UNCHANGED on disk and match the knowledge-MCP canonical exactly, so the drift is benign (in non-consumed constants). Resolved by npz-ground-truth resolution: the runtime SHA is canonical; the drift is documented in the verdict value field (`canonical_drift=True(benign-nonconsumed-constants;3-consumed-match-MCP)`) and the npz (`canonical_drift`, `canonical_runtime_sha`). The frozen S94 cocycle npz SHA (the physics ground truth) matches its plan pin exactly. `tau_exit` is NOT a canonical_constants name (only `tau_fold`); it is sourced from the npz (tau_exit=0.16, S70).

**Artifacts**: `computations/session-95/s95_w7_3_narrow_path_regime_ii.py` / `.npz` / `.png`.

---

## Wave 7 Synthesis (team-lead)

**Wave 7 — Spectral-dimension γ_E / proven_1086 van-Hove / LQG narrow-path (phonon-first-owned, + landau). 3 gates: 1 PASS, 1 INFO, 1 FAIL.**

| Gate | Verdict | One-line outcome |
|:-----|:--------|:-----------------|
| §W7-1 GAMMA-E-CRYSTALLIZATION | **INFO** | γ_E=0 (n=1 linear) crystallized on the WINDOW-STABLE invariants (c_1→v_g CV 1.10e-12; |c_2|W/|c_1|→0; n=1 at 100% of windows, both corridors). The literal CV(order_ratio)<0.10 metric is structurally unsatisfiable (order_ratio is a 1/W-divergent non-invariant) → INFO; the physics is decisive. |
| §W7-2 VAN-HOVE-NOUN | **FAIL** | "van Hove" NOT licensed for proven_1086 (m=4,4,4,4 no accretion; gap L_max-invariant; Casimir floor clean → no continuum limit). Honest label: "maximal-multiplicity DOS edge" (ℂ¹⁶ Clifford degeneracy at E₀). Physics (rho_smooth=14.02, BCS driver g·N(0)=3.24) INVARIANT. |
| §W7-3 NARROW-PATH-REGIME-II | **PASS** | substrate-OWN Regime-II geometry characterized (γ_emergent=398.08; A∝√(C₂+1) ladder, slope≈½, R²=0.993); structurally distinct from canonical LQG (SU(3) rank-2 vs SU(2) rank-1; 0/10 incommensurate rungs). 1676× Immirzi mismatch IS the characterization. |

**The W7-1 ⊗ W7-2 coherence (proven_1086).** The two coupled gates reinforce each other: W7-1's n=1 linear dispersion (v_g≠0, hence no band extremum) is *exactly why* W7-2 finds "van Hove" NOT licensed — a van Hove singularity requires v_g→0 at a saddle/extremum. proven_1086 is a maximal-multiplicity DOS edge, not a van Hove singularity: a terminology correction with the physics invariant (the BCS driver g·N(0)=3.24 via rho_smooth=14.02 is untouched). Routes the `Classification-of-phonon-exflation.md:59` re-word (doc-track).

**The W7-3 cross-framework finding.** Pillars VII (spectral-action cocycle) and VIII (KK-on-Lie-groups) share the universal `√(quadratic-Casimir+1)` area-ladder form; the substrate's SU(3) (rank-2) version is structurally INCOMMENSURATE with canonical LQG's SU(2) (rank-1) version (0/10 ladder rungs land on a half-integer SU(2) j). The narrow-path-to-canonical-LQG corridor stays CLOSED; the substrate has its OWN consistent Regime-II effective geometry. The discriminating content is the group RANK.

**Structural read.** W7 self-characterizes the substrate's emergent geometry: a linear-dispersion DOS edge (not van Hove), and a √(Casimir+1) area spectrum that is the substrate's OWN (not canonical LQG's). Two methodology sharpenings: the energy-axis γ_E discriminator (min d_s<3 RETIRED per the diffusion-window discipline) + the window-stable-invariant lesson for dispersion-order gates. One genuine future-compute (the lqg Regime-II Stage-2 cross-axis verify → STAGE-3) below.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator before STOP)

- [x] `lqg-narrow-path-bridge-class.md` PROMOTED (correspondence edit, orchestrator-direct) — workshop-internal-pending → **DOCUMENTED substrate-OWN Regime-II effective geometry** (W7-3 PASS characterization: γ_emergent=398.08; √(C₂+1) area ladder; j_equiv closed-form map; 0/10 incommensurate rungs vs SU(2)); frontmatter type + title + status-tag + refinement-pathway item 7 updated. The Stage-2 verify → STAGE-3 is the S96 CF below
- [x] W7-2 van-Hove-noun FAIL → `Classification-of-phonon-exflation.md:59` proven_1086 re-word ("van Hove" → "maximal-multiplicity DOS edge"; 4 modes/sector × 2 at E₀=0.8359; rho_smooth=14.02 BCS driver stands) ROUTED to the doc-`/rclab-workshop` (curated-doc, doc-integration track; the S95 index pre-identified this re-word)
- [x] W7-1 methodology note recorded — dispersion-order gates should CV-stabilize the leading coefficient c_1 (or the dimensionless |c_2|W/|c_1|→0), NOT order_ratio (a 1/W-divergent non-invariant under window-shrinking); Class-8.2-adjacent (pre-registered verifier metric structurally unsatisfiable for a clean band); recorded in housekeeping §A as an S96-planning methodology note
- [x] proven_1086 / γ_E / LQG findings recorded — γ_E=0 honors the diffusion-window discipline (min d_s<3 retired; energy-axis discriminator); the §24 ENRICH-companion (diffusion-window-observable) cross-link noted; W7-3 LQG rank-2-vs-rank-1 incommensurability documented in the correspondence ledger

**Math-vs-non-math discriminator applied**: the lqg promotion + doc-corrections + methodology note are effected/recorded now; the one genuine future-compute item (the lqg Regime-II Stage-2 verify) is below.

## Carry-Forward Computations

### CF-S96-LQG-REGIME-II-STAGE-2-VERIFY — Stage-2 two-agent cross-axis verify of the substrate-OWN Regime-II effective geometry → STAGE-3-PERMANENT

| Field | Spec |
|:------|:-----|
| **What** | Stage-2 two-agent cross-axis independent-verify (per `joint-theorem-promotion.md §"Stage 2"` + the substrate-input-orthogonality clause) of the W7-3 Regime-II characterization: **Axis-A `connes-ncg-theorist`** (Hochschild-cocycle existence at HH^•(A_K) + the HKR-Cheeger-Simons bridge-map class), **Axis-B `volovik-superfluid-universe-theorist`** (the a_4 BCS-condensation kinematics in the cocycle + the Bogoliubov-covariance constraint); BOTH without prior workshop context (read only the registered `lqg-narrow-path-bridge-class.md` entry, never the S92 workshop transcript). On PASS-AND → crystallize `lqg-narrow-path-bridge-class.md` as a STAGE-3-PERMANENT substrate-OWN Regime-II effective-geometry characterization (NOT a canonical-LQG bridge). |
| **Inputs** | `sessions/framework/correspondence/lqg-narrow-path-bridge-class.md` (the registered Regime-II entry); `computations/session-95/s95_w7_3_narrow_path_regime_ii.npz` (W7-3, audit `70b2c5e2…`); the frozen S94 W7-23 cocycle npz (SHA `60e06590…`); `canonical_constants.py`. |
| **Gate** | `S96-LQG-REGIME-II-STAGE-2-VERIFY` PASS iff BOTH cross-reviewers independently PASS-AND every clause (Hochschild/HKR + BCS/Bogoliubov) WITHOUT the S92 workshop transcript (structurally-independent agreement per `epistemic-discipline.md §"What Counts as Evidence"`). |
| **Effort** | ~0.5 wave-equivalent. **Depends on**: W7-3 (PASS, DONE). |

(W7-1's γ_E=0 and W7-2's noun-FAIL CLOSE their gates — no math CF; W7-1's metric lesson is a methodology note, W7-2's re-word is a doc-track item. The session's other standing math CFs are unchanged.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-28 | proven_1086 noun (B2 mult-8 optical band edge) | "van Hove singularity" | "maximal-multiplicity DOS edge" (NOT van Hove); physics (rho_smooth=14.02, BCS driver) INVARIANT | W7-2 FAIL (noun not licensed); routes Classification-of-phonon-exflation.md:59 re-word |
| 2026-05-28 | γ_E spectral-dimension / dispersion order | fit-window-fragile order ambiguity (S94 order_ratio 688→18.9→27.4) | γ_E=0, n=1 linear (window-stable invariant); fragility was a non-invariant, not an order ambiguity | W7-1 INFO; min d_s<3 retired (energy-axis discriminator) |
| 2026-05-28 | LQG narrow-path bridge class | workshop-internal-pending Regime-II | DOCUMENTED substrate-OWN Regime-II effective geometry; canonical-LQG corridor CLOSED (rank-2 vs rank-1 incommensurate) | W7-3 PASS; lqg-narrow-path-bridge-class.md promoted |
| 2026-05-28 | dispersion-order verifier metric (methodology) | order_ratio CV<0.10 (pre-registered) | CV-stabilize c_1 / |c_2|W/|c_1|→0 (window-stable); order_ratio is 1/W-divergent | W7-1 Class-8.2-adjacent finding (S96-planning note) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) |
|:-----|:-------|:------------|:------------|
| §W7-1 | `s95_w7_1_gamma_e_crystallization.py` | `…​.npz` | `…​.png` |
| §W7-2 | `s95_w7_2_van_hove_noun.py` | `…​.npz` | `…​.png` |
| §W7-3 | `s95_w7_3_narrow_path_regime_ii.py` | `…​.npz` | `…​.png` |

(All under `computations/session-95/`. Verdict lines in `s95_gate_verdicts.txt`: W7-1 `b0a0e174…` [INFO], W7-2 `a1f54312…` [FAIL], W7-3 `70b2c5e2…` [PASS; latest-non-superseded, supersedes `356808c3…` per Option A]. All sig_5-unique.)
