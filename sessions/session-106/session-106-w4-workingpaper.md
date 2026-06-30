# Session 106 Wave 4 — Stage-2 Verification Cohort (REGISTER-SOURCED) (Results Working Paper)

**Session**: 106 | **Wave**: 4 | **Plan**: session-106-plan-w4.md | **Theme**: register-sourced Stage-2 two-agent parallel cross-axis independent-verify of two STAGE-1-CANDIDATE §VII entries (§VII.BZ K12, §VII.AD K3) from the `open-channel-ledger.md §C` cohort queue; two blind reviewer dispatches + a procedural-owner PASS-AND closeout per gate.

## Gate Sections

### §W4-1. S106-VIIBZ-STAGE2-VERIFY (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S106-VIIBZ-STAGE2-VERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **PHONONIC** (Stage-2 cross-axis verify of the §VII.BZ BDI Horizon-Faithfulness Protection STAGE-1-CANDIDATE)
**Agent**: `gen-physicist` (procedural owner of STEP-2 closeout; STEP-1 reviewers: van-den-dungen-bridge-theorist Axis-A, landau-condensed-matter-theorist Axis-B)
**Hypothesis**: both blind cross-reviewers PASS their single-axis clauses ((b) connes-axis Type-II trace / (a) volovik-axis BDI-CdGM) AND the JOINT clause (c) — the `+1/2` identification (bosonic Wightman floor = fermionic CdGM minigap = the single BDI datum fixing trace AND faithfulness) — PASSes in BOTH verdicts, qualifying §VII.BZ for STAGE-3-PERMANENT.
**Plan reference**: `sessions/session-plan/session-106-plan-w4.md` §W4-1 (reviewer assignment + Axis-B Selection Protocol, JOINT-clause PASS-AND logic, substrate-input-orthogonality declaration, machinery pin, substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-106/s106_w4_viibz_stage2_passand_closeout.py` — EXISTS (34,999 B). `grep` confirms `from canonical_constants import *` (line 121) + `def print_verdict_payload(` (line 507; called line 772). Source: modeled verbatim on `computations/session-105/s105_w6_viiu2_stage2_passand_closeout.py` (path scaffold lines 71-143; SHA + anchor-extraction + dual-SHA lines 146-236; aggregate collapse lines 269-312; payload lines 319-348; plot lines 355-411; main lines 418-509), adapted for the §VII.BZ 3-clause partition + N/A off-axis discipline.
- `computations/session-106/s106_w4_viibz_stage2_passand.npz` — EXISTS (per-clause matrix + protocol/orthogonality/SHA-drift state).
- `computations/session-106/s106_w4_viibz_stage2_passand.png` — EXISTS (per-clause PASS/FAIL/INFO/N/A grid; columns Axis-A (vdd) / Axis-B (landau) / PASS-AND).
- `computations/session-106/s106_w4_viibz_reviewer_vdd_axisA_verdict.json` — EXISTS (STEP-1 Axis-A; a=N/A, b=PASS, c=PASS).
- `computations/session-106/s106_w4_viibz_reviewer_landau_axisB_verdict.json` — EXISTS (STEP-1 Axis-B; a=PASS, b=N/A, c=PASS).
- verdict line in `computations/session-106/s106_gate_verdicts.txt` — EXISTS, matches `^S106-VIIBZ-STAGE2-VERIFY:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion row + 4 annotation rows (reviewer-pair, clause-partition, orthogonality, SHA-drift).
- this WP section — `**Status**: COMPLETED`, `**Verdict**: PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present.

**MCP Pre-Compute Audit**:
- `search_knowledge('VII.BZ BDI horizon faithfulness crossed product modular weight Stage-2')` → confirms §VII.BZ = K12 STAGE-1-CANDIDATE, atlas-08 record "Stage-2 = S106 W4" (this gate); atlas-04 K12 entry records clause (c) JOINT with "CdGM +1/2 minigap = bosonic Wightman floor" — matching the registered clause-attribution block. NOT a recompute: this gate aggregates the two on-disk reviewer JSONs under the pre-registered set-conjunction.
- `get_constant('a_2_FW_zeta')` → 2776.165389 (S88-A-N-FW-CANONICALIZATION; superseded=False). The area-operator Â = a₂ second-Seeley-DeWitt moment cited in the §VII.BZ entry — confirms the substrate-framing anchor (the horizon area IS the a₂ spectral moment, NOT a geometric area IN a container).
- PRE-CLOSED status: NO — the Stage-2 verify is the open promotion leg (the per-block numerical realization `S105-W2-2-OMEGA-FAITHFUL-NORMAL` was the already-PASS pre-gate; this gate is the cross-axis verify leg).

**Verdict**: **PASS** — composite = PASS (full all-PASS conjunction over {(a),(b),(c)}). `audit_sha256=566cdcb5fd3f9c19b3705ab20e075cbcc4ba47d29cbdad379dce40f6a68ff7c3`, `content_sha256=96be5034e872106d44b87b7460f69d9e7933d2425ae6d14b20a8d5fa2eb97c85`. The `+1/2` identification (JOINT clause (c)) is INDEPENDENTLY confirmed by both blind cross-reviewers without shared workshop context ⇒ §VII.BZ is STAGE-3-PERMANENT-ELIGIBLE.

**Results**:

*STEP-1 reviewer clause-verdict JSONs (blind, no-workshop-context):*
- **Axis-A (van-den-dungen-bridge-theorist)** — `no_workshop_context_attestation: true`; `inputs_read = [permanent-results-registry.md, canonical_constants.py]`. Clause verdicts: **(a) N/A** (volovik-axis, not Axis-A's clause — the CdGM-vs-Weyl universality-class assignment is a superfluid-universality judgment outside the NCG/Tomita-Takesaki axis), **(b) PASS** (Tomita-Takesaki construction with f.n.s. weight ⇒ modular operator Δ_ω + conjugation J, S = J·Δ^{1/2}; the crossed product `A_K ⋊_{σ^ω} ℝ` is the canonical Takesaki-duality Type-II_∞ construction with trace-scaling `τ̃ ∘ θ_s = e^{−s} τ̃`; uniqueness as faithful normal tracial weight up-to-scalar, the second moment fixing the free scalar — faithful, NOT an overstatement), **(c) PASS** (the +1/2 fixes BOTH trace (the bosonic Wightman floor IS the symmetric second moment fixing the trace-normalizing scalar) AND faithfulness (the BDI minigap +1/2·ω_0 ≠ 0 ⇒ no exact zero mode ⇒ ω faithful, the Tomita-Takesaki separating-cyclic-vector criterion); EMERGENCE-1 confirmed — both roles are extractions from ONE modular weight ω, not two independent inputs).
- **Axis-B (landau-condensed-matter-theorist)** — `no_workshop_context_attestation: true`; `inputs_read = [permanent-results-registry.md, s105_w2_2_omega_faithful_normal.npz]`. Clause verdicts: **(a) PASS** (BDI/N₃=0 anomaly-free class; CdGM ladder `E_n=(n+1/2)ω_0` with `|E_0|=1/2·ω_0 ≠ 0`, the 3He-A/DIII Weyl zero does NOT inherit through χ; RE-derived the Fermi-Dirac closed form `f_a=1/(exp(β_a E_a)+1)` at `T_GGE=0.668` (β=1.497006) to machine precision across ALL 12 Peter-Weyl blocks; `f ∈ [0.157, 0.435]` strictly interior to (0,1), all gaps strictly positive, P_exc=1.000 ⇒ saturated-but-finite β ⇒ ω faithful), **(b) N/A** (connes-axis, not Axis-B's clause), **(c) PASS** (the fermionic CdGM minigap `|E_0|=+1/2·ω_0` is FORCED by the BDI class — not adjustable; the bosonic Wightman floor `W_GGE=n_k+1/2` is the zero-point offset of `[a,a†]=1`; both +1/2's are the SAME structural object; npz confirms +1/2 as the exact additive floor `W_global_min=0.561207 = 1/2 + 0.061207`, the excess being GGE relic occupation ⇒ W>1/2 strict).

*Protocol pre-flight (STEP-2 item 2)*: **ok=True**. Reviewer identity == pinned (vdd Axis-A, landau Axis-B); `no_workshop_context_attestation == true` in BOTH; neither reviewer ∈ {connes-ncg-theorist, volovik-superfluid-universe-theorist, mack-cosmic-bridge}; clause-set exact match {a,b,c}; off-axis N/A discipline holds (vdd (a)=N/A and landau (b)=N/A on the non-owning side; JOINT (c) binding in BOTH).

*Substrate-input-orthogonality re-check (STEP-2 item 3)*: **SATISFIED**. The npz `s105_w2_2_omega_faithful_normal.npz` appears in EXACTLY ONE `inputs_read` list (landau, Axis-B; vdd loaded canonical_constants.py + registry only). The POSITIVE `inputs_read` lists are scanned (never an `inputs_explicitly_not_read` block). Predicate SATISFIED ⇒ Stage-2 PASS-AND is at the structural CEILING (structural-input independence, not merely structural-output-type independence); **NO substrate-input-overlap caveat tagged** per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`.

*Per-clause PASS-AND matrix*:

| clause | kind | Axis-A (vdd) | Axis-B (landau) | PASS-AND |
|:-------|:-----|:-------------|:----------------|:---------|
| (a) BDI/N₃=0 + CdGM-vs-Weyl | single-axis-B (volovik) | N/A | PASS | **PASS** |
| (b) Type-II trace + Tomita-Takesaki | single-axis-A (connes) | PASS | N/A | **PASS** |
| (c) +1/2 identification (EMERGENCE-1) | JOINT | PASS | PASS | **PASS** |

*Composite*: **PASS** (FAIL>INFO>PASS precedence; reachable ONLY by the full all-PASS conjunction; protocol-ok + orthogonality-satisfied ⇒ no override).

*4-tuple*: `(value=JOINT-CROSS-AXIS-STAGE-2-PASS-AND;composite=PASS|partition[…]|…, scheme=joint-theorem-stage-2-cross-axis-verify, convention=vii-bz-BDI-horizon-faithfulness-stage-1-candidate-to-stage-3-promotion-cross-axis-PASS-AND, L_max=N/A)`.

*Substitution chain (collapse)*:
- clause(a) := axis_B_token(a) = PASS [volovik-axis, landau-only].
- clause(b) := axis_A_token(b) = PASS [connes-axis, vdd-only].
- clause(c) := PASS-AND(axis_A(c)=PASS, axis_B(c)=PASS) = PASS [logical AND, not OR].
- composite := PASS ⟺ clause(a)==PASS ∧ clause(b)==PASS ∧ clause(c)==PASS. Monotone aggregation (a dropped PASS cannot raise composite); PASS reachable ONLY by the full all-PASS conjunction.
- Direction: PASS ⇒ both axes INDEPENDENTLY confirm the +1/2 identification without shared workshop context ⇒ structurally-independent agreement (`joint-theorem-promotion.md` "without prior workshop context") ⇒ STAGE-3-PERMANENT eligible.

*Dual-SHA*: `audit_sha256 = sha256(script ‖ canonical_constants.py ‖ anchor-extracted §VII.BZ entry block ‖ pinmap_json) = 566cdcb5fd3f9c19b3705ab20e075cbcc4ba47d29cbdad379dce40f6a68ff7c3`; `content_sha256 = sha256(script) = 96be5034e872106d44b87b7460f69d9e7933d2425ae6d14b20a8d5fa2eb97c85`. The §VII.BZ block was extracted ANCHOR-BASED (`### §VII.BZ` header → next `### §VII.` header; start_line 21894, len 10762 chars, block_sha256 `054d266c24affecf…`). The pinmap carries the reviewer assignment + clause map + orthogonality anchor as identity entries, so this gate's `audit_sha256` is DISTINCT from §W4-2's.

*SHA-drift disclosure (plan §W4-1 drift-disclosure discipline)*: the plan-pinned registry **file-level** SHA (`a1797e1b…`) DRIFTED to live `2d418892b5ea522f…` because §VII.CA + §VII.CB were landed this session (S106 W3) APPENDED AFTER §VII.BZ; canonical_constants.py also drifted (`38e23ad2…` → live `82dd16e2…`, updated this session). The §VII.BZ entry **BLOCK ITSELF is UNCHANGED** — the block-level content (block_sha256 `054d266c…`) is what feeds `audit_sha256`, and the live file-level SHAs (not the stale plan pins) are folded in. The orthogonality npz witness SHA `7e8a921b36f11f54…` MATCHES the plan pin exactly (drift=False).

*Reviewer registry-text-hygiene findings (DOCUMENTED, NOT registry-edited by this gate)*:
1. **landau's −½ minigap sign note**: the registry's `E_0^CdGM = −1/2·ω_0` sign is a *branch-labelling convention* of the CdGM ladder; the load-bearing physics (`|E_0| = +1/2·ω_0 ≠ 0` offset-from-zero minigap, no exact zero mode) is correct. The sign label does not bear on the clause (a) PASS.
2. **landau's clause-(c) scope point**: from the Axis-B side the +1/2 IS the genuine CdGM minigap, IS the single BDI datum, and DOES equal the bosonic Wightman floor; the *further* leg that this SAME datum "fixes the Type-II semifinite trace" is the **Axis-A (connes/vdd) contribution under the PASS-AND** — landau does not independently certify that trace-defining leg from Axis-B, and correctly defers it to the Axis-A half of the JOINT clause. This is exactly the PASS-AND structure: both halves of the +1/2 consequence (trace ← vdd; minigap/faithfulness ← landau) must each PASS.
3. **vdd's clause-(b) no-over-claim note**: clause (b) is faithful precisely because it assigns the II_∞ **trace residual scalar** to the *physical second moment* (the Wightman two-point) — the crossed product gives uniqueness up-to-scalar, and the second moment supplies the otherwise-free positive scalar; this picks the representative WITHOUT over-claiming what the NCG formalism proves.
4. **§VII.BZ entry harvested-co-author observation**: the registered §VII.BZ header authorship line names `mack-cosmic-bridge` as the registry-landing writer (conservative registry-landing-writer inclusion) alongside the substrate-physics co-authors connes + volovik; the plan-freeze audit harvested `mack` into the Stage-0 exclusion set accordingly. (Process observation; mack IS in the EXCLUDED reviewer set and neither chosen reviewer is mack — exclusion honored.)
5. **stale/un-pinned Stage-2 queued-gate-name observation**: the §VII.BZ Status line's "Promotion gate (Stage-2)" sentence references "a future two-agent cross-axis independent verify on the JOINT clause (c)" WITHOUT a pinned gate-ID, and names the numerical pre-gate as `S105-OMEGA-FAITHFUL-NORMAL` (the on-disk canonical name is `S105-W2-2-OMEGA-FAITHFUL-NORMAL` — a minor naming-drift). This S106 W4 gate IS that "future cross-axis verify". (Registry-text hygiene; routes orchestrator-direct/mack at session close, NOT a registry edit by this gate.)

*Promotion disposition*: on this composite PASS, the §VII.BZ STAGE-1-CANDIDATE → STAGE-3-PERMANENT registry tag-flip is **ORCHESTRATOR-DIRECT at session close** (the `writer_agent` pin; registry lines 21894 header + Status line) — NOT this gate's write. The verdict value + this WP section carry the eligibility; the tag edit itself is orchestrator-direct.

---

### §W4-2. S106-VIIAD-STAGE2-VERIFY (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S106-VIIAD-STAGE2-VERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (Stage-2 cross-axis verify of the §VII.AD Δ_0 LOCALIZATION FORMULA STAGE-1-CANDIDATE)
**Agent**: `gen-physicist` (procedural owner of STEP-2 closeout; STEP-1 reviewers: van-den-dungen-bridge-theorist Axis-A, kitaev-quantum-chaos-theorist Axis-B)
**Hypothesis**: vdd (Axis-A, NCG-axiomatic V_input Schur derivation) and kitaev (Axis-B, Sage-QQ exhaustive 576-config C_output) both PASS their single-axis clauses AND the JOINT SOURCE-DOUBLE-CITE-CO-PRIMARY chain-identity clause (the non-fungible V_input→A_F→C_output sequence) PASSes in BOTH verdicts, qualifying `Δ_0 = 4·c_{σ⁻¹((-1,-1))}` (the Level-1 single-τ-slice calibration-corpus instance) for STAGE-3-PERMANENT.
**Plan reference**: `sessions/session-plan/session-106-plan-w4.md` §W4-2 (reviewer assignment, CO-PRIMARY clause mapping, substrate-input-orthogonality declaration, registry path-drift note, machinery pin, substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | On-disk | `must_contain` verification |
|:---------|:-----|:--------|:----------------------------|
| Closeout script | `computations/session-106/s106_w4_viiad_stage2_passand_closeout.py` | ✅ (exists) | `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # noqa: F401,F403,E402`; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(` + call site at end of `main()` |
| Data | `computations/session-106/s106_w4_viiad_stage2_passand.npz` | ✅ (8679 B) | n/a (data) |
| Plot | `computations/session-106/s106_w4_viiad_stage2_passand.png` | ✅ (48050 B) | n/a (plot) — 3×3 grid columns Axis-A (vdd) / Axis-B (kitaev) / PASS-AND |
| Reviewer-A JSON | `computations/session-106/s106_w4_viiad_reviewer_vdd_axisA_verdict.json` | ✅ (STEP-1) | axis=A, reviewer=van-den-dungen-bridge-theorist, no_workshop_context_attestation=true, clauses {a:PASS, b:N/A, c:PASS} |
| Reviewer-B JSON | `computations/session-106/s106_w4_viiad_reviewer_kitaev_axisB_verdict.json` | ✅ (STEP-1) | axis=B, reviewer=kitaev-quantum-chaos-theorist, no_workshop_context_attestation=true, clauses {a:N/A, b:PASS, c:PASS} |
| Verdict line | `computations/session-106/s106_gate_verdicts.txt` | ✅ | `grep -E '^S106-VIIAD-STAGE2-VERIFY:.* audit_sha256=[a-f0-9]{64}'` matches; dual-SHA companion row + 3 annotation rows present |
| WP section | this section | ✅ | Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit all present |

(Verification by content presence, never line/byte counts.)

**MCP Pre-Compute Audit**:
- `trace_entity('Delta_0 localization formula')` → 2 gates (`S88-DELTA-0-LOCALIZATION-FORMULA-LANDING` PASS, scheme `delta-0-localization-formula-V4-on-4-stratum-partition-EXACT-QQ`, convention `SOURCE-DOUBLE-CITE-CO-PRIMARY`; `S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION` FAIL with `delta_0_numerical=+2.400e+01`, `cc2_delta_0_match=False`) + the producing-script provenance — confirms §VII.AD is the registered STAGE-1-CANDIDATE this gate moves to Stage 2 (NOT pre-closed; the FAIL field is the substrate-CV-asymmetric numerical anchor kitaev reconciles, not a counterexample to the formula).
- `search_knowledge('VII.AD Delta_0 localization formula V_4 character stratum')` → theorem `§VII.AD` (STAGE-1-CANDIDATE, S88 W2-8, connes+volovik CO-AUTHORS+gen-physicist), the `V_4 stratum-coalescence cluster (S88)` mega-matrix row, and the structural equation `Δ_0 = 4·c_3 = 24` at substrate (2,4,8,6) — confirms the theorem statement and the substrate specialization the verify aggregates.
- `search_knowledge('joint theorem stage 2 cross-axis ... PASS-AND SOURCE-DOUBLE-CITE-CO-PRIMARY')` → the pathway precedent (`§VII.AH` FIRST cross-axis joint theorem to STAGE-3-PERMANENT via the 4-stage pathway; `S92-W5-CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY` PASS, `S91-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY` PASS) — structural siblings of this closeout's PASS-AND collapse. Not PRE-CLOSED: §VII.AD has no prior Stage-2 motion (the `S89-DELTA-0-LOCALIZATION-INDEPENDENT-VERIFY` queued in the entry was never executed — a stale placeholder this gate supersedes on PASS).

**Verdict**: **PASS** — composite PASS. value `JOINT-CROSS-AXIS-STAGE-2-PASS-AND;composite=PASS|partition[a:A=PASS/B=N/A/AND=PASS;b:A=N/A/B=PASS/AND=PASS;c:A=PASS/B=PASS/AND=PASS]|single_axis(a)=Axis-A-vdd-only|single_axis(b)=Axis-B-kitaev-only|JOINT(c)=CO-PRIMARY-chain-PASS-AND|substrate-input-orthogonality=SATISFIED-structural-CEILING-no-overlap-caveat|registry-file-SHA-drift=True-VII.AD-block-UNCHANGED-anchor-extracted`. `audit_sha256=ac0bfe8034220fd49925937f1fc8cd1217ccf37cd9bc8efd5ba7eab0a160635c`, `content_sha256=8e9eb5becbb220f7b7f18b5e334bf3bdcb0e1ad43ea7163c699d07b28f0d122c`.

**Results**:

*STEP-1 reviewer clause-verdict JSONs (aggregated only; no workshop transcript read).* Both blind reviewers carry `no_workshop_context_attestation=true`. Per-clause:
- **Axis-A (van-den-dungen-bridge-theorist)**, `inputs_read=[permanent-results-registry.md, canonical_constants.py]`: clause (a) [V_input NCG-axiomatic] = **PASS** (first-principles Sage-QQ verification: `[1−σ_1(i)][1−σ_2(i)] = 4·1_{σ_1(i)=σ_2(i)=-1}` is EXACT in QQ over all four (Z_2)^2 character value-pairs — `{(+,+):0,(+,-):0,(-,+):0,(-,-):4}` — and the collapse to single-stratum support requires the substrate labelling σ_1=[+1,-1,+1,-1], σ_2=[+1,+1,-1,-1] be a faithful V_4 bijection, confirmed, giving Δ_0=4·c_3=24 = direct alternating sum, full orbit 4·{2,4,8,6}={8,16,24,32}); clause (b) = **N/A** (not Axis-A's clause — did not read the npz cache or s88 verdict file); clause (c) [JOINT CO-PRIMARY V→A_F leg] = **PASS** (V_input→A_F is the NECESSARY structural premise; non-fungibility holds; both anchors on the SAME Corner-I algebra-INVARIANT cell).
- **Axis-B (kitaev-quantum-chaos-theorist)**, `inputs_read=[permanent-results-registry.md, s87_w11_hypercube_vertex_identity.npz, s88_gate_verdicts.txt]`: clause (a) = **N/A** (not Axis-B's clause); clause (b) [C_output Sage-QQ exhaustive] = **PASS** (576-config sweep all EXACT in QQ, distinct Δ_0={8,16,24,32}=4·{2,4,8,6}; npz `identity_result_per_d[d=2]='0'` Sage-exact + `per_d_pass` all True; S88 anchor `delta_0_numerical=24=4·c_4` self-consistent both by direct sum and by formula); clause (c) [JOINT CO-PRIMARY A_F→C_output leg] = **PASS** (C_output is the necessary exhaustive completion of the universal-quantifier claim; sequential, non-fungible; NOT PRIMARY+CONFIRMATION).

*Protocol pre-flight: PASS.* Reviewer identities == pinned (vdd Axis-A, kitaev Axis-B); `no_workshop_context_attestation==true` BOTH; neither reviewer ∈ {connes-ncg-theorist, volovik-superfluid-universe-theorist} (the §VII.AD Stage-0 CO-AUTHORS); clause-set exact match `{a,b,c}` on both JSONs.

*Substrate-input-orthogonality re-check: SATISFIED → structural CEILING, NO overlap caveat.* Scanning each `inputs_read`: `s87_w11_hypercube_vertex_identity.npz` (in_A=False, in_B=True) and `s88_gate_verdicts.txt` (in_A=False, in_B=True) each appear in EXACTLY ONE list (kitaev/Axis-B). The C_output certification cache + the S88 numerical anchor are loaded by ONE reviewer only — the PASS-AND is at the structural ceiling (structural-input independence, not merely structural-output-type independence), per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`.

*Per-clause PASS-AND matrix + composite* (npz `s106_w4_viiad_stage2_passand.npz`; png 3×3 grid):

| Clause | Axis-A (vdd) | Axis-B (kitaev) | PASS-AND | kind |
|:-------|:-------------|:----------------|:---------|:-----|
| (a) V_input NCG-axiomatic Schur | PASS | N/A | **PASS** | single-axis-A (vdd governs) |
| (b) C_output Sage-QQ 576-config | N/A | PASS | **PASS** | single-axis-B (kitaev governs) |
| (c) CO-PRIMARY chain identity | PASS | PASS | **PASS** | JOINT (PASS-AND) |

Composite = PASS (every aggregated clause PASS; monotone collapse FAIL>INFO>PASS reaches PASS only by the full all-PASS conjunction).

*4-tuple*: `(value=JOINT-CROSS-AXIS-STAGE-2-PASS-AND;…, scheme=joint-theorem-stage-2-cross-axis-verify, convention=vii-ad-delta-0-localization-stage-1-candidate-to-stage-3-promotion-cross-axis-PASS-AND, L_max=N/A)`.

*Substitution chain (CO-PRIMARY clause(c)=PASS-AND collapse)*: `composite = collapse[ clause(a)=axis_A(a), clause(b)=axis_B(b), clause(c)=PASS-AND(axis_A(c),axis_B(c)) ]`; `clause(c) PASS ⟺ axis_A(c)==PASS ∧ axis_B(c)==PASS` → PASS∧PASS = PASS; `composite PASS ⟺ clause(a)==PASS ∧ clause(b)==PASS ∧ clause(c)==PASS` → PASS∧PASS∧PASS = PASS. Direction: vdd (NCG side) and kitaev (combinatorial side) INDEPENDENTLY affirm the CO-PRIMARY chain's non-fungibility without shared workshop context ⇒ structurally independent agreement (sharpened by substrate-input orthogonality) ⇒ STAGE-3-PERMANENT eligible. The verdict was open (PASS/FAIL/INFO all reachable) and not pre-judged.

*Dual-SHA*: `audit_sha256 = sha256(script ‖ canonical_constants.py ‖ anchor-extracted §VII.AD `##`-block ‖ pinmap_json)` = `ac0bfe80…`; `content_sha256 = sha256(script)` = `8e9eb5be…`. The pinmap `_key` entries (reviewer assignment, clause map, orthogonality declaration) differ from §W4-1's ⇒ distinct `audit_sha256` by construction. The §VII.AD entry block was RE-extracted at runtime (7868 chars; `## §VII.AD` header → next `## §VII.` header at §VII.AE) and folded into `audit_sha256`.

*Registry file-level SHA drift (disclosed, NOT blocking)*: the plan pinned the registry file SHA at `a1797e1b…`; the runtime file SHA is `2d418892…` (DRIFT=True). §VII.CA/§VII.CB were landed THIS session and appended FAR BELOW §VII.AD; the §VII.AD block (registry lines 16836–16894) is UNCHANGED. Anchor-based extraction (`## §VII.AD` → next `## §VII.`) isolates exactly the unchanged block, so the entry-text fold into `audit_sha256` is stable across the file-level drift. The runtime file SHA is logged in the npz (`registry_file_sha256`, `registry_file_sha_drift=True`) and in a verdict annotation row.

*Reviewer findings documented (Methodology — see below). NOT registry-edited here.*

**Methodology — reviewer findings (4 items; aggregation-only, no re-derivation):**

(i) **vdd STRUCTURE-TAG observation (registry-text REFINEMENT candidate, NOT a Stage-2 blocker).** From a pure NCG-axiomatic standpoint, vdd notes the V_input factorization argument is ITSELF already a complete exact-QQ proof of the localization formula for arbitrary (c,σ) — each step is an exact finite-value-set identity — so an arguably-more-precise structure tag would be **PRIMARY (V structural proof) + INDEPENDENT-CROSS-CHECK (C exhaustive enumeration)** [parallel routes], rather than the registered strict **SOURCE-DOUBLE-CITE-CO-PRIMARY** [sequential]. This does NOT falsify clause (c): BOTH readings retain `V_input → A_F` as the NECESSARY structural premise, which is the only thing clause (c) certifies; vdd recorded it as INFO inside a PASS. Flagged here as a possible registry-text structure-tag refinement for the Wave-4 synthesis / orchestrator (per `registry-landing.md §"When PRIMARY+CONFIRMATION is wrong"` the discriminator is sequential-vs-parallel dependence) — a registry-text classification choice, NOT a clause verdict change, and NOT a §VII.AD down-tag.

(ii) **kitaev stronger-than-registry result.** kitaev's clause (b) PASS rests on a symbolic proof over GENERIC sympy QQ: he evaluated `lhs − rhs` over all 24 faithful V_4 bijections with a generic partition `(c0,c1,c2,c3)` — all 24 give `lhs−rhs = 0` EXACT, proving the localization for ALL rational partitions, not merely the registry's substrate-specific 576-instance sweep (which he also reproduced: 576/576 EXACT, Δ_0∈{8,16,24,32}). The C_output leg is therefore independently robust on his axis and, if anything, the registry's finite enumeration is SUBSUMED by the generic-QQ proof.

(iii) **kitaev reconciliation of the S88 anchor's FAIL/`cc2_delta_0_match=False` field.** The S88 substrate anchor verdict carries `delta_0_formula_QQ=8` and `cc2_delta_0_match=False` (verdict_kind FAIL). kitaev verified over all 256 (σ_1,σ_2) assignments that the formula's "unique (-1,-1) stratum" precondition holds IFF the assignment is a faithful V_4 bijection; the `formula=8=4·c_1` mismatch arises ONLY for NON-faithful labelings (multiple or zero strata satisfying (-1,-1)), which lie OUTSIDE the theorem's stated domain ("the UNIQUE stratum index where both σ_1=σ_2=-1"). The faithful substrate σ gives `delta_0_numerical=24=4·c_4` consistently both by direct alternating sum AND by the localization formula. The FAIL field is therefore NOT a counterexample to §VII.AD — it is the substrate-CV-asymmetry numerical-anchor result outside the formula's faithful-bijection domain.

(iv) **Legacy-path registry-text-hygiene note (routes to orchestrator/mack at session close).** The registered §VII.AD entry cites the Sage cache at the bare legacy path `computations/s87_w11_hypercube_vertex_identity.npz` (registry lines ~16859, 16875). The file is ACTUALLY on disk at `computations/session-87/s87_w11_hypercube_vertex_identity.npz` (it moved to the per-session directory after the entry was written). The Axis-B dispatch pointed at the ACTUAL on-disk path, and the closeout's substrate-input-orthogonality re-check matched on the file BASENAME (so the drift did not affect the predicate). This is a registry-text-hygiene observation only — a stale CITED-input path does not bear on the THEOREM's validity; the fix routes to the orchestrator/mack sole-writer at session close (a Constraint-Map process observation, NOT a CF, NOT a registry edit by this gate).

**Promotion disposition (NOTE for the orchestrator — orchestrator-direct at session close, NOT performed by this gate):** on this composite PASS, the §VII.AD theorem-name/Status line flips `STAGE-1-CANDIDATE` → `STAGE-3-PERMANENT` (registry line 16836 header + the `**Status**` line at ~16838), and the stale queued placeholder `S89-DELTA-0-LOCALIZATION-INDEPENDENT-VERIFY` (named in the entry's `**Status**` line and `**Anchor list**` "Independent verification (Stage 2 queued)" row, never executed) is superseded by this `S106-VIIAD-STAGE2-VERIFY` PASS. The Level-1 single-τ-slice Δ_0 localization formula (the `phononic-framing.md` calibration-corpus instance) joins the permanent-results table; `open-channel-ledger.md §C` K3 promotes out of the pending Stage-2 cohort. NOT a §7 falsifier row (NCG/GEOMETRIC structural landing; mack does not apply).

---

## Wave 4 Synthesis (team-lead)

*(Backfilled S107 session-close per the S107 plan obligation (vi)(d); faithful summary from the complete §W4-1/§W4-2 gate records above. No re-derivation.)*

Both register-sourced Stage-2 cross-axis verifies closed **PASS** (full all-PASS conjunction over their clause partitions); both qualify their §VII entries for STAGE-3-PERMANENT.

- **`S106-VIIBZ-STAGE2-VERIFY` (§VII.BZ K12, BDI Horizon-Faithfulness) → PASS.** Axis-A (vdd, connes-axis Type-II trace + Tomita-Takesaki) × Axis-B (landau, volovik-axis BDI-CdGM); JOINT clause (c) — the `+1/2` identification (bosonic Wightman floor = fermionic CdGM minigap = the single BDI datum fixing trace AND faithfulness, EMERGENCE-1) — PASS in BOTH blind verdicts.
- **`S106-VIIAD-STAGE2-VERIFY` (§VII.AD K3, Δ_0 LOCALIZATION FORMULA) → PASS.** Axis-A (vdd, NCG-axiomatic V_input Schur) × Axis-B (kitaev, Sage-QQ C_output); JOINT SOURCE-DOUBLE-CITE-CO-PRIMARY chain-identity PASS in BOTH. kitaev's clause (b) is *stronger* than the registry (generic-QQ proof over all 24 faithful V_4 bijections, subsuming the 576-instance sweep); the S88 anchor's `cc2_delta_0_match=False` is reconciled as a non-faithful-labeling result OUTSIDE the theorem's faithful-bijection domain, NOT a counterexample.

**Substrate-input-orthogonality**: BOTH gates SATISFIED at the structural CEILING (a slot-data file loaded by exactly one reviewer each) → structural-INPUT independence, **no overlap caveat** tagged. **Promotions** (orchestrator-direct at S106 close, per each gate's `writer_agent` note): §VII.BZ + §VII.AD STAGE-1-CANDIDATE → STAGE-3-PERMANENT; `open-channel-ledger.md §C` K12 + K3 promoted out of the pending cohort. Both are NCG/structural landings (mack N/A — no §7 falsifier row). The stale queued placeholders (`S89-DELTA-0-LOCALIZATION-INDEPENDENT-VERIFY`, the §VII.BZ unpinned "future cross-axis verify") are superseded by these PASSes.

## Carry-Forward Computations

No carry-forwards: both gates closed PASS in-session. The forward Stage-2 cohort `{K2, K7, K8, K9, K11}` stayed in `open-channel-ledger.md §C` (NOT lifted here) and was picked up by **S107 Wave 2** (K2/K7/K9/K11 verified — all INFO; K8 §VII.AF.1.STATE-PROJ remained HELD-PENDING-VERIFICATION, precondition unmet).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-13 | §VII.BZ (K12) BDI Horizon-Faithfulness | STAGE-1-CANDIDATE | STAGE-3-PERMANENT | blind Stage-2 PASS-AND (audit `566cdcb5…`); +1/2 EMERGENCE-1 confirmed by both axes |
| 2026-06-13 | §VII.AD (K3) Δ_0 localization formula | STAGE-1-CANDIDATE | STAGE-3-PERMANENT | blind Stage-2 PASS-AND (audit `ac0bfe80…`); CO-PRIMARY chain non-fungibility independently affirmed; localization proved over GENERIC QQ |
| 2026-06-13 | §VII.AD cited-input path (registry-text hygiene) | bare legacy `computations/s87_w11_…npz` | (process obs) routed orchestrator/mack | file moved to `computations/session-87/`; stale CITED path, does not bear on theorem validity |

## Files Produced

| Gate | Script | Data / Plot | Reviewer JSONs |
|:--|:--|:--|:--|
| §W4-1 §VII.BZ | s106_w4_viibz_stage2_passand_closeout.py | s106_w4_viibz_stage2_passand.{npz,png} | reviewer_vdd_axisA, reviewer_landau_axisB |
| §W4-2 §VII.AD | s106_w4_viiad_stage2_passand_closeout.py | s106_w4_viiad_stage2_passand.{npz,png} | reviewer_vdd_axisA, reviewer_kitaev_axisB |

All under `computations/session-106/`; verdict lines in `computations/session-106/s106_gate_verdicts.txt`.
