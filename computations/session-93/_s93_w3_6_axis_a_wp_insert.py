import io, sys

WP = "sessions/archive/session-93/session-93-w3-workingpaper.md"
ANCHOR = "#### Axis-A (van-den-dungen) cross-review"

with io.open(WP, "r", encoding="utf-8") as f:
    text = f.read()

if ANCHOR in text:
    print("ANCHOR ALREADY PRESENT -- no double-write")
    sys.exit(0)

hdr = "### §W3-6. S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT"
hpos = text.find(hdr)
assert hpos != -1, "W3-6 header not found"
sep = text.find("\n---\n", hpos)
assert sep != -1, "section separator after W3-6 not found"

block = r"""
#### Axis-A (van-den-dungen) cross-review

**Reviewer**: `van-den-dungen-bridge-theorist` (Axis-A, NCG-submersion / spectral-functional). **Stage-2 independence**: audited ONLY the registered Stage-1 entries (`VII.AV.OP-PROJ` + `VII.AV.STATE-PROJ` in `sessions/permanent-results-registry.md`) + cited inputs; W-3 / S91 / S92 VII.AV **workshop transcript NOT read** (first-principles on my axis). **OAA exclusion satisfied**: vdd not in {connes-ncg, phonon-first, volovik}, not a W-3 author, no downstream-inheritance reach. **Substrate-input-orthogonality (MANDATORY K=3)**: I loaded ONLY `computations/session-91/s91_w5_1_full_bdg_pv.npz` (key `L_emp_canonical`); I did **NOT** load the OP-PROJ residue cache `s92_w3_9...npz` (Axis-B orthogonal input) -> structural ceiling, NO overlap caveat. Data file `computations/session-93/s93_w3_6_axis_a_vdd_verdicts.json`.

**MCP Pre-Compute Audit (Axis-A)**:
- `search_knowledge("VII.AV OP-PROJ STATE-PROJ slot split Cell I Cell IV algebra-axis orthogonal")` -> returns confirm split; surfaced canonical `VII.U.2` partition (Cell I = INVARIANT x s=3; Cell II = INVARIANT x s=4) + `W15 Cross-Corner Co-Primary Wall`.
- `search_knowledge("L_emp K-window log-derivative -7.046336 BdG OPERATIONAL-ALIGNMENT substrate-natural")` -> `S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE: PASS value='L_emp=-7.046336;...'` (independent pre-workshop S89 confirmation of the STATE-PROJ anchor).
- `get_constant("Delta_BCS")` -> `0.4642547394830737` (R-PROTECTED) -- matches STATE-PROJ Level-1 `|Delta_a|` IR scale.
- `get_constant("tau_fold")` -> `0.19` -- matches single-tau-slice tag on both sub-slots.
- `trace_entity("Cell I substrate-distance-2 pole s=4 OP-PROJ INVARIANT")` -> **No trace** (no precedent for Cell I at s=4; both prior OP-PROJ precedents VII.AF.1 + VII.AU are Cell I x s=3).

**Axis-A independent re-derivation** (orthogonal substrate input only): I reconstructed `d^2 ln P_GGE / d(ln K)^2` at `K_horizon` from the STATE-PROJ npz via a 5-point centered finite difference and a global quadratic fit. The 5-pt FD reproduces `L_emp = -7.046336` (bare GGE) and `-527.966919` (FULL-PV) **to displayed precision**, matching the stored `L_emp_canonical = -7.046336474406761` and `L_emp_PV_L12 = -527.966919`. Global-quadratic fit gives `-7.040661` (rel-diff `8.05e-4`; expected local-vs-global curvature offset). L_max-saturation: `R_KW_PV` flat across L_max in {6..12}, spread `5.6e-9`. `P_GGE_bare` in [5.2e-3, 8.0e-3] (gap-IR-finite). Level-2-B separation: `|L_PV/L_canonical| = 74.93`, `anchor_consistency=False`.

**Per-sub-slot per-clause verdicts (Axis-A):**

| Sub-slot | Clause | Axis-A verdict | Basis |
|:---|:---|:---|:---|
| **STATE-PROJ** (Cell IV) | substrate-IS observable identity | **PASS** | `L_emp = -7.046336` reproduced at machine precision (5-pt FD) from orthogonal npz |
| STATE-PROJ | parse-tree -> DEPENDENT (Cell IV) | **PASS** | `Var_a`/`d(ln.)/d(ln K)` terminus over gapped occupation -> state-pair functional |
| STATE-PROJ | Level-1 regulator-invariant + gap-IR-saturated + L_max-saturated | **PASS** | `R_KW_PV` flat (spread 5.6e-9); IR scale = canonical `Delta_BCS=0.4642547`; corpus 22 |
| STATE-PROJ | Level-3 anchor singleness | **PASS** | `-527.97` is Level-2-B DIAGNOSTIC (ratio 74.93, `anchor_consistency=False`), not co-primary |
| STATE-PROJ | corner-cell = Cell IV (DEPENDENT x s=4) | **PASS** | EXACTLY the canonical VII.U.2 Corner-IV instance (`alpha_s_route_3 = -7.046336`) |
| STATE-PROJ | **JOINT** structural-orthogonal-companion / cross-corner FORBIDDEN | **PASS** (spectral-functional leg) | Cell IV (DEPENDENT) orthogonal to OP-PROJ INVARIANT family; within-Cell-IV diagnostic correctly distinguished from cross-corner split |
| STATE-PROJ | **JOINT** bridge map HKR substrate-natural-binding | **PASS** (spectral-functional leg) | CM-1995 III.4 on `M_2(C) subset A_K`; `L_emp` is substrate's own value (no canonical-import); Level-2-binding PROXY-REFINEMENT correctly scoped |
| **OP-PROJ** (claimed Cell I) | substrate-IS observable identity | **PASS** | `Tr_{A_K}(P_a |D_K|^{-2s})` at s=4, INVARIANT spectrum-only -- well-formed (~375 NOT re-derived: residue cache is Axis-B orthogonal input) |
| OP-PROJ | parse-tree -> INVARIANT | **PASS** | `Tr`-terminus, no `pi(a)`/`[D,pi(a)]`/state-pair sup -> algebra-INVARIANT |
| OP-PROJ | Level-1 single-tau-slice tag | **PASS** | tau_fold=0.19 tag correct; Level-1 STRUCTURAL-THEOREM status correctly gated on W3-3 Class-8.7 witness |
| OP-PROJ | **corner-cell = "Cell I x s=4"** | **FAIL** | MIS-TAG: VII.U.2 fixes Cell I = INVARIANT x **s=3**; INVARIANT x **s=4** = **Cell II**. Both OP-PROJ precedents (VII.AF.1, VII.AU) are Cell I x s=3; no redefinition makes Cell I = s=4. Algebra-axis (INVARIANT) + pole (s=4) sub-claims correct; only the I-vs-II cell terminus is wrong. |
| OP-PROJ | **JOINT** structural-orthogonal-companion / cross-corner FORBIDDEN | **PASS-conditional** (orthogonality substance) | INVARIANT orthogonal to DEPENDENT is the load-bearing fact and holds regardless of I-vs-II; but the JOINT clause cell-pair label "Cell I vs Cell IV" inherits the OP-PROJ mis-tag (correct pair = "Cell II vs Cell IV"). PASS-AND must be conditioned on the Cell I->Cell II remediation. |
| OP-PROJ | **JOINT** bridge map HKR substrate-self-consistent | **PASS** (spectral-functional leg) | HKR `L_max->inf` at d=4 pole s=4 + CM-1995 III.4 on `A_K`, type (i) -- correct map class for an INVARIANT residue |

**Axis-A sub-slot summaries:**
- **VII.AV.STATE-PROJ -> PASS** (Axis-A). All single-axis clauses PASS + both JOINT clauses PASS on the spectral-functional leg. The Level-3 anchor `L_emp` is reproduced at machine precision from the substrate own BdG sub-algebra (substrate-natural-binding confirmed). Axis-A-ready for STAGE-3-PERMANENT eligibility pending Axis-B PASS-AND.
- **VII.AV.OP-PROJ -> FAIL** (Axis-A). The substrate-physics identity, parse-tree INVARIANT classification, Level-1 tag, and bridge map all PASS -- but the **corner-cell classification is mis-tagged** (claims "Cell I x s=4"; per the cited VII.U.2 partition an algebra-INVARIANT functional at s=4 is **Cell II**). Per `joint-theorem-promotion.md` Stage 2, a per-clause Axis-A FAIL blocks OP-PROJ Stage-2->3 promotion; the sub-slot stays STAGE-1-CANDIDATE. **Remediation** is a 1-token registry edit (`Cell I` -> `Cell II` at registry lines ~18451/18459/18460/18465/18467/18475 + the cell-pair label in the orthogonal-companion declaration and the parent-host bullet); the substrate-IS theorem content is otherwise sound. This is a registry-classification defect, NOT a substrate-physics falsification.

**Substrate framing (Axis-A)**: GEOMETRIC. The substrate IS the finite spectral triple `(A_K, H_K, D_K)` at tau_fold = 0.19; the two sub-slots are its algebra-axis-orthogonal observables -- STATE-PROJ the Cell-IV state-pair K-window log-derivative on the BdG sub-algebra `M_2(C) subset A_K`, OP-PROJ the algebra-INVARIANT spectrum-only `Tr`-residue. The cross-corner orthogonality (INVARIANT orthogonal to DEPENDENT) is the load-bearing structural fact and survives the OP-PROJ I-vs-II mislabel; the bridge maps faithfully image each substrate-IS observable to its laboratory-IN counterpart. Direction-of-explanation preserved (substrate -> bridge -> laboratory).

**NOTE**: This is the Axis-A verdict ONLY. The PASS-AND aggregation across both axes + the W3-6 verdict-line emission is the separate Axis-B (mack) step. vdd does NOT emit the W3-6 verdict line and did NOT read Axis-B verdict.
"""

new_text = text[:sep] + "\n" + block.rstrip() + "\n" + text[sep:]
with io.open(WP, "w", encoding="utf-8", newline="\n") as f:
    f.write(new_text)
print("INSERTED Axis-A subsection at offset", sep, "; new length", len(new_text), "(was", len(text), ")")
