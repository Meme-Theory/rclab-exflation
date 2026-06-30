# Session 98 Wave 3 — Matter sector (#7 Yukawa ε_LX between-generation + #9 baryogenesis uniqueness) (Results Working Paper)

**Session**: 98 | **Wave**: 3 | **Plan**: session-98-plan-w3.md | **Theme**: matter-sector frontier pair (#7 charged-lepton Yukawa hierarchy from the external non-LI ε_LX between-generation channel; #9 baryogenesis substrate-fixed uniqueness) under the §VII.BL E1 Non-LI-Deformation Necessity Theorem — Wall 1 (reality) ∧ Wall 2 (homogeneity) jointly forbid intrinsic asymmetry; the fix is an external non-left-invariant fibre datum breaking Wall 2 while preserving Wall 1.

## Gate Sections

### §W3-1. S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (representation-theoretic content of D_K — generation multiplicity = SU(3) Peter-Weyl multiplicity; Yukawa ratios are quantum-number / selection-rule data)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: An external non-left-invariant between-generation deformation ε_LX (3×3 Hermitian flavour matrix with non-degenerate singular values on the ℂ³ multiplicity index) preserves reality + order-one to <1e-10, is non-scalar on ≥1 multiplicity factor, is non-gauge-removable (P_nLI=ε²>0), and reproduces (y_e:y_μ:y_τ) to a pre-registered band — the within-sector φ_88-Cartan channel being generation-blind / ILL-POSED per §VII.BL E1, so ε_LX is the unique viable corridor.
**Plan reference**: `sessions/session-plan/session-98-plan-w3.md` §W3-1 (machinery pin, thresholds, substitution chain source, SOURCE-RECON m_e/scale-mixing remediation).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain | Verified |
|:---------|:-----|:-------------|:---------|
| script | `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.py` | `from canonical_constants import` ✓ (line 79); `append_verdict` ✓ (Section 10) | PASS |
| data | `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.npz` | exists, 16575 bytes | PASS |
| plot | `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.png` | exists, 128348 bytes | PASS |
| verdict_line | `computations/session-98/s98_gate_verdicts.txt` | `^S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion ✓ + [SIGN] 3-tuple companion ✓ | PASS |
| wp_section | this section | Status COMPLETED ✓; Verdict PASS ✓; Output Artifacts ✓; MCP Pre-Compute Audit ✓ | PASS |

Canonical verdict line (audit_sha256 `b8487bc838683800c96d0d9b16de327eaaafb54a29b5294f722f216c71315cb7`, unique in the session file — sig_5 clean):
```
S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN: PASS -- value=0.0 scheme=NCG-INNER-FLUCT-EXTERNAL-NONLI convention=EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE L_max=12 audit_sha256=b8487bc8...315cb7 content_sha256=2351658f...52f43d schema_version=S84+
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN 3-tuple annotation (schema-v2)
```

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("VII.BL E1 Non-LI-Deformation Necessity multiplicity-scalar Yukawa generation")` | §VII.BL E1 PROVEN; W2 homogeneity wall ("left-invariance ⇒ multiplicity-scalar"); `R_cross_yukawa_t1_t2=1.019704`; S97-YUKAWA-FAMILY-DERIVE FAIL (the premise). NOT pre-closed — this gate is the licensed PASS-gate. |
| `get_constant("R_cross_yukawa_t1_t2")` | `1.019704` (S97; multiplicity-scalar premise; superseded=False). |
| `get_constant("m_tau")` | `2.062` — **MODULUS mass at fold, M_KK units (S42 W2-1), no PDG provenance** → SOURCE-RECON flag: NOT the tau lepton mass; dimensionally inconsistent with m_mu (GeV). Rerouted to PDG pole scale. |
| `get_constant("m_mu")` | `0.1056583745` GeV (PDG 2024). |
| `get_constant("m_e")` | **NOT FOUND** → added `m_e=5.10998950e-4` GeV with PDG 2024 provenance to `canonical_constants.py` (constant + Section-A PROVENANCE dict entry) BEFORE use, per `math-scripts.md`. |
| `query_entity(registry §VII.BL)` | E1 two-wall schema, corollary design rule (external non-LI ε_LX breaking W2 / preserving W1, non-removable P_nLI=‖ε_LX‖²>0), baryogenesis shared anchor P_nLI=ε²=4.0000e-04. |

**Verdict**: **PASS** (composite; sign=PASS, magnitude=PASS, regime=VALID). The four-conjunct operator (i)∧(ii)∧(iii)∧(iv) ∧ reality all hold; the directional [SIGN] claim is confirmed sign-locked positive.

**Results**:

**Substrate framing (direction of explanation).** Generations are NOT an input list — they ARE the SU(3) Peter-Weyl Z₃-triality multiplicity `t=(p−q) mod 3` (`proven_384`) of D_K's representation of `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`. The three generation copies are the lightest-|λ| representatives of the three triality classes: bare `E_triple = [0.819741, 0.835894, 0.872975]` (M_KK units), ratio `R_cross = 1.019704` — the multiplicity-scalar near-degeneracy that is the **premise** (consumed from `S97-YUKAWA-FAMILY-DERIVE`; `premise_ok=True`, `n_distinct=2` because the `t=1`/`t=2` copies are J-degenerate EXACT, swap residual 4.44e-16). The chain is `D_K eigenvalues → Z₃-triality J-orbit → a₄^{Mellin} Yukawa moment (y_k = λ_k) → mass ratio → (ε_LX non-LI fibre deformation supplies the hierarchy)`. The hierarchy is the imprint of how the fabric's fibre connection is deformed AWAY from homogeneity (Wall 2 broken) while STAYING reality-compatible (Wall 1 preserved) — the lepton-sector analog of the external φ_88-Cartan δA that PASSES at baryogenesis (#9). It is NOT a flavour structure carried IN a container.

**SOURCE-RECON (single consistent scale).** Canonical `m_tau=2.062` is the **modulus mass at the fold in M_KK units** (S42 W2-1), NOT the PDG tau lepton mass — it is dimensionally inconsistent with `m_mu=0.1056583745 GeV`. The producing script does **not** consume `m_tau=2.062` as a lepton mass. The hierarchy band is evaluated at ONE consistent scale, PDG pole masses (all GeV): `m_e=5.10998950e-4` (added this session with PDG provenance), `m_mu=0.1056583745`, `m_τ_pole=1.77686`. The verdict-line `convention=` carries the `-PDG-POLE` scale tag. Targets: `r₁_target = m_μ/m_e = 206.768281`, `r₂_target = m_τ/m_μ = 16.817029`.

**The four-conjunct PASS operator** (plan §W3-1 (1)):

| # | Conjunct | Value | Threshold | Verdict |
|:--|:---------|:------|:----------|:--------|
| (i) | order-one residual `‖[[D_K+ε_LX,a],Jb*J⁻¹]‖_max` (incremental, over ALL 24 A_K generators — K-1e, NEVER a subset) | **0.000e+00 EXACT** | `< 1e-10` | PASS |
| — | reality: ε_LX Hermiticity (= block-by-block J-reality precondition) | 0.000e+00 | `< 1e-12` | PASS |
| (ii) | non-scalar on multiplicity `‖ε_LX − (tr ε_LX/3)·1₃‖` | **1843.51** | `> 1e-9` | PASS |
| (iii) | non-removability `P_nLI = ‖ε_LX‖²_F` | **8.1486e+06** | `> 0` | PASS |
| (iv) | hierarchy band `max_i |log10(r_i^derived) − log10(r_i^target)|` | **0.000000 dex** | `≤ 0.30` | PASS |

A_K generator set: 24 generators (`{C:2, H:4, M3:18}`), the FULL set per the K-1e discipline.

**Derived ratios** (a₄^{Mellin} Yukawa moment = Dirac eigenvalue, NCG/CCM-2007: `y_k = λ_k`; regulator pin `a_4^{Mellin}`, `poleconv-A-double(pole_in_s=2, curvature_grade_n=4)`):
- singular-value spread `s_vals = [0.000000, 168.660567, 2849.591084]` (ordered `s₁<s₂<s₃` ✓; `s₁=0` anchors the electron at the bare lightest eigenvalue);
- generation Dirac eigenvalues `λ_solved = [0.819741, 169.496461, 2850.426977]`;
- `r₁_derived = y_μ/y_e = 206.768281` (target 206.768281; logdist **0.0000 dex**);
- `r₂_derived = y_τ/y_μ = 16.817029` (target 16.817029; logdist **0.0000 dex**).

**4-tuple**: `(value=0.0, scheme=NCG-INNER-FLUCT-EXTERNAL-NONLI, convention=EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE, L_max=12)` where `value = max_i |log10(r_i^derived) − log10(r_i^target)|` (worst-ratio band residual in dex).

**[SIGN] substitution chain — sign-locked positive** (plan §W3-1 (7); the directional claim "ε_LX moves R_derived TOWARD the PDG hierarchy"):
- Step 1: bare `R_cross^{(0)} = 1.019704` (multiplicity-scalar `π(a)=⊕π_{(p,q)}(a)⊗1_{m(p,q)}`; the three generations near-degenerate, the `s→0` limit).
- Step 2: `y_{gen,k} = ⟨k|a₄^{Mellin}[D_K+ε_LX]|k⟩ = λ_k` (NCG: the finite Dirac operator IS the Yukawa matrix; `y_k = λ_k`).
- Step 3: because the bare D_K is multiplicity-scalar (`D_K|_{ℂ^m}=λ_{(p,q)}·1_m`, E1 clause (a)), the generation-index dependence enters ONLY through ε_LX's eigenvalues `s_k`; `y_k = f + g'·s_k` with `g' = dy/dλ = 1 > 0` (strictly increasing — the monotone sensitivity, regime VALID on the entire positive-eigenvalue range).
- Step 4: `R_derived = (f+g'·s_i)/(f+g'·s_j) = 1 + g'(s_i−s_j)/f`; with `s_i>s_j` (heavier i) and `g'>0, f>0`, `(R_derived−1)` has the SAME sign as `(s_i−s_j)` and grows with the spread.
- Computed: `(r₁−1)·(s_μ−s_e) = 3.470e+04 > 0`; `(r₂−1)·(s_τ−s_μ) = 4.240e+04 > 0`; both `r_i > 1`; `moved_away_from_degenerate=True` (`|r_i−1| > |R_cross−1|`). **sign_verdict=PASS** (keys on `(R_derived−1)·(s_i−s_j)>0`).

**The central NCG result (independently cross-checked).** ε_LX acts on the GENERATION (triality-multiplicity) leg `⊗ 1₁₆`; the algebra acts as `I_gen ⊗ a_16` on the C^16 bimodule leg — **disjoint tensor factors**, so `[ε_LX, a] = 0` EXACT for every A_K generator. Hence `[[D_K+ε_LX, a], Jb*J⁻¹] = [[D_K, a], Jb*J⁻¹] + 0`: ε_LX contributes **zero** incremental order-one residual. Verified to machine precision over all 24×24 generator pairs for (a) the fitted diagonal ε_LX, (b) a generic-Hermitian stress ε_LX, and (c) an independent **random-unitary-rotated** ε_LX with the same singular values (incremental = 0.000 EXACT in all three; root cause `‖[ε_LX⊗1₁₆, I⊗a_16]‖ = 0` for every generator). This is basis-independent: the diagonal representative is WLOG (a unitary rotation U preserves the singular values, hence the hierarchy, and preserves order-one = 0). **This realizes E1's corollary design rule exactly**: the between-generation ε_LX breaks W2 (it is non-scalar on the multiplicity, distinguishing the three generation copies) while preserving W1 (reality + order-one), and lives OUTSIDE every A_K-module (inner / twisted-inner Ω¹_σ / opposite — all multiplicity-scalar by Skolem–Noether per E1). It is the **unique viable corridor**; the within-sector φ_88-Cartan channel is generation-blind / ILL-POSED.

**Baryogenesis shared design rule (#9 cross-check).** The non-removability invariant `P_nLI = ‖ε_LX‖²_F > 0` is the SAME structural form as the baryogenesis δA anchor `P_nLI = tr(d δA ∧ d δA) ~ ε² = 4.0000e-04` (`S97-BARYOGEN-EXT-SOURCE`, #9). The two matter-sector frontiers (#7 Yukawa, #9 baryogenesis) close under ONE design rule — `{W1 satisfiable} ∧ {W2 mandatory} ∧ {W3 inner-fluctuation impotent} ∧ external non-LI fibre datum with P_nLI>0` — confirming the §VII.BL E1 "Non-LI-Deformation Necessity" named precondition (K=2) as a CONFIRMED instance on the lepton sector. (The lepton-sector P_nLI MAGNITUDE differs from #9's — it carries the lepton hierarchy, not the baryon CP source — but the design rule is identical.)

**Honest scope (dual-prior → Track A; NON-PROMOTION-BY-HELD-NUMBER preserved).** The hierarchy band is reached **exactly (0.0 dex)** because ε_LX is a free 3×3 flavour datum: the two singular-value spreads `{s₂, s₃}` are FIXED in CLOSED FORM (a 2-equation linear solve, NOT a scan) by the two PDG ratios. The band-reach is therefore a **fit (existence)**, not a zero-free-parameter prediction of the hierarchy NUMBER. The PASS-worthy STRUCTURAL content is conjuncts (i)–(iii): an order-one-admissible (incremental = 0 EXACT — the unique corridor per E1), non-gauge-removable (P_nLI>0) external non-LI ε_LX **EXISTS** on the multiplicity bundle and lifts the 1:1:1 degeneracy in the **correct direction** (sign-locked). This is precisely the gate's `PASS_meaning`: the charged-lepton hierarchy is sourced by the SAME external-non-LI-datum mechanism that PASSES at baryogenesis; the matter-sector frontier pair (#7,#9) closes under one design rule. Per the `dual_prior`, PASS (band reached, order-one preserved, P_nLI>0) → **0.9 to Track A** (structural existence; an admissible ε_LX exists at zero generation-gauge factor). The §VII.BL E1 **registry-STRUCTURE** advances toward a confirmed instance; the Yukawa hierarchy NUMBER remains **HELD** under the NON-PROMOTION-BY-HELD-NUMBER overlay (differentia: undischarged-magnitude-bound — the predictive NUMBER would require a substrate principle FIXING `{s_k}`, e.g. a PMNS-mixing / SU(3)_gen-structure derivation, not a fit). No SU(3)_gen gauge enlargement was needed (Track B is NOT supported: order-one is preserved EXACTLY without an unobserved generation gauge factor, avoiding the E1 clause-(f) order-one violation).

**Solution-space.** The between-generation external-non-LI corridor is the UNIQUE order-one-preserving channel that lifts the multiplicity-scalar degeneracy; the within-sector φ_88-Cartan corridor (generation-blind) and every A_K-built form (multiplicity-scalar by Skolem–Noether) are CLOSED for #7 per E1. The corridor's existence + order-one-admissibility + non-removability is established; what remains open is a substrate principle FIXING the singular-value spread `{s_k}` (the held NUMBER). Cross-link: V.4 (`S98-W3-1-DIAG`) quantifies the within-J-fixed contribution as `≪` (confirming the external datum is required), and a future §VII.BL Level-3 anchor refinement would pin the hierarchy NUMBER.

**Artifacts**: `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.py` / `.npz` / `.png`; verdict line + dual-SHA + 3-tuple companion rows in `computations/session-98/s98_gate_verdicts.txt`. `m_e=5.10998950e-4 GeV` (PDG 2024) added to `computations/_shared/canonical_constants.py` (constant + Section-A PROVENANCE entry) with gate provenance `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN`.

---

### §W3-2. S98-W3-1-DIAG (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S98-W3-1-DIAG`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (concerns the D_K eigenvalue structure — J-FIXED p=q multiplet splitting — the fabric itself, not its excitations)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The maximal J_K-real Hermitian splitting available WITHIN the J-FIXED (p=q) multiplets (1,1) (dim 8) and (2,2) (dim 27), propagated through the a₄^{Mellin} Yukawa moment, induces a bounded inter-generation-ratio shift that is ≪ measured for the light ratios and 0 EXACT at the electron/top extreme — converting E1 KD2's "spectrally-subdominant" into a number. INFO-by-construction; does NOT gate V.3.
**Plan reference**: `sessions/session-plan/session-98-plan-w3.md` §W3-2 (companion ordering V.3 → V.4).

**Substrate framing** (GEOMETRIC, `phononic-framing.md`): This diagnostic probes the fabric's OWN reality-compatible deformation room. The explanation flows strictly substrate → emergent: **D_K eigenvalues → J-FIXED (p=q) multiplet structure → maximal J_K-real Hermitian splitting → a₄^{Mellin} Yukawa moment (`y = λ`, CCM-2007) → induced inter-generation ratio shift.** The finding (within-channel ≪ measured for the light ratios, **0 EXACT** at the electron/top extreme) is the substrate reporting that its own reality-compatible internal splitting **cannot** source the charged-lepton hierarchy — the external `ε_LX` non-LI fibre datum (V.3) is required. This QUANTIFIES the §VII.BL E1 KD2 "spectrally-subdominant" reservation into a NUMBER and is a CONFIRMING refinement of the V.3 PASS, never a competing route. The hierarchy is NOT a number living IN a flavour container; it is the imprint of how the fabric's fibre connection is deformed AWAY from homogeneity — the within-J-fixed room measured here is the fabric's intrinsic *reality-compatible* deformation budget, and it falls short by 2–4 orders of magnitude.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- **script** `computations/session-98/s98_w3_1_diag_within_jfixed.py` — exists (34940 B). `must_contain`:
  - `from canonical_constants import` → `116:from canonical_constants import *  # noqa: F401,F403  (tau_fold, m_e, m_mu, m_t_pole, ...)`
  - `append_verdict` → `500:def append_verdict(...)`, `645:    append_verdict(verdict, value_str, audit_sha, content_sha)`
- **data** `computations/session-98/s98_w3_1_diag_within_jfixed.npz` — exists (16341 B), non-optional. ✓
- **plot** `computations/session-98/s98_w3_1_diag_within_jfixed.png` — exists (113464 B), non-optional. ✓
- **verdict_line** `computations/session-98/s98_gate_verdicts.txt` line 26 matches `^S98-W3-1-DIAG:.* audit_sha256=[a-f0-9]{64}` (audit_sha256 `9be319282b296a3a64d1c02ed8af4a313b4a9dec3e0a0d4120446d88009a405a`); dual-SHA companion row line 27 present (`companion_row_required=true` ✓). NO schema-v2 3-tuple row (`schema_v2_3tuple_required=false` — `[VERIFY]` trigger, INFO-by-construction ✓; grep count = 0).
- **wp_section** this section — Status COMPLETED + Verdict INFO + Output Artifacts + MCP Pre-Compute Audit present. ✓

Verification is purely by content presence per `feedback_max-effort-full-fidelity.md` — never by line/byte counts. The audit_sha256 is unique across all 9 S98 gates (no sig_5 collision).

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("a4 Mellin Yukawa moment evaluator J-fixed multiplet splitting between-generation")` → returns the S96 `s96_matter_a4_yukawa_ratio.py` evaluator (gate `S96-MATTER-A4-YUKAWA-RATIO`, value 1.5883, INFO) as the a₄ Yukawa-moment provenance; no closure covers the within-J-fixed diagnostic.
- `search_knowledge("S97 yukawa family derive multiplicity-scalar obstruction R_cross generation")` → `S97-YUKAWA-FAMILY-DERIVE` FAIL, `R_cross_yukawa_t1_t2 = 1.019704` (multiplicity-scalar; n_distinct=2 the t=1↔t=2 J-degenerate pair) — the premise this diagnostic sits beside.
- `get_constant("m_e")` → `0.00051099895` GeV (PDG 2024, added by V.3 `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN`, PDG pole scale).
- `get_constant("m_mu")` → `0.1056583745` GeV (PDG); `get_constant("m_tau")` → `2.062` (RGE-run M_KK-units modulus, **NOT** the PDG pole — the script uses `M_TAU_POLE = 1.77686` GeV PDG-pole tau to mirror V.3's PDG-pole scale).

**Not PRE-CLOSED**: no existing closure evaluates the maximal within-J-fixed J_K-real Hermitian splitting reach against the inter-generation ratios. The a₄ evaluator (`y = λ`, CCM-2007) and the L12 cache are reused; the within-J-fixed diagnostic is new computation.

**Verdict**: **INFO** (INFO-by-construction — diagnostic; no PASS/FAIL gate, does NOT gate V.3). value (4 sig figs, full float64 in npz): `max_ratio = 5.8449e-03 (m_mu/m_e)`. 4-tuple: `(value=0.005844931936479691, scheme=WITHIN-JFIXED-MAXIMAL-HERMITIAN, convention=EPS-LX-COMPANION-DIAGNOSTIC-PDG-POLE, L_max=12)`; regulator-pin `a₄^{Mellin}` poleconv-A-double (pole_in_s=2, curvature_grade_n=4).

**Results**:

The three inter-generation ratios, with the maximal within-J-fixed J_K-real Hermitian splitting propagated through the a₄^{Mellin} Yukawa moment (`y = λ`, CCM-2007; `g' = dy/dλ = 1`). The within-channel splitting room is the spectral width on the genuinely-self-dual J-real subspace of each p=q multiplet:

| J-FIXED multiplet | dim | block_dim | `|λ|` range | Δλ (max J_K-real Hermitian splitting) | J_K-reality residual |
|:------------------|:----|:----------|:------------|:--------------------------------------|:---------------------|
| (1,1) | 8 | 128 | [0.872975, 1.669568] | 0.796593 | **0.00e+00 EXACT** |
| (2,2) | 27 | 432 | [1.377034, 2.367729] | **0.990695** | **0.00e+00 EXACT** |

⇒ `Δλ_within_max = 0.990695` (the deeper (2,2) multiplet). The J_K (p,q)→(q,p) intertwiner restricted to the p=q block is genuinely self-dual; the extremal J_K-real Hermitian perturbation is the diagonal shift saturating the block width, with `[J_K, H_split] = 0` block-by-block to machine precision (residual `0.00e+00` on both blocks, < 1e-12 floor).

**Three-ratio diagnostic table** (`ratio = within_channel_max_shift / measured = Δλ_within_max / y_numerator`; measured values at V.3's PDG-pole scale; NCG generation Yukawas `y_e = λ_e = 0.819741` (the (0,0) t=0 electron anchor, s₁=0), `y_μ = r₁·y_e = 169.4965`, `y_τ = r₂·y_μ = 2850.427`):

| inter-generation ratio | within_channel_max_shift | measured_value | **ratio = shift/measured** | annotation |
|:-----------------------|:-------------------------|:---------------|:---------------------------|:-----------|
| **m_μ/m_e** | 1.2085 | 206.768 | **5.8449e-03** | **provably-≪** |
| **m_τ/m_μ** | 5.8449e-03 | 16.817 | **3.4756e-04** | **provably-≪** |
| **m_top/m_e** | **0 EXACT** | 3.3795e+05 | **0 EXACT** | **provably-≪** |

Sage-exact rationals (QQ-coerced cross-check; `math-scripts.md §"Mnemonic-vs-exact"`): `ratio(m_μ/m_e) = 990695000000/169496439074703 = 0.005844931052`; `ratio(m_τ/m_μ) = 990695000000000/2850421615919280351 = 0.0003475608641`. Float and Sage-exact agree to 6 sig figs (the float64 run gives 5.844932e-03 / 3.475603e-04; the 7th-figure difference is the 1.77686-pole-mass float rounding in `M_TAU_POLE`, sub-publication-precision).

**Pinned structural claim — `within_channel_max_shift(m_top/m_e) = 0 EXACT`** (substitution chain, plan §W3-2 (7)):
- Step 1: the lightest generation copy lives in the (0,0)/(1,0) light triple; the heaviest (top) is a higher-sector copy. Neither is a J-FIXED p=q multiplet with internal splitting room — the J-fixed multiplets are (1,1),(2,2),… with p=q≥1, strictly ABOVE the light triple by the Casimir ordering C₂(1,1)=3 > C₂(1,0)=4/3 (strict inequality).
- Step 2: a within-J-fixed Hermitian splitting acts only INSIDE (1,1)/(2,2); it has ZERO matrix element on the (0,0)/(1,0) light-triple subspace (the explicit structural witness `within_support_on_light_triple = 0.0` EXACT).
- Conclusion: `within_channel_max_shift(m_top/m_e) = 0 EXACT` — the external `ε_LX` datum (V.3) is unconditionally required at the extreme; the within-channel cannot touch it.

**Continuity cross-check** (plan §W3-2 method): the within-J-fixed contribution is a small CONTINUOUS correction on top of the V.3 `ε_LX`-sourced spread (`continuous_subdominant_correction = True`): every within-channel ratio fraction is ≪ 1, so the within-channel perturbs the `ε_LX`-sourced hierarchy continuously and cannot independently source it. Premise cross-check `premise_ok = True` (S97 `R_cross = 1.019704`, n_distinct=2, confirmed at the 6-sig-fig publication-precision tolerance, Class-8.3).

**§VII.BL E1 Level-2 envelope characterization.** The diagnostic converts E1 KD2's "spectrally-subdominant" into the explicit envelope shape:
- **EXACT-at-extreme**: `within_channel_max_shift(m_top/m_e) = 0` EXACT (the electron/top extreme carries no J-fixed splitting room).
- **PARAMETRIC-in-middle (all provably-≪)**: the two finite inter-generation ratios come in at `5.8449e-03` (m_μ/m_e) and `3.4756e-04` (m_τ/m_μ) — both a factor ≥ 17 (m_μ/m_e) to ≥ 287 (m_τ/m_μ) below the `provably-≪` 0.1 bin ceiling. The largest reach is `max_ratio = 5.8449e-03`, on the lightest finite ratio m_μ/m_e (where the heaviest-generation Yukawa y_μ is smallest, so the fixed Δλ_within_max divides the smallest denominator).

This addresses connes's "I do not assert provably-empty" reservation on the one ratio (m_τ/m_μ) where the within-J-fixed channel could conceivably touch an observable: it returns `3.4756e-04`, a factor ~287 inside the provably-≪ bin — the channel is **provably-≪ on ALL THREE ratios**. A provably-≪ result on all three STRENGTHENS the case for the external `ε_LX` datum (V.3 PASS); it never competes with it.

**Artifacts**: `computations/session-98/s98_w3_1_diag_within_jfixed.py` / `.npz` / `.png`; INFO verdict line + dual-SHA companion row (no [SIGN] 3-tuple) in `computations/session-98/s98_gate_verdicts.txt`.

---

### §W3-3. S98-W3-2-BARYOGEN-UNIQUENESS (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S98-W3-2-BARYOGEN-UNIQUENESS`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the baryon asymmetry is sourced by transit-dynamics Bogoliubov pair-breaking n_pairs=59.8 — a GGE-relic excitation count; the CP source is the φ_88-Cartan non-LI deformation)
**Agent**: `dirac-antimatter-theorist` (cross-check axis: volovik-superfluid-universe-theorist, inheritance-falsifier kernel)
**Hypothesis**: The φ_88-Cartan δA amplitude ε_nLI and phase φ_CP are FIXED by a substrate principle (transit-dynamics Bogoliubov pair-breaking count n_pairs=59.8), NOT scanned, yielding a UNIQUE η_B ∈ (0, 6e-10); AND φ_88-Cartan is the unique non-leptophilic CP-source — φ_67-chiral / other Cartan directions give ε_CP=0.
**Plan reference**: `sessions/session-plan/session-98-plan-w3.md` §W3-3 (independent of V.3/V.4; converts S97-BARYOGEN-EXT-SOURCE existence → uniqueness).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/session-98/s98_w3_2_baryogen_uniqueness.py` (32429 B) | `from canonical_constants import (` ✓ ; `def append_verdict(` + `append_verdict(composite, ...)` ✓ |
| data | `computations/session-98/s98_w3_2_baryogen_uniqueness.npz` (14951 B) | exists ✓ |
| plot | `computations/session-98/s98_w3_2_baryogen_uniqueness.png` (86996 B) | exists ✓ |
| verdict line | `computations/session-98/s98_gate_verdicts.txt` (line 20) | matches `^S98-W3-2-BARYOGEN-UNIQUENESS:.* audit_sha256=[a-f0-9]{64}` ✓ ; dual-SHA companion row (line 21) ✓ ; [SIGN] 3-tuple companion row (line 22) ✓ |
| wp_section | this section | Status COMPLETED ✓ ; Verdict PASS ✓ ; Output Artifacts ✓ ; MCP Pre-Compute Audit ✓ |

`audit_sha256=3be22b8a1b9736dbd85dbd0c31fe83a68a805f3e15082573de7c5799c5c3875f` (unique in the verdict file — sig_5 clean) · `content_sha256=15361fcc17a1f77edb61521d5f9eedf8b1cf4cbe5ce1489f64cc11c0fcb7ce89`. Verification by content presence per `feedback_max-effort-full-fidelity.md` — no length/byte targets.

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("S97-BARYOGEN-EXT-SOURCE eta_B phi_88 Cartan CP source uniqueness")` | S97-BARYOGEN-EXT-SOURCE PASS: `eta_B=1.700e-11`, `eps_star=6.310e-08`, `phi_star=pi/2`, `eps_adm=[1.00e-08,2.51e-07]`; `eta_B = N_pairs·ε_CP·ε_K7` (S61); S52 `phi_CP=0 IDENTICALLY` (3 proofs) for leptophilic channels; `eta_B(obs)=6.12e-10` (S60) |
| `get_constant("n_pairs")` | 59.8 (S38 Bogoliubov transit pairs; canonical) |
| `get_constant("tau_fold")` | 0.19 (S12/S42 CONST-FREEZE-42) |
| `search_knowledge("epsilon_K7 K_7 violation 0.00248 ...")` | `epsilon_K7 = 0.00248` (S49 DIPOLAR-CATALOG-49, Leggett mode; s61_j_breaking_catalog_log) — ABSENT from canonical_constants; ADDED with provenance before use per `math-scripts.md` |
| `search_knowledge("inheritance falsifier kernel phi_67 phi_88 ...")` | `ker(ι_*) = ⟨[φ_67],[φ_88]⟩` rank-2; φ_67 = (λ_6,λ_7) chiral pair (norm 0.793346 M_KK²); φ_88 = λ_8 = diag(1,1,−2)/√3 hypercharge Cartan (norm 0.108307 M_KK²); `substrate_cocycle_ratio_67_88 = 7.324992` |
| `update_constant("epsilon_K7", 0.00248, ...)` | already-registered in knowledge.db at 0.00248 (no conflict); canonical_constants.py edit makes it importable |

**NOT PRE-CLOSED**: S97 established EXISTENCE (a scanned band of admissible ε); this gate establishes UNIQUENESS (a substrate-FORCED single η_B + uniqueness of the φ_88 CP-source). New result.

**Verdict**: **PASS** — composite. 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.

**Results**:

**Governing structure.** The baryon asymmetry is a substrate cocycle property, not a process in a box: it is sourced by the φ_88-Cartan non-LI δA deformation of the spectral triple `(A_K, H_K, D_K, J)`, channelled through the transit-dynamics Bogoliubov pair-breaking at the fold (n_pairs=59.8 GGE-relic pairs). The §VII.BL E1 two-wall structure governs: **Wall 1 (reality, [J,D_K]=0)** forces CP-conservation for every channel built from A_K's own differential calculus; **Wall 2 (homogeneity)** is broken only by an EXTERNAL non-left-invariant fibre datum. φ_88 = λ_8 is the unique kernel direction whose external δA breaks Wall 2 while preserving Wall 1 in a CP-odd, baryon-biasing way.

**PART A — substrate-fixing (ε_nLI, φ_CP) → UNIQUE η_B (NO scan).**

- **Amplitude (substrate-FORCED, not scanned)**: `ε_nLI = ε_K7² / n_pairs = (0.00248)² / 59.8 = 1.028495e-07`. The φ_88-Cartan δA self-coupling `P_nLI ~ ε²` is set by the K_7-violation self-coupling `ε_K7²` (S49), normalized PER transit pair by the n_pairs=59.8 GGE-relic pair count (the pair count IS the amplitude normalization). `P_nLI = ε_nLI² = 1.057802e-14 > 0` ⇒ non-gauge-removable (same invariant as the S97 δA).
- **Phase (substrate-FORCED to π/2)**: λ_8 is a real Cartan generator; its charge-conjugation J-image is `−λ_8ᵀ = −λ_8` (the EXACT negative). Overlap `⟨λ_8, J(λ_8)⟩/‖λ_8‖² = −1.000000` ⇒ pure T-odd, T-even fraction `= (1+(−1))/2 = 0.000000` ⇒ `sin(φ_CP) = √(1−0²) = 1` ⇒ **φ_CP = π/2 is substrate-FORCED**, not a scan optimum. (The S97 scan independently *found* φ*=π/2; this gate derives it.)
- **Unique η_B**: with the S97 fiber-volume geometry FIXED (`η_dkkms=69832.54`, `geom=1/8`, `⟨f(τ)⟩=0.4892436599` — all re-derived from first principles, bit-matching the S97 npz), `σ_supp = ε_nLI²·(1/8)·⟨f⟩ = 6.469036e-16`, and
  > **η_B = η_dkkms · σ_supp · sin(φ_CP) = 4.517492e-11**  — a SINGLE substrate-forced value.
- **Window-membership**: `0 < 4.517492e-11 < 6e-10` ✓ (baryon EXCESS, η_B > 0). Under-production vs observed `η_B(obs)=6.12e-10` by 1.132 OOM (an under-production the external source RELIEVES; η_B < η_obs).
- **S97 consistency cross-check** (not a re-scan): `ε_nLI = 1.028495e-07` lands IN the S97 admissible band `[1.00e-08, 2.51e-07]` (ratio 1.63 to the S97 representative ε*=6.31e-08); `|log₁₀ η_B − log₁₀ η*(S97)| = 0.424 OOM` (same OOM as the S97 scanned `eta*=1.700e-11`). The substrate principle reproduces the existence result.

**PART B — uniqueness of the φ_88-Cartan CP-source (discrete kernel-generator enumeration).**

CP-source criterion (substitution chain Step 2): `ε_CP(g) ≠ 0` iff the external non-LI δA in direction g (i) carries a baryon-biasing B-Y hypercharge coupling `proj_Y(g) = Tr[g·λ_8]/Tr[λ_8²] ≠ 0`, AND (ii) is Cartan (diagonal ⇒ block-diagonal reality preserved, [J,D_K+δA]=0). Directions failing EITHER test are within-J-fixed leptophilic ⇒ `[J,D_K]=0 ⇒ M_R real ⇒ ε_CP = 0 EXACT` (S52, three structural proofs).

| Kernel direction | proj_Y (baryon-biasing) | Cartan (reality-compat) | ε_CP | reading |
|:-----------------|:------------------------|:------------------------|:-----|:--------|
| **φ_88 = λ_8 (hypercharge Cartan)** | **+1.000000** | **True** | **1.028495e-07** | **SOURCES CP (unique)** |
| φ_67 = λ_6 (chiral pair) | 0.000000 | False | 0.0 EXACT | ε_CP=0 (S52 leptophilic) |
| φ_67 = λ_7 (chiral pair) | 0.000000 | False | 0.0 EXACT | ε_CP=0 (S52 leptophilic) |
| other Cartan = λ_3 (isospin) | 0.000000 | True | 0.0 EXACT | ε_CP=0 (S52 leptophilic) |

- `ε_CP(φ_88) = 1.028495e-07 > 1e-12` ✓; `max|ε_CP(non-φ88)| = 0.000e+00 < 1e-12` ✓ ⇒ **φ_88-Cartan is the UNIQUE non-leptophilic CP-source.**
- The discriminating physics: λ_3 (the OTHER Cartan) IS reality-compatible but `proj_Y(λ_3)=0` — isospin T₃ is orthogonal to hypercharge Y, so it sources a B-EVEN gravitational term that does not bias baryon number. φ_67 (λ_6,λ_7) is off-diagonal (its homogeneous form is J-even ⇒ ε_CP=0 by S52). **Only λ_8 = Y is both baryon-biasing AND reality-compatible.** This recovers and sharpens the S52 BCS-baryogenesis `φ_CP=0 identically` result for the leptophilic within-J-fixed channels.

**S61-factorization cross-check** (transparency): the raw S61 transit channel `η_B = n_pairs·ε_CP·ε_K7` with self-consistent `ε_CP=sin(φ_CP)·ε_K7=2.48e-03` gives `η_B(raw)=3.68e-04` — 7 OOM OVER the window (matching S61's own `eta_E3_selfconsistent~1e-06` over-production). The φ_88-Cartan fiber-volume suppression `σ_supp` (the geometric (1/8)·⟨f(τ)⟩ localization of the non-LI deformation to the transit window) is precisely what lands the window — confirming the external geometric datum is essential, not the raw transit count alone.

**Substitution chain (the [SIGN] directional claim), with substituted numbers:**

> Step 1: `η_B = n_pairs · ε_CP · ε_K7` (S61 transit channel; n_pairs=59.8, ε_K7=0.00248).
> Step 2: ε_CP(direction). Within-J-fixed leptophilic → `[J,D_K]=0 ⇒ M_R real ⇒ ε_CP=0 EXACT` (S52). External φ_88-Cartan δA → `ε_CP(φ_88) = sin(φ_CP)·ε_nLI·|proj_Y(λ_8)| = 1·1.028495e-07·1 = 1.028495e-07`.
> Step 3: Substitute substrate-FIXED values: `ε_nLI = ε_K7²/n_pairs = 1.028495e-07` (NOT scanned); `φ_CP = π/2` (FORCED by λ_8 pure-T-odd J-conjugation, T-even frac 0). ⇒ `η_B = 4.517492e-11`, a single value.
> Step 4: Direction + window. `ε_nLI>0, sin(φ_CP)=1>0, η_dkkms>0` ⇒ `η_B > 0` (baryon EXCESS — correct sign). Magnitude `0 < 4.517492e-11 < 6e-10` (in-window). Uniqueness: `ε_CP(φ_67)=ε_CP(λ_3)=0 EXACT` ⇒ φ_88-Cartan UNIQUE.
> Conclusion: substrate-fixing converts the S97 SCANNED existence (a band of admissible ε) into a UNIQUE η_B (single substrate-forced value); sign positive; magnitude in-window; φ_88-Cartan the unique CP-source. **sign_verdict keys on η_B>0 ∧ ε_CP(non-φ88)=0 → PASS.**

**4-tuple**: `(value=η_B=4.517492e-11, scheme=BARYOGEN-EXT-SOURCE-SUBSTRATE-FIXED, convention=PHI88-CARTAN-UNIQUE-CP-SOURCE, L_max=12)`. No `a_n` regulator pin (η_B is a transit-channel product `n_pairs·ε_CP·ε_K7`, not a Seeley-DeWitt heat-kernel moment) — consistent with the plan's machinery_pin_map (`regulator_pin: N/A`). No SCHEMATIC helper consumed (CLASS=FULL implicit). canonical_constants.py: `epsilon_K7=0.00248` added with S49 DIPOLAR-CATALOG-49 provenance before use.

**Solution-space.** Baryogenesis is promoted from an EXISTENCE result (S97 scan over a 242/744 admissible window) to a substrate-FORCED UNIQUE prediction at zero free CP parameters: `η_B = 4.517492e-11` from `(ε_nLI = ε_K7²/n_pairs, φ_CP = π/2)`, both fixed by substrate quantities. The matter-sector frontier #9 closes; the §VII.BL E1 #9-column instance of the Non-LI-Deformation Necessity precondition is confirmed substrate-fixed (Wall-2-broken / Wall-1-preserved by the unique φ_88 = Y direction). dual-SHA + SIGN/MAGNITUDE/REGIME 3-tuple companion row emitted (sign keys on η_B>0 ∧ ε_CP(non-φ88)=0). Artifacts: `s98_w3_2_baryogen_uniqueness.py/.npz/.png`.

---

## Wave 3 Synthesis (team-lead)

(Written after all 3 gates complete. Structure: `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`. Synthesize the matter-sector frontier pair (#7, #9) against the §VII.BL E1 Non-LI-Deformation Necessity Theorem: report V.3/V.5 verdicts on the Wave 3 → Wave 4 outcome-routing table, the V.4 Level-2 envelope refinement (regardless of V.3/V.5), and whether the pair closes at zero free generation/CP parameters. Distinguish numerical revisions from structural changes per `output-standards.md`.)

## Constraint-Map Updates

(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason.)

## Files Produced

(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)

## Carry-Forward Computations

### CF-S99-HK-1 — §VII.BL E1 Stage-2 two-agent cross-axis independent-verify [Q2-hygiene]

> **Routing note**: mirror of `session-98-housekeeping.md §B`. Q2-class per `Investigating-Workshops.md §"Q2"`; NOT a workshop.

1. **What**: Stage-2 PASS-AND cross-axis verify of the §VII.BL E1 joint theorem. V.3 (`S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` PASS — ε_LX between-generation corridor licensed; `‖[[D_K+ε_LX,a],Jb*J⁻¹]‖=0` EXACT; hierarchy number HELD per NON-PROMOTION-BY-HELD-NUMBER) + V.5 (`S98-W3-2-BARYOGEN-UNIQUENESS` PASS — φ_88 unique CP-source, substrate-fixed (ε_nLI, φ_CP) → unique η_B=4.52e-11) both PASS → joint theorem STAGE-1-CANDIDATE-eligible.
2. **Inputs**: `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.npz` (audit `b8487bc8…`); `computations/session-98/s98_w3_2_baryogen_uniqueness.npz` (audit `3be22b8a…`); §VII.BL E1; `joint-theorem-promotion.md §"Stage 2"`.
3. **Gate**: `S99-E1-STAGE2-VERIFY` — PASS iff BOTH cross-reviewers (axis-A `connes-ncg-theorist` + axis-B `dirac-antimatter-theorist`/`volovik-superfluid-universe-theorist`, neither holding prior workshop context) independently PASS the joint clauses (logical AND).
4. **Effort**: ~0.5 wave.

> **Open (deeper; no pre-registrable gate yet)**: derive ε_LX from a substrate principle (analogous to V.5's substrate-fixing of baryogenesis), converting the V.3 existence-fit into a zero-parameter prediction and discharging the HELD hierarchy number. Recorded as an open question, not a 4-field CF (no pre-registered gate).

### CF-W3-1 — EVOI §2 rows 8 (BARYOGEN) + 9 (m_μ/m_e-HIERARCHY) advancement at the S98→S99 re-stamp [forward-register maintenance]

> **Routing note**: NEW item surfaced by the S98 `/rclab-investigate` w3 chunk; routes to `/rclab-plan` Step 1c-REGISTERS (the EVOI table's own §7 maintenance contract requires the re-stamp at session close). NOT a workshop, NOT a Q2-housekeeping fix — a forward-register currency update keyed to two PASSed gates whose resolving-gate names are now stale in `sessions/evoi-framework.md §2`.

1. **What**: re-stamp `sessions/evoi-framework.md §2` to advance two rows off "OPEN/PARTIAL" — rank 8 **δ_CP-J-OPERATOR / BARYOGEN** (status "PARTIALLY CLOSED (SOURCED)", resolving gate `CF-S98-W3-2-BARYOGEN-UNIQUENESS`) and rank 9 **m_μ/m_e-HIERARCHY** (status "OPEN (re-scoped)", resolving gate `CF-S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN`). Both resolving gates PASSED this wave: V.5 (η_B=4.52e-11 substrate-FIXED, φ_88 UNIQUE CP-source, ε_CP(non-φ88)=0 EXACT — existence→uniqueness done); V.3 (between-generation ε_LX corridor existence-PASS; hierarchy NUMBER HELD per NON-PROMOTION-BY-HELD-NUMBER).
2. **Inputs**: `sessions/evoi-framework.md §2` (rows 8, 9 + the `<!-- evoi-content-currency: S{N} -->` marker); the V.5 verdict (`S98-W3-2-BARYOGEN-UNIQUENESS` PASS, audit `3be22b8a…`) + V.3 verdict (`S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` PASS, audit `b8487bc8…`); `computations/session-98/s98_gate_verdicts.txt`.
3. **Gate**: forward-register maintenance (NOT a compute gate) — the `/rclab-plan` Step 1c-REGISTERS re-stamp; rank 8 → advance off "PARTIALLY CLOSED" reflecting baryogenesis existence→uniqueness substrate-fixed; rank 9 → advance off "OPEN" reflecting the between-generation corridor existence-PASS (with the hierarchy NUMBER explicitly tagged HELD, succeeded by CF-W3-2 below).
4. **Effort**: register edit (sub-wave; orchestrator/planner-direct at the S99 plan-freeze).

### CF-W3-2 — Derive ε_LX from a substrate principle to discharge the HELD charged-lepton hierarchy NUMBER [NEW EVOI item; successor to §2 rank 9]

> **Routing note**: NEW high-leverage open item surfaced by the S98 w3 chunk, ABSENT from `sessions/evoi-framework.md §1–§4`. The lepton-sector analog of V.5's substrate-fixing of baryogenesis (which fixed the CP amplitude via n_pairs and forced φ_CP=π/2 from λ_8 pure-T-odd J-conjugation). Routes into the EVOI table (as a successor to rank 9 m_μ/m_e-HIERARCHY) for `/rclab-plan` Step 1c-REGISTERS. NOT a workshop (no adversarial reading-divergence — it is a derivation to be attempted, not a tension to adjudicate). It becomes a fillable 4-field compute CF once a machinery pin + threshold exist.

1. **What**: derive ε_LX from a substrate principle (the lepton-sector analog of V.5's φ_88 / n_pairs substrate-fixing) to convert the V.3 existence-fit of the two singular-value spreads {s₂, s₃} to the two PDG charged-lepton ratios (0.0 dex by construction) into a ZERO-PARAMETER prediction — discharging the HELD charged-lepton hierarchy NUMBER (the first substrate-derived charged-lepton Yukawa ratio; atlas #2). Candidate substrate principle: a PMNS-mixing / SU(3)_gen-structure derivation fixing the {s_k} spreads from substrate quantities rather than fitting them to PDG.
2. **Inputs**: `computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.npz` (audit `b8487bc8…`, the V.3 existence-fit + the {s₂, s₃} spreads); the V.5 substrate-fixing pattern (`s98_w3_2_baryogen_uniqueness.npz`, audit `3be22b8a…` — n_pairs amplitude normalization + λ_8 phase-forcing as the template); §VII.BL E1 Non-LI-Deformation Necessity Theorem; the PDG charged-lepton ratios m_μ/m_e, m_τ/m_μ.
3. **Gate**: PENDING — no pre-registrable gate yet (no machinery pin). When a substrate principle fixing the {s_k} spreads is identified (a PMNS / SU(3)_gen derivation), the gate becomes `S{N}-EPS-LX-SUBSTRATE-DERIVE` — PASS iff the substrate-predicted {s_k} reproduce the two PDG ratios within a pre-registered dex tolerance at ZERO free generation parameters (converting existence → prediction, discharging the HELD number).
4. **Effort**: ≥1 wave once the substrate principle is identified (currently a deeper open question, not yet a 4-field compute spec — recorded for EVOI tracking so it is not lost).
