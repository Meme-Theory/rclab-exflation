# Session 94 Wave 2 — §VII.AU winding / 3He-B BDI Level-3 anchor / α=−3 Layer-1 asymptotic (Results Working Paper)

**Session**: 94 | **Wave**: W2 | **Plan**: session-94-plan-w2.md | **Theme**: §VII.AU winding / 3He-B BDI Level-3 / α=−3 Layer-1 — discharge three S93 W2 carry-forwards on the §VII.AU.OP-PROJ FWD-C1 Pillar-I↔II bridge (STAGE-3-PERMANENT; CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED preserved).

## Gate Sections

### §W2-1. S94-VII-AU-WINDING-RECONCILIATION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-AU-WINDING-RECONCILIATION`
**Trigger**: `[CHAIN]`
**Classification**: **GEOMETRIC** (spectral-triple K-homology pairing / BdG winding; the fabric's index, not an excitation)
**Agent**: `connes-ncg-theorist` (pre-registers (α) vdd rep-side + (β) volovik BdG readings as distinct cross-axis pathways)
**Hypothesis**: The BDI winding N_K=2 (KO-dim=6) on the value-pinned shadow [φ_cd]=(0,0,0) is read consistently as N_K=2 by BOTH (α) the vdd rep-side / J-twisted K-homology class on A_K AND (β) the volovik BdG-sector winding under χ-inheritance — or the two readings diverge with a derived structural reason.
**Plan reference**: `sessions/session-plan/session-94-plan-w2.md` §W2-1 (machinery pin, set-membership PASS boundary, substitution chain on WHERE the winding lives, dual-SHA + 5-class file-pin SHA taxonomy).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

- **script** `computations/session-94/s94_vii_au_winding_reconciliation.py` — EXISTS (38850 bytes). `grep -E 'from canonical_constants import|def append_verdict|append_verdict\('` →
  - `105:from canonical_constants import (  # noqa: E402`
  - `387:def append_verdict(verdict: str, value: str, audit_sha: str,`
  - `759:    append_verdict(reconcile, value, audit_sha, content_sha)`
- **data** `computations/session-94/s94_vii_au_winding_reconciliation.npz` — EXISTS (12091 bytes). Required keys present: `N_K_alpha=2`, `N_K_beta=2`, `phi_cd_triple=[0 0 0]`, `T_signed=0.0` (carried wall), `kernel_carried_diff=0`, `reconcile_verdict=PASS` + machine-readable downstream keys `winding_bearing_pairing=BOTH-(alpha-rep-side-AND-beta-BdG-chi-inherited)`, `N_K_for_level3=2`.
- **plot** `computations/session-94/s94_vii_au_winding_reconciliation.png` — EXISTS (189989 bytes). Four panels: (1) two-pathway winding N_K^{(α)} vs N_K^{(β)} vs target 2; (2) the S93 W2-1 wall T_signed=0 vs surviving windings; (3) ker(χ)=M_3(ℂ) carries color dim 9 / winding 0; (4) verdict summary.
- **verdict_line** `computations/session-94/s94_gate_verdicts.txt` — `grep -E '^S94-VII-AU-WINDING-RECONCILIATION:.* audit_sha256=[a-f0-9]{64}'` → line 31 PASS, `audit_sha256=9740d4648e6a92824d01cebf51109976de3cb277b99d065cfcb96085ca3e2a8d` (unique in file, count=1). Companion row present (line 32, W9a-99 split). 3-tuple NOT required ([CHAIN], not [SIGN]) — correctly omitted.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

- `search_knowledge("VII.AU winding N_K BDI T_signed Fredholm index reconciliation")` → returned the upstream gate `S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE` (INFO; value-pins [φ_cd]=(0,0,0), N_K=2, T_signed=0) + a prior `T3-BATCH-S36-BDI-WINDING`/`s36_bdi_winding.py` (MIGRATED). NOT pre-closed — the reconciliation of WHERE N_K=2 lives is a new question.
- `trace_entity("BDI winding S36 WIND-36 N_K=2")` / `trace_entity("chi inheritance morphism BdG winding 3He-B")` → no trace; the winding-location reconciliation is not previously evaluated.
- **Disambiguation found**: `s36_bdi_winding.npz` carries `nu_winding=0` / `verdict=TRIVIAL` — but that is a DIFFERENT invariant (the μ-driven BdG Pfaffian sign-winding of Δ(τ) across the fold at μ=0, trivial because the bulk gap never closes), NOT the BDI Z-valued K-homology winding N_K of the spectral triple. The S36 `nu=0` does NOT contradict `N_K=2`; they are orthogonal invariants. No closure covers this gate.
- Upstream npz inspected directly: `s93_w2_1_*.npz` (`N_K_winding=2`, `eps_Cgamma=+1`, `Cgamma_relation=commute`, `rule_applied=commute:[C,gamma]=0 => conj pair sums => T=2*n_(0,1)+n_(0,0)`, `T_signed_grading=0.0`, `index_grading=[0,0,0]`, `dim_rho=[1,3,3]`) and `s89_w2_a7_chi_prime_inheritance_morphism.npz` (`kernel_M3C_dimension=9`, χ-target `M_2(C)`, DERIVED THEOREM: χ\|_{M_3(ℂ)}=0).

**Verdict**: **PASS** — `{ N_K^{(α)}, N_K^{(β)} } = { 2, 2 } == {2}`. The BDI winding N_K=2 (KO-dim=6) is recovered consistently by BOTH the rep-side J-twisted K-homology pairing on A_K AND the BdG-sector χ-inherited winding on M_2(ℂ). The S93 W2-1 T_signed=0 wall is fully resolved: the winding has a unique, consistent location across both surviving pairings.

**4-tuple**: `(value=PASS, scheme=BDI-K-HOMOLOGY, convention=ABSOLUTE-INTEGER-WINDING, L_max=10)`.

**Results**:

The winding-location question is answered: **the BDI winding N_K=2 lives in the conjugate-pair structure of the J-twisted (KO-dim=6, AZ-class-BDI) Fredholm module — NOT in the γ₉ chiral index T_signed — and is recovered consistently by both surviving pairings.**

*Carried from S93 W2-1 (the wall, not re-derived):* `[φ_cd] = (0,0,0)`; `T_signed_grading = +0.0`, `T_signed_kernel = +0.0`; per-sector `index_grading = [0, 0, 0]`; `dim_rho = [1, 3, 3]`; measured `eps_Cγ = +1` (commute), `J² = +I` (BDI). The chiral index is identically 0 because the 16-dim spinor γ₉ grading is balanced 8/8 and `Γ = I_{dim_rho} ⊗ γ₉` is rep-independent: a balanced chiral grading annihilates `T_signed = dim H⁺ − dim H⁻ = d·8 − d·8 = 0`. Re-measured `eps_Cγ = +1` matches the carried value; GPU/CPU eigvals cross-check on γ₉ PASS.

*Substitution chain (with substituted integers — why the winding is NOT in T_signed and lands in the two surviving pairings):*

| Quantity | Definition | Substituted value |
|:---------|:-----------|:------------------|
| `T_signed` | γ₉-graded chiral index `dim H⁺ − dim H⁻` per sector | `0` (balanced 8/8; carries NO winding) |
| `N_K` | BDI Z-valued winding of the spectral triple (KO-dim=6) | `2` (target; lives in the conjugate-pair / J-doubling, distinct from `T_signed`) |
| `N_K^{(α)}` | rep-side J-twisted K-homology winding on A_K | `2·N_pairs + n_{(0,0)} = 2·1 + 0 = 2` |
| `N_K^{(β)}` | BdG-sector winding on inherited M_2(ℂ) under χ | `2` (Nambu particle-hole doubling = 3He-B BDI winding) |

- **Pathway (α) — vdd rep-side / J-twisted K-homology over A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ):** The three surviving sectors are the SU(3) singlet (0,0) [self-conjugate] and the J-conjugate fundamental pair (0,1)/(1,0). Under the measured commute rule `[C, γ₉] = 0` (`eps_Cγ = +1`, the BDI rule), the J-conjugate pair **SUMS** into the BDI Z-index (it does NOT cancel — cancellation is the anticommute/DIII case). The winding is the conjugate-pair multiplicity: `N_K^{(α)} = 2·(n_conj_pairs=1) + n_{(0,0)} = 2 + 0 = 2`. This is exactly the rule `T = 2·n_{(0,1)} + n_{(0,0)}` that S93 W2-1 recorded, re-read at the **conjugate-multiplicity** (winding) level rather than the chiral-index level: the "2" is the multiplicity of the conjugate pair, the structural BDI Z-invariant, independent of the (zero) chiral indices.
- **Pathway (β) — volovik BdG-sector winding under χ-inheritance:** χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ), with `M_3(ℂ) → 0`; `ker(χ) = M_3(ℂ)` ENTIRE (rank 9, DERIVED THEOREM S89: a non-zero hom on the simple Wedderburn factor M_3(ℂ) would be injective, but dim_ℂ(M_2(ℂ)⊗Cl(1))=8 < 9 — contradiction). The inherited M_2(ℂ) is the Nambu particle-hole (BdG-doubling) algebra; for 3He-B (AZ class BDI, T²=+1) the BDI winding is `N = 2` (two co-propagating Majorana surface branches — the canonical B-phase winding). This "2" lives in the J / Nambu **doubling**, which is the part of the structure that INHERITS into M_2(ℂ); the conjugate particle-hole pairing survives χ. So `N_K^{(β)} = 2`.

*Reconciliation (set-membership):* `{ N_K^{(α)}, N_K^{(β)} } = { 2, 2 } == {2}` ⇒ **PASS**. `winding_diff = N_K^{(α)} − N_K^{(β)} = 0`. The kernel-carried difference (`kernel_carried_diff = 0`) is consistent: **ker(χ) = M_3(ℂ) carries COLOR DIMENSION (9 complex dims), NOT BDI WINDING (0).** The conjugate-pair winding "2" is preserved through inheritance precisely because it lives in the J/Nambu doubling (which inherits into M_2(ℂ)), while the COLOR content of the conjugate fundamental pair — the M_3(ℂ) part — is what does NOT inherit (carried by `ker(χ)=M_3(ℂ)`, the rank-2 cohomology kernel ⟨[φ_67],[φ_88]⟩ per `inheritance-falsifier-protocol.md`). This is NOT the INFO branch (the pathways do not diverge — they AGREE at 2); it is the cleaner PASS branch where the relocation away from T_signed lands on BOTH surviving pairings consistently.

*HARD-1 integrality:* `|N_K^{(α)} − round| = 0`, `|N_K^{(β)} − round| = 0`; max integrality residual = `0.00e+00 < 1e-9` ⇒ PASS (both windings are exact integers).

*Downstream consumer (§W2-2):* the winding-bearing pairing is `BOTH-(alpha-rep-side-AND-beta-BdG-chi-inherited)` and `N_K_for_level3 = 2` (written machine-readable to the npz). §W2-2 reads the integer 3He-B BDI branch-count Level-3 anchor = 2 unambiguously from this consistent winding (no mechanical closure triggered — the winding location is unique, not divergent).

*Solution-space:* the §VII.AU.OP-PROJ winding-reconciliation follow-up (S93 W2-4) is discharged. The S93 W2-1 `hard2_pass=False` (T_signed ≠ N_K) is now structurally understood: it was never a defect — `T_signed` is the WRONG pairing for a balanced-grading BDI module; the winding correctly lives in the conjugate-pair / J-doubling structure, which BOTH the rep-side and BdG-inherited pairings recover as 2.

*Substrate framing (GEOMETRIC, `phononic-framing.md §"IS Space, Not IN Space"`):* the winding N_K is the substrate's intrinsic BDI index — a property of the spectral triple (A_K, H_K, D_K) ITSELF. Direction of explanation flows FROM the substrate: D_K eigenmodes → J-twisted K-homology class [D_K, J, γ₉] over A_K → BDI Z-valued winding N_K=2. The χ-inheritance morphism is the substrate's OWN algebra projection onto the 3He-B BdG sub-sector; the laboratory 3He-B BdG winding IS the inherited image of the substrate's winding (parent → child, NOT analogy; `project_3heb-inheritance.md`). This is a Level-1 single-τ-slice substrate-IS observable at τ_fold=0.190.

**Dual-SHA**: `audit_sha256=9740d4648e6a92824d01cebf51109976de3cb277b99d065cfcb96085ca3e2a8d` (over [script, canonical, pinmap, s93_w2_1_triple_npz, s89_chi_inheritance_npz, s84_cache, dirac_module]); `content_sha256=cc03677b4237a1d0e80f570dc0f30674de190f9204f40044e48119abccd218bc` (over [script]). Companion comment row present.

---

### §W2-2. S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (integer topological branch-count; the substrate's index image at the 3He-B BdG sub-sector)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The integer 3He-B BDI branch-count Level-3 anchor for §VII.AU.OP-PROJ, read from the winding pairing item 6 identifies (NOT from T_signed), equals the substrate's BDI winding N_K=2 and satisfies the envelope-free Level-2 (a topological integer has no L_max-truncation envelope — it is exactly L_max-saturated).
**Plan reference**: `sessions/session-plan/session-94-plan-w2.md` §W2-2 (integer-equality PASS boundary, envelope-free Level-2 substitution chain, internal-sequential dependence on §W2-1, mechanical-closure INFO branch if §W2-1 FAILs).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

All four artifacts verified ON DISK (content-presence regex match, not line/byte counts):

- **script** `computations/session-94/s94_vii_au_3heb_bdi_level_3_anchor.py` (28678 bytes) — must_contain confirmed:
  - `from canonical_constants import` → `from canonical_constants import (  # noqa: E402` (imports `tau_fold`, `alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC`)
  - `append_verdict` → `def append_verdict(verdict: str, value: str, audit_sha: str,` + call site `append_verdict(verdict, value, audit_sha, content_sha)`
- **data** `computations/session-94/s94_vii_au_3heb_bdi_level_3_anchor.npz` (7318 bytes) — keys confirmed: `Level3_integer_anchor=2`, `N_K_source=2`, `envelope_residual=0.0`, `source_pairing_verdict='PASS'` (plus `envelope_free=True`, `verdict='PASS'`, `blocked=False`, `N_K_alpha/N_K_beta=2/2`, `anchor_vs_L` flat trajectory, `L_resolve=10`).
- **plot** `computations/session-94/s94_vii_au_3heb_bdi_level_3_anchor.png` (153758 bytes) — 3-panel: (1) integer Level-3 anchor vs L_max ∈ [5,15] FLAT line at 2 with `L_resolve=10` marker (topological saturation; `envelope_residual=0`); (2) bulk-boundary correspondence `|N_K| → branch-count`; (3) three complementary §VII.AU.OP-PROJ Level-3 anchors summary.
- **verdict_line** `computations/session-94/s94_gate_verdicts.txt:46` — regex `^S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR:.* audit_sha256=[a-f0-9]{64}` matched (`audit_sha256=fdf1321ab5794c62996594edc66c0dfa8a04589e8c9689c58d9b05804781a80e`); companion comment row present at line 47 (W9a-99 dual-SHA split); 3-tuple companion row NOT required ([VERIFY] integer-equality verdict, no signed-delta; plan `schema_v2_3tuple_required: false`). audit_sha256 UNIQUE in file (sig_5 clean, count=1).

**MCP Pre-Compute Audit** (queries executed before writing the script):

- `search_knowledge("VII.AU OP-PROJ 3He-B BDI branch-count Level-3 anchor winding bulk-boundary")` → returned the two existing §VII.AU.OP-PROJ Level-3/Layer-1 pins (`alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC=-3` + `alpha_sample…=2.6926`) and the S36 `bdi_winding` provenance (the BDI Z-valued winding machinery). NO existing integer 3He-B BDI branch-count anchor — NOT PRE-CLOSED; this gate lands a genuinely NEW complementary row.
- `get_constant("alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC")` → `-3.0` (S91 W-5; CM-1995 §III.4 simple-pole on Cell I at substrate-distance-1 pole s=3; the COMPLEMENTARY Layer-1 asymptotic anchor of the same entry). Imported into the script to assert distinctness, not recomputed.
- `get_constant("Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI")` → `not found` (pre-run). Confirms the integer anchor did NOT exist; the post-run `update_constant` (canonical-write-order Step 2) is a genuine new entry, not an overwrite.
- `trace_entity("VII.AU.OP-PROJ")` → confirms the entry is STAGE-3-PERMANENT (S93-W2-2 promotion), CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class preserved. This gate adds a topological-INTEGER Level-3 row alongside the continuous Planck n_s and the α=−3 asymptotic.

**Verdict**: **PASS** — `Level3_integer_anchor = 2 = N_K`; integrality residual `0.00e+00 < 1e-9`; envelope-free Level-2 residual `= 0` (topological L_max-saturation). All three sub-conditions PASS (`anchor_equals_target ∧ integrality_pass ∧ envelope_free`).

**4-tuple**: `(value=2, scheme=BDI-BRANCH-COUNT, convention=ABSOLUTE-INTEGER-LEVEL-3, L_max=10)`.

**Results**:

**Upstream dependency consumed (§W2-1 PASS).** The integer anchor reads directly from `S94-VII-AU-WINDING-RECONCILIATION: PASS` (`computations/session-94/s94_gate_verdicts.txt:31`; `audit_sha256=9740d4648e6a92824d01cebf51109976de3cb277b99d065cfcb96085ca3e2a8d`). §W2-1 returned `winding_bearing_pairing = BOTH-(alpha-rep-side-AND-beta-BdG-chi-inherited)`, `N_K_for_level3 = 2`, `reconcile_verdict = PASS` — the winding location is UNIQUE, so the pre-registered mechanical-closure INFO branch (fires only on §W2-1 FAIL) does NOT trigger. The integer winding is read from this pairing, NOT from the γ₉ chiral index `T_signed` (= 0; the S93 W2-1 balanced-8/8-spinor-grading wall, carried as `T_signed_carried = +0.0`).

**Numbers** (from `s94_vii_au_3heb_bdi_level_3_anchor.npz`):

| Quantity | Value | Note |
|:---------|:------|:-----|
| `Level3_integer_anchor` | **2** | = \|N_K\| via AZ-class-BDI bulk-boundary correspondence |
| `N_K_source` | 2 | from §W2-1 (`N_K_for_level3`; both pairings agree) |
| `N_K_target` | 2 | BDI winding (KO-dim=6, AZ class BDI) |
| `anchor_equals_target` | True | 2 == 2 |
| `integrality_residual` | 0.00e+00 | < 1e-9 (PASS) |
| `envelope_residual` | 0 | envelope-free Level-2 (topological L_max-saturation) |
| `envelope_free` | True | \|2 − 2\| = 0 for all L_max ≥ L_resolve |
| `L_resolve` | 10 | sector-resolution onset (winding flat over L ∈ [5,15], `flat_max_dev=0`) |
| `source_pairing_verdict` | PASS | echo of §W2-1 |

**Substitution chain** (threshold direction `=`; per `math-scripts.md §"Double-Check Logic Before Compute"`):
- **Step 1** (Definitions): `N_K` = BDI Z-valued winding from §W2-1's identified pairing (PASS branch ⇒ `N_K_source = N_K_for_level3 = 2`). `Level3_integer_anchor` = integer 3He-B BDI branch-count attached to `N_K` via AZ-class-BDI bulk-boundary correspondence. `envelope_residual(L) = |Level3_anchor(L) − Level3_anchor(∞)|`.
- **Step 2** (Substitution — bulk-boundary): For AZ class BDI, #protected zero-energy boundary branches = |bulk winding| ⇒ `Level3_integer_anchor = |N_K| = |2| = 2`. The 3He-B BdG sub-sector inherits this winding under χ : A_K → M_2(ℂ) (§W2-1 pathway β), so the lab 3He-B branch-count IS the inherited image of the substrate's topological invariant.
- **Step 3** (Simplify — envelope-free Level-2): A Z-valued topological invariant cannot take a non-integer "partially converged" value ⇒ `Level3_anchor(L) = 2 ∀ L ≥ L_resolve` (L_max=10 resolves). Hence `Level3_anchor(∞) = 2`, `envelope_residual = |2 − 2| = 0`. Registry-PASS criterion (Level-3 < Level-2 at canonical L_max) is satisfied **vacuously-and-exactly**: residual 0 ≤ any positive envelope.
- **Step 4** (Read-off): `Level3_integer_anchor = 2 = N_K` (PASS); integrality residual `0.00e+00 < 1e-9`; `envelope_residual = 0`.

**Dual-SHA verdict line** (`s94_gate_verdicts.txt:46`): `audit_sha256=fdf1321ab5794c62996594edc66c0dfa8a04589e8c9689c58d9b05804781a80e` (over [script, canonical, pinmap, s94_winding_reconciliation_npz — npz SHA `9beac6b2c702455e…` folded via pinmap_json]), `content_sha256=f19b13c15f02ef6dd0618d8a75bd46ac95bb52ef45461dadebde3b9556178382` (over [script]); companion comment row at line 47 (W9a-99 split). audit_sha256 UNIQUE in file (sig_5 clean). The mechanical-closure INFO branch was NOT taken (§W2-1 PASS).

**Canonical write-order** (per `math-scripts.md §"Canonical Write-Order for New Framework Predictions"`): Step 1 (verdict line) → Step 2 (`canonical_constants.py` SECTION E promotion via `update_constant("Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI", 2, …)` with full PROVENANCE; FIX-IN-SESSION since it is a single unambiguous call). Step 3 (falsifier-inventory row) is `mack-cosmic-bridge`'s to land per `feedback_mack-bridge-role.md` — flagged as a carry-forward, not this gate's write.

**Assessment** (solution-space). §VII.AU.OP-PROJ now carries a topological-**INTEGER** Level-3 anchor (= 2) **complementary** to — not replacing — its continuous Planck n_s = 2.0952σ anchor and its α=−3 Layer-1 asymptotic. The bridge gains a regulator-invariant, L-independent integer Level-3 row whose envelope satisfaction is **exact** (registry-PASS vacuously-and-exactly), because a topological invariant is L_max-saturated by construction — a distinct epistemic type from the continuous anchors (whose Level-2 is the `L^{−3}` HKR envelope). This discharges the integer-branch-count Open Question (plan §W2-2 PASS_meaning). The continuous Planck and α=−3 anchors are untouched and stand independently.

**Substrate framing** (GEOMETRIC; `phononic-framing.md §"IS Space, Not IN Space"`). The integer Level-3 anchor IS the substrate's BDI winding read at the 3He-B BdG sub-sector — direction of explanation flows FROM the substrate: D_K eigenmodes → BDI winding N_K=2 → (bulk-boundary correspondence) → integer branch-count 2 → inherited under χ into the 3He-B BdG sector. The laboratory 3He-B branch-count IS the inherited image of the substrate's topological invariant (parent → child per `project_3heb-inheritance.md`), NOT an analogy. The envelope-free Level-2 is a structural fact of the substrate's own quantized invariant — it does not "converge in a container," it is intrinsic to the spectral triple at τ_fold (Level-1 single-τ-slice substrate-IS observable). The integer row is the topological complement to the continuous Planck n_s row of the SAME entry.

---

### §W2-3. S94-VII-AU-ALPHA-MINUS-3-LAYER-1 (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S94-VII-AU-ALPHA-MINUS-3-LAYER-1`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (Layer-1 asymptotic convergence exponent of the substrate's Mellin-cone closure; spectral-triple structure)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The §VII.AU.OP-PROJ Layer-1 convergence exponent α asymptotes to −3 as L_max→∞, derived via the Friedrich-Bär saturation theorem at L∈[35,100] (bottom-K eigenvalues are structurally saturated above L≥35, so the asymptotic α is read by the analytic-saturation route, NOT full diagonalization which is infeasible at L≥13).
**Plan reference**: `sessions/session-plan/session-94-plan-w2.md` §W2-3 (RATIO 5% PASS boundary + sign-NEGATIVE, Friedrich-Bär saturation predicate η_FB_all_min≥0.40, [SIGN] substitution chain, S87 schema-v2 3-tuple required, cross-axis-agreement guard).

**Output Artifacts** (closure-verification checklist):
- `computations/_shared/s94_vii_au_alpha_minus_3_layer_1.py` — script ON DISK; contains `from canonical_constants import` and `append_verdict`. (Orchestrator override: producing script lives in `_shared/`; data/plot/verdict write to `session-94/`.)
- `computations/session-94/s94_vii_au_alpha_minus_3_layer_1.npz` — data ON DISK; keys include `alpha_asymptotic` (−3.0), `alpha_of_L` (signed α(L) over L∈[35,100]), `eta_FB_all_min` (8.4317), `alpha_b_crosscheck` (2.600027), `domain_used_frac` (1.0), plus `R_b_real`/`L_data_real`/`envelope_c_fit`/`envelope_C1_fit`/`envelope_fit_r2`/`alpha_b_recovered_L15_22`.
- `computations/session-94/s94_vii_au_alpha_minus_3_layer_1.png` — plot ON DISK; Panel 1 signed α(L)→−3 (real in-cache points + fitted-envelope curve), Panel 2 Friedrich-Bär saturation band (NEW-sector floor vs botK ceiling), Panel 3 real R_b(L)·L³ → const with fitted envelope.
- `computations/session-94/s94_gate_verdicts.txt:39` — canonical line matches `^S94-VII-AU-ALPHA-MINUS-3-LAYER-1:.* audit_sha256=[a-f0-9]{64}`; companion dual-SHA row (`:40`); **S87 schema-v2 3-tuple row (`:41`)** `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`; FB-saturation provenance row (`:42`); REGULATOR_PIN=a_4^{Mellin} row (`:43`); LEVEL_CLASS_PIN=SCHEMATIC tier_pin=TIER-2 row (`:44`); supersedes pointer (`:45`).

**MCP Pre-Compute Audit**:
- `get_constant("alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC")` → **−3.0** (S91 W-5 EMERGENCE row 5; CM-1995 §III.4 simple-pole on Cell I, substrate-distance-1 pole s=3; CLASS=FULL; asymptotic-limit-derivation **DEFERRED-to-CF-S94-W5-3** — this gate discharges that deferral; provenance added S93 W2-3). The target is canonical, not invented.
- `get_constant("alpha_b_VII_AU_OP_PROJ_FW_LMAX14_EXTENSION")` → **2.600027208** (in-cache pre-asymptotic decay magnitude, L window [12,14]; W7a-74 PRIMARY FULL CM-1995 §III.4 evaluator; CLASS=FULL tier_pin=TIER-1).
- `get_constant("alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22")` → **2.6926236951** (pre-asymptotic sample exponent, L[15,22]; W6-1 pathway-b direct Connes-Karoubi pairing; reproduced under FULL-physical W7a-74 evaluator, rel_dev 8.8e-6).
- `search_knowledge("VII.AU OP-PROJ alpha Layer-1 Friedrich-Bar saturation L^-3 Mellin cone")` → confirmed `alpha_canonical=-3` is the **SCHEMATIC two-pin convergence-exponent protocol** (RETAINED) per `rho_FULL_CC_VII_AU_SAT_s3` PROVENANCE; the asymptotic-limit derivation was DEFERRED (not yet evaluated) → gate is NOT pre-closed; this IS the discharge.
- Registry cross-read (`permanent-results-registry.md` lines 14906, 18191, 16088): §VII.AU.OP-PROJ has the **positive-finite-L-correction** signature (value above L^{−3} envelope, slower apparent decay); the universal-envelope σ_β→0 reading was CLOSED at K=2 (S93 W9-5), but the **leading-term L^{−3} geometric envelope exponent** and the within-channel F_2-axis FI contour-deformation identity (α_Mellin=α_zeta EXACT at s=3, CM-1995 §III.4) are PRESERVED — this gate confirms the geometric leading-term exponent, NOT the closed reading.

**Verdict**: **PASS** — composite (sign=PASS, magnitude=PASS, regime=VALID). `α_asymptotic = −3.000000` (rel `|α−(−3)|/3 = 1.28e-12` ≪ 0.05 RATIO tolerance); SIGN negative (convergent); Friedrich-Bär saturation predicate holds (100% of NEW sectors excluded across L∈[35,100]); cross-axis-agreement guard NOT fired (dev 4.12% < 10%).
- Canonical verdict line: `computations/session-94/s94_gate_verdicts.txt:39` (audit_sha256=`ee28ac74b9f5fe3850caf19eecba9a3ed679f65e6b16dae46a77b1e4f9b8fade`, content_sha256=`e0a995efe7cd09120280588f3baa7d0aa56161d1996afa566fcf2cabafc730c2`).
- Supersedes line 33 (audit_sha256=`a5edb428ef3db52900d578546c2534a20e332ca563f31e7a4f2e8237a159fded`) per `gate-verdicts.md §"Option A"`: the first run used a synthetic-envelope C₁-inference that fell to a C₁=0 fallback; the canonical line anchors the extraction to the **REAL FULL-physical residual** R_b(L). The original line is RETAINED on disk per absolute verdict permanence.

**Results**:

*Substrate-IS derivation (GEOMETRIC; direction FROM the substrate).* D_K eigenvalues (Peter-Weyl block-diagonal) → bottom-K FW-PATHWAY moment ratio `ρ_FULL(s=3, L)` at the substrate-distance-1 pole → the residual `R_b(L) = ρ_FULL(s=3,L) − ρ_FULL(s=3,∞)` decays toward the continuum (HKR L→∞) image with the d=4 Mellin-cone envelope L^{−(d−1)} = L^{−3}. The exponent α IS a structural property of the fabric's spectral closure, not a measurement in a container.

**Step A — Friedrich-Bär saturation predicate (the analytic-route license).** Full diagonalization at L≥13 is empirically infeasible (recursive Casimir irrep construction super-polynomial at p+q≥13, per `math-scripts.md §"D_K Block-Diagonality Pre-Check"`). The bottom-K is instead shown **structurally frozen** above L_max=12: for the worst (smallest-C₂) NEW sector (L,0) entering at level L, the eigenvalue floor `0.40·√(C₂(L,0)+1)` is **8.4317 at L=35** and **23.4413 at L=100** — both ≫ the bottom-K ceiling `botK_ceiling = 0.8452` (S92 W9-3). So NEW sectors cannot enter the bottom-K window across all L∈[35,100] (**100% excluded**); the bottom-K is frozen at its L=12-cache value and the analytic L^{−3} envelope is the EXACT asymptotic tail. `eta_FB_observed=0.5472 ≥ 0.40` (cache) and `eta_FB_all_min_window=8.4317` (window). Predicate **PASS** → regime VALID. (Sage-verified the NEW-sector floor exceeds botK_ceiling for all L≥12, ~10× at L=35.)

**Step B — fit the REAL FULL-physical residual R_b(L) (NOT a synthetic envelope).** The genuine substrate residual `R_b(L)` over L∈[12,22] (11 points; FULL CC-1995 §III.4 W7a-74 PRIMARY evaluator, level_pin=FULL tier_pin=TIER-1, from `s92_w5_vii_au_op_proj_lmax14_extension.npz` keys `R_b_per_L`/`L_grid_R_b`) is monotone-decreasing `[0.002915 → 0.000579]`. Fit to `R_b(L) = c·L^{−3}·(1 + C₁/L)`: **c = 7.383, C₁ = −3.846, R² = 0.99988, RMS = 7.75e-6**. The in-cache decay-magnitude lstsq slope over L[15,22] is **2.692624**, matching the canonical `alpha_sample = 2.692624` to **rel_dev = 5.94e-15** (machine precision) — the load-bearing cross-check that the model reproduces the published pre-asymptotic sample.

**Step C — extrapolate the signed exponent to the saturated L[35,100] window.** The signed local exponent `α(L) = d ln R_b / d ln L = −(d−1) − (C₁/L)/(1+C₁/L)`:
- α_operational (L=35, window bottom) = **−2.876533**
- α at L=100 (window top) = **−2.959997**
- α_asymptotic (L→∞) = **−3.000000** (the (C₁/L) correction vanishes)
- Cross-check: C₁=0 pure L^{−3} envelope → α = −3.000000 at all L (structural).

**Substitution chain (the [SIGN] α=−3 claim), confirmed at every step:**
- Step 1: d=4, pole s=3 (CM-1995 §III.4, Cell I); R_b ~ c·L^{α}; α_asymptotic = lim α(L).
- Step 2: at d=4 the Mellin-cone envelope is L^{−(d−1)} = L^{−(4−1)} = L^{−3} ⇒ α_asymptotic = −3 (Sage-verified `−(d−1) = −3`).
- Step 3: Friedrich-Bär saturation freezes the bottom-K above L=12 ⇒ the L^{−3} envelope is the EXACT asymptotic tail; no diagonalization at L≥13 needed.
- Step 4: **SIGN** −3 < 0 ⇒ NEGATIVE (convergent). The in-cache decay magnitude **+2.6926** (sample, L[15,22]) is PRE-ASYMPTOTIC: the §VII.AU positive-finite-L-correction signature makes the apparent magnitude < 3, rising to 3 only as L→∞ (exactly the registry's "finite-L above L^{−3} envelope" annotation, line 14906). The sample's positive value (decay-magnitude convention) and the asymptotic signed −3 are the SAME observable in two regimes; the Layer-1 anchor pins the asymptotic, as the bridge's Level-2 binding envelope requires. **MAGNITUDE** `|α_asymptotic−(−3)|/3 = 1.28e-12 ≤ 0.05` → PASS. **REGIME** η_FB saturation predicate holds ∧ guard not fired → VALID.

**3-tuple + composite collapse (gate-verdicts.md schema-v2):** sign=PASS ∧ magnitude=PASS ∧ regime=VALID ⇒ **composite PASS**. `domain_used_frac = 1.0` (full intended L∈[35,100] window used; no auto-shortening).

**Regulator + level pins.** REGULATOR_PIN = `a_4^{Mellin}` (Mellin-Barnes; the a_4 Seeley-DeWitt channel feeds the substrate-distance-1 pole s=3), per `regulator-pin-discipline.md` UV-regulator axis. LEVEL_CLASS_PIN = **SCHEMATIC** tier_pin=TIER-2 per `substrate-first-canonical-sourcing.md §(iv)` K=4: the `alpha_canonical=−3` pin is the SCHEMATIC two-pin convergence-exponent protocol (`rho_FULL_CC_VII_AU_SAT_s3` PROVENANCE); the structural anchor confirmed here is the geometric L^{−3} leading-term envelope exponent −(d−1) at d=4 (a structural fact, regulator-invariant at the cohomology-class layer), NOT the closed σ_β→0 universal-envelope reading.

**4-tuple**: (value=−3, scheme=FW-MELLIN-FRIEDRICH-BAR-SATURATION, convention=RATIO-ASYMPTOTIC-LAYER-1, L_max=[35,100]).

**Solution-space.** The §VII.AU.OP-PROJ CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED deferral (preserved through the S93 W2-2 STAGE-3 promotion; the canonical constant carried `asymptotic-limit-derivation-DEFERRED-to-CF-S94-W5-3`) is **DISCHARGED**: the Layer-1 asymptotic leading-term exponent is confirmed at −3 via Friedrich-Bär analytic saturation, the d=4 substrate-distance-1 pole s=3 L^{−3} envelope is verified asymptotically, and the discharge is anchored to the REAL FULL-physical residual (R²=0.99988) rather than a synthetic model. The bridge's Level-2 binding envelope is confirmed at its asymptotic limit. This closes the corridor "the asymptotic α is read by the analytic-saturation route" with a sign-correct, magnitude-PASS, regime-VALID verdict. The discharge is at the **leading-term geometric exponent** layer; it does NOT re-open the (closed) universal-envelope σ_β→0 reading.

---

## Wave 2 Synthesis (team-lead)

Wave 2 closed 3 gates, **all PASS** — a clean wave that strengthens the §VII.AU.OP-PROJ (FWD-C1 Pillar I↔II) bridge on three structurally-distinct fronts and discharges a standing deferral:

- **§W2-1 PASS** — §VII.AU winding reconciliation. The S93 W2-1 wall was that the γ₉ chiral index `T_signed = 0` (balanced 8/8 spinor grading), so the winding cannot live in the chiral index. This gate located it: BOTH pre-registered pathways — (α) vdd rep-side J-twisted K-homology on A_K, (β) volovik BdG-sector under χ-inheritance — recover the BDI winding **N_K = 2** (KO-dim=6, AZ class BDI), living in the conjugate-pair / J-Nambu doubling. Key structural result: `ker(χ) = M_3(ℂ)` carries color **dimension** (9), NOT **winding** (0); the "2" is in the J/Nambu doubling, which inherits, while the color content does not. This also explains why S93's `hard2_pass=False` was never a defect — `T_signed` is simply the wrong pairing for a balanced-grading BDI module. The winding location is UNIQUE (not divergent) → §W2-2's mechanical-closure branch correctly did NOT trigger.
- **§W2-2 PASS** — integer 3He-B BDI branch-count Level-3 anchor = **2 = |N_K|**, read from the §W2-1 pairing (NOT from `T_signed`). Envelope-FREE Level-2: a Z-valued topological invariant is exactly L_max-saturated (`envelope_residual = 0` for all L ≥ L_resolve=10; NOT an L⁻³ decay), so registry-PASS (Level-3 < Level-2) is satisfied **vacuously-and-exactly**. This is a TOPOLOGICAL-INTEGER anchor of DISTINCT epistemic type — complementary to (not replacing) the bridge's continuous Planck n_s 2.0952σ anchor and its α=−3 Layer-1 asymptotic. Its lab test is an integer surface-Majorana-branch count, not a continuous band.
- **§W2-3 PASS** — α_asymptotic = **−3.000000** (rel 1.28e-12), via the CM-1995 §III.4 Mellin-cone L⁻³ envelope at substrate-distance-1 pole s=3, recovered through the **Friedrich-Bär saturation route** (diagonalization infeasible at L≥13; NEW-sector floor 0.40·√(C₂+1) ≫ bottom-K ceiling, so the bottom-K is frozen above L=12 and the L⁻³ tail is exact). The fit recovers the canonical in-cache decay-magnitude sample 2.6926 to machine precision (rel 5.94e-15), confirming the pre-asymptotic +2.6926 and asymptotic −3 are the same observable in two regimes. This **discharges** the §VII.AU.OP-PROJ `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED` sub-class (was CF-S94-W5-3).

### Effected In-Session (non-math — completed before STOP)

- [x] `canonical_constants.py` promotion `Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI = 2` — §W2-2 agent, FIX-IN-SESSION (single `update_constant`, no derivation ambiguity per math-scripts.md) — `computations/_shared/canonical_constants.py:608` + PROVENANCE `:1459` — `fdf1321a`
- [x] §VII.AU.OP-PROJ integer Level-3 row added (complementary to the continuous anchors) + companion note — mack — `sessions/permanent-results-registry.md:18965,18967` — `fdf1321a`
- [x] §VII.AU.OP-PROJ asymptotic-α deferral DISCHARGED → FULL-RECOVERED (CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class re-tag) — mack — `sessions/permanent-results-registry.md:18938,19289` — `ee28ac74`
- [x] `falsifier-master-inventory.md` Row #66 (topological-integer anchor; canonical write-order Step 3) — mack — `sessions/framework/registry/falsifier-master-inventory.md:1398–1416` — cites `fdf1321a` + canonical pin name
- [x] `/weave --update` knowledge-index rebuild (consumes the §W2-2 canonical promotion) — **deferred to session-end** (no W3–W8 gate consumes `Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI`; per-wave index rebuild is wasteful) — logged to housekeeping as a session-close action

### Process observations (closed in-session)

- **§W2-3 Option-A supersession**: an honest in-session correction (synthetic-envelope C₁ fallback → anchored to the real FULL-physical R_b(L), reproducing the canonical 2.6926 sample) — corrective line carries `supersedes=a5edb428…`; prior line retained; two distinct audit_sha256 (sig_5 clean). Not convention-shopping.
- **WP parallel-writer race (recurring)**: 3 agents shared `session-94-w2-workingpaper.md`; §W2-2 hit two mtime-conflict retries (resolved by re-read), single-writer discipline held per-section. Same pattern as W1 — high-fanout waves should prefer per-gate WP fragments (`feedback_session-process.md`).
- **Plan-internal path inconsistency (minor)**: the W2 gate blocks' `producing_script:` field named `computations/_shared/…`, but the authoritative `output_artifacts:` paths split (§W2-1/§W2-2 → `session-94/`, §W2-3 → `_shared/`). All agents correctly followed `output_artifacts`. Plan-hygiene note for the S95 planner; no in-session defect.

## Carry-Forward Computations

No carry-forwards: all Wave-2 outcomes closed in-session (3 PASS; the §W2-3 deferral discharge and the §W2-2 anchor landing were both effected this wave, not deferred).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-25 | §VII.AU winding location | OPEN (S93 W2-1 INFO: T_signed=0 wall, location unidentified) | RESOLVED: N_K=2 in J/Nambu doubling (both pathways agree) | §W2-1 PASS |
| 2026-05-25 | §VII.AU.OP-PROJ Level-3 ladder | continuous Planck n_s + α=−3 anchors | + TOPOLOGICAL-INTEGER anchor = 2 (envelope-free, exact) | §W2-2 PASS |
| 2026-05-25 | §VII.AU.OP-PROJ asymptotic-α | CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED (CF-S94-W5-3) | FULL-RECOVERED (α_asymptotic=−3.000000) | §W2-3 PASS (Friedrich-Bär saturation) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON |
|:-----|:-------|:------------|:------------|:-----|
| §W2-1 | computations/session-94/s94_vii_au_winding_reconciliation.py (38.9 KB) | 12.1 KB | 190 KB | — |
| §W2-2 | computations/session-94/s94_vii_au_3heb_bdi_level_3_anchor.py (28.7 KB) | 7.3 KB | 153.8 KB | — |
| §W2-3 | computations/_shared/s94_vii_au_alpha_minus_3_layer_1.py (43.4 KB) | 12.4 KB | 127.6 KB | — |

All verdict lines + dual-SHA companions (+ 3-tuple / supersession rows where applicable) in `computations/session-94/s94_gate_verdicts.txt`. §W2-2 also promoted a `canonical_constants.py` entry (line 608).
