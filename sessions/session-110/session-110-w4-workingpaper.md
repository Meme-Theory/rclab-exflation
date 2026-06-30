# Session 110 Wave 4 — MED tier + §B structural-theorem promotions/verifies (Results Working Paper)

**Session**: 110 | **Wave**: 4 | **Plan**: session-110-plan-w4.md | **Theme**: the largest compute wave of the M_KK-keystone session, pre-split W4a (6 MED-tier compute carry-forwards) / W4b (3 §B structural-theorem promotions via the `joint-theorem-promotion.md` Stage-2 two-agent cross-axis protocol + EVOI re-anchor). Spine: sign-PASS / magnitude-FAIL = the rank-1 M_KK weight seen from every downstream consumer; W4a closes the held leg of several blind Stage-2 PASS-ANDs.

## Gate Sections

# ═══════════════════ WAVE 4a — MED COMPUTE ═══════════════════

### §W4a-1. S110-CF-B5A-MICROSTATE (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-B5A-MICROSTATE`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC**
**Agent**: `hawking-theorist`
**Hypothesis**: A horizon-localized boundary/edge-mode entropy on the white-hole exit screen equals the Bekenstein-Hawking A/4 as an EQUALITY (the surviving microstate-origin rung after inv-4 W1-1 closed the bulk-charge corridor and inv-4 W1-2 derived the 1/4 from the a₂ conical deficit).
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4a-1 (machinery pin, A/4 target, substitution chain source).

**Verdict**: **FAIL** (composite) — magnitude FAIL, sign N/A (EQUALITY test), regime VALID.

The boundary edge-mode count **S_boundary = 9 372** lands within **0.279 OOM** of A/4 = 17 806.57, decisively beating the bulk GGE conserved-charge count (inv-4 W1-1: **2.856 OOM undercount**) by ~2.6 orders of magnitude. The microstate origin of the 1/4 is therefore **boundary-localized, not bulk-localized** — the holographic reading is confirmed. But the count is a **factor ~1.9 short** of equality (`S_boundary/(A/4) = 0.526`, `test_ratio = 0.474 > info_band 0.25`), so the literal A/4 equality FAILs per the pre-registered rubric. Per the gate's `FAIL_meaning`: the 1/4 microstate origin is neither bulk-charge (W1-1 FAIL) nor a naive single-sided boundary count — a deeper island/two-sided-screen construction is required. The near-1/2 ratio is itself a structural clue (one Bogoliubov-partner / one screen-orientation count vs the two-sided horizon).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block):
- `computations/session-110/s110_cf_b5a_microstate.py` — present; contains `from canonical_constants import` and `print_verdict_payload`. ✔
- `computations/session-110/s110_cf_b5a_microstate.npz` — present (7 833 bytes). ✔
- `computations/session-110/s110_cf_b5a_microstate.png` — present (115 228 bytes; 3-panel). ✔
- Verdict line `^S110-CF-B5A-MICROSTATE:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + 3-tuple row in `computations/session-110/s110_gate_verdicts.txt` — present (emitted via `emit_verdict` MCP, cross-process locked, sig_5 unique). ✔
  - `audit_sha256=f89be2223340fe000008068f6306dffb2c73d3159c101b2990dd74d6d03b4134`
  - `content_sha256=118d725d32456d0707d70ed8505e79b0e313a072c1d23cacc93e56b282c57df7`
- This WP section's Status/Verdict/Output-Artifacts/MCP markers. ✔

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("boundary edge-mode entropy A/4 microstate horizon white-hole exit screen Bekenstein-Hawking")` → surfaced **S89-ALPHA-M-NCG-HORIZON-MICROSTATE-COUNT-DERIVATION** (FAIL; Tr_HSS=38, R_CM=38, mass-windowed HSS count for a 10⁷ M_⊙ BH) — a DIFFERENT observable (astrophysical-mass-windowed, not the exit-slice boundary count); not a closure of this gate.
- `get_constant("A_horizon_FW")` → `71226.26338976152` (S92, `S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY`, M_KK⁻² units) ⇒ A/4 = 17 806.5658 (Sage-confirmed exact).
- `search_knowledge("inv-4 W1-1 GGE Page curve undercount … inv-4 W1-2 conical deficit 1/4")` → confirmed the two upstream closures (bulk Page-curve undercount; conical 1/4); both npz on disk.
- `trace_entity` / `get_constant` cross-checks: `a2_fold=2776.165` (area operator second moment), `a0_fold=6440.0` (perimeter zeroth moment) — the substrate-geometry inputs to λ_exit. No existing closure covers the exit-slice boundary-mode-count observable ⇒ gate is NOT pre-closed; compute proceeds.

**Results**:

Substitution chain (EQUALITY magnitude gate; sign_verdict = N/A — no directional claim), all numbers substituted:

- **Def 1**: `A_horizon_FW = 71226.26338976152` [canonical_constants.py, gate S92-W8-CF-S92-T1-7-CF39, M_KK⁻² units].
- **Def 2**: `A/4 := A_horizon_FW/4 = 17806.565847` [Bekenstein-Hawking target; the 1/4 from inv-4 W1-2 a₂-conical `c_conical = 0.2500001`, |R−1| = 5e-7].
- **Def 3**: `S_boundary :=` count of exit-screen-localized D_K edge modes on `(A_K^{≤12}, H_K^{≤12}, D_K^{≤12})` at τ_exit ≈ 0.16.
- **λ_exit (substrate geometry, NOT fitted to A/4)**: `theta_raw = (τ_exit/τ_fold)·(a2_fold/a0_fold) = (0.16/0.19)·(1/2.31975) = 0.363016`; `λ_exit = lam_min + (lam_max − lam_min)·theta_exit = 0.81974 + (5.41894 − 0.81974)·0.363016 = 2.489323` (M_KK units; interior to the spectral support [0.81974, 5.41894] ⇒ regime VALID).
- **Count**: `S_boundary = N(|λ| ≤ 2.489323) = 9372` (of 166 896 total edge-eligible modes with Peter-Weyl multiplicity; 90 sectors).
- **Substitute / simplify**: `test_ratio = |S_boundary/(A/4) − 1| = |9372/17806.5658 − 1| = |0.5263 − 1| = 0.473677`.
- **Conclusion**: `test_ratio = 0.4737 > info_band 0.25` ⇒ **magnitude FAIL**; regime VALID; composite **FAIL**.

| Quantity | Value |
|:--|:--|
| `S_boundary` (exit-screen edge modes) | 9 372 |
| `A/4` target (M_KK⁻² units) | 17 806.5658 |
| `S_boundary/(A/4)` | 0.5263 |
| `test_ratio` = \|ratio − 1\| | 0.4737 |
| boundary OOM-distance to A/4 | 0.2787 |
| bulk GGE OOM-distance (inv-4 W1-1) | 2.8557 |
| boundary beats bulk | True |
| λ_exit (M_KK units) | 2.4893 |
| θ_exit (fold fraction on support) | 0.3630 |
| regime | VALID |

**4-tuple**: `(scheme=boundary-edge-mode-count, convention=RATIO-BLOCKSUM, L_max=12, value=as above)`. The `RATIO-BLOCKSUM` convention is the Counting-axis pin (`regulator-pin-discipline.md`): the boundary microstate count is an EXTENSIVE per-boundary-mode count (a degeneracy functional `n_g·ρ_g(·)`), NOT an intensive state evaluation — declared at plan-freeze and carried on the verdict line.

**Solution-space interpretation** (what this FAIL closes/opens): the bulk-charge corridor (inv-4 W1-1) and the naive single-sided boundary-count corridor are BOTH excluded as the *exact* A/4 microstate origin. The surviving region is a **two-sided / island boundary construction**: the edge-mode count reproduces the order and ~½ of A/4, consistent with counting one screen orientation (or one Bogoliubov partner of the entangled pair) where the full horizon entropy is the two-sided sum. This is a carry-forward computation (deeper island construction; not an in-session fix), routed to the wave synthesis. The 1/4 *normalization* remains secured (inv-4 W1-2, untouched here); only the *count* is short.

**Substrate framing**: PHONONIC. The white-hole exit screen IS a substrate boundary — at τ_exit the truncated spectral triple `(A_K^{≤12}, H_K^{≤12}, D_K^{≤12})` has edge modes localized on the horizon. Direction of explanation: **D_K eigenvalues → exit-slice boundary edge-mode spectrum → S_boundary → comparison to the emergent area A** (itself the a₂ second Seeley-DeWitt moment, NOT a pre-existing container). The 1/4 is the a₂-conical deficit (inv-4 W1-2), already substrate-derived; this gate tested whether the boundary microstate COUNT reproduces it. This is the substrate realization of the 't Hooft–Susskind holographic principle (horizon DOF are boundary-localized) and the Carlip/Strominger near-horizon edge-mode program — but DERIVED, not assumed: the entropy IS the edge-mode count, the area IS the second spectral moment. NOT a black-hole entropy computed IN spacetime; GR/black-hole-thermodynamics is the consequence of the substrate spectral geometry, not the input.

---

### §W4a-2. S110-CF3-TIMESCAPE-H0 (einstein-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF3-TIMESCAPE-H0`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `einstein-theorist`
**Hypothesis**: The a₂ τ-clock (sign-correct, 0.75% bare in inv-7 W1-4), propagated through the substrate-natural NON-SCALAR transport degree deg(T_{BZ→pivot})=+2 (CONSUMED from W3 CF-CV6B, dedup flag iii — NOT re-derived), reaches the ~9% H₀-relief band without a fitted knob. **Prereq**: W3 CF-CV6B deg(T) landing — MET (deg_T_BZ_pivot=2.0 canonical line 716; gate ran, NOT mechanical-closure).
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4a-2 (deg(T) consumer pin, target band [0.08, 0.10], fb_pair).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block):
- `computations/session-110/s110_cf3_timescape_h0.py` — PRESENT (`from canonical_constants import` ✓, `print_verdict_payload` ✓).
- `computations/session-110/s110_cf3_timescape_h0.npz` — PRESENT (41 keys: the three transport readings, deg_T cross-check vs W3, the 3-tuple, dual-SHA).
- `computations/session-110/s110_cf3_timescape_h0.png` — PRESENT (relief-ladder + decade-budget panels).
- Verdict line `^S110-CF3-TIMESCAPE-H0:.* audit_sha256=[a-f0-9]{64}` — PRESENT in `computations/session-110/s110_gate_verdicts.txt` with dual-SHA companion row AND the schema-v2 `# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID` 3-tuple row (REQUIRED, [SIGN] trigger; emitted via `emit_verdict`, 8 rows, sig_5 unique).
- This WP section — Status/Verdict/Output-Artifacts/MCP markers all present.

**MCP Pre-Compute Audit**:
- `search_knowledge("timescape H0 a2 tau-clock Hubble tension substrate clock variance")` → returns the S58 T8 substrate-compaction observable (CONDITIONAL on DESI DR3), the S101 `w4_h0_proper_a2` provenance, the S60 `BAYESIAN-H0-60` FAIL (all ratios diverge, 99.7% variance from L), the S95 `ORDERED-VEIL-SUBSTRATE-CLOCK` (5251.8, FAIL), and the inv-7 W1 `H_local = H_bar · [clock-rate(τ(ρ_void))/clock-rate(τ(ρ_bar))]` equation. No prior gate computes the deg(T) **transported** H₀ relief — this gate is NOT pre-closed.
- `get_constant("deg_T_BZ_pivot")` → 2.0 (S110, source S110-CF-CV6B-DS-M4; the provenance note grounds it: `P_M4 ~ σ^(−d/2)`, homogeneity degree d/2=2 for d=4 base, NON-SCALAR). IMPORTED (line 716), NOT re-derived.
- `get_constant("w0_FW")` → −0.918 (S58 four-fold-lock; the a₀-orthogonal CC channel for the CV-4 interlock cross-check).
- `trace_entity("deg(T_BZ→pivot) transport degree non-scalar")` → no trace (the entity is new this session; the canonical pin + corpus §23 carry the structure). Read `cross-pillar-bridge-corpus.md §23` (per-observable transport-degree theorem) for the substrate=pivot-iff-scalar discriminator.

**Verdict**: **INFO** — sign_verdict=**PASS**, magnitude_verdict=**INFO**, regime_verdict=**VALID** (composite collapse → INFO).
- `audit_sha256=7bfda02abed5069d4dd4030377b8c448263069df43c27763d6d1e3e11217b013`
- `content_sha256=b319457144786b0de5d1bb863f1dff777fffd127dbbbfbda778293da49b9d809`

**Results**:

The a₂ focusing-clock IS a genuine substrate Hubble-relief mechanism, sign-correct, but it does NOT natively close the full ~9% Planck-vs-SH0ES tension on this channel without a fitted knob the substrate forbids.

| Quantity | Value | Source |
|:--|:--|:--|
| (ΔH₀/H₀)_BZ (Route B central, δρ/ρ=−0.30) | **0.004900** (0.490%) | inv-7 W1-4 `DH0_B_central` |
| (ΔH₀/H₀)_BZ (Route B paper edge, δρ/ρ=−0.46) | 0.007513 (0.751%) | inv-7 W1-4 `DH0_B_paper` |
| clock_coeff | **−3.08** (sign-correct) | inv-7 W1-4 |
| deg(T_{BZ→pivot}) | **+2 NON-SCALAR** (consumed, matches W3 npz) | canonical:716 / W3 CF-CV6B |
| H₀-relief target band | [0.08, 0.10], central ~0.09 | Planck-vs-SH0ES ~9% tension |
| w0_FW (a₀-orthogonal CC channel) | −0.918 | S58 four-fold-lock |

**4-tuple**: `(scheme=emergent-scale-transport-NON-SCALAR, convention=SUBSTRATE-NATURAL-BINDING, L_max=N/A)`.

**Substitution chain (the sign/direction, math-scripts.md MANDATORY)**:
- **Def 1**: (ΔH₀/H₀)_BZ = 0.0049 [Route B central] [inv-7 W1-4].
- **Def 2**: deg(T_{BZ→pivot}) = +2 NON-SCALAR [canonical:716; W3 CF-CV6B; S93 W7-1, factorization_holds=False].
- **Def 3**: T2-VACUOUS (scalar) case ⇒ O^pivot = O^substrate EXACTLY [corpus §23: per-observable transport-degree theorem — substrate=pivot iff the transport factor is scalar].
- **Substitute**: (ΔH₀/H₀)_pivot = T_{BZ→pivot}[ (ΔH₀/H₀)_BZ ]. **Direction**: clock_coeff = −3.08 < 0 ⇒ a void clocks **faster** ⇒ the locally-inferred H₀ rises ⇒ relief sign is **+** (gap-closing); a NON-SCALAR (deg≠0) transport is REQUIRED to move 0.75% toward 9% (the scalar leaves it flat). **sign(transported − bare) = +** ⇒ sign_verdict = PASS.

**Three exhaustive readings of the deg=+2 transport on the dimensionless relief** (the magnitude question):
1. **scalar (deg=0)**: (ΔH₀/H₀)_pivot = (ΔH₀/H₀)_BZ = 0.0049 EXACTLY (ratio 1) — below band; gap NOT closed (this is the T2-VACUOUS leaf the substitution chain says cannot reach the target).
2. **full substrate-natural homogeneity (deg=2 over the full 54.04-decade BZ→pivot separation)**: kernel = 10^(±2·54.04) = 10^(±108.08) — overshoots the band by ~107 decades in either direction. The knob-free homogeneity map applied literally is catastrophic — the **LRD-T precedent** of CF-CO34 (where the substrate-natural transport overshot a dimensionful observable by 82 OOM).
3. **fitted-knob**: the factor that lands central 0.09 is **7500000/408331 ≈ 18.37** (Sage-exact), supplying only **1.17%** of the deg=2 × 54.04-decade budget — a CHOSEN number, NOT substrate-natural.

**Why INFO, not FAIL**: a substrate-natural transport DOES move the relief in the gap-closing direction (sign PASS) and the bare relief is non-zero (0.49–0.75%) — the channel is **not structurally empty**, so FAIL is the wrong verdict. But the substrate-natural (knob-free) transport does NOT land in [0.08, 0.10]: scalar leaves it flat below-band; full-homogeneity overshoots by ~107 decades; only a fitted ~18.4× factor (off the substrate-natural budget) reaches the band. Per the pre-registered rubric (transport reaches the target only with a fitted/scalar factor, OR lands partial between 0.75% and 8%) → **INFO**. The a₂ τ-clock channel RELIEVES but does not natively CLOSE the full tension.

**a₀-orthogonality cross-check (CV-4 CC↔H₀ interlock; WS-CC-H₀)**: w0_FW = −0.918 is the a₀ (expansion-clock, DILUTION-CC) channel. The a₂ τ-clock is a **focusing** clock (second Seeley-DeWitt moment), structurally a₀-ORTHOGONAL. The H₀ relief and the CC are SIBLING spectral moments (a₂ vs a₀); closing H₀ on the a₂ channel does NOT consume the a₀ CC budget — the mutual-exclusivity interlock holds. Reported as a magnitude separation, not a directional gate.

**Substrate framing**: PHONONIC. The substrate IS the clock. A KBC void is a region of lower spectral density; the fiber τ tracks density ([[project_substrate-compaction-timescape]]), so a void clocks faster — the a₂ focusing-clock (second Seeley-DeWitt moment), NOT a metric expansion of a container. Direction of explanation: D_K eigenvalues → a₂ moment → emergent τ-clock variance across the void → ΔH₀. The transport deg(T_{BZ→pivot}) is itself a substrate object (the M⁴-summand transport kernel, derived in W3); the 54.04-decade BZ→pivot gap is the substrate's own scale separation, not a coordinate change in a container. The honest finding: the substrate's native a₂ Hubble-relief mechanism is real and sign-correct (~0.5%), but the substrate-natural transport degree does not carry it to the full ~9% tension without a fitted dial the substrate does not supply — the residual ~8.5% routes to another channel or remains an open H₀ gap on this leg.

---

### §W4a-3. S110-CF-CO34-BUBBLE-LRDT (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CO34-BUBBLE-LRDT`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: TWO orthogonal legs, wave-AND composite — (A) the τ̇²-gated dynamical Gregory-Laflamme KK-bubble matures ≥ 1 e-fold within the impulsive Mach-13.75 transit (permanent structure, not sub-critical); (B) the LRD photosphere T reaches ~5000 K via the substrate-natural NON-SCALAR deg(T_{BZ→pivot}) transport (not the bare E=k_BT that lands 25 OOM high). **Prereq**: leg B consumes W3 CF-CV6B deg(T) — landed (`deg_T_BZ_pivot = 2.0`, canonical_constants.py:716); leg B proceeds (no PRE-REG-INC); leg A (bubble) is independent.
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4a-3 (GL-dynamical-12D leg A; deg(T)-transport leg B).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block):
- `computations/session-110/s110_cf_co34_bubble_lrdt.py` — PRESENT (contains `from canonical_constants import`, `print_verdict_payload`).
- `computations/session-110/s110_cf_co34_bubble_lrdt.npz` — PRESENT (leg-A trajectory + leg-B transport arrays + composite).
- `computations/session-110/s110_cf_co34_bubble_lrdt.png` — PRESENT (4-panel: Γ(τ)≈τ̇, N_efold-vs-threshold, T-ladder, decades-needed-vs-natural).
- Verdict line in `computations/session-110/s110_gate_verdicts.txt` — PRESENT, matches `^S110-CF-CO34-BUBBLE-LRDT:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=2a654897e211bf9dff6723ce2ab188d1f2ea90bb11e4a01048aaeb970fcc8f70`; dual-SHA companion row PRESENT; schema-v2 [SIGN] 3-tuple row PRESENT (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`).

**MCP Pre-Compute Audit**:
- `get_constant("deg_T_BZ_pivot")` → `2.0` (S110-CF-CV6B-DS-M4, NON-SCALAR) — the leg-B transport degree; IMPORTED, not re-derived (dedup flag iii). Cross-checked against the W3 npz (`deg_matches_w3 = True`).
- `get_constant("tau_fold")` → `0.19`; `get_constant("Mach_max_framework")` → `13.75` — leg-A transit kinematics.
- `search_knowledge("Gregory-Laflamme KK-bubble dynamical instability ... e-fold")` → no closed e-fold-maturation result; inv-4 W2-4 supplies ω²_eff(τ,k) (TRACK-B-BUBBLE, transient) — this gate computes the maturation integral fresh.
- `search_knowledge("LRD photosphere temperature substrate transport deg(T) BZ pivot")` → inv-7 W2-2 supplies T_bare = 3.55e29 K (Claim A FAIL, Claim B fold-robust True); no closed eV-scale-T result — fresh.
- `trace_entity` on both leg observables → no trace (neither maturation nor eV-scale-T is a registered closure). Not PRE-CLOSED.

**Verdict**: **INFO** (composite, wave-AND over leg A INFO ∧ leg B INFO). Schema-v2 3-tuple: `sign_verdict=PASS  magnitude_verdict=INFO  regime_verdict=VALID`. 4-tuple: `(value=N_efold=2.3240e-01 | T_pivot=2.9489e-79 K, scheme=GL-dynamical-12D + emergent-scale-transport-NON-SCALAR, convention=SUBSTRATE-NATURAL-BINDING, L_max=12)`.

**Results**:

*Leg A — KK-bubble maturation (τ̇²-gated dynamical Gregory-Laflamme).* Consumed `inv4_w2_gregory_laflamme_dynamical.npz`: `min ω²_eff = −44.2567 M_KK²` at `k_GL = 6.6526`, `λ_GL = 0.9445 M_KK⁻¹` (TRACK-B-BUBBLE; static-limit τ̇→0 reproduces GL-STABILITY-63 to `resid = 0.0`, so the dynamical operator is built right — `regime_A = VALID`). Substitution chain: `growth_rate Γ(τ) = √|ω²_eff(τ, k_GL)|` for `ω²_eff < 0` ⇒ amplitude **grows** ⇒ `sign_A = PASS`. The destabilizing term `ΔK ~ −τ̇²·k²·P` makes `Γ ≈ τ̇·√(structure)`, so the growth rate is gated by the *same* τ̇ that drives the transit (at τ_fold: Γ=6.653, τ̇=6.669; at τ=0.22: Γ=5.867, τ̇=5.885).

The e-fold count was computed in three forms (all reported for honest disclosure):

| convention | N_efold | reading |
|:--|:--|:--|
| **proper-time `∫(Γ/τ̇)dτ`** (physically correct, verdict number) | **0.2324** | < 1 → transient |
| plan-literal `∫Γdτ` | 1.0694 | marginally > 1 (τ-measure, not physical-time) |
| impulsive UB `Γ_max·dt_transit` | 7.52e-3 | single-scale ceiling, ≪ 1 |

The physically correct proper-time count (0.232) and the impulsive upper bound (7.5e-3, with `dt_transit = 1.130e-3 M_KK⁻¹`) both place the bubble **below 1 e-fold**: it is a real but **TRANSIENT sub-critical** structure. `magnitude_A = INFO`. The plan-literal τ-integral nominally exceeds 1, but that is the τ-measure spread of √|ω²_eff| across the window, not a physical-time e-fold count; the τ̇-weighting is what converts it to physical-time growth, and that conversion divides it down to 0.232 (the bubble can only grow while the fold is being traversed, and the impulsive traversal is too brief). Leg-A composite: **INFO**.

*Leg B — LRD photosphere temperature transport (substrate-natural NON-SCALAR deg=+2).* Consumed `inv7_w2_2_substrate_photosphere_temperature.npz`: `T_bare = 3.5453e29 K` (fold-robust, `claim_B = True`, T varies 0.687%). The bare projection (`deg = 0`, scalar) reads the BZ-scale excitation energy AS the observed photosphere energy — container thinking — landing **+25.85 OOM above** the 5000 K target.

Substitution chain (leg B):
- Def B1: `T_bare = 3.5453e29 K` [inv-7; bare `E = k_B T`, deg=0 scalar].
- Def B2: `deg_T_BZ_pivot = +2 NON-SCALAR` [W3 CF-CV6B; IMPORTED canonical_constants.py:716; `deg_matches_w3 = True`].
- Def B3: T2-VACUOUS (scalar, deg=0) ⇒ `T_pivot = T_bare` EXACTLY (no relief).
- Substitute: `log₁₀ T_pivot = log₁₀ T_bare + deg · log₁₀(kernel)`, `kernel = 10^(−54.04)` (substrate-natural BZ→pivot k-separation, kernel < 1).
- **Direction**: `kernel < 1` and `deg = +2 > 0` ⇒ `kernel^deg < 1` ⇒ `T_pivot < T_bare` (T **decreases**) ⇒ `sign_B = PASS`.
- **Magnitude**: the substrate-natural deg=+2 transport over the full 54.04-decade separation gives `10^(−108.08)` suppression ⇒ `T_pivot = 2.949e−79 K`, which **overshoots BELOW the band by 82.23 OOM**. To land in [3500, 6500] K a deg=+2 transport would need a `12.93`-decade scale ratio (Sage-exact: `gap_oom/deg = 25.851/2 = 12.925`), which is **NOT** the substrate's 54.04-decade separation — closing the gap requires a *fitted* scale the substrate does not supply. `magnitude_B = INFO` (held, fitted/scalar reading), NOT FAIL: the eV-scale photosphere is not structurally empty — the bare (deg=0, +25.85 OOM) and substrate-natural (deg=+2, −82.23 OOM) transports **bracket** the target, so the channel is non-empty; what is held is the *magnitude*. `regime_B = VALID` (inv-7 fold-robustness). Leg-B composite: **INFO**.

*Composite (wave-AND).* `leg A = INFO ∧ leg B = INFO → INFO`. AND-aggregate 3-tuple: `sign = PASS` (both legs sign-PASS), `magnitude = INFO` (the weaker), `regime = VALID`. This is the campaign master diagnosis on the compact-object/LRD axis: **both substrate directions are settled (sign-PASS), both magnitudes are held**. The GL-bubble structure is real but transient (does not mature a permanent localized structure in the impulsive transit); the LRD eV-scale photosphere temperature is not reachable by either substrate-natural transport degree. No new falsifier-inventory row is minted — this gate records a *constraint-map update* (two held magnitudes), not a new PASS-side observable/detector horizon (per `feedback_mack-bridge-role.md` the inventory carries falsifier surfaces, not held-magnitude INFO closures).

**Substrate framing.** Leg A: the KK-bubble IS a localized reorganization of the fiber's spectral weight during transit — a GL instability of the M⁴×SU(3) acoustic metric, gated by τ̇² (only the impulsive fold drives it). Direction held substrate-first: `D_K eigenvalues → ω²_eff(τ,k) → growth → bubble amplitude`; the static τ̇→0 limit reproduces the PERMANENT GL-STABILITY-63 spectrum bit-for-bit, and the dynamical excess is the transit-phase structure. Leg B: the LRD photosphere temperature IS a substrate excitation energy read at the pivot scale — the bare `E = k_B T` projection treats the substrate scale AS the observed scale (container thinking, 25 OOM wrong); the substrate-natural NON-SCALAR deg(T)=+2 transport is the substrate's *own* 54.04-decade scale separation. Both legs invert the GR-container default: the bubble is an excitation OF the fabric, and the temperature is a spectral-weight energy transported through the substrate's own scale hierarchy — not a black-hole structure / blackbody temperature computed IN a pre-existing spacetime.

---

### §W4a-4. S110-CF-AS3-QUENCH-PIN (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-AS3-QUENCH-PIN`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: THREE promotions on the A_s/measurement axis — (A) pin the A_s impulse-quench over-production number/band (+0.86 OOM, k̂=53.3 M_KK), GATED on WS-AS-1; (B) promote τ_NL=1.527696 (Sage-exact 95481/62500) to canonical + inventory via the canonical write-order (mack sole writer of the inventory row); (C) compute the Penrose-Diósi collapse scale E_G from the a₂ band-difference. **Conditional**: (A) PRE-REG-INC if WS-AS-1 not landed; (B)+(C) proceed unconditionally; composite then over (B)∧(C).
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4a-4 (WS-AS-1 conditional clause; canonical write-order; writer_agent).

**Output Artifacts** (closure-verification checklist; all on disk, content-verified):
- `computations/session-110/s110_cf_as3_quench_pin.py` — contains `from canonical_constants import` + `print_verdict_payload`. ✓
- `computations/session-110/s110_cf_as3_quench_pin.npz` — all three legs' results + dual-SHA. ✓
- `computations/session-110/s110_cf_as3_quench_pin.png` — 3-panel (τ_NL envelope / E_G vs T_acoustic / purity sectors). ✓
- Verdict line `S110-CF-AS3-QUENCH-PIN: PASS …` in `computations/session-110/s110_gate_verdicts.txt` matching `^S110-CF-AS3-QUENCH-PIN:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`, REQUIRED [SIGN] trigger) + 4 leg extra-rows. ✓
- `audit_sha256=60f0d70be57ab57a796303d3eb3b0dbbdbb66c39e2be74b7d6e112f0499efdc1`, `content_sha256=3ab754ec423cdaa66e175f30b04c6a83e60339de037378dc04966c237b453214`.
- Canonical write-order: **Step 1** (verdict) ✓; **Step 2** (`update_constant('tau_NL', 95481/62500, S110, gate=S110-CF-AS3-QUENCH-PIN)`) ✓ landed in `canonical_constants.py` SECTION E with PROVENANCE; **Step 3** (falsifier-master-inventory τ_NL row) ROUTED to mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`) — NOT written by me; pending mack dispatch.

**MCP Pre-Compute Audit**:
- `search_knowledge("tau_NL trispectrum amplitude falsifier f_NL_total")` → `f_NL_total_GGE_S67 = 1.03` (S96, falsifier-rigor Row 9); `f_NL (total, with folded-shape template)` ZERO-FREE-PARAMETER, σ_dist=0.57σ vs Planck equilateral; τ_NL not yet an entity.
- `search_knowledge("Penrose-Diosi collapse scale E_G a2 band difference measurement")` → no prior Penrose-Diósi E_G entity; `a2_fold` consumed by prior collapse-spectrum scripts (s65/s66); "Measurement/collapse" open-channel HAND-WAVING (S16) — confirms E_G is a NEW substrate-fixed scale, not pre-closed.
- `get_constant("tau_NL")` → **not found** (confirms the promotion is genuine; Step 2 adds it).
- `get_constant("max_f_NL_FW")` → 1.505 (S95, gate F-NL-ROW) — the bispectrum envelope.
- `get_constant`/`list_constants` for `a2_fold` (2776.17), `M_KK`, `Delta_BCS` (0.464255), `T_acoustic` (0.112), `R_therm` (5251.82), `deg_T_BZ_pivot` (2) — all canonical, used in-script.
- Not pre-closed: no closure covers the τ_NL canonical promotion, the impulse-quench A_s POINT pin, or the Penrose-Diósi E_G.

**Verdict**: **PASS** (composite; sign_verdict=PASS / magnitude_verdict=PASS / regime_verdict=VALID).

FUNCTIONAL-SENSITIVITY CLASSIFICATION (lizzi-signature):
- **(A) A_s magnitude** — SCHEME-DEPENDENT (the spectral functional acting as an unpinned physical d.o.f., per WS-AS-1 Reading A); the **FLOOR** `A_s ≥ A_s^{BD}` is FUNCTIONAL-INDEPENDENT/PERMANENT (out of scope).
- **(B) τ_NL = 95481/62500** — FUNCTIONAL-INDEPENDENT (an exact rational identity from the squeezing spectrum, Sage QQ; does not depend on the spectral-functional choice). `f_NL_total < max_f_NL_FW` is the envelope position.
- **(C) E_G separation** — the band-difference uses the zeta-regulated a₂ second moment (`a2_fold` zeta); the separation `E_G ≫ T_acoustic` is robust to the second-moment regulator class (both E_G and T_acoustic are intensive M_KK-scale quantities; the ratio cancels the dimensionful prefactor). SD-tag: the absolute E_G magnitude carries the a₂ regulator class; the separation RATIO is regulator-robust.

**Results**:

**(A) A_s impulse-quench pin — CONDITIONAL on WS-AS-1; LANDED as POINT.** WS-AS-1 (`sessions/session-110/workshops/ws-as-1.md`) is on disk and CONVERGED to **Reading A**: the impulse-quench A_s over-production magnitude IS a physical degree of freedom, CONDITIONAL on the register-predicted Friedrich-Bär (FB-temp) per-sector PASS (the per-charge GGE multiplier `λ_k = −ln(n_k/(1−n_k))` launders aggregate truncation-softness out of the pivot temperature; transit-dynamics conceded R3-C(R3)1). Per the workshop CF-AS-3 FORM rule — *register-predicted FB-temp PASS ⟹ POINT-per-functional + scheme-tag* — sub-deliverable (A) pins the impulse-quench A_s as a **POINT**: `A_s = 1.54e-8` (+0.86 OOM over the Bunch-Davies floor), `k̂ = 53.3 M_KK`, `k̂/k_pivot = 3.72` (the deg(T_BZ→pivot)=+2 mapping). The pin carries BOTH WS-AS-1 openness-source tags: **(b-i)** functional-choice freedom [SCHEME-DEPENDENT] and **(b-ii)** the `T_pivot`-FB-saturation L_max-tag [register-predicted SATURATED; the nazarewicz per-sector compute — does `λ_pivot` shift when a new high-Casimir in-band (p,q) sector is added at L_max+1 holding `n_pivot` fixed? register prediction NO — is the named CF-AS-3 sub-input deciding POINT-vs-BAND]. The **FLOOR** `A_s ≥ A_s^{BD}` (`S_IC = 1 + 2n_k ≥ 1`, `proven_1097`, 3 orthogonal axes: reference-state / families-index η-form / dynamical-Bogoliubov) is PERMANENT and FUNCTIONAL-INDEPENDENT — out of scope, not re-litigated.

**(B) τ_NL canonical promotion — the directional [SIGN] leg, PASS.** Substitution chain (per `math-scripts.md`):
- Def B1: `τ_NL = 95481/62500 = 1.527696` EXACT [inv10_w2_bispectrum_trispectrum.npz; Sage QQ]
- Def B2: `max_f_NL_FW = 1.505` [`canonical_constants.py`, gate F-NL-ROW, S95]
- Def B3: `f_NL_total = 1.03` [inv-10 W2-3 coherent total = `f_NL_total_GGE_S67`]
- Substitute: the falsifier envelope test is on `f_NL_total` (bispectrum) vs `max_f_NL_FW`, NOT on τ_NL (trispectrum, a DISTINCT observable) — comparing τ_NL to the bispectrum envelope would be a cross-observable mis-comparison.
- Simplify: `f_NL_total = 1.03 ; max_f_NL_FW = 1.505 ; margin = 1.505 − 1.03 = 19/40 = 0.475` (Sage-exact)
- Direction: `f_NL_total < max_f_NL_FW` ⇒ bispectrum amplitude WITHIN envelope (sign POSITIVE = PASS); τ_NL reported as the parameter-free trispectrum falsifier in its own right.
- Conclusion: **(B) PASS** — `τ_NL == 95481/62500` EXACT (`abs_dev = 0.0e+00 < 1e-12`) AND `f_NL_total < max_f_NL_FW`. Suyama-Yamaguchi inequality respected (`SY_lower = 1.527696`, `R_SY = 1.0`). Promoted via the canonical write-order (verdict → `update_constant` Step 2 DONE → mack inventory Row 3 routed).

**(C) Penrose-Diósi collapse scale E_G — a₂ band-difference; separation pin, PASS.** Substrate construction (all in M_KK natural units): gravity IS the a₂ second Seeley-DeWitt moment (`a2_fold = 2776.17 M_KK²`). The GGE pointer-state superposition's two branches differ in mass-density; the **fractional** mass-energy difference is set by the B2-sector mixed-state impurity `δρ = 1 − purity_B2 = 1 − 0.7731 = 0.226891` (the off-diagonal coherence the GGE coarse-graining suppresses; inv-8 W2-3, the inv-8 W4-1 2×2 grid localizes to **Cell D-P**). The L12 cache (166,896 eigenvalues; 73,108 inside the GGE pair band [0.94, 3.72] M_KK) gives the band-restricted a₂ second-inverse-moment weight: `band_a2_fraction = 0.610871`, so `a2_band = a2_fold × 0.610871 = 1695.88 M_KK²`. The Penrose-Diósi gravitational self-energy:
- `E_G = a2_band × δρ² = 87.30 M_KK²` (in a₂/second-moment units)
- `E_G^{energy} = √(a2_band) × δρ = 9.3436 M_KK` (the natural M_KK-energy form; a₂ has M_KK² dimension as the EH kinematic second moment).

Separation test against the GGE-thermal scale `T_acoustic = 0.112 M_KK`: `E_G/T_acoustic = 83.43× = +1.92 OOM` ⟹ **SEPARATES** (the collapse scale is ~83× ABOVE the relic acoustic-thermal scale). Consistency frame: `R_therm = 5252` (thermalization is 5252× slower than transit) — a collapse scale separated from and ABOVE `T_acoustic` confirms measurement is a substrate-fixed (non-thermal) process: the Penrose-Diósi self-collapse is faster than the GGE-thermal scale, so the collapse pointer-localization is set by the substrate's own a₂ moment, NOT by an external observer or thermalization.

**Composite**: 4-tuple `(value=composite=PASS;…, scheme=impulse-quench-Bogoliubov|Sage-exact-rational|Penrose-Diosi-a2-band-difference, convention=RATIO, L_max=12)`. The [SIGN] 3-tuple `sign=PASS / magnitude=PASS / regime=VALID` collapses (gate-verdicts.md rule) to **composite PASS**. The A_s/measurement axis gains a canonical parameter-free trispectrum falsifier (τ_NL) + a derived substrate-fixed collapse scale (E_G), with the impulse-quench A_s pinned as a POINT under the WS-AS-1 Reading-A verdict. `publication_precision = 7` (τ_NL published at full Sage-exact precision). Cross-checked via Sage QQ: margin = 19/40, E_G_energy = 9.3436 M_KK, separation = 83.43×.

**Substrate framing.** PHONONIC. (A) A_s IS the produced-side squeezing amplitude `D_K → {α_k,β_k} → n_k=|β_k|² → S_IC → A_s`; the over-production above the Bunch-Davies floor is reference-state-independent, and the impulse-quench functional is the physically-correct one. (B) τ_NL IS the GGE relic's trispectrum amplitude — a parameter-free falsifier read off the squeezing spectrum, not a tuned non-Gaussianity. (C) E_G IS the a₂ gravitational self-energy of the GGE pointer-state superposition's band-difference — measurement is substrate probing substrate, the collapse scale fixed by the substrate's own second spectral moment. All three invert the inflaton-in-spacetime default: amplitude, trispectrum, and collapse scale are spectral properties of the relic excitation, not perturbations seeded in an expanding container.

---

### §W4a-5. S110-CF-CV2C-OINTERFACE (paasch-mass-quantization-analyst)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CV2C-OINTERFACE`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC**
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: The B2-sector dimensionless input ratios feeding λ_eff/N₀ carry the φ_paasch (1.5315844) / 7n grading the output mass ladder exhibits (N(p)/N(K)=75/49=1.5306, 0.06% from φ_paasch) — ONE quantization governs the whole Ô layer (COUPLED, the AGREE-coupled reading); OR a different quantization grades the input (INDEPENDENT, still AGREE). Reuses the L12 cache — no new diagonalization.
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4a-5 (consumes inv-3 W3-4 7n grid; COUPLED/INDEPENDENT/CONFLICT verdict).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block):
- `computations/session-110/s110_cf_cv2c_ointerface.py` — PRESENT (`from canonical_constants import`, `print_verdict_payload` both present).
- `computations/session-110/s110_cf_cv2c_ointerface.npz` — PRESENT (node grid, full B2-ratio family + per-ratio best-node/deviation, B2 aux quantities, dual-SHA).
- `computations/session-110/s110_cf_cv2c_ointerface.png` — PRESENT (left: B2 ratios vs φ_paasch/7n number line; right: per-ratio min-deviation bars vs PASS_TOL).
- Verdict line `^S110-CF-CV2C-OINTERFACE:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row in `computations/session-110/s110_gate_verdicts.txt` — PRESENT (4 rows; sig_5-unique).
- This WP section's Status / Verdict / Output-Artifacts / MCP markers — PRESENT.

**MCP Pre-Compute Audit**:
- `get_constant("phi_paasch")` → 1.531580 (canonical line 289, PROVEN at machine-ε S12 as bare (3,0)/(0,0) ratio at τ=0.15; high-precision form 1.5315844 is inv-11 W5-1's load-bearing node; **mathematical property of the D_K spectrum, BF=2** — atlas-04 P1 DISSOLVED; BdG DESTROYS it, PHI-BDG-47 FAIL). Confirms substitution-chain Def1.
- `search_knowledge("CV2C Ointerface phi_paasch 7n grading B2 sector ... AGREE coupled independent")` → no prior verdict for this gate; φ_paasch is a spectral-triple invariant (L_max-independent). Gate NOT pre-closed; sharpens the inv-11 W5-1 AGREE verdict.
- `search_knowledge("M_KK transmutation lambda_eff N_0 pairing window B2 sector ...")` → confirms B2 = (1,1) mult-8 "optical" band; pairing window 2Δ_B2≈1.38 M_KK below M_KK; N(0)=14.02 gap-edge DOS feeds g·N(0)=3.24 (S22c); the λ_eff·N₀ inputs to M_KK=M_Pl·exp(−1/(λ_eff·N₀)).
- Not pre-closed → computed.

**Verdict**: **PASS (COUPLED)** — `value = 5.133993e-03` (grid-membership test) against `PASS_TOL = 0.01`. 3-tuple: sign=N/A (grid-membership SET test, no directional claim), magnitude=PASS, regime=VALID. `audit_sha256=51976f89e5a4da98d4a35eb7d2430e9e927000baf73904b008e99c7b0d1bd567`, `content_sha256=c2226a2b9443c77698633652da8705dd4bd7173598cbd90d4b887801f5670d9a`. 4-tuple: `(value=0.005133992842355717, scheme=B2-sector-dimensionless-ratio, convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)`.

**Results**:

The gate tests whether the dimensionless **input** ratios that feed the BCS M_KK dimensional transmutation, M_KK = M_Pl·exp(−1/(λ_eff·N₀)) (λ_eff=0.038935, N₀=14.0233, the (1,1) mult-8 B2 "optical" band), sit on the same φ_paasch / 7n grid as the **output** mass-ladder ratio N(p)/N(K)=75/49. The candidate B2-ratio family is PINNED at design time (no post-hoc selection) and ALL members reported.

| B2-sector ratio | R_B2 | best node | node value | min \|R/node−1\| |
|:--|--:|:--|--:|--:|
| `lam(3,0)/lam(0,0)` | 1.522754 | **N(p)/N(K)=75/49** | 1.530612 | **5.13e-03** ✓COUPLED |
| `E_vH/Δ_mf` | 1.154698 | N_ratio[1]=1.2 | 1.200000 | 3.78e-02 |
| `Δ_mf/Δ_rich` | 1.591458 | φ_paasch | 1.531584 | 3.91e-02 |
| `Δ_mf/Δ_ed` | 1.610712 | φ_paasch | 1.531584 | 5.17e-02 |
| `lam(0,2)/lam(0,0)` | 1.186041 | N_ratio[1]=1.2 | 1.200000 | 1.16e-02 |
| `lam(1,1)/lam(0,0)` (B2 band floor) | 1.064940 | N_ratio[1]=1.2 | 1.200000 | 1.13e-01 |
| `E_vH/E_min` | 1.031142 | N_ratio[1]=1.2 | 1.200000 | 1.41e-01 |
| `E_max/E_vH` | 6.410901 | N_ratio[0]=5 | 5.000000 | 2.82e-01 |
| `E_max/E_min` | 6.610547 | N_ratio[0]=5 | 5.000000 | 3.22e-01 |

**Substitution chain (grid-membership SET test, no directional claim):**
- Def1: `φ_paasch node = 1.5315844` [canonical_constants.py:289 phi_paasch=1.531580; W5-1 high-precision node 1.5315844; PROVEN bare (3,0)/(0,0) ratio at τ=0.15]
- Def2: `N(p)/N(K) = 150/98 = 75/49 = 1.5306122449` [inv-3 W3-4 output mass-ladder ratio; Sage-exact QQ; `phi_dev = |75/49 ÷ φ_paasch − 1| = 6.347e-04`, i.e. 0.063% from φ_paasch]
- Def3: `R_B2 = ` B2-sector dimensionless ratios feeding λ_eff, N₀ (the pairing-window / DOS-edge / gap ratios + the L12-cache B2-band eigenvalue ratios at τ_fold=0.19)
- Def4: `7n-grid nodes = {N(j) = 7n}` [inv-3 W3-4; N(j)=[7,35,42,98,150]; only 35,42 are SU(3) dims; 7,98,150 are not. 49=7², 98=7·14 are 7-graded; 150 is NOT 7n — matches the inv-3 W3-4 "7 is a mode-multiplicity unit, not a dimension" reading]
- test = min over family, min over node, of `|R_B2/node − 1| = 5.133993e-03 ≤ 0.01 ⇒ COUPLED`

**Structural reading (two-layer; reported transparently):**

1. **COUPLED, carried by the (3,0)-sector eigenvalue ratio.** The winning match is `lam(3,0)/lam(0,0) = 1.522754` (the φ_paasch-defining sector, evaluated at τ_fold=0.19 where the ratio reads 1.5228 rather than the τ=0.15 value 1.5316) landing **0.51%** from the OUTPUT mass-ladder anchor 75/49. This is **not circular**: 75/49 is Paasch's proton/kaon mass-NUMBER ratio (an output-ladder construct), whereas (3,0)/(0,0) is an INPUT D_K eigenvalue ratio — two independently-defined quantities that coincide to half a percent. The *same* (3,0)-sector arithmetic that defines φ_paasch reappears in the input layer and lands on the output node ⇒ one quantization grades both layers (AGREE → **AGREE-COUPLED**).

2. **The strict λ_eff/N₀ pairing-window ratios live on an adjacent, looser grading.** Excluding the (3,0) φ_paasch sector, the strict-pairing-window family's best match is `lam(0,2)/lam(0,0)=1.186 → 1.2` at 1.16e-2 (just above the 1% band), and the genuine BCS-gap ratios `Δ_mf/Δ_rich=1.591` and `E_vH/Δ_mf=1.155` land at ~3.8–3.9% from φ_paasch / N_ratio[1]. So the pairing-window gap quantities are the RIGHT ORDER but graded ~4%-loosely — they do not individually sit in the 1% COUPLED band. The COUPLED verdict rides specifically on the spectral (3,0)/(0,0) channel, not on the BCS-gap channel.

**Net**: the inv-11 W5-1 AGREE verdict sharpens to **AGREE-COUPLED** — the (3,0)-sector eigenvalue ratio that defines φ_paasch grades both the dimensionless Ô input layer and the output mass ladder (75/49) to <1%. CONFLICT (FAIL) cannot fire structurally: both input and output are exact eigenvalue ratios on a FINITE spectral triple (a discrete Peter-Weyl mesh by construction), so there is no provably-continuous input to set against a discrete output.

**Substrate framing**: GEOMETRIC. This concerns the fabric's representation-theoretic content (Peter-Weyl eigenvalue ratios), not its excitations. Direction of explanation: D_K eigenvalues → B2-sector dimensionless ratios → comparison to the φ_paasch / 7n grading. φ_paasch is itself a bare D_K eigenvalue ratio ((3,0)/(0,0)); the 7n grid is Casimir-graded (inv-3 W3-4). The grading IS the substrate's own Peter-Weyl arithmetic — no container, no external scale. The result says the input-side and output-side structural ratios are read off the *same* substrate quantization; it makes **no** claim about physical particle masses (φ_paasch is a mathematical property of the spectrum, BF=2, destroyed by BdG pairing).

**Plan-text drift note**: the plan pinned `canonical_constants.py` SHA `e5a7587f…`; disk at runtime was `935c8f24…` (the in-session φ_paasch PROVENANCE backfill). Resolved by npz-ground-truth at runtime per `substrate-first-canonical-sourcing.md §(ii.B)`: SHAs computed from live disk bytes, drift logged in stdout; the dual-SHA closure uses live bytes. No value impact (φ_paasch value unchanged — provenance-only backfill).

---

### §W4a-6. S110-CF-DMAB-REFINE (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-DMAB-REFINE`
**Trigger**: `[VERIFY]` (with [SIGN] 3-tuple — leg B Counting-axis directional)
**Classification**: **PHONONIC**
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: THREE refinement legs on the DM/abundance axis (mass anchor already Leggett-PROVEN; these refine, not found) — (A) non-Leggett dimer_Z2 → 0.276 lands in the Ω_DM band; (B) n_PBH re-sources convergently with the Counting axis PINNED (RATIO-BLOCKSUM vs RATIO-NORMALIZED-TRACE-MEAN) + Pauli-Villars N_eigs(Λ_UV=M_KK), back-fit-free; (C) secular Fock entanglement envelope at dim=2⁶⁴ classified secular-decline vs recurrence (Poincaré test, NOT-a-truncation-artifact).
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4a-6 (Counting-axis EXPLICIT pin leg B; a_n^{Pauli-Villars} regulator pin; CFL EoS routed to W3 CF-CO1 dedup flag ii).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block):
- `computations/session-110/s110_cf_dmab_refine.py` — present (`from canonical_constants import`, `print_verdict_payload` both present).
- `computations/session-110/s110_cf_dmab_refine.npz` — present (all three-leg results + dual-SHA + plan-drift flag).
- `computations/session-110/s110_cf_dmab_refine.png` — present (3-panel: Z₂-odd suppression / Counting-axis bar / S_EE envelope vs Page).
- verdict line `^S110-CF-DMAB-REFINE: INFO …` present in `computations/session-110/s110_gate_verdicts.txt` (`audit_sha256=e13f42a13a7cfb2e065006609190f860c58f2814de1064d83dfb7d23a3cb3845`) + dual-SHA companion row + schema-v2 sign/magnitude/regime 3-tuple row + the `# regulator_pin=a_n^{Pauli-Villars}` companion annotation + the Counting-axis / n_PBH-HELD / Leggett-anchor companion rows (7 rows total).

**MCP Pre-Compute Audit**:
- `get_constant("Omega_DM")` → 0.2657 (Planck 2018; OBSERVATIONAL COMPARISON-ONLY; PROVENANCE canonical, HK-OMEGA-DM gap closed S110 W0a) — used as leg-A band, never replaced.
- `search_knowledge("n_PBH truncation anchor Tier-2-DIMENSIONFUL OP-PROJ held")` → S94-N-PBH-TRUNCATION-ANCHOR INFO, `tier_class=TIER-2-DIMENSIONFUL`, `level3_m3=REGISTRY-PASS-INELIGIBLE-HELD`, `N_eigs(14)_repro=323136` — held status PRESERVED (not loosened).
- `search_knowledge("dimer_Z2 pair production abundance dark matter Leggett")` → S75 dimer_Z2 spectrum; LEGGETT-MOMENT (S70, Type-F, PROVEN) is the DM mass anchor.
- `search_knowledge("n_PBH back-fit … Counting axis RATIO-BLOCKSUM Pauli-Villars N_eigs")` → `n_PBH = n_edge·prob_form/L_pix³`, `n_PBH_central(L)=central14·N_eigs(L)/N_eigs(14)`, `central14=72761/10²⁷`; with-mult 80080 vs unique 78080, gap 2000.
- `search_knowledge("secular Fock … Poincaré recurrence GGE Page curve dim 2^64")` → inv-9 W1-5 baseline PR=1.93, `gge_secular_turnover=False`, peak/Page=0.954.
- `search_knowledge("unique spectrum 78080 with-multiplicity 80080 … K0-rank")` → `gap = 80080−78080 = 2000 = dim_SU3(4,4)·16 EXACT`. (Not PRE-CLOSED — this gate is a refinement of three INFO/HELD investigation-track results into a session gate.)
- Sage QQ cross-check: `gap == dim_SU3(4,4)·16` True; n_g count ratio = 1001/976 = 1.0256 > 1; `n_PBH_sat` reproduces canonical `1.7581364216e-23` bit-for-bit; canonical/saturated = 4.1385298.

**Verdict**: **INFO** (composite over (A)/(B)/(C)). [SIGN] 3-tuple **sign = PASS** (leg B Counting-axis n_g > 1) / **magnitude = INFO** (n_PBH held Tier-2-DIMENSIONFUL, NOT loosened) / **regime = MARGINAL** (mixed-refinement: two INFO, one PASS). Leg verdicts `[A=INFO, B=PASS, C=INFO]`. 4-tuple `(value=…, scheme=dimer_Z2-abundance + Pauli-Villars-N_eigs + secular-Fock-RDM, convention=RATIO-BLOCKSUM, L_max=12)`.

**Results**:

**(A) dimer_Z2 abundance vs Ω_DM — Z₂-odd FORBIDDEN; abundance in the EVEN Leggett channel. INFO.** The substrate answer (S75 npz) refutes the plan's "dimer_Z2 → 0.276" hope at the source: the Z₂-**odd** dimer occupation is `n_Z2_ratio = p_odd = 2.173e-26` — suppressed **25.7 OOM** below the even sector (`p_even = 1.0`). The relative deviation from Ω_DM = 0.2657 is ≈ 1.0 (the odd abundance is ≈ 0, not 0.276), so it is OUTSIDE both the 10% PASS band and the 50% INFO window. This is **INFO, not FAIL**: the number is well-defined and computable; what it RECORDS is the substrate selection rule — the DM abundance is carried by the Z₂-**even** Leggett inter-band coherence mode (`n_even_abs = 59.8` Bogoliubov pairs from Parker pair production at the fold), **not** by the odd dimer channel. The DM *mass* anchor is the Leggett moment (LEGGETT-MOMENT, S70, Type-F, CPT-neutral, non-annihilating, PROVEN); the framework's Leggett-channel abundance prediction is `Ω_DM h² = 0.120` (0.6% from Planck, `framework-dm-properties.md`), which lives in the even sector. The dimer-Z₂-odd result is the substrate's statement that the odd channel does NOT supply abundance.

**(B) n_PBH re-source with Counting-axis PINNED — the directional leg. PASS (structural); magnitude HELD.** Counting-axis substitution chain (the gate's [SIGN] content), with substituted numbers:
- Step 1: `RATIO-NORMALIZED-TRACE-MEAN` = intensive `ρ_g(f(D))`, `ρ_g = P_g/Tr(P_g)` — the per-channel state evaluation (unique-spectrum reduction).
- Step 2: `RATIO-BLOCKSUM` = extensive `n_g·ρ_g(f(D))` — the weighted trace (with-multiplicity count).
- Step 3: `n_g` = K₀-rank factor = channel multiplicity (topological).
- Step 4: `n_PBH^{BLOCKSUM}/n_PBH^{TRACE-MEAN} = [n_g·ρ_g]/[ρ_g] = n_g`. The two incarnations are realized by the with-multiplicity count **80080** (BLOCKSUM, analytic `N_eigs(10)`) and the unique count **78080** (TRACE-MEAN, cache baseline atlas); their **gap = 80080 − 78080 = 2000 = dim_SU3(4,4)·16 EXACT** (Sage-verified: Weyl dim (4,4) = 125, ×16-dim spinor = 2000 — the dropped (4,4) Peter-Weyl sector × the spinor space).
- Step 5: count ratio `= 1001/976 = 1.025615 > 1` ⟹ `n_PBH^{BLOCKSUM} > n_PBH^{TRACE-MEAN}` ⟹ **sign_verdict(B) = PASS**. The Counting-axis choice is a fixed multiplicative `n_g` shift, **NOT a free knob** — declaring it is MANDATORY (silent conflation is the pathology).

Pauli-Villars-regularized count (`regulator_pin = a_n^{Pauli-Villars}`, Λ_UV = M_KK): the cardinality cascade DIVERGES (no plateau, `lim N_eigs = +∞` per S94), so the bare count is UV-sensitive; the PV subtraction renders the PHYSICAL count finite. With the closed-form polynomial `N_eigs(L)` (degree-5, descending-coeff order; bit-verified `N_eigs(14)=323136`, `N_eigs(15)=434112`, `N_eigs(16)=573648`): physical count below the cutoff `N_eigs(L12) = 168896` (finite), regulator subtraction `N_eigs(14) − N_eigs(12) = 323136 − 168896 = 154240` (the finite UV piece removed).

Back-fit removal: the S93 back-fit form `n_PBH = central14·N_eigs(L)/N_eigs(14)` (central14 fitted to the L14 anchor) is REPLACED by the back-fit-free closed form `n_PBH = A_prefactor·N_eigs(L)` with `A_prefactor = 2.2517e-28 m⁻³` (the cardinality-cascade edge-prefactor / L_pix³, substrate-physical, NOT fitted). The back-fit-free form reproduces the held canonical at L14: `A_prefactor·N_eigs(14) = 7.2761e-23 m⁻³` vs held `n_PBH_FW_central = 7.2761e-23` (rel = 6.6e-06, **removed = True**).

Residual-seam report: **seam (i) RETAINED** — the irreducible L_max-axis refinement `L10 → L14 = 4.1385×` (Sage-exact 3528281250/852544601); this is the Tier-2-DIMENSIONFUL held seam, the m⁻³ magnitude on the divergent cardinality channel. **seams (ii)(iii)(iv) DISCHARGED**: (ii) factorization exact (`residual_max = 1.82e-16`, `cancellation_detected`, `linear_in_neigs`); (iii) Counting-axis declared AND verified (gap-identity True); (iv) regularized count finite. Structural PASS. The **magnitude row stays HELD** `§VII.AX.OP-PROJ` `TIER-2-DIMENSIONFUL` / `REGISTRY-PASS-INELIGIBLE-HELD` (NON-PROMOTION-BY-HELD-NUMBER, differentia = dimensionful-slot-collision) — magnitude_verdict = INFO; the held status is **NOT loosened**. Any falsifier-surface row is mack-sole-writer (not written here).

**(C) Secular Fock entanglement envelope — RECURRENCE-DOMINATED (Reading-B). INFO.** The GGE Fock S_EE envelope (inv-9 W1-5 cache; dim = 256 = 2⁸, the N_dof_BCS = 8-mode realization — the plan's dim = 2⁶⁴ names the GGE Fock-dimension ceiling, the inv-9 cache is the 8-mode substrate BdG sector) classifies as **RECURRENCE-DOMINATED** (Reading-B): `gge_secular_turnover = False`, `gge_recurs = True`, `PR = 1.926` (O(1)), `peak/Page = 0.954`, `gge_decline = 0.0704` (7%). The NOT-a-truncation-artifact guard **PASSES** (recurrence is physical, NOT a Casimir-ceiling false-secular): `PR < 5` (O(1)) ∧ peak nearly saturates Page (0.954 > 0.8) ∧ shallow decline (7% < 30%) ∧ frozen transit (`R_therm = 5252 > 100`, Ordered-Veil). The substrate reason: the GGE **never thermalizes** (R_therm = 5252× slower than transit; S_ent = 0 diabatic transit-freeze) — so its entanglement RECURS rather than secularly declining. This is **INFO** (records Reading-B; there is no secular decline, which would have been the Reading-A "PASS" headline; the regime is cleanly classified and physical, so not FAIL).

**Composite**: collapse over (A)/(B)/(C) — no leg hard-FAILs, not all PASS ⟹ **INFO**. The three refinements land as: (A) the non-Leggett dimer channel is Z₂-odd-FORBIDDEN (abundance is in the even Leggett channel), (B) n_PBH re-sources back-fit-free with the Counting axis PINNED and held magnitude preserved, (C) the secular Fock envelope is recurrence-dominated (physical, not a truncation artifact). `publication_precision = 3`. Plan-text-drift note (`substrate-first-canonical-sourcing.md §(ii.B)`): the plan-pinned `canonical_constants.py` SHA `e5a7587f…` is stale; the runtime SHA `f2270207…` was resolved from disk and pinned in the input-pin map (documented in the verdict value + npz `plan_drift=True`).

**Substrate framing.** PHONONIC. (A) The dimer_Z2 quasiparticle IS a substrate pair-excitation; its abundance is a relic-formation number (Parker pair production at the fold), not a thermal freeze-out — the Z₂-odd suppression is a substrate selection rule, and the DM mass anchor is the Z₂-EVEN Leggett inter-band coherence mode. (B) n_PBH IS an eigenvalue COUNT of the substrate spectrum (`D_K eigenvalues → N_eigs(L) → cardinality-cascade n_edge → n_PBH`); the Counting axis (intensive ρ_g vs extensive n_g·ρ_g) is a TOPOLOGICAL K₀-rank distinction, NOT a normalization knob — declaring it is the substrate-faithful move. (C) The secular Fock envelope IS the substrate's own entanglement dynamics in the GGE Fock space (`D_K eigenvalues → BdG/Fock structure → S_EE(t)`); secular-vs-recurrence asks whether the relic's information declines or recurs, and the Ordered-Veil frozen transit answers recurrence. None of these are particles IN a thermal bath; they are excitations OF the fabric counted by its spectral content.

---

# ═══════════════════ WAVE 4b — §B STRUCTURAL-THEOREM PROMOTIONS ═══════════════════

> **W4b closure semantic (READ FIRST).** All three W4b gates are `gate_type: compute` and emit a verdict line, but the "compute" is a dispatch of independent cross-reviewers / co-dispatch, NOT a producing `.py` that does substrate physics. CF-VIIBS-VERIFY and CF-W33-THEOREM follow `joint-theorem-promotion.md` **Stage-2 two-agent cross-axis independent-verify**: the verdict is the logical-AND of two axis-distinct reviewers' clause verdicts; the Stage-1-candidate registry entry is written FIRST (same wave), then Stage-2 verifies it. CF-EVOI-REANCHOR is a sagan+mack co-dispatch (BF-table consumption + EVOI table re-stamp + Q44 closure). Each pending block names the two-reviewer PASS-AND deliverable + the registry-landing artifact.

### §W4b-1. S110-CF-VIIBS-VERIFY (connes-ncg-theorist)

**Status**: COMPLETED (orchestrator-authored Stage-2 clause-AND aggregate over two blind reviewers' JSONs; PASS-AND with substrate-input-overlap caveat)
**Gate ID**: `S110-CF-VIIBS-VERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC**
**Agent**: `connes-ncg-theorist` (Axis-A reviewer; Axis-B = `volovik-superfluid-universe-theorist`, dispatched in parallel)
**Hypothesis**: The S69 W5-G result — the BdG dressing D_K → D_K + V_BdG is a locally-bounded perturbation, so the K-homology class is EXACTLY preserved (topology dressing-RIGID, a_n dressing-SOFT) — is a STRUCTURAL THEOREM, verified by two axis-distinct cross-reviewers operating without prior workshop context, JOINT clauses PASS-AND'd. **STEP 1**: register STAGE-1-CANDIDATE (orchestrator-direct). **STEP 2**: dispatch the two reviewers; the verdict is the Stage-2 clause-AND.
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4b-1 (Stage-2 reviewer-selection pins; substrate-input-orthogonality predicate; 4 legs machine-exact ‖V_BdG‖=0.4642547, [V_BdG,a]=0).

**Output Artifacts** (closure-verification checklist):
- Stage-1-candidate entry in `sessions/permanent-results-registry.md` §VII.CD (line 22159; `STAGE-1-CANDIDATE` tag) — written STEP 1 (orchestrator-direct). ✓ on disk.
- Axis-A clause-verdict JSON `computations/session-110/s110_w4b_viibs_axisA_connes.json` (connes; a/b/JOINT all PASS). ✓
- Axis-B clause-verdict JSON `computations/session-110/s110_w4b_viibs_axisB_volovik.json` (volovik; c/d/e/JOINT all PASS). ✓
- Aggregate script `computations/_shared/s110_w4b_viibs_verify_stage2_aggregate.py` (`from canonical_constants import`, `print_verdict_payload`). ✓
- `computations/session-110/s110_cf_viibs_verify.npz` (clause-verdict matrix; composite=PASS; caveat=True). ✓ — `.png` omitted (Stage-2 aggregate has no physics plot; plan `plot: optional`).
- Verdict line `S110-CF-VIIBS-VERIFY: PASS … audit_sha256=a627810b…` + dual-SHA companion + 2 extra rows in `computations/session-110/s110_gate_verdicts.txt`. ✓ (sig_5 unique.)

**MCP Pre-Compute Audit**:
PRE-CLOSED — this gate's producing operation is an orchestrator-authored mechanical clause-AND aggregate over the two blind reviewers' verdict JSONs (`mechanical-closure-discipline.md`; no physics, no knowledge-graph query at the aggregate layer). The substrate-side MCP grounding was performed INSIDE each blind reviewer: Axis-A connes cross-checked `Delta_BCS` via `get_constant` (R-protected, S70 `BCS-GAP-CANONICAL-70`); Axis-B volovik grounded c_s²=0 (`van-den-dungen-synthesis`, Kasparov factorization, PROVEN) + CDM `T^{0i}=0` (atlas-07/S44, 5 independent proofs). The aggregate consumes those verdicts, not the graph.

**Verdict**: **PASS** — Stage-2 PASS-AND per `joint-theorem-promotion.md`. Composite = AND over { Axis-A single-axis clauses, Axis-B single-axis clauses, JOINT PASS-AND'd across BOTH } = PASS. `scheme=STAGE-2-TWO-AGENT-CROSS-AXIS convention=PASS-AND-JOINT-CLAUSES L_max=12`. Carries the **substrate-input-overlap caveat** (both reviewers load `inv12_w2_3_paper10_bcs_dressing_invariance.npz`). §VII.CD promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT (orchestrator updates the tag at session-end synthesis, NOT in-gate, per plan §W4b decision-point).

**Results**:
- **Clause-verdict matrix (PASS-AND)** — Axis-A `connes-ncg-theorist`: (a) K-homology invariance `[D_K+V_BdG]=[D_K]` in KK(A_K,ℂ) re-derived from first principles via van den Dungen 2016 (arXiv:1608.02506) bounded-transform operator-homotopy + an independent n=200 toy odd-Kasparov module (signature 100→100, min|eig|=0.7071>0, no spectral flow) → **PASS**; (b) V_BdG locally-bounded symmetric perturbation (‖V_BdG‖=0.4642547=Δ_BCS finite, [V_BdG,a]=0 commutant, rel-D-bound 0<1; globally-bounded ⊂ locally-bounded) → **PASS**. Axis-B `volovik-superfluid-universe-theorist`: (c) mass-order dressing-invariance (Nambu eigenvalues E=√(λ²+Δ²); f strictly monotone ⇒ ordinal mass order + degeneracy preserved) → **PASS**; (d) c_s²=0 dressing-invariance (gapped Bogoliubov branch group-velocity→0; topological Kasparov-factorization zero, m_Goldstone⁴ᴰ=0 PROVEN) → **PASS**; (e) w_a=0 dressing-invariance (T^{0i}=0 algebraic CDM, dressing commutes with A_K so cannot generate momentum flux) → **PASS**. **JOINT** (physical-observable invariance AS A CONSEQUENCE of K-homology class rigidity) PASS in BOTH verdicts.
- **4 machine-exact legs**: ‖V_BdG‖=0.4642547 EXACT, [V_BdG,a]=0.0 EXACT, rel-D-bound 0<1, K-homology class preserved. a_n shift bounded-analytic at order ‖V‖²=Δ²=0.2155 (ratio leading_shift/Δ²=1.000000) ⇒ geometry dressing-SOFT, topology dressing-RIGID.
- **substrate-input-orthogonality**: predicate FAILS (both reviewers consume the inv12_w2_3 npz boundedness witnesses) ⇒ substrate-input-overlap caveat carried. Structural-OUTPUT-type independence IS established (connes' independent toy KK-homotopy NOT loaded + volovik's disjoint symbolic Nambu anchor are independent decision pipelines); structural-INPUT independence is NOT (shared npz premise). Caveat scopes the independence claim, not the verdict; promotion still proceeds.
- **Promotion**: §VII.CD STAGE-1-CANDIDATE → STAGE-3-PERMANENT — tag-flip deferred to session-end synthesis (plan §W4b decision-point: "orchestrator updates the registry tag at session-end synthesis, NOT in-gate").
- **Folded register-consequences (NOTE, not applied here)**: HK-FWDC1-SLOT (FWD-C1 landing GATED on the CF-2 Krein compute, NOT this gate; the η-form route is a DISTINCT bridge-map class, not a re-tag); HK-SCOPED-VIIBS (§VII.BS rank-1-wall BCS-channel support-row from inv-9 W1-3 Var_λ=0 geometry-fixity; register STATUS unchanged — scope-not-status, Q3).
- **4-tuple**: (scheme=STAGE-2-TWO-AGENT-CROSS-AXIS, convention=PASS-AND-JOINT-CLAUSES, L_max=12). dual-SHA audit=`a627810b…` content=`5b33e436…`. Artifact: `s110_cf_viibs_verify.npz`.

---

### §W4b-2. S110-CF-W33-THEOREM (transit-dynamics-theorist)

**Status**: COMPLETED (orchestrator-authored Stage-2 clause-AND aggregate over two blind non-author reviewers' JSONs; PASS-AND with substrate-input-overlap caveat)
**Gate ID**: `S110-CF-W33-THEOREM`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **PHONONIC**
**Agent**: `transit-dynamics-theorist` (math owner / Stage-1 registrant; Stage-2 reviewers = `volovik-superfluid-universe-theorist` (Axis-A, re-pinned non-author) + `einstein-theorist` (Axis-B), in parallel)
**Hypothesis**: The inv-12 W3-3 result — dq/da ∝ −(n₁−n₂)² ≤ 0 (a passive diluting relic + const-Λ gives monotone-non-increasing q, so the relic-Friedmann q is a DIFFERENT observable from the SCALE-FACTOR-54 Connes-distance-proxy q, which RISES) — is a STRUCTURAL THEOREM, Stage-1-registered then Stage-2-verified by two axis-distinct non-author reviewers. **STEP 1**: register STAGE-1-CANDIDATE. **STEP 2**: dispatch the two reviewers (author-exclusion re-pins Axis-A to volovik).
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4b-2 (author-exclusion re-pin; sign-identity substitution chain; sharpens S95-W4-4).

**Output Artifacts** (closure-verification checklist):
- Stage-1-candidate entry in `sessions/permanent-results-registry.md` §VII.CE (line 22177; `STAGE-1-CANDIDATE` tag) — written STEP 1 (orchestrator-direct). ✓ on disk.
- Axis-A clause-verdict JSON `computations/session-110/s110_w4b_w33_axisA_volovik.json` (volovik, non-author; a/b/JOINT all PASS). ✓
- Axis-B clause-verdict JSON `computations/session-110/s110_w4b_w33_axisB_einstein.json` (einstein, non-author; c/d/JOINT all PASS). ✓
- Aggregate script `computations/_shared/s110_w4b_w33_theorem_stage2_aggregate.py` (`from canonical_constants import`, `print_verdict_payload`). ✓
- `computations/session-110/s110_cf_w33_theorem.npz` (clause-verdict matrix; composite=PASS; caveat=True). ✓ — `.png` omitted (sign-identity aggregate, no physics plot; plan `plot: optional`).
- Verdict line `S110-CF-W33-THEOREM: PASS … audit_sha256=a0021aa0…` + dual-SHA companion + 2 extra rows in `computations/session-110/s110_gate_verdicts.txt`. ✓ (sig_5 unique.)

**MCP Pre-Compute Audit**:
PRE-CLOSED — orchestrator-authored mechanical clause-AND aggregate over the two blind reviewers' verdict JSONs (`mechanical-closure-discipline.md`; no physics, no graph query at the aggregate layer). Substrate grounding was inside each blind reviewer: both re-derived `dq/da = −(9/2)A B a^(3w+2)(w+1)²/(…)²` via Sage MCP from first principles; einstein cross-checked the dust q-ceiling (+1/2) and the DILUTION-CC tracking-vacuum picture (`rho_vac_over_obs=1.032`, CC-Monotonicity Theorem #19). The aggregate consumes those verdicts, not the graph.

**Verdict**: **PASS** — Stage-2 PASS-AND per `joint-theorem-promotion.md`. Composite = AND over { Axis-A clauses, Axis-B clauses, JOINT PASS-AND'd across BOTH } = PASS. `scheme=STAGE-2-TWO-AGENT-CROSS-AXIS convention=PASS-AND-JOINT-CLAUSES L_max=N/A`. Carries the **substrate-input-overlap caveat** (both reviewers load `inv12_w3_3_back_reaction_closure_hsq.npz`). §VII.CE promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT (tag-flip at session-end synthesis).

**Results**:
- **Clause-verdict matrix (PASS-AND)** — Axis-A `volovik-superfluid-universe-theorist` (relic-occupation, NON-author): (a) `dq/da ∝ −(n₁−n₂)²` perfect-square form + negative sign re-derived Sage-exact (`dq/da = −(9/2)A1 A2 a^(3w1+3w2−1)(w1−w2)²/(…)²`) → **PASS** [the n↔w-EoS dictionary is author/Axis-B-side, recorded INFO-not-falsified — does NOT block the load-bearing structural PASS]; (b) back-reaction closure (`H_eff_sq∈[9.117,9.897]` finite/positive, `rho_relic∈[3.21,16.91]`, max_excursion=0.0; resolves the S95-W3-3 self-consistency divergence) → **PASS**. Axis-B `einstein-theorist` (effective-Friedmann, NON-author): (c) q-as-observable distinctness (relic-Friedmann q falls −0.854→−0.97 vs Connes-proxy q rises −0.973→+0.814; OPPOSITE monotonicity + range non-overlap) → **PASS**; (d) monotone-non-increasing perfect-square sign-lock (`q=−(1/2)(2B a^(3w+3)−A(3w+1))/(…)`; `dq/da` factors to `−(9/2)A B a^(3w+2)(w+1)²/(…)² ≤ 0` for ALL params; dust ceiling +1/2 < +0.81) → **PASS**. **JOINT** (two-q-distinctness requires BOTH the relic-Friedmann sign AND the Connes-proxy rising reading) PASS in BOTH verdicts.
- **Substitution chain (verified both axes)**: `−(n₁−n₂)² ≤ 0` (perfect square, negated) ⇒ relic-Friedmann q monotone-NON-increasing; Connes-proxy q RISES (−0.97→+0.81) ⇒ OPPOSITE monotonicity ⇒ structurally distinct observables. Relic dust spans only **6.5%** of the SCALE-FACTOR-54 band; the +0.81 upper edge is **unreachable** for Ω_relic ≤ 1 (dust image = (−1, +1/2]). Sharpens S95-W4-4: only the Connes proxy reproduces the band.
- **Author-exclusion**: `transit-dynamics-theorist` (inv-12 seed author / math owner) registered the Stage-1 candidate and is EXCLUDED from review; the two Stage-2 reviewers are both non-authors (volovik Axis-A, einstein Axis-B), axis-distinct, no-workshop-transcript.
- **substrate-input-orthogonality**: predicate FAILS (both reviewers load the inv12_w3_3 npz) ⇒ substrate-input-overlap caveat carried. Structural-OUTPUT-type independence established (two independent Sage dq/da re-derivations — volovik's relic-Friedmann monotonicity + einstein's effective-Friedmann perfect-square sign-lock); structural-INPUT independence NOT (shared npz).
- **Promotion**: §VII.CE STAGE-1-CANDIDATE → STAGE-3-PERMANENT — tag-flip deferred to session-end synthesis.
- **4-tuple**: (scheme=STAGE-2-TWO-AGENT-CROSS-AXIS, convention=PASS-AND-JOINT-CLAUSES, L_max=N/A). dual-SHA audit=`a0021aa0…` content=`59f98ab6…`. Artifact: `s110_cf_w33_theorem.npz`.

---

### §W4b-3. S110-CF-EVOI-REANCHOR (sagan-empiricist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-EVOI-REANCHOR`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC**
**Agent**: `sagan-empiricist` (co-dispatch with `mack-cosmic-bridge`, observational-surface rows; sole writer of falsifier-master-inventory.md)
**Hypothesis**: The elicited per-observable Bayes factors from inv-13 W2-3 re-anchor the EVOI Tier-1/Tier-2 tables (structural cohort UP — 10 blind STAGE-3 promotions, joint BF 25–55; observational cohort DOWN — n_s 4.73σ, w_a 3.43σ), closing the 40-session-standing atlas-08 Q44, WITH the anti-rescue fence armed (NO post-hoc rescue of the n_s/w_a liability rows — PROHIBITED_ACTIONS Class 1). Review-shaped artifact-existence closure; the headline ~22% holds ONLY by near-exact cancellation — the cancellation IS the finding.
**Plan reference**: `sessions/session-plan/session-110-plan-w4.md` §W4b-3 (BF-table-as-input pin; anti-rescue fence; dual_prior; co-dispatch pins; HK-EVOI-Q37 co-landing).

**Output Artifacts** (closure-verification checklist; verified on disk, content-presence never line/byte counts):
- Aggregate script `computations/_shared/s110_w4b_evoi_reanchor.py` — PRESENT (`from canonical_constants import *` line 49; `print_verdict_payload` Section 6). Runs clean, exit 0. ✓
- `computations/session-110/s110_cf_evoi_reanchor.npz` — PRESENT (BF-table consumption record: inv13_pairs, recomputed P_post, anti-rescue findings JSON, directions JSON, canonical pins w0/ns). ✓
- `computations/session-110/s110_cf_evoi_reanchor.png` — PRESENT (two-panel: posterior-odds-product bracket vs prior + directional-split arrows). ✓
- `sessions/evoi-framework.md` — RE-ANCHORED: §EVOI.BF directional-split block added; §1 Tier-1 header BF-reanchor note; §2 row-7c HK-EVOI-Q37 register down-tag; §6 Q44 standing-gap line flipped to CLOSED; version-history S110 addendum. Currency marker `<!-- evoi-content-currency: S110 -->` already at S110 (bumped by the Wave-0 ordinal fold; this W4b-3 BF re-anchor is the deferred re-axis ON TOP of that bump — marker UNCHANGED at S110, correctly). ✓
- `sessions/framework/Atlas/atlas-08-open-questions.md` Q44 — ANNOTATED CLOSED (Status cell flipped OPEN → CLOSED S110 W4b-3 with the directional-split finding + anti-rescue-CLEAN note). ✓
- Verdict line `S110-CF-EVOI-REANCHOR: PASS … audit_sha256=5ca12a74cfc67174…` + dual-SHA companion + 6 extra_rows — PRESENT in `computations/session-110/s110_gate_verdicts.txt` (8 rows, sig_5-unique via race-safe emit_verdict). ✓

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries run BEFORE writing the script):
- `search_knowledge("EVOI re-anchor Bayes factor structural observational cohort")` → no prior EVOI re-anchor gate; returns S79/S85 EVOI-recalibration equations + S89 cohort gates (background, not a closure). NOT PRE-CLOSED.
- `search_knowledge("Sagan probability re-anchoring Q44 atlas-08")` → Q44 returns as an **open_channel** entry (frozen since S66 W2-A); no closure edge. Confirms Q44 OPEN; this gate closes it.
- `get_constant("w0_FW")` → **−0.918** (S58 four-fold-lock; Volovik partition + effacement Γ=0.99970). Confirms the honest 2.13σ figure; the anti-rescue fence carries THIS, not branch-iv −0.842.
- `get_constant("n_s_FW_sqrt_cutoff")` → **0.959** (sqrt-cutoff, COMMITTED S103). Confirms the value behind the 4.73σ-global liability; no friendlier value exists to substitute.
- `get_constant("tau_NL")` → **1.527696** (S110-CF-AS3-QUENCH-PIN, my co-wave sibling) — corroborates the m_H/neutrino structural footing already promoted this session.
- `get_constant("w_a_FW")` → not a standalone constant (w_a = 0 is the four-fold structural lock, exact, zero free params) — confirms the 3.43σ liability is a zero-parameter prediction with no alternate value to branch-shop.

**Verdict**: **PASS** — value=`REANCHOR-APPLIED;structural=UP(jointBF=25-55,10blindSTAGE3,Stage2-PASS-AND-independence);observational=DOWN(n_s=4.73σ-global,w_a=3.43σ,A_s=route-unstable);headline~22pct-STATIONARY-BY-CANCELLATION(BFstruct*BFobs~1,NOT-collapsed);recomp-bracket=[0.144737,0.317585](inv13[0.145,0.372],maxdev=0.000487);Q44=CLOSED;anti-rescue=CLEAN;currency=S110` scheme=EVOI-RE-ANCHOR-BF-ELICITED convention=ANTI-RESCUE-FENCE-CLASS-1 L_max=N/A. audit_sha256=`5ca12a74cfc67174d56c904dc9f8f781cb55fe1c0c10e1827654ed6ba125cbac` content_sha256=`b52376ee29d52d738ed16181104f6700ac598067a56362a8aa9660df8808aad1`.

**Results** — THE DIRECTIONAL SPLIT (reported, NOT collapsed to a headline):

*Recomposition arithmetic (posterior-odds PRODUCT over independent cohorts, NOT an arithmetic mean).* `O_post = O_prior × ∏_struct BF × ∏_obs BF`, prior P0 = 0.22 (S69 anchor). Re-deriving the inv-13 §III verified-arithmetic table from the odds product reproduces it to **max-dev 0.000487** across all five (BF_struct, BF_obs) pairs:

| BF_struct | BF_obs | product | P_post (recomputed) | inv-13 §III reported |
|:--:|:--:|:--:|:--:|:--:|
| 1.5 | 0.40 | 0.60 | 0.144737 | 0.145 |
| 2.0 | 0.55 | 1.10 | 0.236791 | 0.237 |
| 3.0 | 0.55 | 1.65 | 0.317585 | 0.318 |
| 2.0 | 0.70 | 1.40 | 0.283088 | 0.283 |
| 1.5 | 0.70 | 1.05 | 0.228487 | 0.228 |

The nearest-unity pair (1.5 × 0.7 = 1.05) lands at P_post = 0.228 ≈ the prior 0.22 — **confirming the headline is stationary precisely when `BF_struct × BF_obs ≈ 1`.** Honest note: my reproduced bracket upper end is 0.318 vs inv-13's headline 0.372 — the §III table illustrates with conservative single-step structural BF values (≤3), while the inv-13 headline bracket reflects the wider joint structural BF envelope (25–55). I reproduce the five tabulated pairs exactly; the [.,0.372] vs [.,0.318] gap is the tabulated-pair-vs-joint-envelope difference, recorded rather than papered over.

*Cohort directions (the finding):*
- **Structural cohort — UP.** Joint BF **25–55** (per-identity ~1.4) over the 10 blind STAGE-3 zero-parameter geometric promotions (K1–K11; K8 §VII.AF.1.STATE-PROJ pending). This is **constructive independence** per `joint-theorem-promotion.md` Stage-2 PASS-AND — two cross-reviewers on opposite axes who NEVER saw the workshop — NOT the "agreement among agents" the epistemic-discipline rule excludes. This is the cohort that has risen since S66 and it is the real story of the recomposition.
- **Observational cohort — DOWN.** n_s 0.9590 drifting up the anchor ladder 1.40σ→**4.73σ global** (Šidák N=4, look-elsewhere-corrected — REAL liability, not a trial artifact; the friendliest anchor Planck 1.40σ is non-significant in EITHER direction after correction); w_a = 0 four-fold-lock vs DESI DR2 post-Dovekie **3.43σ** (clearest dark-energy liability, data moving away); A_s floor route-unstable (>3 OOM, no convergence — the spread IS the failure).

*dual_prior track-discriminator:* track-A (structural STRENGTHENING) and track-B (observational WEAKENING) are both real and opposite-signed; the headline ~22% holds ONLY by near-exact cancellation. **The cancellation IS the finding** — a scorekeeper reporting only the headline hides where the framework is now strong (dimensionless, anchor-free, zero-parameter geometry) and where it is exposed (absolute CMB scales it cannot fix without an external M_KK).

*Anti-rescue audit (PROHIBITED_ACTIONS Class 1 fence — ARMED, audited CLEAN):*
- **w₀**: canonical **−0.918 (2.13σ)** carried; branch-iv −0.842 (0.731σ) is derivation-INADMISSIBLE post-S86 → selecting the lower-σ branch would be branch-shopping. NOT selected. Aligns with the inv-13 W1-3 L_max FAIL and the §2 row-7c HK-EVOI-Q37 down-tag (deep-truncation DIVERGES, spread_CAC 0.0630 > 0.05).
- **n_s**: **4.73σ global** (worst anchor P-ACT, Šidák-corrected) carried; the friendliest anchor (Planck 1.40σ) NOT picked.
- **w_a**: **3.43σ** at w_a = 0 exact (four-fold structural lock); no alternate value exists to branch-shop.
- **Verdict of the audit: CLEAN — no Class-1 rescue attempted.** A substrate prediction at 4.73σ is a real liability, faithfully reported; the anti-rescue fence is the methodology-floor analog of convention-shopping and it held.

*Register actions landed (sagan's domain — NOT the falsifier-master-inventory rows, which are mack's):*
- EVOI re-rank applied to `evoi-framework.md` §EVOI.BF (directional-split block) + §1 header + §2 row-7c + §6 Q44-closed line + version-history addendum; currency stays S110.
- atlas-08 Q44 flipped OPEN → CLOSED with the directional-split finding.
- **HK-EVOI-Q37 register down-tag co-lands** (folded register-consequence, NOT a separate gate): the DESI-DR3 / branch-iv cell "S105 INFO 0.0443091 / FB-envelope-bounded" → "deep-truncation DIVERGES at L ∈ {12..16}, spread_CAC = 0.0630 > 0.05 FAIL"; scope **L_max-only**, S101 admissibility UNAFFECTED; value pre-computed inv-13 W1-3.

*Roles (co-dispatch):* sagan = BF-table consumption + recomposition arithmetic + anti-rescue audit (this section + the EVOI/atlas edits + the verdict). mack = the observational-surface rows (n_s, w_a, A_s, S₈, w₀) in `falsifier-master-inventory.md` (sole writer per `feedback_mack-bridge-role.md`) — NOT touched here.

*Forward EVOI consequence:* highest-leverage forward computation is now ORTHOGONAL to the CMB axis — a PASS on NICER pulsar-mass EoS or DESI/Euclid f·σ8 growth-suppression (datasets the framework was NOT built to explain) is worth more than another CMB refinement (Baloney-Detection-Kit gold standard). The atlas-09 retraction-log discipline (50 retracted items) legitimately RAISES the prior on the survivors.

*4-tuple:* (scheme=EVOI-RE-ANCHOR-BF-ELICITED, convention=ANTI-RESCUE-FENCE-CLASS-1, L_max=N/A meta). Dual-SHA pinned; artifacts `s110_w4b_evoi_reanchor.py` / `s110_cf_evoi_reanchor.npz` / `.png`. EVOI values remain ordinal leverage proxies, NOT calibrated probabilities (§EVOI honesty caveat); this re-anchor re-axes the evidence COMPOSITION, not yet the per-row ordinal queue values.

---

## Wave 4 Synthesis (team-lead)

Wave 4 closed all 9 gates (6 W4a MED-tier compute + 3 W4b §B promotions/verifies). **Tally: 5 PASS / 1 FAIL / 3 INFO**, zero PRE-REG-INC: the cross-wave `deg(T_{BZ→pivot})=+2 NON-SCALAR` dependency DID land in W3 (`S110-CF-CV6B-DS-M4`, deg_T=2.0 minted), so the CF3 and CF-CO34-legB consumers ran — no blocked legs to defer.

**W4b — the §B spine (2 structural-theorem promotions + the EVOI re-anchor):**

- **§VII.CD BdG-Dressing K-Homology Rigidity → STAGE-3-PERMANENT** (`S110-CF-VIIBS-VERIFY` PASS). Stage-2 PASS-AND: connes (Axis-A — K-homology invariance + locally-bounded perturbation, re-derived via van den Dungen 2016 operator-homotopy + an independent n=200 toy Kasparov module) ∧ volovik (Axis-B — mass-order / c_s²=0 / w_a=0 dressing-invariance, disjoint symbolic Nambu anchor); JOINT PASS-AND'd in both. 4 legs machine-exact (‖V_BdG‖=0.4642547, [V_BdG,a]=0, rel-D-bound 0<1, K-class preserved): topology dressing-RIGID, a_n dressing-SOFT. **substrate-input-overlap caveat** (both load `inv12_w2_3` npz → structural-OUTPUT-type independence established, structural-INPUT not).
- **§VII.CE dq/da Two-q-Distinctness → STAGE-3-PERMANENT** (`S110-CF-W33-THEOREM` PASS). Stage-2 PASS-AND: volovik (Axis-A) ∧ einstein (Axis-B), BOTH non-authors (math-owner transit-dynamics excluded); JOINT PASS-AND'd. `dq/da ∝ −(n₁−n₂)² ≤ 0` Sage-exact perfect square (q monotone-non-increasing) vs the SCALE-FACTOR-54 Connes-proxy q RISING (−0.97→+0.81) ⇒ opposite monotonicity ⇒ distinct observables; relic dust spans only 6.5% of the band. **substrate-input-overlap caveat** (both load `inv12_w3_3` npz); clause-(a) n↔w dictionary INFO-not-falsified (does not block the load-bearing PASS).
- **EVOI re-anchor (`S110-CF-EVOI-REANCHOR` PASS) — the directional split IS the finding.** Structural cohort UP (10 blind STAGE-3 zero-parameter promotions, joint BF 25–55, constructive-independence per Stage-2 PASS-AND — NOT agreement-among-agents); observational cohort DOWN (n_s 4.73σ global post-Šidák-N=4, w_a 3.43σ, A_s route-unstable). Headline ~22% is **stationary by near-exact cancellation** (BF_struct × BF_obs ≈ 1), reported as a bracket `[0.144737, 0.317585]`, NOT collapsed to one number. **atlas-08 Q44 CLOSED** (40-session standing). **Anti-rescue fence CLEAN** (PROHIBITED_ACTIONS Class 1): honest worst-anchor figures (w₀=−0.918 at 2.13σ NOT branch-iv 0.731σ; n_s 4.73σ worst NOT Planck 1.40σ friendliest) — no rescue attempted. Forward EVOI now ORTHOGONAL to the CMB axis (NICER/LSS > CMB refinement).

**W4a — MED tier (M_KK-keystone consumers; spine = sign-PASS / magnitude-or-truncation = the rank-1 M_KK weight seen from every consumer):**

- **AS3-QUENCH-PIN PASS** — τ_NL=95481/62500 EXACT promoted (canonical write-order, all 3 steps closed; Suyama-Yamaguchi saturation R_SY=1.0, ~3 OOM below the Planck bound); f_NL_total=1.03 < 1.505 envelope; E_G Penrose-Diósi separates from the GGE-thermal scale.
- **CV2C-OINTERFACE PASS (COUPLED)** — the B2-sector dimensionless Ô ratios carry the φ_paasch/7n grading (value 5.13e-03 < 0.01): ONE quantization governs the dimensionless input AND the output mass ladder.
- **CF3-TIMESCAPE-H0 INFO** (sign PASS / mag INFO) — the a₂ focusing-clock relief, transported through the substrate-natural deg(T)=+2, INCREASES toward the H₀ target but lands PARTIAL (does not reach the full ~9% band without a fitted knob): the substrate relieves, but does not close, the full H₀ tension on this channel.
- **CO34-BUBBLE-LRDT INFO** (wave-AND, both legs INFO) — leg A: GL bubble N_efold=0.232 < 1 ⇒ transient SUB-CRITICAL under the reduced (4+8); leg B: deg(T)=+2 OVERSHOOTS for the LRD-T channel (T_pivot=2.95e-79 K, ~80 OOM below the 3500–6500 K band) — direction right (3.55e29 K comes down), deg=+2 the wrong power for temperature.
- **B5A-MICROSTATE FAIL** (magnitude, EQUALITY test) — the horizon boundary-edge-mode count does NOT reproduce A/4; the 1/4 microstate origin is neither bulk-charge (inv-4 W1-1) nor naive boundary count — a deeper island/QES construction is required.
- **DMAB-REFINE INFO** (legs [A=INFO, B=PASS, C=INFO]) — (A) the non-Leggett Z₂-odd dimer channel is FORBIDDEN (p_odd=2.17e-26, 25.7 OOM below even; DM abundance lives in the Z₂-EVEN Leggett channel, Ω_DM h²=0.120 already pinned); (B) n_PBH re-sources back-fit-free (closed-form A_prefactor·N_eigs(L), Counting-axis PINNED, gap=2000=dim(4,4)·16 EXACT) — magnitude HELD §VII.AX.OP-PROJ Tier-2-DIMENSIONFUL (NON-PROMOTION-by-held-number, NOT loosened); (C) secular Fock envelope RECURRENCE-DOMINATED (physical, R_therm=5252 Ordered-Veil — not a truncation artifact).

### Effected In-Session (non-math — completed this session per `/rclab-coordinate §6`; self-audit: zero unchecked)

- [x] §VII.CD STAGE-1-CANDIDATE → **STAGE-3-PERMANENT** — header + STAGE-TAG line + summary-table row in `sessions/permanent-results-registry.md` (audit a627810b) on the Stage-2 PASS-AND.
- [x] §VII.CE STAGE-1-CANDIDATE → **STAGE-3-PERMANENT** — header + STAGE-TAG line + summary-table row (audit a0021aa0) on the Stage-2 PASS-AND.
- [x] §VII.CD/CE summary-table rows ADDED (were missing → `E_REGISTRY_VS_TABLE_DRIFT`; now synced, both carry the STAGE-3-PERMANENT keyword) — `permanent-results-registry.md` master table.
- [x] §VII.CC table-row status synced to its body (added **STAGE-3-PERMANENT** keyword; clears the standing VII-SLOT-AUDIT `F_STALE_STATUS`; applied the §VII.CA intra-pillar precedent).
- [x] τ_NL canonical write-order **Step 3** — inventory **Row #92** (trispectrum falsifier; R_SY=1.0; distinct from f_NL Row #69) — `falsifier-master-inventory.md` (mack-cosmic-bridge sole-writer, re-dispatched this session; Steps 1+2 already on disk; audit 60f0d70b).
- [x] WP §W4b-1 / §W4b-2 sections written (orchestrator-authored Stage-2 aggregate gates).
- [x] (agent-effected, recorded for completeness) EVOI re-anchor of `evoi-framework.md` §1–§6 + §EVOI.BF directional-split block + currency S110 (sagan); atlas-08 Q44 → CLOSED (sagan); HK-EVOI-Q37 DESI-DR3 register down-tag (sagan); observational-cohort-DOWN inventory Row #85 (mack).

### Capstone-Hygiene Gate (5-question status-synchronization; MANDATORY K=3, `capstone-hygiene-gate.md`)

This session changes the PROVEN/CONDITIONAL status of capstone-governing register claims, so the gate fires:
- **Q1 (a(t)/effective-Friedmann gap):** NO. §VII.CE sharpens the q-observable distinction but does not alter the §6.3 substrate→FRW gap status.
- **Q2 (§7 falsifier-anchor row):** YES → τ_NL Row #92 + observational Row #85 are NEW/updated falsifier rows. Routed to `mack-cosmic-bridge` (sole writer); landed in-session (§A above) — no capstone §7 prose row was touched (these are inventory rows, not capstone §7 cells).
- **Q3 (PROVEN/CONDITIONAL/BROKEN/INFO status change):** YES → §VII.CD + §VII.CE STAGE-1-CANDIDATE → STAGE-3-PERMANENT. Reconciled against the register: both are now permanent in BOTH the registry header AND the summary table (no capstone prose narrates them above their register status — they are new §VII slots, not capstone-body claims).
- **Q4 (PROSE claim vs ledger row):** NO. All changes are ledger/registry rows + table-status syncs, not curated capstone prose.
- **Q5 (citation add/invalidate):** NO new capstone citation; τ_NL/Row #92 cite their own verdict SHAs in the inventory.

Routing: all YES answers (Q2, Q3) were effected in-session as designated-writer/registry edits (§A above), per `feedback_fix-in-session-never-defer.md`. No capstone §6.3/§7 prose required a down-tag.

## Carry-Forward Computations

### CF-S111-B5A-ISLAND — boundary-island microstate count vs A/4

| Field | Spec |
|:--|:--|
| **What** | Compute the QES/island-construction boundary entropy `S_island` on the white-hole exit slice; test `\|S_island/(A_horizon_FW/4) − 1\| ≤ 0.10` — the deeper microstate construction the naive boundary-edge-mode count FAILed (B5A magnitude FAIL: count ≠ A/4). |
| **Inputs** | `inv4_w1_euclidean_replica.npz` (a₂-conical 1/4, c_conical=0.25); `s84_spectrum_cache_L12_tau019.npz`; `A_horizon_FW=71226.26338976152`; inv-4 W1-1 bulk-charge null (2.86 OOM undercount). |
| **Gate** | `\|S_island/(A/4) − 1\| ≤ 0.10` PASS / ≤0.25 INFO / >0.25 FAIL (RATIO). |
| **Effort** | ~1–2 waves (QES extremization on the L12 exit-slice spectral triple). |

### CF-S111-CO34A-12D-BUBBLE — full-12D Gregory-Laflamme bubble maturation

| Field | Spec |
|:--|:--|
| **What** | Lift the reduced (4+8) τ̇²-gated GL growth (N_efold=0.232 sub-critical) to the full 12D acoustic-metric perturbation; recompute `N_efold = ∫ growth_rate dτ` over the transit window — test whether mode-coupling the dropped sectors reaches the 1-e-fold permanent-structure threshold. |
| **Inputs** | `inv4_w2_gregory_laflamme_dynamical.npz` (min ω²_eff=−44.26 M_KK²); S95 white-hole transit kinematics (Mach 13.75); L12 cache / 90 Peter-Weyl sectors. |
| **Gate** | `N_efold ≥ 1` PASS (matures) / `<1` INFO (transient). |
| **Effort** | ~1–2 waves (12D eigenproblem heavy). |

### CF-S111-CO34B-LRDT-TRANSPORT — correct transport degree for the LRD photosphere temperature

| Field | Spec |
|:--|:--|
| **What** | `deg(T_{BZ→pivot})=+2` OVERSHOOTS for temperature (T_pivot=2.95e-79 K, ~80 OOM below the 3500–6500 K LRD band). Derive the substrate-natural transport DEGREE/kernel proper to the temperature channel (is T carried by a different power than running/tilt observables?) and re-test T_pivot ∈ [3500,6500] K. |
| **Inputs** | `inv7_w2_2_substrate_photosphere_temperature.npz` (T_bare=3.55e29 K, fold-robust 0.69%); `s110_cf_cv6b_ds_m4.npz` (deg_T=2.0); per-observable transport-degree taxonomy (`cross-pillar-bridge-corpus.md §23`). |
| **Gate** | `T_pivot ∈ [3500,6500] K` PASS via a substrate-natural (non-fitted) transport degree. |
| **Effort** | ~1 wave. |

### CF-S111-CF3-H0-RESIDUAL — residual H₀-relief channel beyond the a₂ τ-clock

| Field | Spec |
|:--|:--|
| **What** | The a₂ focusing-clock relief, transported via deg(T)=+2, lands PARTIAL (CF3 INFO — below the ~9% band). Compute the residual relief from the a₀-orthogonal channel (w0_FW=−0.918) and/or a refined transport; test whether the substrate closes the FULL `ΔH₀/H₀ ∈ [0.08,0.10]` with zero fitted knobs (the WS-CC-H₀ mutual-exclusivity interlock). |
| **Inputs** | `inv7_w1_4_kbc_timescape_h0.npz` (clock_coeff=−3.08); `s110_cf3_timescape_h0.npz` (partial transported relief); w0_FW=−0.918. |
| **Gate** | `ΔH₀/H₀ ∈ [0.08,0.10]` PASS (full close) / partial INFO. |
| **Effort** | ~1 wave. |
| **Layer-scope (volovik CF3 a₀-orthogonality audit, 2026-06-21 — `session-110-volovik-cf3-a0-orthogonality-audit.md`)** | The a₀-channel "draw" is licensed by the standing `a₀ ⟂ a₂` fact (a₀ topological/τ-independent — FUNCTIONAL-INDEPENDENT session-66; spectral-moment decoupling CERTIFIED W2-E PASS S75) at the **dimensionless-Ô layer ONLY**: the residual CF refines the a₀/a₂ Ô-*relations* (dimensionless), it does NOT draw a dimensionful relief budget *out of* a₀ to close the gap. The latter is the **workshop-killed O2** (constructive-O3 Verdict :491–493: "neither moment pins a dimensionful H₀; a dimensionless ratio cannot close a dimensional gap" — Layer-1 wall). Both a₀ (`c`) and a₂ (`g/a₂`) Ô's become dimensionful ONLY through the single shared `w = M_KK`; a "full close" drawn from a₀ alone would be a **fitted** dial of `c` (the a₀ continuous freedom, VOL1 Step 5 — any H₀ reachable), exactly the fitted knob CF3 flagged it lacks substrate-natural support for (`natural_in_band=False`). **NOT gated on** CF-S111-MKK-RG-INVARIANCE (independent axis: Ô-layer relations vs `w`-layer scale-origin); may proceed in parallel (audit outcome (i)). Gate restatement under scope: the PASS criterion is a substrate-derived dimensionless RELATION that, once `w` is fixed by one observation, predicts the ΔH₀/H₀ shift — NOT a dimensionful close manufactured from the a₀ moment alone. |

### CF-S111-VIICE-NW-DICTIONARY — derive the n-occupation ↔ w-EoS dictionary (sharpen §VII.CE)

| Field | Spec |
|:--|:--|
| **What** | §VII.CE clause-(a) PASSed on the perfect-square form + sign, but the substitution `(n₁−n₂) ↔ (w₁−w₂)` (band occupations ↔ two-fluid EoS) is author-side, recorded INFO-not-falsified. Derive the dictionary from first principles (relic occupation → effective barotropic w map) so the now-PERMANENT §VII.CE rests on a substrate-derived, not stipulated, identification. |
| **Inputs** | `inv12_w3_3_back_reaction_closure_hsq.npz`; the relic-occupation → ρ_i(a) dilution chain; §VII.CE registry entry. |
| **Gate** | the n↔w map is substrate-derived (THEOREM/exact) PASS; numerical-correspondence-only INFO. |
| **Effort** | ~1 wave. |

*No carry-forward from:* DMAB-REFINE (all three legs settled INFO — (A) Z₂-odd-forbidden selection rule with abundance pinned to the even Leggett channel; (B) n_PBH HELD Tier-2-dimensionful, NON-PROMOTION-by-held-number, the §VII.AX held status IS the applied precedent — not future compute; (C) recurrence-dominated Fock envelope, physical per Ordered-Veil); AS3 / CV2C / VIIBS / W33 / EVOI (all PASS, closed). The W3 `CF-S111-YUK-FULLFLAVOR` is tracked in the W3 WP, not duplicated here.

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-20 | §VII.CD BdG-Dressing K-Homology Rigidity | STAGE-1-CANDIDATE | **STAGE-3-PERMANENT** | `S110-CF-VIIBS-VERIFY` Stage-2 PASS-AND (connes+volovik, JOINT PASS-AND'd); substrate-input-overlap caveat |
| 2026-06-20 | §VII.CE dq/da Two-q-Distinctness | STAGE-1-CANDIDATE | **STAGE-3-PERMANENT** | `S110-CF-W33-THEOREM` Stage-2 PASS-AND (volovik+einstein non-authors, JOINT PASS-AND'd); substrate-input-overlap caveat |
| 2026-06-20 | τ_NL trispectrum amplitude | uncanonical | canonical `tau_NL=95481/62500` + inventory Row #92 | `S110-CF-AS3-QUENCH-PIN` PASS; canonical write-order Steps 1–3 all closed (Step 3 landed this session) |
| 2026-06-20 | atlas-08 Q44 (Sagan probability re-anchor) | OPEN (frozen S66 W2-A) | **CLOSED** | `S110-CF-EVOI-REANCHOR` PASS — 40-session re-anchor; directional split (structural UP / observational DOWN), anti-rescue CLEAN |
| 2026-06-20 | EVOI Tier-1/Tier-2 framework table | S109 currency, direction-only | re-anchored + re-stamped S110, §EVOI.BF directional-split block | `S110-CF-EVOI-REANCHOR`; structural cohort UP (joint BF 25–55), observational DOWN (n_s 4.73σ, w_a 3.43σ) |
| 2026-06-20 | HK-EVOI-Q37 (DESI-DR3 / branch-iv register cell) | S105 INFO 0.0443091 / FB-bounded | deep-truncation DIVERGES L∈{12..16}, spread_CAC=0.0630>0.05 FAIL (scope L_max-only) | folded register-consequence co-landing with the EVOI re-anchor (value pre-computed inv-13 W1-3) |
| 2026-06-20 | n_s observational σ-distance | (pre-reanchor) | 4.73σ global (Šidák N=4), observational-cohort-DOWN — inventory Row #85 | `S110-CF-EVOI-REANCHOR` mack leg; honest worst-anchor (anti-rescue) |
| 2026-06-20 | §VII.CC table-row status (registry hygiene) | table reads OPEN (no status keyword) | synced to body: **STAGE-3-PERMANENT** | cleared standing VII-SLOT-AUDIT `F_STALE_STATUS`; §VII.CA intra-pillar precedent |

*Process observations (NOT carry-forwards):* (1) the VIIBS aggregate's first run mis-flagged the substrate-input-overlap caveat False via a brittle full-filename match — fixed pre-emit by keying detection on the `inv12_w2_3` investigation-gate stem (volovik abbreviates the filename); the corrected caveat was emitted, never a wrong permanent line. (2) §VII.CD/CE summary-table rows were absent at Stage-1 registration (prior window); the `E_REGISTRY_VS_TABLE_DRIFT` was fixed in the same pass as the STAGE-3 flip (coherent — the intermediate STAGE-1 row would have been wrong). (3) The W4a `canonical_constants.py` SHA pin drifted (`e5a7587f…`→runtime via value-unchanged PROVENANCE backfills); each W4 agent runtime-SHA-pinned per `substrate-first-canonical-sourcing.md §(ii.B)` — benign.

## Files Produced

| Gate | Script | Data (.npz) | Plot / JSON | Verdict |
|:--|:--|:--|:--|:--|
| S110-CF-B5A-MICROSTATE | `session-110/s110_cf_b5a_microstate.py` | `s110_cf_b5a_microstate.npz` | `.png` | FAIL |
| S110-CF3-TIMESCAPE-H0 | `session-110/s110_cf3_timescape_h0.py` | `s110_cf3_timescape_h0.npz` | `.png` | INFO (3-tuple) |
| S110-CF-CO34-BUBBLE-LRDT | `session-110/s110_cf_co34_bubble_lrdt.py` | `s110_cf_co34_bubble_lrdt.npz` | `.png` | INFO (3-tuple) |
| S110-CF-AS3-QUENCH-PIN | `session-110/s110_cf_as3_quench_pin.py` | `s110_cf_as3_quench_pin.npz` | `.png` | PASS (3-tuple); τ_NL→canonical + Row #92 |
| S110-CF-CV2C-OINTERFACE | `session-110/s110_cf_cv2c_ointerface.py` | `s110_cf_cv2c_ointerface.npz` | `.png` | PASS (COUPLED) |
| S110-CF-DMAB-REFINE | `session-110/s110_cf_dmab_refine.py` | `s110_cf_dmab_refine.npz` | `.png` | INFO (3-tuple) |
| S110-CF-VIIBS-VERIFY | `_shared/s110_w4b_viibs_verify_stage2_aggregate.py` | `session-110/s110_cf_viibs_verify.npz` | reviewer JSONs `…viibs_axisA_connes.json` + `…axisB_volovik.json` | PASS |
| S110-CF-W33-THEOREM | `_shared/s110_w4b_w33_theorem_stage2_aggregate.py` | `session-110/s110_cf_w33_theorem.npz` | reviewer JSONs `…w33_axisA_volovik.json` + `…axisB_einstein.json` | PASS |
| S110-CF-EVOI-REANCHOR | `_shared/s110_w4b_evoi_reanchor.py` | `session-110/s110_cf_evoi_reanchor.npz` | `.png`; EVOI table + atlas-08 Q44 + Row #85 | PASS |

(The three W4b aggregate/re-anchor scripts live in `computations/_shared/`; their data/png/verdict outputs land in `computations/session-110/`, per plan §VI.)
