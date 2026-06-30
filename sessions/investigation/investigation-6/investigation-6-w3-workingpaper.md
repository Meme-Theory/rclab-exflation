# Investigation 6 Wave 3 — Baryogenesis, CPT & the Antimatter Sector (Results Working Paper)

**Investigation**: 6 | **Wave**: 3 | **Plan**: investigation-6-plan-w3.md | **Theme**: Antimatter-sector self-assessment at the equation level — the η_B magnitude shortfall (two independent enhancement mechanisms), the δA J-breaking-deformation uniqueness, and δA's missing spatial-domain characterization. Verdicts land at `computations/investigation-6/inv6_gate_verdicts.txt` (investigation track).

## Gate Sections

### §W3-1. INV6-W3-1-ETA-B-GGE-RESCATTERING (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV6-W3-1-ETA-B-GGE-RESCATTERING`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (inter-branch GGE strong-rescattering phase → C6 η_B amplitude)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The post-transit 8-branch GGE relic's nonzero inter-branch strong-rescattering phase (the substrate analog of LHCb-2025 baryon-CP final-state rescattering) supplies the missing ~13.5× and lifts η_B from 4.52e-11 into the observed band [3e-10, 1.2e-9].
**Plan reference**: `sessions/investigation/investigation-6/investigation-6-plan-w3.md` §W3-1 (machinery pin, PASS band, substitution chain source).

**MCP Pre-Compute Audit**:
- `search_knowledge("eta_B baryogenesis C6 phi_88 Cartan shortfall")` → Baryogenesis #9 (atlas-04 **C6**): `S98-W3-2-BARYOGEN-UNIQUENESS` PASS (audit `3be22b8a`), η_B = 4.52e-11, ε_nLI=ε_K7²/n_pairs, φ_CP=π/2 — C6 is **CONDITIONAL** (existence→uniqueness proven; magnitude shortfall open). Gate is NOT pre-closed; it computes a new number.
- `search_knowledge("GGE relic 8-branch two-speed Row 67 rescattering inter-branch overlap")` → `GGE-TWO-FLUID-67` / Row #67 two-speed infra confirmed; "The GGE relic is J-symmetric: matter and antimatter sectors carry identical occupation numbers" (S71, PROVEN) — the relic is the substrate object; the strong phases live in its branch structure.
- `get_constant("eta_BBN_obs")` → 6.12e-10 (BBN datum; band center). `get_constant("eta_BBN_err")` → 4e-12.
- `get_constant("epsilon_K7")` → 0.00248; `get_constant("n_pairs")` → 59.8; `get_constant("phi_CP_K7_transit")` → 1.5707963267948966 (= π/2 EXACT, S100b, gate `S98-W3-2-BARYOGEN-UNIQUENESS`).
- `get_constant("IBO_ratio")` → 1118.0 (S64 skyrmion inter-branch-overlap baseline; δ_CP_UV = 1/√IBO = 0.029907). `list_constants(...)` → `R_machine_substrate_67_88` = 7.32499, `c_BLV` = 0.485, `Mach_max` = 13.75 confirmed.
- `get_constant("delta_CP_UV")` → NOT a canonical constant; computed locally as 1/√(IBO_ratio) per plan line 64 (tagged `# (local)`).
- **Verdict**: gate NOT covered by any closure; C6 magnitude is the open question this gate attacks. Proceeded to compute.

**Verdict**: **FAIL** — composite (collapse rule) from 3-tuple `sign_verdict=PASS, magnitude_verdict=FAIL, regime_verdict=VALID`. The inter-branch GGE strong-rescattering phase does **NOT** supply the missing ~13.55×; η_B stays at 4.514e-11 (R_enh = 0.999219 ≤ 1). Track-B (failing-prediction) confirmed; the "GGE strong rescattering supplies the OOM" corridor is **CLOSED**.

- Canonical line: `INV6-W3-1-ETA-B-GGE-RESCATTERING: FAIL -- value='eta_B_enh=4.513962e-11;R_enh=0.999219;R_required=13.5473;eta_base=4.517492e-11;in_band=False;enhances=False;...' scheme=GGE-RESCATTERING-S98-AMPLITUDE-CHAIN convention=RATIO L_max=12 audit_sha256=d08cffd98bd58fb920012a5e56d71c7eb33caf1258be7eb1da18e85cc6cc6482 content_sha256=41148293d9790068138fca9f451f43f845e5c6d50f304026ff18f411169a64eb schema_version=S84+`
- **dual-SHA**: `audit_sha256=d08cffd98bd58fb920012a5e56d71c7eb33caf1258be7eb1da18e85cc6cc6482` `content_sha256=41148293d9790068138fca9f451f43f845e5c6d50f304026ff18f411169a64eb`
- **schema-v2 3-tuple**: `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID` (emitted via `emit_verdict(session=6, track="investigation")`).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:`):
- **script** `computations/investigation-6/inv6_w3_1_eta_b_gge_rescattering.py` — EXISTS. `grep -n "from canonical_constants import"` → `99:from canonical_constants import *  # noqa: F401,F403`; `grep -n "print_verdict_payload"` → def at `172` + call at `608`. PASS.
- **data** `computations/investigation-6/inv6_w3_1_eta_b_gge_rescattering.npz` — EXISTS (full float64 headline + spectra + verdict block). PASS.
- **plot** `computations/investigation-6/inv6_w3_1_eta_b_gge_rescattering.png` — EXISTS (4-panel: strong phases / R_enh-vs-13.55 / η_B base→enhanced→obs / R_enh(φ_weak) sweep). PASS.
- **verdict line** in `computations/investigation-6/inv6_gate_verdicts.txt` matching `^INV6-W3-1-ETA-B-GGE-RESCATTERING:.* audit_sha256=[a-f0-9]{64}` — EXISTS with dual-SHA companion row + schema-v2 3-tuple companion row + 8 extra annotation rows. PASS.
- grep output pasted in the agent's final completion message (content-presence verification only, never line/byte count).

**Results**:

*Governing structure (substrate-first).* The substrate IS the post-transit GGE relic (S_ent=0, T2): Bogoliubov pairs across 8 branches from the Row #67 two-speed spectrum (`s94_bao_peak_branch.npz`). One branch (Goldstone) is protected/gapless (δ=0, `is_protected=True`); the **7 gapped branches** (B1, B2, B3, Leggett-L1/L2, Optical-O1/O2) carry strong (final-state) phases. B2 is the K_7-charged, φ_88-Cartan CP-source sector. The C6 amplitude (S98) is a **single-amplitude readout** carrying only the weak phase φ_CP = π/2 and implicitly δ_strong = 0. The explanation flows `D_K eigenvalues → 8-branch GGE two-speed spectrum → inter-branch overlap phase δ_strong → CP-observable η_B amplitude`.

*NUMBERS (computed before the gate).*
| Quantity | Value |
|:---|:---|
| η_B_base (S98 `eta_B`, audit `3be22b8a`) | 4.517492e-11 |
| φ_CP (`phi_CP_K7_transit`) | 1.570796 rad = π/2; sin(φ_CP) = 1.000000 |
| sound speed c_s = c_BLV | 0.485 M_KK |
| IBO_ratio; δ_CP_UV = 1/√IBO | 1118.0; 0.029907 rad |
| δ_strong,i (Construction A = arctan(δ_i/c_s)), 7 gapped | [0.031252, 0.000784, 0.054673, 0.009989, 0.009989, 0.009989, 0.009989] |
| δ_strong,i (Construction B = IBO-scaled) | [0.051642, 0.001294, 0.090406, 0.016502, 0.016502, 0.016502, 0.016502] |
| branch weights w_i (LAYER-1 c1, Σ=1) | [0.246677, 0.006182, 0.431839, 0.078825, 0.078825, 0.078825, 0.078825] |
| **R_enh (A, c1 weights) [PRIMARY]** | **0.999219** |
| R_enh (A, equal weights) | 0.999688 |
| R_enh (B, c1) | 0.997865 |
| R_enh (B, equal) | 0.999148 |
| R_enh (Reading-2 product-form, upper bound) | 0.036570 |
| coherent-sum ceiling (cos ≤ 1) | 1.000000 (R_ceiling_check = 0.999219 — identical) |
| R_required = η_obs/η_base | **13.547339** |
| PASS-band R edges [3e-10/base, 1.2e-9/base] | [6.6409, 26.5634] |
| **η_B_enhanced = base · R_primary** | **4.513962e-11** |
| η_obs (BBN) | 6.120000e-10 |
| in PASS band [3e-10, 1.2e-9]? | **False** |
| enhances (R_enh > 1)? | **False** |

**4-tuple**: (value=`eta_B_enh=4.513962e-11;R_enh=0.999219;R_required=13.5473;eta_base=4.517492e-11;in_band=False;enhances=False;...`, scheme=`GGE-RESCATTERING-S98-AMPLITUDE-CHAIN`, convention=`RATIO`, L_max=`12`).

*Substitution chain (SIGN claim, with substituted numbers).*
- **Claim** (plan): "A nonzero inter-branch strong-rescattering phase δ_strong ENHANCES (multiplies up) the CP-observable η_B amplitude" — pre-registered as **CONDITIONAL** (Step 5: not automatic at φ_CP = π/2).
- **Step 1**: η_B_base = 4.517492e-11 [S98; ε_nLI = ε_K7²/n_pairs = (0.00248)²/59.8 = 1.028495e-07; φ_CP = π/2].
- **Step 2**: A_CP ∝ |A₁||A₂| sin(Δφ_weak) sin(Δδ_strong) [interfering-amplitude CP form, LHCb-2025 arXiv:2504.15008]. CP-observability needs BOTH a weak-phase difference AND a strong-phase difference.
- **Step 3**: the S98 single-amplitude readout sets Δδ_strong = 0; the multi-branch readout reintroduces the 7 gapped-branch strong phases δ_strong,i.
- **Step 4** (substitute): R_enh = |Σ_i w_i sin(φ_CP + δ_strong,i)| / |sin(φ_CP)|. At φ_CP = π/2, sin(π/2 + δ) = cos(δ), so **R_enh = |Σ_i w_i cos(δ_strong,i)|**.
- **Step 5** (read-off): with δ_strong,i ∈ [0.00078, 0.0547] rad (all ≪ 1), cos(δ_strong,i) ≈ 1, and since Σ w_i = 1, **R_enh = 0.999219 ≤ 1.0 EXACTLY**. The plan's Step-5 caveat is CONFIRMED: enhancement is NOT automatic at maximal weak phase — `cos(δ) ≤ 1` is a structural ceiling. **SIGN preserved**: η_B_enhanced = 4.513962e-11 > 0 (baryon excess) since cos(δ_strong,i) > 0 for |δ_strong,i| < π/2.
- **Conclusion**: η_B is NOT enhanced (R_enh ≤ 1); the required 13.55× is not supplied. The direction matches the chain's structural prediction (ceiling), so **sign_verdict = PASS**; the magnitude FAILs the band.

*Structural finding (the decisive identity — "follow the algebra").* At maximal weak phase φ_CP = π/2,
> **R_enh = |Σ_i w_i cos(δ_strong,i)| ≤ Σ_i w_i = 1.0 EXACTLY** (every cos ≤ 1, weights normalized).

The coherent branch sum **cannot exceed 1**. The strong-rescattering phase can only mildly *suppress* η_B at φ_CP = π/2 — it cannot enhance. This is construction-independent: a φ_weak-sweep (panel 4) shows R_enh > 1 requires SMALL φ_weak, where sin(φ_weak + δ_strong) benefits from the strong phase; the substrate sits at exactly the no-boost point φ_CP = π/2. **Both readings agree**: Reading-1 (coherent sum) R_enh = 0.9992; Reading-2 (product form A_CP ∝ sin(Δδ_strong)) upper bound 0.0366 — the strong-phase *differences* between branches are tiny (the two-speed split δ_i/c_s is a per-cent effect). Neither supplies 13.55×.

*Physical reason the LHCb-2025 lesson does NOT transfer.* LHCb's O(10–30) baryon-CP enhancement comes from **per-mille (non-maximal) weak phases**, where a large strong rescattering phase converts a small weak phase into a per-cent CP asymmetry via sin(φ_weak + δ_strong). The substrate's CP phase is **already maximal** (φ_CP = π/2, substrate-FIXED), which is precisely the configuration where final-state rescattering provides no leverage. The mechanism is structurally closed.

*Constraint-map consequence (dual prior).* **Track-B (failing-prediction), 0.55 → 0.9.** The corridor "GGE strong rescattering supplies the OOM" is eliminated. The δA magnitude posit (LBA-1) remains the open failure locus. The remaining shortfall routes to the W3-3 acoustic-Schwinger mechanism and the G-4 M_KK-degeneracy attribution (compared at the Wave-3 synthesis). **C-3** (lepton/baryon CP-sector orthogonality) is NOT structurally derived by this gate — the rescattering route did not close, so δ_CP^PMNS = 0 (S99) stands on its own derivation, not on a baryon-rescattering contrast. (FAIL is a real constraint-map outcome eliminating one of the two named enhancement corridors, not an agent failure.)

*SOURCE-RECON note (Class-(c)).* The orchestrator STALE CACHE-SHA HINT (`88f1e9b1…` → `9e6d9cf7…`) applies to the **s84 L12 mode cache** used by sibling gates; THIS gate reads `s94_bao_peak_branch.npz` (on-disk SHA `ae31cac5d0965129…`) + `s98_w3_2_baryogen_uniqueness.npz` (on-disk SHA `4a3f9470bb52f56e…`), both pinned `<computed-at-runtime>` in plan §W3-1 input_files — no hardcoded stale literal to drift from; the s84 cache is NOT read here → zero physics effect. Documented in the verdict-line extra rows.

*Output artifacts*: `inv6_w3_1_eta_b_gge_rescattering.py` / `.npz` / `.png` under `computations/investigation-6/`.

---

### §W3-2. INV6-W3-2-J-BREAKING-DEFORMATION-ENUM (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV6-W3-2-J-BREAKING-DEFORMATION-ENUM`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (J-breaking deformation classification of A_F=ℂ⊕ℍ⊕M₃(ℂ) via Boyle-Farnsworth / Bochniak-Sitarz)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: Over the complete BF/BS-filtered enumeration of the off-Jensen 35D non-left-invariant moduli, the φ_88-Cartan direction is the UNIQUE minimal non-leptophilic CP-source J-breaker — converting the δA posit (LBA-1) into a derivation.
**Plan reference**: `sessions/investigation/investigation-6/investigation-6-plan-w3.md` §W3-2 (set-cardinality operator, BF/BS + center-character admissibility predicates, selection-rule pre-flight).

**MCP Pre-Compute Audit**:
The following `mcp__knowledge__*` queries were executed BEFORE writing the script (query-first discipline). NOT pre-closed — the S98 precedent established the criterion over an INCOMPLETE 4-direction set; this gate completes the enumeration over the full 35D moduli, exactly the open gap the plan flags.

- `search_knowledge("J operator C2 conj D_K real structure CPT baryogenesis phi_88 Cartan")` → `[J,D_K(τ)]=0 ∀τ` PROVEN (atlas-04 G8, dev 3.29e-13; T11 all left-invariant metrics); KO-dim-6 `J²=+I, JD=DJ, Jγ=−γJ`. Confirms δA MUST break `C2·conj(D_K)·C2=D_K` to source CP (J-incompatibility-by-construction premise).
- `search_knowledge("off-Jensen 35D moduli J-breaking deformation Boyle-Farnsworth Bochniak-Sitarz fermion doubling")` → S76 W2-J `OFF-JENSEN-MODULI-76` CLOSED: 35D restoring potential, signature (0+, 35−, 0~0), Jensen=ridge; moduli basis = volume-preserving Sym(8) on left-invariant SU(3) metrics. Identifies the enumeration domain.
- `search_knowledge("baryogenesis uniqueness eps_CP phi_67 lambda_3 zero exact eta_B S98 W3-2")` → `S98-W3-2-BARYOGEN-UNIQUENESS` PASS (`3be22b8a`): `eps_CP_phi88=1.028e-07`, `max_other_eps_CP=0.0`, `phi88_unique=True` over only 4 hand-picked directions; verdict string flags `substrate_fixed=True_NOT_scanned`. The INCOMPLETE-set precedent this gate extends.
- `get_constant("n_pairs")` → 59.8 (S38). `get_constant("phi_CP_K7_transit")` → 1.5707963267948966 = π/2 (S98-W3-2). `get_constant("eps_K7")`/`get_constant("eta_B_FW")` → not canonical pins; sourced from the S98 npz (`eps_K7=0.00248`, `eps_nLI=1.028e-07`).

**Verdict**: **INFO** — value=`|S_admissible|=2; S_admissible={diag(7), off(2,7)}; phi88_unique_basis=False; indep_CP_source_rank=1; phi88_unique_independent=True`; scheme=NCG-DEFORMATION-CLASSIFICATION-BF-BS; convention=ABSOLUTE; L_max=12; CLASS=FULL. The literal pre-registered operator (set-cardinality over off-Jensen basis directions) returns `|S_admissible|=2`, firing the plan's INFO clause (1<|S_admissible|<∞ → φ_88 NOT unique as a *basis direction*). The independent-CP-source RANK is **1** = span{λ₈} = φ_88 (two-layer result; see Results).
`audit_sha256=ca1fd44a7c9f16d379a345b35fe1477fbffffd5ca988b18c527dd8f40fb2dca8`
`content_sha256=c58ee47294815c4f9864f04d8af0a29fd3c27ea37daeb7f64158d978aeedc6c9`

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:`):
All four artifacts verified on disk by content (grep), never line/byte count:
- **script** `computations/investigation-6/inv6_w3_2_j_breaking_deformation_enum.py` — contains `from canonical_constants import` and `print_verdict_payload` (def + call). PASS.
- **data** `computations/investigation-6/inv6_w3_2_j_breaking_deformation_enum.npz` — present (36-direction records + elimination ladder + independent-CP-source-rank cross-check). PASS.
- **plot** `computations/investigation-6/inv6_w3_2_j_breaking_deformation_enum.png` — present (panel 1: ε_CP per direction; panel 2: BF/BS elimination ladder + Reading-A/Reading-B annotation). PASS.
- **verdict line** `computations/investigation-6/inv6_gate_verdicts.txt` matches `^INV6-W3-2-J-BREAKING-DEFORMATION-ENUM:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion row + CLASS=FULL pin row + SOURCE-RECON Class-(c) cache-SHA row (no 3-tuple — `[VERIFY-THEOREM]` set-cardinality). PASS.
- grep output pasted in the agent's final completion message (content-presence verification only).

**Results**:

**Headline.** Over the COMPLETE 36-direction Sym(8) off-Jensen basis (35D moduli + projected-out volume direction), the four-filter conjunction (F1 triality ∧ F2 Cartan ∧ F3 baryon-biasing proj_Y ∧ F4 BF/BS) admits **two basis directions**: `diag(7)`=λ₈ (ε_CP=1.028495e-07, matches S98 canonical EXACTLY) and `off(2,7)`=(λ₃+λ₈)/√2 (ε_CP=7.272558e-08). Literal set-cardinality → |S_admissible|=2 → **INFO** (φ_88 NOT the unique basis direction). **But** the independent-CP-source RANK is **1**: ε_CP(g) ∝ |proj_Y(g)| = |⟨g,λ₈⟩_HS|/⟨λ₈,λ₈⟩_HS is a projection onto the **1-dimensional** subspace span{λ₈}=φ_88. The second survivor `off(2,7)` sources CP ONLY through its λ₈-projection — its residual orthogonal to λ₈ is exactly λ₃ with proj_Y = 2.776e-17 ≈ 0 (machine zero). φ_88 IS the unique *independent* CP source; `eps_CP_naive_basis_sum=1.755751e-07` is NOT a physical sum of independent contributions.

**4-tuple**: `(value=|S_admissible|=2 (indep_rank=1), scheme=NCG-DEFORMATION-CLASSIFICATION-BF-BS, convention=ABSOLUTE, L_max=12)`, CLASS=FULL.

**ε_CP per direction (machine-ε EXACT-zero discrimination, floor 1e-12):**
| Direction | g_eff | sector | Cartan | proj_Y | BF/BS | ε_CP | source? |
|:----------|:------|:-------|:-------|:-------|:------|:-----|:--------|
| `diag(7)` | λ₈ | u(1)_hypercharge | True | 1.0000 | True | 1.028495e-07 | **YES** |
| `off(2,7)` | (λ₃+λ₈)/√2 | mixed-diagonal | True | 0.7071 | True | 7.272558e-08 | **YES** |
| `diag(2)` | λ₃ | su(2)_isospin | True | 0.0000 | True | 0 EXACT | no (leptophilic) |
| `diag(5)`,`diag(6)` | λ₆,λ₇ | C²_coset_chiral | False | 0.0000 | False | 0 EXACT | no (φ_67 chiral) |
| `off(a,7)` a∈{0,1,3,4,5,6} | (λ_{a+1}+λ₈)/√2 | off-diagonal | False | 0.7071 | **False** | 0 EXACT | no (BF/BS: off-diag order-zero/no-mirror violated) |
| all other off(a,b) | — | off-diagonal | False | 0.0000 | False | 0 EXACT | no |

**BF/BS + center-character elimination ladder** (36 → 2):
`total 36` → `F2 Cartan: 3` (the 3 diagonal-content dirs: diag(2)=λ₃, diag(7)=λ₈, off(2,7)=(λ₃+λ₈)/√2 — diagonal) → `F2∧F3 (Cartan ∧ proj_Y≠0): 2` (drops diag(2): isospin λ₃ has proj_Y=0, leptophilic) → `F4 BF/BS-admissible ∩ all: 2` (both survivors diagonal ⇒ order-zero preserved, no mirror). F1 triality passes all 36 (adjoint real, t=0 ∀ direction). The 6 off(a,7) directions have proj_Y=0.7071 (F3 pass) but FAIL F4 (off-diagonal ⇒ BS doubling/order-zero violation) — **BF/BS is the load-bearing filter** eliminating the off-diagonal hypercharge-overlap directions.

**Selection-rule pre-flight substitution chain (center-character / triality; math-scripts.md MANDATE):**
- Step 1: t(p,q) = (p−q) mod 3. The adjoint rep (1,1) ⇒ t=0; every metric deformation (symmetric quadratic in adjoint generators) is triality-0.
- Step 2: t(δA = φ_88) = 0 (λ₈ color-neutral diagonal Cartan, triality-preserving).
- Step 3: CG-admissibility t(p,q) = t(p′,q′) + t(δA) (mod 3).
- Step 4: substitute t(δA)=0 ⇒ t(p,q)=t(p′,q′) ⇒ admissible ONLY between same-triality sectors; cross-triality elements = 0 EXACTLY.
- Step 5: all 36 directions triality-0 (adjoint) ⇒ F1 eliminates nothing here but is the NECESSARY pre-flight scoping same-triality CP-sourcing; the discriminating filters are F2∧F3∧F4. No "generically nonzero" claim asserted without this admissibility check.

**Independent-CP-source-rank substitution chain (two-layer result; Gram-Schmidt verification):**
- ε_CP(g) ∝ |proj_Y(g)| = |⟨g_eff, λ₈⟩_HS| / ⟨λ₈, λ₈⟩_HS — projection onto span{λ₈}.
- `diag(7)`=λ₈: λ₈-parallel coeff = 1.4142; residual ⊥ λ₈ = 0 ⇒ proj_Y(residual) = 0.
- `off(2,7)`=(λ₃+λ₈)/√2: λ₈-parallel coeff = 1.0000; residual ⊥ λ₈ ∝ λ₃; proj_Y(residual) = 2.776e-17 ≈ 0 EXACT.
- n_orthogonal_sources = 0 ⇒ INDEPENDENT CP-source rank = 1 = span{λ₈} = φ_88. **φ_88 is the unique independent CP source.**

**Cross-checks:**
- **#1 S98 4-direction precedent reproduced EXACTLY**: diag(7)~φ_88 (1.028495e-07=1.028495e-07), diag(5)~φ_67-l6 (0=0), diag(6)~φ_67-l7 (0=0), diag(2)~isospin-l3 (0=0). All 4 match (`xcheck_ok=True`).
- **#2 eps_CP(φ_88) value match**: ours 1.028495e-07 = S98 canonical 1.028495e-07.
- **#3 elimination ladder** (above).
- **#4 independent-CP-source rank** (above).

**Constraint-map consequence** (per the dual prior: INFO → 0.9 mass to Track B):
- **LBA-1 (δA-direction posit)**: PARTIALLY closed and SHARPENED. φ_88 is NOT the unique admissible *basis direction* (off(2,7) also survives the literal filter), so the bare "unique CP source" claim as a *basis-direction* statement must be retracted. **However**, φ_88 IS the unique *independent* CP source (rank-1 span{λ₈}): the correct statement is "the J-breaking CP-source subspace is 1-dimensional = the φ_88-hypercharge direction." STRUCTURAL change (epistemic-type promotion: "unique direction" → "rank-1 source subspace"), not a numerical revision.
- **η_B "sum" check**: eps_CP_naive_basis_sum=1.755751e-07 (factor 1.706 above φ_88-alone) is NOT a genuine sum over independent sources — off(2,7) is collinear (proj_Y sense) with φ_88. η_B does NOT become a larger sum; the G-1 magnitude shortfall is NOT relieved by a multiplicity-of-sources mechanism. This *contradicts* the plan's optimistic "a sum is typically LARGER, which would help G-1" — the rank-1 collapse forecloses that route.
- **C6 "uniqueness" tag (HY1, routed to investigation-close)**: the atlas-04 C6 / EVOI Rank-8 "unique CP source" tag is CORRECT at the independent-source-rank level but IMPRECISE as worded (reads as basis-direction uniqueness). Recommended reconciliation at session-promotion: re-word to "rank-1 CP-source subspace = span{λ₈} (φ_88-hypercharge)." NO register row / EVOI down-tag written by this Wave-3 gate (track-local boundary).
- **δA NOT structurally inadmissible** (FAIL branch did NOT fire): |S_admissible| ≥ 1, so the φ_88-Cartan posit IS a legitimate J-breaking deformation; the deeper-problem outcome is averted.

**Substrate-first framing.** GEOMETRIC. The substrate IS the finite spectral triple (A_F=ℂ⊕ℍ⊕M₃(ℂ), H_F=ℂ³², J, γ); deformation directions live in the off-Jensen 35D moduli — the substrate's own Level-2 moduli-deformation manifold (phononic-framing.md), NOT a coordinate on a meta-container. Explanation flows D_K real-structure axioms (J, KO-dim 6) → J-breaking deformation classification (F1–F4) → the rank-1 admissible CP-source subspace span{λ₈} → the η_B amplitude. δA is J-INCOMPATIBLE by construction (it MUST break C2·conj(D_K)·C2=D_K to source CP, since T11 proves that identity for every left-invariant metric); the BF/BS classification + the SU(3) center-character selection rule are the substrate's own algebraic filters on which J-breaking directions are admissible — the CP source is determined by the deformation algebra of the finite triple, not imported.

**Output artifacts**: `computations/investigation-6/inv6_w3_2_j_breaking_deformation_enum.py` / `.npz` / `.png`; verdict in `computations/investigation-6/inv6_gate_verdicts.txt`.

---

### §W3-3. INV6-W3-3-ETA-B-ACOUSTIC-SCHWINGER (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV6-W3-3-ETA-B-ACOUSTIC-SCHWINGER`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (acoustic-Schwinger pair production from the Mach-13.75 transit field gradient)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: Recomputing η_B as a CP-biased acoustic-Schwinger pair-production rate in the supersonic transit's strong field gradient yields a field-strength-sensitive η_B; the exponential exp(−πm²/eE) sensitivity means the 1.1-OOM shortfall could be a Mach-number (field-strength) effect that lands η_B in [3e-10, 1.2e-9].
**Plan reference**: `sessions/investigation/investigation-6/investigation-6-plan-w3.md` §W3-3 (span operator, PASS band, Schwinger field-strength substitution chain).

**MCP Pre-Compute Audit**:
- `search_knowledge("eta_B baryogenesis acoustic Schwinger pair production transit field gradient")` → surfaced the **substrate-native** Schwinger anchors: `s43_schwinger_factor36.py` (equation `exp(-exponent)=5.6569e-09; pi m²/eE=18.99`), the chiral rate `Γ_± = (eE)²/4π³ Σ_n (1/n²) exp(−nπ m_±²/eE)` (session-43-wave6), and `s61_transit_baryogenesis.py` (`eta_B = N_pairs · ε_CP · ε_K7`). Confirms a substrate Schwinger channel exists — NOT imported sphaleron physics.
- `search_knowledge("Schwinger pair production acoustic white hole Mach transit")` → **Acoustic white hole PROVEN S85** ("pre/post-fold causally separated"); `s85_w6_acoustic_white_hole_formal.py` imports `Mach_max`, `tau_fold` — the transit IS the strong-field background.
- `trace_entity("schwinger_factor36")` → gate `T3-BATCH-S43-SCHWINGER-FACTOR36` = **MIGRATED/INFO** (no live verdict); not a closure covering this gate.
- `trace_entity("transit_baryogenesis")` → gate `T3-BATCH-S61-TRANSIT-BARYOGENESIS` = **MIGRATED/INFO**; not a closure. ⇒ this gate computes a NEW number (the Mach-scan field-strength sensitivity); nothing pre-closes it.
- `get_constant`: `Mach_max`=13.75; `c_BLV`=0.485 (S64); `phi_CP_K7_transit`=1.5707963267948966 (=π/2 EXACT, S100b); `eta_BBN_obs`=6.12e-10; `eta_BBN_err`=4e-12; `Delta_0_GL`=0.7704350982797368 (QP gap = pair-creation threshold = m_eff); `Delta_0_OES`=0.4642547394830737 (robustness x-check); `epsilon_K7`=0.00248; `n_pairs`=59.8; `H_fold`=586.5267713108464. From `s43_schwinger_factor36.npz`: `v_terminal`=26.54496622 (substrate acoustic-white-hole surface gravity = e·E at canonical fold), `S_Schwinger_BCS`=0.0702 PROVEN.
- **Verdict**: gate NOT covered by any closure. The prior S43 Schwinger + S61 transit-baryogenesis are MIGRATED/INFO; the acoustic-Schwinger **Mach-scan** of η_B is unevaluated. Proceeded to compute.

**Verdict**: **FAIL** — composite (collapse rule) from 3-tuple `sign_verdict=PASS, magnitude_verdict=FAIL, regime_verdict=VALID`. The acoustic-Schwinger η_B at the Mach-13.75 transit is **4.517492e-11**, and its **absolute ceiling** (production-unsuppressed limit E→∞) is **4.846254e-11** — still **1.10 OOM below** the band-low 3e-10. The 1.1-OOM shortfall is **NOT** a Mach-number (field-strength) effect; the field-strength corridor is **CLOSED**. Track-B (independent-mechanism-insufficient) confirmed.

- Canonical line: `INV6-W3-3-ETA-B-ACOUSTIC-SCHWINGER: FAIL -- value='eta_B_schwinger=4.517492e-11;eta_ceiling=4.846254e-11;boost_ceiling=1.072775;R_required=13.5473;boost_band_lo=6.6409;band_reachable=False;underprod_oom_ceiling=1.1013;eta_base=4.517492e-11;in_band=False' scheme=ACOUSTIC-SCHWINGER-dS-BACKREACTION convention=ABSOLUTE L_max=N/A audit_sha256=97960ac4f5f27b47fe43c92e63feaa483bd49e7891e02526e9698b47c5b98dd5 content_sha256=e6220550327456ab12daf31fea423692fd27b4e571c2923578d921a0c3d13865 schema_version=S84+`
- **dual-SHA**: `audit_sha256=97960ac4f5f27b47fe43c92e63feaa483bd49e7891e02526e9698b47c5b98dd5` `content_sha256=e6220550327456ab12daf31fea423692fd27b4e571c2923578d921a0c3d13865`
- **schema-v2 3-tuple**: `sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID` (emitted via `emit_verdict(session=6, track="investigation")`; 12 rows total).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:`):
- **script** `computations/investigation-6/inv6_w3_3_eta_b_acoustic_schwinger.py` — EXISTS. `grep "from canonical_constants import"` → `from canonical_constants import *  # noqa: F401,F403`; `grep "print_verdict_payload"` → def + call present. PASS.
- **data** `computations/investigation-6/inv6_w3_3_eta_b_acoustic_schwinger.npz` — EXISTS (full float64 headline + Mach-scan arrays + Schwinger structure + cross-checks + dual-SHA). PASS.
- **plot** `computations/investigation-6/inv6_w3_3_eta_b_acoustic_schwinger.png` — EXISTS (4-panel: exp(−S) vs Mach / η_B(Mach) vs PASS band / required-vs-achievable boost bars / Schwinger action S vs Mach). PASS.
- **verdict line** in `computations/investigation-6/inv6_gate_verdicts.txt` matching `^INV6-W3-3-ETA-B-ACOUSTIC-SCHWINGER:.* audit_sha256=[a-f0-9]{64}` — EXISTS with dual-SHA companion row + schema-v2 3-tuple companion row + 9 extra annotation rows. PASS.
- grep output pasted in the agent's final completion message (content-presence verification only, never line/byte count).

**Results**:

*Governing structure (substrate-first; acoustic-Schwinger, NOT imported sphaleron physics).* The substrate IS the supersonic transit through the van Hove fold — an acoustic white hole at Mach 13.75 (`v_transit = Mach·c_BLV = 13.75·0.485 = 6.66875 M_KK > c_s = c_BLV = 0.485 M_KK`). Pair creation at the fold is a Schwinger process in the strong, time-dependent **acoustic** background. The substrate-native Schwinger exponent (S43 SCHWINGER-36 resolution; Volovik 3He-A PG-horizon pair creation, Papers 07/29) is `n_Schwinger ~ exp(−S), S = π·m_eff²/(e·E_acoustic)`. The explanation flows `D_K eigenvalues → transit acoustic-metric (ρ/c_s)[…] → effective acoustic field gradient E_acoustic → Schwinger pair-production rate → η_B`. Substrate identifications (S43, machine-anchored): **m_eff = Δ_0 = quasiparticle gap = pair-creation threshold = `Delta_0_GL = 0.7704350983`**; **e·E at the canonical fold = the acoustic white hole's surface gravity = the modulus sweep rate `v_terminal = 26.5450 M_KK²`** (S43 proved `S_Schwinger = π·Δ_0²/|v_terminal| = 0.0702`, the substrate-correct form with NO `c_s` denominator — the system is effectively 0D, `L/ξ_GL = 0.031`; this resolved the spurious "factor-36"). The CP-bias and entropy normalization are held FIXED from the SAME S98 chain that fixed `eta_B_base`.

*NUMBERS (computed before the gate).*
| Quantity | Value |
|:---|:---|
| η_B_base (S98 `eta_B`, audit `3be22b8a`) | 4.517492e-11 |
| **eta_B_base reconstruction** (η_dkkms·σ_supp·sin φ_CP) | 4.517492e-11 — **bit-for-bit match** (`recon_match=True`) |
| m_eff = Δ_0,GL (QP gap = pair-creation threshold) | 0.7704350983 M_KK |
| e·E_canon = v_terminal (acoustic surface gravity at fold) | 26.544973 M_KK² |
| sound speed c_s = c_BLV; Mach; v_transit | 0.485; 13.75; 6.66875 M_KK |
| **S_canon = π·m_eff²/eE** | **0.070249** |
| **exp(−S_canon) (production at the fold)** | **0.932162** (93% of the way to the ceiling) |
| η_B(Mach=13.75) (the substrate value) | 4.517492e-11 |
| **η_B CEILING (E→∞, exp(−S)→1; max the channel can give)** | **4.846254e-11** |
| Schwinger ceiling boost (1/exp(−S_canon)) | 1.072775× |
| η_obs (BBN) | 6.120000e-10 |
| R_required = η_obs/η_base | 13.5473× |
| boost needed for band-low [3e-10] | 6.6409× |
| **required exp(−S) for band-low** | **6.1903 — IMPOSSIBLE (exp(−S) ≤ 1 always)** ⇒ `band_reachable=False` |
| underproduction (ceiling < band-low)? | **True**; underprod OOM at ceiling = 1.1013 |
| direction: monotone↑ in Mach; η_B > 0? | True; True |
| OES-gap x-check: ceiling (Δ_0,OES=0.4643) | 4.6342e-11 (boost 1.0258×) — still < band-low |
| in PASS band [3e-10, 1.2e-9]? | **False** |

**4-tuple**: (value=`eta_B_schwinger=4.517492e-11;eta_ceiling=4.846254e-11;boost_ceiling=1.072775;R_required=13.5473;boost_band_lo=6.6409;band_reachable=False;underprod_oom_ceiling=1.1013;eta_base=4.517492e-11;in_band=False`, scheme=`ACOUSTIC-SCHWINGER-dS-BACKREACTION`, convention=`ABSOLUTE`, L_max=`N/A`).

*Substitution chain (SIGN claim, with substituted numbers).*
- **Claim** (plan): "The acoustic-Schwinger η_B INCREASES exponentially with E_acoustic; larger Mach ⇒ larger E_acoustic ⇒ larger η_B, so the supersonic (Mach 13.75) transit is the η_B-MAXIMIZING regime, and the shortfall could be a field-strength effect."
- **Step 1**: `n_Schwinger ∝ exp(−π m_eff²/(e E_acoustic))` [Schwinger 1951; S43 substrate analog].
- **Step 2**: `E_acoustic = |∂_τ v|/c_s` → linear in `v_transit` → linear in Mach. Anchor: `e·E_acoustic(Mach) = v_terminal·(Mach/Mach_max)`, fixing the canonical fold field strength to `v_terminal = 26.545`.
- **Step 3**: `dn/dE_acoustic ∝ exp(−S)·(π m²/(eE)²) > 0` ⇒ n MONOTONE INCREASING in E. **Verified numerically**: `monotone_up=True` (all `dn>0`), `n(Mach=1)=0.3806 < n(Mach=13.75)=0.9322`.
- **Step 4**: `dn/dMach = (dn/dE)(dE/dMach) > 0`; the exponent `S = π m²/eE → 0⁺` as E grows ⇒ `exp(−S) → 1` (production UNSUPPRESSED ceiling).
- **Step 5** (read-off): `η_B = CP_bias·n/s`, `CP_bias > 0` (`sin(φ_CP=π/2)=1`) ⇒ η_B MONOTONE INCREASING in Mach; at Mach 13.75 the field is near-maximal ⇒ η_B near its production ceiling. **SIGN: η_B > 0 (baryon excess) preserved** (`sign_eta_pos=True`). The direction "supersonic transit maximizes η_B" matches the chain ⇒ **sign_verdict = PASS**; the magnitude FAILs the band.

*Structural finding (the decisive identity — "follow the algebra").* The Schwinger suppression obeys **exp(−S) ≤ 1 ALWAYS**. At the canonical fold the substrate ALREADY sits at
> **exp(−S_canon) = exp(−0.0702) = 0.9322** — i.e. 93% of the way to the production ceiling.

Therefore the MAXIMUM possible Schwinger boost (E→∞, the entire exponential headroom) is `1/exp(−S_canon) = 1.0728×`, giving an absolute ceiling `η_max = 4.846e-11`. The PASS band-low needs a **6.64×** boost; the required `exp(−S)` to reach band-low is **6.19 > 1**, which is **physically impossible**. So the in-band value is **UNREACHABLE at ANY Mach number**: `band_reachable=False`. This is construction-independent — the OES gap (`Δ_0=0.4643`) gives ceiling `4.634e-11`, still below band-low (`verdict anchor-robust`). The Schwinger exponential IS exquisitely field-strength-sensitive *in the weak-field regime* (`exp(−S)` swings 0.38→0.93 over Mach 1→13.75), but the substrate fold is already in the **strong-field (near-unsuppressed) regime**, where there is no exponential headroom left.

*Physical reason the field-strength hypothesis (feynman B-F5) does NOT close the gap.* The hope was that the exp's sensitivity means a factor-few error in the effective E maps to an OOM in η_B. That logic holds where `S ≫ 1` (suppressed). But the substrate is at `S = 0.07 ≪ 1` — already essentially unsuppressed. Increasing the field from here changes `exp(−S)` by at most 7%. The 13.5× shortfall cannot come from the production exponential because production is already near-saturated. **The shortfall lives in the CP-bias × fiber-volume suppression `σ_supp = ε_nLI²·geom·fbar = 6.469e-16`** — the SAME locus the W3-1 GGE-rescattering gate identified (its `R_enh ≤ 1` at φ_CP=π/2). Both substrate η_B-enhancement corridors (W3-1 rescattering phase, W3-3 acoustic-Schwinger field strength) are CLOSED; they converge on the same conclusion: the magnitude deficit is in the CP/suppression normalization, not in the production count.

*Constraint-map consequence (dual prior).* **Track-B (independent-mechanism-insufficient), 0.65 → 0.9.** The corridor "the Schwinger channel closes the gap at the substrate field strength" is eliminated. The δA magnitude posit (LBA-1) remains the open failure locus. **INFO-attribution (G-4 link)**: in-band would require `exp(−S) > 1` (unphysical), NOT a finite alternative Mach/E — so the residual is **NOT** a wrong-M_KK (G-4) field-strength artifact either; M_KK degeneracy cannot rescue η_B through the Schwinger production exponential. (FAIL is a real constraint-map outcome eliminating the second of the two named η_B-enhancement corridors, not an agent failure.)

*SOURCE-RECON note (Class-(c)).* The orchestrator STALE CACHE-SHA HINT (`88f1e9b1…` → `9e6d9cf7…`) targets the **s84 L12 mode cache** used by sibling gates; THIS gate reads ONLY `computations/_shared/canonical_constants.py` (on-disk SHA `8505153a884277ba…`) + `s98_w3_2_baryogen_uniqueness.npz` (on-disk SHA `4a3f9470bb52f56e…`), both pinned `<computed-at-runtime>` in plan §W3-3 input_files — no hardcoded stale literal to drift from; the s84 cache is NOT read here → zero physics effect. Documented in the verdict-line extra rows. (Minor: the imported canonical `v_terminal=26.544973` matches the `s43_schwinger_factor36.npz` value `26.54496622` to 5 sig figs; `S_canon=0.070249` is identical either way — no material effect.)

*Output artifacts*: `inv6_w3_3_eta_b_acoustic_schwinger.py` / `.npz` / `.png` under `computations/investigation-6/`.

---

### §W3-4. INV6-W3-4-ANTIMATTER-DOMAIN-HORIZON (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `INV6-W3-4-ANTIMATTER-DOMAIN-HORIZON`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (pre-transit acoustic sound-horizon vs present Hubble scale; acoustic white hole, PROVEN S85)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The pre-transit acoustic sound-horizon of the Mach-13.75 transit exceeds c/H_0, so the observable universe was inside ONE causally-connected pre-transit acoustic patch — making the δA-sourced asymmetry single-domain (consistent with the Fermi-LAT antimatter-fraction <10⁻⁵ / zero annihilation-boundary γ-flux) and giving δA a spatial characterization.
**Plan reference**: `sessions/investigation/investigation-6/investigation-6-plan-w3.md` §W3-4 (inequality operator R_horizon>1, sound-horizon integral, white-hole causal-disconnect substitution chain).

**MCP Pre-Compute Audit**:
Query-first discipline executed before writing the script (`.claude/rules/knowledge-index-usage.md`). NOT pre-closed — this specific R_horizon comparison had never been computed; the gate is new. Salient returns:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("acoustic sound horizon pre-transit white hole causal disconnect")` | **Acoustic white hole causal-disconnect FORMALIZED — PROVEN S85** (`s85_w6_acoustic_white_hole_formal`); pre/post-fold causally separated. (load-bearing structural input) |
| `search_knowledge("Fermi-LAT antimatter fraction domain bound annihilation boundary")` | No prior gate computes the antimatter-domain horizon; KZ-domain boundary-mode counting exists (S44) but not the c/H_0 comparison. Gate is NEW. |
| `get_constant("H_fold")` | 586.5267713108464 (M_KK units; S38 `s38_kz_defects.npz`). |
| `get_constant("c_BLV")` | 0.485 (M_KK units; S64 four-speed hierarchy; sound speed c_s). |
| `get_constant("M_KK")` | 7.428660036284456e16 GeV (S42 CONST-FREEZE-42). |
| `get_constant("tau_fold")` / `get_constant("Mach_max")` | 0.19 (S42) / 13.75 (van Hove fold). |
| `search_knowledge("horizon problem inflation super-horizon comoving Hubble scale")` | R_Hubble = c/H_0 = 1.3727e26 m (canonical anchor); **"Horizon problem — Ameliorated by tau-simultaneity, NOT eliminated"** (S41 §9.3). |
| `search_knowledge("pre-transit e-folds expansion scale factor cold big bang")` | **N_e^acoustic_only = 0.0282** (S53 Section 8); q(τ) transitions −0.97→+0.81 (S54 SCALE-FACTOR-54). Substrate has essentially NO metric inflation. |
| `trace_entity("tau-simultaneity horizon problem")` / `search_knowledge("single Jensen slice one tau fold")` | Canonical: **"substrate has ONE Jensen slice"** (`tau_pivot` provenance S87/S88). Single-domain = τ-simultaneity, not a metric causal patch. |

Decisive pre-compute finding: the substrate's OWN integrated expansion history (S53 EoS: N_e^total = 2.9205; S54: q −0.97→+0.81) shows exflation is **spectral complexification, NOT metric inflation** — which directly bears on whether the acoustic sound-horizon can grow super-Hubble. The S53 numbers `N_e^total = 2.9205`, `N_e^geom = 0.1734`, `N_e^acoustic_only = 0.0282` are read from `s53_phonon_eos_output.txt` Section 8 and pinned in the script's `MACHINERY_PINS` with provenance.

**Verdict**: **FAIL** (composite). `[SIGN]` 3-tuple: **sign_verdict = FAIL** (chain Step-5 predicts R_horizon > 1; measured R_horizon ≪ 1), **magnitude_verdict = FAIL** (R_horizon not in PASS band and not within the INFO a(t)-map band |log₁₀R| < 0.30), **regime_verdict = VALID** (deterministic 1000-pt quadrature, full τ-window, numeric=closed cross-check). Collapse rule: sign FAIL ⇒ composite FAIL.

`audit_sha256=198255d7b7fc13ad173be70a34939bda60b2bc2943583ca2dc70f4ce76672aac`
`content_sha256=c1bc2e893c60374d62ebb9283cde1399edc06f966baed184d3ea987c95171329`

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:`):

| Artifact | Path | must_contain | Verified |
|:---------|:-----|:-------------|:---------|
| script | `computations/investigation-6/inv6_w3_4_antimatter_domain_horizon.py` | `from canonical_constants import`, `print_verdict_payload` | ✓ (grep in completion message) |
| data | `computations/investigation-6/inv6_w3_4_antimatter_domain_horizon.npz` | exists (full float64 headline + horizons m/Mpc + e-fold history + cross-checks + dual-SHA) | ✓ |
| plot | `computations/investigation-6/inv6_w3_4_antimatter_domain_horizon.png` | exists (2-panel: horizon comparison log-bar / e-fold requirement vs substrate e-folds) | ✓ |
| verdict_line | `computations/investigation-6/inv6_gate_verdicts.txt` | `^INV6-W3-4-ANTIMATTER-DOMAIN-HORIZON:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 3-tuple companion row + 9 extra annotation rows | ✓ |

(grep output pasted in the agent's completion message; verification by content presence only, never line/byte count.)

**Results**:

**4-tuple**: `(value=R_horizon=8.885564e-32;…;super_horizon=False, scheme=ACOUSTIC-SOUND-HORIZON-S85-WHITE-HOLE, convention=RATIO, L_max=N/A)`.

| Quantity | Value |
|:---------|:------|
| **R_horizon = r_acoustic / (c/H_0)** | **8.885564e-32** (log₁₀ = −31.0513) |
| r_acoustic (comoving pre-transit sound horizon → today) | 1.219306e−05 m = 3.9515e−28 Mpc |
| c/H_0 (present comoving Hubble scale) | 1.372232e+26 m = 4.4471e+03 Mpc (anchor R_Hubble = 1.3727e26 m ✓) |
| N_required (for R_horizon = 1) | 74.3634 e-folds |
| N_e^total (substrate, S53 EoS) | 2.9205 e-folds |
| **e-fold shortfall** | **71.4429 e-folds (31.03 dex)** |
| proper sound horizon @fold | 3.854972e−35 m |
| proper Hubble radius @fold (acoustic, c_s/H_fold) | 2.196493e−36 m |
| 1+z_fold (M_KK/T_CMB, entropy-conserving) | 3.162943e+29 |

**Cross-checks (numeric 1000-pt quadrature vs own closed form)**: PROPER@fold ratio = 18.550574 (= e^N; the numeric integral computes the COMOVING-rel-fold form `(c_s/H_f)(e^N−1)`, distinct from the PROPER closed form `(c_s/H_f)(1−e^{−N})` by a factor e^N — both legitimate, separately labeled); COMOVING-rel-fold ratio = 1.000001 (numeric=closed to <1e-3). The headline R_horizon uses the proper-at-fold horizon scaled to today by (1+z_fold); the verdict is invariant to the proper-vs-comoving choice (factor e^N ≈ 18.5 = 1.27 dex against a 31-dex deficit).

**Horizon-inequality substitution chain** (with substituted numbers; plan §W3-4 Step 1–5):
- Step 1: r_acoustic = ∫₀^{τ_fold} c_s/a(τ) dτ, c_s = c_BLV = 0.485 M_KK; evaluated on the substrate's e-fold history N_e^total = 2.9205 (S53 acoustic-metric driven).
- Step 2: c/H_0 = c_fabric/H_0 with H_0 = H_fold redshifted forward (H_fold = 586.5267713108464 M_KK = 4.357e19 GeV; 1+z_fold = M_KK/T_CMB = 3.163e29).
- Step 3: white-hole causal-disconnect PROVEN S85 (v_transit = 6.66875 > c_s = 0.485; Mach 13.75 > 1) — the pre-fold patch is one causally-connected region of comoving size r_acoustic.
- Step 4: R_horizon = r_acoustic/(c/H_0) = 8.886e−32.
- Step 5 (direction read-off): chain PREDICTED R_horizon > 1 (super-horizon, single-domain). **MEASURED R_horizon = 8.886e−32 ≪ 1** ⇒ sign FAIL. The predicted direction is NOT realized.

**Constraint-map consequence** — this is a structurally-forced result, not a marginal one:
- **Track-B realized (dual-prior 0.20 → 0.9)**: the metric-acoustic sound horizon is sub-Hubble by ~31 dex. The plan's track_A super-horizon-metric hypothesis (prior 0.80) is **FALSIFIED by the substrate's own integrated expansion history**. The corridor "the acoustic white hole makes the pre-transit patch super-Hubble like inflation does" is CLOSED.
- **The substrate-first reason**: exflation is **spectral complexification, NOT metric expansion** (phononic-framing.md). The acoustic horizon cannot grow super-Hubble because there is essentially NO metric inflation (N_e^total = 2.92 ≪ ~60 required; q −0.97→+0.81). The PROVEN S85 white-hole causal-disconnect is REAL but only prevents post-fold RE-connection; it does not grow the PRE-fold comoving horizon to super-Hubble size.
- **Fermi-LAT <10⁻⁵ single-domain SURVIVES via a structurally distinct mechanism**: **τ-simultaneity** (the substrate has ONE Jensen slice; the fold occurs at one τ value for the whole substrate — `tau_pivot` canonical provenance). This is consistent with S41 "Horizon problem AMELIORATED by τ-simultaneity, NOT eliminated." The single-domain property is an INTERNAL-space (fiber) coherence, NOT a 4D metric causal patch.
- **δA spatial characterization (UB-2 / G-3 antimatter face)**: the metric-acoustic coherence scale is r_acoustic = 3.95e−28 Mpc (NOT super-Hubble); δA's actual single-domain coherence is τ-simultaneity. The G-3 antimatter-domain-structure face is filled — but by τ-simultaneity, not by R_horizon > 1. This is a substrate-honest reframe of the plan's UB-2 closure: the conclusion (single-domain, zero annihilation-boundary γ-flux) HOLDS; the mechanism is τ-simultaneity, not a metric acoustic horizon.
- **Routing**: the a(t)-map sharpening (the post-fold expansion history H_fold→H_0) carries the K_pivot/a(t) gap (atlas-04 C1/C2); but no plausible a(t)-map refinement closes a 31-dex / 71-e-fold deficit, so the FAIL is robust against the a(t)-map uncertainty (hence magnitude FAIL, not INFO).

**dual-SHA**: `audit=198255d7b7fc13ad…`, `content=c1bc2e893c60374d…`. **schema-v2 3-tuple**: `sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`. **Output artifacts**: `inv6_w3_4_antimatter_domain_horizon.py/.npz/.png`.

---

## Wave 3 Synthesis (team-lead)

Wave 3 attacked baryogenesis (η_B) and the antimatter sector. The wave's signature is a **convergent FAIL**: the two independent η_B-enhancement mechanisms both close, and they localize the deficit to the *same* place — the CP-bias/σ_supp normalization, not the production count — while the uniqueness gate forecloses the natural rescue.

- **W3-1 FAIL** — GGE inter-branch rescattering cannot supply the ~13.5× η_B gap. Decisive structural identity: at the substrate's maximal CP phase φ_CP=π/2, `R_enh = |Σ wᵢ cos(δ_strong,i)| ≤ 1 EXACTLY` (coherent branch sum capped at 1; measured 0.999). Rescattering can only *suppress*, never enhance, at the no-boost point (the LHCb-2025 baryon-CP boost needs *non-maximal* weak phases). sign=PASS (ceiling confirmed), magnitude=FAIL.
- **W3-3 FAIL** — the acoustic-Schwinger field-strength/Mach corridor is also eliminated: `exp(−S) ≤ 1` and the fold already sits at 93% of the production ceiling (S_canon=0.0702 ⇒ exp(−S)=0.9322), so the entire E→∞ headroom is only ×1.073; in-band needs the impossible exp(−S)=6.19. Anchor-robust (OES gap gives the same). sign=PASS, magnitude=FAIL.
- **W3-2 INFO** — the J-breaking deformation enumeration: |S_admissible|=2 basis directions (so φ_88 is not the unique *basis* direction → literal INFO), BUT the **independent CP-source rank is 1 = span{λ₈} = φ_88** (the second survivor is collinear with λ₈ in hypercharge projection, machine-zero residual). So φ_88 IS the unique CP-source *subspace* — which **forecloses** the optimistic "source-multiplicity enlarges η_B" rescue (no physical sum).
- **W3-4 FAIL** — the pre-transit acoustic sound-horizon single-domain test for the Fermi-LAT antimatter-fraction <10⁻⁵ returns FAIL (verdict on disk, line 88; full characterization in §W3-4 above).

**The convergence (the wave's headline)**: W3-1 (rescattering R_enh≤1) and W3-3 (Schwinger exp(−S)≤1) are *independent* mechanisms that both cap η_B-enhancement at ≈1 — and both conclude the magnitude deficit lives in the **CP-bias × fiber-volume suppression σ_supp normalization, NOT the production count**. W3-2 then proves the CP source is rank-1 (φ_88), so the deficit cannot be relieved by multiplying CP sources. Three gates triangulate the same residual locus.

### (a) Numerical revisions
- W3-1: R_enh=0.999219 (ceiling 1.0); R_required=13.5473; η_B stays 4.514e-11 vs observed 6.12e-10.
- W3-3: S_canon=0.0702, exp(−S)=0.9322 (93% of ceiling); boost ceiling ×1.073; η_max=4.846e-11; band needs ×6.64.
- W3-2: |S_admissible|=2; independent CP-source rank=1; ε_CP(λ₈)=1.028e-07 (= S98 canonical EXACTLY); off(2,7) residual proj_Y=2.78e-17.

### (b) Structural changes
- **Both η_B-enhancement corridors CLOSED convergently** — rescattering (W3-1) and acoustic-Schwinger (W3-3) both capped at ≈1; the deficit is normalization (σ_supp), not production count.
- **CP-source rank = 1 (φ_88)** (W3-2) — sharpens LBA-1 from a basis-uniqueness claim to a rank-1 subspace statement; forecloses source-multiplicity rescue of η_B.
- **Single-domain antimatter test FAIL** (W3-4) — closes that corridor for the Fermi-LAT bound (detail in §W3-4).

### Effected In-Session (non-math; team-lead)
- [x] Wave-3 synthesis (this section) + math/non-math split written — `investigation-6-w3-workingpaper.md §"Wave 3 Synthesis"`.
- [x] No session-track register edits (track-local boundary): HY1 (EVOI Rank-8 baryogenesis CLOSED→CONDITIONAL down-tag), HY2 (η_B falsifier-row mint, mack sole-writer), HY3 (δ_CP^PMNS falsifier-row), and the atlas-04 reconciliations are SESSION-TRACK — routed to housekeeping §B / `/rclab-investigate --investigation 6` close, NOT effected here.

## Carry-Forward Computations

### CF-INV6-W3-A — σ_supp normalization recompute (the localized η_B deficit)
1. **What**: compute the CP-bias × fiber-volume suppression σ_supp directly (the residual locus both W3-1 and W3-3 convergently identified), to test whether the ~13.5× η_B deficit is a σ_supp normalization error rather than a production-count shortfall.
2. **Inputs**: `inv6_w3_1_eta_b_gge_rescattering.npz` (audit d08cffd9), `inv6_w3_3_eta_b_acoustic_schwinger.npz` (audit 97960ac4), `inv6_w3_2_*.npz` (rank-1 φ_88 CP source); C6 baryogenesis canonical.
3. **Gate**: `|η_B(σ_supp-recomputed)/6.12e-10 − 1| ≤ info_band` PASS (deficit was normalization) / FAIL (deficit is structural in production); pre-register the band.
4. **Effort**: ~1 compute.

### CF-INV6-W3-B — Session-track promotion: η_B convergence + CP-source rank-1 + HY1/HY2/HY3
1. **What**: lift the W3-1/W3-3 convergent closure + the W3-2 rank-1 φ_88 CP-source into session-mode for: EVOI Rank-8 baryogenesis CLOSED→CONDITIONAL down-tag (HY1), η_B + δ_CP^PMNS falsifier-row mints (HY2/HY3, mack sole-writer), atlas-04 reconciliation.
2. **Inputs**: the three W3 npz + verdict lines (W3-1 d08cffd9, W3-2 ca1fd44a, W3-3 97960ac4); EVOI table; atlas-04; falsifier-master-inventory.
3. **Gate**: session re-verify + registry/EVOI/inventory landings (artifact-existence, mack sole-writer for inventory rows).
4. **Effort**: ~1 compute + registry/EVOI/inventory landings.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | η_B GGE-rescattering enhancement (W3-1) | candidate ~13.5× source | CLOSED — R_enh≤1 at φ_CP=π/2 | coherent-sum ceiling |
| 2026-06-15 | η_B acoustic-Schwinger enhancement (W3-3) | candidate Mach/field-strength source | CLOSED — exp(−S)≤1, fold at 93% ceiling | Schwinger exponential ceiling |
| 2026-06-15 | η_B deficit locus | unlocalized (~13.5× short) | σ_supp CP-bias/fiber-volume normalization (not production count) | W3-1 ∧ W3-3 convergence |
| 2026-06-15 | J-breaking CP source (LBA-1) | "φ_88 unique" (basis claim) | rank-1 CP-source subspace = span{λ₈}=φ_88; source-multiplicity rescue foreclosed | deformation enumeration |
| 2026-06-15 | Single-domain antimatter (W3-4) | candidate | FAIL (sound-horizon vs c/H_0; detail §W3-4) | pre-transit horizon test |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict (audit short) |
|:-----|:-------|:------------|:------------|:----------------------|
| INV6-W3-1 | `inv6_w3_1_eta_b_gge_rescattering.py` | ✓ | ✓ | `d08cffd9` (FAIL) |
| INV6-W3-2 | `inv6_w3_2_j_breaking_deformation_enum.py` | ✓ | ✓ | `ca1fd44a` (INFO) |
| INV6-W3-3 | `inv6_w3_3_eta_b_acoustic_schwinger.py` | ✓ | ✓ | `97960ac4` (FAIL) |
| INV6-W3-4 | `inv6_w3_4_antimatter_domain_horizon.py` | ✓ | ✓ | (FAIL, line 88) |

All under `computations/investigation-6/`; verdicts in `inv6_gate_verdicts.txt`.
